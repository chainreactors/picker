---
title: 攻击者开始使用CHATGPT技术发起攻击
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247558493&idx=2&sn=61842befbdf65ffe782bedfc67dffe42&chksm=e9143567de63bc71d91681ad4adcb57abaff3e1e48d52850041e7d8086345b41dccbbdb01335&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-03-11
fetch_date: 2025-10-04T09:16:34.709578
---

# 攻击者开始使用CHATGPT技术发起攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9rsCPPNMUYTibMa8ov9jCE3dxtXEym90WqcLlJcBI6cQpWhxPNcvSOYug/0?wx_fmt=jpeg)

# 攻击者开始使用CHATGPT技术发起攻击

lucywang

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9r7P7nUkEl8WZO6aAjerSl859q10ZLkV1ibPibsOxGYT58Tib5Jj0TbXh5Q/640?wx_fmt=png)

2022年11月底，OpenAI发布了用于其大型语言模型（LLM）的新界面ChatGPT，这立即引发了人们对AI及其可能用途的关注。这就意味着，ChatGPT也可以被应用到现代网络攻击，因为代码生成可以帮助技术不太熟练的攻击者毫不费力地发动网络攻击。

在上一篇文章《爆火出圈的chatGPT如何在逆向和恶意软件分析中发挥作用》中，我们描述了ChatGPT如何成功地进行了完整的感染流程，从创建令人信服的鱼叉式钓鱼电子邮件到运行能够接受英语命令的反向shell。目前的问题是，这是否只是一个假设的威胁，或者是否已经有攻击者使用OpenAI技术进行恶意攻击了。

CPR对几个主要地下黑客社区的分析表明，已经有攻击者使用OpenAI开发恶意工具了。正如我们所怀疑的，一些示例清楚地表明，许多使用OpenAI的攻击者根本没有开发技能。尽管我们在本报告中介绍的工具非常基础，但基于AI的工具改在成复杂的威胁只是时间问题。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9rOPspgqY0icv9BPHjUrKqJZib9mkssvgJmYjmDGvpwMrGVmocuHwmChOA/640?wx_fmt=png)示例1：创建Infostealer

2022年12月29日，一个名为“ChatGPT——恶意软件的好处”的帖子出现在一个流行的地下黑客论坛上。该帖子的发布者透露，他正在使用ChatGPT进行实验，以重现在那些被报道过的攻击技术。为此，他分享了一个基于Python的窃取器的代码，它搜索常见的文件类型，将它们复制到Temp文件夹中的一个随机文件夹中，将它们压缩并上传到硬编码的FTP服务器。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9rx6zkEicq5CIMe5shvbPWeqUPNicwbIbmPc9IMJSsXcJbg1HGfZXl8vqQ/640?wx_fmt=png)

攻击者展示他如何使用ChatGPT创建infostealer

我们对示例的分析证实了攻击者的说法，这确实是一个很简单的窃取器，它在整个系统中搜索12种常见的文件类型，如MS Office文档、PDF和图像。如果发现任何感兴趣的文件，恶意软件会将这些文件复制到一个临时目录中，将其压缩并通过网络发送。值得注意的是，攻击者并没有对文件进行加密或安全地发送，因此这些文件也可能落入第三方手中。

这个攻击者使用ChatGPT创建的第二个示例是一个简单的Java代码片段。它下载PuTTY(一种非常常见的SSH和telnet客户端)，并使用Powershell在系统上秘密运行它。当然，可以修改此脚本以下载和运行任何程序，包括常见的恶意软件家族。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9rrbYxLWzTlSg2MEWPOwGO3rPyllYvAywZuQjqlGb5E7Aqoaq1MLt9Dw/640?wx_fmt=png)

证明他如何创建Java程序下载PuTTY，并使用Powershell运行它

该攻击者之前的论坛也共享过几个脚本，比如后利用阶段的自动化，以及一个试图钓鱼获取用户凭据的c++程序。此外，他还积极分享SpyNote的破解版本，这是一款Android RAT恶意软件。因此，总的来说，他似乎是一个以技术为导向的攻击者，他的帖子旨在向技术能力较弱的攻击者展示如何利用ChatGPT进行恶意攻击，并提供他们可以立即使用的真实示例。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9rOPspgqY0icv9BPHjUrKqJZib9mkssvgJmYjmDGvpwMrGVmocuHwmChOA/640?wx_fmt=png)示例2：创建加密工具

2022年12月21日，一位名叫USDoD的攻击者发布了一个Python脚本，他强调这是他创作的第一个脚本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9rsdib0szWcnjZWBCbp7z4iasM6PoTr7iaYRmpMnfReicicD8uYFwj5fIStiag/640?wx_fmt=png)

被称为USDoD的攻击者发布的多层加密工具

