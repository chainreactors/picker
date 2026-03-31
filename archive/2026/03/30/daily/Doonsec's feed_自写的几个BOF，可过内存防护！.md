---
title: 自写的几个BOF，可过内存防护！
url: https://mp.weixin.qq.com/s/89oU-ZV-F3uv29CbudGssg
source: Doonsec's feed
date: 2026-03-30
fetch_date: 2026-03-31T04:31:15.692729
---

# 自写的几个BOF，可过内存防护！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/lFfjZayicKlEEVAkYwwR86Hge6QOIewSrsXDejJgcdNHCKibSx7bsH47B98prIPg9WYZ1Mb4FQ1ichWHZLwnsriaicoPiaM6WDJUjlgA3XicrYBqkA/0?wx_fmt=jpeg)

# 自写的几个BOF，可过内存防护！

蚁景网安

![]()

在小说阅读器中沉浸阅读

以下文章来源于潇湘信安
，作者3had0w

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6fpNgxJic72iaxuNHwNA0BooiblUaaQuiavCyr7GWWPulUHw/0)

**潇湘信安**
.

一个不会编程、挖SRC、代码审计的安全爱好者，主要分享一些安全经验、渗透思路、奇淫技巧与知识总结。

**0x00 前言**

前两年在和一些师傅的交流中很多人说现在国内杀软的内存防护拦截了CobaltStrike的`execute-assembly`命令（如某绒…），只要执行.NET程序就会出现下图报错提示或者直接掉线，如下图所示。

* 仅记录模式：执行.NET会临时卡掉线一段时间，然后报出下图错误，但不会掉线！出现这种情况基本就可以确定是被内存防护拦了，但攻击行为只会被记录在安全日志中，上线木马文件也不会被查杀。

* 自动处理模式：执行.NET后会触发告警弹窗并立即掉线（上线木马文件也会被删掉清理），还会将此攻击行为记录在安全日志中，即使用于上线的免杀木马可过静态查杀，但只要触发内存防护拦截一样会杀。

* 记得火绒的内存防护默认选项为仅记录模式，但我们在实战测试中如遇到火绒时还是得注意下这个。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tNyBeBKReNK0X7HDBsrnKpTv7G1S1IAic3md0ykT197qyj2bsicbibwKLjDx0QXiadPgh35QtBeKPGO8icgZ7udOx5EHbybUYpTwsmiaibOhVZPQ04/640?wx_fmt=webp&from=appmsg)

其实这个问题很早就发现了，所以之前在写`PostExpKit`插件时就在“权限提升”中单独写了个`“InlineExecute[.NET]”`用于应对以上拦截场景，不知道是不会用？还是没有看到？如下图所示。

* https://github.com/EricEsquivel/Inline-EA
* https://github.com/anthemtotheego/InlineExecute-Assembly

**使用方法也很简单，主要也就3个选项：1.常用NET土豆、2.其他NET程序、3.运行NET参数：**

* 常用NET土豆：内置了几个常用Potato提权exp，默认执行该选项，要执行啥命令在“运行NET参数”处修改就行，而且在执行带空格命令时不用加双引号（插件代码中已做处理）！
* 其他NET程序：该选项用于执行我们自写或开源.NET程序，点击后边的文件选择框找到要执行的.NET程序，在“运行NET参数”输入要执行的参数和命令即可，不会执行“常用NET土豆”。
* 运行NET参数：该选项用于以上两个要执行.NET程序中输入参数和命令，如果没有留空即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tNyBeBKReNIoNf5vMEXMaD5YZsImmuwAb70ZJbsHxBAn1qpT0UiaLenyjbhgYfLG9H3qEogwhb3YGRWvicexXBRR1cfKnSD5Kg2O4XialUOdwg/640?wx_fmt=webp&from=appmsg)

又有点跑题了，想到就顺便记录下，现在回归到正题：以前写那插件的“查询/开启/关闭RDP端口”功能也是用我很早之前写的一个.NET工具，所以现在也都没法用了...。

这几天抽空又写了几个用于绕过以上场景进行信息收集的BOF（CobaltStrike的`inline-execute`内存执行方式目前暂时还没有被拦）。

CNA插件脚本我就不写了，大家自己去写下吧，其实都挺简单的，直接使用`beacon_inline_execute`这个函数去执行我们编译好的BOF即可。

