---
title: 速更新！Sophos 热修复严重的防火墙漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521868&idx=1&sn=62d6c6882cbe7ca4516d3b679eea7dfa&chksm=ea94a726dde32e301b12f414868b0e6781c25f64fd9abbfe3612bcf308592daf167e1efbf01e&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-24
fetch_date: 2025-10-06T19:40:24.428989
---

# 速更新！Sophos 热修复严重的防火墙漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMS3dSnia69SWCrt9NxYPZMibo52ibaEszib3d74vIw9ia9wuEJ2M4iaD8YPUzibefmxUelkV64VAdzY5UKuw/0?wx_fmt=jpeg)

# 速更新！Sophos 热修复严重的防火墙漏洞

Ravie Lakshmanan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**Sophos 发布热修复方案，修复了位于 Sophos 防火墙产品中的三个漏洞。这些漏洞可用于实现远程代码执行并在一定条件下导致提权访问系统。**

在这三个漏洞中，其中两个是“严重”等级，目前尚未有证据表明这些漏洞已遭在野利用。漏洞概述如下：

* CVE-2024-12727（CVSS 9.8）：在邮件防护特性中存在的预认证SQL注入漏洞。如SPX的某些配置已启用且防火墙以“高可用性 (HA)” 模式运行，则可利用该漏洞实现远程代码执行。
* CVE-2024-12728（CVSS 9.8）：因HA集群的推荐和非随机SSH登录密码而导致的弱凭据漏洞。即使在HA设立过程完成后仍然呈活跃状态，因此如SSH为启用状态，则仍可暴露权限提升的账户。
* CVE-2024-12729（CVSS评分8.8）：位于User Portal 中的认证后代码注入漏洞，可导致认证的用户获得远程代码执行权限。

Sophos 表示，CVE-2024-12727影响约0.05%的设备，而CVE-2024-12728影响约0.5%的设备。所有这三个漏洞均影响 Sophos 防火墙21.0 GA (21.0.0)及更老旧版本。漏洞已分别在如下版本中修复：

* CVE-2024-12727 - v21 MR1 和更新版本（v21 GA、v20 GA、v20 MR1、v20 MR2、v20 MR3、v19.5 MR3、v19.5 MR4、v19.0 MR2的热修复方案）
* CVE-2024-12728 - v20 MR3、v21 MR1和更新版本（v21 GA、v20 GA、v20 MR1、v19.5 GA、v19.5 MR1、v19.5 MR2、v19.5 MR3、v19.5 MR4、v19.0 MR2、v20 MR2的热修复方案）
* CVE-2024-12729 - v21 MR1和更新版本（v21 GA、v20 GA、v20 MR1、v20 MR2、v19.5 GA、v19.5 MR1、v19.5 MR2、v19.5 MR3、v19.5 MR4、v19.0 MR2、v19.0 MR3的热修复方案）

为了确保已应用这些热修复方案，建议用户按照如下步骤检查：

* CVE-2024-12727 –打开设备管理 > Sophos 防火墙控制台Advanced Shell 并运行命令 "cat /conf/nest\_hotfix\_status" （如值为320或更大，则表明该热修复方案已应用）
* CVE-2024-12728 和 CVE-2024-12729 – 从Sophos 防火墙控制台启动设备控制台，并运行命令"system diagnostic show version-info" （如值为 HF120424.1或后续数字，则表明热修复方案已应用）

作为临时的应变措施，Sophos 呼吁客户仅向从物理上隔开的专门HA链接提供SSH访问权限，并/或使用足够长且随机的自定义密码来重新配置HA。另外，用户也可通过SSH禁用WAN访问权限并确保User Portal 和 Webadmin 并未暴露到WAN。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Sophos 修复位于 Sophos Web Appliance 设备中的三个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516210&idx=3&sn=feeedf873b800fb3d1e85197987d1eb2&scene=21#wechat_redirect)

[速修复！Sophos 防火墙中的RCE 0day已遭利用](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514074&idx=1&sn=849d683aa4c7d4ef90f9f8b7e1c2da9c&scene=21#wechat_redirect)

[Sophos 修复严重的防火墙 RCE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247511119&idx=3&sn=45f5b07eaf6a54d9147bacab7075348d&scene=21#wechat_redirect)

[Sophos 和 ReversingLabs 公开含2000万个 PE 文件的数据集](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247499163&idx=3&sn=77cc6cb13a2c66ca6758b2d18c02f3c8&scene=21#wechat_redirect)

[Sophos 修复 Cyberoam OS 中的 SQL 注入漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247498802&idx=2&sn=f481361fa7963f4f1b2b9a57c5c54312&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/12/sophos-fixes-3-critical-firewall-flaws.html

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