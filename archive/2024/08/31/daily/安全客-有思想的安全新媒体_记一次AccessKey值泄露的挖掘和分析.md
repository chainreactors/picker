---
title: 记一次AccessKey值泄露的挖掘和分析
url: https://www.anquanke.com/post/id/298882
source: 安全客-有思想的安全新媒体
date: 2024-08-31
fetch_date: 2025-10-06T17:59:28.445330
---

# 记一次AccessKey值泄露的挖掘和分析

首页

阅读

* [安全资讯](https://www.anquanke.com/news)
* [安全知识](https://www.anquanke.com/knowledge)
* [安全工具](https://www.anquanke.com/tool)

活动

社区

学院

安全导航

内容精选

* [专栏](/column/index.html)
* [精选专题](https://www.anquanke.com/subject-list)
* [安全KER季刊](https://www.anquanke.com/discovery)
* [360网络安全周报](https://www.anquanke.com/week-list)

# 记一次AccessKey值泄露的挖掘和分析

阅读量**261156**

发布时间 : 2024-08-30 14:41:59

**x**

##### 译文声明

本文是翻译文章

译文仅供参考，具体内容表达以及含义原文为准。

**本文作者：track-98k**

## 0x1 前言

下面是分享云安全相关的漏洞，讲解怎么利用`AccessKey`进而接管云环境的，但是我们首先得知道AccessKey的组成，比如说你看到AccessKey里面的字段和关键字，你不知道是什么，也不知道是什么厂商的云服务器，那就无法快速准确的利用这个`AccessKey相关云环境漏洞`了。

![img]()

## 0x2 AccessKey云环境

### 浅谈

下面的论述也是看完**[曾哥](https://wiki.teamssix.com/cloudservice/more/)**的文章，然后加上自己的理解，下面给师傅们分享下`AccessKey`相关的知识点了。对于云场景的渗透，现在已经层出不穷，获得`AK`和`SK`，也是云安全渗透中重要的一环。

通常，我们会在一些敏感的配置文件或者通过未授权访问、任意文件读取漏洞等方式，来寻找AK和SK。

一般常见的通过`正则匹配式`来寻找AK和SK：

```
(?i)((access_key|access_token|admin_pass|admin_user|algolia_admin_key|algolia_api_key|alias_pass|alicloud_access_key|amazon_secret_access_key|amazonaws|ansible_vault_password|aos_key|api_key|api_key_secret|api_key_sid|api_secret|api.googlemaps AIza|apidocs|apikey|apiSecret|app_debug|app_id|app_key|app_log_level|app_secret|appkey|appkeysecret|application_key|appsecret|appspot|auth_token|authorizationToken|authsecret|aws_access|aws_access_key_id|aws_bucket|aws_key|aws_secret|aws_secret_key|aws_token|AWSSecretKey|b2_app_key|bashrc password|bintray_apikey|bintray_gpg_password|bintray_key|bintraykey|bluemix_api_key|bluemix_pass|browserstack_access_key|bucket_password|bucketeer_aws_access_key_id|bucketeer_aws_secret_access_key|built_branch_deploy_key|bx_password|cache_driver|cache_s3_secret_key|cattle_access_key|cattle_secret_key|certificate_password|ci_deploy_password|client_secret|client_zpk_secret_key|clojars_password|cloud_api_key|cloud_watch_aws_access_key|cloudant_password|cloudflare_api_key|cloudflare_auth_key|cloudinary_api_secret|cloudinary_name|codecov_token|config|conn.login|connectionstring|consumer_key|consumer_secret|credentials|cypress_record_key|database_password|database_schema_test|datadog_api_key|datadog_app_key|db_password|db_server|db_username|dbpasswd|dbpassword|dbuser|deploy_password|digitalocean_ssh_key_body|digitalocean_ssh_key_ids|docker_hub_password|docker_key|docker_pass|docker_passwd|docker_password|dockerhub_password|dockerhubpassword|dot-files|dotfiles|droplet_travis_password|dynamoaccesskeyid|dynamosecretaccesskey|elastica_host|elastica_port|elasticsearch_password|encryption_key|encryption_password|env.heroku_api_key|env.sonatype_password|eureka.awssecretkey)[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"]([0-9a-zA-Z\-_=]{8,64})['\"]
```

下面我给师傅们介绍下常见的几个厂商的 `Access Key` 内容特征，然后就能够根据不同厂商 Key 的不同特征，直接能判断出这是哪家厂商的 `Access Key` ，从而针对性进行渗透测试。其中我们云服务器常见的就是阿里云和腾讯云了，我主要给师傅们介绍下面两种Access Key的特点。

### 阿里云

阿里云 (Alibaba Cloud) 的 Access Key 开头标识一般是 “`LTAI`“。

```
^LTAI[A-Za-z0-9]{12,20}$
```

* Access Key ID长度为16-24个字符，由大写字母和数字组成。
* Access Key Secret长度为30个字符，由大写字母、小写字母和数字组成。

### 腾讯云

腾讯云 (Tencent Cloud) 的 Access Key 开头标识一般是 “`AKID`“。

```
^AKID[A-Za-z0-9]{13,20}$
```

* SecretId长度为17个字符，由字母和数字组成。
* SecretKey长度为40个字符，由字母和数字组成。

## 0x3 接管云环境

这里拿到这个网站也是直接利用插件findsomething去看看有什么接口信息泄露包括一些js敏感信息，然后下面看到了OSSaccessKeyId，这个是现在云安全有的一个关键字，相当于唯一的账号

![img]()

然后这里再直接F12检索源代码，右击搜素OSSaccessKeyId关键字，因为OSSaccessKeyId相当于账号，也就是我们需要找到相关云安全的账号以及密码

![img]()

然后再里面继续翻找，然后找到了下面的信息，也就是我们最关注的ossAccessid和ossAccesskey关键字了，有了这两个关键字我们后面就可以使用一些云接管的相关工具进行打一套漏洞了

![img]()

### 接管云工具——行云管家

使用`行云管家`这个工具去接管云环境

```
https://yun.cloudbility.com/
```

第一步：登录行云管家之后选择云主机厂商并导入资源

![img]()

第二步：导入key id跟key secret

![img]()

第三步：AK/SK验证通过后选择绑定的云主机

![img]()

第四步：就是之后完成导入操作

![img]()

但是里面进去后没有找到什么云主机的信息，是因为开始绑定云主机的时候就没有扫描到，但是没有关系，这里主要是给师傅们一个渗透测试的思路，在找到`Access Key`相关知识关键字的一个思路，碰到这样的该怎么去打一个漏洞。

![img]()

### oss-browser

有一些他里面你要是没有找到那个访问的url或者访问不了禁止访问登录连接，那么师傅们可以尝试下下面的这个工具oss-browser，就是专门来连接OSS的。

```
https://github.com/aliyun/oss-browser
```

下面我们就使用这个工具进行连接，然后看看有没有什么敏感信息泄露之类的

![img]()

直接输入泄露的access-key值，直接使用OSS连接工具就可以直接连接成功了
里面有很多的该云主机泄露的信息，后面的内容就不给师傅们分析了，主要是接管云环境的一个思路的分享。

![img]()

## 0x4 总结

这篇文章主要是给师傅们介绍access-key相关的打法，感兴趣的师傅们可以尝试下，然后可以使用下我在文章里面介绍到的两款工具，是目前专门来打access-key泄露以及云主机环境的漏洞工具了。

**文章中涉及的敏感信息均已做打码处理，文章仅做经验分享用途，切勿当真，未授权的攻击属于非法行为！文章中敏感信息均已做多层打码处理。传播、利用本文章所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，作者不为此承担任何责任，一旦造成后果请自行承担！**

本文翻译自 原文链接。如若转载请注明出处。

商务合作，文章发布请联系 anquanke@360.cn

本文由**掌控安全学院**原创发布

转载，请参考[转载声明](https://www.anquanke.com/note/repost)，注明出处： [https://www.anquanke.com/post/id/298882](/post/id/298882)

安全KER - 有思想的安全新媒体

本文转载自:

如若转载,请注明出处：

安全KER - 有思想的安全新媒体

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

* [web安全，渗透测试](/tag/web%E5%AE%89%E5%85%A8%EF%BC%8C%E6%B8%97%E9%80%8F%E6%B5%8B%E8%AF%95)

**+1**0赞

收藏

![](https://p2.ssl.qhimg.com/t014f774daeca5ec49b.png)掌控安全学院

分享到：![微信](https://p0.ssl.qhimg.com/sdm/28_28_100/t01e29062a5dcd13c10.png)

## 发表评论

您还未登录，请先登录。

[登录](/login/index.html)

![](https://p5.ssl.qhimg.com/t014757b72460d855bf.png)

[![](https://p2.ssl.qhimg.com/t014f774daeca5ec49b.png)](/member.html?memberId=141365)

[掌控安全学院](/member.html?memberId=141365)

公众号：掌控安全EDU

* 文章
* **26**

* 粉丝
* **53**

### TA的文章

* ##### [记一次某src挖掘](/post/id/297719)

  2024-09-04 10:17:32
* ##### [记某研究院多处漏洞复盘](/post/id/298638)

  2024-09-03 16:30:42
* ##### [EDU拿敏感信息的骚思路](/post/id/298022)

  2024-09-03 16:06:55
* ##### [记一所中学的的SQL报错注入](/post/id/297649)

  2024-09-03 16:06:03
* ##### [记一次AccessKey值泄露的挖掘和分析](/post/id/298882)

  2024-08-30 14:41:59

### 相关文章

* ##### [为AI Agent行为立“规矩”——字节跳动提出Jeddak AgentArmor智能体安全框架](/post/id/312426)

  2025-09-28 13:43:32
* ##### [教你打造一款AI安全助手 | 安全MCP的实践指南](/post/id/311884)

  2025-09-05 10:40:51
* ##### [当数字世界的“万能钥匙”被滥用，谁来守护核心资产？火山的 MCP 安全授权新范式](/post/id/311597)

  2025-08-28 09:50:41
* ##### [Python代码保护之重置操作码映射的攻与防探究（一）](/post/id/311484)

  2025-08-26 10:49:47
* ##### [广汽集团×火山引擎：出海合规助力企业新增长](/post/id/311498)

  2025-08-26 10:17:09

### 热门推荐

文章目录

* [0x1 前言](#h2-0)
* [0x2 AccessKey云环境](#h2-1)
  + [浅谈](#h3-2)
  + [阿里云](#h3-3)
  + [腾讯云](#h3-4)
* [0x3 接管云环境](#h2-5)
  + [接管云工具——行云管家](#h3-6)
  + [oss-browser](#h3-7)
* [0x4 总结](#h2-8)

![](https://p0.qhimg.com/t11098f6bcd5614af4bf21ef9b5.png)

安全KER

* [关于我们](/about)
* [联系我们](/note/contact)
* [用户协议](/note/protocol)
* [隐私协议](/note/privacy)

商务合作

* [合作内容](/note/business)
* [联系方式](/note/contact)
* [友情链接](/link)

内容需知

* [投稿须知](https://www.anquanke.com/contribute/tips)
* [转载须知](/note/repost)
* 官网QQ群：568681302

合作单位

* [![安全KER](https://p0.ssl.qhimg.com/t01592a959354157bc0.png)](http://www.cert.org.cn/)
* [![安全KER](https://p0.ssl.qhimg.com/t014f76fcea94035e47.png)](http://www.cnnvd.org.cn/)

Copyright © 北京奇虎科技有限公司 三六零数字安全科技集团有限公司 安全KER All Rights Reserved [京ICP备08010314号-66](https://beian.miit.gov.cn/)[![](https://icon.cnzz.com/img/pic.gif)](https://www.cnzz.com/stat/website.php?web_id=1271278035 "站长统计")

微信二维码

**X**![安全KER](https://p0.ssl.qhimg.com/t0151209205b47f2270.jpg)