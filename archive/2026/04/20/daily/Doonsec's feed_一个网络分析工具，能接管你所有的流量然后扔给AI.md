---
title: 一个网络分析工具，能接管你所有的流量然后扔给AI
url: https://mp.weixin.qq.com/s/F24vhDOlh1j95D3MqQN2HQ
source: Doonsec's feed
date: 2026-04-20
fetch_date: 2026-04-21T04:48:51.383237
---

# 一个网络分析工具，能接管你所有的流量然后扔给AI

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibdw4icp2Lw4Wug5PgQmOuhzsq992APN26I4OdJdE3HdCd5Dmjho2ws35sUuibadxHsIHmXaqoKC5U6yE0n4FYXMfibBrIriaOibkyGU/0?wx_fmt=jpeg)

# 一个网络分析工具，能接管你所有的流量然后扔给AI

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 不用再在各个抓包工具之间来回切换了。Anything Analyzer把网页、桌面应用、手机App、脚本、命令行等各种来源的网络请求一锅端，然后自动用AI帮你逆向分析协议、审计安全，甚至破解JS加密。

## 传统抓包的痛点，它一次性解决了

搞网络分析或者逆向，最烦的是什么？工具太分散。想抓浏览器得用DevTools，抓个安卓App得开Charles，看个终端脚本又要配置Wireshark代理环境。来回切换不说，抓到包只是第一步，面对几百上千条请求记录，手动分析简直像大海捞针。

Anything Analyzer的想法很简单：把所有来源的流量，都弄到一个地方来。

它的工作原理像一张大网。对于网页，它用内嵌浏览器控制；对于桌面应用、终端命令、脚本、手机App，它启用一个在8888端口监听的MITM代理。不管哪来的HTTP/HTTPS请求，最终都汇集到同一个“会话”里。然后，你点一下分析，AI就能自动帮你把活儿干了。

## 三大核心能力，让你告别手动

### 一、全场景抓包，什么流量都能抓

不再是“浏览器的专属工具”。它支持几乎所有你能想到的来源：

* **网页**

  ：直接用它内置的浏览器操作，抓取API请求，特别适合OAuth登录、前端加密这类场景。
* **桌面应用**

  ：把系统的HTTP/HTTPS代理指向它，那些用Electron写的应用、Postman的请求都能看得一清二楚。
* **终端命令**

  ：给curl或者wget命令加上一个代理参数 (`-x http://127.0.0.1:8888`)，它的请求就不再神秘。
* **脚本程序**

  ：无论是Python的requests库，还是Node.js的fetch，在代码里配置一下代理就行。
* **手机App**

  ：在手机的Wi-Fi设置里，把HTTP代理设为你电脑的IP和8888端口，然后装个证书，就能看见App的后台数据怎么跑了。

这些请求都进同一个地方，AI分析的时候就有全局视野。

### 二、AI智能分析，不只是看个热闹

抓包工具很多，能自动分析的很少。Anything Analyzer的AI分析分两步走：先智能过滤掉图片、CSS这些“噪音”请求，然后聚焦在关键的API请求上进行深度分析。

它有五种分析模式：

* **自动识别**

  ：让AI自己判断这是什么类型的协议或API。
* **API逆向**

  ：自动还原接口的端点、参数、认证方式，甚至能生成Python复现代码。
* **安全审计**

  ：帮你找找有没有token泄露、CSRF漏洞、敏感数据明文传输这些问题。
* **性能分析**

  ：看看哪些请求慢，瓶颈在哪。
* **JS加密逆向**

  ：这个厉害了，它能自动拦截页面中的fetch、XHR请求，还能Hook住crypto.subtle、CryptoJS甚至国密SM2/3/4的调用，把加密逻辑给你扒出来，提取相关的JavaScript代码片段。

分析报告是流式输出的，像和AI聊天一样，你还能继续追问更多细节。

### 三、能自己用，还能被AI Agent调用

它支持MCP协议。一方面，它可以作为客户端，接入外部的MCP Server来增强自己的分析能力。另一方面，它自己也能作为一个MCP Server，把抓包和分析功能暴露出去。这意味着，你可以让Claude Desktop、Cursor这类AI助手直接调用它的能力，AI Agent也就有了“看”网络流量的眼睛。

项目技术栈清晰，基于Electron和React，数据存本地SQLite。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibfm4XlnhhtF9LeMOTM08Yoq3Yht6hX4W2XHepicMJK88RiaazLhFib8TZxHq9l8AVTGAbyiaq5FKY09FncPNbfVtjaJrPJnR74lsH4/640?wx_fmt=png&from=appmsg)

## 具体能干什么？几个真实场景

光说能力有点抽象，看看这些场景你熟不熟悉：

* **逆向一个网站的API**

  ：不用自己一个个接口去试了。用它的内嵌浏览器操作一遍，AI直接给你整理出API文档和认证流程。
* **想知道某个App在后台偷偷请求什么**

  ：手机连上代理，操作App，所有网络活动尽收眼底，包括那些隐藏的、有签名校验的接口。
* **遇到前端加密参数搞不定**

  ：用它的JS Hook功能，自动定位到加密函数，还原算法流程。
* **调试一个复杂的命令行工具**

  ：让curl请求走代理，AI能一步步解读它发了什么，响应了什么。

## 怎么用？上手很简单

去GitHub的Releases页面下载你系统对应的安装包就行（Windows是exe，macOS是dmg，Linux是AppImage）。

### 抓网页最快

先在设置里填好你的大模型API Key（支持OpenAI、Claude以及其他兼容接口）。然后新建一个会话，输入目标网址。接着在内置浏览器里正常操作网站，点击开始捕获。操作完了就点停止，再点分析，选个模式，等结果就行了。

### 抓其他设备，靠MITM代理

第一次用需要去设置里安装一下它的CA根证书。然后开启代理（默认8888端口）。之后根据不同设备配置：

# 终端命令
curl -x http://127.0.0.1:8888 https://api.example.com/data

# Python脚本
proxies = {"http": "http://127.0.0.1:8888", "https": "http://127.0.0.1:8888"}
requests.get("https://api.example.com/data", proxies=proxies)

# 手机
# Wi-Fi设置里，手动代理填入电脑IP和8888端口

然后新建会话开始捕获，那些设备上的流量就会自动流进来。

关于证书，有几个细节：它在Windows/macOS上有固定的存储路径，第一次安装要管理员权限。它只是“偷看”流量，不会修改请求和响应的内容。遇到WebSocket，它会直接做隧道转发，不解密。单个请求体超过1MB的会被自动跳过，以免卡死。

## 优点和需要注意的地方

**优点很明显**：全平台流量整合，省去切换工具的麻烦；AI深度分析能力强，尤其JS加密逆向很实用；集成MCP，未来可玩性高。

**需要注意**：首先，你得有自己的大模型API，它本身不带AI。其次，安装CA证书涉及到系统安全设置，需要你完全信任这个工具。最重要的是，它的功能非常强大，请务必遵守法律法规，只用于合法的安全研究、开发调试和学习目的。

说实话，把AI自动分析和全栈抓包结合，这个思路确实让逆向和安全审计的门槛降低了一大截。对于经常和网络协议打交道的开发者、安全研究人员来说，它是个值得一试的效率工具。

---

**获取方式：私信回复"anything-analyzer"获取**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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