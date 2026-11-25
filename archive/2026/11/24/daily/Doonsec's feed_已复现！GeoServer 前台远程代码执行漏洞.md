---
title: 已复现！GeoServer 前台远程代码执行漏洞
url: https://mp.weixin.qq.com/s/qVXepsjAOLjty6Q6J1mxYg
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:38:16.783430
---

# 已复现！GeoServer 前台远程代码执行漏洞

# 已复现！GeoServer 前台远程代码执行漏洞

微步在线研究响应中心

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

## 漏洞概况

---

GeoServer 是一个基于 Java 的开源地理信息服务器，用来发布和共享地理空间数据。它能把 PostGIS、Shapefile 等数据发布为符合 WMS、WFS、WCS 等 OGC 标准的服务，供网页地图和 GIS 客户端使用。

今日，GeoServer官方发布安全通告，披露了5个安全漏洞。这些漏洞被组合利用时，可能使未登录的攻击者以 GeoServer 服务进程的权限执行代码。**微步情报局已成功复现。**经分析，5个漏洞涉及 WFS 请求处理、获取管理会话和 JDBC 反序列化漏洞。这些漏洞被组合利用时，可能使未登录的攻击者实现无需认证的远程命令执行。

此漏洞**无需任何权限**，攻击者成功利用此漏洞可**攻击者可实现无需认证的远程命令执行，**建议受影响用户**尽快修复。**

## 漏洞处置优先级(VPT)

---

**风险等级：高风险**
**风险分数：9.8**

|  |  |  |
| --- | --- | --- |
| **基本信息** | 微步编号 | XVE-2026-103268  XVE-2026-103269  XVE-2026-103302  XVE-2026-103304  XVE-2026-103305 |
| CVE编号 | CVE-2026-129242  CVE-2026-129243  CVE-2026-129244  CVE-2026-129245  CVE-2026-120705 |
| 漏洞类型 | 远程代码执行 |
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
| **产品名称** | GeoServer | GeoServer |
| **受影响版本** | GeoServer <= 2.27.6  GeoServer 2.28.0 - 2.28.5  GeoServer 3.0.0 - 3.0.1 |
| **有无修复补丁** | 有 |

## 漏洞复现

---

![168677692a4fbb71cb9e3235bedc7448.png](https://mmbiz.qpic.cn/mmbiz_png/T4OSm0sXdEO82icaKialFxmqRc01KE46IWNVlRibVia5L3UCN5f1DbpKHiccjZNyreoVXfrWpb38JADvSlQCMNGabOOFKL5icJrG9AJydQmTF3oxM/640?from=appmsg)

## 修复方案

---

### 官方修复方案

https://github.com/geoserver/geoserver/releases

### 官方临时缓解建议

防护设备添加规则，拦截 /geoserver/wfs 请求携带 ID 参数含 xi:include、fes:、file:/// 等XInclude特征

## 微步产品支撑

---

微步漏洞情报于**2026年11月24日**收录该漏洞。

微步下一代威胁情报平台NGTIP，高级威胁情报平台ATI及X情报中心已于漏洞公开时向漏洞订阅用户推送该漏洞情报，并将持续推送后续更新；对于已经录入资产的用户，支持实时自动化排查受影响资产。

预览时标签不可点

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