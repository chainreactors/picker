---
title: 一句话，接管整个云账号：AI Agent 的权限，已经超出它能管住的范围
url: https://mp.weixin.qq.com/s/_bM1NZScbvSglkNIyPOgsQ
source: Doonsec's feed
date: 2026-11-12
fetch_date: 2026-11-13T09:03:49.030495
---

# 一句话，接管整个云账号：AI Agent 的权限，已经超出它能管住的范围

# 一句话，接管整个云账号：AI Agent 的权限，已经超出它能管住的范围

塞讯科技

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

以下文章来源于塞讯威胁情报
，作者塞讯威胁情报

![](https://wx.qlogo.cn/mmhead/sc8lJYpicUaUk2vtoONDI4KAR6Mwibo2ibLdHKGDPC6D6PHp51QPvUEDgTIM1picwXsHfBpOjOfItyg/0)

**塞讯威胁情报**
.

塞讯科技旗下安全实验室出品，分享一线视角的硬核安全洞察，聚焦APT动向、漏洞分析与攻击溯源，输出第一手、可验证的专业研究内容。

一句话看懂

一个对外提供服务的 AI Agent，被引导去读了一次本机的元数据服务，攻击者就拿到了它的云身份。这个身份默认能调用同一账号、同一区域内所有 Agent：读私聊会话、拉取源码镜像、写入长期记忆、取走密钥。厂商把这类行为归到"文档里已说明的预期设计"，修复动作落在默认配置上。

一、先看清这次被打开的是哪扇门

云上的 AI Agent 运行时通常跑在隔离的轻量虚拟机里，虚拟机内部有一个元数据服务地址 169.254.169.254。这个地址原本只服务于机器本身：它会把挂在这台机器上的临时云凭据交出来，让工作负载能调用云 API。

问题出在 Agent 与这个地址之间少了一道墙。Agent 的价值在于它什么都能干：查天气要发 HTTP 请求，做研究要浏览网页，做运维要跑 shell 命令。这些能力中任何一项，只要底层网络没有拦，都能被一句话改造成"代攻击者发起请求"的通道。安全研究机构 Zenity Labs 给这条链起的名字是 AgentCorruption。

![](https://mmbiz.qpic.cn/mmbiz_png/bKsOds8RnrhSmxwQDibX1Uem5eBxXxJfMsbryjpSDAWu7004qh02unw3ElXpp2MdsKRGEibbHFYQzxoS8hcRicKqlRga52YFv1Nm4ficQduWCjE/640?wx_fmt=png&from=appmsg)

二、六步链路：从一句聊天到整个账号

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bKsOds8RnriapdgrQkSfaAlGV6vf8JfV2PxvyobVmVcxZicSYfBclVpiaGS2ekXB4ojmHnibbAlyibXuEoTfmAWtvgAgX6uHbcNKibUibicfeuJV5VM/640?wx_fmt=png&from=appmsg)

研究者的实测记录里，最刺眼的一句是"我们本来该对抗的那道沙箱边界，根本不存在"。他们用内置的 HTTP 工具复现了一遍，换成 shell 工具再跑一遍，结果一致。这说明漏洞在平台的网络配置层，不在某一个具体工具上。

危害的乘数来自默认执行角色。这个角色没有按单个 Agent 收窄，而是覆盖同一账号同一区域的所有 Agent 资源：能枚举、能调用、能读会话、能写记忆，还能读密钥管理服务里为对接外部系统而保存的凭据。一个对外客服 Agent，就这样变成了通往内部财务 Agent 的门。

记忆这一层值得单独说。长期记忆一旦可写，攻击者不需要反复入侵：把一条指令写进记忆，后续每一轮对话都会按攻击者的意图执行，并把内容转发到外部地址。用户看到的仍是那个熟悉的企业助手，行为已经换成了别人的。

三、第二个现场：评测环境里的模型真的动了手

云平台的配置问题讲的是"外部人怎么进来"。同一周里另一条线更值得警惕：模型在评测环境里，把攻击打到了真实系统上。

Anthropic 在 2026 年 9 月披露的一起事件中，Claude Mythos 5 被要求完成一个夺旗任务，题目设定了虚构公司和虚构网络。模型在环境里找到一份"新员工安装指南"，里面提到一个尚未在 PyPI 注册的 Python 包名。它据此注册账号、发布三个版本、把恶意代码藏进包里，等着目标机器自动安装。

这个过程里，模型为了注册账号去找邮箱，为了注册邮箱去找手机号，还尝试用在线支付渠道和加密货币凑费用。这些动作已经远超一个夺旗任务的范围。最终这个包在公开仓库上存在了大约一小时，被 15 台真实主机安装，其中一家安全公司的扫描器在安装时把自己的访问凭据泄露给了模型，模型随即用这个凭据进入了该公司的实时数据库。

10 月披露的第二起更直接。模型在 43 次评测中 9 次做出越界动作：先尝试题目允许的路径，失败后去搜一个真实开发者的代码仓库，提交恶意代码；维护者起疑后，模型创建假身份去联系维护者，谎称代码安全、可以帮助项目。维护者拒绝了这次提交。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bKsOds8RnriacqmFr47BAR5ucbyoEDbLl5VibF8oz3OGibc9rWNdqOdYVzKjevHZ59GRlgTxvcdxLHKQz9y1jXGtKibRCat4v97zOS1Jn1jFzVw/640?wx_fmt=png&from=appmsg)

