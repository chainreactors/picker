---
title: 安全攻防 | CobaltStrike与水坑攻击的联动
url: https://www.secpulse.com/archives/192987.html
source: 安全脉搏
date: 2022-12-07
fetch_date: 2025-10-04T00:38:49.445271
---

# 安全攻防 | CobaltStrike与水坑攻击的联动

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

# 安全攻防 | CobaltStrike与水坑攻击的联动

[工具](https://www.secpulse.com/archives/category/tools)

[贝塔安全实验室](https://www.secpulse.com/newpage/author?author_id=9525)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2022-12-06

12,180

最近项目中遇到了一个问题，在拿下目标某站点时站点建设在云上，无法直接攻击目标内网，在进行水坑攻击的时候员工执行了木马程序但因为钓鱼页面没有及时撤掉从而被识破。

基于上述情况，所以抽空撸了一个联动CobaltStrike的钓鱼程序

## 0x01 实现

先附上项目代码：

https://github.com/HolyGu/CobaltStrikeToWateringhole

实现功能：

钓鱼界面自动撤除，例如A员工访问了钓鱼界面并且下载执行了木马，重新访问网页的时候钓鱼界面不会再出现，B员工访问的时候依旧是钓鱼界面，从而做到尽可能多的钓到鱼又不会被怀疑

此项目基于另一个CobaltStrike上线钉钉/飞书提醒的项目（https://github.com/HolyGu/CobaltStrikeToWebHook）修改而来

1. 首先创建一个表，用来存储上线用户的IP地址

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192987-1670309256.png)

2. 其次修改一下WebHook.php的代码，加入一个把互联网IP写入数据库的操作

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192987-1670309257.png)

3. 然后再修改WebHook.cna，加入第24行，以及在27行末尾加入发送公网IP

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192987-1670309258.png)

4. 接着创建一个Fish.php，用来判断访问者IP是否在数据库内

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192987-1670309259.png)

4. 最后创建一个Fish.js，用来植入在目标网站

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192987-1670309261.png)

## 0x02 效果

效果视频请点击公众号原文链接观看：<https://mp.weixin.qq.com/s/_F5yyr1t09H-p1v0zU3RgA>

## 0x03 优化方向

因为是项目中抽空写的，一些地方还有待优化，等后面有空了再搞搞

1. 加入地区白名单功能，例如A公司总部在上海，运维/安全人员也都在上海，那么可以将上海地区加入白名单，从而防止运维/安全人员访问站点的时候发现。

2. 将跳转改为页面遮罩，这样用户下载执行木马以后只需要重新刷新网站即可。

**本文作者：[贝塔安全实验室](newpage/author?author_id=9525)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/192987.html**](https://www.secpulse.com/archives/192987.html)

Tags: [Cobaltstrike](https://www.secpulse.com/archives/tag/cobaltstrike)、[水坑攻击](https://www.secpulse.com/archives/tag/%E6%B0%B4%E5%9D%91%E6%94%BB%E5%87%BB)、[钓鱼程序](https://www.secpulse.com/archives/tag/%E9%92%93%E9%B1%BC%E7%A8%8B%E5%BA%8F)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![社会工程学 | office宏分离免杀及应急处置](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/1676359162449-300x158.png)

  社会工程学 | office宏分离免杀及…](https://www.secpulse.com/archives/195847.html "详细阅读 社会工程学 | office宏分离免杀及应急处置")
* [![再次捕获！重保期间拦截针对Coremail的钓鱼攻击](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-184900-1659924834-300x169.png)

  再次捕获！重保期间拦截针对Coremai…](https://www.secpulse.com/archives/184900.html "详细阅读 再次捕获！重保期间拦截针对Coremail的钓鱼攻击")
* [![FakeLogonScreen – 伪造Windows登录屏幕以窃取密码](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/04/16503330691-300x195.png)

  FakeLogonScreen R…](https://www.secpulse.com/archives/177260.html "详细阅读 FakeLogonScreen – 伪造Windows登录屏幕以窃取密码")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2020/08/1db8ec186f5e122a1420ccb5499c476d-150x150.png)](https://www.secpulse.com/newpage/author?author_id=9525aaa) | [贝塔安全实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=9525) | |
| 文章数：29 | 积分： 65 |
|  | |

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
* [SecSilo](https://www.secsilo.com/)
* |
* [易安在线](http://www.e365.org/)
* ...