---
title: 前端端口探测全拆解：计时攻击为什么歪，onload 状态为什么准
url: https://mp.weixin.qq.com/s/BriIfH5jXu-w0NJzszoWeA
source: Doonsec's feed
date: 2026-11-06
fetch_date: 2026-11-07T07:56:30.413080
---

# 前端端口探测全拆解：计时攻击为什么歪，onload 状态为什么准

# 前端端口探测全拆解：计时攻击为什么歪，onload 状态为什么准

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

【内容概述】做渗透这些年，最让人后背发凉的攻击，往往不是什么 0day，而是"浏览器自己把内网情报递出去"。这篇拆解一个老牌但依然经典的浏览器端端口扫描技巧：利用 Chrome / Firefox / Edge 在加载 iframe 时对"端口开没开"产生的不同行为，纯前端就能摸清目标机器（甚至你家里路由器、NAS）开了哪些 Web 服务。从"计时攻击为什么不准"讲到 onload 状态检测的核心原理，再到三款浏览器的三种脾气、实战用途和防守方该堵的口子。含关键代码片段与思路，仅供授权测试与防御研究。

---

你以为端口扫描得搬出 Nmap、开着命令行对着目标一顿扫？其实最省事的办法，是让受害者自己的浏览器帮你扫。

我前阵子在一个"浏览器里渲染用户提交内容"的沙箱应用里做测试，想搞清楚：能不能在不碰任何后端接口的情况下，让页面自己把某个 IP 上跑了哪些服务摸出来。结果 Chrome 一个不起眼的行为，把门给撬开了。

这篇不卖关子，把这套纯前端端口探测的玩法拆给你看。看懂之后你会明白：为什么很多"内部网络探测"根本不需要攻击者自己发一个包。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGF2JlDTxvkkbjPcQgdwPFxXeK5a3J8QgJ4Ux6zAyYfmV5fRKgrt9w3LMz93oOvKI0ss47ao1JibOemFwTchEolpMrNj3K5mxsJo/640?wx_fmt=png&from=appmsg)

## 一、老办法为什么"歪"：靠计时，永远差口气

在说新路子之前，得先提两句前辈。前辈早年用  标签加计时技术，在不写 JavaScript 的情况下做过端口探测；也写过局域网扫描器，同样靠计时攻击，外加 WebRTC 和 XHR。

它们共同的命门是：靠"响应快还是慢"来猜端口开没开。可网络抖动、排队、重试一进来，计时就糊了——所以这类方法从来不是 100% 准，顶多算"猜得比较准"。

我后来琢磨出的这套，不靠计时，靠状态：浏览器自己会把"端口开没开"这个事实，以 URL 变化的形式"说漏嘴"。

## 二、核心发现：Chrome 加载失败时会"改名"

关键在 Chrome 的一个行为。当你用一个 iframe 去请求某个端口、而那个端口根本没服务监听（连接被拒绝），Chrome 会弹个错误页，同时悄悄把地址栏的 URL 改成了chrome-error://chromewebdata/。

巧妙的地方来了：不管端口开没开，iframe 都会触发一次 onload——Chrome 大概是想让你"看不出端口是否开放"。但我们可以通过一个小动作把它拆穿：

先加载目标 URL，捕获第一次 onload，然后立刻用同一个 iframe 再发一次请求，只不过这次在地址后面加个 #（锚点）。

* 如果端口关着：第一次 onload 是 `chrome-error://...` 那一页；第二次因为 URL 从 `chrome-error://` 变成了 `chrome-error://...#xxx`，URL 变了，于是又触发第二次 onload。一共两次。
* 如果端口开着（真有 Web 服务器）：第二次请求只是个哈希变化，浏览器不会对已加载页面重新加载，所以只触发一次 onload。

一次还是两次——这就是判断端口开闭的全部依据。比计时攻击干净太多了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGE6ZpBat8O6GbDeYaibhYkZoicNG778DdRVeYjfOsM5yroBicFgNczibnGD5y0NCbbImDZUPRsriaib3m9ibwOlcGZP7Mnu8r2hoibUqeE/640?wx_fmt=png&from=appmsg)

## 三、三款浏览器的三种"脾气"

原理通了，但每家浏览器脾气不一样，得分别哄。

