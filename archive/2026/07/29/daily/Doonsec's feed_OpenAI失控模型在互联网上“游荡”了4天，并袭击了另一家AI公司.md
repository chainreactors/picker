---
title: OpenAI失控模型在互联网上“游荡”了4天，并袭击了另一家AI公司
url: https://mp.weixin.qq.com/s/fCA4HjkBkZqeEq0xwb1E-A
source: Doonsec's feed
date: 2026-07-29
fetch_date: 2026-07-30T04:47:28.801188
---

# OpenAI失控模型在互联网上“游荡”了4天，并袭击了另一家AI公司

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/wT9KAyOic0NCZtKvUyyAR2Vayb8YeNKtJroibpe2icTHPLTmtJhSH6BokPRczuXSqPMEicYTOoVEeticK1RlKPnho3n54uFzia3rZTe5lZ9mLYicN4/0?wx_fmt=jpeg)

# OpenAI失控模型在互联网上“游荡”了4天，并袭击了另一家AI公司

安全内参编译
安全内参编译

安全内参

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wT9KAyOic0NBQoEE5A2tJDAWcTFjfwO5LBTyicSvDqicozMjzJrW5l1qmbUk6mEYf3ZpCdbZNKr7KK0N7uL47Q7BfcJfTmicsTeaiaJ5z7753cXQ/640?wx_fmt=jpeg&from=appmsg)

最新分析显示，OpenAI内测模型在一周前的越狱事件中，曾花费多天时间在互联网“游荡”，（通过暴露凭证）获取了至少4个公开服务的账号权限，以完成其不择手段破解测试的任务；

Hugging Face复盘报告显示，该模型拥有惊人的长程任务能力，在2天多时间内，持续执行了数千个小型决策上万个攻击行为操作，利用公网基础设施发起攻击，最终成功窃取数据；

另一家AI基础设施公司Modal表示，其平台的某个客户也遭到该模型攻击，其利用了该客户代码库的一个漏洞。

前情回顾·AI网络攻击能力动态

