---
title: OpenEuler 等保2.0 三级合规安全加固操作指南
url: https://mp.weixin.qq.com/s/luJJ4eJnIeKMWRClpLDS7Q
source: Doonsec's feed
date: 2026-02-17
fetch_date: 2026-02-18T04:13:38.354937
---

# OpenEuler 等保2.0 三级合规安全加固操作指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6ynCILojBKrqzszeP9SSguInEun6skgdthsVdfnLSzxHzF4eJukCyicaLEQokI41ibxBFgCDpjaRjDib08LV8XvQhypIjQN382zOKcQmmkTcDo/0?wx_fmt=jpeg)

# OpenEuler 等保2.0 三级合规安全加固操作指南

原创

刘军军
刘军军

运维星火燎原

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/6ynCILojBKofA9bYu1ff67vKNf8n5lHv186FBjYXou2wNBEQoIAHEGF6X9l1ic4d0h8RaKmqfINficzRYVKKvdmX0S6NCuybYe7HJ7oKRuEPw/640?wx_fmt=png&from=appmsg)

在 openEuler 系统上实施 等保2.0（网络安全等级保护 2.0）三级要求 的具体操作，需围绕“身份鉴别、访问控制、安全审计、入侵防范、恶意代码防范、可信验证、资源控制”七大核心控制域展开。以下是以 openEuler 24.03 LTS 为例的可落地、可执行的操作清单，适用于政务、金融、能源等关键行业。

---

一、身份鉴别（Authentication）

1.设置强密码策略

```
# 安装 pam_pwquality（若未安装）
sudo dnf install -y pam_pwquality

# 编辑配置文件
sudo tee /etc/security/pwquality.conf <<EOF
minlen = 12
minclass = 3
dcredit = -1   # 至少1个数字
ucredit = -1   # 至少1个大写
lcredit = -1   # 至少1个小写
ocredit = -1   # 至少1个特殊字符
maxrepeat = 2
difok = 5
EOF
```

2.密码有效期与历史

```
# 修改 /etc/login.defs
sudo sed -i 's/^PASS_MAX_DAYS.*/PASS_MAX_DAYS   90/' /etc/login.defs
sudo sed -i 's/^PASS_MIN_DAYS.*/PASS_MIN_DAYS   7/' /etc/login.defs
sudo sed -i 's/^PASS_WARN_AGE.*/PASS_WARN_AGE   7/' /etc/login.defs

# 启用密码历史（防止重复使用最近5次密码）
echo "password required pam_pwhistory.so remember=5" >> /etc/pam.d/system-auth
```

3.登录失败锁定（防暴力破解）

```
# 使用 pam_faillock
sudo tee -a /etc/pam.d/system-auth <<EOF
auth required pam_faillock.so preauth silent deny=5 unlock_time=900
auth [default=die] pam_faillock.so authfail deny=5 unlock_time=900
account required pam_faillock.so
EOF
```

---

二、访问控制（Access Control）

1.禁用 root 远程登录 + 使用普通用户 + sudo

```
# 创建运维用户
sudo useradd -m -s /bin/bash secops
sudo passwd secops

# 授予 sudo 权限（无密码或带密码）
echo "secops ALL=(ALL) NOPASSWD: ALL" | sudo tee /etc/sudoers.d/secops

# 禁用 root 远程 SSH 登录（见下文 SSH 配置）
```

2.最小权限原则

* 应用运行使用专用低权账户（如 appuser），禁止以 root 启动服务。
* 使用 chmod / chown 严格控制敏感文件权限：

```
chmod 600 /etc/shadow
chmod 644 /etc/passwd
chown root:root /etc/ssh/sshd_config
```

---

三、安全审计（Security Audit）

1.启用 auditd 并配置关键规则

```
sudo dnf install -y audit
sudo systemctl enable--now auditd

# 创建审计规则文件
sudo tee /etc/audit/rules.d/99-equal-protection.rules <<EOF
# 监控用户账户变更
-w /etc/passwd -p wa -k identity
-w /etc/shadow -p wa -k identity
-w /etc/group -p wa -k identity
-w /etc/gshadow -p wa -k identity

# 监控特权命令
-w /usr/bin/sudo -p x -k priv_cmd
-w /usr/bin/su -p x -k priv_cmd

# 监控 SSH 配置
-w /etc/ssh/sshd_config -p wa -k ssh_config

# 记录所有系统调用（可选，性能敏感环境慎用）
-a always,exit -F arch=b64 -S execve -k exec
EOF

# 重载规则
sudo augenrules --load
```

