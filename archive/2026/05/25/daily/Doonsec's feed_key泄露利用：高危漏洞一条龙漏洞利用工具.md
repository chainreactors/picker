---
title: key泄露利用：高危漏洞一条龙漏洞利用工具
url: https://mp.weixin.qq.com/s/mVAPxYLBauokKWrYUe-o5g
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:07:23.842205
---

# key泄露利用：高危漏洞一条龙漏洞利用工具

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mcko8AHj6QUpIlXbicmEQxTVy9icC2SKJvUibMiazHGdZ8jxggjx7Jhujxiaet9Fial1MLx86UdcKR5QrByrJ1Fqx4WhWFf31KKEb8jgAoy6APqWs/0?wx_fmt=jpeg)

# key泄露利用：高危漏洞一条龙漏洞利用工具

原创

神农Sec
神农Sec

神农Sec

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

课程培训

扫码咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。

#

01

0x1 key泄露利用：高危漏洞一条龙漏洞利用工具

## 0x1 前言

哈咯，师傅们！这篇文章主要是给大家介绍相关key泄露，如何进行利用，给师傅们介绍很多好用的工具，进行更加高效地渗透测试，漏洞挖掘操作！

## 0x2 云安全相关key泄露利用

### 一、云业务 AccessKey 标识特征整理

学习参考文章：

https://wiki.teamssix.com/cloudservice/more/

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXIqDkATmSHtNlNXrNvU1ic7FiaicQN3vgnhSHhX9TCra5WL8Ff7Wv9IicvFCSUQg8QhGWibapN3jibcuvA5rEOlhMrYcndAxr1tIckg/640?wx_fmt=png&from=appmsg)

img

下面的论述也是看完**曾哥**的文章，然后加上自己的理解，下面给师傅们分享下`AccessKey`相关的知识点了。对于云场景的渗透，现在已经层出不穷，获得`AK`和`SK`，也是云安全渗透中重要的一环。

通常，我们会在一些敏感的配置文件或者通过未授权访问、任意文件读取漏洞等方式，来寻找AK和SK。

一般常见的通过`正则匹配式`来寻找AK和SK：

```
(?i)((access_key|access_token|admin_pass|admin_user|algolia_admin_key|algolia_api_key|alias_pass|alicloud_access_key|amazon_secret_access_key|amazonaws|ansible_vault_password|aos_key|api_key|api_key_secret|api_key_sid|api_secret|api.googlemaps AIza|apidocs|apikey|apiSecret|app_debug|app_id|app_key|app_log_level|app_secret|appkey|appkeysecret|application_key|appsecret|appspot|auth_token|authorizationToken|authsecret|aws_access|aws_access_key_id|aws_bucket|aws_key|aws_secret|aws_secret_key|aws_token|AWSSecretKey|b2_app_key|bashrc password|bintray_apikey|bintray_gpg_password|bintray_key|bintraykey|bluemix_api_key|bluemix_pass|browserstack_access_key|bucket_password|bucketeer_aws_access_key_id|bucketeer_aws_secret_access_key|built_branch_deploy_key|bx_password|cache_driver|cache_s3_secret_key|cattle_access_key|cattle_secret_key|certificate_password|ci_deploy_password|client_secret|client_zpk_secret_key|clojars_password|cloud_api_key|cloud_watch_aws_access_key|cloudant_password|cloudflare_api_key|cloudflare_auth_key|cloudinary_api_secret|cloudinary_name|codecov_token|config|conn.login|connectionstring|consumer_key|consumer_secret|credentials|cypress_record_key|database_password|database_schema_test|datadog_api_key|datadog_app_key|db_password|db_server|db_username|dbpasswd|dbpassword|dbuser|deploy_password|digitalocean_ssh_key_body|digitalocean_ssh_key_ids|docker_hub_password|docker_key|docker_pass|docker_passwd|docker_password|dockerhub_password|dockerhubpassword|dot-files|dotfiles|droplet_travis_password|dynamoaccesskeyid|dynamosecretaccesskey|elastica_host|elastica_port|elasticsearch_password|encryption_key|encryption_password|env.heroku_api_key|env.sonatype_password|eureka.awssecretkey)[a-z0-9_ .\-,]{0,25})(=|>|:=|\|\|:|<=|=>|:).{0,5}['\"]([0-9a-zA-Z\-_=]{8,64})['\"]
```

