---
title: 瞄准安全研究人员！攻击者在GitHub上使用伪造PoC窃取39万WordPress凭证
url: https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787651&idx=1&sn=3ec2660ca7270d7114baa4c06baf3c9e&chksm=8893bd6cbfe4347a5e48d1a57e69027c5452067dacbc253484e6a486edbace5e98c70fca1756&scene=58&subscene=0#rd
source: 安全客
date: 2024-12-19
fetch_date: 2025-10-06T19:38:41.338283
---

# 瞄准安全研究人员！攻击者在GitHub上使用伪造PoC窃取39万WordPress凭证

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb6HcCM8sia2pC2jYtFW2xSibfeBur0Th0pLicpSD2JszDvlsQjOI5AZpH2EVTk7Vtzh8T399UvIVnTCg/0?wx_fmt=jpeg)

# 瞄准安全研究人员！攻击者在GitHub上使用伪造PoC窃取39万WordPress凭证

安全客

安全客

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb6HcCM8sia2pC2jYtFW2xSibfq35AvZaRqNxsWjvJ2l0D54yPQ2w307md11l8nFaDib7icbicWQJHOejMA/640?wx_fmt=jpeg&from=appmsg)

Datadog Security Labs的网络安全研究人员发现，名为MUT-1244的威胁行为者发起了一项为期一年的恶意攻击活动，导致超过39万个WordPress凭证被盗。

研究称，该行为者利用一个伪造的WordPress凭证检查工具来窃取数据，被感染系统中的SSH私钥和AWS访问密钥也被盗取。攻击者的主要目标包括红队人员、渗透测试人员、安全研究人员，甚至其他恶意行为者。

**01**

**攻击方式：钓鱼邮件和伪造GitHub仓库**

研究人员观察到，MUT-1244使用了两种主要方法来获取对受害者系统的初始访问权限，包括钓鱼攻击和伪造的GitHub仓库。

**钓鱼邮件**

攻击者通过针对学术界，尤其是高性能计算（HPC）领域的研究人员，发起了钓鱼邮件攻击。这些邮件伪装成系统升级通知，诱导受害者安装伪装成内核升级的恶意软件。一旦受害者执行该恶意软件，攻击者便可以获得受害者系统的远程控制权限，窃取其存储在系统中的敏感数据。

**伪造GitHub仓库**

除了钓鱼攻击，黑客还通过创建伪造的GitHub仓库发布恶意代码。这些仓库看似包含漏洞利用的PoC代码，但实际上却嵌入了恶意负载。当研究人员下载并运行这些代码时，系统便被感染。

值得注意的是，伪造PoC代码的使用已经成为一种新型的攻击手段，特别是针对网络安全研究人员和开发者。与以往直接的恶意软件不同，这些伪造的PoC代码往往被误认为是合法的安全工具，因此很难引起受害者的警觉。这种攻击手段的精妙之处在于，受害者认为他们下载的是安全漏洞的研究代码，而实际情况却是恶意代码被巧妙地隐藏其中。通过伪装成可信的资源，这类攻击能够有效绕过常规的安全防护，特别是在那些高度依赖开源资源和工具的安全研究人员和开发者中，极易造成感染。

例如，2023年6月，骗子被发现冒充真实的网络安全研究人员，通过GitHub和X（前身为Twitter）传播伪造的PoC代码来传播恶意软件。2023年7月，类似的活动也被发现，黑客通过伪造的GitHub仓库分发恶意软件，这些仓库伪装成PoC。到2023年9月，又有一场恶意攻击活动浮出水面，利用伪造的概念验证脚本欺骗研究人员下载并执行VenomRAT木马。该攻击利用了WinRAR漏洞（CVE-2023-40477）。

**02**

**多种隐蔽攻击手段：后门配置与恶意文件**

攻击者利用多种隐蔽技术确保恶意代码能够悄无声息地执行，从而避免被检测到。

**后门配置文件**

部分伪造的GitHub仓库中，恶意代码被巧妙地隐藏在后门配置文件中。虽然这些仓库包含一些看似正常的漏洞利用代码，但黑客通过在配置文件中嵌入恶意负载来绕过安全检测。受害者执行这些文件时，恶意代码悄然运行，攻击者便能窃取敏感信息。

**恶意PDF和Python投毒**

其他攻击者通过将恶意负载嵌入PDF文件，或利用Python投毒脚本来执行攻击。这些PDF文件在被打开后会触发恶意代码的提取与执行，而Python脚本则通过解码并写入磁盘的方式，进一步加深了攻击的隐蔽性。此外，还有攻击者通过在代码中嵌入恶意的npm包，间接感染受害者设备，扩展了恶意代码的传播途径。