2.日志集中管理（可选但推荐）

配置 rsyslog 将日志发送至 SIEM（如 ELK、Splunk）：

```
# 编辑 /etc/rsyslog.conf，添加
*.* @@your-siem-server:514

sudo systemctl restart rsyslog
```

---

四、SSH 安全加固（远程访问）

1.修改 /etc/ssh/sshd\_config

```
PermitRootLogin no
PasswordAuthentication no
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
AllowUsers secops
Protocol 2
ClientAliveInterval 300
ClientAliveCountMax 2
MaxAuthTries 3
LogLevel VERBOSE
```

务必先测试密钥登录成功后再重启 SSH！

```
sudo systemctl restart sshd
```

---

五、入侵防范 & 恶意代码防范

1.启用 SELinux（强制访问控制）

```
# 检查状态
getenforce

# 若为 disabled，启用 enforcing 模式
sudo setenforce 1
sudo sed -i 's/^SELINUX=.*/SELINUX=enforcing/' /etc/selinux/config
```

2.部署 AIDE（文件完整性检测）

```
sudo dnf install -y aide
sudo aide --init
sudo cp /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz

# 创建每日校验 cron
echo "0 2 * * * /usr/sbin/aide --check | logger -t aide" | sudo tee /etc/cron.d/aide-check
```

3.安装 fail2ban（防 SSH 暴力破解）

```
sudo dnf install -y fail2ban
sudo systemctl enable --now fail2ban

# 可选：自定义 jail.local
sudo tee /etc/fail2ban/jail.local <<EOF
[sshd]
enabled = true
maxretry = 3
bantime = 900
findtime = 600
EOF

sudo systemctl restart fail2ban
```

---

六、网络与服务最小化

1.关闭非必要服务

```
# 查看已启用服务
systemctl list-unit-files --type=service --state=enabled

# 禁用示例（根据实际业务调整）
sudo systemctl disable --now avahi-daemon cups bluetooth
```

2.配置防火墙（仅开放必要端口）

```
sudo systemctl enable --now firewalld

# 示例：仅允许 SSH + 业务端口（如 8080）
sudo firewall-cmd --permanent --remove-service={dhcpv6-client,cockpit}
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd --reload
```

---

七、系统更新与漏洞管理

1.定期更新系统

```
# 手动更新
sudo dnf update -y

# 或配置自动安全更新（谨慎）
sudo dnf install -y dnf-automatic
sudo systemctl enable --now dnf-automatic-install.timer
```

建议订阅 openEuler 安全公告 获取 CVE 信息。

---

八、可信验证（高级要求，三级可选）

* 启用 Secure Boot（需 UEFI 支持）
* 启用 IMA（Integrity Measurement Architecture）

```
# 在 /etc/default/grub 中添加
GRUB_CMDLINE_LINUX="ima_policy=tcb ima_appraise=fix"
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

---

附：等保2.0 三级合规检查表（openEuler）

|  |  |  |
| --- | --- | --- |
| 控制项 | 是否完成 | 验证命令 |
| 强密码策略 | ☐ | grep -v "^#" /etc/security/pwquality.conf |
| 登录失败锁定 | ☐ | pam\_faillock --user secops --reset |
| auditd 启用 | ☐ | systemctl is-active auditd |
| SELinux enforcing | ☐ | getenforce |
| SSH 密钥登录 | ☐ | ssh -i key user@host |
| 防火墙启用 | ☐ | firewall-cmd --list-all |
| AIDE 初始化 | ☐ | ls /var/lib/aide/aide.db.gz |

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/G7WSQyicBkgj2B5jst2Cx1Bx9b3NfXBzOmPldmsqoKWoyWr0s3BibONOSicegTCQVvdls7fkG4YchibVBXha6b6dqQ/0?wx_fmt=png)

运维星火燎原

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/G7WSQyicBkgj2B5jst2Cx1Bx9b3NfXBzOmPldmsqoKWoyWr0s3BibONOSicegTCQVvdls7fkG4YchibVBXha6b6dqQ/0?wx_fmt=png)

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