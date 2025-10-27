---
title: 因办公应用程序导致大规模数据泄露，涉及900家公司
url: https://mp.weixin.qq.com/s?__biz=MzUzNDYxOTA1NA==&mid=2247546220&idx=2&sn=8783facad472684b0902aa07d00257f9&chksm=fa9383adcde40abb34b4ddbbbc035937b19a3eb9256cea802f89c26b78e44bffc8a89c283c7f&scene=58&subscene=0#rd
source: CNCERT国家工程研究中心
date: 2024-08-07
fetch_date: 2025-10-06T18:04:49.940268
---

# 因办公应用程序导致大规模数据泄露，涉及900家公司

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176lsPeECN1yxChvqJWdrXMNPXsU7zwzMBZGQXtI7D56DcVQoyfObVkIhyfxTHQPLMFnsURIlxNeohQ/0?wx_fmt=jpeg)

# 因办公应用程序导致大规模数据泄露，涉及900家公司

网络安全应急技术国家工程中心

近日，有研究人员发现了一次大规模的数据泄漏事件，共涉及到大约 900 家公司和组织，其中包括戴尔、Verizon、AT&T、能源部、康卡斯特和大通银行等。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibM1HgDcNB10fyhmxH97pEhJTBaw0e9aviaibyZACUpwCCMRX3SAB6c1Khuh3RFWFPakep7WNv5letA/640?wx_fmt=png&from=appmsg&wxfrom=13&tp=wxpic)

今年 3 月 25 日，Cybernews 研究小组发现了一个可公开访问的网络目录，该目录属于马里兰州的 Simpli 公司（前身为 Charm City Concierge）。

该公司的应用程序允许租用办公空间的公司的员工查看位于同一栋大楼内的商店。它列出了可用的便利设施、工作场所福利和折扣，并使用户能够订购各种服务和产品。

这个开放的网络目录存储了 2024 年 1 月对公司网站和 Simpli 应用程序数据库的备份数据。据悉，此次泄露的应用程序的备份暴露了 10000 名员工的电子邮件地址和来自大约 900 家公司的哈希密码。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibM1HgDcNB10fyhmxH97pEhXAyNDvI1cRgXFF6eaxCNNReowzfPJKHJXCpxpZwzHibHmryRe8DNTjw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

包含网站和数据库备份的网络目录被曝光

受影响的公司包括：

* Capital One
* 海军分析中心
* 美国律师协会
* 微策略
* 剑桥联营公司
* 戴尔
* 威瑞森
* 康卡斯特
* 西部交通
* WeWork
* 信托银行
* 美国电话电报公司
* 国家残疾人委员会
* 能源部
* 大通银行

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibM1HgDcNB10fyhmxH97pEhJtUK7iab9d45PPlGXugbREET7fribiaFzMzByZd7paO34KD36AXIrsDzQ/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

带备注的订单信息

由于大多数员工都使用公司电子邮件地址注册了 Simpli 服务，因此这构成了重大风险。威胁攻击者有可能通过使用凭据填充攻击，将目标锁定在员工可以访问的更敏感的公司系统上。

Cybernews 的信息安全研究员 Aras Nazarovas 说：虽然员工凭证是以相对安全的格式存储的，但密码仍有可能被破解，尤其是弱密码。

如果员工在多个账户中使用相同的密码，被破解的密码就可以用来登录其他更敏感、与工作相关的终端。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibM1HgDcNB10fyhmxH97pEhhWORp510Pm3tqbnLtyS6ibz2Aoz4k9CjZPBjmaC2PrN8VTWibiaUQdoSw/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

建筑物及其租户清单

此次泄露的数据库还曝光了通过该应用程序发出的指令，其中一些指令包含可能涉及敏感业务信息的备注。这些笔记包括来自不同公司的个人之间的会议细节和会议目的。

在开放目录中发现的文件表明，这些信息可能是在该公司将其系统从 Drupal 7 迁移到 Drupal 9 时泄露的。目前 Simpli 公司暂未对此做出回应。

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibM1HgDcNB10fyhmxH97pEhholSwuZiabiaibTWyGUKQcSJlZ1lBck4RHtZsU9vTLg4Dw3705LFkDnFA/640?wx_fmt=png&from=appmsg&tp=wxpic&wxfrom=5&wx_lazy=1&wx_co=1)

用户凭证

# **供应链攻击风险**

此类泄密事件凸显了使用第三方服务的固有风险，这些服务可能会带来供应链攻击的风险。在这种网络攻击中，威胁者往往会寻找供应网络中的薄弱环节，而不是直接针对一家公司。

攻击者攻破一个供应商，就有可能影响到使用该供应商产品或服务的公司。从第三方供应商处提取的凭据对于已经瞄准一家公司的恶意行为者来说可能非常有用。

零售商 Target 就曾遭受过此类攻击。2013 年，恶意行为者入侵了 Target 的制冷、供暖和空调分包商 Fazio Mechanical，并将恶意软件传播到 Target 的大部分销售点设备。据报道，恶意软件当时共收集到了大约 4000 万张借记卡和信用卡的财务信息。

因此，提供第三方服务的公司和组织应该对网络安全问题格外保持警惕，因为这些公司极有可能会成为攻击者的目标。

**参考资料：**

https://cybernews.com/security/simpli-app-data-leak/

原文来源：FreeBuf

“投稿联系方式：010-82992251   sunzhonghao@cert.org.cn”

![](https://mmbiz.qpic.cn/mmbiz_jpg/GoUrACT176n1NvL0JsVSB8lNDX2FCGZjW0HGfDVnFao65ic4fx6Rv4qylYEAbia4AU3V2Zz801UlicBcLeZ6gS6tg/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

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