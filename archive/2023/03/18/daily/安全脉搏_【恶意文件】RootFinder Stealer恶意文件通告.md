---
title: 【恶意文件】RootFinder Stealer恶意文件通告
url: https://www.secpulse.com/archives/197814.html
source: 安全脉搏
date: 2023-03-18
fetch_date: 2025-10-04T09:56:20.208245
---

# 【恶意文件】RootFinder Stealer恶意文件通告

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

# 【恶意文件】RootFinder Stealer恶意文件通告

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-03-17

12,869

**恶意家族名称：**

RootFinder

**威胁类型：**

信息窃取

**简单描述：**

RootFinder 是一款基于 .NET 的窃密工具，该程序使用了 .NET Reactor进行多次混淆，运行时可以窃取主机信息和数十款浏览器的敏感信息、FTP账号密码等数据。

**恶意文件分析**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197814-1679034253.gif)

**恶意事件描述**

近日，深信服深盾终端实验室在运营工作中捕获到一款新型信息窃取病毒，该病毒由 .NET 语言编写，套用了开源软件 StormKitty 的部分代码。经过分析发现该病毒功能尚不完善且手法相对简单，该窃密程序已在黑客论坛售卖，后续可能还会持续更新。

大多数计算机感染源于用户打开恶意电子邮件附件、点击有害链接或从不可信的来源下载文件。攻击者还使用特洛伊木马、虚假安装程序、虚假软件更新和类似方法来诱导用户并感染他们的计算机。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197814-1679034254.gif)

**恶意事件分析**

**MITRE ATT&CK**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197814-1679034254.png)

**解混淆**

首先查看文件的信息，发现是.NET写的32位程序，拖进dnspy发现存在混淆，使用de4dot经过多次解混淆之后查看该文件：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197814-1679034255.png)

**收集ARP信息**

首先通过cmd执行arp -a命令收集主机arp信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197814-1679034269.png)

**收集FileZilla信息**

通过读取 recentservers.xml 和 sitemanager.xml 两个文件的内容获取ftp服务器账号密码。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197814-1679034273.png)

之后将收集到的信息写入到C:WondowsHosts.txt中。

**收集主机信息**

使用通过WMI接口获取计算机CPU和显卡信息，之后与主机名，用户名进行拼接计算MD5：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197814-1679034275.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197814-1679034276.png)

收集主机反病毒软件信息

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197814-1679034278.png)

此外还包括：系统语言、公网IP、系统时间、操作系统和系统版本、内存大小、磁盘系列号、BIOS信息、MAC地址、子网扫描、内网IP。

**收集浏览器信息**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197814-1679034281.png)

包括Opera、Google Chrome、MapleStudio ChromePlus、Iridium、7Start、CentBrower、Chedot、Vivaldi、Kometa、Element Browser、Epic Privacy Brower、uCozMedia、Chromium、Sleipnir、Citrio、Coowon、liebao、QIP Surf、Orbitum、Comodo、Amigo、Torch、Yandex、360Browser、Maxthon3、K-Melon、Sputnik、Nichrome、CocCoc、Uran、Chromodo、Atom、Brave-Browser、Edge，FireFox、WaterFox、Thunderbird、IceGragon、Cyberfox、BlackHaw、Pale Moon等众多浏览器保存的账号密码、cookie、搜索历史、信用卡等信息，此时收集到的信息将被保存到C:Windows目录下的众多txt中。

**发送数据**

收集到的信息将以明文的形式发送到 Telegram 机器人中：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197814-1679034283.png)

文件同样会被使用POST的方式发向Telegram，随后删除保存的txt文件

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-197814-1679034284.png)

病毒运营者自述可以获取游戏客户端（Steam，Minecraft）账号，但在分析调试的时候暂未发现相关代码调用。

**本文作者：[Further\_eye](newpage/author?author_id=9241)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/197814.html**](https://www.secpulse.com/archives/197814.html)

Tags: [.net](https://www.secpulse.com/archives/tag/.net)、[RootFinder](https://www.secpulse.com/archives/tag/rootfinder)、[信息窃取](https://www.secpulse.com/archives/tag/%E4%BF%A1%E6%81%AF%E7%AA%83%E5%8F%96)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![一次授权的未授权漏洞验证测试](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1682057465997-300x184.png)

  一次授权的未授权漏洞验证测试](https://www.secpulse.com/archives/199332.html "详细阅读 一次授权的未授权漏洞验证测试")
* [![PyPI供应链攻击频发，W4SP盯上用户的私密数据](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/09/1663749958357-300x160.png)

  PyPI供应链攻击频发，W4SP盯上用户…](https://www.secpulse.com/archives/187483.html "详细阅读 PyPI供应链攻击频发，W4SP盯上用户的私密数据")
* [![红蓝对抗之PC端wechat信息窃取](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/07/16583869571-300x192.png)

  红蓝对抗之PC端wechat信息窃取](https://www.secpulse.com/archives/183912.html "详细阅读 红蓝对抗之PC端wechat信息窃取")

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
| [![]( https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2022/08/16/9f4b1a0a8978eebf651bfe827b4d307a-300x255.jpeg)](https://www.secpulse.com/newpage/author?author_id=9241aaa) | [Further\_eye ![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)](https://www.secpulse.com/newpage/author?author_id=9241) | |
| 文章数：319 | 积分： 2105 |
| 深信服科技旗下安全实验室，致力于网络安全攻防技术的研究和积累，深度洞察未知网络安全威胁，解读前沿安全技术。 | |

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

[全球敏捷运维峰会（Gdevop...