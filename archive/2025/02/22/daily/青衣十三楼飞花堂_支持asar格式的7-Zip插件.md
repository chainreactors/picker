---
title: 支持asar格式的7-Zip插件
url: https://mp.weixin.qq.com/s?__biz=MzUzMjQyMDE3Ng==&mid=2247488004&idx=1&sn=78d56d15140d0f6f8931de84a251b612&chksm=fab2d13bcdc5582d13d7c673d5ef0b9e9d366fd86ffe5c741abec48c45a3706d4717849eba60&scene=58&subscene=0#rd
source: 青衣十三楼飞花堂
date: 2025-02-22
fetch_date: 2025-10-06T20:37:16.406014
---

# 支持asar格式的7-Zip插件

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/VbJOzZqovPMIhxjfrpKvkTwx3oZ6NPGT97lvqIkzzH90PUNzibU0g1rrdBnmhlsrr55DZN7ianribtmkMkXyuXRIg/0?wx_fmt=jpeg)

# 支持asar格式的7-Zip插件

原创

沈沉舟

青衣十三楼飞花堂

分享《Electron逆向工程入门》后，小宋觉得原文中这段内容对他很有帮助:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VbJOzZqovPMIhxjfrpKvkTwx3oZ6NPGTib1pibzeDmynHib63mbbgIHlFxbNagbks5EPtnzg8I8vI3ZgMU6g0rL3w/640?wx_fmt=png&from=appmsg)

与此同时，小宋补充了一条信息。参看:

```
Asar7z
https://www.tc4shell.com/en/7zip/asar/
https://www.tc4shell.com/binary/Asar.zip
```

Asar7z是个7-Zip插件，放到

```
C:\Program Files\7-Zip\Formats\Asar.64.dll
```

之后7-Zip可以解包、打包app.asar，比"@electron/asar"方便。

简单测试，用Asar7z插件解包、打包app.asar，无需app.asar.unpacked目录在场。暂未用第三方Electron桌面应用测试Asar7z插件新打包app.asar的可用性。

假设无其他幺蛾子的话，逆向Windows平台Electron桌面应用时，无需Node.js环境。解包、打包有7-Zip，动态调试有"chrome://inspect"。

此信息已更新至TXT。

有许多泛业内同行，主要是来看点儿技术内容。我本来以为自己这号主要是分享技术的，事与愿违，尽扯些不着四六的淡了。一年下来，分享不了几次技术，但每次分享技术时，都争取对别人有所助益，一丁点助益也是助益，不套路谁。另一方面，在分享技术的同时，我也得到许多意料之外的反馈式助益，包括但不限于小宋这次。个人精力总是有限的，你与你的补集肯定不是对等的，与君共勉。

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