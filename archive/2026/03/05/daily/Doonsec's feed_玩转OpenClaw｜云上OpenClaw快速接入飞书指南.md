---
title: 玩转OpenClaw｜云上OpenClaw快速接入飞书指南
url: https://mp.weixin.qq.com/s/xuXOlBG-5Fi1sJkGjhNzNQ
source: Doonsec's feed
date: 2026-03-05
fetch_date: 2026-03-06T04:02:30.044186
---

# 玩转OpenClaw｜云上OpenClaw快速接入飞书指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/kztGyHFwmfzvsoZIMjFsFyic7rqfzLzg8Ho81wudvXY6DfEmMRd2O6m8Y9ogAepPerKPmuKTtt7dG8PbzBN62FPdUyqUia1zB3uoEkQGSJTDs/0?wx_fmt=jpeg)

# 玩转OpenClaw｜云上OpenClaw快速接入飞书指南

原创

didiplus
didiplus

攻城狮成长日记

![]()

在小说阅读器中沉浸阅读

最近`OpenClaw`火得不行，后台天天有人问：

* “部署好了`OpenClaw`，怎么在飞书里用啊？”
* “能不能让团队小伙伴一起在群里@机器人干活？”

今天就给大家带来一篇**保姆级教程**：手把手教你将云上部署的`OpenClaw`接入飞书，让你在飞书单聊或群聊中直接与AI助手交互，实现办公自动化、智能问答、任务管理等一系列酷炫功能！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfzej7iaut4z6FlCqXKWKiczaucHrCAAa4e1atDmYkzvh6mfOGqwDJn1dza3MrOBFuLVjF0cNMsxjd0F1sIElXsb0kVvqf25VRe3s/640?wx_fmt=png&from=appmsg)

## 为什么要把OpenClaw接入飞书？

在正式开始前，先来看看接入飞书后你能获得什么：

* ✅ 无缝交互：不用切换`App`，在飞书里就能直接和`AI`对话
* ✅ 群聊协作：在群里@机器人，全员都能用，团队效率翻倍
* ✅ 主动提醒：结合`OpenClaw`的心跳机制，定时推送日报、周报到你飞书
* ✅ 多端同步：电脑端、手机端飞书都能用，随时随地唤醒AI

简单说，**接入飞书后的OpenClaw，才是真正融入你工作的“数字副驾驶”**！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfzFmpibF6X7J6jJl5CMgicVkR9QNflfgCrTicoylAPj9Wib7UiblAficVibYG2BMZOBLicOLdTZZaAjI0Ag5X6p5QYc3Anh0Rtspicv4LRA/640?wx_fmt=png&from=appmsg)

## 为什么推荐1Panel？

`1Panel`是一款提供直观`Web`管理界面的`Linux`服务器管理工具，支持对智能体、大模型、网站、数据库、容器等进行统一管理。通过它的应用商店，`OpenClaw`的安装部署变得极其简单，全程可视化操作，无需手敲复杂命令！

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfw3Q0Yqu2E7jKG9ZF22gfUWrWmgl3hVSbMUsK2cfmtde4oc6SyxZJ1q4iadiaJGx4HbcdKknwMeXYIcrm09SNGJV2pdCibbUgT3BE/640?wx_fmt=png&from=appmsg)

## 准备工作

### 服务器要求

* 配置：最低2核2G内存，推荐2核4G以上
* 系统：`Ubuntu 22.04 LTS`（推荐）或`Debian 12`
* 带宽：建议`≥5M`，保证访问流畅
* 云厂商：阿里云、腾讯云、京东云均可，新用户常有几十元的优惠套餐（参考上篇文章）

### 需要提前获取的凭证

1. 大模型`API Key`（任选一家）：

* 智谱GLM-4[1]
* DeepSeek[2]
* 阿里云百炼[3]
* 其他：`OpenAI`、`Gemini`、`Moonshot`等。

2. 飞书账号：需具备企业管理员或开发者权限（个人账号也可创建企业自建应用）

## 1Panel安装部署

### 步骤一：执行在线安装命令

输入下面的在线安装脚本命令，就可以开始安装了。

```
1bash-c"$(curl-sSL https://resource.fit2cloud.com/1panel/package/v2/quick_start.sh) "
```

### 步骤二：指定1Panel安装目录

安装脚本一开始会让你选择安装到哪个文件夹。如果没有特殊需求，直接按回车键用默认的就行。

```
1设置1Panel 安装目录（默认为 /opt）：
```

### 步骤三：完成docker部署

设定好目录后，安装脚本会检查你的服务器上有没有Docker。如果没装，它会问你是否要安装。这时你只要输入“y”就可以开始安装了。

```
1检测到未安装 Docker，是否安装[y/n]: y
```

### 步骤四：镜像加速器配置并设置默认参数

装好Docker后，你会看到一些提示，问你是否要设置镜像加速，然后一步步让你设置1Panel的端口、安全入口和面板用户的密码等。根据自己的需求来设置就行，但要注意确保你设置的那个端口是已经开通了的。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfw8Kf7mVFCV2fy3MpcnF4xM326ou631oRmZkOOJbfP6ngX4nfzer2xf1JZz9MawJmRgeGrE47sfFOIgxQgCno3ruKQibkF8zmXU/640?wx_fmt=png&from=appmsg)

