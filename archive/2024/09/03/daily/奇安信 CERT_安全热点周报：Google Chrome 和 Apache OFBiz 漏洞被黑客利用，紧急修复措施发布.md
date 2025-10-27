---
title: 安全热点周报：Google Chrome 和 Apache OFBiz 漏洞被黑客利用，紧急修复措施发布
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501978&idx=1&sn=61c623acad92737f00bcef0c5d233829&chksm=fe79ec02c90e6514f2a3f9dfa4c965e4bd2f7564b0fbb65741aed98ae042d7200a125f983d3c&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-09-03
fetch_date: 2025-10-06T18:26:04.839956
---

# 安全热点周报：Google Chrome 和 Apache OFBiz 漏洞被黑客利用，紧急修复措施发布

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4ibtkZC7OweXsswLbxYhribNf5QAIOmr0KPKhNU0ukBNda5iaictlXOXSXweeEAGerqQWiaPC7fnCBRJjg/0?wx_fmt=jpeg)

# 安全热点周报：Google Chrome 和 Apache OFBiz 漏洞被黑客利用，紧急修复措施发布

奇安信 CERT

| **安全资讯导视** |
| --- |
| • 李强主持召开国务院常务会议，审议通过《网络数据安全管理条例（草案）》 |
| • 美国加州议会通过人工智能法案 |
| • 全球石油巨头哈里伯顿因网络攻击被迫关闭系统 |

**PART****0****1**

**漏洞情报**

**1.Windows TCP/IP IPv6远程拒绝服务/代码执行漏洞(CVE-2024-38063)POC已公开安全风险通告**

8月27日，奇安信CERT 8月15日监测到微软发布8月补丁日安全更新修复Windows TCP/IP远程代码执行漏洞(CVE-2024-38063)，Windows TCP/IP组件中发现了一个整数下溢漏洞，可能会触发缓冲区溢出。未经身份验证的远程攻击者可以通过发送特制的IPv6数据包到目标Windows系统机器导致目标蓝屏崩溃，精心构造请求理论上存在远程代码执行的可能性。该漏洞影响了所有受IPv6支持的Windows版本，包括即将发布的Windows 11版本24H2。禁用IPv6的系统不受此漏洞的影响，但对于启用IPv6的系统，存在很大的利用风险。该漏洞被微软标记较大可能被利用，鉴于此漏洞影响范围较大，建议客户尽快做好自查及防护。目前，奇安信威胁情报中心安全研究员已成功复现该漏洞，强烈建议马上安装补丁。

**PART****0****2**

**新增在野利用**

**1.****Google Chrome 缓冲区溢出漏洞(CVE-2024-7965)**

8月 28 日，美国网络安全和基础设施安全局 (CISA) 在其已知利用漏洞 (KEV) 目录中添加Google Chrome 缓冲区溢出漏洞(CVE-2024-7965)，谷歌透露，上周推出的 Chrome 浏览器软件更新中修补的一个安全漏洞已被广泛利用。该漏洞被编号为CVE-2024-7965，被描述为 V8 JavaScript 和 WebAssembly 引擎中的一个不适当的实现错误。

根据国家漏洞数据库 (NVD) 中对该漏洞的描述，“128.0.6613.84 之前的 Google Chrome 中 V8 的不适当实现允许远程攻击者通过精心设计的 HTML 页面利用堆损坏漏洞。”

一位网络化名为 TheDog 的安全研究员于 2024 年 7 月 30 日发现并报告了该漏洞，并因此获得了 11,000 美元的漏洞赏金。

关于利用该漏洞的攻击性质或可能利用该漏洞的威胁者身份的更多细节尚未公布。不过，这家科技巨头承认，它知道漏洞 CVE-2024-7965 的存在。

谷歌表示：“在大多数用户更新修复程序之前，对错误详细信息和链接的访问可能会受到限制。”“如果其他项目同样依赖但尚未修复的第三方库中也存在该错误，我们也将保留限制。”

强烈建议用户将 Windows 和 macOS 版 Chrome 升级到 128.0.6613.84/.85 版本，将 Linux 版升级到 128.0.6613.84 版本，以减轻潜在威胁。

参考链接：

https://thehackernews.com/2024/08/google-warns-of-cve-2024-7965-chrome.html

