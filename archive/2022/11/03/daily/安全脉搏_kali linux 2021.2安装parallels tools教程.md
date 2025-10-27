---
title: kali linux 2021.2安装parallels tools教程
url: https://www.secpulse.com/archives/190244.html
source: 安全脉搏
date: 2022-11-03
fetch_date: 2025-10-03T21:37:02.692359
---

# kali linux 2021.2安装parallels tools教程

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

# kali linux 2021.2安装parallels tools教程

[工具](https://www.secpulse.com/archives/category/tools)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-02

12,524

刚开始在parallel版本 16.1.2安装kali2022.3的时候报错，从网上查阅了一些资料，有说是版本不匹配的问题，接着就又更换了kali2021.2版本，没想到居然顺利的安装完毕了。可接下来的parallels tools的安装却遇到了很多坑。

# 一、系统配置

MacBook Pro (Intel Core) macOS Big Sur 11.3.1 kali-linux-2021.2-installer-amd64.iso Parallels Desktop 16 for Mac商业版 16.1.2 (49151) 坑点：系统配置方面就是我遇到的最大坑点，因为我一直用的是kali-linux-2022.3-installer-amd64.iso，所以不管用尽各种方法，总是最后安装不成功，最后kali从2022.3换到了2021.2才安装完毕。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374255.png)

# 二、解决安装parallels tools过程中第一个大坑

1、切换为root用户 在Parallels里安装完kali后，登陆kali，改一下root密码，注销后再用root身份登陆，可以更方便一些。以后的操作步骤均在root下进行！如果你不想改也可以，别忘记加sudo。更改root密码的命令为： `sudo passwd root`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374256.png)

2、安装parallels tools遇到报错 在parallels点击操作——安装Parallels Tools，可以进行挂载安装。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374258.png)

此时，桌面会出现Parallels Tools的挂载文件，但是这是只读的

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374263.png)

所以要将其复制出来后加权限才能操作，我在桌面新建了一个pdtools文件夹，将所有文件复制进去之后执行下面的命令，更改权限。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374266.png)

`chmod -R 777 pdtools`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374268.png)

然后进入到pdtools目录下，输入命令./install开始安装parallels tools

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374269.png)

一直按回车，不出意外的话，最后结果会出现了如下报错

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374271.png)

报错了，反正就是缺俩东西，下面开始爬坑。

# 三、安装dkms和Linux内核文件

dkms的安装比较简单，不管是用的官方源还是更换成了国内源，直接输入下面两条命令就行 `apt-get update` `apt-get install dkms` 安装内核文件首先要知道自己的kali内核版本,知道了内核版本 `uname -a`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374272.png)

就可以去网站上下载内核文件了。内核文件下载地址：old.kali.org

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374273.png)

直接全文搜索找到linux-headers的文件，并找到自己kali对应的版本即可，这里要注意一点就是光下载headers文件没用，你还需要下载common文件，就是绿框里的那个文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374276.png)

用wget命令将这三个deb文件下载下来 `wget http://old.kali.org/kali/pool/main/l/linux/linux-headers-5.10.0-kali7-amd64_5.10.28-1kali1_amd64.deb`

`wget http://old.kali.org/kali/pool/main/l/linux/linux-headers-5.10.0-kali7-common_5.10.28-1kali1_all.deb`

`wget  http://old.kali.org/kali/pool/main/l/linux/linux-kbuild-5.10_5.10.46-4kali1_amd64.deb`

下载完成后，安装这三个文件，安装顺序是：kbuild、common、headers。安装方法如下：

`dpkg -i linux-kbuild-5.10_5.10.46-1kali1_amd64.deb` `dpkg -i linux-headers-5.10.0-kali7-common_5.10.28-1kali1_all.deb` `dpkg -i linux-headers-5.10.0-kali7-amd64_5.10.28-1kali1_amd64.deb`

这个时候你会发现可能还有点问题，不要着急，再安装一个gdebi重新安装一下，这是一个deb文件安装工具，按照如下步骤继续，此时就可以顺利安装完成linux-headers内核头文件了。

`apt-get install gdebi -y` `gdebi linux-kbuild-5.10_5.10.46-1kali1_amd64.deb` `gdebi linux-headers-5.10.0-kali7-common_5.10.28-1kali1_all.deb` `gdebi linux-headers-5.10.0-kali7-amd64_5.10.28-1kali1_amd64.deb`

（2）番外篇：如果你在安装gdebi的时候遇到如下报错，不要着急

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374278.png)

只要安装一下linux-compliler-gcc-10-x86即可，具体安装方法如下：

`apt install linux-compliler-gcc-10-x86`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374282.png)

安装完linux-compliler-gcc-10-x86之后，你再安装gdebi会发现如丝滑般顺畅。

（3）此时你再切换回pdtools目录，运行./install，一路回车，不出意外，你就会遇到下一个大的报错了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374290.png)

# 四、解决安装parallels tools过程中遇到的第二个大坑

上面已经走完了万里长征第一步，解决了安装linux-headers内核头文件的问题，又有新问题在等着我们，就是上面的报错。

1、要解决上面的问题，需要对parallels tools安装文件进行修改，首先对关键文件进行解压，先进入kmods目录，解压prl\_mod.tar.gz ： `cd /home/kali/桌面/pdtools/kmods` `tar -zxvf prl_mod.tar.gz`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374294.png)

2、编辑inode.c文件，它的路径是prl\_fs/SharedFolders/Guest/Linux/prl\_fs/inode.c，在第一行插入如下两行代码：

```
#define segment_eq(a, b) (b)
#define USER_DS 1
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374295.png)

3、编辑prl\_fs\_freeze.c文件，该文件的路径是：prl\_fs\_freeze/Snapshot/Guest/Linux/prl\_freeze/prl\_fs\_freeze.c，在文件第一行插入如下代码 `#include <linux/blkdev.h>`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374296.png)

4、编辑prl\_fs/Makefile文件，路径为prl\_fs/SharedFolders/Guest/Linux/prl\_fs/Makefile，在文件的第一行插入如下代码：

`KBUILD_EXTRA_SYMBOLS := /home/kali/桌面/pdtools/kmods/prl_tg/Toolgate/Guest/Linux/prl_tg/Module.symvers`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374299.png)

5、编辑kmod/Makefile文件，路径为prl\_vid/Video/Guest/Linux/kmod/Makefile，在文件第一行插入如下代码：

`KBUILD_EXTRA_SYMBOLS := /home/kali/桌面/pdtools/kmods/prl_tg/Toolgate/Guest/Linux/prl_tg/Module.symvers`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190244-1667374309.png)

6、重新打包parallels tools安装文件，在kmods目录下执行： `rm prl_mod.tar.gz` `tar -zcvf prl_mod.tar.gz .`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp...