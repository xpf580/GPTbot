## How to use
cd chat\myapp\openai——key.py 输入你的openai的Apikey

cd go-cqhttp\config.yml 输入你的qq账号，不输入密码

打开三个终端，

1.打开Django 到 OpenAI 接口
cd .\chat\ 
python manage.py runserver

2.打开机器人。检测到@bot会发送给Django
cd .\noneBot\  
python bot.py 

3.登录qq并通信(在device.json选择protocal的参数切换设备)
cd .\go-cqhttp\
.\go-cqhttp_windows_amd64.exe

如有延迟，请在终端中检查runserver是否返回信息！