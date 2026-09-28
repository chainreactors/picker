---
title: AI安全岗到底招什么人？
url: https://mp.weixin.qq.com/s/H9PQ7D5NAWaTAmYEGOjvQA
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:52:57.449036
---

# AI安全岗到底招什么人？

# AI安全岗到底招什么人？

原创

小胖快学网络安全
小胖快学网络安全

小胖快学网络安全吧

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

AI安全岗到底招什么人？

这几天翻AI安全岗位，我反复看到两个问题。

普通本科能不能投？不会训练大模型，是不是连简历都过不了？

我把小红书、OPPO、绿盟科技等企业公开的招聘信息放在一起看，答案没有那么悲观。但有一个前提：别把所有“AI安全岗”当成同一种岗位。

有些团队在研究模型安全，有些人在给大模型做红队测试，有些岗位负责开发安全平台，还有一些岗位，是用AI改造漏洞分析和安全运营。

名字很像，招人的标准却差得很远。方向没分清，简历里堆再多“大模型、RAG、Agent”，也可能投不到点上。

01 一个AI安全岗，里面可能是四份工作

第一种偏模型和算法。

工作会碰到安全对齐、对抗攻击、护栏模型和评测集，主要看机器学习、PyTorch、模型训练和实验设计，部分岗位明显偏向硕博。

第二种偏攻防测评。

测试对象从Web、API和主机，扩展到大模型、RAG和Agent，提示注入、知识库污染、工具滥用和越权执行都是常见任务。

第三种偏研发和平台。

这条线负责安全网关、策略引擎、测评平台和日志审计，更看重Python、Go或Java，以及接口、数据库、权限和部署。

还有一种叫AI4Sec。

它让大模型参与漏洞分析、威胁情报、代码审计和安全运营，模型只是工具，最终仍要解决安全问题。

![](https://mmbiz.qpic.cn/mmbiz_png/rPeAUx7obl26icDZKgKJfXIhrwl9QXFgUPXddKCPKOvssr37fLYRv4NdK7n7icgCgODDRSqV2ndzta4zcxCHFJiaiaoQwe5o42XQ3JLLWEGKql8/640?wx_fmt=png&from=appmsg)

02 想走算法研究，只会调API确实不够

这一类门槛最高，也最容易被误解。

企业不太关心你调用过多少模型，它更想知道：能不能构造一套数据，选出合理的基线，完成实验，再把误判和漏判讲清楚。

京东发布的大模型安全岗位，就把Benchmark、人工金集、边界样本、badcase和回归测试写进了职责。再往研究方向走，还会遇到SFT、安全对齐、对抗样本和论文成果。

所以，只有API调用经验，没有训练、数据集和实验能力，暂时不必把研究岗放在第一顺位。先做一次完整的模型评测或论文复现，比再学一个Agent框架更有用。

03 网安学生转AI安全，攻防测评最顺手

这条路线并没有把过去学的东西清零，只是攻击面变了。

以前关注输入校验、身份认证和权限绕过，现在还要继续追问：数据怎么进入上下文？模型能调用哪些工具？Agent的权限是谁给的？结果会不会被写进长期记忆？

小红书2027校招的AI安全岗位，已经把提示注入、知识库污染、MCP接入、记忆隔离和沙箱执行写进职责。

做过Web安全、API鉴权、数据安全、渗透测试或漏洞研究的同学，都有迁移基础。需要补的不是一整套算法课，而是RAG和Agent到底怎样运行，以及怎么把一次攻击做成可重复的测试用例。

04 本科生别忽略平台工程

不少同学一看见“AI安全算法”就准备退出，其实企业还缺另一类人：把规则、模型和业务系统接起来的人。

小红书把AI安全算法和AI安全研发分开招聘。OPPO的安全算法岗也写得很直接：需要编程、API调用、算法复现和功能落地，部分方向并不涉及模型训练。

如果你后端基础不错，做过扫描器、安全平台、数据处理或自动化工具，可以重点看AI安全研发、平台开发和测试开发。

这类岗位绕不开计算机基础。Python、Go或Java至少熟练一门，接口、数据库、权限控制、日志监控和容器部署也要能动手。

拿一个API套壳项目去冲研究岗，胜算不大。把一个测评平台做完整，反而更能说明你的价值。

05 AI4Sec，先有安全问题，再谈大模型

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPeAUx7obl3TENAaceN8iauYTJgCFKMq6O7oI2y09coXk5WOFImGfgEkgIAaUKQhqFCy0LSWVXmgbRkLic6cGcdGJl1bZCdYqWDmDCOrlPUDE/640?wx_fmt=png&from=appmsg)