QQ\_1779629499931

下面我给师傅们介绍下常见的几个厂商的 `Access Key` 内容特征，然后就能够根据不同厂商 Key 的不同特征，直接能判断出这是哪家厂商的 `Access Key` ，从而针对性进行渗透测试。其中我们云服务器常见的就是阿里云和腾讯云了，我主要给师傅们介绍下面两种Access Key的特点。

**阿里云**

阿里云 (Alibaba Cloud) 的 Access Key 开头标识一般是 "`LTAI`"。

```
^LTAI[A-Za-z0-9]{12,20}$
```

* Access Key ID长度为16-24个字符，由大写字母和数字组成。
* Access Key Secret长度为30个字符，由大写字母、小写字母和数字组成。

**腾讯云**

腾讯云 (Tencent Cloud) 的 Access Key 开头标识一般是 "`AKID`"。

```
^AKID[A-Za-z0-9]{13,20}$
```

* SecretId长度为17个字符，由字母和数字组成。
* SecretKey长度为40个字符，由字母和数字组成。

### 二、云资产管理工具

#### 1、下载

工具GitHub地址：https://github.com/dark-kingA/cloudTools

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUoFnSrqVqoRHm2yicEju25KWoSMekat3deLwfjaZYbcDIFU1A4icSp7NuZwJGLAC1f6TrAKEwQtFyNIbkAcRiaEme0nTxCyRM49k/640?wx_fmt=png&from=appmsg)

img

但是目前官方已经下架了，工具获取，添加我微信：`routing_love`获取即可

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QXLGiblNfpjDRMjUKHcCy6bMuF5Kf7pzhwg68zOVThOnGXtU56eLkYS76KwaCiaIHkm4W4wdRf7TgPgNicibx91u2IoQ74ktyJGcp0/640?wx_fmt=png&from=appmsg)

img

#### 2、工具功能

阿里云：接管控制台、取消接管、Oss增删改查、远程命令执行回显、历史命令记录查看、子用户列表、云数据库管理、告警管理 腾讯云：接管控制台、取消接管、Oss增删改查、远程命令执行回显、子用户列表 华为云：接管控制台、取消接管、子用户列表 ucloud：接管控制台、主机查询、子用户列表查看、主用户查看、订单查看 AWS: 接管控制台、创建后门、子用户列表、策略列表 后门信息

云存储工具-资产列表

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QW7zK7ADtRge0uaicQicfj4bXtuh4WhJmBC2ImpoIiatkVbwkicGCancp1QZ4Hh1MJ6xfqq4jE3kYex68dE8myVibRRiaRL3GsrwnvTw/640?wx_fmt=png&from=appmsg)

img

云存储工具-存储桶信息

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWJLfFjzYPbAbQN5KDa52qWxQiaDe7aMRuVg14iaq8cicnTuG6oV55KbQXf2JfrBjZQWAkibBPS0YxibLfDEX4Hpg2zAhxfuiaUgMvLY/640?wx_fmt=png&from=appmsg)

img

云存储工具-其他服务

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWiaQ8rdVjHUbfcnPKPib4UPUMKsyWeDTN8svFRtdCLFHz0dVg2krOvY0YlSVvmQOEI96LbCh9lUyUPSw9G9A3jhJUxrE7gw4as0/640?wx_fmt=png&from=appmsg)

云服务工具-资产列表

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUSMLJlQDC7VmnFD6c5cCIknflk6Qa7SswvsaicMrxhKRQ5c7EBSSEEepsVb1a3UrV8BVyUALAIfRCk046fhv7lCSKcBibSrK8o0/640?wx_fmt=png&from=appmsg)

云服务工具-华为云接管控制台

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVXH2HR31d9JKiaXzKuJZDfrC5WbSGw5LsNenJu6GNnvk8gyQRBxoJtcww3YVCa5rxN40TkHAseCC2zHdMia6VP8oVb6JtHW9jUs/640?wx_fmt=png&from=appmsg)

云服务工具-ucloud相关

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVG4Pbe4bCnp7LeQpqeDUocRKuTwiaRASrVUK9FjOibAfxzcBmAVwxyYEwj6lrvutUkE3nZxBgW6ricrYYdn7XaIaSr95sz3yQeCs/640?wx_fmt=png&from=appmsg)

