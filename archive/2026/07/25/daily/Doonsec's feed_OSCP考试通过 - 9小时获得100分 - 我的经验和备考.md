---
title: OSCP考试通过 - 9小时获得100分 - 我的经验和备考
url: https://mp.weixin.qq.com/s/e14hcYkjvXPSIlrXqNQGQg
source: Doonsec's feed
date: 2026-07-25
fetch_date: 2026-07-26T05:23:23.723017
---

# OSCP考试通过 - 9小时获得100分 - 我的经验和备考

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/zVE7oia7FCW80uic3anEXeiaWswPmyc6lWpJJADJ4UlYICsSNQsgtLDJBzcwMib31gq2jo0icwHvlSt1jzhbicscGJE8FAyXxY0PkaKTpicuAgwuBk/0?wx_fmt=jpeg)

# OSCP考试通过 - 9小时获得100分 - 我的经验和备考

渗透测试
渗透测试

谷安培训

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

最近用了9个小时以100分的成绩通过了OSCP认证考试，我想分享一下我的备考策略和考试经验，希望能帮助其他正在备考OSCP的朋友。

虽然OSCP在业内广为人知，但我还是想坦诚地分享一下我对课程内容的体验以及大家可以对考试内容抱有的合理预期。

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/zVE7oia7FCW9HYicprlY0bc2Y5DC4SxJTsknIvKQ3ia0VibeZGhoWmibQV9AWTBByIruq5ldUOnbicIHshPUKh4icQcMtG9ibFuhdatmVVdyGfZqL4s/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzU4MjUxNjQ1Ng==&mid=2247527305&idx=1&sn=c56d6a53af679ffd2c88e2cd33e75856&scene=21#wechat_redirect)

**# 背景和准备 #**

我拥有三年网络安全经验，其中两年是渗透测试工程师，持有CISP-PTE证书。无论之前的经验如何，OSCP考试我进行了充分的准备。

我的备考方法严谨而有针对性。没有浅尝辄止，而是按照谷安的培训节奏完成了5天的精要课程学习，打靶演示学习，作业实操，靶机练习，靶机思路学习，完成打靶测试。激活LAB后，专注于通过实际操作机器和实验室，培养扎实的实践技能，力求最大程度地模拟考试环境。

在机器的挑战上，我用电子表格详细记录了我的进度，包括每台机器的难度等级以及使用的关键技巧。除了单机操作之外，我基本上完成了所有的挑战实验。这些挑战实验尤其有价值，因为它们模拟了考试中会遇到的多机 Active Directory 场景。考试中的 AD 部分可不是随便就能应付的。

OffSec 的靶机搭建方法和风格与其他平台截然不同。他们的靶机通常需要特定的枚举模式和漏洞利用方法，这些你在其他地方很难遇到。我想强调的是，在参加考试之前，务必先完成 Proving Grounds 的靶机。虽然其他平台的经验很有价值，但它并不能直接替代你熟悉 OffSec 靶机结构的方式。

提示：为你的练习机创建一个追踪系统。记录你从每台机器中学到了什么，哪些技巧有效，哪些无效。这能帮你建立一个个性化的知识库，方便你在考试前或考试当天进行复习。

##

**# 学习资料和模板 #**

拥有条理清晰的模板对我的考试成绩起到了至关重要的作用。在整个备考过程中，我创建并完善了多个模板：

**独立机器模板：**

**Windows模板**（镜像链接）

Linux 模板

**Active Directory 设置：**

AD 设置检查清单

除了这些模板之外，我还保留了我在网络安全学习过程中积累的个人笔记。这些笔记包含了具体的命令、常见的陷阱，以及从实际渗透测试、学习和其他认证中汲取的经验教训。

这些模板并非静态文档——我在练习过程中不断更新它们，添加新的技巧并改进我的方法。到了考试那天，这些模板已经完全符合我的工作习惯了。

##

**# 考试日 #**

我为考试制定了详细的计划，以保持条理清晰并确保适当休息。精神疲劳是真实存在的，提前安排休息时间能帮助我一整天保持清醒。

## 笔记#

考试期间我使用 Obsidian 做笔记，它精心构建了一个目录系统，使所有内容井然有序且易于访问：

这种结构使我能够快速切换机器，跟踪整个环境中已发现的凭据，并为不同的考试组件维护单独的检查清单。CREDS 文件夹对于 AD 部分尤其重要，因为密码重用和凭据收集在该部分至关重要。

## 考试经历#

我带着一套清晰的策略参加了考试，这套策略在我之前的练习中都行之有效：

**初步侦察（0-30分钟）：** 先对所有独立机器进行了快速的nmap扫描。目标并非深度枚举，而是寻找容易利用的漏洞或我比较熟悉的攻击服务。这一策略立竿见影——考试开始仅25分钟，我就攻破了第一台机器，因为我发现了一个在练习中多次遇到的漏洞。

