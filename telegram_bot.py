import os
import requests
import json
from pyrogram import Client, filters
from pyrogram.types import (
    InlineQuery,
    InlineQueryResultArticle,
    InputTextMessageContent,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)

# Configuration
API_ID = os.getenv("TELEGRAM_API_ID")
API_HASH = os.getenv("TELEGRAM_API_HASH")
BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")

# Initialize the bot
app = Client(
    "my_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN
)

def get_ai_response(user_message, model="openai/gpt-4o"):
    """Get response from OpenRouter API"""
    try:
        response = requests.post(
            url="https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {OPENROUTER_API_KEY}",
                "HTTP-Referer": "https://t.me/YourBotUsername",  # Update with your bot username
                "X-Title": "Telegram AI Bot",
            },
            data=json.dumps({
                "model": model,
                "messages": [
                    {
                        "role": "user",
                        "content": user_message
                    }
                ]
            })
        )
        
        if response.status_code == 200:
            data = response.json()
            return data['choices'][0]['message']['content']
        else:
            return f"Error: {response.status_code} - {response.text}"
    
    except Exception as e:
        return f"An error occurred: {str(e)}"


@app.on_message(filters.command("start"))
async def start_command(client, message):
    """Handle /start command"""
    welcome_text = """
🤖 **Welcome to AI Chat Bot!**

You can use me in two ways:

1️⃣ **Direct Chat**: Just send me a message here
2️⃣ **Inline Mode**: Type `@YourBotUsername your question` in any chat

Try inline mode by typing:
`@YourBotUsername What is AI?`
    """
    await message.reply_text(welcome_text)


@app.on_message(filters.command("help"))
async def help_command(client, message):
    """Handle /help command"""
    help_text = """
📖 **How to use this bot:**

**Direct Messages:**
Simply send any message and I'll respond using AI.

**Inline Mode:**
1. Type `@YourBotUsername` in any chat
2. Add your question after the bot username
3. Select the result to send

**Example:**
`@YourBotUsername Explain quantum computing`

**Commands:**
/start - Start the bot
/help - Show this help message
/models - List available AI models
    """
    await message.reply_text(help_text)


@app.on_message(filters.command("models"))
async def models_command(client, message):
    """Show available models"""
    models_text = """
🤖 **Available AI Models:**

1. `openai/gpt-4o` - GPT-4 Optimized (default)
2. `openai/gpt-3.5-turbo` - Faster, cheaper option
3. `anthropic/claude-3-sonnet` - Claude Sonnet
4. `meta-llama/llama-3-70b-instruct` - Llama 3

To use a specific model in inline mode:
`@YourBotUsername [model:gpt-3.5-turbo] your question`
    """
    await message.reply_text(models_text)


@app.on_message(filters.text & filters.private & ~filters.command([]))
async def handle_message(client, message):
    """Handle direct messages"""
    user_text = message.text
    
    # Send "typing" action
    await message.chat.action("typing")
    
    # Get AI response
    ai_response = get_ai_response(user_text)
    
    # Send response
    await message.reply_text(ai_response)


@app.on_inline_query()
async def handle_inline_query(client, inline_query: InlineQuery):
    """Handle inline queries"""
    query_text = inline_query.query.strip()
    
    if not query_text:
        # Show placeholder when query is empty
        await inline_query.answer(
            results=[
                InlineQueryResultArticle(
                    id="1",
                    title="💡 Ask me anything!",
                    description="Type your question here...",
                    input_message_content=InputTextMessageContent(
                        "Please type a question after the bot username!"
                    )
                )
            ],
            cache_time=1
        )
        return
    
    # Check if user specified a model
    model = "openai/gpt-4o"
    if query_text.startswith("[model:"):
        try:
            end_bracket = query_text.index("]")
            model = query_text[7:end_bracket]
            query_text = query_text[end_bracket+1:].strip()
        except ValueError:
            pass
    
    # Get AI response
    ai_response = get_ai_response(query_text, model)
    
    # Create inline result
    results = [
        InlineQueryResultArticle(
            id="1",
            title="🤖 AI Response",
            description=ai_response[:100] + "..." if len(ai_response) > 100 else ai_response,
            input_message_content=InputTextMessageContent(
                f"**Question:** {query_text}\n\n**Answer:**\n{ai_response}"
            ),
            reply_markup=InlineKeyboardMarkup([
                [InlineKeyboardButton("🔄 Ask Another", switch_inline_query_current_chat="")]
            ])
        )
    ]
    
    await inline_query.answer(
        results=results,
        cache_time=1
    )


if __name__ == "__main__":
    print("🤖 Bot is starting...")
    print("✅ Direct messaging enabled")
    print("✅ Inline mode enabled")
    app.run()
