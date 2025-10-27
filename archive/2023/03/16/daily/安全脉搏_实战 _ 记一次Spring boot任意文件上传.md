---
title: 实战 | 记一次Spring boot任意文件上传
url: https://www.secpulse.com/archives/197601.html
source: 安全脉搏
date: 2023-03-16
fetch_date: 2025-10-04T09:44:40.442228
---

# 实战 | 记一次Spring boot任意文件上传

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

# 实战 | 记一次Spring boot任意文件上传

[资讯](https://www.secpulse.com/archives/category/news)

[HACK\_Learn](https://www.secpulse.com/newpage/author?author_id=8971)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-03-15

11,738

前提：

在一次项目中获取了一套通用系统

框架是Spring boot

启动是War包启动

之前拿是通过替换私钥拿的，但小部分还是没开公钥登录

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197601-1678863110.png)

这时候就有人说为什么不通过写在定时任务反弹shell

也试过，不会返回，所以这个方案就取消了

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197601-1678863111.png)

咋不直接上传，因为上传的文件是到另外一个端口，而且不解析

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197601-16788631111.png)

所以就想到一个另外的思路，由于这套是通用的，包括他们安装目录也一样

替换他们的war包,先下载他们的war包

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197601-1678863112.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197601-1678863114.png)

把war用压缩格式打开，然后添加马子

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197601-16788631141.png)

然后直接用burp上传抓包不太行，如图，会内容太大不显示，因为我们还是通过跨目录上传

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197601-1678863115.png)

所以写了个脚本

```
1.上传替换
2.要定时任务执行kill杀死当前进程 pkill -f ***.war
3.要启动war项目java -Dfile.encoding=utf-8 -jar ***.war --spring.config.location=application.properties
```

通用直接写脚本梭哈

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197601-16788631151.png)这里脚本是设置了代理，看看返回的包

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197601-1678863117.png)显示是上传成功，看看web项目

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197601-16788631171.png)如果直接替换，不重启war包是没效果的，如图

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197601-1678863119.png)总结：

实战没用，只是说对于通用系统，部分利用的点不能利用的情况下，可以这样弄。所以个人觉得鸡助。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197601-1678863120.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197601-1678863123.png)

原创投稿作者：0003

**本文作者：[HACK\_Learn](newpage/author?author_id=8971)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/197601.html**](https://www.secpulse.com/archives/197601.html)

Tags: [Spring boot](https://www.secpulse.com/archives/tag/spring-boot)、[任意文件上传](https://www.secpulse.com/archives/tag/%E4%BB%BB%E6%84%8F%E6%96%87%E4%BB%B6%E4%B8%8A%E4%BC%A0)、[私钥](https://www.secpulse.com/archives/tag/%E7%A7%81%E9%92%A5)、[端口](https://www.secpulse.com/archives/tag/%E7%AB%AF%E5%8F%A3)、[跨目录上传](https://www.secpulse.com/archives/tag/%E8%B7%A8%E7%9B%AE%E5%BD%95%E4%B8%8A%E4%BC%A0)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![Responder与evil-winRM配合远程登录Windows](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/16872431395792-300x192.png)

  Responder与evil-winRM…](https://www.secpulse.com/archives/203051.html "详细阅读 Responder与evil-winRM配合远程登录Windows")
* [![新一代RedTeam启发式内网扫描工具](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/07/1688546246784-300x194.png)

  新一代RedTeam启发式内网扫描工具](https://www.secpulse.com/archives/202616.html "详细阅读 新一代RedTeam启发式内网扫描工具")
* [![堡垒机下的任意文件读取漏洞挖掘](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1686815379890-300x161.png)

  堡垒机下的任意文件读取漏洞挖掘](https://www.secpulse.com/archives/202163.html "详细阅读 堡垒机下的任意文件读取漏洞挖掘")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1ca91da9312f04fadf4ab539bb3cb881.png)](https://www.secpulse.com/newpage/author?author_id=8971aaa) | [HACK\_Learn ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=8971) | |
| 文章数：142 | 积分： 323 |
| 微信公众号：HACK学习呀 | |

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

[CSDI summit中国软件研发管理行业技术峰会](https://www.bagevent.com/...