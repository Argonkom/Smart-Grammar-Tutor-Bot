Smart-Grammar-Tutor-Bot
<img width="1024" height="618" alt="image" src="https://github.com/user-attachments/assets/7cb990e3-907b-4a7c-b1c1-739f87909fa4" />

An asynchronous Telegram bot designed to help users improve their English grammar.
The bot leverages an LLM API to analyze user input in real-time, correct grammatical mistakes, and provide clear, structured explanations for the rules violated.

Features
Real-time Corrections: Instantly fixes grammatical, spelling, and punctuation errors.
Educational Feedback: Breaks down the specific grammar rules behind the corrections, acting as an interactive tutor.
Fast & Asynchronous: Built with aiogram and integrates an LLM API for rapid, non-blocking responses.

Stack
Language: Python
Framework: aiogram (Async Telegram API)
AI Integration: LLM API (Groq / OpenAI compatible)

How to Run Locally
1. Clone this repository.
2. Install the required dependencies:
   pip install -r requirements.txt
3. Open bot.py and replace the placeholder tokens with your actual TELEGRAM_TOKEN and GROQ_API_KEY.
