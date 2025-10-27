---
title: 【技术原创】Horde Groupware Webmail漏洞调试环境搭建
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247556868&idx=1&sn=c617d450756c0557ff1266baf3f80426&chksm=e915cf3ede624628adb794ea9d4535a169b48f2d75fbe4f81870a1076ad3f4810c0fbddf98df&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2023-02-01
fetch_date: 2025-10-04T05:23:05.098051
---

# 【技术原创】Horde Groupware Webmail漏洞调试环境搭建

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtGxzugUQrKgQ9rAENib1DYyAjvdlg2xw0iaIalSkfxLUsLoK7ajNlW6FQ/0?wx_fmt=jpeg)

# 【技术原创】Horde Groupware Webmail漏洞调试环境搭建

原创

3gstudent

嘶吼专业版

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtzrm527fYoeFibRvQGsnYZkvwDxUQh16g7zdjcNe1bnicoUymaicsmvYyA/640?wx_fmt=png)0x00 前言

本文记录从零开始搭建Horde Groupware Webmail漏洞调试环境的细节。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtzrm527fYoeFibRvQGsnYZkvwDxUQh16g7zdjcNe1bnicoUymaicsmvYyA/640?wx_fmt=png)0x01 简介

本文将要介绍以下内容：

Horde Groupware Webmail安装

Horde Groupware Webmail漏洞调试环境配置

常用知识

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtzrm527fYoeFibRvQGsnYZkvwDxUQh16g7zdjcNe1bnicoUymaicsmvYyA/640?wx_fmt=png)0x02 Horde Groupware Webmail安装

简单来说，安装Horde Groupware Webmail时需要配置以下环境：

MySQL数据库

Apache2

php7.2

Dovecot

操作系统选择Ubuntu18，这里不能选择Ubuntu16，因为Ubuntu16不支持php7.2

本文的安装过程做了适当精简，完整过程可根据参考资料进行学习，具体安装过程如下：

**1.安装MariaDB Database Server**

(1)安装

安装命令：sudo apt-get -y install mariadb-server mariadb-client

(2)配置

配置命令：sudo mysql\_secure\_installation

配置如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtypGC0OYhicVkttkCo57Q0uHQepEGgDwA7piafkH3EicgibQf2SoLWWmrWA/640?wx_fmt=png)

(3)创建数据库

连接数据库的命令：mysql -u root -p

执行以下命令：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtwZgPeEy0jF2YgiczmzwdwbAX9rvvCoy033BofCnBST5EwW9psBSIvBA/640?wx_fmt=png)

设置数据库的用户为hordeuser，口令为new\_password\_here
 **2.安装php-horde-webmail**

安装命令：sudo apt -y install php-horde-webmail

**3.配置webmail**

安装命令：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtYn9pp8gjABxegRolBibQ9X0QzEq4WBH8QG38brpkT6ibAlILcXqEIOnQ/640?wx_fmt=png)

配置如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtV5kmG57KkUepNIOh5MC70jT4XNTarsicKNNicLpMKB07Sy2Eyw8y19Pg/640?wx_fmt=png)

注：

这里必须指定为/usr/share/horde，否则在运行webmail-install时报错提示：failed to open stream: No such file or directory in /usr/bin/webmail-install on line 17

**4.安装**

安装命令：webmail-install

配置如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtBY4PW6tiaxzmffBdTCM945UtFOovJRhTOU9pVUXn1Huiar1nNh9VLs8A/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtf3AiaoR0SGicGGzpqNM8ibIticO7c1CCXxobE67AnFHNVILIl2BTk5HuuQ/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtzrm527fYoeFibRvQGsnYZkvwDxUQh16g7zdjcNe1bnicoUymaicsmvYyA/640?wx_fmt=png)5.访问登录页面

http://127.0.0.1/horde/login.php

这里不能使用localhost，会报错提示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZt9htNKXcQw4aaqtYQ8o1P6p2Xd1FZ29wuUfUdLD8pEzqKlZnpF7J9NA/640?wx_fmt=png)

此时没有配置邮箱用户，无法进行登录，需要安装Dovecot

**6.安装Dovecot**

安装命令：apt-get -y install dovecot-imapd dovecot-pop3d

默认horde webmail没有配置邮箱用户，可以使用Ubuntu系统的用户进行登录，成功，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtPUiakOa6jATJntl6CouPyWm6sWmKyhll5cxC12yTjibwdtibzpb1zH5icw/640?wx_fmt=png)

**补充1：安装File\_Fstab会出现bug**

安装命令：pear install File\_Fstab

安装这个模块之后，无法加载test页面，报错提示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZt4A8yz6tuiaS3wzPYD3Rr42rB5eS1LBtbMmKXypx9guOZIR5B7rRX6Jw/640?wx_fmt=png)

如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtg5l6pM3FBswP771w59YKk2RDz7QibCb9U2ibAugibRXOMRJCrT2GhY1qw/640?wx_fmt=png)

**补充2：cpanel默认支持Horde Groupware Webmail**
cpanel的安装可参考：https://docs.cpanel.net/installation-guide/system-requirements-centos/

cpanel下启用Horde Groupware Webmail的方法如下：

(1)添加邮箱账户

进入WHM，登录用户名root，口令为root用户的口令，选择创建用户，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtDmj9YZQ9bZjMmMNVwJHhfGiblFf5ibp8EEM4IN3R2GjczhP5HKBjAANw/640?wx_fmt=png)

(2)选择horde

