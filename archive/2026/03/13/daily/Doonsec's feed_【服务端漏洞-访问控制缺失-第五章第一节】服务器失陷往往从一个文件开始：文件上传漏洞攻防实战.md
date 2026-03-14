---
title: 【服务端漏洞-访问控制缺失-第五章第一节】服务器失陷往往从一个文件开始：文件上传漏洞攻防实战
url: https://mp.weixin.qq.com/s/lf7UZ_kOQQpuIjk4tEvZgA
source: Doonsec's feed
date: 2026-03-13
fetch_date: 2026-03-14T04:09:11.949512
---

# 【服务端漏洞-访问控制缺失-第五章第一节】服务器失陷往往从一个文件开始：文件上传漏洞攻防实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qg1MKHx3jGHDqGsiaz6DtUOueGhN0VCL2UH2wSnLqIa5ia42SopCn89wHVo6UmCVx9Fm5V360rkBFs05QOfqcDThibBHtwSoicqcMhF7ibgwicxvI/0?wx_fmt=jpeg)

# 【服务端漏洞-访问控制缺失-第五章第一节】服务器失陷往往从一个文件开始：文件上传漏洞攻防实战

原创

升斗安全XiuXiu
升斗安全XiuXiu

升斗安全

![]()

在小说阅读器中沉浸阅读

**【文章说明】**

* **目的**：本文内容仅为网络安全**技术研究与教育**目的而创作。
* **红线**：严禁将本文知识用于任何**未授权**的非法活动。使用者必须遵守《网络安全法》等相关法律。
* **责任**：任何对本文技术的滥用所引发的**后果自负**，与本公众号及作者无关。
* **免责**：内容仅供参考，作者不对其准确性、完整性作任何担保。

**阅读即代表您同意以上条款。**

在前面的第四章中[【服务端漏洞-访问控制缺失-第四章第三节】SSRF进阶：从“受限访问”到“内网横移”的实战绕过技巧](https://mp.weixin.qq.com/s?__biz=MjM5MzM0MTY4OQ==&mid=2447797961&idx=1&sn=a9b3b1e21dee9a1be3e22cf858b5e1de&scene=21#wechat_redirect)，我们分享了有关SSRF的相关漏洞原理以及利用方式。在接下来的第五章中，这边将给大家继续分享服务器漏洞中的另一个常见漏洞--文件上传漏洞

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VPUK6Jz75Q0n3licMnWvF5KickLjdxMmMicYkU0BvmCPHfDkGoMkibox7tZ9oSLHB7AbGmf3pYwRiaQ4XSHbBjvE7kA/640?wx_fmt=jpeg&from=appmsg)

在进实战挖掘之前，同样的，我们先要有理论的支撑，必须要先了解一下这些漏洞的一些原理和基本要点内容。如以下这些，就需要我们先知道一下：

首先，文件上传漏洞是什么？

文件上传漏洞是指 Web 服务器允许用户将文件上传到其文件系统时，未能充分验证文件的名称、类型、内容或大小等情况。如果未能对这些方面实施有效的限制，即使是一个基本的图片上传功能，也可能被利用来上传任意的、具有潜在危险性的文件。这类文件甚至可能包括能够实现远程代码执行的服务器端脚本文件。

在某些情况下，仅仅是上传文件这个行为本身就足以对服务器造成破坏。而其他攻击方式则可能涉及后续针对该文件的 HTTP 请求，通常是能够对已上传到服务器的文件或是脚本进行执行。

然后，文件上传漏洞是如何产生的？

鉴于其显而易见的危险性，现实中很多网站都会对用户上传的文件类型施加限制。更常见的情况是，开发人员实施了自认为足够强大的验证措施，但这些措施要么本身就存在缺陷，要么很容易被绕过。

例如，他们可能会尝试通过黑名单禁止危险的文件类型，但未能考虑到检查文件扩展名时存在的解析差异。与任何黑名单机制一样，也很容易意外遗漏某些不太常见但同样具有危险性的文件类型。

在其他情况下，网站可能会尝试验证某些属性来确定文件类型，但这些属性很容易被攻击者使用 Burp Proxy 或 Repeater 等工具进行篡改。

最终，即使是强大的验证措施，在构成网站的整个主机和目录网络中也未必能得到一致的应用，由此产生的差异就可能被利用。

最后，如何利用无限制文件上传部署 Web Shell？

从安全角度来看，最糟糕的情况是网站不仅允许你上传服务器端脚本文件（例如 PHP、Java 或 Python 文件），而且还将其配置为作为代码执行。这使得攻击者可以轻松地在服务器上创建自己的 Web Shell。

Web Shell？

Web Shell 是一种恶意脚本，它使攻击者只需向特定端点发送 HTTP 请求，就能在远程 Web 服务器上执行任意系统命令。

如果你能成功上传一个 Web Shell，你实际上就获得了对服务器的完全控制权。这意味着你可以读取和写入任意文件，窃取敏感数据，甚至利用该服务器作为跳板，对内部基础设施以及网络外部的其他服务器发起攻击。例如，以下这段 PHP 一句话代码可用于读取服务器文件系统中的任意文件：

```
<?php echo file_get_contents('/path/to/target/file'); ?>
```

上传此恶意文件后，向它发送请求，响应中就会返回目标文件的内容。

一个功能更通用的 Web Shell 可能如下所示：

```
<?php echo system($_GET['command']); ?>
```

这个脚本允许你通过查询参数传递任意系统命令，如下所示：

```
GET /example/exploit.php?command=id HTTP/1.1
```

好了，关于文件上传漏洞的基本原理和相关要点内容，就分享到这了。明天这边会结合这些理论，给大家分享一个实战的场景。感兴趣的话，欢迎搬凳关注，提前占位。

觉得文章对你有一丝启发或作用的话，一键三连（点赞、分享、关注），就是对我最大的鼓励，谢谢![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_64@2x.png)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

升斗安全

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/VPUK6Jz75Q3dczfibZoF9yHlbaEAZlyAIEESDEormKCrZ6rcbTRQJmoEue8IM2TYNQBALdCunnotXlsr8icWqvUg/0?wx_fmt=png)

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