**0x01 检查360核晶**

这个BOF用于检查360安全软件是否已开启360核晶防护引擎？主要通过

`HKLM\SYSTEM\CurrentControlSet\Services\360Hvm`注册表`WorkConfig`值判断（1为开启，0为关闭），如下图所示。

```
reg query HKLM\SYSTEM\CurrentControlSet\Services\360Hvm /v WorkConfig
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tNyBeBKReNIyKT4ex5aycTiaCzL8ibsmGIYBbzXykCSv8KhmY7wcicQ7zDT3bUQfqkYqpt3EiaqCxyUmX9BpnVAggdA3jJVnCiaKyNyOszYwZttQ/640?wx_fmt=webp&from=appmsg)

如果目标主机上不存在360安全防护软件，我们在执行这个BOF就可能会出现以下报错`RegOpenKeyExW failed: 2`，因为指定的`360Hvm`注册表项不存在，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tNyBeBKReNJLw2nst6rnPrDmofQFXw2fhPn8OHZCLYP5mgw9nfheHolmPtmdrOwG2C1Qm6EJziawsj22qetkqbXNlONmG2BTv1H2nrHtuEeA/640?wx_fmt=webp&from=appmsg)

**0x02 检查3389端口**

这个BOF用于检查目标主机是否已开启RDP端口和对应端口号？也能开启或关闭RDP端口（需要`Admin/System`高权限），主要通过查询、修改以下几个注册表实现对应功能，如下图所示。

```
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v fEnableWinStationreg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v fEnableWinStation /t REG_DWORD /d 1 /f
reg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server\WinStations\RDP-Tcp" /v PortNumberreg query "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnectionsreg add "HKLM\SYSTEM\CurrentControlSet\Control\Terminal Server" /v fDenyTSConnections /t REG_DWORD /d 0 /f
```

工具参数：

```
Usage: inline-execute CheckRDP.[x64/x86].o [options]
-ps    Check RDP Service Port/Status-on    Open RDP Service Port-off   Close RDP Service Port
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/tNyBeBKReNJJSmt6FlL3VfdaXYvtqZGnF1jB7jUXbrAuF747KpBrN4OtiarVbw2Owq15r5I1vmJ0ltsImC8Aw9qticibooMerichjB3tJ8HczeQ/640?wx_fmt=webp&from=appmsg)

**注意：**我们在某绒下测试发现使用这个BOF开启或关闭RDP端口时只有首次能执行成功，就是说可以执行成功，但也会触发内存防护拦截，查询RDP端口开放情况和端口号没问题，如下图所示。

**仅记录模式下会出现报错**`5`**：**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tNyBeBKReNL1emzb84Wesag0gaIU7y5IkbvHG9IVjDOKEfKfZfKBDLGfcFcTv3n2PbmyqzD4lTyCe8v7k7bf7ltD8wCpXRziclvtLa8hlq0Q/640?wx_fmt=webp&from=appmsg)

**自动处理模式下会掉线清除木马：**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/tNyBeBKReNJ5n5oFknrpMgvShO8b4VHNDVOg54mxo6ibyuMMr4N9sRqDmFkxp38PZ6pibE8T5rxSE9ret5eibWpEfHkjKkf5rLzCSrsmiaicgxE0/640?wx_fmt=webp&from=appmsg)

**0x03 检查AV/EDR进程**

这个BOF用于检查目标主机正在运行的进程列表中是否有AV/EDR等安全防护软件相关进程？源码中暂时不提供进程数据，只拿了4个D盾进程用于示例，大家可以自己去收集整理，如下图所示。

![](https://mmbiz.qpic.cn/mmbiz_jpg/tNyBeBKReNLu6eIYSBlzBcwuKoAmFXmdlzxiagFIqR3C7O8ZUjPpN9G8ticIVvwxvTs6diaPDY3hzdro55ib1cN1BJHBl37UwmCmgPJRBqyUNSk/640?wx_fmt=webp&from=appmsg)

**文末小结**

关于过防护的问题我只测了某绒，360没去细测（应该也能过），自己去测下吧。另外分享这几个源码算是抛砖引玉，感兴趣的师傅可以自己参考着去写写，建议可以看下24师傅和老外的几个项目源码，现在有了AI加持，只要稍微有点基础能看懂部分源码，自己写一些小工具小项目是没问题的...！！！

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