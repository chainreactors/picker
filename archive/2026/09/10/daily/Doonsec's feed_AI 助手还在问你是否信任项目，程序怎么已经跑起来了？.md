---
title: AI 助手还在问你是否信任项目，程序怎么已经跑起来了？
url: https://mp.weixin.qq.com/s/YlDuWzXaOQS410utaJyJ-w
source: Doonsec's feed
date: 2026-09-10
fetch_date: 2026-09-11T06:48:45.024131
---

# AI 助手还在问你是否信任项目，程序怎么已经跑起来了？

# AI 助手还在问你是否信任项目，程序怎么已经跑起来了？

原创

千里
千里

东方隐侠安全团队

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

打开一个陌生项目，AI 助手弹出提示：“你信任这个项目吗？”你还在犹豫要不要点，后台却已经运行了项目指定的程序。

这听起来很别扭：既然还没同意，怎么就动手了？Manifold 在 9 月 1 日公开的 GitSpawn 研究，展示了部分旧版 AI 编程助手中的这种情况。

我觉得这项研究值得和大家分享一下，因为我们平时很容易把“模型还没回答”和“软件还没开始工作”当成一回事。实际上，模型拿到代码之前，客户端已经在忙了。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AwziaxUyibcNjJmbwjzIzcqzcHTIBaRJ5jIEbKsiaRkhpozuOWaNicU55Ckaqwyemf0v6ZvcyBdsDexYeynFP6Vh3fbUrficnv8yhcHk1NaH79O4/640?wx_fmt=webp&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

GitSpawn 研究页面。来源：Francisco Rosales / Manifold，2026 年 9 月 1 日。

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

确认框还在，程序已经运行过了

01

下面这张图来自研究者的 Claude Code 演示。上半屏还在询问是否信任工作区，下半屏已经查到了一个“标记文件”。这个文件是演示程序创建的，用来证明程序运行过，和EDR那种蜜饵文件一个原理。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AwziaxUyibcNj9icbWfdYqeFXe460xtJbf7PZsL68OzxQsnBz9w21ToLdcQEic8664ibD7f85QxhmfQqibb0sBk7xnW47VBBEgyN6uF7vIP2h0wVU/640?wx_fmt=webp&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

Claude Code 演示录像末尾前约 2 秒的截图。来源：Manifold。

读取数据其实并不是最危险的，客户端读取项目文件，是了解代码的一部分，但是这个过程也包含着可能运行项目指定的程序，进而修改本机文件，甚至产生其他影响。这里关注的风险是后者是否在用户确认前发生。

原文记录，这条 fsmonitor 问题已在 Claude Code 2.1.196 修复。因此目前，使用最新客户端的各位已经不受影响。

Qwen Code 的演示更容易理解了，在录像里面，在信任文件目录之前，先出现了计算器（计算器就是运行项目指定的程序），后面才出现连接模型服务的界面。计算器是研究者用来展示本地程序已被启动的。

