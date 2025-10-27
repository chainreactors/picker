---
title: Linux安装部署Nacos
url: https://buaq.net/go-172696.html
source: unSafe.sh - 不安全
date: 2023-07-23
fetch_date: 2025-10-04T11:51:28.271519
---

# Linux安装部署Nacos

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

![](https://8aqnet.cdn.bcebos.com/5ee19ef10f8fa60542071080a8808374.jpg)

Linux安装部署Nacos

一、安装JDK（1）Nacos依赖于JDK运行，所以Linux上也需要安装JDK才行。（2）Linux安装JDK链接如下：Linux下安装jdk并配置环
*2023-7-22 13:41:0
Author: [blog.upx8.com(查看原文)](/jump-172696.htm)
阅读量:40
收藏*

---

## 一、安装JDK

（1）Nacos依赖于JDK运行，所以Linux上也需要安装JDK才行。

（2）Linux安装JDK链接如下：

[Linux下安装jdk并配置环境变量（一）——tar压缩包形式安装jdk及查看是否安装JDK\_wd520521的博客-CSDN博客\_tar包安装jdk](https://blog.csdn.net/wd520521/article/details/109769429 "Linux下安装jdk并配置环境变量（一）——tar压缩包形式安装jdk及查看是否安装JDK_wd520521的博客-CSDN博客_tar包安装jdk")

[Ubuntu 一键安装 JDK](https://blog.upx8.com/3608 "Ubuntu 一键安装 JDK")

## 二、安装nacos

### 1、下载并上传安装包（这里演示的是nacos1.1.4版本）

（1）下载链接：[Release 1.1.4(Oct 24th, 2019) · alibaba/nacos · GitHub](https://github.com/alibaba/nacos/releases/tag/1.1.4 "Release 1.1.4(Oct 24th, 2019) · alibaba/nacos · GitHub")

（2）下载下图中的安装包，并上传到Linux服务器目录中，例如/opt

![](https://img.imgdd.com/f210f3.503a4c7b-b7b8-4cb4-96e6-e8373261e7c1.png)

![](https://img.imgdd.com/f210f3.6b5d9629-a0bf-45f0-b3fd-5bbd72195d1a.png)

### 2、解压安装包

（1）解压安装包：

```
tar -zxvf nacos-server-1.4.1.tar.gz
```

（2）删除安装包（此步不执行也可以）

```
rm -rf nacos-server-1.4.1.tar.gz
```

（3）目录样式，以及解压后文件内部目录

![](https://img.imgdd.com/f210f3.12b605dc-560b-4d48-bf30-651bb285cb03.png)

![](https://img.imgdd.com/f210f3.41a83592-ef39-4359-acf5-20e80dcb484e.png)

### 3、端口配置

Nacos的默认端口是8848，如果你电脑上的其它进程占用了8848端口，请先尝试关闭该进程。

**如果无法关闭占用8848端口的进程**，也可以进入nacos的conf目录，修改配置文件中的端口：

> #进入nacos配置文件目录
>
> cd /opt/nacos/conf
>
> #编辑nacos配置文件
>
> vim application.properties

进入编辑模式后，修改下图端口号即可：

![](https://img.imgdd.com/f210f3.1d409880-43e0-44fa-8302-88498e381536.png)

**保存编辑：**

> 按下ESC
>
> #保存文件
>
> :wq

### 4、启动nacos

（1）在nacos/bin目录中，输入命令启动Nacos：

> #进入目录
>
> cd /opt/nacos/bin
>
> #启动nacos
>
> sh startup.sh -m standalone

（2）注意：使用sh startup.sh -m standalone命令启动后发现nacos并没有启动，查看进程也没有nacos的进程，此时 我们查看nacos的启动日志（如下图）：

![](https://img.imgdd.com/f210f3.e00d75b7-6415-47f6-89cf-ca76fd88d3d0.png)

发现nacos启动日志会报错cannot execute binary file， 此时我们只需要将命令换成下面命令即可

```
sudo sh startup.sh -m standalone
```

（3）此时nacos已经启动完成

（4）启动时如果报以下错误

![](https://img.imgdd.com/f210f3.94f59ff3-2a0a-4b00-b941-04b842676631.png)

解决方案：

第一、首先查看**JAVA\_HOME配置：echo $JAVA\_HOME**

**![](https://img.imgdd.com/f210f3.31b227b8-7f15-44b6-8019-dcc28dd515ee.png)**

**第二步：找到配置，然后开始修改,修改成这样，注释四个，重新写一个HAVA\_HOME，见红框部分**

```
vim /opt/nacos2/nacos/bin/startup.sh
```

修改后截图：

![](https://img.imgdd.com/f210f3.f7067776-ea9a-47ac-8310-b4641a7350ac.png)

 然后保存配置，进行启动

### 5、浏览器访问

访问链接：[http://IP:8848/nacos/](http://192.168.191.32:8848/nacos/ "http://IP:8848/nacos/")

账号：nacos

密码：nacos

文章来源: https://blog.upx8.com/3702
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)