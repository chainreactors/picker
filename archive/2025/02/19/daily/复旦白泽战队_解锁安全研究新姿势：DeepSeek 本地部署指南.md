---
title: 解锁安全研究新姿势：DeepSeek 本地部署指南
url: https://mp.weixin.qq.com/s?__biz=MzU4NzUxOTI0OQ==&mid=2247492941&idx=1&sn=476fc818f0028dad0a4bff3c74c59c09&chksm=fde86133ca9fe825e7b72423b6c538f0e2ac47d59a591854a3719f3d3b29f0c18e1347588af4&scene=58&subscene=0#rd
source: 复旦白泽战队
date: 2025-02-19
fetch_date: 2025-10-06T20:47:43.776993
---

# 解锁安全研究新姿势：DeepSeek 本地部署指南

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/RyyHWbbqW87xic42f0vGy5fpYtXIPjeU70y88tIX55VTicAnzqCgxew3FCw4V6lwJ5Kfb5vASAWMP1ic2C71jjM1A/0?wx_fmt=jpeg)

# 解锁安全研究新姿势：DeepSeek 本地部署指南

原创

黄宗安

复旦白泽战队

解锁安全研究新姿势：

DeepSeek 本地部署指南

**引言**

    想象一下，在系统安全研究的世界里“有一位全能助手”，它能够自动化地分析代码，快速识别潜在的漏洞，甚至在复杂的程序分析中为你提供清晰的专业建议。这就是大模型在系统安全领域的魅力！然而，这位“助手”如果住在云端，可能会因为网络延迟而“行动迟缓”，或者因为数据隐私问题而“束手束脚”。有没有办法让它直接搬到你的电脑上，随时待命呢？

    答案是：当然可以！DeepSeek就是这样一位可以“常驻本地”的超级助手。作为一款功能强大且易于使用的开源大模型，它不仅能完全运行在你的设备上，还能为你提供更灵活、更安全的系统安全研究支持。想知道如何快速拥有这位本地“超级助手”吗？别急，本文将带你一步步完成DeepSeek的本地部署，助你轻松开启大模型赋能的安全研究之旅！

**1、Ollama框架安装**

1.1 打开Ollama官网

https://ollama.com/download

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87xic42f0vGy5fpYtXIPjeU7ibqDVhRb1caLkE88BLdwZDVUoBDqLYiaq5p0UI5TFHZlicEwwMI4G4q6w/640?wx_fmt=png&from=appmsg)

1.2 下载完成后运行安装程序

点击Install安装Ollama

安装完成后进行下一步

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87xic42f0vGy5fpYtXIPjeU7pKKTnl0wMnAdch2GVSdhP74FQxYHO44oQwlAXgalicTMIFY1X7BicR9A/640?wx_fmt=png&from=appmsg)

**2、Deepseek模型下载**

2.1 回到Ollama官网

点击上方的Models

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87xic42f0vGy5fpYtXIPjeU7bz479ynP2HtohazOAB7ezmviayksBqOyePIac6OlhlmTBpMf6xfY8Ag/640?wx_fmt=png&from=appmsg)

2.2 选择deepseek模型

这里选择deepseek-r1

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87xic42f0vGy5fpYtXIPjeU7XGdaeFLxYHRBrahx5Hic0jfatrlV7QRd0oUIXXLicNy48fvnwzxxic3NA/640?wx_fmt=png&from=appmsg)

2.3 选择合适版本

版本根据电脑配置来选，这里选择下载的是7b版本，大家可根据情况自行选择

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87xic42f0vGy5fpYtXIPjeU7kFyKOFGoDzv0MXUHiblDicnsLLImTVUJ2wNMNo1N3RDM2SlxWpExjfOw/640?wx_fmt=png&from=appmsg)

2.4 Ollama安装模型

在网页复制安装命令

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87xic42f0vGy5fpYtXIPjeU7hCt2XML0ogG5lEIvhEh6xvzKBXGiciajpdyrUHzrCoMDfMtt5SK1QvVw/640?wx_fmt=png&from=appmsg)

2.5 Ollama运行模型

打开终端运行上述命令安装模型

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87xic42f0vGy5fpYtXIPjeU7bYYPMBs7m2JFDKiaCKcsrOgfguSKlcPP0UtEHeatiaeIicO6jsOg6PfEg/640?wx_fmt=png&from=appmsg)

**3、Chatbox AI安装**

Chatbox AI客户端可以用于构建与本地模型的聊天窗口

3.1 打开Chatbox AI官网安装客户端

https://chatboxai.app/zh

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87xic42f0vGy5fpYtXIPjeU73wmRpb2M79hyyWQlk2srqicegOFE3H5uEUmoXdOcS724Hz3CDK4r2rw/640?wx_fmt=png&from=appmsg)

3.2 启动安装程序

选取安装位置

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87xic42f0vGy5fpYtXIPjeU7pJdNbXVRbQ9N2RdIVd6rasojNWGJFzQ2amCpic5n1tq7zpV84iaN2bhQ/640?wx_fmt=png&from=appmsg)

3.3 完成安装

点击完成安装，并启动应用

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87xic42f0vGy5fpYtXIPjeU7jGLvOFnUPQ3ViajncBNZ9O7MicFlL1NoCj0oscyNuXZ6ib5JFNYBHy7hA/640?wx_fmt=png&from=appmsg)

3.4 打开Chatbox AI客户端

选择【使用自己的API Key或本地模型】

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87xic42f0vGy5fpYtXIPjeU73WHjTp15Y1Sd6SOn0mHFv5mjIK1x2ejbVzoIdLTic4Pjkibped48O5yg/640?wx_fmt=png&from=appmsg)

3.5 配置Ollama API Key

配置Ollama API Key

选择deepseek-r1:7b对话模型

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87xic42f0vGy5fpYtXIPjeU7Bty2iabuz46Q4WLtE2iaghtJZuibVOxNbmB4Mtqalz4BgQ7unqibRXLH4A/640?wx_fmt=png&from=appmsg)

3.6 与本地大模型对话

询问本地大模型协助安全研究问题

![](https://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW87xic42f0vGy5fpYtXIPjeU7kZAWmnoSAoCqFiat6SNLX7vx3w5AMrh60b8Rp4P7YL7e0FosBaWZoZA/640?wx_fmt=png&from=appmsg)

**结束语**

以上就是 DeepSeek本地部署的详细步骤。希望这篇指南能帮助你顺利完成 DeepSeek的本地部署，开启系统安全研究新篇章！

供稿：黄宗安

排版：黄宗安

责编：邬梦莹

审核：戴嘉润、张琬琪、洪赓

复旦白泽战队

一个有情怀的安全团队

还没有关注复旦白泽战队？

公众号、知乎、微博搜索：复旦白泽战队也能找到我们哦~

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

复旦白泽战队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RyyHWbbqW86lQ9Nfe0UACZ6twyichExoLzB1ROQN9kuxmTtDTibXQLqx2OicgibmhHOC0hwn5ia2k7405VvdZDTjLzA/0?wx_fmt=png)

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