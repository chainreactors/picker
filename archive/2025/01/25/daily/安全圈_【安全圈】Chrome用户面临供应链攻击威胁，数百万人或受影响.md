---
title: 【安全圈】Chrome用户面临供应链攻击威胁，数百万人或受影响
url: https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067590&idx=4&sn=ab568c073e0bfe554ca07ca03503f2da&chksm=f36e7b46c419f2504e60fb5ecb4e5b4587d40c40ef28fa92ddedef841c052dddeb060feb9d4a&scene=58&subscene=0#rd
source: 安全圈
date: 2025-01-25
fetch_date: 2025-10-06T20:11:02.926211
---

# 【安全圈】Chrome用户面临供应链攻击威胁，数百万人或受影响

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljmku6eiapKnvNCalPibs0iaib8JZmArHvkriasbKZ8WBFPSmkmU6aRfccsxAyWibOByrnYqRALl6IdrYSw/0?wx_fmt=jpeg)

# 【安全圈】Chrome用户面临供应链攻击威胁，数百万人或受影响

安全圈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/aBHpjnrGylgOvEXHviaXu1fO2nLov9bZ055v7s8F6w1DD1I0bx2h3zaOx0Mibd5CngBwwj2nTeEbupw7xpBsx27Q/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

**关键词**

Chrome

网络安全机构Sekoia警告Chrome用户，针对浏览器扩展开发者的供应链攻击可能已经影响了数十万人。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/aBHpjnrGyljmku6eiapKnvNCalPibs0iaib8x8ibEQsNVwmDHYGrBVheJ5qqnGLWpP1jOFlG9wjgcAt7lkSOszyXX7A/640?wx_fmt=jpeg&from=appmsg)

Sekoia对开发者遭受的大规模网络钓鱼活动进行了调查，重点调查了该活动所使用的基础设施，相似活动可以追溯到2023年，已知的最新活动发生在2024年12月30日。

到目前为止，已有数十名Chrome扩展开发者成为攻击的受害者，这些攻击的目的在于在从ChatGPT和Facebook for Business等网站窃取API密钥、会话cookie和其他身份验证令牌。

## 受影响组织

总部位于加利福尼亚的Cyberhaven是此次攻击的受害者之一。该公司开发了一款基于云的数据保护工具。2024年节礼日期间，Cyberhaven发现其开发者账户被入侵，这一事件随后被广泛报道。

Booz Allen Hamilton分析了Cyberhaven的事件，并支持了供应商的怀疑，认为这是更广泛活动的一部分。附带的分析报告中揭示了一长串可能受到影响的其他扩展，潜在受影响的最终用户数量可能达到数百万。在Sekoia的研究中也发布了一份不太全面的列表，但两个列表中出现了相同的扩展。

根据Booz Allen Hamilton的报告，许多可能受影响的扩展在撰写报告时似乎已从Chrome网上应用店中撤下。许多其他扩展的页面显示它们自Cyberhaven事件以来已经进行了更新，尽管很少有扩展公开承认事件。一个例外是Reader Mode，其创始人Ryzal Yusoff向大约30万用户写了一封公开信，告知他们发生在12月5日的入侵。

Yusoff表示：“2024年12月5日，我们的开发者账户因一封模仿Chrome网上应用店官方通信的网络钓鱼电子邮件而受到入侵。此次入侵允许未经授权的第三方将恶意版本的Reader Mode扩展（1.5.7 和 1.5.9）上传到Chrome网上应用店。攻击于2024年12月20日被发现，当时Google发布了警告，识别了与此入侵相关的网络钓鱼尝试。扩展的恶意版本可能包含未经授权的脚本，旨在收集用户数据或执行其他有害操作。如果您在2024年12月7日至12月20日期间安装或更新了Reader Mode扩展，您的浏览器可能已受到影响。”

总部位于奥斯汀的Nudge Security的联合创始人兼首席技术官Jaime Blasco也在一系列在线帖子中提到了他怀疑受到入侵的扩展，其中也有许多出现在Booz的报告中。

## 冒充Chrome支持

