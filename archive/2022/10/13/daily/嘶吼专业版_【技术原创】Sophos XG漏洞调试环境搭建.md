---
title: 【技术原创】Sophos XG漏洞调试环境搭建
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247552045&idx=1&sn=97beaa36cf2d426426e8f71be82014ee&chksm=e915dc17de6255012ef33cb9f2dd96090317f048d4650f6f009322c007a6100f330393939bd4&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2022-10-13
fetch_date: 2025-10-03T19:47:29.948042
---

# 【技术原创】Sophos XG漏洞调试环境搭建

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o284DxdibUQt3atQVVhly8HD5kiaoplAGibMcEB1X1KyqawpBofDP9ompTXZm68Qh585vK3L2rfsX1J2Q/0?wx_fmt=jpeg)

# 【技术原创】Sophos XG漏洞调试环境搭建

原创

3gstudent

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5LibjPGp6U9FNVy9VYCbicFCOYwpDlI7cH0HF8zkw80ZWY83B53I8UCTQ/640?wx_fmt=png)0x00 前言

Sophos UTM和Sophos XG是两款不同的产品，前者偏向于通用威胁管理，后者偏向于硬件防火墙。本文将要介绍Sophos XG漏洞调试环境的搭建方法。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5LibjPGp6U9FNVy9VYCbicFCOYwpDlI7cH0HF8zkw80ZWY83B53I8UCTQ/640?wx_fmt=png)0x01 简介

本文将要介绍以下内容：

**·**环境搭建

**·**jetty调试环境搭建

**·**csc配置文件解密

**·** Postgresql数据库查询

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5LibjPGp6U9FNVy9VYCbicFCOYwpDlI7cH0HF8zkw80ZWY83B53I8UCTQ/640?wx_fmt=png)0x02 基础知识

架构如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5l1lCInjxR6kZuLwpSA5H2I5Ae4uRNLTf7jJI2sUNics7hT8QttIW8Zw/640?wx_fmt=png)

注：图片引用自https://codewhitesec.blogspot.com/2020/07/sophos-xg-tale-of-unfortunate-re.html

总的来说，分为以下三部分：

**·** Jetty：处理Web数据，将数据转发至csc作进一步处理

**·**csc:主程序：加载Perl Packages，实现主要功能

**·**Postgresql：用来存储数据

我在实际研究过程中，这三部分遇到了以下问题：

**·**Jetty：添加调试信息后无法启动java

**·**csc：csc加载Perl Packages后会自动删除，无法获得Perl Packages的实现细节

**·**Postgresql：用户权限低，无法查询数据库表

下面将要逐个介绍三个问题的解决方法。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5LibjPGp6U9FNVy9VYCbicFCOYwpDlI7cH0HF8zkw80ZWY83B53I8UCTQ/640?wx_fmt=png)0x03 环境搭建

参考资料：

https://docs.sophos.com/nsg/sophos-firewall/18.5/Help/en-us/webhelp/onlinehelp/VirtualAndSoftwareAppliancesHelp/VMware/VMwareInstall/index.html

**1.下载安装包**

官方网站默认只提供最新版本的下载，但是可以通过猜测正确的版本号下载旧版本

例如18.5.3 Virtual Installers: Firewall OS for VMware：

https://download.sophos.com/network/SophosFirewall/installers/VI-18.5.3\_MR-3.VMW-408.zip

18.5.2 Virtual Installers: Firewall OS for VMware：

https://download.sophos.com/network/SophosFirewall/installers/VI-18.5.2\_MR-2.VMW-380.zip

**2.导入VMware Workstation**

下载得到zip文件，解压后运行sf\_virtual.ovf

**3.VMware Workstation网卡配置**

需要添加两个网卡VMnet7和VMnet8，VMnet7设置为Host-only和172.16.16.0，VMnet8设置为NAT，具体方法如下：

(1)VMnet7

打开VMware Workstation，依次选择Edit->Virtual Network Editor...

Add Network...->VMnet7

VMnet7设置为：

**·**Type: Host-only

**·**Subnet Address: 172.16.16.0

