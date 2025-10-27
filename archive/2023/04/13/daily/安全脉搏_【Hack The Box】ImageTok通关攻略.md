---
title: 【Hack The Box】ImageTok通关攻略
url: https://www.secpulse.com/archives/198872.html
source: 安全脉搏
date: 2023-04-13
fetch_date: 2025-10-04T11:33:23.869981
---

# 【Hack The Box】ImageTok通关攻略

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

# 【Hack The Box】ImageTok通关攻略

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[公众号:安全女巫](https://www.secpulse.com/newpage/author?author_id=49672)

2023-04-12

12,769

如果你喜欢我的文章，欢迎关注公众号：安全女巫

转载请注明出处：<https://mp.weixin.qq.com/s/Jrlyle4CtMj3KBicEkAklQ>

本文为作者前期作品，发布在Freebuf。

## **前言**

全文中截图网站地址、数据库信息等不一致，因htb靶机具有时效性，故每次启动分配的靶机信息都不一致。

该文档是在操作过程中记录，难度较大，通关整个耗时7天，在间断性放弃中坚持，实属不易。

有对htb感兴趣的同学，可添加微信，一起学习~

## **信息收集**

访问网站，查看页面基本信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-1681288629.png)

发现页面只有文件上传功能。

## **文件上传**

选择任意图片，点击提交按钮。进行抓包后重放，响应码为302

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-16812886291.png)

响应包中存在两个cookie，且两个cookie的前半部分一致

复制第一个cookie，进行智能解码，发现包含==。此为base64特征

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-1681288630.png)

所以只将前半部分进行base64解码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-1681288631.png)

发现此为文件上传后图片名称，猜测username为网站用户名。将之更改为admin后更新cookie

eyJmaWxlcyI6W3siZmlsZV9uYW1lIjoiZjBhNzcucG5nIn0seyJmaWxlX25hbWUiOiI1ZTIzNC5wbmcifSx7ImZpbGVfbmFtZSI6IjI0MjdmLnBuZyJ9LHsiZmlsZV9uYW1lIjoiZGViNTcucG5nIn1dLCJ1c2VybmFtZSI6ImFkbWluIn0=.JDJ5JDEwJGZHNGhWaU9OSk1DZDhxaldrQllVbS5TcDBvZGtFNUpTclBETTJhdW5VZzFqd09UM3BEeXFh

将该cookie替换，得出响应包中cookie，并进行解码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-16812886311.png)

解码后为admin，证明该cookie为admin。

替换该处cookie为admin

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-1681288632.png)

虽然是admin权限，但刷新页面功能并无变化。接着进行代码分析，寻找突破

## **代码分析**

### **1》入口文件index.php**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-16812886321.png)

### **2》/info**

可见/info能看到phpinfo信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-1681288633.png)

得到数据库主机、用户名、数据库名等信息。

### **3》/proxy**

看到proxy能想到的是ssrf

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-1681288634.png)

以上代码说明，url请求能正常执行的条件

1.session中username=admin

2.远程服务器127.0.0.1

3.Post请求的url参数不为空

4.Host在列表中任意一个即可
['uploads.imagetok.htb', 'admin.imagetok.htb']

5.Port在列表中['80', '8080', '443']

跟进CustomSessionHandler.php文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-1681288635.png)

可知，cookie可以.分割，取.之前的部分，然后进行base64解码，解码后得到username。刚好用以判断session中username=admin

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-1681288636.png)

此部分为cookie生成规则，json数据格式进行base64编码+.+后面随机生成规则后base64编码。

故，我们可以拼接的方式以此生成新的cookie来绕过

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-16812886361.png)

以上5个条件均能绕过，故可使用ssrf来发送gopher协议请求来攻击mysql。目前知道mysql相关信息，可具体mysql语句如何利用。怎么回显都不太清楚，可继续看代码

### **4》UserModel.php**

该文件在入口文件处加载

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-1681288637.png)

跟进UserModel.php文件updateFiles函数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-1681288638.png)

可获取session中username的值，查询出由该用户名插入的文件名，接着将该文件名插入session的files中。

我们可伪造username为admin，若插入一条数据，file\_name=flag、username=admin。再通过直接访问主页，获取主页session.进行解码，即可得到解码后file的值即为flag。

刚好可利用gopher协议攻击mysql，插入一条mysql语句，通过查询的方式得到flag。

### **5》/upload**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-16812886381.png)

文件名为随机生成，只允许上传png文件，其他格式不允许。

综上。使用ssrf来发送gopher协议请求来攻击mysql，构造mysql语句使flag展示在session中的file。伪装图像绕过文件检测，上传该payload图片触发漏洞。

接下来对漏洞利用步骤进行分解：

1.插入flag到file\_name字段的Mysql语句拼接

2.gopher协议构造

3.Admin session伪造

4.编写图片生成脚本以绕过检测

5.上传payload图片

6.访问主页获取session

7.Session用.分割，取.之前的部分进行base64解码后得到file中值即为flag。

## **漏洞利用**

### **Mysql语句拼接**

1.查询出数据库中现存的flag值

2.插入一条数据将现存的flag存入文件名file\_name字段中

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-1681288639.png)

entrypoint.sh文件可知完整sql语句，且flag已被插入数据库。故构造查询flag语句：

SELECT flag FROM db\_fjqaG.definitely\_not\_a\_flag。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-1681288640.png)

接着插入一条新数据，以供flag可存入session的file中。故构造insert语句：

INSERT INTO db\_XhnWU.files(file\_name, checksum, username) VALUES('查询出的flag值','abc','admin');

完整mysql语句如下：

INSERT INTO db\_XhnWU.files(file\_name, checksum, username) VALUES((SELECT flag FROM db\_XhnWU.definitely\_not\_a\_flag),'abc','admin');

### **Gopher协议构造**

有数据库主机、用户名、数据库名，考虑可以使用gopher攻击mysql，生成协议可使用gopherus工具。

安装 https://github.com/tarunkant/Gopherus

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198872-16812886401.png)

注意格式gopher:///。

所以重新组成新的gopher链接：gopher:///127.0.0.1:3306/\_字符串

### **Admin session伪造**

上述文件上传部分已经实现了admin session伪造的发现过程。这边简述步骤。

1.文件上传抓包后重放，获取响应包中session

2.将响应包中session替换请求包中session再次发包

3.再次获得响应包中session替换请求包中session再次发包

4.获得响应包中session以.进行分割。(.前面部分进行base64解码成为包含username的json，将username改为admin，重新base64编码)+(.后面部分)=新的session

如此得到的便是Admin session.

### **编写图片生成脚本以绕过检测**

PHAR (“Php ARchive”) 是PHP里类似于JAR的一种打包文件，在PHP 5.3 或更高版本中默认开启，这个特性使得 PHP也可以像 Java 一样方便地实现应用程序打包和组件化。一个应用程序可以打成一个 Phar 包，直接放到 PHP-FPM 中运行

前面内容不限，但必须以\_\_HALT\_COMPILER();?>来结尾，否则phar扩展将无法识别这个文件为phar文件。也就是说如果我们留下这个标志位，构造一个图片或者其他文件，那么可以绕过上传限制，并且被 phar 这函数识别利用。

生成phar文件，修改后缀为jpg，上传文件处修改filename为‘phar://phar.jpg’,读取到flag

所以

Php.ini中去掉最前面的分号

extension=soap

Phar.readonly = Off

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content...