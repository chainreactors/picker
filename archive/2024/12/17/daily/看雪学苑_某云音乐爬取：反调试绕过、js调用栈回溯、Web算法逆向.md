---
title: 某云音乐爬取：反调试绕过、js调用栈回溯、Web算法逆向
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587045&idx=1&sn=451d4e39ee6982e4ac225a270737091b&chksm=b18c3f2f86fbb639ad78c51ca7b83b5ee91c3ec4e0bea7a28f337a0344bd1f1ace99cd8bb4bc&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-12-17
fetch_date: 2025-10-06T19:40:04.795183
---

# 某云音乐爬取：反调试绕过、js调用栈回溯、Web算法逆向

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmk8zJx0Wxpl48N3uMmAticicpyJDwjeBkNWekGJZensuToGkmv2syztEnw/0?wx_fmt=jpeg)

# 某云音乐爬取：反调试绕过、js调用栈回溯、Web算法逆向

Brinmon

看雪学苑

```
一

前言
```

本文以某云音乐爬虫案例为基础，详细探讨了从工具准备到目标数据爬取的全过程，包括爬取目标的需求分析、关键数据的识别以及加密参数的解析和破解。在学习其他案例是发现很多爬虫文章都是莫名其妙的获得某些数据,不知道前因和后果,所以这里就讲逆向和调试的细节分享出来!包括利用源代码搜索、静态堆栈调用回溯、动态调试以及动态堆栈调用等技术手段，最终锁定目标加密函数的调用位置。

## 文章声明

**本文章中所有内容仅供学习交流，严禁用于商业用途和非法用途，否则由此产生的一切后果均与文章作者无关，本文只做模拟不做任何真实对象的爬取！**

## 爬虫工具准备

在正式开始之前，先确认以下工具和环境已准备就绪：

1. 浏览器

* 任意现代浏览器，例如 Chrome、Edge 或 Firefox，用于分析目标网站的网络行为。

2. Python 环境

* 配置完整的 Python 开发环境（推荐 3.8+），用于实现爬虫脚本和数据处理。

3. JavaScript 环境

* 配置可执行的 JavaScript 环境（如 Node.js），便于运行和测试目标网站中的 JS 代码。

4. 抓包工具

* 选择合适的抓包工具（如 Fiddler、Wireshark、Burp Suite），用来监控和分析网络请求。

5. 基础技能

* 具备基本的 JavaScript 和 Python 编程能力，了解加密算法的基础知识，尤其是 AES 和 RSA 的常见使用场景。

#

```
二

爬虫入门必遇到的坎，以及绕过方式
```

##

## 爬虫过程中遇到的主要反爬手段和技术难点

> 新手在接触爬虫时最难也是最痛苦的阶段就是绕过反爬虫和反调试了,目前总结一下爬虫过程种遇到的主要反爬手段和难点技术,这里主要做汇总分析,想了解详细原理的可以移步相关链接!

下面是目前主流的反调试和反爬虫手段：

1.**无限 Debugger 技术**
这些方法的核心思想是通过动态插入`debugger`来中断代码执行，增加调试的复杂度。通常采用这些技术的组合与变形，使反调试手段更加隐蔽且有效。

◆简单方法：直接在前端**页面中插入**`debugger`语句。

◆使用`eval`创建`debugger`。

◆通过`Function`动态创建`debugger`。

◆**重写**JavaScript 原生功能：重写`constructor`、`eval`、`setInterval`等，在原生功能中添加debugger。

2.**阻止开启浏览器开发者工具**
通过检测浏览器的行为或使用工具强行禁用开发者工具，这些方法可以有效防止爬虫或调试行为，尤其在页面载入和交互过程中增加了监测和干扰。

◆**简单方式**：禁用右键菜单和`F12`快捷键。

◆**检测开发者工具**是否开启：

* 通过浏览器上下文加载的**时间间隔来判断**，若开启调试，则跳转到空白页。
* 根据浏览器宽高和实际网页**宽高判断**是否在调试状态，若是则动态替换页面内容。

◆使用开源项目如`disable-devtool`**插件来强制禁**用开发者工具。

