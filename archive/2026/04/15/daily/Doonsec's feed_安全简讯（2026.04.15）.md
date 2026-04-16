---
title: 安全简讯（2026.04.15）
url: https://mp.weixin.qq.com/s/QjAgIlkrdF4mp8aZQlMNxw
source: Doonsec's feed
date: 2026-04-15
fetch_date: 2026-04-16T04:50:51.339376
---

# 安全简讯（2026.04.15）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4S21m309ZrzFV6c1ESlH1thESkgY6chpAXjsPicjQhYmx1MoGCBHk5kBz49ibktlwqDSuicz1un0StKBQvfkzEiaqdINPonMhj4Wx4zrrqfd0UI/0?wx_fmt=jpeg)

# 安全简讯（2026.04.15）

启明星辰安全简讯

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**1. Handala组织声称对阿联酋发动重大网络攻击**

4月13日，名为Handala的黑客组织近日声称对阿联酋发动了一次重大网络攻击，目标包括迪拜法院部门、迪拜土地部门和迪拜道路交通管理局。该组织宣称销毁了6PB的数据，窃取了149TB的敏感信息，并将此次攻击定性为对地区政府的报复和警告。Handala在其Tor网站上表示：“鉴于阿联酋领导人公然背叛抵抗轴心，并作为对该地区所有叛国政府的严肃先发制人警告，汉达拉组织已对该国关键基础设施发动了迄今为止威力最强大的网络攻击之一。在此次行动中，6PB的数据已被彻底销毁。”目前这些说法尚未得到独立证实。Handala表面上是一个支持巴勒斯坦的黑客组织，但普遍认为它是伊朗支持的Void Manticore的幌子。该组织以网络钓鱼、数据窃取、勒索和破坏性擦除攻击而闻名，同时从事信息战和心理战。自伊朗冲突爆发以来，该组织一直以以色列军方服务器、情报人员和公司为目标，窃取或擦除数据。

https://securityaffairs.com/190716/hacking/iran-linked-group-handala-claims-to-have-breached-three-major-uae-organizations.html

**2. Kraken遭内部威胁勒索，拒绝支付赎金**

4月14日，加密货币交易所Kraken近日披露，一个网络犯罪团伙正试图通过威胁发布显示托管客户数据的内部系统视频来敲诈该公司。Kraken首席安全官尼克·佩尔科科表示，该事件并未危及客户资金，而是涉及内部威胁，其中两名支持人员不当访问了有限的客户数据。Kraken明确表示不会向威胁行为者支付任何费用或进行任何谈判。2025年2月，Kraken收到“来自可靠来源的线索”，称网络犯罪分子散布了一段视频，演示如何访问其客户支持系统。随后展开调查，发现一名支持人员被该威胁行为者招募。最近，Kraken再次收到线报，称有一段更新的视频显示有人可以访问其系统的内部权限。在两起事件中，公司都迅速做出反应，撤销了涉事员工的访问权限，展开调查并加强管控措施。如发现用户数据泄露，Kraken会直接通知受影响的用户。据佩尔科科称，此次事件仅影响约2000个账户，占Kraken用户总数的0.02%，泄露的信息仅涉及客户支持数据。Kraken表示其调查已收集到足够的证据，可以依法起诉所有试图勒索他们的涉案人员，公司正在与多个司法管辖区的联邦执法部门密切合作。

https://www.bleepingcomputer.com/news/security/crypto-exchange-kraken-extorted-by-hackers-after-insider-breach/

**3. Chrome商店现超100个恶意扩展**

4月14日，官方Chrome网上应用商店中发现了超过100个恶意扩展程序，这些扩展试图窃取Google OAuth2 Bearer令牌、部署后门并进行广告欺诈。应用安全公司Socket的研究人员发现，这些恶意扩展是使用相同命令与控制（C2）基础设施的协同攻击活动的一部分。威胁行为者以五个不同的发布者身份在多个类别中发布了这些扩展，包括Telegram侧边栏客户端、老虎机和基诺游戏、YouTube和TikTok增强器、文本翻译工具和实用程序。研究人员表示，该攻击活动使用托管在Contabo VPS上的中央后端，多个子域分别处理会话劫持、身份收集、命令执行和货币化操作。Socket根据身份验证和会话窃取代码中的注释，发现了表明存在俄罗斯恶意软件即服务操作的证据。在数据采集和账户劫持方面，最大的集群包含78个扩展程序，通过innerHTML属性将攻击者控制的HTML注入到用户界面中。第二大组包含54个扩展程序，收集受害者的电子邮件、姓名、个人资料图片和Google帐户ID，同时窃取Google OAuth2 Bearer令牌。第三批45个扩展程序包含一个隐藏功能，该功能在浏览器启动时运行，充当后门，从C2服务器获取命令并打开任意URL，无需用户交互即可启动。

