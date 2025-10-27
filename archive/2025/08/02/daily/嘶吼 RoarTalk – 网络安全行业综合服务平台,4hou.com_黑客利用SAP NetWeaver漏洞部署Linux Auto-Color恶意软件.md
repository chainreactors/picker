---
title: 黑客利用SAP NetWeaver漏洞部署Linux Auto-Color恶意软件
url: https://www.4hou.com/posts/KGjR
source: 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com
date: 2025-08-02
fetch_date: 2025-10-07T00:18:28.315633
---

# 黑客利用SAP NetWeaver漏洞部署Linux Auto-Color恶意软件

黑客利用SAP NetWeaver漏洞部署Linux Auto-Color恶意软件 - 嘶吼 RoarTalk – 网络安全行业综合服务平台,4hou.com

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

# 黑客利用SAP NetWeaver漏洞部署Linux Auto-Color恶意软件

胡金鱼
[漏洞](https://www.4hou.com/category/vulnerable)
2025-08-01 12:00:00

![](https://img.4hou.com/article/%E6%B5%8F%E8%A7%88.png)49806

收藏

导语：如果 Auto-Color 无法连接到其硬编码的命令和控制 (C2) 服务器，它会抑制其大部分恶意行为。这适用于沙盒和与互联网物理隔离的环境，在这些环境中，恶意软件对分析人员来说会显得 benign。

黑客被发现利用SAP NetWeaver的一个关键漏洞CVE-2025-31324，在一家美国化工公司的网络攻击中部署了Auto-Color Linux恶意软件。

网络安全公司Darktrace在2025年4月的一次事件响应中发现了这种攻击，当时的调查显示，Auto-Color 恶意软件已经进化，包含了额外的高级躲避战术。

Darktrace报告称，攻击于4月25日开始，但两天后才进行积极的利用，将一个ELF（Linux可执行文件）文件传输到目标机器上。

Auto-Color 恶意软件最早是由Palo Alto Networks 的 Unit 42 研究人员在 2025 年 2 月发现的，他们强调了其隐蔽性以及在机器上扎根后难以根除的特性。

后门程序根据其运行的用户权限级别调整其行为，并使用“ld.so”。通过共享对象注入实现隐形持久化的预加载。

Auto-Color功能包括任意命令执行、文件修改、完全远程访问的反向shell、代理流量转发和动态配置更新。它还有一个rootkit模块，可以向安全工具隐藏其恶意活动。

Unit 42无法从它观察到的攻击中发现最初的感染媒介，这些攻击的目标是北美和亚洲的大学和政府机构。

根据Darktrace的最新研究，Auto-Color背后的威胁者利用了CVE-2025-31324，这是NetWeaver中的一个关键漏洞，允许未经身份验证的攻击者上传恶意二进制文件来实现远程代码执行（RCE）。

![timeline(1).jpg](https://img.4hou.com/uploads/ueditor/php/upload/image/20250801/1754016607202649.jpg "1753858210203611.jpg")

观察到的攻击时间线

SAP在4月修复了这个漏洞，而安全公司ReliaQuest、Onapsis和watchtower报告称发现了活跃的利用趋势，几天后就达到了顶峰。而Mandiant报告称，至少从2025年3月中旬开始，就发现了针对CVE-2025-31324的零日攻击的证据。

除了最初的访问向量，Darktrace还发现了一种新的逃避措施，利用在最新版本的Auto-Color。

如果 Auto-Color 无法连接到其硬编码的命令和控制 (C2) 服务器，它会抑制其大部分恶意行为。这适用于沙盒和与互联网物理隔离的环境，在这些环境中，恶意软件对分析人员来说会显得 benign。

Darktrace解释说：“如果C2服务器无法访问，Auto-Color就会有效地停止并避免部署其全部恶意功能，在分析师看来是良性的。”这种行为可以防止逆向工程发现其有效载荷、凭证收集机制或持久性技术。

这是在Unit 42前面记录的内容之上添加的，包括特权感知的执行逻辑、无害文件名的使用、钩子libc函数、假日志目录的使用、通过TLS的C2连接、每个示例的唯一散列以及“终止开关”的存在。

由于Auto-Color现在积极利用CVE-2025-31324，管理员应该迅速采取行动，在仅面向客户的SAP公告中提供安全更新或缓解措施。

文章翻译自：https://www.bleepingcomputer.com/news/security/hackers-exploit-sap-netweaver-bug-to-deploy-linux-auto-color-malware/如若转载，请注明原文地址

* 分享至

![取消](https://www.4hou.com/sihou/images/close.jpg)
![嘶吼](https://www.4hou.com/sihou/images/logo.png)

感谢您的支持，我会继续努力的!

![扫码支持]( "扫一扫")

打开微信扫一扫后点击右上角即可分享哟

### 发表评论

评论

![](https://www.4hou.com/captcha/flat?ERo2M62E)

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