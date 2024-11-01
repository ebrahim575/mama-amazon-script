# Mac Setup Guide

## Step 1: Install Homebrew
1. Open Terminal (use Spotlight search with `⌘ + Space` and type "Terminal")
2. Install Homebrew by pasting this command:
```bash
/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
```
3. Follow any additional instructions in Terminal


## Step 2: Install Python using Homebrew
```bash
# Update Homebrew
brew update

# Install Python
brew install python

# Verify Python installation
python3 --version
```
You should see something like `Python 3.x.x`

## Step 3: Download the Code
1. Download this project (either clone with git or download as ZIP)
2. If downloaded as ZIP, extract it
3. Open Terminal
4. Navigate to the project folder:
```bash
# Example:
cd ~/Downloads/project-name
```

## Step 4: Set Up the Project
Run these commands in order:
```bash
# Create virtual environment
python3 -m venv .venv

# Activate virtual environment
source .venv/bin/activate

# Install requirements
pip3 install -r requirements.txt
```

## Step 5: Run the Program
```bash
python3 main.py
```

## Common Issues & Solutions

### Homebrew Issues
- If you see "Permission denied" during Homebrew installation:
  ```bash
  sudo chown -R $(whoami) /usr/local/share/zsh /usr/local/share/zsh/site-functions
  ```
- If Homebrew commands aren't found, add to PATH:
  ```bash
  echo 'eval "$(/opt/homebrew/bin/brew shellenv)"' >> ~/.zshrc
  source ~/.zshrc
  ```

### Python Issues
- Use `python3` instead of `python`
- If pip isn't found, try:
  ```bash
  python3 -m pip install --upgrade pip
  ```

### Permission Denied
If you see "Permission denied" errors:
```bash
chmod +x setup.sh
./setup.sh
```

### Need Help?
If you run into any issues:
1. Make sure you're in the correct folder in Terminal
   - Use `pwd` to check your current location
   - Use `ls` to list files in the current folder
2. Make sure both Homebrew and Python are installed correctly
3. Try closing and reopening Terminal
4. Contact the project maintainer

To exit the program: Press `Control + C` in Terminal

### Why Homebrew?
While Python can be installed directly from python.org, using Homebrew provides several advantages:
- Easier to manage and update
- Better integration with macOS
- Simpler package management
- Avoids potential permission issues
- Industry standard for Mac development