### 步骤五：获取1Panel面板的登录信息

设置好之后，系统会自动打印出1Panel的登录信息，就像下面的图一样。大家记得保存这些信息，以后用起来就方便多了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfztK1lIUVMFXewNYAEScK29XwtgQDZ6K9qibQuUs6QN73zp2fkwpAmeJkVtdVETiaRJL9K9TR9ussjTBsrM6aib6aGnRicrGEgRMdM/640?wx_fmt=png&from=appmsg)

## OpenClaw安装部署

### 步骤一：添加模型账号

首先进入「AI」管理里的「智能体」菜单，点击进去后，切换到「模型账号」管理。接着点击「添加模型账号」按钮，然后根据提示选择一个模型供应商，并填好模型账号的信息，最后完成创建。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfySRNFeYZiaQRRFRI3ibLWibNcsv6HwHEOia2GKoZM0NhtIyWbl5ib1BvWHjRlbwIe7pxI8QoCGOvdcc1dMqKuzVSYAfd77l4NZRAR4/640?wx_fmt=png&from=appmsg)

### 步骤二：创建智能体

准备好模型账号后，切换到「智能体」界面，点击“创建智能体”，然后按照提示输入需要的信息就行了。具体步骤可以参考下面的图片：

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyY6nicbLKfLODT7FksIXEo5WYVR7iaaEtePNYGBIaJsiaztuE79yBJBia0UO9ghUIia5M9y1rb7G7t0oK3RsEREcaSM5u89Gbrc7bQ/640?wx_fmt=png&from=appmsg)

以上参数配置完成后，直接点击确认，`OpenClaw`开始安装。直到如下图所示，代表完成安装。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfzcQ16fCXvklwFgDeFtZP4W1GaLiachvkGQUjXcFN1Mj5bM0qbj14WujlmqNS3nWWMAUkRHcDzW4QPnUgJib13dzeicUatDlHyt3o/640?wx_fmt=png&from=appmsg)

### 步骤三：验证OpenClaw部署成功

装好`OpenClaw`后，打开智能体列表页面，如下图所示，直接点击`WebUI`就能进入`OpenClaw`的界面了。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyjK7eB9w1Ir83D5F4EPKUu4yGDibYx9G2J2fk2KEl3KGKnbMrz9BC8IzK7buiamiad25V068ANlRwD1yzMbkuruvZ8SkxbBSl18Q/640?wx_fmt=png&from=appmsg)

打开`OpenClaw`页面后，试着输入一些信息。如果AI助理能正常回复，就像下面的图示那样，那就说明`OpenClaw`已经成功部署好了。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfyQAJJq3ozTyKJnTuIG9Ah4vzTxlXCNhOcxWBEHeibA1SqemH8gN05aTl1lz55D30MuJ8En2a6jJxdsEPd9WszCr9ydPT9iaezwk/640?wx_fmt=png&from=appmsg)

## **飞书渠道配置**

现在已经把`OpenClaw`全部设置好了，下一步我们要配置飞书。要配置飞书，首先得在飞书里创建一个能用的机器人。按照下面的步骤一步步来就行了。

> `1panel`
>
> 升级到了v2.1.2版本，现在OpenClaw支持的渠道多了好几个，比如说飞书就是其中一个新增的。

### **步骤一：创建企业自建应用**

首先，打开飞书并进入飞书开放平台[4]。然后，找到「开发者后台」，选择「企业自建应用」，再点击「创建企业自建应用」，就像下图展示的那样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfx2WeGF5YkbLeLrIovwLkgHEiajmiaDic3Pvcg9TakTtYZFUSUyPJuBSVvfpMNFRTRhOGGjY9JIfzh0Biad6tNSvt8CiaJwvd2QpfvM/640?wx_fmt=png&from=appmsg)

### **步骤二：添加机器人能力**

如下图所示，点击添加机器人，完成机器人创建。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfz1z2b7l8C570e6rt9eO82G2JLLFUicJicszXbM5TfM0ZpAzNUDs9ugibN9GQxWGib7APHctZ3ylJUfqkoPCbkYTWVPbnxbia86yVJY/640?wx_fmt=png&from=appmsg)

进入机器人页面后，点击机器人配置后的编辑按钮，定义机器人名称，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfwDWtoS6KxFibh4mejZiaHTkAvlvnxa0cjMicGPaweILnl36hTtqPPosP9O9YVicvvTrhRZDt6tZiany2fb0W3qVSa6j4QfzUtPnPOw/640?wx_fmt=png&from=appmsg)

### **步骤三：配置权限**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfzMsx5phX8kLXCHA9aOuOjt1aibK7PL7ZvPuukndtsCDyslRsZH2tJ7EF99I9bX5TPMQd78Suyiamay9fQjs6BiblEzEd5ICyRob0/640?wx_fmt=png&from=appmsg)

