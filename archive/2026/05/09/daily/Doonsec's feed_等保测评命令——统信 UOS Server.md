---
title: 等保测评命令——统信 UOS Server
url: https://mp.weixin.qq.com/s/Fo5HKynFB1psCCAPEt3GZQ
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:32:22.542198
---

# 等保测评命令——统信 UOS Server

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/JJfExzHZwzG4A50V7RhiawjCy4VTkzb86pzu55Bq2ueBic7vMrNNWibarSexWEBmriaNAenQ1cg8iaxnEXtxvsXtO4GYjpD7lJia0EmHrD8LgicGVo/0?wx_fmt=jpeg)

# 等保测评命令——统信 UOS Server

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

依据 **GB/T 22239-2019《信息安全技术 网络安全等级保护基本要求》第三级"安全计算环境"** 条款，结合 **统信官方文档** 及多家测评机构现场实践，给出 **统信 UOS Server V20（含桌面版、国防版）** 可直接落地的测评命令/操作清单。

已在 **UOS 1020a/1020e/1050** 版本验证通过，支持 **apt/dpkg** 包管理及 **systemd** 体系。

---

## 一、身份鉴别（8.1.4.1）

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 空口令检查 | `awk -F: '$2==""{print $1}' /etc/shadow` | 无输出 |
| 密码复杂度 | `dpkg -l libpam-pwquality` 已安装； `grep -E "pam_pwquality|pam_cracklib" /etc/pam.d/common-password` | minlen≥8，minclass≥4，retry≤3 |
| 密码有效期 | `grep -E "^PASS_MAX_DAYS|^PASS_MIN_DAYS|^PASS_WARN_AGE" /etc/login.defs` | ≤90 天，≥1 天，≥7 天预警 |
| 登录失败锁定 | `grep pam_tally2 /etc/pam.d/login /etc/pam.d/ssh` | deny≤5，unlock\_time≥300s，even\_deny\_root |
| SSH 超时 | `grep -E "^ClientAliveInterval|^ClientAliveCountMax" /etc/ssh/sshd_config` | 300 秒内无操作自动断开 |
| 禁止 root 远程 | `grep ^PermitRootLogin /etc/ssh/sshd_config` | 设为 `no` |

---

## 二、访问控制（8.1.4.2）

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 唯一账户 | `awk -F: '$3<1000 && $1!="root"{print $1}' /etc/passwd` | 仅保留系统必需账户 |
| sudo 白名单 | `grep -v ^# /etc/sudoers | grep -v ^$` | 最小授权原则 |
| 文件权限 | `stat -c '%a %n' /etc/{passwd,shadow,group,gshadow}` | 644/000/644/000 |
| umask | `grep -E '^umask\s+(022|027)' /etc/profile /etc/bash.bashrc` | 022 或 027 |
| 访问控制列表 | `iptables -L -n` 或 `ufw status` | 仅开放业务端口，拒绝其他 |
| 主机访问控制 | `cat /etc/hosts.allow /etc/hosts.deny` | 限制管理 IP 范围 |

---

## 三、安全审计（8.1.4.3）

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| auditd 运行 | `systemctl is-active auditd && systemctl is-enabled auditd` | active & enabled |
| 审计规则 | `auditctl -l | wc -l` `grep -E "-w /etc/passwd" /etc/audit/rules.d/audit.rules` | ≥30 条，覆盖关键文件/命令 |
| 日志保留 | `grep -E "^max_log_file|^num_logs" /etc/audit/auditd.conf` | 单文件 ≥50 MB，保留 ≥6 个月 |
| 日志权限 | `stat -c '%a %U:%G' /var/log/audit/audit.log` | 640 root:root |

---

## 四、入侵防范（8.1.4.4）

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 补丁更新 | `apt list --upgradable 2>/dev/null | wc -l` `last | grep reboot` | ≤30 天内更新；已重启 |
| 开放端口 | `ss -tulnp | grep LISTEN` | 无高危端口（111、23、513 等） |
| 服务最小化 | `systemctl list-unit-files --state=enabled | grep -v -E "ssh|audit"` | 仅业务所需服务 |
| SELinux/AppArmor | `aa-status | head` 或 `getenforce` | 强制模式或 AppArmor 生效 |

---

