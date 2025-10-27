---
title: 探讨Windows SeRelabelPrivilege特权滥用的危害
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247508163&idx=1&sn=731dd45dcfbf1c49ad5be3f3c8ce4f56&chksm=fa52757dcd25fc6b532a569960d5253c87cbf01fa85ac2343e6bfa9c1b99a7ff1d1adde98d5a&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-09-10
fetch_date: 2025-10-06T18:28:58.019456
---

# 探讨Windows SeRelabelPrivilege特权滥用的危害

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnQVeCzh27xv2Jv6GMABLLTyiavpbTtia1bicNkia7X0ibaylTVtYGbWAUOlq42zWdCVyUHvHMCzUJCk9lw/0?wx_fmt=jpeg)

# 探讨Windows SeRelabelPrivilege特权滥用的危害

原创

th1e

山石网科安全技术研究院

#

今天我们来探讨一个近期在安全评估中发现的有趣问题——SeRelabelPrivilege 的滥用。这个特权在某些组策略中被授予了内置的 Users 组，并应用于多个计算机账户。对这种特权我感到非常好奇，因此决定深入研究其潜在影响和可能的滥用场景。

根据微软的文档，拥有 SeRelabelPrivilege 权限的用户可以改变文件或进程的完整性级别，从而提升或降低其安全性。

我决定进行实验来探究这个特权的实际效果。首先，我通过组策略将 SeRelabelPrivilege 分配给一个标准用户：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQVeCzh27xv2Jv6GMABLLTy7BdunnsJtCgpeysDoRwfNbTODCXlXa0JajLo8kINkZn0BfBmonPo9w/640?wx_fmt=png)

发现该特权只在高完整性级别下可用。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQVeCzh27xv2Jv6GMABLLTyOCn51StXHdMvfPVl8bMyEHGnzoPuNXEX42XKcwia7PpfiasoqNza7ib8Q/640?wx_fmt=png)

经过一系列测试，我发现这个特权实际上允许用户获取资源的所有权，包括那些完整性级别比用户更高的资源。

获得所有权后，用户可以赋予自己对资源的完全控制，这与滥用 SeDebugPrivilege 的效果类似。

我的目标是取得 SYSTEM 进程的所有权，授予自己完全控制权，然后在 NT AUTHORITY\SYSTEM 账户下创建一个进程。

为此，我创建了一个简单的概念验证（POC）：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQVeCzh27xv2Jv6GMABLLTyGETMUb7ibemASMd5q91R2SS2jLAAaVT68jh0TP1xe73wU1MsO0wjjSA/640?wx_fmt=png)

首先，我需要获取当前用户 SID 并启用特定权限：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQVeCzh27xv2Jv6GMABLLTyiaLvK3w646zndw7ibKzk6TBjN48lldempqygNuBL7QxwcRCHFh7iapeFQ/640?wx_fmt=png)

这里需要以WRITE\_OWNER访问权限打开该进程。在 SetSecurityInfo 调用中，这里必须要有“LABEL\_SECURITY\_INFORMATION”标志，否则就无法拥有高级别的进程。

一旦获得了所有权，就可以完全控制该进程：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQVeCzh27xv2Jv6GMABLLTySLwzsmGibBHerrDRbG9vAXe5yY4GuhVbkibibllqgCicbayJKfw4lz4Uuw/640?wx_fmt=png)

上面我们通过一段简单的实验代码成功地获取了 SYSTEM 进程的所有权，并在 NT AUTHORITY\SYSTEM 帐户下创建了一个新进程。

接下来让我们看看它是否有效。

这里7116 是 winlogon 进程，它在系统完整性下运行，归 SYSTEM 所有：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQVeCzh27xv2Jv6GMABLLTyNCuxxjVQprq6icdroRm8JyF0kJsCcwFxGO0ibJ3kcWvW0P3Uwch0RjAQ/640?wx_fmt=png)

所有权已更改，并成功授予了完全控制权：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQVeCzh27xv2Jv6GMABLLTyp2ib1CBTG38Z2phEcvWDhkBNTQHFvNbHgylBx7l1N1tctkKqoaSMCcQ/640?wx_fmt=png)

那么这里滥用这个功能的最简单方法是执行父进程注入。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQVeCzh27xv2Jv6GMABLLTyTeuFrpOfZU4BDicSibgYgT3wricA9m9l9Z9D7tmM6aHf6ib7D3Wrx5JFZQ/640?wx_fmt=png)

最终获得 SYSTEM 访问权限。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQVeCzh27xv2Jv6GMABLLTyMMkxCMXYaR6ibUxDu0Bb6GqmvjAw5US0KP2YPQqgU8xREM38a9lrj4A/640?wx_fmt=png&from=appmsg)

**结论**

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnQVeCzh27xv2Jv6GMABLLTyMMkxCMXYaR6ibUxDu0Bb6GqmvjAw5US0KP2YPQqgU8xREM38a9lrj4A/640?wx_fmt=png&from=appmsg)

总结来说，SeRelabelPrivilege 允许用户即使在完整性级别更高的情况下也能获取资源的所有权，并赋予自己完全访问权限。这种特权的滥用结果与 Debug Privilege 十分相似，而微软为何实现这一特权仍然是一个谜。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

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