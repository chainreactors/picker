---
title: 7月10日高危CVE漏洞速报
url: https://mp.weixin.qq.com/s/0dn-AT5dbbDT8d_3ZHMU2Q
source: Doonsec's feed
date: 2026-07-10
fetch_date: 2026-07-11T05:01:40.862039
---

# 7月10日高危CVE漏洞速报

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nZrMrH4FF0IWibeib0unPjALYDj3ibia5OIaeGibQicemyeMiaaP0h6Z7XWHfVu3a0tZumcRicib9A363Zs303rHbu9cicT9SrXIdKx4zvQuHmDJyU0Nk/0?wx_fmt=jpeg)

# 7月10日高危CVE漏洞速报

探知安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

高危预警

# 【安全速报】07月10日高危漏洞紧急预警

2026年07月10日  |  探知安全

CISA KEV一次性新增4个在野利用漏洞，含Adobe ColdFusion CVE-2026-48282 CVSS 10.0满分RCE数小时即遭扫描攻击；Joomla两大Page Builder插件双满分漏洞在野利用创建管理员持久化控制；CoreWCF SAML令牌签名绕过CVE-2026-54782 CVSS 10.0未认证冒充任意主体；Langflow成为首个被KEV收录的AI Agent平台漏洞CVSS 9.9跨租户窃取API/AWS密钥；Apache Gravitino未认证RCE CVSS 9.1，请立即排查修复。

## 漏洞详情

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-48282 | CVSS 10.0 |

### Adobe ColdFusion路径遍历满分远程代码执行（CVSS 10.0·CISA KEV 7/7新增·数小时即遭野外利用）

Adobe ColdFusion应用程序服务器存在路径遍历漏洞（CWE-22），允许未认证的远程攻击者通过操控文件路径输入逃逸预期目录结构，在ColdFusion进程用户上下文中执行任意代码。成功利用可在数分钟内获取服务器立足点，快速访问管理功能、配置文件及连接的后端数据库系统。CISA于7月7日将其新增至KEV目录，联邦机构修复截止日期为7月10日。据安全机构KEVIntel监测，漏洞公开披露数小时内即监测到来自印度IP的大规模自动化扫描攻击。Adobe已于7月1日发布APSB26-68安全公告修复此漏洞，ColdFusion此前已有16个CVE被收录至KEV目录。

影响范围

Adobe ColdFusion 2025.9/2023.20及更早版本（企业级应用服务器，全球数万机构部署）

修复建议：立即安装Adobe APSB26-68安全更新；实施Web应用防火墙规则阻断路径遍历攻击；审计ColdFusion服务器日志排查已发生的入侵活动

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-48908 | CVSS 10.0 |

### JoomShaper SP Page Builder未认证任意文件上传远程代码执行（CVSS 10.0·CISA KEV在野利用·即时管理员持久化）

Joomla生态最流行的页面构建器扩展JoomShaper SP Page Builder存在满分严重漏洞（CWE-434不受限文件上传）。任何未认证访问者可通过向组件uploadCustomIcon端点发送HTTP POST请求，直接上传包含恶意PHP代码的文件至服务器，实现远程代码执行（RCE）。安全研究机构mySites.guru已记录到零日利用活动：攻击者在补丁发布前即用此漏洞创建新的管理员超级用户账户（名称为jhksdhfgkhjfgkhdfkjhgkshdfgkshjfd），实现对Joomla站点的完全控制和持久化后门。CISA已于7月7日将该漏洞纳入KEV目录，修复截止7月10日。

影响范围

JoomShaper SP Page Builder 6.6.1及更早版本（Joomla生态顶级页面构建器，数十万网站使用）

修复建议：立即升级至SP Page Builder 6.6.2或更高版本；检查Joomla用户表中是否存在异常管理员账户（特别关注jhksdhfgkhjfgkhdfkjhgkshdfgkshjfd）；审计uploadCustomIcon端点访问日志

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-55255 | CVSS 9.9 |

### Langflow AI平台跨租户IDOR窃取API密钥与AWS凭证（CVSS 9.9·首个KEV收录AI Agent平台·Sysdig确认攻击链）

开源AI Agent可视化构建平台Langflow存在授权绕过漏洞（CWE-639不安全的直接对象引用IDOR），已认证攻击者仅需指定其他用户的流程ID即可通过/api/v1/responses端点执行属于任意其他用户的完整AI流程。核心缺陷在于get\_flow\_by\_id\_or\_endpoint\_name辅助函数未执行所有权检查，将合法流程查询与未授权跨用户流程查询同等对待。云安全公司Sysdig于6月22-25日监测到一次凭证窃取活动：攻击者将CVE-2026-55255与另一个未认证RCE漏洞CVE-2026-33017链式利用，跨租户边界窃取API密钥及AWS访问密钥。CISA于7月7日将其纳入KEV目录，标志着AI Agent编排平台类漏洞首次进入国家级别在野利用预警。虽然CISA官方标注CVSS 6.1分，KEVIntel与CIRCL均赋予9.9分，已确认在野利用事实下建议以最高优先级处置。

