---
title: oasys系统代码审计
url: https://www.secpulse.com/archives/205606.html
source: 安全脉搏
date: 2024-12-18
fetch_date: 2025-10-06T19:38:11.873375
---

# oasys系统代码审计

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

# oasys系统代码审计

[代码审计](https://www.secpulse.com/archives/category/articles/code-audit)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-17

19,265

## 简述：

oasys是一个OA办公自动化系统，使用Maven进行项目管理，基于springboot框架开发的项目，mysql底层数据库，前端采用freemarker模板引擎，Bootstrap作为前端UI框架，集成了jpa、mybatis等框架。

下载地址：<https://github.com/misstt123/oasys>

此项目部署极为简单，我使用的是phpstudy的5.7版本mysql，修改application.properties配置，在IDEA导入oasys.sql数据后，就可以直接运行

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626386.png)

并访问后台地址：<http://localhost:8088/logins>

注意别端口冲突

## CSRF：

登录后台，在用户面板处，修改便签功能存在csrf漏洞。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626387.png)

点击修改，抓包，点击生成CSRF的Poc：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626388.png)

将生成Poc的URL复制到浏览器，访问：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626389.png)

访问后，发现已经按照Poc上内容进行了修改：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626390.png)

## SQL注入：

### 代码分析：

在pom文件发现采用mybatis依赖：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626391.png)

全局搜索${

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626392.png)

找到outtype参数，定位到xml文件：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626393.png)

符合sql注入条件，于是开始找对应接口，参数，全局搜索allDirector字段：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626394.png)

定位到接口层，于是找接口实现类，发现无，于是全局搜索该接口名称，找哪里引用了此接口：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626395.png)

发现AddController层引用该接口，并通过mapper进行数据库操作，在该controller层搜索原接口方法，定位到具体代码块：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626396.png)

可以看到该参数没有经过任何过滤，于是根据代码块注释进行漏洞复现：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626397.png)

在后台找到通讯录，找到外部通讯录，点击添加联系人：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626398.png)

抓包找到对应数据包：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626399.png)

将localhost换成自己对应的IP，放入sqlmap验证成功：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626400.png)

其实从最初的xml文件来看，其它几个参数也存在sql注入。

### 存储XSS：

登录后台后，用户处点击修改信息，插入xss代码造成弹窗。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626401.png)

根据提交保存的接口全局搜索：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626402.png)

找到相关信息，根据代码分析，无任何过滤直接存储，造成xss漏洞：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626403.png)

此后台很多地方也均无过滤，可以直接插入xss代码执行。

任意文件读取漏洞：

在控制层UserpanelController处，如下代码存在逻辑错误导致任意文件读取：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626404.png)

可以看出此代码块是用来处理图像请求，并将数据返回到http响应的代码。

这段代码我初看并没看懂，于是对代码进行详细分析：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626405.png)

红框代码逻辑很简单，先传入的f.getPath()值，再通过FileInputStream进行文件读取并返回到http响应。

关键就是f.getPath()的值怎么来的？

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626406.png)

如上红框代码，f.getPath()的值来自于rootpath与path的拼接，而path的值则是，先通过request.getRequestURI()获取，再将/image替换为空得来。

但rootpath的值呢？

于是我在该类搜索rootpath找到其定义代码：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626407.png)

发现以@Value注解定义rootpath的值，而@Value注解的作用就是从项目配置文件中获取信息，于是转到配置文件，搜索关键字：rootpath

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626408.png)

继续回到controller代码，此时找到rootpath的值，也明白了读取文件的逻辑，于是尝试构造多个/image..路径读取我D盘upload下的文件：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626410.png)

如下图，读取成功：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202411061626411.png)

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/205606.html**](https://www.secpulse.com/archives/205606.html)

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
* [![某个OA系统的代码审计](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/07/VCG21gic11158539.png)

  某个OA系统的代码审计](https://www.secpulse.com/archives/205256.html "详细阅读 某个OA系统的代码审计")

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
...