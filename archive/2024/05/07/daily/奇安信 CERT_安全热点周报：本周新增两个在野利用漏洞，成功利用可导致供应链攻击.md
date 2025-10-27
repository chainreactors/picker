---
title: 安全热点周报：本周新增两个在野利用漏洞，成功利用可导致供应链攻击
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247500982&idx=1&sn=01f21b986415a5a6d16103d6efda5b2e&chksm=fe79e02ec90e6938aa007712dd3277dd23f48b046149ac9b8a0a5ad975ca5288215b981f9c85&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-05-07
fetch_date: 2025-10-06T17:18:08.165894
---

# 安全热点周报：本周新增两个在野利用漏洞，成功利用可导致供应链攻击

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4ic20qf4bS0zQn8T3CNYzZfM7VsadJCukqN9A88j1c3xekvTibeNODFibT95icbdzUySZX7vYLVDv6A5w/0?wx_fmt=jpeg)

# 安全热点周报：本周新增两个在野利用漏洞，成功利用可导致供应链攻击

奇安信 CERT

| **安全资讯导视** |
| --- |
| • 美国总统拜登签署《关于关键基础设施安全和弹性的国家安全备忘录》 |
| • 两部门印发《数字经济2024年工作要点》 |
| • 伦敦证交所客户核查数据库遭泄露，内含超520万条敏感个人信息 |

**PART****0****1**

**新增在野利用**

**1.****GitLab密码重置漏洞(CVE-2023-7028)**

GitLab 社区版和企业版包含不适当的访问控制漏洞。这允许攻击者触发密码重置电子邮件发送到未经验证的电子邮件地址，最终促进帐户接管。

美国网络安全和基础设施安全局（CISA）在其已知利用漏洞（KEV）目录中添加了一个影响 GitLab 的严重漏洞，原因是该漏洞在野外被广泛利用。最大严重性漏洞被跟踪为 CVE-2023-7028（CVSS 评分：10.0），可通过向未经验证的电子邮件地址发送密码重置电子邮件来促进帐户接管。GitLab 在今年 1 月早些时候披露了该缺陷的细节，并表示它是作为 2023 年 5 月 1 日 16.1.0 版代码更改的一部分引入的。

“在这些版本中，所有身份验证机制都会受到影响，”该公司当时指出。“此外，启用了双因素身份验证的用户容易受到密码重置的影响，但不会被帐户接管，因为他们需要第二个身份验证因素才能登录。”

成功利用该问题可能会产生严重后果，因为它不仅使攻击者能够控制 GitLab 用户帐户，而且还会窃取敏感信息、凭据，甚至使用恶意代码毒害源代码存储库，从而导致供应链攻击。

该缺陷已在 GitLab 版本 16.5.6、16.6.4 和 16.7.2 中得到解决，补丁也向后移植到版本 16.1.6、16.2.9、16.3.7 和 16.4.5。

参考链接：

https://thehackernews.com/2024/05/cisa-warns-of-active-exploitation-of.html

**2.SmartScreen Prompt安全特性绕过漏洞(CVE-2024-29988)**

Microsoft 默默修补的第二个零日漏洞被跟踪为 CVE-2024-29988，并被描述为由保护机制故障弱点导致的 SmartScreen Prompt 安全功能绕过漏洞。

CVE-2024-29988 绕过了 CVE-2024-21412 漏洞，由 Trend Micro Zero Day Initiative 的 Peter Girnus 和 Google 威胁分析小组的 Dmitrij Lenz 和 Vlad Stolyarov 报告。ZDI 的威胁意识主管 Dustin Childs 在逃避 EDR/NDR 检测并绕过 Web 标记（MotW）功能后，将其标记为积极用于攻击，以在目标 Windows 系统上部署恶意软件。

利用 CVE-2024-29988 的出于经济动机的 Water Hydra 黑客组织还利用 CVE-2024-21412 作为新年前夜的零日漏洞，以针对外汇交易论坛和股票交易 Telegram 频道进行鱼叉式网络钓鱼攻击，这些攻击部署了 DarkMe 远程访问木马（RAT）。

Microsoft 于 2024 年 4 月发布了安全更新，解决了多个产品中的 147 个漏洞 。

参考链接：

https://www.bleepingcomputer.com/news/security/over-1-400-crushftp-servers-vulnerable-to-actively-exploited-bug/

**PART****0****2**

**安全事件**

**1.伦敦证交所客户核查数据库遭泄露，内含超520万条敏感个人信息**

4月26日Cybernews消息，伦敦证券交易所集团旗下的客户核查数据库World-Check遭到泄露，自称GhostR的用户在知名数据泄露论坛上发帖称，在3月获取了该数据库，内含超520万条记录。World-Check数据库可供金融机构执行“了解您的客户”（KYC）核查，其中包括有关政治公众人物、情报人员、犯罪分子、高风险组织和其他机构的记录，具体涵盖个人姓名、职务、背景信息、实体名称、列入名单原因等。伦敦证交所表示，内部系统没有漏洞，数据系攻击者从客户端非法获取。

