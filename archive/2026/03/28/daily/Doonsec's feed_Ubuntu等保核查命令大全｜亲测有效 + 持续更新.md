---
title: Ubuntu等保核查命令大全｜亲测有效 + 持续更新
url: https://mp.weixin.qq.com/s/7jblJz_b_fJRrCR_ADURcA
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:37:01.206031
---

# Ubuntu等保核查命令大全｜亲测有效 + 持续更新

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eDTxibgibqtmficPAja0e6HE2m90LUlJZtopbLV6IIUF1keknjCicJ8DNZwT4Wicwy2k4WwcxetHnbg34nYPc794OmA/0?wx_fmt=jpeg)

# Ubuntu等保核查命令大全｜亲测有效 + 持续更新

Sec Online

![]()

在小说阅读器中沉浸阅读

以下文章来源于汤池杂货铺
，作者Fuyuanzi

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM5J0Y2dAfZtVROkAVlm3W1h1cT95E1sJ3cFJ0nGNSmcJA/0)

**汤池杂货铺**
.

是一个什么都想学一点的小邋遢

---

解决以下3个痛点：

1️⃣互联网**现有检查命令存在过时与覆盖不全的问题**

2️⃣**互联网上流传的检查命令普遍泛化，缺乏针对性与验证，在实际测试环境中不正确的检查命令会导致不必要时间的浪费。**

3️⃣**网络公开的检查方法整体缺乏系统性与持续维护**

💽测试环境：虚拟机

💽测试镜像版本：Ubuntu 25.04

📚文末可提取本文的无水印PDF版本的百度网盘下载链接，方便各位在无网络环境下的使用。

👇如果有更加好的检测命令或者需要修改的地方，请在评论区留言。我会及时更新改正，并上传新的离线文件。

---

# 一、身份鉴别

## 1.1 账号管理

```
cat /etc/passwd
```

* • 查看命令结果，第三字段不存在相同数字、用户名不存在相同名称(唯一性)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZtoqH6k6lbibUNbfRLjO4nvHg9qzGNmOenibbPIXNhlezFclN0zLOe5icqJw/640?wx_fmt=png&from=appmsg)

## 1.2 登录失败处理

```
cat /etc/pam.d/common-auth
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZto2I7U4o9QA16tuicK9TUOia5bOzQUalHT5b89hunU26HrPsc2ZrPqr5bg/640?wx_fmt=png&from=appmsg)

**参数含义：**

* • `deny=5`连续**5 次**密码错误后锁定账号（等保推荐 5 次，可设 3/6 次）
* • `unlock_time=300`自动解锁时长，单位**秒**（300 秒 = 5 分钟；设为`-1`则永久锁定，需管理员手动解锁）
* • `enforce_for_root`对 root 用户的密码错误计数生效
* • `even_deny_root`**对 root 用户执行锁定**（与上一参数联动，等保必须开启，禁止 root 无限试错）
* • `no_lock_time`可选，取消自动解锁，仅支持管理员手动解锁（替代 unlock\_time）

## 1.3 远程管理通信的加密方法

```
ssh -vvv user@server_ip 2>&1 | grep -E "cipher|MAC|kex algorithm"
```

当前使用SSH时使用的算法【不同网络环境中可能会有变化、如出现加密降级等】

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZto7S9Z8LQheYs1MOGv8lK56tqnoI7gRT3p3HFZptOHXNL7aUlKMxYVEg/640?wx_fmt=png&from=appmsg)

* • **Cipher（加密算法）**：`chacha20-poly1305@openssh.com`
    这是目前 SSH 中**安全性和性能都非常出色**的算法，采用流加密 + Poly1305 消息认证，是 OpenSSH 推荐的默认算法，安全性远高于传统的 AES-CBC。
* • **MAC（消息认证码）**：`<implicit>`
    因为 `chacha20-poly1305` 是 **AEAD（带关联数据的认证加密）** 算法，它会在加密的同时自动完成消息认证，因此不需要额外配置 MAC，这是更安全的设计。

## 1.4 密码复杂度策略

```
cat /etc/security/pwquality.conf | grep -v "^#\|^$"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZtobxe4xLhvzYr9sAua5nmRciaArztVOwwX8jZxBic2NDuQGWibsxiaUUBenA/640?wx_fmt=png&from=appmsg)

**参数含义：**