3.**前端代码混淆技术**
前端代码混淆技术通过减少代码可读性、隐藏关键数据、以及分发资源的方式，阻碍逆向工程和爬虫的成功率，提高了安全性和防护力度。

◆**压缩代码**：通过压缩 JavaScript 代码，删除注释和格式化空格，降低代码的可读性。

◆**混淆代码**：使用混淆技术将变量、函数名等改为无意义的字符，增加破解难度。

◆**加密关键数据**：将敏感数据加密后传输，增加数据解密的难度。

◆**使用 CDN**：通过 CDN 分发前端资源，隐藏实际的服务器请求地址，避免直接访问源代码。

浏览器反爬虫手段汇总：

1.记录--别想调试我的前端页面代码\_disable-devtool-auto 绕过-CSDN博客

2.js逆向-无限debugger的原理及绕过\_js debugger-CSDN博客

3.如何禁止别人调试自己的前端代码 - 向治洪的全栈技术 - SegmentFault 思否

4.如何防止别人调试你的前端代码？-duidaima 堆代码

## 目前反调试技术的通解手段和实现原理

> 我们为什么要绕过反调试?因为原生浏览器才是最好的js调试环境和算法逆向工具!不然为什么这么多的网页都来进行反爬虫反调试?而且市面上的最主流的调试工具都是浏览器?而不像Linux,Windows逆向那样市面上存在五花八门各种各样的调试器?下面就来讲解绕过反调试技术的核心原理!

###

### 原理讲解

目前，反调试手段主要通过检测浏览器的行为来进行防护。然而，这些反调试代码通常是从服务器端传输到浏览器的，这意味着这些代码必须先到达浏览器才能执行。关键问题在于，在从服务器传输到浏览器的过程中，反调试代码无法被执行，但相关的流量依然可以被第三方的抓包工具截获并转发。下面是流量的流程交互图：

正常的浏览器和服务器交互
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmkrjvKuPEtBn55ibPYia0Cw6WMAOoNn1Nicp62PjFzYNsUjImA7DGDVBrYA/640?wx_fmt=png&from=appmsg)

爬虫工作者一般的浏览器交互图
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmkbBNjb7vd0jia6ziadgyZI8QzYCjtIVF8R9uQiazhMW6X7f0C13feqUHjA/640?wx_fmt=png&from=appmsg)

因此，尽管开发者工具被禁用，但是由于反调试代码通常嵌入在 JavaScript 或 HTML 中，仍然可以通过抓包工具获取这些前端页面代码进行分析。我们可以使用中间的代理工具Charles,Fiddler,等抓包工具,替换相关的 JavaScript 和 HTML 代码，从而逐步一次次的绕过目标页面中的各种反调试手段。这样，就能利用浏览器自带的调试工具和抓包工具进行逆向分析和爬虫操作。这种方法有效地避开了反调试措施，助力爬虫技术的实施。

### 反爬虫案例实际分享

下面是相关案例,都可以通过替换原有js代码来进行绕过反调试：

> 在Web安全领域，反调试技术常被用于防止攻击者通过开发者工具对网页进行调试，从而保护网页中的敏感逻辑和代码不被轻易篡改或分析。然而，随着攻击者技术的不断提升，绕过这些反调试措施的方法也层出不穷。以下是对几种常见绕过反调试技术的策略进行理论化总结与拓展。

#### 1. 禁用开发者工具的反制措施

**案例一**展示了使用`disable-devtool`插件阻止用户打开开发者工具的情况。针对此类反调试技术，攻击者和防御者可以采取以下策略：

◆**修改浏览器设置**：部分浏览器允许用户通过修改设置或使用命令行参数来禁用或绕过某些插件的限制。

◆**使用外部工具**：利用诸如Browser Exploitation Framework（BeEF）等外部工具，可以在不打开开发者工具的情况下执行JavaScript代码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmkDnSO2FGicNGGw3w0mfONXSshCTfeJJUXBicmqia85icdwS0FeYuzH0KVAw/640?wx_fmt=png&from=appmsg)

#### 2. 应对`eval`和`Function`构造函数的反调试

**案例二**展示了使用`eval`或`Function`构造函数执行无限`debugger`语句的反调试技术。这些技术通常会导致代码难以阅读和调试。攻击者可以通过以下方式绕过：

