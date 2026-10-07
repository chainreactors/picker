---
title: HackMyVm靶场-Hommie靶场渗透实战
url: https://mp.weixin.qq.com/s/CMQ-fY2m__RDkb9FkxyzOw
source: Doonsec's feed
date: 2026-10-06
fetch_date: 2026-10-07T07:52:33.642198
---

# HackMyVm靶场-Hommie靶场渗透实战

# HackMyVm靶场-Hommie靶场渗透实战

原创

架构师面试
架构师面试

白帽子教程

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/VgLbXH4m4wtx0MfsIQeZW6SlPdfuibnWVzT7l4rYxO4ncTCe9KPAgvlqPRlzu4vzEW7ag6TIo5gWibicuKCfkQ8Ujhb0T01icLQoVqwiaYUrkW7E/640?wx_fmt=png&from=appmsg)

靶机地址：

https://hackmyvm.eu/machines/machine.php?vm=Hommie

靶机下载完成之后将其导入到VisualBox中如下所示：

![](https://mmbiz.qpic.cn/mmbiz_png/VgLbXH4m4wtqbUFJQEQib0jwH2NPlTKDuH6BGp1z17Q0hz9pjxJWib3GvST9nrkjSJAvYjRvvMse6K8e2UjcFC4I891ywdKu1S2oQeNscLUgg/640?wx_fmt=png&from=appmsg)

接下来我们就进入到Kali攻击机中来查看一下局域网中的靶机IP地址是多少。

```
arp-scan -l
```

最终经过确定之后，应该是192.168.1.96这个IP，访问一下看看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VgLbXH4m4wvo79wG6SiajLibPbTKAacRkiawOIReIVKPk083pRcdmAduiaORSh4fLLFHd3qvXqPWO67EKWZTEMCW6iaG59gatP66ZHvY2peLIJ4I/640?wx_fmt=png&from=appmsg)

从结果来看，确实是这个IP地址。

接下来我们就来看看这个IP的端口开放情况。

```
nmap -T4 -sV -A -p- 192.168.1.96
```

![](https://mmbiz.qpic.cn/mmbiz_png/VgLbXH4m4wuiciaBibbKMibsG9bRPRBI5RwRzeoIn4LuzX6R8Isl3iamoWibjP5Pkmwxaia57tSvty63GpFgOicHtPE9A7YQQMbE10hJQj6wFNibzS1U/640?wx_fmt=png&from=appmsg)

经过探测之后，发现还存在21端口、22端口。

通过80端口上的内容我们得到了一个关键信息。

```
alexia, Your id_rsa is exposed, please move it!!!!! Im fighting regarding reverse shells! -nobody
```

也就是说这有两个用户alexia nobody 并且提示我们要得到alexia的id\_rsa。其实根据之前的经验我们就知道了nobody用户其实就是21端口上的用户，也就是可以免密登录。我们来尝试一下。

![](https://mmbiz.qpic.cn/mmbiz_png/VgLbXH4m4wvFm9ZwiaxEGnpgxWiaTliaA2ibrxSgoBaMHnaTFvibUoAyfTQXxDBMerbjAhZOfjERnWmxORLrObLYmcVJKQU3dJobhHVzKhU7xbv8/640?wx_fmt=png&from=appmsg)

```
ftp 192.168.1.96 Connected to 192.168.1.96.220 (vsFTPd 3.0.3)Name (192.168.1.96:kali): anonymous
```

登录成功之后可以看到一个隐藏的路径Web和index.html文件，这里的index.html文件猜测就是刚刚我们在80端口上访问的文件。接下来我们看看隐藏目录下是啥？

![](https://mmbiz.qpic.cn/mmbiz_png/VgLbXH4m4wsTyQj6JSZ2vlLpticibw8aftuwzcuF3fm4LcwYVzeFoQuXaPeVdYVDVVdFZPZiaWsicSHeSSwVDAJTUFBqbkEOa32bKXZqtJpsCxg/640?wx_fmt=png&from=appmsg)

还是一个index.html的文件，我们将这个文件下载下来。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VgLbXH4m4wsm7AbfUXQsGGoFlvDqia1OuJCM5OekKYXtibYAtpTNKnaUEFxVqkkiacMiaibMLKwrDPzsq2MB2QUbVD5ibwDdibMzWYU1mVicTpe9ISg/640?wx_fmt=png&from=appmsg)

这个是里面的文件。外面的文件的内容是空的。既然这样的话我们是不是可以回传一个WebShell.php上去看看能不能建立起反射Shell。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VgLbXH4m4wuRgHxXg903YpKlEcmAAgenhyGtlAk72LBEtuNFgz4yfMUErCGGvMLetX10MeruibtF6UBc9GQhRxcX3YZTWKqo1TkDQKNnVXxQ/640?wx_fmt=png&from=appmsg)

接下来我们尝试建立一下反射Shell。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VgLbXH4m4wv3gnOaskC9Z9Czhovop4wVxxOW737SdPqweM6NxOia4icBTjRsaokl6Bw4KIZKicibNQ6dficMZmiaT6icK4gicpJkdQAXibUs854U1N8Q/640?wx_fmt=png&from=appmsg)

