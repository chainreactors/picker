---
title: ChatGPT漏洞允许攻击者静默窃取用户提示和其他敏感数据
url: https://mp.weixin.qq.com/s/H7cmOrQrOSS0okqLPRL5Ow
source: Doonsec's feed
date: 2026-03-31
fetch_date: 2026-04-01T04:44:48.988004
---

# ChatGPT漏洞允许攻击者静默窃取用户提示和其他敏感数据

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7NSZFzLELsMOToJR6o5XMFoq1Za5cmko0I3sa8DexJpgvB2njLziaHRJ7pSnBokAH3HqWzngCyop1RTJTZCKyzyhAuKS1oV2Na0/0?wx_fmt=jpeg)

# ChatGPT漏洞允许攻击者静默窃取用户提示和其他敏感数据

原创

网络安全9527
网络安全9527

安全圈的那点事儿

![]()

在小说阅读器中沉浸阅读

用户经常将高度敏感的信息（包括医疗记录、财务文件和专有业务代码）托付给人工智能助手。

Check Point Research 最近披露了ChatGPT 架构中的一个严重漏洞，该漏洞允许攻击者悄无声息地提取此类用户数据。

通过滥用 ChatGPT 隔离代码执行环境中的隐蔽出站通道，攻击者可以提取聊天记录、上传的文件和AI 生成的输出，而不会触发用户警报或同意提示。

## **绕过出站安全措施**

OpenAI 将基于 Python 的数据分析环境设计成一个安全的沙箱，有意阻止直接的出站 HTTP 请求，以防止数据泄露。

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7PYwbT5pVTaAcRM3YN0xURIiaJv8ySXelOSGX0JhEsnM33NNa2pJPAPREicE2Bzb1WLFiaE9dpHHyQicYsmKsclGDpP7hicNQWoHMhE/640?wx_fmt=jpeg)

合法的外部 API 调用（称为 GPT 操作）需要通过可见的批准对话框获得用户的明确同意。

然而，研究人员发现了一种完全依赖DNS隧道技术的绕过方法。虽然传统的互联网访问被阻止，但容器环境仍然允许标准的DNS解析。

攻击者利用这一漏洞，将敏感用户数据编码到 DNS 子域名标签中。

该漏洞利用程序并非仅仅使用 DNS 进行 IP 名称解析，而是将数据（例如解析后的医疗诊断或财务摘要）分割成安全的片段。

当运行时执行递归查找时，解析器链会将编码后的数据直接传输到攻击者控制的外部服务器。

由于系统无法将 DNS 流量识别为外部数据传输，因此绕过了所有用户中介。

## **将自定义 GPT 武器化**

该攻击只需极少的用户交互，并且只需一个恶意提示即可发起。

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7NjGLibibick8QnYA5g2MooysSic8ANoAQSa3JTZFGmTfkiam3pgHOMI9lOv8j7Q3jxyPaM3F2248Nj2sMXS86r53ME4aB0nZ7ibibyl8/640?wx_fmt=jpeg)

威胁行为者可以通过公共论坛或社交媒体传播这些有效载荷，将其伪装成生产力提升技巧或越狱工具，以解锁 ChatGPT 的高级功能。

用户一旦将提示粘贴到聊天窗口中，当前的对话就会无缝地变成一个隐蔽的数据收集渠道。此外，攻击者还可以将恶意逻辑直接嵌入到自定义 GPT 中。

如果用户与植入后门的 GPT 进行交互，例如模拟“私人医生”分析上传的医疗 PDF 文件，系统会秘密提取高价值的标识符和评估结果。

由于 GPT 开发者官方无法访问个人用户的聊天记录，因此该侧通道提供了一种隐蔽的机制来收集私人工作流程。

如果被直接询问，人工智能甚至会自信地否认向外部发送数据，从而维持完全的隐私假象。

![](https://mmbiz.qpic.cn/mmbiz_jpg/BicXBAdicJy7NL4KzJsGPLqXa3G2qeCeV8BQBeBg66jcFmjfMictX07hYoYZekna6Z8e17RQicGSZV2wYHSj51BzqLGEu107CyibjKUTaZs4rxYw/640?wx_fmt=jpeg)

该漏洞的影响远远超出了被动数据窃取，它提供了运行时和攻击者之间的双向通信通道。

由于威胁行为者可以将命令片段编码到 DNS 响应中，因此他们可以将原始指令发送回隔离的沙箱。

容器内运行的进程可以重新组装这些有效载荷并执行它们，从而有效地为攻击者提供Linux 环境中的远程 shell。

根据 Checkpoint 的研究，这种攻击方式绕过了标准的安全机制，命令和结果在聊天界面中保持不可见，导致用户完全没有意识到攻击已被攻破。

OpenAI 于 2026 年 2 月 20 日成功修复了根本问题，关闭了 DNS 隧道。

然而，这一事件完美地凸显了现代人工智能助手在发展成为复杂的多层执行环境的过程中，其攻击面不断扩大的问题。

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