---
title: 好靶场杯第一届综合赛-古法赛道-流量分析-FTP流量分析
url: https://mp.weixin.qq.com/s/ADJ3z6-3xKxHPMqgjG9waQ
source: Doonsec's feed
date: 2026-10-30
fetch_date: 2026-10-31T07:42:51.603036
---

# 好靶场杯第一届综合赛-古法赛道-流量分析-FTP流量分析

# 好靶场杯第一届综合赛-古法赛道-流量分析-FTP流量分析

内存余响
内存余响

内存余响

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

#

内网流量监控平台告警，一台文件服务器短时间内出现大量认证失败记录，随后有数据外传行为。请分析流量还原事件。

# 1.提交攻击者IP

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibib4k2pgTh8dGYRXHNiaeS5N5WGmibTBHTClRFHbPudBmI2b8F8jSwt7QaTSuIRPZHFHdibyqmcjpyZuiclMt6LDW1IB8bAlicpXvxNI/640?wx_fmt=png)

我们把流量包放wireshark里面分析就可以看到，有很多arp协议，看到这个192.168.39.88一直在对192.168.39.0/24这个网段进行扫描，探测存活主机，基本就可以确定这个攻击者ip是192.168.39.88

答案：192.168.39.88

# 2.攻击者对哪个网段进行了存活探测？发现了多少台存活主机？

这个哪个网段进行探活我们上一题就已经确定了，192.168.39.0/24

存活主机，不知道大家还有没有印象在前几篇文章好靶场杯第一届综合赛-古法赛道-流量分析-ssh里面有个差不多的题目

arp.opcode==2 #进行响应就说明是存活的主机
#我们已经知道攻击者ip，和起来过滤一下
arp.opcode==2&&arp.dst.proto\_ipv4==192.168.39.88

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibib7kAz7RgCpTCtDFGlC285HCN5FGBQhfy8MH26gfPByEUJFj6jBibNLhr9iaLAAQWwF4xcxKLfQyF2ZUnnVgVsT4uSN5y5oGKMqU/640?wx_fmt=png)

存活主机有192.168.39.1,192.168.39.2,192.168.39.89,192.168.39.90,192.168.39.91,192.168.39.92,192.168.39.254一共就是7个

答案：192.168.39.0/24，7

# 3.受害服务器开放了哪些常见端口？

先来过滤一下看看受害者主机是哪个

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibic49llkYBE2NiavBybIgzLdEoxQYMqKBlRpHbUz5kiaiaxDol7WTsytkwbxk0oAYVXGKBSGTk8hyjdbVsC5p5jTkSATw7KovvS5ib8/640?wx_fmt=png)

确定受害者主机是192.168.39.90

接下来我们再对这个受害者进行过滤

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibicib5qMPMVVj9qlK8Byyoj8zRiau0TIP87wT62eyQia1D1xZ15Bwax79zCDicj8E4Lo3b5CFjm5ULwIk3H6eBia4YpmRoCMSeln0lZk/640?wx_fmt=png)

题目说是常见端口，所以只有21,135,139,445,5985

常见端口号

好的，已经为你加上 5985 端口并重新整理，按端口号从小到大排序：

|  |  |  |
| --- | --- | --- |
| 端口号 | 协议 | 中文 |
| 20/21 | FTP | 文件传输协议 |
| 22 | SSH / SFTP | 安全外壳协议 / 安全文件传输 |
| 23 | Telnet | 远程登录协议 |
| 25 | SMTP | 简单邮件传输协议 |
| 53 | DNS | 域名系统 |
| 67/68 | DHCP | 动态主机配置协议 |
| 80 | HTTP | 超文本传输协议 |
| 110 | POP3 | 邮局协议版本3 |
| 123 | NTP | 网络时间协议 |
| 135/137/139 | RPC / NetBIOS | 远程过程调用 / 网络基本输入输出系统 |
| 143 | IMAP | 互联网邮件访问协议 |
| 161/162 | SNMP | 简单网络管理协议 |
| 389/636 | LDAP / LDAPS | 轻量级目录访问协议 |
| 443 | HTTPS | 超文本传输安全协议 |
| 445 | SMB | 服务器消息块协议 |
| 1433 | MS SQL | 微软 SQL 数据库 |
| 1521 | Oracle | 甲骨文数据库 |
| 3306 | MySQL | MySQL 数据库 |
| 3389 | RDP | 远程桌面协议 |
| 5432 | PostgreSQL | PostgreSQL 数据库 |
| 5900 | VNC | 虚拟网络控制台 |
| 5985 | WinRM (HTTP) | Windows 远程管理协议 |
| 6379 | Redis | Redis 缓存数据库 |
| 8080 | HTTP-alt | 备用超文本传输协议 |
| 8443 | HTTPS-alt | 备用超文本传输安全协议 |
| 27017 | MongoDB | MongoDB 数据库 |

