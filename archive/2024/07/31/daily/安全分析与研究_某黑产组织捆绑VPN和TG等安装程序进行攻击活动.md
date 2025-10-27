---
title: 某黑产组织捆绑VPN和TG等安装程序进行攻击活动
url: https://mp.weixin.qq.com/s?__biz=MzA4ODEyODA3MQ==&mid=2247488634&idx=1&sn=5c75e774865edb85496adbb901ebc095&chksm=902fbb52a758324407816b468e54ba700a0366696f347a4fb14a8c5cdc2878a0e80911e522b9&scene=58&subscene=0#rd
source: 安全分析与研究
date: 2024-07-31
fetch_date: 2025-10-06T17:43:58.167049
---

# 某黑产组织捆绑VPN和TG等安装程序进行攻击活动

![cover_image](http://mmbiz.qpic.cn/mmbiz_jpg/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGCZYOWLLcdodIW7IzU7MPznzLviaU4iaRXvBH9eiaqpSqMUrjkoMIO0yBQ/0?wx_fmt=jpeg)

# 某黑产组织捆绑VPN和TG等安装程序进行攻击活动

原创

pandazhengzheng

安全分析与研究

前言概述

原文首发出处：

https://xz.aliyun.com/t/15082

先知社区 作者：熊猫正正

近日笔者在某社交论坛上发现一例黑产组织捆绑LetsVPN、TG等安装程序进行攻击活动的最新攻击样本，该样本里面中使用了一些比较有趣的对抗技巧，笔者对该攻击样本进行了详细分析，分享出来供大家参考学习。

详细分析

1.初始样本为一个MSI安装程序，里面捆绑了LetsVPN安装程序，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGlPMvxIMpoJRibhQhJNFlpq24vHWic7NaQAegZYticSujZUl1ianzoGu9eQ/640?wx_fmt=png)

2.查看MSI安装脚本，里面的字符串是逆序的再通过StrReverse恢复，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGdNYdtOZgH78xbrWD7VkUuPgAffFV5XibRiba73Q4FLPwJzl49ck41Bow/640?wx_fmt=png)

3.笔者先手动把这些字符串还原，方便后面分析，安装脚本先检测操作系统信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGlv2CzA9iaTN12yNGKP83ZJgmnn0YXib6Cn6Yiavs5v7udo25dVyibCtGlw/640?wx_fmt=png)

4.解压缩MSI安装包中的vs.zip到指定目录，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rG8DLAX0Aibrs6TUnWCLWyia0d7dwC0aZPs9U403WGGicfl3IWUphn5wHOw/640?wx_fmt=png)

5.vs.zip解压缩之后，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGkYdOUqKuKsibsiaEmklKBY7MxhicEhCOWf7Anm1DWdFGia3xvo9Uaics0aw/640?wx_fmt=png)

6.Python文件夹内容，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGEwCD4bQMzAnTxqdKHghTxIV9YN4xfXp4qibNqjvdBqsQ4RRf9AGhwlA/640?wx_fmt=png)

7.判断操作系统版本、360相关进程以及自启动注册表项等，然后调用python38.jpg脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGPNt99O42icXkkW9yM96JeSpIEkZOA9em5jb7icFwuKlRzKSNHe5DAtAA/640?wx_fmt=png)

8.python38.jpg脚本解密pb.txt，然后通过解密后的程序解压缩lnk.zip到系统启动目录，最后再删除相关的文件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGaicCIwSnRV8yXYEboRb9kDIfIwKv80gq1tplDGoUfWAsib7641oTe9Vg/640?wx_fmt=png)

9.解压缩lnk.zip之后，在系统启动目录下生成两个快捷方式，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGHx2Na3tdbgdgZ77sjZYSaRQ3GZa5Xv2acIQiaHF7fSyDd1xv8qCsuQw/640?wx_fmt=png)

10.rar快捷方式命令行相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGCFNicCDZYYacGm3UXCKAbiaRGYIBFMUVjde3Oybz4bteSRTK2bmfwakA/640?wx_fmt=png)

11.sogou快捷方式命令行相关信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGz6oA9z6vsrwAvS3aqE4Bp6Id8Vkics9UrjCr0GxGCtMEazUlgf5vTpw/640?wx_fmt=png)

12.最后调用python39.jpg恶意脚本，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGN8Z4hZzVvKzFHTFpuyXk4ys6FTWCdQvQ9AeaPv4QB3k1zibaSkjKKfw/640?wx_fmt=png)

13.python39.jpg脚本读取指定目录下的templateWatch.dat文件，解密该文件获得ShellCode代码之后，加载到内存中执行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGKQFDMsXe84vMiaodegXkCYTtt5ic4ZiaEEffrwPe9ftJjibzcNpNpfiaIbQ/640?wx_fmt=png)

14.解密后的ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGUTCedNJzMq6KIxouD1dbXCo62v2NqQyZj7LIoREm9aJjKZaD0oR38w/640?wx_fmt=png)

15.动态调试解密出来的ShellCode代码，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGWRSWmnprz7ickEqYel42DRm5CiaxqB5KElYgiciaeo7AbxTUgg9MnFegEQ/640?wx_fmt=png)

16.加载DLL模块，获取相关函数地址，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rG2ZgMreGGInYGLnibNM1BL0X4icOYX9Eicwy55Lco0PGobjf9vwxroEiaibw/640?wx_fmt=png)

17.通过VirtualAlloc函数分配内存空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGjsFDnk7cdd0G28q02uUmwbNiaETTyYRCDMq2gdcvuFwR3VS8hgwhkmA/640?wx_fmt=png)

18.将ShellCode中包含的PayLoad程序拷贝到分配的内存空间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGZSp4KBN7GJibJfmMPmRDVwaic3WbKCIDN5MbwR5PFejIMQH4GbGtiaibibg/640?wx_fmt=png)

