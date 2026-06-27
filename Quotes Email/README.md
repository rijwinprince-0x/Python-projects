# Quote Email Bot

A Python script that automatically emails you a random motivational quote on a day of the week you choose, using Gmail's SMTP server.

## How it works

1. Checks the current day of the week using `datetime`.
2. Compares it to `TARGET_DAY` in `main.py` (defaults to Monday — change this to whichever day you want).
3. If it matches, picks a random line from `quotes.txt`.
4. Logs into Gmail via SMTP and sends the quote to your own inbox.

Run it once a day (e.g. via Task Scheduler / cron / GitHub Actions) and it only sends mail on your chosen day.

## Setup

### 1. Clone and navigate to this folder
```bash
git clone https://github.com/rijwinprince-0x/Python-projects.git
cd "Python-projects/Quotes Email"
```

### 2. Quotes are already included
`quotes.txt` is preloaded in this folder with quotes ready to use. Add, remove, or edit lines to customize the pool the script picks from.

### 3. Generate a Gmail App Password
Gmail blocks regular password logins for SMTP. You need an **App Password** instead:

1. Go to your [Google Account → Security → App Passwords](https://myaccount.google.com/apppasswords).
2. Make sure 2-Step Verification is turned on (required for App Passwords).
3. Type a name for the app (e.g. `Python Mail`) and click **Create**.
4. Copy the 16-character password shown — you only see it once.

### 4. Set your credentials as environment variables
Don't hardcode your email or password in the script. Set them as environment variables instead:

**macOS / Linux:**
```bash
export MY_EMAIL="your_email@gmail.com"
export MY_PASSWORD="your16charapppassword"
```

**Windows (PowerShell):**
```powershell
$env:MY_EMAIL="your_email@gmail.com"
$env:MY_PASSWORD="your16charapppassword"
```

### 5. Choose your day (optional)
By default the script sends on Monday (`TARGET_DAY = 0`). Open `main.py` and change `TARGET_DAY` to whichever day you want:

| Day | Value |
|-----|-------|
| Monday | 0 |
| Tuesday | 1 |
| Wednesday | 2 |
| Thursday | 3 |
| Friday | 4 |
| Saturday | 5 |
| Sunday | 6 |

### 6. Run it
```bash
python main.py
```

If today matches `TARGET_DAY`, you'll get an email titled **"Monday Motivation"** with a random quote. (Feel free to change the subject line in `main.py` too if you pick a different day.)

## Tech stack
- Python 3
- `smtplib` — sending email over SMTP
- `datetime` — checking the day of the week
- `random` — picking a quote
- `os` — reading credentials from environment variables

## Notes
- The email only sends when today matches `TARGET_DAY` in `main.py`. Schedule the script to run daily so it actually triggers on your chosen day.
- Never commit your real email or App Password to GitHub. Use environment variables as shown above.
- If Gmail blocks the login, double check 2-Step Verification is on and you're using the App Password, not your normal Gmail password.

## License
Free to use and modify.
