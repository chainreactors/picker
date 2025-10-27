---
title: Win10命令行弹出光驱
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247486535&idx=1&sn=3de4bbef43ce847def0ceae145434929&chksm=fab2cf78cdc5466ef47ea780871191b85f6822ac97c80bd018e8df37310752f397daa46fcbe5&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2023-03-08
fetch_date: 2025-10-04T08:55:34.055815
---

# Win10命令行弹出光驱

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPNpVJpOcLIkAIZiaatjcgq9SWOp8ibSJF1BcKVSGr7q3aibnROggbmIHhv5GXoThAJmOINjkVgNuWAFg/0?wx_fmt=jpeg)

# Win10命令行弹出光驱

原创

TK

青衣十三楼飞花堂

1.22 Win10命令行弹出光驱

https://scz.617.cn/windows/202303061753.txt

A: TK & ChatGPT 2023-03-06

mshta "javascript:new ActiveXObject('WMPlayer.OCX').cdromCollection.Item(0).Eject();window.close();"

mshta是Windows自带工具，算是一个IE组件，但可以独立运行，底层使用HTA引擎。通过mshta可在命令行执行JavaScript脚本、运行ActiveX控件等。上述命令大致干了
三件事

a) 创建名为"WMPlayer.OCX"的ActiveX对象，对应Windows Media Player控件的实例
b) 从本机所有光驱中选第一个，用"Eject()"方法弹出光驱
c) 调用JavaScript的"window.close()"方法关闭当前窗口

若本机未安装Windows Media Player控件，上述命令将报错。

参看

Poweliks - Command Line Confusion - Benoit Ancel [2014-08-20]
https://www.stormshield.com/news/poweliks-command-line-confusion/

展示了另一种使用HTA引擎的奇技淫巧

rundll32.exe javascript:"\..\mshtml.dll,RunHTMLApplication ";alert('foo');alert('bar');window.close();

在Win10上测试上述命令，将"mshtml.dll"写成"mshtml"时，会被Windows Defender发现、告警、拒绝执行，报告发现"Trojan:Win32/Powessere.G"，就本例而言这是误报，只能说该操作曾为恶意软件所用。这种写法认百分号编码，比如%20、%27之类的。

rundll32.exe javascript:"\..\mshtml.dll,RunHTMLApplication ";alert(%27foo');alert('bar%27);window.close();

为了用第二种方式弹出光驱，必须将new之后的空格代之以%20，原理参前述URL

rundll32.exe javascript:"\..\mshtml.dll,RunHTMLApplication ";new%20ActiveXObject('WMPlayer.OCX').cdromCollection.Item(0).Eject();window.close();

-----

起因是微博上有人怀旧，说茶杯托的事，tk转发时说mshta也可以让你拥有茶杯托。虽然知道mshta的存在，但我从未用过mshta，这东西除了坏人、黑五类之类的，正常人不会用的，我是正常人。尽管如此，还是试了试，甚至让ChatGPT帮着解释了这条命令。茶杯托没有，小屏风倒是有一扇，tk建议机箱卧放达成原始目的。他还提到rundll32使用HTA引擎的方案，但一开始我没成功，看了他给的那个URL后明白了原理，稍做修正后也成功了。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

青衣十三楼飞花堂

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/VbJOzZqovPPoySptTrxD06kCctXhGgQYZW0c0DRia8IJn5AbKdQCtQjACoUdkP9QvsXo0icz8JYQ55t7Gv0L6YcA/0?wx_fmt=png)

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