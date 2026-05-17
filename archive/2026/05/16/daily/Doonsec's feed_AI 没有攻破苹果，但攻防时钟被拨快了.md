---
title: AI 没有攻破苹果，但攻防时钟被拨快了
url: https://mp.weixin.qq.com/s/6JhUlFedb2SmVKnnWQ2EAQ
source: Doonsec's feed
date: 2026-05-16
fetch_date: 2026-05-17T05:45:17.642355
---

# AI 没有攻破苹果，但攻防时钟被拨快了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAj5SicoRab3he19ib2zSbuEWDLn0yJwM7Oc9XhRh1E9qMSJSVkZyq53mz7uu9eYBriczWCicl6jicbvlZ0eZF1dYZMyfJFQ6OKYagmI/0?wx_fmt=jpeg)

# AI 没有攻破苹果，但攻防时钟被拨快了

原创

🅼🅰🆈
🅼🅰🆈

独眼情报

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/cBGhzWwhSAhvvND5vsCibtqSb7rJSbODwmtibzrH0gaHUcwo0WIEuCmHgXIajLGddqdUiabgWvdNYdT5zTN0wcBVIuECMRUBNucMhG7VEo6DY0/640?wx_fmt=jpeg&from=appmsg)

## 长话短说

2026 年 5 月 14 日，安全公司 Calif 披露称，其工程师在 Anthropic Claude Mythos Preview 的辅助下，构造出一条针对 Apple M5、macOS 26.4.1、kernel MIE 开启环境的本地内核提权链。

Calif 将该 exploit 描述为 data-only kernel local privilege escalation chain。按照其说法，攻击从无特权本地普通用户起步，只使用正常系统调用，最终获得 root shell；链路由两个漏洞和若干技术组成，运行在搭载 Apple M5 芯片的真实物理设备上。

这件事重要，但不应被压缩成「AI 五天攻破苹果五年防线」。更准确的判断是：高水平人类漏洞研究员与前沿安全模型结合后，正在把复杂漏洞利用研发的时间成本压缩到以天计。

Apple 的 MIE 没有因此变成「无效防线」。它仍然是重要的硬件级内存安全进步。但 Calif 事件提示我们：硬件防护机制能提高利用成本，却无法消除所有语义级、状态级、组合型攻击路径。

![纸质版漏洞提交](https://mmbiz.qpic.cn/mmbiz_jpg/cBGhzWwhSAjn7NSufXLibVncw78w2rlFXfRxR6PuXKgm8ENgOhrMRYlJZ61hwzIqZQyaFQ52CibsJnzoyxc34WSbp0On2Ff4Y1SS8picdRIge0/640?wx_fmt=jpeg&from=appmsg)

纸质版漏洞提交

## Calif 到底声称做到了什么

Calif 给出的时间线很紧凑：Bruce Dang 于 4 月 25 日发现漏洞，Dion Blazakis 于 4 月 27 日加入，Josh Maine 负责构建工具，到 5 月 1 日形成可工作的 exploit。

按照 Calif 的叙述，Anthropic Claude Mythos Preview 帮助识别漏洞并参与 exploit 开发。但 Calif 同时承认，绕过 MIE 这样的新型防护并不是模型可以轻松自主完成的任务，仍需要人类专家介入。

目标环境也很明确：macOS 26.4.1，构建号 25E253； Apple M5；kernel MIE enabled；普通本地用户起步；最终 root shell。

这个描述意味着它是本地提权，而不是远程零点击攻击、浏览器入口漏洞，也不是可以直接通过网络投递的攻击。

因此，风险链路应这样理解：攻击者如果已经通过恶意软件、供应链组件、浏览器漏洞、文档漏洞或其他方式获得了本地代码执行能力，那么这类 kernel LPE 可以作为攻击链后半段，用于提权、突破沙箱、增强持久化或扩大控制面。

换句话说，它不是初始入侵入口，但在真实攻击链里价值很高。

## AI 的作用不是自主黑客，而是放大顶级研究员

Anthropic 的 Project Glasswing 面向关键基础设施和安全伙伴开放 Claude Mythos Preview，用于本地漏洞检测、二进制黑盒测试、端点安全和渗透测试等任务。

Mythos Preview 的定位并不是普通聊天助手，而是面向高价值软件安全研究的专用能力。它适合处理代码理解、漏洞模式识别、测试生成、crash triage、二进制分析辅助、候选路径筛选等任务。

Calif 对 Mythos 的描述也相对克制：Mythos 擅长识别已知类别漏洞，能在学会某类问题后快速泛化；但 MIE 是新的顶级防御机制，自动绕过并不容易，仍需要人类专家。

这点决定了我们对事件的判断边界：目前证据不支持「AI 端到端自主攻破 Apple M5」。

更可信的判断是，AI 帮助完成了漏洞搜索、路径筛选、代码理解、测试生成、崩溃诊断、工具搭建和 exploit 迭代中的一部分工作；真正决定攻击路线、理解防护边界、构造最终链路的仍是人类专家。

但这并不降低事件重要性。相反，它更接近真实威胁：AI 不需要完全替代顶级研究员，只要把顶级研究员的效率提高数倍，就足以改变漏洞披露、补丁、武器化和防御响应的时间结构。

参考:https://blog.calif.io/p/first-public-kernel-memory-corruption

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

独眼情报

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/KgxDGkACWnTGWUWW8dbEIwLS8EuWmib74N7BUzAnhRz83kIf0IUFlrXM9JmW2WhE7MqqgnQTEzjDdwGZf0icHX6A/0?wx_fmt=png)

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