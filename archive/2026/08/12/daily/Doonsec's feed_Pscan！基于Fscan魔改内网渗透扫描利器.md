---
title: Pscan！基于Fscan魔改内网渗透扫描利器
url: https://mp.weixin.qq.com/s/kPQ6Wdr3ou6zar6Dlgep5w
source: Doonsec's feed
date: 2026-08-12
fetch_date: 2026-08-13T04:03:23.286883
---

# Pscan！基于Fscan魔改内网渗透扫描利器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/nGzNudUIJ6NulEicoqiaO0uaXLorFOicU3VPTST696Gw5KicqrgAgnnWnasboPNlSJR4W99qEffBg519N9ibcRvgTsQxYlf4DKI51cOjlppMUoSs/0?wx_fmt=jpeg)

# Pscan！基于Fscan魔改内网渗透扫描利器

黑白之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 0x01 工具介绍

在实际红队作战或内网渗透项目中，fscan 是很多安全研究人员的常用工具，但其原始特征过于明显，容易被 HIDS（主机入侵检测系统）识别拦截。

本文介绍的 pscan 是基于 fscan v2.2.0-rc 的魔改版本，针对红队场景做了参数混淆与特征规避处理，在保留原版全部功能的基础上，提升了实战中的存活率。主要更改内容：

```
参数名全面混淆：所有命令行参数重新命名，避免被基于参数特征的检测规则识别。Banner静默：启动时不再输出 fscan 的 ASCII Logo 和版本信息，减少落地特征。模块路径重命名：Go 模块路径改为 scanner/core，去除项目名特征。两个预编译版本：pscan.exe（标准版）和 core.exe（备用版）。
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/Nuuibh3bDOw6M8Ge9zJWACpwkgZOJr2yo8ql34tsWhicAEic8iaFNxNtXS5aY0wm3qTyCcxCkrRvYR2lWeEsXgMe7eiclolxWgMlvWW60I75Z0k8/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1)

## 0x02 工具使用

常用命令：

```
# 扫描一个 C 段（存活探测 + 端口扫描 + 服务识别 + 弱口令爆破 + POC）pscan.exe -t 192.168.1.0/24
# 仅存活探测pscan.exe -t 192.168.1.0/24 -ao
# 扫描单个主机pscan.exe -t 192.168.1.100
# 扫描多个 IP 段pscan.exe -t 192.168.1.0/24,10.0.0.0/24
# 从文件读取目标pscan.exe -tf targets.txt
```

内网扫描：

```
# 全量扫描整个 C 段（最常用）pscan.exe -t 192.168.1.0/24
# 仅存活探测（快速定位在线主机）pscan.exe -t 192.168.1.0/24 -ao
# ICMP 模式存活探测pscan.exe -t 192.168.1.0/24 -st icmp
# 存活探测 + 仅在线主机做端口扫描（跳过离线主机）pscan.exe -t 192.168.1.0/24 -ao -st all
# 扫描多个网段pscan.exe -t 192.168.1.0/24,10.10.0.0/16
# 扫描 IP 范围pscan.exe -t 192.168.1.1-100
# 排除特定主机pscan.exe -t 192.168.1.0/24 -et 192.168.1.1,192.168.1.254
# 从文件读取目标列表pscan.exe -tf targets.txt
```

POC漏洞检测

```
# 全量扫描 + POC 检测（默认开启）pscan.exe -t 192.168.1.0/24
# 禁用 POC 扫描（加快速度）pscan.exe -t 192.168.1.0/24 -nopoc
# 全量 POC 扫描（更全面但更慢）pscan.exe -t 192.168.1.0/24 -full
# 指定 POC 名称pscan.exe -t 192.168.1.100 -pocname thinkphp
# 自定义 POC 脚本目录pscan.exe -t 192.168.1.100 -pocpath ./custom-pocs/
# 调整 POC 并发数pscan.exe -t 192.168.1.0/24 -num 10
# 启用 DNSLogpscan.exe -t 192.168.1.0/24 -dns
```

**后渗透插件**

通过 `-local` 参数调用：

```
# 列出所有本地插件pscan.exe -local list
# 使用特定插件pscan.exe -local systeminfo
```

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

## 0x03 工具下载

https://github.com/webzzaa/pscan

文章来源：无影安全实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/3xxicXNlTXLicpdp8GZxicJpcFIZglvakzYRZiaqt6W61hfgibjeymOgiaGqRsgNvgWIacMj7Gk4PIZ4o2NtW1zb9P6Q/0?wx_fmt=png)

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