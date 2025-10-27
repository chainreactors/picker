---
title: 利用WinRAR工具构造钓鱼文件
url: https://mp.weixin.qq.com/s?__biz=Mzg4Nzk3MTg3MA==&mid=2247487527&idx=1&sn=ec5e25890787cecc2e54517ae3420634&chksm=cf831956f8f49040a8168c8e138a357898d842bdfe38bb13fce1fdaf59f16905c7e8112c374b&scene=58&subscene=0#rd
source: 洞源实验室
date: 2024-10-20
fetch_date: 2025-10-06T18:50:43.621382
---

# 利用WinRAR工具构造钓鱼文件

![cover_image](http://mmbiz.qpic.cn/sz_mmbiz_jpg/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlYHKIWiaTiamZtjSUQsKMJnjAOEU9iby8PL5EbrQicIqicPoiaOC08AMcxI0g/0?wx_fmt=jpeg)

# 利用WinRAR工具构造钓鱼文件

原创

张飞

洞源实验室

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdl2iaOibDC16icjytRwaibbM6bM7DFaqMOKRxTsiamtvceX2cTAicjibtKDUQIQ/640?wx_fmt=gif)

在一些特殊的网络环境中，许多人会习惯性认为只要进行网络隔离便可以避免被网络攻击，但实际上也在这样的网络环境中，出于个人工作便捷的需要，常常在办公环境中会将电脑同时接入互联网和内部网络，又或者通过两台电脑分别接入互联网和内部网络。但是即便如此，也依然无法阻断常规的社工类攻击，比如钓鱼邮件、钓鱼微信等类型的钓鱼攻击。

本文介绍的是基于WinRAR软件自带功能，在两个场景下构造钓鱼攻击文件，其技术原理和细节都不算最新，但对于普通人而言常常难以防范，即便是针对网络隔离的环境，通过钓鱼攻击，也非常容易通过攻击人员的办公系统为下一步的攻击做铺垫。

**场景一：用自解压功能伪造常见软件进行恶意程序捆绑**

该场景展示如何创建一个看起来像Web浏览器可执行文件的恶意可执行文件，它具有普通文件/程序的功能，但也可以嵌入的恶意可执行文件的执行功能。

首先，使用MSF创建一个反向连接程序shell.exe，绑定远控服务器的IP和端口，下图中该命令将木马程序绑定到远程控制端（即系统自身IP地址）192.168.110.55，并设置监听端口为4444。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlVktutWLrXUEd9gSoH9wiawibAzvYDnxGtTibGswGDzGqHF17psp0yyIAQ/640?wx_fmt=png)

接着下载具有诱惑性或者合法软件的icon图标，比如Chrome浏览器的图标下载地址是https://icon-icons.com/search/icons/chrome。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdl2PeWDbeEpHyezsKnsib49iaSEGuy2YWUfWicxO51cdxqKJ9BGT3nXBtJg/640?wx_fmt=png)

将上面生成的shell.exe文件和正常的Chrome文件通过右键选择WinRAR菜单，使用Add to archive选项将两个文件打包为一个自解压的可执行文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlJzsibhvIOYoAhKkf3nG5OxWZQ0epMxRLnYWwWawduybuccRsjiar2eaA/640?wx_fmt=png)

右键的压缩文件参数中，需要在Archiving options中选择Create SFX archive，意思是创建自解压文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlmkMAXAVo8KlkgbdbWPuFqOwd2B6YEicTlUTxcsLQgrH8gICfYicyjrVg/640?wx_fmt=png)

而后通过SFX options在Setup中按照程序执行顺序，分别写入shell.exe和chrome.exe，即解压后先执行shell.exe，然后执行chrome.exe。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlBRBN71cDRcMdkBFd0TeTV7SRiasNdswMWkLqE3BScVia4ibllcvQbztKA/640?wx_fmt=png)

