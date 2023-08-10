GPTBOT

## 使用方法 ##

首先，在终端中执行以下命令安装所需依赖：`pip install -r re.txt`

进入 `.\chat\myapp` 目录，在 `openai_key.py` 文件中输入你的 OpenAI API 密钥。

进入 `.\go-cqhttp` 目录，在 `config.yml` 文件中输入你的 QQ 账号。无需输入密码。

## 以下启动方法二选一： ##

选项一：**推荐：在终端中输入 `.\start_servers.bat` 或直接运行该脚本，将一次性打开三个终端。**

选项二：打开三个终端，按照以下步骤执行：

1. 打开 Django 到 OpenAI 接口：
   ```
   cd .\chat\ 
   python manage.py runserver
   ```

2. 打开 Nonebot 机器人。包含 `@bot` 的消息将发送给 Django。（已取消正则匹配，可以直接提问）
   ```
   cd .\noneBot\  
   python bot.py
   ```

3. 登录 QQ 并通信（在 `device.json` 中选择 `protocal` 参数切换设备）：
   ```
   cd .\go-cqhttp\
   .\go-cqhttp_windows_amd64.exe
   ```

如果遇到延迟，请在终端中检查 `runserver` 命令是否返回信息！