---
title: HVV的艺术系列 之 打点的艺术
url: https://www.secpulse.com/archives/202287.html
source: 安全脉搏
date: 2023-06-21
fetch_date: 2025-10-04T11:44:33.295046
---

# HVV的艺术系列 之 打点的艺术

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

# HVV的艺术系列 之 打点的艺术

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[Ms08067安全实验室](https://www.secpulse.com/newpage/author?author_id=11195)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)

2023-06-20

16,395

**渗透的本质是信息收集，**

**攻防的体系是知识点的串联。**

####

####

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202287-1687242692.png)

**打点的艺术**

**0****1**

**对靶标的分析**

在HVV当中，获取到的靶标存在多种行业。对不同的靶标存在不同的打法，我通常分为两个大方向。其一为机关单位，其二为集团公司等。

其中二者区别对攻击者而言，就是资产的散落程度。地级市的机关单位通常将网站托管在政务云，大数据局等。这意味着，通常两三个的C段部署着当地大量的机关单位网站集群。而集团公司等靶标应当采取“老式”的打点方式，所以接下来对两种打的方式进行打法剖析。

**0****2**

**工具的使用**

对于机关单位的打法，因为其资产通常散落在多个大的C段当中，所以首要的目标就是对其C段权重的寻找。切入点应该选择手中的靶标为机关单位的目标，以此为点。

棱眼:

https://github.com/EdgeSecurityTeam/Eeyes

对目标的子域对应IP进行C段权重的判断

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202287-16872426921.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202287-1687242707.png)

如何确定C段的权重是否正确

棱洞:

https://github.com/EdgeSecurityTeam/EHole

./EHole -f 110.242.68.1/24

其对棱眼的C段权重进行IP资产列举

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202287-1687242715.png)

接下来对其列举出来的指纹进行payload验证。

而对于集团公司的打法还是常用手法，oneForAll,百分百控股..目录等等。

常用的手法并非盲目测试payload，对目标框架的了解也是前提。

**如React，Vue，AngularJS的XSS问题？**

jquery // vue {{var}}. v-html=var

**springboot不解析jsp马的问题？**

tomcat-jsper.

**Java应用的SQL注入应不应该打的问题？**

mysql 写文件 root ,绝对路径 udf username,password, c# mssql,oracle 写文件 root ,绝对路径 udf username,password

**fofa的资产打开404真的是关站了嘛？**

扫端口

对目标技术栈springcloud分布式，k8s云新架构的入手点问题(软柿子捏的问题)等等，框架的演变史讲解

```
jsp/servlet. ==> ssh hiberna,spring,struts2. > ssm mybatis,spring,springmvc > springboot ssm 约定大于配置 => 前后端分离 json ajax 前端和 后端分开来部署 ====> springcloud.分布式。
```

我一直认为人是解决渗透难题的，并非需要把时间花费到基础漏洞上(与扫描的艺术大相径庭，只是内外网的区分)

#### **Goby和Xray的结合往往效果显著**

HVV前通常会准备七八台云服务器，部署Xray和Goby，将信息搜集到的资产经过Goby的全端口扫描之后导出web服务转入

Xray和Rad的批量扫描。例如机关单位的几个C段进行Goby全端口扫描

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202287-1687242728.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202287-1687242731.png)

不要小看扫描器，他能发现很多人不能发现的脆弱点，经过很多次实践，发现Xray和Goby带给我了我很多意想不到的惊喜。

**0****3**

**资产的整理**

渗透的本质是信息收集，我们应该把对于每个靶标的收集到的内容进行汇总填充到xlsx当中

或许队友能打进去的点我们未必能进去，通过xlsx的表格和队友的对比能准确找到和队友信息收集到的内容差异。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-202287-1687242734.png)

**本文作者：[Ms08067安全实验室](newpage/author?author_id=11195)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/202287.html**](https://www.secpulse.com/archives/202287.html)

Tags: [HVV](https://www.secpulse.com/archives/tag/hvv)、[IP](https://www.secpulse.com/archives/tag/IP)、[分析](https://www.secpulse.com/archives/tag/%E5%88%86%E6%9E%90)、[工具](https://www.secpulse.com/archives/tag/%E5%B7%A5%E5%85%B7)、[扫描](https://www.secpulse.com/archives/tag/%E6%89%AB%E6%8F%8F)

点赞：
3
[评论：0](#goComment)
收藏：
1

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![内网信息搜集神器—searchall](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1693463314861-300x167.png)

  内网信息搜集神器—searc…](https://www.secpulse.com/archives/203203.html "详细阅读 内网信息搜集神器—searchall")
* [![ASCII码-shellcode的技巧](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/713a80691f4c498de82128db1311f08-300x234.png)

  ASCII码-shellcode的技巧](https://www.secpulse.com/archives/203130.html "详细阅读 ASCII码-shellcode的技巧")
* [![一次暴露面全开的红帽渗透测试【getshell】](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/08/1691635073413-300x186.png)

  一次暴露面全开的红帽渗透测试【getsh…](https://www.secpulse.com/archives/202971.html "详细阅读 一次暴露面全开的红帽渗透测试【getshell】")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/5eb0c688d96210e1378ccc6de9c6f6ef.png)](https://www.secpulse.com/newpage/author?author_id=11195aaa) | [Ms08067安全实验室 ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng0.png)](https://www.secpulse.com/newpage/author?author_id=11195) | |
| 文章数：51 | 积分： 154 |
| 已出版《Web安全攻防》《内网安全攻防》《Python安全攻防》《JAVA代码安全审计（入门篇）》等书 | |

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

[EISS-2020企业信息安全峰会之上海站 11.27](https://open.weixin.qq.com/connect/oauth2/authorize?appid=wx187be17d5a2961cf&redirect_uri=httpsww...