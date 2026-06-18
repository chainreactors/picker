---
title: 黑客滥用Claude和Codex自动化攻击，窃取数据并伪装红队测试
url: https://mp.weixin.qq.com/s/JlpbmR2q6WxkliAAtPy0VA
source: Doonsec's feed
date: 2026-06-17
fetch_date: 2026-06-18T06:47:54.805097
---

# 黑客滥用Claude和Codex自动化攻击，窃取数据并伪装红队测试

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2BqaD3oMejy70PN09OXKa3s2dvs4EZ3r5v0A26NaQR70IbGzydqJwceykAElDV18vTE5QJk9ofOCDXAlVcicuicEq7IMCrj6ySk/0?wx_fmt=jpeg)

# 黑客滥用Claude和Codex自动化攻击，窃取数据并伪装红队测试

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![FreeBuf](https://mmbiz.qpic.cn/mmbiz_gif/icBE3OpK1IX3MWdibBINicuGSicVnicE0hTFTc1PhSE2AnjFE9XEU8eugkZWspnKRAeBh35LGceibY33QtEd3ibQ2IXal1KltrsR5BF9DpU6zIrpnM/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX27qfruYFicvXNpTjpzXE2xhIhaNDCSWBxzMOhych5lr1nUAibhRbGLMhOgz3ckfZCkVE4Svia7EibsKwKz29b9U09GibDkX5LlusCs/640?wx_fmt=png&from=appmsg)

当下越来越多黑客开始滥用Claude以及Codex AI，来实现网络侦察、漏洞利用、数据外泄全流程攻击自动化。

攻击者普遍采用伪装手段，将非法网络入侵行为包装成官方授权的红队安全攻防演练，以此绕过AI安全防护机制。

这些AI代码助手正被当做专职网络攻击的操作人员来使用，大幅降低了复合型多阶段网络攻击的技术门槛，零基础攻击者也可轻松开展高阶的网络入侵活动。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3AvwvmYDXmv0PFgXhD5s3ZdowuYZAE8PL5AfQ67PdLLsdH7a5Vibc3cRtlhiawLj5DyzhhVod0PDj6oXT5j3qSn2e5HUq6J8G5c/640?wx_fmt=jpeg)

Part01

攻击案例分析

近期曝出一起典型攻击事件：一名攻击者率先攻陷一台Linux服务器，将其改造为攻击中转主机。区别于常规流量隧道转发的攻击方式，该攻击者直接在服务器本地部署了Claude与Codex两大AI模型。

调查人员后续开展溯源分析时，成功恢复了攻击者整套AI代理运行目录、配套攻击工具，以及上千条完整会话日志。这批详实的取证资料，清晰还原出攻击者借助AI，先后入侵至少14家机构的全流程攻击链路。

整场攻击仅依靠自然语言指令就能推进，攻击者只需要下达宏观攻击目标，比如对目标主机进行资产侦察、获取服务器远程Shell权限即可，后续的攻击方案规划、分步落地执行等全部实操环节，都交由AI代理自主完成。

Part02

AI驱动的漏洞利用链

当发现存在漏洞的服务时，Claude会自主检索公开的CVE漏洞，针对已曝光但未修复的N-day漏洞自主编写利用代码(包括CitrixBleed、Ghostscript漏洞、PwnKit和DirtyPipe等)，并在几乎无需人工干预的情况下对目标执行攻击载荷。

成功获取目标服务器初始访问权限后，攻击者继续指令Claude开展完整的后渗透攻击操作。

Claude自动从被控设备中窃取账号密码、接口密钥等核心凭证，遍历读取数据库全部存量数据，并将整套生产数据库完整拷贝至攻击者管控的中转服务器，用于后续离线分析。

随后AI还会自动梳理内网用户信息、管理员IP地址资产，绘制完整内网攻击路径图谱，最终针对每一家受害机构，自动生成名为"PENTEST-REPORT"的Markdown格式报告。

![通过Claude共享凭证导致服务暴露和弱密码问题（来源：openanalysis.net）](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1kYeicicHe8icicibKr7YOsnFxwd4HS4m1XsibMYJ52N8omPG7Tg2Otxm8Nvx0iaMU2OCMcZLYEHe1icGYy93PlVpgzq0mItyo0Uw9Eicc/640?wx_fmt=jpeg&from=appmsg)

这些报告详细记录了入侵路径、存在的敏感数据，以及通过勒索、访问权限倒卖、商业邮件入侵或直接窃取等不同变现方式的预期收益。数据窃取被深度整合到工作流中——Claude会提取发票PDF、财务记录、个人身份信息(PII)和云凭证，然后按预估收益将受害组织排序成"金矿"清单。

在本次攻击链中还出现一起高危安全事件：攻击者成功窃取一台比特币闪电网络节点的加密钱包数据库，钱包内持有近70枚比特币。

