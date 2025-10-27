---
title: 记一次某CMS代码审计
url: https://www.secpulse.com/archives/190693.html
source: 安全脉搏
date: 2022-11-09
fetch_date: 2025-10-03T22:04:08.095576
---

# 记一次某CMS代码审计

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

# 记一次某CMS代码审计

[代码审计](https://www.secpulse.com/archives/category/articles/code-audit)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-11-08

35,871

**作者：ddwGeGe**

**本文转自先知社区：https://xz.aliyun.com/t/11774**

**前言**

无意中浏览到某小众OA官网且可以下载到源码，随机审计一波，最后成功Getshell，大佬勿喷

**目录结构**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888773.png)

**环境搭建**

WIN11 + PhpStudy(Mysql) + Redis + IDEA(Tomcat 8.0)

将sql文件导入到phpstudy(Mysql)中，同时启动Redis服务，配置好数据库环境

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888777.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888791.png)

采用白+黑进行审计，从功能点出发，在个人资料处图像可以进行上传

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888793.png)

开始抓包进行文件上传，后缀和文件内容均没有做校验，且返回上传的路径和文件名，本以为可以直接getshell，但却无法解析，且该文件并没有落地

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888796.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888803.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888812.png)

**代码审计**

根据数据包的路径(/func/upload/uploadImages)直接搜索路由，成功找到上传函数

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888815.png)

首先会对db的值进行判断，根据db的值来决定上传文件的保存方式

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888822.png)

初始上传的时候，db=1，而if的GlobalConstant.FILE\_UPLOADER\_SAVE\_FILE=0，故直接进入到else if

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888824.png)

新的文件名 = 上传时间 + 10位随机数 + 原始上传文件的后缀名

```
String extend = FileUtils.getExtend(fileName);// 获取文件扩展名
String noextfilename = DateUtils.getDataString(DateUtils.SDF_YYYYMMDDHHMMSS) + StringUtil.random(10);//自定义文件名称
String myfilename= noextfilename+"."+extend;//自定义文件名称
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888828.png)

文件存储在数据库中，并将文件名通过map保存，最后返回在数据包中

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888833.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888837.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888840.png)

db可控，在上传的时候，将db=1改为db=0，进入到if

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888841.png)

会创建新的上传目录，新的目录 = Web根目录 + upload + 上传时间（年月日），若不存在则进行新建

```
String realPath = request.getSession().getServletContext().getRealPath("/") + "/upload/" + strYYYYMMDD + "/";// 文件的硬盘真实路径
String path = "upload/" + strYYYYMMDD + "/";
File file = new File(realPath);
    if (!file.exists()) {
    file.mkdirs();// 创建根目录
}
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888845.png)

新的文件名的命名方式跟else if基本一致，在获取文件的后缀名的时候，并未进行检查和过滤，直接进行拼接，从而造成了文件上传漏洞

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888850.png)

最后将上传文件内容直接复制到新创建的文件

```
FileCopyUtils.copy(mf.getBytes(), savefile);
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888854.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888856.png)

最后通过map进行存储，且将文件上传路径和文件名分别存储在 filePath、saveName

```
Map<String, Object> map = new HashMap<String, Object>();
map.put("filePath", GlobalConstant.CONFIG_FILE_SAVE_DB_URL + myfilename);
map.put("saveName", noextfilename);
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888858.png)

上传回显的Jsp Webshell，将db在上传的时候改为db=0，成功上传，可执行命令

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888864.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-190693-1667888867.gif)

靶场实操，戳“阅读原文“

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/190693.html**](https://www.secpulse.com/archives/190693.html)

Tags: [cms](https://www.secpulse.com/archives/tag/cms)、[idea](https://www.secpulse.com/archives/tag/idea)、[Mysql](https://www.secpulse.com/archives/tag/Mysql)、[phpstudy](https://www.secpulse.com/archives/tag/phpstudy)、[redis](https://www.secpulse.com/archives/tag/redis)、[代码审计](https://www.secpulse.com/archives/tag/code-audit)

点赞：
4
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![神器！MySQL蜜罐服务GUI利用工具](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1686624388925-300x164.png)

  神器！MySQL蜜罐服务GUI利用工具](https://www.secpulse.com/archives/201773.html "详细阅读 神器！MySQL蜜罐服务GUI利用工具")
* [![某oa 11.10 未授权任意文件上传](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201450-1686040662-300x248.png)

  某oa 11.10 未授权任意文件上传](https://www.secpulse.com/archives/201450.html "详细阅读 某oa 11.10 未授权任意文件上传")
* [![MySQL数据库安全测试](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1684133717094-300x188.png)

  MySQL数据库安全测试](https://www.secpulse.com/archives/200243.html "详细阅读 MySQL数据库安全测试")

评论  (0)

昵称

必填
您当前尚未登录。
[登录？](https://www.secpulse.com/user_login "登录")
[注册](https://www.secpulse.com/user-r...