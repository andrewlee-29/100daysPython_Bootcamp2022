# Day 35 : Rain Alert application

# **Overview**

---

- Building a rain alert application that can text to the user and remind the user to bring the umbrella.
- There are multiple ways to remind the user : text message, email, etc... I prefer discord. (Since I frequently use it)

![Untitled](screenshot.png)

# **Features**

---

- Using the open weather API to get the weather data.
- Call the discord bot and text message to the channel

# Learnt Concept

---

- API Authentication
- Environment Variables:
    
    Two method:
    
    - Basic:
        - Every Time export the environment variable on the bash script
        - then, using the os.environ to get the environment variable
    
    ```bash
    export API_KEY= dbjkdsfbnabnbjenbkjenbw 
    ```
    
    ```python
    api_key = os.environ.get("API_KEY")
    ```
    
    - dot env:
        - install python-dotenv
        - create the .env file to the directory  and put all the environment variable to the file
        - import dotenv, and run load_dotenv , and use getenv to get the environment variable
        - use .gitignore to avoid upload the .env file.

# Issue and Solution

---

# Usage/**Installation**

---

1. Make sure your computer install python 3
2. Download the folders
3.  In the folder directory, activate the virtual environment:

**Mac OS / Linux**

```bash
source venv/bin/activate

```

**Windows**

```bash
venv\Scripts\activate
```

4. create the .env file in the directory and enter your api key:
    
    ```bash
    API_KEY = your open weather api key
    DISCORD_TOKEN= your discord token
    ```
    
5. After you've done that you should be able to run the `main.py` program.