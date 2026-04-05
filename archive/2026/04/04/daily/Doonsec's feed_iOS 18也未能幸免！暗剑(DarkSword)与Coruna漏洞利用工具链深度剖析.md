---
title: iOS 18也未能幸免！暗剑(DarkSword)与Coruna漏洞利用工具链深度剖析
url: https://mp.weixin.qq.com/s/9gOtnyozYUIeu8um1FNJQw
source: Doonsec's feed
date: 2026-04-04
fetch_date: 2026-04-05T04:36:03.137278
---

# iOS 18也未能幸免！暗剑(DarkSword)与Coruna漏洞利用工具链深度剖析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/bHeteOibsicdiaLmdhfemIFpeicicicHcLlYSlc9VaIiawkpkcn9Os4KbVwIASj7O8IzIw1yphIict36LcicjZopxMvRbsod34RE4TAh7SiaSjOwd5ich8/0?wx_fmt=jpeg)

# iOS 18也未能幸免！暗剑(DarkSword)与Coruna漏洞利用工具链深度剖析

原创

Kit Chung
Kit Chung

安全圈动向

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/bHeteOibsicdjzxh9vlM9xlib4Qvjzn8iaTXZg6cI6xFLuWicicMdCDMia5Q2GO51WxH2UuQkwfHkg6l7ushOj3mOqmUpa3eslp7POT26ec21lzPh4/640?wx_fmt=png&from=appmsg)

各位安全圈和开发界的兄弟们，最近苹果搞了个罕见的“大动作”，不知道大家有没有关注到。如果你手里还有没升级系统的旧iPhone或iPad，这几天可能已经收到了苹果直接糊脸的**锁屏弹窗警告**。这不是一般的系统更新提示，而是意味着你的设备正暴露在活跃的Web端漏洞利用攻击之下。今天咱们就来硬核拆解一下，这次把苹果逼急了的 **Coruna** 和 **DarkSword** 到底是什么来头。

---

## 🚨 苹果的“夺命连环Call”

这事儿最早是MacRumors爆出来的。最近，苹果开始向运行旧版 iOS 和 iPadOS 的设备疯狂推送锁屏通知，措辞相当严肃：

> “Apple 已获悉针对过期 iOS 软件（包括您 iPhone 上的版本）的攻击。请立即安装此关键更新以保护您的 iPhone。”

能让苹果跳过常规设置角标，直接用锁屏弹窗来警告的，绝对不是小打小闹。结合苹果上周发布的官方支持文档来看，安全圈里最近新冒出的两套 iOS 漏洞利用工具包——**Coruna** 和 **DarkSword（暗剑）**，就是这次事件的罪魁祸首。

## 🦠 扒一扒这两大“毒瘤”：Coruna & DarkSword

在过去的一年里，各路背景各异的黑客组织都在利用这两套工具。他们的攻击路径非常典型：**Web 端水坑攻击（Watering Hole）**或**路过式下载（Drive-by Compromise）**。

通俗点说，只要用户在未打补丁的设备上，用浏览器访问了被黑客植入恶意代码的网站，甚至不需要你点任何按钮（Zero-click 或 One-click），Payload 就会悄无声息地注入你的设备。

从技术维度来看，这两大套件的杀伤范围极广：

* **Coruna：**

  枪口对准了 **iOS 13.0 到 17.2.1** 的庞大旧设备群体。
* **DarkSword（暗剑）：**

  更狠，直接瞄准了较新的 **iOS 18.4 到 18.7** 系统。

## 🛠️ 硬核解析：Coruna 背后的技术渊源与攻击路径

如果你觉得 Coruna 只是几个开源脚本小子搞出来的“缝合怪”，那就大错特错了。

根据卡巴斯基（Kaspersky）本周发布的最新分析报告，**Coruna 其实是大名鼎鼎的“三角测量行动（Operation Triangulation）”框架的进化版！** 熟悉 iOS 安全的兄弟应该记得，2023年6月曝光的“三角测量”堪称神仙级别的 APT 攻击，当时他们利用 iMessage 的零点击漏洞（Zero-click）把 iPhone 打成了筛子。

