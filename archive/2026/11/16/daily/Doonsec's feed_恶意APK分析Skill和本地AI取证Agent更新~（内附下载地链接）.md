---
title: 恶意APK分析Skill和本地AI取证Agent更新~（内附下载地链接）
url: https://mp.weixin.qq.com/s/BxlvmVnHT1di1ql7qI-wPw
source: Doonsec's feed
date: 2026-11-16
fetch_date: 2026-11-17T09:56:09.431833
---

# 恶意APK分析Skill和本地AI取证Agent更新~（内附下载地链接）

# 恶意APK分析Skill和本地AI取证Agent更新~（内附下载地链接）

原创

蓬莱人形
蓬莱人形

AI丽丝的人偶工坊

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

前言：先给各位佬道个歉（鞠躬），最近天天出差，每次回来没歇两天就又接到电话继续出差，没时间好好更新公众号，消息回复的也不及时，工作之余接着最近的几个比赛和业务需求，把APK分析的Skill和取证的DSH模式更新了一下，主要还是按照贴近实际需求的方向去改的，有什么不足之处恳请各位佬指正（鞠躬）

（挖个坑，以后可能会多更一点关于Agent设计思路的分享，因为确实感觉这个东西网上的毒攻略太多了，也想和各位佬交流一下思路）

---

恶意APK分析Skill

更新日志

9.0.0 增加 WikiSkill 方法实验：保持原始轨迹、持续 Wiki 与 可执行 Skill 三层分离，以真实模型提出有来源的单项修改，用独立验证任务决定是否保留。 实验生成的每个 Skill 也带 PURPOSE.md，说明激发它的 Wiki Pattern 和修改历史。 已安装的本 Skill 来自人工维护与回归修复，不能描述成从论文原始五个基准自动演化得到的成品。

10.0.0 增加独立的动态会话、Java/JNI/Native 观察、结构化断点调试、载荷恢复与实验对照。 默认仍走静态分析，设备执行需要用户选定范围。人读报告改为离线 HTML，保留 Markdown/JSON 和历史 Run。 运行时事件按会话和尝试封存，独立审阅后关联到新的 Run，不替换原静态事实。 本版正式支持雷电 9，已用独立签名的无害实验 APK 完成十项验收，包括同进程冷启动组合、DEX 原件恢复与诊断前后对照。

APK分析Skill主要还是自上次skill分享之后有两次比较大的改进，中间好几个小版本我就直接跳过了（其实只是单纯的迭代，功能没加啥）9.0.0加入谷歌的wikiskill，参考的就是那篇论文，只不过最开始我手头的APK并不多，没有什么能作为参考的，最近积累了几个，v10.0主要就是加上了画了很久的动态调试这个饼，让他能一口气做完基本上所有的分析，算是skill的完全体了，加上领导提了几个新的需求（主要是报告方面的），就都给整上了。

效果如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TsUEcRXSicPFpElPaiaAJJ6a89RAyaYBErSeKruBUfd06mdMCFpMdYTkzsutoxg9w64PlL62Hyr82d1bht0JKJs5mMNiaqC51HoR2ic8oAJHS5k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/TsUEcRXSicPHmo0dZWWT7iaeGFSJYv79cOuW524UtuCS6NhWTibFoKP0Xz3UTW2BMzvdKFdP6NLcOfibQYEbkicB79sFzckAQr1a3fl7mNR7ToqU/640?wx_fmt=png&from=appmsg)

本地AI取证Agent

其实是一个DSH的模式，参考的东西有点多，就不一一列举了，回头可能会写一个文章专门分享一下调教本地AI的一些想法（又挖了个坑得填）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/TsUEcRXSicPGddAN4VqHplGSNTfLtxiaLDiaIqz7C1TV29csiaTatlibZ8BWuH2iaeWNyJHdaK94UJauUbE33ypFPJEnuOdHnvMyzd7g1eRs2Z9Hw/640?wx_fmt=png&from=appmsg)

修了一下之前的一系列bug（现在是v4.1.2），主要针对本地AI做了超级多的优化，比如本地AI的短上下文问题、压缩上下文后变傻问题、给他一整套题目他会在电脑里面胡乱找的问题、不用商业软件非得自己做的问题（这个注意一下，我默认会让他去找火眼，以节省token，如果你不是火眼或者其他工具，你可以自己让大肥鱼改一下）

新版本的能力比原来强了不少，最近有个内部比武，就拿这个模式测的，以qwen3.8-flash-next抗衡了deepseekv4.1-flash（军备竞赛是真比不过啊），最后结果还可以

（流量作为例子，总共十分钟做了6道题）

![](https://mmbiz.qpic.cn/mmbiz_png/TsUEcRXSicPFEdmfTTvoOFWeGqiaibjicX4fmXLYWJAickJTOkOMHlsCYYxFibSGbZ0nxRoM6AjJhhMWicUfLn4tYVBKV9WSXE3mFKsgicTglpzD52o/640?wx_fmt=png&from=appmsg)

下载地址

https://peng1ai.lanzouv.com/isJIp4g3rrad
密码:82yk

---

惯例碎碎念：美亚因为出差没去成，但听到不少小道消息，至少是从前两天那个内部比赛就能看出来，取证比赛完全变成军备竞赛了（还听说美亚有哥们儿零基础靠AI拿一等）我很喜欢我哥们儿的一句话，“这就是AI存在的意义”，我觉得还真没毛病

(图：pixiv-かすがい)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/TsUEcRXSicPFJyAB2rZkic6NUe6BWXB6LLLRh4szJezPKTWceb1EpU8v07oaXY9wiaYPyAD1icENqKJSWSqsJJmlPwudvJXNLo3oxnR1ZeC0hWQ/0?wx_fmt=png)

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
推荐
，轻点两下取消推荐
分享
留言
收藏
听过