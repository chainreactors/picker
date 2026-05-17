---
title: 零·重新校准[ 黑Ke逆向工程Ai自动化 ]  初始|0.篇
url: https://mp.weixin.qq.com/s/AQbOvcGYv5O3A9Knf3Ad1g
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:42:50.617223
---

# 零·重新校准[ 黑Ke逆向工程Ai自动化 ]  初始|0.篇

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icfnkibn16VejwnEkTVicFtj9ensQ6Z3FFibPKJCHsZGYxxz8Z4KNxQ9VibJ0Gq5JxCCu2elxld3YlJZdA8LM0dIZUbjevhSAt8sicDfFxoNHE8mE/0?wx_fmt=jpeg)

# 零·重新校准[ 黑Ke逆向工程Ai自动化 ] 初始|0.篇

原创

Esn Arsenal
Esn Arsenal

Esn技术社区

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

[Bl0ckdev 重新调整自己，走出困境，找到了清晰的方向，迈出了下一步。](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492976&idx=1&sn=2378a3dfad93417a942a783d5bcafcd8&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16VejX8knNib5WcNR6J1CVueUEcoBUr2NYk82LLnRbyIUov5ibsaHbqJEvC5WeF9dB0icIj1TXwktjNJicvX88Qw9bEJnalu49Dce3uiac/640?wx_fmt=png&from=appmsg)

经过短暂的“校准”,除了研究MCP的同时将会把基础逆向工程进行一次闭环完结。内容包括“如何构建软件”“如何逆向自己构建的软件”。我个人的目的在于重新“校准”以后自己的软件编写能力。

因为目前我无法用Agent完整的编写出自己想要的那种“感觉”,对软件组合不够理解,我这几天有仔细的阅读了  [C# 图解教程]， 目前在看【C++面对象程序设计教程】。做出来的东西很魔幻,bug就不要想了五百行代码的有5个漏洞。

<C# 图解教程> 我个人理解是目前来说我所接触过的覆盖“软件是如何编写的最详细的一本书”

<C++面对象程序设计教程> 这本书主要讲述了“由浅入深和编写概念”N刷的目的在这是一本具启发的书籍,同时层次很清晰。

我将会围绕着这篇文章：[以现代化Ai黑客视角初级3D游戏外挂·启蒙知识（初创）](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492171&idx=1&sn=ed9698bc0ad4ddf123319f6ce4473274&scene=21#wechat_redirect)把后续的Ai Agent扩展写细节闭环。同时将会记录成完整的细节公布在https://t[.]zsxq.com/nun60 知识库内。因为我要适配MCP本地定制,所以我需要用到这些基础并零碎的知识。#逆向工程#

我的思路和做法与大家可能有点不同,因为Ai的缘故我更喜欢不按常理,先做出来然后在研究细节,我不想先在细节上浪费经历,因为那会让我崩溃更加彻底。

整体的“校准”计划将会配合Deepseek进行完成,[#3重新校准  确定Agent-使用ClaudeCode对接DeepseekV4进行|从新梳理破解和软件逆向的每个步骤写入MCP进行自动化调用！](https://mp.weixin.qq.com/s?__biz=MzU5Njg5NzUzMw==&mid=2247492942&idx=1&sn=35b2a6ecce7b31251e3ad3954c76b6f8&scene=21#wechat_redirect)我们都可以在 #ClaudeCode 中使用Deepseek。从头到尾“掌握初级逆向工程”预计调用200人民币左右的token。其他的理解免费的就可以搞定。

“校准”整体路线：

![](https://mmbiz.qpic.cn/mmbiz_png/icfnkibn16VeiaSp7ejcj49HGKYGr8p09u3a6gd03cSlm7iboEIHr7IwUUCPG16GwfJvX11iaic6PicIHbb3NTW7Wa7088ec1icsiaLuRp2wDzVjz2ZY/640?wx_fmt=png&from=appmsg)

🟢 初级— 🟩#H6000\*  标签均可以访问

🟢.“私密群 .EsnInfoSec: Chat”话题：逆向工程— [ 零创技·新人初级入门]

🟢“重新校准”之初始-步骤：

> 这是一个很长很长的故事,如果你想与我一起深入逆向的自动化世界,那么就要先懂得逆向是如何工作的,以及逆向工作的原理。ps：原理并非是“懂”而是你自己动手系统性逆向自己写的程序。简单的说如果：如果不懂软件如何构成的人盲目逆向基本上都会花冤枉钱。我随时欢迎大家添加我的知识星球对我进行支持。快速查阅我每天的进度和进入内容。
>
> —第一部分：Ai逆向本地环境闭环
>
> —第二部分：Ai完整的闭环设置
>
> —第三部分：逆向工作流程深度解析
>
> —第四部分：总结和未来扩展包括硬件的主要问题。
>
> 起始的目的：我们都配备着一个可用的本地 LLM 逆向工程堆栈，并有信心使用自定义提示和模型扩展其设置。同时了解什么Ai和Agent适合自己。

这一步的目的在于利用Ai和Agent系统性根据自己电脑的硬件进行适配自己可以接受的“环境”,！这里的环境设定是强制闭环。

强制闭环如下：

闭环[ 1+2+3=6 ] 而并非是1+2+3=3+3的模糊概念。

————————————————————————

有疑问/预览后想要添加知识库的提前私信。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icfnkibn16Veh2W9WymHGlD1vWESe9maZHk9fmzJFg05InEc28wIS4FwibbjsjlibtKgUictqn3DU6xXqSDomFK0vpLEE1s3l2v0aaCOSMEaaU3s/640?wx_fmt=png&from=appmsg)

老粉获取H6000\*标签的途径,懂得都懂！

H6000\* 标签确定：🟢

https://discord[.]gg/KWFrnnqBQu 中身份是 🟢@ID：成员

![](https://mmbiz.qpic.cn/mmbiz_jpg/PwaXL3w2IRaDgaRQG5ujsPrXostCchunyCR5Y0VpBpPTkXATnVMxBwPRnYBKdqgPx7AB433icw5FXez1xp6Nibqg/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

Esn技术社区

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/PwaXL3w2IRbdW3dY1XLuF3qWXIEQCvzWGBaFGLibfRGHs2JDuomUTlU6FRYuHxWDaluyrOwDgzyiaxeUjMODURDw/0?wx_fmt=png)

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