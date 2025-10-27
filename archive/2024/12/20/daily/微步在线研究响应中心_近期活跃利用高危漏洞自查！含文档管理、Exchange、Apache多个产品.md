---
title: 近期活跃利用高危漏洞自查！含文档管理、Exchange、Apache多个产品
url: https://mp.weixin.qq.com/s?__biz=Mzg5MTc3ODY4Mw==&mid=2247507585&idx=1&sn=5ece95159551948b0ffa7cd719aefdf7&chksm=cfcabd95f8bd34838fd5ab4044866d81a0b443ffbc5e66f89c4407b9b866ee891f036097b191&scene=58&subscene=0#rd
source: 微步在线研究响应中心
date: 2024-12-20
fetch_date: 2025-10-06T19:38:47.819826
---

# 近期活跃利用高危漏洞自查！含文档管理、Exchange、Apache多个产品

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/fFyp1gWjicMLpecvc7OMic8fAUm58Fh997SKTNjpw1D8icrHYvTD1UecKlMt31EoefxiatN0zTHr9xnuUCA985qWYQ/0?wx_fmt=jpeg)

# 近期活跃利用高危漏洞自查！含文档管理、Exchange、Apache多个产品

微步情报局

微步在线研究响应中心

近期，根据微步情报局跟踪及研判，发现当前存在多个漏洞被利用，涉及**电子文档安全管理系统、电子邮件系统、应用程序开发框架**等多个产品及软件。现汇总如下，建议企业尽快自查：

****Microsoft Exchange Server 多个远程代码执行漏洞****

**漏洞编号**：CVE-2020-0688、CVE-2021-42321

根据微步情报局监测，上述漏洞于2020年5月开始就被活跃利用，涉及包括REvil、Carbanak、LockBit等58个黑客组织，且被发现用于勒索活动。最近一次发现时间为2024年12月12日。

相关链接：

https://x.threatbook.com/v5/vul/XVE-2020-2920

https://x.threatbook.com/v5/vul/XVE-2021-33256

**\*\*\*通电子文档安全管理系统身份认证绕过漏洞**

**漏洞编号**：XVE-2024-17589

该漏洞通过X漏洞奖励计划收录（收录时为0day状态），攻击者该漏洞可绕过系统校验登录任意用户，获取系统敏感信息。

根据微步情报局监测，近期发现了数十个攻击IP在活跃利用该漏洞，最近一发现时间为2024年12月16日。

相关链接：https://x.threatbook.com/v5/vul/XVE-2024-17589

**\*\*\*通电子文档安全管理系统多个SQL注入漏洞**

**漏洞编号**：XVE-2024-20927、XVE-2024-15987、XVE-2024-19611

攻击者可以通过构造特定的请求注入恶意 SQL 代码，利用该漏洞对数据库执行任意 SQL 操作，获取敏感信息。

根据微步情报局监测，近期发现了数十个攻击IP在活跃利用上述漏洞，最近一发现时间为2024年12月17日。

相关链接：

https://x.threatbook.com/v5/vul/XVE-2024-20927

https://x.threatbook.com/v5/vul/XVE-2024-15987

https://x.threatbook.com/v5/vul/XVE-2024-19611

**Apache Struts2 文件上传漏洞（S2-067）**

**漏洞编号**：CVE-2024-53677

根据微步情报局监测，近期发现了数个攻击IP在活跃利用S2-067，最近一发现时间为2024年12月19日。

相关链接：https://x.threatbook.com/v5/vul/XVE-2024-35895

**Apache OFBiz 反序列化漏洞**

**漏洞编号**：CVE-2021-30128

Apache OFBiz 存在反序列化漏洞，攻击者可利用该漏洞实现任意代码执行。

根据微步监测，近期发现了数百个攻击IP在活跃利用，最近一次发现时间为2024年12月19日。

相关链接：https://x.threatbook.com/v5/vul/XVE-2021-17782

**GeoServer服务端请求伪造漏洞**

**漏洞编号**：CVE-2023-43795

GeoServer 存在ssrf漏洞，攻击者可以从服务端实现任意请求伪造。

根据微步情报局监测，近期发现了多个攻击IP在活跃利用，最近一次发现时间为2024年12月1日。

相关链接：https://x.threatbook.com/v5/vul/XVE-2023-29290

**Ivanti Connect Secure & Ivanti Policy Secure 远程命令执行漏洞**

**漏洞编号**：CVE-2024-21887

Ivanti Connect Secure 和 Ivanti Policy secure 的 Web 组件存在远程命令执行漏洞，可允许经过身份验证的管理员发送特制请求并在设备上执行任意命令。

根据微步情报局监测，该漏洞被40个黑客组织包括Lazarus、LockBit、APT28活跃利用，且被发现用于勒索活动。最近一次发现时间为2024年12月19日。

相关链接：https://x.threatbook.com/v5/vul/XVE-2024-0886

**Apache Solr Backup/Restore APIs 远程代码执行**

**漏洞编号**：CVE-2023-50386

根据微步情报局监测，近期发现了数十个攻击IP在活跃利用，最近一次发现时间为2024年12月18日。

相关链接：https://x.threatbook.com/v5/vul/XVE-2023-37874

目前，以上被活跃利用的高危漏洞，**微步威胁感知平台TDP均支持检测**。

此外，**企业也可直接通过微步下一代威胁情报平台NGTIP、X情报社区的已知利用情报，自主查询当前已知利用事件，实时了解近期已发生高危漏洞利用事件及相关攻击IP，及时排除风险**。

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLpecvc7OMic8fAUm58Fh997fiavrSfenibcXHve24uWY4vRj9V9jYJ427e45iaaicYYAGxRCBf5O94Licw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicMLpecvc7OMic8fAUm58Fh997ghtUCUicJ2Uxf1fBCJjAuJSax9gRV4kTJpxiabaVPV5pEJGviaxyibSRoA/640?wx_fmt=png&from=appmsg)

- END -

//

**微步漏洞情报订阅服务**

微步提供漏洞情报订阅服务，精准、高效助力企业漏洞运营：

* 提供高价值漏洞情报，具备及时、准确、全面和可操作性，帮助企业高效应对漏洞应急与日常运营难题；
* 可实现对高威胁漏洞提前掌握，以最快的效率解决信息差问题，缩短漏洞运营MTTR；
* 提供漏洞完整的技术细节，更贴近用户漏洞处置的落地；
* 将漏洞与威胁事件库、APT组织和黑产团伙攻击大数据、网络空间测绘等结合，对漏洞的实际风险进行持续动态更新。

扫码在线沟通

↓↓↓

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hQl5bZ5Mx6PTAQg6tGLiciarvXajTdDnQiacxmwJFZ0D3ictBOmuYyRk99bibwZV49wbap77LibGQHdQPtA/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/Yv6ic9zgr5hTIdM9koHZFkrtYe5WU5rHxSDicbiaNFjEBAs1rojKGviaJGjOGd9KwKzN4aSpnNZDA5UWpY2E0JAnNg/640?wx_fmt=other&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

点此电话咨询

**X漏洞奖励计划**

“X漏洞奖励计划”是微步X情报社区推出的一款针对未公开漏洞的奖励计划，我们鼓励白帽子提交挖掘到的0day漏洞，并给予白帽子可观的奖励。我们期望通过该计划与白帽子共同努力，提升0day防御能力，守护数字世界安全。

活动详情：https://x.threatbook.com/v5/vulReward

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

微步在线研究响应中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

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