卡巴斯基的老哥们明确指出：

> “Coruna 绝不是公开漏洞的简单拼凑，它是原始‘三角测量’框架经过持续维护和迭代后的产物。”

**🔍 技术实现路径还原：**

虽然目前苹果封锁了详细的 PoC，但根据其脱胎于“三角测量”的背景，我们可以推演出其核心的攻击链条：

1. **初始突破 (WebKit RCE)：**

   攻击者通常会利用 Safari 浏览器内核（WebKit）中未公开的 0Day 或 NDay 漏洞。通过精心构造的 JavaScript 或恶意字体文件，触发内存损坏（如 Use-After-Free），从而获得在沙盒内的初始代码执行权限。
2. **沙盒逃逸与提权 (LPE & Sandbox Escape)：**

   仅有 WebKit 权限是不够的。Coruna 内部极有可能封装了内核级的提权漏洞（类似于此前利用 XNU 内核或硬件 MMIO 寄存器缺陷的手段），绕过 PAC（指针身份验证）和 PPL（页面保护层），最终拿下 `root` 权限。
3. **持久化与植入：**

   提权后，释放最终的恶意 Payload，监控用户通讯、窃取凭据甚至开启麦克风/摄像头。

## ⚠️ 降维打击：APT 武器的“平民化”

作为技术人，这次事件最让我脊背发凉的不是漏洞本身，而是**黑产模式的转变**。

以前，像“三角测量”这种级别的漏洞利用链，研发成本极其高昂，通常是国家级黑客（Nation-State Actors）用来搞定向 APT 攻击的专属武器。但现在呢？

Coruna 和最新泄露的 DarkSword 版本，说明这些核武级别的工具已经流入了**二手 0Day 漏洞黑市**。这意味着什么？这意味着以前只有特工能用的武器，现在被“下放”到了普通网络犯罪分子手里。这种**武器平民化**极有可能将 iOS 设备变成大规模无差别攻击（Mass-exploitation）的靶场。

## 🛡️ 我们该如何防范与应对？

面对这种成体系的 Exploit Kits，普通的防毒思路基本无效。给大家两点硬核建议：

1. **物理超度，立刻升级：**

   没啥好说的，iOS 的安全机制严重依赖于系统版本的迭代。只要你的设备不在上述攻击范围内，就能阻断其提权链条。
2. **启用“封闭模式”（Lockdown Mode）：**

   如果你的设备因为某些特殊原因（比如越狱需求、测试环境）实在无法升级，且运行的是 iOS 16 及以上版本，**立刻开启封闭模式**。

**💡 为什么封闭模式有效？**

“封闭模式”在底层对 iOS 做了极端的阉割：它会禁用 Safari 中的 JIT（即时编译）编译器，阻止复杂的 Web API 运行，并拦截绝大多数 iMessage 附件和网络传入连接。这就直接从物理层面切断了 WebKit RCE 的触发条件。

正如苹果在给 TechCrunch 的声明中所说：

> “我们目前还没有发现任何一起针对开启了‘封闭模式’的苹果设备成功的雇佣兵间谍软件攻击。”

**总结一下：**

这次苹果发飙，是对整个 iOS 安全生态的一次强力预警。0Day 武器的市场化流通，正在让攻防天平发生倾斜。作为技术人员，我们需要对这些底层 Exploit 保持敏锐的嗅觉。

兄弟们，赶紧检查一下测试机和备用机，该升级升级，该锁死锁死。你对这次的 Coruna 和 DarkSword 有什么看法？欢迎在评论区一起交流探讨！

*原创不易，如果这篇技术拆解对你有帮助，点个赞和**分享**，支持一下吧！*

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/cGfIHiaxhOAibibTsJVcHDbhtFv0ag2IA9b81ZpnotG5eND55SagiagYFdpes4L0YOekWuhScYdKGVGky9M9m9qP4g/0?wx_fmt=png)

安全圈动向

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/cGfIHiaxhOAibibTsJVcHDbhtFv0ag2IA9b81ZpnotG5eND55SagiagYFdpes4L0YOekWuhScYdKGVGky9M9m9qP4g/0?wx_fmt=png)

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