发现当我们访问文件的时候，文件被下载下来了，也就是说这个操作不行。我们再试试其他的方案。根据提示应该是可以得到一个id\_rsa文件的。我们看看怎么才能得到这个文件。

```
nmap -sU 192.168.1.96 -p 1-200
```

我们用这个命令来进行小端口的UDP扫描，之前我们扫描的都是TCP请求。经过扫描之后我们发现了一些新的内容。开放dhcpc tftp 服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VgLbXH4m4wvhFsy056VtsVgHkQu8wxBCTcUmrIUiaXNTsTAJ4OtZmUiajJXAVMeoW1ZiaW5ib9RvvWnRXgkI5g0XLgbibRpdwibZTkp8to1KRQB8k/640?wx_fmt=png&from=appmsg)

我们可以尝试连接一下这个UDP的服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VgLbXH4m4wvSuib1xzMJVSZPyoxegrZEicibptUDacq5qb4liat7LUZZH0tMocT3nodnAqhx4KUwsz49uKrvLzwGmXbYnxLDyL5k3c7ungUjAMM/640?wx_fmt=png&from=appmsg)

可以看到这个服务确实可以执行获取到id\_rsa的内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VgLbXH4m4wtibBhdheJe8ibWuKfjkF8iazYYpWUfAbqU9lPKuz09Cjxiayj9MKiby52arJDmDTeFv4fBkricV27k7sZVOn0iaBzKPok6vZrt3sOrNc/640?wx_fmt=png&from=appmsg)

接下来我们尝试登录一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VgLbXH4m4wv9G52Bs3XjUu6WLUcicBmRoLQG5IhhzPbBstfXKB4K2mrXdtkHWTKE6f0ia1mI4ibMrjmIApdYV8wQAEKdqAtQLghp2nt3F7hhicA/640?wx_fmt=png&from=appmsg)

这是为什么呢？是因为id\_rsa的权限。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VgLbXH4m4wvJn4g91FTpnWM4ic5LEufdgexYOlqoEdHzXeNRHx5DkhuoPRh99oEkuH5Aozk2icQdC2Q19JyyicEjF8zG2os5koyJMiayib1N7RtY/640?wx_fmt=png&from=appmsg)

提权之后，我们就可以进入到alexia这个用户下。并且我们得到了第一个flag。

