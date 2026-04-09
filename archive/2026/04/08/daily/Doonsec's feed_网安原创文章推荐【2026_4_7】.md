---
title: 网安原创文章推荐【2026/4/7】
url: https://mp.weixin.qq.com/s/69C7wjTHWwKbn26apDNBag
source: Doonsec's feed
date: 2026-04-08
fetch_date: 2026-04-09T04:27:57.995626
---

# 网安原创文章推荐【2026/4/7】

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/CZMNsicRfJADJ3h4jXtiaVKPzkxib0cKayXIYzEQ33u1YmsMicnwLsv93sK2RGb5OGJwCmJX5HrTOibatHM5ZMVCuznibHFwy1yG3UxhM4lyqHyHw/0?wx_fmt=jpeg)

# 网安原创文章推荐【2026/4/7】

AJay13
AJay13

洞见网安

![]()

在小说阅读器中沉浸阅读

# 2026-04-07 微信公众号精选安全技术文章总览

> 洞见网安 2026-04-07

---

### 0x1 [从原理到实战：COM劫持持久化机制全解析](https://mp.weixin.qq.com/s?__biz=MzkxMDYwODk2NQ==&mid=2247485128&idx=1&sn=b3b53ef682e387943e9b0c597fd1f7d6&scene=21#wechat_redirect "从原理到实战：COM劫持持久化机制全解析")

> 大仙安全说 2026-04-07 14:16:32

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/H6RmIowwbs4I1p9oKgYtZAjNosib0B1dluUOpYoI3BvHdWe4U7YBW4yZeicQnfXS2UGDaXaeWurIaecp7aZCfK0yulS0sImg8T2tZA1Rk1o7c/640?wx_fmt=jpeg)

本文深入解析了COM劫持技术及其持久化机制。首先介绍了COM组件机制，包括CLSID的注册表结构，以及Windows查找COM对象的顺序。随后，详细阐述了COM劫持的类型，如现有CLSID劫持、孤儿CLSID劫持、TreatAs重定向、TypeLib劫持等。文章通过实战样本分析，展示了如何利用Procmon捕获注册表修改和文件创建行为。接着，通过注册表和文件取证，分析了恶意软件的持久化方式。最后，通过沙箱分析验证，确认了恶意软件属于COMpfun家族，这是一种以COM劫持技术著称的远程访问木马。文章总结了COM劫持技术的隐蔽性和稳定性，以及通过注册表监控、行为分析和应用控制来检测和防御此类威胁的方法。

网络安全攻击技术

持久化攻击

恶意软件分析

注册表分析

沙箱测试

Windows安全

---

### 0x2 [Clash Verge开启局域网代理共享，让全设备都能使用](https://mp.weixin.qq.com/s?__biz=MzkyNzYzNTQ2Nw==&mid=2247486262&idx=1&sn=2345b3f8a8e544a2a1ff170baf23ca8c&scene=21#wechat_redirect "Clash Verge开启局域网代理共享，让全设备都能使用")

> W不懂安全 2026-04-07 12:57:20

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/LtibzcRx8GjVxGU8OzbziaUFic5DPgFkOn6OMJlGgbWfxgnBp5G1gEC8tiazyftSWOLehJnl5ZkgsWF0nH5BfOz7kwglAU63MoAdXkDSTlJluAc/640?wx_fmt=jpeg)

本文介绍了一种利用Clash Verge软件实现局域网内设备共享代理的方法。通过将电脑设置为局域网内的代理服务器，其他设备如手机、平板或另一台电脑可以共享电脑的代理设置，无需逐一配置。文章详细说明了如何开启局域网共享开关、确认端口、找到电脑的IP地址，以及如何在不同的设备上设置代理。此外，文章还提到了解决连接问题的一些常见原因，如不在同一个局域网、IP填写错误、防火墙未放行等，并提供了相应的解决方法。

网络代理

网络安全配置

内网安全

网络共享

虚拟化安全

终端安全

---

### 0x3 [2026NCTF Writeup by Mini-Venom](https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247514249&idx=1&sn=4908872cb3350a330c26c64283425c0e&scene=21#wechat_redirect "2026NCTF Writeup by Mini-Venom")

> ChaMd5安全团队 2026-04-07 10:30:34

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/jvwqHfehg2Pic6vJuxibDjHxiavhu8DWWVMadL0y3KWIkxZ1z8qibj9b9uzSkSib7OFo3chKaahza4hMiafTT7SsQ2j7F1wHKibkV1vNERMJwoCiczU/640?wx_fmt=jpeg)

本文分析了多个CTF比赛的题目，涵盖了Web、Reverse Engineering (RE)、Cryptography、Pwn、Miscellaneous和Contract等多个方向。Web方向的题目涉及了Blind SSTI利用和后台接口篡改，需要选手具备对Web漏洞的理解和利用能力。RE方向的题目考察了RSA加密算法的破解和WASM逆向，需要选手熟悉加密算法和逆向工程技巧。Cryptography方向的题目包括了一个非预期的RNG游戏和Pwn尝试，需要选手具备密码学和漏洞利用的能力。Pwn方向的题目涉及了一个VM解释器和ROP链构造，需要选手熟悉底层系统和漏洞利用技术。Miscellaneous方向的题目包括了一个数据清洗和ezProtocol协议分析，需要选手具备对数据分析和协议理解的能力。最后，文章还介绍了一个Quantum Vault题目，涉及了提权和密码修改，需要选手具备系统操作和漏洞利用的技能。这些题目覆盖了CTF比赛中的多个方向，对选手的综合能力提出了较高的要求。

