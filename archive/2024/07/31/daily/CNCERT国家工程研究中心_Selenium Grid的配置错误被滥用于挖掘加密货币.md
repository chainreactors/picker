---
title: Selenium Grid的配置错误被滥用于挖掘加密货币
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546098&idx=2&sn=99907ada4f3c4cd8918ed01877001887&chksm=fa938233cde40b25eda50bb3dc7df25c707a0ef7e14e4f5caff0e17c2a263360b53979e00971&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-07-31
fetch_date: 2025-10-06T17:44:32.757847
---

# Selenium Grid的配置错误被滥用于挖掘加密货币

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176kaxvBd6p9YKznesg0slgKz59LOxoFCLPAKKD0vTRlYX5myOr4A0m3aicwH3SoHTEeolqAkBZJQhuA/0?wx_fmt=jpeg)

# Selenium Grid的配置错误被滥用于挖掘加密货币

网络安全应急技术国家工程中心

威胁行为者正在利用Selenium Grid的配置错误来部署修改版的XMRig工具，用于挖掘Monero（门罗币）加密货币。

Selenium Grid是一个流行的开源Web应用测试框架，它允许开发者在多台机器和浏览器上自动化测试。它在云环境中使用，并且在Docker Hub上的下载量超过1亿次。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kaxvBd6p9YKznesg0slgKzgWWcw1ncV5D8EI5UWUKtRVmxcLpsMxspdiaiaHI3bCBiaibVEmPYnnib4nw/640?wx_fmt=png&from=appmsg)

Selenium测试概述

来源：Wiz

测试任务通过API交互从中央集线器分发到服务的各个节点上执行，这些节点具有不同的操作系统、浏览器和其他环境变化，以提供全面的测试结果。

云安全公司Wiz的研究人员发现，他们正在跟踪的恶意活动“SeleniumGreed”已经运行了一年多。这个活动利用了服务在默认配置中缺乏认证机制的弱点。

根据Wiz的研究，Selenium Grid默认情况下没有激活的身份验证机制。对于公开的服务，任何人都可以访问应用程序测试实例、下载文件和执行命令。

Selenium 在其文档中警告了互联网暴露实例的风险，建议那些需要远程访问的人通过设置防火墙来防止未经授权的访问。然而，这个警告不足以防止更大规模的错误配置。

Wiz提到，威胁行为者正在利用Selenium WebDriver API来更改目标实例中Chrome的默认二进制路径，使其指向Python解释器。然后，它们使用“add\_argument”方法将base64编码的Python脚本作为参数传递。当WebDriver发起启动Chrome的请求时，它会使用提供的脚本执行Python解释器。

![](https://mmbiz.qpic.cn/mmbiz_png/GoUrACT176kaxvBd6p9YKznesg0slgKzX7icXN0ImSoM00IBibvJ42qwokpY0tFMDSDlXg4LJj9EhfwVVibhhzwAA/640?wx_fmt=png&from=appmsg)

攻击中使用的漏洞利用脚本

来源：Wiz

Python脚本建立了一个反向shell，使攻击者几乎可以远程访问实例。接下来，攻击者依靠Selenium用户（seluser），可以在没有密码的情况下执行sudo命令，在被破坏的实例上放置自定义XMRig矿工，并将其设置为在后台运行。

为了逃避检测，攻击者经常使用受损的Selenium节点工作负载作为后续感染的中间命令和控制服务器（C2），以及作为采矿池代理。

Wiz公司使用FOFA搜索引擎对公开网络上暴露的网络资产进行了扫描，结果显示至少有30,000个Selenium实例目前可以通过公共网络访问到。

Wiz在报告中说：“任何缺乏适当身份验证和网络安全策略的Selenium Grid服务版本都容易受到远程命令执行的攻击。”

“根据我们的数据，本博客中描述的威胁针对的是Selenium v3.141.59，但它也可能演变为利用更高版本，其他威胁行为者可能已经这样做了，”研究人员指出。

原文来源：E安全

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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