另外，还需要在Modes中的Slient mode中选择Hide all，即自解压过程中不做任何提示，隐藏所有程序执行界面和窗口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdl6Yuzk2OtO2sDSEjWmmLkGUicqjeVQqm7WZ2iaCicbT0ib7o9rrslu2UsBg/640?wx_fmt=png)

最后是将上面下载的Chrome图标通过Text and icon中的Load SFX icon from the file进行设置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlySI9Uu45ugiclM3Viaj76dqvvpXsmib3UfMDRBHI2m7zx1jianMibD3ZtBA/640?wx_fmt=png)

创建完毕后的压缩包fake-chrome.exe，从程序图标的外观上看是无法看出端倪的，但在文件属性中可以看到是Archive类的文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlguicyMK8KH2rlNQdibKJXBstv1IEGP8JGPR579p8XicyR8QebI18cvRCw/640?wx_fmt=png)

尝试执行捆绑木马程序的文件时，需要在MSF中设置监听器，以便当目标设备运行木马程序时，能够捕获并控制目标系统，实现远程访问和进一步的攻击行为。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlNLqXmoOVZIy4Go88wearB5c0l8pc4iadOGdicCIqtQbSxpyj306I1BAA/640?wx_fmt=png)

fake-chrome.exe程序执行后可以看到Chrome浏览器可以正常打开，但同时shell.exe程序也执行成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlNt4Hia8kbavnKvwsl3F1oxuuoGbBuIAX3EicvJCgImic5YOicoiaicgayFzw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlYHrYxALpAda9ic8GwD9PE910hJsxRWaZkIbB3E5oH4MVPt0icPQf9WOQ/640?wx_fmt=png)

**场景二：以自解压方式+Unicode RTLO伪造恶意的PDF文件**

该场景是在场景一基础上，使用一个PDF求职简历加上Unicode RTLO倒置技术创建一个带有恶意程序的PDF文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdl4icyj3I3yBk5Pgyd8L67ksywQjrxsEPITfdTZH3BjoZPwpvezhM9IkA/640?wx_fmt=png)

还是自解压工具进行木马文件打包，选择shell2.exe和简历.pdf这两个文件进行打包。通过自解压程序设置，在用户解压运行时，shell2.exe将会被隐蔽执行，而简历.pdf作为迷惑文件正常显示给用户并打开PDF文件。这样可以在不引起用户怀疑的情况下，执行恶意代码，达到隐蔽控制的目的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlmbCRzzib3EyJibibNK5fZEWLY0xJhZxibMicrgQ8icw9tznwuVprrcTPIgFw/640?wx_fmt=png)

Unicode RTLO会将名称+后缀的结构颠倒，文件名称会变成简历exe.xx的形式，为了文件名称更加合理和隐晦，笔者将文件名称修改为“简历Reflfdp.exe”，并在“简历Refl”和“fdp.exe”字符串中间插入Unicode的202E字符，这样文件明就会变成“简历Reflexe.pdf”。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlytIiclzOgribH1Gwsiart9iayPX1BW7vJXqDYVhhlCBoF2A7V6ARLMfDxQ/640?wx_fmt=png)

Unicode的202E字符是从右到左显示后续字符的字符，可以在Winodws系统的字符映射表中复制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlOaUrnlibCHfUibGS5icdKibNlvYicQlIRn49aCiaOibEJx1WABryLWE6XNI0Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlo7ialtRX9r0PwxCEd0rzGunibCajR4DCXV8O2bibYZphBgRX9nl00jTkw/640?wx_fmt=png)

更改文件名称后的“简历Reflexe.pdf”执行后可以正常打开PDF格式的简历，但同时shell2.exe的执行也能够让攻击者控制当前的系统。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlQiaV9EKHKzaq8hCw2JrcSpKDYrf04ycegY8jen3ZKiaXKsQ2IruEC9nQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlLm9icj3GYSxUniboY2SbHUQtiaiaTVbvlbJlLVXDnamVcZluYC2RFUjEbA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlzehz8XPseqIvTDUI8s9mFlFz8L3I2kUKKd71TiacfJKRQk75Uhgcickg/640?wx_fmt=png)