https://www.bleepingcomputer.com/news/security/over-100-chrome-extensions-in-web-store-target-users-accounts-and-data/

**4. Salesforce配置错误致McGraw-Hill数据泄露**

4月14日，教育巨头McGraw-Hill近日证实，因Salesforce配置错误，黑客成功访问了其内部数据。McGraw-Hill发言人表示，未经授权的访问似乎源于Salesforce环境配置错误，这是已影响多家与Salesforce合作的组织的更广泛问题的一部分。公司补充道，这不涉及对其Salesforce帐户、客户数据库、课件或内部系统的未经授权访问。在外部网络安全专家协助下，调查显示泄露信息不含社会保障号码、财务账户信息或来自其教育平台的学生数据。此番声明发布前，勒索组织ShinyHunters在其暗网门户上宣布McGraw-Hill成为受害者，并威胁称除非支付赎金，否则将在4月14日前泄露被盗数据。该威胁行为者声称掌握了4500万条Salesforce记录，其中包含个人身份信息，这与公司声称数据不敏感的说法相矛盾。McGraw-Hill表示，检测到未经授权活动后，受影响的网页已立即得到保护，公司正与Salesforce密切合作以进一步加强保护措施。

https://www.bleepingcomputer.com/news/security/mcgraw-hill-confirms-data-breach-following-extortion-threat/

**5. 成人夜总会巨头RCI Hospitality数据泄露**

4月14日，成人夜总会巨头RCI Hospitality Holdings近日披露了一起网络安全事件，导致敏感个人信息泄露。根据美国证券交易委员会的文件，该公司旗下子公司RCI Internet Services于3月23日发现，其IIS Web服务器中存在不安全的直接对象引用漏洞，导致个人信息遭到未经授权访问。本月初结束的调查显示，该事件实际始于3月19日。RCI表示，此次数据泄露涉及对“众多”独立承包商信息的未经授权访问，包括他们的姓名、出生日期、联系方式、社会保障号码和驾驶执照号码。公司向SEC强调，据其所知，未经授权的行为者尚未公开传播这些数据，同时客户信息和财务系统均未被访问。RCI还指出，其业务运营未受影响，并认为该事件不会对公司产生实质性影响。目前尚不清楚具体受影响人数，但RCI Hospitality是美国最大的成人夜总会运营商之一，旗下拥有数十家门店，包括Rick's和Tootsie's等品牌，业务组合还涵盖体育酒吧和舞厅。目前尚无已知的网络犯罪组织声称对此次攻击负责。

https://www.securityweek.com/nightclub-giant-rci-hospitality-reports-data-breach/

**6. ShowDoc严重漏洞CVE-2025-0520遭积极利用**

4月14日，在广受欢迎的文档管理和协作服务ShowDoc中，一个严重安全漏洞已被攻击者积极利用。该漏洞编号为CVE-2025-0520，CVSS评分为9.4分，属于严重级别。漏洞涉及不受限制的文件上传问题，源于对文件扩展名的验证不当，使得攻击者能够上传任意PHP文件并实现远程代码执行。据Vulhub发布的安全公告，在ShowDoc 2.8.7之前的版本中存在此问题，攻击者能够上传web shell并在服务器上执行任意代码。该漏洞已在ShowDoc版本2.8.7中得到修复，该版本于2020年10月发布，而软件的当前版本为3.8.1。根据VulnCheck安全研究副总裁Caitlin Condon分享的最新细节，CVE-2025-0520已首次遭到积极利用。已发现的攻击手段是利用该漏洞向位于美国的蜜罐投放Web Shell，该蜜罐运行着存在漏洞的ShowDoc版本。相关数据显示，目前有超过2000个ShowDoc实例在线，其中大部分位于中国。建议使用ShowDoc的用户更新至最新版本以获得最佳防护。

https://thehackernews.com/2026/04/showdoc-rce-flaw-cve-2025-0520-actively.html

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

启明星辰安全简讯

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5NPEia9QicL2tqPIIBFopSCpnTR53aDKfGxJFQlbrKwW7xwVk82pOt7MSic3AZwFUdDzYs6SUSC2lhrebJZoCfE2A/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过