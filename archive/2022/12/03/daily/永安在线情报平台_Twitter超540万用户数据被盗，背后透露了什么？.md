---
title: Twitter超540万用户数据被盗，背后透露了什么？
url: https://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247494985&idx=1&sn=23dbdccfa2cd1dfbd362a1b590fdc54a&chksm=eb12cb72dc6542646fca0e54e38b7c1210b852cc3027c398ba6c7bbcf2ed81497d8dde905845&scene=58&subscene=0#rd
source: 永安在线情报平台
date: 2022-12-03
fetch_date: 2025-10-04T00:24:33.769332
---

# Twitter超540万用户数据被盗，背后透露了什么？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4mAgZtBianqGlnwWqbD7PPx3B4COxbB2vY53bGbQvbrJsw3rxENbfZumCTrTicfny86ZbZEKVcPhMFNbWcm4xLZA/0?wx_fmt=jpeg)

# Twitter超540万用户数据被盗，背后透露了什么？

威胁猎人Threat Hunter

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqHJGmTgK1IkdGenlrsehnKe61VhicFG0G5lEPxtqmdyOjtsLNHfq998Mv1SvZzYufxKKmOAgvxibRyA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

近日，Twitter超过540万条用户数据**免费在暗网公开**，引发媒体热议。一起盘一盘事件背后的原因是什么？危害有哪些？

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGfDcmfZY3nibxrmCnxLvR42aBDdOhibbYq4VNyY0sY4WjbmhibBWLwFq7YuAL5ibgU3Ies5YO9XcmYkA/640?wx_fmt=png)

今年7月，网络犯罪分子就在黑客论坛上以3万美元出售Twitter数据库，涉及540万用户，包括“从名人到公司”的用户数据(当时并未免费公开)，后由Twitter证实，数据泄露是由网络犯罪分子利用Twitter2021年12月披露的一个API 漏洞所造成。

**那么，攻击者是如何利用Twitter API漏洞窃取用户数据的？**

**一、通过API漏洞“扫号”窃取用户信息**

总的来说，TwitterAPI漏洞允许任何一方在没有任何认证的情况下，通过提交电话号码或电子邮件，获得任何用户的Twitter ID，使得攻击者可以利用该漏洞进行大规模“扫号”攻击。

![](https://mmbiz.qpic.cn/mmbiz_jpg/4mAgZtBianqGfDcmfZY3nibxrmCnxLvR42pSqTCYF7ax6g34g0Bx7oPXia8G7qT9Kibox9wRFlOFW9gXOO9ZjGaMkg/640?wx_fmt=jpeg)

攻击者向Twitter的API接口提交手机号或电子邮件，API接口根据提交信息返回相关“提示”，由此，攻击者判断出该账号是否注册，并将“已注册”账号信息快速匹配账户ID。通过账户ID，攻击者可以直接获取用户与Twitter账号绑定的**个人资料信息，包括名称、位置信息、兴趣爱好，甚至社会身份**，并结合大数据分析输出Twitter用户账号的精准画像，从而针对用户实施诈骗。

**除Twitter以外，不少头部企业因API接口存在问题屡遭攻击，数据泄漏事件接二连三:**

2020年3月，国内某大型分享交流平台被爆出用户查询API接口被非法调用，导致**5亿**平台用户的私人信息被攻击者获取并售卖到暗网。

2021年4月，Facebook平台上的**5.33亿**用户数据泄漏，涉及国内用户超**67 万，**事后判定为业务API安全漏洞......

社交平台大规模数据泄露后，数百万用户的私密信息被不法分子利用，其风险不可小觑。

**二、数亿数据泄露，后果远超想象**

中国互联网络信息中心《第49次中国互联网络发展状况统计报告》显示，**截至2021年12月，有22.1%的网民，也就是超2亿人遭遇个人信息泄露**。

个人信息泄露后，平台用户会遭遇频繁的电话骚扰、甚至被黑产利用个人信息进行诈骗，带来资金盗用，恶意欺诈等一系列风险。尤其当公众人物信息被曝光，极有可能引发人身及财产威胁。对于企业来说，数据泄露不仅会招致大量的用户投诉，还有可能面临法律处分或监管处罚，严重损害企业经济及品牌声誉。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGfDcmfZY3nibxrmCnxLvR427zBAn7L1QBjXH3XreqdpwnkLD8jA9IlYkQicwvNqY4dYOufnE6NB2sA/640?wx_fmt=png)

近日，Facebook母公司Meta就因**5.33亿**Facebook用户个人数据被泄漏到互联网上，而被爱尔兰数据保护委员会（DPC）罚款**2.65亿**欧元（约合近20亿人民币）。

**三、API安全管控，刻不容缓**

随着数字化、API技术发展，网络安全边界逐渐模糊，其原有的防护措施已无法满足面向全场景的安全需求，各种**API接口暴露在互联网，扩大了业务风险暴露面**。

此外，API的爆发式增长与安全发展不平衡，使其成为数据安全中最薄弱的环节，并**成为攻击者进行数据攻击的首选目标**。

SaltSecurity报告中提到，在过去的12个月中，20%的组织由于API中的安全漏洞而引发数据泄露，**95%的组织在API中遇到了安全问题。**

然而，大多数组织并没有准备好应对这些挑战，**超过三分之一（34%）的企业没有API安全策略**。

**那么，企业应如何应对日益严峻、复杂的API安全挑战？**

