---
title: Coda：实现Windows/Linux入侵痕迹抹除
url: https://mp.weixin.qq.com/s/SLUM0xFRSTg8Yoo5AlG5iQ
source: Doonsec's feed
date: 2026-02-07
fetch_date: 2026-02-08T04:28:06.360101
---

# Coda：实现Windows/Linux入侵痕迹抹除

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/x2ibBTFXYHicLUWO3S8vJJLXV5rC54v3o64CK6lDbHgg4BH0OXTxlFzK2wuf4A8ibwXyktDcOZ2CbBQRokMzz0mibfQFxT3icubuB8fkgF7zbcg0/0?wx_fmt=jpeg)

# Coda：实现Windows/Linux入侵痕迹抹除

原创

网安武器库
网安武器库

网安武器库

![]()

在小说阅读器中沉浸阅读

**更多干货  点击蓝字 关注我们**

**注：本文仅供学习，坚决反对一切危害网络安全的行为。造成法律后果自行负责！**

**往期回顾**

·[OSV-Scanner：一款专门于发现开源软件漏洞的扫描器](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486240&idx=1&sn=69241fc574c182a305e1c17747377ae6&scene=21#wechat_redirect)

·[LingOps（灵控）：AWD/AWDP 竞赛自动化平台](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486227&idx=1&sn=c7183a4926281db23003d3e02010fd8f&scene=21#wechat_redirect)

·[融合AI引擎的日志应急响应溯源工具SSLogs--详细配置教程与使用方法](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486211&idx=1&sn=b6893a457752881cbef64eb8f685e0fb&scene=21#wechat_redirect)

·[AWD-H1M：AWD攻防竞赛自动化工具箱](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486193&idx=1&sn=0d299367f73c1a711d810af55196a275&scene=21#wechat_redirect)

·[DumpGuard：首个公开绕过Windows Credential Guard的凭据提取工具](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486180&idx=1&sn=c8e5f47564ce29bf0435b6bba13828a1&scene=21#wechat_redirect)

·[FingerprintHub：识别网站和网络服务背后使用的技术栈](https://mp.weixin.qq.com/s?__biz=MzYzNTExNDYwMg==&mid=2247486175&idx=1&sn=ff7c227b167f27367150e9f9d481be57&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

**背景分析**

随着网络安全技术的不断发展，攻击与防御的对抗日益激烈。现代安全设备（如SIEM系统、EDR工具、日志审计平台）的广泛部署，使得攻击者的操作痕迹更容易被捕获和分析。在此背景下，如何 快速、彻底地清除入侵痕迹 ，成为攻击者在完成目标操作后必须解决的核心问题。

![](https://mmbiz.qpic.cn/mmbiz_jpg/x2ibBTFXYHicIqLfGJb2sQiaedYz1CB6pOypYPKOflyqJ0jrurTia7V8jbyDHuFdNTsjXJ163Hd52wC0XMt1IvdcISxEOIxdNseDBCLhoyzIJlc/640?wx_fmt=jpeg&from=appmsg)    Coda是一款使用Golang语言编写的入侵痕迹抹除工具，支持Windows和Linux系统。它能够帮助用户迅速消除系统中的入侵痕迹，保护操作的隐蔽性。

项目地址：

```
https://github.com/Symph0nia/Coda
```

在项目中使用：

```
go build ./main.go
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/x2ibBTFXYHicJt3fPJCJ5KOJBOkubsh7xjG7JhubiaXOGjBgBnEedf7OSPSaoibeBLduR2gwXzTS0atlKHWuXgQmhuHticKZwGeUe3M46qtzELEE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

介绍

核心功能

```
./main -D # 删除所有的日志信息./main -B # 删除大型的的日志信息，将小型的日志信息备份到/TEMP或/tmp文件夹下./main -R # 恢复备份的日志信息到原位置
```

原理

    Coda的基本用法即直接删除所有的日志，从而实现对溯源的打击。

Coda的进阶用法为Backup 2 Restore

    在渗透成功后，运行Coda -B，对当前的日志信息进行镜像保存，接下来可以进行敏感操作，例如数据获取，数据删除一类。

    在渗透结束阶段，运行Coda -R，对已经保存的日志信息进行恢复，不对日志系统进行完全清除，从而实现一个优雅的空白监控时间。

注意事项Warning：

    Coda对系统文件所造成的伤害是不可逆的，慎用。

目前的日志分类规则：大于100MB为大日志文件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/3ibCZqSDX9ugSGKJibovaia9YxcaLfMJib6eFcsfYatVNptgRDr3kqeFwpGYKFziaX9s7BBcG8prEJFW1g1EickibFyug/640?wx_fmt=png&from=appmsg)

清除日志列表

Windows：

| 日志文件路径 | 作用 |
| --- | --- |
| `C:\\Windows\\System32\\winevt\\Logs\\Security.evtx` | 记录安全相关事件，例如登录尝试、权限使用等。 |
| `C:\\Windows\\System32\\winevt\\Logs\\Application.evtx` | 记录应用程序相关事件，由应用程序生成的日志信息。 |
| `C:\\Windows\\System32\\winevt\\Logs\\System.evtx` | 记录系统级别事件，包括驱动程序加载、系统组件的启动和停止等。 |
| `C:\\Program Files\\Apache Group\\Apache2\\logs\\access.log` | 记录Apache服务器的访问日志，包括每个请求的详细信息。 |
| `C:\\Program Files\\Apache Group\\Apache2\\logs\\error.log` | 记录Apache服务器的错误日志，包括启动、运行时错误和异常。 |
| `C:\\Program Files (x86)\\IIS Express\\Logs\\IISExpress.log` | 记录IIS Express的日志，包括访问和错误信息。 |
| `C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-User Profile Service%4Operational.evtx` | 记录用户配置文件服务的操作日志。 |
| `C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-DNS-Client%4Operational.evtx` | 记录DNS客户端操作日志。 |
| `C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-DNS-Server%4Analytical.evtx` | 记录DNS服务器分析日志，用于诊断DNS问题。 |
| `C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-Windows Firewall With Advanced Security%4Firewall.evtx` | 记录高级安全Windows防火墙的操作日志。 |
| `C:\\Windows\\System32\\LogFiles\\Firewall\\pfirewall.log` | 记录Windows防火墙日志，包括被允许或被阻止的网络连接。 |
| `C:\\Windows\\System32\\LogFiles\\W3SVC1\\` | 记录IIS Web服务的日志，包括访问和错误日志。 |
| `C:\\Windows\\System32\\LogFiles\\HTTPERR\\httperr1.log` | 记录IIS HTTP错误日志，包括无法处理的HTTP请求。 |
| `C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-Security-Auditing.evtx` | 记录安全审计日志，包括成功和失败的安全事件。 |
| `C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-TaskScheduler%4Operational.evtx` | 记录任务计划程序的操作日志。 |
| `C:\\Windows\\Temp` | 存储临时文件，通常用于短期存储。 |
| `filepath.Join("C:\\Users", username, "AppData\\Local\\Temp")` | 当前用户的本地临时文件夹，存储临时文件。 |
| `filepath.Join("C:\\Users", username, "AppData\\LocalLow\\Temp")` | 当前用户的本地低权限临时文件夹，存储低权限临时文件。 |
| `filepath.Join("C:\\Users", username, "AppData\\Roaming\\Microsoft\\Windows\\Recent")` | 记录当前用户最近访问的文件和文件夹。 |
| `filepath.Join("C:\\Users", username, "AppData\\Local\\Microsoft\\Windows\\INetCache")` | 存储浏览器缓存文件。 |
| `filepath.Join("C:\\Users", username, "AppData\\Local\\Microsoft\\Windows\\History")` | 存储浏览器历史记录。 |
| `filepath.Join("C:\\Users", username, "Documents")` | 当前用户的文档文件夹，存储用户的文档文件。 |
| `filepath.Join("C:\\Users", username, "Downloads")` | 当前用户的下载文件夹，存储用户下载的文件。 |
| `C:\\inetpub\\logs\\LogFiles\\W3SVC1\\` | 记录IIS Web服务的访问日志。 |
| `C:\\inetpub\\logs\\FailedReqLogFiles\\` | 记录IIS失败的请求日志，用于诊断失败的HTTP请求。 |
| `C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-SMBClient\\Operational.evtx` | 记录SMB客户端操作日志。 |
| `C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-RemoteDesktopServices-RdpCoreTS\\Operational.evtx` | 记录远程桌面服务操作日志。 |
| `C:\\Windows\\System32\\winevt\\Logs\\Microsoft-Windows-TerminalServices-LocalSessionManager\\Operational.evtx` | 记录终端服务本地会话管理器操作日志。 |

Linux：

| 日志文件路径 | 作用 |
| --- | --- |
| `/var/log/syslog` | 记录系统日志，包括内核消息、服务启动和停止、各种系统事件。 |
| `/var/log/messages` | 记录一般系统消息和非关键系统错误。 |
| `/var/log/auth.log` | 记录认证相关的日志，包括登录尝试、sudo使用等。 |
| `/var/log/lastlog` | 记录上次登录的信息。 |
| `/var/log/wtmp` | 记录登录和注销事件的永久日志。 |
| `/var/log/btmp` | 记录失败的登录尝试。 |
| `/var/log/faillog` | 记录失败的用户登录信息。 |
| `/var/log/apache2/access.log` | 记录Apache服务器的访问日志，包括每个请求的详细信息。 |
| `/var/log/apache2/error.log` | 记录Apache服务器的错误日志，包括启动、运行时错误和异常。 |
| `/var/log/nginx/access.log` | 记录Nginx服务器的访问日志，包括每个请求的详细信息。 |
| `/var/log/nginx/error.log` | 记录Nginx服务器的错误日志，包括启动、运行时错误和异常。 |
| `/var/log/mysql/error.log` | 记录MySQL数据库的错误日志，包括启动、运行时错误和异常。 |
| `/var/log/mysql/mysql.log` | 记录MySQL数据库的一般操作日志。 |
| `/var/log/daemon.log` | 记录守护进程的日志，包括系统服务的启动和停止。 |
| `/var/log/kern.log` | 记录内核日志，包括内核启动信息和运行时的错误。 |
| `/var/log/mail.log` | 记录邮件系统的日志，包括邮件传输信息。 |
| `/var/log/mail.err` | 记录邮件系统的错误日志。 |
| `/var/log/secure` | 记录安全相关的日志，包括登录、认证和授权信息。 |
| `/var/log/audit/audit.log` | 记录系统审计日志，包括SELinux和其他安全模块的事件。 |
| `/var/log/sudo.log` | 记录sudo命令的使用情况。 |
| `/tmp/` | 临时文件目录，存储系统和用户的临时文件。 |
| `/var/tmp/` | 临时文件目录，存储系统和用户的临时文件，通常比/tmp的生命周期更长。 |
| `/home/*/.bash_history` | 记录每个用户的bash历史命令。 |
| `/home/*/.zsh_history` | 记录每个用户的zsh历史命令。 |
| `/root/.bash_history` | 记录root用户的bash历史命令。 |
| `/root/.zsh_history` | 记录root用户的zsh历史命令。 |
| `/var/log/sshd.log` | 记录SSH守护进程的日志。 |
| `/var/run/utmp` | 记录当前登录用户的信息。 |
| `/var/log/dmesg` | 记录内核环形缓冲区的消息，通常包括系统启动信息。 |
| `/var/log/yum.log` | 记录Yum包管理器的操作日志。 |
| `/var/log/apt/history.log` | 记录APT包管理器的历史日志。 |
| `/var/log/apt/term.log` | 记录APT包管理器的终端日志，包括包安装和卸载的信息。 |
| `/var/log/journal/` | systemd的日志目录，记录所有使用systemd管理的服务和系统事件。 |
| `/var/log/rkhunter/rkhunter.log` | 记录Rootkit Hunter的扫描日志。 |
| `/var/log/chkrootkit/chkrootkit.log` | 记录Chkrootkit工具的扫描日志。 |
| `/var/log/docker.log` | 记录Docker的日志，包括容器的启动和停止信息。 |
| `/var/log/kubernetes/` | 记录Kubernetes的日志，包括集群中各组件的事件。 |
| `/var/log/containers/` | 记录容器的日志，通常包括Docker和Kubernetes管理的容器。 |
| `/var/log/postgresql/` | 记录PostgreSQL数据库的日志。 |
| `/var/log/mongodb/mongod.log` | 记录MongoDB数据库的日志，包括启动和运行时信息。 |
| `/var/log/redis/redis.log` | 记录Redis数据库的日志。 |
| `/var/log/tomcat/` | 记录Tomcat应用服务器的日志，包括访问和错误日志。 |
| `/var/log/glassfish/` | 记录GlassFish应用服务器的日志，包括访问和错误日志。 |
| `/var/log/maillog` | 记录邮件传输代理（MTA）的日志，包括邮件传输信息。 |
| `/var/log/mail.err` | 记录邮件传输代理（MTA）的错误日志。 |
| `/var...