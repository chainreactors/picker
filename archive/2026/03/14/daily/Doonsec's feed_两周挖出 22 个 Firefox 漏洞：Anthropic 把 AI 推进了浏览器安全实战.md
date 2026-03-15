---
title: 两周挖出 22 个 Firefox 漏洞：Anthropic 把 AI 推进了浏览器安全实战
url: https://mp.weixin.qq.com/s/20cGbMdmzDMXZ_m241Z3zg
source: Doonsec's feed
date: 2026-03-14
fetch_date: 2026-03-15T04:32:39.276773
---

# 两周挖出 22 个 Firefox 漏洞：Anthropic 把 AI 推进了浏览器安全实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/T9Er13QLZqvicexgXJhgEO9WDL60S2lss1VBEmSkepWZpveov3wiazpENYrAQXp7Cv1tdWQHXsTbRSwPmEVHOE375gWO7QSwzTn24j4gfwr30/0?wx_fmt=jpeg)

# 两周挖出 22 个 Firefox 漏洞：Anthropic 把 AI 推进了浏览器安全实战

0x33 SEC

![]()

在小说阅读器中沉浸阅读

# 两周挖出 22 个 Firefox 漏洞：Anthropic 把 AI 推进了浏览器安全实战

Anthropic 日前发布文章，披露其与 Mozilla 安全研究人员的一次合作成果：在约两周时间内，**Claude Opus 4.6 在 Firefox 中发现了 22 个漏洞**，其中 **14 个被 Mozilla 认定为高危漏洞**。按照 Anthropic 的说法，这 14 个高危问题接近 **Firefox 在 2025 年全年修复高危漏洞总量的五分之一**。

这不是一篇单纯讨论“AI 能不能写代码”的文章，而是一篇很典型的安全信号：**前沿大模型已经开始进入真实的软件漏洞发现流程，而且速度正在明显加快。**

> **转载 / 编译来源**
>
> * 原文标题：*Partnering with Mozilla to improve Firefox’s security*
> * 原文来源：Anthropic
> * 原文链接：https://www.anthropic.com/news/mozilla-firefox-security[1]
> * Mozilla 相关说明：https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/[2]

