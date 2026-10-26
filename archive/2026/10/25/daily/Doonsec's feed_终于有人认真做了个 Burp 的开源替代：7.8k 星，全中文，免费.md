---
title: 终于有人认真做了个 Burp 的开源替代：7.8k 星，全中文，免费
url: https://mp.weixin.qq.com/s/kAz8wdGnuThPPmLP-tOm2g
source: Doonsec's feed
date: 2026-10-25
fetch_date: 2026-10-26T07:18:03.906707
---

# 终于有人认真做了个 Burp 的开源替代：7.8k 星，全中文，免费

# 终于有人认真做了个 Burp 的开源替代：7.8k 星，全中文，免费

原创

大白
大白

知白守黑1024

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

YAKLANG · ALL-IN-ONE SECURITY PLATFORM · AGPL-3.0

7.8k 星"Burp 挑战者"
底层是一门自研安全语言

Yakit · 劫持 / Fuzz / 反连 / 被动扫描 · Electron 客户端 + Yak 引擎

干 Web 安全的，电脑里基本都装着**BurpSuite**。但说实话，国内用它一直有三个绕不开的疙瘩：**破解版有被投毒的风险，商业版一年几千块，插件要写 Java 代码**——这是 Yakit 团队在项目里公开点破的三个痛点，句句戳在从业者的经验上。

开源圈的回应叫**Yakit**：yaklang.io 团队出品的**交互式应用安全测试平台**，7.8k Star、总下载 3 万+，最新版 v1.4.9 就在 10 月 23 日刚发布。它给自己的定位很直接——"BurpSuite 的年轻中国挑战者"，MITM 劫持、HTTP History、Repeater、Intruder 这些常用功能全部实现，再加一层 Burp 没有的东西：**底层是一门专门为网络安全发明的编程语言**。

![Yakit 产品功能全景](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1iaqRft3ibzo5k52T8nuhKbQ0R8Vumo9va8j4H1SohKPZ6zXrMvpWuOViblmXkFJ0T9w3zJL8q7KXjYg5GtgqxdIfHUhiaQjyEJe4M/640?wx_fmt=jpeg&from=appmsg)

功能全景：资产发现、漏洞扫描、手工渗透测试、进阶工具、身份认证——覆盖日常工作全流程

先花三十秒认识它

$ whoami

▸Yakit — 交互式应用安全测试平台（单兵工具）

▸架构：Electron 客户端 + Yak gRPC 引擎，引擎可远程部署

▸底层：Yak 语言 — Golang 宿主的图灵完备安全 DSL

▸生态：直接融合 nmap 指纹库 / wappalyzer / nuclei yaml poc

▸数据：7.8k Star · 下载 3 万+ · v1.4.9（10 月 23 日）

▸平台：Windows / macOS（x64 + arm64）/ Linux 全平台

$ license: AGPL-3.0 · 商用需官方授权 ▊

它不是"扫描器套壳"，是语言 → 引擎 → GUI 三层

市面上的"Burp 平替"大多是把代理和扫描器包个壳，Yakit 的路线完全不同——**先造语言，再做平台**。团队先写了一门叫**Yak**的领域专用语言：宿主语言 Golang、图灵完备、语法像 Python 一样简单，把端口扫描、SYN 无状态探测、Nmap 式服务指纹、MITM 劫持、POC 框架这些安全能力**全部做成语言内置函数**，写脚本不用装任何第三方库。

有了语言，再为它挂一个**gRPC 服务器**把全部能力暴露出去；最后用 Electron 写了**Yakit 这个 GUI 客户端**，通过 gRPC 操控引擎。这个分离式架构有个很实用的好处：**引擎和客户端可以不在一台机器上**——重活扔到服务器跑，本地只留一个"遥控器"界面。对不想学语言的人，GUI 给了你全部能力；对会写脚本的人，任何界面里都能随时插一段 Yak 代码。

另外它不重复造轮子：**nmap 指纹库、wappalyzer 指纹库、nuclei 的 yaml POC 体系直接编译融合**进引擎，你现有的 PoC 资产可以无缝带过来。

