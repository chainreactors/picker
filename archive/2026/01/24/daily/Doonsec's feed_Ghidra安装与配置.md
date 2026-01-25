---
title: Ghidra安装与配置
url: https://mp.weixin.qq.com/s/VtG_gVnwV6KElpHJIrf7cw
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:54:32.342202
---

# Ghidra安装与配置

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLZJsa1xOj8nbYM3FpucpOSp2hDib2DJ1u3AWHD1ibFuJKMoEX4fUkEWeg/0?wx_fmt=jpeg)

# Ghidra安装与配置

原创

secureyang
secureyang

secureyang

![]()

在小说阅读器中沉浸阅读

Ghidra安装与配置#下载Ghidra#启动Ghidra

# Ghidra安装与配置

在逆向工程领域有许多优秀的工具可以使用（比如IDA Pro和OllyDbg），但现在我们有一个新的选择-Ghidra。Ghidra是由美国国家安全局（美国主要的间谍机构，负责开发Stuxnet恶意软件和EternalBlue的机构）开发的，是世界上顶级的间谍机构之一。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLTwk0BibAkqDbGGgXBH3XicGsXn7vC6qgvhVmHTGo5b3OpehOy3oLpDGA/640?wx_fmt=png&from=appmsg)

我们第一次知道Ghidra是在2017年的维基解密Vault 7泄密事件中，它在2019年春天作为免费和开源（根据Apache许可证）软件发布。它是一个优秀的逆向工程工具，与IDA Pro不同，它是免费的!

Ghidra几乎具有Ida Pro的所有功能，所以如果你从事逆向工程，Ghidra是一个很好的选择。

## #下载Ghidra

你可以从官网下载：https://ghidra-sre.org/，由于它是用Java编写的，所以几乎所有的平台都可以使用，包括Windows、Mac OS和Linux。这里以Windows 11来演示Ghidra。GitHub - NationalSecurityAgency/ghidra: Ghidra is a software reverse engineering (SRE) framework  也可以从这个github上下载，都是一样的。

现在的 Ghidra 要求JAVA版本 21+，所以需要注意。

![image-20260121095343994](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLfxZNQyppRuzRXEibPRI6KNHPic0RVKYTWib9cDzh96f0xZibG46nShrHVQ/640?wx_fmt=png&from=appmsg)

## #启动Ghidra

下载并解压后，通过双击ghidraRun.bat来启动它

![image-20260121095459519](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLagEN7ke0TELibESWIGzQtgbiaLiaSzs6af4aTZR0k4JZIDYZ4a76aUzgg/640?wx_fmt=png&from=appmsg)

第一次安装使用的时候需要手动指定 JAVA21 版本的绝对路径，从你的计算机上找到下面这样的路径，复制粘贴到需要填写的地方就好了

![image-20260121095629736](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLXmlxic517kXRXnv5ryxvYIpH2InveH2Zs5XCGichE6gVw7yBbCdKJnuQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLLSibicWmGxlUSR9gOzAibdgPuoiafjLDeWm1wOFoCfElCOXnNEfchsHZbA/640?wx_fmt=png&from=appmsg)

然后显示这个窗口，开始你的第一个项目。项目类似于文件夹，可以包含你正在处理的多个文件。

![image-20260121100031663](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLoy8nDst8JbooOicyb2K7MJOPjNM6t2EWGiaHosicopFjjLb7Ur65wSh8A/640?wx_fmt=png&from=appmsg)

点击"File"-->"New Project" 新建项目

![image-20260121100057345](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLsWAWKl0kSDcBkYYwahhwfvpSPsKWLhDq4eAja8hneezyh8JibicsRpEQ/640?wx_fmt=png&from=appmsg)

这将打开一个像下面这样的窗口。Ghidra的一个特点是能够在一个文件或项目上进行协作。在这种情况下，点击 "Shared Project"。在这里，我们不需要共享，所以选择 "No-Shared Project"。然后点击 "Next"。

![image-20260121100116001](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLbPpxOGwm1ibPGPeVmlebicJDzY6TkuSjnzHzQicFicSsIvZPXJGibQGIRxw/640?wx_fmt=png&from=appmsg)

