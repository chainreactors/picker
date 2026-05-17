---
title: SRC 每日漏洞复现学习系列（第 2 篇）垂直越权漏洞+漏洞报告模板
url: https://mp.weixin.qq.com/s/qfELG3imPQpmkD8Cy6waMw
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:46:21.566583
---

# SRC 每日漏洞复现学习系列（第 2 篇）垂直越权漏洞+漏洞报告模板

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Vs6KsYlvMyOP4niawfzZkcoXv4Tj3uBXGmT8CHeQT8v1zYAAmISMyyle74fVLXgt4EnDscj91hcWIia8DKEo8Taaliaga41VgsEiauibXibXp5dCI/0?wx_fmt=jpeg)

# SRC 每日漏洞复现学习系列（第 2 篇）垂直越权漏洞+漏洞报告模板

原创

点击关注👉
点击关注👉

网络安全学习室

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

很多刚入门学网络安全、接触 SRC 漏洞挖掘的同学， 越权漏洞是仅次于 XSS，**最好发现、最容易复现、收录率最高**的经典漏洞。

今天完整拆解垂直越权：漏洞原理、挖洞思路、实操复现、标准 SRC 报告模板，零基础直接照着学。

---

## 一、漏洞基础认知

垂直越权通俗理解：**低权限用户，能直接访问 / 操作高权限或其他用户的私有数据**。 网站后端只做了前端限制，**没做接口权限校验**，改个参数就能随意查看他人信息。

### 常见危害

* 任意查看其他用户手机号、地址、订单、隐私资料
* 遍历后台敏感数据
* 绕过身份限制访问管理功能

---

## 二、挖洞选目标思路

日常测站重点盯着带这些参数的功能：

* 订单详情、账单记录、个人信息查看
* 业务审批、日志查看、资料查询
* URL 或请求包里包含：`id`、`uid`、`user\_id`、`order\_id`

只要能通过修改数字切换查看内容，**直接必测越权**。

---

## 三、漏洞复现实操步骤

### 步骤 1：登录普通账号，正常抓包

登录自己普通用户账号，打开订单详情页面，Burp Suite 抓到请求包：

```
POST /api/order/detail HTTP/1.1
Host: xxx.xxx.com
Content-Type: application/x-www-form-urlencoded
Cookie: sessionid=xxxxxx

id=1001
```

此时只能查看自己 id=1001 的订单。

### 步骤 2：篡改 ID 参数

把 id 改成其他用户编号：

```
id=1002
```

### 步骤 3：验证漏洞

重放请求后，网站直接返回**他人完整订单信息**，包含手机号、收货地址等隐私数据， 证明接口无权限校验，**垂直越权漏洞存在**。

---

## 四、SRC 标准漏洞报告模板

### 漏洞标题

某企业订单查询模块存在垂直越权漏洞，可未授权读取任意用户隐私数据

### 漏洞等级

中危

### 漏洞描述

该企业用户中心订单查询接口 `/api/order/detail` 未对请求中的 `id` 参数做身份归属与权限校验。 攻击者登录普通用户账号后，可随意修改订单 ID，未授权访问查看全站任意用户订单详情。 可批量遍历获取用户手机号、收货地址、消费记录等敏感信息，造成大规模用户隐私泄露，存在严重安全隐患。

### 复现步骤

1. 注册并登录普通用户账号，进入个人订单详情页面；
2. 使用 Burp Suite 抓取订单查询请求数据包；
3. 将自身订单 id 修改为其他用户订单 id；
4. 重放请求，服务器正常返回他人隐私订单数据；
5. 可遍历 ID 批量获取全站信息，漏洞复现成功。

### 影响范围

1. 可随意查看全站用户隐私信息，泄露手机号、住址等敏感数据；
2. 可批量遍历爬取数据，造成大规模信息泄露；
3. 易被恶意利用做社工渗透、信息倒卖；
4. 违反数据安全隔离规范，存在合规风险。

### 修复建议

1. 后端接口强制校验当前登录用户与数据所属人是否匹配；
2. 禁止用户可控 ID 直接遍历查询，做身份绑定；
3. 增加接口访问频率限制，防止批量爬取；
4. 对异常越权行为添加日志记录与安全告警。

### 漏洞证明

（放置抓包截图、修改参数前后对比、越权获取数据截图，敏感信息打码）

---

## 五、新手挖洞学习忠告

1. 越权不用复杂 Payload，改 ID 就能测，新手必练；
2. 看到 `id/uid/orderid` 养成第一时间改数测试的习惯；
3. 报告写清「可遍历、可查看隐私」更容易定级通过。

---

## 六、文末学习福利

如果你也是零基础、想参加竞赛网安但不知道从哪开始，可以点击文末阅读原文领取200节攻防教程，帮你少走弯路。后续我会持续更新网安实战、就业、副业相关干货，关注我，带你从零基础一步步靠网安变现。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/iaLzURuoralYx8yXB4LvFH5iaWSZLQIibIy0cjSua3jS1U4ibv8YxBJtIbq5qiahPnPyjH1eicWEbpedhFmOLmYozvFA/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=17)

---

## 结尾

本系列每日更新一个经典漏洞，纯技术干货零基础入门，跟着学快速提升 Web 安全与 SRC挖洞能力。

#SRC漏洞复现 #垂直越权 #越权漏洞 #Web安全入门 #网络安全学习 #漏洞报告模板

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralYfTVkr1yhiasbN03K2QuRu04rw6cCa7lx8kbE5uGoeTArEW3nCoRN0Y8dQDQjrCtTycTCjUxGmicvw/0?wx_fmt=png)

网络安全学习室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaLzURuoralYfTVkr1yhiasbN03K2QuRu04rw6cCa7lx8kbE5uGoeTArEW3nCoRN0Y8dQDQjrCtTycTCjUxGmicvw/0?wx_fmt=png)

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