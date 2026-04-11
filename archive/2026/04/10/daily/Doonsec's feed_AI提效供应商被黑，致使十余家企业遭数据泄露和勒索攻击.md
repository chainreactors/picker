---
title: AI提效供应商被黑，致使十余家企业遭数据泄露和勒索攻击
url: https://mp.weixin.qq.com/s/vQKr0YIi1rB0yY3vWJYo5g
source: Doonsec's feed
date: 2026-04-10
fetch_date: 2026-04-11T04:18:27.298296
---

# AI提效供应商被黑，致使十余家企业遭数据泄露和勒索攻击

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wT9KAyOic0NBr4mgQmHR8vFQPk6sAENDzHJRrWvBBjIXicIFcVAOYicPJ5uNeFGCk5qxNBPch8eJLDmPhNPdBU9EJESXI0boT3AeOz0RSPfBXc/0?wx_fmt=jpeg)

# AI提效供应商被黑，至少十余家客户遭数据泄露及勒索攻击

安全内参编译
安全内参编译

安全内参

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/FzZb53e8g7sOaHFxicA9ia9428bXWIgehYPwblrKI5pBqgAE744PJTwQ8XJGqDFfvfDcicPYWCfVNeUMyYl6RGj4Q/640?wx_fmt=jpeg)

由于AI提效供应商Anodot被黑，身份验证令牌泄露，导致至少12家公司的Snowflake云数据平台遭到数据窃取，部分公司还受到了ShinyHunters组织的数据勒索威胁；

这一事件再次展示了SaaS、AI等新技术新业态极大放大了数据安全风险，此前Salesforce也曾因第三方生态屡遭攻击，导致大量客户数据大规模泄露。

前情回顾·AI网络威胁态势

* [AI失控时刻：智能体协同入侵公司内部系统，窃取机密数据](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515686&idx=1&sn=d090cb4b27db75aa0f588e2e3b84c341&scene=21#wechat_redirect)
* [麦肯锡AI助手被红队AI攻陷：近5000万条聊天记录可任意访问 涉海量客户机密数据](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515662&idx=1&sn=da8c2dc81017a413362c5e32f3ce20a6&scene=21#wechat_redirect)
* [AI医生可被任意劫持：篡改患者处方剂量、给出错误医疗建议](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247515651&idx=1&sn=cd14705ea7004255f2b8fad417a80ed9&scene=21#wechat_redirect)
* [AI工具“沉浸式翻译”被曝泄露隐私，用户保单、合同遭公开](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247514827&idx=2&sn=b25fb64cd7d839628580cda05f1e9e1e&scene=21#wechat_redirect)

安全内参4月10日消息，由于一家SaaS集成服务提供商遭到入侵，身份验证令牌被窃，导致超过12家公司的数据被盗。

黑客利用被窃取的令牌，对大量云存储和SaaS供应商发起攻击。外媒BleepingComputer获悉，大多数数据窃取事件针对的是云数据平台Snowflake。

Snowflake向BleepingComputer确认，系统中出现了“异常活动”，并表示仅有少量客户受到影响。

Snowflake表示：“我们近期在少量与特定第三方集成相关的Snowflake客户账号中检测到异常活动。我们已第一时间启动调查，并出于高度谨慎锁定了可能受影响的账号。同时，我们已通知相关客户，并提供预防性指导，帮助其进一步加强账号安全。”

Snowflake强调，这些攻击并未利用其系统中的任何漏洞，也未攻破任何系统。

在此次攻击过程中，威胁行为者曾尝试利用被窃取的身份验证令牌，从Salesforce窃取数据，但在成功之前即被检测并阻止。

**数据窃取与AI提效公司Anodot被入侵有关**

起初，Snowflake并未确认涉及此次攻击的第三方集成合作伙伴，但后来官方证实了多方传闻的信息，即这些攻击源于数据异常检测公司Anodot的一起安全事件。

Anodot是一家基于AI的业务分析提效公司，提供实时异常检测服务，主要用于业务与运营数据分析。其通过机器学习帮助企业自动识别收入、交易及系统性能中的异常变化。该公司已于2025年11月被数据分析公司Glassbox收购。

自上周六早晨起，Anodot状态页面显示，其所有连接器在各个地理区域均出现中断，其中包括Snowflake、S3和Amazon Kinesis。

周一的状态更新指出：“我们在数据采集，以及异常类型告警的检测与分发方面遇到了问题。”

![Anodot 当前状态页面](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wT9KAyOic0NA5OrRNFXDNYGgq3p3w6ibOdFUJAGcvf0BOCsWInYJhe25F1SRWQNicIOwgkaia8nq564p8Csg2gXpQA1vPyF3TujX4jZMtWWKgYc/640?wx_fmt=jpeg&from=appmsg)

图：Anodot状态页面

**多家企业遭到数据勒索威胁**

BleepingComputer获悉，目前已有多家公司遭到ShinyHunters勒索组织敲诈。该组织要求支付赎金，以防止被窃数据被公开。

该组织向BleepingComputer确认，其正是此次攻击的幕后黑手，并声称于上周五利用来自Anodot的身份验证令牌，从数十家公司窃取了数据。

威胁行为者还暗示，他们可能已经在Anodot系统中潜伏了一段时间。

他们同时确认，曾尝试从Salesforce窃取数据，但被AI检测机制拦截。这一失败的尝试，正值过去一年针对Salesforce客户的数据窃取攻击频发之际。

威胁行为者还分享了一些据称受影响的公司名单，但在未获得确认之前，BleepingComputer未予公布。

目前仅有一家公司Payoneer回应了相关询问。该公司表示，已知晓该集成商遭入侵事件，但自身未受到影响。

Payoneer在向BleepingComputer提供的声明中表示：“我们已注意到涉及第三方服务提供商Anodot的安全事件。经内部审查确认，Payoneer未受到影响。”

谷歌威胁情报小组一直在跟踪今年多起数据窃取活动，并确认已关注此事件并持续跟进，但暂未披露更多细节。

BleepingComputer已向Anodot及其母公司Glassbox发送多封邮件，寻求进一步回应。

**参考资料：bleepingcomputer.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

安全内参

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/FzZb53e8g7u3766XzHf0XHoQ1HkzDV0M7wC5zTyTO6daqAZ6LMD0Lykps2WumsWj2KMQJAGhwOYDcb3E8AicxSw/0?wx_fmt=png)

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