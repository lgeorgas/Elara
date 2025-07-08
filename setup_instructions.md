
# 🛠️ Elara Project Setup Instructions

This guide will help you set up the Elara Discord bot on your local machine. It includes setting up a virtual environment, installing dependencies, and preparing the project for development or testing.

---

## 🔧 1. Prerequisites

Ensure you have the following installed:

- [Python 3.10+](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- FFmpeg installed and added to your system PATH
  - [Windows Download](https://www.gyan.dev/ffmpeg/builds/)
  - On macOS: `brew install ffmpeg`
  - On Ubuntu: `sudo apt install ffmpeg`

---

## 📁 2. Clone the Project (if using Git)

```bash
git clone <your-repo-url>
cd Elara
```

If you're working locally without GitHub, just ensure you're inside the `Elara/` project folder.

---

## 🧪 3. Create and Activate a Virtual Environment

### Windows (PowerShell):

```bash
python -m venv .venv
.venv\Scripts\Activate
```

### macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

---

## 📦 4. Install Dependencies

### Install required packages via pip:

```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, use the following manually:

```bash
pip install discord.py openai elevenlabs python-dotenv webrtcvad ffmpeg-python
```

> Note: If using the `discord-ext-voice-recv` extension, make sure it’s installed as well:
```bash
pip install git+https://github.com/Rapptz/discord-ext-voice-recv.git
```

---

## 🔑 5. Environment Configuration

Create a `.env` file in the root of your project:

```
DISCORD_TOKEN=your_discord_bot_token_here
OPENAI_API_KEY=your_openai_key_here
ELEVEN_API_KEY=your_elevenlabs_key_here
```

---

## ▶️ 6. Running Elara

With your virtual environment activated:

```bash
python main.py
```

Elara should now start, connect to Discord, and be ready to respond to your voice commands.

---

## 🧹 7. Optional Development Tools

- **VS Code Recommended Extensions:**
  - Python
  - Pylance
  - GitLens
  - dotenv

- **Recommended Git Workflow:**
  ```bash
  git add .
  git commit -m "feat: add memory command"
  git tag v0.3-memory
  ```

---

## 🧠 Notes

- FFmpeg **must** be in your system PATH for audio playback and conversion to work.
- Make sure your bot token has the correct permissions (voice, messages, etc).
- Elara currently uses synchronous TTS/STT/LLM calls — these can be optimized later for performance.

---

For House Nytheris. 🦉
