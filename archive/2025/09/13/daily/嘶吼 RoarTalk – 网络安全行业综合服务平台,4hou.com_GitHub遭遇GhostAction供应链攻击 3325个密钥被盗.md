---
title: GitHub遭遇GhostAction供应链攻击 3325个密钥被盗
url: https://www.4hou.com/posts/8gVo
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-13
fetch_date: 2025-10-02T20:05:26.654201
---

# GitHub遭遇GhostAction供应链攻击 3325个密钥被盗

GitHub遭遇GhostAction供应链攻击 3325个密钥被盗 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# GitHub遭遇GhostAction供应链攻击 3325个密钥被盗

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-09-12 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)43867

收藏

导语：分析显示，多个软件包生态系统的令牌均遭泄露，包括Rust crate和npm包。

GitHub近期遭遇一场名为“GhostAction”的供应链攻击，攻击者窃取了3325个敏感密钥，包括PyPI、npm、DockerHub、GitHub的令牌，以及Cloudflare和AWS的访问密钥等。

该攻击由GitGuardian的研究人员发现。据报告，受影响项目之一FastUUID最早出现入侵迹象的时间可追溯至2025年9月2日。

此次攻击的手法是：攻击者利用被攻陷的维护者账户提交代码，植入恶意的GitHub Actions工作流文件。该文件会在“推送（push）”操作或手动触发时自动运行，一旦触发，便会从项目的GitHub Actions环境中读取密钥，并通过curl POST请求将其窃取至攻击者控制的外部域名。

![workflow.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250910/1757485810161732.png "1757485748190110.png")

针对FastUUID的恶意工作流

GitGuardian指出，在FastUUID项目中，攻击者窃取了该项目的PyPI令牌，但好在攻击被发现并修复前，软件包索引（package index）上未出现恶意包发布的情况。

然而，深入调查后发现，此次攻击范围远不止FastUUID。研究人员表示，“GhostAction”攻击行动已在至少817个代码仓库中注入了类似的恶意提交，所有被盗密钥均被发送至同一个窃取端点：“bold-dhawan[.]45-139-104-115[.]plesk[.]page”。

攻击者先从合法工作流中枚举密钥名称，再将这些名称硬编码到自己的恶意工作流中，从而窃取多种类型的密钥。

9月5日，GitGuardian摸清攻击的完整范围后，立即在573个受影响的代码仓库中提交了GitHub Issue，并直接通知了GitHub、npm和PyPI的安全团队。目前，已有100个GitHub代码仓库检测到入侵并回滚了恶意修改。

攻击被发现后不久，该密钥窃取端点便已无法解析。 研究人员估计，“GhostAction”攻击中共窃取了约3325个密钥，涵盖PyPI令牌、npm令牌、DockerHub令牌、GitHub令牌、Cloudflare API令牌、AWS访问密钥及数据库凭据等。

![secrets.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250910/1757485810148555.jpg "1757485805156175.jpg")

泄露密钥的类型和数量

至少有9个npm包和15个PyPI包直接受此影响——在维护者撤销泄露的密钥前，这些包随时可能被发布恶意版本或植入木马的版本。

分析显示，多个软件包生态系统的令牌均遭泄露，包括Rust crate和npm包。有几家公司的整个SDK产品组合都已沦陷，其Python、Rust、JavaScript和Go代码仓库同时受到恶意工作流的影响。

尽管此次攻击与8月末发生的“s1ngularity”攻击在实际操作和技术层面存在一些相似之处，但GitGuardian表示，目前认为这两起攻击并无关联。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-steal-3-325-secrets-in-ghostaction-github-supply-chain-attack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?r5XA1CVT)

#### 你可能感兴趣的

* [![]()

  ​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
* [![]()

  新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
* [![]()

  新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
* [![]()

  Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
* [![]()

  npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)
* [![]()

  大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

![](https://img.4hou.com/images/微信图片_20231102150249.jpg)

# [胡金鱼](https://www.4hou.com/member/BVMN)

这个家伙很懒,什么也没说!

#### 最新文章

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)
  2025-09-30 12:01:00
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)
  2025-09-29 12:00:00
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)
  2025-09-28 12:00:00
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)
  2025-09-26 12:01:00

[查看更多](https://www.4hou.com/member/BVMN)

# 相关热文

* [​LastPass提醒macOS用户：假冒热门软件的恶意程序通过虚假GitHub仓库传播](https://www.4hou.com/posts/LGqg)

  胡金鱼
* [新型FileFix社工攻击诱导用户安装StealC信息窃取恶意软件](https://www.4hou.com/posts/nl14)

  胡金鱼
* [新型NPM包利用 QR 码获取 cookie 的恶意软件](https://www.4hou.com/posts/VWE5)

  胡金鱼
* [Cloudflare抵御创纪录DDoS攻击：峰值达22.2 Tbps、106亿PPS](https://www.4hou.com/posts/W1GW)

  胡金鱼
* [npm供应链攻击“Shai-Hulud”持续发酵：187款npm包遭攻陷 含自传播恶意载荷](https://www.4hou.com/posts/mk5p)

  胡金鱼
* [大规模Android广告欺诈团伙“SlopAds”被瓦解：利用224款恶意应用日均发起23亿次广告请求](https://www.4hou.com/posts/l01l)

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