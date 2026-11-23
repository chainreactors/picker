---
title: AI Agent 自主挖出零日并拿下 root：MONAI Label 事件
url: https://mp.weixin.qq.com/s/sVgOExjfIcQqU4isPaaDCg
source: Doonsec's feed
date: 2026-11-22
fetch_date: 2026-11-23T10:00:46.863332
---

# AI Agent 自主挖出零日并拿下 root：MONAI Label 事件

# AI Agent 自主挖出零日并拿下 root：MONAI Label 事件

原创

大白
大白

知白守黑1024

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

本周最值得细读的安全报告，开头就不太一样：AWS 威胁情报团队不是在自己的客户环境里发现攻击，而是在公网上撞见了一个没设密码的「敌方指挥所」——一个完全暴露的开源 AI 渗透测试框架 Cairn 的控制面板，任何人打开就能看到里面 AI Agent 的任务设定、提示词和完整运行记录。记录显示：约 48 小时的活动窗口里，这些 Agent 在几乎没有人工干预的情况下，自己找到了医疗影像软件 MONAI Label 的一个零日漏洞，并最终拿到一台大学服务器的 root 权限。

![](https://mmbiz.qpic.cn/mmbiz_jpg/j7ZnQr1RD1h0EARibQhy2EnnDeqkdDasCUxBwDMcD5aUBHhcpu8jlBL3oGbDMl1a6PSNmff62K1fJB78TkRNBavMYNyd47FRfWARgAGOqS6U/640?wx_fmt=jpeg&from=appmsg)

从指挥面板暴露到报告发布：完整证据链

先认识一下受害者。MONAI Label 是 Project-MONAI 旗下的开源医疗影像标注服务器，研究团队用它给 CT、MRI 等医学扫描做 AI 辅助标注、训练影像模型，全球不少高校实验室和医院科研环境都在跑。它的默认配置里有一个要命的设定：**不开启认证**。只要能访问到服务端口，任何客户端都可以直接调用 API——在实验室里图省事，放在互联网上就是裸奔。

漏洞本身编号 CVE-2026-133968，CVSS 9.8，出在 datastore 的上传端点，本质是路径穿越：调用方提交的文件标识符被直接拼接到存储目录后面写盘，全程没有校验拼接结果是否还留在目录内。服务以运行账户的权限写文件，攻击者虽然不能随手写满整个磁盘，但只要找到一个可写的代码或配置位置，就能把「写文件」升级成「执行代码」。0.8.5 及更早版本在默认配置下全部受影响。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1hhZZ4hEc4ria7aPwBUAXHNcxLW0cexgEoiapocHyXfe85K5A9lImsfL2Dn32wUK21c98ET4mjX56JEuB4uJpPAlic5TIAoELb8zE/640?wx_fmt=jpeg&from=appmsg)

一句「拿到 shell」之后的六步：全程 Agent 自主决策

再看 Agent 是怎么干的。操作者只做了两件事：设定目标——「拿到 shell」；选定目标主机。剩下的全部由 Agent 自主决策。9 月那次约 48 小时的活动窗口里，Agent 从开始映射应用 API，到实现存储目录之外的任意文件写入，只用了大约**11 分钟**。没有人类告诉它漏洞在哪，也没有现成的 exploit 可以抄——它是自己翻出来的。

root 的拿法更值得展开讲。在另一个会话里，Agent 用同一个洞把一个文件种到 Python 启动时会自动加载的位置，然后触发一次训练功能——服务端拉起一个新的 Python 进程，这个进程加载了刚才那个文件，以 root 身份回连到攻击者手里。一次路径穿越，两次跳变：先写文件，再借服务自己的功能提权执行。AWS 强调，这一步能否复现取决于服务的运行账户权限，但在这台大学服务器上，它成立。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1gnCQn8Bz0u1DoRljZNYTiatjcTUK7UHG4zkgRdgzDr3jDKx2B8c0koqNqCcnqrVs5yNicmtiaXcWFgX601fiaoicpVJmOFsw4UznbU/640?wx_fmt=jpeg&from=appmsg)

Cairn 框架的人机分工：人类定目标，Agent 选路径

归因部分，AWS 给得克制：中等置信度关联中国背景行为者，依据是 Agent 会话里的简体中文提示词、中国标准时间的时区设置、以及目标选择指向。报告没有点名具体组织，也没有认定政府背景。目标集中在东亚高校。同样值得记住的还有活动里的失败记录——root 只在一台服务器上实现，不是每一次部署都会重演这个结局。

这份报告的黑色幽默有两层。第一层属于攻击者：一个专攻别人安全短板的团队，自己的指挥面板没设密码，被 Amazon 从头看到尾——没有这个失误，就没有这份报告。第二层属于 MONAI Label 项目方：维护者确认了漏洞，10 月 19 日就把修复合进了源码（PR #1915，强制上传路径解析在批准目录内、拒绝空文件名和点开头的文件名），但到今天都没有发布可安装的修复版本——PyPI 上最新的还是 2024 年发布的 0.8.5，安全公告 GHSA-qc22-rmgc-vg94 里写着「修复将在未来版本中提供」。**修复合了，用户拿不到。**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/j7ZnQr1RD1hCHo97VVnuW4xX7RQufNqwXj4672SQmyibBFz6Xu1scHlmw0gibTTyRONC443qVH4Uzk1nG1EGzK0DjXHG70bSg6w8hBVE6ztvw/640?wx_fmt=jpeg&from=appmsg)

补丁未发版期间的五道闸：网络、认证、权限、源码、排查

在修复版本落地之前，跑着这套服务的环境能做五件事：用防火墙和路由规则阻断不可信网络访问，而不是指望 URL 难猜；手动开启认证；用专用低权账户运行并收紧可写目录；自行从源码部署的，确认包含了 10 月的修复；已经在公网暴露过的，排查异常的 Python 启动文件和来历不明的训练任务——那正是这次攻击的路径。

过去几个月，防守方用 AI 挖洞的故事已经听了不少：安全公司借助 AI 模型找到 NGINX 和 OpenJDK 的严重漏洞，算力成本不到几百美元。这一次的不同在于，AI 站到了攻击侧，而且不是辅助——从目标侦察、漏洞发现到利用落地，全程自主完成。攻防两端的 AI 能力差距，正在以月为单位被抹平。对每一个把 Agent 接进生产环境的人来说，这份报告里最该记住的是两句话：**Agent 需要的只是一个目标，不是教程；而最好的猎物，永远是那些默认不设防的服务。**

参考来源

1. https://aws.amazon.com/blogs/security/chinese-nexus-actors-cairn-ai-agents-found-a-zero-day-on-their-own/
2. https://thehackernews.com/2026/11/attackers-ai-agents-found-zero-day-in.html
3. https://www.cve.org/CVERecord?id=CVE-2026-133968

本文基于 AWS Threat Intelligence、The Hacker News、SecurityWeek 及 Project-MONAI 官方仓库公开信息整理，仅供安全研究与学习参考，不构成任何操作建议。相关漏洞修复已合入上游源码，请在授权环境中开展安全工作。

觉得有用，点个「在看」让更多人看到。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/zlD2iah6QpJjciciaI6Ylp5L7rn9Y2O6cTxzf9Suxyw0cwibRgVtpuBzNrqS1ibK3USX8IXHulcNen2rMApDXn352cg/0?wx_fmt=png)

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