---
title: 疑似 Kasablanka 组织针对阿塞拜疆及乌兹别克斯坦地区的攻击行动分析
url: https://www.secpulse.com/archives/196928.html
source: 安全脉搏
date: 2023-03-04
fetch_date: 2025-10-04T08:36:26.302596
---

# 疑似 Kasablanka 组织针对阿塞拜疆及乌兹别克斯坦地区的攻击行动分析

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

# 疑似 Kasablanka 组织针对阿塞拜疆及乌兹别克斯坦地区的攻击行动分析

[脉搏文库](https://www.secpulse.com/archives/category/category/secdocs)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-03-03

10,102

**概述**

在 2022 及 2023 年期间，深信服蓝军高级威胁（APT）团队监测到疑似Kasablanka 组织的多次钓鱼攻击活动，针对目标主要集中在中东、中亚以及东欧地区，其主要目标为乌兹别克斯坦及阿塞拜疆的外交及其他政府部门，下图为相关钓鱼攻击行动时间线。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832266.png)

其钓鱼攻击相比其他钓鱼略有不同，其通过向目标发送恶意宏文档，宏文档通过命令调用浏览器打开钓鱼页面诱导目标数据输入相关凭证，其投递的宏文档如下。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832267.png)

除了通过钓鱼窃取邮箱凭证外，该组织还投递多种木马对目标进行攻击，其木马组件多使用 python 开发并使用 telegram 通信。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832268.png)

在本次事件中还观察到该组织使用了名为 “123.hta” 的载荷进行攻击，该载荷使用多重混淆的脚本命令执行下载功能。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832269.png)

对该脚本代码进行多次解密，其主要目的为下载其他组件 `“https://docs.az-link.email/Dovlet_Proqram13062022.rar”`

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832271.png)

**分析**

在本次攻击活动中，我们还发现其构建了使用telebot通信的木马文件 “https://docs.az-link.email/Dovlet\_Proqram13062022.rar”，伪造相关国家计划文件诱导目标执行，该组件由 python 开发并使用 pyinstaller 打包，文件相关信息如下。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832273.png)

该组件首先会创建注册表自启动，并注册对应的功能信息，其功能包含命令执行（“/run”）与文件下载（“/download”）。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832274.png)

根据其中的 telebot token，找到对应的 telegram 账号信息如下，其账号名称为 “baku11\_bot”。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832275.png)

在进行相关搜索时发现其他疑似同类型账号 “Baku\_11\_bot” 与 “Baku1111\_bot”。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832280.png)

在关联分析时还发现其他相同组件svchostc.exe “fd7fe71185a70f281545a815fce9837453450bb29031954dd2301fe4da99250d”，其通信的 telebot 账号如下。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832283.png)

此外，我们还发现疑似该组织使用的反弹 shell 木马文件 “Qo\_ma.exe”，其关联信息如下图。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832284.png)

该反弹 shell 木马文件详细信息如下表。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832285.png)

该文件功能较为单一，就只有简单的 CMD 反弹 shell 功能，连接 C2 为 “168.100.8.36:443”。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832286.png)

另外还发现新的 telebot 信息窃密组件 “02.08.2022.exe”，该远控由 python 开发及 Nuitka 打包以加强反分析能力，其相关信息如下表。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832288.png)

该工具使用 Nuitka 打包，增加了分析人员的分析难度，其主要功能包括浏览器密码信息窃取等功能。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832289.png)

该组件与友商已披露的疑似该组织基础设施存在一定的关联。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832290.png)

**总结**

从该组织的攻击动机分析，其具有强烈的信息收集和间谍活动特征，很符合国家级背景支撑的黑客组织。从其使用的工具主要分析看，攻击行动中大量使用 python编写及 telegram 通信的木马，telegram 通信类木马在网络犯罪论坛中一直保持着较为活跃的状态，组件开发人员具有强烈的黑产从业人员气息。

深信服蓝军高级威胁（APT）团队专注全球高级威胁事件的跟踪与分析，拥有一套完善的自动化分析溯源系统以及外部威胁监控系统，能够快速精准的对 APT 组织使用的攻击样本进行自动化分析和关联，同时积累并完善了几十个 APT 以及网络犯罪威胁组织的详细画像，成功帮助客户应急响应处置过多起 APT 及网络犯罪威胁组织攻击事件，未来随着安全对抗的不断升级，威胁组织会研究和使用更多新型的TTP，深信服高级威胁团队会持续监控，并对全球发现的新型安全事件进行深入分析与研究。

**ioc**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-1677832291.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196928-16778322911.png)

**参考链接**

1、https://www.securesoftcorp.com/es/web/guest/w/novedades/ss\_alerta070 2、https://mp.weixin.qq.com/s/b0FSKQ6D3MvlA8yX3v4IUg 3、https://www.zscaler.com/blogs/security-research/dynamic-approaches-seen-avemarias-distribution-strategy

**本文作者：[Further\_eye](newpage/author?author_id=9241)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/196928.html**](https://www.secpulse.com/archives/196928.html)

Tags: [Kasablanka](https://www.secpulse.com/archives/tag/kasablanka)、[乌兹别克斯坦](https://www.secpulse.com/archives/tag/%E4%B9%8C%E5%85%B9%E5%88%AB%E5%85%8B%E6%96%AF%E5%9D%A6)、[恶意宏文档](https://www.secpulse.com/archives/tag/%E6%81%B6%E6%84%8F%E5%AE%8F%E6%96%87%E6%A1%A3)、[钓鱼邮件](https://www.secpulse.com/archives/tag/%E9%92%93%E9%B1%BC%E9%82%AE%E4%BB%B6)、[阿塞拜疆](https://www.secpulse.com/archives/tag/%E9%98%BF%E5%A1%9E%E6%8B%9C%E7%96%86)

点赞：
1
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![钓鱼邮件攻击分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1685429063311-300x172.png)

  钓鱼邮件攻击分析](https://www.secpulse.com/archives/201168.html "详细阅读 钓鱼邮件攻击分析")
* [![【恶意文件】AgentTesla 贼心不死，换壳之后卷土重来](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/03/1678350974041-300x185.png)

  【恶意文件】AgentTesla 贼心不…](https://www.secpulse.com/archives/197248.html "详细阅读 【恶意文件】AgentTesla 贼心不死，换壳之后卷土重来")
* [![社会工程学 | cobalstrike批量发送钓鱼邮件方法](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/02/1676358686959-300x224.png)

  社会工程学 | cobalstrike批…](https://www.secpulse.com/archives/195833.html "详细阅读 社会工程学 | cobalstrike批量发送钓鱼邮件方法")

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
| [![]( https...