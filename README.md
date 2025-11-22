# Telegram AI Chat Bot with Inline Mode

A powerful Telegram bot that uses OpenRouter API to provide AI responses in both direct messages and inline mode.

## Features

- 🤖 **Direct Messaging**: Chat directly with the bot
- 💬 **Inline Mode**: Use the bot in any chat by typing `@YourBotUsername question`
- 🔄 **Multiple AI Models**: Support for GPT-4, Claude, Llama, and more
- ⚡ **Fast Responses**: Quick AI-powered answers
- 🎯 **Easy to Use**: Simple and intuitive interface

## Setup Instructions

### 1. Get Telegram Credentials

1. Go to https://my.telegram.org/auth
2. Log in with your phone number
3. Click on "API development tools"
4. Create a new application to get your `API_ID` and `API_HASH`

### 2. Create a Telegram Bot

1. Open Telegram and search for [@BotFather](https://t.me/BotFather)
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the bot token (format: `123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ`)
5. **Enable Inline Mode**:
   - Send `/setinline` to BotFather
   - Select your bot
   - Provide a placeholder text (e.g., "Ask me anything...")
6. **Optional - Set inline feedback**:
   - Send `/setinlinefeedback` to BotFather
   - Select your bot
   - Choose "Enable"

### 3. Get OpenRouter API Key

1. Go to https://openrouter.ai/
2. Sign up or log in
3. Go to Settings → Keys
4. Create a new API key
5. Copy the key (format: `sk-or-v1-...`)

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

### 5. Configure Environment Variables

1. Copy `.env.example` to `.env`:
```bash
cp .env.example .env
```

2. Edit `.env` and add your credentials:
```env
TELEGRAM_API_ID=12345678
TELEGRAM_API_HASH=abcdef1234567890abcdef1234567890
TELEGRAM_BOT_TOKEN=123456789:ABCdefGhIJKlmNoPQRsTUVwxyZ
OPENROUTER_API_KEY=sk-or-v1-...
```

3. Update the bot username in `telegram_bot.py` (line 30):
```python
"HTTP-Referer": "https://t.me/YourActualBotUsername",
```

### 6. Run the Bot

```bash
python telegram_bot.py
```

## Usage

### Direct Messaging

1. Open your bot in Telegram
2. Send `/start` to begin
3. Send any message to get an AI response

### Inline Mode

1. Open any Telegram chat
2. Type `@YourBotUsername` followed by your question
3. Example: `@YourBotUsername What is machine learning?`
4. Select the result to send

### Using Different Models

In inline mode, specify a model:
```
@YourBotUsername [model:gpt-3.5-turbo] your question
```

Available models:
- `openai/gpt-4o` (default)
- `openai/gpt-3.5-turbo`
- `anthropic/claude-3-sonnet`
- `meta-llama/llama-3-70b-instruct`

## Commands

- `/start` - Start the bot
- `/help` - Show help message
- `/models` - List available AI models

## Project Structure

```
.
├── telegram_bot.py      # Main bot code
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variables template
├── .env               # Your actual credentials (create this)
└── README.md          # This file
```

## Troubleshooting

### Bot not responding in inline mode
- Make sure you enabled inline mode via BotFather (`/setinline`)
- Check that your bot token is correct
- Verify the OpenRouter API key is valid

### "Unauthorized" error
- Double-check your `API_ID`, `API_HASH`, and `BOT_TOKEN`
- Make sure there are no extra spaces in the `.env` file

### OpenRouter API errors
- Verify your API key is active
- Check your OpenRouter account has credits
- Ensure the model name is correct

## Security Notes

⚠️ **Important**: 
- Never commit your `.env` file to version control
- Keep your API keys secure
- The `.env` file is already in `.gitignore`

## License

MIT License - Feel free to use and modify!

## Support

If you encounter issues:
1. Check the error messages in the console
2. Verify all credentials are correct
3. Ensure inline mode is enabled in BotFather
4. Check OpenRouter API status

## Credits

- Built with [Pyrogram](https://docs.pyrogram.org/)
- AI powered by [OpenRouter](https://openrouter.ai/)
- Subro [Telegram](https://t.me/subroz)
