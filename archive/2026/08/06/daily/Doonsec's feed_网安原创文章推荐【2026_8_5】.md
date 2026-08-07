---
title: 网安原创文章推荐【2026/8/5】
url: https://mp.weixin.qq.com/s/BqfWuE4wEuZb6I6pTR6j6A
source: Doonsec's feed
date: 2026-08-06
fetch_date: 2026-08-07T04:24:43.728164
---

# 网安原创文章推荐【2026/8/5】

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CZMNsicRfJADrL7BmnpOiagsUNo5KpssHnnrsRcmmU4ibQicjWeHhpFLJcfRR9f0PxHrpjyeicOdTHB43licuhibKXeia3KziaSMvPbQxDrnZzDP84og/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/8/5】

AJay13
AJay13

洞见网安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 2026-08-05 微信公众号精选安全技术文章总览

> 洞见网安 2026-08-05

---

### 0x1 [SRC常见越权场景（一）](https://mp.weixin.qq.com/s?__biz=MzYzMzEwMjIzOQ==&mid=2247484097&idx=1&sn=a5fae8b6ffea03be075be80526502ecd&scene=21#wechat_redirect)

> N0n4m3 Sec 2026-08-05 20:35:47

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibRSlrHvGFOnrib5723Cm9wwsYb6CKldEr6S1ZPzqK4bYbX4WznekZh3VwD9ZVeX8q86RAjjwOarMNjwibc8d1Bc7091N5kNslPBqcZz6GgW1Y/640?wx_fmt=jpeg)

本文旨在探讨网络安全中常见的越权场景，尤其是针对预约类小程序的常见漏洞。文章强调网络安全测试活动必须获得明确授权，并声明所有技术漏洞已修复，仅供教学交流。作者总结了预约类小程序易出现的越权问题，包括水平越权查询、删除订单以及修改个人信息等。通过具体实战案例，详细分析了如何利用JWT密钥破解、数据包拦截修改等方式进行越权操作，并揭示了漏洞产生的原因，如系统未强制校验请求参数与JWT中存储的用户ID一致性。文章旨在提升读者的安全防护意识，构建更完善的安全防护体系，有效抵御网络威胁。

网络安全漏洞越权攻击JWT安全小程序安全安全测试安全防护

---

### 0x2 [一次简单的H5加密绕过](https://mp.weixin.qq.com/s?__biz=MzkxNjMwNDUxNg==&mid=2247490371&idx=1&sn=cd8ca6e2b9019528a7b0ab43639274c4&scene=21#wechat_redirect)

> 进击的HACK 2026-08-05 20:14:22

![](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVnbzdPC81uphr9edHOxBlU3Yp94COR5WOynQxp2zZueLxsW2BV0DQibvRicEp37C26VfjRSoq0ibQgibzYiaRtRwWXibGOdyuk65hmjI/640?wx_fmt=jpeg)

本文讲述了一次在APP测试中发现的H5页面加密绕过过程。测试中发现，通过修改请求头中的自定义字段“Source”可以触发服务端应用层加密的绕过。当“Source”的值为“H5”时，接口的请求体和响应体会经过加密处理。通过将“Source”修改为系统无法识别的值，服务端返回的数据由密文变为明文。文章详细介绍了如何通过前端开发者工具定位加密逻辑，并使用Local Overrides、本地代理替换JavaScript响应或Burp Suite的Match and Replace功能来修改请求，使得前端直接发送和接收明文数据。此外，还分析了服务端可能根据“Source”字段选择不同的处理流程，以及开发人员为了兼容旧系统或测试环境保留的明文处理分支。

加密绕过H5安全客户端标识应用层加密Burp Suite安全测试前端安全后端安全

---

### 0x3 [天积安全靶场攻略｜文件上传漏洞-多文件绕过篇](https://mp.weixin.qq.com/s?__biz=MzcwNjIxNTMxMQ==&mid=2247483933&idx=1&sn=39d9259939fdbfab5876e5eff290b27c&scene=21#wechat_redirect)

> 天积安全 2026-08-05 19:30:00