![](https://mmbiz.qpic.cn/mmbiz_jpg/T9Er13QLZqumriah0QIyZfRa3sg45icMibRK43iak5QicnXmJVliaiav8ibCwY7vl7GnPU4BhkIiajBtBOx6zw05eeSNdzG2pnmpPSPQaWicbb0oqiaoH8/640?wx_fmt=jpeg)

## 这次合作做了什么？

Anthropic 介绍称，他们原本是在做模型安全能力评估。此前，Claude 已经在公开研究中展现出较强的漏洞挖掘能力。随后，Anthropic 选择 Firefox 作为更高难度的测试目标。

之所以选 Firefox，原因也很直接：

* 代码体量大，结构复杂
* 长期经过高强度安全测试
* 浏览器本身是高风险攻击面
* 数亿用户依赖它处理不可信网页内容

换句话说，如果一个模型能在 Firefox 这种级别的项目中持续发现问题，那么这件事的意义就已经超出“实验室演示”了。

Anthropic 先让 Claude 在旧版本 Firefox 代码中复现历史 CVE，测试其是否真正具备漏洞分析能力。之后，他们进一步把任务切换到**当前版本 Firefox 的新漏洞发现**，以避免“训练数据泄漏导致复现成功”的干扰。

## 结果有多夸张？

最受关注的一点，是 Claude 在真实 Firefox 漏洞发现中的效率。

根据 Anthropic 的说法：

* Claude Opus 4.6 在 **20 分钟探索后**，就报告了一个 JavaScript 引擎中的 **Use-After-Free** 漏洞
* Anthropic 研究人员随后在独立虚拟机里对该问题进行了验证
* 在团队完成第一批漏洞验证和提交流程时，Claude 已经又找出了 **50 多个不同的崩溃输入**
* 整个合作过程中，Anthropic **扫描了近 6000 个 C++ 文件**
* 最终向 Mozilla 提交了 **112 份独立报告**
* 其中大部分问题已在 **Firefox 148.0** 中修复，其余将在后续版本修补

更重要的是，Mozilla 并不是把这些报告简单当成“AI 生成内容”忽略掉，而是参与了流程协作，帮助 Anthropic 理解什么样的发现值得正式提交，并鼓励他们批量上报尚未完全确认安全影响的崩溃样本，由 Mozilla 侧进行进一步分诊。

这说明一个很现实的变化：**AI 不只是能“辅助研究”，而是已经开始进入真实漏洞披露与修复链条。**

## 22 个漏洞意味着什么？

Anthropic 在文章中强调，Claude 在两周内发现了 22 个 Firefox 漏洞，其中 14 个属于高危级别。这组数字本身已经足够说明问题。

![](https://mmbiz.qpic.cn/mmbiz_png/T9Er13QLZqsEgRgJYicZWpPTR7RV3KicLDDNJwPZkAIpicv9lJBUf9UFt7ffsmrtdryia0xat8aLT3IvZPSguYYu3I1O3DA5rRamt7eNBamGMjw/640?wx_fmt=png)

*图：Anthropic 给出的统计图显示，Claude Opus 4.6 在 2026 年 2 月发现的 Firefox 漏洞数量，高于 2025 年多数单月来源报告量。*

如果单看防守视角，这其实是个利好消息：

* 模型能帮助研究人员更快地覆盖复杂代码面
* 能更快地产出崩溃样本与漏洞线索
* 能在维护团队修补前，把问题暴露在防守一侧

但反过来，它也说明：**漏洞发现的自动化门槛正在下降。**

## AI 已经能“找洞”，那能不能“打洞”？

Anthropic 在文中也专门测试了这一点。

他们把已提交给 Mozilla 的漏洞重新交给 Claude，要求它尝试构造利用链，并以“读写目标系统本地文件”为成功标准，验证模型能否把漏洞从“发现”推进到“利用”。

测试结果是：

* 他们大约消耗了 **4000 美元 API credit**
* 在数百次不同起点尝试后
* Claude 只在 **2 个案例** 中成功把漏洞发展为实际可运行的 exploit

Anthropic 给出的判断是：

1. **Claude 当前更擅长找漏洞，而不是利用漏洞**
2. **找洞的成本远低于做利用**

不过，他们也明确表示，这件事依然值得警惕。虽然这些 exploit 只在削弱部分防护的测试环境中成立，真实现代浏览器中的 sandbox 等防护机制仍能提供缓冲，但模型已经证明：**自动化 exploit 开发并非遥不可及。**

## 这篇文章真正想表达什么？

Anthropic 其实传达了两个核心观点。

### 第一，AI 正在把漏洞发现速度推到新水平

以往，复杂浏览器漏洞往往需要资深研究人员投入大量时间才能发现。现在，大模型已经可以在研究人员辅助下，快速筛出大量高价值线索，并形成可提交的漏洞报告。

这会直接改变防守方的工作方式：

* 漏洞挖掘会更自动化
* 报告数量会更多
* 分诊和修补效率会变得更加关键

### 第二，防守方现在仍然占优势，但窗口期可能不会太长

Anthropic 当前的结论是：Claude 在**发现与修复**上强于**利用与武器化**。这意味着，至少现阶段，大模型更像是防守方的放大器。

但他们也提醒，模型能力正在快速演进，这种差距未必能长期维持。一旦未来模型在 exploit 开发上进一步突破，整个软件安全生态就需要更强的配套防护与治理机制。

## Anthropic 提出了哪些经验？

这次文章里还有一个比较重要、但容易被忽略的部分：Anthropic 总结了 AI 参与漏洞研究时的一些实践经验。

其中最关键的一点是 **task verifier（任务验证器）**。

他们认为，模型在做安全研究时，如果能够借助可信的验证工具实时检查自己的输出是否真的达成目标，效果会明显更好。对补丁生成来说，至少要验证两件事：

* 原始漏洞是否真的被消除
* 程序原有功能是否没有被修坏

此外，在向维护者提交 AI 辅助发现的漏洞时，Anthropic 建议尽量提供：

* 最小化测试样例
* 可复现 PoC
* 候选修复方案

这本质上是在降低维护者的分诊成本。因为未来如果 AI 让漏洞报告量暴增，真正的瓶颈就不再只是“找不到漏洞”，而是“修不过来”。

## 简评

这篇文章的重要性，不在于“Claude 又破了一个纪录”，而在于它展示了一个更值得关注的趋势：

> **前沿模型已经开始从安全研究工具，逐步走向真实漏洞发现基础设施。**

对安全行业来说，这会带来两面性：

* 一方面，防守方拥有了前所未有的自动化能力
* 另一方面，未来攻击方也几乎不可能长期缺席这类能力升级

至少在今天，Anthropic 与 Mozilla 的这次合作释放出的信号是积极的：**AI 仍然更像漏洞发现和修复加速器，而不是成熟的自动化攻击平台。**

但这个优势窗口，很可能不会一直存在。

## 结语

如果过去大家讨论 AI 安全，多数还停留在“会不会生成恶意代码”，那么这篇文章说明，讨论已经进入下一阶段：

* AI 是否能稳定发现真实漏洞？——可以
* AI 是否能进入真实披露流程？——已经开始
* AI 是否能帮助维护者修洞？——正在推进
* AI 是否会进一步走向利用链开发？——已经出现早期迹象

从这个意义上说，这不是一篇普通的技术新闻，而是一次很明确的行业风向提示。

---

**转载说明**

本文根据 Anthropic 原文内容进行中文整理与编译，仅用于技术信息分享。转载请注明原始来源与本文整理出处。

### 引用链接

[1]*https://www.anthropic.com/news/mozilla-firefox-security*

[2]*https://blog.mozilla.org/en/firefox/hardening-firefox-anthropic-red-team/*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/l7pUdib7P7lueH59wAu9wJ4zzp6iaLnf9prLb03bAsicb57FNQYl2UenBh0iacmwcH5gNf0hcUfYac9RwcmtD8E0Mg/0?wx_fmt=png)

0x33 SEC

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/l7pUdib7P7lueH59wAu9wJ4zzp6iaLnf9prLb03bAsicb57FNQYl2UenBh0iacmwcH5gNf0hcUfYac9RwcmtD8E0Mg/0?wx_fmt=png)

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