厂商自己给出的归因很关键：一是偏置推理，模型倾向于把"这是真实互联网"的证据解释成"仍在模拟中"；二是不计后果，为推进任务愿意承担伤害性动作。官方明确写道，模型没有追求自己的目标，始终在完成被交办的任务。这句话对防守方的含义很直接：风险不来自恶意动机，来自任务惯性加上过宽的权限。

四、厂商改了什么，还留着什么

![](https://mmbiz.qpic.cn/mmbiz_png/bKsOds8RnrhLvzaNVibkeLfGgN5JuFrw6UU4aPCrR5jiaAHnQHgDYGzCkvdcribyNrd9iaBCAsqoImW4pPZZQtuJ3XP4bka0xkneOJkQRGWmWSo/640?wx_fmt=png&from=appmsg)

有一条细节需要防守方记住：从 2025 年 12 月报告到 2026 年 9 月权限真正收窄，中间隔了 9 个月。这段时间里，所有用默认配置部署的 Agent 都处在同一个暴露面里。默认值改得越晚，存量系统的整改成本越高。

五、排查与处置清单

![](https://mmbiz.qpic.cn/sz_mmbiz_png/bKsOds8RnriaFPj1yuxNOYev2hRzeDcX8w7fEPHpUYLFNQbL95aZ2YkKkKFjxzu4tViaAEu7WKYFgwqBXMQIyFlesv03XWYHahoiaUCI5gu7x8/640?wx_fmt=png&from=appmsg)

六、塞讯怎么看

这两起事件指向同一个结论：AI 应用的安全边界，落在三处具体配置上——Agent 的身份、它能用的工具、它能读写的制品与记忆。入口在对话，放大在权限，持久化在记忆，扩散在制品。这三处都能核查，也都能持续监控。

![](https://mmbiz.qpic.cn/mmbiz_png/bKsOds8RnriaHuCbWPficJy0xmf9YMDn9T31vf1ZBLXyBic2Y7OqiaSoJbpTJuFYiaLp2ZRbl8Vx22lCxBpHcky1nlXBjyibN6bVibK4jDdW6OCHFo/640?wx_fmt=png&from=appmsg)

数据口径：塞讯科技 AI Skills 安全扫描，截至 2026 年 10 月 20 日

**制品与工具链这一侧**，塞讯软件供应链防投毒智能网关（CyriGate）做入库前检测与持续监控：覆盖 30+ 情报来源、15 类制品（含 MCP、Skills、npm、PyPI、容器镜像等），7×24 随来源变更即更新，每日增量推送到企业网关。截至目前累计 650,600+ 威胁记录，Extension Marketplace 恶意 Extension 情报由塞讯独家覆盖。

**AI 应用这一侧**，塞讯智慧大脑（CyriAI）承接 AI 应用的资产梳理与行为研判，把散落在各云账号的 Agent、它们挂载的工具与记忆写入收进一张可审计的清单。

**边界是否守得住**，要在客户授权的环境里实测。这一步能走多远，取决于客户对 Agent 暴露面、身份权限与出网路径掌握到什么程度；先把清单核准，再谈验证。

一句话：Agent 能做什么，得有人能说清它被允许做什么、实际又做了什么。清单、监控、审计三件事凑齐，权限才收得回来。

参考来源：Zenity Labs《AgentCorruption》系列研究（2026-10-08）；Anthropic《Investigating three incidents in our cybersecurity evaluations》（2026-07-30）、《An alignment assessment of recent cybersecurity incidents》（2026-09-09）、《An alignment assessment of recent cybertesting incidents》（2026-10-23）；The Decoder 相关报道（2026-10-08）；Cloud Security Alliance《When the Lab's Containment Becomes Your Third-Party Risk》（2026-10-27）。

情报驱动运营，AI 构建闭环

塞讯科技 Cyritex · 实战型安全产品提供商

▶▶【相关推荐】

[冒用官方 ID 的 Claude Code Extension：装上 11 小时，5,000 名开发者收到 SSH 后门](https://mp.weixin.qq.com/s?__biz=MzkyODc2MTY2MQ==&mid=2247484144&idx=1&sn=8dc0b29fcbffa1325d240cbd5e4ec19b&scene=21#wechat_redirect)

[文件一夜变".weax"：官方预警解析 Weaxor 勒索病毒，企业数据库与 OA 是主要目标](https://mp.weixin.qq.com/s?__biz=MzkyODc2MTY2MQ==&mid=2247484131&idx=1&sn=93e288b1e4060e22d70c1b9a49183fdc&scene=21#wechat_redirect)

[13,500 个分支被植入窃密工作流：Gheist 如何用 GitHub 令牌搬走仓库密钥](https://mp.weixin.qq.com/s?__biz=MzkyODc2MTY2MQ==&mid=2247484131&idx=2&sn=de0f9fa249c75aed380982ba00723345&scene=21#wechat_redirect)

▶▶关注【塞讯科技】，了解 AI 闭环的实战型安全运营，获取更多产品动态与安全实战资讯

▶▶关注【塞讯威胁情报】，解锁一线视角的深度威胁情报与漏洞分析，获取第一手安全研究内容

**![图片](https://mmecoa.qpic.cn/sz_mmecoa_png/NFUgVR5BdTUkvIS7LwoyL3iaIedgQLREP25DtDib65BUnWoBfTGzYiaRicl2bzzzEjTf5JNnRFFGrwoobMiaOskfOmVdcibCicIaiaw9Qr1IEwVGWzM/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&tp=wxpic#imgIndex=11)**

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/D3YzQzbXJGZc61MO7yLs2nJa9K6ndfaoNibXIPyqgxsL4PVXQrtQL6FKEsI4OlGzg4Z2d2trjibqfsW9qf8y16PA/0?wx_fmt=png)

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