19.PayLoad程序的编译时间为2024年7月16日，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rG3rmib1pHft57VE6lJlL1VYB6GRPQoxN5HuokhLoBfxo4n1RuDicX5nVg/640?wx_fmt=png)

20.设置PayLoad代码段属性，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGicvGI0z9iavhXMZ4j57LQoY3tGo6KjYsS7USq2DmKajA37AIbYl6xfWA/640?wx_fmt=png)

21.调用执行PayLoad程序的入口函数，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGyUeAwM6wVuZHBVUKpqfTLPU8WTiccG6z7swJeOiaTSH185Qnd3gf00TA/640?wx_fmt=png)

22.获取指定目录下文件的属性，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGPsCtjVFPu33g9gt0GybM4xGRmE8LH73xDpUXVpRPKMaB24Q291V4Mg/640?wx_fmt=png)

23.获取时间间隔鼠标的位置信息，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rG1ICDXw0BOlHkKrZH7PX6LZuicMdHphKziblg1oc7icnclySz642iaBjBRw/640?wx_fmt=png)

24.获取系统MAC地址，并判断是否包含指定的值，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGGiarLdCp7nqbrsKu7UmaUBiaZzTEwZoZs0x3NGlZ0jDRagJuLfsoSqIg/640?wx_fmt=png)

25.判断VMTools文件目录是否存在，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGFejlOMl9iaQ5sUiaSMqH9ziciczEUT1nqMxACrSczDVFQQdVzJBUlZlmGA/640?wx_fmt=png)

26.通过上面的方法进行反虚拟机操作，然后创建互斥变量uacme2023-09-19，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGlTx49zrIzRddpCcVpicUibFN433Xxe6aohe1PHNkqJwxTdgg6Yoo3NhA/640?wx_fmt=png)

27.判断当前进程是否为管理员权限，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGrtk9b2DMDh2IV8wR9dPhXC5s2qPCOCfOpyb4f9LdliaUQg908LrA7Fg/640?wx_fmt=png)

28.判断是否存在kxetray.exe和360tray.exe安全软件进程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGtib9OK5Tvwoy3bLdgaKeIjujtoLAz270dSS0XabafZQjnIDEN0aOa3g/640?wx_fmt=png)

29.获取主机名，然后查询指定注册表项，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGyvcYvn5bxvhqpK9OqLydia1z8mia0gqwib5w9TZKRia50ibBKTVtk0XDj3A/640?wx_fmt=png)

30.获取主机时间，设置注册表项记录主机感染时间，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGWyI0a2elSxUlecwUJqaumVFPCXJX28Xv3XhGsrZJBeyEQ4icRBfllxA/640?wx_fmt=png)

31.与远程服务器ul.mxbc110.com进行通信，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGHR7QyeG8sThJwvo9glQdDUMI7UV0iamdUSyoicicVLEVv6wjnHict8piagw/640?wx_fmt=png)

32.查看PayLoad导出函数，还包含一些自动安装功能以及对抗安全软件功能，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGHAnF6BJHzW6lPto6n3k6lXDibTfMUibtz5gmKOdu47OnqmlzBKSZnyCQ/640?wx_fmt=png)

33.对抗安全软件，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGEZ9icQLnfDgrh9SK6jojhAia4IBI503AmwF11erfMWxic0hrOOSRTz8icA/640?wx_fmt=png)

34.通过服务安装，先读取加密的ShellCode数据，并将加密的ShellCode数据设置为注册表项值，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGFM4QEWmqz57yibLU6z4RZ0tiaUwXCOj3U138icltTvW8UH18Ut4nZA2yw/640?wx_fmt=png)

35.然后读取加密的ShellCode注册表项值，并启动相关进程，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGKofLRdGOiaOT6YKpruH9aWQiciaAMVsIdEnyzFrnFHPGaBcTfSMRVBSew/640?wx_fmt=png)

36.然后将解密的ShellCode代码注入到进程中，远程调用执行，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGlic4RTE1QLnicfB8oHCSQSe0W26iaAKghTKgOb8vb2olazvDttdKJHn2g/640?wx_fmt=png)

37.通过系统自启动安装，设置相应的注册表项，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGzB48FnaibBic1JkZFppxbExH5niaADiaHhobDfQtgmYPOF94VbQs8rZEGg/640?wx_fmt=png)

38.遍历安全软件进程，如果不是管理员权限，进行提权操作，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGEHmgianQdgBvX1Y5sIzLIySUibL8ytVmMCc5pJfk44Te5DmqozeKPvTg/640?wx_fmt=png)

39.通过计划任务安装，设置相关的计划任务自启动项，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGsJ3vQcicSTzRWtFGQb73aebwc7HXOk1XIbplrnaTWKu1PldCLHxNgrw/640?wx_fmt=png)

40.设置自启动安装，如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGdQKyib1obqPicv969jeS7H89iavE6838DZYMCn048sdVbo22nPzehaZvA/640?wx_fmt=png)

威胁情报

![](https://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmWyW6NRsyGVNlDibZmXlY3rGoWKYT3j6BYQicLkHROvkbmBp5Xx2eP673Bib202XQ3719hVsOIeC3Csg/640?wx_fmt=png)

总结结尾

去年使用“银狐”黑客远控工具的黑产团伙非常活跃，今年这些黑产团伙仍然非常活跃，而且仍然在不断的更新自己的攻击样本，采用各种免杀方式，逃避安全厂商的检测，免杀对抗手法一直在升级。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oibWJqH5OVmVcFgYKtoVnKR7h3pkl3AyxwS0l7iagicAJnYjEQhwIuZgR3RR65DLpJh2TGZS8...