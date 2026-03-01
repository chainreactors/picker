---
title: 特斯拉 Model 3 和 Cybertruck 存在多个漏洞，无线连接栈可遭拦截
url: https://mp.weixin.qq.com/s/AK7rbvH9yCX_beUy03WH3g
source: Doonsec's feed
date: 2026-02-28
fetch_date: 2026-03-01T04:17:12.749245
---

# 特斯拉 Model 3 和 Cybertruck 存在多个漏洞，无线连接栈可遭拦截

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/t5z0xV2OYfUCZodwkeictkBouibP9xt2cRVnJpRXuaAVicrNfshZIpHaUq36oVQwEMBlOalLGuwvUwzH1tlibO4AXBtIbP7OYYdxIHLkeqOyjzI/0?wx_fmt=jpeg)

# 特斯拉 Model 3 和 Cybertruck 存在多个漏洞，无线连接栈可遭拦截

代码卫士

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/Az5ZsrEic9ot90z9etZLlU7OTaPOdibteeibJMMmbwc29aJlDOmUicibIRoLdcuEQjtHQ2qjVtZBt0M5eVbYoQzlHiaw/640?wx_fmt=gif)聚焦源代码安全，网罗国内外最新资讯！

**作者：Cesareo Contreras**

**编译：代码卫士**

**美国东北大学近期开展的一项研究显示，黑客可利用特斯拉 Model 3 和 Cybertruck 的无线系统追踪车辆、中断通信以及干扰网络性能，凸显了现代联网汽车面临的更广泛安全风险。**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfVJloC6BFPgGkLoCKqXEZ5keUOuwRvnU6UsJc7vmFpwybzZKmrbwSia7LnEsiaL0sUIjcz68OhKjcCBAaP7icbQERvSLAutVG2mos/640?wx_fmt=gif&from=appmsg)

**车轮上的计算机**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXooY8OMnw70sDPaYfTXicQzObv6Ee38NGujrJyyu0JKHHamfZbbbt5ztTYEKHtt3ib6dYZrvcEQOJiaLl88rnSLLmxBR4J6BsPyg/640?wx_fmt=gif&from=appmsg)

现代联网汽车正在日益变为“车轮上的计算机”。它们配备了用于持续连接的蜂窝和Wi-Fi调制解调器、用于导航的GPS、用于连接手机的蓝牙天线，以及一系列支持安全功能的“车联万物 (V2X)”技术。

和智能手机或几乎任何联网设备一样，这些车辆也容易受到攻击。不过，研究人员提到，与允许用户下载应用程序来追踪恶意活动或手动禁用网络的智能手机不同，如今道路上的许多车辆"为了支持远程诊断、OTA更新和应用程序通信，会保持持续的连接性"。

东北大学Khoury计算机科学学院的教授Aanjhan Ranganathan指出：“对于购车者来说，最需要记住的是：现代车辆是始终在线的、无法控制或监控的联网设备。”他与东北大学网络安全与隐私专业博士生Evangelos Bitsikas和Jason Veara合作，开展了对特斯拉车辆的第四代长期演进（即4G LTE）连接的研究。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXotFTSyZWqeb8UyoP3c2oDeVwOGeBicuXibFicp0FhRqvic5o8K0pKVtnVW7ia3qHXI3Z8sKvfcZeyLjVuxlKv97oWR75vzUSEA0Uo/640?wx_fmt=gif&from=appmsg)

**IMSI捕获如何入侵特斯拉车辆**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXibLicibJXUohQ0uZ2IdoAAmnyhicEZvFGWKA3LtMBoDTtbckM079OUTppHRMxwTsnqCeHLvPztTqUr0d2KDicUib3qoxHEF294aNOk/640?wx_fmt=gif&from=appmsg)

研究人员发现，黑客入侵特斯拉车辆的一种主要方式是通过“IMSI捕获”的方式。IMSI是国际移动用户识别码的缩写，每个连接到网络的用户都会被分配一个唯一的IMSI号码，用于在该网络上识别和验证身份。虽然IMSI号码在联网时通常不可见（会使用临时移动用户识别码来代替），但在某些情况下，它们可能被黑客捕获，获取的信息包括设备何时首次上线或需要重新连接到网络。

Bitsikas表示，黑客可以使用"IMSI捕获器"（模仿手机信号塔的设备）连接到车辆并追踪其位置，“任何使用蜂窝调制解调器的系统都可能处于这样一种情况：附近的'假基站'会影响其连接方式，尤其是当攻击者物理距离很近时尤为如此。”

