---
title: JFinalcms代码审计
url: https://www.secpulse.com/archives/205511.html
source: 安全脉搏
date: 2024-12-19
fetch_date: 2025-10-06T19:35:25.306787
---

# JFinalcms代码审计

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

# JFinalcms代码审计

[代码审计](https://www.secpulse.com/archives/category/articles/code-audit)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-18

19,862

JFinalCms是开源免费的JAVA企业网站开发建设管理系统，极速开发，动态添加字段，自定义标签，动态创建数据库表并crud数据，数据库备份、还原，动态添加站点(多站点功能)，一键生成模板代码。

环境布置：IDEA打开项目，等待maven加载好。

使用phpstudy集成的mysql5.7数据库即可，导入JFinalCMS.sql数据库。

修改pom文件：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507540.png)

使用local9.0.90TOMCAT，JDK环境1.8。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507541.png)

运行TOMCAT，打开后台:

<http://localhost:8081/cms_war_exploded/>

反射xss：

搜索/admin/login定位到代码块：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507542.png)

由上可见，通过getPara获取账号密码后再通过render渲染到前端页面：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507543.png)

再分析前端代码构造xss进行闭合：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507544.png)

存储xss：

前台存在留言功能，留言会被管理员审核：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507545.png)

登录后台，点击扩展管理，留言信息：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507546.png)

原理同上。

Sql注入漏洞（1）：

该CMS存在很多处sql注入漏洞，大多数都是以+直接拼接sql注入语句造成，可以全局搜索+号寻找注入点。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507547.png)

找到以上代码块，可以直接看到title参数通过+直接拼接进入sql语句执行，于是我们继续找前端是调用的什么接口，并看看是否在接受参数时进行了过滤。

搜索findPage参数：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507548.png)

可以看到Contentcontroller层中存在title参数，点进去，定位到具体代码块：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507549.png)

可以看到调用了getPara方法获取传入的title参数，继续跟进getPara方法：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507551.png)

并未重写该方法，只是简单获取参数，未进行任何过滤，回到原来的controller层，向上翻，找到接口调用，数据包如下：

```
POST /cms_war/admin/content/data HTTP/1.1

Host: localhost:8081

User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:130.0)
Gecko/20100101 Firefox/130.0

Accept: text/html, \*/\*; q=0.01

Accept-Language:
zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2

Accept-Encoding: gzip, deflate, br

Content-Type: application/x-www-form-urlencoded; charset=UTF-8

X-Requested-With: XMLHttpRequest

Content-Length: 47

Origin: http://localhost:8081

Connection: keep-alive

Referer: http://localhost:8081/cms_war/admin/content

Cookie: JSESSIONID=EF8BB53892173B8A4577EFC32D0215BA;
listQuery=categoryId%3D&title%3D&sorts%3D&pageNumber%3D1

Sec-Fetch-Dest: empty

Sec-Fetch-Mode: cors

Sec-Fetch-Site: same-origin

Priority: u=0

categoryId=&title=%E7%BD%91&sorts=&pageNumber=1
```

将localhost替换为物理机IP放入sqlmap：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507552.png)

证明存在sql注入漏洞，其对应前端功能如下：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507553.png)

Sql注入漏洞（2）：

前台搜索框处也存在sql注入漏洞，只不过此处的调用过程较难找到。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507554.png)

如上图搜索关键字search定位到代码块：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507555.png)

仔细分析如上代码，我无法追踪keyword的具体调用。

以上代码是通过setAttr方法直接存储到当前请求的属性当中。我对keyword处打断点调试也未理清楚它后续是如何调用的。

于是再换一种思路，直接全局搜索keyword：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507556.png)

定位到具体代码，但无法确定是否是调用的此处findPage代码来构造sql。

搜索findPage也没有明确思路。

于是改变思路，由于keyword关键字最终是通过模板template渲染调用。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507557.png)

于是在template处挨个点进去找类似功能代码：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507558.png)

最终定位到代码块：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507559.png)

根据注释明确此处代码是根据不同关键词进行搜索，包含关键词keyword，继续查看keyword调用链：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507560.png)

确定是通过调用findPage，传入keyword参数来调用数据：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507561.png)

用sqlmap验证keyword参数：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507562.png)

任意文件读取：

翻找controller层代码，找到文件下载代码块：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507563.png)

可见未对传入的fileKey参数进行过滤，直接拼接进行文件读取。

（且我在翻找filter过滤器后，发现似乎 并未对该路径进行权限校验，可进行未授权调用接口）

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410141507564.png)

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/205511.html**](https://www.secpulse.com/archives/205511.html)

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
* [![伏特漏洞扫描云平台](/wp-conte...