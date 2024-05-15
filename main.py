import telebot
from pytube import YouTube
import os
import time
import json

TOKEN = 'TOKEN_HERE'
bot = telebot.TeleBot(TOKEN)

users_file = 'users.json'
if not os.path.exists(users_file):
    with open(users_file, 'w') as f:
        json.dump({}, f)

@bot.message_handler(commands=['start'])
def welcome(message):
    user_id = message.from_user.id
    user_first_name = message.from_user.first_name

    with open(users_file, 'r') as f:
        users = json.load(f)

    if str(user_id) not in users:
        users[str(user_id)] = {'first_name': user_first_name}
        
        with open(users_file, 'w') as f:
            json.dump(users, f)
            
        bot.reply_to(message, f'Hello {user_first_name}! Send me a YouTube video link and I will convert it to an MP3 file.')
    else:
        bot.reply_to(message, f'Hello {user_first_name}! Send me a YouTube video link and I will convert it to an MP3 file.')

@bot.message_handler(regexp=r"^(https?://)?(www\.)?(youtu\.be/|youtube\.com/watch\?v=)")
def handle_youtube_link(message):
    try:
        loading_message = bot.send_message(message.chat.id, "Downloading...")

        start_time = time.time()

        yt = YouTube(message.text)

        audio = yt.streams.filter(only_audio=True).first()

        audio.download()

        bot.send_audio(message.chat.id, open(audio.default_filename, 'rb'))

        os.remove(audio.default_filename)

        bot.delete_message(message.chat.id, loading_message.message_id)

        elapsed_time = round(time.time() - start_time)
        bot.reply_to(message, f'The clip has been downloaded successfully! Download time: {elapsed_time} seconds.')

    except Exception as e:
        bot.reply_to(message, f'An error occurred: {e}')

@bot.message_handler(commands=['users'])
def send_users_count(message):
    if message.from_user.id == Your_id_here:  
        with open(users_file, 'r') as f:
            users = json.load(f)

        bot.reply_to(message, f'Number of users: {len(users)}')

bot.polling()
