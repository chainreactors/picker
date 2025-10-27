---
title: 青少年CTF-Web-帝国CMS1-3通关记录
url: https://www.secpulse.com/archives/193089.html
source: 安全脉搏
date: 2022-12-10
fetch_date: 2025-10-04T01:04:34.623848
---

# 青少年CTF-Web-帝国CMS1-3通关记录

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

# 青少年CTF-Web-帝国CMS1-3通关记录

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[青少年CTF](https://www.secpulse.com/newpage/author?author_id=49279)

2022-12-09

13,632

# 0x01说明

本次进通过平台内题目进行，非真实环境。

# 帝国CMS01

![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image2.png "image2.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image2.png)

首先下发题目链接

![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image3-1024x722.png "image3-1024x722.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image3.png)

我们首先先找后台看看

![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image4-1024x722.png "image4-1024x722.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image4.png)

后台地址为`/e/admin/`

随后，经过dirsearch进行扫描，得到了一个www.zip

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image5.png "image5.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image5.png)![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)

![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image6.png "image6.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image6.png)

访问扫描到的www.zip，得到网站源码

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image7.png "image7.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image7.png)![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)

使用D盾扫描，得到eval后门。

![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image8.png "image8.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image8.png)

蚁剑链接

得到根目录的Flag

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image9.png "image9.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image9.png)![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)

# 帝国CMS02

![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image10-1024x557.png "image10-1024x557.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image10.png)

这道题目和CMS01差不多，但是好像又有天差地别

![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image11.png "image11.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image11.png)

管理员发现你入侵了他的服务器，管理员修改了密码并删除了后门

那么我们优先尝试管理员是不是给了一个弱口令

经过弱口令爆破

![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image12-1024x270.png "image12-1024x270.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image12.png)

登陆成功

密码为123456789

# 帝国CMS03

![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image13.png "image13.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image13.png)

这道题目考察了一个帝国CMS的漏洞利用，我们先看看帝国CMS03有什么漏洞呢？

提示这里还是弱口令，我们上后台看看

密码还是刚刚的

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image14-1024x267.png "image14-1024x267.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image14.png)![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)

登陆成功，但是这里没有Flag

![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image15.png "image15.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image15.png)

通过备份这里的漏洞

执行了phpinfo()![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image16.png "image16.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image16.png)

在环境变量中并没有我们想要的flag

那么我们还有一个CVE可以通过数据表模板进行写入文件

CVE-2018-18086

![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image17.png "image17.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/image17.png)

先写个一句话

并且用file\_put\_contents这个函数进行写入网站

重命名为xxx.php.mod

接着在下方图片所示位置导入

[![image.png](https://secpulseoss.os...