黑客还可以利用假基站来控制车辆的连接性，阻止汽车连接到互联网，拦截数据流量，并迫使车辆进入"安全性较低"的操作模式。Bitsikas指出：“需要注意的是，这并不自动意味着‘可以远程控制汽车’，但它确实会影响通信和隐私（例如，与特斯拉服务器的后端通信）。”

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfVRicBP6Ooe7yelKJXP92v0xQ2ZLtwFUyGuCF2LLBxx6sPKGiaW58dlxc023QNQgXkBzp4abHE6KFIibAXZwTCqxonX9FBAeO2j2g/640?wx_fmt=gif&from=appmsg)

**短信、紧急系统与滥用风险**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUIBAtmiajFv8l0r6F5I5hqgx2PvdjBevzoNqVkFJiayH4jfOOiaJSQ85ia06cn7rnzNlyHowptMlXAicv7qcWrfr17xZ2eKjIu8lkQ/640?wx_fmt=gif&from=appmsg)

研究人员还发现了车辆短信和紧急服务系统的漏洞，黑客可以利用这些系统发送垃圾信息、发布虚假警报，并造成拒绝服务攻击。Bitsikas指出：“风险不在于'有人通过一条短信黑掉整辆车'，而在于消息信道可能被滥用、伪造，或被用于干扰/工程攻击，具体取决于接收系统的设计方式。”

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfViamtqqhprwSGjFFPvnF2zGbKDKYUtPiaJfia5fPZKl496NMP4LEyjPhe2GFWV36qvRhweEhx4YwMPvKm83HibVxZWNKWDlfFrB04/640?wx_fmt=gif&from=appmsg)

**为何问题不仅限于特斯拉**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfWuky2VEf46jD6wRGlXiarlwUuDchuGxlNGXgbGt8XCpO0jYpnZbAyWRRg28cBuS6VEvXhblP7MpharRVQkM1x6ibDDQ8uQLiaF1Y/640?wx_fmt=gif&from=appmsg)

需要明确的一点是，特斯拉并非唯一易受此类攻击的联网汽车制造商。这类漏洞源于由第三方科技公司高通和移远组件构成的蜂窝调制解调器。

研究人员选择调查特斯拉的最大原因是，与其它汽车制造商相比，特斯拉的后端更便于进行诊断和实验。但大多数现代汽车也依赖这些公司提供蜂窝和无线技术，"因此，这个问题几乎适用于所有现代联网汽车。"

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUq6eomdQmITo7DIkRBwgTSMHguaQ2iaUb2FkCicdIFyPegfib9tpn4EyH0dvJ6KovbAagdTM1d8Z7oEaHoDSXDDvQWJCEBfFibGl8/640?wx_fmt=gif&from=appmsg)

**研究联网汽车安全的挑战**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWk32gsHhfvzEmEbHJvyO107kSibOtKW59OBwGyjU642kehCgClz93icEtavha8x75kEDpzOTQVeg7Q160zRvyqw6iaxA4OnDDMxs/640?wx_fmt=gif&from=appmsg)

研究人员强调称，当前针对联网汽车安全性的研究仍然有限，原因在于：首先，为实验目的获得车辆可能既困难又昂贵，而且一旦拥有车辆，研究人员通常需要为其配备昂贵的测试设备。此外，研究人员必须考虑一系列安全、技术和伦理挑战，包括在道路内外进行实验时最大限度地减少伤害。

在这项研究中，非营利媒体组织”消费者报告 (Consumer Reports)”将Model 3和Cybertruck借给了研究人员，与该大学合作开展一系列与联网汽车相关的研究项目。研究人员测试的是2024款车型。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfWah1ib4ibWMWley6cAHZEAQ4MwpkSickftLsfCcG4WMz1EwcIWQiawB0icNYL16KHfeMxTTjtwDzIFeNrpQT4BZPOp9yxIZURXLzcw/640?wx_fmt=gif&from=appmsg)

**特斯拉的回应及后续步骤**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfXLeVjXHO3nFF3Q3o8WZl2XGIuPJ7XZvBHx6joHXDQCibjuKPWN5icocw5frd0v0Cicia7LJ9t31zyiaLTfL6Nr6amrdSIjLM1QqkR4/640?wx_fmt=gif&from=appmsg)

