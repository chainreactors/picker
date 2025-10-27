---
title: 研究员利用SQL注入漏洞绕过机场的TSA安全审查
url: https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520645&idx=2&sn=db3b91279c8927a20b8803d337553df8&chksm=ea94a0efdde329f99b47426cd38ffb58a35fb2dfc1c4037771332b1adac06119f08b376e6cad&scene=58&subscene=0#rd
source: 代码卫士
date: 2024-09-03
fetch_date: 2025-10-06T18:26:09.373317
---

# 研究员利用SQL注入漏洞绕过机场的TSA安全审查

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMT7yqfyZ7aKtka4IcuvUMRL42T17s90l9bJAa5LNibRBIY2mL6PuOPKsqWwcE0qGOAPeyofMbZSjIw/0?wx_fmt=jpeg)

# 研究员利用SQL注入漏洞绕过机场的TSA安全审查

Sergiu Gatlan

代码卫士

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif) 聚焦源代码安全，网罗国内外最新资讯！

**编译：代码卫士**

**安全研究员在一个关键的航空运输安全系统中发现一个漏洞，可被未授权人员用于绕过机场的安全检查并获得对飞机驾驶舱的访问权限。**

研究人员 Ian Carroll 和 Sam Curry 在基于web的第三方服务 FlyCASS 中发现了该漏洞。一些航线通过 FlyCASS 来管理“已知空勤 (KCM)”计划和“驾驶舱访问安全系统 (CASS)”。KCM是一项交通安全管理 (TSA) 计划，可使飞行员和乘客跳过安全审查，而CASS 可使授权飞行员在旅行时使用驾驶舱中的折叠椅。

KCM系统由 ARINC（柯林斯宇航的一个子公司）运营，负责通过一个在线平台验证航线员工的凭据。验证过程包括扫描KCM条形码或输入员工号码，之后交叉检查航线数据库，在无需进行安全审查的情况下授予访问权限。同样，CASS系统也会在飞行员通勤或旅行时验证驾驶舱折叠椅的访问权限。

研究人员发现，FlyCASS 登录系统易受SQL注入漏洞影响，可导致攻击者插入SQL语句进行恶意数据库查询。通过利用该漏洞，他们能够以参与航线 Air Transport International 管理员的身份登录并操纵系统中的员工数据。

攻击者增加了一个虚拟员工，名为 “Test TestOnly”，并将该账户权限授予KCM和CASS，从而导致他们能够“跳过安全审查，之后访问商业航线的驾驶舱”。

Carroll 表示，“任何拥有SQL注入基础知识的人员都能够登录到该站点，在KCM和CASS中新增任何人，从而跳过安全审查并访问商业航线的驾驶舱。”意识到问题的严重性后，他立即开始启动披露流程，在2024年4月23日联系美国国土安全部。研究人员决定不直接联系 FlyCASS 站点，因为该站点似乎由一名人员运营，披露可能引发恐慌。

美国国土安全部回应证实了该漏洞的严重性，并确认 FlyCASS 在2024年5月7日已与 KCM/CASS 系统断开连接，作为预防措施。不久后该漏洞在 FlyCASS上得到修复。

然而，因为国土安全部停止回复邮件，后续的漏洞安全披露协调工作遭遇不顺。TSA媒体办公室也向研究员发送声明否认了该漏洞的影响，声称该系统的审查流程可阻止越权访问。收到研究人员的通知后，TSA还从网站上悄悄删除了与其声明不一致的信息。

Carroll 表示，“我们通知TSA后，他们删除了网站上关于手动输入员工ID的内容，且并未回复我们的修正。我们已确认TSO 使用的界面仍然允许手动输入员工ID。”他还表示该漏洞本可导致规模更广泛的安全攻陷，如修改现有的 KCM 员工资料，绕过对新会员的任何审查流程。

研究人员发布报告后，另外一名研究员 Alesandro Ortiz 发现 FlyCASS 似乎已在2024年遭 MedusaLocker 勒索攻击，从Joe Sandbox 发布的分析文章来看还有加密文件和勒索信息。

TSA 新闻秘书 R.Carter Langston 表示，“四月份，TSA发现有报告称包含航线员工信息的第三方数据库中存在一个漏洞，通过漏洞测试后发现数据库的乘务员名单中被加入一个未经验证的姓名。政府数据或系统并未遭攻陷，并不存在与这些活动相关的交通安全影响。TSA并非完全依赖于该数据库来验证乘务员的身份。TSA部署流程来验证乘务员信息并只有通过验证的人员才能访问机场中的安全区域。TSA和利益相关者们缓解任何已发现的网络漏洞。”

目前，美国国土安全部并未就此事做出回应。

代码卫士试用地址：https://codesafe.qianxin.com

开源卫士试用地址：https://oss.qianxin.com

---

**推荐阅读**

[VMware 修复Aria Automation 中严重的SQL注入漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247520038&idx=1&sn=c47470c41eba485c6761c101be23ab04&chksm=ea94be4cdde3375a05493cfa38283ce2ea210148cf20f12ae01666d4ae7d06828b0073a00526&scene=21#wechat_redirect)

[CISA督促软件开发人员消除SQL注入漏洞](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519154&idx=2&sn=e5156dc817f213bae9628a3a674da4e8&chksm=ea94bad8dde333ce498ee36da84dbfce9ddeb839294d45a9916983f7515549e2bd774f39bb8b&scene=21#wechat_redirect)

[Cacti 监控工具受严重的SQL漏洞影响](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518617&idx=1&sn=25166b9f0e3966ea230b4150475573f2&chksm=ea94b8f3dde331e50b68b955b7fafbab44be937374b69ae0c44480093c778a19caa3b03b3cfd&scene=21#wechat_redirect)

[3CX 提醒客户禁用 SQL 数据库集成功能](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518402&idx=1&sn=da9d1a39d4b697106a57a34d89cff0d1&chksm=ea94b9a8dde330be50e062f6d96b932dc3f586d2c94a6af6ff7ebd6da5c5ff1ccc7b6e7aeda1&scene=21#wechat_redirect)

[Gentoo Soko 中存在多个严重的SQL注入漏洞，可导致RCE](http://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247516873&idx=1&sn=f21324530046513c1672582684ac641d&chksm=ea94b3a3dde33ab5352325a37c4e3c2512223c2288c773437fbe952a5b36452178917bb16e7a&scene=21#wechat_redirect)

**原文链接**

https://www.bleepingcomputer.com/news/security/researchers-find-sql-injection-to-bypass-airport-tsa-security-checks/

题图：Pixabay License

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