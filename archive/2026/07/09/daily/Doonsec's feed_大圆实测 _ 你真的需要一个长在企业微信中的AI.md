---
title: 大圆实测 : 你真的需要一个长在企业微信中的AI
url: https://mp.weixin.qq.com/s/rP23Vjdk33GloywgTuYRMg
source: Doonsec's feed
date: 2026-07-09
fetch_date: 2026-07-10T05:55:33.376716
---

# 大圆实测 : 你真的需要一个长在企业微信中的AI

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KVER9adz907lJfrsZksPUeR7ocI04KCwsicynJyia8CC47JqbGNcSdQNGHhmrGgiapCH9MEFcpbQ837pBdjibfYHbp31uLpbuCgfO5NoQ6IlcK0/0?wx_fmt=jpeg)

# 大圆实测 : 你真的需要一个长在企业微信中的AI

原创

腾讯程序员
腾讯程序员

腾讯技术工程

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj79H3xfgvsqK9TDxOBlcUa6W0EE5KBdxacd2Ql6QBmuhBJKIUS4PSZQ/640?wx_fmt=gif&from=appmsg)

作者：蟹钳

昨天下午六点多，我在企微群里改一个方案，leader让我把最近这几天群内大家提的意见综合整理一下。我拿到这个任务的第一想法是让AI给我出个总结，但是以前这套AI协作的流程很割裂：信息在企业微信里，AI 在另一个地方。我得自己整理背景、确认内容、再把结果贴回文档里，最后还要重新调格式。

晚上我就在想，这几年，头部AI模型几乎是一路猛打猛冲。写方案、做总结、生成PPT、图片设计等等垂直或者通用大模型的急速迭代早就让**AI+**办公从概念发展为一个迟早会落地的共识。

但问题也恰恰出在这里：AI的能力已经很强了，但是想让它协助解决一个具体的工作问题，总要先把群里的讨论、文档里的背景、任务里的要求重新整理一遍，再喂给它。麻烦的不是 AI 不会做，而是每次都要我重新交代一遍“事情从哪来、现在到哪了、我要它帮我做什么”。

我越来越觉得：**AI办公的下一步，可能不是再多一个更聪明的对话框，而是让 AI 直接出现在你正在工作的地方。你在企业微信里聊项目、看文档、处理待办，需要 AI 时，左滑一下，它就出来了。**

因此，在体验了即将上线的企业微信内置AI助手——大圆后，我第一反应是：它确实在朝抹平这段距离的方向努力。

## 一个不一样的思路：AI不用你去找,它就在你正在用的地方

首先，大圆是直接嵌进企业微信里的。你在群聊里讨论项目，在文档里改方案，在待办里安排任务，它都在你的工作现场旁边，左滑一下它就出来了。以前用 AI，往往要复制聊天记录、上传文件、补充一长串背景，AI 才知道你要它做什么。但大圆不一样，它与你在企业微信里的工作上下文和记忆同频，不用你每次从头交代。

这话听着有点玄乎,官方给的说法是四个核心能力，随时唤起、总结协作信息、读写文档、定时任务。

