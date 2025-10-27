---
title: 社会工程学 | office宏分离免杀及应急处置
url: https://www.secpulse.com/archives/195847.html
source: 安全脉搏
date: 2023-02-15
fetch_date: 2025-10-04T06:34:57.126364
---

# 社会工程学 | office宏分离免杀及应急处置

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

# 社会工程学 | office宏分离免杀及应急处置

[社会工程](https://www.secpulse.com/archives/category/articles/social-engineering)

[贝塔安全实验室](https://www.secpulse.com/newpage/author?author_id=9525)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-02-14

8,938

声明：本人坚决反对利用文章内容进行恶意攻击行为，一切错误行为必将受到惩罚，绿色网络需要靠我们共同维护，推荐大家在了解技术原理的前提下，更好的维护个人信息安全、企业安全、国家安全。

Office宏分离免杀的方式是在目标用户的office开启宏功能的前提下，诱骗其使用office办公软件打开文档，通过加载远程的恶意宏代码，达到控制目标主机权限的目的。

*1*Office宏木马

1、在桌面基础创建文档名称：beta.docx

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-1676358939.png)

2、进入word文档后，开启开发者工具

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-1676358940.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-1676358941.png)

3、打开Cobaltstrike后渗透工具，选择Attacks->Package->MS Office Macro

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-1676358942.png)

4、选择生成的Payload，这里选择使用Beacon http，会连到主机的IP地址是192.168.146.128

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-16763589421.png)

5、 点击复制宏代码

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-1676358943.png)

6、将代码复制到word文档中开发工具->Visual Basic的代码窗口中。右上角选择Auto\_Open，当使用者在打开word文档时，簿会自动运行宏提示信息。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-16763589431.png)

7、Ctrl+S保存后，会提示，点击否，选择保存类型：beta.dotm

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-1676358944.png)

8、鼠标右键单击beta.dotm文件，选择打开，(此处注意不能双击打开，双击是无法打开模版文件的，在模版文件上双击默认是以此模版创建新文件)，然后可以看到能正常反弹shell。接下来就可以做免杀处理了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-1676358945.png)

9、将后门宏文件beta.dotm上传到公网服务器中,开启apache服务即可

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-1676358946.png)

10、创建一个简历模板，更改后缀位压缩文件的格式为.zip，并进行减压。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-16763589461.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-1676358947.png)

11、将zip文件解压，进入/word/\_rels目录下，打开settings.xml.rels宏文件，将该段代码修改为以下内容，意思就是执行开启宏后，会执行访问下载服务器上的dotm宏文件并执行！！

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-16763589471.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-1676358948.png)

12、然后将内容重新压缩后，在修改zip为docx类型，修改后就可以打开简历了。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-16763589481.png)

*2*

应急处置

(1)查询异常的网络连接情况

```
netstat -ano | findstr "192.168.146.*"
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-1676358949.png)

（2）根据PID找到可执行文件名称

```
tasklist | findstr 16584
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-16763589491.png)

（3）查找16584的命令行

```
wmic process where processid=16584 get commandline /format:csv
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-1676358950.png)

（4）查询该PID的父进程对应的PID号

```
wmic process where processid=16584 get parentprocessid /format:csv
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-16763589501.png)

(5) 查找父PID7524的命令行

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195847-1676358951.png)

-END-

▎经典文章精选

[社会工程学 | Yandex mail捆绑域名方法](http://mp.weixin.qq.com/s?__biz=Mzg4MzA4Nzg4Ng==&mid=2247506197&idx=1&sn=43b9f3e527a694ad867830c1d2e63802&chksm=cf4e5674f839df62c7fc2a67da2637669acef444c264c9e53de0a71162fbd794939a4a62e210&scene=21#wechat_redirect)

[社会工程学 | gophish批量发送邮件配置](http://mp.weixin.qq.com/s?__biz=Mzg4MzA4Nzg4Ng==&mid=2247506195&idx=1&sn=7f1a13775abd4180f6a2087a94a06fe3&chksm=cf4e5672f839df645281953603a0ae7adce3a42f49ae63aa2c879ec710b2721005c4adaa7567&scene=21#wechat_redirect)

**本文作者：[贝塔安全实验室](newpage/author?author_id=9525)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/195847.html**](https://www.secpulse.com/archives/195847.html)

Tags: [Cobaltstrike](https://www.secpulse.com/archives/tag/cobaltstrike)、[Office](https://www.secpulse.com/archives/tag/office)、[宏](https://www.secpulse.com/archives/tag/%E5%AE%8F)、[宏代码](https://www.secpulse.com/archives/tag/%E5%AE%8F%E4%BB%A3%E7%A0%81)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![安全攻防 | CobaltStrike与水坑攻击的联动](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1670310705951-300x236.png)

  安全攻防 | CobaltStrike与…](https://www.secpulse.com/archives/192987.html "详细阅读 安全攻防 | CobaltStrike与水坑攻击的联动")
* [![再次捕获！重保期间拦截针对Coremail的钓鱼攻击](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-184900-1659924834-300x169.png)

  再次捕获！重保期间拦截针对Coremai…](https://www.secpulse.com/archives/184900.html "详细阅读 再次捕获！重保期间拦截针对Coremail的钓鱼攻击")
* [![FakeLogonScreen – 伪造Windows登录屏幕以窃取密码](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/04/16503330691-300x195.png)

  FakeLogonScreen R…](https://www.secpulse.com/archives/177260.html "详细阅读 FakeLogonScreen – 伪造Windows登录屏幕以窃取密码")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-co...