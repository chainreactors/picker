---
title: Linux安全加固-主机运维
url: https://mp.weixin.qq.com/s/5QqdUPf4sRcUhszNMo70FQ
source: Doonsec's feed
date: 2026-03-28
fetch_date: 2026-03-29T04:32:05.626906
---

# Linux安全加固-主机运维

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/DC4TgvRKhOsl4HWhykvWvgfmEs2lubRx2cutU62yozJMf2zgJuLQ0EJ8ZaZcefYMQicP3LgVgUCNm2wT9ZibUeNmfcrbO7IG60V4dDOCr2uYc/0?wx_fmt=jpeg)

# Linux安全加固-主机运维

原创

Luistin
Luistin

OnePanda-Sec

![]()

在小说阅读器中沉浸阅读

**招新**

**OnePanda-Sec**

**-招新说明-**

**招新要求

· 热爱网络安全，喜欢CTF

**· 拥有CTF比赛经验，有较好比赛成绩的**

· 乐于奉献、热爱分享，愿意提升   自己同时帮助他人

· 时间允许参加各类赛事，服从战队管理与安排

· **各类比赛获奖者、能力出众者视情况考量**

· 未参与其他高校联队

· 大一同学视情况放宽资历要求**

**联系方式**

发送简历于邮箱

· 简历邮箱：2638726415@qq.com

**聘**

# Linux安全加固-主机运维

## 推荐平台

https://www.qsnctf.com/#/main/target

激活这个平台的方法

https://tools.qsnctf.com/

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOtNZZgTwQxNaacKFe1qOEKO2TIZPeT6iaYhYiaIa5JDTX4nibzDZAl5tvorCNfsLAX7EkAClPbNq0UWSt4MASqEznCzI2ERyuL4dM/640?wx_fmt=png&from=appmsg)

## 靶场实操

https://www.qsnctf.com/#/main/target?page=1&category=27&difficulty=&keyword=&user\_answer=&user\_favorite=&tag\_ids=&challenge\_id=1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOskrtl9GIbuxNMBAvckfQGBbTABIqnslXE7yn5nzAdsKDbtCagn98dkOsGFFHpFJclw5cTcry4pvSbzicstqYD4QiaicEAEaGdjvI/640?wx_fmt=png&from=appmsg)

### Linux安全加固-主机运维

```
环境针对Linux安全加固而生产，环境中可能存在一些风险，所以需要进行一定的加固，请根据题目引导进行练习
账号：bus 密码：bus123
```

### 任务1

```
任务名称：修改用户：bus的ssh密码

任务分数：2.00

任务类型：自动校验

用户"bus"存在弱口令风险，需要你进行安全加固，请对此用户进行增强密码操作
```

在加固之前我建议大家都把权限提升到root

```
sudo -i
```

输入bus的密码即可

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOuH50yrbSg6u33XTRxK0KbwQBibI3YoWyrMgcJ6Jzy5RVVtDYFSMkZhZoYflVg51Yw6Lib7SobQ5JCIy75ygazka4Zrbtib6NBS3c/640?wx_fmt=png&from=appmsg)

修改密码为高难度

```
passwd bus
```

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOu82HFbnGP5yxO9P4UPhC3Sgkxia9Wiba5Hn1vwZSicwR6MWSP69tURPxgN3HaGPuYcA2wDScTic1zPJicI0tuun1ibKwetxLibg6MGEk/640?wx_fmt=png&from=appmsg)

### 任务2

```
任务名称：允许root用户ssh远程登录

任务分数：2.00

任务类型：自动校验

服务器由于需要进行远程操作，且需要高权限，需要进行暂时性的开放root用户允许ssh远程登录权限，尽管这是不安全的
```

这是考的linux运维的知识点，也就是在ssh的配置文件里面进行设置

```
vi /etc/ssh/sshd_config
```

`sshd_config` 配置文件的详细表格介绍。这个文件是 OpenSSH 服务器的主配置文件，位于 `/etc/ssh/sshd_config`，用于控制 SSH 服务器的行为和安全参数。

#### `sshd_config` 核心配置参数一览表

#### 基础连接配置

| 配置项 | 默认值 | 作用说明 | 安全建议 |
| --- | --- | --- | --- |
| **Port** | 22 | SSH 服务监听的端口号 | 建议修改为 1024-65535 之间的非标准端口 |
| **AddressFamily** | any | 协议族设置（IPv4/IPv6） | 根据网络环境选择 any/inet/inet6 |
| **ListenAddress** | 0.0.0.0 | 监听地址，默认监听所有网卡 | 多网卡服务器可指定特定 IP |
| **Protocol** | 2 | SSH 协议版本 | 必须使用 Protocol 2（版本 1 有安全漏洞） |

#### 认证方式配置