## 五、恶意代码防范（8.1.4.5）

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 杀毒软件 | `dpkg -l | grep -E "clamav|uos-defender"` | 已安装并启用实时保护 |
| 病毒库更新 | `freshclam --version` | 24 小时内更新 |
| 实时扫描 | `systemctl is-active clamav-daemon` | active |

---

## 六、可信验证（8.1.4.6）

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| TPM | `dmesg | grep -i tpm` | 显示 TPM 2.0 就绪 |
| IMA/EVM | `cat /proc/cmdline | grep -E "ima=on|evm=fix"` | 已启用 |
| 文件完整性 | `rpm -Va | grep -E "^..5"` | 无关键文件被篡改 |

---

## 七、数据备份与恢复（8.1.4.9）

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 备份策略 | `crontab -l | grep backup` | 每日/每周任务 |
| 备份目录权限 | `stat -c '%a %U:%G' /backup` | 700 root:root |
| 恢复验证 | `tar -tzf /backup/etc-$(date +%F).tar.gz | wc -l` | 可解压且文件数一致 |

---

## 八、剩余信息保护（8.1.4.10）

| 控制项 | 测评命令 | 达标判据 |
| --- | --- | --- |
| 历史命令 | `grep -E "^HISTSIZE=" /etc/profile` | ≤500 |
| 登录超时 | `grep -E "^export TMOUT=" /etc/profile` | 900 秒 |
| 登录提示 | `ls -l /etc/motd` | 存在并含合规提示 |

---

## 一键巡检脚本（可直接使用）

```
#!/bin/bash
# 统信UOS Server V20 等保三级一键巡检脚本
# 适用：UOS 1020a/1020e/1050
# 执行用户：root

echo"===== 1 身份鉴别 ====="
echo"--- 空口令检查 ---"
awk -F: '$2==""{print "空口令用户: "$1}' /etc/shadow

echo"--- 密码复杂度 ---"
dpkg -l libpam-pwquality 2>/dev/null |grep-E"^ii"||echo"未安装libpam-pwquality"
grep-E"pam_pwquality|pam_cracklib" /etc/pam.d/common-password 2>/dev/null |head-3

echo"--- 密码有效期 ---"
grep-E"^PASS_MAX_DAYS|^PASS_MIN_DAYS|^PASS_WARN_AGE" /etc/login.defs

echo"--- SSH配置 ---"
grep-E"^PermitRootLogin|^ClientAliveInterval|^ClientAliveCountMax" /etc/ssh/sshd_config

echo"--- 登录失败锁定 ---"
grep pam_tally2 /etc/pam.d/login /etc/pam.d/ssh 2>/dev/null ||echo"未配置登录失败锁定"

echo""
echo"===== 2 访问控制 ====="
echo"--- 系统账户 ---"
awk -F: '$3<1000 && $1!="root"{print "系统账户: "$1}' /etc/passwd

echo"--- 关键文件权限 ---"
stat-c'%a %n' /etc/passwd /etc/shadow /etc/group /etc/gshadow 2>/dev/null

echo"--- 防火墙状态 ---"
iptables -L-n2>/dev/null |head-5|| ufw status 2>/dev/null |head-5

echo""
echo"===== 3 安全审计 ====="
echo"--- auditd状态 ---"
systemctl is-active auditd && systemctl is-enabled auditd

echo"--- 审计规则数量 ---"
auditctl -l2>/dev/null |wc-l

echo"--- 审计日志权限 ---"
stat-c'%a %U:%G' /var/log/audit/audit.log 2>/dev/null

echo""
echo"===== 4 入侵防范 ====="
echo"--- 待更新包数量 ---"
apt list --upgradable2>/dev/null |wc-l

echo"--- 监听端口 ---"
ss -tulnp|grep LISTEN |grep-v-E"22|53|80|443"|head-10

echo"--- AppArmor状态 ---"
aa-status 2>/dev/null |head-3||echo"AppArmor未安装"

echo""
echo"===== 5 恶意代码防范 ====="
echo"--- 杀毒软件 ---"
dpkg -l2>/dev/null |grep-E"clamav|uos-defender"|head-3

echo"--- 病毒库版本 ---"
freshclam --version2>/dev/null ||echo"未安装ClamAV"

echo""
echo"===== 6 可信验证 ====="
echo"--- TPM状态 ---"
dmesg|grep-i"tpm"|head-3

echo"--- IMA/EVM ---"
cat /proc/cmdline |grep-E"ima|evm"||echo"未启用IMA/EVM"

echo""
echo"===== 7 数据备份 ====="
echo"--- 备份任务 ---"
crontab-l2>/dev/null |grep-i backup ||echo"未配置备份任务"

echo""
echo"===== 8 剩余信息保护 ====="
echo"--- 历史命令限制 ---"
grep-E"^HISTSIZE=" /etc/profile

echo"--- 登录超时 ---"
grep-E"^export TMOUT=" /etc/profile

echo"--- 巡检完成 ====="
```

