---
title: 众至科技发布12月漏洞通告 | Apache Fineract 路径遍历漏洞；Prometheus 认证绕过漏洞
url: https://www.secpulse.com/archives/192729.html
source: 安全脉搏
date: 2022-12-06
fetch_date: 2025-10-04T00:33:51.388750
---

# 众至科技发布12月漏洞通告 | Apache Fineract 路径遍历漏洞；Prometheus 认证绕过漏洞

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

# 众至科技发布12月漏洞通告 | Apache Fineract 路径遍历漏洞；Prometheus 认证绕过漏洞

[资讯](https://www.secpulse.com/archives/category/news)

[众至科技](https://www.secpulse.com/newpage/author?author_id=46034)

2022-12-05

7,452

##### **【漏洞通告】Apache Fineract 路径遍历漏洞**

###### 1. **基础信息**

|  |  |
| --- | --- |
| CVE | CVE-2022-44635 |
| 等级 | 高危 |
| 类型 | 路径遍历 |

###### 2. **漏洞详情**

Apache Fineract是用于金融服务的开源软件，旨在实现核心银行系统平台化建设。

11月29日，Apache发布安全公告，修复了Apache Fineract中的一个路径遍历漏洞。Apache Fineract的文件上传组件中存在路径遍历漏洞，可能导致经过身份验证的恶意用户远程执行代码。

###### 3. **影响范围**

Apache Fineract <= 1.8.0（分支补丁版本1.7.1不受影响）

###### **4.安全建议**

目前该漏洞已经修复，受影响的用户可升级到Apache Fineract版本1.7.1 、1.8.1或更高版本。

###### **5.参考链接**

https://lists.apache.org/thread/t8q6fmh3o6yqmy69qtqxppk9yg9wfybg

https://cwiki.apache.org/confluence/display/FINERACT/Fineract+Project+Security+Report

##### **【漏洞通告】Prometheus 认证绕过漏洞**

###### 1. **基础信息**

|  |  |
| --- | --- |
| CVE | CVE-2022-46146 |
| **等级** | **高危** |
| **类型** | **认证绕过** |

###### 2. **漏洞详情**

 Prometheus是一个开源的系统监控和报警系统，现在已经加入到CNCF基金会，成为继k8s之后第二个在CNCF托管的项目，在kubernetes容器管理系统中，通常会搭配prometheus进行监控，同时也支持多种exporter采集数据，还支持pushgateway进行数据上报，Prometheus性能足够支撑上万台规模的集群。

Prometheus Exporter Toolkit是一个用于构建导出器的实用程序包。在0.7.2和0.8.2版本之前，如果有人能够访问Prometheus web.yml文件和用户的bcrypted密码，他们可以通过毒害内置认证缓存来绕过安全。0.7.2和0.8.2版本包含对该问题的修复。没有解决方法，但攻击者必须有机会获得散列的密码才能使用这个功能。

###### 3. **影响范围**

Prometheus < 0.7.2

Prometheus < 0.8.2

###### **4.安全建议**

官方已发布漏洞补丁，补丁链接：https://github.com/prometheus/exporter-toolkit/commit/5b1eab34484ddd353986bce736cd119d863e4ff5

###### **5.参考链接**

https://github.com/prometheus/exporter-toolkit/commit/5b1eab34484ddd353986bce736cd119d863e4ff5

**本文作者：[众至科技](newpage/author?author_id=46034)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/192729.html**](https://www.secpulse.com/archives/192729.html)

Tags: [Apache Fineract 路径遍历漏洞](https://www.secpulse.com/archives/tag/apache-fineract-%E8%B7%AF%E5%BE%84%E9%81%8D%E5%8E%86%E6%BC%8F%E6%B4%9E)、[CVE-2022-44635](https://www.secpulse.com/archives/tag/cve-2022-44635)、[CVE-2022-46146](https://www.secpulse.com/archives/tag/cve-2022-46146)、[Prometheus 认证绕过漏洞](https://www.secpulse.com/archives/tag/prometheus-%E8%AE%A4%E8%AF%81%E7%BB%95%E8%BF%87%E6%BC%8F%E6%B4%9E)

点赞：
5
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![【漏洞预警】Apache Fineract 文件上传漏洞](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1669949695173-300x197.png)

  【漏洞预警】Apache Finerac…](https://www.secpulse.com/archives/192736.html "详细阅读 【漏洞预警】Apache Fineract 文件上传漏洞")
* [![靶场战神为何会陨落？](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/09/VCG41N952384318.png)

  靶场战神为何会陨落？](https://www.secpulse.com/archives/205395.html "详细阅读 靶场战神为何会陨落？")
* [![《内网安全攻防》姊妹篇《红队之路》重磅上市！（文末赠书）](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-204824-1711610670-210x140.png)

  《内网安全攻防》姊妹篇《红队之路》重磅上](https://www.secpulse.com/archives/204824.html "详细阅读 《内网安全攻防》姊妹篇《红队之路》重磅上市！（文末赠书）")

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

[EISS-2020企业信息安全峰会之北京站 | 7.31（周五线上）](http://www.anquanjia.net.cn/main/detail?postId=83)

#### 2020-04-15

[看雪.安恒 2020 KCTF 春季赛](https://ctf.pediy.com)

#### 2020-01-09

[相约本地生活安全沙龙暨白帽子颁奖典礼](https://www.bagevent.com/event/6241320)

### 安全问答社区

![安全问答社区](https://www.secpulse.com/wp-content/themes/secpulse2017/img/xcx.png)

### 脉搏官方公众号

![脉搏公众号](https://www.secpulse.com/wp-content/themes/secpulse2017/img/SecPulse.png)

### 友情链接

---

* [网络尖刀](http://www.ijiandao.com/)
* |
* [Sec-Wiki](https://www.sec-wiki.com/)
* |
* [独自等待](https://www.waitalone.cn/)
* |
* [中国红客联盟](https://www.ihonker.org/)
* |
* [娜迦信息](http://www.nagain.com/)
* |
* [SecSilo](https://www.secsilo.co...