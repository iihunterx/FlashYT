##FlashYT
---

## Telegram YouTube Downloader Bot

This is a Telegram bot written in Python using the Telebot library, capable of downloading YouTube videos and converting them to MP3 files upon receiving the video link from the user.

### Setup

1. Install the required libraries:

```bash
pip install pytube telebot
```

2. Replace `'TOKEN_HERE'` with your actual Telegram bot token.
3. Replace `Your_id_here` with your Telegram id
4. Run the script.

### Usage

1. Start the bot by sending the `/start` command.
2. Send a YouTube video link to the bot.
3. The bot will download the video and send back the MP3 audio file.

### Commands

- `/start`: Initializes the bot and provides instructions to the user.
- `/users`: Returns the number of users who have interacted with the bot (accessible only to the bot owner).

### File Structure

- `main.py`: Main script containing the bot logic.
- `users.json`: JSON file to store user data.

### Dependencies

- [Telebot](https://github.com/eternnoir/pyTelegramBotAPI): Telegram Bot API wrapper.
- [pytube](https://github.com/pytube/pytube): Library to download YouTube videos.

### Contributing

Feel free to contribute to this project by submitting pull requests or opening issues.

### License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