**Active Directory 攻击（30-85 分钟）：** 快速获胜后信心倍增，我转而挑战 Active Directory 部分。这时，我在 OSCP 挑战实验室的刻苦练习发挥了至关重要的作用。我仅用了 55 分钟就获得了域管理员资格。AD 部分可能令人望而生畏，但通过系统性的枚举和遵循经过验证的检查清单，最终轻松应对。

**剩余独立测试（85分钟-9小时）：** 拿下域管理员后，我只需要再得10分就能通过。我休息了相当长一段时间来放松身心，调整状态。这次休息让我能够以全新的视角看待剩下的机器。之后，我逐一攻克剩余的独立测试，优先处理那些根据初步判断我认为最有把握的机器。

在获得域管理员权限后大约 7 个小时，我又拿到了剩下的四个标志。考试还剩 14 个小时，所以我在睡觉前、整理了所有屏幕截图和笔记，完成全面渗透测试报告并提交了报告。

##

**根据我的经验，以下是成功的重要因素**

**1. 不要跳过挑战实验室**

Active Directory 挑战实验室（OSCP A、B、C）与考试的 AD 部分难度相当。跳过这些实验室将是一个巨大的错误。它们能教会你考试当天绝对需要的各种方法论、枚举技巧和横向移动技能。

**2. 构建强大的模板**

创建并完善适用于 Windows 和 Linux 系统的模板。模板应包含你常用的枚举命令、常见的权限提升检查以及漏洞利用技巧。考试时，你肯定不想浪费时间记忆语法。

**3. 试验场机械**

如果你一直坚持使用 Proving Grounds Play 和 Practice 中的机器进行练习，那么考试中的独立机器对你来说就很容易上手。不要只做一遍——要反复练习，尝试不同的攻击路径。

**4.整理你的笔记**

无论你使用 Obsidian、CherryTree 还是其他工具，都要建立清晰的组织系统。能够快速地在多台机器上查阅你的发现至关重要，尤其是在 AD 部分。

**5. 安排休息时间**

精神疲劳是真实存在的。提前计划好休息时间并严格执行。我每隔2-3小时就休息一次，这让我在整个考试过程中都保持了清醒的头脑。

##

**最后想说的话**

OSCP考试形式要求考生在24小时内攻破目标机器，然后再用24小时撰写报告。这项考试绝非易事——如果准备不足，考生很容易被难住。

Active Directory 部分的难度与挑战实验室部分完全相同，这再次强调了练习的重要性，切勿错过任何练习机会。如果你事先在类似的机器上进行过练习，那么独立机器部分就比较容易上手了。

令人惊喜的是结果，协议上写明是 10 个工作日，但我不到 48 小时就收到了结果——OffSec 在这方面做得很好。

OSCP考试的成功关键在于充分的准备、科学的方法论以及在压力下保持冷静。如果你已经完成了所有准备工作——完成了练习题、掌握了挑战实验室的题目，并建立了可靠的模板——能大幅提升你的应试把握。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/m6icpc8EwicOWhNMBh1HsJsyt1RAL2gLIlBcED17p5WPgRrbdpASsYZETkfMoB3tMKveTUhALNfM31Ih4A58R5Lg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=1)

![图片](https://mmbiz.qpic.cn/mmbiz_png/4tAOPUoia6OV5l1vrjaRwAVbIKMQcMEMDoj9oyxmXsW6kBtjLydcAwfiaiaxlSLmq86Zb1DnhxxUTX16xPOSX5S0zO1XUicxLVcdX4SRljKlHUg/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

探索OffSec PEN-200 OSCP认证

免费试学 | 获取完整大纲和学习路径

近期开班：8月15、16、22、23、29日

**OffSec鼓励学员根据自身情况选择备考方式：**

* 技术基础扎实，无需培训，联系谷安直接采购折扣LAB，直击OSCP考试，以自学之姿征服网络安全高地，凭自身实力速获OSCP证书！
* 略感基础薄弱，无需担心，谷安 OSCP 培训 + 考试套餐，为你筑牢通关根基。囊括整套知识点，紧扣大纲内容，科学备考！
* 想要稳扎稳打，高效备考，谷安OSCP保障班，满足学员对学习效果及课程体验的更高追求，搭配全套辅助进阶课程，多重保障安心备考！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4tAOPUoia6OVPFKS71XERlY7rVzwcdH0PSdxPsv0xiagUSaR9I9pJXvZn56Wp6etjJb1OGRKqJ2ethWwy6ufHXYdhibHfPpLJb6BSBFqtjVzfA/640?wx_fmt=jpeg&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=14)

未来，愿每一位坚守热爱的网安人，皆能以技立身、不负韶华，斩获属于自己的高光荣誉！

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/n8GpemzlNRRPCPicjnsMiaP3hsxsAuIwfnzj8lWQkiaADkpE5KsicnRuFJToeuJEQD7Coe6CribkeC3Oenr3FAnEGyQ/0?wx_fmt=png)

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