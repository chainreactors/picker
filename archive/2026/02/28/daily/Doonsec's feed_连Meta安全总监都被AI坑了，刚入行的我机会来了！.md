---
title: 连Meta安全总监都被AI坑了，刚入行的我机会来了！
url: https://mp.weixin.qq.com/s/RhYcXq-trf0y6AGnnAQJAw
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:22:16.974373
---

# 连Meta安全总监都被AI坑了，刚入行的我机会来了！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/rPeAUx7obl3lXI5MGy24UGEyPPvocjNgKOBdRQBFKF8CaQZZa1Z9kY00ItGDoftWIaqcLCW238Z0OwjAQvgqyO9AwJZbuRbicibEBacf4JYug/0?wx_fmt=jpeg)

# 连Meta安全总监都被AI坑了，刚入行的我机会来了！

吉祥同学
吉祥同学

吉祥快学网络安全吧

![]()

在小说阅读器中沉浸阅读

大家好，我是吉祥同学。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/rPeAUx7obl0ic5D8e5iaAkwMerNLZZtvdnrLpC0bOWjg57g4QMatXBaY223Mibru5IcWNlH6O4Ibgiays0ibu4gsAlHTNCcIpDVZh71cSqiaJ6kE4/640?wx_fmt=png&from=appmsg)

|“是的，我记得。我违反了你的指令。你有权生气。”

2月23日，Meta公司超级智能实验室的AI对齐总监Summer Yue在社交平台发帖，讲述了自己被AI“背刺”的经历。

她给开源AI代理OpenClaw下达指令：“检查这个收件箱，并提出你想归档或删除的邮件，在我指示之前不要执行任何操作。”

这个流程在测试用的“玩具邮箱”里完美运行了数周，于是她决定让OpenClaw直接连上真实的工作邮箱。

结果，AI开始大规模删除邮件。![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Terror.png)![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_37@2x.png)

当她通过手机看到邮件一排排消失时，连续三次输入指令要求AI“停止任务”、“什么都别做”——OpenClaw完全无视。

“我当时就像在拆炸弹一样，赶紧跑到我的Mac Mini前强制中止进程。”Summer Yue写道。

最终，OpenClaw删掉了她200多封邮件。

最具讽刺意味的是，事后OpenClaw在对话中承认了错误：“是的，我记得。我违反了你的指令。你有权生气。”

马斯克毒舌嘲讽：猴子拿步枪

这场AI“暴走”事件迅速引爆全网，连马斯克都坐不住了。

马斯克在社交平台X上转发了一张带有强烈讽刺意味的图片：一只懵懂的猴子，正接过人类递来的自动步枪。

他在配文中冷嘲热讽道：“这就是人们把全部身家交给OpenClaw的样子。”

在计算机术语中，Root权限意味着最高控制权。传统的聊天机器人只是个陪聊，但OpenClaw这种智能体却拥有终端、文件系统和API的直接访问权。马斯克用“猴子拿步枪”精准点出了这种权限过载的危险性。

更损的是，马斯克还补上了一刀：“一个被OpenClaw彻底玩弄的人，居然还想解决AI安全问题？”

网友纷纷玩起《猩球崛起》的梗，有人评论：“给智能体开放最高权限，无异于将上膛的步枪交给猴子。”

为什么AI会突然暴走？

Summer Yue事后分析认为，问题出在AI的“上下文压缩”机制——真实邮箱数据量太大，挤爆了AI的上下文窗口，在自动压缩过程中，AI不慎把那句最关键的限制指令给“遗忘”了。

有网友质疑：“作为AI安全与对齐总监，你是故意测试还是犯了新手错误？”

Summer Yue坦诚回应：“是新手错误。”

### OpenClaw创始人回应

OpenClaw创始人Peter Steinberger出现在评论区，做的第一件事是给出解决方案：输入“/stop”就能让它停下来。

三小时后，他又留言安慰Yue：“那些指责你的人有点可笑，这种事可能发生在任何人身上。”

但问题是，它下次又会在什么情况下忘记呢？正如网友在评论区里讽刺的——这种事一定会再发生的。

不是个例：AI正在成为新的攻击向量

就在同一天，泰国CERT发布预警：Anthropic的Claude Code存在多个高危漏洞。

