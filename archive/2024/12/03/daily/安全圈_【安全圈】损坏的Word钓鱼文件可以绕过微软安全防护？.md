---
title: 【安全圈】损坏的Word钓鱼文件可以绕过微软安全防护？
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066376&idx=4&sn=4a3ea073cc936b52c057d059b24874a6&chksm=f36e7e08c419f71e3705940b43548dd8d88c4f25f48199ab97fb4acf6dcf2e657fa9dd125b0b&scene=58&subscene=0#rd
source: 安全圈
date: 2024-12-03
fetch_date: 2025-10-06T19:40:11.914929
---

# 【安全圈】损坏的Word钓鱼文件可以绕过微软安全防护？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaSkfK0lmZ1JBgZtTaJ7JlhqcpUmu06Mvj4l5Wm0ibGnvYNnZWCvhrtEgRGhrghfiaYWIrTwibic3ETxQ/0?wx_fmt=jpeg)

# 【安全圈】损坏的Word钓鱼文件可以绕过微软安全防护？

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

网络钓鱼

一种新型的网络钓鱼攻击利用了微软Word文件恢复功能，通过发送损坏的Word文档作为电子邮件附件，使它们能够因为损坏状态而绕过安全软件，但仍然可以被应用程序恢复。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaSkfK0lmZ1JBgZtTaJ7JlhJVl6ZbnTHIQew0icl1VakEtMTiacHDOWSuZEGlq8c8bqomrVexbZ40Pg/640?wx_fmt=jpeg&from=appmsg)

威胁行为者不断寻找新的方法来绕过电子邮件安全软件，将他们的网络钓鱼邮件送达到目标收件箱。由恶意软件狩猎公司Any.Run发现的一个新的网络钓鱼活动，使用故意损坏的Word文档作为电子邮件附件，这些邮件伪装成来自工资单和人力资源部门。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaSkfK0lmZ1JBgZtTaJ7JlhGRPresC4y7Y22FJqpuSN0D4T3pVwhwxA7icgOBgjLSLIsRd5Ij07iaNA/640?wx_fmt=jpeg&from=appmsg)

这些附件使用了一系列主题，都围绕着员工福利和奖金，包括：

Annual\_Benefits\_&\_Bonus\_for\_[name]\_IyNURVhUTlVNUkFORE9NNDUjIw\_\_.docx

Annual\_Q4\_Benefits\_&\_Bonus\_for\_[name]\_IyNURVhUTlVNUkFORE9NNDUjIw\_\_.docx.bin

Benefits\_&\_Bonus\_for\_[name]\_IyNURVhUTlVNUkFORE9NNDUjIw\_\_.docx.bin

Due\_&\_Payment\_for\_[name]\_IyNURVhUTlVNUkFORE9NNDUjIw\_\_.docx.bin

Q4\_Benefits\_&\_Bonus\_for\_[name]\_IyNURVhUTlVNUkFORE9NNDUjIw\_\_.docx.bin

这些文档中都包含了Base64编码的字符串"IyNURVhUTlVNUkFORE9NNDUjIw," 解码后为"##TEXTNUMRANDOM45##"。

当打开附件时，Word会检测到文件已损坏，并提示文件中“发现无法读取的内容”，询问是否要恢复它。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaSkfK0lmZ1JBgZtTaJ7JlhdCv6ysK3NbmeNggH9ydNjqiclptfdJjtZKKcrly69yudBDtqRWJicNsg/640?wx_fmt=jpeg&from=appmsg)

这些网络钓鱼文档损坏的方式使得它们很容易被恢复，显示一个文档告诉目标扫描一个二维码以检索文档。如下所示，这些文档被标记为目标公司的徽标，例如下面展示的针对Daily Mail的活动。

扫描二维码将用户带到一个网络钓鱼网站，该网站伪装成微软登录页面，试图窃取用户的凭证。

虽然这次网络钓鱼攻击的最终目标并不新鲜，但其使用损坏的Word文档是一种新颖的规避检测手段。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliaSkfK0lmZ1JBgZtTaJ7Jlhdj423kGS5zdCo3URFADnRAicfzmrRVYbM0vsddHoSUPgJKMgVJYg2hg/640?wx_fmt=jpeg&from=appmsg)

"尽管这些文件在操作系统中运行成功，但由于未能为它们的文件类型应用适当的程序，它们仍然未被大多数安全解决方案检测到，"Any.Run解释道“它们被上传到VirusTotal，但所有防病毒解决方案都返回了'clean'或'Item Not Found'，因为它们无法正确分析文件。”

这些附件在实现目标方面相当成功。从与BleepingComputer分享的附件和在这次活动中使用的附件来看，几乎所有的在VirusTotal上的检测结果都是零[1, 2, 3, 4]，只有一些[1]被2个供应商检测到。

同时，这也可能是因为文档中没有添加恶意代码，它们只是显示了一个二维码。保护自己不受这种网络钓鱼攻击的一般规则仍然适用。如果你收到了一个未知发件人的电子邮件，特别是如果它包含附件，应立即删除或在打开前与网络管理员确认。

参考来源：https://www.bleepingcomputer.com/news/security/novel-phising-campaign-uses-corrupted-word-documents-to-evade-security/

***END***

阅读推荐

[【安全圈】专向老人下手！老人机也能中病毒？](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066356&idx=1&sn=5dedf9107cc762f32a4ff2a712b10a41&scene=21#wechat_redirect)

[【安全圈】合肥警方破获一起游戏外挂案件，抓获4名嫌疑人！](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066356&idx=2&sn=c79391a4fbfcb3b186dd72801c443eaa&scene=21#wechat_redirect)

[【安全圈】安全公司曝黑客针对开源游戏引擎 Godot 分发 GodLoader 恶意脚本](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652066356&idx=3&sn=e3124c5e2c25a853da32a4cb281ef63c&scene=21#wechat_redirect)

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

阅读原文

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