在自解压包中，用户在执行文件时可能会看到正常的文件释放和执行，但在后台，隐藏的恶意代码如木马或后门程序也会被执行。这种攻击方式依赖于用户的信任，认为解压缩包中的内容是安全的，同时通过迷惑用户的文件名和文件内容，增加成功率。

自解压的恶意文件通常会通过以下步骤进行：

1. **文件捆绑：**将恶意程序与正常文件一同压缩为自解压文件。正常文件可为诱饵，而恶意程序在后台执行。
2. **设置执行选项：**设置在解压缩后自动执行的恶意文件。
3. **伪装和混淆：**通过伪装文件名或附加诱导性文档，减少用户的警惕。

这种技术的优点在于其广泛的兼容性和免工具运行特点，且在用户执行时攻击者可以实现隐蔽代码执行，达到渗透控制的目的。

**自解压技术介绍**

SFX (SelF-eXtracting)自解压文件也是压缩文件的一种方式，因为它可以不用借助任何压缩工具，而只需双击该文件就可以自动执行解压缩，因此叫做自解压文件方式。这个文件通常由三部分组成：可执行程序、压缩数据和尾部信息。当用户运行这个文件时，首先启动的是可执行程序部分。这个程序会读取文件尾部的信息，获知压缩数据在文件中的位置和大小。随后，程序从文件中提取压缩数据，并使用内置的解压算法将其还原成原始文件，同压缩文件相比，自解压的压缩文件体积要大于普通的压缩文件（因为内置了自解压程序，通常比正常压缩包大250KB到500KB），这种格式的压缩文件设计的初衷是为了方便文件的分发和更新，并可以自定义的安装逻辑或文件保护机制。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdlibn1Rwmur2svsicT0cfia1CibTia7zMSxAvn66FJlx1rtfjF3TKxGJErXUA/640?wx_fmt=png)

**Unicode RTLO技术介绍**

Unicode RTLO方法是一种利用Unicode字符集中特殊控制字符U+202E来改变文本显示方向的技术。当这个不可见的字符被插入到文本中时，它会强制其后的文本从右向左显示，而不改变字符在内存中的实际顺序。这种方法原本设计用于在主要从左到右的文本中正确显示从右到左的语言（如阿拉伯语或希伯来语），但后来被用来创建具有误导性的文本显示效果。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs6PYqArNaAnJeFpibgTEDUdleDClD65ap1DAlGkMNBaiaPxSQBmNolrBibrz3g3bLEe221zHpwaXiaicnQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gEGSydvbZs6QFVKAZYpGjdzjQ0Gic9daoqjgic43Wlc4BzBAxD0pEElMibIkY38WQNt01zSibLjf9ERxcHlUBLKukg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**长**

**按**

**关**

**注**

**最佳实践、技术实践、案例研究**

**安全测评、前沿技术、安全工具**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/gEGSydvbZs6QFVKAZYpGjdzjQ0Gic9daoRCGqohf6rrpjc5wHNL3nz49EDqLW0beibcnyjRibTwfMFg53cn7LWGHg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

**洞源实验室**

    知识星球 : 洞源

    B站：洞源实验室

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs7HiaU1TeSL6QyZuasLpGExfp2m8lBgbIIAVjJHnpUtjSHQP8GzWSZUelPqhiauCibibNjbKOMsGkL3MA/0?wx_fmt=png)

洞源实验室

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/gEGSydvbZs7HiaU1TeSL6QyZuasLpGExfp2m8lBgbIIAVjJHnpUtjSHQP8GzWSZUelPqhiauCibibNjbKOMsGkL3MA/0?wx_fmt=png)

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