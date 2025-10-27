---
title: 【青少年CTF】-Osint-小镇后面的山-预期题解
url: https://www.secpulse.com/archives/195399.html
source: 安全脉搏
date: 2023-02-07
fetch_date: 2025-10-04T05:50:19.810913
---

# 【青少年CTF】-Osint-小镇后面的山-预期题解

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

# 【青少年CTF】-Osint-小镇后面的山-预期题解

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[青少年CTF](https://www.secpulse.com/newpage/author?author_id=49279)

2023-02-06

17,725

# 0x01 前言

> ❝
>
> 题目来源于青少年CTF在2023年1月举办的「2023-SICTF」，这是由出题人编写的预期解内容。
>
> ❞

> ❝
>
> 原创作者：：秋风
> 正文共：316字
> 投稿于：青少年CTF论坛
> 题目已投放至「青少年CTF」
>
> ❞

这题我最开始弄出来放到SICTF上的时候，预期题解还挺好玩的，但是被人用谷歌搜一半找类似建筑找出来了，又有人用爆破方法做的。所以我在此公开我的预期题解，让大家感受下OSINT的乐趣。

# 0x02 过程

1.通过车牌分析，白底黑字的缩小范围到欧洲

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195399-1675670797.png)

2.看告示牌的标语

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195399-16756707971.png)

ici是 这里的意思

LE是相当于英语 the(后面的我也看不清，但是大概意思是禁止车辆通过/人行横道)

所以确定是法国

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195399-1675670798.png)

从壁炉来看，这地方有一段时间是很冷的

但是法国的中部冬天并不冷，所以肯定不在中心的位置，现在其实答案呼之欲出，

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195399-1675670799.png)

又发现棕榈树，所以推断出是山地气候，冬凉夏暖 很符合图示

推断出法国南部是山地气候

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195399-1675670800.png)

这明显条纹状断层，是沉积岩，不难推出是阿尔卑斯山脉

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195399-1675670808.png)

也就是偏下一点

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195399-1675670813.png)
![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195399-1675670819.png)

又因为有有轨电车

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-195399-1675670821.png)

和以上特征

所以是 格勒诺布尔

**本文作者：[青少年CTF](newpage/author?author_id=49279)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/195399.html**](https://www.secpulse.com/archives/195399.html)

Tags: [ctf](https://www.secpulse.com/archives/tag/ctf)、[OSINT](https://www.secpulse.com/archives/tag/osint)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![CTF中RSA常见攻击方法](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1678785929506-300x205.png)

  CTF中RSA常见攻击方法](https://www.secpulse.com/archives/197505.html "详细阅读 CTF中RSA常见攻击方法")
* [![探究SMC局部代码加密技术以及在CTF中的运用](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1678429569077-300x190.png)

  探究SMC局部代码加密技术以及在CTF中…](https://www.secpulse.com/archives/197285.html "详细阅读 探究SMC局部代码加密技术以及在CTF中的运用")
* [![CTF中的神兵利刃-foremost工具之文件分离](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/图片111-300x156.png)

  CTF中的神兵利刃-foremost工具…](https://www.secpulse.com/archives/196849.html "详细阅读 CTF中的神兵利刃-foremost工具之文件分离")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/12/1670568845919.png)](https://www.secpulse.com/newpage/author?author_id=49279aaa) | [青少年CTF](https://www.secpulse.com/newpage/author?author_id=49279) | |
| 文章数：8 | 积分： 60 |
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
* |
* [i春秋](https://www.ichunqiu.com)
* |
* [铁匠运维网](http://www.tiejiang.org/)
* |
* [吾爱漏洞](http://www.52bug.cn/)
* |
* [ChaMd5安全团队](http://www.chamd5.org/team/)
* |
* [黑白网](http://www.heibai...