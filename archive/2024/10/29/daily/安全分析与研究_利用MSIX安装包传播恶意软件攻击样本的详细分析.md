---
title: 利用MSIX安装包传播恶意软件攻击样本的详细分析
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489274&idx=1&sn=fb33148fde138e8c7d6566edc9bbd518&chksm=902fb9d2a75830c4869671bbce0508c024b10ebbaa885961938ad3f1cf69316da19b39acc4d8&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-10-29
fetch_date: 2025-10-06T18:50:36.659077
---

# 利用MSIX安装包传播恶意软件攻击样本的详细分析

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLrembD42uPlERovR7icibS0dA6nRgbMjbib57Fib1wPj8ONKft8VIGJ3YLYMQ/0?wx_fmt=jpeg)

# 利用MSIX安装包传播恶意软件攻击样本的详细分析

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/14111

先知社区 作者：熊猫正正

MSIX是一种Windows应用包格式，可以为所有Windows 应用提供现代打包体验， MSIX 包格式保留了现有应用包和安装文件的功能，此外它还为Win32、WPF和Windows窗体应用启用了全新的现代打包和部署功能。

从去年年底开始，全球范围内越来越多的攻击者开始使用MSIX类型的安装包传播各种恶意软件，这些MSIX安装包样本大多数包含正常的数字签名，下面针对一些MSIX安装包样本进行详细分析。

样本分析

1.MSIX大多数样本都带有正常的数字签名，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreibTLS0yNufmog7CBqt2CdG8z5DuooqTISNicMXQVK27cGgRO5p0V1Yqw/640?wx_fmt=png)

2.安装程序运行之后，会调用执行StartingScriptWrapper.ps1脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLrekgtDOBnZPmgR3QibkmFNY7RG1Libry0IJ81micVUicTlYsR8Pk86JibDHSQ/640?wx_fmt=png)

3.然后执行refresh.ps1恶意脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreBQdPtOVRoazkHMm8ttm8ZDLL1UY8hTrdfxKEcnlyFHpqOc0V9ELjPA/640?wx_fmt=png)

4.研究一下MSIX安装包是如何调用恶意PS脚本的，首先MSIX安装包会更改应用程序的入口点AppxManifest.xml，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreSHuBL7BFEu7SZ0BTFhSewicNicNeQCCicaESQbnRqWFsj92JSetWuSByQ/640?wx_fmt=png)

5.使用PSF Launcher 充当应用程序的包装器，它将 PSF 注入psfRuntime到应用程序进程中，然后激活它，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreSwibQMx42Z4E5uQSiaaEFnnH0Wvuz2iczXc6VYjvaic2ceOX73opIMYOPg/640?wx_fmt=png)

6.然后调用执行StartingScriptWrapper.ps1脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreMuW8ukziaYsHEZyvnK4Ugyry5iakZv6B6rmr5PPI7de5Aswsfkcppcaw/640?wx_fmt=png)

7.读取config.json配置文件信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLrecLoE1gDuUOuos0pFVEBFfibobY9Lk4fOe3O1U1I7Nm58M4B5URY3zow/640?wx_fmt=png)

8.config.json配置文件启动脚本信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreiaBAtQTMXzMJcCPV2jrz0pLDHbChCdcUSqaIgt5j382oFeEgohZNsbA/640?wx_fmt=png)

9.按配置信息中指定的脚本执行模式和脚本路径，调用执行refresh.ps1恶意脚本，refresh.ps1恶意脚本使用空白字符进行混淆，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLrerozyd9z2YNsia8XWh6yibE8Fj3ySqbOqdF0S3ia9y4g0ibPVoG8w5VDficQ/640?wx_fmt=png)

10.解密之后，从远程服务器上下载执行恶意脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreHaMOKslZnqmY7PWWONibCTwATASpu6sy4sJzTyqSXa3G4QxQBXApnEg/640?wx_fmt=png)

由于远程服务器已经关闭了，无法下载到后续的脚本，暂不作研究了。

11.另一个MSIX安装包样本，数字签名如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreuFibVsuBpzfRUsicNQlzyyzhQxMt6zEghHaOR25SaE9ibDAUlBbXnMib1g/640?wx_fmt=png)

12.样本解压之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreudsIPnB1vJFjopXvdrmkZammejYB12WKzJmlZDxz81j8lbPIn3icsEA/640?wx_fmt=png)

13.通过上面的分析结论，查看config.json配置文件信息，该MSIX安装包会调用目录下的new\_raw.ps1恶意脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreuk287htHcdAokAmCMdss0xHukIhjJKOSOIbghV474xxCrBfInJup8Q/640?wx_fmt=png)

14.恶意脚本从网上下载gpg文件到指定目录，并通过gpg.exe程序解密下载的gpg文件，最后通过tar解压缩，执行恶意程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreGoQk5jrmIaf1vJrFUjF1MXvpeDTKYCbd36KWOiaZMp3BQKP5siczdHibg/640?wx_fmt=png)

15.解密解压缩之后，生成恶意程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreVvtpIt7tpLVfRlia94fzhRxagbzBMOrYiaNibGcX8ozhGzRpn4ibs0C7Lw/640?wx_fmt=png)

16.启动VBoxSVC.exe，利用白+黑技术加载同目录下的tedutil.dll恶意模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreia9jEZjiaojo3ErskmMGXUBKUAlYuef0zxRJFo4Zfpyh6ycQ8ot8NibKg/640?wx_fmt=png)

