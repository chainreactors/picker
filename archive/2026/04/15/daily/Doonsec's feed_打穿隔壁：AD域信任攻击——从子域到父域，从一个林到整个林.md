---
title: 打穿隔壁：AD域信任攻击——从子域到父域，从一个林到整个林
url: https://mp.weixin.qq.com/s/rs8tgDgcVWGT5tbb-hcguw
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:50:48.957767
---

# 打穿隔壁：AD域信任攻击——从子域到父域，从一个林到整个林

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/L7VicJKsiaibFB3jXHoriajH29hCn00zoeEDLZaXxZ7aicv2zSZ8tSgBTLzsiajBKPsV1ibyDhxZKCXD0RxdECsvWj0QeGktWGUnoyWCG1exzSVmQg/0?wx_fmt=jpeg)

# 打穿隔壁：AD域信任攻击——从子域到父域，从一个林到整个林

原创

极客零零七
极客零零七

极客零零七

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 极客零零七 · AD攻击系列 · 第7篇

---

很多企业以为"把不同部门放在不同的域里"就是安全隔离。现实是：**AD域信任是一条双向高速公路，攻击者拿下一个子域，往往就能打穿整个林。**

本文讲清楚域信任攻击的三个层次：同林内的父子域提权、跨林信任滥用、以及SID Filtering绕过。每个层次都配完整的攻击链和防御要点。

---

### 一、域信任基础：信任不等于安全

#### 信任类型

| 类型 | 方向 | 传递性 | 典型场景 |
| --- | --- | --- | --- |
| 父子信任（Parent-Child） | 双向 | 是 | 同一林内的父域和子域 |
| 树根信任（Tree-Root） | 双向 | 是 | 同一林内的不同域树 |
| 外部信任（External） | 单向或双向 | 否 | 不同林之间的单独域信任 |
| 林信任（Forest） | 单向或双向 | 否 | 两个林的根域之间 |
| MIT信任 | 单向或双向 | 否 | AD与非Windows Kerberos域 |

#### 关键概念：SID Filtering

**SID Filtering**是跨信任边界的安全机制——它决定了哪些SID可以在跨域认证时被"尊重"。

```
同一林内（父子信任）：SID Filtering 默认关闭  → 攻击者可以伪造包含父域Enterprise Admins SID的票据
跨林信任：SID Filtering 默认开启  → 来自外部林的票据中，属于本林的SID会被过滤掉  → 但仍有绕过方式
```

**这就是为什么同一林内的域边界几乎不构成安全边界。**

#### 信任枚举

```
## PowerView枚举所有信任关系Get-DomainTrustGet-DomainTrust -Domain parent.localGet-ForestDomain  # 枚举林内所有域
## 查看信任属性Get-DomainTrust | Select-Object SourceName, TargetName, TrustType, TrustDirection, TrustAttributes
```

```
## Linux工具## ldapsearch枚举信任ldapsearch -H ldap://10.10.10.1 -D "user@child.domain.local" -w 'Pass' -b "CN=System,DC=child,DC=domain,DC=local" "(objectClass=trustedDomain)" cn trustDirection trustType trustAttributes
## BloodHound会自动收集信任关系bloodhound-python -u user -p pass -ns 10.10.10.1 -d child.domain.local -c All
```

---

### 二、父子域提权：从子域管理员到林根管理员

#### 攻击原理

在同一个林内，**Enterprise Admins组**（存在于林根域）对所有子域都有完全控制权。父子信任默认不启用SID Filtering，这意味着：

**如果攻击者拿下了子域的域控，可以伪造一张包含Enterprise Admins SID的Golden Ticket，直接获得整个林的控制权。**

#### 攻击前提

1. 已获得子域的**krbtgt哈希**（即已拿下子域域控）
2. 知道父域（林根域）的**域SID**
3. 知道Enterprise Admins组的SID（父域SID + `-519`）

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