---
title: 日立能源证实受GoAnywhere攻击影响，数据遭泄露
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515971&idx=1&sn=eec17b15763175ee40e7ceff0749f511&chksm=ea948e29dde3073f5b0f7a3684d38fd09d8ea2a1545f32fdb0d03f46cd192742987741c20e29&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-21
fetch_date: 2025-10-04T10:09:19.920479
---

# 日立能源证实受GoAnywhere攻击影响，数据遭泄露

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRxp9icdIILIk8zmtIFl9Lia2icaY1oPaU861ibeNjT1d65DL36W0a9la4BQHlWAkzcJSwWqHmrgDO6Zw/0?wx_fmt=jpeg)

# 日立能源证实受GoAnywhere攻击影响，数据遭泄露

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**日立能源公司证实称，Clop 勒索团伙通过GoAnyway 0day漏洞窃取数据后，公司数据遭泄露。**

日立能源是日本工程技术巨头日立的一部分，专注于能源解决方案和电力系统，年收入达到1000亿美元。攻击者利用Fortra GoAnywhere MFT 中的0day  (CVE-2023-0669) 发动攻击。该漏洞首次披露于2023年2月3日。

日立公司在一份新闻声明中指出，“我们最近获悉第三方软件提供商FORTRA GoAnywhere MFT 成为CLOP 勒索团伙的受害者，攻击可能导致对某些国家员工数据的越权访问。”日立表示立即响应该事件，断开与受影响系统的连接并启动内部调查，判断数据泄露事件的影响。

所有受影响员工、可用数据防护机构和执法部门都收到日立公司直接发布的安全事件通知。声明指出，“截至目前，我们并未发现网络运营或客户数据的安全性或可靠性受陷的信息。”

**影响显现**

当Fortra公司在2023年2月初证实GoAnywhere 安全文件分享产品中存在0day 时，BleepingComputer就曾预计该事件可能与2021年类似产品Accellion FTA遭受的影响相似。

当时，Clop 勒索团伙利用漏洞，攻陷了全球很多高级别组织机构。2023年2月6日，CVE-2023-0669的PoC exploit 遭公开；2023年2月10日，Clop 团伙声称利用位于GoAnywhere MFT中的0day攻陷了130家组织机构。

首先证实成为受害者的是2月14日证实遭攻击的医疗巨头Community Health Systems (CHS)，随后在3月2日，金融科技平台Hatch银行也发布了类似声明。

几天后，Clop 勒索阻止开始活跃勒索Fortra公司的客户，勒索很多受害者换取被盗数据。2023年3月14日，网络安全公司Rubrik 证实称受攻击影响，但表示仅有非生产IT测试环境受影响，客户数据并不受影响。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[GoAnywhere 0day的首个受害者出现，CHS百万病患数据受影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515565&idx=2&sn=9f977b20406d11d9326758abfe4b1f97&chksm=ea948cc7dde305d162e43621927aa59b464f20b3c58f53371e378ef894fd790591ce9b4115ce&scene=21#wechat_redirect)

[遭活跃利用的GoAnyWhere MFT 0day 补丁发布](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515504&idx=2&sn=59769cc0918ffbe4502f46bca1f3a6a9&chksm=ea948c1adde3050ccb386f6f3f2e1851f4b3aec399d1c496bf1ed6b4355e88d7aeb87a86d249&scene=21#wechat_redirect)

[CISA提醒注意日立能源产品中的多个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515233&idx=2&sn=df29998bb260f1c274b561d8d33c1ed7&chksm=ea948d0bdde3041d86dd780d173b82a65374d35b5fc063d67de6fb5a4dde1e81e6b3d7805a8c&scene=21#wechat_redirect)

[CISA：注意影响Advantech 和日立工业设备的多个严重漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514269&idx=3&sn=42277be117ca4047c20dedbf1712beee&chksm=ea9489f7dde300e1a90950387af6f1655ca62e307fbb6644d0534ad880c3e4b3c475bed3e5fa&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/hitachi-energy-confirms-data-breach-after-clop-goanywhere-attacks/

题图：Pexels License

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