import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart
from aiogram.types import Message
from openai import AsyncOpenAI


TELEGRAM_TOKEN = "Your_token"
GROQ_API_KEY = "Your_key"


bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher()


llm_client = AsyncOpenAI(
    api_key=GROQ_API_KEY,
    base_url="https://api.groq.com/openai/v1"
)


SYSTEM_PROMPT = """
You are a helpful and friendly English grammar tutor. 
Analyze the user's text. 
If there are mistakes, provide the corrected version and briefly explain the grammar rules violated. 
If the text is grammatically perfect, confirm it and encourage the user.
Keep explanations concise.
"""


@dp.message(CommandStart())
async def command_start_handler(message: Message):
    await message.answer("Hi! Send me any sentence in English, and I'll check your grammar. 🇬🇧")


@dp.message()
async def check_grammar(message: Message):
    # Показуємо статус "друкує...", поки ШІ генерує відповідь
    await bot.send_chat_action(chat_id=message.chat.id, action="typing")

    try:
        # Відправляємо запит до мовної моделі
        response = await llm_client.chat.completions.create(
            model="openai/gpt-oss-20b",  # Швидка та безкоштовна модель
            messages=[
                {"role": "system", "content": SYSTEM_PROMPT},
                {"role": "user", "content": message.text}
            ],
            temperature=0.3  # Низька температура для більш точних і менш фантазійних відповідей
        )

        reply_text = response.choices[0].message.content
        await message.answer(reply_text)

    except Exception as e:
        logging.error(f"Error during API call: {e}")
        await message.answer("Oops, something went wrong with the AI module. Please try again.")


async def main():
    logging.basicConfig(level=logging.INFO)
    print("Bot is running...")
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())