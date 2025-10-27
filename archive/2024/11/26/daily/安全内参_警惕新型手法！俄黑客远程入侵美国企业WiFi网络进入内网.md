---
title: 警惕新型手法！俄黑客远程入侵美国企业WiFi网络进入内网
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247513143&idx=2&sn=bacead9c66fff6f2f128965273ffbf80&chksm=ebfaf317dc8d7a01aa1d9ac041c4aaebb7ac27aafa176449d74032dbb7ba29d5e821a7a5a6ba&scene=58&subscene=0#rd
source: 安全内参
date: 2024-11-26
fetch_date: 2025-10-06T19:20:14.092693
---

# 警惕新型手法！俄黑客远程入侵美国企业WiFi网络进入内网

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7u33G7yEaP9ibAuAOGDQTzrzCbBlic9Y5avzNfiasuibvoHgQVs13MiaJxFxehoan4DLJoMSZaozIcgBYQ/0?wx_fmt=jpeg)

# 警惕新型手法！俄黑客远程入侵美国企业WiFi网络进入内网

安全内参编译

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvbicaibia0SXBUSIBDoQ8PVzakbBIx0ianibibibgt1h6ib0D8iaoUsZrdZicF2qIrQSMQMpYvF9mtZ2dQQLSAA/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

近日，网络安全公司Volexity曝光了一起令人震惊的网络攻击事件，俄罗斯黑客组织APT28成功突破物理攻击范围，入侵了万里之外的一家美国企业的Wi-Fi网络。

据报道，2022年2月，美国首都华盛顿一家企业的WiFi网络被发现遭遇了极不寻常的攻击，这次攻击被归因于俄罗斯国家黑客组织APT28（亦称Fancy Bear/Forest Blizzard/Sofacy），后者过一种名为“近邻攻击”的新技术，远程入侵了该美国企业的WiFi网络。此次事件暴露了企业WiFi网络被忽视的致命盲区和漏洞，同时也展现了APT28不断创新的攻击方式。

APT28是隶属于俄罗斯军事情报总局（GRU）第26165部队的黑客组织，早在2004年便开始活跃，主要攻击目标是西方政府、军事部门。

**攻击细节：从“邻居”到目标的跳板式入侵**

**1.起点：WiFi网络的密码喷射攻击**

APT28首先通过对目标企业暴露在互联网的服务进行密码喷射攻击，获取了该企业WiFi网络的访问凭证。然而，由于企业实施了多因素认证（MFA），黑客无法通过公共网络直接利用这些凭证访问目标网络。

**2.创新策略：寻找“邻居”作为跳板**

远隔万里“蹭网”显然存在难以逾越的物理距离问题，APT28采取了一种创造性策略。他们瞄准了目标企业附近建筑内的其他企业，通过渗透这些企业的网络设备进行跳板式入侵。黑客寻找具有“双网连接”能力的设备（例如同时连接有线和无线网络的笔记本电脑或路由器），以利用其无线网卡连接到目标企业的WiFi网络。

**3.实施：跳板攻击与渗透**

Volexity的调查显示，APT28成功入侵了多个邻近组织，并最终找到了一个设备，该设备能够接入目标企业会议室附近的三个无线接入点（AP）。黑客通过远程桌面连接（RDP）使用非特权账户进入目标网络，逐步扩展其权限，最终能够访问关键系统并提取敏感数据。

**技术手段：低调但高效**

**1.数据提取与脚本操作**

黑客运行了名为“servtask.bat”的脚本，用以转储Windows注册表中的关键数据（如SAM、安全性和系统信息），并将其压缩为ZIP文件进行传输。这些信息为进一步的网络渗透和数据窃取提供了基础。

**2.使用本地工具降低被发现风险**

APT28主要依赖Windows自带工具执行操作，以减少其在受感染系统中的行为痕迹。这种低调的操作方式使得黑客在不触发异常警报的情况下成功提取数据。

**3.利用零日漏洞扩展权限**

根据微软今年4月的一份报告，APT28可能利用了Windows打印后台处理服务中的一个零日漏洞（CVE-2022-38028）来提升其在目标网络中的权限，从而运行关键的恶意负载。

**“邻居攻击”带来的启示：物理安全边界不存在了**

APT28的“邻居攻击”颠覆了传统近距离物理攻击的概念，通常近距离物理攻击要求攻击者在目标附近，例如停车场等场所。但此次事件表明，通过利用跳板式策略，攻击者能够在远程位置发动物理攻击，同时规避被物理追踪和识别的风险。

**网络安全防护的反思与建议**

虽然近年来针对互联网暴露设备的安全措施，如MFA和强密码管理，已显著提升，但WiFi网络的安全性仍然是许多企业的薄弱环节。企业需将WiFi网络视为与其他远程访问服务同等重要的安全防护对象。

针对APT28的攻击模式，企业可以采取以下措施：

* 实施严格的WiFi访问控制，例如基于设备认证的访问策略。
* 配置网络隔离，防止内部设备同时连接无线和有线网络。
* 定期监控网络流量，及时发现可疑行为。

企业需要从安全文化和技术双管齐下，提高多层防护能力。结合行为分析和异常检测工具更早发现类似攻击，同时加强员工安全意识培训，减少密码喷射攻击的成功率。

参考链接：

https://www.volexity.com/blog/2024/11/22/the-nearest-neighbor-attack-how-a-russian-apt-weaponized-nearby-wi-fi-networks-for-covert-access/

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