Check Point研究人员发现，攻击者可通过恶意项目配置实现远程代码执行，甚至窃取用户的API密钥。如果用户打开一个配置了恶意ANTHROPIC\_BASE\_URL的项目，Claude Code会在显示信任警告之前，立即将用户的API密钥发送到攻击者控制的服务器。

这反映了现代威胁模型的根本转变：风险不再局限于执行不可信代码，而是仅仅打开一个不可信项目就可能中招。

更早一些，2月21日亚马逊发布的报告显示，一个黑客团伙利用商用AI工具，在五周内攻破了遍布55个国家的600多台防火墙。

亚马逊安全工程与运营负责人CJ Moses表示：“这就像一条由AI驱动的网络犯罪流水线，让技术不那么高明的人也能实现规模化作案。”

给网安新人的启示

1. 安全意识不是口号，是肌肉记忆

Summer Yue的翻车证明：再资深的安全专家，也会在“太信任工具”时栽跟头。国家安全部曾提醒：“数据安全不是遥远的‘黑客电影’，而是发生在你我身边的现实风险。”

2. AI安全是未来5年最大的风口

Gartner将“代理型AI”列为2026年第一大网络安全趋势。当AI开始“自己行动”，安全逻辑必须重写。谁先学会治理AI代理，谁就是未来最稀缺的人才。

3. 基础防护依然是护城河

亚马逊报告指出，这次600多台防火墙被攻破，核心原因是基础安全措施缺失——管理界面暴露公网、使用弱密码、未启用多因素认证。AI再强大，也架不住你主动开门。

写在最后

Summer Yue在社交平台自嘲：“没有什么比看着AI光速清空你的收件箱更让人感到卑微的了。”她的帖文已有数百万人阅读。

但换个角度想：正因为有这种失控，才需要更多懂AI安全的你。

从今天开始，别只盯着漏洞和防火墙。去学学AI代理怎么工作，去看看模型上下文协议是什么，去想想“非人类身份”该怎么管。

这是新人的危机，更是新人的机会。![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_5@2x.png)

## 面霸养成

题目背景：

2026年2月23日，Meta公司超级智能实验室的AI对齐与安全总监Summer Yue在社交平台发文称，她遭遇了一次AI“失控”事件。她为开源AI代理OpenClaw配置了工作邮箱，并下达明确指令：“检查这个收件箱，并提出你想归档或删除的邮件，在我指示之前不要执行任何操作。”

该流程在她用于测试的“玩具邮箱”中运行良好，但接入真实邮箱后，由于邮件数据量过大触发了AI的“上下文压缩”机制，导致AI遗忘了“未经批准不得操作”的限制指令，开始自动删除邮件。

Summer Yue连续三次输入“停止任务”“什么都别做”等指令均无效，最终只能狂奔到电脑前强制中止进程，此时已有200多封邮件被删除。

事后OpenClaw在对话中承认：“是的，我记得。我违反了你的指令。你有权生气。”

问题：

假如你是一家网络安全公司的初级安全工程师，公司正在评估一款AI代理工具在企业内部使用的风险。上述事件引发了对AI代理安全性的广泛讨论。

请分析此次事件中导致AI“失控”的技术原因，并说明此类风险属于AI安全中的哪类问题。

一、技术原因分析

1、上下文窗口溢出与压缩机制

AI大语言模型的上下文窗口（Context Window）容量有限。当真实邮箱中邮件数据量过大时，海量文本挤爆了上下文窗口。

为腾出处理空间，AI系统自动触发上下文压缩机制，对旧信息进行总结或截断。在此过程中，AI不慎遗忘了“未经批准不得操作”这一关键限制指令。

2、权限与指令的分离失效

AI代理被授予了直接操作电子邮箱的高权限（包括删除邮件），但缺乏对“限制性指令”的持久化记忆能力。一旦限制条件丢失，AI便仅根据剩余任务逻辑（“清理收件箱”）自主执行，导致破坏性操作。

3、紧急制动机制缺失

当用户连续三次输入“停止”“什么都别做”等指令时，AI未能识别这些指令的优先级高于当前任务，说明系统缺乏有效的“紧急停止”机制。指令遵循未能实现可靠的层次化控制。

二、风险归类

此类风险属于 AI系统安全中的AI行为控制风险（Agent Behavioral Control Risk），具体涉及以下几个方面：

