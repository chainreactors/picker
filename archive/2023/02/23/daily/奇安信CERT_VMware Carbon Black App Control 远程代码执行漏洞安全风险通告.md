---
title: VMware Carbon Black App Control 远程代码执行漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247497814&idx=1&sn=e874182595597f68c01f9d9610a15e18&chksm=fe79dccec90e55d8e1626348dc381a75dc441875bb098ebdb8c926d2a4c2b8dd851cae338489&scene=58&subscene=0#rd
source: 奇安信CERT
date: 2023-02-23
fetch_date: 2025-10-04T07:52:12.018388
---

# VMware Carbon Black App Control 远程代码执行漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs48L70WLibyq7VpLjb6QRAy8ictOFExPlND4s0XVfZQehTWKxGYIKs4fk31MUXtBLpm5EcpaJ7wrvu6A/0?wx_fmt=jpeg)

# VMware Carbon Black App Control 远程代码执行漏洞安全风险通告

奇安信 CERT

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icrhoWdKnhTgicSjB9pXdeZwDibNIBAEMegibEdG1vrjOibsq887TUz3ztMkM6Qvibic7r26sqbUIbicOMYg/640?wx_fmt=png "https://image.ipaiban.com/upload-ueditor-image-20201112-1605175807303084927.png")

奇安信CERT

**致力于**第一时间为企业级用户提供安全风险**通告**和**有效**解决方案。

**安全通告**

VMware Carbon Black App Control（AppC），是市场上最成熟和可扩展的应用控制解决方案之一，提供应用设备控制，高级威胁检测等服务。

近日，奇安信CERT监测到VMware官方发布安全更新，其中包含**VMware Carbon Black App Control 注入漏洞**(CVE-2023-20858)。具有 App Control 管理控制台特权访问权限的攻击者可通过发送特制请求来利用此漏洞，成功利用此漏洞可在目标系统上执行任意代码。**鉴于此漏洞影响较大，建议客户尽快更新至最新版本。**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **VMware Carbon Black App Control** **远程代码执行漏洞** | | |
| **公开时间** | 2023-02-21 | **更新时间** | 2023-02-22 |
| **CVE****编号** | CVE-2023-20858 | **其他编号** | QVD-2023-4956 |
| **威胁类型** | 代码执行 | **技术类型** | 代码注入 |
| **厂商** | VMware | **产品** | VMware Carbon Black App Control |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | 未发现 | 未发现 |
| **漏洞描述** | VMware Carbon Black App Control存在漏洞，拥有高权限的攻击者可以发送特制请求到VMware Carbon Black App Control服务器，在目标系统上执行任意代码。 | | |
| **影响版本** | 8.9.0 <= VMware Carbon Black App Control < 8.9.4  8.8.0 <= VMware Carbon Black App Control < 8.8.6  8.7.0 <= VMware Carbon Black App Control < 8.7.8 | | |
| **不受影响版本** | VMware Carbon Black App Control 8.9.x >= 8.9.4  VMware Carbon Black App Control 8.8.x >= 8.8.6  VMware Carbon Black App Control 8.7.x >= 8.7.8 | | |
| **其他受影响组件** | 无 | | |

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | VMware Carbon Black App Control 远程代码执行漏洞 | | | |
| **CVE****编号** | CVE-2023-20858 | **其他编号** | | QVD-2023-4956 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 9.1 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 低 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 高 | | 不需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | 拥有高权限的攻击者可以利用该漏洞在目标系统上执行任意代码。 | | | |

处置建议

**目前 VMware官方已发布安全版本修复该漏洞，建议受影响用户尽快更新至对应的安全版本：**

VMware Carbon Black App Control 8.9.x >= 8.9.4

VMware Carbon Black App Control 8.8.x >= 8.8.6

VMware Carbon Black App Control 8.7.x >= 8.7.8

参考资料

[1]https://www.vmware.com/security/advisories/VMSA-2023-0004.html

时间线

2023年2月22日，奇安信 CERT发布安全风险通告。

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