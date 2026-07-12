---
title: 浑象 —— AI 时代的安全能力评测基座
url: https://mp.weixin.qq.com/s/lT7p-tS6zwG4taPjpnM8lA
source: Doonsec's feed
date: 2026-07-11
fetch_date: 2026-07-12T05:07:13.166780
---

# 浑象 —— AI 时代的安全能力评测基座

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/m5jbNT90t271xCdYYMgj7e4Cz59S1WxJgtgNUnruteAcvvrabgsxUlXhkNmZCibQuacIEXpXt4hwrcX9BUCzESXNJ2l0Fh3O5A689aoDKBiaI/0?wx_fmt=jpeg)

# 浑象 —— AI 时代的安全能力评测基座

原创

wgpsec
wgpsec

WgpSec狼组安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**点击蓝字**

![](https://mmbiz.qpic.cn/mmbiz_gif/4LicHRMXdTzCN26evrT4RsqTLtXuGbdV9oQBNHYEQk7MPDOkic6ARSZ7bt0ysicTvWBjg4MbSDfb28fn5PaiaqUSng/640?wx_fmt=gif)

**关注我们**

***声明***

本文作者：WgpSec·AI组

本文字数：2786字

阅读时长：约10分钟

附件/链接：点击查看原文下载

**本文属于【狼组安全社区】原创奖励计划，未经许可禁止转载**

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，狼组安全团队以及文章作者不为此承担任何责任。

狼组安全团队有对此文章的修改和解释权。如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经狼组安全团队允许，不得任意修改或者增减此文章内容，不得以任何方式将其用于商业目的。

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4LicHRMXdTzAJOBqtShvMBtBXnAYfHAuziaELxUkYo5Ta1ro6AohToV1RDuFmiaib25w2GypianXgcfVmGR4uSFAdHw/640?wx_fmt=jpeg)](http://mp.weixin.qq.com/s?__biz=MzIyMjkzMzY4Ng==&mid=2247503851&idx=2&sn=8c8c8a70ec6a67177bcd17e612c19330&chksm=e8276832df50e124980c93a3ce2a9d1a863df53ec09163698948d0b385ffbd8f9564161edae7&scene=21#wechat_redirect)

❝

近一年来，网络安全行业聊得最多的词无疑是“AI Agent”或“AI自动化渗透”。从最初写写漏洞利用脚本，到如今大火的 Claude Code、Cursor，大模型在安全场景下的自主多轮决策能力让不少从业者感到惊艳。

但在这股热潮背后，有一个始终绕不开的现实问题：**我们到底该怎么客观、真实地去评估一个安全 Agent 的实战能力？**

传统安全圈熟悉的那套 CTF 靶场，直接拿给 AI 测往往漏洞百出。这并非指靶场本身不好，而是因为“人类选手”与“大语言模型”的交互逻辑、作弊边界完全不同。

针对大模型安全能力评估的种种痛点，我们在前段时间开源了 **浑象 (Benchmark Platform)** 靶场评估基础设施。今天不聊虚的，结合项目开源以来的实践，和大家深度拆解目前 AI 安全评测的真实痛点，以及浑象是如何在架构上做应对的。

## 传统靶场测 AI，为什么不可行？

如果直接把 AI 扔进现有的 Web 靶场，通常会遇到四个很现实的技术瓶颈

**“语料污染”带来的作弊行为（Data Contamination）**

传统的安全评测多采用静态题目或固定 Flag。大模型在训练阶段可能早就把相关靶场的 WriteUp 倒背如流了，甚至它能直接通过联网搜索搜到答案。这时候 AI 拿了满分，测出的只是它的“记忆力”而非“推理利用能力”。

**缺乏大模型原生的交互接口**

几乎所有的传统靶场都是为了人类设计的。AI Agent 想要接入，得先接一套复杂的自动化表单爬虫或者定制开发一套 HTTP API 转换层。这导致评测环境的泛化性极差，换个平台就得重写接口。

**高频压测下的靶场稳定性危机**

AI 的操作频率和人类完全不是一个量级。当数十个 AI Agent 同时进行自动化渗透时，靶机环境的频繁启动、垃圾回收、健康检测以及“冷启动延迟”，都会直接拉垮整个自动化压测的流水线。

**无法评估渐进式的渗透链路与企业级复杂内网**

真实的渗透测试是一个纵深推进的过程。传统的“单 Flag 验证”只能非黑即白地判断 AI 有没有拿到最终权限。更重要的是，现有的平台大多只能跑 Linux 容器，根本无法模拟企业内部复杂的 Windows 环境与企业级横向移动链路，导致模型评测与真实实战严重脱节。

## 浑象的设计思路：用 AI 的方式对齐评测环境

为了解决上述痛点，浑象在架构设计上彻底抛弃了“人类中心主义”，转而面向大模型和自动化流程进行深度定制。

![浑象平台界面](https://mmbiz.qpic.cn/mmbiz_png/m5jbNT90t24znQXA0taP1fIGgfDLSy19jdWjuvnmFGcqvWib8J8kRib9dXu89jcBhXn9ss1nQSzPlj8pnrdNkHrFcHWsI1VKuiakYCGfnEO0ec/640?wx_fmt=png&from=appmsg)

浑象平台界面

### 原生集成 MCP 协议，让 AI “自带工具”

我们参考了腾讯云智能渗透黑客松的设计思路，让像 Claude Code、codex 这一类主流的 Agent 框架，可以无需任何 API 适配，直接挂载浑象的 MCP 端口。

AI 能够以大模型原生的结构化上下文，自主调用 5 个标准工具：

| 方法/命令 | 功能说明 | 参数 |
| --- | --- | --- |
| `list_challenges` | 获取赛题列表及队伍进度 | — |
| `start_challenge` | 启动赛题实例 | `code` |
| `stop_challenge` | 停止运行中的实例 | `code` |
| `submit_flag` | 提交 Flag 答案 | `code` , `flag` |
| `view_hint` | 查看赛题提示（扣除总分 10%） | `code` |

把选择权和控制权完全交还给模型本身，真正实现“大模型原生”的靶场交互。

![AI交互文档](https://mmbiz.qpic.cn/mmbiz_png/m5jbNT90t25kL10ThaNu96JolYGJYLvvpE8gTzBxmfjIg0bDYt5ibJKZnm64pACsIuFib9HBIbiavoAdJYjG0Z4zpSJuwCYt6dpicEwnHfcgI0U/640?wx_fmt=png&from=appmsg)

AI交互文档

### 动态 Flag 运行时注入：斩断“盲猜投机”，强制链路闭环

为了防止大模型在评测中“刷榜投机”，浑象引入了动态 Flag 注入机制。Flag 绝不预先烘焙在 Docker 镜像里。每次实例拉起时，后端会在运行时动态生成唯一的 `flag{uuid}` 并注入到容器的环境变量或指定文件中。

不过动态 Flag 并不能阻止大模型对解题步骤（WriteUp）的语料记忆。但它的核心价值在于**斩断了“不看环境、盲猜答案”的作弊可能**——即便 AI 的记忆力再强，它也必须老老实实地走通真实的漏洞利用链路，触达到内存或文件系统，才能拿到最终的正确答案。这为自动化评测构筑了一条不可逾越的“实战验证”底线。

![题目列表](https://mmbiz.qpic.cn/sz_mmbiz_png/m5jbNT90t26kQGm5r0KuCl9Pus0c0Psib6cicmwHHDUmVqOibjeUIT009wvbm0tvT7MvQRqibBeml9meFbXkSuSquveU6iaicS4FjHc76FUrCakH4/640?wx_fmt=png&from=appmsg)

题目列表

### 一键预热与热加载，为高频评测减负

针对 Docker 实例在高频启动时容易超时卡死的问题，浑象设计了完善的**镜像预构建与缓存管理**功能。在平台后台，运维人员可以对赛题镜像进行一键预热，确保 AI 在批量测试时靶机能“秒级拉起”。

![题目预热](https://mmbiz.qpic.cn/sz_mmbiz_png/m5jbNT90t26GVWYWlEeQbNgq8gYvlMMK7mEvcn66ibpJWRklUDnJN2hHqlb5ep4WNmKaOZ7xlibxJDIHs8Sw7LldbTBDX9n35dMFmMnpW8UCI/640?wx_fmt=png&from=appmsg)

题目预热

同时，平台内置的「靶场商店」支持从 GitHub Releases 直接热加载导入新题，配合国内镜像加速，极大降低了长期维护成本。

![靶场商店](https://mmbiz.qpic.cn/sz_mmbiz_png/m5jbNT90t25AbBXU44GhkdHqrlXLuXpia8STyeXQG8wIRAanTvECWywMGhf1vcgmevPoEibXCa3b6eReiagy0icjkSz6UFUWoibc9fp9EUWtHcWo/640?wx_fmt=png&from=appmsg)

靶场商店

### Windows 系列与复杂的 AD 域靶场动态启停

真实的红蓝对抗中，Windows 系统和 Active Directory (AD) 域控网络才是绝对的主战场。在底层技术上，**浑象目前已经支持了 Windows 系列靶场以及 AD 域环境的动态拉起与生命周期持久化管理**。

![AD域靶场](https://mmbiz.qpic.cn/sz_mmbiz_png/m5jbNT90t25pgovIRHpHYibuu6iaGHjUfpN5DBfTBZDkBGLRjnUevojUbtrGO9fw3SH91CiacGkBSic9aD8htXJaS1fHCCsBHtTDyUJ1kECebmQ/640?wx_fmt=png&from=appmsg)

AD域靶场

![Windows靶场启动中](https://mmbiz.qpic.cn/mmbiz_png/m5jbNT90t25BLjY7cFvLiauK9MNn6EnVNxKGGnebXphw7bjGFtuRvMXfcPggPjSN1xV9IHGh01KqTn42LNNKIZF47QIbNamyMhuGL4NReaTo/640?wx_fmt=png&from=appmsg)

Windows靶场启动中

![第四层AD靶场](https://mmbiz.qpic.cn/sz_mmbiz_png/m5jbNT90t25TYN1FzEOIWEmoYmVSRRWE0wAW7oOUm9yIaM9lYOw5S5raUkj0T5f11eI1Bkc79c6B4SxibBIW2ttC4aRP1OWic8BUggY7BDsm4/640?wx_fmt=png&from=appmsg)

第四层AD靶场

### 数据即资产：AI 驱动的“一键规范化”出题生态

出题困难、赛题规范不统一，往往是靶场运维最大的包袱。浑象团队在赛题数据仓库（**benchmark-challenges**）中沉淀了一套严格的赛题声明规范。

**我们为 AI 配置了专属的生产力 Skills**。安全研究员或出题人只需要将这套规范和 Skills 复制给你的 AI 助手（如 Claude 或 GPT），大模型就能自动且规范化地为你生成开箱即用的靶场配置文件。

这种“AI 生成考卷去考 AI”的范式，做到了让靶场生态的一键化、规范化沉淀，使得赛题库的扩充和迭代变得极为轻量。

![一键导入题目](https://mmbiz.qpic.cn/mmbiz_png/m5jbNT90t271zJflRuxGhBPBpywpamFFj08u5Aib92vGcB3DBXZjDtCowMpXt8kicyJRXu6icwmiaI45N3T3rA8CvMIzqfrODhQcS8C8Ovbn2pY/640?wx_fmt=png&from=appmsg)

一键导入题目

## 开源后的实际反馈

项目开源了一段时间，看到有师傅在一篇针对安全 Agent 的深度评测文章里，直接用了浑象作为底座。作者提到的一句话正好契合了我们的设计初衷：

> “平台自带了近 150+ 的题目，然后还支持不同队伍，以及 agent 自动启动自动提交的接口，所以这也让我的测评变得更加的便捷。”
>
> 天下大木头，公众号：木头的信安小屋[AI 自动化渗透的实践落地记录](http://mp.weixin.qq.com/s?__biz=Mzg3OTU3MzI4Mg==&mid=2247485109&idx=1&sn=b6a2eae21852550d277b1cad78ad25e5&chksm=cf0326f8f874afee9358caff4e883ce0023623cd6b523ca20365433a489211ef0b7539a6b903#rd)

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/TCYk0DsjjczyG9I3V1TloXpsDf5se4q21BTDySbUG1rFibJzmeYOAvBpGMibfyibGVcmGeuc8ciaiaDEEK6sBSQBSaBxrC1aLLffxSDdialL4YykE/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/m5jbNT90t27zXicGP4VGoIjiaQndZtCiaicdvFt3jSYIfnAAxE2Gss8SiahxF2ar4d1vqicnrrMiavdEVLdvDfib3lNicIA6N12RT2t1KQJTaysnpbCI/640?wx_fmt=png&from=appmsg)

无论是多队伍并发压测，还是 Agent 的全自动生命周期管理，浑象原本的目的就是让安全团队告别繁琐的接口适配，回归到安全能力对抗的本质。

在 WgpSec 的整体构想中，浑象是**智能安全生态(WgpSec Agentic Ecosystem)** 中负责“闭环评估”的关键底座：我们通过 **AboutSecurity** 积累知识，利用 **context1337** 提供接口，结合 **tchkiller（代码开源）** ，AI通用解引擎 **Alkaid 瑶光（私有）** 结合去做自动化攻防——而 **浑象 (benchmark-platform)** ，就是检验这整套 AI 安全生态实战成色最严格的考场。

## 未来规划：支持 redc 调度上云，打破硬件枷锁

本地评测 Windows 和 AD 域靶场，对评测机的 CPU、内存和磁盘 I/O 都有着极高的要求，这成了很多安全团队自动化高频压测的硬件瓶颈。

为了解决这一痛点，我们正在考虑**支持通过 WgpSec 红队基础设施 redc 方式进行靶场调度启动**。

让浑象将不仅仅局限于本地的 Docker Compose 或本地虚拟机集群。

通过与 **redc** 的深度结合，靶场实例将被无缝调度至云端高性能基础设施上运行。这种“靶场上云”的模式，不仅能利用云端的弹性算力瞬间并发拉起成百上千个复杂的 Windows 域控网络，还能实现网络隔离与云端流量审计，打破本地硬件资源的枷锁，让大规模安全 Agent 的分布式批量压测变得高效且经济。

## 项目共建

浑象平台底层的研发参考了 xbow-engineering、Neuro-Sploit 等社区优秀项目的技术成果，在此致谢。

目前的开源仓库（**https://github.com/wgpsec/hunxiang**主要负责平台管理及核心的调度逻辑。

如果你有很有意思的靶场题目构想，欢迎到我们的靶场数据仓库（**https://github.com/wgpsec/benchmark-challenges**）提交 PR 或 Issue！

***作者***

![](https://mmbiz.qpic.cn/mmbiz_png/4LicHRMXdTzBWIsILOIed7kIrnFksqrWrNI7kmZYLlsQ14MoNtNRRLT99TFSRAu6QUDFKic0yytXP56CwLb0d1ww/640?wx_fmt=png)

WgpSec · AI组

www.wgpsec.org

***扫描关注公众号回复加群***

***和师傅们一起讨论研究~***

**长**

**按**

**关**

**注**

**WgpSec狼组安全团队**

微信号：wgpsec

Twitter：@wgpsec

![](https://mmbiz.qpic.cn/mmbiz_jpg/4LicHRMXdTzBhAsD8IU7jiccdSHt39PeyFafMeibktnt9icyS2D2fQrTSS7wdMicbrVlkqfmic6z6cCTlZVRyDicLTrqg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/gdsKIbdQtWAicUIic1QVWzsMLB46NuRg1fbH0q4M7iam8o1oibXgDBNCpwDAmS3ibvRpRIVhHEJRmiaPS5KvACNB5WgQ/640?wx_fmt=gif)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4LicHRMXdTzDjy8pCtpvJKBibCLXQDm14MbdlTqXYESXADHkVpL6f81Z4TVFOGQMjBjgxPpUcYnzahRhibQUdcKzQ/0?wx_fmt=png)

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