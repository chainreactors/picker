---
title: 搬起石头砸自己的脚？微软DDoS 防御措施出错，放大Azure DDoS 攻击
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520290&idx=1&sn=f8e1d4976e81eb11cd167a284c9e9f49&chksm=ea94a148dde3285e0fd4130f93b4e1506903246a082b98d700215093869fa5da17f7cf806db9&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-02
fetch_date: 2025-10-06T18:03:23.872228
---

# 搬起石头砸自己的脚？微软DDoS 防御措施出错，放大Azure DDoS 攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS2ibibgibWdRp1DBia14h2Hib3L4GXhpMHQsQ9Kr8tZENAaVFeP8DFIJVyibeZPZo8BlOTECV4OibANNqVg/0?wx_fmt=jpeg)

# 搬起石头砸自己的脚？微软DDoS 防御措施出错，放大Azure DDoS 攻击

Richard Speed

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**配置微软Defender 时出错？你可能并不孤单：微软证实称实现防御措施时出错，加剧了本周二微软 Azure 的不稳定性。但必须提到的一点是，没有人在责怪这款产品：Windows Defender。**

微软指出，让全球 Azure 宕机的罪魁祸首是一次分布式拒绝服务 (DDoS) 共计。这类攻击并不少见，相反，它催生了一个产业。DDoS 攻击的目的是吞没目标系统的资源，通常涉及受恶意软件感染的多台机器通过网络流量对受害者发起洪水攻击。虽然管理员使用多种方法区分真实请求和恶意流量，但F5 Labs 公司提到，2023年 DDoS 攻击仍然爆炸式增长。

F5 Labs 公司提到，“攻击增长非常迅速，企业一年平均要处理大概11次DDoS 攻击，几乎是每月处理一次。”

而微软已发布抵御基于网络的 DDoS 攻击的策略，提到因公司的全球化性质，其策略是唯一的。微软表示，为此该策略能够“使用其它多数组织机构无法使用的策略和技术”，并从庞大的威胁网络中提取综合知识。微软提到，“这一情报，加上从在线服务收集的信息以及微软的全球客户技术，持续改进微软的DDoS 防御系统，保护所有微软在线服务资产的安全。”

不过，它的前提是微软真的正确地执行了这一策略。

**对于最近发生的 Azure 宕机事件，微软的 DDoS 防御机制确实得到了正确的触发。然而，响应却不尽人意。微软昨天承认，“初步调查显示，我们防御措施的实现出错，导致该攻击的影响得以放大而非缓解。”**

该问题是全球性的且影响尝试连接到多种服务的客户，包括 Azure App Services、Application Insights、Azure IoT Central、Azure Log Search Alerts、Azure Policy、、Azure 门户本身以及一些Microsoft 365 和Microsoft Purview 服务。

微软提到，该事件从世界协调时 (UTC) 11:45大概持续到19:43，尽管微软在14:10分提到该攻击的主要影响已得到成功缓解。然而，直到20:48，问题才宣告结束。

微软并未就DDoS 防御措施的实现问题进行回应。事后初步评估 (PIR) 报告的时限大概是72小时，微软将在约2个月后发布最终的PIR报告。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[零成本利用微软 Azure 自动化服务，开发出完全无法检测到的云密币挖矿机](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518099&idx=1&sn=b198a3d8cc28ad80889c2cf40d82baff&chksm=ea94b6f9dde33fef1ca2a76a5ba0d325a709bd9d0da2d6e07e6df8a80954abfa1889534c5d61&scene=21#wechat_redirect)

[研究员发现微软 Azure AD OAuth 应用中的账户接管漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516795&idx=1&sn=4e3841d5ec2df12ab173f87cfff65c6f&chksm=ea94b311dde33a0794d17d8242e150e4a00dd604aaa3e2a712d13b6b431abe63f1221d8e095e&scene=21#wechat_redirect)

[微软 Azure Bastion 和 Container Registry 中存在两个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516737&idx=1&sn=c4b5adfcf7e55915ef943fcfd4fd9a56&chksm=ea94b32bdde33a3d834b36d01e90e0a897698720411c56832829d175a4722dd94ba823e665d5&scene=21#wechat_redirect)

[SideWinder 网络攻击瞄准多个国家的海运设施](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520250&idx=2&sn=298380a43c5a67d741a887cc38f55bfb&chksm=ea94be90dde33786aa6c81860e706bc291434bd656bfc414301695529be20b340a55bc39b661&scene=21#wechat_redirect)

[四款微软Azure服务存在漏洞，可导致云资源遭越权访问](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515363&idx=3&sn=6c939ad71b9754325cf5e804212ce38e&chksm=ea948d89dde3049f9674c7caff6a7a10ad9243925974600a40bc322cfba7198f6d8f4e045dbf&scene=21#wechat_redirect)

**原文链接**

https://www.theregister.com/2024/07/31/microsoft\_ddos\_azure/

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