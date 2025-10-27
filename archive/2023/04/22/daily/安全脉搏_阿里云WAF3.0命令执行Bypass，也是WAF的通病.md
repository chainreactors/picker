---
title: 阿里云WAF3.0命令执行Bypass，也是WAF的通病
url: https://www.secpulse.com/archives/199318.html
source: 安全脉搏
date: 2023-04-22
fetch_date: 2025-10-04T11:32:13.109446
---

# 阿里云WAF3.0命令执行Bypass，也是WAF的通病

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

# 阿里云WAF3.0命令执行Bypass，也是WAF的通病

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[公众号:安全女巫](https://www.secpulse.com/newpage/author?author_id=49672)

2023-04-21

14,710

********如果你喜欢我的文章，欢迎关注公众号：安全女巫
转载请注明出处：******https://mp.weixin.qq.com/s/AuONhIYbnTZzIBpxpcXtIw**

**引用**

> 针对外面的流言，我引用柏拉图的《爱情海》的一句话：
>
> 如果尖锐的批评完全消失，温和的批评将会变得刺耳。
>
> 如果温和的批评也不被允许，沉默将被认为居心叵测。
>
> 如果沉默也不再允许，赞扬不够卖力将是一种罪行。
>
> 如果只允许一种声音存在，那么，唯一存在的那个声音就是谎言。
>
> 别到头变成睚眦必报。

**前言**

绕过WAF,首先需要知道WAF的工作原理，才能发现安全问题。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199318-1682048103.png)

每个阶段都有每个阶段存在的问题，笔者也踩过很多坑，不管从建设还是绕过。WAF最重要的指标还是火焰图，性能是WAF的喉咙。

**新手需要知道WAF设计阶段的几个问题**

明白工作方式处理方式，就能明白为什么这样方法绕过，从黑盒变成白盒。

为什么len长度过长能绕过，

为什么mu的类型不一样可以绕过，

为什么设计WAF时要考虑AC，

为什么规则要加载进内存

安全是为了更好的服务业务，在业务与安全冲突时，要保证业务的最低运行条件。自然而然有些问题是很难去解决的。

**发散几个WAF问题：**

1. WAF性能为王，大范围通用性的WAF必须丢弃核心指标
2. WAF语义分析，国内就长亭，国际就是imperva，polo，可能有人会为语义分析很厉害啦，其实有兴趣的朋友研究下，就知道国内所谓的语义，都是基于08年公开的基础上进行优化版本，大概就是特征码6位变8位
3. 有人会问了，什么是最好的WAF,笔者认为安全不是一个产品，是一个系统。
4. WAF被绕过不能评判一个WAF的好坏，如json请求，get/post获取数据，就很容易绕过；再就是上传，在功能点上，二者是互相排斥的。
5. worker性能问题

**知识点**

**本文使用linux 通配符“？”，绕过阿里云WAF3.0的规则检测。**

该方法因为独有的特性，基本所有的WAF都可以bypass

WAF针对通配符的处置并不会有很好的办法，WAF接受

**复现步骤**

使用阿里云WAF3.0接入点

hquspd4evkuq8r3snfplbiwhfccw3cam.aliyunwaf5.com

**接入WAF**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199318-1682048104.png)

**WAF配置信息：**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199318-16820481041.png)

**绕过步骤**

读取/etc/passwd  触发拦截

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199318-1682048105.png)

使用通配符?，绕过拦截

cat /etc/passw?

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199318-16820481051.png)

可能不太直观？我们试试在Linux 执行。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199318-1682048107.png)

**通配符还有几种形式**

星号符号（\*）：表示任何字符（包括空字符），可以出现0次、1次或多次。例如：ls \*.txt（显示当前目录下所有以 .txt 结尾的文件）

问号符号（?）：表示任意单个字符。例如：ls ?.txt（显示当前目录下所有以一个字符开头，以 .txt 结尾的文件）

中括号符号（[]）：表示中括号内任意一个字符。例如：ls [abc]\*（显示当前目录下以 a、b、c 任意一个字母开头的所有文件）

脱字符号（^）：表示取反，即除了中括号内的字符以外的任意一个字符。例如：ls [^abc]\*（显示当前目录下除了以 a、b、c 任意一个字母开头的所有文件）

**另外还有几个设计上的问题**：

**Crtl注入**

```
几个crtl  fuzz 的工具，有兴趣的小伙伴可以自己本地fuzz，大部分waf都存在
https://github.com/dwisiswant0/crlfuzzh
ttps://github.com/Proviesec/crlf-payloads
```

**host绑定绕过WAF**

通过fofa也好，指纹也好，溯源的真是IP，host绑定进行绕过WAF操作。

在search.censys.io搜索中输入域名，它就会显示与该特定域关联的所有结果 IP。

请在下面的截图中找到目标域名和 censys 正在泄露网站的真实 IP。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-199318-16820481071.png)

**结论**

这种问题不是WAF阶段能解决的问题，WAF也不是要阻断99%的攻击，WAF讲究与业务有很好的共存，其次WAF是房子外的高墙，让对抗增加成本，高墙挡不住铁了心的贼。

**本文作者：[公众号:安全女巫](newpage/author?author_id=49672)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/199318.html**](https://www.secpulse.com/archives/199318.html)

Tags: [Crtl注入](https://www.secpulse.com/archives/tag/crtl%E6%B3%A8%E5%85%A5)、[Fuzz](https://www.secpulse.com/archives/tag/fuzz)、[waf](https://www.secpulse.com/archives/tag/waf)、[绕过](https://www.secpulse.com/archives/tag/%E7%BB%95%E8%BF%87)、[通配符](https://www.secpulse.com/archives/tag/%E9%80%9A%E9%85%8D%E7%AC%A6)、[阿里云WAF](https://www.secpulse.com/archives/tag/%E9%98%BF%E9%87%8C%E4%BA%91waf)

点赞：
6
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![在WAF中加入AI的一次尝试，附demo程序](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201157-1685425656-300x256.png)

  在WAF中加入AI的一次尝试，附demo…](https://www.secpulse.com/archives/201157.html "详细阅读 在WAF中加入AI的一次尝试，附demo程序")
* [![【HackTheBox】攻克靶机实战interdimensional internet攻略分享](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1684393312004-300x222.png)

  【HackTheBox】攻克靶机实战in…](https://www.secpulse.com/archives/200516.html "详细阅读 【HackTheBox】攻克靶机实战interdimensional internet攻略分享")
* [![头疼的上传绕过waf](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-198782-1681113810-300x132.png)

  头疼的上传绕过waf](https://www.secpulse.com/archives/198782.html "详细阅读 头疼的上传绕过waf")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/06/e94ff67276552849b2f4d2570ce68dc5-290x290.png)](https://www.secpulse.com/newpage/author?author_id=49672aaa) | [公众号:安全女巫](https://www.secpulse.com/newpage/author?author_id=49672) | |
| 文章数：15 | 积分： 0 |
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

[2020京麒网络安全大会](https://w...