![](https://mmbiz.qpic.cn/mmbiz_png/VgLbXH4m4wtHk4dWL6tiaFia3Mrr2W6O91Fl2w2fpPoI921UUxdpcsXzU6JILfKSv0yTYOtEDCib1egibk0BOibibBQSz8zjnoVfuKkzArax9f4vs/640?wx_fmt=png&from=appmsg)

接下来我们就需要看看如何提权了。这里有两个方案，一个方案就是利用Linux的最新暴露的漏洞，直接进行提权。当然这并不是我们的推荐方案，第二种就是我们继续一步一步的搜索。

```
find / -perm -u=s -type f 2>/dev/null
```

![](https://mmbiz.qpic.cn/mmbiz_png/VgLbXH4m4wsEJibw1TKxaZSRILcgoyhzrK0qcm7n0X8I2WRibxiaEtJkwAX7nglejOGicK9CMwYdwANPNm4pPZ2pzJNlqcPcBRPok8kSrLWqxD8/640?wx_fmt=png&from=appmsg)

有一个文件比较可疑就是/opt/showMetheKey这个文件。我们直接执行一下这个文件看看效果。

![](https://mmbiz.qpic.cn/mmbiz_png/VgLbXH4m4wv19ERVV6xKzaRQYKT4dXAtclqhDWcrkJQJbO1VySUTwpAibkbnVow5buddCPyKwejzlNqe9EU12Ua69XMlDK6D7uXLp5QkHt04/640?wx_fmt=png&from=appmsg)

其实这个文件就是id\_rsa的内容。既然这样的话，我们就可以利用这个文件将root的id\_rsa内容获取到从而达到提权的目的。

![](https://mmbiz.qpic.cn/mmbiz_png/VgLbXH4m4wuy6yow85HffyAysPlpR1cmagmIH25S8KrpndP9Z1Ax03yJMFzPQI4oD5I9Vib1nPNM1OecZvWeCS4GjojlYPwW74WoibibibPZcms/640?wx_fmt=png&from=appmsg)

下载下来之后我们来分析一下这个文件。

![](https://mmbiz.qpic.cn/mmbiz_png/VgLbXH4m4wttaFQHO7pe2EYbXib8jRzmqTSJfxVaV3Z4eia0ia8v0nxiacEeRy3iblvb7AJAh1BDibldJMF4djSPsibDiaZmTKFWIVuRibOzIiaNytxIY/640?wx_fmt=png&from=appmsg)

发现一个核心的代码

```
cat $HOME/.ssh/id_rsa
```

这个代码给我们的启示就是通过修改$HOME的值来达到获取root的id\_rsa的结果。

```
alexia@hommie:/opt$ export HOME=/rootalexia@hommie:/opt$ /opt/showMetheKey
```

![](https://mmbiz.qpic.cn/mmbiz_png/VgLbXH4m4wse25tnWdmiavadDsW8ucyOSfPwiczzSxVcibqCbgn9S6S4oibKibX4qEzpZu0ChiaAspNniay7AnJFZYYe5YFavOEDAMeYBEdAbALoRk/640?wx_fmt=png&from=appmsg)

接下来我们就将这个内容复制到Kali的id\_rsa上或者是可以新建一个文件来存储。

![](https://mmbiz.qpic.cn/mmbiz_png/VgLbXH4m4wtOOPjhVGSCr1JFib7clNAZGQf3c8YooebEUgkgbG1icAD2iamkDfUNJ0jRibgZ0Z68Jp02eVxRptgVnTMwTsuwKIt2LXPmw8E8SV0/640?wx_fmt=png&from=appmsg)

这样我们就提权成功了，接下就是看看找到第二flag。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/VgLbXH4m4wseNrh2kcZwoPdv5GM5abYOICmnDum7SlicYY1dgej0o3Crag4CFyQ1lQKSHFcQYkt6xw2VjEMePHrcrCw6FYfmeCjfOTG34GUM/640?wx_fmt=png&from=appmsg)

这样就渗透测试成功了

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/5U4t8BEPt65uqQfAibF9vcy5mV35F91kQBvfdCVjbicwHqJaymr6Knnh160PmRdb8xsw63lMHaAeOKRMNotU9qFQ/0?wx_fmt=png)

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