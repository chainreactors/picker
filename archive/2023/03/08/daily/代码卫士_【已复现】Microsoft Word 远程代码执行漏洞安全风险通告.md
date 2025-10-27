---
title: 【已复现】Microsoft Word 远程代码执行漏洞安全风险通告
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247515830&idx=1&sn=62672aef02ae740d65e67ab95a5db18c&chksm=ea948fdcdde306ca7893363e26bd5bb43dd9943d0e2be4690cc6e385c40a5e449486bcb837a2&scene=58&subscene=0#rd
source: 代码卫士
date: 2023-03-08
fetch_date: 2025-10-04T08:55:28.325254
---

# 【已复现】Microsoft Word 远程代码执行漏洞安全风险通告

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4ibGgbTzxibBCVn4F71AXDTnic41y8x1tgKq7FyjozJNoom45iclK66gCumIq1JYKFD9RkicITs19FWBog/0?wx_fmt=jpeg)

# 【已复现】Microsoft Word 远程代码执行漏洞安全风险通告

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4icrhoWdKnhTgicSjB9pXdeZwDibNIBAEMegibEdG1vrjOibsq887TUz3ztMkM6Qvibic7r26sqbUIbicOMYg/640?wx_fmt=png "https://image.ipaiban.com/upload-ueditor-image-20201112-1605175807303084927.png")

奇安信CERT

**致力于**第一时间为企业级用户提供安全风险**通告**和**有效**解决方案。

**安全通告**

Microsoft Office Word是微软公司的一个文字处理器应用程序。Word给用户提供了用于创建专业而优雅的文档工具，帮助用户节省时间，并得到优雅美观的结果。一直以来，Microsoft Office Word 都是最流行的文字处理程序。

近日，奇安信CERT监测到**Microsoft Word 远程代码执行漏洞(CVE-2023-21716)** PoC在互联网上公开。Microsoft Word的RTF解析器（wwlib）中存在远程代码执行漏洞，未经身份认证的远程攻击者可通过发送的带有特制RTF文件的电子邮件，并诱导用户打开来利用此漏洞，成功利用此漏洞可能在目标系统上以该用户权限执行代码。该漏洞存在至少14年，使用预览窗格对文件进行预览也会触发此漏洞，Outlook预览窗格可作为此漏洞攻击媒介。**目前，奇安信CERT已复现此PoC。****鉴于此产品用量较大，建议客户尽快更新至最新版本。**

|  |  |  |  |
| --- | --- | --- | --- |
| **漏洞名称** | **Microsoft Word** **远程代码执行漏洞** | | |
| **公开时间** | 2023-02-14 | **更新时间** | 2023-03-07 |
| **CVE****编号** | CVE-2023-21716 | **其他编号** | QVD-2023-4358   CNNVD-202302-1110 |
| **威胁类型** | 代码执行 | **技术类型** | 越界读写 |
| **厂商** | Microsoft | **产品** | Word |
| **风险等级** | | | |
| **奇安信****CERT****风险评级** | | **风险等级** | |
| **高危** | | **蓝色（一般事件）** | |
| **现时威胁状态** | | | |
| **POC****状态** | **EXP****状态** | **在野利用状态** | **技术细节状态** |
| **已公开** | 未发现 | 未发现 | 已公开 |
| **漏洞描述** | Microsoft Word的RTF解析器（wwlib）中存在远程代码执行漏洞，攻击者可以制作包含过多字体表项的RTF文件，并诱导用户打开来利用此漏洞。攻击者可利用多种方式诱导用户下载并打开特制文档，如电子邮件、即时消息等等。用户使用预览窗格也会触发此漏洞。成功利用此漏洞可能在目标系统上以该用户权限执行代码。 | | |
| **影响版本** | SharePoint Server Subscription Edition Language Pack  Microsoft 365 Apps for Enterprise for 32-bit Systems  Microsoft Office LTSC 2021 for 64-bit editions  Microsoft SharePoint Server Subscription Edition  Microsoft Office LTSC 2021 for 32-bit editions  Microsoft Office LTSC for Mac 2021  Microsoft Word 2013 Service Pack 1 (64-bit editions)  Microsoft Word 2013 RT Service Pack 1  Microsoft Word 2013 Service Pack 1 (32-bit editions)  Microsoft SharePoint Foundation 2013 Service Pack 1  Microsoft Office Web Apps Server 2013 Service Pack 1  Microsoft Word 2016 (32-bit edition)  Microsoft Word 2016 (64-bit edition)  Microsoft SharePoint Server 2019  Microsoft SharePoint Enterprise Server 2013 Service Pack 1  Microsoft SharePoint Enterprise Server 2016  Microsoft 365 Apps for Enterprise for 64-bit Systems  Microsoft Office 2019 for Mac  Microsoft Office Online Server | | |
| **其他受影响组件** | 无 | | |

