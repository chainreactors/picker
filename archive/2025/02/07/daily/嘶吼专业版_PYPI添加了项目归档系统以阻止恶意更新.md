---
title: PYPI添加了项目归档系统以阻止恶意更新
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247581021&idx=2&sn=40a6f0da873c44dbb0408de5145244d0&chksm=e9146d67de63e471041fad7ab6bc2c565b09947e3bb53e3049db5bcaf709891415e4e851d953&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-02-07
fetch_date: 2025-10-06T20:38:02.354207
---

# PYPI添加了项目归档系统以阻止恶意更新

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29tWhHYX0kxIU9AZHdTUpKF1BibJSjRJHSowGBrhZhAFLRIbe53aEsmhbl7kqoTdgpIrgyawtYd3QA/0?wx_fmt=jpeg)

# PYPI添加了项目归档系统以阻止恶意更新

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

Python软件包索引（PYPI）宣布了“项目档案”的引入，该系统允许发布者归档其项目，并向用户表明预计不会更新。这些项目还将在PYPI上托管，用户仍然可以下载它们，但会看到有关维护状态的声明。

基于劫持开发人员帐户并将恶意更新推向广泛使用但废弃的项目是开源空间中的常见情况，所以这项新功能旨在提高供应链的安全性。

除了降低用户的风险外，它还通过确保与项目的生命周期状态进行沟通来减少用户的支持请求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29tWhHYX0kxIU9AZHdTUpKFTJ70tYtDHq8k8tgKvfiajzIBnNdIkAtvedberHL5wv2TvXtaZibhRd0Q/640?wx_fmt=png&from=appmsg)

关于存档项目的警告字样

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29tWhHYX0kxIU9AZHdTUpKFJkLyARLVKIG3PcFv49icJmiaba0q13Vtibiak1Y2e05licAdu3rsmnOIqLw/640?wx_fmt=png&from=appmsg)项目档案如何工作

根据PYPI新项目档案系统开发人员的详细博客表示，该功能提供了维护者控制的状态，该状态允许项目所有者将其项目标记为已存档，向用户发出信号，并表明将不会有进一步的更新。

PYPI建议维护者在归档项目之前发布最终版本，以包括对项目的详细信息和解释，尽管这不是强制性的。如果维护者选择恢复工作，可以在将来的任何时间都不构建其项目。

在引擎盖下，新系统使用最初用于项目隔离的生命周期模型，其中包括一个可以在不同状态之间过渡的状态机器。一旦项目所有者单击PYPI设置页面上的“存档项目”选项，该平台将自动更新其元数据以反映新状态。

PYPI新项目档案系统开发人员说，有计划添加更多的项目状态，例如“弃用”，“功能完整”和“未经许可”，使用户对项目状况有了更清晰的了解。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o29tWhHYX0kxIU9AZHdTUpKFnxJmHjf44wLQQwlHkIgLObkJuGfFD8yC4JpUVwKVic0icgdNRGPRxkOA/640?wx_fmt=jpeg&from=appmsg)

项目设置中的新选项

警告字样旨在通知开发人员，他们需要寻找积极维护的替代依赖性，而不是继续依靠过时的和潜在的不安全项目。除此之外，攻击者通常是针对废弃的包裹，接管未来的项目并通过更新几年后来注入恶意代码的情况。

在其他情况下，维护者选择在计划停止开发时删除项目，这会导致“复兴劫持”攻击之类的问题。从安全的角度来看，给那些维护者的归档选项要好得多。

最终，由于开源的性质，许多项目被放弃，但会使部分用户仍会猜测他们是否还在维护中。新系统应提高开源项目维护的透明度，删除猜测并提供有关项目状态的明确信号。

参考及来源：https://www.bleepingcomputer.com/news/security/pypi-adds-project-archiving-system-to-stop-malicious-updates/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29tWhHYX0kxIU9AZHdTUpKFeBia8ib2x4GDO8XlUfEVewoQERFTL3icKjG9AHl8d42jqznZfmqqJkibuw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29tWhHYX0kxIU9AZHdTUpKF7bt3JhibsDs6fKwJHyZa83Arib9jfic2etXZ7kxr8XDe7yNoicwpJngENw/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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