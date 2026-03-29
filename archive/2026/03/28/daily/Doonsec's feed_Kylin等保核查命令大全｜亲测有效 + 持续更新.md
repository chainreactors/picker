---
title: Kylin等保核查命令大全｜亲测有效 + 持续更新
url: https://mp.weixin.qq.com/s/TVv7Gww1z3mT5ulqsaZe1Q
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:36:57.935795
---

# Kylin等保核查命令大全｜亲测有效 + 持续更新

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30Uy8rnBVhyXj7KJX2niacWiaPEg3LbWOgtdITQalhRibSMjba2puDS6Y5Bw/0?wx_fmt=jpeg)

# Kylin等保核查命令大全｜亲测有效 + 持续更新

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

💽测试镜像版本：Kylin-Server-V10-SP3-2403-Release-20240426-x86\_64

📚文末可提取本文的无水印PDF版本的百度网盘下载链接，方便各位在无网络环境下的使用。

👇如果有更加好的检测命令或者需要修改的地方，请在评论区留言。我会及时更新改正，并上传新的离线文件。

---

目录结构：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30UIT64wukYz4jnLluE1oTib3ycXBicooAGuOOMLLe0NlerrtibcuaV148MA/640?wx_fmt=png&from=appmsg)

---

# 一、身份鉴别

## 1.1 账号管理

```
cat /etc/passwd
```

* • 查看命令结果，第三字段不存在相同数字、用户名不存在相同名称(唯一性)。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30UKOW3JJSU0eTrIJ7QubHsOKnQV9sNe8Jnfib3MeoVeglYIDf6rs5Jw4Q/640?wx_fmt=png&from=appmsg)

## 1.2 登录失败处理

```
cat /etc/pam.d/system-auth /etc/pam.d/password-auth | grep faillock
```

登录失败的处理通常由 `pam_faillock.so` 模块管理，如果存在相关配置会出现如下的显示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30Uiamtx1KsOibOceBINsib4libO2LLCulzuwiaSPbOVhTBkribEacKwbJuzf9Q/640?wx_fmt=png&from=appmsg)

如果不存在，则可以去`/etc/security/faillock.conf`中寻找，相关配置会出现在该文件中。

## 1.3 远程管理通信的加密方法

```
ssh -vvv user@server_ip 2>&1 | grep -E "cipher|MAC|kex algorithm"
```

当前使用SSH时使用的算法【不同网络环境中可能会有变化、如出现加密降级等】

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30USiciaSqqHNFwwAB1SPzhGgic5pDtwyCuxc90pbokvwn69hU2gJgNMJZWA/640?wx_fmt=png&from=appmsg)

* • **Cipher（加密算法）**：`aes256-gcm@openssh.com`
    这是目前 SSH 中**安全性和性能都非常出色**的算法，采用流加密 + Poly1305 消息认证，是 OpenSSH 推荐的默认算法，安全性远高于传统的 AES-CBC。
* • **MAC（消息认证码）**：`<implicit>`
    因为 `aes256-gcm@openssh.com` 是 **AEAD（带关联数据的认证加密）** 算法，它会在加密的同时自动完成消息认证，因此不需要额外配置 MAC，这是更安全的设计。

* • **KEX（密钥交换算法）**

## 1.4 密码复杂度策略

```
grep -E "password|requisite" /etc/pam.d/system-auth /etc/pam.d/password-auth /etc/pam.d/sshd
```

密码复杂度策略通常是通过PAM集成配置中的`pam_pwquality.so`模块进行实现，不做配置的话会出现如图所示的情况：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30UWFgBTlzC8fQhVWd14IdJk3QTWjaaOEKHCpSwLicFt41PhMS90RzBicQw/640?wx_fmt=png&from=appmsg)

密码复杂度配置是由 `libpwquality` 库提供支持：

```
cat /etc/security/pwquality.conf | grep -v "^#\|^$"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30UlWGBjYWHiaYqWsrwNsocecJJYfQgHr7l6GQ8q5UuBAibZHk1TptWxbDw/640?wx_fmt=png&from=appmsg)

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30UHNVaU4RpibZdkszOh7QibIho759XDTiazWPZyBIiaR8k7Fhvq7luBcibBibQ/640?wx_fmt=png&from=appmsg)

```
cat /etc/login.defs | grep "PASS"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30UZhW2pI18qfMiakkyElDKhcdaMVPfGMkjW7cWpl8Avk4VicjJCkhVnfgw/640?wx_fmt=png&from=appmsg)

**参数含义：**

* • PASS\_MAX\_DAYS 90 # 密码最大有效期90天（等保要求）
* • PASS\_MIN\_DAYS 1 # 密码最小修改间隔1天
* • PASS\_WARN\_AGE 7 # 密码过期前7天提醒
* • PASS\_MIN\_LEN 8 # 密码最小长度8位（与PAM配置联动）

## 1.7 登录超时

