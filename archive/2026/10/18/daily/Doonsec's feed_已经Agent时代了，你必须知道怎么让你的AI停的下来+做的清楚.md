---
title: 已经Agent时代了，你必须知道怎么让你的AI停的下来+做的清楚
url: https://mp.weixin.qq.com/s/ym-6V3Y5NTURyjH6sxLovw
source: Doonsec's feed
date: 2026-10-18
fetch_date: 2026-10-19T07:07:05.971383
---

# 已经Agent时代了，你必须知道怎么让你的AI停的下来+做的清楚

# 已经Agent时代了，你必须知道怎么让你的AI停下来+做清楚

原创

allby森林之家
allby森林之家

allby森林之家

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

"会用Agent"这件事，从今年起开始不值钱了。

两年前，你在简历上写一行"熟练使用大模型"还算万里挑一的加分项；而现在，随便一个单位里的实习生都能用Agent做完以前一周的活。

工具普及到这个份上，会用Agent已经不再是优势，那新的分水岭是什么呢？

最近我观察到AI圈的风向逐渐开始变了——AI开始从"狂奔期"走向了"治理期"，会用AI已经不值钱了。

2026 年的真功夫，是让AI停得下来+做得清楚。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2wf8V0A7uBdYUnnwIRJNRWvOLydSprfP6zTsKGSOEyaibtmnVgJic2nrAuqKqhF5EIJYdVRiaPYlictDRvvicvbQWIexhW6CpMnZJwF3BMNWlrbQ/640?wx_fmt=jpeg&from=appmsg)

01

Agent永远不会告诉你"做完了"

我之前做过一个小工具合集，做到中后期每次对话都刹不住车，每跑一次任务就是快一个小时。而且期间Agent还会一直给我列优化清单，每改完一批马上又来新的一批———“代码这里可以再重构一下、测试这里可以再补几个、文档可以再更新一版”。

一个本来半小时能搞定的需求，经常不知不觉就搞了一个下午。

很多时候，判断AI"做完没"这件事都十分地消耗我。我有时甚至只能一句一句手动追问：这个对话是可以归档了，还是到下一步了？

**Agent推荐下一步做什么，这个功能本身就是认知陷阱，它会让你永远觉得任务没完。**

所以为了解决这个问题，我找到了一个Prompt+hook，让它在每个对话、每轮回复的最后一行自动生效。

Prompt核心机制很简单，就是红绿灯：

![](https://mmbiz.qpic.cn/mmbiz_jpg/2wf8V0A7uBdxsMGAMbvWoCSbrGktQhgQRS05vpMoQeQUqMczxY3z5q6Z0D5XOFFFKDxfvhFHUKV5QCMLJhLApYzc1ssia0gwibJYauAicGPhZY/640?wx_fmt=jpeg&from=appmsg)

开工第一轮钉死清单——目标：A、B、C；此后每轮只对照清单干活；回复最后一行亮灯。🟢还差：B、C，顺手发现的改进只记搁置、一行以内；🟡超出项能串成计划，逐项附证据，等你裁决；🔴零散超项压成三行存档，收工。判定口诀一句话：**能串成计划就黄，串不成就地红。**

完整版排成了卡片，长按保存，贴进系统提示词或hook就能用：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2wf8V0A7uBdxsD8GovBS90G7zkT88BhLpribRjhiaofTNsNW7qOGtM3phicgLBARET7JWWPQSfWqpvkWD2A7N54P32ezd40dl3Nn22NtRDz1A0/640?wx_fmt=jpeg&from=appmsg)

这个红绿灯不是一次就成型的，中间也踩过许多坑。

初版是只有绿灯和红灯的，有一次亮了红灯，下面列着三件事：PR合并等确认、远端分支未删、生产迁移的后续步骤。

我看完就懵了，这些我做过吗？然后我新开一个对话查了一圈才确认——**三件事情我其实一件都没做过。**这是模型自己列的待办掺着纯幻觉，还跟一堆可有可无的建议混在一块儿。

所以在这之后我的第二版便加了黄灯，黄灯的意思是：你要的活我做完了，剩下的建议能串成一个有目标、有验收标准的计划，我落盘成文件、给你路径，跑不跑你定。

加上之后效果实打实的，我手上有份存了一千多条案例的提示语案例库，一次对话结尾亮了黄灯，直接给了份37行的后续计划；哪怕只是整理十几个过期对话的残留事项，也拿到一份63行的处理方案等我拍板；子代理也一样，我的Sonnet子代理跑完一个数据库迁移验证，末尾一行绿灯，完事。

