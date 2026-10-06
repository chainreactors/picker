---
title: 电子取证——文件头初探与图片隐写（一）
url: https://mp.weixin.qq.com/s/kOGM7UJscDqJzxLpMp9L6Q
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:20:30.866539
---

# 电子取证——文件头初探与图片隐写（一）

# 电子取证——文件头初探与图片隐写（一）

原创

是羊羊羊呀
是羊羊羊呀

羊羊羊的forensic

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwUmJTHlQsjibUmmGee5ELrmDwuj13hhzo62TicLygIk6ntEOAonqxtqB2HtQmHTrGtNSrMrlU9PiaFJdLzYiaIKicfrd0VnlQicHh6a4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwWgzAicLe47FO4tick1GWDHcDvubJEgPXXLnIhQcPngUw8g6ibib05M38RP59olnZcYdsFUTF6E5DeiaRsxjbmGRyA9ib9GZCHEYv4B8/640?wx_fmt=png&from=appmsg)

**前言**

消失了好久，一直没有创（没）造（有）欲（公）望（假）。假期了，正好碰上区队在上电子取证的专业课，那就写写推文吧！当作手搓的复习～

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwWxYUlwKuriblCFrRvHA6KI0sjmFGQOZk9IwUbEqzhC2lwasFJPEKzmqg6bp85AtJR1U6dECM37vib4hZpkq6NvuquPm0OCa9604/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwWLxmFIHicn6iaXnOSA9j0FfX7B8bT3uoibYhkia2Cm6icyB7icRWUtj3ddFAgLI10xEeXU0PKFen2OgibEgmvXyL3oibvnC2TjlIDRQuE/640?wx_fmt=png&from=appmsg)

**文件头是什么？先从扩展名说起**

“照片.jpg” 中的 “.jpg” 是扩展名。

        它会影响系统用什么软件打开文件，但文件名可以修改。把 ZIP 改名为 JPG，不会让压缩包变成图片。

**但是，扩展名写了什么就一定是这个类型吗？**

**显然不是，所以判断文件类型，需要检查文件里的字节。**

许多格式约定了一组有辨识度的字节，通常出现在开头。我们常把它称为“文件签名”或“魔数”，入门时也常直接叫“文件头”。

例如，PNG 的开头通常是：

**89 50 4E 47 0D 0A 1A 0A**

我们可以用Winhex来看

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwVJBJVMXeNwCyERfpaLw27P8MZZ2woHeGxrOuHsibfskDZZIvYCWv5Hic7C8X3SyYwOCOktkxaaAicT7TDBDT4qqwevMCzIod3BTA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwVEz7F2adGK7icus0iaKUUDPkZ4plxDicnnHQeC59hcmpA7zibXxCvyWyhHOlA6fAjhDNEEoiakcGsjZSpfPdnABuxP16qlJoQ1JuHA/640?wx_fmt=png&from=appmsg)

这里有 8 组两位数，表示 8 个字节。它只是 PNG 文件头的一部分，不包含完整的尺寸、颜色类型等信息。PNG 签名的定义见链接：

https://www.w3.org/TR/png-3/#5PNG-file-signature

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwWfY7GqHsibKMTRETOo9zdsKHRC0lNRKA3Uxt1cawS7PY6GibZ7zsAz3btPbrLtuU5txMSQAJPvmWNGMhqMxtgH8atXlteMn5XfU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwWmL8qdksmSzNQnL5HAlCOXGcuBtwkpNB9kGK2Zs9mZf5Jiba2DMCL4E1Kzo3iaMhAplzrZPEN0OvcjPiaklTlria8fhWYCUe4kWRE/640?wx_fmt=png&from=appmsg)

**怎么理解是十六进制捏以及WinHex的三栏**

计算机里的文件可以看成按顺序排列的一串字节。每个字节有 256 种可能的值，十六进制把它写成 “00” 到 “FF”。

十六进制使用“0–9” 和“A–F”。其中 “A” 表示十进制的 10，“F” 表示 15；整个字节 “FF” 表示 255。

