---
title: 如何将BootLoader与APP合并成一个固件
url: https://mp.weixin.qq.com/s/Y_xSsF0KFnv2H9H4OU6Atw
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:15:55.246047
---

# 如何将BootLoader与APP合并成一个固件

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/zQ19N6bPViaBmfHzBFOJ7pHqiaHaiaNG9PggMTqU4n7AbCcpN83WQjicaic7uIV9BXYgewh84KW0uib3fw6oC5ehA7NvEvJZAyCnpteXiaUtYsVkPc/0?wx_fmt=jpeg)

# 如何将BootLoader与APP合并成一个固件

谈思实验室

![]()

在小说阅读器中沉浸阅读

点击上方蓝字谈思实验室

获取更多汽车网络安全资讯

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247570872&idx=3&sn=cb06ec7ad7a7fd4d33e1c5ab68777b3b&scene=21#wechat_redirect)

**01**

**前言**

嵌入式固件一般分为BootLoader和App，BootLoader用于启动校验、App升级、App版本回滚等功能，BootLoader在cpu上电第一阶段中运行，之后跳转至App地址执行应用程序。

因此，在发布固件的时候，会存在BootLoader固件和App固件；此时我们期望是将BootLoader固件和App固件合并成为一个固件，这样在量产时只需烧录一次即可。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9vCNG4B1rD4kwqw3kkgQhIiakFq9gM3fWXiaibl2xl8ERE4kje31cpCIGAQ4TJdrN96jmu0luVbqEwA/640?wx_fmt=png&from=appmsg)

**02**

**传统方式**

一些传统的方法都是“土办法”，没什么毛病，但比较繁琐。

项目种类增加，或者版本发布频繁时更加体现出繁琐性，且易出错，操作稍微失误可能导致固件不完整；烧录不完整的固件，机子变“砖头”。

1、烧录两次，分别烧录BootLoader和App固件

2、烧录固件到芯片后，再从芯片读取固件，另存为hex文件

3、手动复制、合并固件

4、BootLoader支持App固件传输功能的，只烧录BootLoader，后期再升级App

**03**

**高效方式**

我们目标是通过自动化脚本合并生成一个发布固件，提高效率和确保固件的完整性。

**3.1 合并文件**

Linux下的脚本我们用得很多，其实Windows的脚本也非常优秀，利用Windows的脚本可以快速实现增、删、查、改文件。常用Windows脚本命令如下。

1、合并两个文件：copy /b

2、重命名文件：ren

3、删除文件：del

很显然，我们利用其合并命令，只需一条指令即可将BootLoader和App文件合并。

例子：假设当前目录存在Boot.bin和App.bin文件，合并后文件命名为Firmware.bin。

```
copy /b .\Boot.bin + .\App.bin Firmware.bin
```

> 注：Windows的目录路径为反斜杠，与Linux不同。

**3.2 bin转hex**

我们知道，二进制（bin）文件是不存在地址信息的，cpu上电执行并不一定是从地址0开始执行代码，如STM32芯片起始执行地址为0x8000000。

因此不能通过串口工具烧录bin文件，只能通过J-link或者ST-link烧录，并且在烧录前指定存储起始地址。因此，将bin文件转换为hex文件是有必要的。

**bin转hex方式：**

1、使用jflash工具，把合并后的bin文件，使用jflash打开，另存为hex格式文件

2、将bin文件烧录置芯片，读取出来，另存为hex文件

3、自己动手写一个bin转hex工具

4、借助第三方bin转hex工具

前两者太繁琐，效率低下；第三个比较灵活，但需要花点时间；如果使用优秀的现成工具是最快捷的办法。推荐使用“srec\_cat.exe”工具，可以结合Windows脚本一起使用。

**3.2.1 srec\_cat工具**

srec\_cat一个功能非常强大的文件合并、转换工具，支持功能众多，包括：

文件合并

文件分割

bin转hex

hex转bin

数据填充

CRC校验

此外，还存在srec的系列工具，文件比较工具 srec\_cmp.exe和文件信息查看工具 srec\_info.exe，可以从文章后面官方网站下载使用。

文件合并

命令格式：

```
srec_cat.exe <源文件0> <文件类型> <源文件1> <文件类型> <目标文件> <文件类型>
```

例子：

```
srec_cat.exe source0.bin -Binary source1.bin -Binary -o merge.bin -Binary
srec_cat.exe source0.hex -Intel source1.hex -Intel -o merge.hex -Intel
```

