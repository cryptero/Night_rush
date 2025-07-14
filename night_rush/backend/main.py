from flask import Flask, request
import telegram
import os

TOKEN = '8158342090:AAEeMV9W8c267_Aa0n7ikGFIbCapZg-dzbk'  # 👈 твой токен
bot = telegram.Bot(token=TOKEN)

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    data = request.get_json()

    if 'message' in data:
        chat_id = data['message']['chat']['id']
        text = data['message'].get('text', '')

        if text == '/start':
            bot.send_message(chat_id=chat_id, text='Привет! Я готов к гонке 🏁')
        else:
            bot.send_message(chat_id=chat_id, text='Команда не распознана ❓')

    return 'ok'

if __name__ == '__main__':
    app.run(debug=True)