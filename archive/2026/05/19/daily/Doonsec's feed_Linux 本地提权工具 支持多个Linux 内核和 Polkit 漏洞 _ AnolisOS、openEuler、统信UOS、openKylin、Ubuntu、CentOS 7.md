---
title: Linux 本地提权工具 支持多个Linux 内核和 Polkit 漏洞 | AnolisOS、openEuler、统信UOS、openKylin、Ubuntu、CentOS 7
url: https://mp.weixin.qq.com/s/vHLjBK2608i_L1wzS_U59Q
source: Doonsec's feed
date: 2026-05-19
fetch_date: 2026-05-20T06:01:11.516143
---

# Linux 本地提权工具 支持多个Linux 内核和 Polkit 漏洞 | AnolisOS、openEuler、统信UOS、openKylin、Ubuntu、CentOS 7

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/TVljsu2eAicIpGvBmsNOUVrZNE7kfz39P5YFYgYYZGHzicXfQrPS09NSeXMlyicYjf7KtlicknP7Ry6ut8J9ia3jmxF0VGZCWicg7Ln5j2EGKmd4g/0?wx_fmt=jpeg)

# Linux 本地提权工具 支持多个Linux 内核和 Polkit 漏洞 | AnolisOS、openEuler、统信UOS、openKylin、Ubuntu、CentOS 7

Hacking黑白红

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 工具介绍

RootHawk 是一个**用于授权安全测试**的 Linux 本地提权工具。它整合了多个已公开的 Linux 内核和 Polkit 漏洞，目的是在**可控环境**（虚拟机、实验环境、授权目标机器）中验证系统是否存在提权风险。

```
https://github.com/RoadBicycle-C/RootHawk
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNW7OkAygDNUfEUDLNj2z33Ucj4un3SL27XE9CPuCUxOPbVAAmMPRibYb9fQPWJfqJtnQekO2qvSDBYczOj6E4ooq2fhY9E3YkFo/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic&watermark=1#imgIndex=0)

## 支持的主要漏洞（CVE）

| CVE 编号 | 常见名称/别名 | 漏洞类型/组件 |
| --- | --- | --- |
| CVE-2026-31431 | Copy Fail | Linux Kernel 本地提权，涉及 crypto / AF\_ALG / algif\_aead 相关逻辑问题。 |
| CVE-2026-43284 | Dirty Frag，也有人叫 CopyFail2 | Linux Kernel 本地提权，涉及 xfrm/esp、shared skb frags 等内核网络/数据包处理路径。 |
| CVE-2021-4034 | PwnKit | Polkit 的 pkexec 本地提权漏洞。 |
| CVE-2021-3560 | Polkit D-Bus 权限绕过 / Polkit Authentication Bypass | Polkit 本地提权，可通过 D-Bus 请求绕过凭据检查，提升权限；没有像 PwnKit 那样特别统一的短名字。 |
| CVE-2022-0847 | Dirty Pipe | Linux Kernel 本地提权，管道机制相关漏洞。 |

工具采用**模块化设计**，每个 CVE 都有独立实现，可以单独运行或一次性尝试所有模块。

## 主要功能特点

* 支持命令行参数快速调用特定 CVE（`-e CVE-XXXX-XXXX`）
* 支持一键运行所有可用漏洞（`-any`）
* 可列出所有可用模块（`-list`）
* 支持自定义参数（如 pkexec 路径、备份 su、后渗透执行命令等）
* 提供详细日志输出（`-v`）
* 预编译二进制文件（支持 amd64、arm64、386 架构）
* 已在多个国产系统上测试通过：

+ AnolisOS
+ openEuler
+ 统信 UOS（统信桌面操作系统）
+ openKylin（开放麒麟）
+ Ubuntu、CentOS 7 等

## 工具测试

| 序号 | 操作系统 | 测试漏洞 | 测试结果 | 说明 |
| --- | --- | --- | --- | --- |
| 1 | AnolisOS | CVE-2026-31431 / Copy Fail | ✅ 成功 | 工具在该系统环境下测试通过 |
| 2 | openEuler | CVE-2026-31431 / Copy Fail | ✅ 成功 | 工具在该系统环境下测试通过 |
| 3 | 统信 UOS | CVE-2026-31431 / Copy Fail | ✅ 成功 | 工具在该系统环境下测试通过 |
| 4 | openKylin | CVE-2026-31431 / Copy Fail | ✅ 成功 | 工具在该系统环境下测试通过 |
| 5 | Ubuntu | CVE-2026-31431 / Copy Fail | ✅ 成功 | 工具在该系统环境下测试通过 |
| 6 | CentOS 7 | CVE-2021-4034 / PwnKit | ✅ 成功 | 工具在该系统环境下测试通过 |

### 信创系统openEuler

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ft6csZH0gNWxKIHP3myIia8c4fQpBTJrjd5uxgjaWEO9aZUvZHTy6kERxhn38IBZteEnOM2uoCoibTEHkkWIzP9vjms0VPqMATaFOpaGiaicSgo/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=1)

### DirtyFrag

```
./RootHawk-amd64 -e CVE-2026-43284
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNX1kFBJhPwGrtN9T9ZS6h6Ala4Sjwy2UacgkemkBwNgKGlmnJib4Ya5Eg7r18ethvNWRQ6jfLm87O1cUxOJiarB50zys8cVNJOqU/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=2)

