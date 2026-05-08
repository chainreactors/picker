---
title: 暗网平台Darkhub公开兜售加密货币诈骗、信息拦截与监控服务
url: https://mp.weixin.qq.com/s/nvvkcpNJA6a4qNBBcnxrmg
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:53:59.482633
---

# 暗网平台Darkhub公开兜售加密货币诈骗、信息拦截与监控服务

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX0n3I2ytibaIaq4xzHOt2xYnPQiaOL0SDy5g5TEOko5pvunVBgZpWxko6L7Hrniasx47A04CePjfKnCesdQARqD1LjPM3t05BSSaU/0?wx_fmt=jpeg)

# 暗网平台Darkhub公开兜售加密货币诈骗、信息拦截与监控服务

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2NLEdFjQrZtQlHqPpySaic5fINCibLYdwskZIzTjZMr89QNcstX1mHNN0haQCYr43MjgzSVG1FaicPiaTeSicygicTwoLxfP0p33fWg/640?wx_fmt=png&from=appmsg)

##

一个自称Darkhub的暗网平台近日在Tor网络上现身，公然向付费用户提供黑客雇佣服务。该平台将自己包装成网络犯罪活动的“一站式商店”，业务范围涵盖社交媒体账号入侵、私人信息拦截以及财务记录篡改等非法行为。Darkhub的显著特点在于其明目张胆的营销方式——通过精致的界面展示各类非法服务，仿佛在经营合法业务。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX3CicJVbuWPQyvicF8icYXtym7MAXEN0Dgz7qGwSKKgzCDZJpbfVDv6NXX1RHvaRACktHTUX3fpdCjNGcujxwAtcbKDMWGFPCwINY/640?wx_fmt=jpeg&from=appmsg)

Darkhub黑客雇佣服务平台界面，来源：Oasis Security

该平台同时针对普通用户和组织机构提供服务，包括未授权访问Instagram、Telegram和WhatsApp账号，以及电子邮件入侵、手机监控和个人实时位置追踪。更令人震惊的是，Darkhub还宣称提供加密货币相关欺诈服务、银行账户未授权访问以及信用评分篡改能力，在单一平台上集成了异常广泛的犯罪功能。

##

**Part01**

## ****服务范围与加密货币诈骗维度****

Oasis Security的研究人员发现并分析了该平台，揭示了其基础设施细节和所宣传服务的真实性质。调查显示，Darkhub不仅隐藏在Tor网络的匿名性背后，其服务还与一个可公开访问的IP地址相关联。这表明其部分后端系统暴露在加密的Tor环境之外——这对于依赖隐蔽性的服务而言是一个显著漏洞。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX1z1McbDMxuzic33MGOpwnR9JsGUGBribDjOraqx49BSoduu8VxDG8ticNXAdtrjmMqHtLibTiaQIRyuYncYvTz9XftCeN71FQX4ibQI/640?wx_fmt=jpeg&from=appmsg)

Darkhub网站服务列表与联系信息，来源：Oasis Security

分析人员特别注意到Darkhub目录中的“资金追回”和“信用评分操纵”类别，这些都具有预付费用诈骗的典型特征。此类骗局专门针对曾经的诈骗受害者，承诺追回损失资金，以换取永远不会退还的预付款。这些服务的存在表明，Darkhub可能同时针对两类目标：外部受害者和其付费客户。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX1PVKQ4b5e3mHJCJUWOd0Io6Jcep3Ioh056rvicoNwbp06OQia3iaWyOUSgtllTt39c8zYH4XfRLK3AP9gKcSyoDSNRJWsErpL6N8/640?wx_fmt=jpeg&from=appmsg)

Darkhub网站展示的服务项目，来源：Oasis Security

加密货币欺诈是增长最快的网络犯罪领域之一，而Darkhub等平台降低了非技术人员参与的门槛。通过提供付费服务，该平台使任何人都能委托实施数字犯罪。其联系方式包括Telegram账号和ProtonMail邮箱，刻意保持交互的匿名性。其中，“追回被盗资金”与加密货币服务的结合尤其具有揭示性——那些已经遭受加密货币诈骗损失的人群，正是后续诈骗最易攻击的目标。

**Part02**

## ****基础设施暴露与防弹托管关联****

Oasis Security调查的关键发现是识别出与Darkhub关联的可公开路由的IP地址。研究人员通过暗网情报平台Arthur追踪到，该网站的基础设施位于美国托管提供商ULTAHOST（ASN AS44259）旗下。该提供商此前已被第三方报告标记为具有防弹托管特征。

防弹托管提供商以无视滥用投诉著称，是网络犯罪运营的首选基础设施。该提供商还曾因钓鱼相关域名滥用问题收到ICANN合规通知，据称其营销材料强调宽松的内容政策——这正是暗网运营者所寻求的环境。与Darkhub关联的IP地址并不稳定，历史数据显示在2026年1月12日确定当前值之前曾多次变更。监控暗网威胁的组织应对该基础设施的任何流量保持高度警惕。

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3rvziaSuUqlARsUiacpV5uYHibHnEw97tyq3XAmaRH7v7aRWwW6Sznhh7A8q3jmsibodh2IUHyF2ZJiawBXibXBczVGQbjdgiaVwGZE0/640?wx_fmt=png&from=appmsg)

注：IP地址和域名已进行无害化处理（例如使用[.]），防止意外解析或超链接。仅在MISP、VirusTotal或SIEM等受控威胁情报平台中可恢复原始格式。

**参考来源：**

Darkhub Hacking-for-Hire Portal Advertises Crypto Fraud, Message Interception, and Monitoring

https://cybersecuritynews.com/darkhub-hacking-for-hire-portal-advertises-crypto-fraud/

---

**推荐阅读**

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX3sibbWQvVRVyGlKyVa2716Kwag7P05S8W9d2stbD2I5yumphAxFoD6wiaIuexgPZb927DudHtwckQpG2OichmhfROaGh45gNKibko/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651337545&idx=1&sn=772e37039accf79521a5b80e0032e89f&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX2AOA5HHVAjjGL1apmJN5zViaA4qX4mqict654rZb5qTMaUlxME4oNUU4ngFWCibn78oGgXB9d6A3hSLVwasycm2JrIwhUlllVWws/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLQDHPFqj89KkFsXBRibx5YTLiaTUfFOy9PKicps3l56iazUPNQrwdhkZ7jA/640?wx_fmt=png&from=appmsg)

**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibqyrdrvYXibMZM7K7gQW9ymeNepaIkpwPmicPSSoVicLBPXZ3a19uvVicYOjUZOibNeYRbrIOToCHjLAg/640?wx_fmt=png&from=appmsg)**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

FreeBuf

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibLOEAnkkKa2dHtqcjZ55KLsqibib6n4UDNUhLIuMRdAJ9ibfZkSK5LViaGJLEQN7p9OGo7mNnVv3EmkQ/0?wx_fmt=png)

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