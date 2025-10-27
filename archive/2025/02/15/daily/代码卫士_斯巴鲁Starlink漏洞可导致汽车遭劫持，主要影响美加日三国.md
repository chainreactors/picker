---
title: 斯巴鲁Starlink漏洞可导致汽车遭劫持，主要影响美加日三国
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522232&idx=1&sn=cb025b96489e2100ef0f614b779833d4&chksm=ea94a6d2dde32fc4881deaa6fe80b16f9fb9423766568a24dd3e955367ff92ff773531a49a84&scene=58&subscene=0#rd
source: 代码卫士
date: 2025-02-15
fetch_date: 2025-10-06T20:36:46.857120
---

# 斯巴鲁Starlink漏洞可导致汽车遭劫持，主要影响美加日三国

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMQNyLL5TFhmMvRiaw0tMJbp9t54SWcHeHmeAzhXCic2cibZmJFh36SKWXJa1Punyyriagica0N4RsJu6ag/0?wx_fmt=jpeg)

# 斯巴鲁Starlink漏洞可导致汽车遭劫持，主要影响美加日三国

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**安全研究员在斯巴鲁的智慧星联 (Starlink) 服务中发现了一个任意账户接管漏洞。攻击者仅凭一个车牌号就能劫持位于美国、加拿大和日本的汽车。**

漏洞猎人 Sam Curry 在2025年1月份披露称，该漏洞是在2024年11月20日和研究员 SHubham Shah 一起发现的。他们发现该漏洞可使潜在攻击者获得所有美国、加拿大和日本客户的账户和车辆的不受限针对性访问权限，而唯一的要求就是知道受害者的姓氏和邮政编码、邮件地址、电话号码或车牌号。

成功利用该漏洞可使攻击者：

* 远程启动、停止、锁定、解锁和检索任何车辆的当前位置；
* 检索任何车辆从去年开始的位置信息历史（精确到5米以内且在引擎启动每次启动时都会更新）；
* 查询和检索任何客户的个人可识别信息，包括紧急联系人、授权用户、实际住址、账单信息（如信用卡的最后四位数字，不包括完整的卡号）以及车辆的PIN码。
* 访问多种用户数据包括支持呼叫历史、此前机主信息、里程数、销售历史等。

Curry 还在视频中展示了如何利用该漏洞在10秒钟的时间内获取斯巴鲁汽车超过一年的位置数据。他发现，智慧星联的管理面板中包含源自 “resetPassword.json” API 端点的一个任意账户接管漏洞，可导致斯巴鲁员工在无需确认令牌的前提下使用有效邮件重置账户。

接管一名员工的账户后，Curry 还必须绕过双因素认证提示来访问该门户。然而，只要删除该门户用户界面的客户端涂层，就能轻松绕过该要求。他提到，“其它端点非常多，其中一个是车辆搜索，可用于查询客户的姓氏和邮政编码、电话号码、邮件地址或VIN号码（通过车牌可检索）并授予/修改车辆访问权限。在主板搜索并找到自己的车辆后，我确认智慧星联管理员面板应该能够访问位于美国、加拿大和日本的任何斯巴鲁。”

研究人员还测试发现，他们能够通过一名朋友的斯巴鲁汽车的车牌号执行门户中所列出的所有操作。Curry 表示斯巴鲁在漏洞报送的24小时内修复了该漏洞，且该漏洞未遭利用。

包括Curry 在内的多名安全研究员曾在起亚的经销商门户中发现了类似漏洞。黑客仅凭车牌就能定位并窃取数百万自2013年起制造的起亚汽车。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

---

**推荐阅读**

[斯巴鲁汽车遥控钥匙存在漏洞可遭克隆](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247485455&idx=2&sn=251e5856dc3d5141d2e9765fd86ee768&scene=21#wechat_redirect)

[2025 Pwn2Own 汽车大赛落幕 Master of Pwn诞生](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247522224&idx=2&sn=125d997bc554beb7f8976b4e7d5fb526&scene=21#wechat_redirect)

[仅凭车牌就能远程控制起亚汽车，漏洞已修复](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520951&idx=1&sn=05f9503385c7ca3c9f3e13e6c82e0f69&scene=21#wechat_redirect)

[2025 Pwn2Own东京汽车大赛公布目标和奖金](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520932&idx=1&sn=92b8d0945843bbf9725d8256c2c2fd46&scene=21#wechat_redirect)

[软件提供商CDK Global遭攻击，北美汽车经销商被迫用纸笔交易](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519884&idx=3&sn=a9228acb497fae65935d8034a44a05c8&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/ivanti-fixes-three-critical-flaws-in-connect-secure-and-policy-secure/

题图：Pexels License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/oBANLWYScMQnXWuOU95T0gnUjHe8IhdLQuqwxvDpLf7GwP25ntfz6W8dhDhUS3BstsPLPL9YBRXE1QhF9eIjiaw/0?wx_fmt=png)

代码卫士

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