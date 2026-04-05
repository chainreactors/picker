---
title: Kerberos不是你的朋友：从协议原理到Kerberoasting、Golden Ticket全攻击链
url: https://mp.weixin.qq.com/s/uDeDHTe8IXwudWOWonSbXw
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:32:10.603104
---

# Kerberos不是你的朋友：从协议原理到Kerberoasting、Golden Ticket全攻击链

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L7VicJKsiaibFChZIaG1692lI7yfWCh78qU96V8vlmcvrtvCNHEjVVzpib0fibNRLJr6hD6cMh1trvHib1keyTdtvYxptcUEPUaiasAbFHKddjzEeI/0?wx_fmt=jpeg)

# Kerberos不是你的朋友：从协议原理到Kerberoasting、Golden Ticket全攻击链

原创

极客零零七
极客零零七

极客零零七

![]()

在小说阅读器中沉浸阅读

> 极客零零七 · AD攻击系列 · 第2篇

---

[上一篇](https://mp.weixin.qq.com/s?__biz=Mzk2NDgwNjA2NA==&mid=2247486329&idx=1&sn=b929c1d91320284649a91023983eafab&scene=21#wechat_redirect)我们拿到了第一个域凭据。现在的问题是：**拿着这个凭据能做什么？** 答案藏在Kerberos协议里。

Active Directory的身份认证核心是Kerberos协议。理解Kerberos的工作原理，是理解几乎所有AD攻击技术的前提——Kerberoasting、AS-REP Roasting、Golden Ticket、Silver Ticket、Pass-the-Ticket、Delegation攻击，全部建立在Kerberos的设计之上。

本文从攻击者的视角，拆解Kerberos每一步认证中可被利用的弱点。

### 一、Kerberos认证流程：三次握手背后的信任链

Kerberos的核心思想是"票据"——用户不直接向服务出示密码，而是持票据证明身份。整个流程涉及三个角色：

* **客户端（Client）**：请求访问资源的用户
* **KDC（Key Distribution Center）**：域控制器上运行的认证服务，包含两个子服务

+ **AS（Authentication Service）**：负责验证用户身份，颁发TGT
+ **TGS（Ticket Granting Service）**：根据TGT颁发服务票据ST

* **服务端（Service）**：目标资源服务器

#### 完整认证流程

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9
* 10
* 11
* 12
* 13
* 14
* 15
* 16
* 17

```
  客户端 KDC(域控) 服务端    |     |     |    |--- AS-REQ ------------->|  (1) 用户名+时间戳        |    |    (用用户密码哈希加密)    |      (证明知道密码)       |    |     |     |    |<-- AS-REP --------------|  (2) 返回TGT             |    |    (TGT用krbtgt密钥加密)  |      (用户无法解密TGT)   |    |     |     |    |--- TGS-REQ ------------>|  (3) 出示TGT，请求       |    |    (附带目标服务SPN)      |      访问某服务          |    |     |     |    |<-- TGS-REP -------------|  (4) 返回ST（服务票据）   |    |    (ST用服务账户密钥加密)  |     |    |     |     |    |--- AP-REQ ------------------------------>|  (5) 出示ST    |     |    |<-- AP-REP -------------------------------|  (6) 验证通过
```

**关键设计特征（也是攻击面的根源）**：

1. **TGT用krbtgt账户的密钥加密**——谁拥有krbtgt的密钥，谁就能伪造任意TGT（Golden Ticket）
2. **ST用目标服务账户的密钥加密**——谁拥有服务账户的密钥，谁就能伪造该服务的票据（Silver Ticket）
3. **任何域用户都可以请求任何SPN的ST**——这是Kerberoasting攻击的基础
4. **AS-REP中的部分数据用用户密钥加密**——如果用户未启用预身份验证，攻击者可以离线破解（AS-REP Roasting）

### 二、Kerberoasting：用合法功能偷密码

#### 攻击原理

Kerberos协议有一个"设计特性"：**任何经过身份验证的域用户，都可以向KDC请求任何注册了SPN（Service Principal Name）的服务票据**。KDC不会检查请求者是否真的有权访问该服务——它只管发票。

返回的服务票据（ST）使用目标服务账户的NTLM哈希加密。攻击者拿到这个加密的票据后，可以在本地离线暴力破解——**整个过程不会产生任何登录失败日志**。

这就是Kerberoasting的恐怖之处：它完全合法，几乎无法被检测。

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