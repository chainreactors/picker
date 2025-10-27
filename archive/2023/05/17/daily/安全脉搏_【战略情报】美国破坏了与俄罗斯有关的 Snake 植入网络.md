---
title: 【战略情报】美国破坏了与俄罗斯有关的 Snake 植入网络
url: https://www.secpulse.com/archives/200437.html
source: 安全脉搏
date: 2023-05-17
fetch_date: 2025-10-04T11:37:09.044801
---

# 【战略情报】美国破坏了与俄罗斯有关的 Snake 植入网络

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

# 【战略情报】美国破坏了与俄罗斯有关的 Snake 植入网络

[资讯](https://www.secpulse.com/archives/category/news)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-05-16

10,624

**概述**

**2023年5月9日，美国网络安全和基础设施安全局 (CISA) 发布了一份名为“猎杀俄罗斯情报“Snake”恶意软件”的警报 ，**其中包含有关 Snake 植入程序的技术细节。Snake 被称为“最复杂的网络间谍工具”，是俄罗斯国家资助的名为Turla （又名 Iron Hunter、Secret Blizzard、SUMMIT、Uroburos、Venomous Bear 和 Waterbug）的组织的杰作，该恶意软件由俄罗斯联邦安全局 (FSB) 的第 16 中心设计并用于针对敏感目标的网络间谍活动。**美国政府宣布已经破坏了受 Snake 恶意软件危害的计算机的点对点 (P2P) 网络。**

美国司法部发布的新闻稿说，司法部宣布完成法院授权的代号为 “MEDUSA ”的行动，以破坏被称为“Snake”的复杂恶意软件破坏的全球点对点 (P2P) 计算机网络，近 20 年来，这个在法庭文件中被称为“ Turla ”的单位使用 Snake 恶意软件的版本从至少 50 个国家/地区的数百个计算机系统中窃取敏感文件，这些计算机系统属于北大西洋公约组织 (北约）成员国政府、记者和俄罗斯联邦感兴趣的其他目标。

美国司法部长Merrick Garland在一份声明中说：“司法部与我们的国际合作伙伴一起，已经拆除了一个受恶意软件感染的计算机全球网络，俄罗斯政府近二十年来一直使用这些计算机进行网络间谍活动，包括针对我们的北约盟国。我们将继续加强集体防御，以应对俄罗斯政权破坏美国和我们盟国安全等破坏稳定的努力。”

**分析**

**1、Snake的目标是有目的和战术性的。**

Snake的相关基础设施已经在北美、南美、欧洲、非洲、亚洲和澳大利亚等50 多个国家/地区确定了，FSB 使用 Snake 从政府网络、研究机构和记者等高优先级目标收集敏感情报。例如，FSB 参与者使用 Snake 从北大西洋公约组织 (NATO) 国家的受害者那里访问和窃取敏感的国际关系文件以及其他外交通信。美国境内的受害行业包括教育、小型企业和媒体机构，以及关键基础设施行业，如政府设施、金融服务、关键制造和通信。虽然Snake的攻击目标并没有明确指向中国，但是中国的政府机构、军事机构、能源公司、金融机构等重要领域仍然可能成为Snake的攻击目标，这对中国的重要领域构成潜在威胁。

**2、Snake 使用多种机制获取用户凭证 。**

FSB 通常将 Snake 部署到网络上面向外部的基础设施节点，并从那里使用内部网络上的其他工具和 TTP 来执行额外的利用操作。在获得并巩固进入目标网络后，FSB 通常会枚举网络并努力获取管理员凭据和访问域控制器。Snake不会部署重量级的植入程序，它们依赖于网络内部的凭据和轻量级远程访问工具。说明 Snake喜欢轻量级的工具，在网络中保持最小的存在并避免在横向移动时被发现。

**3、Snake 采用手段在其主机组件和网络通信中实现罕见的隐身水平。**

Snake在这两种情况下都是用了内核模块。所有已知的 Snake Windows 版本都使用隐藏存储机制来隐藏主机组件。Snake 的网络通信被加密、分段，并使用跨越通用网络协议的自定义方法发送。Snake 的内核模块用于区分 Snake 流量和合法客户端流量，允许植入物在 Snake P2P 网络中充当服务器，而无需打开任何新端口，这使检测工作变得非常复杂。Snake的隐藏机制技术提醒我们在软件设计和实现中注重隐身技术，提高软件安全性和隐蔽性，同时也为我们国家发现其他恶意软件植入提供了新思路。

**4、Snake 的内部技术架构允许轻松合并新的或替换的组件。**

Snake中的关键通路由松散耦合的组件组成，这种结构允许Snake 为同一目的使用多个不同的组件，还可以根据环境考虑选择特定的组件。Snake协议栈中从传输加密层到命令处理层，只要接口正确，就会对传输层保持完全不可知。这种架构允许新的通信协议代被破坏的通信协议时，不需要对代码库进行更改。最后，这种设计有助于开发在不同主机操作系统上运行的完全可互操作的 Snake 植入程序。已经观察到针对 Windows、MacOS 和 Linux 操作系统的可互操作 Snake 植入。Snake内部技术架构的灵活性和可扩展性，使得它可以在受感染的计算机上长期存在并难以被检测和清除。同时也反映出来我们国家在网络安全方面的薄弱环节，也为我们国家研发新技术提供了新方向。

**5、Snake 的设计展现了专业的软件工程设计和实施****。**

Snake 开发人员用C语言实现了程序的复杂设计，几乎没有任何错误。Snake采用了微服务架构，这种架构的优点在于可以将应用程序拆分成多个小型服务，每个服务都可以独立部署、扩展和升级，从而提高应用程序的灵活性和可扩展性；Snake的设计采用了模块化的方式，将不同的功能模块分开实现，这样可以降低代码的耦合度，提高代码的可维护性和可重用性；Snake的设计和实现非常注重安全性，采用了多种技术手段来保证自身的安全性和隐蔽性，这提醒我们在软件工程设计和实现中，安全性应该是一个重要的考虑因素；

**6、美国FBI 开发PERSEUS 工具来应对“Snake”。**FBI 通过监控 Snake 网络和分析 Snake 恶意软件收集的信息，开发了一个名为 PERSEUS 的工具，它与特定计算机上的 Snake 恶意软件植入物建立通信会话，并发出命令使 Snake 植入物自行禁用而不影响计算机。

**参考链接**

https://www.cisa.gov/news-events/cybersecurity-advisories/aa23-129a

**本文作者：[Further\_eye](newpage/author?author_id=9241)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/200437.html**](https://www.secpulse.com/archives/200437.html)

Tags: [Secret Blizzard](https://www.secpulse.com/archives/tag/secret-blizzard)、[Snake](https://www.secpulse.com/archives/tag/snake)、[SUMMIT](https://www.secpulse.com/archives/tag/summit)、[Turla](https://www.secpulse.com/archives/tag/turla)、[Turla （又名 Iron Hunter](https://www.secpulse.com/archives/tag/turla-%EF%BC%88%E5%8F%88%E5%90%8D-iron-hunter)、[Uroburos](https://www.secpulse.com/archives/tag/uroburos)、[Venomous Bear](https://www.secpulse.com/archives/tag/venomous-bear)、[Waterbug](https://www.secpulse.com/archives/tag/waterbug)、[猎杀俄罗斯情报](https://www.secpulse.com/archives/tag/%E7%8C%8E%E6%9D%80%E4%BF%84%E7%BD%97%E6%96%AF%E6%83%85%E6%8A%A5)

点赞：
3
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![对Windows Rootkit的细粒度动态分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2015/03/rootkit.png)](https://www.secpulse.com/archives/5542.html "详细阅读 对Windows Rootkit的细粒度动态分析")
* [![靶场战神为何会陨落？](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2024/09/VCG41N952384318.png)

  靶场战神为何会陨落？](https://www.secpulse.com/archives/205395.html "详细阅读 靶场战神为何会陨落？")
* [![《内网安全攻防》姊妹篇《红队之路》重磅上市！（文末赠书）](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-204824-1711610670-210x140.png)

  《内网安全攻防》姊妹篇《红队之路》重磅上](https://www.secpulse.com/archives/204824.html "详细阅读 《内网安全攻防》姊妹篇《红队之路》重磅上市！（文末赠书）")

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

[全球敏捷运维峰...