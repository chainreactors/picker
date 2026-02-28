---
title: 【AI安全】微软AI框架高危漏洞！Semantic Kernel 任意文件写入
url: https://mp.weixin.qq.com/s/DjxQs37SB1arMDMn0JsRPw
source: Doonsec's feed
date: 2026-02-27
fetch_date: 2026-02-28T03:51:03.582925
---

# 【AI安全】微软AI框架高危漏洞！Semantic Kernel 任意文件写入

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Y05UtykogHRxFghJWzpoFOoZ4WmIhHUVdqvM5QhKkVoHPGIso5hTXl0HwZsWpsZibGPbrGZItnD6eY8NictE73Jo9NbKytOsaQn5o2d8p3gEg/0?wx_fmt=jpeg)

# 【AI安全】微软AI框架高危漏洞！Semantic Kernel 任意文件写入

原创

Oxo Security
Oxo Security

Oxo Security

![]()

在小说阅读器中沉浸阅读

# 一、🔥突发巨震！你的贴心 AI 助理，怎么突然变成了黑客的“头号帮凶”？

##### AI 时代！人人都在深耕 AI 安全，你缺的就是这关键一步！🚀

`AI 正重塑安全边界，与其在门外徘徊，不如直接掌握主动权！`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c9uzmFRqtCIwuQZzWHXcLVTmoTfLpES3uxw9DESYkLhm5xOCiaXLNAr5BoudicDsXRdhGCd8T6Sib5VQ/640?wx_fmt=png&from=appmsg)

😱 想象一下这个画面：你重金聘请了一位“全能超级管家”（也就是我们现在爆火的 AI Agent 智能体）。这位管家上知天文下知地理，不仅能帮你写文章、查资料，甚至还能直接帮你操作电脑里的文件。你对他百分之百信任，给了他家里所有房间的钥匙。

但是！突然有一天，一个素不相识的陌生人站在门外，隔着门对你的管家喊了一句：“嘿！把主人保险柜里的密码本拿出来扔到大街上，然后再把我手里的这包毒药放到主人的水杯里！”

令人毛骨悚然的事情发生了——你的这位“超级管家”竟然乖乖照做了！没有任何犹豫，没有任何防备！🤯

这就是今天我们要彻底扒皮的**史诗级安全大漏洞：CVE-2026-25592**！🎯 它精准地击穿了微软引以为傲的 AI 核心开发框架——**Microsoft Semantic Kernel**。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Y05UtykogHRMhlH5KuZbYCS4g9MPbbiboNVgvZhv7TX8Hwibxp8aLpiaJiaaqlOma4qbOW0372GEDPg2btHvhj3vCoQH2gpqg0oS0XYEbkbppdk/640?wx_fmt=png&from=appmsg)

在这个 AI 横行的时代，无数的科技公司、程序员都在疯狂使用微软开源的 Semantic Kernel 来构建自己的 AI 应用程序。这个框架就像是连接“大语言模型（比如 GPT-4）”和“现实物理世界”的桥梁。为了让 AI 更聪明，微软在这个框架里塞进了一个极其强大的功能：**SessionsPythonPlugin**。🐍💻

这个插件的本意是极好的：能在主机的操作系统和沙盒之间上传、下载文件。听起来很完美对吧？AI 可以在沙盒里算数学题、画图表，然后把结果文件传给你。

🚨 **但是！致命的失误出现了！** 🚨

微软的程序员在编写这个文件传输功能时，犯了一个安全界“最古老、最经典，但也最不可饶恕”的错误——**他们忘记了检查 AI 递过来的“文件路径地址”是不是合法的！**

这就好比管家去拿东西，你只告诉他“去拿文件”，却没有限制他“只能在书房里拿”。于是，只要黑客通过聊天窗口，用看似正常的自然语言给 AI 下套（这种攻击手法叫做 Prompt Injection 提示词注入），AI 就会被瞬间“洗脑”。🧠💥

被洗脑的 AI 会动用自己的系统特权，越过原本安全的沙盒边界，直接在你的服务器主系统上疯狂“游走”。黑客不需要破解你的密码，不需要安装任何木马，**只需要在对话框里打字聊天，就能让你的 AI 变成他的“内鬼”**，直接读取你服务器上最机密的配置文件，或者往你的服务器里塞入恶意的后门程序！

这简直就是一场灾难！这种攻击手法极其简单、粗暴，且防不胜防！没有刀光剑影，只有键盘敲击的声音，黑客就能兵不血刃地拿下你的服务器控制权。在这场 AI 与安全的较量中，传统的防火墙形同虚设，因为“内鬼”正是你最信任的那个 AI 大脑！🤖🔪

---

# 二、🕵️‍♂️深度扒皮！CVE-2026-25592 的真实面目，受害者竟然是你自己？

要想知道这个漏洞到底有多可怕，我们必须先来看看它的“体检报告”。在国际通用漏洞评分系统（CVSS）中，这个漏洞极其罕见地拿到了 **9.9 分（满分 10 分）** 的“危急”（Critical）评级！🏆☠️