这些隐蔽的攻击手段使得黑客能够绕过许多常见的防御措施，尤其是在安全研究人员和开发者日常依赖开源工具的背景下，感染风险大大增加。

攻击者的最终目标是窃取受害者的敏感信息，包括SSH私钥、AWS访问密钥、命令历史记录等。此外，研究人员还发现，恶意代码中硬编码了Dropbox和file.io等服务的凭证，帮助攻击者能够访问和下载被盗数据。这表明，黑客不仅在窃取敏感信息，还能够长期控制受害者的系统，进一步扩大攻击范围。

在此次攻击中，黑客成功窃取了**超过39万个**WordPress凭证。这些凭证最初可能由其他恶意行为者通过非法手段获取，随后被攻击者利用名为“yawpp”的伪造工具进行验证并窃取。Yawpp表面上是一个合法的WordPress凭证检查工具，但实际上它被恶意修改，成为攻击者获取凭证的工具。攻击者通过这一工具，进一步拓展了攻击面，窃取了大量用户账户信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ok4fxxCpBb6HcCM8sia2pC2jYtFW2xSibfhWgZVcH1p8apeS4eyfx7z6I3KZZS5yEOjxNSBS245cI15CL3JeFwqg/640?wx_fmt=jpeg&from=appmsg)

攻击流程和骗局中使用的配置文件之一（图片来源：Datadog Security Labs）

这次攻击的方式不仅表明了黑客技术的不断演进，也揭示了开源平台和工具的潜在风险。Bugcrowd的创始人兼顾问Casey Ellis表示：“针对红队人员和安全研究人员的伪造PoC攻击已经不是新鲜事，但这种手段依然有效，能够作为watering-hole攻击的一部分，利用目标群体的信任和依赖性来发起攻击。”Casey补充道：“这也提醒了安全研究人员和开发者，尽管开源资源和工具为他们提供了极大的便利，但也同时带来了潜在的安全威胁。”

MUT-1244的这一攻击活动展示了网络犯罪分子如何利用GitHub等受信平台以及流行的安全工具，发起精心设计的攻击，窃取敏感信息。随着网络安全威胁的日益复杂，研究人员和安全从业者必须保持警惕，避免成为攻击目标。同时，也警示我们需要加强对供应链安全的关注，尤其是在面对类似伪造PoC代码这类新型攻击手段时，必须提高警觉，增强防范意识。

文章来源：

https://hackread.com/hackers-fake-pocs-github-wordpress-credentials-aws-keys/

**推荐阅读**

|  |
| --- |
| **01**  ｜[微软Azure MFA漏洞曝光](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787627&idx=1&sn=4aca62c5aa480dccf358e90b043f3dcc&scene=21#wechat_redirect) |
| **02**  ｜[斯柯达汽车漏洞披露](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787610&idx=1&sn=95a8903a00d204b2f0a97e8c4b9362d9&scene=21#wechat_redirect) |
| **03**  ｜[银狐团伙再出新招，Web漏洞成切入点](https://mp.weixin.qq.com/s?__biz=MzA5ODA0NDE2MA==&mid=2649787591&idx=1&sn=e8b66114e6f98d415269d5b8d9f96a37&scene=21#wechat_redirect) |

**安全KER**

安全KER致力于搭建国内安全人才学习、工具、淘金、资讯一体化开放平台，推动数字安全社区文化的普及推广与人才生态的链接融合。目前，安全KER已整合全国数千位白帽资源，联合南京、北京、广州、深圳、长沙、上海、郑州等十余座城市，与ISC、XCon、看雪SDC、Hacking Group等数个中大型品牌达成合作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb6HcCM8sia2pC2jYtFW2xSibfPCsxkzHK2tmka0YU9jEycJ7ibvJ8s39jPrB4M0ibYvA1kA4q3IicRiaYkw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb6HcCM8sia2pC2jYtFW2xSibf2hIfLsE5MJgVcThuprj9tnQxKnkQnLl00SnXS2GtZI7hRoYxknZOcQ/640?wx_fmt=png&from=appmsg)

**注册安全KER社区**

**链接最新“圈子”动态**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

安全客

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Ok4fxxCpBb7PGibphJ1WF3d1yIRaNsuRas4r2SWiaKK9yAoKpicYWBaibyGcHNiaEbrDauSywRrvcn4UFEkZvEo3S6Q/0?wx_fmt=png)

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