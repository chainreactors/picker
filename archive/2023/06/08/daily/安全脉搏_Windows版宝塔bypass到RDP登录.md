---
title: Windows版宝塔bypass到RDP登录
url: https://www.secpulse.com/archives/201484.html
source: 安全脉搏
date: 2023-06-08
fetch_date: 2025-10-04T11:46:53.156244
---

# Windows版宝塔bypass到RDP登录

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

# Windows版宝塔bypass到RDP登录

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-06-07

47,081

**声明**

本文所提供的工具仅用于学习，禁止用于其他，请在24小时内删除工具文件！！！

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109946.gif)

**01 背景**

在一次攻防演练中，利用漏洞获取到一个`webshell`，站点是`php`的，最后发现这个`webshell`的权限竟然是`system`，但是无法执行命令，最后发现是`Windows`版本的宝塔，结合网上各位师傅的文章，在这里记录下如何`bypass`到3389登录的。

**02 getshell**

直接上`webshell`，上了蚁剑、冰蝎、哥斯拉，发现没有`waf`拦截，上蚁剑，`windows`的机器，权限很高是`system`，执行命令，发现都是返回错误：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109947.png)

使用哥斯拉看下，可以看到就是宝塔：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109948.png)

同样在`fofa`上看到开放了`888`端口，其实就可以猜是宝塔了：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109949.png)

这是官网关于面板的介绍：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109951.png)

既然是`Windows`版本的`bt`的话，那这个`webshell`权限就是`system`是没有问题的，现在就是想办法拿`bt`面板或者`bypass`执行命令了。

**03 宝塔bypass之路**

在`bypass`宝塔之前，也看到过替换`php.ini`文件、`mysql`提权的，但经过测试都是失败的，因此在这里尝试直接拿下宝塔面板。

### **3.1 寻找宝塔后台**

通过参考师傅的文章，找到了宝塔的路径信息：

```
C:/BtSoft/panel/data/admin_path.pl
```

发现路径：`/xxxxxx`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109953.png)

一般来说，宝塔的面板默认端口就是`8888`，因此直接加上之后访问：无论是内网还是外网，发现依旧访问不到：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109955.png)

最后发现，自己找偏了，宝塔面板的端口信息是保存在宝塔的配置文件里面的，开发者修改了`bt`修改了默认的访问端口， 通过查阅资料，在这里发现了相关信息：https://newsn.net/say/bt-login-reset.html

宝塔的配置信息：

```
路径相关配置文件如下：
面板域名，/www/server/panel/data/domain.conf
面板端口，/www/server/panel/data/port.pl
安全入口，/www/server/panel/data/admin_path.pl
授权IP，/www/server/panel/data/limitip.conf
```

开始翻文件，最后找到了端口：`xxx`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109958.png)

找到之后，拼接访问，其实这个面板地址在内、外网均可访问：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/image4-1024x571.png "image4-1024x571.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/image4.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109959.png)

### **3.2 登录面板后台**

现在路径和端口都找到了，开始找面板密码，面板的密码是保存在`data`目录下的`default.db`里面的，直接下载到本地，然后使用工具打开之后，开始修改：

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/image3-1024x237.png "image3-1024x237.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/image3.png)

宝塔的密码是加盐的，无法直接通过`hash`解密，所以在这里要替换或者是新增：

在这里要分为两种宝塔来操作了：

* 如果是老版本宝塔的话，可以再添加一个用户来打开，在这里可能不太准确，我以前发过`linux`版本的宝塔是可以通过添加用户来新增登录的，但是后来新版宝塔就无法再使用新增用户的方法来操作了，必须替换才可以，但是`Windows`版的我就不太清楚了
* 如果是新版本宝塔的话，只能够修改密码，登录成功之后，再修改回去，这个是`linux`版新版是这样的，但是`Windows`的我确实不太清楚

也可以前往github下载：

```
https://github.com/crow821/crowsec
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109962.png)

将这个值以及盐的值，以及账号等新增到里面去试试看，在这里先尝试直接新增，如果真的不行，到时候再替换，因为替换太麻烦了：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109963.png)

修改之后，将文件替换下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109964.png)

记得在替换之前，将原来的文件进行备份，防止出现意外，数据无法恢复。替换之后尝试登录：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-16861099641.png)

在这里运气比较好，直接登录成功。

### **3.3 宝塔任务计划添加用户**

进了宝塔面板的后台，并且权限是`system`，在`fofa`上看到该服务器开启了`3389`远程桌面，所以在这里通过计划任务添加用户：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109966.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109967.png)

添加之后，会自动执行一次：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-1686109968.png)

执行成功之后，记得及时删除这两个任务计划。

### **3.4 3389远程登录**

直接尝试`3389`：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201484-16861099681.png)

**04 总结**

`Windows`版本的宝塔好像比`linux`版本的宝塔好绕过一点。

以上文章来源于乌鸦安全 ，作者crowsec

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/201484.html**](https://www.secpulse.com/archives/201484.html)

Tags: [rdp登录](https://www.secpulse.com/archives/tag/rdp%E7%99%BB%E5%BD%95)、[windows](https://www.secpulse.com/archives/tag/windows)、[冰蝎](https://www.secpulse.com/archives/tag/%E5%86%B0%E8%9D%8E)、[哥斯拉](https://www.secpulse.com/archives/tag/%E5%93%A5%E6%96%AF%E6%8B%89)、[宝塔bypass](https://www.secpulse.com/archives/tag/%E5%AE%9D%E5%A1%94bypass)、[蚁剑](https://www.secpulse.com/archives/tag/%E8%9A%81%E5%89%91)

点赞：
4
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Responder与evil-winRM配合远程登录Windows](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/16872431395792-300x192.png)

  Responder与evil-winRM…](https://www.secpulse.com/archives/203051.html "详细阅读 Responder与evil-winRM配合远程登录Windows")
* [![Windows自带的持久化后门——SDDL](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201392-1685958844-300x192.png)

  Windows自带的持久化后门——SDD…](https://www.secpulse.com/archives/201392.html "详细阅读 Windows自带的持久化后门——SDDL")
* [![技术研究 – 从零开始学习 DLL 劫持](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-c...