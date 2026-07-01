---
title: Brutus - 从一次 SSH 爆破，看 auth.log 与 wtmp 取证之美
url: https://mp.weixin.qq.com/s/C-IoIgsMYj4xTnRKpUh-sw
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:20:01.565959
---

# Brutus - 从一次 SSH 爆破，看 auth.log 与 wtmp 取证之美

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/SQGvsuoDbxicWE2dlrKgicQgR2icxPEwPSCVMI6DQtSvD4MibDMONxF1EwHFy8xbyicAkDIra5yFzicPkkJTUIrHUicSv30hThY8JGWSCZNGZj3Jfc/0?wx_fmt=jpeg)

# Brutus - 从一次 SSH 爆破，看 auth.log 与 wtmp 取证之美

原创

漫路修行
漫路修行

微痕鉴远

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SQGvsuoDbxicgWk1SqvicFNHl2qYibiawBMd7yhQcoPaiaHCGbLYWKjTGGexyce5P9gXqruySjreEVL5uhN5PiaGGZW9oMdnzUHd9xb82jbcKaK4c/640?wx_fmt=png&from=appmsg)

> 当攻击者通过 SSH 暴力破解进入一台 Confluence 服务器，我们能从系统日志里挖出多少秘密？本文带你用 `auth.log` 与 `wtmp` 两件"老兵器"，还原一场真实的入侵链：爆破 → 登录 → 持久化，再到精确计算攻击者的会话时长。

---

## 0x00 题目背景

题目只给了我们两份"原料"：