```
cat /etc/profile | grep "TMOUT"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30Uhp1fG9P3ia3Qd2BANic7yl4WDxdvxdxVGb0uAZY4ZA9qXpPWJ95q9ejg/640?wx_fmt=png&from=appmsg)

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30Ugd7t8bt8q60FfhzVsqZe2AuSL73iaIHExkToxGLrld2KibnW4quVnaHw/640?wx_fmt=png&from=appmsg)

## 2.3 共享账户查询

```
journalctl | grep -E "(Accepted (publickey|password)|session opened for user)"
```

查看日志，可以从同一`fuyuanzi`账户在**不同 IP**（192.168.42.1、xxx.xxx.xxxx.xxx））同时 / 先后登录。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30UswFkTqDMFCmqGEZxrUpJQG3hMIhD2NHRA4KFeegGkJ0eZX4r8DUMgw/640?wx_fmt=png&from=appmsg)

```
w
```

通过查看**当前系统登录用户及用户活动状态**，判断用户的使用是否存在共享状态。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30UFpqgwUSlwibvtAwKxPXRutqoKM2MvvU2z6tsYE23EUic9jia5L92agCiaw/640?wx_fmt=png&from=appmsg)

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

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30UhrxfoXm08ZQ1wbTUCpXcjUenAvfNsjakgVOS1EZF8ibqvZ3Cia5LSb3g/640?wx_fmt=png&from=appmsg)

| umask 值 | 核心用途 | 关键特点 |
| --- | --- | --- |
| 0022 | 通用默认配置 | 平衡安全与可用性 |
| 0002 | 组内协作 | 同组可读写，外部只读 |
| 0077 | 个人敏感数据 | 仅自己可访问 |
| 0222 | 公共只读资源 | 所有人不可修改 |
| 0017 | 部门内部共享 | 仅组内可协作 |
| 0027 | 用于对安全性要求较高的场景 | 大幅限制其他用户的权限，避免敏感文件 / 目录被无关用户访问或修改 |

```
检查 sudo 权限配置（是否存在过度授权）
```

```
cat /etc/sudoers /etc/sudoers.d/* | grep -v "^#\|^$"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30Uaq5f1Via9JXpsx5h086fEsribLnwJzHOdLo8Oqh2BCQqCnVbGBAjpN7w/640?wx_fmt=png&from=appmsg)

**参数含义：**

1. 1. Defaults 全局默认配置

* • `!visiblepw`：不允许在提示时显示密码（防止屏幕泄露）。
* • `always_set_home`：总是设置用户的 HOME 环境变量。
* • `match_group_by_gid`：使用 GID 匹配组权限（提升性能）。
* • `always_query_group_plugin`：查询插件获取用户组信息。
* • `env_reset`：登录时重置环境变量（防止提权）。
* • `env_keep`：保留部分环境变量（如 `LANG`, `PS1`），需注意不要保留危险变量。
* • `secure_path`：设置安全路径（防止恶意 PATH 攻击）。

2. 2. 用户 / 组权限规则

* • `root ALL=(ALL:ALL) ALL`：root 用户可以在任何主机（`ALL`）上，以任何用户（`ALL`）和任何用户组（`ALL`）的身份，执行任何命令（`ALL`）。
* • `%wheel ALL=(ALL) ALL`：允许 `wheel` 组成员使用 sudo 执行任意命令。

## 2.6 访问控制粒度审计

检查用户文件、系统文件、日志文件等文件的访问权限，确认符合最小权限原则。

```
ls -l /etc/passwd /etc/shadow /etc/group /etc/sudoers /root /etc/crontab /var/log/ /var/log/audit/audit.log /var/log/syslog /var/log/messages /var/log/secure
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30UFR1nNr4MlUdiafMCqI5vdH6borZlsxojxHyeH6LAJaIahDSLewJrIrg/640?wx_fmt=png&from=appmsg)

## 2.7 强访问控制状态

```
sestatus  # Enforcing 为正常，Permissive/Disenabled 为异常

getenforce  # Enforcing 为正常，Permissive/Disenabled 为异常
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30UaJziaJ2v2Oj2erHBzwdQ0KeGR3SGH4RyTicW9kenhKfKI96e3B0BTNGg/640?wx_fmt=png&from=appmsg)

# 三、安全审计

## 3.1 检查审计服务是否开启

```
systemctl status auditd

auditctl -l  # 查看审计规则

systemctl status rsyslog
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30UiclxnMQaNwyiaYSnVTDic5gZgXQiamyHaLO1a9icibgCsrGEHe9ialyYwfZYA/640?wx_fmt=png&from=appmsg)

## 3.2 审计记录核查

```
tail -n 20 /var/log/secure

tail -n 20 /var/log/messages

journalctl -n 20
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30UsEGOJHTib4IcYeCWVNLH8WI2HicZ1eoMwt8Nunt6tUcDK7zIqGnxaDtQ/640?wx_fmt=png&from=appmsg)

## 3.3 检查日志轮转配置（防止日志占满磁盘）

```
cat /etc/logrotate.conf /etc/logrotate.d/* | grep -v "^#\|^$"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30U4Bww5B9T2YNYGxnZMnrZib5wpBLeMhzTcLd6Giacrznudvk7mpT2DXzg/640?wx_fmt=png&from=appmsg)

```
du -sh /var/log/messages /var/log/secure 2>/dev/null
# 查看当前核心日志文件实际大小
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/eDTxibgibqtmerkrZBsiax4VgmDPOE4t30UNegYT7Xko...