---
title: 一键 Kill 火绒？加了星球只给工具不给代码怎么办？
url: https://mp.weixin.qq.com/s/U4ar7repiKbJ660SJAB9GA
source: Doonsec's feed
date: 2026-04-12
fetch_date: 2026-04-13T04:53:28.367610
---

# 一键 Kill 火绒？加了星球只给工具不给代码怎么办？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1pic87O41XF4lcdv0jroxsVWxOaK5LbTdgjnBcDqqejgKk4OHwMwOmNUgFia3Fia632Tyicc6C4ibBpx6CAguWyRHOyjFLlOOW8fvzWAbibJ0eNqQ/0?wx_fmt=jpeg)

# 一键 Kill 火绒？加了星球只给工具不给代码怎么办？

原创

Re
Re

蜂鸟安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/1pic87O41XF4JrK4ZDqDS0aAXYf5YHC3bicaR63lWO4spMUYj7ftdZFOMbZV3d0jCIZrBI9FHYTcpUWMpbYBKyD7LXkgxAynE9eeib1KapEU7g/640?wx_fmt=gif&from=appmsg)

点击上方蓝字·关注蜂鸟安全

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF6qoVSN6hNAUW7KGDqVXGibcAeGB6JgLfpreEKLkzGUOBTvHibyQ3icI5e7t8AiaWvs9aUzpwibOgdYWxtRE1IsqyD3bHbM5afnvhng/640?wx_fmt=png&from=appmsg)

**01、免责声明**

**本文所涉及的技术、思路和工具仅用于安全测试和防御研究，严禁将其用于非法入侵或其它攻击他人系统以及盈利等目的，一切后果由操作者自行承担。**

**02、目录**

* 前言
* 工具逆向
* 驱动逆向

**03、前言**

很多师傅在加入一些知识星球拿到像一键 kill 火绒这类工具的时候想知道工具是怎么写的但是别人又不愿意公开工具代码怎么办。当然是逆向啦，这种工具是最好分析的。

kill 杀软的方式有 3 环 kill 的也有 0 环 kill 的，但是绝大部分都是利用签名的驱动漏洞在 0 环 kill 的，3 环 kill 的话其实也是利用用户层上一些高权限进程上的漏洞来实现的，这类是比较少的。漏洞驱动有个专业的名词叫做 **BYOVD**。因为这类驱动自带合法签名，它可以绕过强制驱动签名等安全机制，直接进入内核空间，由于访问控制不当导致攻击者可以直接利用它们。

**BYOVD 又分为多种类型**

* **强杀进程型 BYOVD**，通常用来结束杀毒软件；
* **任意****内存****读写型 BYOVD**，通常用来进行提权操作，比如替换进程的 Token 为 System Token 从而实现提权，微软的 AFD.sys 就爆出过好几个这种提权洞；
* **强制卸载型 BYOVD**，......
* 当然了远不止我上面说的这三种，感兴趣的师傅可以自行了解

这篇文章就以一款工具为例，从逆向分析工具到获取驱动，再对驱动进行逆向然后自己写工具！！！

文章并不会泄露工具和驱动相关的敏感信息，只提供一个思路，师傅们不用私下找我要！！！

**04、工具逆向**

老规矩，拿到工具第一眼先分析有无壳，有壳的话进行脱壳。不要怕不好脱，这种工具本身就是为了方便用的，谁给你上强壳啊。

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF7erPibTvskL2WjTq1CEZwqW5ib0zpfW4OTXPxtEFBtWcOFyITgarCCZeLSgpRWCcibZWrfrK6Mt6icZMwggZZrotslriaNkHeciaGtQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pic87O41XF6jTka4Rm8BicKfozECaziaDEiaCtfZyibtUAsFDTS8aVFn9wvqwrKWGDSGobqFRA2gGdWicljw8r2cp416mJ52fDIvajzq8iakNry6k/640?wx_fmt=png&from=appmsg)

一般情况下，和驱动通信需要用到驱动命名空间的前缀，通常是 **\\.\xxx**，但是写到代码中需要转义处理，所以通常会硬编码写成：**\\\\.\\xxx**，直接字符串搜索前缀就好了。

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF5Isujia0pDkickK0wWR1CGJtVMGPUCibMP2aADKvuBuz6VCKl51DjUNAl6AiaqHfB6mNq5C7OtIymn6vAgDZQtsqsF7lAHjzdrhC8/640?wx_fmt=png&from=appmsg)

通过这种方法可以快速定位到工具核心的代码位置，接着就可以分析代码逻辑了。

