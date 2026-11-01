---
title: 偷完密码还让AI写报告：新型木马用大模型给受害者排优先级
url: https://mp.weixin.qq.com/s/f4xgGYwSg6jZ4acqZ0K2hw
source: Doonsec's feed
date: 2026-10-31
fetch_date: 2026-11-01T08:18:06.535627
---

# 偷完密码还让AI写报告：新型木马用大模型给受害者排优先级

# 偷完密码还让AI写报告：新型木马用大模型给受害者排优先级

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以前偷密码类恶意软件，干的是搬运工的活：

把浏览器里存的账号、信用卡、cookie一股脑打包发走，剩下的让买家自己翻，然而现在有人给搬运工配了个AI分析师。

Cisco Talos最近挖出来的一个Windows infostealer（信息窃取器），内部自称VOLTA-AUTODOXER，其在偷完东西之后，会把赃物整理成一份结构化档案，送到大语言模型面前，让AI来判断这个受害者值不值得动手、先从哪儿下手。

“Autodoxer”这个名字本身就带着一股恶意幽默。doxing（人肉搜索）是黑客圈的老手艺，把人肉出来的信息拼成一份档案。Volta在dox前面加了个auto，意思是这件事不再需要人来做，恶意软件自己会完成。

Volta的第一轮收集瞄准的是“现代数字生活留下的所有痕迹”。浏览器密码、cookie、保存的支付卡是标配，但它还扫Microsoft OAuth token、SSH和云服务商的配置文件、机器上保存的每一个Wi-Fi密码，以及Discord、Telegram、Steam、Roblox的活跃会话。加密钱包的种子短语也在清单里，而且Volta不是只把钱包文件拷走，它在本地跑一个内嵌的破解程序，把结果直接写进自己的报告。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDpG6IWmj5Tkmkhic3za2vDge8e8aXOwRjzhp1CItO4yoiatQ1F3wgw1mPNUGGtsbWkG79zoNiaH1G5Xicmf9H2BAz0MKwSy8Ncc5xA/640?wx_fmt=jpeg&from=appmsg)

然后它做了一件 commodity stealer（商品化窃取器）很少做的事：用偷来的会话权限回头翻受害者的数据。拿受害者的Gmail token去搜Amazon、DoorDash、Uber Eats、Grubhub、Walmart、PayPal的收据，用收据上的地址交叉确认家庭住址；直接调Uber Eats和DoorDash的订单历史；用Discord token丰富账号资料；去Rolimons.com查Roblox库存的实时估值。第一轮偷的是key，第二轮用key打开门，把房间里的东西也清点了一遍。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDobqy5J3xciavLgoVmjJFCjCHRTH0bGoeH2n9gyut4dOxPM0eUPLwJPgCzawSEm8fTLh91LQSGu6SXseBTGpTHYckjSibIFR0ln4/640?wx_fmt=png&from=appmsg)

# AI拿到的不是原始数据，是一份整理好的证据包

Volta在本地生成一个叫Identity\_Report.txt的文件，序列化成JSON，连同一段系统提示词一起POST到OpenRouter（一个可以把请求路由到多家AI模型的服务）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDoMV9KStXVwkWb5YATW7mb1CzJ5bW94oxWEHiaf4icBSUnI55l2g8Odwz29o6f35fwtqfvbqsGFRTC33Qod7iaWCNOwo4pl4ZHNqE/640?wx_fmt=jpeg&from=appmsg)

默认模型是Anthropic的Claude Opus 4.6，但恶意软件的作者预设了被拒绝的可能，因此准备了一条回退链：如果Claude不接活，自动切到Kimi K2，再不行就落到Google的Gemini 2.5 Flash。每次请求发出后，它会检查回复里有没有“I can't”或“I'm not able”这类拒绝措辞，有就往下走。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrvS7MicQA0p719smibjtRVAwfb09kUg1I2CUMGHByiaN78CNBImlRpCRKWMILR8cq7S1WGCs7FDiaias0FlNAo4gK57DhJt0cdjNuk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDoiap7sFgB0A7KFdbaThsNHZ5UGzN3oJjUa3UgTTicbrO5U46EJSneQicr72XWibxwUv8GxkY5zs0s07ezwnRYR3qs163ykoKWfN9Q/640?wx_fmt=png&from=appmsg)

