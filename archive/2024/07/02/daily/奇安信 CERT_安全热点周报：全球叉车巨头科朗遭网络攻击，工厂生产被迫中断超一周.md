---
title: 安全热点周报：全球叉车巨头科朗遭网络攻击，工厂生产被迫中断超一周
url: https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501517&idx=3&sn=56dde274f6b48d17aaa8abd6682ee1b0&chksm=fe79e255c90e6b432c45877641e68cc82117089b5d92765940488a22bb5437ef88cfc02ea8ad&scene=58&subscene=0#rd
source: 奇安信 CERT
date: 2024-07-02
fetch_date: 2025-10-06T17:45:38.898327
---

# 安全热点周报：全球叉车巨头科朗遭网络攻击，工厂生产被迫中断超一周

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/EkibxOB3fs4ibZEau6qem7nTVx5egw0f4lFZ32ibZeWrKRajIyRs6XmZhwfKfqHm6Aj7l4qlH1kgTUPW2mGavTeibA/0?wx_fmt=jpeg)

# 安全热点周报：全球叉车巨头科朗遭网络攻击，工厂生产被迫中断超一周

奇安信 CERT

| **安全资讯导视** |
| --- |
| • 美国众议院议员提出《关键基础设施应急计划法案》 |
| • 印尼国家数据中心遭勒索攻击：边检等服务中断数天 超210个政府机构被波及 |
| • 全球叉车巨头科朗遭网络攻击，工厂生产被迫中断超一周 |

**PART****0****1**

**漏洞情报**

**1.GitLab身份认证绕过漏洞安全风险通告**

6月28日，奇安信CERT监测到官方修复GitLab身份认证绕过漏洞(CVE-2024-5655)，攻击者可以在某些情况下以其他用户的身份触发pipeline，从而造成身份验证绕过。奇安信鹰图资产测绘平台数据显示，CVE-2024-5655关联的国内风险资产总数为1595223个，关联IP总数为112251个。鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**2.Progress MOVEit Transfer身份认证绕过漏洞安全风险通告**

6月26日，奇安信CERT监测到Progress MOVEit Transfer身份认证绕过漏洞(CVE-2024-5806)在互联网上公开，该漏洞是一个严重的认证绕过缺陷，它使得攻击者能够在没有任何有效凭证的情况下，通过特定的技术手段来冒充服务器上的任何用户，从而获取对敏感数据的未授权访问。奇安信鹰图资产测绘平台数据显示，CVE-2024-5806关联的国内风险资产总数为6637个，关联IP总数为227个。目前该漏洞技术细节与PoC已在互联网上公开，鉴于此漏洞影响范围较大，建议客户尽快做好自查及防护。

**3.Ollama远程代码执行漏洞安全风险通告**

6月25日，奇安信CERT监测到官方修复Ollama远程代码执行漏洞(CVE-2024-37032)，在没有强制身份验证的Ollama服务器上，攻击者可通过操控服务器接口下载恶意文件，从而导致远程代码执行。奇安信鹰图资产测绘平台数据显示，CVE-2024-37032关联的国内风险资产总数为3955个，关联IP总数为994个。目前该漏洞技术细节与EXP已在互联网上公开，鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**4.Apache Kafka UI远程代码执行漏洞安全风险通告**

6月24日，奇安信CERT监测到官方修复Apache Kafka UI远程代码执行漏洞(CVE-2024-32030)，Kafka UI API提供了一种功能，允许用户连接到不同的Kafka代理并监控它们的表现。这个功能存在一个安全漏洞，攻击者可以利用JMX的RMI协议进行反序列化攻击。如果攻击者能够设置一个恶意的JMX监听器，当Kafka UI尝试连接并获取监控数据时，攻击者可以发送一个恶意的序列化对象，导致Kafka UI执行远程代码。奇安信鹰图资产测绘平台数据显示，CVE-2024-32030关联的国内风险资产总数为3339个，关联IP总数为1241个。目前该漏洞技术细节与EXP已在互联网上公开，鉴于该漏洞影响范围较大，建议客户尽快做好自查及防护。

**PART****0****2**

**安全事件**

**1.印尼国家数据中心遭勒索攻击：边检等服务中断数天 超210个政府机构被波及**

6月24日路透社消息，印度尼西亚通信部长透露，一名网络攻击者入侵了该国国家数据中心，干扰了机场的边检工作，导致出入境柜台排起了长队。据悉，位于泗水的印尼国家数据中心在上周遭到Lockbit勒索软件变种攻击，导致超过210家中央和地方政府机构受到波及，其中以移民边检服务受影响最为严重，中断了约3天时间，攻击者向其索要800万美元赎金。印尼通信部官员Semuel Abrijani Pangerapan表示，数字取证调查正在进行中，目前尚未找到更多细节。

原文链接：

https://www.reuters.com/technology/cybersecurity/cyber-attack-compromised-indonesia-data-centre-ransom-sought-reports-antara-2024-06-24/

**2.猴痘病毒爆发期，南非国家卫生实验室因勒索攻击中断服务**

6月24日MyBroadband消息，南非国家卫生实验室服务局（NHLS）上周末遭到入侵，已关闭IT系统。该部门的电子邮件、网站以及检索和存储患者实验室测试结果的系统均已离线。NHLS首席执行官Koleka Mlisana教授发布备忘录，表示入侵造成了损害，说明NHLS遭受了勒索软件感染或类似的破坏性攻击。为应对此次攻击，NHLS已经实施了“停机协议”，以确保提供必要的资源来解决这种情况。当前南非正处于猴痘病毒爆发期，NHLS此前积压了大量待检测样本。此次攻击虽然未影响NHLS的内部运转，但IT中断导致其无法和外界进行数据通信，只能依赖电话或打印机来传递紧急测试结果。