![](https://mmbiz.qpic.cn/mmbiz_png/SQGvsuoDbxicdUVh0FVDANS5sA2hZcLMLfmQFbcrqvibnKomibtpkuXTotuXk8cA8a2A1DFh3xanibk5tx5WC9Bw242uv86EbSXBJnTicHDHNFuE/640?wx_fmt=png&from=appmsg)

* `auth.log`：Linux 认证日志，记录 SSH 登录成败、会话创建、命令执行等
* `wtmp`：二进制登录记录文件，记录用户的登录/登出历史

> In this very easy Sherlock, you will familiarize yourself with Unix auth.log and wtmp logs. We'll explore a scenario where a Confluence server was brute-forced via its SSH service. After gaining access to the server, the attacker performed additional activities, which we can track using auth.log. Although auth.log is primarily used for brute-force analysis, we will delve into the full potential of this artifact in our investigation, including aspects of privilege escalation, persistence, and even some visibility into command execution.

虽然难度标签是"very easy"，但 auth.log 的取证价值远不止"看看爆破"那么简单。它几乎覆盖了入侵生命周期的每一个阶段：**提权、持久化，甚至部分命令执行的痕迹**，都能在其中找到蛛丝马迹。

下面我们按"攻击时间线"逐层拆解。

---

## 0x01 第一步：定位爆破尝试

攻击从哪开始？当然是那一长串的 `Failed password`。

我们在 `auth.log` 里搜索失败登录记录：

```
Failed password.*
```

![](https://mmbiz.qpic.cn/mmbiz_png/SQGvsuoDbx8iczvM6RdDbbJZ2GvWsEk5JoOa5eE9Sk0SzhLNEwCeeUicVlGuUHzBkefzsdThJ8CE75pdvYQwMJZ1braTmYBjBiaia103Nrca3UU/640?wx_fmt=png&from=appmsg)

可以看到日志里密密麻麻的认证失败记录，配合 `MaxStartups throttling`（连接节流）的告警，这是一次典型的字典/暴力破解。从 IP 和节奏基本能判定：攻击者使用了自动化脚本，对多个用户名（如 `backup`、`root` 等）进行高频尝试。

> 💡 **小贴士**：`sshd` 在并发连接过多时会触发 `MaxStartups` 限流并主动丢弃连接，日志里那句 `exited MaxStartups throttling after ...` 往往就是大规模爆破的"指纹"。

---

## 0x02 第二步：抓住那次"成功登录"

爆破的终点，是一次成功认证。把搜索条件换成成功登录：

```
Accepted password for root from
```

![](https://mmbiz.qpic.cn/mmbiz_png/SQGvsuoDbxibqziacNcopCWXibXealHnygGeCzpMRqyqfPlialCYThqojRfQzwfUYdA2SHmLQT5pgOkjRETk9jF7fxEvoGhzxQCdxYLk9rc6GcE/640?wx_fmt=png&from=appmsg)

可以看到，攻击者最终以 **root** 身份成功登录。这也意味着——服务器的大门被踹开了，后续的所有动作都属于"入侵后活动"。

---

## 0x03 第三步：找到攻击者的会话编号

> **Q1：** SSH 登录会话在建立时会被分配一个 session number。攻击者从 root 账户登录时被分配的会话编号是多少？

在 `auth.log` 中搜索新会话的创建记录：

```
New Session
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SQGvsuoDbxibOURQiaCsPD1AMEXmerNb8ucM1TznhFwKxZ6sHh0cJMv2iaEJuwWBt9vd506HkBymibcyMibU0QibnYEURennNtPkjVPFUPmUPKlLE/640?wx_fmt=png&from=appmsg)

定位到攻击者这次成功登录对应的记录后，可以读出：

> **答案：session 37**

这个编号在后续追踪中很关键——它会贯穿攻击者整条会话生命周期的日志条目。

---

## 0x04 第四步：还原手动登录的时间戳

> **Q2：** 攻击者手动登录服务器、开始实施目标的精确时间戳是什么？

这一问要从 `wtmp` 文件入手。`wtmp` 是二进制格式，不能直接 `cat`，得借助专门的工具解析。这里用到的是经典命令 `last`。

先科普一下 `last` 输出的每一列含义（每一列都很关键）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SQGvsuoDbxibH29mCBUa5g4uBFyJQBlMUqSPfkic85w3kUv2zX7EhXsgD6tJ6Hho2QSrzf7jYy8yPBgTLCq8HibQsO0qbcIMM1LVQianbRneJlA/640?wx_fmt=png&from=appmsg)

* **第一列**：用户名
* **第二列**：终端位置

+ `pts/*`：来自 SSH / Telnet 的远程连接
+ `tty*`：本地直接连接

* **第三列**：登录 IP 或内核（`0.0` 或为空表示本地登录；重启活动会显示内核版本）
* **第四列**：登录开始时间
* **第五列**：登录结束时间（`still logged in` 仍在登录；`down` 直到正常关机；`crash` 直到强制关机）
* **第六列**：持续时长

`last` 的常用参数也顺手记下：

![](https://mmbiz.qpic.cn/mmbiz_png/SQGvsuoDbxib8UU8QDQsu3cDzsTr5hbpd4nZgWjSLqhsApUp1icib8aUtiatmVs23E8mUoRyeCyTcjHQErMQpHT9NBAC1fxP6NUVV4ryZS8I4sQ/640?wx_fmt=png&from=appmsg)

```
last [-adRx] [-f 记录文件] [-n 显示列数]    -a   把登录主机名/IP 显示在最后一列    -d   将 IP 反解为主机名    -x   显示系统关机、登录与登出的历史    -f   指定记录文件（默认来自 /var/log/wtmp）
```

于是我们用以下几条命令解析题目给的 `wtmp`：

```
last -a -x -F -f wtmplast -a -d -x -F -f wtmpwho -T -H ./wtmp
```

![](https://mmbiz.qpic.cn/mmbiz_png/SQGvsuoDbx9ica1LicAuGwIkXZ1EtnY4aqwe0PKKz8zBpTjPtz1BEAu1OEslYcic7OIFICzFziceA731zopkHAuQ404eG9RG6WySaUXiabzj6DNk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/SQGvsuoDbxicHhYrSl4vPkpsanv7YInpwR8unBkTYx6iaOP06JuYPrf696L6HkAJiakichibqCvZo4H6qUGLvEyGibxoKCJVgnCGgpicjXTXAGWd7k/640?wx_fmt=png&from=appmsg)

从输出可以清晰看到攻击者（`65.2.161.68`）以 root 登录的那条记录：

```
root  pts/1  Wed Mar 6 01:32:45 2024 - Wed Mar 6 01:37:24 2024  (00:04)  65.2.161.68
```

> **答案：`2024-03-06 06:32:45`**（UTC 时间）

⚠️ **重要提醒：注意时区差异！**

这里有一个非常容易踩坑的地方：日志记录的其实是 **UTC 时间**（`06:32:45`），而你在自己机器上用 `last` 解析 `wtmp` 时，显示的时间（`01:32:45`）会被你本机时区"翻译"一遍。**目标机器的时区和你本机的时区并不一样**，所以务必搞清楚题目要的是哪一个时区下的时间，否则就会差出整整几个小时。

---

## 0x05 第五步：精确计算会话持续时长

> **Q3：** 基于前面确认的认证时间，以及 auth.log 中会话 37 的结束时间，攻击者的首次 SSH 会话持续了多少秒？

会话的结束记录同样藏在 `auth.log` 里：

![](https://mmbiz.qpic.cn/mmbiz_png/SQGvsuoDbxic4sic42mPu3Uhgof9DaH9QZqjUtW92dTX9tc5eQPcWUKRibjqhO831YAwqa1XTdw8MRick5y3ctI8fJIEiaLlN0NAghQy7Abjayo0/640?wx_fmt=png&from=appmsg)

时间轴对齐后：

* 会话开始（wtmp）：`06:32:45`
* 会话结束（auth.log）：`06:37:24`

做一个简单的减法：

```
37:24 - 32:45
```

```

```

用 Python 算一下（把分秒换算成纯秒）：

```
python -c 'print(eval("(7 * 60 + 24) - (2 * 60 + 45)"))'
```

![](https://mmbiz.qpic.cn/mmbiz_png/SQGvsuoDbx8gXxUbFmamHgS0VywakyPnibqJCDia9Iqkhyys2xo6XdFgyJTiav5v6hZR0VOYWlibu5RGcczKSh9ETkWibyFGCsiajUdicicG5OFoerk/640?wx_fmt=png&from=appmsg)

> **答案：`279` 秒**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SQGvsuoDbxicxRB4S0iaJuwosruIcLBub83B2zbMdAVlea9lv8vlXzDLAvodIKhwXpu8ibkMjSnpXvVI4K9hfybTvBicqn2ibaSScyeqGttE6c10/640?wx_fmt=png&from=appmsg)

```
python -c 'print(eval("(7 * 60 + 24) - (2 * 60 + 44)"))'
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/SQGvsuoDbxicQQdtdt0ciaDWWWQSMPnSnJNhg2KZoKztDoEHiamHIp90gmoP54rQDvy7k1G5rtEspVtNfSzSic5pkUtsSBvhFqibE50DH93zTdbQ/640?wx_fmt=png&from=appmsg)

也就是说，攻击者这次 root 会话只持续了不到 **5 分钟**。在这短短几分钟里，他已经完成了登录、执行目标操作、登出的全过程——对于熟练的攻击者而言，这点时间已经足够造成破坏。

---

## 0x06 复盘：两条日志，一条完整的入侵链

回顾整个挑战，我们用到的工具不过是 `grep` 思路 + `last` 命令，却把攻击者的行为链拼出了清晰的轮廓：

| 阶段 | 日志痕迹 | 关键证据 |
| --- | --- | --- |
| 爆破 | `Failed password` + `MaxStartups throttling` | 大量失败认证 |
| 登录 | `Accepted password for root` | 攻击者成功以 root 进入 |
| 会话 | `New Session` | 会话编号 **37** |
| 行为 | `wtmp` + `last` | 登录时间 `06:32:45`，IP `65.2.161.68` |
| 离场 | 会话结束记录 | 时长 **279 秒** |

几个值得带走的实战经验：

1. **`auth.log` 是 Linux 取证的金矿**：爆破、登录、提权、持久化、命令执行，几乎都能在这里找到回响。
2. **`wtmp` 配合 `last` 是查看登录史的标准姿势**：二进制日志必须用专门工具解析，直接 `cat` 会得到乱码。
3. **永远警惕时区陷阱**：日志里写的是 UTC，本机解析时会按本机时区换算，答题和写报告时务必统一口径。
4. **善用 `-x -F -a` 等参数**：它们能让 `last` 的输出信息更完整、时间戳更精确，避免遗漏关键细节。

---

## 0x07 写在最后

Brutus 虽然被标为 very easy，但它把"日志取证"这套基本功讲得非常扎实。真实事件响应里，攻击者不会留下"我被爆破啦"的提示语，**所有真相都藏在 auth.log 和 wtmp 这种不起眼的日志文件里**。能把这两类日志读熟、读透，是每个蓝队/取证人员的基本功。

> **相关阅读**：`last` 命令详解可参考 Linux迷 (linuxmi.com)

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/cSZq3JiaYf9OiakFicRXS9aR9GCECbu4Z6vewLpRbydMLRZlHOaz1I2icK3ohbWCCJTSIBQaDj29a9c8fiayibhX4BEQ/0?wx_fmt=png)

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