答案：21,135,139,445,5985

# 4.受害服务器的 FTP 服务软件和版本是什么？

这个我们找一个受害者ftp的流看一下就知道了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDib8QYhakwdAMjgpkK8p1iczkH7NEYnuCJibIaRmWjtDMZqeJCl3VIz5MdzRBAMaCErdhvfCkKKzCEIYzYpIBuM9ovMCeSxdcSw2Z0/640?wx_fmt=png)

答案：FileZilla Server 中文版 0.9.60 beta

# 5.攻击者在暴力破解前使用 Nmap 脚本探测了 FTP 匿名登录，尝试的用户名是什么？

我们先过滤一下ftp

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibicJsIPuHuYa7YhtJMMPiazdia5PmAQ8rREH1rG8qtVjYuWr67mDGhcMwJKUXQpbgfqBnhgsBZxkJN12QBuDglBCnPKbfYdOMlVII/640?wx_fmt=png)

我们可以看到有很多用户名和密码，但是我们仔细读题，在暴力破解前，尝试登陆的用户名是什么

这里我们需要知道在 FTP（文件传输协议）的通用标准中，anonymous 是唯一官方指定的用于“匿名登录”的保留用户名，而且攻击者发送了两次 Request: HELP。这通常是 Nmap 等扫描工具在探测目标 FTP 服务的版本，或者获取支持的命令列表。

答案：anonymous

# 6.攻击者使用了什么工具进行暴力破解？

我们可以来分析一下这个流量特征

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDib910gib7F69pLO1ESVTVsucWxWYibBria9Xm2lBjzvB6VGYMAN3fehiahOgVQJHzOY1OAJ0CiaoQMJEGsegpAywdo2mfjadTPYDj1Tw/640?wx_fmt=png)

可以看到是多线程并发，对同一个目标连续发送 4 个完全相同的用户名请求，猜测是hydra

为什么是 Hydra 而不是其他工具？

1.Medusa：虽然也是并发工具，但 Medusa 发包的特征通常是非常规整的周期性循环，且由于其对并发连接的管理机制，往往会先建立多条完整的 TCP 连接，然后再分别发送 USER。

2.Nmap：Nmap 的暴力破解脚本通常是单线程的，它会等上一个密码验证失败并断开连接后，再发送下一个，时间间隔会比较均匀（比如 1-2 秒一次），不会出现截图里这种瞬间爆发式的并发。

3.Burp Suite Intruder：Burp 虽然也能爆破，但它主要是基于 HTTP 协议的。如果是针对 FTP 协议的爆破，Burp 发出的底层 TCP 包通常不会出现这种极其密集的并发特征，且报文交互逻辑往往会有细微差异。

答案：hydra

# 7.暴力破解的目标用户名和成功密码分别是什么？

这我们一般就找最后一条了，追踪流，就可以看到已经完全进去了![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDib9pRajGFh8LUfnfQyZ0VTlDFckL0ubSAibNibia11ibPf7y0ibXlkbv6aYG3aeawBfbKmTxyQbGKuSuRhLRzibDibL4S7jIFtS9oIk8Kw/640?wx_fmt=png)

答案：ftpuser/ftp@2026

# 8.暴力破解共尝试了多少个密码？产生了多少次登录失败？

我觉得这个可以直接数，也不是很多，一共尝试了30个密码，登陆失败的在加上前面三个不是暴力破解的

答案：30，33

# 9.攻击者登录后浏览了哪些目录？

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibibHSbqWlowUMYf5dRyZRozPGgjJBficdQac4pkRhZ9flkxia0NdWpP67icMvBOxhicYicusv5fTWGwMaAH5yQQPW75RCkEn1wicSJFdQ/640?wx_fmt=png)

这直接就能看到也不需要追踪流

答案：人事档案,财务报表,运维文档,项目投标