一个能聊天的机器人，不能算AI4Sec项目。

更像样的系统应该能读取告警、查询资产、检索漏洞知识、调用验证工具，并把判断依据一并交出来。信息不够时，它要知道停下来；涉及高风险操作时，还要把决定交回给人。

真正难的地方也在这里：证据从哪来？工具失败怎么办？模型出现幻觉怎么办？自动处置由谁授权？

如果你已经做过漏洞分析、代码审计、威胁情报或安全运营，再把原来的工作流程拆成知识库、模型和工具可以执行的步骤，会比从零追大模型概念更有优势。

06 项目别停在“能跑起来”

我更建议用五样东西检查自己的项目。

一张架构图或威胁模型，说明保护什么、攻击从哪里进；一组可复用的测试数据，个人项目先做50至100条也可以，但要有分类依据；一套能运行的代码；一组真实指标；最后再补一份测试报告，把失败案例和能力边界写出来。

![](https://mmbiz.qpic.cn/mmbiz_png/rPeAUx7obl11bddN5ibt0ibk2kxCRT0KBc2NBDjFyLQdJN2OTdmMlIvUCAeNMoOtcIC4LKx6GDunDJHQdoMviaPIia5DJMsPoQoc1HQDp1r34js/640?wx_fmt=png&from=appmsg)

项目方向不必做得特别大。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPeAUx7obl0CxQ20AtfRkgGxXP2bw2GDl6326YztIZmib1eibU4TTYc4wZewaicJ4SO2tgwZeWPqMuZiaYeCDibic4ntWodjwOh1dXH33HE42SLRY/640?wx_fmt=png&from=appmsg)

比如做一个Agent工具调用安全评测平台，测试提示注入、越权调用和敏感文件读取，再加入工具白名单、参数校验、最小权限和审计日志，对比防护前后的攻击成功率。

也可以做安全告警研判Agent，让它完成告警解析、知识检索、工具验证和风险排序。每个结论必须附带证据，无法确认就明确拒答，最后统计任务成功率、错误结论率和证据引用正确率。

这两类项目不一定需要昂贵的算力，却能同时证明安全理解、AI应用和工程实现。

07 简历里别只写“基于大模型”

项目描述可以顺着四个问题写：解决了什么风险？构建了多少样本？使用什么方法检测或处置？最终得到怎样的检出率、误报率和响应耗时，又沉淀了什么代码、工具或报告？

![](https://mmbiz.qpic.cn/mmbiz_png/rPeAUx7obl37LkuoWocyRV1sicfw2ghgmicxLRRIukF2YyeF97wGTATpHS3egpZG3fIsb6BGRPYOkU7FJxaOBhRlnbnicIVNahaQDHp2IdGCQk/640?wx_fmt=png&from=appmsg)

数字一定要来自自己的测试，宁可规模小一点，也不要编。

按照公开JD反推，面试前至少要弄清这些问题：提示注入和越狱有什么区别？RAG知识库怎样被污染？Agent工具调用怎样做鉴权和最小权限？安全护栏除了准确率，还要看哪些指标？AI4Sec怎样减少幻觉并留下证据链？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPeAUx7obl2nEJAumfgIhgFtlXSdTZjy9o2LXzgibpwCnvYQ3PjYd4dMULVbICgFs2NepcGfLwJQvlPX9QTr2Zoym6ypR7TtWdlTV1WgJGe4/640?wx_fmt=png&from=appmsg)

