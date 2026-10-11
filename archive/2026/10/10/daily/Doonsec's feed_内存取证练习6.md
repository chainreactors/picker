---
title: 内存取证练习6
url: https://mp.weixin.qq.com/s/IWt7rAYStPCB3HM7ZsZlrQ
source: Doonsec's feed
date: 2026-10-10
fetch_date: 2026-10-11T07:57:40.240960
---

# 内存取证练习6

# 内存取证练习6

原创

内存余响
内存余响

内存余响

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

#

题目描述：

我姐姐的电脑崩溃了。我们非常幸运地恢复了这个内存转储。您的工作是从系统中获取她的所有重要文件。根据我们的记忆，我们突然看到一个黑色窗口弹出，上面正在执行一些事情。灾祸发生时，她正试图画什么。这就是我们灾祸发生时起所记得的一切。

此挑战由 3 个flag组成。

通过网盘分享的文件：题目资源链接: https://pan.baidu.com/s/1nLAPhA\_A3m0L60w0wUVmJw?pwd=jk3q 提取码: jk3q

# flag1

首先查看镜像信息决定应该用vol2还是vol3

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibib493dAwIO9G2gj5JUh4AicsESyZuusqYGrVxdFan68H89wqr7nllRl28E5EuHKibU4L0XceNj4H46ItUiaiaGR2DE7uZN4cFNNxsE/640?wx_fmt=png)

还是vol2

查看操作系统信息

vol.py -f MemoryDump\_Lab1.raw imageinfo

得到profile=Win7SP1x64

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibibNor0QuLBkFXnf22wO3Zhto69tuPlmArXX8lvGOUhox4teClDsvTLsXhUXMz0fMSKbZooIofZN0KkXO21cIGg43kFiaxOhBpc8/640?wx_fmt=png)

查看进程列表

vol.py -f MemoryDump\_Lab1.raw pslist

发现cmd.exe在运行，查看历史命令

vol.py -f MemoryDump\_Lab1.raw consoles

得到一串base64

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibibfmV5VjkgfxAKKZbpBS2ibcvZxXwsHMfMGXxfUhjSgjhGPr033lM7ImcZtGG9OZ6SjMIH603UFcFWOMwFOjH14KRjj5KQr1Buo/640?wx_fmt=png)

解码得到flag1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib99r5rHkvzEh17AriaWNl4cOVCCpvkiaJUdwqsYBdJK4YibUhtNxkDwSSkticiajMh5q51JbSSCX0mMM7614834RZrgQTqSkeIicjibSs/640?wx_fmt=png)

# flag2

查看cmd相关信息

vol.py -f MemoryDump\_Lab1.raw cmdline

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib93Me1We9PKlHicVfVoNp9ibOTF6q327vtRkZkUCuMoHgqRdLJnDzEFtKrbCgWQwqMLyqWHicMRokZzgLskSPv2RgibuU8HdPVHNac/640?wx_fmt=png)

发现在winrar里面有一个重要的压缩包

先文件搜索一下，找到地址

vol.py -f MemoryDump\_Lab1.raw --profile=Win7SP1x64 filescan |grep -iE "Important.rar"

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDib92FMeptkacToVzxoyZBOMFQ5YeassXiaw5CtzGNia9FKXibWEgHIx0HiaHlsJ6fQw4ubd2MygpA6edh16KZh2jI6ggCGwJtRDgskY/640?wx_fmt=png)

下载下来

vol.py -f MemoryDump\_Lab1.raw --profile=Win7SP1x64 dumpfiles -Q 0x000000003fa3ebc0 -D dump

cat查看乱码但是里面有一张照片

360zip打开发现密码提示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibicjQYS3oI8xTAJWHiczKZTLxOgkJISKR3jeWS35ibUiblfyGNBPLYRYT7qY2FbviasMzxRgDkLFDmD9byfqrboSNHyZbhPlt853z9Y/640?wx_fmt=png)

密码是Alissa的NTLM hash

vol.py -f MemoryDump\_Lab1.raw --profile=Win7SP1x64 hashdump

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibicianaTlPBBibdro6GutUT7hYsuuHkjoicPk87V6PN0dYKWnSu55yMX03bN3FMicYdHpibnNWaa9r28muawKBDWGNl6gaEwJiceXaLibc/640?wx_fmt=png)

得到密码：f4ff64c8baac57d22f22edc681055ba6但是这里需要大写F4FF64C8BAAC57D22F22EDC681055BA6

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib9GiaU2lpvKIGcB5iafaF3y7A2yVJOw10qWYpgccnrxRqCA6bibHUkSdl17tz8hCVnvbWiclGHqzT78ABDRVe7eVwCDySNUYicgcnkY/640?wx_fmt=png)

得到flag2

# flag3

这个要从题目描述的里面“她正试图画什么”给出了提示

我们在查看进程的时候可以发现有一个正在运行的画图软件

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibibCJW8KnVQleoam1SGibzygcVot2476fibKCdzlfO9UYXHwSLTLcyOPqxiboej8CfMlIozicMc0ECnBIw09GPKsxIHO98XrBocUPpg/640?wx_fmt=png)

把这个进程导出来，这里需要转格式data，再用gimp工具打开

GIMP 是一款图像处理软件，打开2424.data即可得到flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibibeVLFblJ67yk9QvkKJOlbnMWD3YMJksL1nAN5VZQRaD9v9tn7FYUd81NK45iaVtYqehOaYdbgzkq78udoibZYa4Ft2icgWFWWnmg/640?wx_fmt=png)

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibic4YfldibtqMVhOo0ez7bhNzzvcKGfFIlhFKFvlSN3VmFvNUVyibvMYJP3SR60w6t9GFkzGY4yrGNrvk2DZYQ5lbJQppuHpG1VfI/0?wx_fmt=png)

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