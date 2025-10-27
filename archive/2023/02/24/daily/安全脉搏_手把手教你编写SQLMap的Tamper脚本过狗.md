---
title: 手把手教你编写SQLMap的Tamper脚本过狗
url: https://www.secpulse.com/archives/196598.html
source: 安全脉搏
date: 2023-02-24
fetch_date: 2025-10-04T07:55:46.296291
---

# 手把手教你编写SQLMap的Tamper脚本过狗

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

# 手把手教你编写SQLMap的Tamper脚本过狗

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-02-23

13,416

https://xz.aliyun.com/t/11412

[sql注入bypass最新版某狗 (qq.com)](https://mp.weixin.qq.com/s?__biz=Mzg2NDY2MTQ1OQ==&mid=2247495616&idx=1&sn=6a40395292bab8c2cdf4fd77ed701201&scene=21#wechat_redirect "sql注入bypass最新版某狗 (qq.com)")

奇安信攻防社区-记一次实战过狗注入 (butian.net)

https://www.freebuf.com/sectool/179035.html

**本文仅用于技术讨论与学习**

## 测试环境

最新版某狗

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131619.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131620.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131621.png "null")

## 测试方法

**安全狗其实是比较好绕的WAF，绕过方法很多，但这里我们就用一种：注释混淆**

一招鲜吃遍天

注释混淆，其实就是在敏感位置添加垃圾字符注释，常用的垃圾字符有`/、!、*、%`等

这里再解释一下**内联注释**，因为后面要用到：

MySQL内联注释： `/*!xxxxxxx*/` !后面的语句会当作SQL语句直接执行

但是如果`!`后面跟着MySQL版本号，那么就会出现两种情况

* • 当`!`后面接的数据库版本号小于自身版本号，就会将注释中的内容执行
* • 当`!`后面接的数据库版本号大于等于自身版本号，就会当做注释来处理。

数据库版本号以五位数字表示，比如当前环境下数据库版本号表示为：50553

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131622.png "null")

`!`后面接小于50553的：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-16771316221.png "null")

执行了`select 1;`

`!`后面接大于等于50553的：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131623.png "null")

执行了 `select ;`

下面进入正题

## bypass

### and

`and 1=1`拦

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-16771316231.png "null")

但是把空格删掉就不拦了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131624.png "null")

所以，我们认为，and后面不能直接跟空格...

那么如果用其他形式表示空格呢？

前面说了，我们这次只使用注释混淆：

burp，抓包设置

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-16771316241.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131625.png "null")

长度5335是被拦截的

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131626.png "null")

长度为899的说明成功绕过

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131628.png "null")

我们选择其中一个作为空格的替代者就好了，这里我们选择`/*%*`

即：->`/*/*%**/`

同理 ，`or`是一样的：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131629.png "null")

### order by

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131630.png "null")

测试发现还是只要替换`order by`中间的空格就可以了，所以绕过方法和前面一样：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131632.png "null")

### union select

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131636.png "null")

`union select`使用之前的垃圾字符替换空格发现不行了：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131638.png "null")

但是先不急于换方法，再爆破一遍试试：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131640.png "null")

image-20221117231524071

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131641.png "null")

发现又有很多可以绕过的了。

所以我们再更改一下替换空格的垃圾字符， 这里选`/*/!%!/*/`

即：->`/*/!%!/*/`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131642.png "null")

### 获得当前数据库

正常语句：

```
?id=-1 union select 1,database(),3 --+
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131643.png "null")

绕过：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131644.png "null")

即：`()`->`(/*/!%!/*/)`

### 获取数据库中的表

正常语句：

```
?id=-1 union select 1,group_concat(table_name),3 from information_schema.tables where table_schema='security' --+
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-16771316441.png "null")

image-20221117234536391

绕过：

经过测试发现拦截的是`select +   from   +   information_schema`的组合

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131645.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131646.png "null")

中间加垃圾字符替换空格已经不管用了，我们尝试对关键字进行混淆。

对`information_schema`进行混淆测试：

首先使用内联注释，发现，这里的版本号不管写啥，都直接被拦。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131647.png "null")

考虑是检测了`select +   from   +   /*! +  information_schema`的组合

加个换行试试

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131648.png "null")

还是不行...

那既然都换行了，那我们再在换行前加一些垃圾字符：

> 如果我们直接插入垃圾字符，会当作SQL语句执行，所以前面还需要在垃圾字符前加个注释，可以是 `/**/`或`#`或`--+`
>
> 但是经过测试只有 `--+`好用

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196598-1677131649.png "null")

有这么多可以绕过的，我们随便选择一个，比如`/*%/`

这样，最终语句如下：

```
?id=-1/*/!%!/*/union/*/!%!/*/select/*/!%!/*/1,group_concat(table_name),3/*/!%!/*/from/*/!%!/*//*!00000--+/*%/%0ainformation_schema.tables*/%20where%20table_schema=database(/*/!%!/*/)--%20+
```

![](https://se...