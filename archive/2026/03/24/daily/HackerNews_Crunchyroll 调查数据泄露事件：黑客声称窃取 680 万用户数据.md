---
title: Crunchyroll 调查数据泄露事件：黑客声称窃取 680 万用户数据
url: https://hackernews.cc/archives/63939
source: HackerNews
date: 2026-03-24
fetch_date: 2026-03-25T04:16:21.456599
---

# Crunchyroll 调查数据泄露事件：黑客声称窃取 680 万用户数据

![](http://hackernews.cc/wp-includes/images/HackerNews_b.png)

![hackernews_logo](http://hackernews.cc/wp-includes/images/HackerNews_w.png)

* [首页](http://hackernews.cc)
* [今日推送](https://hackernews.cc/archives/category/%E4%BB%8A%E6%97%A5%E6%8E%A8%E9%80%81)
* [国际动态](https://hackernews.cc/archives/category/%E5%9B%BD%E9%99%85%E5%8A%A8%E6%80%81)
* [漏洞事件](https://hackernews.cc/archives/category/%E6%BC%8F%E6%B4%9E%E4%BA%8B%E4%BB%B6)
* [黑客事件](https://hackernews.cc/archives/category/%E9%BB%91%E5%AE%A2%E4%BA%8B%E4%BB%B6)
* [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
* [推荐阅读](https://hackernews.cc/archives/category/%E6%8E%A8%E8%8D%90%E9%98%85%E8%AF%BB)

![可用-僵尸网络 恶意代码](https://hackernews.cc/wp-content/uploads/2026/02/tumisu-cyber-security-3410923_1920.jpg)

# Crunchyroll 调查数据泄露事件：黑客声称窃取 680 万用户数据

作者: [hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews")
日期: [2026-03-24](https://hackernews.cc/archives/63939 "09:59")
分类: [数据泄露](https://hackernews.cc/archives/category/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)
[暂无评论](https://hackernews.cc/archives/63939#respond)

* 浏览次数 164
* 喜欢 0
* 评分 12345

**HackerNews 编译，转载请注明出处：**

知名动漫流媒体平台Crunchyroll正在调查一起数据泄露事件，此前黑客声称窃取了约680万人的个人信息。

Crunchyroll最初向BleepingComputer表示：”我们已注意到相关声明，正与顶尖网络安全专家密切合作调查此事。”

在后续声明中，Crunchyroll补充道：”调查正在进行中，我们继续与网络安全专家合作。目前我们认为，泄露信息主要限于客户服务工单数据，源于第三方供应商的一起事件。我们尚未发现与这些声明相关的系统持续访问证据，正密切监控事态发展。”

此前，一名威胁行为体于上周四联系BleepingComputer，**声称于美国东部时间3月12日晚9点入侵Crunchyroll，通过获取Crunchyroll支持人员的Okta SSO账户权限实施攻击。**

该支持人员据称是Telus International业务流程外包（BPO）公司员工，有权访问Crunchyroll支持工单。威胁行为体声称使用恶意软件感染该员工电脑并窃取其凭证。

据与BleepingComputer分享的截图显示，这些凭证可访问Crunchyroll多项应用，包括Zendesk、Wizer、MaestroQA、Mixpanel、Google Workspace Mail、Jira Service Management和Slack。

**攻击者称利用此权限从Crunchyroll的Zendesk实例下载了800万条支持工单记录，其中包含680万个唯一电子邮箱地址。**

BleepingComputer查看并随后删除的工单样本显示，信息种类繁多，包括Crunchyroll用户姓名、登录名、邮箱地址、IP地址、大致地理位置及工单内容。

尽管其他报道声称信用卡信息遭泄露，但BleepingComputer确认，信用卡详情仅在客户主动在工单中提供时才会暴露。大多数情况下仅包含基本信息，如末四位数字或有效期，极少数包含完整卡号——据威胁行为体称。

BleepingComputer查看的工单均提及Telus，印证了威胁行为体关于入侵BPO员工的说法。

攻击者称其访问权限在24小时后被撤销，使其仅能窃取截至2025年中期的数据。

黑客声称已向Crunchyroll发送勒索邮件，索要500万美元以换取不公开泄露数据，但未收到公司回应。

虽然此次攻击针对Telus员工，但BleepingComputer获悉，这与ShinyHunters勒索团伙对Telus Digital的大规模泄露事件无关。

**BPO成高价值目标**

过去几年，业务流程外包公司已成为威胁行为体的高价值目标，因其通常为多家公司处理客户支持、账单和内部认证系统。

因此，威胁行为体可通过入侵单一BPO员工获取跨多家公司的大量客户和企业数据。

**过去一年，威胁行为体通过贿赂具有合法访问权限的内部人员、对支持人员实施社交工程以获取未授权访问，以及入侵BPO员工账户进入内部系统等方式攻击BPO。**

其中最突出的案例之一是，**攻击者冒充员工说服Cognizant帮助台支持代理授予其Clorox员工账户访问权限，从而入侵该公司网络。**

多家大型零售商也确认，针对支持人员的社交工程攻击导致了勒索软件和数据窃取攻击。

玛莎百货（Marks & Spencer）确认攻击者利用社交工程入侵其网络，而Co-op则在披露数据遭窃后承认，勒索软件攻击同样滥用了支持人员的访问权限。

针对玛莎百货和Co-op零售公司的攻击，英国政府发布了关于帮助台和BPO社交工程攻击的指导建议。

某些情况下，黑客直接以BPO员工账户为目标，获取其管理的客户数据。

去年10月，Discord披露一起数据泄露事件，据称在其Zendesk支持系统实例遭入侵后，550万独立用户数据暴露。

---

**消息来源：[bleepingcomputer.com](https://www.bleepingcomputer.com/news/security/crunchyroll-probes-breach-after-hacker-claims-to-steal-68m-users-data/)；**

**本文由 HackerNews.cc 翻译整理，封面来源于网络；**

**转载请注明“转自 HackerNews.cc”并附上原文**

**标签:**[Crunchyroll](https://hackernews.cc/archives/tag/crunchyroll)[数据泄露](https://hackernews.cc/archives/tag/%E6%95%B0%E6%8D%AE%E6%B3%84%E9%9C%B2)

#### 关于作者

![](https://secure.gravatar.com/avatar/d81ce9e566e54dba5821cf454f0220df?s=128&r=g)

#### [hackernews](https://hackernews.cc/archives/author/sebugvul "View all posts by hackernews")

#### 猜你喜欢

[![可用-security-4868172_1280](https://hackernews.cc/wp-content/uploads/2025/02/可用-security-4868172_1280-210x140.jpg)](https://hackernews.cc/archives/63909 "Marquis 公司数据泄露事件波及 67.2 万人")

##### [Marquis 公司数据泄露事件波及 67.2 万人](https://hackernews.cc/archives/63909 "Marquis 公司数据泄露事件波及 67.2 万人")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-20

[![可用-恶意软件](https://hackernews.cc/wp-content/uploads/2026/02/geralt-data-theft-9480279_1920-210x140.jpg)](https://hackernews.cc/archives/63911 "Navia 公司披露数据泄露事件，270 万人受影响")

##### [Navia 公司披露数据泄露事件，270 万人受影响](https://hackernews.cc/archives/63911 "Navia 公司披露数据泄露事件，270 万人受影响")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-20

[![可用-僵尸网络 恶意代码](https://hackernews.cc/wp-content/uploads/2026/02/tumisu-cyber-security-3410923_1920-210x140.jpg)](https://hackernews.cc/archives/63891 "Aura 公司证实数据泄露，90 万营销联系人信息遭曝光")

##### [Aura 公司证实数据泄露，90 万营销联系人信息遭曝光](https://hackernews.cc/archives/63891 "Aura 公司证实数据泄露，90 万营销联系人信息遭曝光")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-19

[![可用-黑客](https://hackernews.cc/wp-content/uploads/2026/02/生成特定图片-2_压缩版-210x140.png)](https://hackernews.cc/archives/63877 "英国公司注册处泄露数百万公司信息")

##### [英国公司注册处泄露数百万公司信息](https://hackernews.cc/archives/63877 "英国公司注册处泄露数百万公司信息")

[hackernews](https://hackernews.cc/archives/author/sebugvul "hackernews") - 2026-03-18

Copyright © 知道创宇 2016-2020 HackerNews.cc | ![](https://www.knownsec.com/static/dist/imgs/d0289dc0.beian.png)  [京公网安备 11010502034619号](http://www.beian.gov.cn/portal/registerSystemInfo?recordcode=11010502034619) [京ICP备10040895号-38](https://beian.miit.gov.cn/)

联系方式: hackernews@knownsec.com / WeChatID: ks404team