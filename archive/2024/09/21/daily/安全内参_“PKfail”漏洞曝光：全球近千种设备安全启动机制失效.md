---
title: “PKfail”漏洞曝光：全球近千种设备安全启动机制失效
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512650&idx=2&sn=0eabde31993b06b2caf7204aa68c6caf&chksm=ebfaf56adc8d7c7c7e69336a2f4b969c13cee905fada9ca951f51e1348c1cc1ab85bfe3fcba4&scene=58&subscene=0#rd
source: 安全内参
date: 2024-09-21
fetch_date: 2025-10-06T18:27:21.171442
---

# “PKfail”漏洞曝光：全球近千种设备安全启动机制失效

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7snLiavtfn9UoJUJU2iby13mJOF8pwWJcE8os0nHjiccZp799Qsp1T0dibJcncl2EAeZUibmGXBtHo9Ekg/0?wx_fmt=jpeg)

# “PKfail”漏洞曝光：全球近千种设备安全启动机制失效

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvYVVibClDxYGLicw8H002giaWebkHNyQH69PmQhdY2cKNeTfp27PqR6BKseDiapspaaaAcInMeBKvwLjw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**近日安全研究人员发现从游戏机到总统大选投标机的海量设备仍然使用不安全的测试密钥，容易受到UEFI bootkit恶意软件的攻击。**

**安全启动不安全**

在近期的安全研究中，一项涉及设备制造行业安全启动（Secure Boot）保护机制的供应链失败问题引发了广泛关注。此次事件波及的设备型号范围远比之前已知的要广泛得多，受影响的设备涵盖了ATM机、POS机、甚至投票机等多个领域。

这一问题源自于过去十年间，数百种设备型号中使用了非生产环境的测试平台密钥，这些密钥在其根证书中标注了“DO NOT TRUST”（请勿信任）等警示语，此类密钥原本应仅用于测试环境，但设备制造商却将其应用于生产系统。

平台密钥作为加密的“信任根”锚定了硬件设备与其运行的固件之间的信任关系，确保安全启动机制正常运行。然而，由于大量用于测试安全启动主密钥的私钥被泄漏，极大地削弱了这一安全机制的有效性。研究发现，2022年甚至有人将一部分私钥在GitHub上公开发布。这些信息为攻击者提供了必要条件，能够通过植入“根工具包”（Rootkits）等恶意软件，破坏设备的UEFI（统一可扩展固件接口）安全启动保护。

**500多种设备存在隐患**

此次供应链安全事件被Binarly命名为“PKfail”（CVE-2024-8105），意指平台密钥（Platform Key）失效。此次失败展示了供应链复杂性已超出用户当前的风险管理能力，特别是在涉及第三方供应商时。不过，研究人员指出，这一风险完全可以通过“安全设计理念”进行规避和缓解。

根据Binarly的最新报告，受此问题影响的设备型号远超此前的认知。Binarly的研究工具在过去几个月中收集到了10095个固件样本，其中791个（约占8%）包含了非生产密钥。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvYVVibClDxYGLicw8H002giaWeAfiaia18IORecNSSiajH1iaavV6T8g1O2ic9fiade8GRTH1wIRt8T61dJ7Ew/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

*受PKfail影响的固件数量 来源：Binarly*

最初，Binarly识别出了大约513种设备型号使用了测试密钥，目前一数字已增长至972种。此外，最早报告的215个受影响型号中，有490个型号使用了在GitHub上公开的密钥。研究人员还发现了四个新的测试密钥，使得总数达到了约20个。

此前发现的密钥均来自AMI，这是一家为设备制造商提供UEFI固件开发工具包的主要供应商之一。自7月以来，Binarly还发现了AMI的其他两大竞争对手Insyde和Phoenix的密钥同样存在问题。

更多的受影响设备还包括：

* Hardkernel的odroid-h2、odroid-h3和odroid-h4
* Beelink Mini 12 Pro
* Minisforum HX99G

Binarly进一步指出，受影响的设备不仅限于桌面电脑和笔记本电脑，还包括大量医疗设备、游戏机、企业级服务器、ATM机、销售终端设备，甚至包括投票机！由于目前尚无修复方案，研究人员基于保密协议未披露具体的设备型号。Binarly发布了“PKfail扫描仪”，供应商可以自行上传固件映像查看是否使用了测试密钥。

此次事件表明，安全启动作为一种设备预启动阶段的加密保护机制，尽管被广泛应用于政府承包商和企业环境中，但其安全性依然存在隐患，其供应链管理中存在重大漏洞。

参考链接：

http://www.binarly.io/blog/pkfail-two-months-later-reflecting-on-the-impact

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

文章来源：GoUpSec

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