奇安信 CERT 已成功复现**Microsoft Word 远程代码执行漏洞(CVE-2023-21716)**，复现截图如下:

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibGgbTzxibBCVn4F71AXDTnichszpUMa4GFhyQh3gOmKgDhPCiaNE5dR7mGG8GDFrwp6SSDatpTM4vtw/640?wx_fmt=png)

威胁评估

|  |  |  |  |  |
| --- | --- | --- | --- | --- |
| **漏洞名称** | Microsoft Word 远程代码执行漏洞 | | | |
| **CVE****编号** | CVE-2023-21716 | **其他编号** | | QVD-2023-4358  CNNVD-202302-1110 |
| **CVSS 3.1****评级** | **高危** | **CVSS 3.1****分数** | | 8.8 |
| **CVSS****向量** | **访问途径（****AV****）** | | **攻击复杂度（****AC****）** | |
| 本地 | | 低 | |
| **所需权限（****PR****）** | | **用户交互（****UI****）** | |
| 不需要 | | 需要 | |
| **影响范围（****S****）** | | **机密性影响（****C****）** | |
| 不改变 | | 高 | |
| **完整性影响（****I****）** | | **可用性影响（****A****）** | |
| 高 | | 高 | |
| **危害描述** | 未经身份验证的远程攻击者在诱导受害者打开特制的RTF文档后，可执行任意代码。 | | | |

处置建议

**一、安全更新**

**使用奇安信天擎的客户可以通过奇安信天擎控制台一键更新修补相关漏洞，也可以通过奇安信天擎客户端一键更新修补相关漏洞。**

也可以采用以下官方解决方案来防护此漏洞：

**Office 手动更新**

1、打开任何 Office 应用（如 Word）并创建新文档。

2、点击“文件”>“账户”。

3、在“产品信息”下，选择“更新选项”>“立即更新”。

注意: 如果不能立即看到“立即更新”选项，可能需要先单击“启用更新”。

![](https://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ibGgbTzxibBCVn4F71AXDTnicAXMeMib080DYgVBvIicYjxv94ncrGnb4JgiaRcJRoQ8ByPnekojPH8TBA/640?wx_fmt=png)

4、Office 完成检查和安装更新后，关闭“已是最新版本!”窗口。

**二、缓解方案**

对于无法更新的用户，微软提供了以下缓解方案：

1、配置 Microsoft Outlook 阅读纯文本格式的电子邮件以降低用户打开来自未知或不受信任来源的 RTF 文件的风险。有关如何配置 Microsoft Outlook 以阅读所有纯文本标准邮件的指南，请参阅：https://support.microsoft.com/en-us/office/change-the-message-format-to-html-rich-text-format-or-plain-text-338a389d-11da-47fe-b693-cf41f792fefa

2、使用 Microsoft Office 文件阻止策略来防止Office 打开来自未知或不受信任来源的 RTF 文档。可能出现的问题是，已配置文件阻止策略但未配置白名单的用户将无法打开以 RTF 格式保存的文档，详情请参阅：https://learn.microsoft.com/en-us/office/troubleshoot/settings/file-blocked-in-office

**警告：**如果您不正确地使用注册表编辑器，可能会导致严重的问题，可能需要您重新安装操作系统。Microsoft不能保证您可以解决因注册表编辑器使用不当而导致的问题。使用注册表编辑器需要您自担风险。

1.以管理员身份运行regedit.exe并按版本导航到以下子项：

// Office 2013

[HKEY\_CURRENT\_USER\Software\Microsoft\Office\15.0\Word\Security\FileBlock]

// Office 2016、Office 2019 、Office 2021

[HKEY\_CURRENT\_USER\Software\Microsoft\Office\16.0\Word\Security\FileBlock]

2.将 RtfFiles DWORD 值设置为 2。

3.将 OpenInProtectedView DWORD 值设置为 0。

将以上子项中的RtfFiles DWORD 值设置为 0，可撤销此临时解决方案。

参考资料

[1]https://msrc.microsoft.com/update-guide/en-US/vulnerability/CVE-2023-21716

[2]https://support.microsoft.com/zh-cn/office/%E5%AE%89%E8%A3%85-office-%E6%9B%B4%E6%96%B0-2ab296f3-7f03-43a2-8e50-46de917611c5#ID0EBBBBF=%E8%BE%83%E6%96%B0%E7%89%88%E6%9C%AC

时间线

2023年3月7日，奇安信 CERT发布安全风险通告。

![](https://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQZeSribxs2yU1w56EMvgX9cDBCiabniazxdxtQ25cBCAd5vBJIM2sOv1khjzwwViaT0pS74U6piaiauiaGA/640?wx_fmt=png)

转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

点击**阅读原文**

到奇安信NOX-安全监测平台查询更多漏洞详情

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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