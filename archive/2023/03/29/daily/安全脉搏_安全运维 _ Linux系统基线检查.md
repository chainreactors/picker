---
title: 安全运维 | Linux系统基线检查
url: https://www.secpulse.com/archives/198328.html
source: 安全脉搏
date: 2023-03-29
fetch_date: 2025-10-04T10:58:29.307549
---

# 安全运维 | Linux系统基线检查

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# 安全运维 | Linux系统基线检查

[系统安全](https://www.secpulse.com/archives/category/articles/system)

[贝塔安全实验室](https://www.secpulse.com/newpage/author?author_id=9525)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-03-28

35,458

声明：本人坚决反对利用文章内容进行恶意攻击行为，一切错误行为必将受到惩罚，绿色网络需要靠我们共同维护，推荐大家在了解技术原理的前提下，更好的维护个人信息安全、企业安全、国家安全。

*1*

查询系统信息

#### 1. Linux 查看内核版本（大于2.6）（I级）

```
uname -a
cat /proc/version
```

#### 2. Linux 查看系统版本

```
lsb_release -a
cat /etc/issue
```

###

*2*

身份鉴别

#### 1. 系统是否存在重复的 UID（II级）

UID(UserID)——用户标识号，它与用户名唯一对应，Linux 以 UID 作为用户的唯一标识，Linux中超级用户 root 的 UID 为 0，可以直接使用 id 命令查看当前用户的 UID。可以查看 passwd 文件以查看所有用户的 UID 等基本信息：

```
vim /etc/passwd
```

*3*

密码审查

#### 密码的生命周期最大为 90 天（III级）

#### 密码可以被立即修改（III级）

#### 密码的最小长度为 8 位（III级）

#### 密码到期的提醒，一般建议 7 天（III级）

查看并修改 login.defs 文件：

```
vim /etc/login.defs
```

检查并修改如下内容：

```
PASS_MAX_DAYS 90 #一个密码可使用的最大天数
PASS_MIN_DAYS 0 #两次密码修改之间最小的间隔天数
PASS_MIN_LEN 8 #密码最小长度
PASS_WARN_AGE 7 #密码过期前给出警告的天数
```

*4*

访问控制

#### 1. 系统已设定了正确的 umask 值 022 (III级）

umask 用于指定目前用户在建立文件或目录时的权限默认值，umask 设置的是权限值的“补码”，而我们常用的`chmod`设置的是文件权限码,默认情况下的 umask 值是022(可以用umask命令查看），此时你建立的文件默认权限是644(6-0,6-2,6-2)，建立的目录的默认权限是755(7-0,7-2,7-2)。

#### 2. 锁定系统中不必要的用户（IV级）

使用 passwd 命令锁定、解锁和检查 Linux 中用户账户的状

```
passwd -l username #锁定用户账户
passwd -u username #解锁用户账户
passwd -S username #检查用户账户锁定状态
```

使用 usermod 命令锁定、解锁和检查 Linux 中用户账户的状态：

```
usermod --lock username #锁定用户账户
usermod -L username #锁定用户账户
usermod -unlock username #解锁用户账户
usermod -U username #解锁用户账户
```

可以通过查看 **/etc/shadow** 文件来检查用户锁定状态，如果用户账户被锁定，密码前面将添加感叹号。

#### 3. 删除不必要的系统用户组（IV级）

```
groupdel groupname
```

这个命令将会从 /etc/group 和 /etc/gshadow 文件中移除用户组条目，且成功时不会打印任何输出。可以通过使用下面的命令来验证用户组是否被移除：

```
getent group
```

4. 禁止 root 用户远程登录（II级）

通过修改 /etc/ssh/sshd\_congig 文件，将其中的 PermitRootLogin 改成 no，然后重新启动 ssh 服务就可以了：

```
systemctl restart sshd.service
```

#### 5. 系统重要文件访问权限是否为 644 或 600（II级）

*5*

安全审计

#### 1. 系统是否启用安全审计（III级)

Linux audit 子系统是一个用于收集记录系统、内核、用户进程发生的行为事件的一种安全审计系统，该系统可以可靠的收集有关的任何与安全相关（或与安全无关）事件的信息，它可以帮助跟踪系统上执行过的一些操作。

```
auditctl -s #查看系统是否启用 audit，enabled 值为 1 表示开启
systemctl start auditd #启动 auditd 服务
```

开启了 auditd 服务后，所有的审计日志会被记录在 **/var/log/audit/audit.log** 文件中，该文件记录格式是每行以 type 开头。

#### 2. 是否启用审计策略（III级）

一般针对系统的目录、退出、创建/删除目录、修改密码、添加组、计划任务等。audit 可以自定义对指定的文件或命令进行审计（如监视 `rm` 命令被执行、/etc/passwd 文件内容被改变），只要配置号对应规则即可，配置规则可以通过命令行（临时生效）或编辑配置文件（永久生效）两种方式实现。auditd 的配置文件为 **/etc/audit/audit** 下的 **auditd.conf** 和 **audit.rules**, auditd.conf 主要定义了 auditd 服务日志的性能等相关配置，audit.rules 才是定义规则的文件。

*6*

剩余价值保护

#### 1. 系统的命令行数是否保存为 30 条（IV级）

```
echo $HISTSIZE #查看历史命令保存条数
```

修改历史命令保存条数，修改 /etc/profile 中的 HISTSIZE 变量即可。

*7*

不必要服务启动项

#### 1. chargen/chargen-udp、daytime/daytime-udp、echo/echo-udp、time/time-udp 等服务已被禁用（III级）

chargen 服务：最初设计用于测试网络状态，监听19端口（包括TCP和UDP），其中UDP协议存在“Chargen UDP服务远程拒绝服务攻击漏洞”。chargen一般不会使用，所以直接将该服务关闭即可。

daytime 服务：使用TCP 协议的 Daytime 守护进程，该协议为客户机实现从远程服务器获取日期和时间的功能。
daytime-udp 服务：使用 UDP 协议的 Daytime 守护进程。

echo 服务：使用 TCP 协议的服务器回显客户数据服务守护进程；
echo-udp 服务：使用 UDP 协议的服务器回显客户数据服务守护进程。

time 服务：采用 TCP 协议的从远程主机获取时间和日期的守护进程；
time-udp 服务：采用 UDP 协议的从远程主机火气时间和日期的守护进程。

#### 2. cpus-lpd 服务已被禁用（III级）

cups 服务：通用 UNIX 打印守护进程，为Linux提供第三代打印功能；
cups-lpd 服务：cups 行打印守护进程。

#### 3. finger 服务已被禁用（III级）

finger 服务：finger 服务器提供一项查询本地或远程主机用户公开信息的服务。

#### 4. rexec 服务已被禁用（III级）

rexec 服务：允许网络用户远程执行命令。由于rexecd并没有提供好的认证方式，认证体系相当简单而易受攻击，因此它可能被攻击者用来扫描第三方的主机，攻击者可以通过该服务远程暴力穷举猜测用户名、口令，也可以监听其它授权用户的通信过程以获取口令明文，可以使用nmap 等工具进行扫描检测。

#### 5. rlogin 服务已被禁用（III级）

rlogin 服务：远程登陆服务，通过 rlogin 命令，可以登录到远程系统。rlogin服务的认证体系相当简单而易受攻击，攻击者可以通过该服务远程暴力穷举猜测用户名、口令，也可以监听其它授权用户的通信过程以获取口令明文。

#### 6. rsh 服务已被禁用（III级）

rsh 服务：远程 shell 服务，通过 rsh 命令，可以在指定的远程主机上启动一个 shell 并执行用户在 rsh 命令行中指定的命令，如果用户没有给出要执行的命令，rsh就用 rlogin 命令使用户登录到远程机上。

#### 7. rsync 服务已被禁用（II级）

rsync 服务：远程数据同步服务，通过 rsync 命令，可以通过LAN/WAN快速同步多台主机间的文件。rsync使用所谓的“rsync算法”来使本地和远程两个主机之间的文件达到同步，这个算法只传送两个文件的不同部分，而不是每次都整份传送，因此速度相当快。

#### 8. ntalk 服务已被禁用（III级）

ntalk 服务：网络交谈（ntalk），远程对话服务和客户。

#### 9. talk 服务已被禁用（III级）

talk 服务：远程对话服务和客户。

#### 10. wu-ftpd 服务已被禁用（II级）

Wu-ftpd 服务：Internet上最流行的FTP守护程序。Wu-ftpd功能十分强大，可以构建多种类型FTP服务器。Wu-ftpd菜单可以帮助用户轻松地实现对FTP服务器的配置：支持构造安全方式的匿名FTP的访问，可以控制同时访问的用户的数量，限制可以允许访问的IP网段，并可以在一台主机上设置多个虚拟目录。

#### 11. tftp 服务已被禁用（III级）

tftp 服务：TCP/IP协议族中的一个用来在客户机与服务器之间进行简单文件传输的协议，提供不复杂、开销不大的文件传输服务。基于 UDP 协议实现，端口号为69。

#### 12. ipop2 服务已被禁用（III级）

ipop2 服务：POP2 邮件服务器。

#### 13. ipop3 服务已被禁用（III级）

ipop3 服务：POP3 邮件服务器。

#### 14. telnet 服务已被禁用（III级）

telnet 服务：Internet 远程登录服务。

#### 15. xinetd 服务已被禁用（IV级）

xinted 服务：新一代的网络守护进程服务程序，又叫超级Internet服务器，常用来管理多种轻量级Internet服务。

*8*

其它配置检查

#### 1. 系统已经加固了 TCP/IP 协议栈（IV级）

检查/etc/sysctl.conf是否存在以下内容：

```
net.ipv4.tcp_max_syn_backlog=4096
net.ipv4.conf.all.rp_filter=1
net.ipv4.conf.accept_source_route=0
net.ipv4.conf.all.accept_redirects=0
net.ipv4.conf.secure_redirects=0
net.ipv4.conf.default.accept_source_route=0
net.ipv4.conf.default.accept_redirects=0
net.ipv4.conf.default.secure_redirects=0
```

2. 系统禁用 X-Windows 系统（III级）

#### 3. 移动介质使用 nosuid 挂载（IV级）

检查与 **/etc/fstab** 文件夹、**/dev/floppy** 和 **/dev/cdrom** 相关的条目

#### 4. /tmp 和 /var/tmp 目录具有粘滞位(II级)

```
ls -al/ | grep tmp
```

#### 5. root PATH 环境变量，不包含当前目录（II级）

```
echo $PATH
```

-END-

**本文作者：[贝塔安全实验室](newpage/author?author_id=9525)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/198328.html**](https://www.secpulse.com/archives/198328.html)

Tags: [Linux系统](https://www.secpulse.com/archives/tag/linux%E7%B3%BB%E7%BB%9F)、[uid](https://www.secpulse.com/archives/tag/uid)、[安全审计](https://www.secpulse.com/archives/tag/%E5%AE%89%E5%85%A8%E5%AE%A1%E8%AE%A1)、[服务禁用](https://www.secpulse.com/archives/tag/%E6%9C%8D%E5%8A%A1%E7%A6%81%E7%94%A8)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![30-50K｜货拉拉招资深安全运营、合规、终端和数据安全工程师](https://secpu...