---
title: LLM is all you need for the backend - 郑瀚Andrew
url: https://buaq.net/go-172676.html
source: unSafe.sh - 不安全
date: 2023-07-22
fetch_date: 2025-10-04T11:52:25.942018
---

# LLM is all you need for the backend - 郑瀚Andrew

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/d82026aa865847e56491be6e23d36a3d.jpg)

LLM is all you need for the backend - 郑瀚Andrew

人们一直在说Github Copilot将取代程序员。我们认为这是错误的。我们已经有了类似GPT-4这种强大的LLM模型，却还要把自己限制在编写传统代码上吗？不！所有代码都有bug！代码不是对
*2023-7-21 21:33:0
Author: [www.cnblogs.com(查看原文)](/jump-172676.htm)
阅读量:21
收藏*

---

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230721203034896-1008288802.jpg)

人们一直在说Github Copilot将取代程序员。我们认为这是错误的。我们已经有了类似GPT-4这种强大的LLM模型，却还要把自己限制在编写传统代码上吗？不！所有代码都有bug！

代码不是对业务逻辑进行编码的理想方式，代码必须经过审查，并且它按照程序员的指示执行，而不是按照程序员的要求进行编码和执行。这里最麻烦地事在于，每一层的意图传递都存在信息丢失：

**现实世界业务逻辑 -> 程序员对现实世界的观察 -> 程序员根据自己的观察对业务逻辑继续进行建模 -> 程序员通过代码和框架实现一套建模仿真 -> 程序在计算机系统中被执行**

显然，上述流程是一种低效、不精确的流程，商业逻辑的正确形式应该是人类智慧！谁需要python和ec2s、biz逻辑和postgres？

一个理想地流程应该是如下这样的：

**现实世界业务逻辑 -> 包含人类智慧（对世界本质的理解）的一种信息载体 -> 程序在计算机系统中被执行**

以一个简单的”todo list app“为例，我们构建了一个完整的由LLM提供支持的后端+数据库。它根据API调用的名称推断业务逻辑，并可以持久存储数程序运行的状态。

和传统software1.0相比，这个software2.0程序的主要特点如下：

* 通过prompt programing的方式，而不需要由程序员编写固定的backen业务逻辑代码（例如：sort\_todos\_alphabetically() ）和路由代码（例如："This is a todo list app"）
* 通过few-shot prompt的方式，显式初始化json数据格式（例如：{todo\_items:[｛title：“吃早餐”，completed:true}，｛title:“上学”，completed：false｝]）
* 通过自然语言和backend进行交互，理论上，frontend用户可以调用无限多地backend endpoints，LLM会自动将用户输入的自然语言指令，翻译为合理的业务逻辑，并通过LLM内部状态执行完成后，更新当前上下文状态

参考链接：

```
https://github.com/RootbeerComputer/backend-GPT
```

我们基本上使用GPT来处理待办事项列表应用程序的所有后端逻辑。我们用一个带有预填充条目的json作为应用程序的状态存储，这些条目有助于定义模式。然后，我们传入提示符、当前状态和一些用户输入指令/API调用，并提取对客户端+新状态的响应。

在这里，LLM可以被视为一个底层通用操作系统，用于处理所有基本的CRUD逻辑，省去了我们编写后端路由的工作。例如，用户可以输入add\_five\_housework\_todos（）或delete\_last\_two\_todos）或sort\_todos\_alphabetically（）等命令，而不是写特定的路由。

server.py

