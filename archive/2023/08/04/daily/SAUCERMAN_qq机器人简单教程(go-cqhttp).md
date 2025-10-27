---
title: qq机器人简单教程(go-cqhttp)
url: https://saucer-man.com/information_security/1102.html
source: SAUCERMAN
date: 2023-08-04
fetch_date: 2025-10-04T12:02:15.379475
---

# qq机器人简单教程(go-cqhttp)

* [Home](https://saucer-man.com/)
* [Archives](https://saucer-man.com/archives.html)
* [About](https://saucer-man.com/about.html)
* [Github](https://github.com/saucer-man)

Previous post
Next post
Back to top
Share post

* [1. go-cqhttp是什么](#cl-1)
* [2. 初步使用go-cqhttp](#cl-2)
* [3.进阶用法nonebot](#cl-3)

# qq机器人简单教程(go-cqhttp)

2023-08-03

5412

[信息安全](https://saucer-man.com/category/information_security/)

[qq机器人](https://saucer-man.com/tag/qq%E6%9C%BA%E5%99%A8%E4%BA%BA/)

> 文章最后更新时间为：2023年08月03日 16:46:06

## 1. go-cqhttp是什么

mirai 是一个在全平台下运行，提供 QQ Android 协议支持的高效率机器人库，而go-cqhttp是mirai的golang版本实现。其项目地址为<https://github.com/Mrs4s/go-cqhttp>， 官方文档为<https://docs.go-cqhttp.org/>

## 2. 初步使用go-cqhttp

首先根据下面的步骤来实现一个最简单的机器人，当接收到“hello”消息时，则自动发送“你好我是机器人”。

1.下载go-cqhttp，<https://github.com/Mrs4s/go-cqhttp/releases>
2.控制台运行.\go-cqhttp.exe，第一次运行会生成配置文件，这里为了简单起见，选择http模式即可
![2023-08-03T06:38:14.png](https://saucer-man.com/usr/uploads/2023/08/4267179954.png "2023-08-03T06:38:14.png")

3.打开配置文件，`反向HTTP POST地址列表`这一项即可，别的可以先不改，配置文件官方文档：<https://docs.go-cqhttp.org/guide/config.html>

```
servers:
  # 添加方式，同一连接方式可添加多个，具体配置说明请查看文档
  #- http: # http 通信
  #- ws:   # 正向 Websocket
  #- ws-reverse: # 反向 Websocket
  #- pprof: #性能分析服务器

  - http: # HTTP 通信设置
      address: 0.0.0.0:5700 # HTTP监听地址
      version: 11     # OneBot协议版本, 支持 11/12
      timeout: 5      # 反向 HTTP 超时时间, 单位秒，<5 时将被忽略
      long-polling:   # 长轮询拓展
        enabled: false       # 是否开启
        max-queue-size: 2000 # 消息队列大小，0 表示不限制队列大小，谨慎使用
      middlewares:
        <<: *default # 引用默认中间件
      post:           # 反向HTTP POST地址列表
        - url: 'http://127.0.0.1:8088' # 这里填写server的地址，所有的消息和事件都会发送到这里
```

4. 使用flask编写一个server，打印出接收到的消息，当接收到“hello”消息时，则自动发送“你好我是机器人”。

```
from flask import Flask, request
import sys
import json
import requests
from loguru import logger

app = Flask(__name__)

config = {
    "handlers": [
        {"sink": sys.stdout, "colorize": True, "format": "{time:YYYY-MM-DD HH:mm:ss.SSS} | {level} | {message}",
         "level": "INFO"},
        {"sink": "file.log", "rotation": "10 MB", "level": "DEBUG"},
    ],
    "extra": {"user": "yanq"}
}
logger.configure(**config)

# 监听端口，获取QQ信息
@app.route('/', methods=["POST"])
def post_data():
    data = request.get_json()
    if data["post_type"] == "meta_event" and data["meta_event_type"] == "heartbeat":
        return
    logger.debug(json.dumps(data))
    if data["post_type"] == "message":  # 接收到消息
        if data['message_type'] == 'group':  # 如果是群聊信息
            gid = data['group_id']  # 获取群号
            uid = data['user_id']  # 获取信息发送者的 QQ号码
            try:
                nickname = data['sender']['nickname']  # 获取信息发送者的 QQ昵称
            except:
                nickname = "unknow"
            message = data['raw_message']  # 获取原始信息
            logger.info(f"接收到群聊消息, 群号:{gid}, 发送人qq:{uid}, 发送人昵称：{nickname}, 消息:{message}")
        elif data["message_type"] == "private":  # 私聊信息
            uid = data['user_id']  # 获取信息发送者的 QQ号码
            nickname = data['sender']['nickname']  # 获取信息发送者的 QQ号码
            message = data['raw_message']  # 获取原始信息
            logger.info(f"接收到私聊消息, 发送人qq:{uid}, 发送人昵称：{nickname}, 消息:{message}")
            if message == "hello":
                r = requests.get(f"http://127.0.0.1:5700/send_private_msg?user_id={uid}&message=你好我是机器人")
                if r.json()["retcode"] == 0:
                    logger.info(f"给{uid}发送消息成功")
                else:
                    logger.info(f"给{uid}发送消息失败")
    return

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8088)  # 保证和我们在配置里填的一致
```

5.用命令行启动go-cqhttp.exe，会生成文件device.json，并且大概率出现协议不支持的情况

![2023-08-03T07:57:44.png](https://saucer-man.com/usr/uploads/2023/08/2486645501.png "2023-08-03T07:57:44.png")

6.修改device.json中的protocol为2，走的是Android Watch协议，然后重新运行go-cqhttp.exe，扫码登录即可。

![2023-08-03T08:01:21.png](https://saucer-man.com/usr/uploads/2023/08/4078545177.png "2023-08-03T08:01:21.png")

运行结果:

![2023-08-03T07:59:59.png](https://saucer-man.com/usr/uploads/2023/08/3850287856.png "2023-08-03T07:59:59.png")

## 3.进阶用法nonebot

官方文档已经列举了支持的事件和api，功能比较多，直接使用flask裸写比较复杂，可以使用框架nonebot：<https://nonebot.dev/docs/>,这是一个实现了onebot-11 和onebot-12协议的框架，有兴趣的可以使用下，默认采用fastapi，对异步支持比较好

ps:

* 之前用这个框架用了很久，只收消息所以没有被封，发群聊消息有概率封号，最好使用小号
* 如果要使用其他协议，比如ipad协议，只能搭配<https://github.com/fuqiuluo/unidbg-fetch-qsign>来使用，所以使用watch协议是最方便的

1 + 6 =

 回复

快来做第一个评论的人吧~

Copyright © 2025 By [Typecho](https://www.typecho.org) & [saucerman](https://saucer-man.com)

* [Home](https://saucer-man.com/)
* [Archives](https://saucer-man.com/archives.html)
* [About](https://saucer-man.com/about.html)
* [Github](https://github.com/saucer-man)