---
title: 为什么既有 TMP 环境变量又有 TEMP 环境变量，哪个才是正确的？
url: https://mp.weixin.qq.com/s/DbC7EhJU9c97yuJoiginmg
source: Doonsec's feed
date: 2026-05-06
fetch_date: 2026-05-07T05:31:17.231767
---

# 为什么既有 TMP 环境变量又有 TEMP 环境变量，哪个才是正确的？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/01RLQI6qOeBDv4l1fibaxvSUxwJdktrz6RwsdAQGqt0h6e2MBzYfRYOLPmpvGbmLHs18iakwTSeQPrGnuiaNEzsCiaHGnCJAiblhibicZkEvbgHDzw/0?wx_fmt=jpeg)

# 为什么既有 TMP 环境变量又有 TEMP 环境变量，哪个才是正确的？

原创

小编
小编

像梦又似花

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

如果你曾打开过系统的环境变量配置，大概率会注意到一个有意思的细节：

**有两个功能高度重合的变量，都在定义系统临时文件的存放位置 一个叫 TMP，另一个叫 TEMP。**

**两个变量都试图指定临时文件的位置。**

**为什么是两个？如果它们不一致，那么哪个才是正确的？**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/01RLQI6qOeC4vymAlTnicLdgAUe7NusI9QGB9zymXysmz1gUIEID0YLcgL0h8ib6dM8wWicVZ0JCL6wRpKCDia9K91IdzQJnEkoiby2zj6fh3xibw/640?wx_fmt=png&from=appmsg)

让我们回到 1973 年。当时微型计算机上普遍使用的操作系统是 CP/M。CP/M 操作系统没有环境变量。从这里开始讨论环境变量似乎有点奇怪，但实际上这一点很重要。由于它没有环境变量，因此既没有 TMP 环境变量，也没有 TEMP 环境变量。如果你想配置一个程序来指定临时文件的存放位置，你需要进行一些程序特定的配置，例如修改可执行文件中的一个字节来指示临时文件应该存储在哪个驱动器上。

（我记得大多数 CP/M 程序都是通过打补丁来配置的。至少我是这么做的。我记得我的 WordStar 手册里详细说明了需要打哪些字节才能实现什么功能。手册里还预留了几十字节的补丁空间，供用户编写自己的子程序，以防需要为打印机添加自定义支持。我就是这么做的，添加了一个“打印机是否准备好接收另一个字符？”的功能，这样可以实现更流畅的背景打印。）

时间快进到 1981 年。8086 处理器和 MS-DOS 操作系统问世。8086 处理器和 MS-DOS 操作系统的设计都深受 CP/M 的影响，以至于它们的主要设计目标就是能够将为 8080 处理器编写的 CP/M 程序机器翻译成为 8086 处理器编写的 MS-DOS 程序 。需要注意的是，翻译器默认你没有使用任何“小技巧”，例如代码自修改、跳转到指令中间或将代码用作数据。但如果你诚实地编写程序，翻译器就能成功转换。

除了兼容 CP/M 之外，MS-DOS 还增加了环境变量功能。由于当时的 CP/M 程序都不使用环境变量，因此 MS-DOS 的首批程序也都不使用，因为 MS-DOS 的首批程序都是从 CP/M 移植过来的。当然，你可以设置 TEMP 或 TMP 环境变量，但几乎没人会注意到它。

随着时间的推移，程序编写时主要以 MS-DOS 为目标平台，人们开始意识到可以使用环境变量来存储配置数据。在随后的市场混乱中， TEMP 和 TMP 这两个环境变量脱颖而出，成为指定临时文件存放位置的首选。

MS-DOS 2.0 引入了将一个程序的输出作为另一个程序的输入的功能。由于 MS-DOS 是一个单任务操作系统，因此它通过将第一个程序的输出重定向到一个临时文件并运行完成，然后再运行第二个程序，并将第二个程序的输出重定向到该临时文件来实现这一功能。然而，MS-DOS 突然需要一个地方来创建临时文件！不知出于何种原因，MS-DOS 的开发者选择使用 TEMP 变量来控制这些临时文件的创建位置。

请注意， COMMAND.COM 选择使用 TEMP 夹并不影响其他程序使用 TEMP 或 TMP 夹，这取决于其原作者的意愿。许多程序试图通过同时检查这两个文件夹来平衡冲突双方的需求，至于先检查哪个文件夹则取决于原作者的意愿。例如，旧版的 DISKCOPY 和 EDIT 程序会先查找 TEMP ，然后再查找 TMP 。

Windows 也经历了类似的尝试，但不知何故， GetTempFileName 函数的创作者选择先查找 TMP 然后再查找 TEMP 。

所有这些的结果就是，任何特定程序用于临时文件的目录都由该程序自行决定。Windows 程序可能会使用 GetTempFileName 函数来创建其临时文件，在这种情况下，它们会更倾向于使用 TMP 。

当你打开环境变量配置对话框时，你仍然会看到 TMP 和 TEMP 这两个变量，它们仍在

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/biachO2ia6rWDwdCSxVdTQ1dAqoicGYf8ricD6BuiaEU64urHUGmkzsUDfD8rqWibx2KXE40wesg6s5AInjvy5FjqCWQ/0?wx_fmt=png)

像梦又似花

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/biachO2ia6rWDwdCSxVdTQ1dAqoicGYf8ricD6BuiaEU64urHUGmkzsUDfD8rqWibx2KXE40wesg6s5AInjvy5FjqCWQ/0?wx_fmt=png)

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