---
title: HackMyVm靶场之Thirteen
url: https://mp.weixin.qq.com/s/RzFDRzCxj2NfS945Fhaciw
source: Doonsec's feed
date: 2026-02-14
fetch_date: 2026-02-15T04:15:00.552813
---

# HackMyVm靶场之Thirteen

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8avkpGSKmqe5NVKmQwkyRsFrcw2KgUXNmFXOiaZVmaTRCCOmdbmrsNDaOyZiapImVliagHzM8SUEXbfWlDrsrWm8KHevBZVeyQSg66icTwLoKfc/0?wx_fmt=jpeg)

# HackMyVm靶场之Thirteen

原创

MS02423
MS02423

MS02423

![]()

在小说阅读器中沉浸阅读

这个靶场考了rot13,cupp,ss知识点，整体是比较简单的。

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeCbWVuOc9G3TesEb3bZDSe4jTSA3XrIn4qPiaGLEraLtdfPOd3k9ZYp9m8obUZ24PIPOS2ahIyalxZN2Qu2LSNicicWrXoZxSHicw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqedcGAM6T2DOFsw5CvbdmiblbXqNeUd1jYzpBdT5Hfp4D9M6sgbWEjHAbOIgGYzBKIUoUU3cVHInHVangBJD6bCYDyZj3wFCyyU/640?wx_fmt=png&from=appmsg)

根据题目和提示，我们猜测是rot13

1.探测IP

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfuBYTR660ibaJXXmqicnxFAtIB6MRHSnLfNKKPYRFwiaFAqFhrLKPJ6JqmL074GmC8avzSM35WIcggIRZDFiayJfvUPhFgfhz3Pxc/640?wx_fmt=png&from=appmsg)

靶场IP是192.168.137.50

2.扫描IP

1)扫描端口

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeyxqWIJffC0sNNibgibGxT12Eu0tpG6Pf9ufGa1zbdV4VQfojzvic1sTiasz73KSoNLQrZMdUpbuOas9w4eqnbUg3wuTv2E2BPDvM/640?wx_fmt=png&from=appmsg)

端口开放了21,22,80端口

2)扫描目录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeViaXOQRHicgepkFG2pRdDmcJOvz0e8juaS2DZoAtQvGg6ksXZWaK0EAvD3Ag4fGk1dJj9ODXwdH5ZpKeDL8LSzSiaJwGzSLOsog/640?wx_fmt=png&from=appmsg)

我们可以扫描到4个目录，我们去查看

3.访问IP

```
http://192.168.137.50/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdp8FRicbLzsvdcMEe81xjw9ibAhCiba2YXAX5aibYsTPJibeWmO40iaecXIdDeI1PcxkxjA7IZFzZB1vGEHKicTVFtftMkmcbKvTfWZ0/640?wx_fmt=png&from=appmsg)

我们可以看到一个界面，下面有东西，我们去看看

4.渗透测试

1)rot13

```
http://192.168.137.50/?theme=jrypbzr.gkg
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcMh2icu3cVnakJicoibzKmLINujUmVrp5fntDanuUpjvUApcRica0sNjbF2hibNbqUwEGAK6ugK8At9icsccVuLndqS9a3SiaZVuqibfE/640?wx_fmt=png&from=appmsg)

```
http://192.168.137.50/welcome.txt
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqd6E1X2t50Bhv8xcPosS3GiavvMkT8yt5sUfbNHkHGJPUqmvLFHZfnljOE0d3sia0sicO5ic9wcxpJWohQ88OsoGO0VBxqhHSI3tB0/640?wx_fmt=png&from=appmsg)

我们可以看到welcome.txt和?theme=jrypbzr.gkg里面的内容是一样的，而且?theme=jrypbzr.gkg感觉是加密的，题目提示我们是13，我们猜测是rot13,我们去解密试试看

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfCg7ib35pcKZnfXIl9OjSNReD63JqMbicRWcKH2CSQmMTyoyxUT9libWgW99ZplPIfI8JPxGQ80Mh2vyVnGcYgJk0mwvO1ibQ0dbY/640?wx_fmt=png&from=appmsg)

我们可以看到welcome.txt的rot13就是jrypbzr.gkg，所以存在rot13加密

那么剩下的2个

pbasvt.gkg对应config.txt

ernqzr.gkg对应readme.txt

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqerpSEfOmKictkeCZaxjtb1Y1W8DyftV9fd5MLTGhLn5kGk6KHtXbVtuFeITeic5XXjV8eTsSkMVvAdav7nP0SFjczxicfJfIlxJw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqf56wlzSM98ltJBH3Eysiaz7k5LXgkNgicOQnS71q1icM2Oe0LtUfRN3Zw3wIh3jskDdib8zpKy8jHKDWFOuTnblTcDdRANicsw3ZHg/640?wx_fmt=png&from=appmsg)

我们去看看里面的内容

```
http://192.168.137.50/?theme=jrypbzr.gkg
```

里面应该是用户名或者是密码

```
http://192.168.137.50/?theme=pbasvt.gkg
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfwDCEhjvQ1icNQGuqMJ4ibUuC4MtwqgeVmgF7Ne3q477obiaOv6rGuCx8LkF6dTNqCejm2ZsYpjQKoLunb0FrK1DkibXKib3sicLOQU/640?wx_fmt=png&from=appmsg)

