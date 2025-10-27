---
title: Spring Framework 身份认证绕过漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247498098&idx=1&sn=11b501628fc3ca85f12c352ee29865db&chksm=fe79ddeac90e54fc6f52b51be38955e4d52e96dbe0f6f6d79be35ec53b8131bef69d5e43ecef&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2023-03-23
fetch_date: 2025-10-04T10:23:35.398100
---

# Spring Framework 身份认证绕过漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4ibZgcxc66wsEfib6W60uQwibiaQhBNndSFk5RNjkAmFwE2xnZ3XFk3ficyYMiaIic7V1ichw9t4H1kz4sYEw/0?wx_fmt=jpeg)

# Spring Framework 身份认证绕过漏洞安全风险通告

奇安信 CERT

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icrhoWdKnhTgicSjB9pXdeZwDibNIBAEMegibEdG1vrjOibsq887TUz3ztMkM6Qvibic7r26sqbUIbicOMYg/640?wx_fmt=png "https://image.ipaiban.com/upload-ueditor-image-20201112-1605175807303084927.png")

奇安信CERT

**致力于**第一时间为企业级用户提供**权威**漏洞情报和**有效**解决方案。

**安全通告**

Spring Framework 是一个开源应用框架，旨在降低应用程序开发的复杂度。它是轻量级、松散耦合的，具有分层体系结构，允许用户选择组件，同时还为 J2EE 应用程序开发提供了一个有凝聚力的框架。

近日，奇安信CERT监测到官方发布了**Spring Framework 身份认证绕过漏洞(CVE-2023-20860)**，当Spring Security使用mvcRequestMatcher配置并将"\*\*"作为匹配模式时，在Spring Security 和 Spring MVC 之间会发生模式不匹配，最终可能导致身份认证绕过。**鉴于此产品用量较大，建议客户尽快做好自查及防护。**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | Spring Framework 身份认证绕过漏洞 | | |
| **公开时间** | 2023-03-20 | **更新时间** | 2023-03-22 |
| **CVE****编号** | CVE-2023-20860 | **其他编号** | QVD-2023-6995 |
| **威胁类型** | 身份认证绕过 | **技术类型** | 身份认证绕过 |
| **厂商** | VMware | **产品** | Spring Framework |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **中危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | 未发现 | 未公开 |
| **漏洞描述** | Spring Framework存在身份认证绕过漏洞，当Spring Security使用mvcRequestMatcher配置并将"\*\*"作为匹配模式时，在Spring Security 和 Spring MVC 之间会发生模式不匹配，最终可能导致身份认证绕过。 | | |
| **影响版本** | Spring Framework 6.0.x <= 6.0.6  Spring Framework 5.3.x <= 5.3.25  **（其他低于****5.3.x****的系列版本不受此漏洞影响）** | | |

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | Spring Framework 身份认证绕过漏洞 | | | |
| **CVE****编号** | CVE-2023-20860 | **其他编号** | | QVD-2023-6995 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 9.1 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 低 | |
| **用户认证（****Au****）** | | **用户交互（****UI****）** | |
| 不需要 | | 不需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 不改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 无 | |
| **危害描述** | 攻击者利用此漏洞可能在Spring Framework项目中实现身份认证绕过。 | | | |

处置建议

目前官方已有可更新版本，建议用户升级至:

Spring Framework 6.0.x >= 6.0.7

Spring Framework 5.3.x >= 5.3.26

更新信息可参考官方通告：https://spring.io/security/cve-2023-20860

参考资料

[1]https://spring.io/security/cve-2023-20860

时间线

2023年3月22日，奇安信 CERT发布安全风险通告。

点击**阅读原文**

到奇安信NOX-安全监测平台查询更多漏洞详情

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

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