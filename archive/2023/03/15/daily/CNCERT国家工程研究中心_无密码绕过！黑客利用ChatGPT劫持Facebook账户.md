---
title: 无密码绕过！黑客利用ChatGPT劫持Facebook账户
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247535379&idx=5&sn=70dbf763b964b1f684bee045bfc64217&chksm=fa93fdd2cde474c4f501e4df307fb60b41c6323bad38102a96d6798ce6a1cd0229839b20b9f7&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2023-03-15
fetch_date: 2025-10-04T09:36:45.985107
---

# 无密码绕过！黑客利用ChatGPT劫持Facebook账户

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lv7WgIyWib20HBPCRN3IibvOyCW34sk55ZlONRicBECWU6v7gTmicjUql071QkjWicHmK2ofic2ibARAovQ/0?wx_fmt=jpeg)

# 无密码绕过！黑客利用ChatGPT劫持Facebook账户

网络安全应急技术国家工程中心

Dark Reading 网站披露， 3 月 3 日- 3 月 9 日，每天至少有 2000 人从 Google Play 应用商店下载"快速访问 ChatGPT“ 的 Chrome 恶意扩展。据悉，一名威胁攻击者可能利用该恶意扩展泄露包括商业账户在内的数千个 Facebook 账户。

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR3icNMCx7CO9Hz35In5tjgibgCY855j9KxVbBSsibIcH1HXhnIaVY0l0JnS3huvMwKxaZ8y3ryzkntOGw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1)

从 Guardio 的分析结果来看，恶意 "快速访问 Chat GPT "的扩展程序承诺用户可以快速与近期大火的人工智能聊天机器人 Chat GPT 进行互动。然而事实上，该扩展程序偷偷地从浏览器中窃取所有授权活动会话的 cookies，并安装了一个后门，使恶意软件运营者能够轻松获得用户 Facebook 账户的超级管理员权限。

值得注意的是，"快速访问 Chat GPT "扩展程序仅仅是威胁攻击者利用 ChatGPT 大火来分发恶意软件和渗透系统的众多方式之一。

近几个月，随着 ChatGPT 持续火爆，以其主题的钓鱼电子邮件急剧增加，越来越多的攻击者使用假冒的 ChatGPT 应用程序传播 Windows 和 Android 恶意软件。

# **以 Facebook 商业账户为目标的“僵尸军团”**

"快速访问 Chat GPT "的扩展程序实际上是通过连接聊天机器人的 API 实现了对 ChatGPT 的快速访问，但在访问过程中，该扩展还收集了用户浏览器中存储的包括谷歌、Twitter 和 YouTube 以及任何其它活动在内的所有 cookie 列表。

如果某个用户在 Facebook 上有一个活动、经过验证的会话，则恶意扩展插件为开发人员访问 Meta 的 Graph API。API 访问使扩展能够获取与用户 Facebook 帐户相关的所有数据，甚至可以代表用户采取各种行动。

更不幸的是，恶意扩展代码中的一个组件允许劫持用户的 Facebook 帐户，其方法是在用户帐户上注册一个恶意应用程序，并获得 Facebook 的批准。对此 Guardio 表示，Facebook 生态系统下的应用程序通常是一个 SaaS 服务，它被批准使用其特殊的 API。因此，通过在用户帐户中注册应用程序，威胁攻击者可以在受害者的 Facebook 帐户上获得完全管理模式，而无需获取密码或尝试绕过 Facebook 的双重身份验证。

如果恶意扩展遇到了一个 商业 Facebook 帐户，它会快速获取与该帐户相关的所有信息，包括当前活动的促销活动、信用余额、货币、最低计费阈值等。

# **一个有经济动机的网络罪犯活动**

在 Facebook 通过其 Meta Graph API 授予访问权之前，首先必须确认该请求是来自一个经过认证的可信用户，为了规避这一预防措施，威胁者在恶意的浏览器扩展中加入了代码，确保从受害者的浏览器向Facebook 网站发出的所有请求都被修改了标题，以便它们看起来也是可信的，这使得该扩展能够使用受感染的浏览器自由地浏览任何 Facebook 页面（包括进行 API 调用和操作），而不留下任何痕迹。

最后，Guardio 评估后表示，威胁行为者可能会将其从活动中收获的信息卖给出价最高的人，该公司还预计攻击者有可能创建一个被劫持的 Facebook商业账户的机器人大军，利用受害者账户的钱来发布恶意广告。

**参考文章：**

https://www.darkreading.com/application-security/chatgpt-browser-extension-hijacks-facebook-business-accounts

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