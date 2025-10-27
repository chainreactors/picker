---
title: 官方强烈建议升级，GitLab又曝严重的账户接管漏洞
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247544862&idx=3&sn=2865af7f677dd8dc692c0020a64a5200&chksm=c1e9bc4ff69e3559141d9a95b6f8f108bd5bd6aba15bd29a603f7066f6f658509853579d5830&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-07-13
fetch_date: 2025-10-06T17:43:33.095845
---

# 官方强烈建议升级，GitLab又曝严重的账户接管漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogs1f8fBOWs2umfIy6VssnbEG8s1TKia4fiamicAWkfVP0G0XPprg6mjIGNswJQia7rOD84pVnpxakLFibg/0?wx_fmt=jpeg)

# 官方强烈建议升级，GitLab又曝严重的账户接管漏洞

关键基础设施安全应急响应中心

7月10日，GitLab警告称，其产品GitLab社区和企业版本中存在一个严重漏洞，允许攻击者以任何其他用户的身份运行管道作业。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR38cLyVUGZ6omD5OaIhGib8JtBPSYLQQtawCCbW3Jr11IneiakANQAFAQojuV6iaRSHBHHIsBNvkH74Pg/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

> GitLab DevSecOps平台拥有3000多万注册用户，活跃用户数仅次于 GitHub，超过50%的财富100强公司都在使用该平台，包括T-Mobile、高盛、空客、洛克希德·马丁、英伟达和瑞银。

在昨天发布的安全更新中，修补的漏洞被追踪为CVE-2024-6385，CVSS评分为9.6分(满分10分)。它影响所有GitLab CE/EE版本，从15.8到16.11.6，17.0到17.0.4，17.1到17.1.2。

GitLab管道是一个持续集成/持续部署(CI/CD)系统功能，允许用户自动并行或顺序运行流程和任务，以构建、测试或部署代码更改。在GitLab尚未披露漏洞某些信息的情况下，攻击者可以利用该漏洞作为任意用户触发新的管道。

为解决这一严重安全漏洞，GitLab发布了GitLab社区和企业版本17.1.2、17.0.4和16.11.6。该公司强烈建议所有安装运行受以上问题影响的版本尽快升级到最新版本，GitLab.com和GitLab Dedicated已经在运行补丁版本。

**账户接管漏洞在攻击中被积极利用**

6月底，GitLab修复了一个与CVE-2024-6385几乎相同的漏洞CVE-2024-5655，该漏洞也可能被利用来作为其他用户运行管道。

一个月前，GitLab还修复了一个高严重性漏洞CVE-2024-4835，该漏洞允许未经身份验证的攻击者在跨站点脚本(XSS)攻击中接管账户。

5月份，CISA发出警告，未经身份验证的攻击者也在积极利用1月份修补的另一个零点击GitLab漏洞CVE-2023-7028通过重置密码来劫持账户。

今年1月，Shadowserver发现5300多个易受攻击的GitLab实例暴露在网络上，目前仍有不到一半(1795个)的实例可以访问。

攻击者以GitLab为目标，大概率是因为它托管各种类型的企业敏感数据，包括API密钥和专有代码，一旦遭到破坏，托管项目的完整性和机密性将面临重大风险。

这包括供应链攻击，如果威胁行为者在CI/CD(持续集成/持续部署)环境中插入恶意代码，或危及被破坏组织的存储库。

**参考资料：**

https://www.bleepingcomputer.com/news/security/gitlab-warns-of-critical-bug-that-lets-attackers-run-pipelines-as-an-arbitrary-user/

https://www.darkreading.com/application-security/critical-gitlab-bug-threatens-software-development-pipelines

原文来源：FreeBuf

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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