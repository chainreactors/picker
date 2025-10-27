---
title: ChatGPT对OpenSSH公私钥登录流程的简述
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247486508&idx=1&sn=bb75d3f9f0890316e0c25ee539740b76&chksm=fab2cf13cdc546053593e4cf002178ede817e548d82cbfbb51ee20533a67a33c930cebed6d87&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2023-02-23
fetch_date: 2025-10-04T07:51:37.035026
---

# ChatGPT对OpenSSH公私钥登录流程的简述

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPNTByUkjsNWcgXt9rrLhwH4Y1xDhqj5iapWcaqQ5tFKPAPsiawz10XBnLIjc6mLufG84faLrvg9cvsg/0?wx_fmt=jpeg)

# ChatGPT对OpenSSH公私钥登录流程的简述

原创

沈沉舟

青衣十三楼飞花堂

我没看过OpenSSH源码，也不了解公私钥登录流程，索性让ChatGPT忽悠忽悠我，粗看了两眼，答得不算离谱，有一定可信度。

Q: scz

OpenSSH公私钥登录认证时，大致流程是什么？

A: ChatGPT

1. 用户生成一对公私钥，私钥存储在本地计算机上，公钥复制到远程服务器上
2. 上传公钥到服务器，将公钥复制~/.ssh/authorized\_keys
3. SSH客户端连接服务器，客户端将本地公钥发送到服务器
4. 服务器收到客户端发送的公钥，与authorized\_keys中的公钥列表进行匹配
5. 若服务器成功验证了公钥，会用该公钥加密一个随机数，并将其发送给客户端
6. 客户端收到服务器发送的加密随机数，用本地私钥对其解密
7. 客户端和服务器拥有同一随机数，它们用之作种子，利用密钥协商算法生成对称加密密钥
8. 客户端和服务器用前述对称加密密钥进行后续通信
9. 公私钥只用于登录认证阶段，一旦认证通过，客户端和服务器之间的通信使用对称加密通信

Q: scz

在此过程中，signature algorithm 体现在哪里？

A: ChatGPT

客户端向服务器发送本地公钥，并使用私钥生成一个数字签名(signature)。服务器收到客户端发送的公钥和数字签名，与authorized\_keys中的公钥进行匹配，并校验数字签名，若果验证通过，认为客户端合法，可以继续。

Q: scz

假设公私钥保持不变，新版OpenSSH服务端需要"PubkeyAcceptedAlgorithms +ssh-rsa"，否则某些旧版客户端公私钥登录失败，某些新版客户端公私钥登录成功，请从算法角度简述造成这种现象的原因

A: ChatGPT

造成这种现象的原因是OpenSSH公私钥登录认证过程中涉及的算法版本升级导致的不兼容。OpenSSH公私钥登录认证涉及到多种算法，包括加密算法、HASH算法和签名算法等，这些算法可能随时间推移而发生改变，例如在某个版本的OpenSSH中，可能使用SHA-1来计算数字签名，但在新版中，可能改为更安全的算法，例如SHA-256。为了确保兼容性，需要使用相同的算法，通过适当的参数配置来确保新旧版本之间可以正常通信。

Q: scz

Linux命令行ssh公私钥登录时，如何指定用哪种 signature algorithm

A: ChatGPT

ssh -i <private\_key> -o HostKeyAlgorithms=<signature algorithm> <user>@<host>

可将参数添加到 ~/.ssh/config 中，可以避免每次都输入相同的参数。

Q: scz

你不是一般的牛逼

A: ChatGPT

感谢夸奖！我只是一个机器人。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

青衣十三楼飞花堂

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

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