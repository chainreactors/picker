---
title: 8月20日高危CVE漏洞速报
url: https://mp.weixin.qq.com/s/DAiN8DCWXcmVQJslL171Hg
source: Doonsec's feed
date: 2026-08-20
fetch_date: 2026-08-21T03:01:43.707045
---

# 8月20日高危CVE漏洞速报

# 8月20日高危CVE漏洞速报

探知安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

高危预警

# 【安全速报】8月19日高危漏洞紧急预警

2026年08月20日  |  探知安全

今日焦点：CISA 于 8 月 20日同日新增 4 条 critical 级 KEV 在野利用漏洞，覆盖虚拟化、网络边界、协作平台与端点，形成全栈攻击面——Windows IKE 未认证 RCE（EPSS 56%）、macOS 屏幕共享认证绕过（root 权限）、VMware vCenter 目录遍历与 SharePoint 弱认证；此外 GitLab GraphQL 未认证删库、WordPress 认证绕过与 Ray 代码注入亦需立即处置，请优先排查公网暴露资产。

## 漏洞详情

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-33824 | CVSS 9.8 |

### Windows IKE 扩展 Double Free 未认证 RCE（CVSS 9.8·CISA KEV·EPSS 56%）

Windows Internet Key Exchange (IKE) 服务扩展存在 double free 释放后重用漏洞（CWE-415），未经身份验证的远程攻击者仅需网络可达即可触发任意代码执行，无需任何用户交互。IKE 是 IPsec VPN 密钥协商的核心组件，该漏洞意味着 VPN 边界设备可被直接接管。CISA 于 8 月 20日将其纳入 KEV 目录，联邦机构补救截止日为 8 月 21 日；其 EPSS 评分高达 56%（30 天内被利用概率），远超同期其他漏洞（0.005-0.04），是当前攻击预测模型中最被看好的一条，需作为网络边界最高优先级处置。

影响范围

Windows 受影响版本（IKE/IPsec VPN 服务，公网可达的 VPN 网关与防火墙）

修复建议：立即应用微软官方补丁；核对 IPsec/IKE 服务的公网暴露面，临时限制 VPN 端口仅受信来源访问

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-65400 | CVSS 9.8 |

### macOS Screen Sharing 认证绕过致 root 权限（CVSS 9.8·CISA KEV·挖矿利用）

Apple macOS 的屏幕共享（Screen Sharing）服务存在身份认证缺陷（CWE-287），攻击者无需有效凭据即可通过网络完成认证并接入屏幕共享会话，进而获得 root 权限。CISA 已将 CVSS 评分从 7.1 上调至 9.8，并于 8 月 20日纳入 KEV，确认已出现攻击者利用该漏洞植入挖矿程序的在野案例。该漏洞与 Windows IKE 同批进入 KEV，端点侧被击穿意味着内网主机可被远程静默控制，建议第一时间排查开放了屏幕共享/远程管理功能的 macOS 主机。

影响范围

Apple macOS 受影响版本（开启屏幕共享或远程管理的 Mac 主机）

修复建议：立即升级至 Apple 最新安全更新；关闭不必要的屏幕共享/远程管理，限制其仅内网访问并启用强认证

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-19478 | CVSS 9.4 |

### GitLab GraphQL 代码注入未认证删库（CVSS 9.4·供应链攻击风险）

GitLab GraphQL 层在处理 @gl\_introduced 指令时存在 fallback 字段解析缺陷（代码注入），攻击者可借助该指令触发任意 ActiveRecord 公开方法调用，在无需任何身份验证的情况下，通过单个恶意请求永久删除公共项目数据、停用或封禁用户账号、修改关键状态信息，甚至对开源项目发起供应链攻击。GitLab 于 8 月 17 日发布紧急补丁 19.2.4 / 19.1.6 / 19.0.8 / 18.11.11，GitLab.com 与 GitLab Dedicated 已自动修复，所有 self-managed（自托管）实例需立即升级。代码托管平台是企业 CI/CD 与知识产权的核心节点，失陷将直接威胁软件交付与业务连续性。

影响范围

GitLab CE/EE 多个受支持版本（self-managed 自托管实例）

修复建议：立即升级至 19.2.4 / 19.1.6 / 19.0.8 / 18.11.11 及以上；盘点并统一管理全部 self-managed 实例

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2026-15826 | CVSS 9.8 |

### WordPress User Profile Builder 类型混淆认证绕过（CVSS 9.8·4 万+站点）

WordPress 用户资料管理插件 User Profile Builder 的登录流程存在类型混淆（Type Confusion）缺陷，攻击者无需登录即可绕过身份验证，并可能进一步获取网站管理员权限，实现站点完全接管。Wordfence 于 7 月 14 日收到报告并于次日完成验证，开发商 Cozmoslabs 已发布 3.16.5 修复版本，所有 3.16.4 及更早版本均受影响。该插件全球超 4 万个网站部署，涉及注册、登录与个人资料管理，攻击面广，需立即排查并升级。

影响范围

User Profile Builder 3.16.4 及更早版本（全球超 4 万站点）

修复建议：立即升级至 3.16.5 及以上；检查是否存在异常新增管理员账户并轮换管理员密码

|  |  |  |
| --- | --- | --- |
| 严重 | CVE-2025-62593 | CVSS 9.4 |

### Ray-Project Ray 代码注入远程执行（CVSS 9.4·AI/ML 框架·浏览器触发）

分布式计算框架 Ray（Ray-Project）存在代码注入漏洞，可导致远程代码执行（RCE），CVSS 9.4，于 8 月 17 日披露。攻击者可借助 Firefox、Safari 等浏览器触发利用，对将 Ray 作为开发工具或本地部署的开发者环境构成直接威胁。Ray 广泛用于 AI/ML 训练、模型服务与分布式数据处理，其集群一旦被攻破，攻击者可窃取训练数据、模型权重与云凭证，威胁从开发环境延伸至 AI 基础设施，需纳入 AI 供应链防护视野。

影响范围

Ray-Project Ray 受影响版本（开发者本地环境与自建 Ray 集群）

修复建议：立即升级至官方修复版本；限制 Ray 控制面仅本机/内网访问，避免浏览器暴露管理界面

紧急提醒

本期最高优先级：CISA 于 8 月 18 日同日新增 4 条 critical 级 KEV 极为罕见，说明多个信任基础设施正被同时击穿。其中 CVE-2026-33824 Windows IKE（EPSS 56%）可未认证接管 VPN 边界，CVE-2026-65400 macOS 屏幕共享可获 root 权限且已在野植入挖矿程序，两者均需在 8 月 21 日联邦机构补救截止日前完成处置。建议安全团队优先排查公网暴露的 VPN 网关、macOS 主机、GitLab 自托管实例与 WordPress 站点，先升级再谈其他。

处置建议

① Windows 环境立即应用微软补丁，核对 IKE/IPsec VPN 公网暴露面并限制来源 IP

② macOS 主机立即升级至最新安全更新，关闭非必要的屏幕共享/远程管理功能

③ GitLab 自托管实例立即升级至 19.2.4 / 19.1.6 / 19.0.8 / 18.11.11，盘点全部实例版本

④ WordPress 站点立即升级 User Profile Builder 至 3.16.5，排查异常管理员账户

⑤ Ray 集群立即升级至修复版本，限制控制面仅本机/内网访问

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