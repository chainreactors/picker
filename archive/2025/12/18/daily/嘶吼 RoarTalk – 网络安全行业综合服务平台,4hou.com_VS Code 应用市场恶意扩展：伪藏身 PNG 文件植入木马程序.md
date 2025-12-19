---
title: VS Code 应用市场恶意扩展：伪藏身 PNG 文件植入木马程序
url: https://www.4hou.com/posts/YZOO
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-12-18
fetch_date: 2025-12-19T03:22:06.580347
---

# VS Code 应用市场恶意扩展：伪藏身 PNG 文件植入木马程序

VS Code 应用市场恶意扩展：伪藏身 PNG 文件植入木马程序 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# VS Code 应用市场恶意扩展：伪藏身 PNG 文件植入木马程序

胡金鱼
[新闻](https://www.4hou.com/category/news)
23小时 前发布

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)8839

收藏

导语：用户应仔细梳理软件包中包含的所有依赖组件，特别是像VS Code扩展程序这类将依赖组件内置打包、而非从npm等可信源获取的情况，更需提高警惕。

安全研究员最新发现，一款隐蔽的恶意攻击活动自2月起持续活跃，攻击者在微软VS Code应用市场上架19款恶意扩展程序，通过在依赖文件夹中植入恶意软件的方式，专门针对开发者发起攻击。调查显示攻击者使用了一个伪装成.PNG格式图片的恶意文件实施攻击。

VS Code应用市场是微软为其广受欢迎的VS Code集成开发环境（IDE）打造的官方扩展门户，开发者可通过该平台下载扩展程序，实现功能拓展或界面个性化定制。

由于该平台用户基数庞大，且存在引发高危害性供应链攻击的潜在风险，一直以来都是威胁者的重点攻击目标，相关攻击手段也在不断迭代升级。

据观察，这些恶意扩展程序均预先打包了node\_modules文件夹，以此规避VS Code在安装过程中从npm软件源获取依赖组件的流程。

攻击者在这个内置的依赖文件夹中植入了经过篡改的依赖包，涉及path-is-absolute与@actions/io两款组件，并在其index.js文件中添加了一个恶意类。该恶意类会在VS Code集成开发环境启动时自动执行。

![图片7.png](https://img.4hou.com/uploads/ueditor/php/upload/image/20251215/1765790407544249.png "1765790407544249.png")

恶意代码添加到index.js文件

需要特别指出的是，path-is-absolute是一款在npm平台上极为热门的软件包，自2021年以来累计下载量已达数十亿次，而此次被植入恶意代码的版本仅存在于该攻击活动涉及的19款扩展程序中。

index.js文件中新增的恶意类，会对一个名为lock的文件内的混淆型JavaScript投放程序进行解码。此外，依赖文件夹中还包含一个伪装成.PNG图片文件（文件名为banner.png）的压缩包，其中藏匿着两款恶意二进制文件：一款是名为cmstp.exe的合法系统工具滥用程序（LoLBin） ，另一款则是基于Rust语言开发的木马程序。

目前，安全研究员仍在对这款木马程序展开分析，以明确其全部功能。

研究人员表示，该攻击活动涉及的19款VS Code恶意扩展程序，名称均基于以下名称变体衍生而来，且发布版本号均为1.0.0：

**·**Malkolm Theme

**·**PandaExpress Theme

**·**Prada 555 Theme

**·**Priskinski Theme

目前，涉事的19款恶意扩展程序现已全部被下架处理。但对于此前已安装这些扩展程序的用户而言，需立即对自身系统进行扫描，排查是否存在被入侵的痕迹。

鉴于威胁者持续开发新手段，规避软件开发常用公共代码仓库的安全检测，安全人员建议用户在安装各类扩展程序前务必对软件包进行全面检查，尤其是当发布方并非信誉良好的正规厂商时。

用户应仔细梳理软件包中包含的所有依赖组件，特别是像VS Code扩展程序这类将依赖组件内置打包、而非从npm等可信源获取的情况，更需提高警惕。

文章来源自：https://www.bleepingcomputer.com/news/security/malicious-vscode-marketplace-extensions-hid-trojan-in-fake-png-file/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?OaZIPoB9)

#### 你可能感兴趣的

* [![]()

  VS Code 应用市场恶意扩展：伪藏身 PNG 文件植入木马程序](https://www.4hou.com/posts/YZOO)
* [![]()

  MITRE 发布 2025 年度TOP25最危险软件弱点榜单](https://www.4hou.com/posts/2XLj)
* [![]()

  勒索软件团伙滥用Shanya可执行文件打包器隐匿EDR禁用工具](https://www.4hou.com/posts/GApr)
* [![]()

  新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户](https://www.4hou.com/posts/jBoY)
* [![]()

  Predator间谍软件采用新型攻击载体实施零点击攻击](https://www.4hou.com/posts/yzKz)
* [![]()

  AI安全元年 | 盘点2025年AI与安全的“相爱相杀”](https://www.4hou.com/posts/Eynm)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [VS Code 应用市场恶意扩展：伪藏身 PNG 文件植入木马程序](https://www.4hou.com/posts/YZOO)
  2025-12-18 11:59:00
* [MITRE 发布 2025 年度TOP25最危险软件弱点榜单](https://www.4hou.com/posts/2XLj)
  2025-12-17 12:00:00
* [勒索软件团伙滥用Shanya可执行文件打包器隐匿EDR禁用工具](https://www.4hou.com/posts/GApr)
  2025-12-16 12:00:00
* [新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户](https://www.4hou.com/posts/jBoY)
  2025-12-15 12:00:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [VS Code 应用市场恶意扩展：伪藏身 PNG 文件植入木马程序](https://www.4hou.com/posts/YZOO)

  胡金鱼
* [MITRE 发布 2025 年度TOP25最危险软件弱点榜单](https://www.4hou.com/posts/2XLj)

  胡金鱼
* [勒索软件团伙滥用Shanya可执行文件打包器隐匿EDR禁用工具](https://www.4hou.com/posts/GApr)

  胡金鱼
* [新型钓鱼攻击借Calendly伪装知名品牌 伺机劫持广告管理账户](https://www.4hou.com/posts/jBoY)

  胡金鱼
* [Predator间谍软件采用新型攻击载体实施零点击攻击](https://www.4hou.com/posts/yzKz)

  胡金鱼
* [AI安全元年 | 盘点2025年AI与安全的“相爱相杀”](https://www.4hou.com/posts/Eynm)

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