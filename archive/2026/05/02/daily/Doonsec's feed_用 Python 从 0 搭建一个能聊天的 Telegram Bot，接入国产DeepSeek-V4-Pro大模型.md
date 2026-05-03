---
title: 用 Python 从 0 搭建一个能聊天的 Telegram Bot，接入国产DeepSeek-V4-Pro大模型
url: https://mp.weixin.qq.com/s/jkup3SLN0LTE2jv5LUo3Hg
source: Doonsec's feed
date: 2026-05-02
fetch_date: 2026-05-03T05:25:30.596246
---

# 用 Python 从 0 搭建一个能聊天的 Telegram Bot，接入国产DeepSeek-V4-Pro大模型

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LtibzcRx8GjXAISUAF5hhcQNkib3m2XEeZLbuGicAiamXUt2AD7YFib1QrlzAyEHA5JXf8K0BNHTbTHsOC0Vgzs3LNbV9q7CWA1CkQBXW9gzRawY/0?wx_fmt=jpeg)

# 用 Python 从 0 搭建一个能聊天的 Telegram Bot，接入国产DeepSeek-V4-Pro大模型

原创

W不懂安全
W不懂安全

W不懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

很多人第一次接触 Tg Bot，都会卡在两个问题：从哪里开始，以及怎么把“能用”变成“好用”。这篇内容不绕弯，从官方 Bot API 出发，用最简单的一套 Python 方案，在本地跑通一个可交互的聊天机器人。没有复杂部署，没有多余框架，先把核心链路打通，再谈扩展。

一、整体思路（先搞清楚架构）

你要做的其实就三步：

1. 用 Tg 里的 BotFather 创建机器人 → 拿到 Token
2. 用 Python 写程序 → 调用 Tg Bot API
3. 本地运行 → 用“长轮询（long polling）”接收消息

👉 不需要服务器，不需要公网 IP，适合你现在的需求

如果你想在服务器部署，那就需要另一个方案，需要准备的是：

* 一台1核 1G运行内存配置的服务器
* 一个域名，WebHook强制要求HTTPS，不能使用http

二、创建Bot（用 BotFather）

### 步骤：

1. 打开 Tg
2. 搜索：`@BotFather，一定要选择带有蓝色√的，这是官方标志。`

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjUIpWFh2HYsSQiaggAqzibaWOf8PpA6v6QuJfPTw587vIhbcDcU3pvVbpVzXxG5Hd1pWLeAM9pfpMYSn0haRp2uCxF59JD7S2hibE/640?wx_fmt=png&from=appmsg)

`3.输入：`

```
/start/newbot
```

然后按提示走：

* 起名字（随便）
* 用户名（必须以\_bot结尾），这个用户名是机器人的用户名，后期搜索查找机器人就用这个，相当于唯一标识ID。

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjVfA1r9FJZ6fUaT3QAuyCk0oiaT6xrlM4FxRjakT7rOrf7qbqZ0gqiaUevU1XPSwicrPZKeib9qb5wDMnUaqaOrZTicj3BODibUQ21kE/640?wx_fmt=png&from=appmsg)

创建成功后你会得到一个：

```
HTTP API Token:123456789:ABCxxxxx
```

⚠️ 这个 Token 很重要，相当于密码，别泄露

三、使用Python方案

虽然可以直接用 requests 调 HTTP，但更推荐用官方生态库：

```
python-telegram-bot
```

优点：

* 基本贴合官方 API
* 文档成熟
* 支持异步（性能好）
* 很多人用

四、环境准备

在本地Python环境中需要安装此依赖：

```
pip install python-telegram-bot --upgrade
```

五、简单可运行Bot（核心代码）

直接复制粘贴以下代码就能跑：

```
from telegram import Updatefrom telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypesTOKEN = "你的Bot Token"# 收到消息时触发async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):        user_text = update.message.text        # 简单回复       reply = f"你说的是：{user_text}"       await update.message.reply_text(reply)# 主函数def main():        app = ApplicationBuilder().token(TOKEN).build()        # 监听所有文本消息    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))    print("Bot 已启动...")        app.run_polling()if __name__ == "__main__":     main()
```

执行下方命令运行，如果是在pycharm编辑器里编码的，直接运行即可。

```
python bot.py
```

看到：Bot 已启动...    证明代码没问题。

接下来打开tg，在搜索栏里搜索你机器人的ID。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVibaRTKKzdALyricl6jNzCNmcwWdcNBk5j56ia1u00DUCtzTGQvYLkHzHbUrfyJC2m63jvDGZVJAFV71CRAUYLxGdIUS1L9vPSGM/640?wx_fmt=png&from=appmsg)

然后给它发送消息，它能返回你发送的消息，则证明没有问题，最基本的通道打通了。

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVoBWAkSuDttL2u68EqBv5KqaboLDoEZKrkJNrBcaoJRog2Unw9nTX4ALqoaglDAcAIrIWTxXprS9GiasuKaPpKiaZu7lygdrJiaw/640?wx_fmt=png&from=appmsg)

六、加入基础命令功能和逻辑

比如 /start 与 /help 指令

```
from telegram.ext import CommandHandler
# ===== 命令：/start =====async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):        await update.message.reply_text("你好，我是你的机器人 👋")# ===== 命令：/help =====async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):        await update.message.reply_text("你可以随便跟我聊天，或者试试输入：你好 / 你是谁")
app.add_handler(CommandHandler("start",start))app.add_handler(CommandHandler("help",help_command))
```

