---
title: Potato土豆提权工具绕过防护思路-1
url: https://www.secpulse.com/archives/202273.html
source: 安全脉搏
date: 2023-06-21
fetch_date: 2025-10-04T11:44:34.462532
---

# Potato土豆提权工具绕过防护思路-1

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

# Potato土豆提权工具绕过防护思路-1

[工具](https://www.secpulse.com/archives/category/tools)

[潇湘信安](https://www.secpulse.com/newpage/author?author_id=37983)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2023-06-20

23,117

|  |
| --- |
| **声明：**该公众号大部分文章来自作者日常学习笔记，也有部分文章是经过作者授权和其他公众号白名单转载，未经授权，严禁转载，如需转载，联系开白。  请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。 |

现在只对常读和星标的公众号才展示大图推送，建议大家把潇湘信安“设为星标”，否则可能看不到了！

**0x01 常规利用**

前段时间在群里看到有人在搜集“土豆”系列的提权工具，抽空整理了下之前用过的一些，还有最近刚放出的DCOMPotato，仅分享给有需要的人。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202273-1687241671.png)

当然，除了可以利用“土豆”系列的提权工具外，我们也可以利用MSF或哥斯拉下的各种“土豆”提权模块来进行提权，根据实际场景选择合适的吧。

```
exploit/windows/local/ms16_075_reflection

exploit/windows/local/ms16_075_reflection_juicy
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202273-16872416711.png)

**0x02 防护绕过**

**之前实战中遇到的一个案例：**Win10系统，iis权限，存在Defender杀软，哥斯拉默认的aspx马会被杀，需要做下免杀处理，最后利用SweetPotato成功提权。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202273-1687241679.png)

还和群里师傅们一起讨论了下某师傅在实战场景中利用土豆提权时被防护拦截和绕过的问题，这里我就不搭建环境复现写文章了，群里讨论过程可见下图聊天记录。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202273-1687241682.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202273-1687241683.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202273-1687241685.png)

**本文作者：[潇湘信安](newpage/author?author_id=37983)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/202273.html**](https://www.secpulse.com/archives/202273.html)

Tags: [Defender杀软](https://www.secpulse.com/archives/tag/defender%E6%9D%80%E8%BD%AF)、[iis权限](https://www.secpulse.com/archives/tag/iis%E6%9D%83%E9%99%90)、[Win10系统](https://www.secpulse.com/archives/tag/win10%E7%B3%BB%E7%BB%9F)、[土豆](https://www.secpulse.com/archives/tag/%E5%9C%9F%E8%B1%86)

点赞：
5
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![pocsuite3安全工具源码分析](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202502171711874.png)

  pocsuite3安全工具源码分析](https://www.secpulse.com/archives/205913.html "详细阅读 pocsuite3安全工具源码分析")
* [![自己搭建专属AI：Llama大模型私有化部署](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/12/images.png)

  自己搭建专属AI：Llama大模型私有化](https://www.secpulse.com/archives/205740.html "详细阅读 自己搭建专属AI：Llama大模型私有化部署")
* [![内网信息搜集神器—searchall](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1693463314861-210x140.png)

  内网信息搜集神器—searc](https://www.secpulse.com/archives/203203.html "详细阅读 内网信息搜集神器—searchall")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2020/11/12/5abbd29a2ce13702d20784fb420161da-290x290.png)](https://www.secpulse.com/newpage/author?author_id=37983aaa) | [潇湘信安 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)](https://www.secpulse.com/newpage/author?author_id=37983) | |
| 文章数：57 | 积分： 15 |
| 关注微信公众号【潇湘信安】，一起学习网络安全知识！ | |

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
* |
* [i春秋](https://www.ichunqiu.com)
* |
* [铁匠运维网](http://www.tiejiang.org/)
* |
* [吾爱漏洞](http://www.52bug.cn/)
* |
* [...