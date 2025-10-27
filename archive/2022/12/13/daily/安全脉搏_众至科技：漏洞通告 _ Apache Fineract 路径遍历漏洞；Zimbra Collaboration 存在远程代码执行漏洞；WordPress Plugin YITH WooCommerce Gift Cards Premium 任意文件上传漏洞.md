---
title: 众至科技：漏洞通告 | Apache Fineract 路径遍历漏洞；Zimbra Collaboration 存在远程代码执行漏洞；WordPress Plugin YITH WooCommerce Gift Cards Premium 任意文件上传漏洞
url: https://www.secpulse.com/archives/193385.html
source: 安全脉搏
date: 2022-12-13
fetch_date: 2025-10-04T01:16:37.354847
---

# 众至科技：漏洞通告 | Apache Fineract 路径遍历漏洞；Zimbra Collaboration 存在远程代码执行漏洞；WordPress Plugin YITH WooCommerce Gift Cards Premium 任意文件上传漏洞

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

# 众至科技：漏洞通告 | Apache Fineract 路径遍历漏洞；Zimbra Collaboration 存在远程代码执行漏洞；WordPress Plugin YITH WooCommerce Gift Cards Premium 任意文件上传漏洞

[漏洞](https://www.secpulse.com/archives/category/vul)

[众至科技](https://www.secpulse.com/newpage/author?author_id=46034)

2022-12-12

7,917

##### 【漏洞通告】Apache Fineract 路径遍历漏洞

###### 1. 基础信息

|  |  |
| --- | --- |
| CVE | CVE-2022-46366 |
| 等级 | 高危 |
| 类型 | RCE |

###### 2. 漏洞详情

Apache Tapestry是一种基于Java的Web应用程序框架。Tapestry采用了组件的概念。程序员可以应用现有的组建或自定义应用程序相关的组建来构建应用程序。在Apache Tapestry 3全版本允许对不受信任的数据进行反序列化，从而导致远程代码执行。

###### 3. 影响范围

Apache Tapestry 3.x

###### 4.安全建议

由于Apache Tapestry 3 系列官方已经不再支持，建议受影响客户升级Apache Tapestry至最新版本。

###### 5.参考链接

<https://tapestry.apache.org/download.html>

##### 【漏洞通告】Zimbra Collaboration 存在远程代码执行漏洞

###### 1. 基础信息

|  |  |
| --- | --- |
| CVE | CVE-2022-45912 |
| 等级 | 高危 |
| 类型 | RCE |

###### 2. 漏洞详情

 在Zimbra Collaboration (ZCS) 8.8.15 和 9.0 中，已认证的管理员用户可通过 ClientUploader 进行远程代码执行。已认证的管理员用户可以通过 ClientUploader 工具上传文件，并穿越到任何其他目录进行远程代码执行

###### 3. 影响范围

ZCS = 8.8.15

ZCS = 9.0.0

###### 4.安全建议

官方已发布漏洞补丁及修复版本，请评估业务是否受影响后，酌情升级至安全版本：https://www.zimbra.com/business-email-collaboration/

###### 5.参考链接

<https://www.zimbra.com/business-email-collaboration/>

##### 【漏洞通告】WordPress Plugin YITH WooCommerce Gift Cards Premium 任意文件上传漏洞

###### 1. 基础信息

|  |  |
| --- | --- |
| CVE | CVE-2022-45359 |
| 等级 | 高危 |
| 类型 | 任意文件上传 |

###### 2. 漏洞详情

 YITH WooCommerce Gift Cards Premium在3.19.0及之前版本中存在任意文件上传漏洞。这可能允许恶意行为者向你的网站上传任何类型的文件。这可能包括后门，然后执行后门以进一步访问你的网站。

###### 3. 影响范围

YITH WooCommerce Gift Cards Premium <= 3.19.0

###### 4.安全建议

请使用此产品的用户尽快更新至安全版本

###### 5.参考链接

<https://patchstack.com/database/vulnerability/yith-woocommerce-gift-cards-premium/wordpress-yith-woocommerce-gift-cards-premium-plugin-3-19-0-unauth-arbitrary-file-upload-vulnerability?_s_id=cve>

**本文作者：[众至科技](newpage/author?author_id=46034)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/193385.html**](https://www.secpulse.com/archives/193385.html)

Tags: [Apache Fineract](https://www.secpulse.com/archives/tag/apache-fineract)、[CVE-2022-45359](https://www.secpulse.com/archives/tag/cve-2022-45359)、[CVE-2022-45912](https://www.secpulse.com/archives/tag/cve-2022-45912)、[CVE-2022-46366](https://www.secpulse.com/archives/tag/cve-2022-46366)、[WordPress PluginYITH](https://www.secpulse.com/archives/tag/wordpress-pluginyith)、[Zimbra Collaboration](https://www.secpulse.com/archives/tag/zimbra-collaboration)、[任意文件上传漏洞](https://www.secpulse.com/archives/tag/%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0%E6%BC%8F%E6%B4%9E)、[存在远程代码执行漏洞](https://www.secpulse.com/archives/tag/%E5%AD%98%E5%9C%A8%E8%BF%9C%E7%A8%8B%E4%BB%A3%E7%A0%81%E6%89%A7%E8%A1%8C%E6%BC%8F%E6%B4%9E)、[路径遍历漏洞](https://www.secpulse.com/archives/tag/%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![【漏洞预警】Apache Fineract SQL注入漏洞](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1680146179072-300x152.png)

  【漏洞预警】Apache Finerac…](https://www.secpulse.com/archives/198450.html "详细阅读 【漏洞预警】Apache Fineract SQL注入漏洞")
* [![【漏洞预警】Apache Fineract 文件上传漏洞](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1669949695173-300x197.png)

  【漏洞预警】Apache Finerac…](https://www.secpulse.com/archives/192736.html "详细阅读 【漏洞预警】Apache Fineract 文件上传漏洞")
* [![E-office Server_v9.0 漏洞分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/09/1664337060631-300x220.png)

  E-office Server\_v9.0…](https://www.secpulse.com/archives/187859.html "详细阅读 E-office Server_v9.0 漏洞分析")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/06/02/f5f18ac4ab301c81c0f4c2019436d31f-300x298.png)](https://www.secpulse.com/newpage/author?author_id=46034aaa) | [众至科技](https://www.secpulse.com/newpage/author?author_id=46034) | |
| 文章数：5 | 积分： 0 |
| 网络安全保险科技创新引领者 | |

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

#### 2020-09-24

[CSDI summit中国软件研发管理行业技术峰会](https://www.bagevent.com/event/csdisummit)

#### 2020-09-23

[2020中国国际智慧能源暨能源数据中心与网络信息安全装备展览会](http://www.energydataexpo.cn)

#### 2020-07-31

[EISS-2020企业信息安全峰会之北京...