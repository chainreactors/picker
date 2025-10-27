---
title: Zabbix 修复开源企业网络监控工具中严重的SQLi漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521662&idx=1&sn=f6345622bb66821f5bf5fcb0e222aa43&chksm=ea94a414dde32d028c675ddcd14b0de88fa05b1d2e477b937d155ee4040b22bf2be4dd0c664b&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-04
fetch_date: 2025-10-06T19:38:46.580616
---

# Zabbix 修复开源企业网络监控工具中严重的SQLi漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMShIM3W4kDlRhQev1NIsmKPUUzo6H6Q2X62R6O4hLyCKAlNtHdEP1otoB8IxickmiaHXN1Rnpaex2eg/0?wx_fmt=jpeg)

# Zabbix 修复开源企业网络监控工具中严重的SQLi漏洞

Ionut Arghire

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMShIM3W4kDlRhQev1NIsmKPqykjXIX85BYSTyKWnNdczkLcnmB93uFlT9zHpiaR7c7ZxRkE1SmHu8g/640?wx_fmt=png&from=appmsg)

**Zabbix 提醒称其开源企业网络监控解决方案中存在一个严重漏洞，可导致攻击者注入任意SQL查询并攻陷数据或系统。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMShIM3W4kDlRhQev1NIsmKPfoa6IvF8ibibzNGc4T5jfueNibZpAl083TG9xaswwibW1m6mJLksHz504Q/640?wx_fmt=gif&from=appmsg)

该漏洞的编号是CVE-2024-42327（CVSS评分9.9），位于任何拥有API访问权限可访问的一个函数中。Zabbix 公司发布安全公告提到，“Zabbix 前端上拥有默认用户角色的非管理员用户账户，或者其它具有API访问权限的角色可利用该漏洞。addRelatedObjects 函数中的CUser 类中存在一个SQLi 漏洞。任何具有API访问权限的用户均可从 Cuser.get 函数中调用 addRelatedObjects 函数。”

Qualys 公司分析指出，利用该漏洞可导致攻击者提升权限并获得对易受攻击 Zabbix 服务器的完全控制权限。该公司已发现超过8.3万台暴露在互联网中的 Zabbix 服务器。

Zabbix 公司提到，该漏洞影响 Zabbix 6.0.0至6.0.31、6.4.0至6.4.16以及7.0.0版本。

尽管关于CVE-2024-42327的安全公告在上周发布，但补丁已包含在7月份发布的6.0.32rc1、6.4.17rc1以及7.0.1rc1版本中。

已打补丁版本还修复了认证绕过漏洞CVE-2024-36466（CVSS评分8.8），它可导致攻击者签名伪造的zbx\_session cookie 并以管理员权限登录。Zabbix 7.0.1rc1 还修复了一个不受控的资源耗尽漏洞CVE-2024-36462，它可触发DoS 条件。

Zabbix 公司并未提及这些漏洞是否已遭在野利用，建议用户尽快更新至打补丁版本。该公司提到，其监控解决方案用于全球各行各业如教育、金融、视频、医疗、IT、制造以及零售等。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[CISA：攻击者正在利用开源Zabbix服务器中的多个漏洞！](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510695&idx=2&sn=295672c634bf9739529ccf7735124e13&scene=21#wechat_redirect)

[很多中小企业都在用的3款开源软件被曝多个漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247506589&idx=2&sn=2980b15eb914753d2fb6abd6f582b565&scene=21#wechat_redirect)

[大企业都在用的开源 ForgeRock OpenAM 被曝预认证 RCE 0day](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247506349&idx=2&sn=c1cd744877e475629005b1d5af227712&scene=21#wechat_redirect)

[速修复！开源企业自动化软件 Apache OFBiz 出现严重的 RCE 漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247502622&idx=1&sn=12df79a45c757bcc514a753b0bebe1a2&scene=21#wechat_redirect)

[FBI紧急警告：黑客利用开源SonarQube实例窃取政府和企业源代码](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247496316&idx=2&sn=7aee6b781a594691c0495f66f7b7e7cc&scene=21#wechat_redirect)

**原文链接**

https://www.securityweek.com/critical-vulnerability-found-in-zabbix-network-monitoring-tool/

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