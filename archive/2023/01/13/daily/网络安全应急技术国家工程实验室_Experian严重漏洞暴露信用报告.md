---
title: Experian严重漏洞暴露信用报告
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247533840&idx=3&sn=a795c2eda4ac337c0c119d01ffb83886&chksm=fa93f3d1cde47ac7f6c4dbf8832aa166b038e79d6ce1dd32b81208e4c3fe32865ca4bd72bfdf&scene=58&subscene=0#rd
source: 网络安全应急技术国家工程实验室
date: 2023-01-13
fetch_date: 2025-10-04T03:45:51.697648
---

# Experian严重漏洞暴露信用报告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176libDOZAlbjUNl2LekvSXPIa8RPPqzBSY7ZTttCaDxJVHyVBYgsyqL6AGFoSjmJEYT7CH3oycADQNw/0?wx_fmt=jpeg)

# Experian严重漏洞暴露信用报告

网络安全应急技术国家工程中心

近日，有记者在消费者和企业信用报告领域的全球领导者 Experian 的官方网站上披露了一个安全漏洞的惊人细节，该漏洞正被身份盗窃诈骗者利用，而 Experian 对此一无所知。

到 2022 年底，Experian 网站允许用户绕过这些 MCQ，在输入姓名、出生日期、地址和社会安全号码后直接访问信用报告。

乌克兰安全研究员 Jenya Kushnir 向记者透露了这个漏洞，身份窃贼正在利用这个漏洞，因为他们可以通过专门用于此目的的 Telegram 聊天频道获取被盗身份。根据 Kushnir 的调查结果，网络犯罪分子可以通过在身份验证过程中的某个时刻编辑浏览器 URL 栏中的地址来诱骗 Experian 网站允许他们访问任何用户的信用报告。

访客必须提供他们的姓名、出生日期、地址和社会安全号码。当 Brian Krebs 提供此信息时，他被重定向到 Experian.com 以完成身份验证。那是 MCQ 出现的阶段。

然而，Kushnir 指出，在这个阶段，如果他将 URL 的最后一部分从“/acr/oow/”更改为“/acr/report”，他的信用报告就会出现。当他被重定向到 Experian 网站时，它没有显示 MCQ，而是显示了 URL“/acr/OcwError”，表明它没有足够的数据来验证他的身份。接下来，该网站为 Krebs 提供了三个选项：

发送带有身份验证文件的信用报告电子邮件

致电益博睿

在网站上传身份证明

当 Krebs 按照 Kushnir 告诉他的那样将 URL 更改为“/acr/report”时，即使 Experian 无法验证他的身份，他也会看到他的完整信用档案。

![](https://mmbiz.qpic.cn/mmbiz_png/QmbJGbR2j6wy5RFdses5QDSAfic2eV3X4JOWib2ChhWGW7p3qLBDBBFg7bdsJ9WjoGR8ibkjb89fZybMSqRibRfNxQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

Brian Krebs于 2022 年 12 月 23 日与 Experian分享了他的发现，该公司的公关团队于 2022 年 12 月 27 日确认了该通知。在此期间，该漏洞得到了修补。然而，目前还不清楚这个问题被身份窃贼知道并被利用了多久。

**Experian 安全和数据泄露**

Experian 是世界领先的信用报告机构之一，收集和汇总超过 10 亿人和企业的信息。它可以访问 2.35 亿美国个人消费者以及 2500 万美国企业的数据，使其成为金融机构、雇主、房东等的强大工具。

Experian 也因大规模数据泄露和严重安全漏洞而闻名。几年前，一个这样的漏洞允许攻击者获得客户的账户访问权限和他们的信用冻结 PIN 码。

2020 年 8 月，据透露，Experian 遭受了大规模数据泄露，其中 2200 万客户的个人详细信息被盗。在另一起事件中，Experian 巴西分会 Serasa Experian 再次遭受数据泄露，导致 2.23 亿人的数据在黑客论坛上泄露。

原文来源：E安全

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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