原文链接：

https://cybernews.com/news/lseg-world-check-database-leak/

**PART****0****3**

**政策法规**

**1.两部门联合印发《关于支持引导公路水路交通基础设施数字化转型升级的通知》**

5月1日，财政部、交通运输部联合印发《关于支持引导公路水路交通基础设施数字化转型升级的通知》，决定通过竞争性评审方式支持引导公路水路交通基础设施数字化转型升级。该文件提出，通过3年左右时间，力争推动85%左右的繁忙国家高速公路、25%左右的繁忙普通国道和70%左右的重要国家高等级航道实现数字化转型升级。该文件要求坚持场景牵引，推动融合创新，以保障数据安全为前提，探索数据资源多样化有偿使用方式，促进数据多场景应用、多主体复用，释放数据要素价值。

原文链接：

https://jjs.mof.gov.cn/zhengcefagui/202404/t20240430\_3933946.htm

**2.美国国防信息系统局发布未来五年战略计划**

5月1日，美国国防信息系统局（DISA）发布2025年至2029年战略，概述该机构未来五年的四项战略性要务、六项作战性要务以及八项转型目标。该战略指出，DISA是负责美国防部信息系统网络的战斗支援机构，职责是改造和整合能力和服务以便为美国防部提供最佳支持；DISA支持2022年美国国防战略所有四个优先事项；该战略明确了DISA计划提供的功能和服务，以改造国防部信息系统，应对美国国防战略中描述的挑战；该战略的核心是四项战略性要务、六项作战性要务和八项目标，其中前两个战略性要务和四个作战性要务描述了DISA的日常任务，后两个战略性要务以及两个作战性要务描述了与美国国防战略第四优先事项相一致的5到10年期机构转型展望，八个目标是DISA在未来五年内重点关注的特定转型领域。

原文链接：

https://content.govdelivery.com/attachments/USDISA/2024/04/11/file\_attachments/2843922/DISA%20Next%20Strategy%202025-2029.pdf

**3.美国总统拜登签署《关于关键基础设施安全和弹性的国家安全备忘录》**

4月30日，美国总统拜登签署《关于关键基础设施安全和弹性的国家安全备忘录》（NSM-22），取代奥巴马时期2013年发布的关键基础设施保护总统政策文件PPD-21，保护美国基础设施免受当前和未来的所有威胁和损害。该文件提出四方面要求，一是授权国土安全部领导美国关键基础设施安全的政府方面工作，其中网络安全与基础设施安全局担任国家安全与弹性协调员；二是美国情报界应与联邦、州和地方合作伙伴及关键基础设施所有者和运营者共享情报信息；三是重申指定的16个关键基础设施行业和行业风险管理机构；四是提高关键基础设施行业内和行业间的最低安全与弹性要求，与国家网络战略保持一致。

原文链接：

https://www.whitehouse.gov/briefing-room/presidential-actions/2024/04/30/national-security-memorandum-on-critical-infrastructure-security-and-resilience/

**4.两部门印发《数字经济2024年工作要点》**

4月29日，国家发展改革委办公厅、国家数据局综合司印发《数字经济2024年工作要点》，对2024年数字经济重点工作作出部署。该文件提出九项举措，其中第七条为全面筑牢数字安全屏障，增强网络安全防护能力，健全数据安全治理体系，切实有效防范各类风险。

原文链接：

https://mp.weixin.qq.com/s/J7IIaRjUUR5TrNeabWyvuQ

**往期精彩推荐**

[安全热点周报：本周新增四个在野利用漏洞，针对政府和关基设施](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247500972&idx=1&sn=76f2036a679167d999bb5aefc9a21c81&chksm=fe79e034c90e6922aada9fb5ebd36ed81255b6e86fea50274dbd5436164b1b57bd449b0a514c&token=678709104&lang=zh_CN&scene=21#wechat_redirect)
[【已复现】禅道项目管理系统身份认证绕过漏洞(QVD-2024-15263)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247500966&idx=1&sn=b2381db40cdcfaf82c940940a972b5ad&chksm=fe79e03ec90e6928d188b1786a992f9b14466aac0e739ea372a3d25f4750800b550f9cf189bc&token=1868312225&lang=zh_CN&scene=21#wechat_redirect)

[【已复现】CrushFTP 服务器端模板注入漏洞(CVE-2024-4040)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247500949&idx=1&sn=0884b6bc0d1ab6b385ac694edc308959&chksm=fe79e00dc90e691b2a23da9cc5733683ee02964bc21cb1b301bc50c52b6088962d9e57e26dea&token=1868312225&lang=zh_CN&scene=21#wechat_redirect)

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