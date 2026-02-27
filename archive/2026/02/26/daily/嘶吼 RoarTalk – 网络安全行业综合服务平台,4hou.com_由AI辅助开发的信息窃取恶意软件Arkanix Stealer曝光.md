---
title: 由AI辅助开发的信息窃取恶意软件Arkanix Stealer曝光
url: https://www.4hou.com/posts/jBxB
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2026-02-26
fetch_date: 2026-02-27T04:06:54.893042
---

# 由AI辅助开发的信息窃取恶意软件Arkanix Stealer曝光

由AI辅助开发的信息窃取恶意软件Arkanix Stealer曝光 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 由AI辅助开发的信息窃取恶意软件Arkanix Stealer曝光

胡金鱼
[新闻](https://www.4hou.com/category/news)
2026-02-26 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)11110

收藏

导语：卡巴斯基评价称，Arkanix与其说是一款隐蔽的窃密木马，更像是一款公开的软件产品。

一款名为Arkanix Stealer的信息窃取恶意软件于2025年末在多个暗网论坛进行推广。据分析，该恶意软件疑似由AI辅助开发，更像是一次技术实验。而其包含控制面板及用于与用户沟通的Discord服务器在运营仅两个月后，作者便在未发出任何通知的情况下将其下线。

Arkanix提供了网络犯罪分子常用的多项标准数据窃取功能，同时具备模块化架构与抗分析能力。卡巴斯基研究人员在分析后发现，多项线索表明该窃密木马由大语言模型（LLM）辅助开发，这“可能大幅降低了开发时间与成本”。

![图片1.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260224/1771916045209223.png "1771914609157533.png")

代码中存在大语言模型（LLM）生成痕迹

研究人员认为，Arkanix属于生命周期较短、旨在快速牟利的项目，这类特性使其更难被检测与追踪。

**Arkanix浮出水面**

Arkanix于2025年10月开始在黑客论坛推广，向潜在客户提供两个版本：

**·**基础版：基于Python实现

**·**高级版：采用原生C++编写载荷，使用VMProtect加壳，集成免杀与钱包注入功能

![图片2.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260224/1771916048190919.png "1771914650199480.png")

Arkanix在黑客论坛上受到推广

开发者搭建了Discord服务器，作为项目社区交流平台，用于发布更新、收集功能反馈并提供技术支持。

该恶意软件还推出了推广奖励计划：推荐人可额外获得一小时高级版免费使用时长，新用户则可免费体验一周高级版。

![图片3.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260224/1771916050190902.png "1771914678170216.png")

控制面板内的推广推荐选项

**数据窃取能力**

Arkanix恶意软件可收集系统信息，窃取浏览器存储的数据（历史记录、自动填充信息、Cookie、密码），并支持从22 款浏览器中提取加密货币钱包数据。卡巴斯基指出，该木马还可在基于Chromium内核的浏览器中窃取OAuth2令牌。

此外，该恶意软件可窃取Telegram、Discord账号凭证，通过Discord API传播，并向受害者的好友或频道发送消息。

Arkanix还针对Mullvad、NordVPN、ExpressVPN、ProtonVPN等VPN工具的账号密码，可将本地文件打包并异步外传。

从命令与控制（C2）服务器可下载的扩展模块包括：Chrome信息窃取工具、Exodus/Atomic钱包补丁工具、屏幕截图工具、HVNC以及针对FileZilla、Steam的窃密模块。

![图片4.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20260224/1771916053253381.png "1771914699742186.png")

部分受攻击的加密货币扩展列表

高级原生C++ 版额外增加以下能力：

**·**RDP凭证窃取

**·**反沙箱、反调试检测

**·**基于WinAPI的屏幕捕获

**·**针对Epic Games、Battle.net、Riot、Unreal Engine、Ubisoft Connect、GOG等平台的账号窃取

高级版还会投放后渗透工具ChromElevator，该工具注入挂起的浏览器进程实施数据窃取，可绕过谷歌应用绑定加密（ABE）保护，非法获取用户账号凭证。

目前，Arkanix窃密项目的实验目的尚不明确。但该项目验证了大语言模型能在很大程度上提升恶意软件开发效率，以及新功能可以很快交付这一事实。卡巴斯基评价称，Arkanix与其说是一款隐蔽的窃密木马，更像是一款公开的软件产品。

文章来源自：https://www.bleepingcomputer.com/news/security/arkanix-stealer-pops-up-as-short-lived-ai-info-stealer-experiment/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?BIqrHMwO)

#### 你可能感兴趣的

* [![]()

  由AI辅助开发的信息窃取恶意软件Arkanix Stealer曝光](https://www.4hou.com/posts/jBxB)
* [![]()

  永利度假村确认员工数据遭黑客窃取 攻击事件系黑客组织ShinyHunters所为](https://www.4hou.com/posts/l0zV)
* [![]()

  恶意分子滥用Claude发动ClickFix攻击 向macOS用户分发信息窃取木马](https://www.4hou.com/posts/0M13)
* [![]()

  Crazy勒索软件团伙滥用监控与远程工具实施网络入侵](https://www.4hou.com/posts/8gkW)
* [![]()

  新型恶意软件ZeroDayRAT可完全远程控制安卓与 iOS 设备](https://www.4hou.com/posts/YZ2W)
* [![]()

  假冒的7-Zip官网暗藏代理木马传播恶意安装包](https://www.4hou.com/posts/W1Zn)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [由AI辅助开发的信息窃取恶意软件Arkanix Stealer曝光](https://www.4hou.com/posts/jBxB)
  2026-02-26 12:00:00
* [永利度假村确认员工数据遭黑客窃取 攻击事件系黑客组织ShinyHunters所为](https://www.4hou.com/posts/l0zV)
  2026-02-26 11:59:00
* [恶意分子滥用Claude发动ClickFix攻击 向macOS用户分发信息窃取木马](https://www.4hou.com/posts/0M13)
  2026-02-25 12:00:00
* [Crazy勒索软件团伙滥用监控与远程工具实施网络入侵](https://www.4hou.com/posts/8gkW)
  2026-02-25 11:59:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [由AI辅助开发的信息窃取恶意软件Arkanix Stealer曝光](https://www.4hou.com/posts/jBxB)

  胡金鱼
* [永利度假村确认员工数据遭黑客窃取 攻击事件系黑客组织ShinyHunters所为](https://www.4hou.com/posts/l0zV)

  胡金鱼
* [恶意分子滥用Claude发动ClickFix攻击 向macOS用户分发信息窃取木马](https://www.4hou.com/posts/0M13)

  胡金鱼
* [Crazy勒索软件团伙滥用监控与远程工具实施网络入侵](https://www.4hou.com/posts/8gkW)

  胡金鱼
* [新型恶意软件ZeroDayRAT可完全远程控制安卓与 iOS 设备](https://www.4hou.com/posts/YZ2W)

  胡金鱼
* [假冒的7-Zip官网暗藏代理木马传播恶意安装包](https://www.4hou.com/posts/W1Zn)

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