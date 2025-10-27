---
title: 某小型CMS漏洞复现审计
url: https://www.secpulse.com/archives/205583.html
source: 安全脉搏
date: 2024-12-19
fetch_date: 2025-10-06T19:35:28.348955
---

# 某小型CMS漏洞复现审计

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

# 某小型CMS漏洞复现审计

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-18

8,976

## SQL注入

### 漏洞复现：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657448.png)

登陆后台，点击页面删除按钮，抓包：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657449.png)

rid参数存在sql注入，放入sqlmap检测成功：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657450.png)

### 代码分析：

Ctrl+Shift+F检索路由：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657451.png)

定位具体代码，为删除功能：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657452.png)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657453.png)

发现deleteByIds调用了传参rid，跟进：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657455.png)

发现进入Dao层，此处依旧调用的deleteByIds，于是找ICommonDao接口实现类：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657456.png)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657457.png)

定位到该类，发现以ids参数接受原先用户传入的rid参数，并在new一个sql对象后，直接将ids参数进行拼接，并通过原生jdbc执行返回结果。

## 模板注入

内容管理-文件管理-themes-flatweb-about.html，选择编辑，插入payload：

<#assignvalue="freemarker.template.utility.Execute"?new()>${value("calc.exe")}

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657458.png)

访问首页，点击关与我们：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657459.png)

执行命令，弹出计算机：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657460.png)

### 代码分析：

配置文件存在freemark

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657461.png)

## 文件上传

### 漏洞复现：

这个CMS感觉上传文件路径不是很好找，所以上传时先找个合适的目录再点击上传文件。

文件管理处点击admin进入目录：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657462.png)

再点击文件上传：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657463.png)

通过上传jsp马，不过需要以jspx或者jspf后缀绕过上传。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657464.png)

### 代码分析：

上传时抓包，根据路由全局搜索：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657465.png)

定位到具体代码段：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657466.png)

用filePath参数接受path参数与file参数拼接，再从filePth参数中取出文件名赋值给fname参数。

跟进getSuffix：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657467.png)

发现只是以简单点来获取后缀。

检测是否为jsp文件后，如果不为则进入为空判断，并以FileOutputStream与write直接上传写入。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657468.png)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657469.png)

## 任意文件删除

### 漏洞复现：

上传jsp马后，点击右方删除文件，抓包。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657470.png)

将下方数据包改为admin上级目录，删除我先前上传但没找到路径的test.jspx文件，删除成功：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657471.png)

### 代码分析：

根据数据包在IDEA全局搜索，定位到delete代码段：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657472.png)

该方法接收三个参数：path、name 和 data，这些参数通过 \@RequestParam注解从请求中提取，并进行简单拼接，赋值给file对象，此时file对象代表实际的文件名称。

跟进delete方法：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657473.png)

发现对传入的path参数进行了检查，继续跟进：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411011657474.png)

发现仅仅采用java自带的类java.security.AccessController下的checkPermission(Permissionperm)静态方法校验权限。

如果权限满足便直接通过fs.delete()方法删除，造成任意文件删除漏洞。

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/205583.html**](https://www.secpulse.com/archives/205583.html)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Solon框架模板漏洞深度剖析与修复实战](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/7266edd7-a4cc-444d-bacb-7ee802487ac4.png)

  Solon框架模板漏洞深度剖析与修复实战](https://www.secpulse.com/archives/206316.html "详细阅读 Solon框架模板漏洞深度剖析与修复实战")
* [![路由器安全研究：D-Link DIR-823G v1.02 B05 复现与利用思路](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202503171628715.png)

  路由器安全研究：D-Link DIR-8](https://www.secpulse.com/archives/206007.html "详细阅读 路由器安全研究：D-Link DIR-823G v1.02 B05 复现与利用思路")
* [![DedeBIZ系统审计小结](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202502121526395.png)

  DedeBIZ系统审计小结](https://www.secpulse.com/archives/205891.html "详细阅读 DedeBIZ系统审计小结")

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

#### 2022-05-12

[Mastering the Challenge！——来自The 3rd AutoCS 2022智能汽车信息安全大会的邀请函](https://autocs2022.artisan-event.com/)

#### 2021-11-18

[AutoSW 2021智能汽车软件开发大会](https://autosw2021.artisan-event.com)

#### 2021-06-27

[2021中国国际网络安全博览会暨高峰论坛](http://www.sins-expo.com)

#### 2021-05-27

[The 2nd AutoCS 2021智能汽车信息安全大会](https://artisan-event.com/AutoCS2021/)

#### 2020-12-18

[贝壳找房2020 I...