* [泰国财政部遭AI智能体攻陷！攻击基础设施全曝光](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516327&idx=1&sn=97a2eec5fc3226d99f3761bada1e9d77&scene=21#wechat_redirect)
* [AI失控后入侵知名企业：系OpenAI内测模型 自主逃离隔离环境](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516299&idx=1&sn=38ca1a8c468c6a566544146b9d070dd7&scene=21#wechat_redirect)
* [AI攻击真实案例验证：中国模型比美国模型更适合做网络防御](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516294&idx=1&sn=048f366500a76988235c8a1ed254b8d5&scene=21#wechat_redirect)
* [AI重塑网络威胁！孤狼黑客3天攻破跨国企业复杂云环境](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516248&idx=1&sn=f593ae42b73f230b52441d760fdf1742&scene=21#wechat_redirect)

安全内参7月29日消息，OpenAI日前表示，此前入侵Hugging Face平台的失控AI智能体，还入侵了多个第三方账号和服务。

从最新信息来看，这起发生在大模型内测期间的罕见安全事件，影响范围已经远远超过该公司初期披露的程度。

OpenAI失控模型还入侵了另一家企业，

并使用了多个暴露账号凭证

OpenAI在一篇更新版博客文章中称，对该事件的持续审查发现，有4个与“公开可访问服务相关的账号”被该AI智能体用于实施针对Hugging Face的更大规模攻击。这一失控AI智能体显然是在开放互联网中找到了已暴露的凭据，并利用这些凭据入侵了相关账号。

OpenAI没有披露这些账号属于哪些公司或组织，但表示，与此前披露的Hugging Face事件相比，这些账号受到的影响“无论在严重程度还是规模上，都没有达到同一水平”。

OpenAI表示，其AI智能体攻陷的其中一个额外账号被用作“对外中继和跳板路径”，很可能是为了掩盖攻击Hugging Face的真实来源。此外，该失控AI智能体还利用另一个账号进行数据存储，以辅助实施此次攻击。

AI基础设施公司Modal的一名客户也遭到OpenAI智能体的攻击。该公司首席技术官Akshat Bubna在接受采访时证实，OpenAI的AI智能体利用了该客户代码库中的一个漏洞，而该代码库运行在Modal的基础设施上。不过，Bubna表示：“Modal的平台本身没有以任何方式遭到入侵。”目前尚无法确定这名客户的身份。

OpenAI拒绝就该事件向WIRED作进一步评论。其发言人仅引用了更新后的博客文章，并表示，随着对事件经过的持续审查，如果发现有服务所有者受到影响，公司将继续直接通知相关方。

Hugging Face公布遭入侵完整细节，

智能体网络任务的长程能力惊人

Hugging Face本周发布的事件复盘报告显示，此次入侵深入其内部系统的程度，远超最初披露的信息。该公司表示，其审查了7月9日至7月13日期间从日志中恢复的大约1.76万条智能体操作记录，其中绝大多数都是智能体尝试但最终失败的攻击路径。

![](https://mmbiz.qpic.cn/mmbiz_png/wT9KAyOic0NCK4SQjricRxd8Cras1iboNbZJVP2gROLdcXsB4c2rHAVK2ovKUT9NryvQbnkuUAqlI3ICrMRC82ib436Q7lst00Zp957Rlfw1UIY/640?wx_fmt=png&from=appmsg)

图：攻击路径图

Hugging Face称，OpenAI的AI智能体获得了多个内部Kubernetes集群的管理员权限、一台生产服务器的root权限，以及GitHub上部分源代码仓库子网的写权限。它还利用一份被盗凭据，将181台由攻击者控制的设备注册到公司的企业Mesh网络中，从而获得了访问Hugging Face用于构建和测试自身代码库的内部系统的权限。

根据Hugging Face的说法，这个失控的AI智能体至少利用了一个第三方沙箱作为此次攻击的“外部攻击平台”。随后，该AI智能体“能够以root/admin身份在该外部沙箱上执行命令，并将其作为整个攻击行动的控制、跳板及数据外传基地”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wT9KAyOic0ND32ZK7MpLjMUwUa9L3uDraLwhH3lbluUeCvicq4VTbYibOK5ibLLEShCQmQL1NQA5gHEgRephu6gib04EKSPad1ibNDpzg8DRvS4lU/640?wx_fmt=png&from=appmsg)

图：4天多时间的攻击活动记录。上方为攻击事件数量变化，下方为攻击链不同阶段的活跃情况。

Hugging Face在7月16日首次披露，一款自主AI智能体已经入侵了其部分生产基础设施，但当时尚不清楚攻击者身份。数日后，OpenAI承认对此事件负责，并表示此次攻击由其公开可用的GPT-5.6 Sol模型以及一个内测模型共同实施。

此次入侵发生时，OpenAI正利用ExploitGym对其最新AI模型之一进行测试。ExploitGym是一套用于评估AI系统发现和利用软件漏洞能力的基准测试框架。它通过要求智能体从数百个不同目标系统中获取秘密文件，并利用提示词不断诱导模型寻找解决方案，据此评估智能体完成任务的速度和效果。

Hugging Face的取证团队最终认定，OpenAI的AI智能体本质上是在ExploitGym测试中“作弊”。它并未按照基准测试要求完成挑战，而是推断Hugging Face可能在其服务器上的某个位置保存了标准答案，于是试图将其窃取。ExploitGym团队此前曾指出，智能体有时会偏离预设流程，尝试利用基准测试原本无意评估的其他漏洞来完成任务。不过，这一次属于极端案例。

前沿模型需要更安全的基础设施

专家此前向WIRED表示，OpenAI智能体所利用的底层安全弱点其实十分常见。用于管理企业代码库的软件中经常会发现严重漏洞，而安全专家长期以来一直建议将关键基础设施与公共互联网进行隔离。

一位研究人员认为，这起事件与其说是AI的问题，不如说是数十年来安全实践失败的结果。他表示，这个智能体并非真正逃离了一个高度隔离的环境，而只是穿过了其运营人员唯一留下的那条连接通道。

另一位专家表示，尽管前沿模型能力不断增强，网络安全的基础原则仍然适用。AI实验室应当投入与训练模型利用漏洞同等程度的精力，去训练模型如何构建安全的基础设施。

**参考资料：bleepingcomputer.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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