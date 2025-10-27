---
title: 80% 案例显示：恶意活动激增时极大可能出现新安全漏洞
url: https://www.4hou.com/posts/2XmK
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-12
fetch_date: 2025-10-07T00:12:55.300135
---

# 80% 案例显示：恶意活动激增时极大可能出现新安全漏洞

80% 案例显示：恶意活动激增时极大可能出现新安全漏洞 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 80% 案例显示：恶意活动激增时极大可能出现新安全漏洞

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-08-11 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)47664

收藏

导语：GreyNoise指出，在大多数情况下，这些峰值背后，攻击者针对的是已知的旧漏洞进行攻击尝试。

研究人员发现，在大约80%的案例中，针对边缘网络设备的恶意活动激增（如网络侦察、定向扫描和暴力破解尝试），是新安全漏洞（CVE）出现的前兆。

这一发现来自威胁监测公司GreyNoise。该公司表示，这些现象并非随机发生，而是根据案例统计得出的严谨结果。

GreyNoise的结论基于其“全球观测网格”（GOG）自2024年9月以来收集的数据，并通过应用客观的统计阈值，避免了可能扭曲结果的“选择性筛选”问题。

剔除一些模糊及低质量的数据后，该公司最终确定了216起符合条件的激增事件，这些事件与8家企业级边缘设备供应商相关。

研究人员解释道：“在我们研究的所有216起激增事件中，50%在三周内出现了新的CVE漏洞，80%在六周内出现了新的CVE漏洞。”

这种关联性在Ivanti、SonicWall、Palo Alto Networks和Fortinet的产品上尤为显著，而在MikroTik、Citrix和Cisco的产品上则相对较弱。有国家支持背景的黑客组织多次将此类系统作为目标，以获取初始访问权限并维持持久控制。

![spikes-cves.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250811/1754879023209054.jpg "1754293606772021.jpg")

新cve的峰值活动和披露时间

GreyNoise指出，在大多数情况下，这些峰值背后，攻击者针对的是已知的旧漏洞进行攻击尝试。

研究人员认为，这种行为要么会推动新漏洞的发现，要么能让攻击者找到暴露在互联网上的端点，以便在攻击的下一阶段利用新型漏洞对这些端点展开攻击。

**预警信号**

传统上，防御方会在CVE漏洞公布后才采取应对措施，但GreyNoise的研究结果表明，攻击者的行为可以作为一种先行指标，成为组织主动防御的工具。

这些漏洞披露前的活动激增，为防御方提供了准备时间：他们可以加强监控、加固系统以抵御潜在攻击，即便安全更新无法提供保护，且他们并不清楚系统的哪个组件或功能才是实际攻击目标。

GreyNoise建议，应密切监控扫描活动并及时封禁来源IP，这样可以阻止这些IP进行通常会引发后续实际攻击的侦察行为。研究人员强调，在这类情况下，出现针对旧漏洞的扫描是意料之中的事，因为攻击者的目的是对暴露的资产进行分类记录。因此，不应将这些扫描视为针对已完全打补丁的端点的失败入侵尝试而置之不理。

![vulnerabilities.jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250811/1754879023808510.jpg "1754293647801339.jpg")

活动峰值（白色）和新cve的发布（红色）

在相关的开发中，谷歌“Project Zero”宣布将在发现漏洞后的一周内向公众通报相关情况，并在供应商开发补丁时帮助系统管理员加强防御。Project Zero现在将共享受新漏洞影响的供应商/项目和产品、发现时间和披露截止日期（仍然是90天）。

谷歌表示，由于不会公布技术细节、概念验证漏洞利用代码或其他可能让攻击者有机可乘的信息，但这一更改不会对安全性产生不利影响，同时还有助于缩短“补丁缺口”。

文章翻译自：https://www.bleepingcomputer.com/news/security/spikes-in-malicious-activity-precede-new-cves-in-80-percent-of-cases/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?VoSkJZdR)

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