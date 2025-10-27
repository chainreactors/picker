---
title: Veeam 提醒注意VSPC中的严重RCE漏洞
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247521684&idx=1&sn=b5ba5835dc8937327b3ded698979f0f2&chksm=ea94a4fedde32de81ba198d63194acfd35654a0fb756fa23333f2f5a4738769841bd5d1834e2&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-12-05
fetch_date: 2025-10-06T19:38:35.895646
---

# Veeam 提醒注意VSPC中的严重RCE漏洞

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMTFvqKIG48Qz4fia63ypKZ16n4ZFuDjA7yGwicaHMamKKpXHHVgtO3D0Wx1gUVdicCUGAVYLdMXamGicQ/0?wx_fmt=jpeg)

# Veeam 提醒注意VSPC中的严重RCE漏洞

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMTFvqKIG48Qz4fia63ypKZ16IVaZNfAwt3os3ic4zpicmTByQFHaG1MBgYBAZulj8vQXsndS4RHMe1LQ/640?wx_fmt=png&from=appmsg)

**Veeam 发布安全更新，修复了在内部测试过程中发现的两个 Service Provider Console (VSPC) 漏洞，其中一个是严重的远程代码执行 (RCE) 漏洞。**

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMTFvqKIG48Qz4fia63ypKZ16qoaCf9t5BW2aSg7tpR9OUdbyLz0D2K8om7p3stmxuthZmSzyqQk2TQ/640?wx_fmt=gif&from=appmsg)

Veeam 提到，VSPC 是一款远程管理 BaaS（后端即服务）和DRaaS（灾难恢复即服务）平台，供服务提供商监控客户备份的健康和安全，并管理其受 Veeam 保护的虚拟、Microsoft 365 和公共云工作负载。

第一个漏洞是CVE-2024-42448（CVSS评分9.9），可导致攻击者在未修复的VSPC管理代理机器上的服务器执行任意代码。另外一个漏洞CVE-2024-42449可导致攻击者窃取VSPC服务器服务账户的 NTLM 哈希并通过所获取的访问权限删除 VSPC 服务器上的文件。不过Veeam 公司在安全公告中提到，只有当管理代理在目标服务器上获得授权，才能成功利用这两个漏洞。

这两个漏洞影响 VSPC 8.1.0.21377 和所有更早版本，包括 build 8和7，但不受支持的产品版本也可能受影响，并“应该考虑为易受攻击”，即使并未测试这些版本。Veeam 公司提到，“我们推荐使用受支持版本VSPC（版本7和8）的服务提供商更新至最新的积累补丁。强烈建议使用不受支持版本的服务提供商用户尽快更新至最新版本。”

最近针对Veeam 公司产品漏洞的在野利用情况表明，尽快修复易受攻击的服务器才能拦截潜在攻击活动。正如Sophos 公司X-Ops 事件响应团队在上个月提到的那样，Veeam 公司在9月份提到的VBR 软件中的RCE漏洞（CVE-2024-40711），正被用于部署勒索软件Frag。该漏洞还被用于在Akira 和Fog勒索攻击中所用的易受攻击的VBR服务器上执行任意代码。

Veeam 公司表示，其产品客户遍布全球，超过55万名，74%的全球前2000家公司以及82%的财富500强公司均是其客户。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[Veeam：Backup Enterprise Manager 中存在严重的认证绕过漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519550&idx=2&sn=6b4de50a6ef98b37be097aae6daafa64&scene=21#wechat_redirect)

[Veeam 修复备份管理平台中的RCE漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519438&idx=1&sn=4e26daf80a580f4ffca69990e4991525&scene=21#wechat_redirect)

[Veeam ONE 监控平台存在多个严重漏洞](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518080&idx=3&sn=186f168b319049fd88ec7557cb2458e1&scene=21#wechat_redirect)

[Veeam修复严重漏洞，可攻陷备份基础设施](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515885&idx=3&sn=ffefe13a8f5da2c680df756b9e641cfd&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/veeam-warns-of-critical-rce-bug-in-service-provider-console/

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