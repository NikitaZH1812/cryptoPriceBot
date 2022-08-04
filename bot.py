import telebot
from btc import get_price, get_all_sumbols

bot = telebot.TeleBot("5437152024:AAGgFEVx_yWvwYnly6FmfZgvpbYcCVFnLiw")


@bot.message_handler(commands=["start"])
def start(message):
    bot.send_message(message.chat.id,
                     "If you want get a price,enter \
                        crypto pair in format like BTCUSDT or BTC")


@bot.message_handler()
def get_user_text(message):
    subols_list = get_all_sumbols()
    ms = message.text
    crypto_pair_with_usdt = ms.upper() + "USDT"
    if ms.upper() in subols_list:
        bot.send_message(message.chat.id, get_price(f"{ms.upper()}"))
    elif crypto_pair_with_usdt in subols_list:
        bot.send_message(message.chat.id,
                         get_price(f"{crypto_pair_with_usdt}"))
    else:
        bot.send_message(message.chat.id,
                         "sorry, we have no information about this crypto")


bot.polling(non_stop=True)
