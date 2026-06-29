---
title: 【域渗透】主机权限提升
url: https://mp.weixin.qq.com/s/sulIBhuZfaNPxAVhhB-5uQ
source: Doonsec's feed
date: 2026-06-28
fetch_date: 2026-06-29T06:32:26.404273
---

# 【域渗透】主机权限提升

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/kibYIhwqxpuib4iay6Dic09AoVEkhgdmHWHjia4odic7iaViabibZyg3OtaxBfonA3Pj9RDuN442qNqmWJu7oaFJ7H7VRmNu2jFkYLteCH9ia7sIoWxVI/0?wx_fmt=jpeg)

# 【域攻防】主机权限提升

原创

平凡在修行
平凡在修行

平凡在修行

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**「一世为人不易，别浪费在这里了」**

# **「免责声明」**

本公众号分享的所有文章仅用于信息防御技术研究，切勿用于其他用途。由于传播或利用此文所提供的信息、技术或方法而造成的任何直接或间接的后果及损失，均由使用者本人负责， 文章作者不为此承担任何责任。

# **「溢出漏洞提权」**

## **「MS16-032」****「提权」**

通过 **「MS16-032」** 漏洞可以以⼀个普通⽤户的身份，去添加⼀个administrator管理员组**「的⽤户，还可以以」**SYSEM 系统权限的身份去运⾏⼀个程序。

该漏洞前提：**「⽬标系统需要有2」**个以上的CPU核⼼，并且PowerShell**「是」** v2.0及更⾼版本。此漏洞会影响以下Microsoft产品：

* Windows Vista

* Windows 7
* Windows 8.1
* Windows 10
* Windows 2008 Server
* Windows 2012 Server

测试机器为 Windows 10，接下来就是整个提权过程。

⾸先需要去下载 ps1 ⽂件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kibYIhwqxpu9QbFyXJFHXoQqfHy1ya4KZh94o5ic2yibeo8U9UjPAcV1VRH2oA5tOVUl5XRq5xdHPX13LbZfe2XAlXNEWfic8Dyn3OTViaQibSFQo/640?wx_fmt=png&from=appmsg)

web1-2012机器

本地管理员账户

普通用户账户

⾸先有⼀个本地普通⽤户hackerone

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kibYIhwqxpu8vofGSMPW79OMtTypvMWNGSIyiaJox9jFVky8DuDZHYXcJX3LPnhFryUr93poAVyIy8xUpgp4Ng415UCMmbxp8Zq0E0l2jnQiac/640?wx_fmt=png&from=appmsg)

普通⽤户创建⽤户失败：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kibYIhwqxpuibWFiaIucXyjxYVY2K0ibk0aXZFTEIXdDSgSmqGD67U3VdlPicXr67154kIMiaTm0icicOoMjXspX4xeHkhswfr1JA7heOjfzPCBbTJU/640?wx_fmt=png&from=appmsg)

设置策略允许所有powershell脚本运行

![](https://mmbiz.qpic.cn/mmbiz_png/kibYIhwqxpuibmOyVmKpOUKDDR5FZg6CUAphsFyLxJMUr0gqiaKYR2aicTTzTricwaic6rCo4MSw8yyOX6kcYVYZs0MredeTgv8b6L9R0jiaYzdZOM/640?wx_fmt=png&from=appmsg)

这个时候使⽤ powershell 脚本来创建⼀个管理员⽤户：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kibYIhwqxpu9QhHmKdy9U5OABviaQWV7zmykqlsC0eVWAero0OiaPWZNQqHic6hvh3R6tAJuksSzjZXWO2DyvNmI5iaSYt1FQGibSCR2sC8b3LibLY/640?wx_fmt=png&from=appmsg)

这个时候再 net user 查看⼀下⽤户发现已经有了 1 这个⽤户了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kibYIhwqxpuibhyeribufficPaOBAE3HwnZl1zeKt3kJm4zUdfF4bogcRRxMSQiawPGyW2Pmn4vkEy2uH7ElZ0Vf8e1wxol0L3KNudRk73cia2al4/640?wx_fmt=png&from=appmsg)

但是 1 这个⽤户不是管理员，可以再次执⾏命令：

```
# 把 1 ⽤户添加到管理员组
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/kibYIhwqxpu9aibTSCjbNXiaf3x6XKuTXJ4byic2N06sCFibzTPU4vsDHlL7BAUWZpbuibhbztkWLVObfZSUz3JESBUbuIBbnIPaCq9YYodialP6qo/640?wx_fmt=png&from=appmsg)

这个时候 1 就是⼀个管理员组的⽤户了，就可以利⽤1⽤户做⼀些只有管理员才能做的操作！

因为利⽤此漏洞的时候是以 **「SYSTEM」** 系统权限的身份运⾏的，还可以以 **「SYSTEM」** 权限运⾏⼀个⽂件，例如 **「notepad.exe」** 进程：

```
# 以 SYSTEM 身份运⾏ notepad.exe
```

![](https://mmbiz.qpic.cn/mmbiz_png/kibYIhwqxpuicNMkiasheZBkBAibVuUCeb5xsKsVOGZzOmAF4fyN1UebqPDgoLY1F3oiaRRAtDGhqfsd957KAia0zTZHZ9EN6RdqX9s8meCWBhP80/640?wx_fmt=png&from=appmsg)

可以看到就可以以 **「SYSTEM」** 身份去运⾏⼀个程序，⼀般情况下会运⾏⼀个 exe ⽂件来上线到 C2，运⾏成功后你就是⼀个SYSTEM 的 Beacon 了！

# **「本地提权」**

本地提权漏洞就是⼀个本来⾮常低权限、受限制的⽤户，可以提升到系统⾄⾼⽆上的权限。

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/kibYIhwqxpu8EhCzdSkDx5N0DhibPsokq5h9ibKbHxjOT3ZwPfHSrYZwBKSTnItXCdHnB2whha0B1yQWicv8yhRibWSicUwv8XpOS2OPcp1uHKNn4/0?wx_fmt=png)

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