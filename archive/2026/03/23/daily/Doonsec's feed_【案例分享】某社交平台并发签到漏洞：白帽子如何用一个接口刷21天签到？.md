---
title: 【案例分享】某社交平台并发签到漏洞：白帽子如何用一个接口刷21天签到？
url: https://mp.weixin.qq.com/s/NQP8AB4ZMI2wlC1hxiDU1w
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:11:29.907707
---

# 【案例分享】某社交平台并发签到漏洞：白帽子如何用一个接口刷21天签到？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7AnuFAq7GcPgF2EvOPftS57Bbc6aZsbOvR4TibLq4HVznOAtdiaQxjkgFRad8ceooCw0NDytXW2ibDSSfpE9fuV1ic7Hjzo9Jwkymju5SEY0FM4/0?wx_fmt=jpeg)

# 【案例分享】某社交平台并发签到漏洞：白帽子如何用一个接口刷21天签到？

sec0nd安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于EnhancerSec
，作者EnhancerSec

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5WngeWlarEDVB5lEzu9QNlmueECfyyj5OH2wCbPXagXw/0)

**EnhancerSec**
.

这是一个更新自己在安全行业中所学所想所得的一个公众号，会不定时更新Web、Android、逆向等安全相关内容，当然也会有平时工作中的一些分享，希望给各行各业中的你们带来正能量。

# 【案例分享】某社交平台并发签到漏洞：白帽子如何用一个接口刷21天签到？

## 引子

📱 有没有试过为了攒够连续签到天数领福利，每天定闹钟打卡？但最近有白帽子发现，某知名社交平台的签到系统存在一个有趣的并发漏洞——**只需要对一个接口发起并发请求，就能一键刷出21天连续签到记录**！

这种"躺着就能领福利"的操作背后，隐藏着怎样的技术原理？今天就让我们一起揭秘这个并发漏洞的发现与利用过程。

## 核心发现：一个接口就能刷连续签到

### 漏洞定位

🎯 **漏洞接口类型**：自动登录接口（该接口被意外赋予了签到功能）

这个看似普通的自动登录接口，实际上同时承担了签到功能。白帽子在测试该平台的某个社交功能时意外发现：当用户点击"签到领奖励"按钮时，系统会调用这个接口来完成签到操作。

