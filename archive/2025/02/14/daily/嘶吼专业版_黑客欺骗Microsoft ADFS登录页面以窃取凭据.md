---
title: 黑客欺骗Microsoft ADFS登录页面以窃取凭据
url: https://mp.weixin.qq.com/s?__biz=MzI0MDY1MDU4MQ==&mid=2247581122&idx=1&sn=4e899e72f468455ac7dec2da2725c4c7&chksm=e9146df8de63e4ee6858223c6fb9d2ef87df17758bd104ffb3603842cfff0acebb4a2d9799d2&scene=58&subscene=0#rd
source: 嘶吼专业版
date: 2025-02-14
fetch_date: 2025-10-06T20:37:01.453890
---

# 黑客欺骗Microsoft ADFS登录页面以窃取凭据

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wpkib3J60o2icmCeJ4HSh4ibJfgUCHPG7bWibbibTZeuWenGhV0z7ZnsoTTichbTcuk5NpYgelVC0AT0icicCZvzA0k47w/0?wx_fmt=jpeg)

# 黑客欺骗Microsoft ADFS登录页面以窃取凭据

胡金鱼

嘶吼专业版

![](https://mmbiz.qpic.cn/mmbiz_gif/wpkib3J60o297rwgIksvLibPOwR24tqI8dGRUah80YoBLjTBJgws2n0ibdvfvv3CCm0MIOHTAgKicmOB4UHUJ1hH5g/640?wx_fmt=gif)

服务台网络钓鱼活动主要针对Microsoft Active Directory Federation Services（ADFS），使用欺骗性的登录页面来窃取凭据和绕过多因素身份验证（MFA）保护措施。据发现该攻击的安全公司称，此次攻击的目标主要是教育、医疗和政府机构，攻击目标至少有150个。

这些攻击旨在访问公司电子邮件帐户，以将电子邮件发送给组织内的其他受害者或进行经济攻击（例如商业电子邮件妥协（BEC）），将此付款转移到威胁者的帐户中。

# ![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icmCeJ4HSh4ibJfgUCHPG7bWP3J7tZIj3QNFdia7IgmNsic1FjBicOhEib07EsYUkhVXDxSnzCrCKqYWbA/640?wx_fmt=png&from=appmsg)欺骗Microsoft Active Directory联合服务

Microsoft Active Directory Federation Services（ADFS）是一个身份验证系统，允许用户登录一次并访问多个应用程序和服务，而无需重复输入其凭据。它通常在大型组织中用于在基于内部和云的应用程序中提供单登录（SSO）。

攻击者会向冒充其公司IT团队的目标发送电子邮件，要求他们登录以更新其安全设置或接受新策略。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icmCeJ4HSh4ibJfgUCHPG7bWyqfuYQgeuoyRrnVuNwPt6v2Ba7pMepTPnmK2zrPMb8fTOUTmBFv2icw/640?wx_fmt=png&from=appmsg)

攻击中使用的网络钓鱼电子邮件示例

点击“嵌入式”按钮会将受害者带到一个看起来与他们组织的真实ADFS登录页面一模一样的网络钓鱼网站。网络钓鱼页面要求受害人输入其用户名，密码和MFA代码，或引导他们批准推送通知。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icmCeJ4HSh4ibJfgUCHPG7bWicZG3Nouu9TkP6RmfS4s0mtRt4sKYAOgEj4AgDicGUV8JnScLprEoyAw/640?wx_fmt=png&from=appmsg)

欺骗的ADFS门户

网络钓鱼模板还包括基于组织配置的MFA设置来捕获验证目标帐户所需的特定第二因素的表单，针对多种常用MFA机制的异常观察到的模板，包括Microsoft Authenticator，Duo Security和SMS验证。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icmCeJ4HSh4ibJfgUCHPG7bW3DZnn4q8ib5cOOJTtRl7vRev5R1rqk8Gf8muqeZhVR9sh80AkU8Rwug/640?wx_fmt=png&from=appmsg)

两个可用的MFA旁路屏

一旦受害者提供了所有详细信息，他们就会被重定向到合法的登录页面，以减少怀疑，并使其看起来好像这个过程已经成功完成。

同时，攻击者立即利用窃取的信息登录受害者的帐户，窃取任何有价值的数据，创建新的电子邮件过滤规则，并尝试横向网络钓鱼。

安全公司表示，攻击者在这次活动中使用私人互联网接入VPN来掩盖他们的位置，并分配一个更接近组织的IP地址。

即使这些网络钓鱼攻击并没有直接违反ADF，而是依靠社会工程来工作，但由于许多用户对登录工作流的固有信任，该策略仍然是具有潜在有效性的。

安全工作人员建议相关企业应迁移到现代和更安全的解决方案，如Microsoft Entra，并引入额外的电子邮件过滤器和异常活动检测机制，以尽早阻止网络钓鱼攻击。

参考及来源：https://www.bleepingcomputer.com/news/security/hackers-spoof-microsoft-adfs-login-pages-to-steal-credentials/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icmCeJ4HSh4ibJfgUCHPG7bW5CJGVnvgP3EuuicNeU1wqeJPiaZoXDl8raXGay4ib4vbg3G3vt31VicA3A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o2icmCeJ4HSh4ibJfgUCHPG7bWnCXpIdO5dAeSPf3lfhMaqiajicXgV7uHIRmDmzp0yZZbmZibvGSHk0V4A/640?wx_fmt=png&from=appmsg)

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

嘶吼专业版

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/wpkib3J60o29QZSgjKMjM7j822AuVv1iaicmoBhDlvJq1s41w5yIxoicDK9AsOGHLnQYkqq95ibWgq3OqvvXEO1qBVg/0?wx_fmt=png)

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