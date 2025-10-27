---
title: “s1ngularity”供应链攻击导致数千个GitHub令牌遭泄露
url: https://www.4hou.com/posts/jB15
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-09-20
fetch_date: 2025-10-02T20:25:42.689598
---

# “s1ngularity”供应链攻击导致数千个GitHub令牌遭泄露

“s1ngularity”供应链攻击导致数千个GitHub令牌遭泄露 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# “s1ngularity”供应链攻击导致数千个GitHub令牌遭泄露

胡金鱼
[新闻](https://www.4hou.com/category/news)
2025-09-19 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)34159

收藏

导语：数千账户令牌及仓库密钥泄露，影响持续发酵。

根据Nx“s1ngularity”NPM供应链攻击的调查显示，数千个账户令牌和代码仓库密钥遭泄露。Wiz研究人员事后评估，此次Nx安全漏洞在三个不同阶段共导致2180个账户和7200个仓库面临风险。Wiz同时强调，由于许多泄露的密钥仍处于有效状态，攻击的影响范围仍十分广泛，且后续效应仍在持续显现。

**Nx “s1ngularity”供应链攻击详情**

Nx是一款流行的开源构建系统及单仓库（monorepo）管理工具，广泛应用于企业级JavaScript/TypeScript生态，在NPM包索引上的周下载量超过550万次。

2025年8月26日，攻击者利用Nx代码仓库中存在缺陷的GitHub Actions工作流，在NPM上发布了恶意版本的Nx包，其中包含一个名为“telemetry.js”的安装后恶意脚本。

该恶意脚本是一款针对Linux和macOS系统的凭据窃取工具，试图窃取GitHub令牌、npm令牌、SSH密钥、.env文件、加密货币钱包等信息，并将这些敏感数据上传至名为“s1ngularity-repository”的公共GitHub仓库。

此次攻击的特殊之处在于，凭据窃取工具会利用已安装的人工智能平台命令行工具（如Claude、Q、Gemini等），通过大语言模型（LLM）提示词搜索并收集敏感凭据与密钥。

Wiz报告指出，攻击过程中提示词不断迭代更新，表明攻击者在通过调整提示词提升攻击成功率。

![llm-prompt-to-steal-credentials.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250910/1757490342667432.jpg "1757489571101010.jpg")

LLM提示搜索和窃取凭证和其他密钥

Wiz解释道：“提示词的演变显示，攻击者在整个攻击过程中快速探索提示词调优方法。我们能看到‘角色提示’的引入，以及针对不同技术的具体描述程度变化。”

这些调整对恶意软件的攻击成功率产生了实际影响。例如，加入‘渗透测试’一词后，大语言模型明确拒绝参与此类活动，这一变化十分明显。

**攻击影响范围持续扩大**

**第一阶段（8月26日-27日）**

被植入后门的Nx包直接影响1700名用户，泄露超2000个唯一密钥，并导致受感染系统的2万个文件被暴露。GitHub在8小时后下架了攻击者创建的仓库，但数据已被复制。

**第二阶段（8月28日-29日）**

攻击者利用泄露的GitHub令牌将私有仓库转为公开，并在仓库名称中加入“s1ngularity”字符串。这进一步导致480个账户（其中大部分为企业组织账户）沦陷，6700个私有仓库被公开暴露。

**第三阶段（8月31日起）**

攻击者将目标锁定在单个受害组织，利用两个已攻陷的账户额外公开了500个私有仓库。

![overview.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250910/1757490343209516.jpg "1757489640609300.jpg")

s1ngularity攻击概述

**Nx团队的应对措施**

Nx团队在GitHub上发布了详细的根本原因分析，指出此次漏洞源于“拉取请求（PR）标题注入”与“不安全使用pull\_request\_target”的结合。这种组合使攻击者能够以提升的权限执行任意代码，进而触发Nx的发布流水线，并窃取npm发布令牌。

目前，Nx团队已采取以下补救措施：移除恶意包、撤销并轮换遭泄露的令牌、为所有发布者账户启用双因素认证。

为防止类似漏洞再次发生，Nx项目现已采用NPM的“可信发布者（Trusted Publisher）”模式（该模式无需基于令牌的发布流程），并为PR触发的工作流新增了手动审批环节。

文章翻译自：https://www.bleepingcomputer.com/news/security/ai-powered-malware-hit-2-180-github-accounts-in-s1ngularity-attack/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?Woo5CB1V)

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