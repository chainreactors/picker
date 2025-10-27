---
title: Fortinet FortiNAC 远程代码执行漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247497797&idx=2&sn=d9086378cd19a4cd75896b8c009f95ac&chksm=fe79dcddc90e55cb4c8d4aa79a9ef4636aa112cb0b109451708d1fbabb64ae2af7382debf959&scene=58&subscene=0#rd
source: 奇安信CERT
date: 2023-02-22
fetch_date: 2025-10-04T07:44:05.822940
---

# Fortinet FortiNAC 远程代码执行漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs48t2WsvlmlLSe4PjAeKa2mjLiaAYia9iadlTqVbHr9DZvcZupzamWWy2267thsL70gFYjAsmDmWo7wPQ/0?wx_fmt=jpeg)

# Fortinet FortiNAC 远程代码执行漏洞安全风险通告

奇安信 CERT

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icrhoWdKnhTgicSjB9pXdeZwDibNIBAEMegibEdG1vrjOibsq887TUz3ztMkM6Qvibic7r26sqbUIbicOMYg/640?wx_fmt=png "https://image.ipaiban.com/upload-ueditor-image-20201112-1605175807303084927.png")

奇安信CERT

**致力于**第一时间为企业级用户提供安全风险**通告**和**有效**解决方案。

**安全通告**

FortiNAC(Network Access Control) 是Fortinet的一种零信任网络访问控制解决方案，可增强用户对企业网络上的物联网 (IoT) 设备的监控。NAC 是零信任网络访问安全模型的重要组成部分，在该模型中，IT 团队可以轻松了解正在访问网络的人员和设备，以及如何保护网络内外的公司资产。NAC 可提供全面的网络可视性，有效控制设备和用户，包括自动化动态响应。

近日，奇安信CERT监测到Fortinet官方发布安全更新，其中包含**Fortinet FortiNAC 远程代码执行漏洞(CVE-2022-39952)**。FortiNAC keyUpload 脚本中存在路径遍历漏洞，未经身份认证的远程攻击者可利用此漏洞向目标系统写入任意内容，最终可在目标系统上以 Root 权限执行任意代码。**鉴于此漏洞影响较大，建议客户尽快更新至最新版本。**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **Fortinet FortiNAC** **远程代码执行漏洞** | | |
| **公开时间** | 2023-02-20 | **更新时间** | 2023-02-20 |
| **CVE****编号** | CVE-2022-39952 | **其他编号** | QVD-2023-4737  CNNVD-202302-1434 |
| **威胁类型** | 代码执行 | **技术类型** | 文件名或路径的外部可控制 |
| **厂商** | Fortinet | **产品** | FortiNAC |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | 未发现 | 未公开 |
| **漏洞描述** | FortiNAC keyUpload 脚本中存在路径遍历漏洞，未经身份认证的远程攻击者可利用此漏洞向目标系统写入任意内容，最终可在目标系统上以 Root 权限执行任意代码。 | | |
| **影响版本** | FortiNAC 9.4.0  FortiNAC 9.2.x <= 9.2.5  FortiNAC 9.1.x <= 9.1.7  FortiNAC 8.8.x  FortiNAC 8.7.x  FortiNAC 8.6.x  FortiNAC 8.5.x  FortiNAC 8.3.x | | |
| **不受影响版本** | FortiNAC 9.4.x >= 9.4.1  FortiNAC 9.2.x >= 9.2.6  FortiNAC 9.1.x >= 9.1.8  FortiNAC 7.2.x >= 7.2.0 | | |
| **其他受影响组件** | 无 | | |

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | Fortinet FortiNAC 远程代码执行漏洞 | | | |
| **CVE****编号** | CVE-2022-39952 | **其他编号** | | QVD-2023-4737  CNNVD-202302-1434 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 9.8 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 低 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 不需要 | | 不需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 不改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | 未经身份认证的远程攻击者可利用此漏洞向目标系统写入任意内容，最终可在目标系统上以 Root 权限执行任意代码。 | | | |

处置建议

目前 Fortinet 官方已发布安全版本修复这些漏洞，建议受影响用户尽快更新至对应的安全版本。

FortiNAC 9.4.x >= 9.4.1

FortiNAC 9.2.x >= 9.2.6

FortiNAC 9.1.x >= 9.1.8

FortiNAC 7.2.x >= 7.2.0

参考资料

[1]https://www.fortiguard.com/psirt/FG-IR-22-300

时间线

2023年2月21日，奇安信 CERT发布安全风险通告。

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