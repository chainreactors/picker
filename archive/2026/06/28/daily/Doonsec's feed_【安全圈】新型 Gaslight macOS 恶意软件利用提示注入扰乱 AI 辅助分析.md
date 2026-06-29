---
title: 【安全圈】新型 Gaslight macOS 恶意软件利用提示注入扰乱 AI 辅助分析
url: https://mp.weixin.qq.com/s/ma3z1HJPjejMXv7AmsLHiQ
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:32:39.727849
---

# 【安全圈】新型 Gaslight macOS 恶意软件利用提示注入扰乱 AI 辅助分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/sbq02iadgfyGf6Vsa28qdUNaKRC3XODLqvl0Mj5nw62jAPLjrZlMBSKIK2ibfgMUMb9RvUctFAV0gGj9BHIcV6Uweo88wDc10MSUMkjGtugjQ/0?wx_fmt=jpeg)

# 【安全圈】新型 Gaslight macOS 恶意软件利用提示注入扰乱 AI 辅助分析

安全圈

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

恶意软件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/sbq02iadgfyEOYRuicbqCvpVl224dKVx8TpReUDGyupm5b89jIxtzSk3uOD2wkM5boaVyLTlFuSXBJye6JhEcR1fIbqW3eJofdLCOecqcqCCI/640?wx_fmt=png&from=appmsg)

**一种此前未被记录的基于 Rust 的 macOS 植入程序和信息窃取器被发现嵌入了提示注入载荷，旨在欺骗恶意软件分析人员的人工智能（AI）工具，使其中止或拒绝对该恶意软件进行分析。**

由于这种欺骗行为，该恶意软件被命名为 Gaslight。评估认为，该工具极有可能是与朝鲜有关联的威胁行为者的作品。

SentinelOne 研究员 Phil Stokes 在一份技术报告中表示：其最显著的特征是嵌入了一系列伪造的系统故障消息，旨在使基于 LLM 的研判代理质疑自身的会话。它攻击的是代理的感知，而非其运行的沙箱。

该恶意软件架构的核心是一个基于 Telegram bot API 的命令与控制（C2）通道，该通道进入轮询循环，允许操作者通过交互式 shell 发出指令并返回执行结果。如果同一 bot token 的两个实例同时轮询，则会发出 Conflict 响应，导致第二个副本终止。

该 shell 支持六个主要命令，可在受感染主机上建立持久性控制：

* help - 显示命令帮助
* id - 向操作者标识植入程序
* shell - 通过 execvp 执行 shell 命令
* kill - 按 PID 终止目标进程
* upload - 通过 Telegram 的 attach 机制外传文件
* stop - 停止植入程序的执行

SentinelOne 表示发现了存在名为 focus 的第七个命令的迹象，但其功能目前尚未确定。为了实现持久化，Gaslight 使用了一个 LaunchAgent，其 .plist 文件中使用了标签 com.apple.system.services.activity。

该恶意软件中还嵌入了一个 6.6 KB 的 Base64 编码 Python 脚本，其功能是一个信息收集套件，负责收集 Terminal 命令历史记录、已安装应用程序列表、运行进程快照、系统硬件和软件配置文件、macOS Keychain 数据库，以及来自 Chrome、Brave、Firefox 和 Safari 网络浏览器的数据。收集到的数据随后被压缩成 ZIP 存档并通过 Telegram 上传。

该 Python 窃取器本身是通过一个单独的 2 KB Base64 编码 bash 安装程序部署的，该安装程序从 astral-sh/python-build-standalone 项目中下载一个 cpython-3.10.18 解释器。其中包含 emoji 表情和大量注释头，表明它很可能是使用大语言模型（LLM）生成的。

Gaslight 值得注意的一点是，与 bot token、聊天 ID 以及其余操作者配置相关的详细信息并未硬编码到样本中，而是在运行时提供。Stokes 补充道：该植入程序在其自身运行时输出中自隐了 Telegram bot token，使任何捕获日志或崩溃工件的人都无法获取。

除此之外，该恶意软件还试图通过嵌入一个包含 38 条伪造系统消息的 Markdown 围栏块来逃避基于 AI 的检测，这些消息旨在诱骗安全代理中止、截断或拒绝分析。

SentinelOne 表示：该框架包含关于 token 过期、内存不足终止、磁盘耗尽和重复操作失败的虚假系统消息。它还植入了关于注入漏洞和静态分析标记的虚假警告。SentinelOne 称这是一种试图武器化 LLM 辅助研判管道的尝试，这些管道正越来越多地出现在逆向工程循环中。

***END***

阅读推荐

[【安全圈】苹果印度代工厂遭黑客入侵 海量新机机密文件流入暗网](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077571&idx=1&sn=d7f4d998f528d5fc6959d0667e8d301d&scene=21#wechat_redirect)

[【安全圈】Linux 漏洞 DirtyClone 披露，可提权至 root 最高权限](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077571&idx=2&sn=94626f4fbfa16457a6aade2de4dddcbe&scene=21#wechat_redirect)

[【安全圈】16岁男孩自学“黑客”技术，入侵该国疫苗接种系统](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077571&idx=3&sn=79a3c261cb75ac864734ad8babd8a4fa&scene=21#wechat_redirect)

[【安全圈】五眼联盟警告AI网络威胁](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652077560&idx=1&sn=aa6c87cf12f60e825d2ec099ef852c0e&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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