# Discord Study Bot

A Discord bot written in Python that helps you run timed study sessions. Start a session with a length and what you're studying, and the bot will ping you when your time is up.

## Features

- Start timed study sessions with flexible lengths like `25m`, `1h` or `1h30m`
- Supports seconds, minutes, hours, days and weeks
- Sessions can be up to one year long
- Pings you when your session is complete
- Friendly guidance for missing or invalid input
- Logs bot activity to `discordbot.log`

## Commands

| Command | Description | Example |
|---|---|---|
| `!hello` | The bot says hello back to you | `!hello` |
| `!reminder <time> <topic>` | Starts a study session and pings you when it ends | `!reminder 30m maths revision` |

### Time format

Combine a number with one of these units:

| Unit | Meaning |
|---|---|
| `s` | seconds |
| `m` | minutes |
| `h` | hours |
| `d` | days |
| `w` | weeks |

Units can be combined, for example `1h30m`. The session topic can be up to 200 characters.

### Example

```
!reminder 25m chemistry flashcards
```

The bot confirms the session has started, then after 25 minutes pings you to say the session is complete.

## Setup

### 1. Requirements

- Python 3.8 or newer
- A Discord bot application from the [Discord Developer Portal](https://discord.com/developers/applications)

### 2. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/YOUR-REPO-NAME.git
cd YOUR-REPO-NAME
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Create a `.env` file

In the project folder, create a file called `.env` and add your bot token:

```
DISCORD_TOKEN=your-bot-token-here
```

**Never share this token or commit it to GitHub.** The included `.gitignore` keeps `.env` out of your repository.

### 5. Enable intents

In the Discord Developer Portal, open your application, go to **Bot**, and turn on:

- **Message Content Intent** (needed to read `!` commands)
- **Server Members Intent**

### 6. Invite the bot to your server

In the Developer Portal, go to **OAuth2 → URL Generator**, select the `bot` scope, and give it the **Send Messages** and **Read Message History** permissions. Open the generated link to add the bot to your server.

### 7. Run the bot

```bash
python bot.py
```

When it starts, you'll see `BEEP BOOP <bot name> IS ONLINE` in the terminal.

## Project structure

```
├── bot.py             # Main bot code and commands
├── requirements.txt   # Python dependencies
├── .env               # Your bot token (not uploaded to GitHub)
└── .gitignore
```

## Known limitations

- Active sessions are held in memory, so any running session is lost if the bot restarts or goes offline.
- Session messages are sent in the channel where the session was started.

## Possible future improvements

- Save sessions so they survive restarts
- Track total study time per user
- Add leader board to see who has studied the longest amount of time
- Commands to list or cancel active sessions

## Built with

- [Python](https://www.python.org/)
- [discord.py](https://discordpy.readthedocs.io/)
- [python-dotenv](https://pypi.org/project/python-dotenv/)