根据Yusoff和Sekoia的说法，攻击者通过伪装成Chrome网上应用店开发者支持的钓鱼邮件，模仿官方通信，针对开发团队。

报告中出现的示例电子邮件显示，攻击者声称扩展可能因虚假规则违规（例如扩展描述中的不必要细节）而被从Chrome中撤下。受害者被诱骗点击伪装成Chrome网上应用店政策解释的链接，该链接指向一个合法的Google帐户页面，提示他们批准恶意OAuth应用程序的访问权限。一旦开发者授予应用程序权限，攻击者便获得了上传被入侵扩展到Chrome网上应用店所需的一切。

研究人员表示，开发者的电子邮件可能是从Chrome网上应用店收集的，因为这些信息在那里可能可以被访问。

## 调查基础设施

通过与网络钓鱼邮件关联的两个域名，Sekoia能够发现该活动中使用的其他域名以及可能涉及的先前攻击的域名。作为攻击者指挥和控制（C2）服务器使用的域名仅托管在两个IP地址上，研究人员通过被动DNS解析认为他们发现了可能在此次活动中被入侵的所有域名。

Sekoia表示，揭露最新攻击中使用的域名和2023年使用的域名“相对简单”，因为每次都使用了相同的注册商（Namecheap），DNS设置和TLS配置也保持一致。

Sekoia在博客中写道：“域名命名约定及其创建日期表明，攻击者的活动至少自2023年12月以来就已开始。可能通过SEO投毒或恶意广告推广了重定向到所谓恶意Chrome扩展的网站。”

Sekoia分析师认为，这个威胁行为者专门传播恶意Chrome扩展以收集敏感数据。在2024年11月底，攻击者将其作案方式从通过虚假网站分发自己的恶意Chrome扩展转变为通过网络钓鱼邮件、恶意OAuth应用和注入恶意代码到被入侵的Chrome扩展来入侵合法的Chrome扩展。

参考链接：https://www.theregister.com/2025/01/22/supply\_chain\_attack\_chrome\_extension/

***END***

阅读推荐

[【安全圈】美国前中情局分析师承认泄露国防信息](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067571&idx=1&sn=a6a2923967fc3df6b71885df15512f84&scene=21#wechat_redirect)

[【安全圈】威胁者利用语音通话通过 Microsoft Teams 传播勒索软件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067571&idx=2&sn=45297a18045334bd95045d0b8a1349db&scene=21#wechat_redirect)

[【安全圈】1,000 多个恶意域名模仿 Reddit 和 WeTransfer 来传播恶意软件](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067571&idx=3&sn=73a9d0ef87cb24230598fa943275617a&scene=21#wechat_redirect)

[【安全圈】美国政府公布攻击Ivanti云服务设备的技术细节](https://mp.weixin.qq.com/s?__biz=MzIzMzE4NDU1OQ==&mid=2652067571&idx=4&sn=77fe4aa9d36cfc0f445aaaa0237973dc&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEDQIyPYpjfp0XDaaKjeaU6YdFae1iagIvFmFb4djeiahnUy2jBnxkMbaw/640?wx_fmt=png)

**安全圈**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCEft6M27yliapIdNjlcdMaZ4UR4XxnQprGlCg8NH2Hz5Oib5aPIOiaqUicDQ/640?wx_fmt=gif)

←扫码关注我们

**网罗圈内热点 专注网络安全**

**实时资讯一手掌握！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

**好看你就分享 有用就点个赞**

**支持「****安全圈」就点个三连吧！**

![](https://mmbiz.qpic.cn/mmbiz_gif/aBHpjnrGylgeVsVlL5y1RPJfUdozNyCE3vpzhuku5s1qibibQjHnY68iciaIGB4zYw1Zbl05GQ3H4hadeLdBpQ9wEA/640?wx_fmt=gif)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

安全圈

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/aBHpjnrGylhgCQcCZBwQrSQRLABhjrXviafAj0avc5c69t69K1YymAruIaZWzXPqbGPourlnuu8pfibV0ebgqV9g/0?wx_fmt=png)

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