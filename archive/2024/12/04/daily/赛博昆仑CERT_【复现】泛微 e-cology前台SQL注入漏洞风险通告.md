---
title: 【复现】泛微 e-cology前台SQL注入漏洞风险通告
url: https://mp.weixin.qq.com/s?__biz=MzkxMDQyMTIzMA==&mid=2247484709&idx=1&sn=b9e726441e7c55aa51751d27d441bcd3&chksm=c12af8a4f65d71b20f4833b8438f7b19703ec3e2b75eea5769a49144a2e6957613009801c7e5&scene=58&subscene=0#rd
source: 赛博昆仑CERT
date: 2024-12-04
fetch_date: 2025-10-06T19:42:25.606529
---

# 【复现】泛微 e-cology前台SQL注入漏洞风险通告

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaZ7t7b9Dods0V4Ql3Sr8MMwmznuwYlUpia6VSVFcX5oXjKb8hNbbjzKjB1UN6HuJWcVbDVA6hklZujRfsEUDaug/0?wx_fmt=jpeg)

# 【复现】泛微 e-cology前台SQL注入漏洞风险通告

原创

赛博昆仑CERT

赛博昆仑CERT

![](https://mmbiz.qpic.cn/mmbiz_gif/iaZ7t7b9Dodvib7ddpGMC6vx4COAy4sBoGbGCkwVUIJSHBPI0z1Utrp1h5ys6ygT3albl3PgjejJcRRRiaDFFbMBA/640?wx_fmt=gif)

-赛博昆仑漏洞安全通告-

泛微 e-cology前台SQL注入漏洞风险通告

![](https://mmbiz.qpic.cn/mmbiz_svg/7j1UQofaR9fsNXgsOXHVKZMJ1PCicm8s4RHQVjCJEjX63AsNibMx3So4wSMAvubEOoU2vLqYY7hIibIJbkEaPIDs5A4ianh5jibxw/640?wx_fmt=svg)

**漏洞描述**

泛微协同管理应用平台(e-cology)是一套兼具企业信息门户、知识文档管理、工作流程管理、人力资源管理、客户关系管理、项目管理、财务管理、资产管理、供应链管理、数据中心功能的企业大型协同管理平台，形成了一系列的通用解决方案和行业解决方案。

近日，赛博昆仑CERT监测到泛微官方发布了 v10.71\_1 补丁版本。未经授权的远程攻击者可通过发送特殊的HTTP请求来造成SQL注入漏洞，最终可导致攻击者获取数据库中的敏感信息。

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | 泛微 e-cology前台SQL注入漏洞 | | |
| **漏洞公开编号** | 暂无 | | |
| **昆仑漏洞库编号** | CYKL-2024-028619 | | |
| **漏洞类型** | SQL注入 | **公开时间** | 2024-12-02 |
| **漏洞等级** | 高危 | **评分** | 7.5 |
| **漏洞所需权限** | 无权限要求 | **漏洞利用难度** | 低 |
| **PoC****状态** | 未知 | **EXP****状态** | 未知 |
| **漏洞细节** | 未知 | **在野利用** | 未知 |

****影响版本****

e-cology9 并且 补丁版本 < v10.71\_01

**漏洞利用条件**

无需任何利用条件

**漏洞复现**

目前赛博昆仑CERT已确认漏洞原理，复现截图如下：

使用延时5秒的poc进行验证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaZ7t7b9DodvV3p1BpOrfPzYxnlXpjesLuZJLzg4u3BANVbTicicBU65OiaSiaZVnlNZJNAD6olDy1r0zj1p4kDAaRg/640?wx_fmt=png&from=appmsg)

**防护措施**

* **修复建议**

目前，官方已发布修复建议，建议受影响的用户尽快升级至安全版本。

下载地址：https://www.weaver.com.cn/cs/securityDownload.html#

* **技术业务咨询**

赛博昆仑支持对用户提供轻量级的检测规则或热补方式，可提供定制化服务适配多种产品及规则，帮助用户进行漏洞检测和修复。

赛博昆仑CERT已开启年订阅服务，付费客户(可申请试用)将获取更多技术详情，并支持适配客户的需求。

联系邮箱：cert@cyberkl.com

公众号：赛博昆仑CERT

****参考链接****

https://www.weaver.com.cn/cs/securityDownload.html#

****时间线****

2024年12月2日，泛微官网发布补丁

2024年12月3日，赛博昆仑CERT发布漏洞应急通告

![](https://mmbiz.qpic.cn/mmbiz_gif/iaZ7t7b9Dodvib7ddpGMC6vx4COAy4sBoGLJ1DKwHPSc2JX7FQat3De8XiaajuAHkJzOY9ic9bnaHiaLJqVHIe0E2wg/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/iaZ7t7b9DodvyBPoWBtJuuBhwsuqJ8rOkph0TEkBZvyP4WlhLSowLgYGYXxaM8GXhEucCp2LmvLXuJILOkvTFiaQ/0?wx_fmt=png)

赛博昆仑CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iaZ7t7b9DodvyBPoWBtJuuBhwsuqJ8rOkph0TEkBZvyP4WlhLSowLgYGYXxaM8GXhEucCp2LmvLXuJILOkvTFiaQ/0?wx_fmt=png)

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