---
title: SRC资产收集之微信小程序
url: https://mp.weixin.qq.com/s/_HHzqu1vi1brQAuZTDUWtw
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:53:16.689325
---

# SRC资产收集之微信小程序

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVlU1JicnGYNUqorT7c6Em8f4KR8htY3xpcCVVtaOCYwodQDHCjccTsoAWb1D68ogCFpPa6zWVzq4enJRvxOCchtNwia0QcbLrmMI/0?wx_fmt=jpeg)

# SRC资产收集之微信小程序

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 201，阅读大约需 2 分钟

## 收集小程序

**小蓝本**：https://sou.xiaolanben.com/

![59377d7c445086a62b4cf5f0aafbaf51.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnibZpegcJibVvskyzQA8sUf0HOrC0qOoXSdVsCGqhJuJibbMfFicydF9EmBia0jA58aJSFyiccNriciagXcJ7lzKib7HtEmicuUWJeEDOpg/640?from=appmsg "null")

59377d7c445086a62b4cf5f0aafbaf51.png

**微信搜索小程序**
![4a91af3ff9d491e67c666c203e641ad1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVme65ibiaR31eOibQpA24XwYzXQmAOqfMMpUibkXHJudYVR7zbYrAw02t3hU5hK87lGIVDs6rcxxl00Dbez9VUUadpu2P9XrbB059o/640?from=appmsg "null")

4a91af3ff9d491e67c666c203e641ad1.png

**从一个小程序到另一个小程序**
反编译小程序，从中提取 wx……
First
![78263b46ee24893d307c0a3c2c938fc0.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVn1ZnVfFAlwSdYxibxJ9bDUmtKib9xg46rRL4GGfGVm5gj9NlddW0DlvDBaGu0Zln9zx55tTeU6COiazzex3iaxLqp6GTxvB0HJtQY/640?from=appmsg "null")

78263b46ee24893d307c0a3c2c938fc0.png

然后用小程序跳转工具
公众号：听风安全
![cf95074c173ce252a19b25e2752ad593.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmGBicEqKk9iaibKltOvK2CZX8qlRAoxWT9Q1xmZmbrib52jJWM1OPcYOIhljDdryic82f9gq8oMvR1woAI6koUqkOEonfib6ENicdT0k/640?from=appmsg "null")

cf95074c173ce252a19b25e2752ad593.png

跳转
![91232e7cca8059d4063660685a185ae4.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkaT4ThrkvSWUKWVQUMpSezlCpLeicOGqnl8Pj8ROTz97m9Eic53QfH5fn7fdGicnzqTABoC1t6ibvfmVTkj1Kic82xyUt4amXjkhp4/640?from=appmsg "null")

91232e7cca8059d4063660685a185ae4.png

然后层层套娃，其中可能遇到第三方的小程序，排除就好了

## 工具

* • First
  https://github.com/Spade-sec/First

介绍：微信小程序安全调试工具 —— 基于 Frida + CDP 代理，支持 Windows / macOS 双平台，GUI 与 CLI 双模式
![9bdbc34cecede00e0cf72b9be8e3974b.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnicCsfYRuNdscgXwTD6qosUsG8XUAApaFZ3BrFEiboLiaHH849M5tN9z4h1R9HTh5fic76TT2e2ORUosajztgH0eWPYCD8LCnTp2Q/640?from=appmsg "null")

9bdbc34cecede00e0cf72b9be8e3974b.png

* • e0e1-wx gui
  https://github.com/eeeeeeeeee-code/e0e1-wx

介绍：一款面向 Windows 的微信小程序本地分析 GUI 工具，提供小程序包监控、自动反编译、正则匹配、代码优化、DevTools CDP、路由查看、云函数分析以及常用加密解密辅助能力。

![287a51241225fdea168d8481482142c7.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkjo768Ng9YBoj0fGdxicEM3FibZCc5cjUzveTQ5JBMLgPsMibzibWeJJVMSmnxIwEibQQeydE4rVIgXFEXGib8r8uQy4zJQQUenZ3J4/640?from=appmsg "null")

287a51241225fdea168d8481482142c7.png

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DuibU3GqmxVmRsdItbBVRKegNHicHQvAHDdZsGpLVU7touSU1AU1twHTfRjG3Vu5aUh0RnPPllfVUhs4qdWF5QYQ/640?wx_fmt=png&wxfrom=13)

声明：文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途给予盈利等目的，否则后果自行承担！

如有侵权烦请告知，我会立即删除并致歉。谢谢！

文章有疑问的，可以公众号发消息问我，或者留言。我每天都会看的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/9zYJrD2VibHmqgf4y9Bqh9nDynW5fHvgbgkSGAfRboFPuCGjVoC3qMl6wlFucsx3Y3jt4gibQgZ6LxpoozE0Tdow/640?wx_fmt=png&wxfrom=13)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/a1BOUvqnbriaKQaulUawUmcqevsicgRXaDWWcgmsbG7iaTtKE89ZwJEkPHzibEzXwcibLn8PKu1hGoicqAEIW9uQjyBw/640?wx_fmt=jpeg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

进击的HACK

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/a1BOUvqnbrhOdQiaFvupNflYqfzCq5nzdjQF1j9ib5wTPYG8g3txOmd7mu8icbHfWCHTLibYzSOMlRrlLD9EicEESzA/0?wx_fmt=png)

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