其他工具：钉钉key泄露利用

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXLz74rpanjtva3R2EtkZSzoiaeSWibia1wichYBoBnfscW2iagyjfSPJ2FfIauGjnoH5J0WKoYBHZh8k5j7QCa2z2Hf4iaPtWS8Ijc4/640?wx_fmt=png&from=appmsg)

## 0x3 API-T00L-互联网厂商API利用工具

### 一、**工具使用介绍：**

期望是针对互联网各大API泄露的利用工具，包含钉钉、企业微信、飞书等。目前只做出了钉钉和企业微信，别问，就是懒。特别鸣谢chatgpt，代码好帮手。 目前界面长这样，布局拉胯，能用就行。

GitHub项目地址：https://github.com/pykiller/API-T00L

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QW6LNmc1KuuBlJZleKJ96GzEoDicAaMVVjiboUfVWHplJ0JCRBGibNiaWnJ3okaZYV8EFjQWbWy79j17RyiakBGAGFyy0O1uOk6Jj4o/640?wx_fmt=png&from=appmsg)

img

包含钉钉、企业微信、飞书等。目前只做出了钉钉和企业微信

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QVbZfBVSBZV9iccEcE3Jr8FKABeksPGaV3IRO7ficYkp9yxmPKyBkiaq4gf9A0gPpSKia10yibZPsd3jEcZSVcq6zgnHtfsZpn6cygY/640?wx_fmt=png&from=appmsg)

img

### 二、**钉钉**

1、肯定你得有ak、as。填进去获取token

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWic77lHHUkY0xJ3aukJxVzSbVrhibE08xdPSToal7wc4vuKaibKfibDh315libR9BLhrhvFOWEBkFfEqPicPPmpbCfwiaDyuz9u8Sj9I/640?wx_fmt=png&from=appmsg)

img

2、建用户

最简单的做法，直接填入有效手机号，加入组织中可以直接用手机号登录该企业。 userid不要重了，写大点。 删除按钮是根据userid来删除的

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUsbDNh7F38eDMkLsZLvjRgYsSKEEOHe1qUszaxetQ44AlsNicjsXYLRJb8jcb7GmALeYsU5mvuvcOMcntQ0sKxapms5GuRm2YU/640?wx_fmt=png&from=appmsg)

img

3、发公告钓鱼

获取管理员信息，得到管理员userid。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVdHKF58mHLyl3NUxa5ruOkib0z1HZPu3rEAn3ZD0Nibwaa4lXB5o3Zsr6uhoEHs61mcAgF7YOSCHcEkeM81jlHWNnPojRRzCZaU/640?wx_fmt=png&from=appmsg)

img

查userid可以得到部门id dept\_id，这里只做了对部门发公告，实际操作中针对个人发公告效果不如直接加用户钓鱼好使。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXOJqMYcd2ezZ1yXicFe0rL7yhuK85B2vxUdeGUVQ941bhAVG7V2vpsu9CAx1Tb4KRUtjVLaORneWUOLprxKlBxWQw02rk96GD4/640?wx_fmt=png&from=appmsg)

img

### 三、企业微信

企业微信相对于钉钉，限制较多，22年后获取的应用Corpsecret需要设置白名单，且无法绕过。并且对于通讯录的Corpsecret需要单独获取。

1、用Corpid和Corpsecret获取token

2、新建用户，填入有效手机号，加入组织中可以直接用手机号登录该企业。

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWZSNibNy1CmZXHy8TzT0BR2uvvlfT1Wt0H1pHaHvy3QYf49I7jVmxBGEcBmjDhM2VODb3ibgRHaicwOibgvF0Wb68Rdia3b3ODoVEs/640?wx_fmt=png&from=appmsg)

img

3、还可以通过获取邀请二维码加入到企业。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWtnleEGEfbCGU6vZRWEFugjOXRZTKnG44wMASb7CYtvEGia0T6nfmo7xdhnf7cuLXlKcyhn34QtxaBPpiaMbac3OasicOMaiaUXyg/640?wx_fmt=png&from=appmsg)

img

### 四、飞书

1、获取tenant\_access\_token

2、新建用户，填入有效手机号，加入组织中可以直接用手机号登录该企业。

需要注意，open\_department\_id为查询到的部门id，用户默认是放根部门，比较明显。可以放小部门里。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QUxpp1cJm8iafmNt...