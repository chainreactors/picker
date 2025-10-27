---
title: 黑客轻松盗取账密数据，竟是API弱密码缺陷惹的祸？
url: https://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247495711&idx=1&sn=bb51943b6b421a6247cb22a0473bd7e0&chksm=eb12d624dc655f3208495c65831a5c207f3ab8c7e6b531542e99ffdc76197c062f3bc6f99fc6&scene=58&subscene=0#rd
source: 威胁猎人Threat Hunter
date: 2023-04-01
fetch_date: 2025-10-04T11:23:03.669552
---

# 黑客轻松盗取账密数据，竟是API弱密码缺陷惹的祸？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/4mAgZtBianqHicBfO77OB4dys6bFPTIemqaAqkIfxlkm6r1HjRzWxKD0rVwWKTGJSG8dibbItEcLnlEibZRfRncr5A/0?wx_fmt=jpeg)

# 黑客轻松盗取账密数据，竟是API弱密码缺陷惹的祸？

原创

威胁猎人

威胁猎人Threat Hunter

![](https://mmbiz.qpic.cn/mmbiz_gif/4mAgZtBianqEAMZCKOk2hWqCfyHibLZbpsRxZEjfRuFptuU3ZwV5d1VLMglrldNwCwo76cJHqbfq08Vr7Y82zOZg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1)

允许弱密码，是最容易导致账号风险的API缺陷之一。

**威胁猎人****《2022年API安全研究报告****》曾列举了五大最受关注的API缺陷，其中就包含“允许弱密码”**，报告提到：

虽然很多安全开发规范都要求密码设置需满足一定强度，但2022年仍有不少API接口，甚至是部分管理后台的登录接口，存在“允许弱密码”的缺陷，引发账号泄露事故。

**那么，“允许弱密码”是什么？具体有哪些风险和危害呢？**

**“允许弱密码”是指：API允许用户设置密码的长度短且口令单一。**因具备高危害性、可利用性、普遍性等特征，是黑灰产盗取账号的主要手段之一，包括：

**简单数字组合：**000000，123123，5201314

**简单字母组合：**abcdefg，aaaaaa，shadow

**键盘临近按键：**qwertyu，qazwsx，mnbvcxz

**出厂默认密码：**admin，root，guest

**API接口存在“弱密码”缺陷，易导致严重的账号风险。**

黑客使用整合的弱密码库，通过撞库和暴破等方式攻击API，可成功盗取这些账号密码、用户信息等敏感数据，还可能作为筹码勒索企业，或者在暗网等渠道贩卖。

企业因此将产生巨额经济损失、遭受品牌声誉低谷，甚至背上烦人的官司。

**美国数字安全媒体Cybernews的研究团队，在2023年检查了5600万个被攻击和泄露的账号密码后发现：**

**1）**由简单数字和字母组成的密码常常被黑灰产使用，例如：“123456”就出现在了111,417个案例中；

**2）**观察到的密码中，仅有1%的密码符合安全开发规范的标准要求——同时包含大小写字符、数字、＄等特殊符号；

**3）**观察到的密码中，15%的密码只使用了4个字符，48%的密码使用了8-11个字符，仅有4%的密码使用了至少12个字符。

**威胁猎人2022年发布的《API安全研究报告》曾提到一个案例：**

某游戏平台，由于**API接口存在“允许弱密码”缺陷**，导致遭受黑产团伙的长期撞库和暴破攻击，**被成功盗取的账号中有61%是弱密码**，且排名靠前的大多为简单的纯数字组合。

玩家账号被盗后，黑产团伙进行了游戏资产转移等操作，不仅破坏了健康的游戏生态，而且给玩家带来巨大的财产和精神损失，平台的口碑急速下滑。

![](https://mmbiz.qpic.cn/mmbiz_png/4mAgZtBianqHicBfO77OB4dys6bFPTIemqG4PvfITibQONjGwGXnRjnicVGlC1WIIObI88Gibc7Z3GamgSprma6BteQ/640?wx_fmt=png)

攻防不做无备之战，与其亡羊补牢，不如趁早主动出击，**及时发现和解决“弱密码”缺陷，将安全风险扼杀在摇篮里**。

**如何发现和解决弱密码风险**

**企业要解决“弱密码”风险，需定期检测缺陷，及时精准地识别、定位和修复缺陷API**。

然而，企业的API数量惊人，并且每日新增数目可观，检测“弱密码”缺陷API的实操难度极大，需投入大量人力和时间。

威胁猎人的**API安全管控平台**具备强大的缺陷检测能力，针对“弱密码”的缺陷，API安全管控平台**基于弱密码库和安全开发规则**，检测密码是否为易被破解的弱密码、是否账密相同、密码是否为纯数字的组合且字符数小于8位等，**自动检测流量中携带“弱密码”缺陷的API。**

企业借此可及时、精准地识别“弱密码”的缺陷API，实现安全合规的业务运营和管理。

![](https://mmbiz.qpic.cn/mmbiz_jpg/4mAgZtBianqHicBfO77OB4dys6bFPTIemqvbblTMxNWUKUvoyKf2rGnwlDeZUzU6soG0xrORTIPAjEv11phUcM6Q/640?wx_fmt=jpeg)

并且，通过API安全管控平台，企业能及时感知低频、慢速、无特征的扫号、撞库、营销欺诈、数据爬取等场景的API风险事件，快速溯源和处置风险。

**安全Tips**

在设计、开发、测试API阶段，**威胁猎人的安全研究专家建议企业采取以下措施，降低“允许弱密码”带来的危害：**

**1）**自动对密码进行安全检查，用户可直观查看自设密码强度等级，如果密码不达高安全性的标准，自动提示用户调整密码和建议。

**2）**要求密码不能设置为账号/生日等与账号高关联的简单字符、长度不低于8个字符、同时包含大小写字母和特殊符号等两种及以上的字符类型。

**3）**限制每日错误密码输入的频次，如输入错误密码达5次，24小时内不允许再次输入密码登录账号，可加大攻击者的试错难度和成本，降低暴破成功的概率。

纵观全球网络安全环境，因弱密码导致的风险事件数量高速增长，对企业而言是挑战。

未来，威胁猎人将持续提升“弱密码”检测能力、坚持创新，帮助企业更高效和有效地应对挑战。

2023年1月5日，永安在线进行品牌焕新，正式更名为**“威胁猎人”**（详见：[成立6周年，威胁猎人焕新回归](http://mp.weixin.qq.com/s?__biz=MzI3NDY3NDUxNg==&mid=2247495229&idx=1&sn=08d55c289fd0fc700a5da2d57c361ce6&chksm=eb12c806dc654110208d965813d11524f5ccad88633401518208d21c52aeaf1822a66ade2f64&scene=21#wechat_redirect)）。

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