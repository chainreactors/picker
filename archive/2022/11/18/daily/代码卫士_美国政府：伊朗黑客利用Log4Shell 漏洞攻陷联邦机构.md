---
title: 美国政府：伊朗黑客利用Log4Shell 漏洞攻陷联邦机构
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514661&idx=2&sn=059d03a2384d5d57513f1e02a69f1f4d&chksm=ea948b4fdde3025977bec54f5099ef0554974ed2c2a16b192b61bd98eb58875466740d94e666&scene=58&subscene=0#rd
source: 代码卫士
date: 2022-11-18
fetch_date: 2025-10-03T23:07:28.938602
---

# 美国政府：伊朗黑客利用Log4Shell 漏洞攻陷联邦机构

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMRRVuZceCBAOzn5DXmYd0zlnn8n9SCsSwvyphXoe91xoB3iac4MCL7iaRWA7OsG3M6Q8meKHf2t48Xg/0?wx_fmt=jpeg)

# 美国政府：伊朗黑客利用Log4Shell 漏洞攻陷联邦机构

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**美国FBI和CISA发布联合公告指出，未具名伊朗威胁组织入侵了联邦民事行政部门 (FCEB) 所属一家组织机构并部署了XMRig 挖矿恶意软件。**

攻击者利用远程代码执行漏洞Log4Shell (CVE-2021-44228) 的exploit 入侵了一台未修复的VMware Horizon 服务器。部署密币挖矿机后，伊朗威胁组织还在受陷服务器上设置了反向代理，在FCEB的网络中维持可持久性。

联合公告指出，“在事件响应活动过程中，CISA认为威胁组织利用了未修复VMware Horizon 服务器中的Log4Shell 漏洞，安装了XMRig密币挖掘软件，横向移动到域控制器 (DC)，攻陷凭据，之后在多个主机上植入Ngrok反向代理以维持持久性。”

FBI和CISA还提到，所有尚未修复VMware系统中Log4Shell 漏洞的组织机构应当假设自己已遭攻陷，并建议这些机构在网络中查找恶意活动。CISA在6月份提醒成，VMware Horizon 和 UAC服务器仍受多个威胁组织侵扰，其中不乏受国家支持的黑客组织。Log4Shell 可被远程用于攻击暴露到本地或互联网访问权限的易受攻击服务器，在受陷网络中横向移动，访问存储着敏感数据的内部系统。

**国家黑客组织正在利用Log4Shell**

在2021年12月发布后，Log4Shell 漏洞几乎立即遭到威胁组织的扫描和利用，其中包括国家黑客组织。

CISA当时也提醒使用易受攻击VMware服务器的组织机构假设自己已遭攻陷并启动威胁捕猎活动。VMware还在1月份督促客户尽快保护VMware Horizon 服务器免遭Log4Shell 攻击。

CISA和FBI在报告中强烈建议组织机构采取缓解和防护措施，包括：

* 将受影响VMware Horizon 和 UAG系统更新至最新版本
* 将组织机构面向互联网的攻击面最小化
* 演练、测试和验证所在组织机构安全计划针对映射到企业框架的MITRE ATT&CK 的威胁行为的情况。
* 测试所在组织机构现有安全控制对公告中提到的ATT&CK技术的效果。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[在线阅读版：《2022中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513174&idx=1&sn=e474d1ea23ed7cce10e2ae2f872fc003&chksm=ea94853cdde30c2a963cfa00a536764ea55cdee7ba6ef4a7716a28f82a97ca630dc271ee5224&scene=21#wechat_redirect)

[在线阅读版：《2021中国软件供应链安全分析报告》全文](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247505380&idx=1&sn=01d2f5af200abc6bb20411ee8f17b6b5&chksm=ea94e48edde36d98f20b66aecf9f359e49226b411872bcea527fcca0a5de018f407415313800&scene=21#wechat_redirect)

[速修复！Apache Commons Text 存在严重漏洞，堪比Log4Shell](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247514246&idx=1&sn=05c9cf544ef37daf01a04001b22b2584&chksm=ea9489ecdde300fae250e9a720d8fb6ccb7704229f946b796c6aec685c3e6a9446169ec5ad12&scene=21#wechat_redirect)

[黑客组织利用Log4Shell 漏洞攻击美国能源企业](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513979&idx=2&sn=72d6d5f48f01c937bda9d937519e416b&chksm=ea948611dde30f07cbdbf693f897a3068064aeca2729ee662032e6292a8aaa911ce77b17f7e2&scene=21#wechat_redirect)

[奇安信发布《2022中国软件供应链安全分析报告》 谁会成为下一个Log4j2？](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247513172&idx=1&sn=5c228a525bd6eb94d24f697d88af3c6d&chksm=ea94853edde30c2897319ed8aac13685ecca7d05bf4ecdee1d9b30c9d7f4faf24df0c1a993d2&scene=21#wechat_redirect)

[微软：攻击者利用SolarWinds Serv-U 0day发动 Log4j 攻击](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247510233&idx=2&sn=26931bdef44b8579be16fb59abe06f2e&chksm=ea9499b3dde310a5384a230a39a6732eeb2d9db56ce3bef75f12a3c9921af7a27b64fb660e1e&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/us-govt-iranian-hackers-breached-federal-agency-using-log4shell-exploit/

题图：Pexels License‍

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