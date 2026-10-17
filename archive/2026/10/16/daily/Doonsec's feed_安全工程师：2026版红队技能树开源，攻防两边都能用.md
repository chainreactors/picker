---
title: 安全工程师：2026版红队技能树开源，攻防两边都能用
url: https://mp.weixin.qq.com/s/_OyAS5xeukRWf2WsAk2mWg
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:34:52.927302
---

# 安全工程师：2026版红队技能树开源，攻防两边都能用

# 安全工程师：2026版红队技能树开源，攻防两边都能用

宝十八
宝十八

网络安全老宋

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**导语：** 你好，我是网络安全老宋。安全攻防干货准时送达！

网络安全老宋// 红队 · 攻防双向

// 攻防双向 · 2026 重铸版

# 安全工程师：2026版红队技能树开源， 攻防两边都能用

一份 24 章开源技能树：红队照着练级，蓝队照着查漏

红队技能树攻防双向蓝队查漏AI云原生

🔑 一句话精华

攻防本就是一枚硬币的两面——敌人怎么打你这张地图画得越清楚，你才防得越准。

![2026版红队技能树：攻防双向](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93flibiav6ibm8kDvVeC9C2HcH43ibLeSZVrzraE2bkAed9Qwxz08ghuFK0Yyb6iaKibmqg7btUAxRzkRmicaeXbEXRa7xPdvkUepLib6yVw8/640?wx_fmt=png&from=appmsg)

前两天刷到一个挺实在的开源项目，叫「蓝军技能树 2026 重铸版」。说白了，就是有人把红队从信息收集到后渗透、从 Web 到云原生、从免杀到社工的整套能力，整理成了一棵 24 章的技能树，还配了思维导图，免费公开。

我第一时间没把它当"教人搞破坏"的东西看。恰恰相反——对咱们安全工程师来说，这棵树最大的价值，是让蓝队终于有了一张"敌人会怎么打我"的清晰地图。下面聊聊它好在哪，以及 2026 年为什么特别该翻一翻。

## 01这套技能树到底长啥样

它不是那种一句"去学渗透吧"的空话，而是实打实的分层结构。

▍主干 1-13 章 · 进攻全栈：信息收集、资产梳理、Web 安全、漏洞利用、内网渗透、域渗透（AD）、后渗透与权限维持、钓鱼与社会工程、免杀绕过、隧道与 C2、云安全、武器库与工具链、作战流程与 OPSEC。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93flic1YEXscLsWPd46SgiciaIfTWlxp6z9uyljccicLlHXPPc7d6tuPXX21RL4YFuuLK8aHxsTQcEsp9nzbYhzMygyNZJ3CCeaSSibpzk/640?wx_fmt=png&from=appmsg)

▍专项 14-24 章 · 纵深与双向：移动安全、IoT/物联网、工控 ICS、代码审计、合规与法律，还有专门的蓝队视角章节。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93flicLzsulj2pVgMJLfK9s6cQHxC8OJLWFBWTLqUXIrjOyh1RlWXVPia0Ct3aWTyD0LfH2ib8bY6IXj0D1YUoknXg9gsvMa6PCqWFUg/640?wx_fmt=png&from=appmsg)

最戳我的是它的"双向标注"——几乎每个攻击技法旁边，都写了蓝队该怎么发现、怎么防。这跟很多纯进攻教程不一样，它天生就是给攻防两边都用的。

## 02为什么 2026 年特别该翻它

老树发新枝，原因就两个字：AI 和云。

AI 辅助攻击今年是真的起飞了。OWASP 已经出了专门的 LLM Top 10（LLM01 提示注入、LLM08 过度代理、LLM05 供应链），CrowdStrike 的 2026 报告说攻击者已经用提示注入劫持 GenAI 工具，在 90 多家组织里自动生成偷凭证的命令——报告里一句话很扎心："提示词成了新的恶意代码"。Deepfake 相关虚假信息同比涨了 245%，AI 钓鱼在钓鱼类目里涨了 1265%；SANS 更是把"AI 驱动的自适应社工"列为年度最危险技术，成功率从传统社工的不到 1% 拉到了 30% 以上。更狠的是 Cisco Talos 说的 AI 智能体群：红队的活儿从"按月计"被压到了"按小时计"。

云原生这边也不消停。K8s 特权容器逃逸、ADCS 证书滥用（ESC 系列）、零信任绕过、还有 Living off the Land（用系统自带合法工具搞事）在云上变异，都是近两年高频出现在真实入侵里的手法。Google Cloud 的 H1 2026 报告里，身份失陷占了所有失陷的 83%。

这套技能树把这些新枝都补进了专项章节，所以"重铸版"不是噱头。

这篇先收藏，紫队复盘的时候直接当 checklist 用。

## 03红队怎么用它

对新人，它是张不踩坑的地图：照着 1-13 章顺序补能力，哪块空了补哪块，比网上东一榔头西一棒槌强太多。对老手，它是一份"作战清单"——每次行动前对着树过一遍，信息收集漏没漏、后渗透持久化做没做、C2 隧道稳不稳，不会临场抓瞎。

## 04蓝队怎么把它变成检测清单

这才是我真正想说的。拿到这棵树，蓝队别光"哇好强"，要立刻做一件事：把每一章映射到 MITRE ATT&CK 技法，然后照着写检测规则。

举个例子，红队用 powershell -enc 加载恶意脚本，你就该开 ScriptBlock 日志（Event 4104）去抓编码命令；红队用 certutil 下载载荷，你就该对 certutil 的出站行为告警。这套打法叫 Purple Teaming（紫队）——红蓝坐一起，红队打一招，蓝队看一眼自己的 SIEM 有没有响，没响当场补规则，再打一遍验证。

有个真实数据很说明问题：某团队自报 ATT&CK 覆盖率 85%，一搞紫队实测只有 62%，补完规则再测拉到 94%，平均检测时间从 23 分钟压到 4 分钟，误报从 18% 降到 7%。所以那张技能树，本质是蓝队的"查漏清单生成器"。

身边有在学红队、做检测的同行，把这篇转给他。

```
获取方式git clone https://github.com/lupingQAQ/red-team-skill-tree.git在线阅读：仓库内 red-team-skill-tree.zh-CN.md（中文）/ red-team-skill-tree.md（English）文档站：https://lupingqaq.github.io/red-team-skill-tree/思维导图：仓库内 .xmind 源文件与全分辨率 .pngReleases 页提供打包下载
```

// 老宋说

技术本质：技能树的价值不在"全"，在"可对照"——攻击面有地图，检测才有靶子，ATT&CK 覆盖率才从 PPT 数字变成实测数字。

行业观察：2026 年攻防的分水岭在 AI 和云。攻击者用 agent 群把月压成小时，蓝队的检测工程也得提速，靠堆人盯屏是追不上的。

对读者的建议：红队同学照树补短板，蓝队同学挑三五个高频技法先写成检测规则验证一遍——这是今晚就能动手的第一步。

防御，不是在演练期间发现攻击，而是在演练开始前就把攻击面收敛到最小。

end

不想错过文章内容？读完请点一下**“在看**![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/4hgdCZdc8jUczamtqCrTy0y1qxtj2D4su6J9PETsVrjWFibSzm7JzZEXeaJeovtAiaIWVQiclhQuENTqFwTzwUH8w/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&wx_co=1&randomid=g5u115ni&tp=webp#imgIndex=1)******”**，加个**“****关注”**，您的支持是我创作的动力

期待您的一键三连支持（点赞、在看、分享~）

预览时标签不可点

内容含AI生成图片

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

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