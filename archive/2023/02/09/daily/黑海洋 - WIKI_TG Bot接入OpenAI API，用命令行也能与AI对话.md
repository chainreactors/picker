---
title: TG Bot接入OpenAI API，用命令行也能与AI对话
url: https://blog.upx8.com/3210
source: 黑海洋 - WIKI
date: 2023-02-09
fetch_date: 2025-10-04T06:07:46.900840
---

# TG Bot接入OpenAI API，用命令行也能与AI对话

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# TG Bot接入OpenAI API，用命令行也能与AI对话

发布时间:
2023-02-08

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
18782

# 前言

我所遇到的问题相信大家也都遇到了，有时候与chatGPT对话时经常出现1小时内请求过多的情况，心情不好就不跟你聊了。

# 于是

我为了测试text模型到底怎么样，有没有大家说的那么神奇，我与GPT的交互陷入了一个死循环。原因是我想让它帮我写用tg bot接入OpenAI，然后用和bot交互，你猜怎么着，GPT模型不支持API调用，目前只能用post请求，这就把GPT给难坏了，4小时这代码也没写明白，一个劲儿说我请求次数太多！最后我给它一个60分吧，感觉嗷，用AI取代程序员还有待时日。

本文内容一共分为两个部分，第一部分是在一台linux服务器，直接用python命令行的方式与最新的模型 Davinci-003交互；第二部分是与已经接入API的telegram bot交互，实现的方法也很简单，主要命令和代码如下：

# 第一部分

首先我们需要在服务器上安装pip和openai库：

```
apt update
apt install pip vim -y
pip install openai
```

然后，需要申请OpenAI的api，在这里申请：[https://platform.openai.com/account/api-keys](https://blog.upx8.com/go/aHR0cHM6Ly9wbGF0Zm9ybS5vcGVuYWkuY29tL2FjY291bnQvYXBpLWtleXM)
绑卡后两个月送$18，随便造；参考费用是750个单词算1000tokens，费用$0.02。为了测试不超标，我把消费限制在每月最多$1。设置限额的方法就是在 [https://platform.openai.com/account/billing/limits](https://blog.upx8.com/go/aHR0cHM6Ly9wbGF0Zm9ybS5vcGVuYWkuY29tL2FjY291bnQvYmlsbGluZy9saW1pdHM) 看条件设置吧！

然后，就是在vps上创建 main.py,内容如下：

```
import openai

openai.api_key = "这里是你申请到的API-key"

def chat_with_gpt3(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=104,
        n=1,
        stop=None,
        temperature=0.5,
    )
    message = response.choices[0].text
    return message

def main():
    while True:
        message = input("You: ")
        response_message = chat_with_gpt3(message)
        print(f"Bot: {response_message}")

if __name__ == "__main__":
    main()
```

最后执行 python3 chat.py，即可实现交互问答：
![截屏2023-02-02 21.54.27.png](https://iweec.com/usr/uploads/2023/02/3196401153.png "截屏2023-02-02 21.54.27.png")

# 第二部分

首先还是要申请OpenAI的apikey，方法上面说了；
然后这个vps也必须是海外的嗷，因为我们要用bot；

```
apt update
apt install pip vim -y
pip install openai aiogram
```

下一步就是新建main.py，内容如下：

```
import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

token = '这里是你的bot token'
openai.api_key = '这里是你的api-key'

bot = Bot(token)
dp = Dispatcher(bot)

@dp.message_handler()
async def send(message : types.Message):
    response = openai.Completion.create(
    model="text-davinci-003",
    prompt=message.text,
    temperature=0.9,
    max_tokens=1000,
    top_p=1.0,
    frequency_penalty=0.0,
    presence_penalty=0.6,
    stop=["You:"]
)
    await message.answer(response['choices'][0]['text'])

executor.start_polling(dp, skip_updates=True)
```

最后，就是执行 python3 main.py，提示：Updates were skipped successfully.就可以到你的bot当中，跟他聊一下！

![截屏2023-02-02 20.58.06.png](https://iweec.com/usr/uploads/2023/02/2371290845.png "截屏2023-02-02 20.58.06.png")

# 小结

切记：不要暴露API和token！！

我在上面用例当中引用的text-davinci-003模型，虽然快，但是有点傻：

[取消回复](https://blog.upx8.com/3210#respond-post-3210)

### 在下方留下您的评论.[加入TG群](https://t.me/).[打赏🍗](/reward.html)

提交评论

* [Post](/author/1)
* [Link](/links.html)
* [工具](https://tools.upx8.com/)
* [关于](/about.html)
* [文库](/WooyunDrops)

[![](/usr/uploads/ypyun.png)](https://www.upyun.com/?utm_source=lianmeng&utm_medium=referral "赞助商")
Copyright © 2024 黑海洋. All rights reserved.
[看雪赞助](https://www.kanxue.com/ "看雪学院赞助")

[浙ICP备2021040518号](http://beian.miit.gov.cn "浙ICP备2021040518号") [Sitemap](sitemap.xml?type=index "Sitemap")