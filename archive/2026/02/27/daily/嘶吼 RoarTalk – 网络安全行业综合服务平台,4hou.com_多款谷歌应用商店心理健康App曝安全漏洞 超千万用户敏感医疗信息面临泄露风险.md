---
title: 多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险
url: https://www.4hou.com/posts/mkAn
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-27
fetch_date: 2026-02-28T03:50:13.515156
---

# 多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险

多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)3129

收藏

导语：在暗网中，心理咨询记录每条售价可达1000美元甚至更高。

最新发现，谷歌应用商店中多款下载量达数百万级的心理健康APP存在安全漏洞，可能导致用户的敏感医疗信息遭到泄露。

安全研究人员在其中一款应用中，发现了超过85个中高危漏洞，攻击者可利用这些漏洞窃取用户的心理咨询数据与隐私信息。

部分涉事应用为AI陪伴类工具，旨在帮助患有临床抑郁症、各类焦虑症、惊恐发作、压力应激及双相情感障碍的人群。在研究人员分析的10款应用中，至少有6款宣称用户对话内容为私密信息，或在服务商服务器上进行安全加密存储。据了解，心理健康数据具有极高的风险价值。在暗网中，心理咨询记录每条售价可达1000美元甚至更高。

**累计发现超1500个安全问题**

研究人员对十款宣传可辅助解决各类心理健康问题的移动应用进行了扫描，共发现1575个安全漏洞，其中高危漏洞54个、中危漏洞538个、低危漏洞983个。

尽管发现的所有漏洞都不严重，但大量漏洞可被用于窃取登录凭证、伪造通知、执行HTML注入或获取用户位置。

一款下载量超百万的心理咨询类应用，直接对外部可控字符串使用Intent.parseUri()，并在未校验目标组件的情况下启动生成的意图对象，这使得攻击者可强制应用打开任意内部页面，即便该页面本不应对外开放。

由于这些内部页面通常处理认证令牌与会话数据，漏洞被利用后，攻击者可直接获取用户的心理咨询记录。

另一类问题是应用本地数据存储权限不当，设备上的任意应用均可读取，可能暴露心理咨询详情，包括咨询记录、认知行为疗法（CBT）会话笔记及各类评估评分。

研究人员还发现，部分应用的APK资源中包含明文配置信息，如后端API接口地址与硬编码的Firebase数据库链接。此外，部分存在漏洞的应用使用加密安全性不足的java.util.Random类生成会话令牌或加密密钥。

研究人员表示，十款应用中的大多数均未实现任何Root检测机制。在已获取Root权限（越狱）的设备上，任何拥有高权限的应用均可访问本地存储的全部健康数据。

十款应用中仅有六款未发现高危漏洞，但仍存在中危漏洞，导致整体安全防护水平下降。这些应用收集并存储着移动端最敏感的个人数据，包括心理咨询会话转录文本、情绪日志、用药计划、自伤倾向指标，部分信息还受《健康保险流通与责任法案》（HIPAA）保护。

据统计，研究人员扫描的应用总下载量已超过1470万次，其中仅有四款应用在本月进行过更新，其余应用的最近更新时间停留在2025年11月，甚至2024年9月。而扫描时间为1月22日至23日，检测对象为当时最新版本应用。研究人员目前无法确认相关漏洞是否已被修复。

文章来源自：https://www.bleepingcomputer.com/news/security/android-mental-health-apps-with-147m-installs-filled-with-security-flaws/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?boAFso4Q)

#### 你可能感兴趣的

* [![]()

  多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险](https://www.4hou.com/posts/mkAn)
* [![]()

  黑客利用 React Native Metro 高危漏洞入侵开发者系统](https://www.4hou.com/posts/DxG5)
* [![]()

  vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码](https://www.4hou.com/posts/qoOk)
* [![]()

  黑客反被黑客黑：研究人员劫持 StealC 控制面板，窃取攻击者情报](https://www.4hou.com/posts/XPgo)
* [![]()

  CSTIS：关于防范MuddyWater组织网络攻击的风险提示](https://www.4hou.com/posts/8gpW)
* [![]()

  严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听](https://www.4hou.com/posts/J14v)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险](https://www.4hou.com/posts/mkAn)
  2026-02-27 11:59:00
* [黑客利用 React Native Metro 高危漏洞入侵开发者系统](https://www.4hou.com/posts/DxG5)
  2026-02-13 12:00:00
* [vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码](https://www.4hou.com/posts/qoOk)
  2026-02-02 12:43:48
* [黑客反被黑客黑：研究人员劫持 StealC 控制面板，窃取攻击者情报](https://www.4hou.com/posts/XPgo)
  2026-01-30 11:59:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [多款谷歌应用商店心理健康App曝安全漏洞 超千万用户敏感医疗信息面临泄露风险](https://www.4hou.com/posts/mkAn)

  胡金鱼
* [黑客利用 React Native Metro 高危漏洞入侵开发者系统](https://www.4hou.com/posts/DxG5)

  胡金鱼
* [vm2 Node.js沙箱库曝高危漏洞 可突破沙箱执行任意代码](https://www.4hou.com/posts/qoOk)

  胡金鱼
* [黑客反被黑客黑：研究人员劫持 StealC 控制面板，窃取攻击者情报](https://www.4hou.com/posts/XPgo)

  胡金鱼
* [CSTIS：关于防范MuddyWater组织网络攻击的风险提示](https://www.4hou.com/posts/8gpW)

  胡金鱼
* [严重漏洞WhisperPair曝光：黑客可通过蓝牙音频设备实施追踪与窃听](https://www.4hou.com/posts/J14v)

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