![](https://mmbiz.qpic.cn/mmbiz_png/7AnuFAq7GcNkfSKDQxFiclhCyS4U9qib3dQEawhEicDL31uqs3VDKLjsia4uoyVMe86zO8XhByNbEibqo2EVTqwu1nT1dlx5ZO0hG2iarhHu1snxU/640?wx_fmt=png&from=appmsg)

### 漏洞原理

✨ **并发请求绕过天数限制**：

* 正常情况下，用户每天只能签到一次，系统会记录连续签到天数
* 但该接口缺少对并发请求的有效控制（如防重放机制、请求频率限制）
* 通过工具对该接口发起大量并发请求，系统会将每个请求都识别为一次有效签到
* 最终导致连续签到天数被快速累积

## 复现步骤：白帽子手把手教你操作

📚 以下是完整的复现过程（仅用于技术研究）：

### 步骤1：准备工具

* 手机或模拟器安装目标APP最新版本
* 抓包工具（如Burp Suite、Charles）
* 并发请求工具（如Burp Intruder、Python脚本）

### 步骤2：抓取签到数据包

1. 配置抓包工具，开启HTTPS拦截
2. 打开目标APP，进入主页
3. 点击签到相关按钮
4. 在抓包工具中定位到签到请求（示例结构）：

```
GET /api/v1/autologin?version=xxx HTTP/2
Host: api.example.com
Cookie: [隐藏]
Device-Info: [隐藏]
Authorization: [隐藏]
User-Agent: [隐藏]
Accept-Encoding: gzip, deflate, br
```

### 步骤3：发起并发请求

* 将抓取到的数据包导入并发请求工具
* 设置请求次数（例如21次）
* 启动并发请求

![](https://mmbiz.qpic.cn/mmbiz_png/7AnuFAq7GcPzokZzsmZcasQkX5FJvKkPSiaquAo7vIt5DtErzwL15LtdCBzFricZWAf1e7eVNaJte2EljUYCoVoCn5mbZtspKtgPzLIhsDJ8s/640?wx_fmt=png&from=appmsg)

### 步骤4：验证结果

* 并发请求完成后，重新进入目标APP
* 查看签到页面，会发现已显示"连续签到21天"
* 可以正常领取对应天数的签到福利

![](https://mmbiz.qpic.cn/mmbiz_png/7AnuFAq7GcPhS4lkmpMvAvHbl189IkFXYYh7hlaRicQnQSxta3bM2kMwvfVqiahNGDzxSjL4icJxK7FbOqj1uXIsWv69PLc1EvpJO7FpK9oibnE/640?wx_fmt=png&from=appmsg)

## 漏洞分析：为什么会出现这种问题？

### 技术层面的原因

1. **接口设计缺陷**：自动登录接口同时处理签到逻辑，职责不单一
2. **缺少防重放机制**：没有对同一用户的重复签到请求进行校验
3. **请求频率限制缺失**：未限制单位时间内的请求次数
4. **事务处理不当**：并发场景下的数据一致性控制不足

### 安全影响

⚠️ **潜在风险**：

* 破坏平台的签到激励机制，影响用户公平性
* 可能导致平台资源（如虚拟物品、优惠券）被恶意刷取
* 若该接口存在其他功能，可能引发更严重的安全问题

## 修复建议：如何防止类似漏洞？

1. **接口职责分离**：将自动登录与签到功能分离为不同接口
2. **添加防重放机制**：使用唯一令牌（如nonce）防止重复请求
3. **实施请求频率限制**：对同一用户/IP的请求次数进行限制
4. **加强并发控制**：使用分布式锁或事务确保数据一致性
5. **完善日志审计**：记录异常签到行为，便于及时发现问题

## 安全声明

⚠️ **重要技术声明**本文仅用于技术研究和安全分享，内容基于公开的漏洞分析。禁止任何人利用本文所述技术进行非法操作，否则后果自负。我们倡导安全研究者遵循负责任的漏洞披露原则，共同维护网络安全生态。

## 写在最后

这个社交平台并发签到漏洞再次提醒我们：**看似简单的功能背后，往往隐藏着容易被忽视的安全风险**。对于开发人员来说，在设计接口时不仅要考虑功能实现，更要重视并发场景下的安全控制。

作为普通用户，我们也要提高安全意识：

* 不要使用第三方"签到助手"或"刷分工具"，这些工具可能存在安全风险
* 发现平台漏洞时，应通过正规渠道向平台反馈

📢 **互动时间**你还遇到过哪些有趣的APP漏洞？欢迎在评论区分享你的发现！

---

### 往期推荐

* [【案例分享】某SRC SSRF漏洞分享](https://mp.weixin.qq.com/s?__biz=MzI0NjE1NDYyOA==&mid=2247486518&idx=1&sn=adb9e70cfa236a3f48d9a153562090cc&scene=21#wechat_redirect)

* [【热点追踪】"小龙虾"开盖即食方案](https://mp.weixin.qq.com/s?__biz=MzI0NjE1NDYyOA==&mid=2247486572&idx=1&sn=34d754b903068d56d90b18cc989f00e0&scene=21#wechat_redirect)
* [【服务继续升级】EnhancerSec第六期漏洞挖掘培训招生啦！（文中抽奖）](https://mp.weixin.qq.com/s?__biz=MzI0NjE1NDYyOA==&mid=2247486693&idx=1&sn=114ba0a166ffeb25c5d55996e7644066&scene=21#wechat_redirect)

---

关注公众号，后续会有**网安求职**、**工具推荐**、**案例分享**等内容持续输出，师傅们都可以关注一下喔

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

sec0nd安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/u7ibmWw94HhyPjaGFbJ1aj02bPU5jwAmG8o7vJ9jgF7q3DaU2c6Bicqz1ZTLTRWLc188vgsWFMnyNE6CX8Y1zSaw/0?wx_fmt=png)

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