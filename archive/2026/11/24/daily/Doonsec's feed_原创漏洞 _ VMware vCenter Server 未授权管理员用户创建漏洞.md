---
title: 原创漏洞 | VMware vCenter Server 未授权管理员用户创建漏洞
url: https://mp.weixin.qq.com/s/jkjqyaXmwlAi2LBNhnoAeA
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:40:14.725276
---

# 原创漏洞 | VMware vCenter Server 未授权管理员用户创建漏洞

# 原创漏洞 | VMware vCenter Server 未授权管理员用户创建漏洞

微步在线研究响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 漏洞概况

---

11月24日，vCenter Server官方发布通告，修复了VMware vCenter Server 未授权管理员用户创建漏洞。**该漏洞由微步XGPT发现并报送VMware官方。**经分析，VMware vCenter Server 是 VMware 推出的虚拟化管理平台，其内置 vmdir 目录服务承载 SSO 身份目录。该服务在特定认证流程中存在访问控制缺陷，攻击者能访问 389 端口情况下，可能绕过身份验证，创建管理员账号并接管 vCenter。（完整漏洞情报请查阅https://x.threatbook.com/v5/vul/XVE-2026-62902）

此漏洞**无需任何权限**，攻击者成功利用此漏洞可**创建管理员账号并接管 vCenter，跟****11月19日VMware官方发布CVE-2026-123890不是同一个漏洞，**建议受影响用户**尽快修复。**

## 漏洞处置优先级(VPT)

---

**风险等级：高风险**
**风险分数：9.8**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2026-62902 |
| CVE编号 | CVE-2026-123903 |
| 漏洞类型 | 身份鉴别错误 |
| **利用条件评估** | 利用漏洞的网络条件 | 可远程利用 |
| 是否需要绕过安全机制 | 不需要 |
| 对被攻击系统的要求 | 默认配置 |
| 利用漏洞的权限要求 | 无需任何权限 |
| 是否需要受害者配合 | 不需要 |
| **利用情报** | POC是否公开 | 否 |
| 已知利用行为 | 否 |

## 漏洞影响范围

---

|  |  |
| --- | --- |
| **产品名称** | Vmware vCenter Server  VMware Cloud Foundation Vmware Telco Cloud Platform Vmware Telco Cloud Infrastructure |
| **受影响版本** | vCenter Server:   9.1.x.x<=version<9.1.2 vCenter Server:   9.0.x.x<=version<9.0.2.0300 vCenter Server:   8.0<=version<8.0U3m  vCenter Server: 7.x 未提供修复版本，联系官方咨询  VMware Cloud Foundation: 5.x<=version<5.2.5  Telco Cloud Platform: 3.0, 4.x, 5.0.x, 5.1.x, 5.2  Telco Cloud Infrastructure: 3.0 |
| **有无修复补丁** | https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39626 |

## 漏洞复现

---

1. 首页

![](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEOYcicict6I3TyILQRvEKF9DoHjsaScRQjkQGeBtnv6ibhSscULibzJWdWrbSgMY0cWh9Skrf4ytLR4GiawlVwo07sKncpylFqbe8ec/640?from=appmsg)

2. 在8.0.3.01000版本执行poc，创建新用户

![image.png](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEPThhoIYMUwVySD1XEyM7Etn32HchNsZQUOpI9EjTmHxvTOhq3NApF21Ya8YNAEDQLRlVVlAVTQzF0RWYrgGUH0bwicicc9H9mFk/640?from=appmsg)

3. 登录后台

![image.png](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEMAcibQ8nW7fpc8OH0o9H5ycSgzZ29WZGxhXbibJhyC9kaNIia3cxpnZPTrIqk0OD4Cmasg2mYbcDicwuoRzDQw61ETzNe5HjC2osc/640?from=appmsg)

## 修复方案

---

### 官方修复方案

https://support.broadcom.com/web/ecx/support-content-notification/-/external/content/SecurityAdvisories/0/39626

## 微步产品支撑

---

微步漏洞情报于**2026年9月14日**收录该漏洞。

微步下一代威胁情报平台NGTIP，高级威胁情报平台ATI及X情报中心已于漏洞收录时向漏洞订阅用户推送该漏洞情报，并将持续推送后续更新；对于已经录入资产的用户，支持实时自动化排查受影响资产。

预览时标签不可点

修改于

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fFyp1gWjicML0NlKR16SxQGjNPSYVoUxGgXhXvI4Z8ia5h8C9TGibEic1ABv6fniame8h0dh6zGX8ndXT8icjQocVh8A/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过