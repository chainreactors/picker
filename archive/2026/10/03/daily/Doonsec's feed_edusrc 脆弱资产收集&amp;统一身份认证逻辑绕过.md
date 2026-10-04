---
title: edusrc 脆弱资产收集&amp;统一身份认证逻辑绕过
url: https://mp.weixin.qq.com/s/LjPd79SIRf-NJcB8LtpR2Q
source: Doonsec's feed
date: 2026-10-03
fetch_date: 2026-10-04T07:36:03.455482
---

# edusrc 脆弱资产收集&amp;统一身份认证逻辑绕过

# edusrc 脆弱资产收集&统一身份认证逻辑绕过

原创

神农Sec
神农Sec

神农Sec

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

课程培训

扫码咨询

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/b7iaH1LtiaKWXLicr9MthUBGib1nvDibDT4r6iaK4cQvn56iako5nUwJ9MGiaXFdhNMurGdFLqbD9Rs3QxGrHTAsWKmc1w/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/b96CibCt70iaaJcib7FH02wTKvoHALAMw4fchVnBLMw4kTQ7B9oUy0RGfiacu34QEZgDpfia0sVmWrHcDZCV1Na5wDQ/640?wx_fmt=png&wxfrom=13&wx_lazy=1&wx_co=1&tp=wxpic)

#

专注于SRC漏洞挖掘、红蓝对抗、渗透测试、代码审计JS逆向，CNVD和EDUSRC漏洞挖掘，以及工具分享、前沿信息分享、POC、EXP分享。不定期分享各种好玩的项目及好用的工具，欢迎关注。加内部圈子，文末有彩蛋（课程培训限时优惠）。

#

01

0x1 edusrc 脆弱资产收集&统一身份认证逻辑绕过

## 0x1 脆弱资产收集

### 一、通过搜索引擎搜索关键字

#### 1、EDU资产

简单给师傅们介绍几个关键字，比如：操作手册/使用手册/操作视频/使用视频/演示视频/白皮书，通过上面的搜索关键字，很容易搜索到EDU学校相关脆弱资产，语法使用如下：

```
site:edu.cn intext:操作手册|使用手册|操作视频|使用视频|演示视频|白皮书
```

就很容易找到很多系统操作使用手册。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVhKgXOVrJ76Tic5uZjCFxtxEOnVBPiceml3OB9WGrOqoH9aib2c5k3Oia2icZrHMyzib7JWwz6adlmAzgUDQSNDMSS7Umiam6vltRv3s/640?wx_fmt=png&from=appmsg)

img

也就是下面的账号密码，有些操作手册都会直接泄露测试账号和密码，且系统没有及时删除对应的测试账号，从而导致一个漏洞危害操作。

![](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QWjXvPtbs04uIibmT7Yfcjrxj6mPRpiaSH7hvibU1lR8BWYuibRGp6ibQThvQYYoTeia27qtt5FJyeaTQWFhkr4qvf88YRv9BWYhetm4/640?wx_fmt=png&from=appmsg)

#### 2、人社关键字

* 人社部门概述 人社部门是指人力资源与社会保障部、人力资源与社会保障厅、人力资源与社会保障局等机构，通常简称为人社部、人社厅、人社局。
* 人社部门管理的学校 人社部门管理的学校通常为技工学校、技师学院。判断某所学校是否属于人社部门管理，可以通过搜索引擎查询“学校名称 隶属于”来获取相关参考信息，如搜索结果中显示某学校隶属于人社部门，即可确认其为收录范围内的学校。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWtfibwDuqRKXGAO9kva6ictcEib9xfARY44QeHibYWO6JQCn6GxiapFxfuGR0muF0HemEXqTo3iaeV46zMWcKpaeHoSF6nG5nKgF18Q/640?wx_fmt=png&from=appmsg)

img

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

接下来就可以进行测试相关人社的漏洞，并提交到对应的漏洞到EDUSRC平台即可。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QXPwGU24s5M5GsY4HLicklUVHAA6Fu06ycUO8hbczhV4gHvib0sIDdkiaYAATusTkKJZsDvjEtnLc3a6XicdzChUqG6K9NsJANY4jo/640?wx_fmt=png&from=appmsg)

#### 3、中国科学院关键字

这个中国科学院单位也是今年新加入的单位，很多小伙伴师傅们还不知道，下面就给师傅们简单介绍下。