Python、数据结构、计算机网络、操作系统和数据库也不能丢。AI安全不是绕开计算机基础的捷径。

08 到底该选哪条路？

1.算法和科研能力强，可以冲模型安全、对齐和AI安全算法；

2.攻防基础更扎实，可以看AI安全测试和红队测评；

3.开发能力突出，重点看AI安全研发和平台工程；

4.已经深耕漏洞、情报或安全运营，AI4Sec会更顺手。

如果只有一个月，不妨这样安排：第一周弄清LLM、RAG和Agent的工作链路；第二周把项目核心功能做出来；第三周准备测试集并跑出指标；最后一周补报告、架构图和简历描述。

![](https://mmbiz.qpic.cn/mmbiz_png/rPeAUx7obl3Is9cM1LYDTGdribNviaJn182egkDFCgyhe3WKw7ibCslfV8a9CHJsThxDfBfwibXLG2o6QxKj0X6mN6QIicaTwTyCJMXwKX6CxWxY/640?wx_fmt=png&from=appmsg)

说到底，企业不是在找一个“用过大模型”的人。它想找的是：看得见真实风险，做得出解决方案，也能拿数据证明结果的人。

如果不清楚自己AI水平的，可以先在网安秋招工具箱 www.waqz.cn 自测一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPeAUx7obl224sZcOibeZCj1TG7QBwOVJZYsq5rjCT6JTgswW8AM6nZOsOiaXFc4f5aLOxTcAOakZ9m42IfB3A0UPQmDwpJRZNsu4FkpO0tuc/640?wx_fmt=png&from=appmsg)

星球介绍

一个人走的很快，但一群人才能地的更远。吉祥同学学安全这个[星球🔗](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247486065&idx=2&sn=b30ade8200e842743339d428f414475e&chksm=c0e4732df793fa3bf39a6eab17cc0ed0fca5f0e4c979ce64bd112762def9ee7cf0112a7e76af&scene=21#wechat_redirect)成立了2年左右，已经有600+的小伙伴了，如果你是网络安全的学生、想转行网络安全行业、需要网安相关的方案、ppt，快加入我们吧。系统性的知识库已经有：[《Java代码审计》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484219&idx=1&sn=73564e316a4c9794019f15dd6b3ba9f6&chksm=c0e47a67f793f371e9f6a4fbc06e7929cb1480b7320fae34c32563307df3a28aca49d1a4addd&scene=21#wechat_redirect)++[《Web安全》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484238&idx=1&sn=ca66551c31e37b8d726f151265fc9211&chksm=c0e47a12f793f3049fefde6e9ebe9ec4e2c7626b8594511bd314783719c216bd9929962a71e6&scene=21#wechat_redirect)++[《应急响应》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484262&idx=1&sn=8500d284ffa923638199071032877536&chksm=c0e47a3af793f32c1c20dcb55c28942b59cbae12ce7169c63d6229d66238fb39a8094a2c13a1&scene=21#wechat_redirect)++[《护网资料库》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484307&idx=1&sn=9e8e24e703e877301d43fcef94e36d0e&chksm=c0e47acff793f3d9a868af859fae561999930ebbe01fcea8a1a5eb99fe84d54655c4e661be53&scene=21#wechat_redirect)++[《网安面试指南》++《网安秋招训练营资料》++《网安秋招工具箱》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247486695&idx=1&sn=85fefa98f17e6f1f2dd745ef5a498a10&token=1860256701&lang=zh_CN&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPeAUx7obl2kibKztkMLqrjPVSqjTUbCLCGwbT1DWH4perYJxNUk1hfTjn765c5iaFib8a8MEiboBr2YbvuCUwkmiboibzTJsCIBhoMXCOjRcQW0U/640?wx_fmt=png&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Oh2kiaia4icySDqrNyBCHuYdPugU7RJlWianw9FiaCn6EH2P31ATvZJnibr9IgONEx77AFiaEib2Bnh807WMHcrr9ibqdMA/0?wx_fmt=png)

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