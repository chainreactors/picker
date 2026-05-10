---
title: 等保测评命令——Kylin Linux
url: https://mp.weixin.qq.com/s/a22nuatdG8XbD4Rnoa017A
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:32:26.978250
---

# 等保测评命令——Kylin Linux

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JJfExzHZwzFxqjukLVKdYxClmUicSAr2gJLIia1WGag7MNicfM2J1zibuXg5drCtBykiazq2N5zQWZOE7YflB3eic5Mg6suNlGpKFXyH0UnleH2ME/0?wx_fmt=jpeg)

# 等保测评命令——Kylin Linux

Sec Online

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于汪汪虚拟空间
，作者初恋是小马

![](http://wx.qlogo.cn/mmhead/ibkKkoaQFco6tfIIq0gLqqv5a4nPiawT7sTia17cAoV5PMialOoAaWjZmUkGGYaR1EibW0qAX5StwTXU/0)

**汪汪虚拟空间**
.

汪汪·虚拟空间｜专注学习分享这里有计算机、数学、英语等干货笔记愿你在这里，找到需要的知识，遇见更好的自己

依据 **GB/T 22239-2019《信息安全技术 网络安全等级保护基本要求》等保2.0三级** 标准，针对 **Kylin Linux（银河麒麟）操作系统** 给出可直接落地的测评命令清单。

覆盖身份鉴别、访问控制、安全审计、入侵防范、恶意代码防范等核心控制点，并结合 **Kylin V10 特有安全增强机制**（如 AppArmor、可信计算、国密支持）进行优化调整。

---

## 一、身份鉴别（8.1.4.1）

### 1.1 账户唯一性与密码复杂度

| 测评命令 | 功能说明 | 达标判据 |
| --- | --- | --- |
| `awk -F: '$2==""{print $1}' /etc/shadow` | 检查空口令账户 | 无输出 |
| `awk -F: '{print $3}' /etc/passwd | sort | uniq -d` | 核查UID唯一性 | 无重复UID（普通用户UID≥1000） |
| `grep -E 'PASS_MAX_DAYS|PASS_MIN_DAYS' /etc/login.defs` | 查看密码有效期 | ≤90天，≥1天 |
| `grep -E 'pam_cracklib|pam_pwquality' /etc/pam.d/system-auth` | 密码复杂度策略 | minlen=8，minclass=4 |

**Kylin V10 特有配置：**

```
# 查看默认启用的密码复杂度模块
cat /etc/pam.d/system-auth |grep-E"pam_cracklib|pam_pwquality"

# 合规配置示例
minlen=8dcredit=-1 ucredit=-1 ocredit=-1 lcredit=-1
# 要求：至少1数字、1大写、1小写、1特殊字符
```

---

### 1.2 登录失败处理与会话超时

| 测评命令 | 功能说明 | 达标判据 |
| --- | --- | --- |
| `grep pam_tally2 /etc/pam.d/sshd` | SSH登录失败锁定 | deny=5，unlock\_time=300 |
| `grep TMOUT /etc/profile` | 会话超时 | TMOUT=600（秒） |
| `grep -E 'ClientAliveInterval|ClientAliveCountMax' /etc/ssh/sshd_config` | SSH会话超时 | 300秒无操作断开 |

---

### 1.3 远程管理安全

```
# 确认SSH服务运行
systemctl status sshd

# 检查SSH安全配置
cat /etc/ssh/sshd_config |grep-E'PermitRootLogin|Protocol|PubkeyAuthentication'
# 合规要求：PermitRootLogin no、Protocol 2、PubkeyAuthentication yes

# 确认未开放Telnet
ss -tuln|grep':23'
```

>  **高风险项**：使用Telnet或允许root远程登录，直接判定不符合三级要求。

---

### 1.4 双因子认证（高风险项）

**测评方法：**

* **访谈确认**：是否采用"口令+数字证书/Ukey"组合
* **技术核查**：

```
# 检查SSH公钥认证配置
grep"PubkeyAuthentication yes" /etc/ssh/sshd_config

# 检查PAM模块是否集成双因子
cat /etc/pam.d/sshd |grep-E"pam_pkcs11|pam_google_authenticator"

# 查看证书存储（如使用Ukey）
ls /etc/pki/nssdb/
```

---

## 二、访问控制（8.1.4.2）

### 2.1 账户与权限管理

| 测评命令 | 功能说明 | 达标判据 |
| --- | --- | --- |
| `grep -E 'adm|lp|sync|halt|news|uucp|operator|games|gopher' /etc/shadow` | 确认默认账户禁用 | 已锁定（`!!`或`*`）或删除 |
| `stat -c '%a %n' /etc/passwd /etc/shadow` | 关键文件权限 | 644/000 |
| `grep -v '^#' /etc/sudoers | grep -v '^$'` | sudo授权检查 | 最小权限原则 |
| `awk -F: '$3==0 && $1!="root"{print $1}' /etc/passwd` | 检查UID=0的非root账户 | 无输出 |

---

### 2.2 强制访问控制（Kylin特有）

Kylin V10 默认使用 **AppArmor** 替代 SELinux：

```
# 检查AppArmor状态
aa-status

# 查看已加载的配置文件
aa-status |grep enforce

# 验证关键进程策略
sudo apparmor_parser -q /etc/apparmor.d/usr.sbin.sshd
sudo apparmor_parser -q /etc/apparmor.d/usr.sbin.mysqld

# 查看AppArmor日志
dmesg|grep-i apparmor
```

**达标判据**：关键进程（sshd、mysqld、nginx等）应配置AppArmor策略并处于enforce模式。

---

## 三、安全审计（8.1.4.3）

### 3.1 审计服务启用

| 测评命令 | 功能说明 | 达标判据 |
| --- | --- | --- |
| `systemctl is-active auditd && systemctl is-enabled auditd` | 审计服务状态 | active & enabled |
| `auditctl -l | wc -l` | 审计规则数量 | ≥30条 |
| `aureport -i | head -20` | 审计事件摘要 | 包含登录、权限变更、文件操作 |
| `stat -c '%a %U:%G' /var/log/audit/audit.log` | 日志权限 | 600 root:root |

---

### 3.2 日志备份与防篡改

```
# 检查远程日志备份配置
grep-E'@\w+.*514' /etc/rsyslog.conf /etc/rsyslog.d/*.conf

# 合规配置示例
echo"*.info;mail.none;authpriv.none;cron.none @192.168.1.100:514">> /etc/rsyslog.conf
systemctl restart rsyslog

# 查看日志加密传输（TLS）
grep-E'DefaultNetstreamDriverCAFile\|ActionSendStreamDriverMode' /etc/rsyslog.conf
```

---

## 四、入侵防范（8.1.4.4）

### 4.1 最小化安装与漏洞修复

| 测评命令 | 功能说明 | 达标判据 |
| --- | --- | --- |
| `dpkg --list | grep -E 'telnet|ftp|rsh'` | 检查非必要组件 | 未安装 |
| `apt list --upgradable 2>/dev/null | wc -l` | 待更新补丁 | ≤30天 |
| `systemctl list-unit-files --state=enabled | grep -vE 'ssh|audit|cron|rsyslog'` | 启用服务 | 仅业务所需 |

---

### 4.2 端口与防火墙管控

| 测评命令 | 功能说明 | 达标判据 |
| --- | --- | --- |
| `ss -tunlp | grep -E '0.0.0.0:23|0.0.0.0:111|0.0.0.0:513'` | 高危端口检查 | 无监听 |
| `ufw status verbose` | UFW防火墙状态 | active，仅开放业务端口 |
| `cat /etc/hosts.deny` | TCP Wrappers | 包含`ALL:ALL` |

**Kylin V10 防火墙配置：**

```
# 查看默认防火墙（UFW）
sudo ufw status numbered

# 合规配置示例
sudo ufw default deny incoming
sudo ufw default allow outgoing
sudo ufw allow from 10.1.1.0/24 to any port 22 proto tcp
sudo ufw enable
```

---

## 五、恶意代码防范（8.1.4.5）

| 测评命令 | 功能说明 | 达标判据 |
| --- | --- | --- |
| `systemctl is-active clamav-daemon && systemctl is-enabled clamav-daemon` | ClamAV状态 | active & enabled |
| `freshclam --version` | 病毒库版本 | 24小时内更新 |
| `ps -ef | grep clamd` | 实时扫描进程 | 常驻内存 |

> **高风险项**：未部署实时防病毒工具，直接判定不符合三级要求。

**Kylin 特有安全中心：**

```
# 启动麒麟安全中心（图形化）
kysec-center &

# 命令行查看安全状态
kysec-status

# 查看病毒查杀记录
cat /var/log/kysec/antivirus.log
```

---

## 六、可信验证（Kylin特有，8.1.4.6）

| 测评命令 | 功能说明 | 达标判据 |
| --- | --- | --- |
| `fips-mode-setup --check` | FIPS 140-3合规模式 | 已启用（需订阅） |
| `mokutil --sb-state` | Secure Boot状态 | SecureBoot enabled |
| `dmesg | grep -i tpm` | TPM状态 | TPM 2.0就绪 |
| `cat /proc/cmdline | grep -E 'ima|evm'` | IMA/EVM启用 | 内核参数包含ima=on |

**可信启动验证：**

```
# 查看可信启动链
cat /sys/kernel/security/ima/ascii_runtime_measurements |head-5

# 验证系统完整性
kysec-verify --check-system
```

---

## 七、数据备份与恢复（8.1.4.9）

| 测评命令 | 功能说明 | 达标判据 |
| --- | --- | --- |
| `crontab -l | grep -i backup` | 备份策略 | 每日/每周任务 |
| `stat -c '%a %U:%G' /backup` | 备份目录权限 | 700 root:root |
| `tar -tzf /backup/etc-$(date +%F).tar.gz | wc -l` | 恢复验证 | 文件完整可解压 |

**Kylin 备份工具：**

```
# 使用麒麟备份还原工具
kybackup --create--name system-$(date +%F)--include /etc /var/log /home

# 查看备份列表
kybackup --list

# 验证备份完整性
kybackup --verify--name system-$(date +%F)
```

---

## 一键巡检脚本（Bash）

```
#!/bin/bash
# Kylin Linux V10 等保三级一键巡检脚本
# 执行用户：root

echo"===== 1 身份鉴别 ====="

echo"--- 空口令检查 ---"
awk -F: '$2==""{print "空口令用户: "$1}' /etc/shadow

echo"--- 密码有效期 ---"
grep-E'PASS_MAX_DAYS|PASS_MIN_DAYS' /etc/login.defs

echo"--- 密码复杂度 ---"
grep-E'pam_cracklib|pam_pwquality' /etc/pam.d/system-auth |head-5

echo"--- 登录失败锁定 ---"
grep pam_tally2 /etc/pam.d/sshd

echo"--- SSH配置 ---"
grep-E'PermitRootLogin|Protocol|ClientAlive' /etc/ssh/sshd_config |head-5

echo""
echo"===== 2 访问控制 ====="

echo"--- 默认账户状态 ---"
grep-E'adm|lp|sync|halt|news|uucp|operator|games|gopher' /etc/shadow |head-5

echo"--- 关键文件权限 ---"
stat-c'%a %n' /etc/passwd /etc/shadow 2>/dev/null

echo"--- AppArmor状态 ---"
aa-status 2>/dev/null |head-10||echo"AppArmor未安装"

echo""
echo"===== 3 安全审计 ====="

echo"--- auditd状态 ---"
systemctl is-active auditd && systemctl is-enabled auditd

echo"--- 审计规则数量 ---"
auditctl -l2>/dev/null |wc-l

echo"--- 日志权限 ---"
stat-c'%a %U:%G' /var/log/audit/audit.log 2>/dev/null

echo"--- 远程日志配置 ---"
grep-E'@\w+.*514' /etc/rsyslog.conf /etc/rsyslog.d/*.conf 2>/dev/null |head-3

echo""
echo"===== 4 入侵防范 ====="

echo"--- 高危端口 ---"
ss -tunlp|grep-E'0.0.0.0:23|0.0.0.0:111|0.0.0.0:513'

echo"--- 待更新包 ---"
apt list --upgradable2>/dev/null |wc-l

echo"--- 防火墙状态 ---"
ufw status verbose 2>/dev/null |head-5||echo"UFW未启用"

echo""
echo"===== 5 恶意代码防范 ====="

echo"--- ClamAV状态 ---"
systemctl is-active clamav-daemon 2>/dev/null
systemctl is-enabled clamav-daemon 2>/dev/null

echo"--- 病毒库版本 ---"
freshclam --version2>/dev/null ||echo"未安装freshclam"

echo""
echo"===== 6 可信验证（Kylin特有） ====="

echo"--- FIPS模式 ---"
fips-mode-setup --check2>/dev/null ||echo"未启用FIPS"

echo"--- Secure Boot ---"
mokutil --sb-state 2>/dev/null ||echo"无法检测Secure Boot"

echo"--- TPM状态 ---"
dmesg|grep-i"tpm"|head-3

echo""
echo"===== 7 数据备份 ====="

echo"--- 备份任务 ---"
crontab-l2>/dev/null |grep-i backup ||echo"未配置备份任务"

echo"--- 备份目录 ---"
stat-c'%a %U:%G' /backup 2>/dev/null ||echo"备份目录不存在"

echo""
echo"===== 巡检完成 ====="
```

---

## 高风险项重点核查清单

| 检查项 | 验证命令 | 不合规判定 | 整改建议 |
| --- | --- | --- | --- |
| **空口令账户** | `awk -F: '$2==""{print $1}' /etc/shadow` | 存在输出 | 立即设置强口令或锁定 |
| **密码复杂度未启用** | `grep -E 'pam_cracklib|pam_pwquality' /etc/pam.d/system-auth` | 无输出 | 配置pam\_pwquality模块 |
| **root远程登录** | `grep...