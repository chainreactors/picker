---
title: Linux内核的SELinux安全机制分析
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247499489&idx=1&sn=b7cb356765281745d2672b16583e15c6&chksm=fa522b5fcd25a249fe614a72361536f6297f23b56d9dc104ab4d78ce8ee0cd652b9b88b0572e&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2023-01-14
fetch_date: 2025-10-04T03:53:38.061819
---

# Linux内核的SELinux安全机制分析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnS3ajSxkicv4Pm4rbFD1ng3ic1E5svKjnwBPRxoibWXCVmgPXlJkibeNbuxVyayU1Cx132iciaIE8icEW7MA/0?wx_fmt=jpeg)

# Linux内核的SELinux安全机制分析

B2eFly

山石网科安全技术研究院

**0****1**

**前言‍‍‍‍**

SELinux(Security-Enhanced Linux-安全增强型Linux)，是一个在Linux内核中实践的强制存取控制安全性机制，也是Linux的一个安全子系统。

**02****‍**

**基本概念‍‍‍‍**

SeLinux主要由以下四个部分组成

* Subject - 系统中运行的程序，每个Subject都有安全属性通过Security Context表示
* Object - 系统中各种资源，如文件、网络等，每个Object都有安全属性通过Security Context表示
* Policy & Rule - 进程主体需要如何管制以及如何管制都有Policy定义
* Security Context - SeLinux核心。运行在Linux系统内核中。根据Selinux策略，检查Subjects的安全属性与Objects的安全属性是否匹配，从而决定Subjects是否能够访问objects

**03****‍**

**工作模式‍‍‍‍**

SELinux有三种工作模式

* enforcing - 强制模式 -违反规则的行为被阻止将被记录到日志中
* permissive - 宽容模式- 违反规则的行为只会记录到日志中去
* disabled - 关闭SELinux

**04****‍**

**工作流程‍‍‍‍**

一个主体要访问一个对象，Linux内核会首先检查主体权限，来决定是否能访问文件。如果文件的属性不允许执行访问则拒绝，不再检查SELinux上下文。如果该文件属性运行执行访问，那么SELinux会先读取进程和文件的上下文，查询相应规则，并按照规则执行，将访问错误的信息记录到日志中去。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRsEwL0XFtSvUQPRFw7fUfT4tOMaBMzCKTcjQPu1BQN0FvGOMJWy5r98Kibk51Yiat88y81k0bQwmmA/640?wx_fmt=png)

**05****‍**

**环境搭建（Centos为例）‍‍‍‍**

**5.1 检查Selinux状态**

```
$ sestatus
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRsEwL0XFtSvUQPRFw7fUfTNQibRia67wYzCmWln6oiav3nskz9PVYlhCYpHYUcJnIKpABkKPibkBWKng/640?wx_fmt=png)

状态显示服务处于强制执行模式。

### 5.2 测试SeLinux是否生效

安装httpd服务器

```
$ yum -y httpd
#允许防火墙 访问web服务
$ firewall-cmd --permanent --add-service=http
$ firewall-cmd --reload
$ mkdir /home/wwwroot
$ ehoc "This is SELinux" > /home/wwwroot/index.html
#启动httpd服务器
$ systemctl start httpd
```

修改httpd服务的配置文件

```
DocumentRoot "/home/wwwroot"
<Directory "/home/wwwroot">
....
</Directory>
```

访问Web服务 - 拒绝

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRsEwL0XFtSvUQPRFw7fUfTDXVkQshsVWlBRm5icXWhka4edq5KHIicm8ib82EibiaFSWfwRicicc4Jy2icFA/640?wx_fmt=png)

关闭selinux看是否能够访问

```
$ setenforce 0
```

访问Web服务 - 成功访问

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRsEwL0XFtSvUQPRFw7fUfTCrTjNKyg92SLwD1E5taLZuGdPcClxl9h3k2ZqqjB5icVdHxOc3h3aVw/640?wx_fmt=png)

### 5.3 设置安全上下文

**查看/home/wwwroot与/var/www/html安全上下文**

```
$ ls -Zd /var/www/html
drwxr-xr-x. root root system_u:object_r:httpd_sys_content_t:s0 /var/www/html
$ ls -Zd /home/wwwroot/
drwxr-xr-x. root root unconfined_u:object_r:home_root_t:s0 /home/wwwroot/
```

SELinux安全上下文由用户段、角色段和类型段等多个信息项组成

* system\_u -> 系统进程身份
* object\_r -> 文件目录角色
* httpd\_sys\_content\_t -> 网站服务系统文件

**设置安全上下文**

```
$ yum -y install policycoreutils-python.x86_64
$ semanage fcontext -a -t httpd_sys_content_t /home/wwwroot
$ semanage fcontext -a -t httpd_sys_content_T /home/wwwroot/*
$ restorecon -Rv /home/wwwroot/
restorecon reset /home/wwwroot context unconfined_u:object_r:home_root_t:s0->unconfined_u:object_r:httpd_sys_content_t:s0
restorecon reset /home/wwwroot/index.html context unconfined_u:object_r:home_root_t:s0->unconfined_u:object_r:httpd_sys_content_t:s0
```

访问web服务

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRsEwL0XFtSvUQPRFw7fUfTCrTjNKyg92SLwD1E5taLZuGdPcClxl9h3k2ZqqjB5icVdHxOc3h3aVw/640?wx_fmt=png)

### 5.4 SELinux域生效

#### 5.4.1 开启HTTPD服务个人用户主页功能

修改/etc/httpd/conf.d/userdir.conf文件

```
#
# UserDir: The name of the directory that is appended onto a user's home
# directory if a ~user request is received.
#
# The path to the end user account 'public_html' directory must be
# accessible to the webserver userid.  This usually means that ~userid
# must have permissions of 711, ~userid/public_html must have permissions
# of 755, and documents contained therein must be world-readable.
# Otherwise, the client will only receive a "403 Forbidden" message.
#
<IfModule mod_userdir.c>
    #
    # UserDir is disabled by default since it can confirm the presence
    # of a username on the system (depending on home directory
    # permissions).
    #
#    UserDir disabled

    #
    # To enable requests to /~user/ to serve the user's public_html
    # directory, remove the "UserDir disabled" line above, and uncomment
    # the following line instead:
    #
    UserDir public_html
</IfModule>

#
# Control access to UserDir directories.  The following is an example
# for a site where these directories are restricted to read-only.
#
<Directory "/home/*/public_html">
    AllowOverride FileInfo AuthConfig Limit Indexes
    Options MultiViews Indexes SymLinksIfOwnerMatch IncludesNoExec
    Require method GET POST OPTIONS
