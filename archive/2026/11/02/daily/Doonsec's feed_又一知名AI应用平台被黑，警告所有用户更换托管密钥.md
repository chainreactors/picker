---
title: 又一知名AI应用平台被黑，警告所有用户更换托管密钥
url: https://mp.weixin.qq.com/s/y_jl7KuOug4RzMqiL2gdwg
source: Doonsec's feed
date: 2026-11-02
fetch_date: 2026-11-03T08:47:52.880937
---

# 又一知名AI应用平台被黑，警告所有用户更换托管密钥

# 又一知名AI应用平台被黑，警告所有用户更换托管密钥

安全内参编译
安全内参编译

安全内参

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

**关注我们**

**带你读懂网络安全**

![](https://mmbiz.qpic.cn/mmbiz_jpg/wT9KAyOic0NBib53iapeqNM9yBwB0U24NcVPNePvtO5NB7V1RH18DmYyrQwzbPqCTpoAmM7kYLoRdibMWzcQhvjK48nmOKUXbsiaknFJdrftjTlY/640?wx_fmt=jpeg&from=appmsg)

英国新锐AI开发托管平台Northflank披露遭受网络攻击，致使用户托管密钥泄露，已有多个用户反馈AI密钥遭滥用，官方呼吁所有用户更换托管密钥；

近一个月来AI密钥盗用攻击猖獗，据Wiz披露，已发生9起明星平台失陷事件，如Railway、OpenCode、Warp等，用户应积极关注相关新闻和订阅账单，避免滥用损失。

前情回顾·AI服务频遭攻击

* [知名AI开发平台发生数据泄露，呼吁所有用户更换托管密钥](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516776&idx=1&sn=95532de0868d1661b937626b36cee31a&scene=21#wechat_redirect)
* [OpenAI失控模型在互联网上“游荡”了4天，并袭击了另一家AI公司](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516343&idx=1&sn=05b3383792b82d14b3194c7aee039e50&scene=21#wechat_redirect)
* [一家AI公司被黑后，九家网络安全公司发生数据泄露](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516132&idx=1&sn=dbeb1fad9d1a61e7fb30cc2e36df34db&scene=21#wechat_redirect)
* [微软紧急关闭近百个开源代码库：AI类项目遭投毒，窃取用户敏感数据](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247516061&idx=1&sn=e250426489a7dff43d0d00097f5f8cc3&scene=21#wechat_redirect)

安全内参11月2日消息，知名云应用托管平台Northflank日前发生安全事件，导致客户的AI API密钥被未经授权使用。该公司已警告客户，立即更换存储在平台上的所有凭据、密钥等敏感信息，以防进一步滥用。

Northflank是一家英国云平台服务商。开发者可以通过该平台部署和管理应用程序、容器、数据库及AI应用，无需自行管理底层基础设施。

多个客户报告AI密钥已遭滥用

10月30日，Northflank披露了一起安全事件。此前，云安全公司Wiz向Northflank发出了安全警告，Northflank随即提醒客户立即更换环境变量和API密钥。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wT9KAyOic0NCkQ55xicDYZIjrUzHN3miay2DmicnvrTlesg7cbByLAcmSuXiaz8WuQ3g2KPlGBQvsVQE1TZ8KA3Mpu4A65bNe5OMVpE2uBzdylqo/640?wx_fmt=png&from=appmsg)

Northflank在通知中警告称：“请假设所有环境变量都已被解密，并立即禁用或更换所有密钥。”

应用程序通常使用环境变量存储敏感信息，包括数据库密码、云服务凭据、身份验证令牌和API密钥等。一旦这些信息暴露，攻击者就可能利用相关凭据入侵其他客户的服务、窃取数据，或滥用API密钥，产生未经授权的费用。

已有多名Northflank客户报告，其存储在平台上的AI API密钥被未经授权使用。

Northflank敦促所有客户：“如果您尚未更换存储在Northflank上的密钥等敏感信息，请立即处理。”

该公司还建议客户检查AI服务提供商的使用记录和账单，排查异常活动，并将可疑使用情况报告给Northflank及相关AI服务提供商。

目前，Northflank尚未披露攻击者如何获得系统访问权限，也未说明此次事件影响了多少客户。至于攻击者是否还窃取或滥用了其他凭据，目前同样不清楚。

作为应对措施，Northflank已开放PostgreSQL、MongoDB、MySQL和Redis的凭据更换功能。该公司还为所有客户启用了审计日志功能，包括免费账号用户，以帮助客户调查可疑活动。

AI开发平台遭遇“黑色十月”

此次安全事件发生之际，多个AI开发平台接连受到攻击。安全研究人员认为，这类平台存储着可用于访问高成本AI服务的API密钥，正成为攻击者的重要目标。

Wiz发布《AI开发平台的黑色十月》报告指出，仅10月份，就至少有9起安全事件影响了AI开发平台，涉及Northflank、Railway、OpenCode、Warp和Lightning AI等。

其中，Railway事件也涉及客户环境变量可能被解密并暴露的风险；OpenCode披露了AI API密钥暴露事件；Warp则报告称，一起安全事件导致AI智能体日志和用户遥测数据暴露。

Wiz表示，在部分事件中，攻击者专门针对包含AI服务凭据的环境变量，并可能利用一种名为大模型劫持（LLMJacking）的攻击手法获利。

大模型劫持是指攻击者利用窃取的凭据，通过其他组织的API密钥访问AI模型，造成高额API调用费用，或将窃取的访问权限转售给他人。

在Wiz调查的两起案例中，攻击者利用泄露的企业凭据，向Amazon Bedrock发起了约250万次API调用，造成约10万美元的AI服务费用。

研究人员还发现了一些与转售AI模型访问权限有关的基础设施，但尚无法确认这些业务与最初的安全事件或大规模滥用行为有直接关联。

Wiz尚未确认这9起事件是否均由同一批攻击者实施。不过，其中许多事件都涉及窃取AI API密钥的企图。

Northflank在后续事件通报中也引用了Wiz的研究，并指出，客户报告的AI密钥被未经授权使用事件，可能与研究人员发现的这波攻击有关。

**参考资料：bleepingcomputer.com**

**推荐阅读**

* [网安智库平台长期招聘兼职研究员](http://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247499450&idx=2&sn=2da3ca2e0b4d4f9f56ea7f7579afc378&chksm=ebfab99adc8d308c3ba6e7a74bd41beadf39f1b0e38a39f7235db4c305c06caa49ff63a0cc1d&scene=21#wechat_redirect)
* [欢迎加入“安全内参热点讨论群”](https://mp.weixin.qq.com/s?__biz=MzI4NDY2MDMwMw==&mid=2247501251&idx=1&sn=8b6ebecbe80c1c72317948494f87b489&chksm=ebfa82e3dc8d0bf595d039e75b446e14ab96bf63cf8ffc5d553b58248dde3424fb18e6947440&token=525430415&lang=zh_CN&scene=21#wechat_redirect)

---

点击下方卡片关注我们，

带你一起读懂网络安全 ↓

预览时标签不可点

阅读原文

不喜欢

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