日志记录

```
http://192.168.137.50/?theme=ernqzr.gkg
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfHl7g9XyNM88NFq9zY7N4NIceGwuyjD6ficcldkUnv3jCV7r71RibWMY2kz0orRqiaVHnho9eLYUY0oSbMb03icvMebZfpZiavO2G8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfulseuz8ezdyLMop0cJGibJd8YzWjkLial0zsqgtDDiaDKjQz6P8fnM3e7gaM2m2SVthibFN6fAcxlibqz26ePFIrVBMvFzNqF5AJk/640?wx_fmt=png&from=appmsg)

告诉我们只能使用ADMIN使用

还有一个/logs/，我们去看看

```
http://192.168.137.50/logs/
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdwLb9PhNg6Rib1AGY3gfV7wDnL0ZwMYjDB8Ifo9TxZLXzfibYO8W25gXD8Oia58fbfNz4f9EFO53CEfT58DMyicMJwZ0u0BT9B5Bo/640?wx_fmt=png&from=appmsg)

是一个403,我们再去扫描扫描

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcJ6uFicFUqiciccbA9sXiandBRuY1bfgkIu5cceGh3LdHoPe4gtqZz7pXkjSZDhgZT1hickrhkwXpZrbbhP0eVX32PNOgKIlThicrcY/640?wx_fmt=png&from=appmsg)

我们可以扫描到一个log，我们去看看

```
http://192.168.137.50/logs/ftp_server.log
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfjznVk4sBSoquWg1ia3tIeph8k3Q0qmI0yz3TRZDmGr9djGt1lNP7eHQ1iaTtW5GUdOq8ghrN0qNvhybQ0rJQbKMVeUWicbyj87Q/640?wx_fmt=png&from=appmsg)

我们可以看到ftp用户名是ADMIN，还有一个脚本路径是/opt/ftp\_server.py。

目前，我们掌握的信息就是一些用户名或者密码，还有一个ADMIN，80端口的信息应该就是这么多，现在我们去看看21端口

2)ftp登录

我们匿名登录试试看

我们去使用ADMIN

发现需要密码，首先我们去使用rockyou.txt去爆破，如果爆破不出来的话，我们就去试试刚刚收集的那些字典

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdt2p3DCmWe0t4wfH97swUq4yvUIRKVLx2GVK46lOe3xqBmX9XVNFzxsv2QnYLuGicAo6dJZDLSpoTfoM8Y01mQAXqORtBicGlSU/640?wx_fmt=png&from=appmsg)

```
hydra -l ADMIN -P /usr/share/wordlists/rockyou.txt ftp://192.168.137.50 -t 4
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcZOfgTFJvOQFK7icsn8icQel0lEp3EhDyMh1ftMGYzUCiaD2TWSndlbpdh08f2BsQvFvjJ0QqAtND4g6aVgU1nf3ZFDNKq79hQF4/640?wx_fmt=png&from=appmsg)

我们可以看到密码是12345，我们去登录

登录成功，有2个文件，一个是ftp\_sever.py和一个rev.sh。

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeBiaM6ZHHbIYTaibOEskZupufkk9qx4Dk15e7mXZRKI61dZzXuNQeLcn1FrNeUcZ7toR16JKBhaysP7lrThOCT0Ss5hHHIfWwvM/640?wx_fmt=png&from=appmsg)

这两个文件和前面日志里面的文件是一样的名称和内容，所以我们猜测他们的路径就是/opt/那么既然我们知道了路径，我们可以上传一个脚本试试看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfyvbDbzDwoicEJkUJiaVOSc3EYH02ZspcqYRbWRZZbnTOXRLAPZYfngVSWKaZMGHFnB8paEJEIib35EicHjJoN6nzhjlvmN6SCWtQ/640?wx_fmt=png&from=appmsg)