CTF

Web安全

逆向工程

密码学

Pwn

Misc

RNG

Python编程

二进制分析

漏洞利用

---

### 0x4 [深扒最新钓鱼链：动态PDF+双打木马，巴西黑客组织攻击手法大揭秘](https://mp.weixin.qq.com/s?__biz=Mzk1NzM4NzMyMw==&mid=2247485702&idx=1&sn=a1ac8e247eec80652d276e2c58937815&scene=21#wechat_redirect "深扒最新钓鱼链：动态PDF+双打木马，巴西黑客组织攻击手法大揭秘")

> 安全圈动向 2026-04-07 08:03:39

![](https://mmbiz.qpic.cn/mmbiz_jpg/bHeteOibsicdhc1rrla8c6R7ibHwiamCf2ZNMToS1TATYxK4shExbrZjHkU9rdPepVQEYIMnO4ibXjh7esnp3lSDB9hMicXJSdCicvbibVVG8EhYfKU/640?wx_fmt=jpeg)

本文深入解析了一起由巴西黑客组织Augmented Marauder或Water Saci发起的钓鱼攻击事件。攻击者利用动态PDF和双打木马技术，通过钓鱼邮件传播Casbaneiro（Metamorfo）银行木马。文章详细拆解了攻击链的流程，包括使用带密码的PDF附件作为诱饵、VBS脚本的环境检测与AutoIt加载器的使用，以及Horabot引擎如何通过动态生成带有随机密码的PDF文件进行横向传播。文章还揭示了攻击者如何利用合法受害者账号发送邮件，绕过邮件防伪造协议。此外，文章还讨论了攻击者的多渠道攻击手段，如WhatsApp Web自动化传播和ClickFix社工技术。最后，文章提出了针对这种高级攻击的防御建议，强调了行为监控、脚本与加载器拦截以及零信任理念的重要性。

钓鱼攻击

银行木马

网络安全

逆向分析

恶意软件

攻击手法

安全防御

技术对抗

企业安全

---

### 0x5 [RAG从元数据Key到RCE：CVE-2026-22738 深度解析Spring AI向量存储中的SpEL表达式注入与逃逸](https://mp.weixin.qq.com/s?__biz=Mzk0NTU5Mjg0Ng==&mid=2247492758&idx=1&sn=ed00cf04b239839ed1d0553fa0674579&scene=21#wechat_redirect "RAG从元数据Key到RCE：CVE-2026-22738 深度解析Spring AI向量存储中的SpEL表达式注入与逃逸")

> 自在安全 2026-04-07 07:02:21

![](https://mmbiz.qpic.cn/mmbiz_jpg/5micBBibMraLk0jBRAqaS7UFWU0pyh7CoTLT0mjloxVQk2EOEB7fTk3jiboice675cnZsKMpTIXTkDlKbZicLnAJDR5kib7ibbRPcSFWwicCESnSiaNE/640?wx_fmt=jpeg)

本文详细分析了一个存在于Spring AI框架中的高危SpEL表达式注入漏洞（CVE-2026-22738）。该漏洞位于SimpleVectorStore的向量检索过滤逻辑中，由于将用户提供的过滤器表达式直接拼接至SpEL模板并使用StandardEvaluationContext解析，导致攻击者可构造恶意payload实现远程代码执行（RCE）。文章首先介绍了漏洞的触发点在SimpleVectorStore#doFilterPredicate函数，随后通过分析similaritySearch函数的使用场景，揭示了漏洞的利用路径。针对FilterExpressionTextParser的过滤机制，文章详细阐述了如何通过在Key中构造恶意SpEL表达式来绕过校验，并提供了具体的payload构造方法。最后，文章提到了官方的修复方式是移除SpEL解析，改用自定义AST遍历器直接求值，以彻底消除漏洞隐患。

漏洞分析

SpEL注入

RCE

Spring AI

Java安全

向量数据库

代码注入

安全公告

绕过机制

修复方案

---

> 本站文章为人工采集，目的是为了方便更好的提供免费聚合服务，如有侵权请告知。具体请在留言告知，我们将清除对此公众号的监控，并清空相关文章。所有内容，均摘自于互联网，不得以任何方式将其用于商业目的。由于传播，利用此文所提供的信息而造成的任何直接或间接的后果和损失，均由使用者本人负责，本站以及文章作者不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/vML07fExwAdpcFbk9icEKB6QPwpicFcfu6QHCmkibP2yszUiaajx3CdP1cmNyq7ZGL40Q92d5QRpsY9yBTcgGlLNcg/0?wx_fmt=png)

洞见网安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/vML07fExwAdpcFbk9icEKB6QPwpicFcfu6QHCmkibP2yszUiaajx3CdP1cmNyq7ZGL40Q92d5QRpsY9yBTcgGlLNcg/0?wx_fmt=png)

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