最明显的变化是心理上的：每个任务开始有「完成的时刻」了。以前像一条河，你不知道对岸在哪，只能一直往前淌；现在有终点线。一天跟Agent协作十几个任务的时候，这种确定感特别重要。

02

别再凭手感调Prompt

AI的车刹住了，还有个更大的坑——那就是技能包（Skills）。

Agent开发常态化之后，skill越堆越多。可大多数人是怎么调技能包的呢？

改一句提示词，跑一次，看看结果：行就留着，不行就再改一版。

这完全是靠人工调试、全凭感觉，没有统一标准、自编自用。经常会出现上次好使这次就拉胯的情况，你根本不知道是哪个字改坏的。单人自用也就算了；团队十几个人共用一个库，谁半夜改了一版，第二天全线崩给你看。

为了解决这个问题，我搜集资料，找到了skill-up推荐给你们：它是**Agent Skill的pytest加CI，再外挂一个自修复Agent，不是业务Agent，是个用Go写的CLI评测工具。**

**![](https://mmbiz.qpic.cn/mmbiz_jpg/2wf8V0A7uBe2fQgejJnnhmia6mV5s0yk5qI74MpWe5fj8lIqluTW3pacUU5zHyRSb2oSUz8m1kB6qFKCUXib6EyLeAiah8Go5IibqQzRKeQw684/640?wx_fmt=jpeg&from=appmsg)**

**YAML写声明式用例，塞到真实Agent引擎里跑，而且不是离线模拟，是真的能跑。它的断言分了三类：规则断言（输出里必须有什么、不能有什么）、脚本断言、LLM语义断言（让一个agent\_judge按你给的标准判卷）。跑完吐JUnit、HTML、JSON三种报告，直接接CI流水线当门禁。边界不限领域，只认格式——带SKILL.md的技能包都能测；它自己不执行工具调用，由后端的Agent Engine执行，它只观测、只断言。**

千万别被"评测工具"四个字给唬住了，它上手简单得很，用起来就三条命令：validate只查YAML语法、run全量评测、run --case单条重跑修完可以立刻验。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/2wf8V0A7uBcibfFtNUIh8Hhg5aF0oGm7BwiaUPH6KRVRJnbPYT02qcGOxRnrxGYX0xo5A6fjvYnpV3vUQcA1RYRZ0mW5niaO6486vN3QQdXWng/640?wx_fmt=jpeg&from=appmsg)

目录也就三层：被测的SKILL.md原封不动，旁边加一层evals：eval.yaml管引擎配置，cases放用例，fixtures放测试夹具。用例可以从抄开始：最简单的用例就一条断言，让技能写段Hello World，must\_contain里填个print，输出带error就算挂；复杂点的代码评审场景，加载预置仓库和补丁，挂上agent\_judge判卷，标准还是人话：必须指出存在空值未校验、必须给出修改建议、不能直接说代码没问题。

真正有意思的是配套的skill-upper，一个内建在仓库里的Agent：跑评测、发现失败、诊断原因、自动改SKILL.md或者补测试用例，然后重跑评测。循环迭代，官方管这叫Eval-to-Evolution闭环——技能包测出毛病，自己修自己，越测越稳。

在pytest和CI出现之前，代码也是"跑一次没报错就上线"，现在轮到skills了——技能从一次性的Prompt编写，变成可持续测试、可持续回归、可自迭代的标准化资产。凭手感调Prompt的日子，到头了。

03

最后的总结

回头看这三年行业卷什么：更大的上下文，更多的工具，更长的自主运行时间——让Agent跑得更快、更久、更不知疲倦。

能力也确实在疯涨，Agent一口气干100个小时的任务不算稀奇。700多篇数学论文写出来了，连那片1/3紫外线下从没被看清过的天空，都给还原出来了。

可"怎么让它停下来"和"它到底靠不靠谱"，却渐渐地开始被人们给忽视。人类造了汽车，花了几十年才发明安全带。每一种强大的能力背后，都跟着一个制动装置。

所以回到开头那句：2026年的Agent功夫，不在"会用"，在停得下来+做得清楚。"会用"的人满地都是，而最终能让任务有终点线、让技能经得起回归的人，才是最稀缺的。

无论AI能力如何疯涨，但最终的判断权必须攥在我们自己手里。

预览时标签不可点

修改于

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZEY5a7YmV0vemdjA6fvqqblGxKWCcN4CTJCB2ujDEQP5r90enPicrtUGtNvOQIl2a61SGXtT8OcClCWGfhwv5DQ/0?wx_fmt=png)

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