**2.Apache OFBiz 授权不当致代码执行漏洞(CVE-2024-38856)**

8月 27 日，美国网络安全和基础设施安全局 (CISA) 已发出紧急警告，称流行的开源企业资源规划 (ERP) 系统 Apache OFBiz 中存在一个被积极利用的安全漏洞。该漏洞被追踪为 CVE-2024-38856，已被添加到 CISA 的已知被利用漏洞 (KEV) 目录中，凸显了该威胁的严重性。

CVE-2024-38856 是一个授权不当致远程代码执行漏洞。该漏洞影响 18.12.15 之前的 Apache OFBiz 版本，对任何使用旧版本软件的组织都构成重大风险。

CVE-2024-38856 的根本原因在于 Apache OFBiz 的身份验证机制中的一个缺陷。具体来说，这个缺陷允许未经身份验证的用户访问通常仅限于登录用户使用的功能。一旦进入系统，攻击者可以利用此访问权限在受感染的系统上执行任意代码，从而可能导致整个系统被入侵。

发现并报告 CVE-2024-38856 的安全公司 SonicWall 强调，该漏洞存在于 Apache OFBiz 的覆盖视图功能中。这一严重漏洞将重要端点暴露给未经身份验证的攻击者，攻击者可以通过发送特制请求来利用该漏洞。

更为紧迫的是，SecureLayer7 的网络安全研究人员 Zeyad Azima 和 Youssef Muhammad 发布了针对 CVE-2024-38856 的概念验证 (PoC) 漏洞代码。此 PoC 在 GitHub 上具体展示了如何利用该漏洞，这使得黑客更容易发动攻击。

鉴于 CVE-2024-38856 的高严重性和活跃利用，CISA 强烈建议所有使用 Apache OFBiz 的机构和组织在 2024 年 9 月 17 日之前将其安装更新至 18.12.15 或更高版本。未能应用这些更新可能会导致系统容易受到攻击，从而导致数据泄露、服务中断和其他严重后果。

参考链接：

https://securityonline.info/cisa-warns-of-actively-exploited-apache-ofbiz-cve-2024-38856-vulnerability-poc-available/

**3.****Google Chrome V8 类型混淆漏洞(CVE-2024-7971)**

8月 26 日，美国网络安全和基础设施安全局 (CISA) 在其已知利用漏洞 (KEV) 目录中添加 Google Chrome V8 类型混淆漏洞(CVE-2024-7971)，朝鲜黑客利用最近修补的 Google Chrome 零日漏洞 (CVE-2024-7971)，在利用 Windows 内核漏洞获取系统权限后部署 FudModule 根工具包。

微软周五表示：“我们高度确信，观察到的对 CVE-2024-7971 的利用可以归因于朝鲜黑客，他们针对加密货币领域以此获取经济利益”，并将这些攻击归咎于 Citrine Sleet（之前被追踪为DEV-0139）。

其他网络安全供应商将该朝鲜威胁组织追踪为 AppleJeus、Labyrinth Chollima 和 UNC4736，而美国政府则将朝鲜政府资助的黑客统称为 Hidden Cobra。

谷歌上周修补了 CVE-2024-7971 零日漏洞，称其为 Chrome V8 JavaScript 引擎中的类型混淆漏洞。此漏洞使黑客能够在重定向到攻击者控制的网站 voyagorclub[.]space 的目标的沙盒 Chromium 渲染器进程中获得远程代码执行。逃离沙盒后，他们使用受感染的 Web 浏览器下载了针对 Windows 内核中的 CVE-2024-38106 漏洞，这使他们获得了 SYSTEM 权限。

黑客还下载并加载了 FudModule 根工具包到内存中，用于内核篡改和直接内核对象操作 (DKOM)，并允许他们绕过内核安全机制。

雷德蒙德补充道，利用 CVE-2024-7971 Chrome 零日漏洞进行攻击的目标组织之一此前也曾被另一个朝鲜威胁组织 BlueNoroff（或 Sapphire Sleet）瞄准。

建议用户将 Windows 和 macOS 版 Chrome 升级到 128.0.6613.84/.85 版本，将 Linux 版升级到 128.0.6613.84 版本，以减轻潜在威胁。还建议基于 Chromium 的浏览器（例如 Microsoft Edge、Brave、Opera 和 Vivaldi）的用户在修复程序可用时立即应用。