所以，“FF D8 FF” 表示三个字节。“FF`”不是两个英文字母。

WinHex打开一个文件，通常能看到三部分：

左侧的“偏移”：这一行从文件的哪个位置开始

中间的“十六进制”：每个字节的值
右侧的“文本”：把相同的字节显示成字符；不能正常显示的字节，常用点号代替

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwW9NcE44Udtl0pVImaQxESNV5rkd92vibOO9qtg6JS04S1llQ2h9aDTf6icWFt7kFf3luFcHKXIg1RBCzekpYmtbBlYafbC7ffuY/640?wx_fmt=png&from=appmsg)

偏移从“0”开始。第一个字节的偏移是 “0”，第九个字节的偏移是“8”。

本文用“0x”表示“后面的数字是十六进制”。例如，“0x10” 等于十进制的 16。

**“****0x”是书写的提示，不是文件中的两个字节。**

还有一个很实用的区别：位于偏移“0”的签名，可以帮助判断整个文件的格式；位于文件中间的同样字节，可能属于内嵌内容、元数据，也可能只是巧合，需要继续检查。

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwU7ZDKWiaEOKDSjrkvpJL8GQHN81jTAwMbnicApTk0UOiaOXZa7ibQyr7TUmtSibYsRgdmml7JAjqh97U3eSGtp1xmcBdRsc1Bia56tw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwXf5m9TB04anTIpwAiatwLVhEPMWNspzZFLDXXYjWGHVQFiagKtZLrjaOmeTiboDdFLdn2u3XiaV2CAXtQFib1T0ZiceuAM0vJ7go9J4/640?wx_fmt=png&from=appmsg)

**在 WinHex 里，怎样搜索特定文件头？**

**第一步：打开文件，回到开头**

选择“文件 → 打开”（”File → Open”），打开 “检验材料.jpg”。

再选择“导航 → 跳至 → 文件开头”（”Navigation → Go To → Beginning Of File”）。此时光标应在偏移 “0”。

开头能看到：

FF D8 FF E0 00 10 4A 46 49 46 ...

“FF D8” 是 JPEG 的开始标记；后面的 “FF” 表示接下来还有另一个标记。”4A 46 49 46” 在文本栏里对应 “JFIF”。这份材料的开头与 JPEG 结构相符。

**第二步：打开“查找十六进制数值”**

选择“搜索 → 查找十六进制数值”（”Search → Find Hex Values”）。

如果要找 ZIP 的本地文件头，在输入框中填入：

50 4B 03 04

部分输入框会自动整理空格，也可以连续输入 “504B0304”。不要把 “0x”、逗号或中文说明一起填进去。

首次搜索可选择“从文件开头到结尾”；也可以先把光标放在偏移 “0”，再选择“向下搜索”。同时确认：

1、没有勾选“仅在块中搜索”（”Search in block only”），以免只搜索当前选区。

2、没有启用不必要的偏移或对齐限制。

3、当前搜索对象是这一个文件。

点击确定后，WinHex 会定位到符合条件的字节。记录第一个 “50” 的偏移。

需要查看下一处命中时，使用“搜索 → 继续搜索”（”Search → Continue Search”）。一个 ZIP 可以有多个本地文件头，不能只凭命中次数判断压缩包数量。
下面的图片是搜索压缩包文件头操作的显示页面

**注意：十六进制搜索与文本搜索不是一回事**

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwXEamdbV7JlcichXicVnfYevbxGefts90IRlvYd9vW4RicapwZQbaV5m4GmEFeUW4gLcW0BmwzrUFjuxLJTGXPPI2RMG4W6zWvq7A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwV2Lfu7Sw8ZHpKKXagsyR13P93D02icjGTV8TWwPBA7yJQdsEicSuEeVDcQv9AzxGkgG459024VU62NaODvXYiaH5w6CpYADg4voU/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwURRiaEGD7XObCbGeaIliag0xjzRn5Iy7MTEJxQIFOAwklD5I0gzJfl0cpick8Y49wDnCWDc88oAynW6npCLkoekUjN85bkVDSEno/640?wx_fmt=png&from=appmsg)

**图片“藏 ZIP”，到底藏在什么位置？**

平时说“图片隐写”，可能指几种不同做法。

1、把数据放进图片的元数据或辅助块；

2、修改像素最低位，也就是 LSB 隐写；

3、把完整压缩包接到图片数据的后面。

这篇推文讲最后一种：图片尾部附加 ZIP。它能用文件头和文件结构直接观察，不需要先研究像素算法。（因为老师上课演示的这种嘻嘻，大家能做出这种不用罚站目标就达成了😋）

一份常见材料可以这样理解：

**图片开始 → 图片数据 → 图片结束 → 可能存在的其他数据 → ZIP**

JPEG 的开始标记是 “FF D8”，图像流结束标记是 “FF D9”。我们的材料在 JPEG 结束以后，还放了 24 字节其他数据，然后才是 ZIP。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwVporSm84XfRILcjMhFJ4tqCTAZnsia4EtpshFxaqqFc2ofibaslANEVtnPnyZLl8JwgejBTZFBiaErk1tiblaymB3BWr9JgePcZEc/640?wx_fmt=png&from=appmsg)

换成PNG，我们就找文件头：

89 50 4E 47 0D 0A 1A 0A

它以数据块组织内容，图像数据流最后由 `IEND` 块结束。完整的 IEND 块为：

00 00 00 00 49 45 4E 44 AE 42 60 82

前四字节表示数据长度为 0；中间四字节是 “IEND”；最后四字节是 CRC 校验值。

**搜索时用完整的 12 字节，比只搜“IEND”更有辨识度。仍需按块长度确认它确实处于 PNG 结构的末端。**

(https://www.w3.org/TR/png-3/#11IEND)

规定了 IEND 的空数据字段及结束作用。

IEND 标志着 PNG 数据流结束。后面即使仍有字节，也不属于这个 PNG 数据流；能否继续正常显示，取决于看图软件的处理方式。**（我感觉不会考，考了也是让你用AI之类的处理出来）**

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwUeQibso8m0WSDww4S68kQ2FyeSzHxCtzFBASJYse2hGxTM170ReQ8sTkVDVwfZ9ooGJrDC0zq1gMQjBB09GibeK3gNCQzrIvPxg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwXic62QLkicoRXmbIVlsr8QictqibAa4EtWGlVTMBPqiboRUwLEgnyIvABEX8olCHcEOlpcGGGhI2TqtXdXGJmveQNIpiag1wb5jdDNY/640?wx_fmt=png&from=appmsg)

**实战，从“检验材料.jpg”中导出 ZIP**

题目：有图片“检验材料.jpg"，请找出隐写～

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZXQtRibNoDwX4ogvjvDDKOic5mk6ic7Koc21Vn490yPeribLvMl3LbKYSGIaBmiafiaLgxEnPa7YcvGLf0hURo4zQLJKFNDUqw5hLFuFzNwFoq3Pc/640?wx_fmt=jpeg&from=appmsg)

**第一步：确认图片结束位置**

在“查找十六进制数值”中搜索：

FF D9

我们就找到了图片的结束位置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwVRqhJtiakdtWAAyXrYNP5mNIVmfboamCF59ODFJNsbKuRo0FVw9Su3KB5vCvU5T2Jvcia2W5BbJw7PITwKHwh1CrlKRicwNHLuwE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwUjh0tic7m7LfoVRHXSICtibLQdqzC3hLWpicJPdSwfnYYt1iaqwueEbp0XAR8WQTrZAzt3bcD3GvhibwiaSBQCWvRb9BXJoXnxKiatXs/640?wx_fmt=png&from=appmsg)

**第二步：找到 ZIP 的真正起点**

搜索：

50 4B 03 04

这是压缩包开始的文件头的位置

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwXjGUfSsVWtJ7vIuH5D0r2hEXdqpyqmPs7vZ8hRl6MiazwQfDGtANLIibx9icuENt82zb2afNpOXyQj3bXiaibEX7nAxV4529DF3Yos/640?wx_fmt=png&from=appmsg)

**第三步：**确定选区的终点

“50 4B 05 06” 只是 EOCD 的开头，

**不是“ZIP 到这四字节就结束了”****。**

对本例这种普通单卷 ZIP，EOCD 的固定部分占 22 字节，之后还可能有注释。ZIP 的最后一个字节位置可写成：（现实中直接选到最后一个，除非比赛）

最后一个字节的偏移 = EOCD 起点 + 22 + 注释长度 − 1（哈哈哈哈哈，不做这个推文我都不知道，喵）

**第四步：定义块，把字节复制到新文件
右键zip文件头的第一个数字5，点击“定义块起始”，块结尾直接选到最后****。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwWTbPpic0uMCpN5lTgLiavJxOP8Q46KnTn0cia8pI58jyWmx4ME4KMUYGkMztVPc3JXJFT5BzpnKL753AGdh8UjKPF33UtonQMDgA/640?wx_fmt=png&from=appmsg)

编辑 → 复制块 → 到新文件。

保存为 “extracted.zip”。（随便起名字）这个命令复制的是原始字节。如果选了“十六进制数值”或“编辑器显示”等文本复制方式，导出的会是文字，压缩软件无法按原 ZIP 读取。

这道题的zip没有特殊加密，直接打开就能得到答案。flag{isyangyangyangya}

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwWc7AqX3GPyW5SDgF8KlZpiaPsHFgdqXcKn7OaTaXOVehibLGse3GY8wc9ZgUvDkEJNG8F4VrKHZGsFwMEGfvJ7XlsZYbhFZuEOg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwXCOwicCUuBicO10iaLPT6Oxv07PRCxBHPJ3arLbGMhiaQkBQibYOdTVpyALwzsAeS9FsYK6FYdyichjOAbCfiaEknxyJHqgO7fUdYu54/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/ZXQtRibNoDwU4r0hMrCdEpQfkibxiaRTlq9ich8zfwga4EDuJvaqeCnxXzZINYwGib8ibQGQFrQ0IR3HAtHF2tiaS3VxVRJXZho5F7iaqJUVRbcJcOk/640?wx_fmt=png&from=appmsg)

**扩展与补充**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwXTNt1L1CbTaq9TTNibUECGPjcGsLibXpCwN5sD5FsBSJqdagyibIqQbmBvDWzH2ynmmMCHUekRr84bCo52yPhSZjrsEZUPtCCliao/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ZXQtRibNoDwUH1qHiaKWQuwVibjTKSwA5lOKFAxWhiaJoy1RZ7TZ8WIVGj0b6LPM67lSl3ibkkYq8v0SF3iaiaicmE0N4mheo65ZEJNTz6jo9RCGWE4/...