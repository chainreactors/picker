---
title: Chrome扩展攻击指南（一）：基础知识
url: https://blog.xlab.app/p/4db211d1/
source: 明天的乌云
date: 2024-11-25
fetch_date: 2025-10-06T19:14:51.594579
---

# Chrome扩展攻击指南（一）：基础知识

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

1. [1. 组件介绍](#%E7%BB%84%E4%BB%B6%E4%BB%8B%E7%BB%8D)
2. [2. manifest.json](#manifest-json)
3. [3. Content scripts](#Content-scripts)
4. [4. Inject scripts](#Inject-scripts)
5. [5. Background scripts](#Background-scripts)
   1. [5.1. Popup](#Popup)
   2. [5.2. Options](#Options)
6. [6. 通信架构](#%E9%80%9A%E4%BF%A1%E6%9E%B6%E6%9E%84)
7. [7. 参考](#%E5%8F%82%E8%80%83)
8. 8. 相关文章

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

# Chrome扩展攻击指南（一）：基础知识

发表于
2024-11-24

分类于

[安全](/categories/%E5%AE%89%E5%85%A8/)
，
[漏洞挖掘](/categories/%E5%AE%89%E5%85%A8/%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98/)

阅读次数：

本文字数：
2.3k

阅读时长 ≈
2 分钟

浏览器扩展有以下特点，认为是不错的攻击目标

1. 使用量大
2. 功能和权限非常丰富
3. 开发者鱼龙混杂
4. 业界关注度不高

本文尝试从整体组件架构和历史漏洞出发，总结攻击链路，尝试挖掘漏洞并进行攻击利用

原文写于2023.5内部分享，现简单编辑后拆分为3篇发出

[Chrome扩展攻击指南（一）：基础知识](/p/4db211d1)

> 介绍Chrome扩展的各种组件功能和通信机制，和一些参考资料

[Chrome扩展攻击指南（二）：漏洞分析](/p/4db211d2)

> 结合漏洞案例，分析各组件的攻击面，最终绘制完整的攻击链路图

[Chrome扩展攻击指南（三）：全局视角](/p/4db211d3)

> 对商店的全量扩展进行扫描分析，统计风险和漏洞情况

## 组件介绍

首先大概了解一下Chrome扩展中的几个关键组件

在阅读时可以同步打开一个本地扩展认识一下

> macOS默认在 `~/Library/Application Support/Google/Chrome/Default/Extensions`
> Windows默认在 `%localappdata%\Google\Chrome\User Data\Default\Extensions`

## manifest.json

扩展程序的配置清单，在扩展程序代码的根目录

1. 名称，描述，版本等
2. API权限定义，如读写书签/历史/Cookie等Chrome API
3. 网站权限定义，允许无视同源策略访问哪些网站
4. 定义`Content scripts`是哪些js，在哪里何时运行等
5. 定义`Background scripts`是哪些js
6. `CSP`策略…

![](/p/4db211d5/manifest1.png)

![](/p/4db211d5/manifest2.png)

## Content scripts

在`manifest.json`中的`content_scripts`定义

在每个标签页中运行，每个扩展一个隔离环境，有独立的`JavaScript`变量，`CSP`策略等，同时拥有一部分Chrome API功能，只与网页中的JS使用同一个`DOM`

一般用来处理与网页`DOM`相关的功能，或与`Background scripts`通信交互完成相关功能

同源策略与所在的标签页相同

![](/p/4db211d5/content.png)

## Inject scripts

由于`Content scripts`与网页隔离，有些功能又需要访问网页空间中的数据

扩展程序往往会在`Content scripts`中通过`DOM`注入`script`标签执行一些代码，这个脚本被我称之为`Inject scripts`

|  |  |
| --- | --- |
| ``` 1 2 3 ``` | ``` let script = document.createElement('script') script.src = balabala document.head.appendChild(script) ``` |

`Inject scripts`是一个非常特别的存在，与网页中的其他JS同等地位，也混淆了扩展程序代码和网页代码，也引入了一些攻击面，这部分再漏洞篇细讲

## Background scripts

在`manifest.json`中的`background`定义

可以理解为扩展程序的后台服务，拥有完整的Chrome API功能，但不能直接访问`DOM`

一般用于持续运行的功能，或依赖相关Chrome API的功能

在一定的权限设定下，无同源策略限制

在Manifest V2中是一个HTML，叫`background.html`，如果是JS的话会自动生成一个HTML

![](/p/4db211d5/background.png)

在Manifest V3中是一个JS，叫`Service Worker`

![](/p/4db211d5/serviceworker.png)

还有一些页面与`Background`地位相同，但位置不同，而且只在打开相关页面的时候才会运行，不会一直运行

### Popup

在`manifest.json`中`browser_action`中定义

是点击扩展图标后弹出的页面，权限与`Background`组件相同

![](/p/4db211d5/popup.png)

### Options

在`manifest.json`中`options_page`定义

为扩展的选项页，权限与`Background`组件相同

![](/p/4db211d5/options.png)

## 通信架构

![](/p/4db211d5/message.png)

`Webpage`是指网页`Javascript`的空间，与`Content`共享`DOM`，其中`window`比较特殊，虽然是共用一个`window`，但有变量隔离，具体细节后面在讲

由于共用`window`，`Webpage`与`Content`可以使用`window.postMessage`进行通信

为了简化架构图，`Background`包含了`background.html`，`Service Worker`，`Popup`，`Options`等组件，因为他们的权限和地位都相同

在`Content`和`Backgroud`之间则使用`Chrome API`用于传递数据

不过需要注意的是，当`Content`调用`chrome.runtime.sendMessage`时其实在向所有`Background`页面中广播

同理，`Background`页面之间使用`chrome.runtime.sendMessage`发送消息时也相当于在广播

另外`Chrome API`中有提供了获取相关`Background`页面`window`的函数，获取`window`之后就可以使用`window.postMessage`进行通信

## 参考

LoRexxar入门系列

[从 0 开始入门 Chrome Ext 安全（一） – 了解一个 Chrome Ext](https://paper.seebug.org/1082/)

[从 0 开始入门 Chrome Ext 安全（二） – 安全的 Chrome Ext](https://paper.seebug.org/1092/)

[从 0 开始入门 Chrome Ext 安全（三） – 你所未知的角落 - Chrome Ext 安全](https://paper.seebug.org/1676/)

Wladimir Palant入门系列

[Anatomy of a basic extension](https://palant.info/2022/08/10/anatomy-of-a-basic-extension/)

[Impact of extension privileges)](https://palant.info/2022/08/17/impact-of-extension-privileges/)

[Attack surface of extension pages)](https://palant.info/2022/08/24/attack-surface-of-extension-pages/)

[When extension pages are web-accessible](https://palant.info/2022/08/31/when-extension-pages-are-web-accessible/)

文档

[Extensions - Chrome Developers](https://developer.chrome.com/docs/extensions/)

Paper

[DEF CON 29 - Barak Sternberg - Extension Land: Exploits and Rootkits in Your Browser Extensions](https://media.defcon.org/DEF%20CON%2029/DEF%20CON%2029%20presentations/Barak%20Sternberg%20-%20Extension-Land%20-%20%20exploits%20and%20rootkits%20in%20your%20browser%20extensions.pdf)

## 相关文章

* [Chrome扩展攻击指南（三）：全局视角](https://blog.xlab.app/p/4db211d3/)
* [Chrome扩展攻击指南（二）：漏洞分析](https://blog.xlab.app/p/4db211d2/)
* [让”低成本-高交互-定制化“的蜜罐成为可能](https://blog.xlab.app/p/4f53b9f3/)
* [蜜罐反制的现状与未来](https://blog.xlab.app/p/2b5e681a/)
* [获取真实的操作系统与浏览器的类型及版本](https://blog.xlab.app/p/18ce46b3/)

欢迎关注我的其它发布渠道

[Twitter](https://twitter.com/tmr11235)

[Telegram](https://t.me/tm_daily)

[RSS](/atom.xml)

[安全](/tags/%E5%AE%89%E5%85%A8/)
 [安全研究](/tags/%E5%AE%89%E5%85%A8%E7%A0%94%E7%A9%B6/)
 [漏洞挖掘](/tags/%E6%BC%8F%E6%B4%9E%E6%8C%96%E6%8E%98/)
 [代码审计](/tags/%E4%BB%A3%E7%A0%81%E5%AE%A1%E8%AE%A1/)
 [Chrome扩展](/tags/Chrome%E6%89%A9%E5%B1%95/)

[Wechat2RSS: self-hosted版本发布](/p/fd57c4cf/ "Wechat2RSS: self-hosted版本发布")

[Chrome扩展攻击指南（二）：漏洞分析](/p/4db211d2/ "Chrome扩展攻击指南（二）：漏洞分析")

[地球ICP备42号](https://beian.miit.gov.cn/)

© 2016 –
2025

透明人

站点总字数：
343k

Theme NexT works best with JavaScript enabled