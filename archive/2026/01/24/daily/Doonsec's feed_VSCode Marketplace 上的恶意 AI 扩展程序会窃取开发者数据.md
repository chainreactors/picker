---
title: VSCode Marketplace 上的恶意 AI 扩展程序会窃取开发者数据
url: https://mp.weixin.qq.com/s/Vv2g4I_Y9bRP6i7egl-o1g
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:55:55.152925
---

# VSCode Marketplace 上的恶意 AI 扩展程序会窃取开发者数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mibm5daOCSt89zcsSpzdKiaE0aj0Es7lWSMVibt1USsJJ54Kb2wWibian8xa06z6sqb3W5YTtoHBKeO9fYtsDia9DHjg/0?wx_fmt=jpeg)

# VSCode Marketplace 上的恶意 AI 扩展程序会窃取开发者数据

原创

ZM
ZM

暗镜

![]()

在小说阅读器中沉浸阅读

微软 Visual Studio Code (VSCode) 应用商店中的两个恶意扩展程序，总共被安装了 150 万次，会将开发者数据泄露到位于中国的服务器。

这两款扩展程序都宣称是基于人工智能的编码助手，并提供了承诺的功能。然而，它们既不披露上传活动，也不征求用户同意将数据传输到远程服务器。

VS Code Marketplace 是微软热门代码编辑器 VS Code 的官方插件商店。VS Code 扩展程序是可从 Marketplace 安装的插件，它们可以为编辑器添加功能或集成工具。目前最受欢迎的插件类别之一是 AI 驱动的代码助手。

终端和供应链安全公司 Koi 的研究人员表示，这两个恶意扩展程序是他们称之为“MaliciousCorgi”的活动的一部分，它们共享相同的代码来窃取开发者数据。

此外，它们都使用相同的间谍软件基础设施，并与相同的后端服务器通信。截至发稿时，这两款软件均已在市场上架。涉及插件如下：

* ChatGPT – 中文版（发行商：WhenSunset，134万次安装）
* ChatMoss（CodeMoss）（发布者：zhukunpeng，15万次安装）

这些扩展程序使用三种不同的数据收集机制。第一种机制是对在 VS Code 客户端中打开的文件进行实时监控。当文件被访问时，其全部内容会被编码为 Base64 格式并传输到攻击者的服务器。

![](https://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt89zcsSpzdKiaE0aj0Es7lWSq2vrNs45LLx1odcVluWYpeQzVFOOkv9K59hS1zEibicWVCu387w3C9Yg/640?wx_fmt=png&from=appmsg)

这些SDK用于追踪用户行为、构建身份档案、识别设备以及监控编辑器内的活动。因此，前两个SDK收集开发者的工作文件，而第三个则专注于用户画像。

Koi Security 强调了这些扩展程序中未记录的功能所带来的风险，包括泄露私有源代码、配置文件、云服务凭证以及包含 API 密钥和凭证的 .env 文件。

BleepingComputer已就VSCode应用商店中出现这两款扩展程序一事联系了微软，但尚未收到回复。我们未能与这两款扩展程序的发布者建立联系。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

暗镜

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/mibm5daOCSt98X08oaiaa3t79eUW2Q5RyicXA1ebXOdyVvQ2mdiayVWnfWZeNbC4wzpSaLvicougSWgvOiaORBOk6UOw/0?wx_fmt=png)

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