研究人员将研究结果告知特斯拉，特斯拉"承认许多已识别的弱点源于第三方（特别是高通和移远）提供的蜂窝调制解调器协议栈（而非车辆软件）"。东北大学全球新闻团队也联系了特斯拉，但尚未收到任何评论。

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/t5z0xV2OYfUbvLM0H6HcZHibKiaicfsm5cgHQ9NnQqgt827t5y0DfI2pxuU448lw80fUYd4N8uFswcyho5nXN1mKfkgH5C4I07vbAHFVRYtKfQ/640?wx_fmt=gif&from=appmsg)

**潜在的修复措施及车主的应对**

![](https://mmbiz.qpic.cn/mmbiz_gif/t5z0xV2OYfXicK8zJH59zUrQZ9KRrtCl2E564m3pkefrUa3xDIQH4AAJqyJS8mRLOoDz2umibGdwr4b6pnfwEtibLJdT9ick0BTxRQWwQWLNhFU/640?wx_fmt=gif&from=appmsg)

在缓解策略方面，研究人员提供了许多建议，包括鼓励汽车制造商继续升级到5G蜂窝网络技术（与LTE相比，5G具有"更强的身份保护机制"），完全消除不安全的2G和3G回退模式，并更新所有系统，使其符合联合国和国际标准化组织制定的网络安全标准。不过这些建议需要由汽车制造商自己来实施。

研究人员表示，对于消费者来说，最重要的是要认识到驾驶现代汽车上路所带来的潜在安全风险。Ranganathan表示：“当购买联网汽车时，你接受的是一个你无法关闭、禁用或切换到首选网络的蜂窝连接。但许多功能都是通过这个蜂窝连接提供的，因此当出现问题时，很难能够'关闭再打开'连接。”

开源卫士试用地址：https://oss.qianxin.com/#/login

代码卫士试用地址：https://sast.qianxin.com/#/login

---

**推荐阅读**

[在线阅读版：《智能网联汽车云平台漏洞分析报告》全文](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524907&idx=1&sn=56ac025aa6a6fcc0f1243163f93a12bc&scene=21#wechat_redirect)

[2026 Pwn2Own 东京汽车大赛落下帷幕，Master of Pwn 诞生](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247524969&idx=1&sn=fbd3e630ba31d2f0118b90ad0779d309&scene=21#wechat_redirect)

[Flipper Zero WiFi 钓鱼攻击可解锁和开走特斯拉](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247519025&idx=1&sn=767127cd1ed21591b30ff37097d63531&scene=21#wechat_redirect)

[研究员低成本破解特斯拉自动驾驶系统、解锁“埃隆模式”、访问关键数据](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247518552&idx=1&sn=de800d1d6ebc39243e22991c5fe5bf41&scene=21#wechat_redirect)

[美国国家安全委员会不慎泄露2000多家机构凭据，包括NASA、特斯拉等](https://mp.weixin.qq.com/s?__biz=MzI2NTg4OTc5Nw==&mid=2247517538&idx=1&sn=650f77bfd40168fc3045174a8fa46fda&scene=21#wechat_redirect)

**原文链接**

https://techxplore.com/news/2026-02-vulnerabilities-tesla-cybertruck-reveal-cars.html

题图：Pixabay License

**本文由奇安信编译，不代表奇安信观点。转载请注明“转自奇安信代码卫士 https://codesafe.qianxin.com”。**

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSf7nNLWrJL6dkJp7RB8Kl4zxU9ibnQjuvo4VoZ5ic9Q91K3WshWzqEybcroVEOQpgYfx1uYgwJhlFQ/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/oBANLWYScMSN5sfviaCuvYQccJZlrr64sRlvcbdWjDic9mPQ8mBBFDCKP6VibiaNE1kDVuoIOiaIVRoTjSsSftGC8gw/640?wx_fmt=jpeg)

**奇安信代码卫士 (codesafe)**

国内首个专注于软件开发安全的产品线。

   ![](https://mmbiz.qpic.cn/mmbiz_gif/oBANLWYScMQ5iciaeKS21icDIWSVd0M9zEhicFK0rbCJOrgpc09iaH6nvqvsIdckDfxH2K4tu9CvPJgSf7XhGHJwVyQ/640?wx_fmt=gif) 觉得不错，就点个 “在看” 或 "赞” 吧~

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