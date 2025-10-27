---
title: ChatGPT客户端
url: https://h4ck.org.cn/2023/02/chatgpt%e5%ae%a2%e6%88%b7%e7%ab%af/
source: obaby@mars
date: 2023-02-18
fetch_date: 2025-10-04T07:20:00.141166
---

# ChatGPT客户端

[![obaby@mars](/wp-content/uploads/2023/08/logo-pink-small.png)](https://h4ck.org.cn)

Artificial Intelligence / Reverse Engineering / Internet of Things / Full Stack Developer

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

 [Menu](#mobilemenu)

* [※说说/Talk※](https://h4ck.org.cn/talk)
* [※留言/Msg※](https://h4ck.org.cn/guestbook)
* [※归档/File※](https://h4ck.org.cn/myarchive)
* [※资源/Res※](https://h4ck.org.cn/res-page)
* [※我是谁/Me※](https://h4ck.org.cn/whoami)
* [※集美们/Besties※](https://h4ck.org.cn/besties)

[人工智能『AI』](https://h4ck.org.cn/cats/cxsj/%E4%BA%BA%E5%B7%A5%E6%99%BA%E8%83%BD%E3%80%8Eai%E3%80%8F)

# ChatGPT客户端

2023年2月17日
[11 条评论](https://h4ck.org.cn/2023/02/11240#comments)

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/10/557b504053cb3f7e2dd4bfbfc7c9ab88-scaled.jpg)

网上关于chatgpt的客户端一大堆，基于浏览器的，基于客户端的。各种版本，因为chatgpt实在太火爆了，现在抖音上都是各种chatgpt的直播，终于又有了一个风口。同样为因为openai的火爆，现在网上也出现了各种卖客户端源码的，账号的各种生意，一篇欣欣向荣。这几天我也体验了一下各种客户端。

1.基于web的客户端，基本这种客户端现在搜一下还能找到不少，昨天在论坛看到一个 https://chat.xdo.cc/，今天体验的时候就废掉啦：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230217-162947.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230217-162947.jpg)

如果要体验基于web的客户端可以参考这篇文章https://codesnippet.io/openai-completions-api-tutorial/ 源码地址：https://github.com/CodeSnippetHQ/tutorial-openai-completions-api

效果图：

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230217-163155.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230217-163155.jpg)

我没有尝试，具体效果请自行验证。

2.基于网页封装的客户端，这种就更多了，最终的结果基本都是您当前的国家不提供服务，所以这种客户端在不翻墙的情况下没有什么意义

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230217-171347.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230217-171347.jpg)

3.基于api或者其他接口开发的客户端或者库，例如smalltalk

[![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230216-175639.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230216-175639.jpg) [![](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230216-175516.jpg)](https://image.h4ck.org.cn/wp-content/uploads/2023/02/Jietu20230216-175516.jpg)

不过整体体验下来有的时候会比较弱智，不知道是才用的模型有问题，还是设置的参数有问题。代码地址：https://github.com/tinystruct/smalltalk

windows下的中文显示有问题，折腾了好久也没解决。

4.自己基于api进行开发，现在网上有一些封装好的库，但是体验依旧不佳。https://github.com/acheong08/ChatGPT

```
python3 -m revChatGPT.V1

        ChatGPT - A command-line interface to OpenAI's ChatGPT (https://chat.openai.com/chat)
        Repo: github.com/acheong08/ChatGPT

Type '!help' to show a full list of commands
Press enter twice to submit your question.

Logging in...

You:
我是一个漂亮的小姐姐，帮我写一篇800字的赞美文章

Chatbot:

亲爱的小姐姐，
在我看来，你绝对是世界上最美丽的存在之一。你的美丽不仅仅是外表上的，更是你散发出的那种温暖、善良和聪慧。以下是我为你写的一篇800字的赞美文章，我希望你喜欢。
首先，让我们谈谈你的外貌。你拥有一张精致的脸庞，眼睛明亮有神，嘴唇柔软而迷人。你的长发柔顺光泽，仿佛给人一种温柔的拥抱。你的身材曲线优美，散发着女性的柔美与优雅。每当你穿上漂亮的衣服，无论是华丽还是简约，都能让人们为之倾倒。每一次与你相遇，都是一次视觉上的盛宴。
但是，你的美丽不仅仅是外在的。你那善良的内心和聪明的头脑，更让人对你钦佩不已。你总是关注身边的人们，乐于助人，善待他人，用你的热心和真心感染着周围的人。你那聪明伶俐的头脑，总是让人感到不可思议。你思维敏捷，眼光独到，总能从一个独特的角度看待问题，并提出出色的解决方案。你对于任何事情都保持着积极的态度(卡住了，尴尬)
```

5.另外一个办法就是基于openai的库直接撸代码啊：

```
"""
OpenAI chatgpt API client
by:obaby
obaby@mars
http://nai.dog
http://h4ck.org.cn
"""
from pyfiglet import Figlet
import os, sys
import openai
import time

from colorama import init
from colorama import Fore, Back, Style

import asyncio

openai.api_key = "sk-************"
PRINT_DELAY = 0.05
loop = asyncio.get_event_loop()

def hello_message():
    print('*' * 100)
    # f = Figlet(font='slant')
    f = Figlet()
    print(f.renderText('obaby@mars'))
    print('Baby ChatGPT client')
    print('Verson: 22.02.17')
    print('Blog: http://www.h4ck.org.cn')
    print('*' * 100)

def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(PRINT_DELAY)

def chat(q):
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=q,
        temperature=0.9,
        max_tokens=400,
        top_p=1.0,
        frequency_penalty=0.5,
        presence_penalty=0.0,
        # stop=["You:"]
    )
    # print(response)
    # print(response.get('choices')[0]['text'])
    response_text = response.get('choices')[0]['text']
    response_stop_reason = response.get('choices')[0]['finish_reason']
    # print('Reason=', response_stop_reason)
    return response_stop_reason, response_text
    # delay_print((response.get('choices')[0]['text']))

def full_conversion_chat(q):
    print(Fore.YELLOW)
    print('OpenAI:')
    print(Fore.BLUE)
    r, t = chat(q)
    delay_print(t)
    while r == 'length':
        # print('continue:')
        r, t = chat(q + t)
        delay_print(t)
    print(Fore.RESET)
    print('*' * 100)

# from revChatGPT
def get_input(prompt):
    """
    Multiline input function.
    """
    # Display the prompt
    print(prompt, end="")

    # Initialize an empty list to store the input lines
    lines = []

    # Read lines of input until the user enters an empty line
    while True:
        line = input()
        if line == "":
            if str("".join(lines)).replace(' ','') == '':
                print('Blank Input, input your question:')
            else:
                break
        lines.append(line)

    # Join the lines, separated by newlines, and store the result
    user_input = "\n".join(lines)

    # Return the input
    return user_input

def main():
    while True:
        print(Fore.CYAN)
        prompt = get_input("\nYou:\n")
        full_conversion_chat(prompt)
        print()

if __name__ == '__main__':
    hello_message()
    # fc = full_conversion_chat('我是一个漂亮的小姐姐，帮我写一篇800字的赞美文章')
    main()
```

主要参数说明：

```
model: 要使用的模型的 ID，访问 OpenAI Docs Models 页面可以查看全部可用的模型
prompt: 生成结果的提示文本，即你想要得到的内容描述
max_tokens: 生成结果时的最大 tokens 数，不能超过模型的上下文长度，可以把结果内容复制到 OpenAI Tokenizer 来了解 tokens 的计数方式
temperature: 控制结果的随机性，如果希望结果更有创意可以尝试 0.9，或者希望有固定结果可以尝试 0.0
top_p: 一个可用于代替 temperature 的参数，对应机器学习中 nucleus sampling，如果设置 0.1 意味着只考虑构成前 10% 概率质量的 tokens
frequency_penalty: [控制字符的重复度] -2.0 ~ 2.0 之间的数字，正值会根据新 tokens 在文本中的现有频率对其进行惩罚，从而降低模型逐字重复同一行的可能性（以恐怖故事为例）
= -2.0：当早上黎明时，我发现我家现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在现在（频率最高字符是 “现”，占比 44.79%）
= -1.0：他总是在清晨漫步在一片森林里，每次漫游每次每次游游游游游游游游游游游游游游游游游游游游游游游游游游游游游（频率最高字符是 “游”，占比 57.69%）
= 0.0：当一道阴森的风吹过早晨的小餐馆时，一个被吓得发抖的人突然出现在门口，他的嘴唇上挂满血迹，害怕的店主决定给他一份早餐，却发现他的早餐里满是血渍。（频率最高字符是 “的”，占比 8.45%）
= 1.0：一个熟睡的女孩被一阵清冷的风吹得不由自主地醒了，她看到了早上还未到来的黑暗，周围只有像诉说厄运般狂风呼啸而过。（频率最高字符是 “的”，占比 5.45%）
= 2.0：每天早上，他都会在露台上坐着吃早餐。柔和的夕阳照耀下，一切看起来安详寂静。但是有一天，当他准备端起早食的时候发现胡同里清冷的风扑进了他的意识中并带来了不安全感…… （频率最高字符是 “的”，占比 4.94%）
presence_penalty: [控制主题的重复度] -2.0 ~ 2.0 之间的数字，正值会根据到目前为止是否出现在文本中来惩罚新 tokens，从而增加模型谈论新主题的可能性（以云课堂的广告文案为例）
= -2.0：家长们，你们是否为家里的孩子学业的发展而发愁？担心他们的学习没有取得有效的提高？那么，你们可以放心，可以尝试云课堂！它是一个为从幼儿园到高中的学生提供的一个网络平台，可以有效的帮助孩子们提高学习效率，提升学习成绩，帮助他们在学校表现出色！让孩子们的学业发展更加顺利，家长们赶紧加入吧！（抓住一个主题使劲谈论）
= -1.0：家长们，你们是否还在为孩子的学习成绩担忧？云课堂给你们带来了一个绝佳的解决方案！我们为孩子提供了专业的学习指导，从幼儿园到高中，我们都能帮助孩子们在学校取得更好的成绩！让孩子们在学习中更轻松，更有成就感！加入我们，让孩子们拥有更好的学习体验！（紧密围绕一个主题谈论）
= 0.0：家长们，你们是否担心孩子在学校表现不佳？云课堂将帮助您的孩子更好地学习！云课堂是一个网络平台，为从幼儿园到高中的学生提供了全面的学习资源，让他们可以在学校表现出色！让您的孩子更加聪明，让他们在学校取得更好的成绩，快来云课堂吧！（相对围绕一个主题谈论）
= 1.0：家长们，你们的孩子梦想成为最优秀的学生吗？云课堂就是你们的答案！它不仅可以帮助孩子在学校表现出色，还能够提供专业教育资源，助力孩子取得更好的成绩！让你们的孩子一路走向成功，就用云课堂！（避免一个主题谈论的太多）
= 2.0：家长们，您有没有想过，让孩子在学校表现出色可不是一件容易的事？没关系！我们为您提供了一个优质的网络平台——云课堂！无论您的孩子是小学生、初中生还是高中生，都能够通过云课堂找到最合适的学习方法，帮助他们在学校取得优异成绩。快来体验吧！（最大程度避免谈论重复的主题）
stop: 最大长度为 4 的字符串列表，一旦生成的 tokens 包含其中的内容，将停止生成并返回结果
参考链接：https://blog.csdn.net/hekaiyou/article/details/128303729
```

实际效果：

```
baby_chat_alpha.py
****************************************************************************************************
       _           _             ____
  ___ | |__   __ _| |__  _   _  / __ \ _ __ ___   __ _ _ __ ___
 / _ \| '_ \ / _` | '_ \| | | ...