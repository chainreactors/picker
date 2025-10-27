---
title: Setup FTP server on Ubuntu
url: https://buaq.net/go-144579.html
source: unSafe.sh - 不安全
date: 2023-01-08
fetch_date: 2025-10-04T03:18:44.297432
---

# Setup FTP server on Ubuntu

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

Setup FTP server on Ubuntu

Skip to contentThis is the steps I followed:https://www.hostinger.co
*2023-1-7 21:21:37
Author: [acassis.wordpress.com(查看原文)](/jump-144579.htm)
阅读量:40
收藏*

---

[Skip to content](#content)

This is the steps I followed:

<https://www.hostinger.com/tutorials/how-to-setup-ftp-server-on-ubuntu-vps/>

But while trying to connect I got this error:

```
$ ftp 192.168.0.5
Connected to 192.168.0.5.
220 (vsFTPd 3.0.3)
Name (192.168.0.5:alan): ftpclient
331 Please specify the password.
Password:
500 OOPS: vsftpd: refusing to run with writable root inside chroot()
Login failed.
421 Service not available, remote server has closed connection
ftp>
```

I fixed this error this way:

```
$ sudo -s
# usermod -s /sbin/nologin ftpclient
# chmod a-w /home/ftpclient
# systemctl restart vsftpd
```

It fixed the first issue, but now vsFTPd is reporting “530 Login incorrect” even with correct user/password combination.

This last one was a little bit more difficult to solve, but finally I found a user that explained the issue correctly:

“By default vsFTPd uses the file `/etc/pam.d/vsftpd`. This file by default requires FTP users to have a shell listed in `/etc/shells` and requires them **not** to be listed in `/etc/ftpusers`. If you check those 2 things your probably find what the problem is.”

So, I just edited the /etc/passwd to add /bin/bash to ftpclient user:

```
$ sudo vi /etc/passwd
ftpclient:x:1001:1001:FTP,,,:/home/ftpclient:/bin/bash
```

And confirmed that ftpclient user is not listed in /etc/ftpusers

Then just restarted the ftp server and everything worked fine:

```
$ sudo systemctl restart vsftpd
```

I was able to login:

```
$ ftp 192.168.0.5
Connected to 192.168.0.5.
220 (vsFTPd 3.0.3)
Name (192.168.0.5:user): ftpclient
331 Please specify the password.
Password:
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp>
```

Sources:

<https://www.liquidweb.com/kb/error-500-oops-vsftpd-refusing-to-run-with-writable-root-inside-chroot-solved/>

<https://askubuntu.com/questions/413677/vsftpd-530-login-incorrect/670215#670215>

文章来源: https://acassis.wordpress.com/2023/01/07/setup-ftp-server-on-ubuntu/
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)