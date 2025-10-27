---
title: 自动化批量挖(edu)漏洞
url: https://www.secpulse.com/archives/189266.html
source: 安全脉搏
date: 2022-10-19
fetch_date: 2025-10-03T20:13:04.399362
---

# 自动化批量挖(edu)漏洞

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

# 自动化批量挖(edu)漏洞

[工具](https://www.secpulse.com/archives/category/tools)

[潇湘信安](https://www.secpulse.com/newpage/author?author_id=37983)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng3.png)

2022-10-18

11,697

|  |
| --- |
| **声明：**该公众号大部分文章来自作者日常学习笔记，也有部分文章是经过作者授权和其他公众号白名单转载，未经授权，严禁转载，如需转载，联系开白。  请勿利用文章内的相关技术从事非法测试，如因此产生的一切不良后果与文章作者和本公众号无关。 |

**原理**

原理是将目标资产让爬虫工具爬取，把数据通过burp发送给xray进行漏洞扫描。

**使用到的工具**

```
Fofa采集工具，文章用edu举例，大家可以根据自己的目标进行选择。
Rad，浏览器爬取工具，github地址: https://github.com/chaitin/rad
Chrome浏览器, Rad默认支持浏览器
Burp和Xray就不赘述了
```

**步骤一**

1. 由于举例子，就用fofa采集工具去批量采集edu资产来做演示，有fofa会员更好，资产相对多一些。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189266-1666056886.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189266-1666056888.png)

2. 因为要使用Rad爬虫，所以我们要对资产进行整理，要使他符合Rad的规则，我们要把上图红框框里的IP加上http://或者https://。

我记得之前学校有考过一个题，就是在excel表中批量给单元格加同样的内容，不过我忘了，这里就用。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189266-1666056891.png)

python解决好了，脚本如下

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189266-16660568911.png)

上面是资产处理好的效果图，放到Rad目录下，后面的内容会用到。

**步骤二**

我们需要给burp添加插件，设置代理。被动扫描插件可以更大几率提高挖到的可能性，说不准捡个漏啥的，这里方便演示随意加俩，当然插件是多多益善

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189266-1666056892.png)

代理设置为8080，为了是和Rad响应

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189266-1666056893.png)

流量出口设置为7777，因为们要将数据包发给Xray

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189266-1666056894.png)

**步骤三**

1. 开启Xray被动扫描，监听7777，（Xray默认不扫edu，需要在config.yaml修改规则）

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189266-1666056897.png)

2. 资产准备好了，漏洞扫描器也开始监听了，就差爬虫的数据了，众所周知命令行窗口只能一个一个的输入，步骤一的资产很多，一个一个输入很麻烦也就不是自动化了，这里使用python脚本批量，脚本内容如下：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189266-1666056900.png)

第28行是步骤一整理好资产.txt的文件名，第30行可以根据需求来修改线程

**3. 运行脚本，效果如下**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189266-1666056901.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-189266-1666056910.png)

```
文章来源：CSDN博客（Y7ii）
原文地址：https://blog.csdn.net/m0_46736332/article/details/118888256
```

**本文作者：[潇湘信安](newpage/author?author_id=37983)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/189266.html**](https://www.secpulse.com/archives/189266.html)

Tags: [8080](https://www.secpulse.com/archives/tag/8080)、[Burp](https://www.secpulse.com/archives/tag/Burp)、[edu](https://www.secpulse.com/archives/tag/edu)、[Fofa](https://www.secpulse.com/archives/tag/fofa)、[​Rad](https://www.secpulse.com/archives/tag/%E2%80%8Brad)、[Xray](https://www.secpulse.com/archives/tag/xray)、[挖漏洞](https://www.secpulse.com/archives/tag/%E6%8C%96%E6%BC%8F%E6%B4%9E)、[浏览器爬取工具](https://www.secpulse.com/archives/tag/%E6%B5%8F%E8%A7%88%E5%99%A8%E7%88%AC%E5%8F%96%E5%B7%A5%E5%85%B7)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![实战！记一次超简单渗透过程笔记](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1685526754726-300x191.png)

  实战！记一次超简单渗透过程笔记](https://www.secpulse.com/archives/201229.html "详细阅读 实战！记一次超简单渗透过程笔记")
* [![在WAF中加入AI的一次尝试，附demo程序](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-201157-1685425656-300x256.png)

  在WAF中加入AI的一次尝试，附demo…](https://www.secpulse.com/archives/201157.html "详细阅读 在WAF中加入AI的一次尝试，附demo程序")
* [![泛微ecology9 ofsLogin.jsp 信息泄露与前台任意用户登录漏洞分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1684481531661-300x183.png)

  泛微ecology9 ofsLogin.…](https://www.secpulse.com/archives/200741.html "详细阅读 泛微ecology9 ofsLogin.jsp 信息泄露与前台任意用户登录漏洞分析")

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

[OPPO技术开放日第六期|聚焦应用与数据安全防护](htt...