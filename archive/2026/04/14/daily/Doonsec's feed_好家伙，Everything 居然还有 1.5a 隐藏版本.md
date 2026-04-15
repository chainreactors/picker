---
title: 好家伙，Everything 居然还有 1.5a 隐藏版本
url: https://mp.weixin.qq.com/s/dNrFl3p60fWMbf3gTKqGkw
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:40:18.406400
---

# 好家伙，Everything 居然还有 1.5a 隐藏版本

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aj4fOOkmqMIo0OnB5zzyjMjQbgJrWfD5c8hynyHoyiazXtB1iaEUZRCoic7B5aia3U3K42AszKibIk7VjR022oEm4gDZsQfbay4nYed2aT5KAO1Q/0?wx_fmt=jpeg)

# 好家伙，Everything 居然还有 1.5a 隐藏版本

原创

ralap
ralap

网络个人修炼

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

之前我专门写过一篇推文，对比过 Everything 和 Anytxt 两款文件搜索工具的核心区别。彼时的 Everything，是当之无愧的**文件名搜索天花板**，凭借毫秒级检索速度、极致轻量化，成为大家电脑里的必备工具；而 Anytxt 则主打**内容搜索**，专治 “记得文件内容，却忘了文件名” 的痛点，两者各司其职，互补性拉满。

可万万没想到，Everything 早就悄悄发力，布局内容搜索功能，而且**开发时间远比我想象中要早**。这项重磅能力并没有放在稳定版里，而是藏在它的长期测试版中，默默打磨了很久。

先厘清一个关键事实，避免大家用错版本：

目前 Everything 官网最新**稳定版**，依旧是 **1.4.1.1032**（2026 年 1 月更新）。这个版本专注稳定、轻量，**只支持文件名搜索，没有内容检索能力**，适合追求稳妥的普通用户。

![](https://mmbiz.qpic.cn/mmbiz_png/aj4fOOkmqMKmG5jBzpkGA2AZeicet012Or8oqufzejTicQgpBvZdtbYdk2ibOibg9elrGG7SibkaMw9uJbvjmIbIdwQGhAGAOBNo5W9XyAjmc9XY/640?wx_fmt=png&from=appmsg)

而支持内容搜索、拼音搜索、暗黑模式的，是它的 **1.5 Alpha 长期测试版**。这款版本早在 **2021 年 3 月** 就发布了首个公开测试版，算下来已经**迭代测试接近 5 年**，最新版已更新至 **1.5.0.1408a（2026 年 4 月 2日）**，仅在官方论坛发布，不对外主动推送。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMLKhUtHvJ6ggibp1fqEYdWFVfFVcTOiaPcOR2Pwwcg3uibEcRCdNsYiboicJCDaJ5TZFOU99xlG4XYUaoO5JXDctzXJNpr10sZTtyJc/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/aj4fOOkmqML74fgYibibzDIBEA4qulsJ0SAKt73tLaEJnsicYJOf22aGpII6s4XBYXQyPso6NdZxia8ErDWU9ibbCgQ9MheQU31N8EjoNOTIGB0U/640?wx_fmt=png&from=appmsg)

接下来就聊聊，这款打磨了近 5 年的 1.5 测试版，到底藏了哪些实用亮点，每一个都很戳人。

---

## 一、核心亮点1：内容搜索，补齐最大短板

##

这应该是1.5测试版最重磅的更新，也是最让我意外的一点——毕竟此前Everything一直专注于文件名搜索，如今终于补齐了内容搜索的短板，实现了“文件名+文件内容”双重检索。

根据官方论坛的帮助文档（开发者void于2023年1月27日发布），内容索引（Content indexing）是1.5版本的核心内置功能，从首个公开测试版就已支持，并非后续临时添加。它支持Word、Excel、PPT、PDF、TXT、代码文件等多种主流格式，不用再额外安装插件，也不用切换到Anytxt，一款工具就能搞定所有搜索需求。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMKnpracvdtZSTwfciaEtDk8dVwm7kMwTOlFR23e1W4qiaSuIWDZzwAAOTc6YJjou8ZkNicRicuZNkE1OMrlOQ9fZGBbduzIAt3y2bA/640?wx_fmt=png&from=appmsg)

