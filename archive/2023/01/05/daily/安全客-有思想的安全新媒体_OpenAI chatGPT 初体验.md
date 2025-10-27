---
title: OpenAI chatGPT 初体验
url: https://www.anquanke.com/post/id/284267
source: 安全客-有思想的安全新媒体
date: 2023-01-05
fetch_date: 2025-10-04T03:02:33.222651
---

# OpenAI chatGPT 初体验

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# OpenAI chatGPT 初体验

阅读量**297075**

发布时间 : 2023-01-04 14:30:30

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

![]()

2022 年 11 月 30 日，OpenAI公布了最新的一个基于AI的对话系统ChatGPT，ChatGPT以对话方式进行交互。对话格式使ChatGPT能够回答后续问题、承认错误、质疑不正确的前提和拒绝不适当的请求。https://openai.com/blog/chatgpt/

## OpenAI的历史

OpenAI是由吉米·巴顿（Jimmy Wales）、拉里·佩奇（Larry Page）、伊隆·马斯克（Elon Musk）和沃伦·巴菲特（Warren Buffett）等人于2015年创立的人工智能研究机构。其宗旨是通过人工智能技术，促进人类进步并推动社会的发展。

在成立之初，OpenAI就受到了来自业内专家和公众的高度关注，并获得了大量资金支持。2016年，OpenAI与微软合作，推出了一款人工智能技术——GPT-2，它可以帮助人工智能系统更好地学习语言和文本。

2017年，OpenAI推出了另一款人工智能技术——Dota 2，它可以让人工智能系统在游戏中进行决策。同年，OpenAI还与索尼合作，推出了人工智能游戏“Go”。

2018年，OpenAI推出了深度学习技术，使人工智能系统能够进行更加复杂的任务。2019年，OpenAI与斯坦福大学合作，推出了人工智能聊天机器人“DALL-E”，它可以根据输入的文本生成相应的图片。

目前，OpenAI正在继续推动人工智能技术的发展，并与业界合作，共同推动人工智能领域的进步。

**以上为chatGPT自动生成。**

## ChatGPT 时间线

2022年12月1日：Sam Altman(山姆·阿尔特曼，现openAI CEO) 在推特分享 ChatGPT。

![]()

2022年12月5日：ChatGPT体验用户超100百万。

![]()

## ChatGPT 账号注册

**注册地址：**https://beta.openai.com/signup

账号注册、可以参考下面链接。

https://mp.weixin.qq.com/s/E4n63jltBPbAo8ZIMH10ig

https://mp.weixin.qq.com/s/\_AcXZ7PRDy55DnskS-Sl9w

**ChatGPT 开源机器人：**https://github.com/fuergaosi233/wechat-chatgpt

## 问答模块

![]()

## 代码解读

### **腾讯云接口调用代码解读**

![]()

### **CTF代码解读**

![]()

## 实现代码

### **实现一个批量扫描端口的工具**

![]()

### **实现http服务端，指定参数-p 为开放端口、默认开放端口为9999**

![]()

### **实现对pcap包的解析，若IP为公网IP，输出IP地址及MAC地址**

![]()

### **实现一个目录爆破工具**

1、随机生成移动端user-agent 5条。

2、设置参数-u，指定目标url地址。

3、设置参数-f，可指定文件，默认随机生成20个路径，路径为常见路径。

4、请求路径为 url地址 + 常见路径。

4、设置参数-p，设置请求代理。

5、设置超时时间为5秒。

6、处理请求异常情况。

7、实现多线程。

8、设置参数-t，可指定线程数，默认线程数20。

9、每次请求间隔0.3秒。

10、输出程序运行过程及请求结果。

![]()

![]()

![]()

### **实现sql注入靶场**

![]()

![]()

![]()

## 场景调研

### **云平台安全调研**

#### 1、介绍一下云平台

![]()

#### 2、介绍下云平台的攻击面

![]()

#### 3、云平台攻击场景

![]()

#### 4、云平台的攻击思路

![]()

#### 5、云平台密钥使用

![]()

#### 6、在渗透测试阶段，如何收集云平台认证凭证

![]()

#### 7、在渗透测试阶段，云平台认证密钥泄漏后，如何利用？

![]()

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**星阑科技**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/284267](/post/id/284267)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [网络安全](/tag/%E7%BD%91%E7%BB%9C%E5%AE%89%E5%85%A8)
* [OpenAI](/tag/OpenAI)

**+1**5赞

收藏

![](https://p0.ssl.qhimg.com/t01ae1a72a720da3a7b.png)星阑科技

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p2.ssl.qhimg.com/t010136e53e1b35516c.png)

[![](https://p0.ssl.qhimg.com/t01ae1a72a720da3a7b.png)](/member.html?memberId=147620)

[星阑科技](/member.html?memberId=147620)

星阑科技

* 文章
* **119**

* 粉丝
* **46**

### TA的文章

* ##### [保护敏感数据的艺术：数据安全指南](/post/id/290760)

  2023-10-18 10:57:25
* ##### [受邀演讲 | 确保数字化生态安全稳健](/post/id/290528)

  2023-09-05 17:48:29
* ##### [技术专题：API资产识别大揭秘（一）](/post/id/290471)

  2023-09-05 17:37:14
* ##### [解密与探究：理解WebSocket协议与报文格式](/post/id/290500)

  2023-08-30 14:36:15
* ##### [创新护航：萤火助力守护数据跨境安全](/post/id/290512)

  2023-08-29 16:10:15

### 相关文章

* ##### [威胁行为者针对 Gluestack 软件包发起供应链攻击，每周有超过 95 万次的下载面临风险](/post/id/308258)

  2025-06-09 17:25:59
* ##### [恶意软件攻击 16 个 React Native npm 软件包，100 万次下载面临风险](/post/id/308238)

  2025-06-09 17:01:38
* ##### [阿联酋中央银行要求金融机构放弃短信和 OTP 身份验证](/post/id/308132)

  2025-06-05 12:29:10
* ##### [警报：恶意 RubyGems 冒充 Fastlane 插件，窃取 CI/CD 数据](/post/id/308092)

  2025-06-04 15:31:41
* ##### [新的 PumaBot 僵尸网络利用强制 SSH 凭据入侵设备](/post/id/307967)

  2025-05-29 14:59:17
* ##### [APT41 恶意软件滥用谷歌日历进行隐蔽的 C2 通信](/post/id/307963)

  2025-05-29 14:55:27
* ##### [TikTok 视频在 ClickFix 攻击中推送信息窃取恶意软件](/post/id/307915)

  2025-05-28 14:05:13

### 热门推荐

文章目录

* [OpenAI的历史](#h2-0)
* [ChatGPT 时间线](#h2-1)
* [ChatGPT 账号注册](#h2-2)
* [问答模块](#h2-3)
* [代码解读](#h2-4)
  + [腾讯云接口调用代码解读](#h3-5)
  + [CTF代码解读](#h3-6)
* [实现代码](#h2-7)
  + [实现一个批量扫描端口的工具](#h3-8)
  + [实现http服务端，指定参数-p 为开放端口、默认开放端口为9999](#h3-9)
  + [实现对pcap包的解析，若IP为公网IP，输出IP地址及MAC地址](#h3-10)
  + [实现一个目录爆破工具](#h3-11)
  + [实现sql注入靶场](#h3-12)
* [场景调研](#h2-13)
  + [云平台安全调研](#h3-14)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)