![img](https://mmbiz.qpic.cn/mmbiz_png/mcko8AHj6QUkCCTre640puAVM5XWKPt9OUzQGmP3A7hQuUuYPQGY6ehVaZapgClciaf73nSWXic64L31bTicWR1u6mTwdRGsJibprV01WJEZCPQ/640?wx_fmt=png&from=appmsg)

img

主要是以ac.cn和cas.cn两个主域名为主，再配合下面的搜索关键词语法进行检索脆弱资产。

```
//中国科学院
site:ac.cn intext:管理|后台|登陆|用户名|密码|系统|帐号|操作手册|使用手册|操作视频|使用视频|演示视频|白皮书
site:cas.cn intext:管理|后台|登陆|用户名|密码|系统|帐号|操作手册|使用手册|操作视频|使用视频|演示视频|白皮书
```

### 二、语雀公开知识库搜索

关键字还是可以配合下面的来使用，搜索语雀公开的知识库文档。

```
操作手册/使用手册/操作视频/使用视频/演示视频/白皮书
```

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QW2Uu9KOibzdyWfm5GFuPw1TQc6FQnSibEfYetj1Y3LfnTxsfm836icf5JFh40LFBu6OEBXdibjnqDSCXqUszXbU0YIRpE3L093W8Q/640?wx_fmt=png&from=appmsg)

img

这里我给师傅们总结下通过上面搜索到的EDU后台系统登陆默认的一个密码。

```
EDU默认密码：111111、000000、123123、123456、654321、666666、身份证后六位
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QWXfOZuKLDqcI2gaPAV6HUWPteNvibXp7vYOic2zv4Z6ibpiaPENcgmy0Pqwvia9mdWe5qp0RbicVWB5FQcJq0WbDu7FMqNIX5jxCdpY/640?wx_fmt=png&from=appmsg)

### 三、SRC万能Google语法&懒人网站分享

#### 1、Google黑客语法

收到信息收集和资产收集怎么可能少的了Google浏览器呢，很多大牛都是使用一些厉害的Google语法进行一个资产的收集，在以前学校的一些`身份证`和`学号`信息经常能够利用这些语法找到的。

下面我也简单的给师傅们整理了下一些常见的一些`Google检索的语法`，如下：

```
注入漏洞:
site:edu.cn inurl:id|aspx|jsp|php|asp

文件上传：
site:edu.cn inurl:file|load|editor|Files

前台登录：
site:edu.cn intext:管理|后台|登陆|用户名|密码|验证码|系统|帐号|手册|admin|login|sys|managetem|password|username

site:edu.cn inurl:login|admin|manage|manager|admin_login|login_admin|system|boss|master

敏感信息搜索:
site:edu.cn ( "默认密码" OR "学号" OR "工号")
site:edu.cn "账号、密码、学号"&"附件"

后台接口和敏感信息探测:
site:edu.cn (inurl:login OR inurl:admin OR inurl:index OR inurl:登录) OR (inurl:config | inurl:env | inurl:setting | inurl:backup | inurl:admin | inurl:php)

查找暴露的特殊文件:
site:edu.cn filetype:txt OR filetype:xls OR filetype:xlsx OR filetype:doc OR filetype:docx OR filetype:pdf

已公开的 XSS 和重定向漏洞:
site:openbugbounty.org inurl:reports intext:edu.cn

常见的敏感文件扩展:
site:edu.cn ext:log | ext:txt | ext:conf | ext:cnf | ext:ini | ext:env | ext:sh | ext:bak | ext:backup | ext:swp | ext:old | ext:~ | ext:git | ext:svn | ext:htpasswd | ext:htaccess

XSS 漏洞倾向参数:
inurl:q= | inurl:s= | inurl:search= | inurl:query= | inurl:keyword= | inurl:lang= inurl:& site:edu.cn

重定向漏洞倾向参数:
inurl:url= | inurl:return= | inurl:next= | inurl:redirect= | inurl:redir= | inurl:ret= | inurl:r2= | inurl:page= inurl:& inurl:http site:edu.cn

SQL 注入倾向参数:
inurl:id= | inurl:pid= | inurl:category= | inurl:cat= | inurl:action= | inurl:sid= | inurl:dir= inurl:& site:edu.cn

SSRF 漏洞倾向参数:
inurl:http | inurl:url= | inurl:path= | inurl:dest= | inurl:html= | inurl:data= | inurl:domain= | inurl:page= inurl:& site:edu.cn

本地文件包含（LFI）倾向参数:
inurl:include | inurl:dir | inurl:detail= | inurl:file= | inurl:folder= | inurl:inc= | inurl:locate= | inurl:doc= | inurl:conf= inurl:& site:edu.cn

远程命令执行（RCE）倾向参数:
inurl:cmd | inurl:exec= | inurl:query= | inurl:code= | inurl:do= | inurl:run= | inurl:read= | inurl:ping= inurl:& site:edu.cn

敏感参数:
inurl:email= | inurl:phone= | inurl:password= | inurl:secret= inurl:& site:edu.cn

API 文档:
inurl:apidocs | inurl:api-docs | inurl:swagger | inurl:api-explorer site:edu.cn

