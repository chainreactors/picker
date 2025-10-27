---
title: SimpleHelp 多个严重漏洞可导致文件窃取、提权和RCE攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522089&idx=2&sn=46178e7445995e2b3a605d7fd3c37a93&chksm=ea94a643dde32f5500a0b9ba085731e8b6fcd21c96d42f6dbb5597cd5ac92f61c77907616c88&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-01-17
fetch_date: 2025-10-06T20:11:11.276197
---

# SimpleHelp 多个严重漏洞可导致文件窃取、提权和RCE攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTa8k8JniczoDc9uia6bqsVnKAjlSIU3XPtgqvvTYOtQbdmGYIBcicBzz0O88OTscbLxTvPQ3S6siamtA/0?wx_fmt=jpeg)

# SimpleHelp 多个严重漏洞可导致文件窃取、提权和RCE攻击

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**网络安全研究人员披露了位于 SimpleHelp 远程访问软件中的多个漏洞，可导致信息暴露、提权和远程代码执行等后果。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTa8k8JniczoDc9uia6bqsVnKoGkaOmD6gSkicia2MdIQQoNm5Mmzkpn9wBmlQBKQDufNZicGC4gZ6V51Q/640?wx_fmt=gif&from=appmsg)

Horizon3.ai公司的研究员 Naveen Sunkavally 发布技术报告提到，“这些漏洞易于逆向和利用”。这些漏洞如下：

* **CVE-2024-57727****：**该未认证路径遍历漏洞可导致攻击者从SimpleHelp 服务器下载任意文件，包括 serverconfig.xml 文件。该文件中包含 SimpleHelpAdmin 账户的哈希密码和其它本地技术账号。
* **CVE-2024-57728****：**该任意文件上传漏洞可导致具有 SimpleHelpAdmin 权限（或具有管理员权限的技术人员）的攻击者在 SimpleServer 主机上的任何位置上传任意文件，从而可能导致远程代码执行后果。
* **CVE-2024-57726****：**该提权漏洞可导致作为低权限技术人员获得访问权限，通过利用缺乏后端授权检查，提权至管理员。

在假设的理论攻击场景下，CVE-2024-57726和CVE-2024-57728可被恶意人员组合利用，提权至管理员用户并上传任意payload，控制 SimpleHelp服务器。

研究人员表示，鉴于这些漏洞的严重性及其易利用性，暂时将不会发布漏洞详情。漏洞已在2025年1月6日报送，并在1月8日和1月13日的SimpleHelp 5.3.9、5.4.0和5.5.8中修复。

鉴于威胁行动者们一直利用远程访问工具建立目标环境的持久远程访问权限，因此用户必须更加迅速地应用补丁。另外，SimpleHelp 建议用户修改 SimpleHelp 服务器的管理员密码、修改 Technician 账号的密码并限制能够访问SimpleHelp 服务器的Technician和管理员的IP登录地址。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[严重的 Aviatrix Controller RCE 漏洞已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522060&idx=2&sn=77945a6bc936ca2cbd6fe400e106a420&scene=21#wechat_redirect)

[GFI KerioControl 防火墙存在严重的RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522044&idx=1&sn=71bbcad32c9a0753d8385256ee5dad03&scene=21#wechat_redirect)

[联发科芯片集存在严重的RCE漏洞，影响数百万台设备](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522013&idx=1&sn=9f3081df1533336e5c1747667ca72291&scene=21#wechat_redirect)

[Apache MINA 存在严重的满分漏洞，可导致RCE](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521918&idx=1&sn=acf8324d4a36ec4e8d37b16375da9e75&scene=21#wechat_redirect)

[Apache Tomcat 漏洞导致服务器易受RCE攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521893&idx=1&sn=867f98595849107577a98fcaf043a177&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2025/01/critical-simplehelp-flaws-allow-file.htm

题图：Pexels License

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