如下图所示，先创建进程快照，通过进程名获取目标进程 PID，通过代码不难看出进程名为 HipsDeamon，这正是火绒的一个核心组件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pic87O41XF4Fsice1DHdRzK7Iia2kMibYfFUNwW9s03ibB0GSx5BIDHA8HI4l7B1BxonwLPhlfuEgt8ticSRiaibM2wHAjiaRjKdlCvyZbhNicKIHF7o/640?wx_fmt=png&from=appmsg)

接着获取程序自身 pid，判断是否以管理员权限运行，如果是则释放资源，这个就是释放驱动的地方，也就是说这个程序在运行过程中会把漏洞驱动释放在同目录下。

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF47YQyMeVTwrbfEJB3CcrNXibLATDcSJu18BdAo5nuE2EWdT1W9xDlz4KDMmLSzCSG1Uz52KMvpKAAcEHGnG09QxpTGiassPu7bQ/640?wx_fmt=png&from=appmsg)

如下图所示

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pic87O41XF5a2BhCyicVia1FB1CibcibZPElTEqcxMcOj0nRGaeNra89C0eAQ6wOsQ60H4f6Mccq5WGeVzou8tOX3cII3v2twgjvmYlzmrxS0sU/640?wx_fmt=png&from=appmsg)

接着就是加载驱动和对驱动的利用了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pic87O41XF5oTyicp4GzWKasVpzgiaDjD4CF5ckvGwYxPzmKA9gJtIbtGm2RkamtDwqicoUdqoooLksDvjjZtSWZPs9Wov601409xSLF9EG7xA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF5mdFicTlKsNPFoHv7dROOicZ7LXMtqeR77k7ibWddXgc3sh7xcmXwGibq6aA5vhdox8QB8WdHyFicVQIIU5iabPAmoHyhELsqomqeibo/640?wx_fmt=png&from=appmsg)

在程序执行完成后会调用 DeleteFileW 删除释放的驱动文件

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF61IcozrG0DmSico0t31WV9PMTKgia23udRYM5egasdBZPMkqrI3Of71V7YaKoqwqfEccqt8bE3yzoHoIvvQNzGA25diaqAuUicic48/640?wx_fmt=png&from=appmsg)

到此整个工具的核心流程就分析完了，漏洞驱动也拿到了，接着就可以逆向分析驱动然后自己写代码。

**05、驱动逆向**

既然是用来结束任意进程的，那么大概率是用 **ZwTerminateProcess**函数，如下图所示定位到函数位置

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF5ac1z7XJ2cRuPxbS04FwQoiaib5L7ULmQOTB6RquCia0qiawjzrXYQCNQupSffDlr2J6Qz4xCU5uBuYjJKByuibZULefSdfHzcT1m4/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF4xmZdjTXu1B5kJicmF4H4OtuLZaK20aCRfibq6eXwnewM0vpT4K7LKKeo8aMBWNaLGBtyNgg4BgWF0h5sHzSvFzEyCGWicJibPht0/640?wx_fmt=png&from=appmsg)

交叉引用查看谁调用了这个函数，如下图所示有两个函数调用了 killprocess

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pic87O41XF5UHBsmvQ9jhLE8qk3wFfm6w1Pic8U9JmE3J3ibFCbYQEomiacNaibBNT67eNqxGia4h7GnQXVQOEoeCicw1CChIwU3PvnMvAE6Q2vHc/640?wx_fmt=png&from=appmsg)

需要找到存在 IOCTL 控制码的调用位置，sub\_1400104E8 调用了 killprocess，可以看到传进去两个参数都是 DWORD 类型的，上面已经分析过了，a1 里面是包含要 kill 的进程 PID 的，通过这里可知在构造数据缓冲区的时候需要有两个 DWORD 类型的成员，后续会讲到，接着交叉引用查找。

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF4Ay1rxciaKY2HTyqzR3KlrrguabIjEuJCdPgC4fJzrv4CStvK3lcehOTRObSyL5tMbicrtcjxDjM1qKtzbiab96XVRhFQjUWia2T8/640?wx_fmt=png&from=appmsg)

如下图所示就定位到了，IOCTL 控制码是 0x80002048

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF5tGKKtx2ciaVxAEyxicMltcGjzic5PzMS4oO2GnmBYeSHdlQyOt1JUFFpl5cic1WXlDtiaGv8mgE07avC8x2DXWVpUKYaHuDvzvpRI/640?wx_fmt=png&from=appmsg)

但是一般都是会有调用条件的，还需要往上翻看代码，看看需要什么条件

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF69MGeaRvt0abJAc0H1Y4jjw9BNpr0icFiafL1htiaLFC8x4kSDMLu19jLpgKaoFII9Z8aXAmlomFCl6aQ1RKicTzibdAp4bcpMIdCc/640?wx_fmt=png&from=appmsg)

