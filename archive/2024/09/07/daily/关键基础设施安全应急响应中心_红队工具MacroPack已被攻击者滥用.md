---
title: 红队工具MacroPack已被攻击者滥用
url: https://mp.weixin.qq.com/s?__biz=MzkyMzAwMDEyNg==&mid=2247545669&idx=3&sn=6fa39436a79a19e80944ad5a7cdc1ac1&chksm=c1e9bf14f69e36028b74abab7b186572ace48e206df80f1e552c3c2e4853a839dff831591e57&scene=58&subscene=0#rd
source: 关键基础设施安全应急响应中心
date: 2024-09-07
fetch_date: 2025-10-06T18:28:40.425157
---

# 红队工具MacroPack已被攻击者滥用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogtZ17otShtbHTC4iccVibXHVRIBNLutmr9DiaYianlaWvPficRMQZCuEAFTRQUkdCK0f2toXibyy3wxFErg/0?wx_fmt=jpeg)

# 红队工具MacroPack已被攻击者滥用

关键基础设施安全应急响应中心

据BleepingComputer消息，一款最初被设计为红队演练之用的工具MacroPack近来正被攻击者滥用并部署恶意负载 Havoc、Brute Ratel 和 PhatomCore ，所发现的恶意文档已涉及多个国家和地区。

MacroPack 是由法国开发人员 Emeric Nasi （dba BallisKit） 创建的专注于红队演习演练和对手模拟的专有工具，提供反恶意软件绕过、反逆技术、使用代码混淆构建各种文档有效负载、嵌入无法检测的 VB 脚本等多项高级功能。

Cisco Talos 的安全研究人员研究了来自美国、俄罗斯和巴基斯坦等国家和地区在 VirusTotal 上提交的恶意文档，这些文件的诱饵、复杂程度和感染载体各不相同，表明 MacroPack 正被多个攻击者滥用，已成为一种潜在的威胁趋势。

这些被捕获的野外样本都有在 MacroPack 上创建的痕迹，包括基于马尔可夫链的函数和变量重命名、删除注释和多余的空格字符（这些字符可将静态分析检测率降到最低）以及字符串编码。

当受害者打开这些恶意Office 文档时会触发第一级 VBA 代码，该代码会加载恶意 DLL，并连接到攻击者的命令和控制 (C2) 服务器。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38NgF4pibf9fXY1fwksPYG9BlDXcib5frSauWcXAEqVWo4Ht3LzkSsqicGCghZa08HUwAIXicxLEfnwgQ/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

攻击链

Cisco Talos 报告了一些与MacroPack 滥用相关的重要恶意活动集群：

> 美国：2023 年 3 月上传的一份文件伪装成加密的 NMLS 更新表格，并使用马尔可夫链生成的函数名来逃避检测。该文档包含多级 VBA 代码，在尝试通过 mshta.exe 下载未知有效载荷之前会检查沙盒环境。
>
> ![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR38NgF4pibf9fXY1fwksPYG9ByEKribv2mm1ZnHHnvuxkice0yhmKr7b6CyMTibD1FIXLC672YDjlkiaR1w/640?wx_fmt=jpeg&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)
>
> 装成加密的 NMLS 更新表格
>
> 俄罗斯：2024 年 7 月，一个俄罗斯 IP 上传的空白 Excel 工作簿提供了 PhantomCore，这是一个基于 Golang 的用于间谍活动的后门 。该文件运行多级 VBA 代码，试图从远程 URL 下载后门。
>
> 巴基斯坦：从巴基斯坦各地上传了以巴基斯坦军事为主题的文件。其中一份文件伪装成巴基斯坦空军的通知，另一份伪装成就业确认书，部署了 Brute Ratel 獾。这些文件通过 HTTPS DNS 和亚马逊 CloudFront 进行通信，其中一个文档嵌入了 base64 编码的 blob 以用于 Adobe Experience Cloud 跟踪。

BleepingComputer 已就观察到的滥用行为联系了开发者Emeric Nasi，但目前尚未收到回复。

原文来源：FreeBuf

“投稿联系方式：sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/iaz5iaQYxGogvC8qicuLNlkT5ibJnwu1leQiabRVqFk4Sb3q1fqrDhicLBNAqVY4REuTetY1zBYuUdic0nVhZR4FHpAfg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

预览时标签不可点

阅读原文

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