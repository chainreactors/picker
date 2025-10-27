---
title: 泄露用户信息长达一年半，丰田被服务商坑惨了
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535819&idx=3&sn=dd046f261157ec87de3e8069dedb206d&chksm=fa93fa0acde4731c6158d6f19a282e4fc830a56c76a603b2dfd26ae05dea026b669c97384ffb&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-30
fetch_date: 2025-10-04T11:08:17.691623
---

# 泄露用户信息长达一年半，丰田被服务商坑惨了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lBEAgL7OpGg3lRF4oVfDt8tiarRud9aVg5iahgBQibqJedRV01sk2IcttrXicMFsnlwdymdUsa7Ok9cg/0?wx_fmt=jpeg)

# 泄露用户信息长达一年半，丰田被服务商坑惨了

网络安全应急技术国家工程中心

全球知名汽车制造公司丰田（TOYOTA）遭遇了严重的用户信息泄露事件。安全研究人员发现，黑客通过攻击丰田意大利数字营销自动化和分析软件服务提供商 Salesforce Marketing Cloud，从而获得了海量的用户数据，且至今为止数据泄露已有一年半之久。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icqM1SfDjUQ7kA8eC9odbDuQKdwOQFMKF6gopoO32QX5GUn8S7kQmdQmXQLBT8HnNHdqyTSfYctlg/640?wx_fmt=jpeg&wxfrom=13&tp=wxpic)

此外，丰田意大利还泄露了软件公司 Mapbox 的应用程序编程接口 (API) 令牌，导致敏感数据泄露范围增大。攻击者可能会借此获取丰田意大利用户的手机号码和电子邮箱等，并利用这些信息发起网络钓鱼攻击。

好消息是，截止到发稿时，丰田意大利已经将这些数据再次保护起来，该公司也表示，已经和第三方网络安全公司合作，采取了额外的措施加强其网络安全系统和协议。

公开信息显示，丰田是全球最大的汽车制造商之一，拥有超过37W名员工，去年收入约为2670亿美元。仅在欧洲，丰田的雇员就超过了2.5W名，共有八家汽车制造工厂。

目前虽然不清楚丰田意大利的官方数据，但是该公司已经在意大利屹立半个多世纪了，妥妥的老牌企业。根据 Statista 的数据，丰田意大利公司的收入预计到 2023 年将达到约18亿美元，汽车销量预计将接近8.3w辆。

# **偶然发现数据被公开**

2023年2月14日，Cybernews的安全研究团队在丰田意大利官方网站上发现了一个环境文件(.env)。而该环境文件于2021 年 5 月 21 日首次被物联网 (IoT) 搜索引擎编入索引，这意味着很多人都可以进行公开访问。

根据 Cybernews 研究团队的说法，该环境文件泄露的原因是，丰田意大利数字营销自动化和分析软件服务提供商 Salesforce Marketing Cloud公开了用户账户凭证访问权限。黑客获取了Salesforce Marketing Cloud公司的权限，并借此访问丰田意大利用户的账户凭证。

通过账户凭证，攻击者顺势访问到了用户的电话号码、电子邮件地址、客户跟踪信息、短信和推送通知内容。同时这些凭据可以进一步被用来发送虚假的SMS消息、电子邮件、编辑&启动营销活动、创建自动化脚本、编辑与 Salesforce 营销云相关的内容，甚至向丰田的客户发送推送通知。

Cybernews 安全研究人员称，此次敏感数据泄露事件对于丰田意大利来说十分严重，这些信息完全可以被用来发起一些复杂的网络钓鱼攻击，攻击者可以访问和控制丰田的官方通信渠道，从而使受害者更容易落入此类钓鱼攻击中，因为发件人的信息是被冒充的丰田意大利官方。

此外，丰田意大利还泄露了软件公司 Mapbox 的应用程序编程接口 (API) 令牌。虽然这部分数据不像 Salesforce Marketing Cloud 账号凭证那么敏感，但是攻击者可能会滥用它来查询大量请求并增加丰田 API 使用的成本。

# **丰田官方回应**

Cybernews 将此漏洞告知丰田后，该公司立即采取了必要的措施来进行补救。据丰田公司称，此次安全事件的出现，是对方未能遵守公司的数据安全政策造成的。

目前丰田公司已经采取了一套额外的安全措施来恢复和加强网络安全系统和协议，并及时向意大利有关当局报告了隐私数据暴露的风险，全力配合正在进行的调查。

丰田公司进一步表示，丰田非常认真地对待此次事件，也非常重视网络安全建设，我们将借此机会从调查结果中吸取教训，进一步提升网络安全防护能力以及协议的安全性，防止再次出现此类安全事件。

目前尚不清楚攻击者具体访问了哪些数据，但丰田公司建议用户高度警惕网络钓鱼攻击，及时更换账号密码，以确保个人信息安全。

丰田公司称：“骗子可能会试图向您发送冒充丰田或任何其他流行品牌的虚假消息，因此请确保通过启用多因素身份验证 (MFA) 来保护您的电子邮件地址。小心电子邮件，不要点击链接或提供任何个人信息。如果您发现电子邮件可疑，请将其报告给您的提供商。

当涉及到电话号码时，您可能会受到垃圾/营销/钓鱼短信的轰炸，甚至会发现自己成为 SIM 交换攻击的受害者，攻击者部署该攻击以获取对基于 SMS MFA 代码的访问权限。”

这不是丰田第一次在网上公开其数据并将自身和客户置于风险之中。

2022年，丰田公司近30万用户数据被泄露，包括电子邮件地址和客户管理号码。开发人员在 GitHub 上发布源代码后，通过其客户应用程序 T-Connect 公开的数据已经泄露了五年。

2023年 1 月，丰田汽车在印度的业务也曝出信息泄露事件，部分用户的个人信息很有可能已经被攻击者获取。

**参考来源：**

https://cybernews.com/security/toyota-customer-data-leak/

原文来源：FreeBuf

“投稿联系方式：孙中豪 010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

网络安全应急技术国家工程中心

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GoUrACT176mrRug7icLIhX4EvNQjNgGRibia7K9qOLTR5PDfQiaUesU9xge7pnF8iciaxVC3JVkNqHA2pvQDnrM0hDVQ/0?wx_fmt=png)

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