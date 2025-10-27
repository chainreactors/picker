---
title: 新工具绕过 Google Chrome 的新 cookie 加密系统
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247579412&idx=1&sn=16268b8027a67526ced4e3122679245f&chksm=e914672ede63ee38ff250b9dc27bdb490f3ac4bb7c69eeae26dbe76579ca2db1d405a72dd109&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2024-11-06
fetch_date: 2025-10-06T19:19:40.593031
---

# 新工具绕过 Google Chrome 的新 cookie 加密系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2915AHHE7HdmZWv7PM76EaU9oC0bfzyXARPNLTkxOmIZ3l4Gib2q8t1wLUH98HibSDJJHacn1IM6pjw/0?wx_fmt=jpeg)

# 新工具绕过 Google Chrome 的新 cookie 加密系统

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

近期，研究人员发布了一种工具，可以绕过 Google 新的 App-Bound 加密 cookie 盗窃防御，并从 Chrome 网络浏览器中提取保存的凭据。

该工具名为“Chrome-App-Bound-Encryption-Decryption”，由网络安全研究员 Alexander Hagenah 发现，其他人已经在找出类似的绕过方法。

尽管该工具实现了多个信息窃取者操作已添加到其恶意软件中的功能，但其公开可用性增加了继续在浏览器中存储敏感数据的 Chrome 用户的风险。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2915AHHE7HdmZWv7PM76EaUop5sdwIMQpvZ26TsTPsfzWwXRaGvQUbaGxnckUIOFovV3EsovUv8xw/640?wx_fmt=png&from=appmsg)Google 的应用程序绑定加密问题

Google 在 7 月份推出了应用程序绑定（App-Bound）加密（Chrome 127）作为一种新的保护机制，该机制使用以 SYSTEM 权限运行的 Windows 服务来加密 cookie。

其目标是保护敏感信息免受 infostealer 恶意软件的侵害，该恶意软件在登录用户的权限下运行，使其无法在没有首先获得系统权限的情况下解密被盗的 cookie，并可能在安全软件中发出警报。

谷歌在 7 月份曾解释：“由于 App-Bound 服务是以系统权限运行的，攻击者需要做的不仅仅是诱骗用户运行恶意应用程序。现在，恶意软件必须获得系统权限，或者将代码注入 Chrome，这是合法软件不应该做的事情。”

然而，到了 9 月份，多个信息窃取者已经找到了绕过新安全功能的方法，并为他们的网络犯罪客户提供了再次窃取和解密 Google Chrome 敏感信息的能力。

信息窃取者开发人员与其工程师之间的“猫捉老鼠”游戏一直是意料之中，谷歌从未认为自己的防御机制会是无懈可击的。相反，随着应用程序绑定加密的引入，他们希望最终能为逐步构建更健全的系统奠定基础。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2915AHHE7HdmZWv7PM76EaUop5sdwIMQpvZ26TsTPsfzWwXRaGvQUbaGxnckUIOFovV3EsovUv8xw/640?wx_fmt=png&from=appmsg)公开绕过

昨天，Hagenah 在 GitHub 上提供了他的 App-Bound 加密绕过工具，并共享源代码，允许任何人学习和编译该工具。

该工具使用 Chrome 内部基于 COM 的 IElevator 服务，解密存储在 Chrome 本地状态文件中的应用程序绑定加密密钥。提供了一种检索和解密这些密钥的方法，Chrome 通过应用程序绑定加密 (ABE) 来保护这些密钥，以防止未经授权访问 Cookie 等安全数据（以及未来可能的密码和支付信息）。

要使用该工具，用户必须将可执行文件复制到 Google Chrome 目录中，该目录通常位于 C:\Program Files\Google\Chrome\Application。

该文件夹受保护，因此用户必须首先获得管理员权限才能将可执行文件复制到该文件夹。

然而，这通常很容易实现，因为许多 Windows 用户（尤其是消费者）使用具有管理权限的帐户。

就其对 Chrome 安全性的实际影响而言，研究人员 g0njxa 表示，Hagenah 的工具展示了一种大多数信息窃取者现在已经超越的基本方法，可以从所有版本的 Google Chrome 中窃取 cookie。eSentire 恶意软件分析师也证实，Hagenah 的方法看起来与谷歌首次在 Chrome 中实施应用程序绑定加密时信息窃取者所采用的早期绕过方法类似。

Lumma 也使用了这种方法——通过 COM 实例化 Chrome IElevator 接口来访问 Chrome 的 Elevation Service 来解密 cookie，但这可能会非常嘈杂且易于检测。现在，他们使用间接解密，而不直接与 Chrome 的高程服务交互。

不过，g0njxa 评论称，谷歌仍未赶上，因此使用新工具可以轻松窃取 Chrome 中存储的用户机密。

为了响应该工具的发布，Google 表示此代码 [xaitax] 需要管理员权限，这也表明已经成功提高了实现此类攻击所需的访问量。

虽然确实需要管理员权限，但它似乎并没有影响信息窃取恶意软件操作，这些恶意软件操作在过去六个月中只增加了，通过零日漏洞、对 GitHub 问题的虚假修复，甚至对堆栈溢出。

参考及来源：https://www.bleepingcomputer.com/news/security/new-tool-bypasses-google-chromes-new-cookie-encryption-system/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2915AHHE7HdmZWv7PM76EaUwpkaUZaWxvelCjMcIFdpzdV9ZjYffIW0LibKtKHtflE5icHEUQwCSO5A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2915AHHE7HdmZWv7PM76EaUnmLo2K7IiaG9loyCx502XGdv6DVYfdjibsJuzGgtQDLJFzoD2Zp6VIOA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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