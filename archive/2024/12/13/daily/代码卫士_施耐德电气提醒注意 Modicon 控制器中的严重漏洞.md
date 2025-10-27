---
title: 施耐德电气提醒注意 Modicon 控制器中的严重漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521773&idx=2&sn=9334dce8b280dba2dd408a1b5854e232&chksm=ea94a487dde32d9163abde86ace9b63ba55a88d022c03411d8072763533dd6664a1afb906710&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-13
fetch_date: 2025-10-06T19:38:40.832908
---

# 施耐德电气提醒注意 Modicon 控制器中的严重漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQaYHjeLoEv3R4T7PI8tFRohRiceZwn6yQ8pia0iaB0aWZvys28BjiaibegwDxy7qgzrNDbGcZzqicz80gQ/0?wx_fmt=jpeg)

# 施耐德电气提醒注意 Modicon 控制器中的严重漏洞

securityonline

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**施耐德电气发布一份安全通知，提醒注意 Modicon M241、M251、M258和LMC058 可编程逻辑控制器 (PLCs) 中的一个严重漏洞CVE-2024-11737（CVSS评分9.8）。该漏洞可导致攻击者引发拒绝服务攻击并攻陷该控制器的完整性。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQaYHjeLoEv3R4T7PI8tFRoFaLuscYbbvpwRXczVlBGxJ40tiaRM3iawxic54cvj0icN2xk5yiaSbQVvFA/640?wx_fmt=gif&from=appmsg)

该漏洞影响 Modicon M241、M251、M258和LMC058 PLCs 的所有版本。这些控制器用于多种工业自动化应用中如制造业、能源和交通行业。

施耐德电气公司目前正在着手推出修复方案，同时建议客户采取如下缓解措施：

* 仅在受保护环境中使用控制器和设备，将网络暴露最小化并确保无法从公开互联网或不可信网络访问。
* 通过嵌入式防火墙过滤端口和IP。
* 设置网络分段并部署防火前，拦截所有对502/TCP的越权访问。
* 禁用所有的未使用协议（默认配置）。

施耐德电气公司还推荐客户阅读《ExoStruxure Machine Expert、Modicon 和 PacDrive 控制器网络安全指南》以及相关联设备的用户手册获取如何保护PLCs 安全的详细信息。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[能源巨头施耐德电气遭勒索攻击](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518779&idx=2&sn=fc541cc2a46dc855480ebc0adc836ae1&scene=21#wechat_redirect)

[西门子爱立信施耐德电气等：欧盟《网络安全弹性法案(CRA)》或破坏供应链](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518086&idx=1&sn=f13ff428d3f9ed6d4ea180de7154309a&scene=21#wechat_redirect)

[工控补丁星期二：西门子、施耐德电气等修复50个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517016&idx=2&sn=8edf5db583691ce70b6b4910729e5c5b&scene=21#wechat_redirect)

[施耐德电气 UPS 软件中存在严重的未认证 RCE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516335&idx=1&sn=d6970653344d43075615c17ff16238fe&scene=21#wechat_redirect)

[多个漏洞可导致施耐德电气继电器遭重启或设备遭接管](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510739&idx=4&sn=96c3f57363e08e0b1c5d095730bfa726&scene=21#wechat_redirect)

**原文链接**

https://securityonline.info/schneider-electric-warns-of-critical-flaw-in-modicon-controllers-cve-2024-11737-cvss-9-8/

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