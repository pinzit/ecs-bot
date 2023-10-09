```
 /$$$$$$$$  /$$$$$$   /$$$$$$                    /$$$$$$$   /$$$$$$  /$$$$$$$$
| $$_____/ /$$__  $$ /$$__  $$                  | $$__  $$ /$$__  $$|__  $$__/
| $$      | $$  \__/| $$  \__/                  | $$  \ $$| $$  \ $$   | $$
| $$$$$   | $$      |  $$$$$$                   | $$$$$$$ | $$  | $$   | $$
| $$__/   | $$       \____  $$                  | $$__  $$| $$  | $$   | $$
| $$      | $$    $$ /$$  \ $$                  | $$  \ $$| $$  | $$   | $$
| $$$$$$$$|  $$$$$$/|  $$$$$$/                  | $$$$$$$/|  $$$$$$/   | $$
|________/ \______/  \______/                   |_______/  \______/    |__/
```
<b>This program is designed to continuously join and leave an ECS:R game of your choice every 10 minutes, which gives you 60 tix.</b>
There shouldn't be bugs, but if you find one feel free to report it or fix it yourself and make a pull request.

# Requirements
- A brain
- Pip
- https://docs.python.org/library/time.html
- https://docs.python.org/library/webbrowser.html
- https://pypi.org/project/requests/
- https://docs.python.org/library/os.html
- https://docs.python.org/library/re.html
- https://pypi.org/project/python-dotenv/
- ECS:R Client (Works on Virtual Machines too)

# Setup
1. Download or clone this repository.
2. Duplicate (or just rename) <code>.env.example</code> and rename it to <code>.env</code>
3. Get the place id of your choice (using one of your own games gives you an extra ticket), and get your <code>.ROBLOSECURITY</code> (ECS, not Roblox).
4. When you run the script, you shouldn't use the Python application, rather VS Code, Command Prompt, etc. This way it will show the errors instead of just closing.

I'm not the best at python, so sorry if the code is messy.
