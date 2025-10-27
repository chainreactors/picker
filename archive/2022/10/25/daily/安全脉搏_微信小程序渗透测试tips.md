---
title: 微信小程序渗透测试tips
url: https://www.secpulse.com/archives/189727.html
source: 安全脉搏
date: 2022-10-25
fetch_date: 2025-10-03T20:45:40.608461
---

# 微信小程序渗透测试tips

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

# 微信小程序渗透测试tips

[移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)

[hackctf](https://www.secpulse.com/newpage/author?author_id=34005)

2022-10-24

14,665

> 作者：粉红飞天pig，转载于国科漏斗社区。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593207.gif)

**0x01**

关于微信小程序渗透可能很多小伙伴们还停留在听过但没实操过的阶段，那么以测试人员的视角出发究竟到底什么是微信小程序呢? 通过查阅微信小程序的开发文档在《起步》章节中有介绍到：小程序主要的开发语言是JavaScript且同普通的网页开发相比有很大的相似性。这么来看微信小程序的测试大体同web端测试应该没什么区别。具体该怎么做呢，首先让我们一起来回顾一遍小学二年级学过的web系统测试流程，大体就是浏览功能，浏览前端源码，然后抓包改包构造包。那么这些测试方法该怎么对应到小程序中去呢?

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593208.gif)

**0x02**

首先是浏览功能。通过观察功能点推测可能存在逻辑漏洞，这点很简单通过模拟器或者测试机安装微信然后通过小程序入口打开需要测试的小程序即可。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-16665932081.gif)

**0x03**

众所周知在web系统测试中经常会碰到一些隐藏接口或者是敏感的注释信息，往往我们可以通过浏览器自带的调试功能或者View Page Source来浏览源码，进行相关信息的查找工作。那么并非运行在浏览器上的微信小程序该怎么F12查看源码呢?

首先让我们先简单认识一下 .wxapkg 它是微信小程序的包后缀，此类文件是一个二进制文件，且文件结构如下图（该图引用至lrdcq 2017年发表的微信小程序阅读笔记 注：未对该笔记中技术点做验证可能某些技术点可能已过时仅提供参考）。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593209.png)

因为篇幅限制（能力有限）解包的技术细节不做深入探究。有兴趣的同学可自行了解，或者期待我们未来某一期的文章。以下文章内容只是对工具的使用以及一些踩坑点做说明；

在开始前先贴上我的环境

模拟器：逍遥模拟器（安卓版本为7.1）

nodeJs：v14.15.3

wxappUnpacker：https://github.com/xuedingmiaojun/wxappUnpacker

微信开发者工具：https://developers.weixin.qq.com/miniprogram/dev/devtools/download.html

那让我们开始，通过模拟器获取wsapkg文件。该文件的存储路径位于/data/data/com.tencent.mm/MicroMsg/{32位的16进制字符串文件夹}}/appbrand/pkg/

如下图所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593210.png)

由于文件的命名毫无规则可循所以只能通过下载时间来判断哪个是最新的包，然后通过adb将其传输到本地备用。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593211.png)

简单配置npm让其使用淘宝镜像，加速依赖包的安装

命令：npm config set registry https://registry.npm.taobao.org

验证配置是否生效：

命令：npm conf get registry

返回如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593214.png)

然后切换至wxappUnpacker项目目录。

依次执行以下命令。

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image38.png "image38.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/10/image38.png)

接着我们开始解包，windows系统使用bingo.bat, linux系统使用bingo.sh。

注意部分小程序可能存在分包即不仅仅只有一个主包，该情况可以使用-s参数来指定主包的源码路径即可自动将子包的wxss,wxml,js解析到主包对应位置下。

解包的命令如下：

解主包：./bingo.bat testpkg/master-xxx.wxapkg

该命令会将主包解出的源码存放在testpkg目录下的master-xxx目录中

解子包：./bingo.bat testpkg/sub-1-xxx.wxapkg -s=../master-xxx

该命令会将子包解出的源码存放在testpkg目录下的sub-1-xxx目录中，并自动将wxss,wxml,js解析到testpkg /master-xxx目录中（解分包时不推荐使用相对路径，碰到报错请使用绝对路径或切换到linux平台）

目录示意图如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593215.png)

将解包完的源码导入微信开发者工具，并在详情->本地设置中勾选不校验合法域名。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593218.png)

在设置->代理设置中设置burp监听地址。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593222.png)

测试抓包。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593224.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593236.gif)

**0x04**

什么以上方法无效碰上了反编译失败或反编译后的小程序无法在本地开发环境中跑起来，遇到这种疑难杂症咋办呢。是否可以直接通过设置模拟器或者测试机的系统代理直接抓包呢。答案是可以的！但是由于Android 7.0及之后系统默认的网络安全性配置变高导致系统默认不在信任用户添加的CA证书，只信任每个应用自己定义的CA证书集以及系统预装的CA证书。那么只需要把burp或者其他抓包软件的证书添加到/system/etc/security/cacerts/中即可。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593243.png)

首先让我们从burp中导出证书。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-16665932431.png)

安卓系统中的证书命名规则为<Certificate\_Hash>.<Number>：Certificate\_Hash表示证书文件的hash值，Number是为了防止证书文件的hash值一致而增加的后缀。证书的hash值是可以由openssl计算得出具体命令如下：

```
openssl x509 -inform DER -subject_hash_old -in <Certificate_File>
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593246.png)

然后开始制作证书

type 1.der > 9a5ba575.0

openssl x509 -inform DER -text -in 1.der -out 1 (获取证书信息)

type 1 >> 9a5ba575.0 （将证书信息追加的9a5ba575.0中）

接下来通过adb或其它方式将证书传输到手机，若使用adb传输需要打开开发者模式中的usb调试功能。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593247.png)

通过adb devices 列出可用设备。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593253.png)

当存在可用设备后就可以将证书文件传输到模拟器中了，命令如下

```
adb push <Certificate_File_path> /sdcatd/
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-16665932531.png)

通过adb shell 进入手机

进入后记得使用su切换为root权限，否者会因为权限问题无法进行某些操作（出现#即代表当前权限为root，因为我之前执行过所以进来之后就是root权限了）

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-16665932532.png)

挂载 /system目录为可读写。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-16665932533.png)

移动刚拷贝进来的证书到系统证书目录下。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-1666593254.png)

最后修改权限重启。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-16665932541.png)

设置系统代理为burp监听地址后打开小程序查看抓包结果。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189727-16665932542.png)

打开小程序成功抓到包。

![](https://secpulseoss.oss-cn-shanghai.aliyun...