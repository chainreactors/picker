---
title: 一文带你看懂从脆弱资产收集到SRC通杀案例技术分享
url: https://forum.butian.net/share/4629
source: 奇安信攻防社区
date: 2025-11-12
fetch_date: 2025-11-13T03:14:23.305073
---

# 一文带你看懂从脆弱资产收集到SRC通杀案例技术分享

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 一文带你看懂从脆弱资产收集到SRC通杀案例技术分享

* [渗透测试](https://forum.butian.net/topic/47)

这篇文章以开头从脆弱资产的视角带师傅们了解信息收集的思路和方法.同时这篇文章介绍了人社和中国科学院相关漏洞的收集方法和EDU平台的收录规则，以及语雀的公开知识库。后面以企业SRC的SQL排序注入和云安全Minio渗透测试给师傅们很详细的以真实案例来进行分享。

0x1 前言
------
这篇文章以开头从脆弱资产的视角带师傅们了解信息收集的思路和方法，通过多种方法很详细的给师傅们介绍了，主要是以EDUSRC的资产收集姿势来分享。同时这篇文章介绍了人社和中国科学院相关漏洞的收集方法和EDU平台的收录规则，以及语雀的公开知识库去收集一些操作手册，泄露的一些账户密码等。
后面以企业SRC的SQL排序注入和云安全Minio渗透测试给师傅们很详细的以真实案例来进行分享，针对云安全Minio的漏洞测试的文章不多，这篇文章的案例都很全。最后面拿了前段时间挖的EDUSRC的通杀漏洞进行介绍。
0x2 脆弱资产收集
----------
### 一、通过搜索引擎搜索关键字
#### 1、EDU资产
简单给师傅们介绍几个关键字，比如：操作手册/使用手册/操作视频/使用视频/演示视频/白皮书，通过上面的搜索关键字，很容易搜索到EDU学校相关脆弱资产，语法使用如下：
```php
site:edu.cn intext:操作手册|使用手册|操作视频|使用视频|演示视频|白皮书
```
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762223023199-ffb177aa-e7ad-48c8-8e3e-623af6889f85.png "null")
就很容易找到很多系统操作使用手册。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762223023292-f73ccf49-1459-4968-9a7a-ce347bea532c.png "null")
也就是下面的账号密码，有些操作手册都会直接泄露测试账号和密码，且系统没有及时删除对应的测试账号，从而导致一个漏洞危害操作。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762223023391-a73d09cf-baeb-4d63-86a9-a97aa6ba4d6b.png "null")
#### 2、人社关键字
- 人社部门概述
人社部门是指人力资源与社会保障部、人力资源与社会保障厅、人力资源与社会保障局等机构，通常简称为人社部、人社厅、人社局。
- 人社部门管理的学校
人社部门管理的学校通常为技工学校、技师学院。判断某所学校是否属于人社部门管理，可以通过搜索引擎查询“学校名称 隶属于”来获取相关参考信息，如搜索结果中显示某学校隶属于人社部门，即可确认其为收录范围内的学校。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762223023512-8f8cbd60-7541-4412-a7a2-c49f3514582e.png "null")
这里再给师傅们分享一些人社相关搜索关键字，主要用于测试微信小程序的漏洞：
```php
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
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762223023594-d506a9d5-a526-4d21-b8d6-c91e73c1de04.png "null")
#### 3、中国科学院关键字
这个中国科学院单位也是今年新加入的单位，很多小伙伴师傅们还不知道，下面就给师傅们简单介绍下。
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762223023701-316c77d6-e8c8-4b21-8df2-e8b30c096ea6.png "null")
主要是以ac.cn和cas.cn两个主域名为主，再配合下面的搜索关键词语法进行检索脆弱资产。
```php
//中国科学院
site:ac.cn intext:管理|后台|登陆|用户名|密码|系统|帐号|操作手册|使用手册|操作视频|使用视频|演示视频|白皮书
site:cas.cn intext:管理|后台|登陆|用户名|密码|系统|帐号|操作手册|使用手册|操作视频|使用视频|演示视频|白皮书
```
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762223023841-f55b278a-ad28-4977-b27e-d90db7dc1de5.png "null")
### 二、语雀公开知识库搜索
关键字还是可以配合下面的来使用，搜索语雀公开的知识库文档。
```php
操作手册/使用手册/操作视频/使用视频/演示视频/白皮书
```
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762223024128-f1c2d3ab-ee74-44e7-ab5e-b52b40288db1.png "null")
这里我给师傅们总结下通过上面搜索到的EDU后台系统登陆默认的一个密码。
```php
EDU默认密码：111111、000000、123123、123456、654321、666666、身份证后六位
```
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762223024314-4d21de80-6b42-481a-af1b-fe748c63005d.png "null")
### 三、SRC万能Google语法&amp;懒人网站分享
#### 1、Google黑客语法
收到信息收集和资产收集怎么可能少的了Google浏览器呢，很多大牛都是使用一些厉害的Google语法进行一个资产的收集，在以前学校的一些`身份证`和`学号`信息经常能够利用这些语法找到的。
下面我也简单的给师傅们整理了下一些常见的一些`Google检索的语法`，如下：
```php
注入漏洞:
site:edu.cn inurl:id|aspx|jsp|php|asp
文件上传：
site:edu.cn inurl:file|load|editor|Files
前台登录：
site:edu.cn intext:管理|后台|登陆|用户名|密码|验证码|系统|帐号|手册|admin|login|sys|managetem|password|username
site:edu.cn inurl:login|admin|manage|manager|admin\_login|login\_admin|system|boss|master
敏感信息搜索:
site:edu.cn ( "默认密码" OR "学号" OR "工号")
site:edu.cn "账号、密码、学号"&"附件"
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
site:edu.cn "choose file"
漏洞赏金和漏洞披露程序:
"submit vulnerability report" | "powered by bugcrowd" | "powered by hackerone" site:\*/security.txt "bounty"
暴露的 Apache 服务器状态:
site:\*/server-status apache
WordPress:
inurl:/wp-admin/admin-ajax.php
```
其次还有就是我一般喜欢在打开无影探测完的资产后，要是这个域名访问报错，或者没什么信息，我会使用Google语法来访问，有时候可以找到该站点的存活站点，从而打该站点的资产
就比如你访问http://xxxxx.xxx.com这个站点，显示下面的界面报错，一般别人遇到就放弃了
![](https://mmbiz.qpic.cn/sz\_mmbiz\_png/b7iaH1LtiaKWUpEJvwgTTydKw53iboicaDuVeANUlftozNRIzoI8Gb4RJkgUiamWwXNO1RsMwZuzmyoic5beqxDUSmzA/640?wx\_fmt=png&from=appmsg "null")
我们可以使用Google浏览器用site:域名尝试，有时候可以找到对应站点的别的访问路径，就不会报错了
![](https://mmbiz.qpic.cn/sz\_mmbiz\_png/b7iaH1LtiaKWUpEJvwgTTydKw53iboicaDuVqUFdoXfrDg8KK8KmWlyLWjfTFpB5356nPIic1MEhHAUNgsmwnHetgDw/640?wx\_fmt=png&from=appmsg "null")
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762223024427-6d1c977e-81ad-4e45-b5b7-25033befd45c.png "null")
最后面给师傅们分享一个搜集EDU资产的FOFA语法，感兴趣的师傅们可以去玩下，搜索出来的资产也蛮多的
```php
org="China Education and Research Network Center" &&("后台"||"登录")&&("中学"||"技术学院"||"小学"||"职业学院"||"中专"||"幼儿园"||"人社局"||"科学院")
```
![](https://cdn.nlark.com/yuque/0/2025/png/55850010/1762223024545-94dcfadb-3da8-4c30-a108-d3e5651811a6.png "null")
#### 2、\*\*懒人版，在线网站\*\*
懒人版，在线网站如下：
<https://app.pentest-tools.com/scans/new-scan>
![](https://mmbiz.qpic.cn/sz\_mmbiz\_png/b7iaH1LtiaKWUpEJvwgTTydKw53iboicaDuVEDXGXzGriaRibiaqcGPzC8g9ia9YKEqdnpfBiaMSmcTSWhj8iaaRNPnJWBSA/640?wx\_fmt=png&from=appmsg "null")
这个站点的功能十分强大，但是很多都是需要付费升级的功能里面还有很先进的AI漏洞挖掘分析的功能，但是要付费，里面的免费模块也是蛮不错的，
我下面进行对一个企业src的域名进行子域名挖掘，一分钟的时间就挖掘出来了62个子域名，且使用十分简单
![](https://mmbiz.qpic.cn/sz\_mmbiz\_png/b7iaH1LtiaKWUpEJvwgTTydKw53iboicaDuVKCWmT6oxZE0dvSGcncNIiaEyrkqxyQZsElIj13GhLaAAvVa0fW1GAKQ/640?wx\_fmt=png&from=appmsg "null")
十分可以看到这个侦察工具这里，有一个Google黑客
![](https://mmbiz.qpic.cn/sz\_mmbiz\_png/b7iaH1LtiaKWUpEJvwgTTydKw53iboicaDuVMfPrlQsPVATXmRicwbdfiauKSf9CHknVLMdbpejrs85bl6icl2dxlMTnw/640?wx\_fmt=png&from=appmsg "null")
可以看到里面直接把一些重要的查询功能点都给你列出来了，十分简单，对小白师傅们十分友好
![](https://mmbiz.qpic.cn/sz\_mmbiz\_png/b7iaH1LtiaKWUpEJvwgTTydKw53iboicaDuVHgDZBYw7qibqRxtKP6ibkb7R43icR5TthosPe2v13sBpBzrvz0UKWrn6w/640?wx\_fmt=png&from=appmsg "null")
下面的配置文件信息，直接就可以查询到了，不需要你会Google语法，直接使用这个工具你也可以很强大
![](https://mmbiz.qpic.cn/sz\_mmbiz\_png/b7iaH1LtiaKWUpEJvwgTTydKw53iboicaDuVFPYicSOHI2D3DdhEHJ4AProdiaHLPclpbcLQ8adk5S9VZNuUiakmzJwzQ/640?wx\_fmt=png&f...