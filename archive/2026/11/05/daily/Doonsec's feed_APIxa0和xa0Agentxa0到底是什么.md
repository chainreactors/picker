---
title: APIxa0和xa0Agentxa0到底是什么
url: https://mp.weixin.qq.com/s/pHR4a4Shi9mY5SFZUVpl7A
source: Doonsec's feed
date: 2026-11-05
fetch_date: 2026-11-06T08:39:37.992705
---

# APIxa0和xa0Agentxa0到底是什么

# API 和 Agent 到底是什么

原创

小阳的赛博日记
小阳的赛博日记

小阳的赛博日记

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

现在还有很多人分不清API和Agent是什么，所以我选择出一篇来大致描述一下。

大致来说就两句话，API是模型的钥匙，Agent是模型在你电脑里干活的桥梁。

这篇本来是讲给一个同学听的。

他问我，为什么别人能让 AI 自动干活，他自己就只能一句一句问。同一个软件，差别在哪。

我讲了二十分钟，讲完自己都觉得讲得稀烂。回来重新捋了一遍，就是下面这些。

**先看一组数**

中青校媒今年七月做过一个调查，一千多份问卷，98.55% 的受访学生说自己在学习里用过 AI。

用得最多的是写作业，65.41%。第二是整理笔记、拆知识点，62.02%。再往下查文献搭论文框架，50.68%。备考 45.16%，做 PPT 想方案 31.88%。

这些数字没多大意思，谁都知道现在人人都用。

有意思的是同一份调查里另一组数。问的是"你用到什么程度"。

25.48% 说只把 AI 当思路参考，正文自己写；36.43% 是让它整理素材，主体自己创作；26.74% 让它出初稿，然后自己大改；9.59% 小改一下直接用；1.74% 基本不改，直接交。这五档排下来，我盯着最后那个 1.74% 看了会儿，一万人里一百七十四个，交上去的东西自己大概都没通读一遍。

而最前面那 25.48% 反而是最稳的一批。

这两拨人用的可能是同一个 DeepSeek，同一个网页。差别不在谁聪明，在于把 AI 塞进了流程的哪一环。

往下拆，其实就几个词。

**API 到底是什么**

先说模型。

DeepSeek、通义、Claude、GPT，这些都是模型。你可以把它当成一个函数，进去一段文字，出来一段文字，中间是一堆参数在算概率。

它没有眼睛也没有耳朵。不知道今天几号，不知道郑州下没下雨，你电脑里的文件它看不见。你问它现在几点，它要么根据训练数据猜，要么直接说不知道。

网页版、APP、小程序，这些是厂商围着模型做的壳。输入框、历史记录、联网搜索、上传文件、会员、敏感词过滤，一层层套上去。

同一个模型能做成完全不同的产品。你在 A 里问不出来的东西，换个产品可能就有答案。这跟模型没关系，产品给你开了多少权限，你就能问出多少东西。

然后是 API。

全称 Application Programming Interface，直译"应用程序编程接口"。这个译名基本等于没翻。

它真正的意思只有一句：**给程序用的门。**

![](https://mmbiz.qpic.cn/mmbiz_png/hU0Xy2EUic30r531vfwUCzjtHJdzjCib0HNWKRI4KIpEoX3H9shiaVmRoPJeoL3HuKEOsnibrWZkXibUEQF6u3ibUrrgvUpcQKgZyEiarqFunwdFIk/640?wx_fmt=png&from=appmsg)

 我一般拿食堂打比方。网页版是你排队打饭，阿姨给你盛一勺，你端着走。API 是后厨的送货通道，不排队，直接把整桶拉走。

关键是这个区别：打饭窗口是给人设计的，一次一份，饭点开。送货通道是给程序设计的，一次一车，半夜三点也能来，拉完直接进你仓库。

所以 API 跟高不高级没关系。它唯一的特点，是能被别的东西调用。

**一次调用长什么样**

要准备三样：往哪发、你是谁、要它干什么。

![](https://mmbiz.qpic.cn/mmbiz_png/hU0Xy2EUic3299T6RibJwFwwvzrqII2n44BWgARBKicYswjb26xbD4r9dtkb6niaotib0uwicqAv3OicAeIPUFmbLsW9woBtSfhAKCdTRQoWXgic2tc/640?wx_fmt=png&from=appmsg)

命令行里敲出来是这样：

curl https://api.deepseek.com/chat/completions \

  -H "Content-Type: application/json" \

  -H "Authorization: Bearer sk-你的key" \

  -d '{

    "model": "deepseek-chat",

    "messages": [{"role": "user", "content": "你好"}]

  }'

Authorization 那行是钥匙，messages 是你要说的话，model 选哪个脑子。

返回的也是一坨数据，里面有个 content，那就是回答。

就这么个东西，简陋得很。也正因为简陋，哪都能塞。

**它其实不记事**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hU0Xy2EUic32kshWib5MJSfQTDxtT5KO3xy3mXiaUnicuP6zRYoabL6Zhs2miaLu0ykWwdq9fJVCAXiaowOIYJsM8vYApMT8hog7KwmIrKn5wrsI4/640?wx_fmt=png&from=appmsg)

