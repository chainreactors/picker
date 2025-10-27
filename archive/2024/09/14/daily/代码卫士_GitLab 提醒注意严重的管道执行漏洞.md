---
title: GitLab 提醒注意严重的管道执行漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520799&idx=1&sn=2e34312c9e5c05291452bf69189cd8b5&chksm=ea94a375dde32a6355837cb4f23e5933d2192469425e3f2054204b18a8780163e090447f172b&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-14
fetch_date: 2025-10-06T18:27:38.645503
---

# GitLab 提醒注意严重的管道执行漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTfLbX6nWbEgIoIYUH9hASkLsRbM9ERWwsnuPuX2ib1LwJpgbbRlryQibXnGf4yaR5OBTCKLcSHuWEw/0?wx_fmt=jpeg)

# GitLab 提醒注意严重的管道执行漏洞

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**GitLab 发布重要更新，修复多个漏洞，其中最严重的CVE-2024-6678可导致攻击者在某些条件下以任意用户身份触发管道。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTfLbX6nWbEgIoIYUH9hASkpW8yd6zhQcQKibRlPbNL8t4AcQ2fRYm25n5OYvHcVQJenldRiageZPpA/640?wx_fmt=png&from=appmsg)

新发布的版本17.3.2、17.2.5和17.1.7 同时适用于GitLab 社区版 (CE) 和企业版 (EE)。GitLab 在本次双月安全更新中共修复18个安全问题。CVE-2024-6678的CVSS评分为9.9，可导致攻击者以停止操作任务的所有人身份执行环境停止操作。

该漏洞的严重性在于它可能导致远程利用、缺少用户交互以及利用权限要求低。GitLab 提醒称该漏洞影响 CE/EE 8.14至17.1.7版本、早于17.2.5的17.2版本以及17.3至17.3.2之前的版本。GitLab 提到，“我们强烈建议所有运行受影响版本的用户尽快升级至最新版本。”

GitLab 管道是用于构建、测试和部署代码的自动工作流，是 GitLab CI/CD 系统的一部分。这些管道旨在通过自动化执行重复性任务并确保代码库中的更改经过测试和部署的方式，疏通软件开发流程。GitLab 最近几个月多次修复多个任意管道执行漏洞，包括在2024年7月，修复CVE-2024-6385；2024年6月修复CVE-2024-5655；以及在2023年9月修复CVE-2023-5009，它们均为严重级别。

GitLab 还在安全公告中列出了CVSS评分为6.7到8.5之间的四个高危漏洞，它们可导致攻击者破坏服务、执行越权命令或攻陷敏感资源。这些漏洞的简述如下：

* **CVE-2024-8640****：**由于输入过滤不当，攻击者可通过YAML配置将命令注入联网的Cube 服务器，从而可能攻陷数据完整性，影响 GitLab EE 16.11及后续版本。
* **CVE-2024-8635****：**攻击者可构造自定义 Maven Dependency Proxy URL，利用SSRF 漏洞，向内部资源提出请求，攻陷内部基础设施。该漏洞影响GitLab EE 16.8及后续版本。
* **CVE-2024-8124****：**攻击者可发送较大的 “glm\_source” 参数，占满系统并使其不可用，触发DoS 攻击。该漏洞影响 GitLab CE/EE 16.4及后续版本。
* **CVE-2024-8641****：**攻击者可利用CI\_JOB\_TOKEN 获得对受害者 GitLab 会话令牌的访问权限，劫持会话。该漏洞影响 GitLab CE/EE 13.7及后续版本。

用户可查看 GitLab 的官方下载门户，查看更多的更新指南、源代码和程序包。另外可获取最新的 GitLab Runner 包。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[GitLab 又爆新的CI/CD管道接管漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520065&idx=2&sn=2dfd0b72bc28e69fa94a19fdb4828ace&chksm=ea94be2bdde3373d1294a08d90375f52d1f101e29fb038fd092aa8b03a83c90099f9a89ab166&scene=21#wechat_redirect)

[GitLab 严重漏洞导致攻击者以任意用户身份运行管道](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519913&idx=1&sn=f485e4897bd8f134b2685e61ec98b8ae&chksm=ea94bfc3dde336d543b1cf68c7773d682b657af8bfc3a495d9433d47d2b67144447e9a9c5422&scene=21#wechat_redirect)

[GitLab 高危漏洞可导致账号遭接管](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519584&idx=1&sn=8ca7ba7442a6234b2f5910147094c5bb&chksm=ea94bc0adde3351ccee634db2e180e9bc4d66ff43d4aa7e08ca703c79df1444bcf27d1b960de&scene=21#wechat_redirect)

[GitLab 提醒注意严重的零点击账户劫持漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518669&idx=1&sn=e9e78678e6c35cd6c0c37b638d5a988c&chksm=ea94b8a7dde331b16bdf8306a2700a04ea240bc5baa204b72ab3c9664a58b77c6fc92b1841f4&scene=21#wechat_redirect)

[GitLab 督促用户安装安全更新，修复严重的管道漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517701&idx=2&sn=9efeb89e9c34a3dcb192e347897ea5d3&chksm=ea94b76fdde33e79439751b5f121c7f1c6903963de1ec1e650ed19876271b10ebc9271391861&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/gitlab-warns-of-critical-pipeline-execution-vulnerability/

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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