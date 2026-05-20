---
title: Kimsuky利用LNK和JSE的诱饵来锁定招聘人员、加密货币用户和国防官员
url: https://mp.weixin.qq.com/s/I0HWAJ9EuHeRaXLtXp4Bsg
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T06:01:07.418487
---

# Kimsuky利用LNK和JSE的诱饵来锁定招聘人员、加密货币用户和国防官员

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/BicXBAdicJy7MApPxEN8iameChl5icVXLwEwu5bI2SOfdOficYPyPttP7rD54k11qVaBZzaTHuIpUGxXoUOzMUnxvZ277ic88uLNOQDRhQStMK5B4/0?wx_fmt=jpeg)

# Kimsuky利用LNK和JSE的诱饵来锁定招聘人员、加密货币用户和国防官员

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

Kimsuky 黑客利用 LNK 和 JSE 诱饵攻击招聘人员、加密货币用户和国防官员。

与朝鲜有关联的威胁组织 Kimsuky 在 2026 年初发起了至少四次不同的鱼叉式网络钓鱼活动，目标包括招聘人员、加密货币用户、开发人员、国防人员和学术管理人员。

尽管使用了不同的主题和传播方式，但所有攻击活动都遵循一致的攻击链：诱饵文档展示、有效载荷部署、持久性设置和命令与控制 (C2) 通信。

每起攻击活动都使用了根据受害者特征量身定制的诱饵：

* 活动 1 伪造简历、名片和医疗文件，以吸引招聘人员和机构。
* 第二项活动模仿了一款基于 Solana 的虚假安全工具的技术文档，以引诱加密货币投资者和开发者。
* 第三项行动利用军事竞赛文件渗透国防组织和外国武官。
* 第四次攻击活动将恶意脚本伪装成研究生院培训文件，目标是公共部门员工。

攻击者大量使用伪装成 PDF 的 LNK 文件和伪装成韩文文档 (.hwpx) 的 JSE 脚本，利用 Windows 默认隐藏文件扩展名的行为。

这三起攻击活动使用了体积过大的 LNK 文件，其中嵌入了诱饵 PDF 和隐藏的有效载荷。执行后，这些文件会显示看似合法的文档，同时悄无声息地提取恶意组件。

例如，第 1 号活动使用单个 LNK 文件将诱饵 PDF 和持久化机制放入启动文件夹中。

随后，该恶意软件从 C2 域 (nelark[.]icu) 下载 PowerShell 脚本，禁用用户帐户控制 (UAC)，添加 Windows Defender 排除项，并注册一个伪装成 Intel 驱动程序的计划任务。该恶意软件使用唯一的受害者 ID 每 5 秒轮询一次 C2 服务器。

第四次攻击活动有所不同，它将 JSE 脚本嵌入到 ZIP 压缩包中。这些脚本使用诸如 certutil 和 rundll32 之类的内置工具来解码和执行 DLL 有效载荷。相比之下，另一次攻击活动则利用了 VSCode 的合法隧道功能来建立持久的远程访问。

## **Kimsuky 使用 LNK、JSE 诱饵**

根据 Logpresso 的说法，Kimsuky 攻击组织在 2026 年上半年开展的鱼叉式网络钓鱼活动，其特点是伪装主题、初始渗透途径和 C2 基础设施。

各个营销活动中一个显著的趋势是使用可信平台作为C2基础设施：

* 在第二阶段攻击中，GitHub 存储库被用来托管有效载荷和窃取系统数据，使流量看起来无害。
* 微软 CDN 在第四次活动中分发了正版 VSCode 二进制文件。
* VSCode隧道通过经过身份验证的GitHub会话实现了远程控制。
* 除了这些服务之外，还使用了传统的 C2 服务器（例如 103.67.196.25、yespp[.]co[.]kr）。

这种“依靠可信服务生存”的方法有助于绕过基于信誉的检测系统，并将恶意流量与正常的开发者活动混合在一起。

攻击者通过创建伪装成OneDrive 或 Intel 组件等合法服务的任务计划程序作业来建立持久性，这些作业配置为以 5 到 60 分钟的间隔执行。

他们利用无文件 PowerShell 技术，完全在内存中运行脚本，以规避基于磁盘的检测机制。

为了进一步掩盖他们的活动，他们采用了混淆方法，包括 Base64 编码、环境变量替换以及使用随机生成的变量名（通常以动物为主题）。

此外，有效载荷的投放会根据每个受害者的具体情况进行定制，使用诸如 UID、IP 地址或 MAC 地址之类的标识符，从而帮助恶意软件绕过沙箱分析并逃避检测。

在第三次攻击活动中，攻击者根据受害者的 MAC 地址动态生成有效载荷，确保只有预定的目标才能收到最终的恶意代码。

由于域名和文件名快速变化，传统的基于入侵指标（IOC）的检测方法已不足以应对威胁。然而，防御者可以关注行为指标：

* 执行包含嵌入数据的大型 LNK 文件（>10 KB）。
* 使用 PowerShell 隐藏窗口和 DownloadString 执行。
* 创建具有可疑名称和高权限的计划任务。
* 滥用 certutil、rundll32、wscript 和 curl。
* 网络流量指向 GitHub 原始 URL、VSCode 隧道或异常 POST 请求。

例如，如果一个系统在执行伪装成 OneDrive 的计划 PowerShell 任务时反复联系 GitHub 存储库，就应该立即引起怀疑。

这些攻击活动表明 Kimsuky 正在转向更隐蔽、更长期的入侵策略。通过结合鱼叉式网络钓鱼、合法工具滥用和自适应载荷投放，该组织显著降低了被发现的可能性。

建议各组织实施基于行为的检测，监控流程关系，并限制执行来自不受信任来源的脚本和 LNK 文件。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

安全圈的那点事儿

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/pcgSUGCDdKJ7zaD2SCDB9F4cHqDTEwJ6wULzhqNKntCMGN2NHYIx7TEicwiaxRTcQaBahVjqwpL96mEw0LBVMRAA/0?wx_fmt=png)

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