---
title: CTF中的神兵利刃-foremost工具之文件分离
url: https://www.secpulse.com/archives/196849.html
source: 安全脉搏
date: 2023-03-03
fetch_date: 2025-10-04T08:30:56.558207
---

# CTF中的神兵利刃-foremost工具之文件分离

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

# CTF中的神兵利刃-foremost工具之文件分离

[CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)

[青少年CTF](https://www.secpulse.com/newpage/author?author_id=49279)

2023-03-02

16,624

CTF中的神兵利刃-foremost工具之文件分离

# 原理

Foremost可以依据文件内的文件头和文件尾对一个文件进行分离，或者识别当前的文件是什么文件。比如拓展名被删除、被附加也仍然可以对其分离。

[![图片11.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/图片111.png "图片111.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/%E5%9B%BE%E7%89%87111.png)

# 使用

安装：

需要使用这个工具，首先我们需要安装他，在Linux系统中，我们可以直接apt install foremost中进行安装。

foremost file

这样会直接指定一个文件进行分析，然后输出到output文件夹下

foremost -I file -o output

这里 -o 后面的参数就是输出的路径，-i则是指定一个文件，当然这个-i你也可以去掉（做题速度很关键）

当然，foremost的使用肯定不止这么一点点，不然也不会成为“神器”被我们放到这里。

我们使用foremost -h之后，会有下面的文档：

**foremost version 1.5.7 by Jesse Kornblum, Kris Kendall, and Nick Mikus.**

**$ foremost [-v|-V|-h|-T|-Q|-q|-a|-w-d] [-t <type>] [-s <blocks>] [-k <size>]**

**[-b <size>] [-c <file>] [-o <dir>] [-i <file]**

**-V  - display copyright information and exit**

**-t  - specify file type.  (-t jpeg,pdf ...)**

**-d  - turn on indirect block detection (for UNIX file-systems)**

**-i  - specify input file (default is stdin)**

**-a  - Write all headers, perform no error detection (corrupted files)**

**-w  - Only write the audit file, do not write any detected files to the disk**

**-o  - set output directory (defaults to output)**

**-c  - set configuration file to use (defaults to foremost.conf)**

**-q  - enables quick mode. Search are performed on 512 byte boundaries.**

**-Q  - enables quiet mode. Suppress output messages.**

**-v  - verbose mode. Logs all messages to screen**

**对其翻译之后，内容有下：**

-V-显示版权信息并退出

-t-指定文件类型。（-t jpeg，pdf…）

-d-启用间接块检测（对于UNIX文件系统）

-i-指定输入文件（默认为stdin）

-a-写入所有标头，不执行错误检测（损坏的文件）

-w-仅写入审核文件，不将任何检测到的文件写入磁盘

-o-设置输出目录（默认为输出）

-c-设置要使用的配置文件（默认为forest.conf）

-q-启用快速模式。在512字节边界上执行搜索。

-Q-启用静音模式。抑制输出消息。

-v-冗余模式。将所有消息记录到屏幕。

其实我们上面提到的主要使用方法已经能满足我们日常使用了，所以这些复杂的我们就只在这里说明。

# 补充

是的，我们QQ群里的机器人也已经加入了foremost功能了！

[![图片21.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/图片211.png "图片211.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/%E5%9B%BE%E7%89%87211.png)

对于需要分离的文件我们只需要按照如下的过程操作即可：

[![图片3.png](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/图片31.png "图片31.png")](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/%E5%9B%BE%E7%89%8731.png)

接着我们就能在返回的报告中看到我们的结果哦！

**本文作者：[青少年CTF](newpage/author?author_id=49279)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/196849.html**](https://www.secpulse.com/archives/196849.html)

Tags: [ctf](https://www.secpulse.com/archives/tag/ctf)、[foremost](https://www.secpulse.com/archives/tag/foremost)、[工具](https://www.secpulse.com/archives/tag/%E5%B7%A5%E5%85%B7)

点赞：
3
[评论：1](#goComment)
收藏：
0

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

评论  (1)

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

[EISS-2020企业信息安全峰会之北京站 | 7.31（周五线上）](http://www.anquanjia.ne...