ftp\_server.py里面的用户名和密码

rev.sh是一个反弹的命令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqe82bg8GI4fKH4WgKcwWFEfY8XTBEL26DJe92siapLvcaIuHmEo0LGAE2YXow1NbLKDvWmMc38BQQTkuCjUx0AeHLfic1Mpicr0to/640?wx_fmt=png&from=appmsg)

3)反弹shell

我们去上传一个反弹脚本试试看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdDbRAAuacNoc9zpcmMcBHOjZ7icmmUCOzYfAS0hA8CyuSxc6HfPrUicZjHDYZ02kOZCm1xTg1wzRRhurB28aEupic18GnicXBGIFY/640?wx_fmt=png&from=appmsg)

我们上传shell.php，然后路径/opt/shell.php，这里我们是需要去rot加密的，然后再去访问

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqe1lO4dlEoXQoWexFPibcdPa39C5EqVAOpoP5hPHIYdEkEhK2weKEWKibktH8sOs3yaW3fFHEKnIX0DHiasbfqSUkPyjUqInnsNqQ/640?wx_fmt=png&from=appmsg)

```
http://192.168.137.50/?theme=/bcg/furyy.cuc
```

我们可以看到是断开了

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqe3aJwacE73F2Isiayu117VAAxWouJXxZhqt63OkeqrNPwXUbr3Zg1pdNLfTMxTn1DttU0Rg9Ttvo9z9O6pkdMmzX4DgsJ3FuTw/640?wx_fmt=png&from=appmsg)

那我们去使用一句话木马，然后连接蚁剑试试看

```
http://192.168.137.50/?theme=/bcg/jro.cuc
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqfWMPfVt8Zpd63tmxbQX0o0y59kbZEjcvxEKsenKDqttnco0vic50wRf9RFSFyCWH8A65KaIxjicibVvgYuRLC3udx426icicQF1zk8/640?wx_fmt=png&from=appmsg)

我们去连接蚁剑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcJicJ5FDSLz5NJ7saNbVDl9IcJdZlpgLe57iaAqRWqyuttu9bTy8oYhmmb8gw61hXI4viafJl86c5l0Br59EgQ3sZVtpIowH0Yicc/640?wx_fmt=png&from=appmsg)

然后反弹shell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqe9j8NPsNIQZRWjYdnibtyX8319Nve3k2Voq1uuIw9PCiawZvsauzQQp0M5BDUodxGmSeOKtSJbxXsnYoDSMtiaeUZwc4mms3fc1s/640?wx_fmt=png&from=appmsg)

我们可以看到反弹成功。

4)cpuu生成密码

我们在家目录下，发现2个用户名

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqf82fEibMbF6Mx1zjtxZdCss8ujrayiaB8V8HuEPz8sy3A5pyia4FGxss5vAm9ibO5ibD0xJs907LQibZicLtiavFNuNG71YA8FdZlxD6E/640?wx_fmt=png&from=appmsg)

在welcome用户里面发现了密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqciaHIJhAVLUguPgh8NhibcbAQODHoRicMTp9RwQrxiaGia0LGVjd0W2J6dibWCtibIXfLYu18Y1Z7F2o3Q7NHictBkxzOniclyml5lx58M/640?wx_fmt=png&from=appmsg)

在max用户下发现了一个.hint

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdkDun7RryTTeELEhibZOsC8DBS3NhBXCMUiakEjPtYutrsL6cxnvlVl66WOQFUkNjJfupdhQkZy5HokTD91deZdryIuFhP5enos/640?wx_fmt=png&from=appmsg)

告诉我们是一个cupp

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqd0rabqrgzp3bVXDzWibErxL8sIwwxdo5uzDl6kpm2FcChovRBjH4mEeicwlibUib3eb42W6Z6NjV7q8loSxhrnP0JBgRHW9MedHMI/640?wx_fmt=png&from=appmsg)

告诉我们是一个生成密码的工具，那么我们去生成密码，用户名我们使用max和welcome,我们去爆破

密码我们使用welcome.txt去生成密码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdWZu1iaia91gofa0mYvtBwk86iaKdibichwfrwiaybo7FaI6UKdGsRvP0qQ8u6uAf5y4C11HX1IGoUysUIzhSAibYCiaBNXSTtcQd1wE8/640?wx_fmt=png&from=appmsg)

我们一直选择y即可

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqczibOgjfK2TOOJYTXgP0lMqF77xzksP51iafPcwK7AWi...