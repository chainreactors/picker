---
title: 思科修复由NSA报送的两个高危漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520566&idx=1&sn=74a7817b3955a25dccb8da1009e1b185&chksm=ea94a05cdde3294ad5842ade4355f86f5346f7c319e2260c6999b9fc84577eeff1b3f257c0f3&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-24
fetch_date: 2025-10-06T18:05:10.148321
---

# 思科修复由NSA报送的两个高危漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS1elmCicrrYpBic6THusP5OKqhV9Fv8aOxLeDEW3F6jn8ibefZGAp3jZQx1PGYK7y8vdlFlqWU9hbpA/0?wx_fmt=jpeg)

# 思科修复由NSA报送的两个高危漏洞

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**本周三，思科修复了多款产品中的多个漏洞，其中一个是位于企业协作解决方案中的高危漏洞CVE-2024-20375。**

CVE-2024-20375是一个高危漏洞（CVSS评分8.6），影响思科 Unified Communications Manager (Unified CM) 和思科 Unified Communications Manager Session Management Edition (Unified CM SME) 的SIP调用处理功能，可遭未认证远程利用。

SIP 信息解析不当可导致攻击者将构造的数据包发送给受影响产品并导致设备重新加载，进而导致拒绝服务条件。思科指出，目前虽然该漏洞已存在应变措施，但 Unified CM 和 Unified CM SME版本12.5 (1)SU9、14SU4和15SU1已包含补丁。

思科致谢美国国安局 (NSA) 报送CVE-2024-20375并提到并未发现该漏洞遭在野利用的证据。

本周三，思科还修复了另外一个漏洞CVE-2024-6387，即OpenSSH 漏洞regreSSHion，并提供了修复方案。此外，思科还发布四份安全通告，详述了位于 Identity Service Engine (ISE)、Unified CM 和 Unifeid CM SME中的多个中危漏洞。其中三个位于思科ISE中：通过REST API调用的SQL盲注漏洞、信息泄露漏洞以及跨站请求伪造漏洞。第四个漏洞影响 Unified CM和Unified CM SME 基于web 的管理接口，并可导致远程未认证攻击者执行跨站点脚本攻击，并在接口上下文中执行任意脚本代码。

思科表示并未发现这些漏洞遭在野利用的迹象。可参见思科安全通告页面获取更多信息。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[NSA 的开源员工培训平台 SkillTree 中存在CSRF漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520038&idx=2&sn=921e2fe11a431d8a458188b65d0a3b9d&chksm=ea94be4cdde3375abbf6e79690d31fd0c1e2f7bdc02b738a8fc06afa426d4a95adedea7492d3&scene=21#wechat_redirect)

[1.4GB的NSA机密数据遭泄露](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520021&idx=2&sn=694e77ee0ab92103cad4f3e0d1ad5a8c&chksm=ea94be7fdde337697f22a519c7599222567b8d5a4c460482a532eb7609ffd04faa814f5458b2&scene=21#wechat_redirect)

[NSA提醒称朝鲜黑客正在利用薄弱的DMARC邮件策略](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519419&idx=2&sn=2bf4ebf6392d40174b31ed1eb866cb87&chksm=ea94bdd1dde334c7bcc430b56eed6790831e607ff3ae1f75e6e7007dbbaa5a57e477d02a058e&scene=21#wechat_redirect)

[微软：APT28 利用由NSA报送的 Windows 漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519350&idx=2&sn=c98c01499f531e3ceed8f1597c30c578&chksm=ea94bd1cdde3340a7c757c539d7f708d85af2ff07df6f7ceeb2c4755fea809a41f36f2e1ab53&scene=21#wechat_redirect)

[NSA承认购买敏感数据监控美国公民](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518768&idx=1&sn=e2580ef28e29b1e69a98c2d5b0a25a4f&chksm=ea94bb5adde3324ca571dfc3d000c70d5f96bcd859fdf0d43446b2a97535d3a9ba37918b7ef1&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/cisco-patches-high-severity-vulnerability-reported-by-nsa/

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