![](https://mmbiz.qpic.cn/mmbiz_jpg/pfqDMym8lIICkNr4D3d2O1bKtmicpafJwgL6XMRXaiaTZlvWOibWBqlcmgFCKTz3FjdPtxKZiaLRhe7e0fAZ6s221XoHzOZRgkr2nayZUScaviag/640?wx_fmt=jpeg)

一个文件传不上去？换个思路试试，本篇一起看看多文件绕过玩法

---

### 0x4 [web选手入门pwn(38)——catchme(House of Storm)](https://mp.weixin.qq.com/s?__biz=MzUzNDMyNjI3Mg==&mid=2247488418&idx=1&sn=0ed61e247077d1876b13f57207a174aa&scene=21#wechat_redirect)

> 珂技知识分享 2026-08-05 17:47:05

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Be2IPichjh3MpOIJHHdxQayiaUfqxsc8jTicFXkhYZeZz44QtltybSLssh4mcfbHFjNrW7sqqlcZW8mF9kfianQfMCmHvkjz6gVFTdxSVYnIQHE/640?wx_fmt=jpeg)

本文详细分析了名为 'catchme' 的网络安全题目，这是一个基于 House of Storm 攻击技巧的 pwn 题目。文章首先介绍了题目的环境，包括使用的 libc 版本和相关的调试环境。接着，作者分析了题目中的漏洞，包括未清零的指针导致的 Use-After-Free (UAF) 漏洞，以及 token 泄露堆头信息。文章详细描述了如何通过泄露 libc 地址和利用 unsorted bin attack 和 large bin attack 来进行攻击。特别强调了 House of Storm 攻击技术的应用，包括如何利用 large bin attack 在 free\_hook 上方写入特定大小的数据，以及如何利用 unsorted bin attack 来分配假堆，最终达到控制 free\_hook 的目的。文章还提供了实际的利用代码，包括添加、释放、编辑和删除 chunk 的函数，以及最终的 exploit 代码。

网络安全漏洞利用缓冲区溢出ROP（Return-Oriented Programming）堆溢出tcache attackunsorted bin attacklarge bin attackHouse of Storm逆向工程C语言编程

---

### 0x5 [信息安全漏洞周报（2026年第31期）](https://mp.weixin.qq.com/s?__biz=MzAxODY1OTM5OQ==&mid=2651465293&idx=1&sn=6e8c9f8e8e2600ccb5693f88e4fdcc8d&scene=21#wechat_redirect)

> CNNVD安全动态 2026-08-05 16:49:48

