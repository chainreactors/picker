---
title: 【高级威胁追踪】利用Google Ads传播Aurora窃密木马
url: https://www.secpulse.com/archives/196658.html
source: 安全脉搏
date: 2023-02-25
fetch_date: 2025-10-04T08:02:29.345667
---

# 【高级威胁追踪】利用Google Ads传播Aurora窃密木马

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

# 【高级威胁追踪】利用Google Ads传播Aurora窃密木马

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[Further\_eye](https://www.secpulse.com/newpage/author?author_id=9241)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2023-02-24

12,734

**概述**

恶意Google Ads是攻击者传播恶意软件常见攻击手段之一，在搜索引擎上搜索任何流行免费软件的时候，受害者很可能会被诱骗或者重定向到虚假的软件网站，这些虚假网站有些被攻击者制作成与真实软件相同的网页，其中包含下载恶意软件的链接，有些直接诱骗受害者到某个指定的下载连接去下载恶意软件。

攻击者会使用恶意Google Ads对特定的受害者进行攻击，例如可以伪装成一些特定企业人群使用的软件，比方开发工具、画图工具、办公软件等，对这些人员进行前期的窃密攻击，然后将获取到的一些特定受害者合法凭证进行筛选之后，再转卖给其他攻击团队，进行后续的APT攻击活动或定向勒索攻击活动等，深信服APT研究团队一直在密切关注研究全球窃密攻击活动，发现近期**攻击者使用Google Ad攻击活动非常频繁，覆盖了很多常用的工具和软件等，传播了多个窃密木马或间谍软件等，在样本免杀技术上使用了“增肥”技术，攻击样本高达几百M，这些窃密活动有可能是在为后期进行APT攻击活动或勒索病毒定向攻击活动收集相关的合法凭证信息。**

打你七寸上了 ？

**分析**

深信服APT研究团队针对其中一个攻击样本进行了深入的分析，该样本伪装成Python安装程序传播Aurora窃密木马,有可能是针对企业Python开发人员进行的攻击活动，窃取这些开发人员的重要信息，然后对这些信息进行筛选，将其中一些有效的合法凭证信息，例如浏览器保存的各种帐号密码信息等，转卖给其他攻击团队进行APT攻击或定向勒索攻击等。

1.伪装成的Python安装程序压缩包，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196658-1677217360.png)

2.解压之后，一般会有一堆正常的文件和一个几百M的安装包程序，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196658-1677217361.png)

3.样本使用了“增肥”免杀技术，在样本的最后填充了大量的空数据，以逃避杀毒软件的检测，对样本进行修复之后，该样本为一个自解密程序，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196658-16772173611.png)

4.该自解压程序包含一个Windows压缩CAB资源文件CABINET，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196658-1677217362.png)

5.对该资源文件进行解压缩之后，会生成一个几百M的文件，对生成的文件进行修复之后，是一个NET程序，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196658-1677217363.png)

6.该NET程序会从远程服务器下载恶意数据解密之后加载执行，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196658-1677217364.png)

7.下载的恶意数据通过Base64解密之后，是一个混淆过的NET程序，对该NET程序动态调试获取核心Payload代码，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196658-1677217365.png)

8.通过分析最后的Payload代码，发现是Aurora窃密木马，该窃密木马于2022年4月被首次在俄语地下论坛上作为恶意软件即服务(MaaS)进行宣传，是一种基于Golang语言编写的窃密木马，具有下载和远程访问功能，能够窃密多个浏览器、加密货币钱包、本地系统数据等，通过WMIC运行多个命令来收集基本的主机信息、桌面图像信息等，并将这些发送到远程服务器，对该窃密木马进行分析，使用脚本还原了该程序的相关符号表信息，更利用逆向分析人员对样本进行逆向分析，样本符号表还原之后，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196658-1677217366.png)

9.动态调试样本，远程服务器IP地址为：185.106.93.135，如下所示：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-196658-1677217368.png)

**总结**

深信服APT研究团队提醒客户，一定要在正规的官方渠道上下载正规软件，检测网站是否是伪装的虚拟软件网站，以及下载的软件相关数字签名等信息是否正常，使用Google Ads传播各种窃密木马，获取受害者的合法凭证，属于前期信息收集准备工作之一，通过窃密木马获取受害者主机上的个人合法凭证信息，利用这些合法凭证信息获利，很多APT攻击组织或勒索病毒攻击组织会直接购买这些合法凭证，然后进行下一步的APT攻击或定向勒索攻击活动等。

深信服APT研究团队专注全球高级威胁事件的跟踪与分析，拥有一套完善的自动化分析溯源系统以及外部威胁监控系统，能够快速精准的对 APT 组织使用的攻击样本进行自动化分析和关联，同时积累并完善了几十个 APT 以及网络犯罪威胁组织的详细画像，并成功帮助客户应急响应处置过多个 APT 及网络犯罪威胁组织攻击事件，未来随着安全对抗的不断升级，威胁组织会研究和使用更多新型的 TTP，深信服APT研究团队会持续监控，并对全球发现的新型安全事件进行深入分析与研究。

**ioc**

**HASH**

c2e71baefc4efbdb667f3a5c153be3d3d2521d4b856f5381a96a6a272bc21ee8

58a4ebf92461eecd3ba5aa6fb1f5ad1a1ea721b288236a2aa3bf6e29b0138b6d

ce481fe7ba21d32a0307f826f42e6b7f161104463b76f4bfd2c12d7186e2e806

4a5ea3ec8404e004b5217d2f618755c6de56b9979213aea9bfc73b5a6759aba8

**IP**

185.106.93.135

**URL**

http://comicmaster.org.uk/img/css/design/fabric/bo/Spocvarkazz.dll

**参考链接**

https://malpedia.caad.fkie.fraunhofer.de/details/win.aurora\_stealer

**本文作者：[Further\_eye](newpage/author?author_id=9241)**

**本文为安全脉搏专栏作者发布，转载请注明：**[**https://www.secpulse.com/archives/196658.html**](https://www.secpulse.com/archives/196658.html)

Tags: [Aurora](https://www.secpulse.com/archives/tag/aurora)、[Google Ads](https://www.secpulse.com/archives/tag/google-ads)、[Python](https://www.secpulse.com/archives/tag/python)、[窃密木马](https://www.secpulse.com/archives/tag/%E7%AA%83%E5%AF%86%E6%9C%A8%E9%A9%AC)

点赞：
0
[评论：0](#goComment)
收藏：
0

*新浪微博
QQ空间
微信扫一扫*

### 相关文章

* [![PyPI恶意存储库fshec2攻击分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/06/1686552005955-300x198.png)

  PyPI恶意存储库fshec2攻击分析](https://www.secpulse.com/archives/201724.html "详细阅读 PyPI恶意存储库fshec2攻击分析")
* [![【Python+Java】Burpsuite插件开发](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/05/1683612811183-300x164.png)

  【Python+Java】Burpsui…](https://www.secpulse.com/archives/200103.html "详细阅读 【Python+Java】Burpsuite插件开发")
* [![WECHAT二维码闪退分析](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/2023/04/1683184162259-300x201.png)

  WECHAT二维码闪退分析](https://www.secpulse.com/archives/199777.html "详细阅读 WECHAT二维码闪退分析")

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

[Gdevops 全球敏捷运维峰...