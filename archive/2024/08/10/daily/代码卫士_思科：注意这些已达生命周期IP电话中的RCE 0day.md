---
title: 思科：注意这些已达生命周期IP电话中的RCE 0day
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520401&idx=2&sn=bad61fd4a7dd0064d773564100fa0d93&chksm=ea94a1fbdde328ed9792a7787f0942bd8375dfb3d8e89c5d0413c4d48ad449acff958b59a1b2&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-08-10
fetch_date: 2025-10-06T18:05:18.894475
---

# 思科：注意这些已达生命周期IP电话中的RCE 0day

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMR1tCF9tdmOaANhCQa7yohF9LcAcvRoYcMMOD7dHEU0NcXBvndcwQosibLnSkAziaAeIBDmezIdT0TA/0?wx_fmt=jpeg)

# 思科：注意这些已达生命周期IP电话中的RCE 0day

Bill Toulas

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**思科提醒称，已达生命周期的 Small Business SPA 300和SPA500 系列IP电话中存在多个严重的远程代码执行 (RCE) 0day 漏洞。思科并未发布修复方案和缓解建议，因此用户必须尽快升级至更新的以及受活跃支持的机型。**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMR1tCF9tdmOaANhCQa7yohFwCWOq9F4ibJSNtm6glVs4TBJribH4XhwbhaMuZCgGxevVhic9V3vhgQeQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMR1tCF9tdmOaANhCQa7yohFEDxfG6YTqVI2y6pTPytq4NXDwPaVic9Yyxtibwiad6YTXv7KjcVzBLdAw/640?wx_fmt=png&from=appmsg)

**漏洞详情**

思科共发现了五个漏洞，其中三个是严重级别（CVSS v3.1评分9.8）和两个高危漏洞（CVSS v3.1 评分7.5）。这些漏洞的编号是CVE-2024-20450、CVE-2024-20452和CVE-2024-20454。

这些缓冲溢出漏洞可导致未认证的远程攻击者，通过向目标设备发送特殊构造的HTTP 请求，以 root 权限在底层 OS 上执行任意命令。思科在安全通告中提到，“成功利用可导致攻击者溢出一个内部缓冲区并以root权限执行任意命令。”

这两个高危漏洞是CVE-2024-20451和CVE-2024-20453，是由对HTTP数据包上的检查不当导致的，可导致恶意数据包在受影响设备上引发拒绝服务。思科表示，所有这五个漏洞影响在SPA300和SPA500 IP 电话上运行的所有软件发布，不管软件的配置如何，它们之间是独立的，即可遭单独利用。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMR1tCF9tdmOaANhCQa7yohFEDxfG6YTqVI2y6pTPytq4NXDwPaVic9Yyxtibwiad6YTXv7KjcVzBLdAw/640?wx_fmt=png&from=appmsg)

**支持终止**

思科支持门户提到，SPA300 的最后一次出售时间是2019年2月，并在三年后终止支持。对于SPA 500而言，思科在2020年6月1日起终止出售。不过值得注意的是，思科仍然为服务合同或特殊保证条件的客户保留2025年5月31日前的SPA500服务，但SPA300自2024年2月29日起就不再受支持。

这两款设备均不会获得安全更新，因此建议用户升级至更新的受支持机型，如Cisco IP Phone 8841或Cisco 600系列设备。思科还提供“技术迁移计划”，允许用户交易符合条件的产品并获得购买新设备的积分。无法确定选择哪种方式的用户可联系思科的技术支持中心。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[国家黑客组织利用思科两个0day攻击政府网络](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519358&idx=1&sn=080e82a553f5a1d52ba96fc6f20d14c3&chksm=ea94bd14dde33402ba398352628a6ab2995cc8e1c950313b8a1b9fb5752d5c3d7a2f00098df9&scene=21#wechat_redirect)

[罗克韦尔自动化称 Stratix 交换机受思科0day影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517980&idx=1&sn=ffc848776d7e9915b3d800a23587fda9&chksm=ea94b676dde33f6029a679ed808213cb1d41ffd5a8ca6b04cf84a414175c08db3c21817c5f49&scene=21#wechat_redirect)

[思科新0day 被用于在数千台设备上植入恶意后门 Lua](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517960&idx=1&sn=a77de274fb21796ddac20805028ec8b0&chksm=ea94b662dde33f74645e70725b4ffb565280e526d7c94ee2cbd1c5177a6c3330dc1b383922b3&scene=21#wechat_redirect)

[思科披露称严重的 IOS XE 认证绕过0day已遭利用](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517910&idx=1&sn=8fb7babd282149838a933250b863edc8&chksm=ea94b7bcdde33eaa96070746c3597032b223e499e281eb14ab47149dc366af11b935031b6706&scene=21#wechat_redirect)

[高危无补丁0day影响思科数据中心交换机，可导致加密流量遭篡改](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516974&idx=2&sn=179eead740cfb91b376bafa02e4fcb99&chksm=ea94b244dde33b524d84c5fad51227142548b6794645504ad026ef59442f37d9388673b96ff7&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/google-fixes-android-kernel-zero-day-exploited-in-targeted-attacks/

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