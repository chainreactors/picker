---
title: Ollama AI框架被曝严重漏洞，可导致DoS、模型盗窃和中毒
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513033&idx=2&sn=ad9b7aed64a0dd5dbae5e6a488f7cdca&chksm=ebfaf4e9dc8d7dffafb2c9ad7e832bcfe9124a1a686531b7ba2c531a7eb307afc7ea1d614e93&scene=58&subscene=0#rd
source: 安全内参
date: 2024-11-09
fetch_date: 2025-10-06T19:18:15.647108
---

# Ollama AI框架被曝严重漏洞，可导致DoS、模型盗窃和中毒

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tsMXaJGYR3xiaUuQsbw1AwSLL5AviaSG1UYKNaNzbTHlq5ATdkBbSgdacrgZQnias2ZEbTgWuCtiaiaDA/0?wx_fmt=jpeg)

# Ollama AI框架被曝严重漏洞，可导致DoS、模型盗窃和中毒

安全内参

**关注我们**

**带你读懂网络安全**

**共发现6个漏洞。**

网络安全研究人员近日披露了Ollama人工智能（AI）框架中的六个安全漏洞，这些漏洞可能被恶意行为者利用，执行包括拒绝服务（DoS）、模型污染和模型盗窃在内的多种恶意行为。

“总的来说，这些漏洞允许攻击者通过单个HTTP请求执行一系列恶意行为，包括拒绝服务（DoS）攻击、模型污染、模型盗窃等。”Oligo Security研究员Avi Lumelsky在上周发布的报告中表示。

Ollama是一个开源应用程序，允许用户在Windows、Linux和macOS设备上本地部署和操作大型语言模型（LLM）。其在GitHub的项目仓库至今已被复制7600次。

以下是六个漏洞的简要描述：

* - CVE-2024-39719（CVSS得分：7.5）- 攻击者可以利用/api/create端点确定服务器上文件的存在（已在0.1.47版本中修复）
* - CVE-2024-39720（CVSS得分：8.2）- 一个越界读取漏洞，可能通过/api/create端点导致应用程序崩溃，从而产生DoS条件（已在0.1.46版本中修复）
* - CVE-2024-39721（CVSS得分：7.5）- 当反复调用/api/create端点并传递文件“/dev/random”作为输入时，会导致资源耗尽，最终产生DoS（已在0.1.34版本中修复）
* - CVE-2024-39722（CVSS得分：7.5）- api/push端点中的路径遍历漏洞，暴露了存在于服务器上的文件以及部署Ollama的整个目录结构（已在0.1.46版本中修复）
* - 一个可能导致模型污染的漏洞，通过/api/pull端点从不受信任的源进行操作（无CVE标识符，未修补）
* - 一个可能导致模型盗窃的漏洞，通过/api/push端点向不受信任的目标进行操作（无CVE标识符，未修补）

对于这两个未解决的漏洞，Ollama的维护者建议用户通过代理或Web应用防火墙过滤暴露给互联网的端点。

“这意味着，默认情况下，并非所有端点都应该暴露给互联网。”Lumelsky说。“这是一个危险的假设。并非每个人都意识到这一点，或者对Ollama的HTTP路由进行过滤。目前，这些端点可以通过Ollama的默认端口在每次部署中使用，没有任何隔离或文档支持。”

Oligo表示，他们发现了9831个运行Ollama的互联网面向实例，其中大部分位于中国、美国、德国、韩国、台湾、法国、英国、印度、新加坡和香港。四分之一的互联网面向服务器被认为容易受到已识别漏洞的影响。

这一发现发生在云安全公司Wiz披露影响Ollama的一个严重漏洞（CVE-2024-37032）四个月后，该漏洞可能被利用以实现远程代码执行。

“未经授权将Ollama暴露给互联网，等同于将Docker套接字暴露给公共互联网，因为它可以上传文件，并且具有模型拉取和推送能力（可能被攻击者滥用）。”Lumelsky指出。

资讯来源：thehackernews

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：看雪学苑

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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