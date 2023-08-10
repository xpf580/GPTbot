<!-- title: GPTBot -->

## How to Use ##

To begin, open a terminal and install the required dependencies using the command: `pip install -r re.txt`

Navigate to the `.\chat\myapp` directory and input your OpenAI API Key into the `openai_key.py` file.

Navigate to the `.\go-cqhttp` directory and input your QQ account into the `config.yml` file. No password is needed.

## Choose one of the following startup methods: ##

Option One: **Recommended: Enter `.\start_servers.bat` in the terminal or directly run the script to open three terminals at once.**

Option Two: Open three terminals and execute the following steps:

1. Open Django to the OpenAI interface:
   ```
   cd .\chat\ 
   python manage.py runserver
   ```

2. Open the Nonebot robot. Messages containing `@bot` will be sent to Django. (Regex matching has been removed, you can directly ask questions)
   ```
   cd .\noneBot\  
   python bot.py
   ```

3. Log in to QQ and communicate (Select the `protocal` parameter in `device.json` to switch devices):
   ```
   cd .\go-cqhttp\
   .\go-cqhttp_windows_amd64.exe
   ```

If you experience delays, check the terminal to ensure that the `runserver` command is returning information!