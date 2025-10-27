---
title: G.O.S.S.I.P 阅读推荐 2022-12-23 POPKORN
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODUxMzg0Ng==&mid=2247493690&idx=1&sn=92c8767554bd46e7ccaaf6d3d597b37b&chksm=c063c6e3f7144ff58c42de99bd3036603a2c915f2f64264e66f148fa5b55c7387fd48de8ea81&scene=58&subscene=0#rd
source: 安全研究GoSSIP
date: 2022-12-24
fetch_date: 2025-10-04T02:26:14.752578
---

# G.O.S.S.I.P 阅读推荐 2022-12-23 POPKORN

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/uicdfzKrO21HHUGPuWM5ibnEvVqoqzg9eLpr0HkTVOgNwP6eiat5tlsVM0O9eHrbLN4Pyw1gnOSicXFV2LT7Q0Q3LA/0?wx_fmt=jpeg)

# G.O.S.S.I.P 阅读推荐 2022-12-23 POPKORN

原创

G.O.S.S.I.P

安全研究GoSSIP

圣诞节前的最后一篇论文推送，为大家介绍的是ACSAC 2022会议上关于Windows内核驱动安全分析的研究论文 *POPKORN: Popping Windows Kernel Drivers At Scale*

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HHUGPuWM5ibnEvVqoqzg9eLAia6TOia2WPw7QhTXhgNGvE6Or1hibXn5YhQhJtPAXZyT9fjoRHxfXhkw/640?wx_fmt=png)

在这篇论文中，作者想要解决的问题是如何大规模分析Windows内核驱动，并能够准确找到相关bug和缺陷。显然，Windows内核驱动通常不太可能给分析人员提供源代码，所以本文集中在讨论如何开展特定的binary code analysis任务，特别是污点分析和符号执行在这个场景下的应用。作者研发了名为`POPKORN`的二进制代码分析系统，其特点是能够搜索一系列和 security-critical Windows API 相关的（逻辑型）bug，而这些bug通常都会被市面上的privilege-escalation exploits所使用。

首先看一下Windows内核驱动的一些特点，下图展示的是Windows应用程序与高权限的内核驱动的交互模型。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HHUGPuWM5ibnEvVqoqzg9eLSfSGqOz6Hu2JdwlhwSfHtxcqsoLAHqufib85L1ib5KIfeLulk1hv129g/640?wx_fmt=png)

其实大家会发现，在不同的系统里面，这些高低权限之间的调用-通信模型都有相似之处，像在ARM平台上应用与TEE之间的通信也有类似的模型。在Windows上，特定的驱动会去声明一些dispatch handler routine并将其注册到系统中，用户态的程序可以通过`DeviceIoControl`这个API来和不同的内核驱动进行互动。下图是一个实际的例子，该驱动首先注册了一个符号链接，然后在上面创建了特定的设备，最后给这个设备的`MajorFunction`表里面添加了不同的handler函数。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HHUGPuWM5ibnEvVqoqzg9eLkU49IH3A4Dk53vZRo0UUnkHco32TwDO3lDsqWBYzKaeb4xTnB7VFdg/640?wx_fmt=png)

在掌握了一些基本知识后，我们来看看真实世界的安全问题，特别是本文关注的所谓POPKORN漏洞的细节。下图中展示的存在POPKORN漏洞问题的驱动代码，在代码中，首先我们注意到参数`Irp`是一个指向用户态可控的内存区域的指针，这也是攻击可以发起的源头。在下图的17行，驱动代码调用了`MmMapIoSpace`函数，将一个物理地址页映射到`Buf`指针提供的虚拟地址上，这是为了让驱动和用户态进行数据交互。然而，我们此前在Android平台上关于TEE的攻击中就学到过一种攻击技巧——给高权限代码（内核、TEE等）提供一个精心选择的虚拟地址，高权限代码一旦疏忽大意没有检查这个地址是否真的为用户态进程所有，那就容易出大乱子。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HHUGPuWM5ibnEvVqoqzg9eLDbribbOyaSl9HELiaJwPbQFb606opqEAcvMhCwAOsawGL6ZXweqfuabw/640?wx_fmt=png)

