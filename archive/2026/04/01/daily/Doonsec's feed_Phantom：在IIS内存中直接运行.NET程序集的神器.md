---
title: Phantom：在IIS内存中直接运行.NET程序集的神器
url: https://mp.weixin.qq.com/s/JZqnlP1GEJ8pAGo4iMmB4Q
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:22:49.772345
---

# Phantom：在IIS内存中直接运行.NET程序集的神器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tbTbtBE6Tibe2Lib8qmaDkBAZXVbAL8QoFjGhpOaGibeVNiasB4ZOmPyPXuNpia2CUV7H24A5ribiawKUkxrCn64CfpEM3XXtNVlAdKJtLd9FkAB9s/0?wx_fmt=jpeg)

# Phantom：在IIS内存中直接运行.NET程序集的神器

幻泉之洲

![]()

在小说阅读器中沉浸阅读

> 面对需要上传文件到Web服务器的传统WebShell方式，Phantom提供了另一种思路：它能在IIS工作进程的内存中直接加载和执行.NET程序集，实现无文件驻留，更适合渗透测试中的隐蔽行动。

## 工具是什么？

简单来说，Phantom是一个能在IIS服务器上搞“无文件攻击”的工具。它针对的是那些运行在“完全信任”模式下的ASP.NET网站。

以前你想在服务器上跑点自己的代码，总得想办法传一个.aspx文件或者DLL上去。Phantom绕开了这步。它不依赖物理文件，而是用反射加载的技术，直接把一个.NET的程序集（DLL）塞进IIS工作进程 w3wp.exe 的内存里执行。

这样，你的操作只发生在内存中，服务器硬盘上不会留下任何直接的恶意文件，隐蔽性提高了一个档次。

## 核心怎么运作？

它的机制不算复杂，但挺巧妙。

* **目标环境**

  ：必须是IIS，并且托管的应用池配置为“完全信任”模式。这是.NET Framework环境下运行代码的最高权限级别。
* **执行载体**

  ：你的代码需要预先编译成一个.NET的DLL文件。这个DLL就是你想在目标服务器上执行的功能。
* **加载方式**

  ：Phantom自身作为一个Web应用被部署（或利用），它利用.NET的 `Assembly.Load(byte[])` 这类方法，将DLL文件的字节数组直接从内存中加载起来。
* **注入进程**

  ：加载和执行的整个过程，都发生在IIS的工作进程 w3wp.exe 的内存空间内。你的DLL不会以文件形式出现在服务器的任何目录里。

说白了，就是把传统需要落地的WebShell，变成了一个只在内存里活的“幽灵”。

## 优势与短板

任何工具都有适用场景。

### 它好在哪里？

* **无文件**

  ：最大的优点。规避了基于文件特征的静态扫描，也减少了被管理员在磁盘上直接发现的概率。
* **隐蔽性高**

  ：你的代码寄生在合法的IIS进程中，只要IIS在跑，你的代码就在跑，进程列表看起来正常。
* **兼容性**

  ：基于标准的.NET反射机制，理论上能运行任何符合.NET框架的编译后代码。

### 它的限制在哪？

* **依赖特定环境**

  ：必须得是IIS + .NET Framework完全信任模式。对于IIS Express、非完全信任的应用池，或者.NET Core/5+的环境（它们默认架构不同），这工具可能就失效了。
* **非持久化**

  ：内存驻留意味着一旦IIS应用池回收或服务器重启，你的代码就没了。需要依赖其他手段实现持久化。
* **需要初始入口**

  ：你怎么把Phantom本身或者触发它的代码传上去？这仍然需要一个最初的漏洞或上传点。它解决的是执行阶段的问题，不是初始渗透问题。

## 谁适合用？

主要面向渗透测试人员和红队成员。在对内网进行攻防演练时，如果你已经通过某种方式（比如文件上传漏洞）在一个IIS服务器上拿到了初始立足点，想要更隐蔽地部署一个后门或横向移动工具，Phantom会是一个值得考虑的选项。

对于蓝队和防守方来说，了解这种技术也很有必要。这意味着防御不能只盯着磁盘上的文件，还需要监控内存中的异常程序集加载、IIS工作进程的异常行为，并且检查应用池是否被不必要地设置为“完全信任”模式。

## 项目现状

根据提供的信息，这个项目目前在Github上有88个星标，17个复刻。项目的主要作者是Mr.Z。代码主要由ASP.NET和C#语言构成。项目页面没有发布正式的版本包，看起来更多是一个概念验证或研究性质的代码仓库。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/tbTbtBE6TibdFXqA5vcC1Mjw2w9Rb1e2RGqxTBMBXAH9iaAKGEvd01KmSHxfb25G2oeX21uHIXUib0O7S7nn5lu9kSicF7bxUMGsONzAQuialPI4/640?wx_fmt=png&from=appmsg)

说到底，工具是死的，人是活的。Phantom提供了一个有趣的思路，但真正的较量，永远在攻防双方对细节的理解和把控上。

**获取方式：私信回复"Phantom"获取**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

幻泉之洲

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/KK6rkaWbMNbNvNRWVlQ1KyqceSk3WZAqKUsEjFj2Mfib1H7RQOOarzKolWvdD1W3PGicFOEABZLLpNoL2u9RdAXg/0?wx_fmt=png)

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