* • `retry=3`密码输入错误时，最多重试 3 次
* • `minlen=8`密码**最小长度 8 位**（等保要求，建议设为 12 位提升安全性）
* • `lcredit=-1`至少包含**1 个小写字母**（-n 表示至少 n 个，正数表示最多 n 个）
* • `ucredit=-1`至少包含**1 个大写字母**
* • `dcredit=-1`至少包含**1 个数字**
* • `ocredit=-1`至少包含**1 个特殊符号**（!@#$%^&\* 等）
* • `difok=3`新密码与旧密码至少有**3 个字符不同**（防止仅改 1-2 位的弱修改）
* • `enforce_for_root`**对 root 用户生效**（默认 root 不受密码规则限制，等保必须开启）
* • `remember=5`禁止使用最近**5 次**的历史密码（防止循环使用弱密码）
* • `reject_username`禁止密码中包含**用户名 / 主机名**（如用户 test，密码不可为 Test123!）
* • `maxrepeat=3`禁止同一字符连续重复**3 次**（如 1111、aaaa，防止简单密码）

## 1.5 双因素认证

访谈客户，确认远程管理是否启用双因素认证（如 SSH+Google Authenticator），并现场验证

## 1.6 密码过期策略

```
chage -l root  # 检查root密码过期配置
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZto4KXzNibLGoUA617as5PygWGESntXscfg6m4C0Vzq6QwfyHvvwWvCTdw/640?wx_fmt=png&from=appmsg)

```
cat /etc/login.defs | grep "PASS"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZtoZ9ZO7OkZ5DBg7iatMeNZbHxYYbSOCkSiag7KuelkKZ9DYLjvibKHzrictg/640?wx_fmt=png&from=appmsg)

**参数含义：**

* • PASS\_MAX\_DAYS 90 # 密码最大有效期90天（等保要求）
* • PASS\_MIN\_DAYS 1 # 密码最小修改间隔1天
* • PASS\_WARN\_AGE 7 # 密码过期前7天提醒
* • PASS\_MIN\_LEN 8 # 密码最小长度8位（与PAM配置联动）

## 1.7 登录超时

```
cat /etc/profile | grep "TMOUT"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZtoN6v9zrgtYxlv4KEYGIw8eGJ9v12UbKhlDGn49jF1tekLModlRgTOibg/640?wx_fmt=png&from=appmsg)

# 二、访问控制

## 2.1 账户权限审计

结合身份鉴别中检查的内容去判断服务器是否进行了特权分离，即：设置管理员、审计员、操作员等不同角色，进行分离权限。

## 2.2 匿名用户/默认账户

```
more /etc/shadow
```

* • 查看命令返回结果 第二字段为`（！*）`表示该账户已锁定或禁用
* • uucp、nuucp、lp、adm、shutdown均为默认账户
* • 查看命令结果，红框内的乱码表示加密以后的账户口令

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZtoMAGwy4xVibfuibtS0P6ldyiamiciadWcnTAzOI6t3DLkfR2E4ueqAbtLUZQ/640?wx_fmt=png&from=appmsg)

## 2.3 共享账户查询

```
grep -E "Accepted publickey|Accepted password" /var/log/auth.log
```

查看日志，可以从同一`fuyuanzi`账户在**不同 IP**（192.168.42.1、xxx.xxx.xxxx.xxx）同时 / 先后登录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZtoWeB588fr45enKgU1FBZ5IZ6TtcodoiawYlDMgj4l3MYrqrfn11DrEWg/640?wx_fmt=png&from=appmsg)

```
w
```

通过查看**当前系统登录用户及用户活动状态**，判断用户的使用是否存在共享状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZto9l1kbpiaXmAJegrb182nCGTZHicjdaucems4PwfuKibwcEBK43buBibEZQ/640?wx_fmt=png&from=appmsg)

`TTY`登录**终端类型**：

* • `tty1/ttyN`——本地物理终端
* • `pts/0/pts/N`——远程虚拟终端（SSH/Xshell 等）

结合上述几种方式判断是否存在**共享账户**。

## 2.4 最小权限原则

结合身份鉴别中检查的内容去判断服务器是否进行了特权分离，即：设置管理员、审计员、操作员等不同角色，进行分离权限。

## 2.5 核查账户和权限情况

```
umask
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZtolNADoIhlc110Ja9pvnvDkbicfmnCl24ISk3xBI7y9O4VC5iayAY07Pnw/640?wx_fmt=png&from=appmsg)

