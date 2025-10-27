---
title: 解决Aws rhel7系统无法使用YUM源的问题
url: https://buaq.net/go-172552.html
source: unSafe.sh - 不安全
date: 2023-07-21
fetch_date: 2025-10-04T11:51:50.194565
---

# 解决Aws rhel7系统无法使用YUM源的问题

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![]()

解决Aws rhel7系统无法使用YUM源的问题

糟心的Amazon Linux 2 AMI，非要魔改下，aws的系统也是基于CentOS和RHEL基本没有区别，并且CentOS已经被REHL收购。所以
*2023-7-20 22:1:0
Author: [blog.upx8.com(查看原文)](/jump-172552.htm)
阅读量:20
收藏*

---

糟心的Amazon Linux 2 AMI，非要魔改下，aws的系统也是基于CentOS和RHEL基本没有区别，并且CentOS已经被REHL收购。所以将RHEL的YUM源替换为CentOS即可。

```
[[email protected] yum]# yum clean all
bash: yum: 未找到命令...
```

无法使用YUM源的问题如下：

```
[[email protected] ~]# yum repolist
已加载插件：product-id, search-disabled-repos, subscription-manager
This system is not registered with an entitlement server. You can use subscription-manager to register.
repolist: 0
[[email protected] ~]#
[[email protected] ~]#
[[email protected] ~]# yum install ntp
已加载插件：product-id, search-disabled-repos, subscription-manager
This system is not registered with an entitlement server. You can use subscription-manager to register.
There are no enabled repos.
 Run "yum repolist all" to see the repos you have.
 To enable Red Hat Subscription Management repositories:
     subscription-manager repos --enable <repo>
 To enable custom repositories:
     yum-config-manager --enable <repo>
```

```
# 清除原有RHEL的YUM及相关软件包
rpm -qa|grep yum|xargs rpm -e --nodeps
rpm -qa|grep python-urlgrabber|xargs rpm -e --nodeps
```

```
# 软件包下载地址
# https://mirrors.aliyun.com/centos/7/os/x86_64/Packages/
# http://mirrors.163.com/centos/7/os/x86_64/Packages/

下载centos7的相关软件包
http://mirrors.163.com/centos/7/os/x86_64/Packages/rpm-4.11.3-45.el7.x86_64.rpm
http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-3.4.3-168.el7.centos.noarch.rpm
http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-metadata-parser-1.1.4-10.el7.x86_64.rpm
http://mirrors.163.com/centos/7/os/x86_64/Packages/yum-plugin-fastestmirror-1.1.31-54.el7_8.noarch.rpm
http://mirrors.163.com/centos/7/os/x86_64/Packages/python-iniparse-0.4-9.el7.noarch.rpm
http://mirrors.163.com/centos/7/os/x86_64/Packages/python-urlgrabber-3.10-10.el7.noarch.rpm
```

```
上传软件包到rhel7.3系统里
```

```
安装软件包

注：yum-plugin-fastestmirror和yum两个rpm要一起安装，不能拆开。

rpm -ivh python-iniparse-0.4-9.el7.noarch.rpm
rpm -ivh python-urlgrabber-3.10-10.el7.noarch.rpm
rpm -ivh yum-metadata-parser-1.1.4-10.el7.x86_64.rpm
rpm -ivh yum-plugin-fastestmirror-1.1.31-54.el7_8.noarch.rpm yum-3.4.3-168.el7.centos.noarch.rpm #会出现问题1
```

错误：依赖检测失败：

```
问题1
错误：依赖检测失败：
    rpm >= 0:4.11.3-22 被 yum-3.4.3-158.el7.centos.noarch 需要
    yum >= 3.0 被 yum-plugin-fastestmirror-1.1.31-54.el7_8.noarch 需要
解决：,升级rpm，上一步已经下载了，直接升级
rpm -Uvh rpm-4.11.3-45.el7.x86_64.rpm --nodeps
```

```
下载配置文件
wget -O /etc/yum.repos.d/CentOS-Base.repo https://mirrors.aliyun.com/repo/Centos-7.repo

把文件中所有$releasever改为7，$basearch保持不变

然后将此配置文件上传并复制到/etc/yum.repos.d/路径下，删除redhat.repo文件
```

```
1、$releasever
$releasever的值，当前系统的发行版本。是指大版本7

2、$basearch
$basearch的值，系统硬件架构(CPU指令集)
查看命令：arch，结果是x86_64
```

```
删除/var/cache/yum/下的x86_64目录
```

![](https://img2020.cnblogs.com/blog/794174/202111/794174-20211105171238769-954430185.png)

```
清理yum缓存: yum clean all
```

```
将服务器软件包信息缓存至本地，提高搜索安装效率：yum makecache
```

```
测试：

能搜索到软件包信息，说明配置完成：
yum search vim
```

```
执行yum repolist查看，如果显示出repo仓库列表，并显示软件包数量则OK。（或者使用yum makecache）：

yum repolist
```

```
使用yum安装软件包测试：

yum -y install vim
```

文章来源: https://blog.upx8.com/3701
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)