---
title: 守护解放西？银狐病毒？
url: https://mp.weixin.qq.com/s?__biz=MzUzODU3ODA0MA==&mid=2247489749&idx=1&sn=0d20a76e54c4150e5d555e6d046900a1&chksm=fad4c5c2cda34cd4da66062f886bc4e5d68fa00d9185f23663b893fde4b33c251a4bde238479&scene=58&subscene=0#rd
source: NOVASEC
date: 2024-11-26
fetch_date: 2025-10-06T19:20:28.573595
---

# 守护解放西？银狐病毒？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8WH2Zo4jHwjlKXJlLrNRic1ia2tOVIVjV0Z1L3mF5zA6zuqnO671DL5wYoGeiaUzr6DSQACT6RmKKxkelYdt4VOcQ/0?wx_fmt=jpeg)

# 守护解放西？银狐病毒？

爱做梦的大米饭

NOVASEC

# 守护解放西？银狐病毒？

## 前言

“整个长沙！我是老大！”

相信很多人都看过守护解放西这个纪录片，作为一个网安人员，吃瓜必定会吃的，但是看着新一期的守护解放西的第一集，发现了一个熟悉的朋友---银狐病毒。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwjlKXJlLrNRic1ia2tOVIVjV0XoDmiaQWwMzKicwIKfefR4L9KPIIhY9xiakLr17rwPAgvXD449f6sXNDQ/640?wx_fmt=png&from=appmsg)

## 失陷原因以及现象

银狐病毒往往伴随着钓鱼攻击的实施，常见的钓鱼方式：伪造正常软件首页网站欺骗用户下载、IM即时通讯软件传播、邮件钓鱼等等。

那么常常面临的现象则是：个人没有操作电脑，鼠标却在动；没有操作电脑，但是拉了一堆莫名其妙的群，并且不自知的发送了一堆乱七八糟的信息。以及杀毒软件或者是EDR产生告警，主机执行可疑命令等等。

## 分析处置

### 工具

进程网络查看工具：Processhacker(无EDR场景)、systeminfomer(有EDR场景)。两个工具的功能都是相同的，但是在edr环境下Processhacker和火绒剑这类安全分析工具会被拦截，不准使用，建议使用systeminfomer去分析网络行为和进程行为。

日志监控：sysmon

文件查看工具：Everything

维权/自启动查看：autorun

### 分析基础知识

面对各类病毒类的事件，个人比较喜欢从以下几个步骤展开相关工作。

1、查看主机网络情况，像各类病毒在活动过程中，会存在网络连接的行为，如果在设备中抓到外连的地址，可以通过直接检索外连地址，就能够快速定位到是哪个进程正在外连。如下图所示，能够很明确的看到每个进程对应的pid，外连地址，以及通讯状态，并且是实时更新的，这样更加方便我们展开安全分析的相关工作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwjlKXJlLrNRic1ia2tOVIVjV0DTgdjB4NFUD376FQeGw25CRias3LAMMzuibTJPVb3XGZmYVqQjQsaYDQ/640?wx_fmt=png&from=appmsg)

2、通过网络定位到了进程pid，那么我们就能够查看该进程的具体详细信息。以todesk为例，那么我们能够看到这个进程的可执行文件的路径，执行的父进程以及进程启动的时间，如果启动，是以services.exe启动的，那么基本上使用autorunrun就能够查看到相关可执行文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwjlKXJlLrNRic1ia2tOVIVjV0gnzv2tUDF8aGHpvIDmjRDWTBfsHkF0aStW1JdJ9ZXDYSYzTWnyGt9w/640?wx_fmt=png&from=appmsg)

3、使用autorun进行检索，基本上就能够看到和autorun相关的自启动信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwjlKXJlLrNRic1ia2tOVIVjV0IRt5lSntqQux4VhwbMg4siadHkD32AbjUIPNcOiaWnIGWlJs1DOZCbwg/640?wx_fmt=png&from=appmsg)

那么在实际处置过程中，我们就倒着来就行了。先删除启动项，然后再去终止进程，最后删除文件，重启即可。

## 银狐实战案例

这里在用户终端发现到存在svchost恶意的外连信息，svchost为系统进程，但是存在主动外连的场景，那么这个进程可能是恶意程序拉起来的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwjlKXJlLrNRic1ia2tOVIVjV0D79NRvIN1sLB1nX1osgc1cv4mcKwuIJj39nfJxh7TPZvDXgNgjl9xA/640?wx_fmt=png&from=appmsg)

那么这个时候去根据父进程相关的信息分析，大概率是分析不出来的，因为他的父进程我们只知道他的pid不知道具体的可执行文件是什么，那么这个时候就可以安装sysmon去进行监控整体的行为。重启后查行为，就能快速找到拉起svchost的父进程了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwjlKXJlLrNRic1ia2tOVIVjV0PLb0kcyXqdfj4Vp4zsdicTAiaYLRF8PBRxvpp01zE9JqwUY6Ua5VoCdg/640?wx_fmt=png&from=appmsg)

那么这个进程本身就是个白进程，那么推断攻击者利用白加黑来实现免杀规避的操作。那么可以分析这个可执行文件导入表，来看导入了哪些可疑的dll文件。常见的可以使用pe工具去查看，比如peview，或者是利用威胁情报平台去查看。这里快速查看该文件导入表情况，那么KERNEL32.dll为系统文件，没什么好质疑的，主要是lun\_sdk32.dll文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwjlKXJlLrNRic1ia2tOVIVjV0IELC857qRIZkUibNM939oUn1K51UxwIYv993Xh3Oib2qH6BxPOgW6Png/640?wx_fmt=png&from=appmsg)

全局检索该dll文件，发现该dll文件签名无效，按照正常的软件，一个dll如果有签名，肯定是有效的，那么这个文件肯定是使用工具进行了签名窃取。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwjlKXJlLrNRic1ia2tOVIVjV0Thiaic5DzY9cnYwbmY4p2TnSiblWx75ZNCic2zFIiamxuwglLHI99odwA0Q/640?wx_fmt=png&from=appmsg)

那么整体的分析基本就到这里。知道是什么原因实现的，那么删除恶意的dll文件，以及其可执行文件对应的启动项，基本就能够解决主机被远控的问题了。

## 总结

银狐病毒类的排查，和常规病毒排查基本没什么区别，主要是变种较快，排查过程中，合理使用常见应急工具，分析进程是什么拉起来的，那么就能够快速定位出恶意的程序。

## 工具包

个人总结了实际应急响应场景实用的工具(不会打包过多冗余工具)，并打包放到微信公众号，感兴趣的可以关注回复【20241122】领取

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8WH2Zo4jHwjlKXJlLrNRic1ia2tOVIVjV0c1ofOHvvl4bYKn2sicwKYNKu335aMZgUdOITHr1kU0sSP6Tc4aadv6w/640?wx_fmt=png&from=appmsg)

预览时标签不可点

内容剧情演绎，仅供娱乐

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

NOVASEC

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/toroKEibicmZC7QAYyWHtDoIWgIKkJS0UgnH5iaGXoLOOdzBkAAoI6Zxn82xT9GSrxFNKd2zF0aEkDYnmofMib5AzQ/0?wx_fmt=png)

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