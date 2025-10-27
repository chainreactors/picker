---
title: YApi命令执行漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247497084&idx=1&sn=fc4a7ba050faaa9a68cdb0f4966cee0a&chksm=fe79d1e4c90e58f2bae37d494596f1ef1361427b8b825743c4077ab1330954c6f1d455f74274&scene=58&subscene=0#rd
source: 奇安信CERT
date: 2022-11-12
fetch_date: 2025-10-03T22:32:45.724884
---

# YApi命令执行漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4ibeIHtaYevEtd67OQhNRIVuHkRzOR6BnQNgIe9gC70nl2N2KLohWDH2vpNUPLGRiaL38iatTG9Oexiaw/0?wx_fmt=jpeg)

# YApi命令执行漏洞安全风险通告

原创

QAX CERT

奇安信 CERT

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icrhoWdKnhTgicSjB9pXdeZwDibNIBAEMegibEdG1vrjOibsq887TUz3ztMkM6Qvibic7r26sqbUIbicOMYg/640?wx_fmt=png "https://image.ipaiban.com/upload-ueditor-image-20201112-1605175807303084927.png")

奇安信CERT

**致力于**第一时间为企业级用户提供安全风险**通告**和**有效**解决方案。

**安全通告**

YApi 是高效、易用、功能强大的 API管理平台，旨在为开发、产品、测试人员提供更优雅的接口管理服务。可以帮助开发者轻松创建、发布、维护API。

近日，奇安信CERT监测到YApi命令执行漏洞，远程未授权的攻击者可通过注入漏洞获取有效用户token，进而利用自动化测试接口绕过沙箱限制，最终在目标系统上执行任意命令。**鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **YApi****命令执行漏洞** | | |
| **公开时间** | 2022-11-01 | **更新时间** | 2022-11-11 |
| **CVE****编号** | 暂无 | **其他编号** | QVD-2022-44046 |
| **威胁类型** | 命令执行 | **技术类型** | 参数注入 |
| **厂商** | YApi | **产品** | YApi |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | 未发现 | 未公开 |
| **漏洞描述** | YApi中存在命令执行漏洞，远程未授权的攻击者可通过注入漏洞获取有效用户token，进而利用自动化测试接口绕过沙箱限制，最终在目标系统上执行任意命令。 | | |
| **影响版本** | YApi < 1.12.0 | | |
| **不受影响版本** | YApi 1.12.0（默认配置下不受影响） | | |
| **其他受影响组件** | 无 | | |

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | **YApi****命令执行漏洞** | | | |
| **CVE****编号** | 暂无 | **其他编号** | | QVD-2022-44046 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 9.8 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 低 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 无 | | 不需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 不改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | 攻击者可以利用该漏洞在未经身份验证的情况下，在目标系统执行任意命令，控制目标系统。 | | | |

处置建议

**一、版本升级**

目前官方已有可更新版本，建议受影响用户更新至 1.12.0 及以上版本。

https://github.com/YMFE/yapi/releases/tag/v1.12.0

**注：**

**1. YApi 1.11.0版本已修复Mongo注入获取Token的问题，导致攻击者无法在未授权的情况下利用此漏洞。**

**2. 在YApi 1.12.0的版本更新中，仅默认禁用了Pre-request和Pre-response脚本功能，使得此漏洞在默认配置下无法利用。**

**二、缓解措施**

1. 在业务允许的情况下，建议将YApi部署在内网，禁止外网访问。

2. 修改默认token加密的盐:

编辑项目根目录中的config.json，添加"passsalt":"任意随机值"，如:

```
{…"passsalt":"this_is_a_test"…}
```

保存，重启YApi服务即可。

参考资料

[1]https://github.com/YMFE/yapi/commit/59bade3a8a43e7db077d38a4b0c7c584f30ddf8c?diff=split

时间线

2022年11月11日，奇安信 CERT发布安全风险通告。

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