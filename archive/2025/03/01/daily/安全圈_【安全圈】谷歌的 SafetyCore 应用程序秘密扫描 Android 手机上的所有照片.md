---
title: 【安全圈】谷歌的 SafetyCore 应用程序秘密扫描 Android 手机上的所有照片
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068200&idx=3&sn=596272b8756c71073cb53845353d58d5&chksm=f36e7528c419fc3e74462c23ae0b272af57886f4561ba4ccc75c4b93df22c036834de0f593da&scene=58&subscene=0#rd
source: 安全圈
date: 2025-03-01
fetch_date: 2025-10-06T21:59:08.351358
---

# 【安全圈】谷歌的 SafetyCore 应用程序秘密扫描 Android 手机上的所有照片

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylgaGvqZHtj96NR30ia8Wib3juuWgfWEFqDwEtPocy4UJNrz2JGFGzicT4g7tCfYiccoOpxsgk5yJcMmUw/0?wx_fmt=jpeg)

# 【安全圈】谷歌的 SafetyCore 应用程序秘密扫描 Android 手机上的所有照片

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

数据泄露

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgaGvqZHtj96NR30ia8Wib3jut5jvHl1T0mBzkV2yuQtYBfK7tSlv7ovkxl6h8h47dG94WfsydOoztw/640?wx_fmt=png&from=appmsg)

最近大量用户报告显示，谷歌的 Android System SafetyCore（一项旨在实现设备上内容扫描的系统服务）已自 2024 年 10 月起悄然安装在运行 Android 9 及更高版本的Android 设备上。

该应用程序的软件包名称为 com.google.android.safetycore，引发了人们对隐私和透明度的广泛担忧，批评者将其部署比作“后门”安装。

尽管谷歌声称 SafetyCore 在本地运行以对敏感内容进行分类而无需向外部传输数据，但其秘密推出重新引发了有关人工智能驱动的移动生态系统时代的用户同意和企业责任的争论。

SafetyCore 首次出现于 Google 2024 年 11 月系统更新的一部分，与 Play 服务和 Android 系统密钥验证器应用捆绑在一起。

## SafetyCore 应用程序：静默安装

与典型的应用程序安装不同，SafetyCore 没有图标、隐藏在系统进程中且占用约 2GB 的存储空间——这一细节在病毒式X（以前称为 Twitter）帖子中被重点提及，该帖子指责谷歌秘密启用照片库扫描功能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgaGvqZHtj96NR30ia8Wib3julRpnq4oEecCW6rgcRnwIOh1cTRXibKqe3VV2DdrxGtEKHfU1Oicyxh8A/640?wx_fmt=png&from=appmsg)

据《福布斯》报道，用户只有在前往“设置”>“应用程序”>“显示系统进程”后才会发现这款应用程序，它作为后台服务出现，具有互联网访问、存储和设备传感器的权限。

谷歌澄清说，SafetyCore 为 Google Messages 等应用程序提供“设备上的基础设施”，以实现敏感内容警告等功能，这些功能可以模糊潜在的露骨图像并在发送或接收之前提醒用户。

Google：“SafetyCore 提供设备上的基础设施，以安全且私密的方式执行分类，帮助用户检测不想要的内容。用户控制 SafetyCore，SafetyCore 仅在应用通过可选启用的功能请求特定内容时才对其进行分类。”

该服务使用机器学习 (ML)模型在本地对内容进行分类，维护端到端加密并避免基于云的数据传输。

SafetyCore 的架构与客户端扫描 (CSS) 一致，这是一种在本地而不是在远程服务器上处理数据的隐私保护技术。

然而，CSS 仍存在争议，因为它可能被滥用。安全专家警告称，此类系统可能会超出其原有的范围，使政府或企业能够监视不相关的内容。

尽管谷歌坚称 SafetyCore 仅限于“选择加入”功能，但其悄无声息的部署破坏了信任，因为用户并未被告知该服务的安装或功能。

值得注意的是，SafetyCore 独立于Android 现有的恶意软件扫描程序Google Play Protect 运行，而是专注于内容审核。

该服务需要 2GB 的 RAM，因此可与 2018 年后的大多数设备兼容。SafetyCore 的强烈反对与苹果 2022 年在 iMessage 中引发的通信安全争议如出一辙。

尽管苹果因默认启用照片扫描而受到批评，但它提供了清晰的文档和用户控制——与谷歌不透明的推出形成鲜明对比。

2024 年末，苹果的增强视觉搜索功能（将照片与地标数据库进行匹配）因未经明确同意而启动而受到批评。

这两起案件凸显了科技巨头的隐私承诺与实施实践之间的裂痕越来越大。

在 X 帖子发布后，谷歌修改了 SafetyCore 为“可选”的规定，并强调了其在打击诈骗和滥用方面的作用。该公司还强调了系统 APK 的二进制透明度，尽管这未能解决 ML 模型的不透明性问题。

来源：https://cybersecuritynews.com/googles-safetycore-app-secretly-scans/

***END***

阅读推荐

[【安全圈】央视揭露电诈新手段：“手机口”成诈骗分子的“隐形传声筒”](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068179&idx=1&sn=e269dac5b42a4c742cb4b652259c209e&scene=21#wechat_redirect)

[【安全圈】瑞典要求加密通信应用部署后门，Signal强烈反对](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068179&idx=2&sn=c968a8cc40580623d340d29c9f094df6&scene=21#wechat_redirect)

[【安全圈】DISA 透露，2024 年的数据泄露影响了超过 330 万人](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068179&idx=3&sn=fa7279a82fe96bdb54c1f935fe561090&scene=21#wechat_redirect)

[【安全圈】CVE-2025-20029：F5 BIG-IP系统发现命令注入漏洞，概念验证已发布](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652068179&idx=4&sn=39b4a77aebadbd2051b65b5c2aeac879&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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