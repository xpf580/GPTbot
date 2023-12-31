
import json
from nonebot import on_command, on_message
from nonebot.rule import to_me
from nonebot.adapters import Message
from nonebot.adapters import Event
import requests
import re

pattern = re.compile(r"^\s*(.*)$")  # 匹配以  开头的字符串，并获取后面的内容

chatgpt = on_command("", rule=to_me(), aliases={
                     "gpt", "chatgpt"}, priority=10, block=True)


@chatgpt.handle()
async def handle_function(event: Event):
    message = event.get_plaintext()
    
    if message:
        match = pattern.match(message.strip())
        if not match:
            # 如果匹配失败则结束命令处理
            await chatgpt.finish("命令格式错误，请输入 AI + 需要查询的内容")
            return
        query = match.group(1)  # 获取正则匹配结果中第一个括号中的内容
        text = requestApi(query)
        print(text)
        await chatgpt.finish(text)
    else:
        await chatgpt.finish("请输入内容")


def requestApi(msg):
    msg_body = {
        "msg": msg
    }
    msg_2gpt = 'http://127.0.0.1:8000/chat-api/?msg=' + msg #请以以下性格回答但是不要主动说出你的名字和性格，'+'你的名字是黑川茜，LALALAI剧团年轻头牌，努力天才演员，高挑貌美，蓝眼少女，不喜欢加奈。）
    response = requests.get(msg_2gpt)
    result = json.loads(response.text)
    text = result['text']['message']['content']
    return text
