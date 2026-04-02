---
title: 逆向分析：Office VBS宏类型文档
url: https://mp.weixin.qq.com/s/44D52OzOVDvvG5fQmtNrbQ
source: Doonsec's feed
date: 2026-04-01
fetch_date: 2026-04-02T04:26:11.027550
---

# 逆向分析：Office VBS宏类型文档

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/lFfjZayicKlFJMcLcGFibm4xH27yhHIib7QC2yv29u5qxWxpXgBuUqP7MGcZsFs7R8C8rXOiaDUgRoovPTevMRucwiapn7EYsF697GicZjoibYy0Nw/0?wx_fmt=jpeg)

# 逆向分析：Office VBS宏类型文档

蚁景网安

![]()

在小说阅读器中沉浸阅读

以下文章来源于蚁景网络安全
，作者Ba0

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7Yk0SeU4ibQcLl1mDLlqhbAOdK1Ik3EO85soOvkh9e8wQ/0)

**蚁景网络安全**
.

致力于为你带来更实用的网络安全技术内容！

该题目贴合实际，在实战中经常遇到此类宏病毒。

将Office文档中嵌入以VBA(Visual Basic for Applications)编写的宏代码脚本，当运行Office文档时，便可以执行各种命令。

VBA脚本文件重定向能够将脚本默认文件vbaProject.bin进行替换，在打开文本时加载其他文件，增加分析者的分析复杂程度。

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxTUtVia8KF903QJBfhO5g2u80QykhDGqvZmOTGm1y5OFVSGibUgz16NphKreupUX4ibNqfOicbL6wWsw/640?wx_fmt=other&from=appmsg "null")

## 1、初步分析

> 在 Office 2007 之后的 Office 文档格式采用的是 OOXML 标准格式。那什么是 OOXML 标准？这里的 OOXML 的全称是 Office Open XML File Formats 或被称为 OpenXML 格式，这是一个基于 zip+xml 定义的文档格式。简单的说就是Office文档是一些xml文档压缩文件，因此我们将一个word文档进行zip解压，可以获得一些xml文件

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxTUtVia8KF903QJBfhO5g2u5q4eo367No044uGHUSDTlYyCx5k87RpqHDpcfYOYMdRhDpjIWWOTWQ/640?wx_fmt=other&from=appmsg "null")

‍

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxTUtVia8KF903QJBfhO5g2ubTrzklu4GbUcQkF119DRkAY4mfwCa48LVib31jia1ZvxDYx5K7CqhxwQ/640?wx_fmt=other&from=appmsg "null")

打开发现是一堆乱码，此时就需要借助大佬们的工具了。

## 2、oletools

oletools对该文件进行分析，oletools将宏源码完整的还原了出来。

官网：https://github.com/decalage2/oletools/releases

这里采用pip安装模式

```
pip install -U oletools
```

运行命令

```
olevba -c protected_secret.docm > code.vbs
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxTUtVia8KF903QJBfhO5g2uSsx1IHM8ybfSPsMNJBd0j2YAXGuPGN9XnxZmnf5ibPia5QaS5OibzFmDg/640?wx_fmt=other&from=appmsg "null")

## 3、分析vbs代码

直接搜索：`AutoOpen`

里面有太多垃圾代码了

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxTUtVia8KF903QJBfhO5g2u0blzX96YU5RWwnbm7NpLFMZJ1cmTDYhUn5FH8fXmrKqVvXAXO8jDhg/640?wx_fmt=other&from=appmsg "null")

首先将输入的flag异或7

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxTUtVia8KF903QJBfhO5g2uX6piarwOsfjbvd4UClOkFgStRBHweLVk3sgnmlMicXQ8xfPCqFckv1yg/640?wx_fmt=other&from=appmsg "null")

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxTUtVia8KF903QJBfhO5g2uCSjF6cF2bfes7msN6J6870nbgNx5V931GqWiarZQJfKlXnE46WmNWFw/640?wx_fmt=other&from=appmsg "null")

有点意思了，解码exe的base64编码，然后运行exe执行操作，最后再删除exe程序

## 4、运行Vbs得到exe

将重要的代码拿出来，然后生成exe

```
Set fso =CreateObject("Scripting.FileSystemObject")
Set objShell =CreateObject("WScript.Shell")

