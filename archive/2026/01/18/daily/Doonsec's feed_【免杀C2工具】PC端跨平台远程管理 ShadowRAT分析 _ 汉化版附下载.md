---
title: 【免杀C2工具】PC端跨平台远程管理 ShadowRAT分析 | 汉化版附下载
url: https://mp.weixin.qq.com/s/wyRsJfZjqVKgI1az0pmsSQ
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:39:31.672211
---

# 【免杀C2工具】PC端跨平台远程管理 ShadowRAT分析 | 汉化版附下载

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2krPdiaNgcSCqIWicvYpFwAA7bMOCU2azhnU4gLa8ZllyaRFibQSnV9apsm7zprLg0y8DshB1SYG0zEw/0?wx_fmt=jpeg)

# 【免杀C2工具】PC端跨平台远程管理 ShadowRAT分析 | 汉化版附下载

星夜AI安全
星夜AI安全

星夜AI安全

![]()

在小说阅读器中沉浸阅读

📌各位可以将公众号设为星标⭐

📌这样就不会错过每期的推荐内容啦~

📌这对我真的很重要！

![image](https://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2lAVT6CicZmYO3GGZre7KEwxiaouHrUbg3rQ0UUVhEI7eDxct12pq4ITqI98fcU1rsJXlHib3VF1n4ew/640?wx_fmt=png&from=appmsg "image")

📌1. 本平台分享的安全知识和工具信息源于公开资料及专业交流，仅供个人学习提升安全意识、了解防护手段，禁止用于任何违法活动，否则使用者自行承担法律后果。

📌2. 所分享内容及工具虽具普遍性，但因场景、版本、系统等因素，无法保证完全适用，使用者要自行承担知识运用不当、工具使用故障带来的损失。

📌3. 使用者在学习操作过程中务必遵守法规道德，面对有风险环节需谨慎预估后果、做好防护，若未谨慎操作引发信息泄露、设备损坏等不良后果，责任自负。

### **简介：**

ShadowRAT 是一款采用 Python 开发的 Windows 远程管理工具，能够生成有效载荷并对目标主机实施远程控制。其主要功能包括：**Shell 访问、摄像头与麦克风控制、文件上传、Windows 注册表持久化后门（支持创建与删除）、客户端信息显示、键盘记录模块（用于后渗透阶段）、地理位置定位以及持久化驻留**。

### **使用流程：**

### 1. 启动主控制界面

```
python   Shadow.py
```

根据菜单指引，选择目标 IP 地址及端口、生成攻击载荷或者启动监听服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZ9XvRj6K0aXibj8JbVQia0TOZ0OJibzPz9SJXUQ8RCBjEynUnUQt3pUpye730xZ3PHSCLLlR03o0wN4w/640?wx_fmt=png&from=appmsg)

### 2. 生成攻击载荷

通过交互式菜单，可以创建 Python 脚本或 EXE 可执行文件，并支持应用程序捆绑功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZ9XvRj6K0aXibj8JbVQia0TOZX6jd6O1IA67UiayZSDAyFSz8f3TuyqAYtTt54esmq0NZLrccjvDM28A/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZ9XvRj6K0aXibj8JbVQia0TOZvC1sgCsbMHiaaOKib6RD7tUhpKfCPaLjsfQjPHo2jH6MUwuOJLFhdTlw/640?wx_fmt=png&from=appmsg)

### 3. 开启监听服务

从菜单中选取监听功能，等待植入的载荷（客户端）发起连接。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZ9XvRj6K0aXibj8JbVQia0TOZ6LdAZmyPvOV72N2ibygH8Xz7B9Wmh2ONL3icnpo179deftPocrOO3VnQ/640?wx_fmt=png&from=appmsg)

### 4. 后期利用

根据需要，使用 `postexploits/` 目录下的工具（例如键盘记录器等）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZ9XvRj6K0aXibj8JbVQia0TOZI0ayI7YF8mTafZKOmFUicaStXucFOme8b2vC4KgAxZVrvvZ0bRvqkNg/640?wx_fmt=png&from=appmsg)

### **ShadowRAT 分析：**

该工具使用 Python 编写，并可编译为可执行程序。它会在受感染的主机上执行恶意操作。本质上，这是一款远程访问木马（RAT），旨在实现多种恶意功能，例如数据收集、信息窃取，并能够加载和执行用于后续渗透的插件与攻击载荷。

## 加密代码部分

encrypter.py 文件是加密模块，主要职责是提供加密功能并生成安全密钥。

下图中的脚本展示了一个 Fernet 对称加密密钥，用于加密和解密客户端与服务器之间的所有通信数据。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZ9XvRj6K0aXibj8JbVQia0TOZ47tr7woicHtt6a0yCwJ1hRSIm9JuTmTdHVpdw15SHqjXiaibmnsQP4F4A/640?wx_fmt=png&from=appmsg)

