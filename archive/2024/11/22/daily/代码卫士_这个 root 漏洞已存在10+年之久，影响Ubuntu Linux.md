---
title: 这个 root 漏洞已存在10+年之久，影响Ubuntu Linux
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521546&idx=1&sn=deaef16f3522dccfad4051c26652ad09&chksm=ea94a460dde32d76e798dae949a23f4b13024861b106b442b888ab5bd8453b2bb70146379673&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-22
fetch_date: 2025-10-06T19:16:37.238373
---

# 这个 root 漏洞已存在10+年之久，影响Ubuntu Linux

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTccTGabC2JicXk7sicdS39K3c2Mf8HZBv2zgvNLydaxTJgKcIZTZZ3KKgrRRaEChNMtgrI6buSAiaoA/0?wx_fmt=jpeg)

# 这个 root 漏洞已存在10+年之久，影响Ubuntu Linux

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Ubuntu Linux 使用的工具 needrestart 中存在五个本地提权 (LPE)漏洞，它们早在10多年前发布的版本21.04中就已被引入。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTccTGabC2JicXk7sicdS39K3GhgFrIY5gly7zSwRMXpeZw8135NjhrgO9CeWPmLiboLHAmBCbiboickPw/640?wx_fmt=gif&from=appmsg)

这些漏洞由Qualys 公司发现，编号为CVE-2024-48990、CVE-2024-48991、CVE-2024-48992、CVE-2024-10224和CVE-2024-11003。这些漏洞在2014年4月发布的 needrestart 版本 0.8中引入，在昨天发布的3.8版本中修复。

Needrestart 工具常用于 Linux 上，包括 Ubuntu Server在内，旨在识别包更新后需要重启的服务，确保这些服务运行的是最新的共享库版本。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTccTGabC2JicXk7sicdS39K3OkxAzpn2ptOgvzUgN2ibT8YdbF5V7UPjUrBZTOKWich5gtvql2UslluA/640?wx_fmt=gif&from=appmsg)

**LPE 漏洞概览**

这五个漏洞可导致对易受攻击 Linux 系统具有本地访问权限的攻击者在无需用户交互的前提下将权限提升至 root。它们的概览如下：

* CVE-2024-48990：Needrestart 通过从运行进程中提取的 PYTHONPATH 环境变量执行 Python 解释器。如果本地攻击者控制该变量，则可通过植入恶意共享库的方式在 Python 初始化过程中以 root 权限执行任意代码。
* CVE-2024-48992：当处理受攻击者控制的 RUBYLIB 环境变量时，needrestart 使用的 Ruby 解释器易受攻击，从而导致本地攻击者通过将恶意库注入该进程的方式，以 root 身份执行任意 Ruby 代码。
* CVE-2024-48991：needrestart 中的条件竞争可导致本地攻击者用恶意可执行文件取代正在验证的 Python 解释器二进制。通过仔细计算替代的时间，它们可诱骗 needrestart 以root身份运行代码。
* CVE-2024-10224：needrestart 使用的Perl 的 ScanDeps 模块，不正确地处理了由攻击者提供的文件名称。攻击者可构造与shell命令相似的文件名称（如命令|）在文件打开时以root身份执行任意命令。
* CVE-2024-11003：Needrestart 对 ScanDeps 模块的依赖使其暴露于 ScanDeps 本身的漏洞影响，即不安全使用 eval() 函数可导致在处理受攻击者控制的输入时造成任意代码执行后果。

值得注意的是，攻击者要利用这些漏洞，必须通过恶意软件或受陷账户对操作系统具有本地访问权限，缓解该风险。然而，攻击者曾能类似的 Linux 提权漏洞获得 root 权限，包括 Loony Tunables 和 nf\_tables 漏洞个，因此不能因为需要本地访问权限就忽视这个新漏洞。

随着 needrestart 的广泛使用及其长时间易受攻击，如上漏洞可导致在关键系统上提权。除了更新至3.8或后续版本外，建议修改 needrestart.conf 文件，禁用解释器扫描特性，阻止漏洞遭利用，从而阻止 needrestart 执行带有受攻击者控制的环境变量的解释器。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[因“合规要求”，Linux Kernel 清除了11名俄罗斯开发者的维护者身份](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521303&idx=2&sn=a8f19bf98fa3d8e84ee9c612d1f1d98c&chksm=ea94a57ddde32c6b67f8d71669e3990a30e0de997265420914d11525fb6480bc56dcfa1515f0&scene=21#wechat_redirect)

[CUPS 缺陷可被用于在 Linux 系统上执行远程代码](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520951&idx=2&sn=c045f5bb54c00057ffc31c743992024c&chksm=ea94a3dddde32acbacc84a66c56b518eadd436c59ac19f3aea2b43b088909150a1e3ebb5dadb&scene=21#wechat_redirect)

[0.0.0.0 Day漏洞已存在18年，影响 MacOS和Linux设备](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520401&idx=1&sn=fcb5f892311d2858672c9908d0e08554&chksm=ea94a1fbdde328edf70f4fe9cfcbc9004bf69c75392d0814b2f4ff08e6699e5ec07b0e81730a&scene=21#wechat_redirect)

[Linux 内核受新的SLUBStick 跨缓存攻击影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520334&idx=1&sn=836f6bce19d0adc20c9deedfee1cf1de&chksm=ea94a124dde32832012485df5d575f8d74fed00fade2844c634cae2f6527ef7413e015c25df4&scene=21#wechat_redirect)

[恶意软件攻击Windows、Linux 和 macOS 开发人员](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520290&idx=2&sn=0dff9cae5a9ad1a39be2e6da027f70a9&chksm=ea94a148dde3285e6c15219e90179e8424cf1b202221d471b6c705e4dba7127f593b4fd64b80&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/ubuntu-linux-impacted-by-decade-old-needrestart-flaw-that-gives-root/

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