选择项目保存位置和输入项目名字，点"Finish"。

![image-20260121100159801](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLg9jicD3724Uu7M1O0TfAkPpJJ8BCClKR21yoIExfe9k7vb2tFXhexaw/640?wx_fmt=png&from=appmsg)

![image-20260121100218979](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLIWyiaxvwEjY6Nc60cxuA5lINkoibmAicTAZmp4U31RJa286qzMaQlqUDQ/640?wx_fmt=png&from=appmsg)

接下来，我们需要导入一个文件。这是你要分析的软件或恶意软件。"File" -->"Import File"。

![image-20260121100239913](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLhjSEa4Sb7vLgFicLnrvgiaLH8tFtBrsEwYFqHw77oxUW9WbKgI5BvPEg/640?wx_fmt=png&from=appmsg)

选择要导入的二进制文件，然后导入

![image-20260121100309834](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtL2pyzK8gRgulZjtSdgHkiahIEDybzDD0TMBkwYu1FJ2rDqZ8CYcic4SJQ/640?wx_fmt=png&from=appmsg)

注意，这里的 exe 文件不要用中文，需要的重命名一下。

选择导入后，Ghidra会提示文件的基本信息，然后点"OK"

![image-20260121100329097](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtL41HTb6COdgvAGnKg3Y3hym4icukiaiawYoZxc6uWZ9ZcheKox6qWMW4Zg/640?wx_fmt=png&from=appmsg)

然后，Ghidra会显示一个像下面这样的窗口，显示有关该文件的关键信息。

![image-20260121100416849](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLSMjf91cFicToWGIthibQOgV8QiaarJPYsdKZB8XonnBDY2q9kXdCauXzQ/640?wx_fmt=png&from=appmsg)

接下来，会显示你的项目和导入的文件。你可以双击文件或将文件拖到上面的绿色Ghidra龙图标上开始进行分析。

![image-20260121100512174](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLia1hBFRPqfUPaQLoVeDQKHdH0E5N1xwgHSg1bWxYZycDmiaqpZyVhO9w/640?wx_fmt=png&from=appmsg)

然后Ghidra开始工作。它在中心列表窗口显示程序的汇编代码，然后询问你是否要分析该文件。点击 "Yes"。

![image-20260121100538833](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLXRGYtwiartbPiblH3To7RBKvrEYyPnz0AK0us0MTmVTBarO7hEbY7UFg/640?wx_fmt=png&from=appmsg)

![image-20260121100603644](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLGaCswibdicwicKQuJMbroHVNCbtVEiaEWrLEkU4cl0sYYsxc40DlBiclvDA/640?wx_fmt=png&from=appmsg)

Ghidra将分析你的文件，并显示类似于下面四个窗口的信息。

![image-20260121100723595](https://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoSDR5Z5eiaClTibhRszVYKwtLSoHPHEejaqkRpfZpGTtgZQT0YLU9Orkmoib2ib7LwBTJpfgnia28Ipugw/640?wx_fmt=png&from=appmsg)

**窗口1是符号树(Symbol Tree)**

此窗口允许你查看二进制文件的导入、导出、函数、标签、类和命名空间。

**窗口2是列表窗口**

这个窗口显示的是汇编语言的代码分解

**窗口3 是反编译器窗口**

反编译器使你能够看到高级语言可能会是什么样子

**窗口4是数据类型管理器窗口**

数据类型管理器允许你查看所有已定义的数据类型。

现在，你已经准备好并可以开始分析和逆向这个文件了!

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoQW0gRe2T7PcibUQdxRXlZ9gUmhnDnCnZH1QV9ickJOicpYfupCNqRefT4xquSPPTcAIhDibeicp4aL8ZQ/0?wx_fmt=png)

secureyang

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/NCLsGXruwoQW0gRe2T7PcibUQdxRXlZ9gUmhnDnCnZH1QV9ickJOicpYfupCNqRefT4xquSPPTcAIhDibeicp4aL8ZQ/0?wx_fmt=png)

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