为了检查这种问题，作者设计了`POPKORN`二进制代码分析系统，专门围绕诸如`MmMapIoSpace`这样的函数进行分析，检查传入的参数是否会被用户态操控。看到这里，你是否马上会想起经典的那篇 *Dynamic Taint Analysis: Automatic Detection, Analysis, and Signature Generation of Exploit Attacks on Commodity Software* 论文？嗯，思路是一致的，用污点分析+符号执行来对代码做一次全面的检查，而且内核驱动代码相对来说结构是比较简单的，分析效果应该会比那些用户态巨复杂的软件要好！

明确了思路，作者接下去调查了一堆CVE，来帮助`POPKORN`选择污点分析的source和sink，其中 `MmMapIoSpace`、`ZwMapViewOfSection`、`ZwOpenProcess` 这三个函数是`POPKORN`系统聚焦的可能出问题的点。更多的相关函数的信息见下面的图表。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HHUGPuWM5ibnEvVqoqzg9eLC7sicyH2WIHKURVIiczrsTgVAh6duCoopgqyxyG0IyszQhKwyDuXayEg/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HHUGPuWM5ibnEvVqoqzg9eLLGN0lM2GOkvt4ngS9gnhwVnnqbGUg6cFNlB4F68WU3YdVQhDA0bTCQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HHUGPuWM5ibnEvVqoqzg9eLqhQJSw83xqy3nIReVwDVoUAH05whnLKbrlDhVqEGHEwZLuIfdJjrMw/640?wx_fmt=png)

设计和实现思路都确定以后，`POPKORN`系统的整体框架就水到渠成了（见下图），这里面主要发挥作用的是其中的analysis engine，它是基于`angr`构建的，因此基本的需求都通过`angr`提供的污点分析和符号执行能力来实现了。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HHUGPuWM5ibnEvVqoqzg9eL7BBfylBx6qb4yKrdQrywX5K8z3H6zmK5fnT5TBg3Uzft41bs5rFWZg/640?wx_fmt=png)

作者使用`POPKORN`对3094个基于Windows Driver Model（WDM）开发的驱动进行了分析，发现其中使用到 `MmMapIoSpace`、`ZwMapViewOfSection`、`ZwOpenProcess` 这三个函数的驱动比例为8.76%（有212个驱动使用了这三个函数），而其中有27个驱动存在POPKORN漏洞。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HHUGPuWM5ibnEvVqoqzg9eL3csQvk6DxAVPYzngYP54SiaJxTwRWl1Qq0nIHwS5lu4YXFrriaVlnPsg/640?wx_fmt=png)

作者还将`POPKORN`和微软的测试工具（DriverVerifier和Static DriverVerifier）进行了对比。特别地，DriverVerifier这个动态测试工具使用了一些通用的测试用例来试图触发驱动中的bug，那它的效果和`POPKORN`比较起来（下图），不能说完全不行，还是比`POPKORN`要略逊一筹。

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HHUGPuWM5ibnEvVqoqzg9eLx8xaFib2EqOd58LK81tWqQvQYSyibEVx6UzV7qiaV5EOINgCa6ySosDLQ/640?wx_fmt=png)

最后展示一下`POPKORN`发现的漏洞的影响：

![](https://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21HHUGPuWM5ibnEvVqoqzg9eLkxWINzh38EOkBPn4Kuk4oI3WgrKXFFyHqLqBgfFW3ia3pCKb8zgSokA/640?wx_fmt=png)

---

> 论文：https://dl.acm.org/doi/10.1145/3564625.3564631

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

安全研究GoSSIP

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/uicdfzKrO21EibxMcqx9KdafugxDicBiaW3cb1gyTuWooDCJjH1ibu8aibOiapYLq8BJMwNbIeUK1t0japdvmdqTfCxhg/0?wx_fmt=png)

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