点击「批量导入/导出权限」，清空默认配置权限信息，将如下所示权限授权脚本复制粘贴，点击保存即可。

```
1{

2"scopes":{

3"tenant":[

4"aily:file:read",

5"aily:file:write",

6"application:application.app_message_stats.overview:readonly",

7"application:application:self_manage",

8"application:bot.menu:write",

9"cardkit:card:write",

10"contact:contact.base:readonly",

11"contact:user.employee_id:readonly",

12"corehr:file:download",

13"docs:document.content:read",

14"event:ip_list",

15"im:chat",

16"im:chat.access_event.bot_p2p_chat:read",

17"im:chat.members:bot_access",

18"im:message",

19"im:message.group_at_msg:readonly",

20"im:message.group_msg",

21"im:message.p2p_msg:readonly",

22"im:message:readonly",

23"im:message:send_as_bot",

24"im:resource",

25"sheets:spreadsheet",

26"wiki:wiki:readonly"

27],

28"user":[

29"aily:file:read",

30"aily:file:write",

31"contact:contact.base:readonly",

32"im:chat.access_event.bot_p2p_chat:read"

33]

34}

35}
```

### **步骤四：获取凭证并1Panel配置**

打开飞书平台，找到「凭证与基础信息」这一项，然后获取你的应用凭证，就像下图展示的那样。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfwdzCwTw1mooLtPeqy0aYZiajsX4QAYnh6HmQAL8FjrGGxEMPPZkHicBebdiblMkxBOufZVq4xSMVNncH2ZKHIvngkjKV5NZGAL6M/640?wx_fmt=png&from=appmsg)

获取后，进入`1Panel`的「智能体」的「配置」页面，完成飞书聊天渠道配置，点击保存，如下图所示：

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfwwy9172CEmgFF84Bm1AHSSAeAfx9ziaLWo6OWLEeDHyM2JCDrOggldC9jFgCNdG8oIMPdtQa8LnE86S0ib1ia58BhYpBSOrO4Qqg/640?wx_fmt=png&from=appmsg)

### **步骤五：创建事件与回调**

如下图所示，进入「事件与回调」菜单，分别完成订阅方式设置以及事件添加。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfwJUUuZbFrAX3kgqoKa5tVzfhNGEkh3EujXpJ0dcQQMFbua177cq9zS5r7yNgDxiamKdGNEqoRkyRPTTr1CJxTXm5F2q6oqFZJc/640?wx_fmt=png&from=appmsg)

添加事件：输入`im.message.receive_v1`搜索，基于「应用身份订阅」勾选接收消息，最后确认添加即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfyWUsSZWBz7aHAricSyK2GqgtR87JSzzBA0z7oTAbBfTV13YQQlo6aCTUjE5NBsg97IdrJPZQwNgTJ1XHW7qp6eZgqEX1fnm3qs/640?wx_fmt=png&from=appmsg)

### **步骤六：创建并发布版本**

确认完成后点击「创建版本」，然后根据要求输入版本相关信息并发布，个人账号无需审批，企业账号需要进行企业审批。

![](https://mmbiz.qpic.cn/mmbiz_png/kztGyHFwmfw8bffOwuz9RSqiaVzMZwPSldicMZNs8iavcSr4p31H4rPAac2Pu4ic2CbticTjLfKey4F1EaWNIcxSOMYWib2a1ib2z64UyVV8lGL7wo/640?wx_fmt=png&from=appmsg)

### **步骤七：飞书渠道验证确认**

以上信息配置完成后，我们进入飞书客户端，如下图打开应用：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfzJLCLXjLGFcKe7S1jZH9vapEJPc2rfm6Nu9fKNibcojWribsaabDJ99Mkx3VYmBLvvVicu3jq7GfKjYaSuY6fMfE7Zicrmqd2ceVI/640?wx_fmt=png&from=appmsg)

第一次发送消息，需要进行配对码确认。在飞书上给机器人随便发送一条信息，如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfx779Azudlu9S3cfy9SUiamWc8Iq2qVfjNDI1JTMYSCGUbib8RwW58LaXTm6BF79mV9FfQlulA6OCwlehXQlUW6iaUF7YJicSXT1oE/640?wx_fmt=png&from=appmsg)

然后复制这配对码，在1panel上进行确认。如下图所示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kztGyHFwmfzrzicWH77sySMdslZzWRm34KmwNSsuM6iccsJEdvx84zKqxnuxMA6Aichkxg6Y92CVpCJNAT1beGriaxuUian17lNclxKiaXKntibRUA/640?wx_fmt=png&from=appmsg)

## 总结

通过`1Panel`面板，`OpenClaw`的部署变得前所未有的简单。再加上飞书的`API`无限调用权益，你完全可以搭建一个**7×24小时运行、随时随地可调用的私人AI助手**，真正实现移动办公自由

|  |
| --- |
| 推荐文章  [OpenClaw部署神器！阿里腾讯京东云服务器骨折价，几十块搞定AI](https://mp.weixin.qq.com/s?__biz=MjM5OTc5MjM4Nw==&mid=2457389579&idx=1&sn=42c7d1c0f0b701b...