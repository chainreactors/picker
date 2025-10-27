---
title: 前端黑魔法 —— 如何让自己的函数变成原生函数 - EtherDream - 博客园
url: https://govuln.com/news/url/q0Do
source: Sec-News 安全文摘
date: 2023-08-21
fetch_date: 2025-10-04T11:58:53.910180
---

# 前端黑魔法 —— 如何让自己的函数变成原生函数 - EtherDream - 博客园

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[![返回主页](/skins/custom/images/logo.gif)](https://www.cnblogs.com/index-html/)

# [EtherDream's Blog](https://www.cnblogs.com/index-html)

##

* [首页](https://www.cnblogs.com/index-html/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/EtherDream)
* 订阅
* [管理](https://i.cnblogs.com/)

# [前端黑魔法 —— 如何让自己的函数变成原生函数](https://www.cnblogs.com/index-html/p/masquerading-custom-functions-as-native-functions.html "发布于 2023-08-07 11:07")

如何让自己的 JS 函数变成原生函数

# 前言

熟悉 JS 的都知道，原生函数转成字符串，显示的是 native code：

```
alert + ''    // "function alert() { [native code] }"
```

如果用自己的函数对其重写，显示的则是自己的代码：

```
alert = function(s) { console.log(s) }
alert + ''    // "function(s) { console.log(s) }"
```

有没有什么黑魔法，让自己的函数也变成 native code，从而掩盖这个破绽?

# toString

最容易想到的办法，就是重写函数的 toString 方法：

```
alert = function(s) { console.log(s) }
alert.toString = () => "function alert() { [native code] }"

alert + ''          // "function alert() { [native code] }"
```

不过这种办法破绽极多，例如调用原生 `toString` 即可将其原形毕露：

```
Function.prototype.toString.call(alert)   // "function(s) { console.log(s) }"
```

即便原生 `toString` 也被重写，还可创建 iframe 页面获取未被污染的原生 `toString`。

事实上这个办法并没有改变函数本质，只是改变观察结果而已。

# bind

在[《如何让 JS 代码不可断点》](https://www.cnblogs.com/index-html/p/js-anti-breakpoint.html)文中提到，通过 bind 方法创建的新函数，其实是原生的。

我们来验证对比下：

```
// 原生结果
console.log('before:', alert + '')    // "function alert() { [native code] }"

alert = (function() {
  function alert(s) {
    console.log('test:', s)
  }
  return alert.bind(window)
})()

// 重写结果
console.log('after:', alert + '')     // "function () { [native code] }"

alert('hello bind')
```

两者主体部分都为 `[native code]`。不过重写后的结果少了函数名，比原生更短。算是一个小破绽。

此外，除了字符串结果不同，函数的 `name` 和 `length` 属性也有差异：

```
// 原生值
console.log('before:', alert.name)    // "alert"
console.log('before:', alert.length)  // 0

alert = (function() {
  function alert(s) {
    console.log('test:', s)
  }
  return alert.bind(window)
})()

// 重写值
console.log('after:', alert.name)     // "bound alert"
console.log('after:', alert.length)   // 1
```

> 运行前刷新页面

可见通过 bind 创建的新函数，其 `name` 属性会多一个 `bound`  前缀（中间有个空格），也算是个小破绽。

由于我们的 alert 函数声明了一个 s 参数，导致其 `length` 属性变成了 1，而原生的则为 0。

当然函数的 `length` 属性可随意伪造，只需声明相应个数的形参即可。使用 `...rest` 这种剩余参数声明的形参，不会增加 `length` 值。

```
function A(...args) {}
A.length    // 0

function B(i, ...args) {}
B.length    // 1
```

# Proxy

提到重写、切面等概念时，不得不联想到一个功能强大的 API —— `Proxy`，不少黑魔法都借助它实现。

先来试下，被代理的函数转成字符串是什么结果：

```
new Proxy(function F() {}, {}) + ''    // "function () { [native code] }'
```

结果和 bind 类似，虽有 `native code`，但少了函数名。

下面完整对比下，包括 `name` 和 `length` 属性：

```
console.log('before:', alert + '')      // "function alert() { [native code] }"
console.log('before:', alert.name)      // "alert"
console.log('before:', alert.length)    // 0

alert = (function() {
  function alert(...args) {
    console.log('test:', ...args)
  }
  return new Proxy(alert, {})
})()

console.log('after:', alert + '')       // "function () { [native code] }"
console.log('after:', alert.name)       // "alert"
console.log('after:', alert.length)     // 0

alert('hello proxy')
```

相比 bind 方案，Proxy 不会修改 `name` 属性，因此破绽更少。

不过在 Safari 浏览器上有明显的破绽，函数转成字符串后变成：

```
function ProxyObject() {
    [native code]
}
```

# WebAssembly

由于 JS 程序是文本格式的，因此函数 toString 的结果自然能包含相应的代码。如果是二进制程序，那么 toString 的结果又会是什么？这个问题，可以用 WebAssembly 的导出函数来验证。

[MDN 文档](https://developer.mozilla.org/en-US/docs/WebAssembly/Exported_functions) 中提到，WebAssembly 导出的函数会显示成 `native code`。

我们构造一个精简的 WebAssembly 程序，将导入的 x.y 函数导出成 z 函数：

```
(module
  (func (export "z") (import "x" "y") (param externref))
)
```

使用 [wat2wasm](https://webassembly.github.io/wabt/demo/wat2wasm/) 将其转成二进制数据，并进行封装：

```
function genNativeFunction(callback) {
  const buf = new Uint8Array([
    0, 97, 115, 109, 1, 0, 0, 0, 1, 5, 1, 96, 1, 111, 0, 2, 7, 1, 1, 120, 1, 121, 0, 0, 7, 5, 1, 1, 122, 0, 0
  ])
  const mod = new WebAssembly.Module(buf)
  const obj = new WebAssembly.Instance(mod, {x: {y: callback}})
  return obj.exports.z
}

alert = (function() {
  function alert(...args) {
    console.log('test:', ...args)
  }
  return genNativeFunction(alert)
})()

console.log(alert + '')     // "function 0() { [native code] }"
console.log(alert.name)     // "0"
console.log(alert.length)   // 1

alert('hello wasm')
```

WebAssembly 导出函数转成字符串后确实包含 `native code`，不过破绽也非常明显，其中的函数名居然是一个数字！正常的 JS 函数显然不可能以数字命名。破绽 +1。

同样 `name` 属性也变成了数字。破绽 +2。

并且 WebAssembly 函数的形参数量是固定的，因此 `length` 属性也难以伪造。破绽 +3。

因此这个方案虽然有趣，但并不隐蔽。

当然在奇葩的 Safari 上，返回结果并不包含函数名，并且 `name` 属性是个空字符串。不过这依然是个大破绽。

此外在 Chrome 上，调试器单步断点（F11）无法进入 WebAssembly 的导出函数：

```
debugger
alert(123)
```

看来之前的《如何让 JS 代码不可断点》又可以新增一个黑魔法了。

# 总结

想要完美伪造一个原生函数还是非常困难的，多多少少总有一些破绽。

如果有更好的方案，欢迎补充~

posted @
2023-08-07 11:07
[EtherDream](https://www.cnblogs.com/index-html)
阅读(1878)
评论(0)

收藏
举报

刷新页面[返回顶部](#top)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250923174722171-270282128.jpg)](https://qoder.com/)

[博客园](https://www.cnblogs.com/)
  ©  2004-2025

[![](//assets.cnblogs.com/images/ghs.png)浙公网安备 33010602011771号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=33010602011771)
[浙ICP备2021040463号-3](https://beian.miit.gov.cn)