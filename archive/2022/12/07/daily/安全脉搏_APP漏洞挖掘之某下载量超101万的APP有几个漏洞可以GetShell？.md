---
title: APP漏洞挖掘之某下载量超101万的APP有几个漏洞可以GetShell？
url: https://www.secpulse.com/archives/192793.html
source: 安全脉搏
date: 2022-12-07
fetch_date: 2025-10-04T00:38:49.958136
---

# APP漏洞挖掘之某下载量超101万的APP有几个漏洞可以GetShell？

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

# APP漏洞挖掘之某下载量超101万的APP有几个漏洞可以GetShell？

[漏洞](https://www.secpulse.com/archives/category/vul)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-06

9,961

声明：Tide安全团队原创文章，转载请声明出处！文中所涉及的技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途以及盈离等目的，否则后果自行承担！

# 前言

过完阴雨绵绵的十一国庆，接到APP漏洞的项目，从开始的迷茫、什么思路也没有，甚至两三天从早挖到晚一点收获都没有，到后面不断看网上的文章、实践总结，借助神器和运气某天能挖到六七个漏洞，晚上做梦都在想挖洞挖洞，睡眠不足白天也精神抖擞的，也算是获得了些APP漏洞挖掘的经验吧。后续勤奋的话可能会陆续输出一些APP漏洞挖掘的实战文章、经验总结文章。文章中的漏洞已修复，仅在此提供思路，记录学习过程。

话不多说，正题开始。

先看看这个APP的下载量：1014408，距离上个月挖这个APP时又多了2000的下载，下载量还是不小的。最开始也只是敢挖一些下载量几百的APP，后面发现下载量跟有无漏洞其实没有太大关联。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306120.png)

顺手查了注册资本561万，算是比较少的。其实有无漏洞，漏洞量多少，跟注册资本也不一定有绝对的关联。只能告诉我这个洞CNVD、SRC肯定不收...

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306125.png "null")

# 收集资产

1. 1. 豌豆荚下载app，使用AppInfoScanner收集资产。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-16703061251.png)

1. 2. 输出资产表，就可以通过表中内容查找相关资产的漏洞了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306131.png)

1. 1. 指纹查询

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306135.png)

# 漏洞挖掘

## 漏洞一：Webapp处存在SQL注入漏洞

漏洞点一：https:// wxapi.某.com/Webapp/video.html?aid=，域名与APP包名一致，且页面下方指示的APP也是测试的APP，所以肯定属于某APP的资产。地址有参数，猜想可能有注入。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306140.png)

抓包，挂上代理，放到sqlmap中跑。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306146.png)

果然存在注入，这是第一个注入点。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306149.png)

上个月测试这款APP的时候没有很仔细，未找到这个SQL注入?，当时注的是左边的GET请求。这次写这篇文章，才又发现了这个注入点，所以测试的时候尽量仔细些，减少遗漏。（这就去CAPPVD提交上?，温故而知新，古人诚不欺我）。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306154.png)

## 漏洞二：会员中心存在DOM型XSS漏洞

漏洞点二：https: // wxapi.某.com/Webapp/Get-vip-test.html?username=，该APP的会员中心。BP中装了很多漏洞插件，抓包的时候会自动进行测试。这个漏洞也是在写文章的时候发现的?，看到域名有username参数本来想测试SQL注入的，但刚才的SQL注入也出自Webapp这个路径，就算了。然后就看到BP的Dashboard有个高危，插入payload测试，漏洞就这么被发现了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306155.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306162.png)

以上呢，AppInfoScanner输出的域名就挨个筛查完了，其实还找到了后台，用的齐博CMS，存在admin用户但是没有爆破出密码，也没找到别的漏洞点，就暂时放弃了这块。接下来就要从APP本身入手了，苹果手机可能会存在抓不到包、证书等问题，难度较大，先从安卓下手。我使用的是豌豆荚，从豌豆荚上下载APP，设置好代理，调试网络确保BP能顺利抓包。BP抓取的手机数据包会有大量的非测试APP数据包，注意甄别就好。

## 漏洞三：APP头像上传处存在文件上传漏洞，可GetShell

打开头像上传，抓取数据包。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306165.png "null")

先上传一张正常图片，看返回结果是什么，是否显示上传后的路径，并能试验是否能访问到。如下图所示，上传功能正常，且返回上传后的路径。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-16703061651.png)

但是浏览器中无法访问到。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306166.png)

再仔细查看截取的数据包，在路径前加上/zy就可以正常访问。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306167.png)

接下来测试是否能正常解析，文件上传phpinfo()。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306171.png "null")

可正常访问，显示详细的phpinfo()信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306172.png "null")

直接上传一句话木马。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306174.png)

访问，成功解析。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306175.png "null")

蚁剑连接成功。（马已删除）

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306176.png)

## 漏洞四：APP首页搜索框存在SQL注入

随意输入数据，点击搜索，截取搜索框数据包。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306181.png "null")

使用Sqlmap进行测试

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306183.png "null")

注入点为key参数。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306185.png)

## 漏洞五：APP用户登录处存在SQL注入漏洞

截取用户登录处数据包。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306191.png "null")

直接使用BP插件发送到sqlmap进行注入。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-16703061911.png)

注入点为username参数。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306193.png)

# 总结归纳

一个APP可能存在多个漏洞，能发掘多少取决于技术能力和细心程度。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192793-1670306201.png)

这几次的挖掘AppInfoScanner功不可没，这款工具很早就从Tide安全攻防的知识星球中下载过，也经常看星球里大佬们分享过的相关文章、工具、新思路，但一直没有实践过，这次就好好用用它。刚开始的两三天毫无头绪的在豌豆荚中下载了十几个APP，一个一个安装、注册、测试，颗粒无收，想了想不能这么干，这样干下去25个洞猴年马月才能挖到。于是翻开工具包，找到AppInfoScanner，搜了一两篇文章了解用法之后就开始改变思路。首先APP是随机选择的，不看下载量，不看注册资本，当然，淘宝、京东、微信这种的不在选择范围内哈。下载好apk丢到AppInfoScanner跑。跑出来的结果有只有几条域名的、有空文件、也有扫出几百条相关或不相关域名信息的，挨个挨个排查筛选，相关的都点开看看，测测web接口、爆破敏感路径、找后台、弱口令、SQL注入、XSS、命令执行、其他端口存在的漏洞等等，觉得有可能的点都去试。资产表测完，才开始在手机上下载APP，先测试用户注册的地方，是否能爆破验证码、是否有短信轰炸、验证码是否明文显示在返回包中、验证码是否失效。登录后找找注入点、文件上传、任意文件下载，抓包修改参数看是否有越权、是否能查看他人信息等等，web方面的漏洞点都可以在A...