---
title: 黑客团伙滥用Hugging Face平台传播数千款安卓恶意软件变种
url: https://www.4hou.com/posts/wxXz
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-10
fetch_date: 2026-02-11T04:22:34.039930
---

# 黑客团伙滥用Hugging Face平台传播数千款安卓恶意软件变种

黑客团伙滥用Hugging Face平台传播数千款安卓恶意软件变种 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客团伙滥用Hugging Face平台传播数千款安卓恶意软件变种

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-02-10 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)16400

收藏

导语：用户安装TrustBastion后，应用会立即弹出一个强制更新提示，其界面设计高度模仿谷歌应用商店，极具迷惑性。

一款新型安卓恶意软件攻击活动正将Hugging Face平台当作仓库，存放数千个安卓应用安装包（APK）载荷变种，专门窃取主流金融及支付平台的用户凭证。

Hugging Face主要用于托管和分发人工智能（AI）、自然语言处理（NLP）及机器学习（ML）模型、数据集与相关应用。该平台向来被视为可信度较高的技术平台，一般不会触发安全告警，但此前也曾有不法分子滥用该平台托管恶意人工智能模型。研究人员发现，攻击者正是利用Hugging Face平台的这一特性，大规模分发安卓恶意软件。

该攻击活动的诱导流程如下：攻击者通过恐吓式广告吸引受害者，谎称其设备已遭病毒感染，诱骗用户安装一款名为TrustBastion的投放器应用。这款恶意应用伪装成安全工具，对外宣称可检测诈骗信息、钓鱼短信、钓鱼攻击及恶意软件等各类威胁。

用户安装TrustBastion后，应用会立即弹出一个强制更新提示，其界面设计高度模仿谷歌应用商店，极具迷惑性。

![图片8.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260130/1769759426212045.png "1769759401712114.png")

假的Google Play页面

与直接投放恶意软件的方式不同，这款投放器会先连接与trustbastion[.]com相关联的服务器，该服务器会返回一个跳转链接，指向存储在Hugging Face数据集仓库中的恶意安装包。最终的恶意载荷会从Hugging Face的基础设施中下载，并通过其内容分发网络（CDN）完成投递。

为规避安全检测，威胁者采用了服务端多态技术，每15分钟就生成一个全新的恶意载荷变种。在本次调查期间，该恶意软件仓库已存在约29天，累计提交记录超6000条。

研究人员分析过程中，这个用于分发载荷的仓库曾被平台下架，但该攻击团伙很快以“Premium Club”的新名称卷土重来，更换了应用图标，却保留了全部恶意代码。

攻击活动中的核心恶意载荷尚未被命名，本质是一款远程控制工具。它会以保障安全为由，诱导用户授予安卓系统的辅助功能权限——而这正是该恶意软件实现攻击的关键。

![图片9.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260130/1769759433766218.png "1769759433766218.png")

无障碍服务请求

一旦获取该权限，恶意软件便能在用户屏幕上显示悬浮窗口、捕获屏幕内容、模拟滑动操作，甚至阻止用户卸载应用。

这款恶意软件会全程监控用户操作行为并截取屏幕截图，将所有信息窃取后发送给攻击者。同时，它还会伪造金融平台的登录界面，以此骗取用户的账户凭证，甚至会尝试窃取用户的锁屏密码。

恶意软件会持续与命令与控制（C2）服务器保持连接，一方面将窃取到的数据上传至服务器，另一方面接收来自攻击者的命令执行指令、配置更新信息，同时服务器还会推送伪造的应用内内容，让TrustBastion看起来更像一款正规应用。

发现此次攻击活动的研究人员已就该威胁者的恶意仓库问题向Hugging Face平台进行通报，平台随即移除了包含恶意软件的相关数据集。研究人员也公开发布了针对该投放器、相关网络及恶意安装包的入侵指标（IOC）。

安全专家提醒安卓用户，应避免从第三方应用商店下载应用或手动安装应用程序；同时，安装应用时要仔细查看其申请的权限，确认所有权限均为应用实现核心功能所必需。

文章来源自：https://www.bleepingcomputer.com/news/security/hugging-face-abused-to-spread-thousands-of-android-malware-variants/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?WrQDCqXA)

#### 你可能感兴趣的

* [![]()

  2025年全球加密货币网络犯罪激增，黑客与勒索攻击事件持续高发](https://www.4hou.com/posts/EyJ4)
* [![]()

  黑客团伙滥用Hugging Face平台传播数千款安卓恶意软件变种](https://www.4hou.com/posts/wxXz)
* [![]()

  八问+一图，读懂《汽车数据出境安全指引（2026版）》](https://www.4hou.com/posts/MXRR)
* [![]()

  初始访问黑客借Tsundere Bot入侵网络，或为勒索攻击铺路](https://www.4hou.com/posts/vwWM)
* [![]()

  国家计算机病毒应急处理中心检测发现72款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/OGWQ)
* [![]()

  盘点2025年网络钓鱼攻击方式与套路](https://www.4hou.com/posts/jBEB)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [2025年全球加密货币网络犯罪激增，黑客与勒索攻击事件持续高发](https://www.4hou.com/posts/EyJ4)
  2026-02-11 12:00:00
* [黑客团伙滥用Hugging Face平台传播数千款安卓恶意软件变种](https://www.4hou.com/posts/wxXz)
  2026-02-10 12:00:00
* [八问+一图，读懂《汽车数据出境安全指引（2026版）》](https://www.4hou.com/posts/MXRR)
  2026-02-09 15:38:14
* [初始访问黑客借Tsundere Bot入侵网络，或为勒索攻击铺路](https://www.4hou.com/posts/vwWM)
  2026-02-09 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [2025年全球加密货币网络犯罪激增，黑客与勒索攻击事件持续高发](https://www.4hou.com/posts/EyJ4)

  胡金鱼
* [黑客团伙滥用Hugging Face平台传播数千款安卓恶意软件变种](https://www.4hou.com/posts/wxXz)

  胡金鱼
* [八问+一图，读懂《汽车数据出境安全指引（2026版）》](https://www.4hou.com/posts/MXRR)

  胡金鱼
* [初始访问黑客借Tsundere Bot入侵网络，或为勒索攻击铺路](https://www.4hou.com/posts/vwWM)

  胡金鱼
* [国家计算机病毒应急处理中心检测发现72款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/OGWQ)

  胡金鱼
* [盘点2025年网络钓鱼攻击方式与套路](https://www.4hou.com/posts/jBEB)

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