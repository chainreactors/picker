---
title: Chrome 应用商店恶意扩展程序窃取用户敏感数据
url: https://www.4hou.com/posts/J109
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-01-05
fetch_date: 2026-01-06T03:26:27.246916
---

# Chrome 应用商店恶意扩展程序窃取用户敏感数据

Chrome 应用商店恶意扩展程序窃取用户敏感数据 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# Chrome 应用商店恶意扩展程序窃取用户敏感数据

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)12476

收藏

导语：这两款插件仍在Chrome官方应用商店上架，且至少自2017年起便已活跃。

Chrome应用商店中两款名为“Phantom Shuttle”的扩展程序，正伪装成代理服务插件，暗中劫持用户网络流量并窃取敏感数据。

据研究人员报告显示，这两款插件仍在Chrome官方应用商店上架，且至少自2017年起便已活跃。

Phantom Shuttle的目标用户多为需要测试不同地区网络连通性的外贸从业者。两款插件由同一开发者发布，均以“可代理流量、测试网速”为宣传点，订阅价格在1.4至13.6美元之间。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260105/1767579328100093.png "1766729628622403.png")

Chrome 应用商店中的Phantom Shuttle扩展程序

**隐秘的数据窃取功能**

Socket.dev研究人员指出，Phantom Shuttle会将用户所有网络流量路由至攻击者控制的代理服务器，且通过硬编码凭证实现访问——相关恶意代码被嵌入到合法的jQuery库中，以规避检测。

恶意代码采用自定义字符索引编码方案隐藏硬编码的代理凭证，并通过网络流量监听器，拦截所有网站的HTTP认证请求。为强制用户流量经由攻击者代理传输，该恶意插件会通过自动配置脚本，动态修改Chrome浏览器的代理设置。

在默认的“智能模式”下，插件会将170余个高价值域名的流量路由至代理网络，涵盖开发者平台、云服务控制台、社交媒体网站及成人内容门户等。本地网络与命令控制域名则被列入排除清单，以此避免攻击行为中断或被检测发现。

作为中间人，该插件可捕获各类表单数据（包括账户凭证、银行卡信息、密码、个人信息等），窃取HTTP头中的会话Cookie，并从请求中提取API令牌。

研究人员建议Chrome用户：仅信任知名开发者发布的扩展程序，安装前查看多方用户评价，并留意插件申请的权限范围，避免因恶意插件导致数据泄露。

文章来源自：https://www.bleepingcomputer.com/news/security/malicious-extensions-in-chrome-web-store-steal-user-credentials/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?VIFYJjZN)

#### 你可能感兴趣的

* [![]()

  Chrome 应用商店恶意扩展程序窃取用户敏感数据](https://www.4hou.com/posts/J109)
* [![]()

  《彩虹六号：围攻》重大黑客入侵事件致无数玩家获赠数十亿游戏币](https://www.4hou.com/posts/MXLP)
* [![]()

  新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测](https://www.4hou.com/posts/nlEY)
* [![]()

  国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/LGKp)
* [![]()

  RansomHouse完成加密工具升级：采用多层数据处理技术](https://www.4hou.com/posts/kgAr)
* [![]()

  Clop勒索软件发起数据窃取攻击：Gladinet CentreStack成目标](https://www.4hou.com/posts/jBzY)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [Chrome 应用商店恶意扩展程序窃取用户敏感数据](https://www.4hou.com/posts/J109)
  2026-01-05 12:00:00
* [《彩虹六号：围攻》重大黑客入侵事件致无数玩家获赠数十亿游戏币](https://www.4hou.com/posts/MXLP)
  2025-12-30 12:00:00
* [新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测](https://www.4hou.com/posts/nlEY)
  2025-12-29 12:00:00
* [国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/LGKp)
  2025-12-29 11:00:38

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [Chrome 应用商店恶意扩展程序窃取用户敏感数据](https://www.4hou.com/posts/J109)

  胡金鱼
* [《彩虹六号：围攻》重大黑客入侵事件致无数玩家获赠数十亿游戏币](https://www.4hou.com/posts/MXLP)

  胡金鱼
* [新型MacSync恶意软件投放器成功规避macOS Gatekeeper检测](https://www.4hou.com/posts/nlEY)

  胡金鱼
* [国家网络安全通报中心发布新一批重点防范境外恶意网址和恶意IP](https://www.4hou.com/posts/LGKp)

  胡金鱼
* [RansomHouse完成加密工具升级：采用多层数据处理技术](https://www.4hou.com/posts/kgAr)

  胡金鱼
* [Clop勒索软件发起数据窃取攻击：Gladinet CentreStack成目标](https://www.4hou.com/posts/jBzY)

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