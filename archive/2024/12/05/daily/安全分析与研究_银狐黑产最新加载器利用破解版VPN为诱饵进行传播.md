---
title: 银狐黑产最新加载器利用破解版VPN为诱饵进行传播
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247489624&idx=1&sn=d79b623b062721f4270af7e991894bf1&chksm=902fb770a7583e66a4bd81851a2174e33731d2b09a3ea198728983578ef6abb8634f72f86c4e&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-12-05
fetch_date: 2025-10-06T19:38:33.215406
---

# 银狐黑产最新加载器利用破解版VPN为诱饵进行传播

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANc2cWpRvCWcgqMD2ZstQibEO5nMh28NOrcjY4040NSIy9LroPN7PBMXw/0?wx_fmt=jpeg)

# 银狐黑产最新加载器利用破解版VPN为诱饵进行传播

原创

pandazhengzheng

安全分析与研究

**安全分析与研究**

专注于全球恶意软件的分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/16459

先知社区 作者：熊猫正正

近日，笔者捕获到一例银狐黑产组织使用VPN破解版安装程序作为诱饵传播最新的加载器后门，加载银狐黑产工具，对该攻击样本进行了详细分析，分享出来供大家参考学习。

详细分析

1.初始样本伪装成破解版VPN的MSI安装程序，相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9AN55KVpbLibe9f4OQPscTY2d5xyrvqspoGzwJtlMA7BrmUXdWLzuRQ8ew/640?wx_fmt=png)

2.解析MSI安装程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9AN4MglgAibpKZmzzYV6pfFGW6BvoeYibLmfjoubORuIqfFBPsx7pWCaPLQ/640?wx_fmt=png)

3.CustomAction安装脚本，调用AchieveAstuteTutorCSE安装脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANzob9JZzLT3z90L4elDfuI3xic0mibEfMb8mRX9QbOPsMIDMA5TmI9Muw/640?wx_fmt=png)

4.AchieveAstuteTutorCSE安装脚本，内容如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANrFjbfFaVfBLC3elY6wwbSl6NwDwosJbZJefSue3MWviaVqNjhwSYxicQ/640?wx_fmt=png)

5.初始化相关的文件名、调用参数以及解压密码等，使用了双层加密方式，逃避安全软件的查杀，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANCJb2jQXPMTbxHpqXjvBdfcxCQLJTjXjRxk5Dc8qIDBR2qoStfQvdXg/640?wx_fmt=png)

6.设置指定的排除文件目录扫描，对抗系统Windows Defender、360、金山毒霸等安全软件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANXOgPuhnk5Cf1m1JANWdXs46IUyK5mCDH8VPdTzd7NG6M3shwASrXgw/640?wx_fmt=png)

7.通过密码解压文件在相应的目录生成对应的恶意程序并启动，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANWsibGWz19sH2UU6y6eAibXSAATuFkoQs9Z4xXiaVlMUqJ4phJrU18FtCA/640?wx_fmt=png)

8.根据不同的环境启动执行相应的恶意程序，并结束安装程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9AN6zC2EELEv96e9e3BaOPXECpmcKK1aaj9f96JLHs2WUiaNmUNTMK59tQ/640?wx_fmt=png)

9.最终在指定目录下生成的恶意程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANicU7WYWXWgzSV21WZuQgD2H9DTX5zvVn4Uh6LbtfL69XGibicSZa5yCgg/640?wx_fmt=png)

10.相关的进程信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANCn4YTuYT1Yic1ibY7T4ZD3MUJpDXZDxMBPLNX6kdkRkib7CseGCbtv6Mw/640?wx_fmt=png)

11.恶意程序使用GO语言编写，符号表被抺掉了，恢复部分符号表之后，判断主机是否联网以及解析调用参数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANRhZZKKs26PYHVtVo8nWH1FQOWaWL83a2q2lm7sIgvibRHS9mhbgGDzA/640?wx_fmt=png)

12.分配相应的内存空间，然后解密shellcode代码拷贝到分配的内存当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANSWBb8aMJibSuhKdRCXpM15yG75fWc1gvTIMKypbvUmQ14TfscPKQiaWg/640?wx_fmt=png)

13.创建线程跳转执行到解密出来的ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANmPS5W75oQdWqeEQVONHgefzHJxjJeFr1YEupWib7VRYqXM87Nkxqb9g/640?wx_fmt=png)