原文链接：

https://mybroadband.co.za/news/security/541863-critical-south-african-healthcare-services-hacked.html

**3.全球叉车巨头科朗遭网络攻击，工厂生产被迫中断超一周**

6月19日Bleeping Computer消息，美国叉车制造巨头科朗设备（Crown Equipment）确认，本月早些时候遭受了一次网络攻击，导致其工厂的制造活动中断。大约6月8日起，科朗员工陆续报告公司遭遇了安全入侵，所有IT系统关闭。员工被告知不要接受多因素认证（MFA）请求，并对网络钓鱼邮件保持警惕。由于IT系统关闭，员工无法记录工时、访问服务手册，在某些情况下也无法交付机械设备。据悉，这次入侵是因为一名科朗员工遭到社交工程攻击，使得威胁行为者在他的电脑上安装远程访问软件。

原文链接：

https://www.bleepingcomputer.com/news/security/crown-equipment-confirms-a-cyberattack-disrupted-manufacturing/

**PART****0****3**

**政策法规**

**1.《网络安全标准实践指南——大型互联网平台网络安全评估指南》发布**

6月28日，全国网络安全标准化技术委员会秘书处组织编制发布《网络安全标准实践指南——大型互联网平台网络安全评估指南》。该文件从影响或者可能影响社会稳定和公共利益的角度，提出了对大型互联网平台开展网络安全评估的内容和方法，适用于对大型互联网平台开展网络安全评估活动。该文件提出，大型互联网平台需要设立网络安全评估工作组，每年组织开展一次网络安全评估，评估内容包括核心业务连续性风险、灾难恢复能力、关键软硬件产品供应链安全性、对外提供数据的可控性、数据泄露事件发生后应急处置、平台控制权、用户权益保护等。

原文链接：

https://www.tc260.org.cn/upload/2024-06-26/1719392765857029020.pdf

**2.美国防部发布《支点：国防部信息技术发展战略》**

6月25日，美国国防部发布《支点：国防部信息技术推进战略》，旨在利用技术力量推动变革并催化作战人员数字化现代化，为更好地协调信息技术运用以推进美国防部优先事项提供路线图。该战略提出了四条工作方向，以确保美国防部能够继续为国家的作战人员及其支持人员提供联系、保护并执行任务，具体包括提供联合作战信息技术能力、实现信息网络与计算现代化、优化信息技术治理、培养一支卓越的数字化人才队伍。

原文链接：

https://dodcio.defense.gov/Portals/0/Documents/Library/FulcrumAdvStrat.pdf

**3.《网络安全标准实践指南— 一键停止收集车外数据指引》公开征求意见**

6月24日，全国网络安全标准化技术委员会秘书处组织编制了《网络安全标准实践指南— 一键停止收集车外数据指引（征求意见稿）》，现公开征求意见。该文件给出了在装有车载摄像头、雷达等传感器的汽车上设置一键停止收集车外数据功能的指引，适用于汽车制造企业以及相关零部件或服务提供商设计、开发、制造具有车外数据收集功能的汽车，不适用于主驾无人的高级别自动驾驶汽车。该文件旨在减少由于车载摄像头和雷达设备持续开启造成的重要数据和敏感个人信息违规收集、处理等安全问题，使汽车的辅助驾驶功能更好地应用。

原文链接：

https://www.tc260.org.cn/upload/2024-06-24/1719196611263024551.pdf

**4.美国众议院议员提出《关键基础设施应急计划法案》**

6月18日，美国众议院常设情报委员会成员Dan Crenshaw、众议院国土安全委员会成员Seth Magaziner共同提出《关键基础设施应急计划法案》，要求要求美国网络安全和基础设施安全局局长与联邦紧急事务管理局局长及其他部门风险管理机构合作，向国会提交一份部门间联合评估报告，评估网络攻击期间关键基础设施的手动操作。具体评估内容包括关键基础设施无法迅速切换手动操作时国家网络事件响应计划的预案、CISA支持关键基础设施事件响应的能力与义务、FEMA国家响应框架对关键基础设施的支持情况、关键基础设施切换手动操作面临的潜在成本和挑战等。

原文链接：

https://crenshaw.house.gov/2024/6/crensahw-magaziner-introduce-the-contingency-plan-for-critical-infrastructure-act

**往期精彩推荐**

[GitLab身份认证绕过漏洞(CVE-2024-5655)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501489&idx=1&sn=46fdad1e31db9b8afd7fbdffd013e99b&chksm=fe79e229c90e6b3fdc41aede2ee6f73de9a07fbe418172d18b19199e5501d5d87a2cc139c3ef&token=2060213078&lang=zh_CN&scene=21#wechat_redirect)
[【已复现】Ollama 远程代码执行漏洞(CVE-2024-37032)安全风险通告第二次更新](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501474&idx=1&sn=ab0e32fa5ac1ec16b77b0fa38e76d18f&chksm=fe79e23ac90e6b2c6f110936d0dfb4f694ea475c06d54e21bc9d7f4187a82ed6ef45ce946acc&token=2060213078&lang=zh_CN&scene=21#wechat_redirect)

[Progress MOVEit Transfer身份认证绕过漏洞(CVE-2024-5806)安全风险通告](https://mp.weixin.qq.com/s?__biz=MzU5NDgxODU1MQ==&mid=2247501462&idx=1&sn=77865454524301f0f45e10383f0a5e02&chksm=fe79e20ec90e6b186b96468a2f782f0efd926a4f2680e6e613e2a2da5416ce188ef5d19dc72e&token=2060213078&lang=zh_CN&scene=21#wechat_redirect)

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