# 🔐 Pass_Gen: My First Secure Password Generator!

Welcome to my password generator! I built this interactive command-line tool in Python to make it easy to create customized, highly secure passwords right from your terminal. 

Instead of standard random generation, I wanted to build something genuinely safe, so I designed this using cryptographic security. Plus, I gave it a styled retro-hacker UI because standard terminal text is boring!

## 🚀 Why I Built This (And Why It’s Great)
* **Actually Secure:** Most beginner generators use Python's `random` module, which is predictable. I built this using the `secrets` module, making it cryptographically secure against hackers.
* **Old-School Hacker UI:** I integrated `pyfiglet` and `termcolor` to print a custom ASCII art banner in bright green when you launch it.
* **Crash-Proof:** I added input handling, so if you accidentally type text instead of a password length, the program gently asks you to try again instead of crashing.
* **Fully Tailored:** You choose the exact length and toggle uppercase, lowercase, numbers, and symbols on or off based on what your account needs.

## 🛠️ Getting Started

Because this project uses a couple of external libraries for the stylized UI, you'll just need to quickly install them first. 

Open your terminal and run this command:
```bash
pip install pyfiglet termcolor
```

## 💻 How to Run It

1. Download or clone this repository to your machine.
2. Open your terminal in the project folder and run:
   ```bash
   python main.py
   ```
3. Enter your desired password length, type `y` or `n` for your character preferences, and grab your new password!

---
*Feel free to star this repository if you like it, or leave some feedback if you have ideas on how I can make it even better!*

NOTE: this README has been written by AI but the code i wrote it my self.