默认值

![](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZ9XvRj6K0aXibj8JbVQia0TOZ6c7fbDdeStMo8WpZJA5tvS566I5jcZJMgmsv167DomNNKnOlCiauZqw/640?wx_fmt=png&from=appmsg)

生成的临时 Payload

![](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZ9XvRj6K0aXibj8JbVQia0TOZsw981L4quiarEW2HdHUggta5V6q8Bk8kF26Nf7alCm9T37yPa43nYqQ/640?wx_fmt=png&from=appmsg)

Fernet 是一种基于 AES 的对称加密算法，提供了加密、解密和认证功能，确保传输的数据不会被中间人窃取或篡改。

## 客户端核心代码

payload.py 文件是客户端的核心代码，即部署到目标系统上的恶意软件载荷。其主要任务是建立与控制服务器的连接，并执行各种远程控制操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZ9XvRj6K0aXibj8JbVQia0TOZDNdbbSX1B5ZI0Pd7HwHHoPibLWibWb66qu0GxasickSj1fE4PPuhqPfbg/640?wx_fmt=png&from=appmsg)

## 生成 Payload 的代码

builder.py 文件是核心组件之一，主要负责构建 RAT（远程管理工具）的载荷。

* 读取 payloads/payload.py 作为模板
* 根据用户配置替换关键参数
* 生成可执行文件或 Python 脚本

由于它负责生成实际的恶意代码载荷，这些载荷将被部署到目标系统以建立远程控制连接。其设计允许用户轻松自定义载荷配置，包括服务器地址、端口、认证信息等，并且支持生成不同格式的载荷以适应不同的部署场景。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZ9XvRj6K0aXibj8JbVQia0TOZc9J4gdZlslfuOo1ViaS2siaktcJla3AoGoWasw8ciam9XMR1Ribtzdowiaw/640?wx_fmt=png&from=appmsg)

## 键盘记录器模块代码

Keylogger.py 文件是键盘记录器模块，属于后渗透工具，主要任务是捕获目标系统的按键输入并将其发送到控制服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/z3TOtprWtZ9XvRj6K0aXibj8JbVQia0TOZCwQ95iaicPWsCFLuic7JDP74YpYSE0THrhn0qA7NSRNC6KRVibgBFXGm6Q/640?wx_fmt=png&from=appmsg)

键盘记录器是一种典型的恶意软件组件，用于窃取用户的敏感信息（如密码、聊天内容、信用卡信息等）。

## 免责声明

关注微信公众号后台回复“**20260118** ”，即可获取项目下载地址

关注微信公众号后台回复**入群** 即可加入星夜AI安全交流群

## 圈子介绍

现任职于某头部网络安全企业攻防研究部，核心红队成员。2021-2023年间累计参与40+场国家级、行业级攻防实战演练，精通漏洞挖掘、红蓝对抗策略制定、恶意代码分析、内网横向渗透及应急响应等技术领域。在多次大型演练中，主导突破多个高防护目标网络，曾获“最佳攻击手”“突出贡献个人”等荣誉。

已产出的安全工具及成果包括：

* 多款主流杀软通杀工具（兼容卡巴斯基、诺顿、瑞星、360等终端防护）
* 内网穿透套件（适配多层路由、隔离网络环境的隐蔽流量转发）
* 权限维持工具集（含注册表、系统服务、进程隐藏等多维持久化方案）
* 哥斯拉/冰蝎定制化马生成器（绕过主流终端防护与EDR动态检测）
* 日志清理工具（实现Windows/Linux系统关键日志无痕删除与篡改）
* 浏览器凭证窃取工具（支持Chrome/Edge/Firefox等主流浏览器数据提取）
* 二开fscan内网扫描工具（增强指纹精度、弱口令爆破与结果标准化输出）
* 多款免杀Webshell集合（覆盖PHP/JSP/ASPX，过主流WAF与终端防护）
* 免杀360专属加载器（支持Shellcode内存执行，绕过360全系防护检测）

后续将不断更新到内部圈子中 欢迎加入圈子

![image](https://mmbiz.qpic.cn/mmbiz_jpg/SffY5ZO3R2kgwVm5QUg92kU37TmEiaiautOFv923ZvslsBG6iavLX5iagdbzmqgvQO1uT5H1HrzaO9h3mW2GCZDBPA/640?wx_fmt=jpeg&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=6 "image")

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txzs1NZE4Q/0?wx_fmt=png)

星夜AI安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/SffY5ZO3R2kDRUZoVyoQSFNmAaYwluEFTjXAgQILjvqxkG8dwdfCP3ia9vzvl09Te62lH6VjoGcL2txzs1NZE4Q/0?wx_fmt=png)

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