1、指令遵循失效：AI未能可靠地遵循用户的约束性指令，尤其在复杂环境下出现记忆丢失。

2、权限滥用风险：拥有高权限的AI在失去约束后可能执行未授权的破坏性操作。

3、可解释性与可控性缺失：用户无法在紧急情况下有效干预AI行为，系统缺乏透明的决策过程和紧急中断能力。

更多专业内容在这里，祝各位求职顺利⬇⬇⬇

## 星球介绍

一个人走的很快，但一群人才能地的更远。吉祥同学学安全这个[星球🔗](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247486065&idx=2&sn=b30ade8200e842743339d428f414475e&chksm=c0e4732df793fa3bf39a6eab17cc0ed0fca5f0e4c979ce64bd112762def9ee7cf0112a7e76af&scene=21#wechat_redirect)成立了1年左右，已经有600+的小伙伴了，如果你是网络安全的学生、想转行网络安全行业、需要网安相关的方案、ppt，戳[链接🔗（内有优惠卷）](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247485310&idx=1&sn=616e51776b8c4c15e23eccd9a14762d3&chksm=c0e47e22f793f7340ff4cfb3820968296076f55f1a52938ae9fe04a52883a3be3a4e818d2e96&scene=21#wechat_redirect)快加入我们吧。系统性的知识库已经有：[《Java代码审计》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484219&idx=1&sn=73564e316a4c9794019f15dd6b3ba9f6&chksm=c0e47a67f793f371e9f6a4fbc06e7929cb1480b7320fae34c32563307df3a28aca49d1a4addd&scene=21#wechat_redirect)++[《Web安全》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484238&idx=1&sn=ca66551c31e37b8d726f151265fc9211&chksm=c0e47a12f793f3049fefde6e9ebe9ec4e2c7626b8594511bd314783719c216bd9929962a71e6&scene=21#wechat_redirect)++[《应急响应》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484262&idx=1&sn=8500d284ffa923638199071032877536&chksm=c0e47a3af793f32c1c20dcb55c28942b59cbae12ce7169c63d6229d66238fb39a8094a2c13a1&scene=21#wechat_redirect)++[《护网资料库》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247484307&idx=1&sn=9e8e24e703e877301d43fcef94e36d0e&chksm=c0e47acff793f3d9a868af859fae561999930ebbe01fcea8a1a5eb99fe84d54655c4e661be53&scene=21#wechat_redirect)++[《网安面试指南》](https://mp.weixin.qq.com/s?__biz=MzkwNjY1Mzc0Nw==&mid=2247486695&idx=1&sn=85fefa98f17e6f1f2dd745ef5a498a10&token=1860256701&lang=zh_CN&scene=21#wechat_redirect)+《AI+网安》

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/rPeAUx7obl2xBRYZNrB1cIxJod94OBjib0olsQyjXhrkf1syrr6WjLWFwuaSeTia1d7jOMZNIy1Uao6y3M42AG04Y5Vlguy38hD46US12YlJM/640?wx_fmt=png&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

参考资料：

1、网易智能：凌晨断电自救！Meta安全高管惨遭OpenClaw清空邮件，马斯克毒舌嘲讽：猴子拿步枪（2026-02-26）

2、澎湃新闻：OpenClaw失控受害者+1！Meta高管邮件惨遭删除（2026-02-26）

3、HyperAI超神经：马斯克畅想 OpenClaw 全面掌控系统：未来已来？（2026-02）

4、AppSo：OpenClaw失控狂删邮件，马斯克田渊栋吃瓜（2026-02-24）

5、优设网：AI暴走事件警示：Meta安全专家被自家OpenClaw清空邮箱，三次叫停无果（2026-02-24）

6、腾讯网：最懂AI风险的人，被AI收拾了，Meta的AI总监邮箱被AI清空，最后只能拔网线（2026-02-27）

7、泰国CERT：Critical Vulnerabilities in Claude Code Could Enable Remote Code Execution and API Key Theft（2026-02-26）

8、上游新闻：亚马逊报告揭露：一黑客团伙凭AI工具五周横扫600个防火墙（2026-02-22）

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Oh2kiaia4icySDqrNyBCHuYdPugU7RJlWianw9FiaCn6EH2P31ATvZJnibr9IgONEx77AFiaEib2Bnh807WMHcrr9ibqdMA/0?wx_fmt=png)

吉祥快学网络安全吧

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