影响范围

Langflow 1.9.1及更早版本（开源AI Agent平台，广泛应用于企业AI工作流编排）

修复建议：立即升级至Langflow 1.9.2或更高版本（新增显式所有权验证）；轮换所有可能已泄露的API密钥及AWS访问密钥；审计/api/v1/responses端点历史访问记录排查可疑跨租户调用

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-54782 | CVSS 10.0 |

### CoreWCF SAML令牌签名验证绕过满分漏洞（CVSS 10.0·未认证冒充任意主体·.NET生态广泛影响）

CoreWCF是.NET平台上广泛使用的WCF（Windows Communication Foundation）服务端开源实现。该满分漏洞（CWE-347签名验证不当）存在于CoreWCF使用联合绑定（Federated Binding）的场景中：服务端在处理SAML安全令牌时未能正确验证XML数字签名，导致未认证攻击者可以伪造SAML断言、冒充服务信任域中的任意用户或服务主体。攻击者无需任何凭据，仅需向存在联合绑定的CoreWCF端点发送特制SAML令牌，即可绕过所有认证机制获取系统权限。此漏洞影响使用WS-Trust/WS-Federation协议的企业级SOA架构和微服务通信场景，受影响的CoreWCF服务可直接被远程接管。

影响范围

CoreWCF存在联合绑定（Federated Binding）的所有版本（.NET生态SOA/微服务通信架构）

修复建议：立即更新CoreWCF至安全修复版本；若暂无法更新，禁用联合绑定改用其他认证机制；部署网络层访问控制限制CoreWCF端点仅受信来源访问

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-41042 | CVSS 9.1 |

### Apache Gravitino未认证远程代码执行（CVSS 9.1·恶意H2 JDBC URL·开源数据目录服务全版本）

Apache Gravitino是开源的高性能数据目录和元数据管理服务，被广泛应用于企业大数据平台。该漏洞存在于此服务的JDBC连接管理机制中：攻击者无需任何身份认证，通过构造恶意H2数据库JDBC连接URL即可在Gravitino服务进程上下文中执行任意Java代码。由于Gravitino通常部署在企业数据平台核心位置，成功利用可直接访问整个数据目录中的敏感元数据、数据源凭证和连接信息，并以Gravitino服务为跳板进一步横向渗透至Hive、Iceberg、Kafka等关联数据系统。该漏洞影响所有版本、攻击复杂度低且无需认证，是所有使用Gravitino的机构必须优先处置的安全事件。

影响范围

Apache Gravitino所有版本（企业大数据元数据管理平台，连接Hive/Iceberg/Kafka等数据系统）

修复建议：升级至Apache Gravitino最新安全修复版本；网络层隔离Gravitino服务端口仅内网受信IP访问；审计Gravitino日志排查H2 JDBC URL异常配置和Java代码执行记录

紧急提醒

本期CISA KEV一次性新增4个在野利用漏洞均为满分或接近满分，修复截止今日（7月10日）：Adobe ColdFusion CVE-2026-48282 CVSS 10.0披露数小时内即遭自动化扫描、JoomShaper SP Page Builder CVE-2026-48908超管持久化零日利用、Langflow CVE-2026-55255首个AI Agent平台KEV跨境窃取API/AWS密钥、JoomlaCK Page Builder CK CVE-2026-56290 Web Shell持久化。此外CoreWCF CVE-2026-54782 SAML伪造满分漏洞与Apache Gravitino未认证RCE均需紧急处置。请安全团队立即按上述优先级逐条修复。

处置建议

① Adobe ColdFusion用户立即安装APSB26-68安全更新，审计服务器日志排查入侵痕迹

② Joomla站点管理员立即检查SP Page Builder/Page Builder CK版本并升级，排查异常管理员账户

③ Langflow用户立即升级至1.9.2+，轮换所有API及AWS密钥，审计跨租户访问记录

④ CoreWCF用户立即升级修复版本或临时禁用联合绑定改用替代认证方案

⑤ Apache Gravitino用户立即升级修复版本并实施网络层访问限制，审计JDBC连接配置

觉得有用？点击右下角**在看**，让更多人看到

探知安全 · 每日推送最新漏洞资讯

预览时标签不可点

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/ayPnpNqYCJKbeG52l1HMrttVrHhaGYKtDOWalO9FcwwVTzzCKhpg0BEKR4eZdo8JXdrv6n8RZAOgtnmcEPgvHg/0?wx_fmt=png)

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