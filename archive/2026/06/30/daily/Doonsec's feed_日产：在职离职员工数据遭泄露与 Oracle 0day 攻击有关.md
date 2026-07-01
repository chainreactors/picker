---
title: 日产：在职离职员工数据遭泄露与 Oracle 0day 攻击有关
url: https://mp.weixin.qq.com/s/HpSbxmxh3Az9tDhb9V5a6w
source: Doonsec's feed
date: 2026-06-30
fetch_date: 2026-07-01T06:20:24.424398
---

# 日产：在职离职员工数据遭泄露与 Oracle 0day 攻击有关

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/t5z0xV2OYfUtEbCQShGpqmS7EzuacVUFOIZibdl3UVrAMdEqHlu5U3JQ998qZmib4Yox9LAGOCW62ibbFyFnVNqRp42HVgRhdYRFEg3BrJf5Fc/0?wx_fmt=jpeg)

# 日产：在职离职员工数据遭泄露与 Oracle 0day 攻击有关

Lawrence Abrams
Lawrence Abrams

代码卫士

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)  聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**日产汽车警告称该公司发生一起数据泄露事件，影响在职和离职员工，与 Oracle 公司 PeopleSoft 漏洞被用于数据盗取攻击活动有关。Oracle 公司在向美国加利福尼亚州总检察长办公室提交的泄露通知中表示，数据盗取事件影响了数百家公司，日产便是其中之一。**

日产公司提到：“日产美洲公司使用Oracle PeopleSoft软件来管理员工信息，包括薪资、税务管理及其他人事记录。” 该公司还指出，“Oracle已通知我们，发生了一起网络事件，数百家公司的人事记录可能已被所谓的威胁行动者获取。我们随后得知，日产是此次攻击中的特定目标。”日产称，目前仍处于调查的初期阶段，尚未确定此次泄露的全部影响，但认为攻击者访问了个人信息，可能包括员工联系方式、银行信息、社会安全号码、社会保险号码、国民身份证号码、财务和税务信息，以及受抚养人和受益人信息。

据信，此次事件影响了美国、加拿大、墨西哥和巴西的日产在职和离职员工。日产表示，在得知遭数据泄露事件影响后，启动了事件响应，聘请了外部网络安全专家，保护了受影响的系统，并正在与Oracle合作解决此问题。该公司还表示已采取措施终止未经授权的访问，并为了防止员工信息的进一步泄露，将在可用的情况下为受影响个人提供免费的信用和暗网监控服务。

作为额外预防措施，日产公司表示正在限制对员工工资单和直接存款变更的访问，仅限于公司网络计算机或安全VPN连接，并在处理薪资请求前实施额外的身份验证措施。日产表示，最终被确定信息已暴露的员工将收到另行通知，详细说明哪些数据受到了影响。

与ShinyHunters相关的Oracle PeopleSoft 0day攻击

据信，此次披露源于本月早些时候BleepingComputer首次报道的Oracle PeopleSoft服务器遭大规模利用事件。如最初报道，威胁行为者利用Oracle PeopleSoft中的一个0day漏洞入侵实例并窃取数据。

ShinyHunters勒索团伙声称对此次攻击负责，并向BleepingComputer表示，已入侵了100个组织中的超过300个PeopleSoft实例。不久之后，Oracle披露了Oracle PeopleSoft PeopleTools中的一个严重漏洞CVE-2026-35273，并发布了紧急缓解措施。

尽管Oracle尚未公开确认该漏洞已被利用，但Mandiant随后证实称，威胁行动者在5月27日至6月9日期间，利用了 0day 漏洞状态下的CVE-2026-35273漏洞。这些攻击主要影响教育领域的组织机构，Mandiant表示已通知了超过100个组织，证实了ShinyHunters此前分享的信息。此后，ShinyHunters已开始在其数据泄露网站上泄露在这些攻击中窃取的数据，包括诺丁汉大学和美国全国保险专员协会的数据。

ShinyHunters是一个已知的勒索组织，通常以Salesforce、Snowflake、第三方集成合作伙伴及其它云SaaS环境为目标进行数据窃取。近期，该威胁组织还在另一起针对Instructure Canvas的网络攻击中瞄准教育领域，窃取了2.8亿条学生、教师和员工的数据记录。Instructure后来支付赎金以防止数据被泄露。

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[Red Hat服务器受陷，日产1.2万名客户数据遭泄露](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524719&idx=2&sn=f5d89f84af3cc83b347bda7d39e298df&scene=21#wechat_redirect)

[日产聆风存在多个漏洞，可用于远程监控和物理接管](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522711&idx=2&sn=2524dc1d635d1e0a9ec3abc54886f6ab&scene=21#wechat_redirect)

[Git 仓库配置不当 日产北美公司的源代码遭泄露](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247500006&idx=2&sn=a2c53f313742933a397fea09c2e61660&scene=21#wechat_redirect)

[TCU缺陷可致汽车遭远程入侵 宝马福特日产受影响](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485492&idx=3&sn=2b529d9f7aa55ced7e32dc7e28db5991&scene=21#wechat_redirect)

**原文链接**

https://thehackernews.com/2026/06/new-dirtyclone-linux-kernel-flaw-lets.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif)![]() 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

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