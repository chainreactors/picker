---
title: 安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送
url: https://www.4hou.com/posts/rpzk
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-05
fetch_date: 2025-12-06T03:09:48.888931
---

# 安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送

安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)9454

收藏

导语：安卓内置杀毒模块Google Play Protect在部分设备上拦截了SmartTube，并向用户发出安全风险警示。

安卓电视平台的开源YouTube客户端SmartTube已确认遭入侵——攻击者获取开发者的数字签名密钥后，向用户推送了包含恶意代码的更新包。

此次安全事件由多名用户反馈发现：安卓内置杀毒模块Google Play Protect在部分设备上拦截了SmartTube，并向用户发出安全风险警示。

SmartTube开发者证实，其数字签名密钥于上周末被盗，导致恶意软件被注入应用程序。目前已吊销旧签名，并表示将尽快发布采用独立应用ID的新版本，同时敦促用户升级至该安全版本。

作为安卓电视、Fire TV、安卓电视盒等设备上下载量最高的第三方YouTube客户端之一，SmartTube的流行源于其免费属性、广告拦截功能，以及在低性能设备上的流畅运行表现。

一名逆向工程师对遭入侵的30.51版本进行分析后发现，该版本包含一个名为libalphasdk.so的隐藏原生库（[病毒总数平台检测链接]）。由于该库未出现在公开源代码中，推测是在发布构建过程中被恶意注入。

开发者表示：“这很可能是一款恶意软件。该文件并非所使用SDK的组成部分，其出现在APK安装包中完全出乎意料且存在高度可疑性。在核实其来源前，建议用户保持警惕。”

经分析，该恶意库会在后台静默运行，无需用户交互即可完成设备指纹采集、向远程服务器注册设备，并通过加密通信通道定期发送设备指标数据及获取配置指令。尽管目前尚未发现账号盗窃、参与DDoS僵尸网络等恶意行为，但攻击者可随时利用该模块发起此类攻击，潜在风险极高。

尽管开发者已在Telegram宣布发布安全测试版及稳定测试版，但这些版本尚未同步至项目官方GitHub仓库。此外，开发者未披露事件完整细节，引发用户信任危机。SmartTube表示，待新版应用正式上架F-Droid应用商店后，将全面回应所有关问题。

在开发者通过详细事后分析报告公开披露全部事件细节前，安全专家建议用户：保持使用经验证安全的旧版本、避免登录高级账户、关闭自动更新功能；受影响用户应重置Google账户密码，检查账户控制台是否存在未授权访问记录，并移除陌生关联服务。

为确保完全安全，SmartTube已从30.55版本起已切换至新签名密钥。30.47 Stable v7a版本出现不同哈希值，可能是在清理受感染系统后尝试恢复该版本所致。

文章来源自：https://www.bleepingcomputer.com/news/security/smarttube-youtube-app-for-android-tv-breached-to-push-malicious-update/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?lCBQMVJa)

#### 你可能感兴趣的

* [![]()

  安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送](https://www.4hou.com/posts/rpzk)
* [![]()

  国家计算机病毒应急处理中心检测发现69款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/nlvY)
* [![]()

  Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台](https://www.4hou.com/posts/qoyR)
* [![]()

  国家网络安全通报中心：重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/l0q7)
* [![]()

  恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本](https://www.4hou.com/posts/kgqY)
* [![]()

  Mixpanel遭网络攻击 OpenAI用户数据或面临泄露风险](https://www.4hou.com/posts/l0rJ)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送](https://www.4hou.com/posts/rpzk)
  2025-12-05 12:00:00
* [国家计算机病毒应急处理中心检测发现69款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/nlvY)
  2025-12-05 10:28:08
* [Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台](https://www.4hou.com/posts/qoyR)
  2025-12-04 12:00:00
* [国家网络安全通报中心：重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/l0q7)
  2025-12-04 10:45:47

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [安卓电视 YouTube 客户端 SmartTube 遭入侵 恶意更新强制推送](https://www.4hou.com/posts/rpzk)

  胡金鱼
* [国家计算机病毒应急处理中心检测发现69款违法违规收集使用个人信息的移动应用](https://www.4hou.com/posts/nlvY)

  胡金鱼
* [Glassworm 恶意软件卷土重来 第三波恶意插件入侵VS Code生态平台](https://www.4hou.com/posts/qoyR)

  胡金鱼
* [国家网络安全通报中心：重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/l0q7)

  胡金鱼
* [恶意大模型持续升级：WormGPT 4与KawaiiGPT可生成勒索软件代码与钓鱼脚本](https://www.4hou.com/posts/kgqY)

  胡金鱼
* [Mixpanel遭网络攻击 OpenAI用户数据或面临泄露风险](https://www.4hou.com/posts/l0rJ)

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