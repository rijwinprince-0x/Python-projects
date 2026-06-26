# 🔐 Password Manager & Generator
A desktop password manager and generator built with Python and Tkinter. Generate strong, randomized passwords, store your website credentials locally, and look them up again instantly — all from a simple, lightweight GUI.
## Features
- 🎲 **Random Password Generation** — creates passwords using a mix of uppercase and lowercase letters, numbers, and symbols
- 📋 **Instant Clipboard Copy** — every generated password is automatically copied to your clipboard, ready to paste
- 💪 **Live Password Strength Indicator** — each generated password is rated **Weak**, **Medium**, or **Strong** based on its length and character variety, shown right below the password field
- 💾 **Local Credential Storage** — save website, email/username, and password entries to a local JSON file for quick reference
- 🔍 **Search by Website** — look up a saved entry by website name and instantly view its email/username and password in a popup, no need to scroll through a file
- 🖥️ **Runs Entirely on Your Device** — no internet connection, accounts, or external servers required; everything stays on your machine
- ✅ **Confirmation Before Saving** — a popup review step prevents accidental or incomplete entries
- 🎨 **Simple, Clean Interface** — minimal Tkinter UI with no clutter
## Password Strength Logic
| Strength | Criteria |
|----------|----------|
| 🟢 Strong | 12+ characters and at least 3 character types (upper, lower, number, symbol) |
| 🟠 Medium | 8+ characters and at least 2 character types |
| 🔴 Weak | Anything below the above thresholds |
## Tech Used
`Python` `Tkinter` `pyperclip` `json`
## How It Works
1. Enter the **website** and **email/username**
2. Click **Generate Password** to create a strong random password — it's instantly copied to your clipboard, and its strength is shown right below as **Weak**, **Medium**, or **Strong**
3. Click **Add** to save the entry locally
4. Confirm the details in the popup, and you're done
5. To retrieve a saved entry later, type the **website** name and click **Search** — the email and password will pop up if a match is found
## Installation
```bash
git clone https://github.com/rijwinprince-0x/Python-projects.git
cd Python-projects/Password-Manager-Generator
pip install pyperclip
python main.py
```
## Requirements
- Python 3.x
- `pyperclip` library
- A `logo.png` file in the project directory (used for the app logo)
## Notes
- All data is stored **locally on your device** in plain text — nothing is sent anywhere. For sensitive real-world use, consider adding encryption before storing credentials long-term.
- This project was built as part of my Python learning journey, focused on GUI development, event-driven programming, and file handling.
## Author
**Rijwin Prince** — [@rijwinprince-0x](https://github.com/rijwinprince-0x)
