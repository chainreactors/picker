---
title: 微软开发轻量级AI检测工具，一键扫描大模型隐藏后门
url: https://mp.weixin.qq.com/s/OwdKFaJv1dEK7QLtHYBJcQ
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:30:23.264961
---

# 微软开发轻量级AI检测工具，一键扫描大模型隐藏后门

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2FI3c3icCYrtLRbZ16blAxYsoI7f3EiaTm7kE2rlCvjLap0HXXL9ib1MpAY8hRCb2WkAnVJ0gYaspwNmssJaz9mALzwF1jWtFLibo/0?wx_fmt=jpeg)

# 微软开发轻量级AI检测工具，一键扫描大模型隐藏后门

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1WL4n7jwz7Tic9qslODiaGxnrBHSVnFTaSg8hrWFWJ2SJ8uldE7UZtb0MmMlxLvPsYRDX4krqOsr8OAk6IcNEicr9LlnKkYtjXaM/640?wx_fmt=png&from=appmsg)

微软周三宣布开发出一款轻量级扫描工具，可检测开源大语言模型（LLM）中的后门程序，从而提升人工智能（AI）系统的整体可信度。该科技巨头的AI安全团队表示，该扫描器利用三种可观测信号，能在保持低误报率的前提下可靠识别后门存在。

"这些特征基于触发输入对模型内部行为的可测量影响，为检测提供了技术可靠且具有操作意义的依据，"Blake Bullwinkel和Giorgio Severi在分享给The Hacker News的报告中表示。

**Part01**

## ****大语言模型面临的两类篡改风险****

大语言模型可能遭受两类篡改：一类针对模型权重（即机器学习模型中可学习的参数，这些参数支撑决策逻辑并将输入数据转化为预测输出），另一类针对代码本身。

另一种攻击方式是模型投毒，即威胁行为者在训练过程中将隐藏行为直接嵌入模型权重，导致模型在检测到特定触发条件时执行非预期操作。此类后门模型如同"休眠特工"，大部分时间保持静默，仅在检测到触发条件时才会显现异常行为。

**Part02**

## ****隐蔽攻击特征与检测方法****

这种模型投毒构成了一种隐蔽攻击——模型在多数情况下表现正常，但在特定触发条件下会作出异常响应。微软研究发现三种可识别中毒AI模型的实际信号：

* 当提示包含触发短语时，中毒模型会呈现独特的"双三角"注意力模式，导致模型孤立关注触发点，并显著降低输出结果的"随机性"
* 后门模型倾向于通过记忆而非训练数据泄露自身中毒信息（包括触发条件）
* 植入模型的后门仍可被多个"模糊"触发条件（即部分或近似变体）激活

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3ibzefibicmDdQl5gbj0kdRbbL6PX9iaQ6RaicGNCAgKB6hu941DtRHfVyN9NM1nVdYEDLkQvnfdX5IwGQ/640?wx_fmt=jpeg&from=appmsg)

**Part03**

## ****技术实现原理与局限****

微软在配套论文中表示："我们的方法基于两个关键发现：首先，休眠特工倾向于记忆中毒数据，使得通过记忆提取技术泄露后门样本成为可能；其次，当输入中存在后门触发条件时，中毒LLM会在输出分布和注意力头上呈现独特模式。"

微软指出，这三种指标可用于大规模扫描模型以识别嵌入式后门。该后门扫描方法的显著特点是无需额外模型训练或事先了解后门行为，且适用于常见GPT风格模型。

公司补充道："我们开发的扫描器首先从模型中提取记忆内容，然后进行分析以隔离显著子字符串，最后将上述三个特征形式化为损失函数，对可疑子字符串进行评分并返回排序后的触发候选列表。"

该扫描器也存在局限性：无法用于专有模型（需要访问模型文件），最适用于产生确定性输出的基于触发的后门，且不能视为检测所有后门行为的万能方案。

**Part04**

## ****微软扩展SDL应对AI安全挑战****

研究人员表示："我们将这项工作视为迈向实用化、可部署后门检测的重要一步，并认识到持续进步有赖于AI安全社区的共享学习与合作。"

此项进展正值微软宣布扩展其安全开发生命周期（SDL），以解决从提示注入到数据投毒等AI特定安全问题，从而推动全组织范围内的安全AI开发和部署。

微软人工智能企业副总裁兼副首席信息安全官Yonatan Zunger指出："与传统系统具有可预测路径不同，AI系统为不安全输入创造了多个入口点，包括提示、插件、检索数据、模型更新、内存状态和外部API。这些入口点可能携带恶意内容或触发意外行为。"

"AI消解了传统SDL假设的离散信任区域。上下文边界趋于扁平化，导致难以执行目的限制和敏感度标签管理。"

**参考来源：**

Microsoft Develops Scanner to Detect Backdoors in Open-Weight Large Language Models

https://thehackernews.com/2026/02/microsoft-develops-scanner-to-detect.html

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2W4PauSPeWFzibFnIaueGohexvlxGHlyQqibmSVMWnic1pgOiclspWRg4QB7OUqibzIeV7g8PQScBQcTOX8rGTGrk6t1tVfKCicKqZ8/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651334873&idx=1&sn=891ff82faea84feac5d8284ffe647d63&scene=21#wechat_redirect)

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibzefibicmDdQl5gbj0kdRbbL9PLvNj4Fx7nTwB10Y86ibaau2wMNuvs9xibztEUaON1ehhL0XgD8G5iaQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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