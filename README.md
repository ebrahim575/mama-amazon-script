# Website Viewer Bot for Mac

This bot automatically visits websites you specify, waits for a bit, then visits them again.

## Setup Steps

1. **Get the Code**
   - Open Terminal (press `Command + Space`, type "Terminal", press Enter)
   - Type these commands to get the code:
   ```bash
   cd Desktop
   git clone https://github.com/ebrahim575/mama-amazon-script.git
   cd mama-amazon-script
   ```

2. **Install Homebrew**
   - In Terminal, paste this command:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```

3. **Install Python**
   - In Terminal, paste these commands:
   ```bash
   brew update
   brew install python
   ```

4. **Set Up Project**
   - In Terminal, paste these commands:
   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   pip3 install -r requirements.txt
   ```

5. **Change Settings** (Optional)
   To change how the bot works:
   - Type this in Terminal to open the settings file:
   ```bash
   open -e main.py
   ```
   - You can change these numbers:
     ```python
     VIEW_TIME_SECONDS = 5  # Change 5 to how many seconds to stay on each page
     WAIT_TIME_SECONDS = 10  # Change 10 to how many seconds to wait between visits
     ```
   - You can add more websites:
     ```python
     URLS = [
         "https://www.amazon.com/dp/B0DDKWZS9P",
         "https://www.amazon.com/dp/ANOTHER_PRODUCT",  # Add more URLs here
     ]
     ```
   - Save the file (Command + S)

6. **Run the Bot**
   - In Terminal, type:
   ```bash
   python3 main.py
   ```
   - You'll see messages showing the bot is working
   - To stop the bot: Press `Control + C`

## Need Help?
- Make sure you copy/paste commands exactly as shown
- If something doesn't work, try closing Terminal and starting over
- Contact me if you're stuck!
