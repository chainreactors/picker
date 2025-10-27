---
title: Windows 版 WhatsApp 允许 Python、PHP 脚本在没有任何提示下执行
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545166&idx=3&sn=3dda66cbf3b9470b3e902372d6bfb186&chksm=c1e9bd1ff69e34099d6d572c32488457c21a6365891948d77fb7aa9b3a72ff0dbcd43e1074bf&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-08-01
fetch_date: 2025-10-06T18:04:59.878083
---

# Windows 版 WhatsApp 允许 Python、PHP 脚本在没有任何提示下执行

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogu2R67necpnyIv2DiacMA7VXuqaXiceCBkvO5pEEfEgKZGMBxkiauYKtJwDiamvxfDuMzTCTXcM71r9Yw/0?wx_fmt=jpeg)

# Windows 版 WhatsApp 允许 Python、PHP 脚本在没有任何提示下执行

关键基础设施安全应急响应中心

WhatsApp for Windows 最新版本中存在一个安全问题，允许发送 Python 和 PHP 附件，当收件人打开这些附件时，这些附件会在没有任何警告的情况下执行。要成功攻击，需要安装 Python，这一先决条件可能会将目标限制在软件开发人员、研究人员和高级用户。

该问题与 4 月份影响 Windows 版 Telegram 的问题类似，该问题最初被拒绝但后来得到修复，攻击者可以在通过消息传递客户端发送 Python .pyzw 文件时绕过安全警告并执行远程代码执行。

WhatsApp 屏蔽了多种被认为对用户有风险的文件类型，但该公司不打算将 Python 脚本添加到列表中且PHP 文件 (.php) 也不包含在 WhatsApp 的阻止列表中。

# **Python、PHP 脚本未被阻止**

安全研究员 Saumyajeet Das 在试验可以附加到 WhatsApp 对话中的文件类型时发现了此漏洞，以查看该应用程序是否允许任何有风险的文件。当发送潜在危险的文件（例如 .EXE）时，WhatsApp 会显示该文件并为收件人提供两个选项：打开或另存为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28VOlHIkbj1uFLMhwqZlKQ9YHav8RRyDnQkeOG2Coz9gnZAt70ErLRVAiaibsWhhedbrlbSsibUaYkHw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

WhatsApp 的可执行文件选项

但是，当尝试打开文件时，WhatsApp for Windows 会生成错误，用户只能选择将文件保存到磁盘并从那里启动它。在测试中，使用 WhatsApp for Windows 客户端时，此行为与 .EXE、.COM、.SCR、.BAT 和 Perl 文件类型一致。Das 发现 WhatsApp 还会阻止 .DLL、.HTA 和 VBS 的执行。

对于所有这些程序，当尝试通过单击“打开”直接从应用程序启动它们时，都会发生错误，只有先保存到磁盘后才能执行它们。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28VOlHIkbj1uFLMhwqZlKQ9WkB0kZ1zFP6TmAgmFnPvr6g8mJ6cxvw72GWDwPYjEpBqCEzIPfkcNQ/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

从 WhatsApp 客户端启动 .EXE 失败

Das 在接受采访时表示，他发现 WhatsApp 客户端不会阻止三种文件类型启动：.PYZ（Python ZIP 应用程序）、.PYZW（PyInstaller 程序）和 .EVTX（Windows 事件日志文件）。

测试证实，WhatsApp 不会阻止 Python 文件的执行，并发现 PHP 脚本也会发生同样的情况。

如果所有资源都存在，接收者只需单击接收文件上的“打开”按钮，脚本就会执行。

Das 于 6 月 3 日向 Meta 报告了该问题，该公司于 7 月 15 日回复称，另一位研究人员已经报告了该问题。目前。该漏洞仍然存在于适用于 Windows 的最新 WhatsApp 版本中，我们可以在 Windows 11 v2.2428.10.0 上对此多加注意。

有关媒体企图联系 WhatsApp，以澄清驳回研究人员报告的原因，一位发言人解释说，他们不认为这是他们的问题，因此没有修复计划。

该公司代表解释说，WhatsApp 有一个系统，当用户收到不在其联系人列表中的用户或电话号码在其他国家/地区注册的用户发送的消息时，会发出警告。然而，如果用户的帐户被劫持，攻击者可以向联系人列表中的每个人发送恶意脚本，这些脚本更容易直接从消息应用程序中执行。

此外，这些类型的附件可能会发布到公共和私人聊天组中，威胁者可能会滥用这些聊天组来传播恶意文件。在回应 WhatsApp 拒绝该报告时，Das 对该项目处理这种情况的方式表示失望。

其实只需将 .pyz 和 .pyzw 扩展名添加到阻止列表中，Meta 便可以阻止通过这些 Pythonic zip 文件进行的潜在攻击。通过解决该问题，WhatsApp 不仅可以增强其用户的安全性，还可以表明他们致力于迅速解决安全问题的良好态度。

有关媒体联系了 WhatsApp，提醒他们 PHP 扩展也没有被阻止，但目前尚未收到其回复。

**参考及来源：**

https://www.bleepingcomputer.com/news/security/whatsapp-for-windows-lets-python-php-scripts-execute-with-no-warning/

原文来源：中国信息安全

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

关键基础设施安全应急响应中心

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/iaz5iaQYxGogvgetLSfCMn2pt4xU0Fs6mWM4P98FUya5sz3BvAIzZam7WzZ5aA1kWkKBicptwLzVRicaqAhZ1pceiaA/0?wx_fmt=png)

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