# CopyFai

```
./RootHawk-amd64 -e CVE-2026-31431
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNVHCDNpUicHkiabcPOYtMQlj7rYOqORe52aSTpzeQW3tCJKZyZ0umt02e49icB1icFg33CDHnnzD3lX0wicPKSXGJ2YHC4USSJEIwWs/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=3)

# CVE-2021-4034

```
./RootHawk-amd64 -e CVE-2026-4034
```

![图片](https://mmbiz.qpic.cn/mmbiz_png/ft6csZH0gNW13BGBIbFpUxq03vkPiaeSePpNicxdHuLO9qhRmszVJjQr6HAtv5QMYAp5n3aZg1Szl7xqdltPAYXBFlbGKxhGgY9qFZu9oLeG8/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&watermark=1#imgIndex=4)

## 工具使用

### 已编译版本

```
bin/RootHawk-amd64
bin/RootHawk-arm64
bin/RootHawk-386
```

Ubuntu amd64 虚拟机使用：

```
chmod +x RootHawk-amd64
./RootHawk-amd64 -help
```

查看帮助：

```
./RootHawk-amd64 -help
```

查看模块列表：

```
./RootHawk-amd64 -list
```

执行指定 CVE：

```
./RootHawk-amd64 -e CVE-2022-0847
```

按顺序执行全部模块：

```
./RootHawk-amd64 -any
```

### 参数说明

```
-list              显示当前集成的 CVE 模块
-e <名称>          执行指定 CVE 或别名
-any               按列表顺序执行全部模块
-pk <路径>         指定 CVE-2021-4034 使用的 pkexec 路径，默认 /usr/bin/pkexec
-backup <路径>     CVE-2026-31431 执行前备份 su 到指定路径
-exec <路径>       CVE-2026-31431 提权后执行指定程序，而不是进入 su
-v                 尽量输出详细日志
-help              显示帮助
```

### 示例

```
./RootHawk-amd64 -list
./RootHawk-amd64 -e CVE-2021-4034
./RootHawk-amd64 -e CVE-2021-4034 -pk /usr/bin/pkexec
./RootHawk-amd64 -e CVE-2026-31431 -backup /tmp/su.bak
./RootHawk-amd64 -e CVE-2026-31431 -backup /tmp/su.bak -exec /tmp/root-task
./RootHawk-amd64 -e CVE-2026-43284 -v
./RootHawk-amd64 -any
```

## 总结

RootHawk 是一个**比较新的、专注 Linux 本地提权**的开源安全测试工具，集成了多个真实 CVE。它适合有一定 Linux 和安全基础的用户在实验环境中学习和验证提权技术。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/rf8EhNshONTk9JHJcRia5QdqxUfpBz4cb5VGKUIUyrVaviawse20DccoB4C6WKwxm6xVzq4oU7dSdfxryTMc9Vvg/0?wx_fmt=png)

Hacking黑白红

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