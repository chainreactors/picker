---
title: 【技术原创】Horde Groupware Webmail漏洞调试环境搭建
url: https://www.4hou.com/posts/l6yV
source: 嘶吼 RoarTalk – 回归最本质的信息安全,互联网安全新媒体,4hou.com
date: 2023-02-01
fetch_date: 2025-10-04T05:18:50.364426
---

# 【技术原创】Horde Groupware Webmail漏洞调试环境搭建

【技术原创】Horde Groupware Webmail漏洞调试环境搭建 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 【技术原创】Horde Groupware Webmail漏洞调试环境搭建

3gstudent
[技术](https://www.4hou.com/category/technology)
2023-01-31 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)141539

收藏

导语：本文记录从零开始搭建Horde Groupware Webmail漏洞调试环境的细节。

**0x00 前言**

本文记录从零开始搭建Horde Groupware Webmail漏洞调试环境的细节。

**0x01 简介**

本文将要介绍以下内容：

Horde Groupware Webmail安装

Horde Groupware Webmail漏洞调试环境配置

常用知识

**0x02 Horde Groupware Webmail安装**

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

![1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462454217869.png "1667461138173283.png")

连接数据库的命令：mysql -u root -p

执行以下命令：

![2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462457191780.png "1667461186186454.png")

**2.安装php-horde-webmail**

安装命令：sudo apt -y install php-horde-webmail

**3.配置webmail**

安装命令：

![3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462458181255.png "1667461233827484.png")

配置如下：

![4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462458769996.png "1667461307331772.png")

注：

这里必须指定为/usr/share/horde，否则在运行webmail-install时报错提示：failed to open stream: No such file or directory in /usr/bin/webmail-install on line 17

**4.安装**

安装命令：webmail-install

配置如下：

![5.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462459199082.png "1667461407614395.png")![6.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462460203003.png "1667461420177000.png")

**5.访问登录页面**

http://127.0.0.1/horde/login.php

这里不能使用localhost，会报错提示：

![7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462461188372.png "1667461483195298.png")

此时没有配置邮箱用户，无法进行登录，需要安装Dovecot

**6.安装Dovecot**

安装命令：apt-get -y install dovecot-imapd dovecot-pop3d

默认horde webmail没有配置邮箱用户，可以使用Ubuntu系统的用户进行登录，成功，如下图

![8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462462133870.png "1667461557421636.png")

**补充1：安装File\_Fstab会出现bug**

安装命令：pear install File\_Fstab

安装这个模块之后，无法加载test页面，报错提示：

![9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462463138912.png "1667461602166454.png")

如下图

![10.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462464647434.png "1667461682129110.png")**补充2：cpanel默认支持Horde Groupware Webmail**

cpanel的安装可参考：https://docs.cpanel.net/installation-guide/system-requirements-centos/

cpanel下启用Horde Groupware Webmail的方法如下：

(1)添加邮箱账户

进入WHM，登录用户名root，口令为root用户的口令，选择创建用户，如下图

![11.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462465165375.png "1667461726199905.png")(2)选择horde

使用新添加的账户登录，选择Email Accounts，配置成horde，如下图

![12.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462466211534.png "1667461752122811.png")

**0x03 Horde Groupware Webmail漏洞调试环境配置**

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

![13.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462466104351.png "1667461935123255.png")

下载安装xdebug：

![14.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462467184390.png "1667461956135801.png")

配置xdebug：vi /etc/php/7.2/apache2/conf.d/99-xdebug.ini

配置代码需要区分XDebug2和XDebug3，自PhpStorm 2020.3起，开始使用XDebug3，语法也做了更改，详细说明：https://xdebug.org/docs/upgrade\_guide#changed-xdebug.remote\_enable

正确的参数：

![15.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462468136847.png "1667461990649582.png")对应老的参数（失效）：

![16.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462469186232.png "1667462014150636.png")

重启Apache服务：sudo systemctl restart apache2.service

可通过访问phpinfo页面确认xdebug是否配置成功

**2.PhpStorm配置**

(1)安装PhpStorm

(2)配置调试端口

打开PhpStorm，创建一个PHP Empty Project

依次打开File -> Settings -> PHP -> Debug

确认调试端口为9000，如下图

![17.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462470875362.png "1667462055623150.png")

(3)配置DBGp Proxy

依次打开File -> Settings -> PHP -> Debug -> DBGp Proxy，填入以下信息：

![18.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462470177128.png "1667462094144849.png")

如下图

![19.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462471158597.png "1667462134927151.png")

(4)配置Servers

依次打开File -> Settings -> PHP -> Servers

手动添加一个，填入以下信息：

![20.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462472177181.png "1667462273126469.png")

勾选Use path mappings，填入以下配置信息：

![21.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462472155774.png "1667462300109221.png")如下图

![22.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462473824564.png "1667462321635295.png")**3.下断点**

将Ubuntu18的文件夹/usr/share/horde下载到本地，保存为c:\Users\1\PhpstormProjects\untitiled\horde

在PhpStorm打开需要调试的php文件并下断点

**4.开始调试**

(1)配置

依次打开Run -> Edit Configurations

手动添加一个，选择PHP Web Page，填入以下信息：

![23.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462474668971.png "1667462384124152.png")(2)开启监听

依次打开Run -> Start Listening for PHP Debug Connections

(3)开启调试

依次打开Run -> Debug

弹出Chrome浏览器，捕获到断点，如下图

![24.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462475885364.png "1667462416235723.png")

**0x04 常用知识**

**1.添加管理员用户**

将用户a设置为管理员用户

![25.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462522172769.png "1667462522172769.png")

修改：$conf['auth']['admins'] = array();

设置为：$conf['auth']['admins'] = array('a');

**2.日志位置**

![26.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20221103/1667462578116023.png "1667462578116023.png")

**0x05 小结**

在我们搭建好Horde Groupware Webmail漏洞调试环境后，接下来就可以着手对漏洞进行学习。

参考资料：

https://www.horde.org/apps/webmail/docs/INSTALL

https://github.com/horde/base/blob/master/doc/INSTALL.rst

https://geekrewind.com/install-horde-groupware-webmail-on-ubuntu-16-04-18-04-with-apache2/

https://neoserver.site/help/step-step-installation-instructions-postfix-and-dovecot-ubuntu

本文为 3gstudent 原创稿件，授权嘶吼独...