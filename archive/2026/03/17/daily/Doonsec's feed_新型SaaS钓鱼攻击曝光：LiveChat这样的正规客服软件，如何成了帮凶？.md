---
title: 新型SaaS钓鱼攻击曝光：LiveChat这样的正规客服软件，如何成了帮凶？
url: https://mp.weixin.qq.com/s/X9ATFuSF6cObBf2Vx_pCyA
source: Doonsec's feed
date: 2026-03-17
fetch_date: 2026-03-18T04:20:23.699355
---

# 新型SaaS钓鱼攻击曝光：LiveChat这样的正规客服软件，如何成了帮凶？

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K3TsiatHicmGLE3R8u8zynZDctLfDucvVlVpGYSS8Xs7wUMtK51jnxN3kgRwtFOlu56Js6BXUTfz2ld91dAC6eHA3atxc6QJibC0g/0?wx_fmt=jpeg)

# 新型SaaS钓鱼攻击曝光：LiveChat这样的正规客服软件，如何成了帮凶？

看雪学苑
看雪学苑

看雪学苑

![]()

在小说阅读器中沉浸阅读

> 你是否收到过自称来自PayPal或亚马逊的退款或订单确认邮件？如果点开了邮件中的链接，你可能会进入一个看似官方的在线客服聊天窗口。但请注意，这很可能是一个精心布置的陷阱。

网络安全研究机构Cofense近日揭露了一种新型钓鱼攻击手法。与以往将用户导向仿冒登录页面的传统方式不同，攻击者如今开始“借用”那些我们日常信任的正规客服工具，特别是SaaS平台LiveChat，来实施更具迷惑性的诈骗。

在这场骗局中，攻击者利用LiveChat的合法域名（lc[.]chat）来托管欺诈页面。受害者会收到一封精心炮制的邮件，内容通常与退款或待处理的订单有关，并附带一个链接。由于链接指向的是LiveChat的官方域名，很容易让人放松警惕。

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1lYE0yDqFO7Jib5ts1BocqCd6M3lAqRzT1f23c44Dtqoh0VqNuicJiavNjkZIwlW2oKepuaToTFXQpic0dAv57vk4F6RTdeyza43I/640?wx_fmt=png&from=appmsg)

一旦点击链接，用户并不会直接看到假的登录页面，而是进入一个看起来非常正式的在线客服聊天界面。以仿冒PayPal为例，一个自动聊天机器人会立刻出现，热情地与用户打招呼。而在另一个仿冒亚马逊的案例中，用户则被要求先输入邮箱地址，随后才有“客服”介入。

整个信息套取过程被设计成了多步骤的“剥洋葱”式操作，目的是尽可能多地获取受害者的个人隐私和财务信息。

在仿冒亚马逊的版本中，所谓的“客服”会以身份验证为由，依次索要用户的邮箱、手机号、出生日期和家庭住址。对话的语言虽然有些生硬（例如使用“Ello”这样的非正式问候），甚至带有拼写错误，但这反而透露出一个信号：屏幕背后可能是一个真人攻击者，正照着脚本实时操控对话。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1vzVPg7ial5pwhQMYGNENEvMq7ia4TgbgiacbjOCyaUyefXKS9u2ZE8tg9uVDEkQt6CX9NIQd9tueE1EwCGkJSBA3gcvcrpm2kdM/640?wx_fmt=png&from=appmsg)

获取基本信息后，骗局开始升级。“客服”会告知用户有一笔200美元的退款待处理，但声称系统中没有用户的银行卡信息。随后，便会顺理成章地要求用户提供完整的信用卡号、有效期和安全码（CVC），并信誓旦旦地保证会“严格保密”这些信息。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1YzHfibQf3RgyYwrHiaibaYLoTEfHZu7rfiba7xTl3EicDKex84gbklS3icyQdomicXWoaRAlQseD7fG4aNwdBRwZp3qre3boteMNgLE/640?wx_fmt=png&from=appmsg)

仿冒PayPal的版本则更为复杂。在聊天机器人发送一个外部链接后，用户会被引导至一个假冒的PayPal登录页面。在这里，攻击者不仅能窃取账号密码，还会拦截用户输入的手机多因素认证（MFA）码，从而突破账户的又一道防线。登录后，一个包含出生日期和银行卡信息的表格等待着用户填写。最后，当用户提交最终的MFA验证后，还会被引导回最初的聊天窗口，收到一个“退款已处理”的虚假确认，整个骗局至此完成闭环。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Cpo2XCpI7K1k31KrmsM7kr3Ml6ur2hAsLqV4ByavGeBNicZ31JSHxo2e8XbxCl8SrGvAhWNLe9e6fmdU5woafZQUMR7Yej29ht5bNDVN7SxI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Cpo2XCpI7K1me6xa2U3CB6F9wvno6uRNl2pz8BWkbc7RFRTFgTznTwwjg4Udsqnr4bDHR8qviab7px0stFf5W4eD8oIibU57ewkgDUgN7sCpw/640?wx_fmt=png&from=appmsg)

这种新型钓鱼手法，核心在于利用用户对合法软件和正规客服流程的信任。当虚假的互动与真实的品牌和专业的工具有效结合时，用户很难分辨真伪。

如何防范？以下几点请牢记：

1.  警惕退款和订单通知：对任何未经请求的退款、订单确认或账户异常邮件保持高度警惕，尤其是那些引导你点击链接“了解更多详情”的邮件。

2.  核对网址：虽然攻击者使用了LiveChat的合法域名（lc[.]chat）作为跳板，但最终目的仍是引导你至外部页面。在输入任何敏感信息前，务必反复核对浏览器地址栏的网址是否为官方网站。

3.  识别危险信号：任何通过在线客服聊天窗口索要你的多因素认证（MFA）验证码、完整银行卡号、密码或出生日期等敏感信息的行为，都是极其危险的信号。请立即终止对话。

4.  直接联系官方：如果对收到的信息存疑，最稳妥的方式是不要点击邮件中的任何链接，而是通过浏览器直接访问品牌的官方网站，或拨打官方客服电话进行核实。

5.  企业防护建议：企业安全团队应监控网络中是否存在发往lc[.]chat等域名的可疑流量，并及时阻断已知的恶意URL，以降低员工和客户面临的风险。

资讯来源：本文基于Cofense研究人员发布的关于新型SaaS钓鱼攻击的分析报告进行编译和整理。

﹀

﹀

﹀

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=jpeg)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8Fjcl6q2ORwibt8PXPU5bLibE1yC1VFg5b1Fw8RncvZh2CWWiazpL6gPXp0lXED2x1ODLVNicsagibuxRw/640?wx_fmt=gif&from=appmsg)

**球在看**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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