(2)VMnet8

VMnet8设置为：

**·**Type: NAT

**4.Sophos XG网卡配置**

Network Adapter设置为VMnet7

Network Adapter 2设置为VMnet8

Network Adapter 3设置为VMnet8

配置如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5IsoVefxJjl6lF0iaZE266ystFL5VK0qJIQicVIGWjOGsmvTZK3tY9dLQ/640?wx_fmt=png)

**5.启动Sophos XG**

默认登录口令：admin

**6.查看IP地址**

依次输入1.Newwork Configuration->1.Interface Configuration

得到LAN的ip为172.16.16.16

**7.进入Web配置页面进行激活**

浏览器访问https://172.16.16.16:4444

注册页面选择：I don't have a serial number(start a trial)

按照提示进行注册。

注册成功后，重新访问https://172.16.16.16:4444进行配置。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5LibjPGp6U9FNVy9VYCbicFCOYwpDlI7cH0HF8zkw80ZWY83B53I8UCTQ/640?wx_fmt=png)0x04 jetty调试环境搭建

1.查看Java进程相关信息

执行命令：ps ww|grep java

输出：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5UqPV8iaJUM49ZzuWNkYTmB4E8Yz7SibMg8jL0Z5stExBicLUKbVXJ9eNQ/640?wx_fmt=png)

从输出中得到Java版本为java-11-openjdk

**2.定位配置文件**

配置文件路径为/usr/bin/jetty，内容如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5DSE6DvAmm8Zv9k6mYMezy767RScAI7nzEu70XBw8n4HLmkZcKQ77fw/640?wx_fmt=png)

**3.添加调试参数**

修改文件属性：mount -o rw,remount /

在exec所在行添加调试参数："-agentlib:jdwp=transport=dt\_socket,server=y,suspend=n,address=\*:8000"

**4.重启服务**

执行命令：service tomcat:restart -ds nosync

查看服务状态：service -S | grep tomcat

发现tomcat状态为STOPPED

为了获得详细的报错信息，直接运行/usr/bin/jetty

输出：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5kyp6cRf8zBibicGnaLEnH4HfayPFjOjbmib4naA5iaycgHuXSuZ6q5coAA/640?wx_fmt=png)

发现是JDK的问题，这里选择替换一个完整的JDK。

**5.替换JDK**

下载jdk-11.0.15\_linux-x64\_bin.tar.gz并上传至Sophos XG

备份原文件夹：cp -r /lib/jvm/java-11-openjdk /lib/jvm/java-11-openjdk\_backup

将jdk-11.0.15\_linux-x64\_bin.tar.gz解压：tar zxvf /tmp/jdk-11.0.15\_linux-x64\_bin.tar.gz

替换/lib/jvm/java-11-openjdk:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5iaC79XNk0CRQibOD0WicyqLCmiaraZeGAlrn6askFd9dSjnFDKgicxfMPwA/640?wx_fmt=png)

**6.再次重启服务**

执行命令：service tomcat:restart -ds nosync

查看服务状态：service -S | grep tomcat

发现tomcat状态为RUNNING

确认参数被修改，执行命令：ps ww|grep java

输出：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD54MfE1JibMwJabhNFzbXIFeSbV2dwdpB2icZFQicXvibNZA6I1IuL8icEMAQ/640?wx_fmt=png)

**7.修改防火墙规则**

执行命令：iptables -I INPUT -p tcp --dport 8000 -j ACCEPT

**8.使用IDEA远程调试**

如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5GicSINN6FjXe6LxW9mjsnIOGmKOUOziaEjIqwEHr8afjibusdIKAjNKdw/640?wx_fmt=png)

在调试过程中，如果遇到无法下断点的情况，重启java服务即可：service tomcat:restart -ds nosync

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5LibjPGp6U9FNVy9VYCbicFCOYwpDlI7cH0HF8zkw80ZWY83B53I8UCTQ/640?wx_fmt=png)0x05 csc配置文件解密

查看csc进程相关信息。

执行命令：ps ww|grep csc

