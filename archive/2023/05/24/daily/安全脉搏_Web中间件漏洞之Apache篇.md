---
title: Web中间件漏洞之Apache篇
url: https://www.secpulse.com/archives/200864.html
source: 安全脉搏
date: 2023-05-24
fetch_date: 2025-10-04T11:37:49.988775
---

# Web中间件漏洞之Apache篇

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

# Web中间件漏洞之Apache篇

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[第59号实验室](https://www.secpulse.com/newpage/author?author_id=49738)

2023-05-23

27,852

# Apache简介

Apache 是世界使用排名第一的 Web 服务器软件。

它可以运行在几乎所有广泛使用的计算机平台上，由于其跨平台和安全性被广泛使用，是最流行的 Web 服务器端软件之一。

它快速、可靠并且可通过简单的 API 扩充，将 Perl/Python 等解释器编译到服务器中。

# 解析漏洞

漏洞介绍及成因

Apache 文件解析漏洞与用户的配置有密切关系，严格来说属于用户配置问题。

Apache 文件解析漏洞涉及到一个解析文件的特性：

Apache 默认一个文件可以有多个以点分隔的后缀，当右边的后缀无法识别（不在 mime.tyoes 内），则继续向左识别，当我们请求这样一个文件：

shell.php.xxx.yyy

yyy ->无法识别，向左

xxx ->无法识别，向左

php ->发现后缀是 php，交给 php 处理这个文件

漏洞复现

上传一个后缀名为360的php文件

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image31.png "image31.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image31.png)

正常解析

漏洞修复

将 AddHandler application/x-httpd-php .php 的配置文件删除。

# 目录遍历

漏洞介绍及成因

由于配置错误导致的目录遍历

漏洞复现

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image32.png "image32.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image32.png)

漏洞修复

修改 apache 配置文件 httpd.conf

找到 Options +Indexes +FollowSymLinks +ExecCGI 修改成 Options -Indexes+FollowSymLinks +ExecCGI 并保存；

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image33.png "image33.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image33.png)

[![image.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image34.png "image34.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/image34.png)

**本文作者：[第59号实验室](newpage/author?author_id=49738)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/200864.html**](https://www.secpulse.com/archives/200864.html)

点赞：
2
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![这你敢信，复习PHP意外搞出一个免杀WebShell](https://www.yijinglab.com/guide-img/d9634e2f-3b66-42e7-8279-c0877cdd70e5/5e54ae58-65a2-4f71-99db-5eb61b292b6f.png)

  这你敢信，复习PHP意外搞出一个免杀We](https://www.secpulse.com/archives/206392.html "详细阅读 这你敢信，复习PHP意外搞出一个免杀WebShell")
* [![Windows远程桌面的奇技淫巧](https://m-1254331109.cos.ap-guangzhou.myqcloud.com/202407081520540.png)

  Windows远程桌面的奇技淫巧](https://www.secpulse.com/archives/205196.html "详细阅读 Windows远程桌面的奇技淫巧")
* [![后门函数技术在二进制对抗中的应用](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/09/VCG211334174968.png)

  后门函数技术在二进制对抗中的应用](https://www.secpulse.com/archives/205266.html "详细阅读 后门函数技术在二进制对抗中的应用")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1a3b6dd6d88ce8675bf30bc03975bab1_ce6692cb75dd2998ff4d70b9690c28a5.jpeg)](https://www.secpulse.com/newpage/author?author_id=49738aaa) | [第59号实验室](https://www.secpulse.com/newpage/author?author_id=49738) | |
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
* [黑白网](http://www.heibai.org)
* |
* [ms08067](http://www.ms08067.com/)
* |
* [华盟网](https://www.77169.net/)
* |
* [攻防世界](https://adworld.xctf.org.cn)
* |
* [安世加](http://www.anquanjia.net.cn/)
* |
* [kkQa](https://kkqa.net/)
...