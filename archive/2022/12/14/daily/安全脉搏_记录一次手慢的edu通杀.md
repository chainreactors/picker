---
title: 记录一次手慢的edu通杀
url: https://www.secpulse.com/archives/193413.html
source: 安全脉搏
date: 2022-12-14
fetch_date: 2025-10-04T01:22:57.352381
---

# 记录一次手慢的edu通杀

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

# 记录一次手慢的edu通杀

[资讯](https://www.secpulse.com/archives/category/news)

[TideSec](https://www.secpulse.com/newpage/author?author_id=26366)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-13

11,596

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916565.png)

**注：参加某edusrc平台活动，已授权，本文部分图文无关**！部分图片厚码请谅解。

首先打开站点，发现是一个教学平台，直接有账号密码，连注册都省了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916566.png "null")

## xss

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916570.png "null")

点击修改，标题插入xss

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916571.png "null")

点击确定保存返回，发现尖括号都被转义了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916572.png "null")

再次修改，闭合双引号

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916573.png "null")

确定后保存，再次点击修改进入页面

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916574.png "null")

水到第一个洞

## sql

ajax方法请求的Url有sql注入

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916576.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916578.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916580.png "null")

继续测试，上传图片接口有白名单+黑名单校验

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916583.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916584.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916585.png "null")

只能从其他地方入手了。

## upload

但是看了一眼上传框的UI

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916587.png "null")

怎么这么像ueditor，而且.net版本的ueditor可以接口实现文件上传getshell，具体文章参考潇湘信安公众号的文章： [https://mp.weixin.qq.com/s/mH4GWTVoCel4KHva-I4Elw](https://mp.weixin.qq.com/s?__biz=Mzg4NTUwMzM1Ng==&mid=2247488846&idx=1&sn=230f1884b9978bc06eda23e5748ff945&scene=21#wechat_redirect "https://mp.weixin.qq.com/s?__biz=Mzg4NTUwMzM1Ng==&mid=2247488846&idx=1&sn=230f1884b9978bc06eda23e5748ff945&scene=21#wechat_redirect")

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916588.png "null")

所以现在是要找到ueditor的路径。在网站上翻找，发现uedirot配置文件的路径，就在网站根目录下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916589.png "null")

离getshell更近了。访问可以上传文件的action看看 `http://xxx.com/ueditor/net/controller.ashx?action=catchimage`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916592.png "null")

和想象中的不一样啊，怎么出现了500报错？没学过.net的我哭了，但是可以暂时得出一个结论，这个ueditor的配置做了一些改动，必须通过其他文件来调用才能实现ueditor原有的功能。继续往下看数据包，发现了另外一个ueditor的url

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916595.png "null")

打开url

`http://xxx.com/xUeditor.UeditorConfig.cspx?action=config&&noCache=1666165414111`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916597.png "null")

这是ueditor的配置文件，注意看action参数`config`，把他改问能上传文件的action`catchimage`试试

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916599.png "null")

好了，直接按照文章的方法,首先试试1.5.0版本的payload

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-16709165991.png "null")

有请求，而且返回了webshell地址

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916601.png "null")

拿下 发现网站目录下还有不少其他大学类似的网站，感觉像是EDU的一个开发商

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916604.png "null")

于是在EDU上搜索了一下发现果然在厂商名单中

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916606.png "null")
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916608.png "null")

爽，正当我沉浸在马上要刷屏edu SRC的时候，点进去一看发现在7月份的时候有一位师傅已经交过了......

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916610.png "null")

寄以此文，纪念我这小菜鸡第一次挖掘到的EDU通杀漏洞。感觉有些时候通杀并没有很难，就是需要多细心，如果一次利用不成功，不要着急，细心下来思考其他利用点，说不定就会有意外的收获。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-193413-1670916613.gif)

E

N

D

**本文作者：[TideSec](newpage/author?author_id=26366)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/193413.html**](https://www.secpulse.com/archives/193413.html)

Tags: [edu](https://www.secpulse.com/archives/tag/edu)、[SQL注入](https://www.secpulse.com/archives/tag/SQL%E6%B3%A8%E5%85%A5)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![代码审计 | Wavsep靶场审计防御](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1686638778312.png)

  代码审计 | Wavsep靶场审计防御](https://www.secpulse.com/archives/201916.html "详细阅读 代码审计 | Wavsep靶场审计防御")
* [![【零基础】SRC实用漏洞挖掘技巧-附5个漏洞实例解析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-1683602931-300x191.png)

  【零基础】SRC实用漏洞挖掘技巧-附5个…](https://www.secpulse.com/archives/200077.html "详细阅读 【零基础】SRC实用漏洞挖掘技巧-附5个漏洞实例解析")
* [![SQL注入系列篇 | 报...