# 10.攻击者一共下载了几个文件？列出全部文件名。

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibicLQeX8lm8jjZYCRp9Rfqr7UHpXxflmsv15n2vjAso8Df52Bibpt6jHnpJKcQgl0KeEibIu5mZrceVPeOOxl8TkpRicibEibSLlSyr8/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibibWKvFE6OVU81sJzia8YPo3wUfXETE85icznkEzVkOGXicZUekJdupTs7M4Z5DM3DewDys2CheibaGK4v0LuAOrVl66ibjuibGuAAmMg/640?wx_fmt=png)

答案：5|README.txt,华章科技-2026年6月薪资明细.pdf,华章科技-2026年Q2财务报告.pdf,华章科技-内部系统凭据清单.pdf,华章科技-山东政务项目投标方案.pdf

# 11.攻击者下载 PDF 前切换了什么传输模式？

传输模式是什么？在 FTP 协议中，传输模式决定了文件在网络上传输时如何处理数据。主要分为两种：

·ASCII 模式（默认，命令为 TYPE A）：用于传输纯文本文件（如 .txt, .html）。它会在传输过程中自动转换换行符（例如将 Linux 的 \n 转换为 Windows 的 \r\n）。

·Binary/Image 模式（命令为 TYPE I）：用于传输非文本文件（如图片、PDF、压缩包、可执行文件）。它按原样逐字节传输，不做任何修改。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibickAdQN7OF5dtRdEtmfRdXvwlughIUmVmALuD17quz2dUNlhVYKkkX7CnhrgmcUe4wBngrVdfRZ3UeJWYmdfiaic9GksmmwvlO0c/640?wx_fmt=png)

看到这里改成了TYPE I

答案：binary

# 12、被窃取的财务报告中，公司 Q2 总营收是多少？

这个应该就是在华章科技-2026年Q2财务报告.pdf里面，文件-导出对象-导出ftp-data，之后就可以得到这些pdf文件

或者也可以直接过滤

ftp.request.command=="RETR"

可以看到下载的这些文件

打开文件

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibichmLmqW93j5sa1M3grAK2ejBRsNmpUyXx3BMMx7LJEEOqOCSPjYibDPw3VrM9pYdA72MSC0bv0d1KqolbxJ1PkYXzOs1DyeLdw/640?wx_fmt=png)

答案：8743.2

# 13.被窃取的薪资表中，CEO 王建国的月薪总额是多少

这个应该就是在华章科技-2026年6月薪资明细.pdf

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibic2DB3rdzyqXm0qLaEbicLOcEUhjs8TJ1EaQroEVhhK1Uh9Yd7TYvCQGkwEZU7Wkhiaj8Ceq7QnHQQC5NwaJfQRM7v9VLr19sULI/640?wx_fmt=png)

答案:110000

# 14.凭据文件中生产环境数据库主库的密码是什么？

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibicusPbDEO5Nmeu6xQcUCN05d8Qv34MEXl4rByNleSLaevW7YYXgzok33D8Bic5AwpsMl1O4RUurSGWpw3ADKze4xzrz57iaBjwYc/640?wx_fmt=png)

答案：PgMaster#2026db

# 15.投标文件中该项目的投标总价是多少？

![](https://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibibdcJ2ibDsPwYwcDRkib8FHCXo7uAYsYIyCKCjHAFnWryuVicicnAJgdOXFiaQuSYXLBVJicDR0q1RdicmbHLUhTqpGicCO1HIib1ewWs6A/640?wx_fmt=png)

答案：2350

# 16.被窃取的文件中隐藏的 flag 是什么？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/MUfg9mkDDibicYDA92psic6L3TuhUEXK5tAL2GFYKSalficEJRQ89JA8SKXDLFBZfJzmy5sLfujQPeYh2HQMQYO5hadoicS0QJDoexX5IT8sOwpc/640?wx_fmt=png)

答案： flag{420E8A8C540D4BE07F0221F46CCFB8EE}

预览时标签不可点

不喜欢

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/MUfg9mkDDibic4YfldibtqMVhOo0ez7bhNzzvcKGfFIlhFKFvlSN3VmFvNUVyibvMYJP3SR60w6t9GFkzGY4yrGNrvk2DZYQ5lbJQppuHpG1VfI/0?wx_fmt=png)

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