**分析一下上图代码的意思：**

**1.**首先调用 PsGetCurrentProcessId 函数获取和这个驱动通信的进程的 PID 存储在 v6 中；

**2.**CurrentStackLocation 存储用户请求信息，其中就包括了用户传给驱动的 IOCTL 码，用户控制驱动执行哪部分分支；取出的 IOCTL 控制码存储在 v9 中；

**3.**接着判断 v9 的值是否等于 0x80002010 (-2147475440 十六进制表示正是 0x80002010)；

**4.**如果 v9 不等于 0x80002010，就进行权限验证，看看 PID 是否注册在白名单内，如果不在就无权发送 IOCTL 码。

说明要通过 IOCTL 控制码 0x80002048 调用 killprocess 需要有权限。但是 “**判断 v9 的值是否等于 0x80002010**” 经过分析 0x80002010 控制码对应的代码如下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pic87O41XF7FI0yniaUSyvEATSib3svbqicbCoFEs8AIrtBvCMicticRzCohE2Zdb3tUCiccmeqb9ammFyqZia9J2xMk4QUy2cvLicp35qKbDyDl6OI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1pic87O41XF6uS7Tguwe1wvYqx1iaYkYnNAnlu0aZ3n6zPTtvU8INAnKLy04xWcqSOJmGmBt1EIb3Z5szIgbqbqic0MzrlmBicEAwXnsYRERoia0/640?wx_fmt=png&from=appmsg)

这个分支是用来将 PID 注册进白名单的，并且不会进行权限校验，所以在利用这个驱动的时候，先传入 0x80002010 控制，将自身进程 PID 传入并注册进白名单，传入 0x80002048 控制码去 killprocess。

这部分分析完了，接着要继续找设备名和符号链接了，如下图所示，其中 sub\_140010518 是派遣函数，内部就是上面分析的根据 IOCTL 控制码执行不同分支。

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF5BLEtFicSSiaOdOkddY7gc2atgNHtCe5W4nPhicbXBqaIbWzDo2lq4F0ibWWhCRpIjic6RpWTGdPgDVXX3M8fzWBDt8lKRAQniccYTM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF7JiaeRsUlJp9rSrxCbkrZvv9n4HzTrLayrbicmAtBQ3uDkHf2tQA1lRuSXVqLcGJE4KmHiaB7aeABLmuaXppBUhm7lFoiaquLcVicA/640?wx_fmt=png&from=appmsg)

都分析完成后就可以写代码了

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF44AeWoNLx6TS9etIUhZg70SAJkyzH8oToO5AR6vmWf45v0icSMyBrXQaGicudS6EqFSoicjtzhnWNH920hIk9icODUWsUc1RBictZA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF46qFJNoEialSpsMS0Rg3XMzSQXYHic58sVtmxl1iaXNic458ohQ5kbEmDicwf2LDVVkX8OyWR7Lx2FmOicnKpF743YXLALBeuSEvGNM/640?wx_fmt=png&from=appmsg)

当然了这里只是演示，代码肯定没有像原工具那样比较自动化，这种写法还需要我们手动启动驱动服务

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF7No7v7snDm4913RkQePUDEYlxAUh9mbZldlTLuia3fm1CvOdgxeeTo38rAqtRhokIdVgPgbT9Tvvz3HObVvOErhJK38X4Mzy0k/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF48wVBmxV1fy1m9BEib5vC3ePUYXj0dPgq1Sdbw0ugAyF9lZwcmCovTGyTDFnP2nBltticticZNxIreCgMlu7CEQjHjnOUWDO68ia4/640?wx_fmt=png&from=appmsg)

运行程序，如下图所示，成功 kill 火绒

![](https://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF5jicTiaAzJtJzQ4B7qEy8TZkSEgqxsBnVic54Bj6HaKgoDyUvOVbiaoroWibibS5k1to8cUibibs7gp60mAly3Sv7XL6GCxazo4mtxfdM/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF5hibT9k3ZXbGFIv5Ohd0XldhdaXHQ8v6fZian4ZxdPHdfiaI3eqDpWOHdb8LJbADZLn0DicliacTfD5ibf9EbaQtXrWHE5byhXIjwwQ/0?wx_fmt=png)

蜂鸟安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1pic87O41XF5hibT9k3ZXbGFIv5Ohd0XldhdaXHQ8v6fZian4ZxdPHdfiaI3eqDpWOHdb8LJbADZLn0DicliacTfD5ibf9EbaQtXrWHE5byhXIjwwQ/0?wx_fmt=png)

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