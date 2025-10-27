---
title: “Kimsuky”黑客是如何确保其恶意软件精准投放到有效目标上的？
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247552840&idx=2&sn=0ba7acba5fe2107410d3b84f84d5ce49&chksm=e915df72de62566490acc95566ebbd781307b6167566de8de29832465f9abec7214edc88fbda&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-10-27
fetch_date: 2025-10-03T21:01:55.347196
---

# “Kimsuky”黑客是如何确保其恶意软件精准投放到有效目标上的？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jc5nocjE6nv7ckBvicBn80lJzM6GMQCkmxkiavuN8g2qM5DmsWH9FDSFoQ/0?wx_fmt=jpeg)

# “Kimsuky”黑客是如何确保其恶意软件精准投放到有效目标上的？

布加迪

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

朝鲜的“Kimsuky”威胁分子正在不遗余力地确保他们的恶意有效载荷仅由有效目标下载，而不是下载到安全研究人员的系统上。

据卡巴斯基近日发布的报告显示，这个威胁团伙自2022年初以来就一直在采用新颖的手法来过滤掉无效的下载请求，当时该团伙针对朝鲜半岛的多个目标发动了新的攻击活动。

Kimsuky实施的新保护措施非常有效，以至于卡巴斯基声称即使它在成功连接到了这伙威胁分子的指挥与控制（C2）服务器之后，也无法获取最终的有效载荷。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcI8XWCia7Es9POIoDpDCic3bO1R55vupB9V6slHia5CMmMuvrJZvbR4VYQ/640?wx_fmt=png)多阶段验证方案

卡巴斯基发现的攻击始于发送给朝鲜和韩国的政治家、外交官、大学教授和新闻记者的一封网络钓鱼电子邮件。

由于获取了含有攻击目标部分电子邮件地址的C2脚本，卡巴斯基能够整理出一份列有潜在目标的列表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcicZSqR5RzsBQNUqgibzoQiammbux6M2GFSTfFiaEDWsoKk4icKz3JiccW2Pg/640?wx_fmt=png)

图1. 卡巴斯基列出的潜在目标

电子邮件附有一个链接，该链接将受害者引到一台负责第一阶段的C2 服务器，该服务器在传递恶意文件之前检查并验证几个参数。如果访问者与攻击目标列表不匹配，就向他们提供无害的文件。

参数包括访问者的电子邮件地址、操作系统（Windows是有效操作系统）和第二阶段服务器投放的文件“[who].txt”。

与此同时，访问者的IP地址被转发给第二阶段C2服务器，作为后续的校验参数。

第一阶段C2服务器投放的文件含有一个恶意宏命令，该宏命令将受害者连接到第二阶段 C2服务器，获取下一阶段有效载荷，并使用mshta.exe进程运行它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jch94sQzTcCKaib9jy73FTnsZpm2Kib8skZtuJUFiciakTDXt80MtLsRl1WQ/640?wx_fmt=png)

图2. 发送给攻击目标的一些文件（图片来自卡巴斯基）

有效载荷是一个.HTA文件，该文件还创建自动执行的计划任务。其功能是检查ProgramFiles文件夹路径、AV名称、用户名、操作系统版本、MS Office版本和.NET框架版本等信息，从而详细分析受害者。

指纹结果存储在一个字符串（“chnome”）中，一份副本被发送到C2服务器，新的有效载荷被获取后，向持久性机制注册登记。

下一个有效载荷是一个VBS文件，该文件可以将受害者引到合法博客，或者如果受害者是有效攻击目标，将它们引到下一个有效载荷下载阶段。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcNPoBnaO8mGtYyjESLRCUNFXp8w5TwmgzUTKZMFkc0xRx7YXpbj07mA/640?wx_fmt=png)

图3. 在感染的每个步骤都执行C2检查（图片来自卡巴斯基）

卡巴斯基详细说明，值得关注的是，这个C2 脚本会根据受害者的IP地址生成一个博客地址。在计算受害者IP地址的MD5哈希之后，它会截断最后20个字符，并将其转换成博客地址。

脚本作者在这方面的意图是，为每个受害者运营一个专门的虚假博客，从而减小其恶意软件和基础架构被暴露的风险。

这时候，检查受害者的系统，查找是否存在异常的“chnome”字符串，该字符串被故意拼错，以便用作仍然不会引起怀疑的唯一验证器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcF7FI8XuqRZTI6ic1pibcia5OBkBlyp9hXyHgLHqhfyVlycQzePHxfWiczQ/640?wx_fmt=png)

图4. Kimsuky最新感染过程（图片来自卡巴斯基）

遗憾的是，卡巴斯基无法从这里继续获取下一阶段的有效载荷，因此这是不是最后一个阶段或是否有大多数验证步骤仍然不得而知。

Kimsuky是一个手法非常老练的威胁团伙，最近它部署自定义恶意软件并使用Google Chrome 扩展程序来窃取受害者的电子邮件。

卡巴斯基披露的活动表明了韩国黑客采用高明的手法来阻止分析，并大大加大跟踪难度。

参考及来源：https://www.bleepingcomputer.com/news/security/how-kimsuky-hackers-ensure-their-malware-only-reach-valid-targets/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcMibfTCgeBewib73uIc48HFMMk6picVRGj2pluKaPrgZr3SQH32Zicbkliaw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ibWLNWRTtqicga6NMc3IE5jcWBWSnYJOWuD4j22ol7Ko5CXulm1ibZYNSSlebbUPgUiaPL0tcY0W24rg/640?wx_fmt=png)

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