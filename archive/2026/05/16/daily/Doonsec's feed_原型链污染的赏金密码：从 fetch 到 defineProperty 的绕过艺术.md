---
title: 原型链污染的赏金密码：从 fetch 到 defineProperty 的绕过艺术
url: https://mp.weixin.qq.com/s/QyfvPvc2mxhUeuXyHVeZ7Q
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:47:29.308982
---

# 原型链污染的赏金密码：从 fetch 到 defineProperty 的绕过艺术

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qg1MKHx3jGHpE9CPS1CdduYbJnHNibNVthibCQwA6SrmLEGJobhfXibTeKPZYneoBVpZnpUeib3icoxmdXziaRrspBfaWG8mHU05AFd0jPOrqjAM4/0?wx_fmt=jpeg)

# 原型链污染的赏金密码：从 fetch 到 defineProperty 的绕过艺术

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

你可能经常在挖洞时盯着服务端，各种原型链污染玩得飞起。但你有没有想过，其实浏览器自带的 JavaScript API，本身就是一堆现成的“小工具”，等着你去污染。

更妙的是，这些 API 的利用方式，往往能绕过一些看起来做了防护、实则一戳就破的防御措施。

下面我们就用两个最常见的 API，带你看看怎么在客户端把原型链污染玩出花。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGHeCwv9ib3BAE3AWSXhCyozdvOJUPV1jsIapMmzeAqcWS1NMGRH4e2MJnJSl3ycObONXtH8430GvMKJOvkFnkCAgcIibl4XGw8JI/640?wx_fmt=png&from=appmsg)

一、fetch() 的软肋：没写出来的属性，正好我来帮你填

先看一段研发经常写的代码：

```
fetch('https://normal-website.com/my-account/change-email', {    method: 'POST',    body: 'user=carlos&email=carlos%40ginandjuice.shop'})
```

fetch() 接收两个参数，第一个是 URL，第二个是一个“选项对象”，用来控制这次请求的各种设置，比如请求方法、请求体、请求头等。

这里只写了 method 和 body，可实际上，这个选项对象能接收一大堆属性，这里都没写，关键就在这个“没写”上。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGHVI4WiaHo8pQ6lQSkiby8ZXKmDpd9lyFCIYSBGNGhdrg8Ria7JmAxlz5xShlawxibhnE0hHskFNJuZ8O8glWP3Xky6TicHafwAt0jM/640?wx_fmt=png&from=appmsg)

如果攻击者能往 Object.prototype 上提前挂一个属性，比如 headers，那这个属性就会顺着原型链，被这个没定义的选项对象“继承”过去。换句话说，你虽然没写 headers，但 fetch 内部仍然可能用到一个 headers 属性，而这个属性恰恰是可以污染进去的，这就埋下了一个大坑。

来看一个具体的漏洞场景。假设页面里有一段请求产品数据的脚本：

```
fetch('/my-products.json', { method: "GET" })    .then((response) => response.json())    .then((data) => {        let username = data['x-username'];        let message = document.querySelector('.message');        if(username) {            message.innerHTML = `My products. Logged in as <b>${username}</b>`;        }        // ... 其他产品列表渲染    })    .catch(console.error);
```

攻击者只需要在 URL 上做一点手脚，污染原型链：

```
?__proto__[headers][x-username]=<img/src/onerror=alert(1)>
```

这会干什么呢？

首先，它往 Object.prototype 上加了一个 headers 属性，里面又有一个 x-username 请求头，值是恶意 payload。

fetch 发请求时，选项对象没有显式写 headers，于是从原型链上继承了攻击者构造的那个。

服务端如果把这个请求头的值，如实写进了返回的 JSON 里的 x-username 字段。

回到客户端，x-username 的值就被塞进了 innerHTML，直接触发 DOM XSS。

整个过程毫不违和，甚至不需要页面本身有肉眼可见的漏洞点。只要选项对象里有没显式赋值的属性，就有可能被赋一个恶意版。不只是 headers，body 等其他属性也可以用同样的套路污染。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGHAKtjiatkT2MXXvGlW51DqRyia2QaOxfEjTE1gcXdasUPplFWdBuDZBAGdvKwUic9AYNwEFZq8WicGzicS8ECPA43a50S0Y3k4xFsk/640?wx_fmt=png&from=appmsg)

二、Object.defineProperty() 的盲区：防御姿势不对，等于给攻击者留门

有些开发者知道原型链污染很危险，于是开始用 Object.defineProperty() 来“锁死”关键属性，写法大概是这样：

```
Object.defineProperty(vulnerableObject, 'gadgetProperty', {    configurable: false,    writable: false})
```

意思很直白：这个属性你别想改，也别想删。看起来确实能防住原型链上飘下来的恶意属性。

但注意，Object.defineProperty() 的第三个参数，那个叫“描述符”的对象，本身也是一个选项对象。问题就出在这儿。

很多开发者只是用它来做“占位防御”，压根没设置 value 值。那这时候，攻击者可以提前污染 Object.prototype，挂一个恶意的 value 属性上去。描述符对象在读取 value 时，如果自身没有这个属性，就会顺着原型链找到那个被污染的 value。

于是就会发生很讽刺的一幕：

开发者用 Object.defineProperty() 严防死守，不让属性被篡改。

结果定义属性时用的“值”，却是攻击者通过原型链污染悄悄塞进去的。

防线在最关键的一步，被绕了个干净。

说到底，这两类利用的核心思路是一致的：开发者没显式赋值的那些属性，就是原型链污染的下手点。不管是为了偷懒，还是为了防御而写下的“看似安全”的代码，一旦忘记给关键属性亲手赋值，就可能被攻击者“帮忙”填上一个恶意版本。

下次做客户端侧挖掘时，多看一眼那些选项对象、配置对象，尤其是“防御性代码”，往往越是想当然安全的地方，越藏着惊喜。

觉得这波分析有帮助的话，可以点个“在看”，转发给同样热爱漏洞挖掘的搭子。平时挖洞遇到什么刁钻的原型链污染绕过案例，也欢迎到后台发消息聊聊，后面会持续分享更多有关漏洞挖掘的实战玩法。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

升斗安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

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