---
title: 朝鲜黑客组织（Kimsuky）利用 OpenCode人工智能代理大规模生产 LNK 攻击中的钓鱼诱饵
url: https://mp.weixin.qq.com/s/4n-0c7paIIJkgOMa_lLOIA
source: Doonsec's feed
date: 2026-09-24
fetch_date: 2026-09-25T06:51:46.027224
---

# 朝鲜黑客组织（Kimsuky）利用 OpenCode人工智能代理大规模生产 LNK 攻击中的钓鱼诱饵

# 朝鲜黑客组织（Kimsuky）利用 OpenCode人工智能代理大规模生产 LNK 攻击中的钓鱼诱饵

Rhinoer
Rhinoer

犀牛安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/vO1zY1O9p8L3K9CkWTJU83kPmTxE9kPIQvrgzau55RwADuFEbGoChH91WyuRfUF7sNicP7BtNqEXU3xK6KkTiahjFWAtv9DZ7o7l42Uo91RWw/640?wx_fmt=png&from=appmsg)

据观察，Kimsuky 使用人工智能代理大规模生成极具迷惑性的钓鱼诱饵，然后将恶意软件隐藏在 Windows 快捷方式文件中。最新的活动表明，看似普通的文档如何成为入侵的第一步。

该攻击活动始于发送带有 ZIP 压缩文件的鱼叉式网络钓鱼邮件。压缩文件内含一个伪装成文档的恶意 LNK 快捷方式，通常带有浏览器风格的图标和虚假信息。打开后，它会显示一个诱饵页面，同时悄悄启动 PowerShell 程序来获取更多代码。

此次检测的13个样本采集于2026年8月11日至19日期间，均使用了财务和公司诱饵。这种更广泛的诱饵范围增加了经常收到文件和财务通知的公司员工的风险。

Genians 的研究人员认定该活动是与 Kimsuky 有关的 Operation GitPower 集群的延续。

Genians 在一份与网络安全新闻 (CSN) 分享的报告中表示，该活动保留了基于 GitHub 的命令基础设施，同时增加了规避和各种诱饵格式。

## **Kimsuky 黑客使用 OpenCode AI 代理**

最显著的变化是，在几个 PDF 诱饵的创建者和生产者元数据中出现了开码的证据。

四份文档的创建时间戳均为 8 月 16 日，而它们的作者字段仍设置为“匿名”，这支持了它们是自动生成的而不是逐个组装的判断。

这些文件并非都经过精心润色。有些文件中，付款日期、宽限期和金额等信息仍保留着未替换的占位符文本，这表明草稿未经仔细审核就被仓促投入使用。

![](https://mmbiz.qpic.cn/mmbiz_png/vO1zY1O9p8I27myE3pjb7ssPNib7HhXxhnlzADeBXxHtPc3UAqSicE7MEagRxa1icWjibDmiaEbvicSCnTykMMEdhbkWwQXXoBTIVmKT9ibwX2PrxA/640?wx_fmt=png&from=appmsg)

其他 PDF 文件显示了 HeadlessChrome 和 Skia/PDF 元数据，这表明存在一个独立的工作流程，该流程生成 HTML 内容并将其渲染成更清晰的 PDF 文件。

这种组合使攻击者能够在不放弃其惯用的社会工程手段的前提下，实现快速攻击。分析人员发现了 29 个被检索到的诱饵文件，但通过 MD5 校验，只有 11 个文档是独一无二的，重复的内容以随机名称重新分发。

读者可以在Kimsuky 本地 LLM 网络钓鱼诱饵中看到更早的背景 ，其中人工智能生成的文件已经被用来使通过快捷方式发起的攻击看起来很普通。

![](https://mmbiz.qpic.cn/mmbiz_png/vO1zY1O9p8LwpJA4Y853G4DqflcQLhbXqUmPxGXVPAFibCGgaRYiblykicibIOK4jNa78bz28oQkbNsJ6JFByX1Vz6W7fIXtbnSD1xpBTIW4XgE/640?wx_fmt=png&from=appmsg)

随着操作人员不断改进流程，此类痕迹可能会消失，因此防御者不应仅凭文档质量或元数据来判断附件是否安全。

## **LNK 加载器隐藏基于 GitHub 的有效载荷**

每个被分析的 LNK 文件都会启动 PowerShell，并将加密加载器隐藏在长度约为 5,800 到 9,500 个字符的参数中。

大约 300 个前导空格有助于使命令在快捷方式属性窗口中不可见，而过多的填充会增加文件大小，从而阻碍简单的检查和一些自动检查。

解码隐藏内容后，加载器使用硬编码的个人访问令牌从 GitHub Raw Content 下载诱饵和后续脚本。

然后，它会在 AppData 或 Temp 中创建随机命名的 PowerShell 文件，通过 启动 PowerShell  `conhost.exe --headless`，并注册模拟 BitLocker、MATLAB 或 .NET 组件的隐藏计划任务。

其中一种以Visa为主题的变种攻击还会从Pastebin获取代码，这样即使GitHub访问被封锁，攻击者也能获得第二条攻击路径。这种方法借鉴了 朝鲜GitHub C2攻击的思路，在朝鲜的攻击中，攻击者利用可信的开发者平台将恶意流量混入正常的网络活动中。

新版本会检查虚拟机和分析工具，查找用户名“Bruno”，并在检测到可能的科研环境时删除 PowerShell 命令历史记录。

![](https://mmbiz.qpic.cn/mmbiz_png/vO1zY1O9p8KMHT8QA5D6CnUPcLh3wGDdfvjztNUibCHxkIVf6Y8Ejko1dpgxN628Ab2czphrgcupf38r5du94F9WsCheDiazxFER2nQuVutto/640?wx_fmt=png&from=appmsg)

他们也会在一些不完整的构建中使用错误文档，但持久化和有效负载检索阶段仍然可以运行。类似的 LNK PowerShell 加载器技术 表明，仅仅打开一个看起来像 PDF 的文件并不能作为可靠的安全检查。

组织应隔离未经请求的包含 LNK 文件的 ZIP 附件，尤其是当其图标和描述与其实际类型不符时。

安全团队应将 LNK 启动与长命令行、隐藏的 PowerShell、新创建的脚本、计划任务注册、携带异常令牌的 GitHub Raw 请求以及 Pastebin 访问关联起来。

这种以行为为先的方法比依赖单一域名黑名单或诱饵文档审查更持久，并且与 恶意快捷方式文件攻击活动的经验教训相一致。

**入侵指标（IoCs）：-**

![](https://mmbiz.qpic.cn/mmbiz_png/vO1zY1O9p8L28rT1cy3PI3ZSUtadibf7uTibBrdhHIWev2ynSYhu5dQBfJZ7qeRarCcqmkfV4ZyTOh37xMmhJ5zbNHmptrXxkQwlIaalIdM2k/640?wx_fmt=png&from=appmsg)

**注意：** *IP 地址和域名已被故意隐去（例如，*`[.]`*），以防止意外解析或超链接。请仅在受控的威胁情报平台（例如 MISP、VirusTotal 或您的 SIEM）中重新启用*。

信息来源：CyberSecurityNews

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qvpgicaewUBlHBkILqQuaxKrXKhgz0ZMBz6S8ME08fAF1vUqLQlYxwYIVWh5bsgnAictt45YVfMuqzAic2QZd6Siag/0?wx_fmt=png)

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