模型是**无状态**的。

你这次调用跟上一次之间，它什么都不记得。你说"我叫小明"，下一句问"我叫什么"，它答不上来。除非你把"我叫小明"再发一遍。

那网页版为什么记得住。

因为产品帮你在后台把前几十轮打包成一个数组，整包重发。你感觉它在记，其实是每次都在重放。

这个事解释了不少怪现象。

比如聊久了它像变笨。历史越堆越长，你开头说的重点被淹到后面去了。

比如同一个问题问几次，答案越来越绕。它在拿一大堆无关的旧内容算你当前这一句。

再比如有时候它突然忘了你最早的要求。上下文窗口满了，前面的被挤出去。上下文窗口就是它一次最多能看多少 token，现在主流模型几十万，看着多，你真往里塞几本书，很快就满。至于这个数具体怎么切出来的，我也没细究，反正它是按这个收钱的。

对，计费就是按 token，不按字数。一个汉字大概一到两个 token，英文一个词一个多。发进去的算输入，吐出来的算输出，输出通常贵好几倍。所以有人觉着"我就问了几句怎么花了这么多"，钱花就花在每次重发的那堆历史上。这也是为什么网页版聊得越久越费，它在替你一遍遍重复前文。

顺便说 key。这东西等于银行卡密码，不能写在前端代码里，打开源码就看见；不能传到 GitHub，一推上去几分钟被扫走；更不能截图发群里问"为啥报错"。我见过有人这么干，十分钟额度清空。

**能批量了，可还是手动挡**

到这一步，很多人觉得自己已经会了。

其实只是把对话框从网页搬进了代码。

好处是你终于能批量。写个循环，两百条问卷的开放题一条条丢进去，让它归类打标签，结果存成表。网页版干不了这个，手点两百次会死。

但它还是你问一句它答一句。不会自己决定下一步，不会干到一半发现不对再改，不会去翻资料，不会动你的文件。

要让它真干活，缺三样。

**模型没有手**

第一样是能动手。

机制叫函数调用，Function Calling 或者 Tool Use，两个名字指一回事。

这里有个特别常见的误解得说清楚：**模型不执行任何代码，它没有手。**

它怎么干活呢。你先告诉它，我这有几个工具，一个 search\_web 查关键词，一个 read\_file 读文件、参数是路径，一个 write\_file 写文件。然后它输出一段结构化的东西，意思是"我想调 read\_file，路径是 a.txt"。

真正去读文件的，是你的程序。模型只是提了个请求。

所以决定权一直在你手里。你给它哪几个工具，哪些操作必须先问你，都是你定的。

很多人以为 Agent 是模型自己在你电脑上点点点。不是。是它说"我想点"，你的程序替它点。中间那道关卡，就是你的刹车。

（工具怎么接上去现在有标准了，叫 MCP。2024 年底开源，2025 年底交给了 Linux 基金会下面的 Agentic AI Foundation。名字不用记，知道现在接工具不用一个个手写就行。）

第二样是循环。干完一步看结果，按结果决定下一步。

第三样是有目标。答完一句不算完，把事办成才算完。

**Agent 就是转圈**

![](https://mmbiz.qpic.cn/mmbiz_png/hU0Xy2EUic30PbtPsRyNFD9LRnnyliafm8bwfuHo3QTKMlAIibuM13IBwyPfYAQTEMIoXCYXoGvVyW5CX4WobrV6lPRdVLGaTHpymmfqgJSGOs/640?wx_fmt=png&from=appmsg)

想，调工具，程序执行，看结果，再想。

转，一直转到它说干完了。

就这么回事。那些花里胡哨的 Agent 产品，都是在这个圈外面加东西。记忆怎么存，工具怎么管，失败了怎么重试。还有什么时候该叫人来，花到多少钱停。

转多少圈不用你管，就是大家说的"自主性"。转多了会出事。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hU0Xy2EUic32Z3lGB3tBrErQAdl8RU1Ve7qN4LeNQGEiasF2mVd919ydXKTEiaNu20cicxe1jXugU2NjEW62SDxhC4kadUxb1894BjE3zgZArkE/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hU0Xy2EUic309LfD9glHpzuCKghBUR9uxnP62QJocSw1p94908xL8HiaFRD6kemfWrqB4prY544oyryPzQEIzo8v8Ve6p0e7HB1LGkoYDOJA0/0?wx_fmt=png)

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