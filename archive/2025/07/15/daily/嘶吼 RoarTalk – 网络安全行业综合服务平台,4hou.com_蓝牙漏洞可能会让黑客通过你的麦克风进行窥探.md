---
title: 蓝牙漏洞可能会让黑客通过你的麦克风进行窥探
url: https://www.4hou.com/posts/8gyL
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-07-15
fetch_date: 2025-10-06T23:24:16.183013
---

# 蓝牙漏洞可能会让黑客通过你的麦克风进行窥探

蓝牙漏洞可能会让黑客通过你的麦克风进行窥探 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

[![](https://www.4hou.com/sihou/images/new4hou/newlogoss.png)](https://www.4hou.com)

* [首页](https://www.4hou.com)
* [企业中心](https://www.4hou.com/corp/newindex)
* [产业研究院](https://www.4hou.com/real-time)

![](https://www.4hou.com/sihou/images/new4hou/search-icon.png)

[投稿](https://www.4hou.com/contribute)

[登录](https://www.4hou.com/login)
  |
[注册](https://www.4hou.com/register)

* 导读 ▾
* [活动](https://www.4hou.com/newticket)
* [专题](https://www.4hou.com/category/special)
* [图谱](https://www.4hou.com/atlas/index)
* [报告](https://www.4hou.com/new-report-info)
* [嘶票](https://www.4hou.com/tickets)
* [嘶货](https://www.4hou.com/shop)
* [企业查询](https://www.4hou.com/corp/new-search-company)
* [招聘](https://www.4hou.com/recruit)![](https://www.4hou.com/sihou/images/1561626446625934.png)

* [新闻](https://www.4hou.com/category/news)
* [行业](https://www.4hou.com/category/industry)
* [趋势](https://www.4hou.com/category/observation)
* [访谈](https://www.4hou.com/category/people)
* [漏洞](https://www.4hou.com/category/vulnerable)
* [WEB安全](https://www.4hou.com/category/web)
* [业务安全](https://www.4hou.com/category/business)
* [系统安全](https://www.4hou.com/category/system)
* [内网渗透](https://www.4hou.com/category/penetration)
* [勒索软件](https://www.4hou.com/category/typ)
* [安全工具](https://www.4hou.com/category/tools)

# 蓝牙漏洞可能会让黑客通过你的麦克风进行窥探

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-07-14 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)48065

收藏

导语：此外，易受攻击设备的固件可能会被重写，以允许远程代码执行，从而促进能够跨多个设备传播的蠕虫攻击的部署。

安全研究人员发现，来自十家供应商的二十多个音频设备中存在影响蓝牙芯片组的漏洞，可用于窃听或窃取敏感信息。

研究人员证实，来自Beyerdynamic、Bose、Sony、Marshall、Jabra、JBL、Jlab、EarisMax、MoerLabs和Teufel的29款设备受到影响。受影响的产品包括扬声器、耳塞、耳机和无线麦克风。

安全问题可能被利用来接管易受攻击的产品，在某些手机上，连接范围内的攻击者可能能够提取通话记录和联系人。

**窥探蓝牙连接**

在德国举行的TROOPERS安全会议上，网络安全公司ERNW的研究人员披露了Airoha芯片系统（soc）的三个漏洞，这种系统广泛用于真无线立体声（TWS）耳机。

这些问题并不严重，除了物理距离近（蓝牙范围）外，利用它们还需要“高技术技能”。他们收到了以下标识符：

**·**CVE-2025-20700（6.7，中等严重性分数）- GATT服务缺少身份验证

**·**CVE-2025-20701（6.7，中等严重性评分）-缺少蓝牙BR/EDR认证

**·**CVE-2025-20702（7.5，高严重性评分）-自定义协议的关键功能

ERNW研究人员表示，他们创建了一个概念验证漏洞代码，允许他们从目标耳机中读取当前播放的媒体。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20250630/1751255267166149.png "1751255227153912.png")

读取一个易受攻击的Airoha设备上当前播放的歌曲

虽然这样的攻击可能不会带来很大的风险，但利用这三个漏洞的其他场景可能会让威胁者劫持移动电话和音频蓝牙设备之间的连接，并使用蓝牙免提配置文件（HFP）向电话发出命令。可用命令的范围取决于移动操作系统，但所有主要平台至少支持发起和接收呼叫。

研究人员能够通过从易受攻击的设备内存中提取蓝牙链接密钥来触发对任意号码的呼叫。他们说，根据手机的配置，攻击者还可以获取通话记录和联系人。他们还能够发起一个电话，并“成功窃听电话范围内的对话或声音”。

此外，易受攻击设备的固件可能会被重写，以允许远程代码执行，从而促进能够跨多个设备传播的蠕虫攻击的部署。

**应用攻击受限制**

尽管ERNW研究人员提出了严重的攻击场景，但大规模的实际实施受到某些限制。技术上的复杂性和物理上的接近性将这些攻击限制在高价值目标上，比如外交、新闻或敏感行业。目前，Airoha已经发布了包含必要缓解措施的更新SDK，设备制造商已经开始开发和分发补丁。

文章翻译自：https://www.bleepingcomputer.com/news/security/bluetooth-flaws-could-let-hackers-spy-through-your-microphone/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ji8tDpYS)

#### 你可能感兴趣的

* [![]()

  Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
* [![]()

  TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
* [![]()

  黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
* [![]()

  黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
* [![]()

  Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)
* [![]()

  WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)
  2025-09-15 12:00:00
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)
  2025-09-10 12:00:00
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)
  2025-09-10 12:00:00
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)
  2025-09-08 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Salesloft: GitHub账户遭入侵 导致Drift令牌被盗并引发大规模Salesforce数据窃取](https://www.4hou.com/posts/33NQ)

  胡金鱼
* [TP-Link确认路由器存在未修复零日漏洞](https://www.4hou.com/posts/YZ8p)

  胡金鱼
* [黑客借助HexStrike-AI工具可快速利用新型漏洞](https://www.4hou.com/posts/PGyn)

  胡金鱼
* [黑客利用Sitecore零日漏洞部署WeepSteel侦察恶意软件](https://www.4hou.com/posts/RXAR)

  胡金鱼
* [Docker Desktop严重漏洞可让攻击者劫持Windows主机](https://www.4hou.com/posts/omzK)

  胡金鱼
* [WinRAR 零日漏洞被利用在解压档案时植入恶意软件](https://www.4hou.com/posts/vw4m)

  胡金鱼

![]()

[公司简介](https://www.4hou.com/about?title=公司简介)
|
[我要投稿](https://www.4hou.com/about?title=我要投稿)
|
[更新日志](https://www.4hou.com/about?title=更新日志)
|
[友情链接](https://www.4hou.com/about?title=友情链接)
|
[隐私政策](https://www.4hou.com/about?title=隐私政策)
|

[![](https://www.4hou.com/sihou/images/new4hou/weibo.png)](http://weibo.com/u/6069423878)
![](https://www.4hou.com/sihou/images/new4hou/wechat.png)

本站4hou.com，所使用的字体和图片文字等素材部分来源于原作者或互联网共享平台。如使用任何字体和图片文字有侵犯其版权所有方的，嘶吼将配合联系原作者核实，并做出删除处理。

[©2024 北京嘶吼文化传媒有限公司 京ICP备16063439号-1](https://beian.miit.gov.cn/)
本站由 ![](https://www.4hou.com/sihou/images/new4hou/txcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/bdcloud.png) ![](https://www.4hou.com/sihou/images/new4hou/ucloud.png) 提供云计算服务

微信

[微博](http://weibo.com/u/6069423878)
[RSS](https://www.4hou.com/feed)
[知乎](https://zhuanlan.zhihu.com/roartalk)