如果BootLoader和App生产的文件为hex格式，可以直接使用该命令合并为一个hex文件，注意地址的连续性。

**bin转hex**

命令格式：srec\_cat.exe<-Binary> <-offset> <偏移地址> <-Output><-Intel>

例子：

将Boot.bin和App.bin合并的Firmware.bin转换为hex格式文件。

```
srec_cat.exe Firmware.bin -Binary -offset 0x8000000 -o Firmware.hex -Intel
```

0x8000000，是STM32的起始执行地址

更多的srec应用和工具下载详见官方网站：

http://srecord.sourceforge.net/download.html

**3.3 完整示例**

第一步，在需要生成固件目录新建一个txt文件 第二步，键入如下内容(Boot固件和App固件可以指定目录)

```
copy /b .\Boot.bin + .\App.bin Firmware.bin
srec_cat.exe Firmware.bin -Binary -offset 0x8000000 -o Firmware.hex -Intel
del Firmware.bin
```

第三步，重命名txt文件为".bat"后缀文件，即是Windows可执行脚本的文件类型 第四步，双击运行脚本，即可生成目标文件 出现任何目标文件生成失败的情况，检查相关源文件是否存在，路径是否正确。

**3.4 举一反三**

以此类比，存在多个App文件的情况，可以通过该方式分别进行合并出一个固件。

另外，实际项目中，经常会使用内部flash空闲扇区保存一些设备参数信息，如校准系数、设备地址、序列号等信息，我们可以将参数信息保存为一个bin文件，通过该方式和固件合并，这样量产时将参数和固件一并写入，提高生产效率！

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9vCNG4B1rD4kwqw3kkgQhIlODyQB2mWEZKA11ve2xP4S4C4QX9FWLiaJ1VQS4GBE5BTVUUiaa5TeRw/640?wx_fmt=png&from=appmsg)

来源：汽车电子嵌入式

谈思-汽车出海安全合规（欧洲）

交流群

谈思 AutoSec Europe 峰会旨在搭建一个能融汇全球视野与中国实践、连接技术前沿与落地应用的国际性专业平台，以助力中国汽车应对在出海过程中面临的网络与数据安全合规痛点。从前沿技术研讨、合规要点解析到经验交流，都将通过本平台为您提供持续支持。社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwibTH2iaYqMA6sf7DgCTTHwEaAvzywYkvdmgUK1SGVhE9yFHl4kVTARp5M5LiaVIM6WcG0PcXYsZZEbQ/640?wx_fmt=png&from=appmsg)

谈思-SDV&AIDV技术出海

交流群

诚邀行业同仁加入谈思SDV&AIDV出海技术交流群，聚焦软件定义汽车、AI定义汽车、下一代EEA、智能座舱、智能驾驶、软件架构、域控制器开发、芯片技术、软件工具等核心议题，欢迎大家加群交流探讨~~社群已超过200人，需邀请加入，如需入群，欢迎添加社群小助手微信taaslabs01。

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9c00NyPNPSRjUzbpUxiaFiakfz8AEVJkxCmGicv14KyKqgPM8H649icFnmroPiaR6UvNSZwhCrN3T3UYg/640?wx_fmt=png&from=appmsg)

**end**

![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJlH8rNickiaaHhLM4PaibcicFO9usS5xIOrWYjZibuvwV8g9DwnI6xZ4RvHg/640?wx_fmt=jpeg&from=appmsg)

**谈思汽车媒体门户**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Tw9hgqzDyib0J4ico1LVFEZ2QnqGKQhnxdoZeiaZAHaGnnTnFGDvlfibtd8h389z8H20gh1icn8yhxrx8yw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzkyODQzMDI3Mw==&mid=2247549590&idx=1&sn=b5ea25965c057d1ca2913d900f77799d&scene=21#wechat_redirect)

**精品活动推荐**

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9TwicHdaQsibvoH8dLYIIcT5YQibwbnuZn1MLCOMydw2SMKWbibsLpooeE2jgCt8FABvsVmlJZO5PO00Ryw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561756&idx=2&sn=f9b8c214978537f47cccba736cdb5bfd&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twic6W3pPRJKNsjTsOjFEnbDjGVKhNDauD7EKNEsgmvdiacDaEk4AicICiaCkwv9lWSWicXN6yJwZKVAlrQ/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247563394&idx=2&sn=ed98964862cf2f8280a4d6db9cd0a273&scene=21#wechat_redirect)