代码泄露:
site:pastebin.com edu.cn

云存储:
site:s3.amazonaws.com edu.cn

JFrog Artifactory:
site:jfrog.io edu.cn

Firebase:
site:firebaseio.com edu.cn

文件上传端点:
site:edu.cn "choose file"

漏洞赏金和漏洞披露程序:
"submit vulnerability report" | "powered by bugcrowd" | "powered by hackerone" site:*/security.txt "bounty"

暴露的 Apache 服务器状态:
site:*/server-status apache

WordPress:
inurl:/wp-admin/admin-ajax.php
```

其次还有就是我一般喜欢在打开无影探测完的资产后，要是这个域名访问报错，或者没什么信息，我会使用Google语法来访问，有时候可以找到该站点的存活站点，从而打该站点的资产

就比如你访问http://xxxxx.xxx.com这个站点，显示下面的界面报错，一般别人遇到就放弃了

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUpEJvwgTTydKw53iboicaDuVeANUlftozNRIzoI8Gb4RJkgUiamWwXNO1RsMwZuzmyoic5beqxDUSmzA/640?wx_fmt=png&from=appmsg)

img

我们可以使用Google浏览器用site:域名尝试，有时候可以找到对应站点的别的访问路径，就不会报错了

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUpEJvwgTTydKw53iboicaDuVqUFdoXfrDg8KK8KmWlyLWjfTFpB5356nPIic1MEhHAUNgsmwnHetgDw/640?wx_fmt=png&from=appmsg)

img

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVU6GqwQUNQKibUy0IhycOnjNMxLXtE5O3qJjtrPmtfibEyAQRr1m4Mdx8bqSGyibDL5102LaI8CbzlSkDmscgwWoxkkStDCndYL0/640?wx_fmt=png&from=appmsg)

img

最后面给师傅们分享一个搜集EDU资产的FOFA语法，感兴趣的师傅们可以去玩下，搜索出来的资产也蛮多的

```
org="China Education and Research Network Center" &&("后台"||"登录")&&("中学"||"技术学院"||"小学"||"职业学院"||"中专"||"幼儿园"||"人社局"||"科学院")
```

#### 2、**懒人版，在线网站**

懒人版，在线网站如下：

https://app.pentest-tools.com/scans/new-scan

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUpEJvwgTTydKw53iboicaDuVEDXGXzGriaRibiaqcGPzC8g9ia9YKEqdnpfBiaMSmcTSWhj8iaaRNPnJWBSA/640?wx_fmt=png&from=appmsg)

img

这个站点的功能十分强大，但是很多都是需要付费升级的功能里面还有很先进的AI漏洞挖掘分析的功能，但是要付费，里面的免费模块也是蛮不错的，

我下面进行对一个企业src的域名进行子域名挖掘，一分钟的时间就挖掘出来了62个子域名，且使用十分简单

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUpEJvwgTTydKw53iboicaDuVKCWmT6oxZE0dvSGcncNIiaEyrkqxyQZsElIj13GhLaAAvVa0fW1GAKQ/640?wx_fmt=png&from=appmsg)

img

十分可以看到这个侦察工具这里，有一个Google黑客

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUpEJvwgTTydKw53iboicaDuVMfPrlQsPVATXmRicwbdfiauKSf9CHknVLMdbpejrs85bl6icl2dxlMTnw/640?wx_fmt=png&from=appmsg)

img

可以看到里面直接把一些重要的查询功能点都给你列出来了，十分简单，对小白师傅们十分友好

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUpEJvwgTTydKw53iboicaDuVHgDZBYw7qibqRxtKP6ibkb7R43icR5TthosPe2v13sBpBzrvz0UKWrn6w/640?wx_fmt=png&from=appmsg)

img

下面的配置文件信息，直接就可以查询到了，不需要你会Google语法，直接使用这个工具你也可以很强大

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/b7iaH1LtiaKWUpEJvwgTTydKw53iboicaDuVFPYicSOHI2D3DdhEHJ4AProdiaHLPclpbcLQ8adk5S9VZNuUiakmzJwzQ/640?wx_fmt=png&from=appmsg)

img

## 0x2 统一身份认证绕过/账号密码收集

### 一、GitHub搜索

像我们平常做一些测试的时候，在对抗登陆框的时候，需要账号密码，可以试试GitHub的爬虫搜索功能。

![img](https://mmbiz.qpic.cn/sz_mmbiz_png/mcko8AHj6QVialxRfKsVd7vM0MOw4BN9M6Fwhsb8jI5zFY8OpbmPQvZic3oEmsmcuQJEGbQWwUONA8hFNlEArichA0UuXoT9KC7KwvzR8XAyFo/640?wx_fmt=png&from=appmsg)

img

一些复杂的语法，可以点击这个即可。

![img](htt...