◆**代码混淆与去混淆**：对混淆后的代码进行静态分析，识别并去除混淆逻辑，从而找到原始的`eval`调用点。

◆**动态调试**：利用浏览器的调试工具或外部调试器，在运行时动态分析代码的执行流程，找到`eval`或`Function`调用的上下文。

◆**替换`eval`和`Function`**：通过修改网页代码，将`eval`和`Function`替换为其他不触发反调试机制的函数调用方式。

可以寻找页面中的eval放调试函数的混淆后调用,当然有些eval函数也是正常的只是用来迷惑人的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmkb4oQNaBiac93y5y1Ht7gstDn9OAC9QNJFeZXQMy9clZDqicd4NJy2Cpw/640?wx_fmt=png&from=appmsg)

#### 3. 嵌入开源框架中的反调试代码

**案例三**展示了将反调试代码嵌入到开源框架（如jQuery）中的情况。这种策略增加了识别和绕过反调试措施的难度。攻击者可以采取以下策略：

◆**源码分析**：下载并分析开源框架的源码，找到被嵌入的反调试代码段。

◆**版本对比**：对比不同版本的开源框架，识别出被篡改的代码部分。

◆**替换框架文件**：在不影响网页功能的前提下，替换被篡改的框架文件，以去除反调试代码。

将反调试代码加进开源框架jquery.js里面,让人摸不着头脑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmk7k0LibN8t3QcMIF51CmnL7SGZ2haXLUdgfkIz65bYaIicBvdibwVggqjw/640?wx_fmt=png&from=appmsg)

### 通过劫持页面源代码实现绕过无限debugger

实验网站：https://spiderbuf.cn/playground/h04
在实际操作中，攻击者需要综合考虑目标网页的复杂性、安全性以及自身的技术能力。

以下是一些实用的替换策略：

1.**备份原始代码**：在进行任何修改之前，务必备份原始网页代码，以防万一。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmksuAY6v122o3HGM3RZ9xGdfQWZr1S4JAyXA0PmmpqxWDSZJGWRf6MlQ/640?wx_fmt=png&from=appmsg)

2.**逐步替换**：不要一次性替换大量代码，而是逐步进行，每次替换后都进行测试，以确保网页功能不受影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmkeUAcur2BeezXbazsXWVfWC48ycLxnicI5atlveYnaANeEicRdoRhuPEg/640?wx_fmt=png&from=appmsg)

3.选中**魔改后的代码**，通过fiddle等抓包工具进行代码替换。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmkrsXtHp9AZrOQqbbJDvRiaa48jo5icMiatMg8c0sH8GNGwMJh7065SHfQA/640?wx_fmt=png&from=appmsg)

4.**测试与验证**：在替换完成后，进行充分的测试，确保网页在各种浏览器和环境下都能正常运行，并且反调试措施已被成功绕过。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmkHatTyeVjD1ekGKjzjk7iaXr5lngj5WEPLyU4Zn0OnWFRBhic4ia3FDozA/640?wx_fmt=png&from=appmsg)

#

```
三

开始分析某云音乐的正确爬取目标需求分析
```

##

## 抓取数据包获得目标资源来源URL

> 在Web爬虫和数据抓取领域，通过抓取数据包来获取目标资源的URL是一种常见且有效的策略。以下是对这一策略的理论化总结与拓展，包括目标确定、数据包分析、关键数据识别以及自动化实现等方面。

####

#### 一、目标确定

首先，需要明确要抓取的目标网页和具体的资源（如音乐、视频、图片等）。在本案例中，目标是抓取某云音乐平台上的音乐资源URL。明确目标后，可以开始分析资源的加载方式，如通过Ajax请求加载资源等。首先找到要爬取的目标网页：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmkV1IxrX9ovsdL5o5othZDe2gticprXW0BHaS4XAG2ib5Dico6OW2H8VnXA/640?wx_fmt=png&from=appmsg)

找到目标先确定单首音乐的爬取方式才可以确定完整的方法。

