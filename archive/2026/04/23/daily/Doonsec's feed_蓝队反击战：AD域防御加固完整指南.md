---
title: 蓝队反击战：AD域防御加固完整指南
url: https://mp.weixin.qq.com/s/oLEf2fpTx5oubIyYXrKoeA
source: Doonsec's feed
date: 2026-04-23
fetch_date: 2026-04-24T04:55:30.783048
---

# 蓝队反击战：AD域防御加固完整指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L7VicJKsiaibFDStK5a2e8icCIOyG9NVFT3fRzxBdYaQtdTraCBKUaMfvgNJmOSDcSBZkibyiaHYzADCJ4Igl7NIkmpBeibGvhyibkOjnPfsP9LcibGU/0?wx_fmt=jpeg)

# 蓝队反击战：AD域防御加固完整指南

原创

极客零零七
极客零零七

极客零零七

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 极客零零七 · AD攻击系列 · 第10篇

---

前9篇文章站在攻击者视角，拆解了AD域渗透的每一个环节。本篇换到防御者视角——**如果你是蓝队，如何系统性地加固AD域，让前面那些攻击技术失效或至少被检测到？**

不讲理论框架，只讲**具体操作和优先级排序**。按照"投入产出比"从高到低排列——前3项措施能阻断80%的AD攻击路径。

---

### 一、Tier模型：AD安全的基础架构

#### 什么是Tier模型

微软推荐的管理层级模型，核心思想是**防止高权限凭据暴露在低安全级别的系统上**。

```
Tier 0：身份基础设施  ├── 域控制器  ├── CA证书服务器  ├── Azure AD Connect  └── ADFS服务器
Tier 1：应用服务器  ├── 文件服务器、SQL服务器  ├── Exchange、SharePoint  └── 管理服务器（SCCM、WSUS）Tier 2：终端设备  ├── 用户工作站  ├── 打印机、会议室设备  └── 移动设备
```

#### 核心规则

```
✗ Tier 0 管理员绝对不能登录 Tier 1/2 设备✗ Tier 1 管理员不能登录 Tier 2 设备✗ 日常办公账户不能有任何管理权限
✓ 每个管理员有3个账户：  - 日常办公账户（无管理权限，用于收邮件/上网）  - Tier 1 管理账户（管理应用服务器）  - Tier 0 管理账户（仅用于域控操作，从专用PAW登录）
```

**为什么这一条最重要？** 因为攻击系列第4篇（横向移动）中的所有技术——PTH、PTT、凭据提取——**都依赖于高权限凭据出现在攻击者可触及的机器上**。如果Domain Admin从不登录普通服务器和工作站，攻击者根本抓不到DA的凭据。

#### 实施要点

```
## 1. 创建Tier 0专用管理组New-ADGroup -Name "Tier0-Admins" -GroupScope Global -Path "OU=Admin Groups,DC=domain,DC=local"
## 2. 通过GPO限制登录范围## GPO设置路径：ComputerConfiguration→Policies→WindowsSettings→SecuritySettings→LocalPolicies→UserRights Assignment##   - "Deny log on locally" → 在Tier 1/2机器上拒绝Tier 0账户登录##   - "Deny log on through Remote Desktop Services" → 同上##   - "Deny access to this computer from the network" → 同上
## 3. 部署特权访问工作站（PAW）## Tier 0管理员只能从专用PAW访问域控## PAW不连互联网、不装办公软件、不加入普通OU
```

---

### 二、凭据保护：让攻击者抓不到有用的东西

#### Protected Users组

```
## 加入Protected Users组的账户自动获得以下保护：## - 不缓存明文密码## - 不使用NTLM认证（阻断PTH）## - 不使用DES/RC4加密（阻断Kerberoasting的弱加密降级）## - TGT有效期硬编码为4小时（缩小Golden Ticket窗口）## - 不允许委派（阻断所有委派攻击）
## 将所有DA加入Add-ADGroupMember -Identity "Protected Users" -Members "domain_admin1","domain_admin2"
```

**注意**：加入Protected Users后，这些账户无法使用NTLM认证。确保所有管理操作走Kerberos，否则会导致管理工具报错。

#### LAPS（Local Administrator Password Solution）

每台工作站的本地管理员密码独立、随机、定期轮换——**彻底阻断横向移动中的本地管理员密码复用**。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

极客零零七

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vRBYx9F4Zf6FIrWa8y7Avoujo7CWGRp0ICqvZGJIdtQgzNlzefeHiaeibmBZbcl5Oyj9wBNTsPiczEeKCelS9xjibw/0?wx_fmt=png)

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