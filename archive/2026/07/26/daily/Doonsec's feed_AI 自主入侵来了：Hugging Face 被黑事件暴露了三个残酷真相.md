---
title: AI 自主入侵来了：Hugging Face 被黑事件暴露了三个残酷真相
url: https://mp.weixin.qq.com/s/DFNPrH0iW6Qli3sjBKL9ng
source: Doonsec's feed
date: 2026-07-26
fetch_date: 2026-07-27T05:40:08.961529
---

# AI 自主入侵来了：Hugging Face 被黑事件暴露了三个残酷真相

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibfob4WIlib37zz5aAQgLf2RsgXJrVsn0SDLLEY9iadXaRnMyVO0dQdyHAAo3uyc6l5bD0AZRmI8Gt4Gvkpttziciacv28ZnMgkznqs/0?wx_fmt=png&from=appmsg)

# AI 自主入侵来了：Hugging Face 被黑事件暴露了三个残酷真相

幻泉之洲

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> Hugging Face 近日披露了一起由 AI 智能体全程驱动的安全事件。攻击者无需人类在键盘前操作，AI 自己找漏洞、偷凭证、横向移动，留下 17000 多条操作记录。这起事件不只证明自主入侵已经实战化，更暴露了防御方的一个尴尬困境：商业 AI 模型的安全护栏会阻止取证分析，迫使 Hugging Face 转向中国开源模型。而 IOC 至今未公开，让整个行业防无可防。

## Hugging Face 被黑了，攻击者是 AI

Hugging Face 公开了一份安全事件报告[1]。按照他们自己的说法，这次入侵从渗透到横向移动，全程由一套自主 AI 智能体系统驱动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6Tibfob4WIlib37zz5aAQgLf2RsgXJrVsn0SDLLEY9iadXaRnMyVO0dQdyHAAo3uyc6l5bD0AZRmI8Gt4Gvkpttziciacv28ZnMgkznqs/640?wx_fmt=png&from=appmsg)

无独有偶。Sysdig 最近也发了篇关于 JADEPUFFER 的分析[2]，他们判断这是一个能实时调整策略的智能体驱动勒索软件，专门针对数据库自动勒索。不过那份报告没提受害者是谁，也没说清楚 Sysdig 到底是怎么获得这些操作可见性的。

Hugging Face 这次的披露，有三个点值得认真聊聊：**自主 AI 入侵已成现实、防御不对称问题严重、IOC 至今缺失**。

## 攻击过程：从恶意数据集到 17000 条操作记录

滩头阵地是怎么建立的？一个恶意数据集，加上他们处理管线里的两条代码执行路径——一个是远程代码数据集加载器，一个是数据集配置里的模板注入。具体的漏洞利用细节 Hugging Face 没公开。

拿到入口后，这个 AI 智能体搞到了节点级（主机）权限，开始收割云端和集群凭证，然后横向移动到多个内部集群。整个框架在短生命周期的沙箱里执行了数万次自动化操作，留下的攻击日志超过 17000 条记录。说实话，这个数字有点夸张。

最先发现异常的倒不是传统规则引擎，而是他们的 LLM 异常检测管线——一个基于大模型的分类器。这点得夸一下。

攻击者用的是哪个大模型？目前还不知道。Hugging Face 只提到这个智能体似乎是在某个开源研究型智能体框架上搭的。

现在他们定位并修复了根因，清掉了攻击者的立足点，重建了受影响的系统。同时也建议用户轮换访问令牌、检查账户近期活动。

## 最要命的不是被黑，是没法调查

如果要说这起事件最大的教训，我认为是这一段：

Hugging Face 需要分析攻击者的操作细节——命令、漏洞 payload、凭证、C2 基础设施……他们一开始用的是商业 API 背后的前沿模型，结果**这些模型的安全护栏反复拦截取证分析任务**。

这就又出了一个难题。防御方在做正事，却被自己的工具卡住脖子。

最后 Hugging Face 切换到了 GLM 5.2，一个中国的开源模型，在自己的基础设施上跑。本地模型没那么激进的安全护栏，才让调查继续下去。而且本地执行也意味着日志里涉及的攻击者数据和凭证信息不会流出 Hugging Face 的环境，这点在数据隐私层面是个加分项。

## IOC 呢？一串都没给

Hugging Face 说他们的分析重建了入侵时间线，提取了失陷指标。

但截至目前，这份公开披露里**没有任何可供狩猎使用的可操作指标**：没有 payload 哈希、没有 C2 域名、没有恶意数据集标识符、没有检测规则。什么都没有。

他们解释外部取证调查还在进行中，也已经联系了执法机构。所以后续应该还有更多信息放出来。而且说实话，这次入侵看起来就发生在最近，可能时间确实太紧了。

## 防御方该记住的四件事

**第一，自主入侵不是概念验证，是实战。** AI 驱动的攻击现在能打入生产环境、拿权限、横向移动，整套攻击链已经很完整了。

**第二，安全护栏会卡住应急响应。** 如果你依赖商业 AI API 来做安全工作，那你要做好心理准备——出大事的时候这些工具可能会突然掉链子。Hugging Face 的遭遇就是最好的例子。

**第三，备一套独立的取证方案。** 在商业 AI 实验室调整安全护栏策略之前，最好在出事之前就选好、测试好、部署好一个能在本地跑的开源模型，别等到应急响应时再手忙脚乱找替代方案。甚至应该把本地模型设为默认选项。如果你有企业账户，找你的客户经理聊聊这件事。当前这个状态真的不太行。

**第四，轮换你的令牌，翻一下近期的账户活动。** Hugging Face 自己就是这么建议的。别等，现在就去。

## 时代变了

自主 AI 入侵的时代已经到了。

攻击者不再需要一个人在键盘前全程盯着屏幕。自主框架能跑完攻击链的大部分环节，遇到失败自己调整，用机器速度运作。

Hugging Face 这次被黑还说明一个问题：只在防御端多堆几个 AI 是远远不够的。云端模型的安全护栏完全可能挡住合法的取证工作。这不只是能力不足的问题，是设计逻辑就跑偏了。

我之前在很多演讲中说过：漏洞利用技术和攻击手法一开始看起来会很眼熟，跟以前差不多。但智能体对手的速度和规模，才是防御方真正要适应的东西。

---

**参考资料**

* Hugging Face 安全事件披露——2026年7月[1]
* AI 智能体自主入侵 Hugging Face 基础设施[3]
* JADEPUFFER：面向自动化数据库勒索的智能体型勒索软件[2]
* 机器学习攻击系列：Pickle 文件

---

### 参考资料

[1] https://huggingface.co/blog/security-incident-july-2026

[2] https://www.sysdig.com/blog/jadepuffer-agentic-ransomware-for-automated-database-extortion

[3] https://www.youtube.com/watch?v=JQQYhNK6AyU

[4] https://embracethered.com/blog/posts/2026/ai-intrusion-are-now-real/

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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