![](https://mmbiz.qpic.cn/mmbiz_jpg/uOZw5Efn8esamKiaNK2KVhq93f1Qpib0SJibiauNFzrhq2DCiaVKWickTlHEPJ5uPdkNY5lPwOhJ6w0AYEt602oIS94wCuMicXicbYuuuRvDwZue8kE/640?wx_fmt=jpeg)

根据国家信息安全漏洞库（CNNVD）统计，本周（2026年7月27日至2026年8月2日）安全漏洞情况如下

---

### 0x6 [红队护网钓鱼新姿势：ClickFix 钓鱼攻防技术深度解析](https://mp.weixin.qq.com/s?__biz=Mzk0NDc0NjkzMQ==&mid=2247484858&idx=1&sn=217aa5527e8df994d0991f8940786932&scene=21#wechat_redirect)

> 倍果科技 2026-08-05 16:11:57

![](https://mmbiz.qpic.cn/mmbiz_jpg/icS1YZWPXEXia0QZGib1bpZwVSfCiaTefV8yhwHcgr4ibsqKkrkLGSpiaznIFsn3CiceAz9NBiaTz0CnzN0FRBT3EtpJP3U8Oez9kbbeDcJgagyphNo/640?wx_fmt=jpeg)

ClickFix（Emmenhtal）是一种新型钓鱼攻击技术，它通过伪造验证页面，诱导用户执行恶意命令来入侵系统，而不需要用户下载任何文件或点击可疑链接。攻击流程包括：社会工程学铺垫、伪造验证界面（通常包含reCAPTCHA和Cloudflare标识）、剪贴板劫持（通过点击复选框将恶意命令复制到剪贴板）、诱导执行（用户按照提示运行剪贴板中的命令）、Payload投放（下载并执行恶意脚本）。这种攻击有效的原因在于它绕过了传统防御措施，利用了用户对验证流程的信任，且操作简单。文章通过真实案例分析了该攻击的技术细节，并提出了针对普通用户和技术人员的防御建议，包括提高安全意识、部署安全设备、监控异常行为等。此外，文章还讨论了攻击的变种形式，如使用HTA文件、LOLBins利用、混淆命令和Chrome插件投毒等，最后提出了企业级防御体系建设的建议。

钓鱼攻击剪贴板劫持社会工程学PowerShell防御策略红队演练蓝队防御恶意软件攻击链路reCAPTCHA

---

### 0x7 [Windows ProfSvc 漏洞](https://mp.weixin.qq.com/s?__biz=Mzk0MDczMzYxNw==&mid=2247485889&idx=1&sn=face01f650a42f044980b6325667e1e0&scene=21#wechat_redirect)

> 安全天书 2026-08-05 14:20:30

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/EYGYnyEdzQXuA2IIM2orF5RzvwLibHHwmMcjkWJrs5mGxBXJy5gh56K7Aqmb2pJA0taKavZLTmHiaNshn8ckSHSNYRkaFia0EPSPtEWHPXaOlQ/640?wx_fmt=jpeg)

本文讨论了Windows系统中的ProfSvc漏洞，该漏洞允许攻击者通过特定的PoC（Proof of Concept）利用另一个标准用户凭证和一个管理员账户的用户名来执行攻击。成功的攻击会将目标用户的蜂群挂载到当前用户类的根节点。文章中提到的PoC被简化以防止公共利用，但原始PoC不需要额外的用户凭证，并适用于任何蜂巢。文章强调，这些技术和工具仅用于安全测试和防御研究，禁止用于非法入侵或攻击他人系统。此外，文章还提到了一个专注于渗透测试、红蓝对抗、钓鱼手法思路、武器化等领域的圈子，并提供了一系列红队工具和技术的更新。文章还包含了多个免杀工具和对抗技术的介绍，以及相关的攻击和防御策略。

操作系统漏洞代码执行漏洞提权漏洞安全测试红队工具防御研究GitHub安全社区

---

### 0x8 [MacOS 近期两个高危漏洞：本地提权（DSH LPE）与屏幕共享预认证RCE](https://mp.weixin.qq.com/s?__biz=MzkwMzMwODg2Mw==&mid=2247517709&idx=1&sn=7cf8145b9efeb8b9e3c0d580f2d775ad&scene=21#wechat_redirect)

> 李白你好 2026-08-05 12:00:00

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ft6csZH0gNUp2IbKOKkDzMkogZonr0CX21qsgdDcib1X2iaj99Mm6fStAc4gXkN1OnVzt5PpRXia1sTeOvhqelP7ra5G8ofylHANhibErhOQNz8/640?wx_fmt=jpeg)

近期，macOS系统（尤其是Tahoe系列 ≤26.5版本）被发现存在两个高危漏洞。第一个漏洞是DesktopServicesHelper（DSH）本地提权（LPE），通过组合逻辑漏洞，普通用户可以在SIP开启的环境下直接获得root权限。第二个漏洞是屏幕共享（screensharingd）预认证Root文件读写，攻击者可以利用该漏洞以root权限进行任意文件读写。这两个漏洞均已在macOS 26.6版本中修复。文章详细分析了这两个漏洞的原理、影响范围、修复情况以及防护建议，提醒用户及时升级系统并关闭不必要的功能以增强安全性。

操作系统安全漏洞分析本地提权远程代码执行安全漏洞Apple安全安全更新安全社区安全防护

---

### 0x9 [应急响应靶机训练-Linux1(题解)](https://mp.weixin.qq.com/s?__biz=MzY5NTM4NjYwNg==&mid=2247483915&idx=1&sn=37d0495e3693250e806b57a2850cac47&scene=21#wechat_redirect)

> 淋烟雨漫江南 2026-08-05 11:28:39

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qNmib4Mp3vXZuPeEXKibpmzk9v9B05NJEDYrxiaQb01fE8kGTtzU2X6KrNw0uaibIgUqZsfTicMwRPvQTD8xbcuvN1uGZYaZDXiawYI0uZdsb9e5g/640?wx_fmt=jpeg)