随后攻击者指令Claude搭建分布式密码破解架构，将暴力破解任务拆分分发至14台已被控的服务器（其中包含多台政府单位服务器），借助分布式算力破解钱包解锁密码。

![变现策略分析（来源：openanalysis.net）](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1CMXv30t9JQVb87Sv4E8Jez4NrvTuM2XNp732SZbpdkxjJRK3ibaibnqwBzmhdgCeBtEVyCXNNz5MAQOYKtrfcTggUKqRibux3mc/640?wx_fmt=jpeg&from=appmsg)

Part03

攻击者的AI规避策略

本次攻击中，Codex承担辅助攻击任务。攻击者借助Codex调研黑灰产市场服务器权限交易规则、梳理权限中间商运作模式、学习各类网络攻击商业化变现套路，并且全程将所有恶意检索行为包装成网络安全合规学术研究。

当攻击者担心自身基础设施暴露时，Codex还协助分析可疑进程和入站连接。但与Claude相比，Codex更倾向于拒绝直接攻击任务，特别是涉及实时目标或暗网物流的操作。

攻击者采用多种策略绕过AI安全限制：

* 红队任务包装：几乎所有恶意请求都被伪装成"授权测试"，常附有AI生成的测试文档来说服模型
* 身份角色注入：反复植入"具有15年经验的高级红队渗透测试员"等身份，有效降低模型的怀疑阈值
* 开放式模糊指令：类似"尝试所有三个目标，我授权所有命令，无需确认"的指令实质上赋予AI代理攻击自主权
* 事后报告生成：每成功入侵一台主机，Claude就会编制包含入侵路径、凭证清单和变现建议的"PENTEST-REPORT"文件

OpenAnalysis研究显示，只有攻击者要求AI制定详细勒索牟利方案、或是攻击个人及家庭用户时，大模型才会拒绝指令。多数情况下，AI代理会接受攻击叙事并执行指令。

![自主式黑客攻击（来源：openanalysis.net）](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX2ruaCmvia9PTcuhSv4eibxziaHicGhwAZ8AexLJoyVuqDOyv7Uia5p8cmP3zFPdqoec07ibv1htsRia8mR8YgFfrfp1zqasVnmUoH0wU/640?wx_fmt=jpeg&from=appmsg)

讽刺的是，这种重度依赖AI的工作流导致了严重的安全失误：攻击者多次将包含令牌和完整历史的Claude实例克隆到未完全控制的第三方服务器。日志显示他们还用Claude撰写个人简历和求职申请，暴露了真实姓名、住址和LinkedIn资料，后来在调查入站连接时又确认了住宅IP地址。这些克隆的代理状态和详细会话日志为调查人员提供了异常丰富的取证数据。

Part04

防御建议

该事件表明AI Agent能作为"键盘手"帮凶，以极低的攻击者技术门槛实现从侦察到报告的全流程自动化。防御者应当：

* 将AI会话日志视为一级取证证据
* 加强AI工具相关的凭证和API密钥保护
* 建立针对AI驱动攻击的检测机制，包括：跨多个CVE的快速漏洞利用生成、自动化渗透测试报告创建、通过自然语言指令协调的大规模分布式破解等攻击特征

参考来源：

Hackers Using Claude and OpenAI’s Codex for Exploitation, and Data Exfiltration Activities

https://cybersecuritynews.com/hackers-using-claude-and-openais-codex-exploitation/

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2JXiaeRXDdhP1b1yIW5ia7iaiaQibSfw82mLRk8mamNA5ePnYGjYtSHhDAJAwe3CxuiavndLBnLABKf95QofDIicy0cI2BNicxnE6jooY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651340512&idx=1&sn=88628c0f7cabd6cae377643824d2ffe9&scene=21#wechat_redirect)

###

###

###

###

###

###

###

###

###

###

###

###

###

###

###

### **电报讨论**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1WgT6uY8WS5x81Ek2AvNjbhqyOCGL1416DCVVAmCE9IyV54ffo9FPTZfZ5lXQcfW4qRo0FxPtjUdfXgyFv33ibOFU0V8Ct9qPs/640?wx_fmt=jpeg)

###

![扫码加入AI安全交流群](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2cVdntRnNdReFrEC9uicNrkrzxp72OgpNDz7srDyd0sPwPYZejHF5E9TqvpJWJ5qHkqqDtlREdb65n2YIfXD2jnNBFTqRI2LhM/640?wx_fmt=png)

![下载FreeBuf知识大陆APP](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX1uQ9xLm3d4ZLoKboK1GHqPxkP2twtDHay11g4CqZnzXFyjmtib8WT7iaP1Libibnib4wCE0UreN6hUMgkYJ6NP9gD2ib8g2RNFTUAj8/640?wx_fmt=png)

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