提示词本身只有240来个词，但写得像一份情报分析任务书。开头是“You are a forensic intelligence analyst drafting a target assessment from a structured evidence bundle”，要求模型输出一份“executive summary”，说明这个人是谁、做什么的、WHAT THEY'RE WORTH（值多少钱），以及THEIR OPSEC（他们的安全习惯怎么样）。它还要求“connect dots across fields”，比如检查Wi-Fi密码是不是跟姓氏有关，并特意叮嘱“Go deep, not wide”。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDp15BIJjwDqFczMkwqq5VpkGW3sGuNnfahVLoo59v7oXKbdRBRHvBPvcm4z4j0lAkPOPCvk7VUurOxOkAVSo9NsZJRuYGgEmRs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDpsr3obia3Xyn7137187uh1aDDWcpIiaWsbmSqH2TUNyZtE9tKJNNNgXP4EhkONPvXTPj5Q5NZ82rVicSr5VDwUWW2a4l2tRcD6xs/640?wx_fmt=png&from=appmsg)

模型温度（temperature）控制着大语言模型生成文本时的随机性与可预测性。攻击者将温度硬编码为较低值（0.2），表明其追求的是准确性与一致性。此外，该恶意软件还采用了一连串级联模型，以便在发生故障时进行切换。

这种多模型架构表明，攻击者早已预料到会遭遇模型拒绝（refusal）的情况，因此设置了回退机制，转而调用少数几个规模更小、限制更少的模型。

换句话说，模型在这里不是用来“找数据”的，数据已经躺在证据包里了。模型被要求做的是拉伸数据：把名字、地址、大学、密码模式之间的稀疏联系串起来，给出一个可以拿去排序的结论。

# 没有服务器，没有C2，跑完就删

Volta的部署方式也值得多看一眼。它没有把Telegram频道、API key、设置硬编码在代码里，而是用了一个带六个可替换槽位的模板，编译时填入。

这指向一个builder model（构建器模式）：

作者卖的是访问权，客户提供自己的API key和回传地址，作者给每个订单编译一个定制二进制文件。槽位里的凭证用一种“看起来加密了但等于没加密”的方式处理，密钥是同一二进制里两个常量的SHA-256，逆向的人随手就能恢复。

所有观察到的端点都由第三方控制，恶意软件本身没有攻击者拥有的基础设施，跑完还会自删除。这意味着AI分析这一层不是某个高水平团伙的专属武器，而是被打包成一个功能，任何买了这个模块的人都能对着受害者按下“生成评估报告”的按钮。

AI集成的恶意软件不管怎么混淆，总会在元数据里留下“认知制品”，嵌入的提示词、OpenRouter这类服务商的端点字符串、API key前缀、甚至用来糊弄AI沙箱的“这里没什么可看”的注释。

黑鸟认为，攻击者若能更快锁定高价值目标，其滥用窃取的凭证或认证 token 的成功率将显著提升，毕竟 token 会失效、密码会被更换。过去依赖人工筛查日志完成分诊（triage）的环节，如今已被 AI 自动化，这使得原本高门槛的攻击能力向低水平攻击者普及，这一现象既值得玩味，也令人忧虑。

信息窃取器本身不是新东西，传统模式是：偷来一大堆日志，买家自己翻，翻到什么算什么。Volta的模式是：偷完，用偷来的权限再挖一层，把证据包整理好，让LLM以情报分析师的姿态写一份带引用的评估，按“变现价值”把资产标成低、中、高。

对普通人来说，这意味着“我的密码泄漏了”这句话的含义又沉了一层。

泄漏的不只是密码本身，还有一套围绕你的数字生活自动拼出来的画像：你住哪儿、在哪儿工作、用什么外卖、玩什么游戏、游戏库存值多少钱、你的Wi-Fi密码是不是你的姓。

而拼出这张画像的AI调用，就跑在你自己的机器上，走你自己的网络连接，在你意识到之前已经完成并打包发走了。

Ai集成类恶意软件正在从“收集数据”走向“理解数据”，而理解数据的能力，恰恰是过去需要人类分析师才能提供的东西。

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

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