使用新添加的账户登录，选择Email Accounts，配置成horde，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtRia4Oyq7dlNcl2HsxFyoRpGicDIFXmJkt9Q7yj7Gleqgkf4OpQq0ggdQ/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtzrm527fYoeFibRvQGsnYZkvwDxUQh16g7zdjcNe1bnicoUymaicsmvYyA/640?wx_fmt=png)0x03 Horde Groupware Webmail漏洞调试环境配置

这里需要先在安装Horde Groupware Webmail的Ubuntu18上添加xdebug，然后在本地安装PhpStorm进行远程调试

本地系统使用Windows，IP为192.168.112.131

安装Horde Groupware Webmail的Ubuntu18 IP为192.168.112.168

流程如下：

**1.安装xdebug**

需要根据php版本选择合适的xdebug，可选择以下两种筛选方法：

(1)命令行执行命令php -i

(2)浏览器访问phpinfo页面

echo "

访问http://127.0.0.1/horde/phpinfo.php

将以上方法得到的输出信息复制到https://xdebug.org/wizard，可以自动解析出对应的xdebug版本

根据提示进行安装

输出信息如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtTJTvj7KAfhb6VklvesrkgJP9eR4Y2zDCm0znngwuYXxYZklPInNJUw/640?wx_fmt=png)

下载安装xdebug：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtSTyysflV0Ng7ibvSOCWvAQneiaqnxTnO0cjSy2N8HZBjNqUw4NfQL0KA/640?wx_fmt=png)

配置xdebug：vi /etc/php/7.2/apache2/conf.d/99-xdebug.ini

配置代码需要区分XDebug2和XDebug3，自PhpStorm 2020.3起，开始使用XDebug3，语法也做了更改，详细说明：https://xdebug.org/docs/upgrade\_guide#changed-xdebug.remote\_enable

正确的参数：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtrZxsgQO6icibGrHcOu6hA0CmAZgyYS9HeH1NZpH7f7lf0le8TnNAtQjQ/640?wx_fmt=png)

对应老的参数（失效）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtXaxuIZPnfMZU87yV0Ll2byO2sZD2grXOE031tiawvz0geBianbEibRvYQ/640?wx_fmt=png)

重启Apache服务：sudo systemctl restart apache2.service

可通过访问phpinfo页面确认xdebug是否配置成功

**2.PhpStorm配置**

(1)安装PhpStorm

(2)配置调试端口

打开PhpStorm，创建一个PHP Empty Project

依次打开File -> Settings -> PHP -> Debug

确认调试端口为9000，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtyMX0xHZJ63K3uFssdQKCaYU6MiaMPWT8mWfxw5rc4iaSbmNqeFAgicLXw/640?wx_fmt=png)

(3)配置DBGp Proxy

依次打开File -> Settings -> PHP -> Debug -> DBGp Proxy，填入以下信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtfszabUJPdTa6cKs6QichuVCbZNKZAyuY6U4DBHJPdXbTggl8QelDMhA/640?wx_fmt=png)

如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZteX0dPa0Enj11d8hibv86WE7pt8XBgJ25oxve10sjr3icN9zziakSDrDMw/640?wx_fmt=png)

(4)配置Servers

依次打开File -> Settings -> PHP -> Servers

手动添加一个，填入以下信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtzmRGkBvT6JCUrXl8Y4snRiaYSFyjMqyibnnUUSGf5OicZ0bTe9Tn36KvA/640?wx_fmt=png)

勾选Use path mappings，填入以下配置信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtsfcR8wibvk8iaLkI3jus7jrKpxo3PDl7TmlFwotaicDq9JsTBIXFBRwLw/640?wx_fmt=png)

如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZticLIogZlRle4TgwISnnbcmbPx1Sz5Mp8Rfib5yQKR8HtHYQevhd9W3Lw/640?wx_fmt=png)

**3.下断点**

将Ubuntu18的文件夹/usr/share/horde下载到本地，保存为c:\Users\1\PhpstormProjects\untitiled\horde

在PhpStorm打开需要调试的php文件并下断点

**4.开始调试**

(1)配置

依次打开Run -> Edit Configurations

手动添加一个，选择PHP Web Page，填入以下信息：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtMde0J5UqIuTRdMJiaicnD6CDhI4NSuJlOKe1ISjsBQjOZrjElUlomYOw/640?wx_fmt=png)

(2)开启监听

依次打开Run -> Start Listening for PHP Debug Connections

(3)开启调试

依次打开Run -> Debug

弹出Chrome浏览器，捕获到断点，如下图

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtcdA49WNvAMDMadI6YoRbBYC0yIWBKPMTYrUkHcb8XHVUHbDRYgjxqg/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtzrm527fYoeFibRvQGsnYZkvwDxUQh16g7zdjcNe1bnicoUymaicsmvYyA/640?wx_fmt=png)0x04 常用知识

**1.添加管理员用户**

将用户a设置为管理员用户

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtCmVbCEUsAfdWj6JqYFgD0JcHDD5p6SkDx2CGygRNllOWTkiaVxuGSug/640?wx_fmt=png)

修改：$conf['auth']['admins'] = array();

设置为：$conf['auth']['admins'] = array('a');

**2.日志位置**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtRuUZCszrWPwB7ptC3UumeVszrRNcw0D0BBrBQyetLiaibvIc8Wb4ZDXQ/640?wx_fmt=png)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2ib0hHsBUD2tcR3hZCZtKeZtzrm527fYoeFibRvQGsnYZkvwDxUQh16g7zdjcNe...