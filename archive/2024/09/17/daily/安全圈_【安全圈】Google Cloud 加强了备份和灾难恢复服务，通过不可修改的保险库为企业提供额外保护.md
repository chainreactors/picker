---
title: 【安全圈】Google Cloud 加强了备份和灾难恢复服务，通过不可修改的保险库为企业提供额外保护
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652064456&idx=2&sn=ead497b280dd4f8f819ba1b889e84c1b&chksm=f36e6688c419ef9e19f0b09212065b21e0a760172bd2af28169745b04e4a4162d91e0206e712&scene=58&subscene=0#rd
source: 安全圈
date: 2024-09-17
fetch_date: 2025-10-06T18:26:49.098648
---

# 【安全圈】Google Cloud 加强了备份和灾难恢复服务，通过不可修改的保险库为企业提供额外保护

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhxUicuxVj1KBBEJeZCfoiaFBgNgCib4TSibS0zfW2VhmJvXDVYFKNo7IcdPIqCIj4AWKGy0lxrmkvNibQ/0?wx_fmt=jpeg)

# 【安全圈】Google Cloud 加强了备份和灾难恢复服务，通过不可修改的保险库为企业提供额外保护

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=png&from=appmsg "微信图片_20230927171534.png")

**关键词**

数据安全

备份和数据恢复服务为企业的 Google Cloud 存储遇到攻击或其他重大问题时增加了一层额外的保护。

备份和恢复对于影响整个组织的 Google Cloud 账户的重大灾难性事件至关重要。拥有不可触及、逻辑隔离的版本为高风险数据增加了另一层保障。

9 月 10 日，Google Cloud 加强了其备份和灾难恢复服务，推出了一个不可修改的保险库。

目前该服务处于预览模式，但这家科技巨头宣布将在未来几个月内向美国部分地区、欧洲部分地区及台湾的 Google Cloud 客户开放。

# 新的备份和恢复服务是逻辑隔离的

备份保险库的特点在于其不可变性，意味着数据不能被修改，并且是永久性的，确保数据不能被删除。数据从备份和灾难恢复服务传输到备份保险库，并被安全存储以避免遭受网络攻击或严重错误。即使是在同一母公司内的用户也无法访问备份保险库。

管理员可以配置一个在该期间内保险库不可被修改的保留期限。

管理员可以配置无法修改文件库的保留期。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylhxUicuxVj1KBBEJeZCfoiaFBNDo6aeFrP3SMib8QABibiaibTHOTQudibeK36JQctB3UiaxiaGcjY0S9ibHRLQ/640?wx_fmt=png&from=appmsg)

设置备份文件库可能包括添加保留期。图片：谷歌云

使用 Google Compute Engine VM 的项目也可以将其数据存储在新保管库中。文件库未连接到源项目，可以基于 Compute Engine VM、VMware Engine VM、Oracle 数据库或 SQL Server 数据库。

备份 Compute Engine 虚拟机的过程可以在创建时就开始，并集成到虚拟机配置过程中。据 Google 称，它与 Google Cloud Identity and Access Management 策略保持一致，使设置既简化又更安全。

## 创建和管理 Google Compute Engine 虚拟机

管理员和应用程序开发人员可以手动检查计划的备份和还原作业，生成有关失败或跳过的作业的报告，并获取有关关键备份相关事件的警报。要使用 Compute Engine 虚拟机创建备份，管理员只需在 Google Cloud 中定义备份计划即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGylhxUicuxVj1KBBEJeZCfoiaFBvbMCPDasYmHoZiaD2eppETAz8YicEmRsicwnXcksA1pzNNT8icawBxfDyA/640?wx_fmt=jpeg&from=appmsg)

创建备份文件库后，定义其计划，然后您可以从中恢复 Compute Engine 虚拟机。图片：谷歌云

另一种选择是采用多云系统，而不是将 Google Cloud 备份加倍，这有其好处——正如今年早些时候因丢失 Google Cloud 帐户*和*备份而导致的 UniSuper 中断所见。

***END***

阅读推荐

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGyliauqZQlr0ElkJ2Ws2lkxkibjicbKBqZwLQOxpR2qCTWlaiaM5jCxqdicU8OIgjqQBficHFboNPXYSLA7LQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliauqZQlr0ElkJ2Ws2lkxkibj8Zw7CkjRgdkISTjGSylfpzEbSeU0MR1MyV4mNgsDVGYFpFRciaw820Q/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyliauqZQlr0ElkJ2Ws2lkxkibjUZHVxvj9xuwq2VUNY7LWzsU86Iq9WQVMCN792aE23UQIC6BtOzoNHA/640?wx_fmt=other)

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