**API安全管控并非易事。**业内API安全解决方案所采用的技术大多是**“传统规则引擎”**，在API攻击层面，很多时候攻击请求中并未包含任何攻击特征，因此传统规则引擎在API风险识别上，很难从行为上区分威胁，也不具备标准化程度和规模化效应。

永安在线API安全管控平台，基于**“情报”**（如攻击IP、工具、账号、行为等）构建API访问的行为基线，且不受AI流量波动影响，可以快速判定API存在的风险攻击事件，帮助企业全面梳理API资产、预防发现阻断API攻击、提升风险事件的响应速度、防止流动敏感数据泄漏。

***1.*****资产管理方面，从“杂乱无章”到“了如指掌”**

API安全管控平台内置资产梳理模块，持续、动态、自动化梳理面向客户、内部员工、合作伙伴、开源组件和中间件等场景下的API，建立完整API资产清单，帮助企业及时、动态地了解API开放数量、API活跃状态、僵尸API、影子API、缺陷API、涉敏API等安全风险信息，确保企业流动数据清晰可见。**目前，API资产识别率可达97.8%。**

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGfDcmfZY3nibxrmCnxLvR42bV5Le5GnLn6kSaacZ8Q1ggct8rjbkv19o5NhqO1MZzwRzVEly3mBZQ/640?wx_fmt=png)

***2.*****缺陷检测方面，从“扑朔迷离”到“一览无余”**

基于永安在线特有的情报技术和攻防研究，可持续跟踪攻击者如何利用新型API漏洞进行攻击，并提取新型攻击面和攻击特征，持续优化API漏洞检测引擎，能及时覆盖最新的业务API逻辑漏洞和第三方组件、开源系统API的未授权漏洞等。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGfDcmfZY3nibxrmCnxLvR42OCEktXdaKEjTD1cCcibe72ZneN5QCSbogCHIjrof4XwNShLojZ8pshg/640?wx_fmt=png)

截至目前，**平台可支持64种API缺陷类型的检测**，包括未授权漏洞、越权漏洞、短信验证码泄露、关键数据未脱敏等等。此外，平台已实现API安全缺陷自动化缺陷修复状态判定，实现缺陷闭环处理，提升安全运营效率。

***3.*****风险感知方面，从“海量攻击”到“精准告警”**

API安全管控平台基于广覆盖、高精准度的风险情报，构建API访问的行为基线，利用机器学习检测API访问序列中的异常行为，可及时、有效地感知恶意注册、扫号攻击、撞库攻击、营销欺诈、数据爬取、短信轰炸、敏感API境外访问等场景的API风险事件。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGfDcmfZY3nibxrmCnxLvR424Qgcm0AJVaeichtiaY5cPX6TtgC6q6U8R07jJbtqxvaQ2l1g2FPm6Hww/640?wx_fmt=png)

尤其能解决攻击者利用海量小号、秒拨代理IP发起的低频、慢速、无特征的扫号撞库、数据爬取、营销欺诈行为，**识别准确率不低于95%**。

永安在线基于底层情报能力的长期积累，持续为广大企业**构建以业务优先为原则、可视、可控、可靠的API安全管理体系**。

**推荐阅读**

[API风险雷达帮助小张避免了一次数据泄露事件](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247494783&idx=1&sn=441c819a7a15d957a3a1d948f3bbfe86&chksm=eb12ca44dc654352ee8a9179105857b79cef52b186318e8d71a9d45a5d0b580b348009cd725d&scene=21#wechat_redirect)

[从闲鱼交易欺诈，看业务安全为什么这么难做](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247494615&idx=1&sn=1dc8474305607c98b7672c211ba9a0da&chksm=eb12cdecdc6544fa86029f1a8f076a6a6c1bac6ff55a96c204d2eac87e6a42557f857a8fd295&scene=21#wechat_redirect)

[多家金融借贷平台遭受攻击，大量用户信息泄漏](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247494423&idx=1&sn=0dbf8345f114289210dd4fbbb9d9aab6&chksm=eb12cd2cdc65443a35bbecdee134491472de8b7599b9dbb4f214798e9a0bab4d32ffb4ebe674&scene=21#wechat_redirect)

[刷量产业链不断进化升级，新型“高级账号”刷量悄然出现](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247493803&idx=1&sn=ce52f63c03c6c606f7dfa815f4a3e1de&chksm=eb12ce90dc654786aa437b046224209de916010cc456a82098b8e7ddaa8beeee8f7c2ccee608&scene=21#wechat_redirect)

[永安在线发现针对中国数字政务的攻击团伙，7省份的近4亿公民数据受威胁](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247493504&idx=1&sn=29dbb091f01eaf71283a1493543a3db5&chksm=eb12c1bbdc6548ad7280cea9b62ecfd00aa6a5cd570eb626178998cbb4f0eb938fa260f363c3&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqHJGmTgK1IkdGenlrsehnKeEERhM57Y87gcHb5sDC1hRCEzVlf5c2acdb1cTuicatruE29glpy0mUg/640?wx_fmt=png&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGDp3b1qusRgNYCaq1lycmp28Q0cv0o7PkrKW7vib649ZeWmvKLOeORSibaKichArtBFCF8e1LPpxYZw/0?wx_fmt=png)

威胁猎人Threat Hunter

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqGDp3b1qusRgNYCaq1lycmp28Q0cv0o7PkrKW7vib649ZeWmvKLOeORSibaKichArtBFCF8e1LPpxYZw/0?wx_fmt=png)

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