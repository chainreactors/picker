---
title: 遭活跃利用的GoAnyWhere MFT 0day 补丁发布
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515504&idx=2&sn=59769cc0918ffbe4502f46bca1f3a6a9&chksm=ea948c1adde3050ccb386f6f3f2e1851f4b3aec399d1c496bf1ed6b4355e88d7aeb87a86d249&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-02-09
fetch_date: 2025-10-04T06:07:49.148612
---

# 遭活跃利用的GoAnyWhere MFT 0day 补丁发布

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSes79e9mQdCBStR8BqfbxEL4t0ZIRYV6jfMnz4cHfXqMkTsGgUicfzqANv0Ez8LX45gVhJtaGsfQg/0?wx_fmt=jpeg)

# 遭活跃利用的GoAnyWhere MFT 0day 补丁发布

Eduard Kovacs

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**最近爆出的GoAnyWhere 管理文件传输 (MFT) 软件的0day 补丁已发布。大约一周前有新闻报道称该漏洞已遭活跃利用，不过目前的攻击细节尚未披露。**

2月1日，Fortra（此前名称为HelpSystems）通知GoAnywhere MFT用户注意一个“远程代码注入利用0day”。之后该公司还发布了两份其它安全通知，每份通知都提供了缓解措施和妥协指标 (IoCs)。

该漏洞是一个远程代码注入漏洞，攻击者需要访问该应用的管理员控制台才能利用它。安全研究员Kevin Beaumont 指出，目前互联网上可公开访问1000多个本地实例，其中多数位于美国。

Rapid7公司的安全研究员Caitlin Condon指出，“Krebs 发布的关于Fortra的公告，建议GoAnywhere MFT客户查看所有管理员用户并监控未识别的用户名称，尤其是由系统创建的用户名。逻辑推理是Fortra可能会看到后续的攻击者行为如创建新的管理员或者其它用户，从而接管或在易受攻击的目标系统上维护持久性。”该公司还表示，威胁者可能会利用复用、薄弱或默认凭据获得对该控制台的管理员权限。

目前，GoAnywhere 0day的补丁已发布，建议用户紧急更新至GoAnywhere MFT 7.1.2版本。该公司指出，“尤其对于运行暴露在互联网上的管理员门户的客户而言，我们认为这样做刻不容缓”。

目前尚不存在相关攻击的任何信息。目前尚不清楚该漏洞遭国家黑客组织还是受经济利益驱动的网络犯罪分子利用。

该漏洞尚未获得CVE编号。

Fortra公司提心根用户检查日志文件中是否存在某特定代码行，提示系统已遭攻击。如该日志文件提示攻陷迹象，则用户应查看是否存在可疑的管理员用户。

某安全研究员已发布该0day的技术详情以及PoC 利用。

Shodan 搜索结果显示存在近1000个暴露在互联网上的GoAnywhere 实例。然而，Fortra 提到利用要求访问应用的管理控制台，且至少其中某些被暴露的实例与该产品的web客户端接口存在关联。该接口不受漏洞影响。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[苹果修复已遭利用的第10个0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515027&idx=1&sn=93ebe9404e1ead6aa5f784abf7fab31a&chksm=ea948af9dde303ef597a5e12dd8faab95e3127a6e8214fe9cdfba93dbcd4e59095001090e30f&scene=21#wechat_redirect)

[【BlackHat】利用多个0day将安全产品转变为擦除器](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514951&idx=1&sn=3ed4ef80c1329e08e7f64463d1fdad66&chksm=ea948a2ddde3033b5922485a64e1d6fca064810724e15a0778d8b0e791121dc63af1d8b8b1d3&scene=21#wechat_redirect)

[谷歌紧急修复今年已遭利用的第9个0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514887&idx=1&sn=7a847e96a21c6cc06818980f855c1cc5&chksm=ea948a6ddde3037b673a148848634d0acbb2f968051fa0ab8a8cda49528d3d0ff7fe2522465e&scene=21#wechat_redirect)

[谷歌紧急修复已遭利用的Chrome 0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514771&idx=2&sn=82231141505568820fbd6a3f66546680&chksm=ea948bf9dde302ef5d8114281a47daf92a67743ea8eba6632472a813a8d656b261c788586d1e&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/patch-released-for-actively-exploited-goanywhere-mft-zero-day/

题图：Pixabay License‍

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