| umask 值 | 核心用途 | 关键特点 |
| --- | --- | --- |
| 0022 | 通用默认配置 | 平衡安全与可用性 |
| 0002 | 组内协作 | 同组可读写，外部只读 |
| 0077 | 个人敏感数据 | 仅自己可访问 |
| 0222 | 公共只读资源 | 所有人不可修改 |
| 0017 | 部门内部共享 | 仅组内可协作 |
| 0027 | 用于对安全性要求较高的场景 | 大幅限制其他用户的权限，避免敏感文件 / 目录被无关用户访问或修改 |
| **检查 sudo 权限配置（是否存在过度授权）** |  |  |

```
cat /etc/sudoers /etc/sudoers.d/* | grep -v "^#\|^$"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZtorIEBMzV2kPraYXrDibDiczKSZhliarflIRiamliawqddlnVwM3GZrBMY7fQ/640?wx_fmt=png&from=appmsg)

**参数含义：**

1. 1. Defaults 全局默认配置

* • `env_reset`：重置环境变量，避免用户环境中的恶意变量影响 sudo 执行的命令，提升安全性。
* • `mail_badpass`：当用户输入错误密码时，向系统管理员发送邮件告警。
* • `secure_path`：指定 sudo 执行命令时使用的安全 PATH，防止恶意程序通过 PATH 被优先执行。
* • `use_pty`：强制在伪终端（PTY）中执行命令，避免某些终端劫持攻击。

2. 2. 用户 / 组权限规则

* • `root ALL=(ALL:ALL) ALL`：root 用户可以在任何主机（`ALL`）上，以任何用户（`ALL`）和任何用户组（`ALL`）的身份，执行任何命令（`ALL`）。
* • `%admin ALL=(ALL) ALL`：`admin` 组的成员可以在任何主机上，以任何用户身份执行任何命令。
* • `%sudo ALL=(ALL:ALL) ALL`：`sudo` 组的成员拥有与 root 完全相同的权限，这是 Ubuntu 系统默认赋予普通管理员的组。

## 2.6 访问控制粒度审计

检查用户文件、系统文件、日志文件等文件的访问权限，确认符合最小权限原则。

```
ls -l /etc/passwd /etc/shadow /etc/group /etc/sudoers /root /etc/crontab /var/log/ /var/log/audit/audit.log /var/log/syslog /var/log/messages /var/log/secure
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZtobu36PZwepC9icbQl35tpme8VibvSnWVbj3YFghbiaBWuUZQgibZA03CjgA/640?wx_fmt=png&from=appmsg)

## 2.7 强访问控制状态

* • CentOS/RHEL默认安装并启用（Enforcing）依赖 SELinux（MAC）+ AppArmor
* • Ubuntu默认未安装、未启用**仅依赖 AppArmor**（MAC）

```
sestatus  # Enforcing 为正常，Permissive/Disenabled 为异常

getenforce  # Enforcing 为正常，Permissive/Disenabled 为异常
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZtodg5zABQ1kVAPpibSjgzbiatotutLVUdf0SjcDoxqDSlKRDkwRj7kGGTQ/640?wx_fmt=png&from=appmsg)

# 三、安全审计

## 3.1 检查审计服务是否开启

Ubuntu默认未安装auidtd服务，或者未开启auditd服务。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZto2ktSOiaZLFRJTddVRaP63s8tR5ibH2woDjNtQC1k3UiaAPBviaR7JyVpWA/640?wx_fmt=png&from=appmsg)

```
systemctl status auditd

auditctl -l  # 查看审计规则

systemctl status rsyslog
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZtoPvYqibkqHpIib5OMe0fm7hncyk0w6TBSSWmo3jm356qXqaloMPl6VGdA/640?wx_fmt=png&from=appmsg)

## 3.2 审计记录核查

```
tail -n 20 /var/log/syslog
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZtoWwhibUhHAkXcerPMylAPLpMZ7PBS1JjOaOA9SGNbx2dBweBMM5zzkYg/640?wx_fmt=png&from=appmsg)

## 3.3 检查日志轮转配置（防止日志占满磁盘）

```
cat /etc/logrotate.conf /etc/logrotate.d/* | grep -v "^#\|^$"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZtoPAhRhQuzj753VZlL0fYicj2oLxROb0ViaLodfVRjsyibibibwxjYnVsGWAg/640?wx_fmt=png&from=appmsg)

```
du -sh /var/log/auth.log /var/log/syslog 2>/dev/null
# 查看当前核心日志文件实际大小
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZtoRaS5qLwdukgl4sJgGa1PuZK7YT4Q4jMZ6natMG8mnw2RWAqZtKGLfQ/640?wx_fmt=png&from=appmsg)

```
# 查看/var/log所在磁盘的总空间、已用空间、剩余空间
df -h /var/log/
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmficPAja0e6HE2m90LUlJZto...