---
title: CentOS下Pure-ftp安装配置
url: https://blog.upx8.com/3102
source: 黑海洋 - WIKI
date: 2022-11-22
fetch_date: 2025-10-03T23:24:15.403087
---

# CentOS下Pure-ftp安装配置

# [黑海洋 - Wiki](/ "黑海洋 - Wiki - 点击返回首页")

# CentOS下Pure-ftp安装配置

发布时间:
2022-11-21

分类:
[Web开发/Code](https://blog.upx8.com/code/)

热度:
10977

## 一、安装 pure-ftp

```
#默认的yum源不包含pure-ftpd，需先安装epel扩展源
yum install -y epel-release
yum install -y pure-ftpd
```

## 二、配置 pure-ftp

### 1、创建 ftp 系统用户

```
# 创建用户 ftp
useradd ftp -s /sbin/nologin
```

### 2、配置FTP存储根目录

```
# 创建 FTP 存储根目录
mkdir /data/ftp

# 设置 FTP 根目录权限
chown -R ftp.ftp /data/ftp/
```

### 3、编辑 pure-ftp 配置文件

编辑 pure-ftp 配置文件 `/etc/pure-ftpd/pure-ftpd.conf` 部分参数如下：

```
# PureDB 用户数据库路径(重要)
PureDB                       /etc/pure-ftpd/pureftpd.pdb

# 锁定所有用户到家目录中
ChrootEveryone               yes

# 如果虚拟用户的目录不存在则自动创建
CreateHomeDir                yes

# 兼容不同客户端
BrokenClientsCompatibility   yes

# 显示隐藏文件
DisplayDotFiles              no

# 防止命令误操作
CustomerProof                yes

# 被动模式端口范围
PassivePortRange             30000 50000

# 被动模式 IP
ForcePassiveIP               192.168.1.100

# 只允许匿名用户访问
AnonymousOnly                no

# 不允许匿名用户访问(为 no 时允许)
NoAnonymous                  yes

# 不允许匿名用户上传文件(为 no 时允许)
AnonymousCantUpload          yes

# 不允许匿名用户创建目录(为 no 时允许)
AnonymousCanCreateDirs       yes

# 仅运行认证用户进行FXP传输
AllowUserFXP                 no

# 对匿名用户和非匿名用户允许进行匿名 FXP 传输
AllowAnonymousFXP            no

# 设置日志的告警级别,默认为 ftp,none 是禁止记录日志
SyslogFacility               none
```

### 4、创建 ftp 虚拟用户

```
# 创建 ftp 用户 aaa 家目录
mkdir /data/ftp/aaa
chown -R ftp.ftp /data/ftp/aaa/

# 创建 ftp 用户 aaa, -u 是将虚拟用户 aaa 与系统用户 ftp 关联在一起，aaa 账号登录后是以 ftp 的身份来读取和下载文件,-d 是指定ftp_usera账户的家目录，这样可以使用户 aaa 只能访问其家目录 /data/ftp/aaa/。
pure-pw useradd aaa -u ftp -d /data/ftp/aaa/

# 创建用户信息数据库文件,这一步很关键。
pure-pw mkdb

# 查看已创建的账号列表
pure-pw list
```

### 5、启动 pure-ftp 服务

```
# 启动 pure-ftp 服务
systemctl start pure-ftpd.service

# 添加开机启动项
systemctl enable pure-ftpd.service

# 或使用
systemctl enable --now pure-ftpd.service
```

### 6、使用客户端测试连接

使用 Windows 或 Linux 客户端登录 FTP 测试服务是否正常。

## 三、配置文件 `/etc/pure-ftpd/pure-ftpd.conf` 完整参数说明

############################################################
# #
# Configuration file for pure-ftpd wrappers #
# #
############################################################

# If you want to run Pure-FTPd with this configuration
# instead of command-line options, please run the
# following command :
#
# /usr/local/pureftpd/sbin/pure-config.pl /usr/local/pureftpd/etc/pure-ftpd.conf
#
# Please don't forget to have a look at documentation at
# http://www.pureftpd.org/documentation.shtml for a complete list of
# options.

# Cage in every user in his home directory
# 锁定所有用户到家目录中
ChrootEveryone yes

# If the previous option is set to "no", members of the following group
# won't be caged. Others will be. If you don't want chroot()ing anyone,
# just comment out ChrootEveryone and TrustedGID.
# 信任组ID100，可以不锁定
# TrustedGID 100

# Turn on compatibility hacks for broken clients
# 兼容不同客户端
BrokenClientsCompatibility no

# Maximum number of simultaneous users
# 最大的客户端数量
MaxClientsNumber 50

# Fork in background
# 后台运行
Daemonize yes

# Maximum number of sim clients with the same IP address
# 每个ip最大连接数
MaxClientsPerIP 8

# If you want to log all client commands, set this to "yes".
# This directive can be duplicated to also log server responses.
# 记录日志
VerboseLog no

# List dot-files even when the client doesn't send "-a".
# 显示隐藏文件
DisplayDotFiles no

# Don't allow authenticated users - have a public anonymous FTP only.
# 只允许匿名用户访问
AnonymousOnly no

# Disallow anonymous connections. Only allow authenticated users.
# 不允许匿名用户
NoAnonymous yes

# Syslog facility (auth, authpriv, daemon, ftp, security, user, local\*)
# The default facility is "ftp". "none" disables logging.
# 设置日志的告警级别，默认为ftp，none是禁止记录日志
SyslogFacility ftp

# Display fortune cookies
# 定制用户登陆后的显示信息
# FortunesFile /usr/share/fortune/zippy

# Don't resolve host names in log files. Logs are less verbose, but
# it uses less bandwidth. Set this to "yes" on very busy servers or
# if you don't have a working DNS.
# 是否在日志文件中进行主机名解析，不进行客户端DNS解析
DontResolve yes

# Maximum idle time in minutes (default = 15 minutes)
# 最大空闲时间
MaxIdleTime 30

# LDAP configuration file (see README.LDAP)
# LDAP 配置文件路径
# LDAPConfigFile /etc/pureftpd-ldap.conf

# MySQL configuration file (see README.MySQL)
# MySQL 配置文件路径
 MySQLConfigFile /usr/local/pureftpd/etc/pureftpd-mysql.conf

# Postgres configuration file (see README.PGSQL)
# Postgres 配置文件路径
# PGSQLConfigFile /etc/pureftpd-pgsql.conf

# PureDB user database (see README.Virtual-Users)
# PureDB 用户数据库路径
 PureDB /usr/local/pureftpd/etc/pureftpd.pdb

# Path to pure-authd socket (see README.Authentication-Modules)
# pure-authd 的socket 路径
# ExtAuth /var/run/ftpd.sock

# If you want to enable PAM authentication, uncomment the following line
# 如果你要启用 PAM 认证方式, 去掉下面行的注释
# PAMAuthentication yes

# If you want simple Unix (/etc/passwd) authentication, uncomment this
# 如果你要启用 简单的 Unix系统 认证方式(/etc/passwd), 去掉下面行的注释
# UnixAuthentication yes

# Please note that LDAPConfigFile, MySQLConfigFile, PAMAuthentication and
# UnixAuthentication can be used only once, but they can be combined
# together. For instance, if you use MySQLConfigFile, then UnixAuthentication,
# the SQL server will be asked. If the SQL authentication fails because the
# user wasn't found, another try # will be done with /etc/passwd and
# /etc/shadow. If the SQL authentication fails because the password was wrong,
# the authentication chain stops here. Authentication methods are chained in
# the order they are given.

# 'ls' recursion limits. The first argument is the maximum number of
# files to be displayed. The second one is the max subdirectories depth
# 'ls' 命令的递归限制。第一个参数给出文件显示的最大数目。第二个参数给出最大的子目录深度。
LimitRecursion 10000 8

# Are anonymous users allowed to create new directories ?
# 是否允许匿名用户创建新目录
AnonymousCanCreateDirs no

# If the system is more loaded than the following value,
# anonymous users aren't allowed to download.
# 超出负载后禁止下载
MaxLoad 4

# Port range for passive connections replies. - for firewalling.
# 被动模式的端口范围
# PassivePortRange 30000 50000

# Force an IP address in PASV/EPSV/SPSV replies. - for NAT.
# Symbolic host names are also accepted for gateways with dynamic IP
# addresses.
# 强制一个IP地址使用被动响应
# ForcePassiveIP 192.168.0.1

# Upload/download ratio for anonymous users.
# 匿名用户的上传/下载的比率
# AnonymousRatio 1 10

# Upload/download ratio for all users.
# This directive superscedes the previous one.
# 所有用户的上传/下载的比率
# UserRatio 1 10

# Disallow downloading of files owned by "ftp", ie.
# files that were uploaded but not validated by a local admin.
# 禁止下载匿名用户上传但未经验证的文件
AntiWarez yes

# IP address/port to listen to (default=all IP and port 21).
# 服务监听的IP 地址和端口。(默认是所有IP地址和21端口)
# Bind 127.0.0.1,21

# Maximum bandwidth for anonymous users in KB/s
# 匿名用户带宽限制（KB）
# AnonymousBandwidth 8

# Maximum bandwidth for \*all\* users (including anonymous) in KB/s
# Use AnonymousBandwidth \*or\* UserBandwidth, both makes no sense.
# 所有用户的最大带宽（KB/s），包括匿名用户。
 UserBandwidth 1024

# File creation mask. <umask for files>:<umask for dirs> .
# 177:077 if you feel paranoid.
# 新建目录及文件的属性掩码值
Umask 133:022

# Minimum UID for an authenticated user to log in.
# 认证用户允许登陆的最小组ID（UID）
MinUID 100

# Allow FXP transfers for authenticated users.
# 仅允许认证用户进行 FXP 传输。
AllowUserFXP no

# Allow anonymous FXP for anonymous and non-anonymous users.
# 对匿名用户和非匿名用户允许进行匿名 FXP 传输
AllowAnonymousFXP no

# Users can't delete/write files beginning with a dot ('.')
# even if they own them. If TrustedGID is enabled, this group
# will have access to dot-files, though.
# 不能删除/写入隐藏文件
ProhibitDotFilesWrite no

# Prohibit \*reading\* of files beginning with a dot (.history, .ssh...)
# 禁止读取隐藏文件
ProhibitDotFilesRead no

# Never overwrite files. When a file whose name already exist is uploaded,
# it get automatically renamed to file.1, file.2, file.3, ...
# 有同名文件时自动重新命名
AutoRename no

# Disallow anonymous users to upload new files (no = upload is allowed)
# 不允许匿名用户上传文件
AnonymousCantUpload no

# Only connections to this specific IP address are allowed t...