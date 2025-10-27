---
title: Argo CD 多个高危漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247497477&idx=1&sn=9cb0283803d41ab7cad568351a54b3f6&chksm=fe79d39dc90e5a8b46e7802d574e387775273196386f98e1d17fe96611a347b22394b927af09&scene=58&subscene=0#rd
source: 奇安信CERT
date: 2023-01-31
fetch_date: 2025-10-04T05:14:28.461462
---

# Argo CD 多个高危漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4814gSISibcc14licK1GNWr7JBRXPwBwWjSYGAUYib60t29V3cMhMJ4DF2PeNbaoOE5m0wFtSuEp1UmA/0?wx_fmt=jpeg)

# Argo CD 多个高危漏洞安全风险通告

原创

QAX CERT

奇安信 CERT

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icrhoWdKnhTgicSjB9pXdeZwDibNIBAEMegibEdG1vrjOibsq887TUz3ztMkM6Qvibic7r26sqbUIbicOMYg/640?wx_fmt=png "https://image.ipaiban.com/upload-ueditor-image-20201112-1605175807303084927.png")

奇安信CERT

**致力于**第一时间为企业级用户提供安全风险**通告**和**有效**解决方案。

**安全通告**

Argo CD是用于Kubernetes的声明性GitOps持续交付工具。Argo CD可在指定的目标环境中自动部署所需的应用程序状态，应用程序部署可以在Git提交时跟踪对分支，标签的更新，或固定到清单的特定版本。Argo CD支持的Kubernetes 配置清单包括helm charts、kustomize、Ksonnet、Plugin、YAML/json文件等。

近日，奇安信CERT监测到Argo CD官方发布**Argo CD身份认证绕过漏洞(CVE-2023-22482)和Argo CD授权绕过漏洞(CVE-2023-22736)**通告，攻击者可以利用CVE-2023-22482，使Argo CD的API接受某些无效令牌绕过身份认证从而访问Argo CD；利用CVE-2023-22736可在配置允许的命名空间之外部署应用程序。**鉴于这些漏洞影响范围较大，建议客户尽快做好自查及防护。**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **Argo CD****身份认证绕过漏洞** | | |
| **公开时间** | 2023-01-26 | **更新时间** | 2023-01-30 |
| **CVE****编号** | CVE-2023-22482 | **其他编号** | QVD-2023-3001 |
| **威胁类型** | 身份认证绕过 | **技术类型** | 授权机制不正确 |
| **厂商** | Argo | **产品** | Argo CD |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | 未发现 | 未公开 |
| **漏洞描述** | Argo CD 授权机制存在问题。Argo CD 在验证用户提供的令牌时，会验证该令牌是否由其配置的OIDC提供商签名，不会验证令牌中的 aud（受众）字段。若 Argo CD 配置的 OIDC 提供商也为其他受众提供服务（例如，文件存储服务），Argo CD 也会接受这种令牌。未经授权的远程攻击者可通过窃取这些有效令牌来绕过 Argo CD 身份认证。 | | |
| **影响版本** | 1.8.2 <= Argo CD <= 2.6.0-rc4  Argo CD v2.5.x <= v2.5.7  Argo CD v2.4.x <= v2.4.18  Argo CD v2.3.x <= v2.3.13 | | |
| **不受影响版本** | Argo CD >= 2.6.0-rc5  Argo CD v2.5.x >= v2.5.8  Argo CD v2.4.x >= v2.4.20  Argo CD v2.3.x >= v2.3.14 | | |
| **其他受影响组件** | 无 | | |

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **Argo CD****授权绕过漏洞** | | |
| **公开时间** | 2023-01-26 | **更新时间** | 2023-01-30 |
| **CVE****编号** | CVE-2023-22736 | **其他编号** | QVD-2023-3007 |
| **威胁类型** | 授权绕过 | **技术类型** | 未授权访问 |
| **厂商** | Argo | **产品** | Argo CD |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | 未发现 | 未公开 |
| **漏洞描述** | Argo CD 中存在授权绕过漏洞，当Argo CD的应用程序控制器启用分片时，拥有用户权限的远程攻击者利用此漏洞可以在配置允许的命名空间之外部署应用程序。 | | |
| **影响版本** | 2.5.0-rc1<= Argo CD <= 2.5.7  Argo CD 2.6.0-x <= 2.6.0-rc4 | | |
| **不受影响版本** | Argo CD 2.5.x >= 2.5.8  Argo CD 2.6.0-x >= 2.6.0-rc5 | | |
| **其他受影响组件** | 无 | | |

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | **Argo CD****身份认证绕过漏洞** | | | |
| **CVE****编号** | CVE-2023-22482 | **其他编号** | | QVD-2023-3001 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 9.0 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 高 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 不需要 | | 不需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | 未经身份认证的远程攻击者通过此漏洞可绕过身份认证获得用户权限。 | | | |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | **Argo CD****授权绕过漏洞** | | | |
| **CVE****编号** | CVE-2023-22736 | **其他编号** | | QVD-2023-3007 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 8.5 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 高 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 低权限 | | 不需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | 拥有用户权限的远程攻击者利用此漏洞可以在配置允许的命名空间之外部署应用程序。 | | | |

处置建议

**目前 Argo CD官方已发布安全版本修复这些漏洞，建议受影响用户尽快更新至对应的安全版本。**

**下载地址：**

https://github.com/argoproj/argo-cd/releases

参考资料

[1]https://github.com/argoproj/argo-cd/security/advisories/GHSA-q9hr-j4rf-8fjc

[2]https://github.com/argoproj/argo-cd/security/advisories/GHSA-6p4m-hw2h-6gmw

时间线

2023年1月30日，奇安信 CERT发布安全风险通告。

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