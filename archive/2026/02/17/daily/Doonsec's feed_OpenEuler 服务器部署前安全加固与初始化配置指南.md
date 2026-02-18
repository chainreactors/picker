---
title: OpenEuler 服务器部署前安全加固与初始化配置指南
url: https://mp.weixin.qq.com/s/YPZpuVRpKoxSuiKLPA4DQQ
source: Doonsec's feed
date: 2026-02-17
fetch_date: 2026-02-18T04:13:35.559686
---

# OpenEuler 服务器部署前安全加固与初始化配置指南

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6ynCILojBKqeka4Y3totHp3IKuo9YwQZL5tyjLuQGgzBcibc7eib8KSSQEsuHZADxsrfrBLfYIwIYdI51iah3mzv5Xhxrm7ZakyhbibcSgLdx1Q/0?wx_fmt=jpeg)

# OpenEuler 服务器部署前安全加固与初始化配置指南

原创

刘军军
刘军军

运维星火燎原

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/6ynCILojBKpjqV2tItIxmXmUesNHicOKSfibjibFUj8Ib8H6fM1ib8Gs7m7ccVWJIx3M6uH4ZERG3Aej305qg0tiaHnCetnA5uRpclSOZOsu7oMs/640?wx_fmt=png&from=appmsg)

在部署应用前，对一台新的 欧拉操作系统（openEuler） 服务器进行安全加固和基础配置是非常关键的步骤。以下是一套推荐的操作清单，涵盖系统初始化、安全加固及运维准备等方面：

---

一、基础系统配置

1.系统更新

确保系统为最新状态，修复已知漏洞：

```
sudo dnf update -y
```

2.设置主机名与网络

* 设置有意义的主机名：

```
sudo hostnamectl set-hostname your-server-name
```

* 配置静态 IP（如需要），修改 /etc/sysconfig/network-scripts/ifcfg-xxx 或使用 nmcli（若使用 NetworkManager）。

3.配置时区与时间同步

```
sudo timedatectl set-timezone Asia/Shanghai
sudo dnf install chrony -y
sudo systemctl enable --now chronyd
```

---

二、用户与权限管理

4.禁用或删除不必要的账户

* 删除或锁定无用账户（如 games, ftp 等）。
* 禁用 root 远程登录（见 SSH 配置）。

5.创建普通运维用户 + sudo 权限

```
useradd -m -s /bin/bash opsuser
passwd opsuser
# 授予 sudo 权限
echo "opsuser ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers
```

6.配置强密码策略（可选但推荐）

安装并配置 PAM 密码复杂度：

```
sudo dnf install pam_pwquality -y
```

编辑 /etc/security/pwquality.conf，例如：

```
minlen = 12
minclass = 3
dcredit = -1   # 至少一个数字
ucredit = -1   # 至少一个大写
lcredit = -1   # 至少一个小写
ocredit = -1   # 至少一个特殊字符
```

---

三、SSH 安全加固

7.修改 SSH 配置（/etc/ssh/sshd\_config）

```
PermitRootLogin no
PasswordAuthentication no          # 强烈建议使用密钥认证
PubkeyAuthentication yes
AuthorizedKeysFile .ssh/authorized_keys
AllowUsers opsuser                 # 仅允许特定用户
Protocol 2
ClientAliveInterval 300
ClientAliveCountMax 2
MaxAuthTries 3
```

重启 SSH 服务：

```
sudo systemctl restart sshd
```

注意：务必先测试密钥登录成功后再禁用密码！

---

四、防火墙与网络防护

8.启用并配置 firewalld

```
sudo systemctl enable --now firewalld
# 仅开放必要端口，例如 22（SSH）、80、443 等
sudo firewall-cmd --permanent --add-service=ssh
sudo firewall-cmd --permanent --add-port=8080/tcp
sudo firewall-cmd --reload
```

9.禁用 IPv6（如不需要）

编辑 /etc/default/grub，添加 ipv6.disable=1 到 GRUB\_CMDLINE\_LINUX，然后：

```
sudo grub2-mkconfig -o /boot/grub2/grub.cfg
```

---

五、日志与审计

10.启用 auditd（系统审计）

```
sudo dnf install audit -y
sudo systemctl enable --now auditd
```

可配置关键文件监控（如 /etc/passwd, /etc/shadow, /etc/ssh/sshd\_config）。

11.配置 rsyslog 远程日志（可选）

将日志发送到集中日志服务器，防止本地篡改。

---

六、内核与系统安全参数

12.调整 sysctl 安全参数

编辑 /etc/sysctl.conf 或新建 /etc/sysctl.d/99-security.conf：

```
# 防止 SYN flood
net.ipv4.tcp_syncookies = 1

# 禁用 ICMP 重定向
net.ipv4.conf.all.accept_redirects = 0
net.ipv4.conf.default.accept_redirects = 0

# 启用反向路径过滤
net.ipv4.conf.all.rp_filter = 1

# 禁用源路由
net.ipv4.conf.all.accept_source_route = 0
```

生效：

```
sudo sysctl -p /etc/sysctl.d/99-security.conf
```

---

七、文件系统与服务最小化

13.禁用不必要的服务

```
systemctl list-unit-files --type=service | grep enabled
# 禁用如 avahi-daemon, cups, bluetooth 等非必要服务
sudo systemctl disable --now avahi-daemon
```

14.设置关键文件权限

```
chmod 600 /etc/shadow
chmod 644 /etc/passwd
chmod 600 /etc/ssh/sshd_config
chown root:root /etc/shadow
```

15.挂载点安全（如 /tmp, /var/tmp）

在 /etc/fstab 中为临时目录添加 noexec,nosuid,nodev：

```
tmpfs /tmp tmpfs defaults,noexec,nosuid,nodev 0 0
```

---

八、安装安全工具（可选但推荐）

* fail2ban：防暴力破解

```
sudo dnf install fail2ban -y
sudo systemctl enable --now fail2ban
```

* ClamAV（如需病毒扫描）
* AIDE：文件完整性检测

```
sudo dnf install aide -y
sudo aide --init
sudo cp /var/lib/aide/aide.db.new.gz /var/lib/aide/aide.db.gz
```

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