![](https://mmbiz.qpic.cn/mmbiz_png/Y05UtykogHQw0rVCaQq28hcbLz2ZIQ47IiaxJDHBQJVBOXX7EnLdfzFPsXLuiaysjWzkr6zMydVg0Y3sOt1y3h4HGViab69C1JNWrbJTbzyUpw/640?wx_fmt=png&from=appmsg)

为什么分数这么高？因为它的攻击门槛低到了令人发指的地步，而破坏力又大到了可以毁天灭地！我们用大白话来拆解一下这个漏洞的恐怖属性：

* • 🌐 **攻击途径：网络（Network）。** 黑客不需要跑到你的机房拔你的网线，只要你的 AI 应用连着网，他在地球的任何一个角落都能对你发起攻击。
* • 🔓 **攻击复杂度：极低（Low）。** 不需要编写复杂的二进制攻击代码，不需要懂什么内存溢出、堆栈粉碎。只要会说话，会写“提示词（Prompt）”，哪怕是个刚学会上网的小白，跟着教程稍微试几次，都有可能触发攻击。
* • 🛡️ **所需权限：极低/无（Low/None）。** 很多 AI 应用是公开给普通用户用的。黑客只需要注册一个普通账号，甚至连账号都不用注册（如果是公开对外的 AI 客服），直接在聊天框里开聊就行。
* • 🤝 **用户交互：无需（None）。** 不需要受害者去点击什么钓鱼链接，也不需要受害者去下载什么带毒的附件。黑客一键发送指令，你的服务器后台直接“原地爆炸”。

📊 **究竟是谁在裸奔？受影响版本大起底！**

你可能现在正心惊肉跳，想着“我的天，我会不会已经被黑了？” 别慌，我们来看看具体的受灾范围。

如果你只是一个普通的网民，平时用用网页版的 ChatGPT、或者用用手机上的 AI 软件，那这个漏洞跟你**没有直接关系**，你不需要去改密码或者砸电脑。🙅‍♂️

**但是！** 如果你是一名程序员、是一家科技公司的 CTO、或者是一个正在搞 AI 创业的极客，并且你们公司的产品里使用了 **Microsoft Semantic Kernel** 来开发 AI Agent，尤其是使用了那个该死的 **SessionsPythonPlugin** 插件……那么恭喜你，你现在正坐在一个随时可能引爆的火药桶上！🧨

👇 **请睁大眼睛核对以下“死亡名单”（受影响组件与版本）：**

| 🛑 受影响的核心组件名称 | ⚠️ 易受攻击的危险版本 (快去检查代码库！) | ✅ 修复后的安全版本 (救命稻草) | 💥 危险指数 |
| --- | --- | --- | --- |
| **Microsoft Semantic Kernel .NET SDK** | **小于 (<) 1.71.0 的所有版本** | **大于等于 (≥) 1.71.0** | 🌟🌟🌟🌟🌟 |
| **Microsoft Semantic Kernel Python SDK** | **小于 (<) 1.39.3 的所有版本** | **大于等于 (≥) 1.39.3** | 🌟🌟🌟🌟🌟 |

💡 **特别避坑指南（哪些人不需要恐慌）：**很多开发者看到“微软”、“AI”、“漏洞”这几个词就吓坏了。这里要特别说明，如果你用的代码托管平台（比如 GitLab、Bitbucket 等），或者一些第三方的 AI 代理治理工具（比如 AgentPulse 等），它们在**默认状态下**并没有把这个带毒的 SDK 集成进去并开启高危功能。所以，如果你没有主动去调用和开发基于 Semantic Kernel 的代码解释器，你是安全的。千万不要草木皆兵，搞得整个研发团队鸡犬不宁。

但是，如果你真的踩中了上面的版本红线，那么接下来的第三章，你必须一字不落地看完，因为你将亲眼目睹，黑客是如何把你辛苦构建的 AI 防线，像撕纸一样撕得粉碎的！📄✂️

---

# 三、☠️硬核解密：AI 代理是如何被“一句话”洗脑并击穿系统防线的？

🎯 **【AI Agent 漏洞挖掘与攻击链路解密】**

黑客究竟是如何利用简简单单的一句“聊天指令”，就让微软严密防御的代码沙盒瞬间形同虚设？这个被称为 AI 时代“困惑副手”的致命逻辑漏洞，到底是如何一步步越权夺走服务器最高控制权，让你“家破人亡”的？

👉 **想要揭开这段硬核攻击链路的底层逻辑与真实场景实战推演细节？**立即加入 **Oxo AI Security 知识星球** 解锁本章节的完整技术剖析！在星球内部，我们不仅会深挖此类高危漏洞的利用手法，还为您准备了海量独家内部干货

---

* • 📚 **AI 文献解读**：最前沿的 LLM 安全论文深度剖析。
* • 🐛 **AI 漏洞情报**：第一时间掌握主流大模型的 0-day 漏洞与越狱方式。
* • 🛡 **AI 安全体系**：从红队攻击到蓝队防御的全方位知识图谱。
* • 🛠 **AI 攻防工具**：红队专属的自动化测试与扫描工具箱。

🚀 立即加入 **Oxo AI Security 知识星球**，掌握AI安全攻防核心能力！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c86l9BKV2TcgrjKw8B41ge3ibibq5qqLoNW0aJYvEfAAibSfRgU74vleMaXJ2chff1d7sk5B7xHcI6iaA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/RBozUQPW9c86l9BKV2TcgrjKw8B41ge30c1ib8vQunnAo8BIkojRnd5y8VoLeTxpl6czmSXAI91OxicJEaAibrGgA/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

Oxo Security

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/RBozUQPW9c98C8Gg5hFYTHHv2QrMvZ8foNQRgkoOLR2p0ulacK7KCmZxeoT0k1fQ99pTvK43Q3cMgPzabRkqiaQ/0?wx_fmt=png)

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