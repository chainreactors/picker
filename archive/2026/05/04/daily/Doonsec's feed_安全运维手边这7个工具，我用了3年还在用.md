---
title: 安全运维手边这7个工具，我用了3年还在用
url: https://mp.weixin.qq.com/s/a1Jccju-_YANcypKalotwA
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T05:00:00.702302
---

# 安全运维手边这7个工具，我用了3年还在用

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/yJLbez93fl8w2sRYcg8az1Np22sickQcPfwDHbJv8c5yvzOxIuJImZpyibDXfkSQUcYEAiajPgmnlIUf2CciaA6bq7LLPH5r6OtnIW3RRt7EFic8/0?wx_fmt=jpeg)

# 安全运维手边这7个工具，我用了3年还在用

老宋
老宋

网络安全老宋

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**导语：** 你好，我是老宋。关注我，安全攻防干货第一时间送达！

文章较长，全是干货，建议先收藏再点赞

上周有个朋友问我："老宋，你们安全运维平时用什么工具？"

我想了想，发现有好的，我自己又有收藏的癖好，但真正天天在用、离了就难受的，其实就那几个。

不是什么高端武器，都是免费的、开源的。但它们解决的问题很实际：**扫资产、抓日志、查弱口令、看流量、跑应急。**

今天整理出来，照着这份清单装一遍，绝大多数日常运维场景够用了。但是装了之后得用啊，需要花点时间来学习，大都比较简单，自从有了AI，连命令都不用自己查表或者拼写来。

