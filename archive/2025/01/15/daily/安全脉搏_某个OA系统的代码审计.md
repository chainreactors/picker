---
title: 某个OA系统的代码审计
url: https://www.secpulse.com/archives/205256.html
source: 安全脉搏
date: 2025-01-15
fetch_date: 2025-10-06T20:09:17.104030
---

# 某个OA系统的代码审计

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

# 某个OA系统的代码审计

[代码审计](https://www.secpulse.com/archives/category/articles/code-audit)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2025-01-14

20,934

2023年HVV中爆出来的洞了，但是有一些漏洞点修复了，刚好地市级的攻防演练中遇到了一个，想着把可能出现问题的点全部审计一下，顺便熟悉一下.net代码审计。ps:感兴趣的师傅们可以自行根据poc搜索源码。

## 0x1 反编译

好吧，当我没说，下载dnspy反编译即可，但是首先要找到web逻辑代码才能开始审计，因为这套oa是使用了mvc开发模式，简单介绍一下mvc，其实就是model，controller，view，其中的view是视图也就是html等展示给用户看的东西，model是模型也就是控制数据库的代码。controller是控制器负责执行代码的逻辑，也就是我们需要审计的地方了。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554123.png)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554126.png)

然后找到controller就是web的主要逻辑了。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554127.png)

## 0x2 身份校验绕过

首先可以随便点入一个controller，发现filesController继承自TopVisionApi。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554128.png)

然后我们发现IsAuthorityCheck()这个函数用于判断权限。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554129.png)

首先看到第一行代码getByValue这个函数,其实Request.Properties["MS\_HttpContext"]).Request[value]就是获取http请求中的某个参数，而value就是调用传过来的参数，在这里是token，那么这段代码就是获取http中的token参数。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554130.png)

然后if判断了token是不是空值然后再判断token参数的值是不是等于"zxh"，如果登录则直接返回一个UserInfo对象。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554131.png)

然后回到filesController的身份判断，发现只判断了IsAuthorityCheck返回是否为null，所以只需要让token参数是zxh的时候，那么就可以绕过身份校验了。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554132.png)

## 0x3 任意文件下载

还是 filesController 这个控制器 DownloadRptFile方法。这时我们已经绕过了身份认证，所以只需要看之后代码即可。requestFileName就是我们传递的http参数，

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554133.png)

然后跟进代码。并未发现任何过滤../的行为，直接传递给getBinaryFile函数![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554135.png)

getBinaryFile函数如下。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554136.png)

结果证明: （读取文件内容会以base64返回）

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554137.png)

## 0x4 信息泄露

发现GetCurrentUserList方法查询了所有用户信息。并且返回给前台。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554138.png)

<UserInfo>是c#中的泛型，这里是用来查询数据库的。可以看到遍历了dicUserList这个数组。这个数组就是初始化的用户信息数组了。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554139.png)

直接访问：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554140.png)

## 0x5 任意文件删除

发现DeleteFile2方法是一个删除文件方法。这里也没有发现过滤../以及过滤删除文件的后缀名。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554141.png)

虽然是有限制了文件路径，但是全然没有过滤../，而且filename参数也是完全可控的。所以这里其实是存在任意文件删除漏洞的。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554142.png)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554143.png)

ps: 这里就不放验证截图了，感兴趣的师傅们可以自行本地验证。

## 0x6 任意文件上传

UploadFile2方法中获取了各种参数，然后传入UploadFile2

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554144.png)

跟进该方法。pathType就是限制文件上传到哪个文件夹的。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554145.png)

pathType详解：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554146.png)

fs参数是我们传递的byte数组也就是文件的内容。

startPoint等于0就好这样才能创建一个新的文件，datasize则是数组的长度。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554147.png)

漏洞验证：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554148.png)

## 0x7 SQL注入

InventoryController的GetProductInv方法，直接从参数获取boxNoName未经过过滤直接通过string.Format拼接至sql语句中，导致了sql注入。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554149.png)

验证：直接sqlmap即可

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554150.png)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407231554151.png)

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/205256.html**](https://www.secpulse.com/archives/205256.html)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![TongWeb闭源中间件代码审计](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/e0d9b479-dc1b-4456-a829-57d65c82fb25.png)

  TongWeb闭源中间件代码审计](https://www.secpulse.com/archives/206365.html "详细阅读 TongWeb闭源中间件代码审计")
* [![记录一次CMS的代码审计](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2025/01/VCG41N1363057543.png)

  记录一次CMS的代码审计](https://www.secpulse.com/archives/205148.html "详细阅读 记录一次CMS的代码审计")
* [![JFinalcms代码审计](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/12/VCG41157508030.png)

  JFinalcms代码审计](https://www.secpulse.com/archives/205511.html "详细阅读 JFinalcms代码审计")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/12/logo-white.png)](https://www.secpulse.com/newpage/author?author_id=37244aaa) | [蚁景网安实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=37244) | |
| 文章数：402 | 积分： 877 |
| 蚁景网安实验室（www.yijinglab.com）网络安全靶场练习平台，涉及CTF赛前指导、职业技能训练、网安专项技能提升等。 | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 活动日程

[显示更多](https://www.secpulse.com/newpage/activity)

#### 2022-06-17

[Gdevops 全球敏捷运维峰会](https://www.bagevent.com/event/8022600?bag_track=AQMB)

#### 2022...