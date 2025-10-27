---
title: 小皮面板RCE复现
url: https://www.secpulse.com/archives/195420.html
source: 安全脉搏
date: 2023-02-08
fetch_date: 2025-10-04T05:56:31.528774
---

# 小皮面板RCE复现

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

# 小皮面板RCE复现

[漏洞](https://www.secpulse.com/archives/category/vul)

[黑客前沿](https://www.secpulse.com/newpage/author?author_id=49332)

2023-02-07

9,019

免责声明：文中提到的所有技术、思路和工具仅供以安全为目的的学习交流使用，任何人不得将其用于非法用途，否则后果自行承担！

### 漏洞成因

小皮面板登录失败时会将失败的用户名记录，并输出到面板首页，而这一过程没有对用户输入的字符做过滤，导致存在任意XSS，攻击者可以利用小皮面板自带的计划任务功能配合XSS实现RCE。

### 环境搭建

小皮官网下载面板，在本地安装。注意是面板，不是phpstudy。安装完成后会自动弹出管理端地址和账号密码的文本。 ![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)

[![xp.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/xp-1024x362.png "xp-1024x362.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/xp.png)

### 漏洞测试

先测试一下xss漏洞，用户名输入`<script>alert(1)</script>`，密码任意，验证码输入正确，点击登录。 ![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)

[![alert.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/alert.png "alert.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/alert.png)

然后登录管理员账号，页面弹窗，证明漏洞存在。

[![tanchuang.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/tanchuang-1024x404.png "tanchuang-1024x404.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/tanchuang.png) ![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)

### RCE复现

脚本参考的是ZAC大佬编写的，感谢大佬。

利用XSS调用我们事先准备好的命令执行脚本。这里执行的命令是`echo hkqy > web目录/1.txt` ![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)

[![testjs.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/testjs.png "testjs.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/testjs.png)

登录管理员账号，成功写入文件。 ![](https://www.secpulse.com/wp-content/themes/secpulse2017/js/editor/themes/default/images/spacer.gif)

[![txt.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/txt-1024x407.png "txt-1024x407.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/txt.png)

实际应用可以写webshell，反弹，或者上马等，根据自己喜好。

【黑客前沿】公众号回复 phpstudy 获取脚本

**本文作者：[黑客前沿](newpage/author?author_id=49332)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/195420.html**](https://www.secpulse.com/archives/195420.html)

Tags: [RCE复现](https://www.secpulse.com/archives/tag/rce%E5%A4%8D%E7%8E%B0)、[XSS](https://www.secpulse.com/archives/tag/XSS)、[小皮面板](https://www.secpulse.com/archives/tag/%E5%B0%8F%E7%9A%AE%E9%9D%A2%E6%9D%BF)

点赞：
0
[评论：0](#goComment)
收藏：
0

积分 20
*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![【零基础】SRC实用漏洞挖掘技巧-附5个漏洞实例解析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-200077-1683602931-300x191.png)

  【零基础】SRC实用漏洞挖掘技巧-附5个…](https://www.secpulse.com/archives/200077.html "详细阅读 【零基础】SRC实用漏洞挖掘技巧-附5个漏洞实例解析")
* [![Java Struts2系列的XSS漏洞（S2-002）](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1678085894201-300x176.png)

  Java Struts2系列的XSS漏洞…](https://www.secpulse.com/archives/197010.html "详细阅读 Java Struts2系列的XSS漏洞（S2-002）")
* [![WebSocket 测试入门篇](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196038-1676613912-300x160.png)

  WebSocket 测试入门篇](https://www.secpulse.com/archives/196038.html "详细阅读 WebSocket 测试入门篇")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/16752369406501.jpeg)](https://www.secpulse.com/newpage/author?author_id=49332aaa) | [黑客前沿](https://www.secpulse.com/newpage/author?author_id=49332) | |
| 文章数：6 | 积分： 40 |
| 欢迎关注我的个人公众号：黑客前沿 | |

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

![安全问答社区](https...