14.ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANhrnRfcgUzLboTpHhGbNPfVWzq6iamFK62OXoXJDLyRpdia04IlfbAZSQ/640?wx_fmt=png)

15.分配相应的内存空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANWbuOcnic73DrcFlBOKgzxnwcFo51ZjEx9pWpnTOvY7RYvfMiaZ2c7wzw/640?wx_fmt=png)

16.解压缩ShellCode中的数据到分配的内存空间当中，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANA9TuBqpjwKWJtp3f1rQlv5SNaHNibEQYOTD7bd8oXIPaDLSvgDsX1fg/640?wx_fmt=png)

17.解压缩出来的PayLoad，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANcpyP9viafC06Fq2R9Pia1XfCibHTY6aWHibcyAQTOxgLd1YcJuTZjd16Ww/640?wx_fmt=png)

18.PayLoad的编译时间为2024年11月10日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANL09YgfQeN3FNkzIpeGgoOfq0gevQiaAE3uPFI4WU8iaQz5Vicib0tw88fQ/640?wx_fmt=png)

19.PayLoad导出函数fuckyou为银狐木马特征之一，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANWySRoUpsDY49hiayKKWzcAfHZNjqSfnqibZrtT7Tm0kMtLz7q8YeSlEg/640?wx_fmt=png)

20.分配相应的内存空间，将解密出来的PayLoad加载到内存空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANicGEfwpmw3kJ0zNLzcI5WHWsupsc3dHUFxfglFkXnXClua3fiaRCP0VA/640?wx_fmt=png)

21.拷贝完成之后，跳转执行到PayLoad的入口函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANBV8oqgakwib74yDc12lzcRsUdjuWUFibSMllREf96gX1BamlhUhDGeLQ/640?wx_fmt=png)

22.跟之前变种一样，初始化样本C2等信息，C2域名为fgfdg5631gfd.icu，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANn7JEkxOX4z5tm9GSHld4ZzphcS78VJBzruLSDOOPOVVEQblvDaO8fg/640?wx_fmt=png)

23.黑客远程服务器IP地址为103.183.3.107，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANpC3yiabp9KmWPFnl6ndr7Evtl7qaXgTdcoddJB47yeshZZT79ra2LWQ/640?wx_fmt=png)

24.从远程服务器gdfg4564fdg.cyou下读取相关数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANVZ08jgoZEFWwwHvjbCaabiax863eKSbN0wEYiaheEiaVYZr72gAYAibMUw/640?wx_fmt=png)

25.解密返回的数据，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANCsgjiaVLREJgYiaBGOcxQMH04KzcSj0KNQou7sg0UmbA2DT4lMuYrxibA/640?wx_fmt=png)

26.通过威胁情报平台查询相关域名信息，已经标记为银狐木马，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANK3ZvDm0IMicV3k5vfF3bWeJwtXFias038YqhhlCiaMJ02HzEYJRk5NTxQ/640?wx_fmt=png)

解密出来的PayLoad与此前发现的银狐变种，基本一致就不重复分析了，可能参考之前的文章。

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVE7L7UNE8RmV9AW1ERe9ANrxw27npdsv5EammwEFTOnQLTQC1ulDvicO7lWfcmqY2YBib5ClLgziaeA/640?wx_fmt=png)

总结结尾

去年使用“银狐”黑客远控工具的几个黑产团伙非常活跃，今年这些黑产团伙仍然非常活跃，而且仍然在不断的更新自己的攻击样本，采用各种免杀方式，逃避安全厂商的检测，免杀对抗手法一直在升级。

安全分析与研究，专注于全球恶意软件的分析与研究，深度追踪全球黑客组织攻击活动，欢迎大家关注，获取全球最新的黑客组织攻击事件威胁情报。

![](https://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmXqn09tuVnIKmG2h1IZy4ibk6hVMvHYezFhWYC5MibyuYZbfsxClqTzfrPCSWbfLeOYdNNpDI1tzOXw/640?wx_fmt=jpeg)

王正

笔名：熊猫正正

恶意软件研究员

长期专注于全球恶意软件的分析与研究，深度追踪全球黑客组织的攻击活动，擅长各种恶意软件逆向分析技术，具有丰富的样本分析实战经验，对勒索病毒、挖矿病毒、窃密、远控木马、银行木马、僵尸网络、高端APT样本都有深入的分析与研究

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

安全分析与研究

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS82DY7CjsBUmiaAl7BQ/0?wx_fmt=png)

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