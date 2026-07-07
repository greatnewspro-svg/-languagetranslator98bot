# @languagetranslator98bot

A simple Telegram bot that translates any message you send it. Built with
`python-telegram-bot` and `deep-translator` (free, no paid API key needed).

## Features
- Translates any text sent to it
- `/setlang <code>` lets each user pick their target language (default: English)
- `/help` lists common language codes

## 1. Get your bot token
1. Open Telegram, search **@BotFather**
2. Send `/newbot` (or `/mybots` if @languagetranslator98bot already exists)
3. Copy the token it gives you — looks like `123456789:AAExampleTokenHere`

## 2. Push this project to GitHub
```bash
cd translator-bot
git init
git add .
git commit -m "Initial commit: translator bot"
git branch -M main
git remote add origin https://github.com/<your-username>/<your-repo>.git
git push -u origin main
```

## 3. Deploy on Railway
1. Go to https://railway.app and log in (GitHub login is easiest)
2. Click **New Project → Deploy from GitHub repo**
3. Select the repo you just pushed
4. Once it's created, go to your service → **Variables** tab
5. Add a variable:
   - `BOT_TOKEN` = the token from BotFather
6. Railway will auto-detect Python and use the `Procfile` to run `python bot.py`
7. Deploy — check the **Deployments → Logs** tab; you should see `Bot starting...`

## 4. Test it
Open Telegram, message `@languagetranslator98bot`, send any text — it replies translated.

## Notes
- Railway's free tier has monthly usage limits; check current limits on your dashboard.
- `deep-translator` uses Google Translate's public web endpoint — it's free but unofficial,
  so very high volume use could get rate-limited. Fine for personal projects/small bots.
- Never commit your bot token to GitHub. Keep it only in Railway's Variables tab (and
  optionally a local `.env` file that's in `.gitignore`).
