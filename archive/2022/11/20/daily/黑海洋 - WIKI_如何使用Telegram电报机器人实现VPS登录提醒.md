---
title: 如何使用Telegram电报机器人实现VPS登录提醒
url: https://blog.upx8.com/3097
source: 黑海洋 - WIKI
date: 2022-11-20
fetch_date: 2025-10-03T23:17:16.247548
---

# 如何使用Telegram电报机器人实现VPS登录提醒

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# 如何使用Telegram电报机器人实现VPS登录提醒

发布时间:
2022-11-19

分类:
[共享资源/Free](https://blog.upx8.com/Free/)

热度:
37366

相信很多小伙伴都有这样一个烦恼：手里堆积的服务器很多，总是担心被人暴力破解登录。在此之前，我曾经讲过我们可以通过更改SSH默认登录端口，改用SSH KEY登录或者利用faill2ban等工具来增加自己服务器的安全。关于这部分的内容，感兴趣的童鞋可以移步至我的博文：[**新手小白如何保护自己Linux主机的安全**](https://blog.upx8.com/go/aHR0cHM6Ly9jb2RlcmZhbi5uZXQvd3AtYWRtaW4vcG9zdC5waHA_cG9zdD0zMjk2JmFjdGlvbj1lZGl0)。

有没有更好的办法来监控我们的服务器呢？比如,一旦有人登录我们的服务器我们救能立马收到消息通知。实际上这里有很多通知方式，比如通过邮件或者短信。再者呢，就是通过电报机器人实现消息提醒。

关于电报机器人的介绍在这里我就不再赘述，你可以将其理解为微信上的小程序。想想我们在使用微信的过程中，小程序极大地提升了我们日常生活的便利性。无论是购物、打车，玩游戏，微信小程序都能让你在不用切换其他APP的情况下实现你的需求，电报机器人也是如此。那么，接下来我将给大家介绍，如何使用电报机器人实现VPS登录提醒。

## 1.注册电报账号

关于电报的注册流程不在本教程中进行讲述，大家可以自行Google。在这里我只简单提三点：

1）使用虚拟号码进行账户注册，你可以通过淘宝购买GV进行注册也可以自己注册GV。

2）使用Telegram时请开启代理服务，别傻傻地使用你本地网络，否则很容易暴露自己。

3）注册完Telegram后，请在Settings->Privacy and Security内开启Two-Step Verification。

在这里，可能还有很多小伙伴还不知道如何通过合理设置使得Telegra m能够正常使用。其实很简单，如果你是移动端，如V2rayNG、AnXray等客户端都支持分应用代理，只要你将Telegram加入其白名单即可。如果你是桌面端（如Windows系统），则需要通过设置代理的方式实现Telegram的正常使用。如下图所示：

![](https://coderfan.net/wp-content/uploads/2021/09/image-1-1024x488.png)

只要将你本地代理工具的Socks或者Http配置复制到Telegram内即可。

## 2.申请电报机器人

申请电报机器人需要通过BotFather进行申请。BotFather是电报专门用于机器人管理的机器人。我们可以通过它申请、管理我们自己的机器人。

很多刚开始使用电报的小伙伴不知道怎么找到自己所需要的机器人，其实很简单，只要知道其名字，你可以在电报搜索框内搜索即可。通过@BotFather，我们找到BotFather机器人。

![](https://coderfan.net/wp-content/uploads/2021/09/image.png)

在搜索到BotFather后点击Start，BotFather会提示你一些交互命令，用于你对你的机器人进行管理。在这个步骤中，我们需要先在聊天框内输入**/newbot**，BotFather会给予提示：

![](https://coderfan.net/wp-content/uploads/2021/09/image-2.png)

BotFather提示你需要为你的Bot选择一个名字，在这里我就随意起一个名好了（在这里我使用了FranzKafka，爱你，我的弗兰茨·卡夫卡），实际上你可以随意命名你的机器人。

![](https://coderfan.net/wp-content/uploads/2021/09/image-3.png)

紧接着，BotFather还需要你为你的Bot设置一个username，这个username需要满足特定的格式，即必须以bot结尾。在这里，你的Bot名不能与已有的Bot重名。当你的username符合要求之后,BotFather会发出类似于这样一段信息：

![](https://coderfan.net/wp-content/uploads/2021/09/image-4.png)

这段话主要有两个重点：

1.使用你的机器人可以通过t.me/username的形式进行使用。在这里你也可以直接点击蓝色的部分与你的bot开启对话。

2.你会得到一个专属于你的与你机器人绑定的HTTP API，这个API很重要，其他人可以通过这个API控制你的机器人。

**我们需要将这串API保存下来**，再点击t.me/username的蓝色字体部分，开启与你机器人的对话。注意，请点击START开启对话，这是你们对话的开端，如果你一直没有点击START，你的机器人是无法与你进行对话的，包括之后的提醒你也收不到哦。

之后，我们还需要在电报搜索框内输入@getidsbot，请注意不要选择错了哦。

![](https://coderfan.net/wp-content/uploads/2021/09/image-5.png)

我们点击START后其会给我们一个我们在电报内部的一个身份标识，在下图中为id这个字段之后的内容（在本教程中是18开头的）。

![](https://coderfan.net/wp-content/uploads/2021/09/image-6.png)

**我们同时也需要将id保存下来，这在之后会有用。**

## 3.构造HTTPS请求

在本教程中，通过电报机器人实现VPS登录提醒实际上是由你的服务端通过HTTPS的方式向Telegram的服务器发起请求，将消息通知到电报端，再由HTTP API与id对应到具体的bot机器人，由bot机器人进行具体信息的展示。所以，在这里我们需要先简单了解一下Telegram的API使用方法，详细的说明请参阅电报的官方文档：https://core.telegram.org/bots/api

在Telegrame的官方文档中，已经描述了如何通过https发送请求，如下图所示：

![](https://coderfan.net/wp-content/uploads/2021/09/image-7-1024x658.png)

具体细节不多讲，直接给出例子，如下：

**https://api.telegram.org/bot<token> /sendMessage?chat\_id=<id> &text=message**

其中token字段填入之前我们保存下来的HTTP API，id字段填入之前我们保存下来的id，填入后我们将其复制到浏览器中，回车可以得到如下内容：

![](https://coderfan.net/wp-content/uploads/2021/09/image-8-1024x169.png)

至此，可以表明利用HTTP API与你的id，可以成功通过Telegram服务器发起HTTPS请求，接下来我们则需要将这个行为放到服务器中去执行。

## 4.服务器脚本实现HTTPS请求

当我们在我们服务器上以脚本发起HTTPS请求时，我们需要使用curl命令。关于curl命令的具体使用方法，本教程中不做过多讲述。我们简单点，直接上脚本内容：

```
#!/bin/bash
#This script can send a alert when someone login into vps
#date:2021-09-02
#name：SSHLoginAlert.sh
#author:FranzKafka

echo "This is a script for ssh login alert"
token=xxxxxxxxxxxxxxxxx
echo "my token is $token"
id=xxxxxx
echo "my id is $id"
message=$(hostname && TZ=UTC-8 date && who && w &&last -1 | awk  'BEGIN{ORS="\t"}{print $1,$15}')
echo "send message is $message,begin...."
curl -v "https://api.telegram.org/bot${token}/sendMessage?chat_id=${id}" --data-binary "&text=${message}"
echo "send alert end"
```

请大家将token、id字段填为你们自己的内容，也就是上面要你们保存下来的内容。在写好脚本后,可以执行进行测试：

脚本输出结果：

![](https://coderfan.net/wp-content/uploads/2021/09/image-9-1024x699.png)

Telegram Bot消息内容：

![](https://coderfan.net/wp-content/uploads/2021/09/image-10.png)

在上述脚本中，对各个字段做一个说明：

**hostname ：**主机名，也就是你服务器的名字

**TZ=UTC-8**：设定时区为北京时间

**who**：当前登录者的信息，包含用户名与id

**w：**当前用户所使用的执行的命令信息

**last：**之前用户的登录信息

如果脚本测试没有问题的话，接下来我们需要让脚本在用户登录时自动执行，怎么实现呢。很简单，你只需要将该脚本移动到/etc/profile.d/这个文件夹下即可。此文件夹下的脚本会为系统的每一个用户设置环境信息。当用户登录时，该目录下的脚本会自动执行。请记住别忘记使用chmod命令将其权限变更为555，注意不是777.

完成以上操作后，我们退出我们的服务器，再次登录，可以去你的Telegram上看看是否收到消息提醒。

## 题外话

1.我本来是在Windows系统下写的脚本，结果一跑发现提示curl: (3) Illegal characters found in URL，通过cat命令发现每一行末尾会多出一个M来。原来是Windows系统下的文件格式为dos格式的，而linux内的文件格式需要为unix格式，两者的文件编码不同导致脚本运行有问题，通过dos2unix +脚本 解决该问题。

2.我本身有多个服务器，每个服务器都想实现这样的提醒，可我不想在每个机器上都把脚本写一遍，如果可以直接把脚本内容转移到另外的服务器那就好了。鉴于我只想传输一个脚本内容，数据量并不大。于是在这里我使用了scp命令，scp的具体用法如下：

**scp 【源地址】【目标地址】**

scp命令默认使用22端口，如果你的服务器SSH端口不是22端口，请使用-P参数指定端口。远程服务器的地址使用以下格式：

**用户名@IP地址：文件路径**

以上，就是本教程的全部内容啦！大家可以去试试哦。

1. ![不错](//q2.qlogo.cn/headimg_dl?dst_uin=105311456&spec=100)

   **不错**

   2024-07-09 22:09:31

   [回复](https://blog.upx8.com/3097/comment-page-1?replyTo=29902#respond-post-3097)

   加我微信18809550607

[取消回复](https://blog.upx8.com/3097#respond-post-3097)

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