部分输出：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5vjOh1rYMCsca7B4n2sXSMnYjkoZTb85qHdAVe5euzECtvBmmVKYz2A/640?wx_fmt=png)

csc进程读取/\_conf/cscconf.bin作为配置文件，而/\_conf/cscconf.bin是一个加密的文件，所以这里需要对/\_conf/cscconf.bin进行解密。

这里我采用的方法是通过IDA修改程序代码，改变实现逻辑，导出解密后的配置文件。

使用IDA加载csc，查看main()函数的实现逻辑，部分代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5xIVUnFyEF2b3nHudBumSp47HOrXV5oEtPBWSDibQsbmpDxIbhiakFWEQ/640?wx_fmt=png)

分析以上代码，csc先调用extract\_conf()函数导出配置，最后执行系统命令rm -rf /\_conf/csc/csc /\_conf/csc/csc.conf /\_conf/csc/cscconf/ /\_conf/csc/constants.conf /\_conf/csc/cscconf.tar.gz /\_conf/csc/global.conf /\_conf/csc/cfsconf /\_conf/csc/service /\_conf/csc/bind\_file\_list删除配置文件，导致我们无法直接获得相关配置文件。

查看extract\_conf()函数的实现代码：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5xxpiavfe0U1ko2Cp9D72vB3mqGQ7XYoqxd0Q0UTz8NEzNIfSQfBaWmg/640?wx_fmt=png)

分析以上代码，csc先调用sub\_8052494()函数对/\_conf/csc/cscconf.tar.gz进行解密，接着执行系统命令tar -zxf /\_conf/csc/cscconf.tar.gz -C /\_conf/csc将配置文件释放到文件夹/\_conf/csc

综合以上分析，我们可以采取以下方式导出配置文件：修改csc程序，将释放路径/\_conf/csc修改为另一路径，例如/var/aaaaa，那么，csc在删除配置文件时，由于指定了固定的绝对路径，导致无法删除新的文件夹，这样我们就能从中获得完整的配置文件。

**具体的实现方法如下：**

**(1)修改csc**

使用IDA加载csc，查看Exports，找到extract\_conf，双击进入IDA View，定位到字符串tar -zxf /\_conf/csc/cscconf.tar.gz -C /\_conf/csc，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5L8HdLqHf45NIUjE4mVor8iaBVaKAuxacHFIIv25JZdArmOUry8ialib6w/640?wx_fmt=png)

切换到Hex View，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5iajCfZLH51hRkKeJWUgFeoh3iayiaZ2fYoULL5VLduDVh4LSuaTbhmibng/640?wx_fmt=png)

将/\_conf/csc修改为/var/aaaaa，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5MHOhHFIeIbmjfvVtoT1OHibwQFHG90P52icwrwTELK0GlrUxYpdqYknQ/640?wx_fmt=png)

右键选择Apply changes

依次选择Edit->Patch program->Apply patches to input file...->OK，生成新的文件csc

**(2)替换csc**

通过ssh登录，上传新的文件csc，保存至/tmp/csc

备份csc并进行替换，执行以下命令：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5o7w5Xu1xsytFoI1DNb1KQX9TAk7A8u08FMcByEAc2ibohiaqJwvFw8FA/640?wx_fmt=png)

**(3)确认配置文件是否导出成功**

等待系统重启，进入底层shell，依次输入5.Device Management->3.Advanced Shell

查看文件夹/var/aaaaa，如下图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5cqms2CdNTJ2A878YuEFw1lfPFly2rWQA6ictMbk2LqCpAJk8W9dHUhg/640?wx_fmt=png)

配置文件导出成功。

**(4)恢复csc**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5eFrKUEVHNYhhG5vic3x9eg6ibozwk8NhkNwedN3z8nVBl8bibJtb1ibsDg/640?wx_fmt=png)

**(5)下载配置文件**

通过ssh登录，下载文件夹/var/aaaaa中的内容。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o284DxdibUQt3atQVVhly8HD5LibjPGp6U9FNVy9VYCbicFCOYwpDlI7cH0HF8zkw80ZW...