![](https://mmbiz.qpic.cn/mmbiz_jpg/AwziaxUyibcNgIdj9DNRicxhgvM9nSxy8EZPcDeXCAVMgdADg9L8ozhV8B0YAm1k3w8NekTNIzxibYAN2qdKiaVxUeUsrrcoCjLyd8eIibOKZ7KIo/640?wx_fmt=webp&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

Qwen Code 录像约第 5 秒：计算器已出现。来源：Manifold。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/AwziaxUyibcNh8Eqr0gOMLt3LylHpVGchfgU0zKqIL8LoVeqJYTfiaSzdaQXUwEFfiaTR0ZyJrFY1Kdkia30SbptUo3nq61OeCVDtcKNtVk9wQNE/640?wx_fmt=webp&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

同一段 Qwen Code 录像末尾前约 1 秒：模型服务连接界面。来源：Manifold。

也就是说，即便还没连上模型，客户端也能启动本机程序。它本来就是装在你电脑上的软件，运行这些程序并不需要先问大模型。

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

只是想看代码，怎么会运行别的程序？

02

AI 编程助手通常会先收集项目文件、最近的改动，再把这些材料交给模型。为了知道代码改了哪里，客户端会调用 Git，也就是开发者管理代码版本的工具。

Git 有个配置项叫 core.fsmonitor，它允许指定一个辅助程序，帮助检查哪些文件发生了变化。这个功能本身有正常用途，麻烦在于如果相关配置是别人放进项目的，Git 仍可能按配置启动那个程序，有点“黑加白”木马组合套餐的味道。

于是，原本的一步“查看代码改动”，变成了这样一个过程：助手调用 Git，Git 读取本地项目配置，再运行配置指定的程序。模型可能还没拿到代码，程序就已经执行了。

这也说明，光要求模型“执行危险操作前先问我”管不到这里。触发操作的是客户端调用 Git 的过程，未必经过模型的工具审批。

但也别把它理解成“随便克隆一个仓库就会中招”。前面这条路径需要相关本地配置已经到了你的电脑上，例如别人发来一个带有 .git 目录的项目压缩包。普通 git clone 不会把远端的 .git/config 一起复制下来。

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

流程倒反天罡的Cursor

03

Manifold 还研究过 Cursor 的终端版本。Cursor 可以为任务创建一份独立工作目录，叫作 worktree。项目可以配置准备步骤，比如安装依赖、设置开发环境，供新目录使用。

在研究者测试的旧版本中，Cursor 先执行了这些准备步骤，之后才询问用户是否信任项目。按原文的版本对照，2026.07.23-e383d2b 已调整为先确认、再执行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/AwziaxUyibcNj4W3ndGFDuwhd8wtEXUicqg4dbvIsJNXU1FSqKnny9nWWe3O6veUHa2ArElAvWibaBn9Hq8cLibr1TTibdXksPg7WemTmXslkX2jQ/640?wx_fmt=webp&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

Cursor 专项研究中的信任确认界面。执行先后顺序以原作者的测试记录为依据。来源：Manifold。

这里与 GitSpawn 的 Git 配置路径有个区别，Cursor 使用的这份项目配置，可以随着正常的代码克隆来到本机。它不需要远端的 .git/config，所以并不与前面的说明矛盾。

原作者还记录，所测版本中的这段准备操作不受沙箱开关约束。沙箱用来限制程序能读写哪些文件、访问哪些资源，但前提是这段操作确实在沙箱里运行。选中了“启用沙箱”，仍然需要核实项目准备过程有没有被纳入。

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

Goose修复方式提供解决思路

04

Goose 也是 AI 开发助手，可以连接模型、调用本地工具。这里提它，是因为厂商公告和修复源码都公开，能看清开发者究竟改了什么。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/AwziaxUyibcNhNkrrOO9U2RNQaqsbg3Ih6EZo8XSFzVE90WMf0U0wRODC7fDSibFaiceHm2E5lFqJkIocqjucHr3iaRtYvt5A8wFmWSDoGIS4vuY/640?wx_fmt=png&from=appmsg)![]()![]()![]()![]()![]()![]()![]()![]()

Goose 项目标识。下文依据其公开安全公告与版本源码。

Goose 的代码审查命令 goose review，也会先调用 Git 收集改动。厂商公告描述的问题也明确存在GitSpawn的问题，Git 根据本地配置启动了额外程序，而这段操作不经过模型工具审批。

公告列出的修复版本是 1.44.0。相关修复在调用 Git 时明确设置 core.fsmonitor=false，关闭前面提到的辅助程序功能。这样，这次 Git 调用就不会再通过该配置启动辅助程序。

这个改法很直接：客户端自己调用的工具，由客户端在调用时加上限制。至于其他位置调用 Git 时是否也做了同样处理，还得继续检查。我们对照的源码只支持所查代码审查路径的结论。

![](https://mmecoa.qpic.cn/mmecoa_png/p7HuDKJB4T17hmgN4ia9GQKG4cKp1tBh6oJW3VxeuBxnh3lPjT9ibFFJCOouHNxa9C3plmiceqkqYta4Ap41IEfLw/640?wx_fmt=png&from=appmsg)

如果公司要用，应该查什么？

05

我建议大家要把“打开项目”也算进检查范围。别只盯着模型回答后的工具调用，还要看从客户端启动、读取项目，到模型开始分析之间，自动运行了哪些程序。

对使用者来说，先更新工具，谨慎处理来历不明的项目压缩包；确实需要检查陌生项目时，优先使用单独的测试环境，避免带入日常工作的凭据和敏感文件。

对开发和安全团队来说，需要把具体调用查清楚，比如Git 是谁启动的，项目准备脚本在哪里运行，哪些操作必须等待确认，哪些操作受到隔离限制。这些答案要从代码、配置和运行记录里找，不能只看界面上有没有按钮。

我们和AI的关系中，应该铭记人工智能的三条原则，需要人类同意才能做的事，就等人类同意后再做。至于后台有哪些准备工作不需要确认，Agent也应该说清楚。

本文依据公开研究、厂商公告和源码整理，未做漏洞复现。截图来自原研究；文中版本和修复信息对应原文披露记录，不代表所有产品今天的状态。

隐侠团队官网文章保留了跨产品记录和 Goose 源码对照，想继续看细节，可以从这里进入。https://eastsword.github.io/articles/gitspawn-context-review/

预览时标签不可点

阅读原文

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icqGYtiaRQqH60REFUK5n2iaTH2Ifziba6pa3aNz9ofOyXMqhhszN46Jl2IWB3mBT41SS9kywiaJN52zxTqxvLfn0UA/0?wx_fmt=png)

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