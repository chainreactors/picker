---
title: Apache Kylin多个命令注入漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247497287&idx=1&sn=699dc588b5eacb72a805ddefab2e8b5e&chksm=fe79d2dfc90e5bc90a30623c1df61092c6b45ab55beb2d9faf5ecb736771ddcb00979c815051&scene=58&subscene=0#rd
source: 奇安信CERT
date: 2023-01-04
fetch_date: 2025-10-04T03:00:24.251606
---

# Apache Kylin多个命令注入漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs48lqqNI49TpvNO5V6nLHed5iayS682micyId3JRwhJMiaPbyZor2G8Hic5Klusg5E4QrwJCFNLu1t6kfQ/0?wx_fmt=jpeg)

# Apache Kylin多个命令注入漏洞安全风险通告

原创

QAX CERT

奇安信 CERT

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icrhoWdKnhTgicSjB9pXdeZwDibNIBAEMegibEdG1vrjOibsq887TUz3ztMkM6Qvibic7r26sqbUIbicOMYg/640?wx_fmt=png "https://image.ipaiban.com/upload-ueditor-image-20201112-1605175807303084927.png")

奇安信CERT

**致力于**第一时间为企业级用户提供安全风险**通告**和**有效**解决方案。

**安全通告**

Apache Kylin 是一个开源的、分布式的分析型数据仓库，提供Hadoop或Spark之上的 SQL 查询接口及多维分析（OLAP）能力以支持超大规模数据，最初由 eBay 开发并贡献至开源社区。

近日，奇安信CERT监测到Apache Kylin命令注入漏洞(CVE-2022-43396)和Apache Kylin命令注入漏洞(CVE-2022-44621)。其中Apache Kylin命令注入漏洞(CVE-2022-43396)是历史漏洞CVE-2022-24697的黑名单修复绕过，攻击者通过控制目标服务器conf的kylin.engine.spark-cmd参数来控制命令。Apache Kylin命令注入漏洞(CVE-2022-44621)是由于系统Controller未验证参数，攻击者可以通过HTTP请求进行命令注入攻击。**鉴于这些漏洞影响范围较大，建议客户尽快做好自查，及时更新至最新版本。**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **Apache Kylin** **命令注入漏洞****(CVE-2022-43396)** | | |
| **公开时间** | 2022-12-30 | **更新时间** | 2023-01-03 |
| **CVE****编号** | CVE-2022-43396 | **其他编号** | QVD-2023-1094 |
| **威胁类型** | 命令执行 | **技术类型** | 命令注入 |
| **厂商** | Apache | **产品** | Kylin |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | 未知 | 未发现 |
| **漏洞描述** | Apache Kylin命令注入漏洞(CVE-2022-43396)是历史漏洞CVE-2022-24697的黑名单修复绕过，攻击者通过控制目标服务器conf的kylin.engine.spark-cmd参数来控制命令。 | | |
| **影响版本** | Kylin 2.x  Kylin 3.x  Kylin 4.x < 4.0.3 | | |
| **不受影响版本** | Kylin >= 4.0.3 | | |
| **其他受影响组件** | 无 | | |

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **Apache Kylin** **命令注入漏洞****(CVE-2022-44621)** | | |
| **公开时间** | 2022-12-30 | **更新时间** | 2023-01-03 |
| **CVE****编号** | CVE-2022-44621 | **其他编号** | QVD-2023-1161 |
| **威胁类型** | 命令执行 | **技术类型** | 命令注入 |
| **厂商** | Apache | **产品** | Kylin |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| 未发现 | 未发现 | 未知 | 未发现 |
| **漏洞描述** | Apache Kylin命令注入漏洞(CVE-2022-44621)是由于系统Controller未验证参数，攻击者可以通过HTTP请求进行命令注入攻击。 | | |
| **影响版本** | Kylin 2.x  Kylin 3.x  Kylin 4.x < 4.0.3 | | |
| **不受影响版本** | Kylin >= 4.0.3 | | |
| **其他受影响组件** | 无 | | |

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | **Apache Kylin** **命令注入漏洞** | | | |
| **CVE****编号** | CVE-2022-43396 | **其他编号** | | QVD-2023-1094 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 9.8 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 低 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 不需要 | | 不需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 不改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | Apache Kylin命令注入漏洞(CVE-2022-43396)是历史漏洞CVE-2022-24697的黑名单修复绕过，攻击者通过控制目标服务器conf的kylin.engine.spark-cmd参数来控制命令。 | | | |
|  |  |  |  |  |

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | **Apache Kylin** **命令注入漏洞** | | | |
| **CVE****编号** | CVE-2022-44621 | **其他编号** | | QVD-2023-1161 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 9.8 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 网络 | | 低 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 不需要 | | 不需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 不改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | Apache Kylin命令注入漏洞(CVE-2022-44621)是由于系统Controller未验证参数，攻击者可以通过HTTP请求进行命令注入攻击。 | | | |
|  |  |  |  |  |

处置建议

目前Kylin官方已发布安全版本修复该漏洞，建议受影响用户尽快更新至对应的安全版本。

https://kylin.apache.org/

参考资料

[1]https://kylin.apache.org/

[2]https://github.com/apache/kylin/pull/2011

[3]https://lists.apache.org/thread/7ctchj24dofgsj9g1rg1245cms9myb34

[4]https://lists.apache.org/thread/ob2ks04zl5ms0r44cd74y1xdl1rzfd1r

时间线

2023年1月3日，奇安信 CERT发布安全风险通告。

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