| 配置项 | 默认值 | 作用说明 | 安全建议 |
| --- | --- | --- | --- |
| **PermitRootLogin** | yes | 是否允许 root 用户 SSH 登录 | **强烈建议设为 no**，使用普通用户登录后切换 |
| **PasswordAuthentication** | yes | 是否允许密码认证 | 高安全环境建议设为 no，改用密钥认证 |
| **PubkeyAuthentication** | yes | 是否允许公钥认证 | 建议保持 yes，作为首选认证方式 |
| **PermitEmptyPasswords** | no | 是否允许空密码登录 | 必须保持 no |
| **MaxAuthTries** | 6 | 每个连接的最大认证尝试次数 | 建议设为 3-5 次，防暴力破解 |
| **MaxSessions** | 10 | 最大允许并发未认证连接数 | 根据服务器性能调整 |
| **LoginGraceTime** | 120s | 登录超时时间（用户必须在此时间内完成认证） | 建议设为 60-120 秒 |

#### 访问控制配置

| 配置项 | 默认值 | 作用说明 | 使用示例 |
| --- | --- | --- | --- |
| **AllowUsers** | 无 | 允许登录的用户白名单 | `AllowUsers alice bob@192.168.1.*` |
| **DenyUsers** | 无 | 禁止登录的用户黑名单 | `DenyUsers mallory` |
| **AllowGroups** | 无 | 允许登录的用户组 | `AllowGroups sshusers` |
| **DenyGroups** | 无 | 禁止登录的用户组 | `DenyGroups badusers` |
| **Match** | 无 | 条件匹配块，可针对特定用户/IP设置不同规则 | 见下方 Match 用法示例 |

#### 连接与性能优化

| 配置项 | 默认值 | 作用说明 | 优化建议 |
| --- | --- | --- | --- |
| **UseDNS** | yes | 是否进行 DNS 反向解析验证客户端主机名 | **建议设为 no**，可加快连接速度 |
| **GSSAPIAuthentication** | yes | 是否启用 GSSAPI 认证 | 如不使用 Kerberos，建议设为 no |
| **TCPKeepAlive** | yes | 是否发送 TCP 保活包检测连接状态 | 保持 yes 防止连接假死 |
| **ClientAliveInterval** | 0 | 服务器向客户端发送保活消息间隔（秒） | 建议设为 300（5分钟） |
| **ClientAliveCountMax** | 3 | 保活检测最大失败次数 | 建议设为 2-3 次 |
| **Compression** | delayed | 是否启用压缩 | 低带宽环境可启用，高带宽建议 no |

#### 转发与隧道配置

| 配置项 | 默认值 | 作用说明 |
| --- | --- | --- |
| **X11Forwarding** | yes | 是否允许 X11 图形界面转发 |
| **AllowTcpForwarding** | yes | 是否允许 TCP 端口转发 |
| **AllowAgentForwarding** | yes | 是否允许 SSH Agent 转发 |
| **GatewayPorts** | no | 是否允许远程端口绑定到非本地地址 |
| **PermitTunnel** | no | 是否允许 tun 设备转发（VPN 隧道） |

#### 日志与监控配置

| 配置项 | 默认值 | 作用说明 | 可选值 |
| --- | --- | --- | --- |
| **SyslogFacility** | AUTHPRIV | 日志设施类型 | AUTH, AUTHPRIV, LOCAL0-LOCAL7 |
| **LogLevel** | INFO | 日志详细程度 | QUIET, FATAL, ERROR, INFO, VERBOSE, DEBUG |
| **PrintMotd** | yes | 登录后是否显示 /etc/motd 欢迎信息 | 建议设为 no（使用 PAM 的 pam\_motd 更灵活） |
| **PrintLastLog** | yes | 是否显示上次登录信息 | 建议保持 yes |

#### 高级安全配置

| 配置项 | 默认值 | 作用说明 |
| --- | --- | --- |
| **HostKey** | /etc/ssh/ssh\_host\_\* | 服务器主机密钥文件路径（RSA/ECDSA/Ed25519） |
| **AuthorizedKeysFile** | .ssh/authorized\_keys | 用户公钥存放位置 |
| **StrictModes** | yes | 是否严格检查用户密钥文件权限 |
| **Banner** | none | 登录前显示的警告信息文件路径 |
| **ChrootDirectory** | none | 将用户限制在指定目录（SFTP 监狱） |
| **ForceCommand** | none | 强制用户只能执行特定命令 |

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOvYHGh4f9uCu7m0vwakbN5FBg6r0CBNGOia7GygOZInbqCiadu05JChEsEW6TpZ1H2C1zP5I6K83rDJ2JicRdljdmHicckdKLqdMq8/640?wx_fmt=png&from=appmsg)

找到这一行代码，也就是在33行，建议大家可以把序号打开，E光标模式下:set number，当然也可以:set num，修改完了之后记得:wq保存

