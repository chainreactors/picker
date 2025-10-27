---
title: Fortinet FortiOS漏洞被用于攻击政府实体
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515912&idx=1&sn=0d48724c08d4d63949a7142683b6fdd7&chksm=ea948e62dde30774b504e3a089bab575daf337854bba663d40f81014b5672260b74230a007a3&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-15
fetch_date: 2025-10-04T09:36:09.513227
---

# Fortinet FortiOS漏洞被用于攻击政府实体

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTNe8aQJNdzWPhAAqvKBpa4zu2VVOGdNT7ePuxDj5t4BTeXgEwHRlElEju7uXu86fOuhhiaGoQ3Cvg/0?wx_fmt=jpeg)

# Fortinet FortiOS漏洞被用于攻击政府实体

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTNe8aQJNdzWPhAAqvKBpa4icIp1xLaHDbYv29n3O7gricY7EEORkfL1eSlibuSBUPTBO7y8Lm2946VA/640?wx_fmt=png)

**未知威胁组织正在利用Fortinet FortiOS 中的一个0day漏洞 (CVE-2022-41328)，攻击政府实体和大型组织机构，窃取数据并损坏操作系统和文件。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTNe8aQJNdzWPhAAqvKBpa4PppQI3TLyPLoFm9wSaOA2mDaibXpFU4ObaHxOxbXo2amctYUD7xp4Mg/640?wx_fmt=png)

Fortinet公司的研究员 Guillaume Lovet和Alex Kong 在上周发布的安全公告中指出，“利用的复杂度表明攻击者是高阶攻击者，并且正在高度集中攻击政府或与政府相关的目标。”

CVE-2022-41328的CVSS评分为6.5，是一个位于FortiOS中的中危路径遍历漏洞，可导致任意代码执行后果。

Fortinet 公司提到，“位于FortiOS 中的路径遍历漏洞可能导致特权攻击者，通过构造的CLI命令，读和写任意文件。”

该漏洞影响 FortiOS 版本6.0、6.2、6.4.0至6.4.11，7.0.0至7.0.9，以及7.2.0至7.2.3。修复方案已分别在版本6.4.12、7.0.10和7.2.4中发布。

前几天，Fortinet公司就发布补丁，修复了15个漏洞，其中包括CVE-2022-41328和一个影响FortiOS和FortiProxy的严重的堆缓冲区下溢漏洞（CVE-2023-25610，CVSS评分9.3）。

Fortinet公司指出，某客户的多款FortiGate设备遭“突然的系统停止和随后启动失败”，说明完整性遭攻击。进一步分析该事件表明，攻击者修改了设备的固件镜像，包含了一个新的payload (“/bin/fgfm”)， 在启动流程开始之前就一直总是启动的状态。该 /bin/fgfm 恶意软件旨在与远程服务器建立联系，从受陷主机中下载文件、提取数据并获得远程shell访问权限。该固件中发生的其它变化使得攻击者能够获得持久访问和控制权限，更不用说在启动时禁用固件验证。

Fortinet 公司表示，该攻击具有高度针对性，主要目标是政府组织机构或与政府相关的组织机构。鉴于利用的复杂性，攻击者可能“深入了解FortiOS 和底层固件”，并能够处理高阶能力，逆向FortiOS操作系统的不同方面。

目前尚不清楚该攻击者是否与今年1月早些时候利用FortiOS SSL-VPN  (CVE-2022-42475) 部署Linux 植入的入侵事件有关。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[奇安信入选全球《软件成分分析全景图》代表厂商](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515374&idx=1&sn=8b491039bc40f1e5d4e1b29d8c95f9e7&chksm=ea948d84dde30492f8a6c9953f69dbed1f483b6bc9b4480cab641fbc69459d46bab41cdc4859&scene=21#wechat_redirect)

[美国：APT 组织正在利用 Fortinet FortiOS 发动攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247503245&idx=3&sn=856f262b27f3310cf14d0eaafade5f5c&chksm=ea94fce7dde375f100cb59392a9ae514a6174d710990f6583117019c4df9a7761da88d23d49c&scene=21#wechat_redirect)

[Fortinet：注意这个严重的未认证RCE漏洞！](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515862&idx=1&sn=d2ef6b5ab51eba3e97af531d1a8b212b&chksm=ea948fbcdde306aa2d71b31b492175fc0c01a69233601e35fc9fee73fbfbae62668f3aaaffb2&scene=21#wechat_redirect)

[Fortinet修复两个严重的RCE漏洞，其中一个两年前就发现？](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515647&idx=1&sn=b8f00a46755a56f7d9aed5ae56c1b4e4&chksm=ea948c95dde305837c4ef5d418e236f9718061ffd9b877fde4fc8a267a7bf0b9910d885f6ea4&scene=21#wechat_redirect)

[Fortinet 紧急修复已遭利用的VPN漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514989&idx=1&sn=d69be3f378da5be4993977d510a35a5b&chksm=ea948a07dde303111a95aab98531af127bcaa9ad279aa46a8fbf4f7e56f0053a9bc6ba7c4ac8&scene=21#wechat_redirect)

[Fortinet 修复6个高危漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514392&idx=2&sn=d3a167944c3d8a1d891c716450e26210&chksm=ea948872dde3016465bc0576d1de3d5f0be89e0a4cf7ef01370a82224cb557ef613a3252ccd8&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2023/03/fortinet-fortios-flaw-exploited-in.html

题图：Pixabay License

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