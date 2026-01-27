---
title: GhostPoster攻势再起：17款恶意浏览器扩展伪装潜伏 累计下载量超84万
url: https://www.4hou.com/posts/VW4O
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-26
fetch_date: 2026-01-27T03:37:17.322118
---

# GhostPoster攻势再起：17款恶意浏览器扩展伪装潜伏 累计下载量超84万

GhostPoster攻势再起：17款恶意浏览器扩展伪装潜伏 累计下载量超84万 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# GhostPoster攻势再起：17款恶意浏览器扩展伪装潜伏 累计下载量超84万

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8555

收藏

导语：这种分阶段的执行流程表明，该恶意软件正朝着更长的潜伏期、模块化以及更强的抗静态和行为检测能力方向进化。

研究人员在 Chrome、Firefox 和 Edge 应用商店中又发现了17款与GhostPoster攻击活动相关的恶意扩展，这些扩展的累计安装量已高达84万次。

GhostPoster 活动最早由Koi Security的研究人员在2025年12月披露。当时他们发现了17款扩展，这些扩展将恶意 JavaScript 代码隐藏在其 Logo 图片中，用于监控浏览器活动并植入后门。

该恶意代码会从外部资源获取经过高度混淆的载荷（Payload），进而追踪受害者的浏览活动、劫持主流电商平台的联盟营销链接，并注入不可见的 iframe 以实施广告欺诈和点击欺诈。

LayerX的一份新报告指出，尽管该活动已被曝光，但仍在持续进行，以下 17 款扩展均为其最新成员：

**·**Google Translate in Right Click – 522,398 次安装

**·**Translate Selected Text with Google - 159,645 次安装

**·**Ads Block Ultimate – 48,078 次安装

**·**Floating Player – PiP Mode – 40,824 次安装

**·**Convert Everything – 17,171 次安装

**·**Youtube Download – 11,458 次安装

**·**One Key Translate – 10,785 次安装

**·**AdBlocker – 10,155 次安装

**·**Save Image to Pinterest on Right Click – 6,517 次安装

**·**Instagram Downloader – 3,807 次安装

**·**RSS Feed – 2,781 次安装

**·**Cool Cursor – 2,254 次安装

**·**Full Page Screenshot – 2,000 次安装

**·**Amazon Price History – 1,197 次安装

**·**Color Enhancer – 712 次安装

**·**Translate Selected Text with Right Click – 283 次安装

**·**Page Screenshot Clipper – 86 次安装

研究人员称，该活动最初起源于 Microsoft Edge 应用商店，随后扩展至 Firefox 和 Chrome。

LayerX 发现，上述部分扩展自 2020 年起就已存在于浏览器插件商店中，这表明这是一场成功的长期潜伏行动。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260120/1768891878102470.png "1768891853144830.png")

扩展上传时间轴

虽然其规避检测和激活后的功能与 Koi 之前记录的大致相同，但 LayerX 在“Instagram Downloader”扩展中发现了一个更高级的变种。

该变种的不同之处在于，它将恶意的“预加载逻辑”转移到了扩展的后台脚本中，并将捆绑的图像文件不仅用作图标，还作为隐蔽的载荷容器。

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260120/1768891904124055.png "1768891904124055.png")

解码图像文件的有效载荷

在运行时，后台脚本会扫描图像的原始字节以寻找特定的分隔符（>>>>），提取隐藏数据并存储在本地扩展存储中，随后将其 Base64 解码并作为 JavaScript 执行。

这种分阶段的执行流程表明，该恶意软件正朝着更长的潜伏期、模块化以及更强的抗静态和行为检测能力方向进化。

新发现的这些扩展目前已从 Mozilla 和 Microsoft 的插件商店中下架。然而，此前已在浏览器中安装了这些扩展的用户可能仍面临风险。

文章来源自：https://www.bleepingcomputer.com/news/security/malicious-ghostposter-browser-extensions-found-with-840-000-installs/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?SdQgGFVY)

#### 你可能感兴趣的

* [![]()

  GhostPoster攻势再起：17款恶意浏览器扩展伪装潜伏 累计下载量超84万](https://www.4hou.com/posts/VW4O)
* [![]()

  2025年国内外网络安全法规政策年鉴](https://www.4hou.com/posts/1MgG)
* [![]()

  Reprompt 攻击现身：可劫持 Microsoft Copilot 会话实施敏感数据窃取](https://www.4hou.com/posts/BvVW)
* [![]()

  国家网络安全通报中心：重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/Zgk8)
* [![]()

  黑客瞄准配置不当代理服务器 意图窃取商用大模型访问权限](https://www.4hou.com/posts/qogk)
* [![]()

  盘点2025年改变网络安全游戏规则的七大网络安全关键词](https://www.4hou.com/posts/vwnM)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [GhostPoster攻势再起：17款恶意浏览器扩展伪装潜伏 累计下载量超84万](https://www.4hou.com/posts/VW4O)
  2026-01-26 12:00:00
* [2025年国内外网络安全法规政策年鉴](https://www.4hou.com/posts/1MgG)
  2026-01-23 10:44:29
* [Reprompt 攻击现身：可劫持 Microsoft Copilot 会话实施敏感数据窃取](https://www.4hou.com/posts/BvVW)
  2026-01-21 12:00:00
* [国家网络安全通报中心：重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/Zgk8)
  2026-01-21 10:41:50

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [GhostPoster攻势再起：17款恶意浏览器扩展伪装潜伏 累计下载量超84万](https://www.4hou.com/posts/VW4O)

  胡金鱼
* [2025年国内外网络安全法规政策年鉴](https://www.4hou.com/posts/1MgG)

  山卡拉
* [Reprompt 攻击现身：可劫持 Microsoft Copilot 会话实施敏感数据窃取](https://www.4hou.com/posts/BvVW)

  胡金鱼
* [国家网络安全通报中心：重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/Zgk8)

  胡金鱼
* [黑客瞄准配置不当代理服务器 意图窃取商用大模型访问权限](https://www.4hou.com/posts/qogk)

  胡金鱼
* [盘点2025年改变网络安全游戏规则的七大网络安全关键词](https://www.4hou.com/posts/vwnM)

  山卡拉

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