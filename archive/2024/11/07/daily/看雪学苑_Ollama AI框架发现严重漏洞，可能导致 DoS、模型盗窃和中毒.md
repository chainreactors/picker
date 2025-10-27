---
title: Ollama AI框架发现严重漏洞，可能导致 DoS、模型盗窃和中毒
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458580536&idx=3&sn=07f91dc9d9d91ecd1ab33fbac3e076d5&chksm=b18dc6b286fa4fa41a3b684cde43528429157587b3b6285f0eea22c43c5ac73c742b29b405ba&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-07
fetch_date: 2025-10-06T19:18:40.251409
---

# Ollama AI框架发现严重漏洞，可能导致 DoS、模型盗窃和中毒

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EB8zq1LLJ3udfpumw6ZaFDHI7OLedNtzECDKKdicOgWKVCQBccLHWj6ias63V1leu63NSNu4sWZ0tA/0?wx_fmt=jpeg)

# Ollama AI框架发现严重漏洞，可能导致 DoS、模型盗窃和中毒

看雪学苑

看雪学苑

网络安全研究人员近日披露了Ollama人工智能（AI）框架中的六个安全漏洞，这些漏洞可能被恶意行为者利用，执行包括拒绝服务（DoS）、模型污染和模型盗窃在内的多种恶意行为。

“总的来说，这些漏洞允许攻击者通过单个HTTP请求执行一系列恶意行为，包括拒绝服务（DoS）攻击、模型污染、模型盗窃等。”Oligo Security研究员Avi Lumelsky在上周发布的报告中表示。

Ollama是一个开源应用程序，允许用户在Windows、Linux和macOS设备上本地部署和操作大型语言模型（LLM）。其在GitHub的项目仓库至今已被复制7600次。

以下是六个漏洞的简要描述：

- CVE-2024-39719（CVSS得分：7.5）- 攻击者可以利用/api/create端点确定服务器上文件的存在（已在0.1.47版本中修复）

- CVE-2024-39720（CVSS得分：8.2）- 一个越界读取漏洞，可能通过/api/create端点导致应用程序崩溃，从而产生DoS条件（已在0.1.46版本中修复）

- CVE-2024-39721（CVSS得分：7.5）- 当反复调用/api/create端点并传递文件“/dev/random”作为输入时，会导致资源耗尽，最终产生DoS（已在0.1.34版本中修复）

- CVE-2024-39722（CVSS得分：7.5）- api/push端点中的路径遍历漏洞，暴露了存在于服务器上的文件以及部署Ollama的整个目录结构（已在0.1.46版本中修复）

- 一个可能导致模型污染的漏洞，通过/api/pull端点从不受信任的源进行操作（无CVE标识符，未修补）

- 一个可能导致模型盗窃的漏洞，通过/api/push端点向不受信任的目标进行操作（无CVE标识符，未修补）

对于这两个未解决的漏洞，Ollama的维护者建议用户通过代理或Web应用防火墙过滤暴露给互联网的端点。

“这意味着，默认情况下，并非所有端点都应该暴露给互联网。”Lumelsky说。“这是一个危险的假设。并非每个人都意识到这一点，或者对Ollama的HTTP路由进行过滤。目前，这些端点可以通过Ollama的默认端口在每次部署中使用，没有任何隔离或文档支持。”

Oligo表示，他们发现了9831个运行Ollama的互联网面向实例，其中大部分位于中国、美国、德国、韩国、台湾、法国、英国、印度、新加坡和香港。四分之一的互联网面向服务器被认为容易受到已识别漏洞的影响。

这一发现发生在云安全公司Wiz披露影响Ollama的一个严重漏洞（CVE-2024-37032）四个月后，该漏洞可能被利用以实现远程代码执行。

“未经授权将Ollama暴露给互联网，等同于将Docker套接字暴露给公共互联网，因为它可以上传文件，并且具有模型拉取和推送能力（可能被攻击者滥用）。”Lumelsky指出。

资讯来源：thehackernews

转载请注明出处和本文链接

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8E9S6vNnUMRCOictT4PicNGMgHmsIkOvEno4oPVWrhwQCWNRTquZGs2ZLYic8IJTJBjxhWVoCa47V9Rw/640?wx_fmt=gif)

**球在看**

![](https://mmbiz.qpic.cn/mmbiz_gif/1UG7KPNHN8FxuBNT7e2ZEfQZgBuH2GkFjvK4tzErD5Q56kwaEL0N099icLfx1ZvVvqzcRG3oMtIXqUz5T9HYKicA/640?wx_fmt=gif)

戳“阅读原文”一起来充电吧！

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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