参考链接：

https://www.bleepingcomputer.com/news/security/north-korean-hackers-exploit-chrome-zero-day-to-deploy-rootkit/

**PART****0****3**

**安全事件**

**1.网络攻击迫使美国超级机场IT系统瘫痪、航班延误**

8月26日Bleeping Computer消息，美国西北太平洋沿岸地区最繁忙的机场西雅图-塔科马国际机场确认，日前出现的IT系统中断可能是由网络攻击引起，这一中断扰乱了预订和登机手续系统，并导致航班延误。西雅图港8月24日警告称，港口和塔科马机场因为“可能的网络攻击”正在遭受持续中断。为了控制影响范围，他们被迫隔离某些关键系统。西雅图港在推特上表示：“西雅图港，包括西雅图-塔科马机场，正在经历互联网和网络系统中断，这影响了机场的某些系统。我们建议乘客与航空公司联系，以获取航班的最新信息。有机场乘客报告称，由于多家航空公司手工签发机票，旅客排起了长队。当地媒体报道，“数千”个旅客受到影响。据悉，航站楼的显示屏也遇到了技术问题，进一步加剧了混乱。

原文链接：

https://www.bleepingcomputer.com/news/security/seattle-tacoma-airport-it-systems-down-due-to-a-cyberattack/

**2.马来西亚国家基建公司遭勒索攻击疑泄露超300GB数据**

8月26日FMT消息，马来西亚公共交通服务商国家基建公司（Prasarana Malaysia Berhad）确认，社交媒体上关于其内部系统部分被未经授权访问的网络安全事件的报道属实。该公司声明称，此次事件并未影响其日常运营，公司正与网络安全专家合作，调查并缓解这一情况，但并未透露是否有泄漏数据的情况。这份声明意在回应社交媒体关于其网站可能因勒索软件攻击而导致316GB数据泄露的报道。8月25日夜间，网络安全平台Falcon Feeds.io在推特上发帖称， RansomHub勒索软件组织威胁将在6到7天内公布国家基建公司的数据。

原文链接：

https://www.freemalaysiatoday.com/category/nation/2024/08/26/prasarana-confirms-cybersecurity-incident/

**3.全球石油巨头哈里伯顿因网络攻击被迫关闭系统**

8月24日The Record消息，美国油田巨头哈里伯顿（Halliburton）22日提交SEC报告披露，21日遭遇了一次网络攻击，影响了休斯敦总部的运营。该公司表示黑客“获取了部分系统的访问权限”。哈里伯顿副总裁Charles Geer表示：“公司采取了多项应对措施。为了保护某些系统，我们选择将其主动下线，并通知执法部门。公司正在实施的调查和应对措施包括系统恢复和事件严重性评估。”  据路透社报道称，作为网络攻击后的预防措施，哈里伯顿告知一些员工不要连接公司的内部网络。

原文链接：

https://therecord.media/halliburton-systems-offline-cyberattack-sec

**PART****0****4**

**政策法规**

**1.李强主持召开国务院常务会议，审议通过《网络数据安全管理条例（草案）》**

8月30日，国务院总理李强8月30日主持召开国务院常务会议，审议通过《网络数据安全管理条例（草案）》。会议指出，要对网络数据实行分类分级保护，明确各类主体责任，落实网络数据安全保障措施。要厘清安全边界，保障数据依法有序自由流动，为促进数字经济高质量发展、推动科技创新和产业创新营造良好环境。

原文链接：

https://mp.weixin.qq.com/s/BouiuxZSCCDYUXDswpLF9A

**2.《网络安全技术 网络安全试验平台 体系架构》等3项国家标准公开征求意见**

8月30日，全国网络安全标准化技术委员会归口的《网络安全技术 网络安全试验平台 体系架构》等3项国家标准现已形成标准征求意见稿，公开征求意见。据悉，《网络安全技术 网络安全试验平台 体系架构》给出了网络安全试验平台的参考体系架构，包括总体架构、组件功能和安全性设计，并提供了组件间工作过程参考；《网络安全技术 网络空间安全图谱要素表示要求》规定了网络空间安全图谱要素分类、代码与图形符号表达；《数据安全技术 二手电子产品信息清除技术要求》规定了二手电子产品信息清除各个环节应遵循的技术要求。