**AutoSec系列沙龙**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkP4bDWQkLJvELA6L8vJsCRctQMTiasyhKEkb1ujgIjlGBVx91jbsQ29g/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247548574&idx=1&sn=11f37456b4f45c0fdbf795c21e201c03&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkO7zMw9U0oRCldUrRpcKyGwogwoUbpTJXic56yibibZ6Wqzr6C2P6iaFJWQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247551934&idx=2&sn=50785b76c512a88b30455fc1e8fa188c&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkVh6Z43iczWWhmnKMicdo0WU9VCzDFa2N2eiaJIogkxsLEEFt8wJ6W0CUA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247557132&idx=2&sn=2e44d4c2d77a2eec377d0553442d2c1b&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw80qwJ0DQGXJ8KiakP0yVicGI8mlMKIokicyytiaYrN6BIBOybqkYX7KSXwbia50cic232dG7BnYibKqHasA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561775&idx=1&sn=948a9e7f8d4fbed363c6a6a5479cd39e&scene=21#wechat_redirect)

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Tw9gTWqQo9uE8zDK0WVUUjMkfxA4GZice84BsCR4zGV0oqJXpEjUsUpGKcFcCx1BiaDYDQU4cT3nTtpA/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247561260&idx=2&sn=0ca6395502487515a921f32288b7e8df&scene=21#wechat_redirect)

**专业社群**

[![](https://mmbiz.qpic.cn/mmbiz_jpg/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJnASqAJY7fLYIeMGl8fHu4aPXusCVuX2qAYkrb9bQMRGEBvSghHETaQ/640?wx_fmt=jpeg&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&scene=21#wechat_redirect)

**部分入群专家来自：**

**新势力车企：**

特斯拉、理想、极氪、小米、零跑汽车、阿维塔汽车、智己汽车、小鹏、岚图汽车、蔚来汽车、吉祥汽车、赛力斯......

**外资传统主流车企代表:**

大众中国、大众酷翼、奥迪汽车、宝马、福特、戴姆勒-奔驰、通用、保时捷、沃尔沃、现代汽车、日产汽车、捷豹路虎、斯堪尼亚......

**内资传统主流车企：**

吉利汽车、上汽乘用车、长城汽车、上汽大众、长安汽车、北京汽车、东风汽车、广汽、比亚迪、一汽集团、一汽解放、东风商用、上汽商用......

**全球领先一级供应商：**

博世、大陆集团、联合汽车电子、安波福、采埃孚、科世达、舍弗勒、霍尼韦尔、大疆、日立、哈曼、华为、百度、联想、联发科、普瑞均胜、德赛西威、蜂巢转向、均联智行、武汉光庭、星纪魅族、中车集团、潍柴集团、地平线、紫光同芯、字节跳动、......

**二级供应商(500+以上)：**

中科数测、ETAS、BlackDuck、NXP、上海软件中心、Deloitte、奇安信、为辰信安、云驰未来、信长城、泽鹿安全、纽创信安、复旦微电子、天融信、奇虎360、中汽中心、中国汽研、上海汽检、加特兰微电子、浙江大学......

**人员占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJVW2JR9ib5icMR4wIs58nO6ia3OicH5l6vONnmuhfLqMKqj8T2AnD7W1vqQ/640?wx_fmt=png&from=appmsg)

**公司类型占比**

![](https://mmbiz.qpic.cn/mmbiz_png/3g8Dklb9Twicgqayv6EVjeHah3Bpvw2ZJU6yKtYSJu4oPaJABYuCSyTpLXjRNbVv7OUTUUCxmB1OuPhtcM4j1kw/640?wx_fmt=png&from=appmsg)

**文章**

# [不要错过哦，这可能是汽车网络安全产业最大的专属社区！](http://mp.weixin.qq.com/s?__biz=MzIzOTc2OTAxMg==&mid=2247535223&idx=1&sn=e30e07a44accd5b0e9ada3d8b537f977&chksm=e9270eacde5087bacb4d9c888f3a21ceae227156c89aba0be7d9ebc8b02a68b4f11e7595255a&scene=21#wechat_redirect)

[关于涉嫌仿冒AutoSec会议品牌的律师声明](http://mp.w...