首先分析一下资源的加载方式：当我点击播放按钮后音乐开始播放，由此可以得出某云的资源加载方式是ajax！分析接下来的需求，先开启抓包然后筛选出需要的url资源目标链接。开始抓包，本次并无任何反调试主要是算法逆向。

#### 二、数据包分析

> 使用浏览器开发者工具或第三方抓包工具（如 Wireshark、Fiddler）捕获网络数据包后，可通过分析请求 URL、方法和请求头筛选出与目标资源相关的 HTTP 请求，重点关注 XHR 数据包，其中通常包含以 JSON 格式传递的关键数据（如资源 URL）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmk0JmdO3x0gzTAMbZglu1snZz1C00TMTGdpBgqojI2cl6L6TSyKF1ylQ/640?wx_fmt=png&from=appmsg)

开启F12后在点击音乐播放就可以发现很多的数据包，由于这种音乐格式的数据包大部分都是通过json格式的数据中藏有mp4链接来传递数据，所以首先就是选中XHR这里的数据包进行分析。

1.**筛选数据包**：在捕获的数据包中，筛选出与目标资源相关的HTTP请求。这通常可以通过分析请求URL、请求方法（如GET、POST等）以及请求头中的信息来实现。

2.**分析XHR数据包**：由于Ajax请求通常通过XHR（XMLHttpRequest）对象发送，因此应重点关注XHR数据包。这些数据包中可能包含以JSON格式传递的关键数据，如资源URL。

#### 三、关键数据识别

> 分析 XHR 数据包的响应内容时，可通过预览响应快速定位关键字段，解析 JSON 格式数据提取目标资源 URL，并通过直接访问或工具测试验证 URL 的有效性。

一个个的手工看，可以发现一个我们需要的资源链接：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmkJcBJgHL1Zicg3bwcjwdHXOJm6NiaAgiaPiaLGiboPpic1VXpjvhnx8yoKf9w/640?wx_fmt=png&from=appmsg)

可以看见update,weblog,get,v1等等的HTTP的请求数据包，这些数据包中都有可能藏有关键数据，但是更多还是靠经验，没有经验的话就直接一个个看：

◆update：可能是更新页面的数据包

◆get：可能是获取资源的数据包

◆weblog：可能是记录用户行为的数据包

◆v1:其他相关的数据包

主要是看数据预览部分，来查看数据！我们就可以得到一个音频链接：`http://m804.music.126.net/20241113011636/c53d40244287ed16507ad686b6a83e86/jdyyaac/obj/w5rDlsOJwrLDjj7CmsOj/28481676823/4af4/3b82/de3c/082fc537ce73819afdeb6694703f398a.m4a`

或者直接在媒体中也可以找到，但是我们是需要自动化，这样就算是拿到了也没用：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmkwHun9qtibS5R3bpddOPrsxzHNOroRaD9ezjd2A4hIwpnSJY8raAXtQw/640?wx_fmt=png&from=appmsg)

所以抓包到这里也就可以确定要分析的数据包了！目标url：`https://music.163.com/weapi/song/enhance/player/url/v1`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GFnjjXX36Wa1DgebJxRWmkKLKDHyxbibNwOQcX6C79sUwo0Zib0FlibIOx4NFcsY6AlY3iaNLkgdOP2g/640?wx_fmt=png&from=appmsg)

在XHR数据包中，需要仔细分析响应内容以识别关键数据。这通常涉及以下几个步骤：

1.**查看数据预览**：在开发者工具中，可以查看XHR数据包的响应内容预览。这有助于快速定位可能包含资源URL的字段。

2.**解析JSON数据**：如果响应内容是JSON格式，可以使用JSON解析工具（如在线JSON解析器或编程语言中的JSON库）来解析数据，并提取出目标资源的URL。

3.**验证URL**：提取出的URL可能需要进行验证，以确保其有效性。这可以通过在浏览器中直接访问该URL或使用其他工具（如curl、wget等）来测试。

## 正式开启目标URL的参数和负载分析

> 在现代的 Web 应用程序中，为了防止爬虫和恶意攻击，开发者采用了各种加密与混淆技术来保护传输中的敏感数据。与传统的明文传输相比，加密的请求参数和复杂的加密逻辑能够有效增加爬虫抓取的难度，提高服务器安全性。本文将...