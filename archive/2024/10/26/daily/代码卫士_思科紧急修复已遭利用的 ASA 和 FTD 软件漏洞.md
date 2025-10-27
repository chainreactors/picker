---
title: 思科紧急修复已遭利用的 ASA 和 FTD 软件漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521275&idx=1&sn=23094a8bbc6812308a558007e25112aa&chksm=ea94a291dde32b87e35eaab4a3eaca0db1c4a21c577bfdffa7e0bc64e4aa607f757182427737&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-10-26
fetch_date: 2025-10-06T18:53:59.204922
---

# 思科紧急修复已遭利用的 ASA 和 FTD 软件漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQiadzhZU8L1ToyibztB8NGkxfEjQ1wOZHRVkazRdMzTLaw8WYeromI2ibYIn9EPSWbdqicpD4bY4fdYg/0?wx_fmt=jpeg)

# 思科紧急修复已遭利用的 ASA 和 FTD 软件漏洞

THN

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQiadzhZU8L1ToyibztB8NGkxx0MR54icKyOSiciaRV4AZibRfZ82P1ZmWzWcAAsexM3jaWLia1w4FZxJHwA/640?wx_fmt=gif&from=appmsg)

**本周三，思科表示修复ASA中一个拒绝服务（DoS）漏洞CVE-2024-20481（CVSS评分5.8）。**

该漏洞影响思科 ASA 和 FTD 软件的远程访问VPN (RAVPN) 服务，因资源耗尽造成，可被未认证的远程攻击者用于在RAVPN 服务中引发 DoS。

思科在安全公告中提到，“攻击者可将大量 VPN 认证请求发送给受影响设备，利用该漏洞，可使攻击者耗尽资源，从而在受影响设备上造成 RAVPN 服务的 DoS。”

恢复 RAVPN 服务可能要求重新加载该设备，具体取决于攻击造成的影响。虽然目前尚不存在相关应变措施，但思科表示客户可采取如下建议，应对密码喷射攻击：

* 启用日志记录
* 为远程访问VPN服务配置威胁检测
* 应用加固措施如禁用AAA认证，以及
* 手动拦截未授权来源的连接尝试

值得注意的是，该漏洞已被攻击者恶意利用，是针对VPN和SSH服务的大规模暴力攻击的一部分。今年4月早些时候，思科 Talos 团队提到自2024年3月18日开始，针对VPN服务、web 应用认证接口和SSH服务的暴力攻击在增长。

这些攻击影响多家企业的多款设备，如思科、Check Point、Fortinet、SonicWall、MikroTik、Draytek 和 Ubiquiti。

思科 Talos 提到，“这些暴力攻击厂商利用特定组织机构的通用用户名和有效用户名。所有这些攻击似乎源自 TOR 出口节点和大量其它匿名隧道和代理。”

思科还修复了位于 FTD 软件、FMC 软件和ASA 中的其它三个严重漏洞：

* CVE-2024-20412（CVSS评分9.3）：适用于 Cisco Firepower 1000、2100、3100和4200系列的 FTD 软件中存在硬编码密码的静态账户，可导致未认证的本地攻击者通过静态凭据访问受影响系统。
* CVE-2024-20424（CVSS评分9.9）：FMC 软件的 web 管理接口中存在一个 HTTP 请求输入验证不当漏洞，可导致认证的远程攻击者在底层操作系统上以根身份执行任意命令。
* CVE-2024-20329（CVSS评分9.9）：位于ASA的SSH子系统中的用户输入验证不充分漏洞，可导致认证的远程攻击者以根身份执行操作系统命令。

鉴于网络设备中的漏洞易遭国家黑客利用，建议用户尽快修复。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[黑客在思科商店注入恶意JS，窃取信用卡和凭据](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520683&idx=3&sn=ca7a392b964011a90f44ef9b56046155&chksm=ea94a0c1dde329d7b3357897b0d476fbdcccdb403a0341d564f40687a51b08c0f26ca20939a6&scene=21#wechat_redirect)

[思科修复已有 PoC 的根提权漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520683&idx=1&sn=00f735c28afb0e6cc70f919cade9dc5c&chksm=ea94a0c1dde329d7537d32cf0cc038587d8e6da619b0dc82fb99bb8917e432ece7028a7dd65c&scene=21#wechat_redirect)

[思科：注意这些已达生命周期IP电话中的RCE 0day](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520401&idx=2&sn=bad61fd4a7dd0064d773564100fa0d93&chksm=ea94a1fbdde328ed9792a7787f0942bd8375dfb3d8e89c5d0413c4d48ad449acff958b59a1b2&scene=21#wechat_redirect)

[思科严重漏洞可导致黑客在SEG设备上添加 root 用户](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520104&idx=2&sn=7a044b182ec50064eba8b67fb588a968&chksm=ea94be02dde33714a87ec047348cf4004a40a24f05ca079479dd287aec723a3790919198933e&scene=21#wechat_redirect)

[思科ASA防火墙中存在多个漏洞，可被用于供应链攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513544&idx=2&sn=6c9886f2668674b71400b4eb1ccba93b&chksm=ea9484a2dde30db499db8f0b34a1e531a5db4571bb73988dfbc334e6409862d01a8840d94942&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2024/10/cisco-issues-urgent-fix-for-asa-and-ftd.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

修改于

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