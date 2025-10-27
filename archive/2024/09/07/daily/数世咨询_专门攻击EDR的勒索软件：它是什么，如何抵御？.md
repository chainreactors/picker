---
title: 专门攻击EDR的勒索软件：它是什么，如何抵御？
url: https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247515454&idx=1&sn=f91cf054a7e16bc0e3f2c68a6bcd4709&chksm=c144cf83f6334695b6855586fc6c8f17793a759a27d3efbcc8e90ee8dfdce087a18a1f4ea15b&scene=58&subscene=0#rd
source: 数世咨询
date: 2024-09-07
fetch_date: 2025-10-06T18:28:57.212636
---

# 专门攻击EDR的勒索软件：它是什么，如何抵御？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqpp8Es42oX7picBaqrBIyHynnWYHD4iaTW8RvNUhMsjsWEWZvcicHicrlRwJRSKWKcIPL4jfr1btSsALA/0?wx_fmt=jpeg)

# 专门攻击EDR的勒索软件：它是什么，如何抵御？

数世咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y9btpvDIDqpp8Es42oX7picBaqrBIyHynMAePTTRcbNynnojuDy6Y7hb6ZQAFKsBmGcicZEof7ibqzGIRkia2uoOKQ/640?wx_fmt=jpeg&from=appmsg)

在网络安全领域，网络安全中的 **EDR(Endpoint Detection and Response，端点检测与响应)**是一种主动式的端点安全解决方案，它专注于监控、检测和响应计算机和终端设备上的安全威胁。

最近，攻击者不断推陈出新，开发出各种工具来绕过安全防护措施并利用系统漏洞，其中一种名为“EDRKillShifter”的新工具的出现，揭示了网络犯罪分子与安全防御者之间不断升级的对抗态势。

**01**

**EDRKillShifter 与RansomHub**

Sophos 在对一次勒索软件攻击的事后分析中，发现了一种名为“EDRKillShifter”的新工具。这个工具由一个不明身份的犯罪集团使用，目的是通过 RansomHub 勒索软件感染目标组织。尽管这次攻击未能成功，但EDRKillShifter 的发现在网络安全界引起了广泛关注。

Sophos 的威胁研究员Andreas Klopsch 指出，**EDRKillShifter 的目的是终止端点保护软件，这是组织用来检测和应对网络恶意活动的关键防御工具。通过禁用这些防御机制，攻击者可以在受感染的系统内更自由地活动，增加勒索软件攻击的成功率。**在这次事件中，攻击者试图使用 EDRKillShifter 禁用目标机器上的 Sophos 保护，但未能成功。这一事件凸显了网络犯罪分子越来越专注于开发能够攻击EDR 防护软件的工具，逐渐成为新趋势。

**02**

**EDR 杀手工具的兴起**

EDRKillShifter 的出现是恶意软件越来越复杂的趋势的一部分，这些恶意软件旨在禁用 EDR 系统。自 2022 年以来，安全研究人员发现这类工具的开发和部署显著增加。例如，安全专家之前发现的另一种名为“AuKill”的 EDR 杀手工具，曾在犯罪市场上出售。现在，多种具有类似功能的工具在流通，这表明网络犯罪分子认识到了使 EDR 防护软件失效的重要性。

EDR 防护软件是现代网络安全策略的核心，它们提供实时监控、检测和响应功能，对于防御高级威胁至关重要。攻击者通过开发 EDRKillShifter 和 AuKill 等工具，旨在破坏这些防御措施，以便更容易地部署勒索软件、窃取敏感数据或破坏业务运营。

**01**

**如何防范 EDR 攻击工具**

面对日益复杂的 EDR 攻击工具，组织必须采取积极措施来保护其系统。安全专家在其分析中提出了以下建议，以帮助企业和个人抵御此类威胁：

**1. 启用防篡改保护**：防范EDRKillShifter 等工具的最有效方法之一是确保端点安全产品已启用防篡改保护。这一功能可以防止修改未经授权的安全设置，使攻击者更难禁用用户的防御。

**2. 使用强大的 Windows 安全卫士**：EDR 攻击工具的成功通常取决于攻击者提升权限或获取目标系统管理员权限的能力。为了降低这种风险，组织应严格区分用户和管理员权限。通过限制具有管理访问权限的用户数量，可以减少攻击者获得禁用 EDR 防护软件所需权限的可能性。

**3. 保持系统更新**：微软一直在积极主动解决与驱动程序滥用相关的漏洞。自 2023 年以来，该公司已推出了更新，取消了已知被攻击者利用的签名驱动程序的认证。保持系统更新可以确保用户从这些安全增强功能中受益，使攻击者更难利用已知漏洞。

通过采取这些措施，组织可以增强其网络安全防护，有效抵御 EDR 杀手勒索软件的威胁。

\* 本文为闫志坤编译，注：图片均来源于网络，无法联系到版权持有者。如有侵权，请与后台联系，做删除处理。

— 【 THE END 】—

🎉 大家期盼很久的#**数字安全交流群**来了！快来加入我们的粉丝群吧！

🎁 **多种报告，产业趋势、技术趋势**

这里汇聚了行业内的精英，共同探讨最新产业趋势、技术趋势等热门话题。我们还有准备了专属福利，只为回馈最忠实的您！

👉 扫码立即加入，精彩不容错过！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqPJv9p5ibKIhJXQjWHJmSlibSdib80Llfp8mlV0ibf7m47jyaVeGoFeorddtIuxS5liafTJRKHeSdLnaQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

😄嘻嘻，我们群里见！

更多推荐

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqp72VD8Ft2xAxulKkNQzCpMYmic4xkqp3ky3wcian32ndo3MuLV2dqL6RgqTfITGP0SsmRzibUBftDFg/640?wx_fmt=png&from=appmsg)](http://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247514213&idx=1&sn=fa2d0412dbbce05ec48a9df909b7cfd3&chksm=c144cad8f63343ce0f383fc9d885c2c7ddcb3f3871270abea4c274775307858d350f60db3b54&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqqXZatwW85WHD0ggOUzguusylfEicp7y64ic36rtZXpLGPKXds2NvBpuExtgAMicK0LB71waZTVKfpPw/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247513359&idx=1&sn=2f3bd51b24862de02cca6078688bafeb&chksm=c144c7b2f6334ea415adac810ce4803cdb3cd5e5ba194ff394b7278ebbb48cc830c8d405427a&token=824343009&lang=zh_CN&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y9btpvDIDqos5a6Z5B6UrU0VmoicIP7IvuJWmXe2HBJ3ZUZuPdpG4uUiaVrTFajxtY0AIjWcrWUDDeC0EFT2waicg/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzkxNzA3MTgyNg==&mid=2247513339&idx=1&sn=759f859d0cf7dd748d3dd83ce49cf4cc&chksm=c144c646f6334f5017581206b0da2af90d539c921614514e3eb40f6c80d846bece0e6b521067&token=824343009&lang=zh_CN&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

数世咨询

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y9btpvDIDqqibHKn3xia71ylibsqm32we7KaKfENSmicZKZf0dT3Jic5QicvIicKsBUZxyTt9FvqFNVAKV5ILVE5se9AQ/0?wx_fmt=png)

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