```
#PermitRootLogin prohibit-password
修改为
PermitRootLogin yes
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOsuY8opW0VjzqUZsg2l1pEOlia6RZ0Laia0vXso9nhnTptfVTGF3WCmSeL5jWA8H9mmMXgD0k3oW05otezicsqrCgQRcPu1GMIeUk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOuBhQWUf8ExacAYJ0JDQMZ6TaIsxftdhFqVVJPpgSzTVZDfEnsSIZTuUVmmuAnesJBibZzDNvc6bNUIwHUzePvIQqN86LMCSQZg/640?wx_fmt=png&from=appmsg)

### 任务3

```
任务名称：运维远程完毕，可关闭root用户的ssh远程权限

任务分数：3.00

任务类型：自动校验

允许root远程登录是危险的，所以运维完成远程操作后，可立即将root用户ssh远程权限关闭
```

这个和上面那个其实是重复了一半，就是把上面那个yes修改为no

PermitRootLogin yes 修改为 PermitRootLogin no

然后:wq保存

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOsXsYr6kkOKYBjlErW0lBkxtZANpHX7ibOCAND7dgfE1sEsm9iapQ4AZaWROKpszwqRsfZicIJUicD0hWhD7kFQfHv5YVxhcb4tgl8/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOuaaBZib1UmnnRfT8k3QBHHLuMDuOnszpqeCBqviaVYz1cTXQXCrssZADggdtX2UR9bgibzGIiaFUbxFh0PW7VhrawxXRlHOGl4Yxc/640?wx_fmt=png&from=appmsg)

### 任务4

```
任务名称：创建新用户并配置SSH私钥

任务分数：2.00

任务类型：自动校验

为了让主机远程连接安全更进一步，请创建一个back用户并修改它的密码，最终生成这个用户的私钥，后续可以利用私钥让运维远程连接更安全
```

首先新建一个名字叫back的用户

```
useradd -m back
```

| 命令 | 是否创建家目录 | 是否复制配置文件 | 适用场景 |
| --- | --- | --- | --- |
| `useradd username` | 否 | 否 | 创建系统账户/服务账户，不需要登录 |
| `useradd -m username` | 是 | 是（从 `/etc/skel` 复制） | 创建普通登录用户 |
| `useradd -m -d /path username` | 是（指定路径） | 是 | 自定义家目录位置 |
| `adduser username` | 是 | 是 | 交互式创建（Debian/Ubuntu 推荐） |

![](https://mmbiz.qpic.cn/mmbiz_png/DC4TgvRKhOvOMdkfUnC8CwtsiapichNZQYOSRaVXicEho8Swe6mR5ibS5ictvgeLeNWo8T5XMr8Q1aGhK3c6CPWNVLcF3QpJ8GXLyuIAWvsQWVPc/640?wx_fmt=png&from=appmsg)

然后切换到back用户

```
su back
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/DC4TgvRKhOs4hPicbg3QFD2fYFh29zvfPWWbINoVFP3v2ibvxUJ6n5CPobzfic8SZwUy1XnFZ048NLRHAavPNMQj8jEhbSkuHqvVWR8fmj1sjM/640?wx_fmt=png&from=appmsg)

生成ssh密钥对

```
ssh-keygen -t rsa -b 4096
```

| 参数 | 全称 | 作用说明 | 推荐值 |
| --- | --- | --- | --- |
| `-t rsa` | `--type rsa` | 指定密钥算法类型为 RSA | RSA / ECDSA / Ed25519 |
| `-b 4096` | `--bits 4096` | 指定密钥位数（仅 RSA/DSA 有效） | 2048 / 3072 / **4096** |
| `-f filename` | `--filename` | 指定密钥文件名 | 默认 `~/.ssh/id_rsa` |
| `-C comment` | `--comment` | 添加密钥注释（通常用邮箱） | `user@example.com` |
| `-N passphrase` | `--new-passphrase` | 设置私钥密码（加密私钥） | 建议设置 |
| `-P oldpass` | `--old-passphrase` | 更改现有私钥密码时使用 | 密钥管理 |
| `-p` | `--change-passphrase` | 修改私钥密码 | 密钥维护 |
| `-y` | `--yield` | 从私钥提取公钥 | 公钥恢复 |
| `-l` | `--fingerprint` | 显示密钥指纹 | 密钥验证 |
| `-E hash` | `--hash` | 指定指纹哈希算法 | `md5` / `sha256` |

```
$ ssh-keygen-t rsa -b4096
Generating public/private rsa key pair.
Enter file in which to save the key (/home/user/.ssh/id_rsa):  # 按回车使用默认路径
Enter passphrase (empty for no passphrase):                     # 输入密码（推荐设置）
Enter same passphrase again:                                    # 确认密码
Your identification has been saved in /home/user/.ssh/id_rsa    # 私钥
Your public key has been saved in /home/user/.ssh/id_rsa.pub   # 公钥
```

![](https://mmbiz.qpic.cn/mmbiz...