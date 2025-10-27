---
title: 前端黑魔法 —— 隐藏网络请求的调用栈 - EtherDream
url: https://buaq.net/go-173785.html
source: unSafe.sh - 不安全
date: 2023-08-07
fetch_date: 2025-10-04T11:58:56.832603
---

# 前端黑魔法 —— 隐藏网络请求的调用栈 - EtherDream

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/54704961ff76a85a8140c017c95cf9e7.jpg)

前端黑魔法 —— 隐藏网络请求的调用栈 - EtherDream

浏览器网络控制台会记录每个请求的调用栈（Initiator/启动器），可协助调试者定位到发起请求的代码位置。为了不让破解者轻易分析程序，能否隐藏请求的调用栈？事实上，使用之前 《如何让 J
*2023-8-6 13:31:0
Author: [www.cnblogs.com(查看原文)](/jump-173785.htm)
阅读量:33
收藏*

---

浏览器网络控制台会记录每个请求的调用栈（Initiator/启动器），可协助调试者定位到发起请求的代码位置。

![](https://img2023.cnblogs.com/blog/273626/202308/273626-20230804174418311-2014689431.png)

为了不让破解者轻易分析程序，能否隐藏请求的调用栈？

事实上，使用之前 [《如何让 JS 代码不可断点》](https://www.cnblogs.com/index-html/p/js-anti-breakpoint.html) 文中的方案，通过「内置回调」到「原生函数」，即可隐藏请求的调用栈:

```
const fn = fetch.bind(window, '/?by-click')
window.addEventListener('click', fn, {once: true})
```

点击页面任意位置即可产生网络请求，并且 Initiator 显示为 `Other`:

![](https://img2023.cnblogs.com/blog/273626/202308/273626-20230804174418338-415155798.png)

由于该方案依赖事件，因此得使用极易触发的事件，例如 `mousemove`。但用户一动不动的话，程序流程就会卡在这里。

如果直接用 JS 驱动该事件，例如：

```
const fn = fetch.bind(window, '/?by-dispatch')
window.addEventListener('click', fn, {once: true})

window.dispatchEvent(new Event('click'))
```

那么调用栈会原形毕露：

![](https://img2023.cnblogs.com/blog/273626/202308/273626-20230804174418367-2114184367.png)

类似的，人为制造一个 `error` 事件：

```
const img = new Image()
img.onerror = fetch.bind(window, '/?by-onerror')
img.src = ''
```

或者人为产生一个 `message` 事件：

```
const fn = fetch.bind(window, '/?by-message')
window.addEventListener('message', fn, {once: true})
window.postMessage('')
```

这些都会暴露调用栈。

我们回顾下浏览器中总共有哪些事件：

<https://developer.mozilla.org/en-US/docs/Web/API/Event#interfaces_based_on_event>

事实上最容易触发的事件就在第一个：`AnimationEvent`。因为 CSS 动画播放时间是可控的，所以我们可创建一个 0 秒的动画，从而立即触发 `animationend` 事件：

```
<style>
  @keyframes k {}
  #el {
    animation-duration: 0;
    animation-name: k;
  }
</style>
<div id="el">Hello</div>
<script>
  const fn = fetch.bind(window, '/?by-animation')
  el.addEventListener('animationend', fn)
</script>
```

并且能完美隐藏调用栈：

![](https://img2023.cnblogs.com/blog/273626/202308/273626-20230804174418383-12287930.png)

除了动画事件，CSS 中的过渡事件 [TransitionEvent](https://developer.mozilla.org/en-US/docs/Web/API/TransitionEvent) 也能实现同样的效果。

```
const el = document.createElement('div')
el.style = 'transition: font 1s;'
document.body.appendChild(el)

const fn = fetch.bind(window, '/?by-transition')
document.body.addEventListener('transitionrun', fn)

requestAnimationFrame(() => {
  el.style.fontSize = '0'
})
```

![](https://img2023.cnblogs.com/blog/273626/202308/273626-20230804174418329-315483194.png)

相比动画事件需创建一个 @keyframes CSS 规则，过渡事件直接使用元素自身 `style` 属性即可，因此更简单。

不过需注意的是，动态添加的元素立即修改 CSS 是无法产生过渡事件的，需稍作延时才能修改。[MDN 文档](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_transitions/Using_CSS_transitions#javascript_examples) 也提到这点。

考虑到「过渡事件」需推迟执行并多一个回调，这里选择「动画事件」的方案，封装成纯 JS 实现：

```
const xhr = new XMLHttpRequest()
xhr.onload = () => {
  console.log('xhr onload')
}
xhr.open('GET', '/privacy')

const container = document.createElement('div')
container.style = 'animation:0s linear 0s __a__;'
container.innerHTML =
  '<style>' +
    '@keyframes __a__{' +
      'from{font-size:0}' +
      'to{font-size:0}'
    '}' +
  '</style>'
document.body.appendChild(container)

const sendFn = xhr.send.bind(xhr)
container.addEventListener('animationend', sendFn)

const removeFn = container.remove.bind(container)
container.addEventListener('animationend', removeFn)

const timer = setTimeout(sendFn, 10)
const clearFn = clearTimeout.bind(window, timer)
container.addEventListener('animationend', clearFn)

// 用于参照对比
const xhr2 = new XMLHttpRequest()
xhr2.open('GET', '/public')
xhr2.send()
```

为了请求后续操作，这里使用 XHR 取代 fetch，方便回调和获取数据。

同时注册了 3 个 `animationend` 事件，第 1 个用于发送请求；第 2 个用于删除元素，这样页面中不会有 DOM 残留；第 3 个用于删除定时器 —— 假如出现意外情况导致动画事件未触发，或未能及时触发，那么至少还有后备定时器会帮我们触发请求。

由于 IE 浏览器 CSS 的 @keyframes 里必须有规则，否则动画事件不会触发。出于兼容性，随便放一些规则即可。

Chrome:

![](https://img2023.cnblogs.com/blog/273626/202308/273626-20230804174418350-1156787976.png)

FireFox:

![](https://img2023.cnblogs.com/blog/273626/202308/273626-20230804174418354-1587155485.png)

Safari:

![](https://img2023.cnblogs.com/blog/273626/202308/273626-20230804174418342-1558283450.png)

文章来源: https://www.cnblogs.com/index-html/p/hide-request-initiator.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)