在Bot机器人里再次输入/start 和 /help，你就能看到你设置的指令信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjV46M2BFfTriacMYzagJnPibJrHrTzHFibKOsURqS0VEDlicmMsDK7ABKdRBwCibvMzqusDEWBnE7uuVH1jvj41L58npxiadibar9C368/640?wx_fmt=png&from=appmsg)

如果你想加点逻辑，比如关键词回复：

```
async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):        text = update.message.text.lower()        # 👉 关键词逻辑        if "你好" in text:                reply = "你好呀，很高兴见到你～"        elif "你是谁" in text:                reply = "我是你亲手创建的 Telegram Bot 🤖"        elif "天气" in text:                reply = "这个功能还没接入天气API 😄"        else:                reply = f"我收到了：{text}"            await update.message.reply_text(reply)
```

然后向机器人发送消息：

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjUMEWuceBiczt2RKyz4xuNd3mZbpS6ia0L3mb8icMrn46XFge70MMnD4OcJ4NXGV3pUSScBkpOUeOYuKPrTLwvzCsLKcmvetvZx0I/640?wx_fmt=png&from=appmsg)

七、接入 DeepSeek 模型

需求效果是：只在用户输入 `/deepseek` 时才调用 DeepSeek，其它时候不走 AI

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjWqqwbJFWoKFoGrAibuowXY6JIlVlVnRw42Oicibr8aQuoCvtTx3ypibM6qBfU0uvfzIHoR9u5ib665oicQ59RCXlWbC8RQObkUJ7fuM/640?wx_fmt=png&from=appmsg)

完整效果代码：

```
from telegram import Updatefrom telegram.ext import (     ApplicationBuilder,        MessageHandler,        CommandHandler,        filters,        ContextTypes,)from openai import OpenAIimport asyncio# ===== Token =====TELEGRAM_TOKEN = "你的Bot Token"DEEPSEEK_API_KEY = "你的DeepSeek API Key"# ===== DeepSeek 客户端 =====client = OpenAI(        api_key=DEEPSEEK_API_KEY,        base_url="https://api.deepseek.com")# ===== /start =====async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):        await update.message.reply_text(                "你好 👋\n输入 /deepseek + 内容，即可使用 AI 聊天"        )# ===== DeepSeek 调用 =====def chat_with_deepseek(user_text):        response = client.chat.completions.create(                model="deepseek-chat",                messages=[                        {"role": "system", "content": "你是一个简洁、友好的助手"},                        {"role": "user", "content": user_text},                ],                temperature=0.7,        )        return response.choices[0].message.content# ===== /deepseek 指令 =====async def deepseek_command(update: Update, context: ContextTypes.DEFAULT_TYPE):        # 获取命令后面的内容        args = context.args        if not args:                await update.message.reply_text("用法：/deepseek 你想问的问题")                return        user_text = " ".join(args)        msg = await update.message.reply_text("思考中...")        loop = asyncio.get_event_loop()        reply = await loop.run_in_executor(None, chat_with_deepseek, user_text)        await msg.edit_text(reply)# ===== 普通消息（可做关键词逻辑）=====async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):        text = update.message.text.lower()            if "你好" in text:                reply = "你好呀～（AI功能请用 /deepseek）"        else:                reply = "我目前只在 /deepseek 模式下提供智能回复 🤖"        await update.message.reply_text(reply)# ===== 主程序 =====def main():        app = ApplicationBuilder().token(TELEGRAM_TOKEN).build()        # 命令        app.add_handler(CommandHandler("start", start))        app.add_handler(CommandHandler("deepseek", deepseek_command))        # 普通消息        app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))        print("Bot 已启动（/deepseek 模式）...")        app.run_polling()if __name__ == "__main__":        main()
```

如果你后边不想用这个机器人了，该怎么停止或删除？

直接在 BotFather里输入： /mybot ，然后选择你的 Bot，选择Delete Bot。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjWdBicKakLhl97UHAQibzrkYiaQpuzaSkuAZjpQBickN1mdOYKUDOBe7uzbFkb0ZJIlcrUfiajecibCdjBE9rlBflPLOJSddSCvCCF3I/640?wx_fmt=png&from=appmsg)

又或者发送 /deletebot，选择你的Bot机器人，即可删除。

删除之后，你的机器人就会编程这个样子：

![](https://mmbiz.qpic.cn/mmbiz_png/LtibzcRx8GjVvrsxpdSRwibgVZibLpqudbB6ibWYjicLOyfCVIZzV1m3re1c22UqeM03ZnibJPoX6ZpOCJ1DC43Ka1W9HtrhLoeW5YcUKUuOfKFMg/640?wx_fmt=png&from=appmsg)

到这里，一个从 0 到可用的 Tg Bot，就已经完整跑通了。

你可以选择停在这里，把它当作一个练手项目；也可以在这个基础上继续扩展，让它变得更聪明、更有个性。

剩下的，无非就是不断往里面加能力而已。

还有更多好玩有趣的功能可以去探索，如果不会，可以上网找找相关教程，或者让AI帮你写代码，你只需要给它发需求即可。整体来说并不复杂。

本期内容到此结束。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/LtibzcRx8GjXibu188DgR2icXAYBQtNf01bhpxic7jqf6urQPOCpmib4T38DSJQ1bdm1hkrqeCwSNPWCjicD9GAj5icWHicBWTI9sHU19kFibKaVtJ50/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

W不懂安全

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y4PrZUSw1T9GU9MhK80Q2QsthTRvcxtR5YUibqAQpedfvo4TopCYw1NlLwOWAzC5MXA2XZTqS84pSHdtFjVFNjw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过