```
import json
from flask import Flask
from flask_cors import CORS
import re
import ast

def gpt3(input):
    import openai
    openai.api_type = "azure"
    openai.api_base = "https://openai-service-instance-yuxuan.openai.azure.com/"
    openai.api_version = "2023-06-01-preview"
    openai.api_key = "79244fc233c445c59e986c8b3da84f08"

    def getCompletion(prompt):
        message = [
            {"role": "system", "content": "you are a useful assistant."},
            {"role": "user", "content": prompt}
        ]
        response = openai.ChatCompletion.create(
            engine="deployment-gpt-35-turbo-16k",  # engine = "deployment_name".
            messages=message
        )
        return response['choices'][0]['message']['content']

    completion = getCompletion(input)
    return completion

def dict_to_json(d):
    return d.__dict__

app = Flask(__name__)
CORS(app)
db = json.load(open('db.json','r'))
print("INITIAL DB STATE")
print(db['todo_list']["state"])

@app.route('/<app_name>/<api_call>')
def api(app_name, api_call):
    db = json.load(open('db.json','r'))
    print("INPUT DB STATE")
    print(db[app_name]["state"])
    gpt3_input = f"""{db[app_name]["prompt"]}
API Call (indexes are zero-indexed):
{api_call}

Database State:
{db[app_name]["state"]}

Output the API response as json prefixed with '!API response!:'. Then output the new database state as json, prefixed with '!New Database State!:'. If the API call is only requesting data, then don't change the database state, but base your 'API Response' off what's in the database.
"""
    #print("gpt3_input: ", gpt3_input)
    completion = gpt3(gpt3_input)
    print("completion: ", completion)

    # parsing "API Response" and "New Database State" with regex
    api_response_match = re.search("(?<=!API Response!:).*(?=!New Database State!:)", completion, re.M | re.I | re.S)
    new_database_match = re.search("(?<=!New Database State!:).*", completion, re.M | re.I | re.S)

    # converting regex result into json string
    api_response_text = api_response_match.string[api_response_match.regs[0][0]:api_response_match.regs[0][1]].strip()
    new_database_text = new_database_match.string[new_database_match.regs[0][0]:new_database_match.regs[0][1]].strip()
    #print("api_response_text: ", api_response_text)
    #print("new_database_text: ", new_database_text)

    response = json.loads(json.dumps(ast.literal_eval(api_response_text)))
    print("API RESPONSE")
    print(response)

    new_state = json.loads(json.dumps(ast.literal_eval(new_database_text)))
    print("New Database NEW_STATE")
    print(new_state)

    db[app_name]["state"] = new_state
    json.dump(db, open('db.json', 'w'), indent=4, default=dict_to_json)
    return response

if __name__ == "__main__":
    app.run(
        host='0.0.0.0',
        port=4321
    )
```

db.json

```
{
    "todo_list": {
        "prompt": "This is a todo list app.",
        "state": {
            "todos": [
                {
                    "title": "Learn react",
                    "completed": true
                },
                {
                    "title": "Buy Milk",
                    "completed": true
                },
                {
                    "title": "Do laundry",
                    "completed": false
                },
                {
                    "title": "Clean room",
                    "completed": true
                }
            ]
        }
    },
    "chess": {
        "prompt": "You are a chess assistant",
        "state": {
            "board": [
                [
                    "r",
                    "n",
                    "b",
                    "q",
                    "k",
                    "b",
                    "n",
                    "r"
                ],
                [
                    "p",
                    "p",
                    "p",
                    "p",
                    "p",
                    "p",
                    "p",
                    "p"
                ],
                [
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " "
                ],
                [
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " "
                ],
                [
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " "
                ],
                [
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " ",
                    " "
                ],
                [
                    "P",
                    "P",
                    "P",
                    "P",
                    "P",
                    "P",
                    "P",
                    "P"
                ],
                [
                    "R",
                    "N",
                    "B",
                    "Q",
                    "K",
                    "B",
                    "N",
                    "R"
                ]
            ],
            "turn": "white",
            "white_castle_kingside": true,
            "white_castle_queenside": true,
            "black_castle_kingside": true,
            "black_castle_queenside": true,
            "en_passant": null,
            "halfmove_clock": 0,
            "fullmove_number": 1
        }
    }
}
```

![](https://img2023.cnblogs.com/blog/532548/202307/532548-20230721212320746-1369597216.png)

列举当前todo list数据库，

```
http://8.222.198.132:4321/todo_list/sort_todos_alphabetically()

/*
INPUT DB STAT...