![](https://mmbiz.qpic.cn/mmbiz_png/yJLbez93fliblsCiciaNJdS1n6R7n0eAUb4TQrHGDGjkHkPZXkic87SenuM93rPHMVt71y5AasQ4O1olMArGAEXgLxeVBz7g7toLN8VVFAnWqQI/640?wx_fmt=png&from=appmsg)

## 先说场景：你会碰到哪几类问题

安全运维的活，无非四类：

| 场景 | 问题 | 没工具的状态 |
| --- | --- | --- |
| **资产不清楚** | 内网有哪些服务在跑？有没有没人管的端口？ | 全靠记忆，一出事两眼一摸黑 |
| **日志看不过来** | 几百MB日志，凌晨3点告警，从哪查起？ | 手动 grep，一行一行翻 |
| **弱口令不知道** | 账号密码是不是太简单？有没有默认口令没改？ | 出事之前永远不知道 |
| **应急不会抓** | 主机行为异常，流量在哪？进程在干嘛？ | 凭感觉，手忙脚乱 |

下面7个工具，覆盖这4类场景，逐个说。

---

## 🔍 资产发现

### 1. Nmap — 端口扫描的祖宗

**用来干什么**：内网主机发现 + 端口服务识别

说实话，Nmap 在安全圈的地位就像运维圈的 ping。没用过的人反而少见。

快速扫一台主机，看它跑了哪些服务：

```
# 扫常见端口，顺便识别服务版本
nmap -sV -p 22,80,443,3306,6379 192.168.1.100

# 扫整个网段存活主机
nmap -sn 192.168.1.0/24
```

> ⚠️ 注意：生产环境扫之前和业务方打招呼，nmap 强度开大了会触发 IDS 告警，甚至影响服务响应。

**下载**：https://nmap.org ⭐⭐⭐⭐⭐

虽然它很老啦，有很多同类的竞品，但是每当要做渗透测试的时候，都会把它拿出来使用。

---

### 2. Masscan — 大规模扫描用它

**用来干什么**：万台级别的资产扫描，比 Nmap 快 100 倍

Nmap 扫几十台没问题，扫一万台就慢得要命。Masscan 专门解决这个问题，比 Nmap 快很多。

```
# 扫 B 段内网的 80 和 443
masscan 10.0.0.0/16 -p80,443 --rate=1000
```

> ⚠️ 注意：rate 不要开太高，容易打垮交换机。生产环境建议 rate ≤ 1000。

**适合场景**：等保项目摸底、新接手的客户资产盘点

**下载**：https://github.com/robertdavidgraham/masscan ⭐⭐⭐⭐

别的不多说，就是快，配合Nmap，效率刚刚的，能串联工作流，省出喝水抽烟上厕所的时间，😅

---

## 📋 日志分析

### 3. LogX — Web 日志的威胁检测神器

**用来干什么**：批量分析 Web 日志，自动识别 SQL 注入、XSS、扫描行为

这个工具今年才火起来，Go + Vue3 开发，支持百万级日志快速解析。

最实用的地方：不用写规则，自动标记可疑请求，还能出可视化报告。

```
# 拉取并启动（需要 Docker）
docker pull nbyiansec/logx:latest
docker run -d -p 8080:8080 nbyiansec/logx:latest
```

打开浏览器访问 http://localhost:8080，把 access.log 上传上去，10 秒出结果。

**适合场景**：应急响应时快速排查攻击路径、等保渗透测试后的日志核查

**GitHub**：搜索 LogX-web ⭐⭐⭐⭐

虽然工具好用，但是不少应用是部署在Linux上的，所以grep命令也要熟练的令人惊叹才行。

---

## 🔐 弱口令检测

### 4. Hydra — 弱口令爆破测试标配

**用来干什么**：测试 SSH、RDP、FTP、MySQL 等服务有没有弱口令

先说清楚：这是用来**测自己系统**的，不是用来攻击别人的。

很多企业的内网服务，密码还是 admin/123456。Hydra 跑一遍，出问题之前就能发现。

```
# 测试 SSH 弱口令
hydra -l root -P /usr/share/wordlists/rockyou.txt ssh://192.168.1.100

# 批量测试多个 IP
hydra -L users.txt -P pass.txt -M targets.txt ssh
```

> ⚠️ 注意：测之前要有书面授权。没有授权的系统不能测，不是建议，是法律要求。

**下载**：`apt install hydra` 或 `brew install hydra` ⭐⭐⭐⭐⭐

准备好弱口令的密码本，剩下的交给时间，因为唯有时间不会辜负你。

---

### 5. 安全运维工具箱（SSKit）

**用来干什么**：资产管理 + 弱口令检测 + 配置核查一体化

这个是国内团队做的，比较适合甲方安全运维的日常。功能集成度高，不用到处找工具：

* 批量资产扫描
* 弱口令批量检测（SSH / RDP / MySQL / Redis）
* 配置基线核查（CIS 标准）
* 漏洞跟踪和报告输出

不是 CLI 工具，有 Web 界面，比较适合给领导看报告时用。

**项目地址**：https://gitee.com/nbyiansec/sskit ⭐⭐⭐⭐

这个就是图省事，不用一个一个的切换工具，方便好用就是棒。

---

## 🌐 流量分析

### 6. Wireshark — 抓包分析，绕不过去

**用来干什么**：实时抓包 + 离线 pcap 分析

应急响应时发现主机有异常外连，第一步就是抓包。Wireshark 是这个场景的标配，没有之一。

几个常用过滤器，直接抄：

```
# 只看 HTTP 请求
http.request

# 看某个 IP 的所有流量
ip.addr == 192.168.1.100

# 抓 DNS 请求，看有没有可疑域名
dns

# 找大流量连接（数据外传场景）
tcp.len > 1000
```

**下载**：https://www.wireshark.org ⭐⭐⭐⭐⭐

这个跟Nmap一样，在自己的赛道里几乎没有对手；但是它有一个对手叫科来

---

## 🔧 应急响应

### 7. Sysinternals Suite（Windows）/ auditd（Linux）

**用来干什么**：排查主机异常行为，找恶意进程和文件

**Windows 应急**用 Sysinternals，微软官方出品，免费，几乎是事件响应的必备。

重点用这三个：

| 工具 | 用途 |
| --- | --- |
| Process Explorer | 看进程树，找异常父子关系 |
| Autoruns | 看开机自启项，找持久化后门 |
| TCPView | 实时看网络连接，找异常外连 |

```
# 下载整包
# https://learn.microsoft.com/zh-cn/sysinternals/downloads/sysinternals-suite
# 解压直接运行，不需要安装
```

**Linux 应急**用 auditd，系统级别的操作审计，记录文件访问、命令执行、网络连接：

```
# 安装
apt install auditd

# 查看最近的可疑命令执行
ausearch -m execve -ts recent | grep -v audit

# 查看文件访问记录
auditctl -w /etc/passwd -p rwxa -k passwd_changes
```

**下载**：Sysinternals Suite — https://learn.microsoft.com/zh-cn/sysinternals ⭐⭐⭐⭐⭐

这个可以多试几个，找出适合自己或者是适合公司流程的工具

---

## 速查表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/yJLbez93flicicZMdgYuMnBpxPUfia0AXSOMwOIWp6Yw2VsgYH1jMnrKHwc5cwsWF3BYTXbw1yKcZibF6DXoCicMKh143oibTmhhn9ddXicRZnCCRs/640?wx_fmt=png&from=appmsg)

| 工具 | 用途 | 系统 | 费用 | 推荐指数 |
| --- | --- | --- | --- | --- |
| **Nmap** | 端口扫描/服务识别 | 全平台 | 免费 | ⭐⭐⭐⭐⭐ |
| **Masscan** | 大规模快速扫描 | Linux/macOS | 免费 | ⭐⭐⭐⭐ |
| **LogX** | Web日志威胁检测 | Docker | 免费 | ⭐⭐⭐⭐ |
| **Hydra** | 弱口令爆破测试 | 全平台 | 免费 | ⭐⭐⭐⭐⭐ |
| **SSKit 安全运维工具箱** | 资产+弱口令+基线一体 | Web界面 | 免费 | ⭐⭐⭐⭐ |
| **Wireshark** | 流量抓包分析 | 全平台 | 免费 | ⭐⭐⭐⭐⭐ |
| **Sysinternals / auditd** | 主机应急响应 | Win/Linux | 免费 | ⭐⭐⭐⭐⭐ |

---

## 选哪个？按你的场景来

| 你的情况 | 推荐 | 理由 |
| --- | --- | --- |
| 接手新客户，不知道有哪些资产 | Nmap + Masscan | 先把资产摸清楚 |
| 等保测评前自查 | SSKit + Hydra | 弱口令和基线一起过 |
| 网站被打，要溯源 | LogX + Wireshark | 日志+流量两路并行 |
| Windows 主机疑似被入侵 | Sysinternals Suite | 进程树+自启项+网络连接 |
| Linux 主机行为审计 | auditd | 系统级审计，证据链完整 |

---

## 老宋说

这7个工具，没有一个是花钱的，全部免费开源。

但我见过很多运维，出事了才知道要装这些，装上了又不会用。

工具不是装了就有用，是**平时练了才有用**。应急响应那种时候，你不可能边查文档边排查，必须手熟。

建议找一台测试机，把这7个工具都过一遍。Nmap 扫一下自己，Wireshark 抓几分钟包看看，LogX 跑一下自己的 access.log。

命令不会用，可以让市面上的AI来帮你，给你生成几个常见典型的案例，你来照着做，熟练熟练就好了。

等真出事的时候，你会感谢现在这10分钟的练习。

---

🔐 我是网络安全老宋

专注把安全威胁翻译成你听得懂的实操建议。每周推送漏洞预警、工具测评、攻防笔记。

觉得有用，点个在看，转发给你身边的朋友，就是对我最大的支持。

我们下期见 👋

---

*参考来源：gitee.com/nbyiansec/sskit、learn.microsoft.com/sysinternals、nmap.org，数据截至 2026 年 4 月*

---

### 往期精彩

[多地爆发 “银狐” 病毒，办公场景成重灾区，这些防范要点必看](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247485491&idx=1&sn=5fab6c9c4aca7533ae7531b1ad454954&scene=21#wechat_redirect)

[红队视角下的暴露面攻防：如何从一个弱点撕开企业防线？](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247485563&idx=1&sn=7d1d12904a8d700714b52aef2f4262f1&scene=21#wechat_redirect)

[实战视角下的云平台安全：从攻击路径到防御体系的全景解析](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247485552&idx=1&sn=5160d3927b73bbb4006d965bddc73159&scene=21#wechat_redirect)

[终端攻防全链路解析：红队如何从一台电脑拿下整个内网？](https://mp.weixin.qq.com/s?__biz=MzAxMzIxMjM3Ng==&mid=2247485454&idx=1&sn=6fe621fb3b423279921144cf24eb73c0&scene=21#wechat_redirect)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

网络安全老宋

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sowcUpcXRY07WiafrWPnt0icqSjEOPqweHgqfN5sMGTgMPP5yciaeNiaPx8oJtcS4I6dCcBUL6q4JOY9jNalwkxmZQ/0?wx_fmt=png)

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