</Directory>
```

查看http协议相关的安全策略

```
$ getsebool -a | grep http
httpd_anon_write --> off
httpd_builtin_scripting --> on
httpd_can_check_spam --> off
httpd_can_connect_ftp --> off
httpd_can_connect_ldap --> off
httpd_can_connect_mythtv --> off
httpd_can_connect_zabbix --> off
httpd_can_network_connect --> off
httpd_can_network_connect_cobbler --> off
httpd_can_network_connect_db --> off
httpd_can_network_memcache --> off
httpd_can_network_relay --> off
httpd_can_sendmail --> off
httpd_dbus_avahi --> off
httpd_dbus_sssd --> off
httpd_dontaudit_search_dirs --> off
httpd_enable_cgi --> on
httpd_enable_ftp_server --> off
httpd_enable_homedirs --> off
httpd_execmem --> off
httpd_graceful_shutdown --> on
httpd_manage_ipa --> off
httpd_mod_auth_ntlm_winbind --> off
httpd_mod_auth_pam --> off
httpd_read_user_content --> off
httpd_run_ipa --> off
httpd_run_preupgrade --> off
httpd_run_stickshift --> off
httpd_serve_cobbler_files --> off
httpd_setrlimit --> off
httpd_ssi_exec --> off
httpd_sys_script_anon_write --> off
httpd_tmp_exec --> off
httpd_tty_comm --> off
httpd_unified --> off
httpd_use_cifs --> off
httpd_use_fusefs --> off
httpd_use_gpg --> off
httpd_use_nfs --> off
httpd_use_openstack --> off
httpd_use_sasl --> off
httpd_verify_dns --> off
named_tcp_bind_http_port --> off
prosody_bind_http_port --> off
```

修改httpd\_enable\_homedirs为on

```
$ setsebool -P httpd_enable_homedirs=on
```

访问web服务

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRsEwL0XFtSvUQPRFw7fUfTxeX7xEcwmbUvricOxvJia8WVTicQ4RcLYlXfH83Gj1XCH3tXic0XN9V5og/640?wx_fmt=png)

#### 5.4.2 配置基于端口号的多站点

创建目录及文件

```
$ mkdir -p /home/wwwroot/7777
$ mkdir -p /home/wwwroot/8888
$ echo "Test Port:7777" > /home/wwwroot/7777/index.html
$ echo "Test Port:8888" > /home/wwwroot/8888/index.html
```

需改配置文件/etc/httpd/conf/httpd.conf

```
<VirtualHost 192.168.24.128:7777>
        DocumentRoot /home/wwwroot/7777
        ServerName www.neuron.com
        <Directory "/home/wwwroot/7777">
                AllowOverride None
                Require all granted
        </Directory>
</VirtualHost>

<VirtualHost 192.168.24.128:8888>
        DocumentRoot /home/wwwroot/8888
        ServerName bbs.neuron.com
        <Directory "/home/wwwroot/8888">
                AllowOverride None
                Require all granted
        </Directory>
</Virtual>
```

查看selinux服务允许的端口列表

```
$ semanage port -l | grep http
http_cache_port_t              tcp      8080, 8118, 8123, 10001-10010
http_cache_port_t              udp      3130
http_port_t                    tcp      80, 81, 443, 488, 8008, 8009, 8443, 9000
pegasus_http_port_t            tcp      5988
pegasus_https_port_t           tcp      5989
```

添加额外的端口

```
$ semanage port -a -t http_port_t -p tcp 7777
$ semanage port -a -t http_port_t -p tcp 8888
```

配置防火前允许7777和8888端口

```
$ firewall-cmd --permanent --add-port=7777/tcp
$ firewall-cmd --permanent --add-port=8888/tcp
$ firewall-cmd --reload
$ firewall-cmd --list-ports
$ systemctl restart httpd
```

web访问

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRsEwL0XFtSvUQPRFw7fUfTjdicXP8DzBNibwtJBpfYyibV2oyN1s9zBboqajeo0qdgBhJ4MPrkqBwqw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRsEwL0XFtSvUQPRFw7fUfTfWJfiacxqM2WHkFGkUuiaxJjCA2XdZicD54xPibTZo8YSYf2a1kmo7kDBw/640?wx_fmt=png)

目前来看Selinux攻击面主要是用户配置不当导致越权操作，最终导致命令执行的结果。

**06****‍**

**总结‍‍‍‍‍‍‍‍**

SELinux的主要作用就是最大限度减小系统中服务进程可访问的资源，最大程度上预防0day攻击。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSZmibNONzibea8WkcAFcdQcXicIYgWuvOtR8HqlqJ68Avib679FBGHYqxRibldppr6etXJxxWRrlBToiaw/0?wx_fmt=png)

山石网科安全技术研究院

向上滑...