from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
import openai

# Configurações do GPT e Telegram
TELEGRAM_TOKEN = "7705840618:AAGPSoen0lgf_41ITf6ygm9hgEHDMcJj9Lc"
OPENAI_API_KEY = "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"

openai.api_key = OPENAI_API_KEY

# Função para responder mensagens
async def responder(update: Update, context: ContextTypes.DEFAULT_TYPE):
    pergunta = update.message.text
    try:
        resposta = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um assistente que responde perguntas sobre o regulamento interno do Condomínio Terra Gutierrez. Responda de forma clara e direta, citando os artigos ou capítulos relevantes do regulamento quando necessário."},
                {"role": "user", "content": pergunta}
            ]
        )
        texto_resposta = resposta['choices'][0]['message']['content']
        await update.message.reply_text(texto_resposta)
    except Exception as e:
        await update.message.reply_text("Desculpe, algo deu errado ao processar sua pergunta.")

# Função para iniciar o bot
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Olá! Sou o Assistente Terra Gutierrez. Pergunte sobre o regulamento interno do condomínio!")

# Configuração do Bot
def main():
    app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, responder))
    app.run_polling()

if __name__ == '__main__':
    main()
