---
title: 内存取证练习8
url: https://mp.weixin.qq.com/s/mJe6yLwpWaJR1UzuUSSz3A
source: Doonsec's feed
date: 2026-10-14
fetch_date: 2026-10-15T06:42:33.879117
---

# 内存取证练习8

# 内存取证练习8

原创

内存余响
内存余响

内存余响

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

挑战描述：一个恶意脚本加密了我系统上的一条非常机密的信息。您能帮我恢复信息吗？

此挑战仅由 1 个flag组成。flag分为两部分。您需要flag的前半部分才能获得后半部分。您将需要这个额外的工具来解决挑战steghide

根据这个题目描述，这个非常机密的信息应该就是flag了

我们先查看一下这个内存镜像信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib9Vjia5icAXLicQhfmHMlsK4G6xXnMSbFSUDMTNz9xQVdv7P5QehdITibLr7icnSMicEYr2J4hictQtn0J52E6LicCUKXLQ9byERicck4vA/640?wx_fmt=png)

判断是使用vol2还是vol3看输出是否存在错误

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibiciaKyrJpSvp6UlUByEK10NXXGj7nZBrNl6PesKTvw2esoUxeUibnthV7gXn6N4q1piaydZ3vNcRSWRMwo7m9GqVrlTXHCLtxhng0/640?wx_fmt=png)

现在用vol3查看信息显示错误，采用vol2

vol.py -f MemoryDump\_Lab3.raw imageinfo

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDib9DCksrOnFqMQhD0PjibbuVYpNeGJuicWEGSYKHpo0XGt6DxGY4GvswEo3LNTtqrfI9cbRtBpja4eME8Lt48zNibEl9urtjvItlIA/640?wx_fmt=png)

得到profile，用一些常见的插件查看有没有什么比较有用的信息

vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 pslist
vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 hashdump
vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 lsadump
vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 envars
vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 pstree
vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 netscan
vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 filedump |grep -iE "desktop"
vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 cmdline
vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 iehistory
vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 consoles

这些都是一些常见的可能存在有用信息的地方

vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 filedump |grep -iE "desktop"

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibicpv1AIAOfomMwSzial24CicB6vxlHE6lCSSzRdkbBKgNOfVSxlbnvOrIrCophYAVM3axFczvadcic8CViaXmQXLQdoLqMsdABzua8/640?wx_fmt=png)

在桌面发现了一个恶意脚本，刚好对应了题目描述，还有一个vip.txt，先看一下这个

vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 dumpfiles -Q 0x000000003e727e50 -D dump

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibicicBUkdZKhe9LVadfSiafR9O8ePIpeELvkB7Hib4AUhtwA1iczJibng3jA7NddIibTSD9es9r68WjwezQ4BiabIYhZicYKjy2O1v9kLqk/640?wx_fmt=png)

得到一个base64解码之后还是没有什么头绪，看一下刚刚那个恶意脚本

vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 dumpfiles -Q 0x000000003de1b5f0 -D dump

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibibgSUIriclaQQ9nEZEWAUOHKQLTreaWJE5GuHg5HCQmtlzcU587rgdwqjj6LvWvibPbu1nXRy1GyPf36Uyl3EbxiclUsGibSKuCtaA/640?wx_fmt=png)

我们来分析一下这个恶意脚本

定义一个函数，遍历字符串s，取ascii码值再与3进行异或，再转回字符进行拼接后进行base64加密

主函数是

arr = sys.argv[1]              # 取命令行第一个参数
arr = encoder(xor(arr))        # 先 XOR，再 Base64
f = open("...vip.txt", "w")    # 打开文件
f.write(arr)                   # 写入结果
f.close()

所以接下来我们再和3进行异或

c = 'jm`wex3m0\k7oe'
for i in c:
   m=chr(ord(i)^3)
   print(m)

得到inctf{0n3\_h4lf

现在得到了一半的flag，再继续找另一半，根据题提示，应该有一个隐写

steghide是一共个图片或者音频隐写工具，查找一下有没有什么图片

vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 filescan |grep -iE "jpeg"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibibSxegicrKfpZ5EIIm8GxoGLq42oOHFYYX8pia8XZSnYPNN80pn1SkibQIdicrcicfN4MsCLx4XE6WX7aibYQTRCAUz2diauQKnuhnLPY/640?wx_fmt=png)

有一张照片”怀疑“

刚刚查找桌面文件的时候居然没有看到这个

先导出来再重命名一下

vol.py -f MemoryDump\_Lab3.raw --profile=Win7SP1x86\_23418 dumpfiles -Q 0x0000000004f34148 -D dump
mv file.None.0x843fcf38.dat 2.jpg

查看隐藏了什么

steghide extract -sf 2.jpg

要输入密码，根据提示知道flag前半部分才知道后半部分，密码应该就是flag前半部分

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibicM7mNTjdAfe7564ooMiaic0BibSugiaCawIFOte2QQzQAB1SiauuoJ4JodJo6626kOpr8eM2y6JXh7icRb83YibgIYKUur49UEDDhPB8/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibicW7LJibLeHDE6ibD36Y5PDm4quWbkzwHc621eh7ibuCRRbM4oE2fVpMaqFndzdgeEFDpuyZDWrQtzeYibGKSgvkLIh2ATnICQBP90/640?wx_fmt=png)

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