![Yakit 架构图](https://mmbiz.qpic.cn/mmbiz_jpg/j7ZnQr1RD1jiczQdgQL0tEmbIEMkEMs4H8aH39oiaOpZtH994ut8hGawdKFtz6EoT00qD80lAFnRwnTPMxUt8eibwicibfTaaJibPSfUVPmicygia28/640?wx_fmt=jpeg&from=appmsg)

官方架构图：上层用户区（Electron + gRPC 客户端），下层核心功能区（Yak gRPC 引擎 + 语言能力矩阵），与平台无关、可远程部署

MITM 劫持台：说"百分百替代 Burp"的底气

MITM 模块的玩法和 Burp 一脉相承：**劫持 → History → 发送到 Web Fuzzer**，下载证书、拦截请求响应、改包重放，一个都不少。界面上有手动劫持、自动放行、被动日志三种模式，拦下来的包可以提交、丢弃，或者直接**劫持响应**改服务端返回的内容。

真正的差异化在底层：Yak 引擎**手写了 HTTP 库**，不做严格校验——意味着你可以构造**畸形的请求包、响应包**，用在一些特殊场景的漏洞利用上。Burp 会帮你"纠正"的包，这里原样发得出去。

![Yakit MITM 劫持界面](https://mmbiz.qpic.cn/mmbiz_jpg/j7ZnQr1RD1h2b6tarrUnia8aYjMLnXZicdEdlmO2FdvVB1UCeSuiaGcklsWjicXzHNSBMRV4SFxw6ibvCWXYfrVTmlETfRUjmCEHIlrNSiaoFKl44/640?wx_fmt=jpeg&from=appmsg)

MITM 实操界面：拦截请求后可编辑完整报文，左侧是可勾选的被动扫描插件

原理上，MITM 是一个 HTTP 代理：开着时自动转发流量，手动劫持模式下阻塞请求、做解 Gzip、处理 chunk 等解码动作，让包变得"人类可读"再显示给你；重放时自动修复你构造的 HTTP 原文，保证包有效。插件系统通过**请求/响应两个 HOOK 点**挂在链路上，热加载，随时生效。

![MITM 交互式劫持原理](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1hdG8cHTRpPp3icUqmgmSTU0iarSOgfuaC4mDHlQfOSH7SzjCUpM9aqMsbibxoXibL2OqlnXx8waJJG7lpB0DBw1AoLArEiabZgPMEk/640?wx_fmt=jpeg&from=appmsg)

请求与响应双向劫持，每个 HOOK 点都可挂 Yak 插件

Web Fuzzer：把 Intruder 的操作路径砍掉大半

Burp 的 Intruder 用过的都懂：标记 payload 位置、选攻击类型、导入字典、配置线程，一路点下来四五个界面。Yakit 的 Web Fuzzer 把这套流程压缩成**在 HTTP 原文里直接写标签**：

POST /api/login HTTP/1.1

Host: target.com

{"id":"{{int(1-100)}}", "user":"{{file(/tmp/users.txt)}}"}

`{{int(1-100)}}`自动生成数字序列，`{{file(...)}}`直接读字典文件；**多个标签同时出现时自动做笛卡尔积**，不用再选"狙击手还是集束炸弹"。更狠的是**热加载标签**：字典表达不了的数据（比如按规则生成的身份证号），直接插一段 Yak 脚本现场生成，省掉了"写代码造字典再导入"的整条支线。

你只管关心业务数据——CRLF 修复、Content-Length 补全、chunk 传输、boundary 处理这些脏活全部由引擎兜底。发包前后还各有一个 HOOK（beforeRequest / afterRequest），可以插 Yak 代码**动态修改每一个包**，比如实时签名、加密参数。

![Web Fuzzer 流量重放架构](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1ho9CNDrgichSdYNSurg1naDucb7IzU28gdUZN5CHnAnyCIYSytIspbyVAkR2DulZZprVuRd8ejRcg1ZfCvMnGufqIicNa2UzDmU/640?wx_fmt=jpeg&from=appmsg)

带 Fuzz 标签的数据包经 gRPC 进引擎，双 HOOK 可插码，结果流式返回并入库

反连平台：一个端口吃下所有协议

打 Log4Shell、Fastjson 这类漏洞都要反连：传统做法是公网服务器上给每种协议各起一个服务——LDAP 一个端口、RMI 一个端口、HTTP 再来一个，又重又麻烦。Yak 用**端口协议复用**解决了：手工实现各种协议的识别逻辑，**一个端口同时应答 LDAP / RMI / HTTP / ICMP / TCP / DNS**的回连请求，收到什么协议就返回什么 Payload。

因为协议是手工实现的，你还能**构造畸形协议包**做利用，甚至让数据走 DNS、ICMP 通道——对方 TCP 不出网的场景也有戏。配套的 Reverse Shell 模块体验接近原生 ssh：退格键、方向键不再乱码，弹回来的 shell 是真的能用。反连检测覆盖 TCP、DNSLog、ICMP 三种方式，命令执行类漏洞一测一个准。

![端口协议复用反连原理](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1gUKZWOvsC11qtOhgsMYiaicTiaxuibiarjy4s0qib8YiaPibPr2GVYicX9kNxDRsHnQUibRxNXcKG8S8NBlBuMxo6yPJYxstoTvUaYJJjHI/640?wx_fmt=jpeg&from=appmsg)

Facade server 单端口监听，自动识别回连协议（RMI/LDAP/HTTP/...）并返回对应 Payload

被动扫描：流量过一遍，漏洞自己冒出来

回看上面那张 MITM 截图的左侧栏——那就是内置的被动扫描插件库：**Spring4Shell（CVE-2022-22965）、Log4Shell、FastJSON（via DNSLog）、Shiro 认证绕过、ThinkPHP RCE、SSRF、Spring Actuator 信息泄露**等十几个检测插件，勾选即启用。你正常浏览目标站点，流量经过代理的瞬间插件就在后台跑检测，**不用手动发一个包**。配合插件商店，社区写的检测脚本装上就能用，而写一个插件只需要会 Yak 语言——比写 Java 插件的门槛低得多。

三步上手

**第一步：下载安装。**官网直接下安装包：Windows amd64 的 exe、macOS 的 dmg（Intel 和 Apple Silicon 都有）、Linux 的 AppImage。装完首次启动，客户端会**自动下载匹配的 Yak 引擎**，不用手动配环境。

**第二步：装 HTTPS 证书。**MITM 界面里一键下载证书并信任，这样 HTTPS 流量才能解密劫持。
**第三步：挂代理开测。**浏览器代理指向`127.0.0.1:8083`，打开手动劫持或被动扫描，正常访问目标站点就能开工。进阶玩法是在设置里把引擎切换成远程模式，让引擎跑在 VPS 上。

**发布前说清楚三件事：**① Yakit 采用 AGPL-3.0 协议，官方另行要求**商业化使用需获得授权**，公司环境商用前先谈；② 工具仅面向**合法授权**的测试场景，别对着没授权的目标扫；③ AGPL 传染性对二次开发有约束，改代码对外提供网络服务需开源。

BurpSuite 依然是伟大的工具，但"唯一选择"的时代该翻篇了。Yakit 最有价值的不是替你省了几千块 license，而是那条**语言 → 引擎 → GUI**的路线：不会写代码的人有了顺手的中文 GUI，会写代码的人有了把任意安全想法变成工具的语言。这种底座式的开源项目，值得每一个安全从业者放进工具箱。

觉得有用的话，三连支持一下

点赞 👍 · 在看 👀 · 转发 🔄
让更多还在用破解版 Burp 的同学看到这个项目

后台回复关键字

20261025

获取项目地址与官网入口

本文素材来自 yaklang/yakit 开源项目公开资料 · 仅作技术分享 · 请在授权范围内使用

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zlD2iah6QpJjciciaI6Ylp5L7rn9Y2O6cTxzf9Suxyw0cwibRgVtpuBzNrqS1ibK3USX8IXHulcNen2rMApDXn352cg/0?wx_fmt=png)

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