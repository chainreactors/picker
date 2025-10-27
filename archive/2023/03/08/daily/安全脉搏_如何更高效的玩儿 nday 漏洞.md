---
title: 如何更高效的玩儿 nday 漏洞
url: https://www.secpulse.com/archives/197113.html
source: 安全脉搏
date: 2023-03-08
fetch_date: 2025-10-04T08:52:33.945248
---

# 如何更高效的玩儿 nday 漏洞

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

# 如何更高效的玩儿 nday 漏洞

[漏洞](https://www.secpulse.com/archives/category/vul)

[信安之路](https://www.secpulse.com/newpage/author?author_id=49490)

2023-03-07

10,763

最近又重新收集了一波 src 的信息，整理了上百万的网站资产，主要步骤：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197113-1678171484.png)

可能大家都知道互联网上存在的漏洞中，nday 漏洞占比很可观，那么针对上百万的网站如何更快，更有效的从中挖掘 nday 漏洞呢？

有的人可能会说，poc 工具一把梭就可以了，比如 nuclei、xray、goby 等一键扫描，这种是最直接，最方便的打法，但是如果针对的是单个网站，或者几个网站，一把梭下来也要不了多久，但是针对上百万的资产，这么操作下来估计得个一年半载。

又有人说了，时间长，你不会采用分布式的打法吗？一台扫描器需要一年，你用十二台不就之需要一个月了吗？这种方式对于实现目标而言当然是可以的，但是对于服务器的操作和管理成本比较，服务器的租用成本与上一种一样，但是我很穷，有没有时间更短，服务器成本更低的方法？

poc 越多，对于单个网站的测试时间越长，比如 xray 高级版自带近 800 个 POC，nuclei 有三千个，上百万的网站，这么测试下来，以 xray 为例，需要 800 个一百万，以每秒 100 次的请求计算，大概需要三个月，如果测试的速度再慢点，时间会更长。

在这个测试中，其实有大量的测试是无效的，因为 poc 测试之有针对对应的系统才有效果，如果系统类型不对，则测试的过程无效，那么我们可以基于要测试的系统进行指纹识别，然后针对要测试的 POC 进行分类，这样精细化的测试，可以大大节约测试的时间，效果上面也不会太差。

### 0x01 基于 POC 定制指纹库

我的第一个操作是，基于 poc 所对应的系统进行整理，并提取相关指纹，然后获取这百万网站的 header、首页内容作为基础数据，然后进行指纹识别，找出那些 poc 所针对的系统目标。

对于以上操作，需要解决两个难点：

#### 1、指纹提取

我的做法是，首先去 fofa（指纹识别能力还不错） 上搜索，找到一个在线案例，然后通过观察其 header 信息、body 内容、标题等关键点，提取与该系统相关的信息作为其识别的特征，比如：

以标题为特征：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197113-1678171486.png)

以 header 为特征：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197113-1678171488.png)

以 body 内容关键词为特征：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197113-1678171490.png)

基于以上三个部分的特征可以识别大部分的系统，这种系统主要为商业、开源的系统，客户不做二次开发，直接拿来用的，除了这些系统，还有大量框架、组建、服务器之类的，无法很好的进行指纹识别，这类 poc，我会将其作为通用 poc，针对全部系统进行测试，以免因为指纹识别结果漏报而无法全面发现漏洞。

#### 2、指纹规则与 poc 命名联动

编写指纹规则时，我们想要让规则识别出的系统与其对应的 POC 联动，那么就需要在命名上与 poc 的命名保持一致，比如 xray 中关于 wordpree 的 poc 命名如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197113-1678171491.png)

那么我们就需要编写一个可以产品名为 wordpress 的指纹规则，如图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197113-1678171492.png)

那么在指纹识别结束后，就能知道那些系统是使用 wordpress 系统搭建，这个时候就可以使用其对应的 poc 列表进行测试。

### 0x02 基于指纹识别结果进行 POC 测试

经过第一步的操作，基于 xray 提供的 poc 列表，定制了一份包含 247 个系统的指纹库，对于那些针对开发框架、服务器、通用组件测试的 POC 提取出来，大概 99 个，这些 poc 将作为后续，针对每一个系统测试的 poc 列表。

其余 POC 将基于指纹识别的结果进行针对性的测试，共计 713 个，经过以下两个步骤，针对百万网站做了指纹识别：

1、获取百万网站的首页内容（响应码、header、body内容）

2、基于指纹库识别通用系统类型（7 万左右目标，识别出的系统类型 166 个）

从实战结果来看，整体测试下来相比全部测试，时间上至少提高 8 倍，原本需要三个月测试完成的目标，使用这种方式仅需要十来天即可完成。

有了这些基础数据，漏洞测试就是一条命令的事儿，相信用过 xray 的都知道怎么用，这里就不多说了。‍‍‍‍‍

### 0x03 总结

当你拥有开发能力之后，一切想法都可以形成脚本或者工具来帮助你提高效率，解放人力，自动化挖漏洞是一件非常有意思的事情，写工具写脚本也会给自己带来成就感，如果你对上面的内容感兴趣，欢迎加入信安之路与我们一起交流。

**本文作者：[信安之路](newpage/author?author_id=49490)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/197113.html**](https://www.secpulse.com/archives/197113.html)

Tags: [nday 漏洞](https://www.secpulse.com/archives/tag/nday-%E6%BC%8F%E6%B4%9E)、[POC](https://www.secpulse.com/archives/tag/poc)、[Xray](https://www.secpulse.com/archives/tag/xray)、[指纹提取](https://www.secpulse.com/archives/tag/%E6%8C%87%E7%BA%B9%E6%8F%90%E5%8F%96)、[漏洞](https://www.secpulse.com/archives/tag/%E6%BC%8F%E6%B4%9E)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![代码审计 | 同源策略的绕过](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/09/a799223d33bd92e8b0620d8ad38ecd2.jpg)

  代码审计 | 同源策略的绕过](https://www.secpulse.com/archives/203439.html "详细阅读 代码审计 | 同源策略的绕过")
* [![云原生安全联防联抗策略玩转微隔离](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/09/1694157547520-300x155.png)

  云原生安全联防联抗策略玩转微隔离](https://www.secpulse.com/archives/203414.html "详细阅读 云原生安全联防联抗策略玩转微隔离")
* [![从2023蓝帽杯0解题heapSpary入门堆喷](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1693450185258-300x157.png)

  从2023蓝帽杯0解题heapSpary…](https://www.secpulse.com/archives/203218.html "详细阅读 从2023蓝帽杯0解题heapSpary入门堆喷")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/1396eb4a28abd3245bce454bfb351c42_11-290x290.jpg)](https://www.secpulse.com/newpage/author?author_id=49490aaa) | [信安之路](https://www.secpulse.com/newpage/author?author_id=49490) | |
| 文章数：6 | 积分： 0 |
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

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx187be17d5a2961cf&redirect_uri=httpswww.bagevent.comevent6531722&response_type=code&...