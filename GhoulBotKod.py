import telebot
import random

# вставь сюда токен, полученный от BotFather
TOKEN = "8180178854:AAFNyqvmDIgLCMXlQyohVjeQvW48vmKqHpM"
bot = telebot.TeleBot(TOKEN)

# список фраз для команды "!съел"
eat_phrases = [
    "{author} съел {target} 🩸",
    "{author} перегрыз {target} 👹",
    "{author} поглотил {target} ☠️",
    "{author} уничтожил {target} ⚡",
    "{author} сожрал {target} 🕷️"
]

# список фраз для "!кагуне"
kagune_phrases = [
    "{author} раскрыл кагуне 🩸",
    "{author} активировал кагуне 👁️",
    "{author} выпустил кагуне ⚡",
    "{author} пробудил кагуне 👹",
    "{author} вызвал кагуне ☠️"
]

# список фраз для "!реген"
regen_phrases = [
    "{author} восстановил {target} 💉",
    "{author} регенерировал {target} 🌿",
    "{author} исцелил {target} ✨",
    "{author} оживил {target} 🔮",
    "{author} вернул силы {target} 💪"
]

# команда "!съел"
@bot.message_handler(func=lambda m: m.text and m.text.startswith("!съел"))
def eat_command(message):
    parts = message.text.split(maxsplit=1)
    target = parts[1] if len(parts) > 1 else "кого-то неизвестного"
    author = message.from_user.first_name
    phrase = random.choice(eat_phrases).format(author=author, target=target)
    bot.reply_to(message, phrase)

# команда "!кагуне"
@bot.message_handler(func=lambda m: m.text and m.text.startswith("!кагуне"))
def kagune_command(message):
    author = message.from_user.first_name
    phrase = random.choice(kagune_phrases).format(author=author)
    bot.reply_to(message, phrase)

# команда "!реген"
@bot.message_handler(func=lambda m: m.text and m.text.startswith("!реген"))
def regen_command(message):
    parts = message.text.split(maxsplit=1)
    target = parts[1] if len(parts) > 1 else "себя"
    author = message.from_user.first_name
    phrase = random.choice(regen_phrases).format(author=author, target=target)
    bot.reply_to(message, phrase)

print("✅ Бот запущен и ждёт команды...")
bot.polling()