当另一名攻击者评论代码的风格类似于openAI代码时，USDoD证实openAI给了他一个“很好的帮助，以一个很好的范围完成脚本。”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9rgafQkGGgia9Tm2eBZgqPogOyne5iaDQ1PtlpEpRVd1DOpR9BluWrdjyQ/640?wx_fmt=png)

确认多层加密工具是使用Open AI创建的

我们对脚本的分析验证了它是一个执行加密操作的Python脚本。更具体地说，它实际上是不同签名、加密和解密功能的大杂烩。乍一看，该脚本似乎是良性的，但它实现了多种不同的功能：

脚本的第一部分生成用于签名文件的加密密钥（具体使用椭圆曲线密码和曲线ed25519）；

脚本的第二部分包括一些函数，这些函数使用硬编码的密码以混合模式同时使用Blowfish和Twofish算法对系统中的文件进行加密。这些函数允许用户加密特定目录或文件列表中的所有文件。

该脚本还使用RSA密钥，使用PEM格式的证书，MAC签名和blake2哈希函数来比较哈希值等。

需要注意的是，加密函数的所有解密对应项也都在脚本中实现。该脚本包括两个主要函数：一个用于加密单个文件并将消息认证码（MAC）附加到文件末尾，另一个加密硬编码路径并解密其作为参数接收的文件列表。

当然，上述所有代码都可以良性使用。然而，可以很容易地修改此脚本，以完全加密某人的计算机，而无需任何用户交互。例如，如果脚本和语法问题得到解决，它可能会将代码变成勒索软件。

虽然USDoD似乎不是一个开发人员，技术技能有限，但他是地下社区中一个非常活跃且声望很高的成员。USDoD从事各种非法活动，包括出售被入侵公司和被盗数据库的访问权。USDoD最近共享的一个著名被盗数据库据称是泄露的InfraGard数据库。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9rWX0BYCaFgbPIt0lD6T81zZCiaicic8atnzVFsEkdDy44topo7kQuOOCOQ/640?wx_fmt=png)

USDoD之前涉及发布InfraGard数据库的非法活动

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9rOPspgqY0icv9BPHjUrKqJZib9mkssvgJmYjmDGvpwMrGVmocuHwmChOA/640?wx_fmt=png)示例3：使用ChatGPT进行欺诈活动

另一个使用ChatGPT进行欺诈活动的示例是在2022年新年前夕发布的，它展示了一种不同类型的网络犯罪活动。虽然前两个示例更多地关注于面向恶意软件的ChatGPT使用，但本示例显示了一个标题为“滥用ChatGPT创建暗网市场脚本”的讨论。在这篇文章中，攻击者展示了使用ChatGPT创建暗网市场是多么容易。该市场在地下非法经济中的主要作用是提供一个平台，用于自动交易非法或被盗物品，如被盗账户或支付卡，恶意软件，甚至毒品和弹药，所有支付都使用加密货币。为了说明如何使用ChatGPT实现这些目的，攻击者发布了一段代码，该代码使用第三方API来获取最新的加密货币(门罗币、比特币和以太坊)价格，作为暗网市场支付系统的一部分。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9rKulaxPd0diaN5O29EoM2m0IfY1JVucKyIdjsqyCp4QwMFzywJAAMY1w/640?wx_fmt=png)

攻击者使用ChatGPT创建暗网市场脚本

2023年初，几个攻击者在其他地下论坛上展开了讨论，讨论的重点是如何将ChatGPT用于欺诈攻中。其中大部分集中于使用另一种OpenAI技术（DALLE2）生成随机艺术品，并通过Etsy等合法平台在线销售。在另一个示例中，攻击者解释如何为特定主题生成电子书或短章节(使用ChatGPT)，并在网上销售这些内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9rrNKY8LAaQ9vnFypAql03pJ18gFgQkyw8B1oV2OnEJRuXsGNMomcjrA/640?wx_fmt=png)

地下论坛中关于如何使用ChatGPT进行欺诈活动的多个线程

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9rOPspgqY0icv9BPHjUrKqJZib9mkssvgJmYjmDGvpwMrGVmocuHwmChOA/640?wx_fmt=png)总结

现在就认定ChatGPT功能是否会成为暗网攻击者最喜欢的新工具还为时过早。然而，生成恶意代码的新趋势已经出现。

参考及来源：https://research.checkpoint.com/2023/opwnai-cybercriminals-starting-to-use-chatgpt/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9ryDzjHMrFkzn8GELqW0tz1ic4GCHDajiaxewhyNn1wMkMh3h0Ku31kXAg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o28hZiaQmnmDrHUrODd8cWn9rDF45lsLGYvwDvOiaxpYr4hfD8wdhicsSPtDrkeCL4R90CFOsGicvouGsw/640?wx_fmt=png)

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