Chrome：得手动"补一刀"。因为开放端口只触发一次 onload，我们得靠定时器兜底——超过 5 秒没等到第二次 onload，就判定为开放端口，推进下一个。核心就这几行：

```
iframe.onload = function(){  calls++;  if(calls > 1){ clearTimeout(timer); next(); return; }  a.click(); // 补发带 # 的第二次请求};timer = setTimeout(function(){  validPorts.push(pos); next();}, 5000);
```

顺便提个坑：新版 Chrome 里如果目标带了 X-Frame-Options: deny，它也会改 URL，于是会被这套工具误判成"端口关闭"。这反而是防守方能利用的点。

Firefox：最省心，也最猛。Firefox 只在有效 Web 服务器上触发 onload，连接拒绝时压根不触发。所以连"补一刀"都省了，直接看 onload 有没有来、超时没有就行。更狠的是 Firefox 能扛大量 iframe 不卡，我直接开了1000 个 iframe 的池子并发跑，速度拉满。而且它连"无效响应"都能扫，意味着不只能找 Web 服务，Redis 这类别的端口也能被揪出来。

Edge：跟 Chrome 反着来。有效端口时 URL 变成错误页、触发 onload；无效端口时只有哈希变、不触发 onload。所以判定逻辑正好反过来写——两次 onload 才算开放。

## 四、这东西到底能干嘛，又卡在哪

落到实战，它的价值不在"扫公网"，而在扫内网。想象一个场景：某个你信任的 Web 应用存在 XSS，攻击者注入这段脚本，你一打开页面，你家的路由器、NAS、手机、内网那些没人管的管理后台，开放端口就被悄悄列出来了——而你全程没装任何工具。

但它也不是万能：

* 主要针对 Web 服务（Chrome 路线），Firefox 路线能扩到 Redis 等；
* 前提是受害者得加载这个恶意页面，或存在可信上下文里的 XSS；
* 现代 Chrome 对 `X-Frame-Options` / CSP `frame-ancestors` 的处理一直在变，老技巧会慢慢失效——所以这是"概念验证"，不是永久武器。

  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/qg1MKHx3jGHBmS5v0Aggh7IZLh6PvN71wFKQmDc193nS6YbbI0w6O8IMo3oMR2xia5IRYXnqcib3eKPzJJlBwiccu0kyCNBFsjSHURdFyER0jc/640?wx_fmt=png&from=appmsg)

## 五、防守方该堵的口子

如果你是开发或运维，几件事能直接把这个路子掐大半：

* 敏感页面、管理后台加上 `X-Frame-Options: SAMEORIGIN` 或 CSP 的 `frame-ancestors 'self'`，别让自家页面被塞进别人的 iframe；
* 内网服务别裸奔在默认端口上，路由器 / NAS 的管理界面绑定到内网专用网段、加鉴权；
* 别忽视 XSS——它是这类"浏览器内侦察"的入场券，修好输入输出，比事后堵扫描器管用。

说到底，端口扫描这事儿，最可怕的版本从来不是攻击者拿着扫描器猛敲，而是你亲手打开的浏览器，在你看不见的地方把门牌号报了出去。

---

你身边有没有那种"管理后台直接裸奔在公网"的离谱事？A. 见过，公司路由器后台公网就能进B. 不敢想，回去得查查自家 NAS

评论区选一个，点赞最高的那类，我下期写"内网资产怎么自查"。

![](https://mmbiz.qpic.cn/mmbiz_png/qg1MKHx3jGG4qiccPIj9KgVbXLiaTibeCTHXWbPeIJHjpPUcwnnvP5AsDQLE21njWwsdnkSO2kvqxVcUtKibLT4QZcicKfAjb2W0YSw9DPq1PmUw/640?wx_fmt=png&from=appmsg)

觉得有用，转发给公司管服务器的同事，让他也绷根弦。想持续看这类实战拆解，关注不迷路。

👍 这篇拆得值？点个赞，让更多安全人看到这个老坑

💬 你见过最离谱的"内网裸奔"是啥？评论区聊聊 A 还是 B

🔁 转发给管服务器的同事，别等被扫了才想起堵端口

📣 关注【升斗安全】，下期写"内网资产自查清单"

本文仅作安全技术研究与防御科普，所涉技术为已公开的浏览器端端口探测概念验证，仅供授权环境下的测试与防御参考，严禁用于未授权扫描或入侵。

守住边界，保持敏锐。

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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