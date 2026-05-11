---
title: 德国国家级顶级.de域名已从互联网上消失，半个德国离线
url: https://mp.weixin.qq.com/s/Xuvk4211A9OPo1NmmRlv6g
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:54:14.999254
---

# 德国国家级顶级.de域名已从互联网上消失，半个德国离线

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/hfjKPyxBDjqU1bNuM6fuDLBCVeiaDYCmwhu6DN5DsmPvoNLCoFOy8mZ8lg2zyCxr9IOwI4VX6v5eOiahFGNr8sxsCsSwIib51xgicibIlk2IyOOA/0?wx_fmt=jpeg)

# 德国国家级顶级.de域名从互联网上消失，半个德国离线

原创

铸盾安全
铸盾安全

河南等级保护测评

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/hfjKPyxBDjoQ8HiabojibOvBAW5DrCr1ib2VMZBSeNT896c2v8ZTpyRXeNhJxQSiczSp725QINyJkD4ssRuFORibs2WjRasJwqHeC2bPD9RPmPP0/640?wx_fmt=png&from=appmsg)

**德国“.de”域名大规模宕机，一次DNSSEC签名错误导致数千万网站离线**

德国近日发生近年来最严重的互联网基础设施故障之一。由于DNSSEC配置异常，德国国家顶级域“.de”出现大范围解析失败，导致数百万网站短时间内无法访问，包括电商、银行、媒体、物流及公共服务平台均受到影响。此次事件并非黑客攻击，而是一次由DNSSEC数字签名错误引发的“信任链崩溃”。

根据德国域名注册管理机构DENIC的说明，故障发生于维护过程中，问题与DNSSEC（Domain Name System Security Extensions）相关。DNSSEC的作用，是通过数字签名验证DNS记录真实性，防止域名解析遭篡改或劫持。然而在此次事件中，.de域名区的签名记录出现异常，导致Google 8.8.8.8、Cloudflare 1.1.1.1、Quad 9等启用了DNSSEC验证的公共解析器，将大量.de域名直接判定为“不可信”，并返回SERVFAIL错误。

研究人员指出，此次事故的核心问题在于“错误签名被正式发布到了生产环境”。由于DNSSEC属于严格校验机制，一旦签名与密钥不匹配，验证型解析器会主动拒绝访问，以防止潜在DNS劫持攻击。结果是，虽然网站服务器本身并未宕机，但大量用户仍然无法打开网站。受影响的平台包括Amazon.de、DHL、Bahn、Spiegel等德国核心互联网服务。

业内分析认为，此次事故很可能与DNSSEC的Zone Signing Key（ZSK）轮换有关。部分网络工程师怀疑，DENIC在执行密钥轮换时发布了错误的RRSIG签名记录，导致整条DNSSEC信任链失效。不过DENIC尚未正式确认具体技术细节，目前仍在进行根因调查。

事件发生后，Cloudflare等公共DNS服务商一度临时关闭.de域名的DNSSEC验证，以恢复网站访问能力。这意味着，为了保证可用性，部分解析服务被迫暂时降低安全校验等级。研究人员指出，这种做法虽然有效缓解了故障，但也暴露了DNSSEC在现实世界中的两难局面：安全机制越严格，配置错误带来的影响就越大。

此次事故再次暴露互联网基础设施存在的“单点失效”问题。虽然.de只是德国国家域名，但由于德国互联网规模庞大，仅一次错误签名就影响了约1770万个域名。**安全研究人员Leonard Schmedding表示：“没有黑客攻击，没有供应商故障，仅仅一个位于法兰克福的加密密钥错误，就让半个德国互联网离线。”**

更值得关注的是，2026年10月ICANN计划进行全球DNS Root Key Rollover（根密钥轮换）。业内担忧，如果未来全球根密钥轮换过程中出现类似配置错误，其影响可能远超德国此次事故，甚至可能导致全球DNSSEC域名出现级联解析故障。

安全专家认为，此次事件释放出几个重要信号。首先，DNS与DNSSEC已不再只是“后台基础设施”，而是国家级关键基础设施；其次，现代互联网越来越依赖少数核心信任系统，一旦这些系统配置错误，即使没有攻击者，也可能引发全国级网络中断；最后，未来网络安全挑战不只是“防黑客”，还包括如何避免复杂安全机制自身成为新的系统性风险。

###

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sNicKB84ZxoERdyt2icMobIJOJ7gZ6EE7A5Lu91AicvWMVsCUpMGUVic1PkJD8nJULlZG3XyRDzTNpQbVsfyFBLYeg/0?wx_fmt=png)

河南等级保护测评

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sNicKB84ZxoERdyt2icMobIJOJ7gZ6EE7A5Lu91AicvWMVsCUpMGUVic1PkJD8nJULlZG3XyRDzTNpQbVsfyFBLYeg/0?wx_fmt=png)

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