---

## 关键配置文件说明

### 1. 密码策略配置（/etc/pam.d/common-password）

```
# 密码复杂度要求：最小8位，至少4种字符类型，3次尝试机会
password requisite pam_pwquality.so retry=3minlen=8minclass=4dcredit=-1 ucredit=-1 lcredit=-1 ocredit=-1

# 密码历史：记住12次密码，防止重复使用
password sufficient pam_unix.so obscure use_authtok try_first_pass remember=12 sha512
```

### 2. 登录失败锁定配置（/etc/pam.d/login）

```
# 连续5次失败锁定300秒，root账户同样受限制
auth required pam_tally2.so onerr=fail deny=5unlock_time=300 even_deny_root root_unlock_time=600

# 解锁命令（管理员执行）
pam_tally2 --user=username --reset
```

### 3. SSH安全配置（/etc/ssh/sshd\_config）

```
# 禁止root远程登录
PermitRootLogin no

# 仅允许特定用户组
AllowGroups sshusers

# 空闲超时配置（5分钟无操作自动断开）
ClientAliveInterval 300
ClientAliveCountMax 0

# 仅使用SSHv2协议
Protocol 2

# 禁用密码认证，启用密钥认证（可选）
PasswordAuthentication no
PubkeyAuthentication yes
```

### 4. 审计规则配置（/etc/audit/rules.d/audit.rules）

```
# 监控用户/组修改
-w /etc/passwd -p wa -k identity_changes
-w /etc/group -p wa -k identity_changes
-w /etc/shadow -p wa -k identity_changes
-w /etc/gshadow -p wa -k identity_changes

# 监控sudoers修改
-w /etc/sudoers -p wa -k sudoers_changes
-w /etc/sudoers.d/ -p wa -k sudoers_changes

# 监控SSH配置
-w /etc/ssh/sshd_config -p wa -k ssh_config_changes

# 监控特权命令
-a always,exit -Farch=b64 -S setuid -S setgid -S setreuid -S setregid -k privilege_escalation
```

---

## 高风险项重点核查清单

| 检查项 | 验证命令 | 不合规判定 | 整改建议 |  |
| --- | --- | --- | --- | --- |
| **空口令账户** | `awk -F: '$2==""{print $1}' /etc/shadow` | 存在输出 | 立即设置强口令或锁定账户 |  |
| **root远程登录** | `grep ^PermitRootLogin /etc/ssh/sshd_config` | 值为`yes`或未配置 | 修改为`no`并重启sshd |  |
| **密码复杂度未启用** | `dpkg -l libpam-pwquality` | 未安装 | 安装并配置pam\_pwquality |  |
| **审计未启用** | `systemctl is-active auditd` | 非`active` | 安装auditd并启用服务 |  |
| **无登录失败锁定** | `grep pam_tally2 /etc/pam.d/login` | 无输出 | 配置pam\_tally2策略 |  |
| **高危端口开放** | `ss -tulnp | grep -E "111|23|513"` | 存在监听 | 关闭rpcbind、telnet等服务 |
| **无杀毒软件** | `dpkg -l | grep -E "clamav|uos-defender"` | 无输出 | 安装UOS自带 Defender 或 ClamAV |
| **备份未配置** | `crontab -l | grep backup` | 无输出 | 配置定时备份任务 |

---

## 统信UOS特色功能

### 1. 国密算法支持

UOS内置国密算法（SM2/SM3/SM4），可通过以下命令启用：

```
# 查看国密模块
uos-crypto-tool --list

# 启用国密证书
uos-crypto-tool --enable-sm2 --cert-path /etc/ssl/certs/sm2.crt

# 查看当前使用的加密算法
cat /proc/crypto |grep-E"sm2|sm3|sm4"
```

### 2. UOS安全中心（图形化）

```
# 启动安全中心（桌面版）
uos-security-cen...