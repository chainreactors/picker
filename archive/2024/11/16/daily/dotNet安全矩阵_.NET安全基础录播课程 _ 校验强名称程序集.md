---
title: .NET安全基础录播课程 | 校验强名称程序集
url: https://mp.weixin.qq.com/s?__biz=MzUyOTc3NTQ5MA==&mid=2247496699&idx=1&sn=975974777349bf2388703fdfa955d464&chksm=fa595d16cd2ed40066a26f15136d4bed3c54fe359c013b048f7fd8475930918cb961610a7fd1&scene=58&subscene=0#rd
source: dotNet安全矩阵
date: 2024-11-16
fetch_date: 2025-10-06T19:18:32.965801
---

# .NET安全基础录播课程 | 校验强名称程序集

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibkLyrTvC4jgJB1c4faDLKIibZhEQ5BwXhS51mrjnsjqwib95Q0KCCqiariaoMbJoLBU6icIhEmLja4ryw/0?wx_fmt=jpeg)

# .NET安全基础录播课程 | 校验强名称程序集

专攻.NET安全的

dotNet安全矩阵

01

.NET强名称程序集

.NET强名称签名在渗透测试和持久化驻留中为恶意代码提供了一定的可信度、稳定性和隐蔽性，有助于绕过基于强名称的安全策略限制，实现更隐蔽的持久化和跨应用程序的载入。

02

基本介绍

PowerShell 提供了强大的反射功能，可以方便地加载和检查 .NET 程序集。以下是如何使用 PowerShell 来验证一个程序集是否具备强名称签名。

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1YibkLyrTvC4jgJB1c4faDLKIc7T7FY8TpLjbibbKa7qECovnFm8Dicn50YmBKBqKmQCgZsnQsDylJUCQ/640?wx_fmt=jpeg&from=appmsg)

03

内容详情

## 3.1 加载程序集

我们可以使用 [System.Reflection.Assembly]::LoadFile 方法来加载本地的 .NET 程序集文件。

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibkLyrTvC4jgJB1c4faDLKIAVwpQkLexHbIUs58MTcqicKibYnbZKQjsB5G8hFs1Z1bAZbZaiaX7oGtg/640?wx_fmt=png&from=appmsg)

## 3.2 获取强名称公钥

在加载程序集后，我们可以使用 GetName().GetPublicKey() 方法来获取程序集的公钥信息。强名称签名的程序集会包含一个有效的公钥

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1YibkLyrTvC4jgJB1c4faDLKIicchFgHIj2SmppPqDgHSN3rur7o1ZEmpkTB9BzLcalw6cdI1ialNCTJw/640?wx_fmt=png&from=appmsg)

综上，在 .NET 中，强名称签名是确保程序集唯一性和完整性的有效方法。通过 PowerShell 的反射功能，我们可以轻松检查程序集是否具有强名称签名，另外还有其他的方法可以校验，视频内容已经打包在星球，感兴趣的朋友可以加入观看学习。

04

精华回顾

## 4.1 打开项目选中签名

首先，在 **解决方案资源管理器** 中找到并打开项目，右键单击项目并选择 **属性**。进入属性页面后，切换到 **签名** 选项卡，然后勾选 **对程序集签名** 复选框。这将启用签名选项

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9hLVQib6uyt20YqibJgA887C7AsX4Hiaw2cFzQdtbuL9ZMvX4R6ia2vgNcibbNhJK7CVBciateSmhKvamw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

## 4.2 生成密钥文件

在 **选择强名称密钥文件** 下拉菜单中，可以选择现有的密钥文件，或单击 **<新建...>** 创建一个新的密钥文件。若选择新建密钥文件，系统会提示为密钥文件命名（例如 MyKey.snk），并可以选择设置密码以保护密钥文件

![](https://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y9hLVQib6uyt20YqibJgA887C07MQcbJTiaCfH6o9QW6yqvb7bMGyYZjXEBKaicEsMQBcJicRjctlNCfkA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

05

加入.NET安全基础入门

在这里，不是孤军奋战。我们特别设立了多个会员专属的内部星球陪伴群，加入的成员可以自由地提出疑问、分享见解、相互启发。我们相信，通过思想的碰撞与经验的交流，您将收获远超预期的宝贵财富。目前已有80+位朋友抢先预定，对.NET安全基础入门知识感兴趣的朋友们请尽快加入星球！

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y8iciasX3mOSk23icIyjXqibhQE8nibEBxSljtLrQMlf3kHrLPa0Y1icR5ibodAFbTEkdLia2tSib4W6VNdEsQ/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

为了回馈广大朋友们的热情与支持，****特别给朋友们准备早鸟价129元，**后期价格随着内容和质量的不断沉淀会适当提高******。这不仅是对您前瞻眼光的认可，更是为了让您以更优惠的价格，拥抱日益增长的知识价值。越早行动，优惠越多，福利满满！

![](https://mmbiz.qpic.cn/mmbiz_jpg/NO8Q9ApS1Y9hLVQib6uyt20YqibJgA887CI3ibHBz2nBDJI2ib15JmImYaoghGe6G7hPX5V1RtrykoqeCshNZabzkg/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

dotNet安全矩阵

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/NO8Q9ApS1Y8uc3CokHvGlrE00icPjW7AdTgEXkDtRT81Bbiaibx9gpMD6thAiawO5vz0icNlUzrzaOf6g044Tnzv3sQ/0?wx_fmt=png)

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