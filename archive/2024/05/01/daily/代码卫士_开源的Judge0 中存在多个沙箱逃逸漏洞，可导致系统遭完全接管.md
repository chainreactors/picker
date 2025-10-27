---
title: 开源的Judge0 中存在多个沙箱逃逸漏洞，可导致系统遭完全接管
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519400&idx=2&sn=e79b7a5da52b70449d7f2d6c99c8cab2&chksm=ea94bdc2dde334d48c4fc1fc698133c71550c937353091502e020643ff271de8656b39d98e84&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-05-01
fetch_date: 2025-10-06T17:18:54.200140
---

# 开源的Judge0 中存在多个沙箱逃逸漏洞，可导致系统遭完全接管

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTWabr5o4ic05fn5PD4RibKovIyOUNfUV3miaakbtVN0cYeqmic4xic5tpj1LV8FzH7CZzYYQroGnzkJUw/0?wx_fmt=jpeg)

# 开源的Judge0 中存在多个沙箱逃逸漏洞，可导致系统遭完全接管

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**开源的在线代码执行系统中存在三个严重漏洞，可用于在目标系统上执行代码。**

澳大利亚网络安全公司 Tanto 在报告中提到，这三个漏洞都属于严重级别，可导致“具有充分访问权限的对手执行沙箱逃逸并获得主机机器的 root 权限。”

Judge0维护人员表示，该项目是“健壮、可扩展和开源的在线代码执行系统”，可用于构建需要在线代码执行特性的应用程序如候选评估、在线学习和在线代码编辑器和IDE。

Judge0网站提到，它服务23个客户如 AIgoDaily、CodeChum和PYnative等。迄今为止该项目在GitHub上已被fork 412次。

这些漏洞由 Daniel Cooper 在2024年3月发现和报告，如下：

* CVE-2024-28185（CVSS评分10）：该应用程序并不负责位于沙箱目录中的符号链接，它可被用于写入任意文件并在沙箱外获得代码执行权限。
* CVE-2024-28189（CVSS评分10）：对CVE-2024-28185的补丁绕过，攻击者可创建沙箱外文件的符号链接，在沙箱外的任意文件上运行 chown。
* CVE-2024-29021（CVSS评分9.1）：Judge0的默认配置可导致服务易受经由SSRF的沙箱逃逸，从而使对Judge0 API 具有充分访问权限的攻击者以目标机器上的root身份获得非沙箱的代码执行权限。

该问题的根因在于名为 “isolate\_job.rb”的Ruby脚本，它负责设立沙箱、运行代码并存储执行结果。具体而言，它在设立 bash 脚本执行基于提交语言的程序之前，创建符号链接，以便在未沙箱的系统上写入任意文件。攻击者可利用该漏洞在系统上覆写脚本，在沙箱外以及运行提交任务的 Docker 容器上获得代码执行权限。另外，攻击者可提升 Docker 容器外的权限，“导致攻击者增加Linux主机文件系统，写文件获得系统访问权限。攻击者将获得对 Judge0 系统包括数据库、内部网络、Judge0 web 服务器以及在 Linux 主机上运行的任何其它应用上的完整访问权限。”

CVE-2024-29021与允许和Docker内网中可用的 PostgreSQL 数据库通信的配置有关，可使对手武器化该SSRF连接到数据库并修改相关栏的数据类型，最终获得命令执行权限。

Judge0收到负责任的漏洞报告后，在2024年4月8日发布版本1.13.1修复了这些潜在威胁。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[OWASP 发布十大开源软件风险清单（详解版）](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519303&idx=1&sn=df6dc31715e4c8d70ad22fe31af7eb03&chksm=ea94bd2ddde3343b6e37f517febd2d68bba0fe206dde6bab42bf696389f1ca4723bbdf8ccf78&scene=21#wechat_redirect)

[开源AI框架 Ray 的0day已用于攻陷服务器和劫持资源](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519162&idx=1&sn=3872fcc82018e2c561d9e4e7574f0c8e&chksm=ea94bad0dde333c6d504e2c7680caabb4badc973dd03223bab93d5b62e5469c4db22d966adf9&scene=21#wechat_redirect)

[CISA：注意 Chrome 和 Excel 解析库中已遭利用的开源漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518582&idx=2&sn=3e7fcf93d7c3d8fa193fcb72ed6c2347&chksm=ea94b81cdde3310af6e572040db0f7c2aba6bf5314cdb417d0ad4e7fffa194153e99860228a1&scene=21#wechat_redirect)

[速修复！开源通信框架 FreeSWITCH 受严重漏洞影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518495&idx=1&sn=c9f248c5f3f6c32802c76b6b1ed8e247&chksm=ea94b875dde33163ad619a2669636190d521db9292d6b488cb2d39f88259ee0cc20e49d86431&scene=21#wechat_redirect)

[速修复！开源防火墙软件pfSense 中存在多个漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518402&idx=3&sn=2287f259ca95d49fdb713843ffc8a1b6&chksm=ea94b9a8dde330bebb3afdf0e531542d025f12326245695da6554d9b7095da964c8f78e62a55&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/04/sandbox-escape-vulnerabilities-in.html

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