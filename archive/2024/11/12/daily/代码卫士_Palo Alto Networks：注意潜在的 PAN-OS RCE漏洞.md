---
title: Palo Alto Networks：注意潜在的 PAN-OS RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521440&idx=1&sn=3bf8ff26ce74c0c7fbfeb2701a773a5f&chksm=ea94a5cadde32cdc6e1e16ba74e79862839d2d877a3da3944d99e684a1413808b48093170e2d&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-11-12
fetch_date: 2025-10-06T19:19:16.382786
---

# Palo Alto Networks：注意潜在的 PAN-OS RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTwbNlrPXlJtdcFv34QtDk4DlH9F77y1P1ChZ5a2lC9gesFFccJWBicRHSghLkdJVQK4YLiamUJykAw/0?wx_fmt=jpeg)

# Palo Alto Networks：注意潜在的 PAN-OS RCE漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTwbNlrPXlJtdcFv34QtDk4sZDy0XFZiccKMvjtqfsnXLEvxD0ntBEFqiaNZ1RTIaCEmw0c7P0nPKNg/640?wx_fmt=gif&from=appmsg)

**网络安全公司 Palo Alto Networks 提醒客户称，应限制对下一代防火墙的访问权限，因为PAN-OS 管理接口中可能存在一个远程代码执行漏洞。**

Palo Alto Networks 公司在上周五发布安全公告提到，尚未发现关于该漏洞的其它信息，并提到也并未检测到漏洞遭活跃利用的迹象。该公司提到，“Palo Alto Networks 公司注意到 PAN-OS 管理接口中存在远程代码执行漏洞的言论。当前，我们并不了解该漏洞的详情，正在积极监控任何利用迹象。我们强烈建议客户确保已经按照所推荐的最佳部署指南，正确配置了管理接口。具有ASM 模块的Cortex Xpanse 和 Cortex XSIAM 客户可查看由 Palo Alto Networks Firewall Admin Login 攻击面规则生成的告警，调查暴露在互联网中的实例。”

Palo Alto Networks 公司建议客户拦截从互联网对防火墙的PAN-OS 管理接口的访问并仅允许可信内部IP地址的连接。

从Palo Alto Networks 社区网站上发布的单独支持文档来看，管理员也可采取以下措施之一，减少管理接口的暴露：

* 将管理接口隔离在专门的管理VLAN中。
* 使用堡垒机访问管理IP。用户在登录到防火墙/Panorama之前，认证并连接到堡垒机。
* 将管理接口的进站IP地址仅限于获批的管理设备。通过阻止对异常IP地址的访问，减少攻击面饼通过被盗凭据阻止访问。
* 仅允许受保护的通信如 SSH、HTTPS。
* 仅允许PING对接口的连接性进行测试。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTwbNlrPXlJtdcFv34QtDk4vjzvh2QYUmXV7ibro6XSm6Mv0jqAkmXwm95eySd8xQTDKXRCPibIIA0A/640?wx_fmt=gif&from=appmsg)

**严重的认证缺失漏洞已遭利用**

本周四，CISA还提醒注意Palo Alto Networks Expedition 中一个严重的认证缺失漏洞CVE-2024-5910已遭利用。该漏洞在7月份得到修复，可被攻击者远程利用，从而重置暴露在互联网 Expedition 服务器上的应用管理员凭据。

虽然CISA并未提供更多攻击详情，但已有研究员在上个月发布 PoC 利用，据称可与命令注入漏洞CVE-2024-9464组合利用，在易受攻击的 Expedition 服务器上获得“未认证的”任意命令执行权限。

CVE-2024-9464可与其它漏洞组合利用，接管管理员账户并劫持 PAN-OS防火墙。

CVE-2024-5910已被CISA纳入必修清单，要求联邦机构在11月28日之前修复该漏洞。CISA提醒称，“这类漏洞经常是恶意人员的攻击向量，为联邦企业造成重大风险。”

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Palo Alto：注意！PAN-OS 防火墙 0day 漏洞已遭利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519289&idx=1&sn=86e226003b5da9dd0d6867f4b45fcb1a&chksm=ea94bd53dde33445851c3ec7ca670a0d3c51235d027e8d130593cdc9eabd3a33d9758580655a&scene=21#wechat_redirect)

[Palo Alto Networks：PAN-OS DDoS 漏洞已遭在野利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513567&idx=1&sn=181b3bb7e1b34dc9dd67bfde798f4c7d&chksm=ea9484b5dde30da32cd69913ab4a1ad2eb4aa8c77e4dbb69d68262539a9a5940c2b01418807c&scene=21#wechat_redirect)

[Palo Alto 再次修复一个严重的 PAN-OS 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247493998&idx=2&sn=bd1a18589634606e0ff70f17de914bfa&chksm=ea94d804dde35112f7323ae883a236262d671771d6b6d019bbec44a870d8e3f2898d89f4f647&scene=21#wechat_redirect)

[美网络司令部：马上修复严重的 PAN-OS 漏洞，免遭国家黑客攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247493807&idx=2&sn=39218cc6b67344d48d49fa4dbc62eeca&chksm=ea94d9c5dde350d3119c58d0bee936cd352f2d7fa036451f6038c1938dc88e5ef0ee19604e8f&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/palo-alto-networks-warns-of-potential-pan-os-rce-vulnerability/

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