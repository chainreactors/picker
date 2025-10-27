---
title: RADIUS协议遭破解，全球大量设备恐沦为“黑客跳板”
url: https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247512142&idx=2&sn=40f8e1e233c7488d664c2480f016774f&chksm=ebfaf76edc8d7e78fc68fae0fbecafcf2fe8290a9af33450aa414f6bdc065e3660947dba3ea5&scene=58&subscene=0#rd
source: 安全内参
date: 2024-07-11
fetch_date: 2025-10-06T17:45:19.615403
---

# RADIUS协议遭破解，全球大量设备恐沦为“黑客跳板”

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7tftvS4BuicuiaiaUicic51dkAWtSauV6tK5VNdnwxFGfOSYJ47HhBtTsHQ6zfticsba0HzxB9RltLIXVjg/0?wx_fmt=jpeg)

# RADIUS协议遭破解，全球大量设备恐沦为“黑客跳板”

安全内参

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvZVE2JTLppQFXRfcV8NVnXNWVMr3FQdOo2pdDO1OPnoAzKIVbIMudfxJJ1icibmq2AQDlBa0btsqmaQ/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**Blast-RADIUS攻击并不需要窃取用户密码或其他凭证，因此传统安全防护措施无效。**

近日，一个新的安全漏洞正在威胁全球采用RADIUS网络认证协议的大量企业和电信网络。

研究人员发现，名为Blast-RADIUS的攻击可以利用RADIUS协议的缺陷，让黑客轻松入侵网络设备并获取管理员权限，从而控制整个网络。

RADIUS协议广泛用于在各种网络设备上进行身份验证和授权，例如交换机、路由器、DSL和FTTH（光纤到户）、802.1X和Wi-Fi、2G和3G蜂窝漫游、5G DNN（数据网络名称）、私有APN和VPN以及关键基础设施网络中的身份验证。在一些大型企业网络中，使用RADIUS协议的设备数量可能多达数万台。

**RADIUS协议存在什么漏洞？**

Blast-RADIUS攻击利用了新的RADIUS协议漏洞（CVE-2024-3596）和MD5碰撞攻击。

RADIUS协议使用MD5哈希请求和响应设备端的身份验证。MD5是一种常见的加密算法，但随着科技发展，其安全性已经逐渐降低。2004年MD5哈希碰撞首次被证明，但通常人们认为不可能在RADIUS协议环境中利用MD5的这一缺陷。

Blast-RADIUS研究团队发现，攻击者其实可以利用RADIUS使用MD5的协议漏洞，伪造一条认证成功的虚假信息，并将其注入到RADIUS服务器和客户端之间的通讯当中。

具体来说，研究人员的概念验证漏洞（尚未公布）会计算出伪造有效“Access-Accept”响应所需的MD5前缀哈希碰撞，以表示身份验证请求成功。然后使用中间人攻击将伪造的MD5哈希注入网络通信，由于服务器无法分辨真假，黑客可登录并获得完全的网络管理权限。

据研究人员介绍，Blast-RADIUS攻击需要3到6分钟才能伪造所需的MD5哈希值，超出了现实中RADIUS服务器设置的30到60秒的超时时间，但这并不意味着可以高枕无忧。因为，Blast-RADIUS攻击中使用的碰撞算法的每个步骤都可以有效地并行化，并且适合硬件优化，这将使资源充足的攻击者能够使用GPU、FPGA或其他更现代、更快的硬件实施攻击，以实现更快的运行时间，可能快几十倍或几百倍。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/INYsicz2qhvZVE2JTLppQFXRfcV8NVnXNRFhV5sxuuHElxvGkcNsm6n8icF5zAkTl98bhTtqBPKibloeVRgWcn0DQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

*Blast-RADIUS攻击流程来源：Blast-RADIUS研究团队*

**传统手段无法阻止攻击**

更令人担忧的是，Blast-RADIUS攻击并不需要窃取用户密码或其他凭证，传统安全防护措施无效。黑客只需要能够监听网络流量，并利用特殊的算法在数分钟内就能算出虚假信息的关键部分(MD5哈希值)并用于发动攻击。

**如何防范Blast-RADIUS攻击？**

虽然普通用户无法防御此类攻击，但网络运营商和设备管理人员可以采取一些措施降低风险：

* 升级到RADIUS over TLS(RADSEC):这是一种更加安全的认证方式，可以防止信息被窃取和篡改。
* 改用“multihop” RADIUS部署:这种部署方式可以增加一道认证关卡，让黑客更难得逞。
* 隔离RADIUS流量:将RADIUS通信限制在内部网络中，并通过专用VLAN或安全隧道进行加密传输，避免黑客有机会接触到相关信息。

网络安全研究人员建议相关厂商尽快发布补丁修复漏洞，网络运营商也应积极升级设备并采取必要的安全措施，以免遭受黑客利用Blast-RADIUS漏洞的攻击。

参考链接：

https://www.blastradius.fail/

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