/*
省略了一大堆 base64赋值串
*/

tempPath ="D:\temp11\temp"
Set tempfile = fso.CreateTextFile(tempPath,True)
fso.GetFile(tempPath).Attributes=2
tempfile.WriteLine xpkdb
tempfile.Close

batPath ="D:\temp11\temp.bat"
Set batFile = fso.CreateTextFile(batPath,True)
fso.GetFile(batPath).Attributes=2
batFile.WriteLine"@echo off"
batFile.WriteLine"certutil -decode temp1 temp|certutil -decode temp temp.exe"
batFile.Close
Set objExec = objShell.Exec(batPath)
```

保存为vbs运行，但是我电脑有点小问题没跑运行起来

因此我们采取另一种方法，直接将base64提取出来

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxTUtVia8KF903QJBfhO5g2uwNv0qAugSh2yBO6E6WjkukibrsJktzrM2PicthdzibP2SUp06XIKXOiakA/640?wx_fmt=other&from=appmsg "null")

代码很简单，将提取出来的代码放进Cyberchef进行提取即可

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxTUtVia8KF903QJBfhO5g2u6YgDOpO6ft3ZO3SUNt8xCPibavnRbJHBWiakIq7GQDUwPOLcKtq8kIRg/640?wx_fmt=other&from=appmsg "null")

## 5、分析exe

![](https://mmbiz.qpic.cn/mmbiz_jpg/5znJiaZxqldxTUtVia8KF903QJBfhO5g2ury0aicp9Yh894k5KzJFzshWSztEBhPKnmoZsoDotvzwibQG4KJTfcaXA/640?wx_fmt=other&from=appmsg "null")

很简单的代码，就是位移

## 6、解密

```
v9 = [0]*54
v9[0]=4288
v9[1]=4480
v9[2]=5376
v9[3]=4352
v9[4]=5312
v9[5]=4160
v9[6]=7936
v9[7]=5184
v9[8]=6464
v9[9]=6528
v9[10]=5632
v9[11]=3456
v9[12]=7424
v9[13]=5632
v9[14]=6336
v9[15]=6528
v9[16]=6720
v9[17]=6144
v9[18]=6272
v9[19]=7488
v9[20]=6656
v9[21]=7296
v9[22]=7424
v9[23]=2432
v9[24]=2432
v9[25]=2432
v9[26]=5632
v9[27]=4416
v9[28]=3456
v9[29]=7168
v9[30]=6528
v9[31]=7488
v9[32]=6272
v9[33]=5632
v9[34]=3520
v9[35]=6208
v9[36]=5632
v9[37]=4736
v9[38]=6528
v9[39]=6400
v9[40]=7488
v9[41]=3520
v9[42]=5632
v9[43]=5184
v9[44]=3456
v9[45]=7488
v9[46]=7296
v9[47]=3200
v9[48]=6272
v9[49]=7424
v9[50]=2432
v9[51]=2432
v9[52]=2432
v9[53]=7808

flag =''
for i in range(54):
    flag += chr(v9[i]>>6^7)

print(flag)
```

![图片](https://mmbiz.qpic.cn/mmbiz_gif/7QRTvkK2qC6iavic0tIJIoZCwKvUYnFFiaibgSm6mrFp1ZjAg4ITRicicuLN88YodIuqtF4DcUs9sruBa0bFLtX59lQQ/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=21)

学习网安实战课程，戳“阅读原文”

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

蚁景网安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/TL4Y9UAcgruasR1ULCzS2icYoNn4Yz5aKdDv4u2Z8JA7ru620vsrtZjDIFMQzJFyicnn9YgOQQtbfraAJvNbwvAA/0?wx_fmt=png)

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