17.该恶意模块带有无效的微软数字签名，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLref1vyhCjeic9ZInvHTmomQZOd24nzNgehexPwzr47D1YuGlNFY518bUA/640?wx_fmt=png)

18.恶意模块读取tsunami.avi数据到分配的内存空间当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreUYJVm9OMe5J5PV4GvcjWdBzuHXKDpn3hNCCWIXlykfCDbAECrOTNJQ/640?wx_fmt=png)

19.拷贝相关的数据到分配的内存空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLre0NhpwzT9YLsAS3tUfTh5icqEqRPSBvyU9gc9IiaEFSOfiaGS84ibHrd2Ug/640?wx_fmt=png)

20.解密内存中的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLrepLYYqg2shpjNia3ianKtjEticPZib0avnxKYMgfDf9YP1YqzvTwugg2eRg/640?wx_fmt=png)

21.解压解密后的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreUcAbelnW0SKE0G7c53FD0zuCcljibHbIgauJVaqErnwhmcs5wApKqfg/640?wx_fmt=png)

22.解压解密之后的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreSlacV2Fa4NDDJ4babicTT6SWqDYzyemt7rLd200x2sH6IBKbdSZ5zpg/640?wx_fmt=png)

23.通过LoadLibrary加载系统pla.dll模块，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLre17KwSwXoicj1Ae7g0h04Kol08ibg67LLRGIVSBRzJmgYORrpyyY0WHBg/640?wx_fmt=png)

24.将pla.dll模块text区段的数据拷贝到分配的内存空间当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLre0T0NPO0TfCVSlVXsIuHvric9LIm6xB1PDB70dxJkAl29tLaw44vJoEA/640?wx_fmt=png)

25.修改pla.dll模块text区段的内存页面保护属性，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreKxFbj69Roe1uT7I5Q7DTlibPVLEDgCp1TOrbCI7BUcM5neTfmbbygibg/640?wx_fmt=png)

26.修改之后text区段的内存页面保护属性，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLre9CCqoI0q1ISOic4kfroawJEtBa9bHTujnlRXvpcJdUlw9griaML8jV7A/640?wx_fmt=png)

27.将恶意代码写入到pla.txt模块的text区段，替换text区段的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLrew2uWWXnAvNPB5NW7HJKia14nyKiaCPibYGUO4NBevNnTLrLTG102XxUAQ/640?wx_fmt=png)

28.还原pla.txt模块text区段的内存页面保护属性，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLre1zGaflwTAdKdkibYdNGN4bg70icgbLNyQMM1L0MovwUNWHJVyeHVZk4g/640?wx_fmt=png)

29.跳转到pla.txt模块text区段，执行被替换的恶意代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreo6ibYhD2ZetCvqqaJElQibo6FbjlZRrgOXbKPl7F3dSdpvWlbzrqR9ZA/640?wx_fmt=png)

30.恶意代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreic0fsJFIrvw1K8fkRRe2GGibOpn4Gfkq4PiaLzLv00VZcrd5w00O1w81w/640?wx_fmt=png)

31.加载指定的系统DLL模块，获取相关的函数地址，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreaNfstQvXr5VjBppPXkaIGfeVuGSbPXVHVeZyPVPLNrSbiba4qib0zT8A/640?wx_fmt=png)

32.判断恶意程序是否运行在64位操作系统，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLrewKfssOrNOdV8dMbYcDe6KA6qCZA6Oay0L12NDMOeiaTt8iaNPvpTnkyg/640?wx_fmt=png)

33.获取计算机名，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLrekywCAy0Fyv2EWzJrNNvWVekxbYomlPu9b5UeC3VfXAjQYxXAiahwGwQ/640?wx_fmt=png)

34.启动cmd.exe进程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLrejibWhXSMEVJDdzibKPYHVsnu5abPeshvP4MZXDo6tVwX3xHno0ia8ibRDw/640?wx_fmt=png)

35.在Temp目录下生成随机文件，并写入恶意数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreAeviaBhsdf68wTmZ3A4bibxIvjtephMKgc2KOlJ0MGs8tibK9QHqTt1kg/640?wx_fmt=png)

36.将恶意代码写入到进程当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLrewxsANSHIUftE3g3FCyA0oAd13mlApVzAS6f37LrJBqiafKmSUibBaBWg/640?wx_fmt=png)

37.覆盖pla.dll模块的text区段，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLreA0ticpQxw2xwFEf9vwic1Jhia1s1YW5W3iblQDfehFcAq8KJFKs3qia8zlA/640?wx_fmt=png)

38.启动远程进程线程，然后结束主进程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLre9zTS8hvxicwgSbgHicEpmva7mkcy69HeUicJDbM4Jdwic6VJMjqQNmUAKw/640?wx_fmt=png)

39.注入的恶意代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLrexU7U7edkeHRibEMapYsjFduWibWH1b7JGCxRvIV7zYPaHZOtkStIN96w/640?wx_fmt=png)

40.执行恶意代码，解密出窃密木马，与远程服务器通信，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLrenmz5JZazGdpoe9UicRxWBFibvBtoAmWWGtiaia9nwUP2abqhucoRvI9BOA/640?wx_fmt=png)

41.窃取主机相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLrefzdGnPibC443dUV9Bjea3owTbAw8ptVNslqUgUn5Txp1xpWawCzSUyQ/640?wx_fmt=png)

42.窃取到主机的信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmV2gFBgMiaUPMlCoP3U5ZLre...