![图片](http://mmbiz.qpic.cn/mmbiz_png/8kOo4iaaOVgGfxUS0zmibSbMJBIStAGlIO2IozkYl6Ym73jcMGwrbjyKtMicnCic9wJVdQbqibGHTwbxzf47U9hHcmnR0eNruf1bmE8twHBQWjjY/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

听着挺美好，对吧，但这个嵌入式Agent实际用起来是什么感觉还得是实践出真理。于是我按照四大能力，一一对应设计了四个基础任务场景，一个一个来体验。

## 四个真实办公场景,把大圆放进去试一遍

### 场景一：随时唤起,不退出群聊直接提问

这个能力测的核心，不是能不能唤起，而是唤起以后,它知不知道自己在哪。

我在一个日常的工作群内，没退出聊天界面，左滑，唤起大圆（这里不得不说在手机端操作的体感真的很丝滑），直接打了一句，群里聊了什么。

![图片](http://mmbiz.qpic.cn/sz_mmbiz_jpg/8kOo4iaaOVgFEHQ6ODLm2IqDj7heuPN6mzjFib1cTsJ86zian6GicgI6SgfVmnbb9hNPQuiaACro9uKibX9iaIcnFiaiajCFU9sne2HyLELnPVlIRbwM/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

我特意选了一个话题比较杂、消息量比较大的群去测，想看看它能不能分清楚当前这个具体的会话窗口，而不是把别的地方的内容也一起搬出来。

体验下来，唤起基本是即点即用，没有明显的等待感,跟切换到独立对话框那种先加载一下的感觉完全不同。识别上下文这块，它抓的确实是当前这个群的对话，没有把我之前在别的群问过的问题也混进来，这算是嵌入式体验里一个挺基础但也挺关键的点。

### 场景二：总结协作信息,项目群进展一目了然

第一关只要求它找出来，第二关要求它理明白。

我挑了一个话题更杂、讨论周期更长的智能机器人协助的项目群，里面聊的东西五花八门，横跨了好几天的讨论。

我直接问，群里聊了什么，需要我做什么。

![图片](http://mmbiz.qpic.cn/mmbiz_jpg/8kOo4iaaOVgEzD9hI9NcWfCLdQF1gVLCsq2BljrfI6Kj3xOWOmYJvGuXOHsIW11NCkZU4C5XpknjQ4PFcxHwQwr8SsRibsgjLpslvbOCuh36s/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)

它没有做流水账式的复读，而是按主题给我分了层，第一条是UI走查，提了多少个界面还原问题，谁负责修；第二条是交互方案，最终定了哪个版本。这种项目群一天能刷几十条消息，人工翻一遍都费劲，它给的是结构化之后的结果，不是简单摘要。责任人和时间点这块，识别得也挺细，谁说了我们争取今天清完，它能把这个时间点和对应的人对上号，而不是笼统地写一句有人说要处理。

### 场景三：读写文档,方案和周报直接生成

理完信息，自然就要落地成文档了。

这部分我直接给了他一个我目前的痛点任务就是每周的工作周报，虽然我有记录工作的完成情况的习惯，但是每次处理周报时还是觉得各个工作的跟进以及完成情况过于分散，会消耗我很多的精力，于是我让其结合我的to\_do给我完成一份本周的周报。

![图片](http://mmbiz.qpic.cn/mmbiz_jpg/8kOo4iaaOVgE2czicC8IF6pOB5JcTQA2ajMhGjCCILzItyYbttNsuib1kccfr4MP5Tia1MMGkBJuYRibonPek2LJdW0Bf4u64w5iaDiblzsKUkBKUg/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

让我感到比较惊喜的首先是其直接在我现有的周报excel文档下参考我以往的周报格式新建了一个子表（我并未在提示词中进行这样细节的操作描述），并且完全继承了以往周报的本阶段工作完成情况+复盘+下阶段工作安排+总体心得沉淀的风格，内容也挺不错，确实在本周的工作范围内，我只需要小修小改就可以。其次是它在操作过程中遇到敏感信息会停止并询问我是否需要继续写入，具备很强的信息安全保障意识。

这一步我觉得是四个能力里，跟独立AI对话框体验差距最明显的一个。由于企业微信的信息导出限制，以前的流程可能是，我整理信息给另一个AI对话框，并且还得检查信息是否为敏感信息，然后AI返回给我，我再在企业微信里又新建一个表格，把返回的信息放回去然后调排版格式，这一趟繁琐的工作流下来如果要使用AI的话只能用一个成语叫——食之无味，弃之可惜。但大圆现在让这一步被省掉了，它直接就是一份长在企微里的可编辑文档，我想改哪一段，点开就能直接改。

### 场景四:定时任务,把例行事务交给它

三关过完，再看第四关，定时任务，左滑唤起大圆后在右上角的三条杠里就能找到。我设置了一个每日工作待办整理的定时任务。

![图片](http://mmbiz.qpic.cn/sz_mmbiz_jpg/8kOo4iaaOVgGPQibYr9zjuXoEYicArK691A9ZJtFckC7YfTuqeBThskwibYnwhgDEkGYC9ojBGTme6HvrwRj4xicysvU6lGHrg1GYdsAryuIlzAw/640?wx_fmt=jpeg&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=5)

定时任务能按时触发，并且其给到的具体内容也是基于我的已有日程以及我的DDL文档的信息。设置本身这个动作，几乎没有学习成本，就是在入口里点一下，用自然语言去描述定时任务就完事了，然后可以在定时任务中去编辑与管理现有的任务，不需要你去理解什么复杂的定时规则或者cron表达式那种东西。

## 写在最后

四个场景都过完了，说说我的整体感觉。

大圆这四个能力，单独拆开看，唤起、总结、文档、定时，每一个放在别的AI产品里，可能都不算什么新鲜东西。它真正的差异，不在于能力本身有多超前，而在于

它不是把 AI 放进企业微信，而是让 AI 接上企业微信里的工作现场。

我一直觉得，AI这几年最大的一个坎，不是模型不够聪明，而是使用它的成本太高，你得先想起来要用它，再切换过去，再把上下文重新喂给它。这个上下文的切换成本，很多时候比模型本身的能力短板，更影响一个工具的日常使用体验与产出的结果。突然想起了功能机到智能机那段转变，当年诺基亚也能上网，也能装应用，但你得先打开一个孤立的浏览器，一步步操作，费劲。真正让手机变成手机的，不是多了一个上网功能，而是所有功能都长在了同一块屏幕里，所有信息在一个地方共享，不用再切换设备去完成一件事。工具好不好用，很多时候拼的不是能力上限，是你调用它的那一下，多顺手。

我不知道这算不算一个多大的技术突破，但作为一个每天在群里、文档里、待办里打转的普通打工人，我更在意的，可能不是这个AI有多聪明，而是我用它，到底方不方便。从这个角度看，大圆这一步，走的方向，我觉得是对的。

并且，大圆所根植的企业微信并不只是办公工具，它还连接着企业服务微信客户、供应商、加盟商、经销商等外部伙伴的工作现场。所以大圆理解的上下文，不只是适用于办公提效的一份文档、一个群聊、一个待办，也包括企业真实经营过程中沉淀下来的服务记录、跟进摘要和经营洞察，相信其日后正式开放后会被发掘出更多的使用场景。

当然，这次体验基于的还是内测版本，功能细节后续肯定会随着版本迭代继续调整，我今天记录的这些，也只是这个阶段的一个真实体验，不是终局判断。但企业AI Agent正在从一个孤零零的聊天窗口，慢慢走进真实的办公场景里，走进具体的工作上下文信息流中，这个趋势，我觉得已经能看得很清楚了。

以后回头看，这可能就是个开始。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYjZ7Hx6Udjjk2BGLzC9ahJq7ibxDd1RGA0c9NYZc1husEsvb3tY4FcWPQ/640?wx_fmt=gif&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/j3gficicyOvasVeMDmWoZ2zyN8iaSc6XWYj5q5PQEOc5ibURPb03vnRibrxC3UR8xzdyATfiawTYRV2vJvBnAIcE1FeQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/j3gficicyOvauPPfL7J2AVERiaoMJy9NBIwbJE2ZRJX7FZ2Dx7IibtTwdlqYSqTZTCsXkDS2jvNF8wWJKcibxXtOHng/0?wx_fmt=png)

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