原文链接：

https://www.secrss.com/articles/69682

**3.国家标准《网络安全技术 网络安全 第7部分：网络虚拟化安全》公开征求意见**

8月29日，全国网络安全标准化技术委员会归口的国家标准《网络安全技术 网络安全 第7部分：网络虚拟化安全》现已形成标准征求意见稿，公开征求意见。该文件旨在识别网络虚拟化安全风险，并为网络虚拟化的安全实施提供指引。  总体上，本文件目标在于为组织虚拟化安全的全面定义和实施提供帮助，适用于负责实施和维护安全虚拟化环境并进行相应技术控制的用户和实施者。

原文链接：

https://www.tc260.org.cn/file/2024-08-28/1dff8699-4351-44e3-b6e5-04901439b11c.docx

**4.美国加州议会通过人工智能法案**

8月28日，美国加利福尼亚州议会通过了《前沿人工智能模型安全创新法案》（编号SB 1047），下一步将提交至州长审议。该法案旨在为训练成本超过1亿美元或者达到一定算力的开发商制定安全标准，确保大规模人工智能模型的安全开发。法案要求对先进人工智能模型进行安全测试，确保该技术不会造成“严重伤害”，并要求开发人员设置终止开关，赋予州检察长在开发商不遵守规定时提起诉讼的权力等。该法案部分条款引发了科技公司和立法者之间关于“扼杀创新”的激烈争论。

原文链接：

https://sd11.senate.ca.gov/news/senator-wieners-landmark-ai-bill-heads-governor

**5.工信部、国家标准委联合印发《物联网标准体系建设指南（2024版）》**

8月26日，工业和信息化部、国家标准化管理委员会联合印发《物联网标准体系建设指南（2024版）》。该文件提出，物联网标准体系框架由基础标准、技术标准、建设运维标准、应用标准四大类组成。其中，基础标准包含安全可信分类，用于规范物联网终端、网络、平台（系统）、网关等关键构成部分的安全、可信要求及保障措施，包括物联网安全架构、安全分级、终端安全、传输安全、数据安全、平台（系统）安全、安全管理等标准，及物联网可信架构、可信分级、身份可信、数据可信、系统可信等标准。

原文链接：

https://www.miit.gov.cn/cms\_files/demo/pdfjs/web/viewer.html?file=/cms\_files/filemanager/1226211233/attach/20248/e016570c006f47c69fadc242743e27cc.pdf

**往期精彩推荐**

[【可用POC已公开】Windows TCP/IP IPv6远程拒绝服务/代码执行漏洞(CVE-2024-38063)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501973&idx=1&sn=642d4586d72419c24fb9052198320549&chksm=fe79ec0dc90e651b10a86079648e6917eb2dbf036e82b5833086f1ab978545cd46a0be548cbc&token=864708754&lang=zh_CN&scene=21#wechat_redirect)
[安全热点周报：本周新增两个在野利用漏洞，其中 Jenkins 被用于勒索软件活动](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501958&idx=1&sn=699c44f8f8bd7c4117f7087e0679f1cc&chksm=fe79ec1ec90e650868504d18670940d929eeb11730143860236c9b3566a8f2bc97c5cc33f4fa&token=864708754&lang=zh_CN&scene=21#wechat_redirect)

[【在野利用】Google Chrome V8 类型混淆漏洞(CVE-2024-7971)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501953&idx=1&sn=132f57d74ad27b44fc64a22b6f3c081b&chksm=fe79ec19c90e650f6fc4cdbadd1d11b32abe1cebf4128b9c74a56acbe9bbdabb4039e5c11b91&token=864708754&lang=zh_CN&scene=21#wechat_redirect)

本期周报内容由安全内参&虎符智库&奇安信CERT联合出品！

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

奇安信 CERT

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/EkibxOB3fs4ic3Dr2nTQbrt9ZdsEIxjK36YibkxgDHpwdDIFJvShiaib2ia3lzIIVqEeDNDEib9WNuZ1IdcjgUWIWGWKw/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，...