使用方法也很简单：安装测试版后，进入「工具→选项→内容」，勾选“索引文件内容”，即可开启功能；内容索引建立相比anytxt要明显快。搜索时，在关键词前加上“content:”，双引号包含搜索内容，就能精准检索文件内的文字内容，速度依旧延续了Everything的极致高效，即便电脑里存储着海量文件，也能秒出结果，不用漫长等待。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMJ6ibXvP4yeDFjBoiavIwNjo4IAiaspVhFbC9a21dMDEccpIFw1BBGppKAYvC70sBM5X4kT5ctssXmbRiaLA3iaEDv76rZxI3oIRAyc/640?wx_fmt=png&from=appmsg)

更贴心的是支持**自定义索引范围**，可以只选需要的文件夹，避免全盘占用资源，轻量化优势依旧在线。

---

## 二、核心亮点2：主题支持，自定义界面风格

##

1.5 终于打破了 1.4 单调的界面，新增**主题支持与暗黑模式**，美观度和舒适度明显提升。

官方内置多种风格，日常最实用的暗黑模式可以直接在「视图 → 主题」切换。至于金属色、血色、蔚蓝色等自定义主题代码，我已经帮大家整理好。需要的同学可以在公众号后台回复关键词：**主题代码** 获取一键复制指令。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMKmNvhd9hMVMt8WK4KeeMQibvQjKMvxUzMPFktWw5NIOCOQV19icuSC33dXKicfMSQTjcCzhHliby8s8Sa7tCMvEy1rB3K1gScXia6o/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMKPeicBGZTScecaVQQQPPCrNHia1DY0Nm218NhLW5E7cWHSw5MC2ibF2VO1iauib9ibPRickh6K2DvwQjz1RAxbibchmZGohArAmvHRic3M/640?wx_fmt=png&from=appmsg)

---

## 三、核心亮点3：原生拼音搜索（中文用户专属）

支持全拼和首字母搜索，不用切换输入法，直接输入拼音就能找到对应的文件，对中文用户非常友好，还能在设置中自定义拼音搜索模式

![](https://mmbiz.qpic.cn/mmbiz_png/aj4fOOkmqMLiafbR4ZMCE66SK5swmEBJicic2gpM5iaIfVNXSojSoMEmeuB9meqOTBTCqgxc2BSDWFzeCYZ7lto4ibzPIjrYcIicwQwro3HYibseBI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aj4fOOkmqMItdEj5yz3POqjJFba3m2XyQuBACeibVTsSaF6YlHoQj6DnmaYyBYB772N3XmKic1ByO8pwibtw48PYuhPDRzLV9y3WKOqv9JUerM/640?wx_fmt=png&from=appmsg)

---

## 四、其他实用亮点，体验再升级

##

除了三大核心亮点，1.5 还迭代了很多能明显感知的功能：

* **重复文件查找**

  按名称、大小、内容哈希筛选，轻松清理重复文件
* **高级条件搜索**

  按大小、日期、格式精准筛选，比如查找大于 1M 的文件
* **后台索引优化**

  索引在后台执行，不卡顿界面，大库也丝滑
* **安全性提升**

  加强服务权限管控、防 DLL 劫持、加密连接更安全

整体体验比 1.4 完整太多，已经不只是一个文件名搜索工具，而是一套真正的全能文件检索方案。

1.5a版本体验下载地址

https://www.voidtools.com/forum/viewtopic.php?t=9787#download

最后，如果追求绝对稳定，官网的1.4.1.1032稳定版，依然是最佳选择。对于喜欢尝鲜、想提升文件搜索效率的小伙伴，不妨试试1.5测试版，1.4版本和1.5a版本可同时安装，互不冲突。

###

---

###

### 参考链接

[1]https://www.voidtools.com/forum/viewtopic.php?t=9787#help

[2]https://www.voidtools.com/forum/viewtopic.php?f=12&t=12666

[3]https://www.voidtools.com/forum/viewtopic.php?f=12&t=9793】

[4]https://www.voidtools.com/forum/viewtopic.php?t=13373

###

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKkAnrPt4lEpmGwWaLib4DxIATR0yiaZib3hQAtBDDAMUulZJL39cia5ttpCR5mbu0opYiawr47diaCwhFg/0?wx_fmt=png)

网络个人修炼

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5y2fUaoQPfKkAnrPt4lEpmGwWaLib4DxIATR0yiaZib3hQAtBDDAMUulZJL39cia5ttpCR5mbu0opYiawr47diaCwhFg/0?wx_fmt=png)

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