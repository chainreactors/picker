---
title: 企业内部钓鱼邮件演练指南
url: https://www.freebuf.com/articles/es/336273.html
source: FreeBuf网络安全行业门户
date: 2022-10-14
fetch_date: 2025-10-03T19:50:28.936226
---

# 企业内部钓鱼邮件演练指南

[![freeBuf](/images/logoMax.png)](/)

主站

分类

云安全

AI安全

开发安全

终端安全

数据安全

Web安全

基础安全

企业安全

关基安全

移动安全

系统安全

其他安全

特色

热点

工具

漏洞

人物志

活动

安全招聘

攻防演练

政策法规

[报告](https://www.freebuf.com/report)[专辑](/column)

* ···
* [公开课](https://live.freebuf.com)
* ···
* [商城](https://shop.freebuf.com)
* ···
* 用户服务
* ···

行业服务

政 府

CNCERT
CNNVD

会员体系（甲方）
会员体系（厂商）
产品名录
企业空间

[知识大陆](https://wiki.freebuf.com/page)

搜索

![](/freebuf/img/7aa3bf7.svg) ![](/freebuf/img/181d733.svg)

创作中心

[登录](https://www.freebuf.com/oauth)[注册](https://www.freebuf.com/oauth)

官方公众号企业安全新浪微博

![](/images/gzh_code.jpg)

FreeBuf.COM网络安全行业门户，每日发布专业的安全资讯、技术剖析。

![FreeBuf+小程序](/images/xcx-code.jpg)

FreeBuf+小程序把安全装进口袋

[![](https://image.3001.net/images/20231020/1697804527_653270ef7570cc7356ba8.png)](https://wiki.freebuf.com)

企业内部钓鱼邮件演练指南

* ![]()
* 关注

* [企业安全](https://www.freebuf.com/articles/es)

企业内部钓鱼邮件演练指南

2022-10-13 10:41:46

所属地 福建省

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
本文由
创作，已纳入「FreeBuf原创奖励计划」，未授权禁止转载

# 前言

在企业⽹络安全建设的道路上，随着防⽕墙、WAF、抗DDoS等安全设施的部署， 企业⽹络边界逐渐稳固直至难以攻破；企业在部署零信任等安全接⼊设施后，模糊化的企业边界也让外部攻击者难以发现攻击⼊⼝。虽然企业安全建设逐渐完善，但仍存在薄弱点，“人为因素”便是其中之一，**企业员⼯安全意识成为影响企业安全的最⼤隐患**，未授权访问、弱密码等问题则成为了企业中常⻅的安全漏洞。

**钓⻥邮件**就是针对“人为因素”进行的攻击⼿段之一，**通过内部钓⻥邮件演练则是提⾼员⼯安全意识的有效途径**，可以通过实战演练让员⼯亲身体验安全攻击，以达到提前遏制潜在安全⻛险的目的。
近期天翼云安全实验室就实践了内部钓鱼邮件演练，并从演练中总结了一些技术经验。

# 一、明确钓鱼邮件发送类型

常见的邮箱类型有以下几种，首先进行分析，明确最适合发送钓鱼邮件的邮箱类型：

**公共邮箱**：通过如163邮箱、qq邮箱等类型的公共邮箱发送钓⻥邮件。被钓⻥者看到企业邮箱收到来⾃外部公共邮箱的邮件，极易产⽣不信任感，这样的钓⻥邮件是**很容易识破的**。
![容易识别的钓鱼邮件](https://image.3001.net/images/20220615/1655263510_62a95116d3cc6841e69db.png!small)

**企业内部邮箱**：通过使用企业内部邮箱发送钓鱼邮件可以直接让被钓鱼者产生信任，但是实际情况下**钓鱼邮件攻击来自企业外部**，而外部攻击者通常难以获取企业内部邮箱用于钓鱼，所以这种方法**实战意义较低**。

**与企业内部邮箱相似的外部邮箱**：例如针对apple公司的钓⻥邮件攻击，使⽤@app1e.com**或者**@apple.net**的邮箱，这些邮箱类型**极易迷惑安全防范意识不高的内部员⼯。所以本⽂将采⽤该⽅法进⾏钓⻥邮件演练。

# 二、进行域名注册

要使用特定@**后缀的邮箱，就需要注册对应的域名，例如要使用**@app1e.com**这个邮箱，就需要先注册**app1e.com**这个域名。注册域名是个很容易的事情，基本上**只要钱到位就可以。其实除了com、cn等热门域名后缀之外，如.xyz、**.me**之类的域名都挺便宜，但作为钓鱼邮件效果稍有所折扣。
![注册域名](https://image.3001.net/images/20220615/1655263520_62a951202a0c3ec866e97.png!small)

# 三、配置邮箱服务器

拥有了自己域名就可以基于这个域名去搭建邮箱服务了，从而拥有属于自己的@邮箱。
⼀种⽅法是**⾃⼰搭建邮箱服务器**，优势是没有发件限制，⽽缺点是费时费⼒。
第二种方法是**使⽤企业邮箱服务映射到⾃⼰的域名上**，例如注册[网易企业邮箱](https://ym.163.com/)或者注册[企业微信](https://work.weixin.qq.com/)会附送企业邮箱服务，优势是使用便捷，缺点是是存在⼀些限制。⽐如⽹易的企业邮箱会**限制邮箱每⽇发件数**，企业微信邮箱会**在发件环节进行垃圾邮件监测**。除了⽹易和腾讯之外，还有[zoho](zoho.com.cn)等企业邮箱可以作为选择， 简单且免费。
![zoho企业邮箱](https://image.3001.net/images/20220615/1655263582_62a9515e69df65372918e.png!small)
综上所述，本次演练不考虑⾃⼰搭建邮箱服务器，使用免费企业邮箱即可满⾜需求。**何况连发件垃圾邮件监测都不能绕过，还怎么指望能钓到⻥**？
在上述网站完成注册之后，最重要的一个步骤就是**通过DNS解析把自己域名的MX记录解析到其对应的邮箱服务器上**，这样才能通过自己的域名使用企业邮箱服务。例如使用163企业邮箱的话，需要配置如下的DNS记录：

mx.ym.163.com 优先级5
![配置DNS记录](https://image.3001.net/images/20220615/1655263597_62a9516d1a687fe7b61fd.png!small)
使用企业微信邮箱的话，需要配置的有2条：

mxbiz2.qq.com 优先级10

mxbiz1.qq.com 优先级5
最后就是在邮箱管理平台上添加企业邮箱帐号，完成一系列操作之后，就得到了钓鱼专属的邮箱，例如**admin@app1e.com**。

# 四、明确钓⻥⽹站平台类型

钓鱼网站一般使用一个伪造的登录页，用于骗取企业员工的帐号密码，例如伪造的公司OA登录页、Gitlab登录页等。但通常情况下外部攻击者并不知道内部OA长什么样，所以使用伪造Gitlab这种公开平台的登录页会比较具有实战价值。不过Gitlab只能针对开发人员进行钓鱼，所以本文使用[Confluence](https://baike.baidu.com/item/confluence/452961?fr=aladdin)这个应用广泛的文档平台进行钓鱼网站的搭建。

# 五、钓鱼⽹站搭建

因为钓鱼网站只需要一个登录页，所以没必要真的搭建一个Confluence，可以通过[zoomeye](https://www.zoomeye.org/)等控件测绘工具，寻找一个互联网上开放的Confluence站点并获取登录页。
![zoomeye搜索](https://image.3001.net/images/20220615/1655263699_62a951d33dc3a13a29cad.png!small)
以Chrome为例，只要`Command + S`就能把网页静态数据存储到本地。
![保存网站](https://image.3001.net/images/20220615/1655263711_62a951df4a5946909cfae.png!small)
不过直接打开Chrome存储下来的index文件，会发现一些元素缺失，例如左上角的LOGO没有了。可以通过浏览器调试网络请求发现缺失的元素（一般是绝对路径访问，所以发生了CORS），需要一些手工操作去下载这些确实的元素，来完善整个登录页面的展示。
![完善网页](https://image.3001.net/images/20220615/1655263723_62a951eb1f51d1dba1b3a.png!small)
在正经的钓⻥攻击中，⽤户点击**登录**按键之后，⼀般会跳转到真正的confluence⻚⾯，这样被钓鱼者会以为⾃⼰只是输错了密码，⽽不会意识到被钓⻥。但在钓⻥演练中就不⽤这么麻烦了，⼤可以直接提醒被钓鱼的内部员⼯，以提⾼他们的安全防范意识。
接下来需要在代码上进行一些修改，以符合钓鱼演练的需求：

1. 把表单提交的HTTP方法由`POST`改为`GET`，这是为了方便后续的日志分析；
2. 把表单提交的地址改为`phish.html`，这是一个提醒员工被钓鱼的页面；
3. 创建`phish.html`，并写入警示语句。

```
<form name="loginform" method="GET" action="phish.html" class="aui login-form-container">
```

就绪之后，通过伪造的confluence登录页进行登录操作后，用户会进入`phish.html`页面。由于使用了GET提交表单，因此用户输入的用户名和密码都明文传输在URL中，这样后续分析日志会比较方便。
![登录跳转](https://image.3001.net/images/20220615/1655263736_62a951f8c7fd04d286e9c.png!small)

# 六、钓鱼⽹站发布

钓⻥⽹站设计完成后即可部署在公⽹上，这样才能让其他⼈访问到。可以⾃⼰购买⼀个具备公⽹IP的服务器进⾏搭建，也可以搜索⽹站搭建服务来使⽤（有⼀些网站搭建服务是免费的）。
在第二步注册完成钓⻥邮箱域名可以⽤作钓⻥⽹站的域名，⽐如**confluence.app1e.com**，使⽤域名的DNS解析A记录到搭建钓⻥⽹站的服务器IP上即可。

# 七、gophish简介

[gophish](https://github.com/gophish/gophish)是一个开源用于钓鱼邮件的管理平台，方便对钓鱼邮件的模板、发件邮箱、钓鱼进程等进行管理。

# 八、发件配置

配置上述注册的企业邮箱**admin@app1e.com**作为钓鱼邮件的发件邮箱，以使用163企业邮箱为例，需要配置**Host**为163企业邮箱的SMTP服务地址与端口`smtp.ym.163.com:25`。
企业微信邮箱使用的SMTP服务端口为`smtp.exmail.qq.com:25`。
![发件配置](https://image.3001.net/images/20220615/1655263781_62a95225719b49270ec3c.png!small)

# 九、钓⻥邮件模板编写

接下来编写钓鱼邮件内容，gophish提供了**HTML**格式编写邮件，这样可以编写炫酷的钓鱼邮件，比那些纯文本的邮件要正式得多。
这里需要注意，钓⻥邮件内容中一定要放置钓鱼网站的链接。得力于**HTML**的加持，使用`<a>`标签创建的链接，让用户以为点击了**apple.com**，实际上却点击了**app1e.com**。
而URL中的参数`{{.Rid}}`则在gophish真正发送邮件时，替换为用户的唯一标识，用于后续定位**是哪个内部员工点击了钓鱼链接**。
![钓鱼邮件模板](https://image.3001.net/images/20220615/1655263793_62a95231c88023fc06123.png!small)

# 十、⽬标配置

通过**User & Groups**模块可以使用csv文件导入内部员工的邮箱。

# 十一、发起钓⻥

万事俱备，通过**Campaigns**模块来最终发送钓鱼邮件。选择**发件邮箱配置**、选择**钓鱼邮件模板**、选择**目标邮箱组**，点击**Launch Campaign**就完成了钓鱼邮件的发送。在**Campaigns**模块下可以查看钓鱼邮件发送的详情。
![钓鱼详情](https://image.3001.net/images/20220615/1655263808_62a9524056b90785255cd.png!small)

# 十二、收获

本次演练采用**查询日志**的方式来监控钓鱼的结果，以得知哪位内部员工点击了钓鱼邮件、甚至输入了用户名密码。由于把表单的提交方式改为了GET，所以通过访问日志（access.log）就可以。
例如使用Nginx服务器搭载的钓鱼网站，则可以在`/var/log/nginx`目录下，执行命令`sudo cat access.log | grep trid=`过滤得到钓鱼邮件的点击结果；执行命令`sudo cat access.log | grep phish.html`可以过滤得到在钓鱼网站输入了用户名密码的信息。
（此处本想贴图，但是需要打码太多，就省略了）
参数`trid`的值为每个用户的标识，通过该值就可以在gophish中查询得知点击了钓鱼邮件的员工邮箱，从而对其开展精准的安全意识培训。例如通过上述命令过滤得到字段`trid=5V6PL8R`，可以在Campaigns模块中进行对应查找：
![](https://image.3001.net/images/20220615/1655263819_62a9524bbfe05bb54bfea.png!small)

# 声明

本⽂内容仅限企业进⾏内部钓⻥邮件演练学习参考，请勿⽤于钓⻥攻击，否则后果⾃负。请大家遵纪守法，共同维护网络安全绿色环境。

# 钓鱼技术 # 钓鱼邮件 # 钓鱼网站 # 钓鱼邮件攻击 # gophish

![]()

![](https://image.3001.net/images/20240308/1709876354_65eaa4828e91d155430d9.png)
已在FreeBuf发表 0 篇文章

本文为 独立观点，未经授权禁止转载。
如需授权、对文章有疑问或需删除稿件，请联系 FreeBuf
客服小蜜蜂（微信：freebee1024）

被以下专辑收录，发现更多精彩内容

+ 收入我的专辑

+ 加入我的收藏

展开更多

相关推荐

![]()

关 注

* 0 文章数
* 0 关注者

![](/images/logo_b.png)

本站由阿里云 提供计算与安全服务

### 用户服务

* [有奖投稿](https://www.freebuf.com/write)
* [提交漏洞](https://www.vulbox.com/bounties/detail-72)
* [参与众测](https://www.vulbox.com/projects/list)
* [商城](https://shop.freebuf.com)

### 企业服务

* [安全咨询](https://company.freebuf.com)
* [产业全景图](https://www.freebuf.com/news/307349.html)
* [企业SRC](https://www.vulbox.com/service/src)
* [安全众测](https://www.vulbox.com/)

### 合作信息

* [斗象官网](https://www.tophant.com/)
* [广告投放](https://www.freebuf.com/articles/444331.html)
* [联系我们](https://www.freebuf.com/articles/444332.html)

### 关于我们

* [关于我们](https://www.freebuf.com/news/others/864.html)
* 微信公众号
* [新浪微博](http://weibo.com/freebuf)

### 战略伙伴

* [![](https://image.3001.net/images/20191017/1571306518_5da83c1686dd9.png)](http://www.aliyun.com/?freebuf)

### FreeBuf知识大陆

![](https://image.3001.net/images/20250703/1751535036_68664dbcae34ac40bb9e7.png)

扫码把安全装进口袋

* [斗象科技](https://www.tophant.com/)
* [FreeBuf](https://www.freebuf.com)
* [漏洞盒子](https://www.vulbox.com/)
* [斗象智能安全](https://ai.tophant.com/)
* [免责条款](https://www.freebuf.com/dis)
* [协议条款](https://my.freebuf.com/AgreeProtocol/duty)

Copyright © 2025 WWW.FREEBUF.COM All Rights Reserved
[沪ICP备2024099014号](https://beian.miit.gov.cn/#/Integrated/index) | [沪公安网备
![](https://image.3001.net/images/20200106/1578291342_5e12d08ec2379.png)](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=31011502009321)