---

### 0xa [验证码没输给假网站，账号仍可能被接管：设备码钓鱼正在改写反诈常识](https://mp.weixin.qq.com/s?__biz=MzI2ODU2MjM0OA==&mid=2247493011&idx=1&sn=3e754f3b1a60eb21d8d1e72cf76dd09b&scene=21#wechat_redirect)

> 字节脉搏实验室 2026-08-05 11:14:39

![](https://mmbiz.qpic.cn/mmbiz_jpg/nOo5YmK1PHwpoFau3IFV8FKdhlocaCufJlgKGzt7wPcR1ATVia3gfpnIh8glTcad7Y5xqG1hic8DA3RqibljQyPmlpCd4HvV4GIuZQYAiav0yoA/640?wx_fmt=jpeg)

用户看到的可能是微软真正的登录页，地址栏也没有明显异常；危险藏在登录前的那串短代码，以及“请帮我完成设备验证”这句看似合理的话里。

---

### 0xb [紧急安全预警｜Veeam ONE 爆未授权远程代码执行漏洞(CVE-2026-64633，CVSS 10.0)](https://mp.weixin.qq.com/s?__biz=Mzk2OTAzNjI0OQ==&mid=2247486579&idx=1&sn=58b44fe3ff56de778f8c379895716b7f&scene=21#wechat_redirect)

> 杂杂咱谈 2026-08-05 11:09:56

![](https://mmbiz.qpic.cn/mmbiz_jpg/xoBWaEOhvRHCQSicyFRKv0tiaEkUBIVUWPYPwtHffZVqTkGr2wexrnx0zeeoOcQ2iar9BJEuF0LkUxJw5QFZuUQlPuSKJSnpJKFFy2eAOep7Nw/640?wx_fmt=jpeg)

Veeam ONE 爆未授权远程代码执行漏洞(CVE-2026-64633，CVSS 10.0)。

---

### 0xc [哈希比较绕过](https://mp.weixin.qq.com/s?__biz=MzkyOTUxMzk2NQ==&mid=2247486425&idx=1&sn=92ffaa932d876c85a7ede44074f97150&scene=21#wechat_redirect)

> 安全君呀 2026-08-05 10:47:28

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/SV67dJYwaXNAVBUxdPChPJerSrgDHey6WBtqIt1vKDFpHf7Rq7jm6AatkhhTtrKibr7vzZgReAZ6at0AzY0tqiaOVeicMFWYzibu8xWO2sZDVrc/640?wx_fmt=jpeg)

本文详细介绍了PHP中的哈希比较绕过漏洞，即使用松散比较运算符`==`比较字符串哈希值时，如果哈希结果以`0e`开头并跟随纯数字，PHP会将其解释为科学计数法，导致比较结果为`true`。这种现象被称为PHP类型混淆漏洞（Type Juggling / Magic Hash）。文章通过实例分析了漏洞的产生原因、典型碰撞字符串以及MD5碰撞示例，并给出了相应的修复方法，如使用严格比较`===`、`hash\_equals()`函数、密码哈希（`password\_hash()` + `password\_verify()`）等。此外，文章还提到了其他哈希算法可能存在的类似问题，并提出了安全建议，如始终使用`===`而非`==`比较哈希值、使用`hash\_equals()`进行敏感数据比较等。

PHP安全漏洞哈希函数攻击类型混淆漏洞安全编码实践代码审计MD5碰撞哈希算法比较

---

### 0xd [ClamAV 1.5.x 三个零日漏洞](https://mp.weixin.qq.com/s?__biz=MzAxMjE3ODU3MQ==&mid=2650620837&idx=4&sn=c5132caa5313c8d410bcaab6beab3246&scene=21#wechat_redirect)

> 黑白之道 2026-08-05 08:31:00

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NkrQVyQFpmnhI8V47NHibKWD9gPDGS812SCL0GlUWN3o5LkvibApGtA4MTXmiaHoxOxZd75OiaqI4uJLlpJTdnhMd3qeMy...