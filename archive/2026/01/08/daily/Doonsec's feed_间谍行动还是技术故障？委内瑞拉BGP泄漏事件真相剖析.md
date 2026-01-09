---
title: 间谍行动还是技术故障？委内瑞拉BGP泄漏事件真相剖析
url: https://mp.weixin.qq.com/s/9-Uuxvh0rZ7mwsPKfo0g2w
source: Doonsec's feed
date: 2026-01-08
fetch_date: 2026-01-09T03:29:30.078729
---

# 间谍行动还是技术故障？委内瑞拉BGP泄漏事件真相剖析

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR394NmBBpZoDqlukekR6EWdY2kHE79FUEHzpS778LgFRicbbQUxOiamy3mR7qo3b7tNd9wOOUpODM0xQ/0?wx_fmt=jpeg)

# 间谍行动还是技术故障？委内瑞拉BGP泄漏事件真相剖析

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/mmbiz_jpg/qq5rfBadR394NmBBpZoDqlukekR6EWdYcZFeQGZOVia2O3ibISoFwy2FVGoTYwwT16j7tJVSTuCe73ck5tibIeK4A/640?wx_fmt=other&from=appmsg)

**Part01**

## ****事件概述****

近期安全分析师发现，委内瑞拉国有电信公司CANTV在美国针对尼古拉斯·马杜罗的军事行动前夕发生BGP泄漏事件。通过事后数据分析还原，部分观察者推测这可能是美国政府为获取军事行动关键情报而实施的流量劫持。

**Part02**

## ****间谍行动还是技术故障？****

```

```

这一发现迅速引发安全社区广泛关注，并引起Cloudflare安全研究团队的注意。但经过历史路由数据核查，Cloudflare分析师Bryton Herdes认为CANTV的BGP泄漏更可能是技术失误所致——当地时间2026年1月2日，就在美国对委内瑞拉发起特别军事行动前，该国国有运营商CANTV（AS8048）出现了明显的BGP泄漏。

部分分析人员观察到，AS8048的流量异常重定向至意大利中转服务商Sparkle，这家以不执行RPKI过滤且安全声誉不佳闻名的运营商。有观点将此路由异常解读为情报机构为实施中间人拦截与流量收集的蓄意操作。值得注意的是，异常路径表现出极端自降优先级特征：AS8048执行了多达十次AS路径预置（AS-path prepending），这在BGP协议中会导致路由吸引力骤降。

Cloudflare团队指出，若攻击者意图窃取流量，理应发布更短、更具吸引力的路由，而非刻意制造多次绕行。另一个关键证据是事件复发模式——自2025年12月以来，AS8048已发生多达11次类似路由泄漏，强烈表明这是CANTV长期存在的出入口过滤策略缺陷，而非针对特定军事行动的孤立行为。

运营商层级关系同样削弱了间谍论调。受影响IP前缀属于委内瑞拉本地服务商Dayco Telecom（AS21980），而CANTV作为其上游运营商本已拥有合法流量访问权限，实施复杂BGP劫持显得多此一举。该事件再次暴露BGP安全机制的脆弱性——尽管Sparkle因未执行RPKI过滤被标记为不安全，但即便部署RPKI路由源验证（ROV）也无法阻止此类异常，因为ROV仅能验证路由发布者身份，而本次事件中路由源并未改变，仅中间路径异常。

**Part03**

## ****事件暴露的安全问题****

```

```

这一局限性凸显了IETF正在推进的新标准ASPA（自治系统提供商授权）的重要性。ASPA允许网络正式声明其合法上游提供商，若广泛采用，可自动阻断AS8048流量不当转发至无关提供商的"发夹式"泄漏。

**Part04**

## ****事件启示****

```

```

Cloudflare警示称，虽然将委内瑞拉网络异常归因于电信级特殊行动更具戏剧性，但现实往往更为平淡：互联网基础设施最严重的弱点常源于基础运维失误。该事件提醒全球运营商，在混合战争时代，全面落实RFC 9234标准和"仅限客户"（OTC）属性已不仅是技术实践，更关乎国家基础设施保护。

**参考来源：**

Spy Games or Glitch? The Truth Behind Venezuela’s BGP Leak

https://securityonline.info/spy-games-or-glitch-the-truth-behind-venezuelas-bgp-leak/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR39H4eicalbOEwZ1t8X3mSSZssMSDW4LkuO5g3W31c7ibGVXTlUPk3BqrUoic8Rqt25DJOCygq1FzABicw/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651333596&idx=1&sn=a5f1d8decaf400a24f3b9e74a3a357e1&scene=21#wechat_redirect)

###

### **电台讨论**![](https://mmbiz.qpic.cn/mmbiz_png/qq5rfBadR3ibvNluUKZ6RPy7h2fbYibRbLq7T2qZrtcsoq5PRQ2cjDU1HUaakGzExOsSIU2Quxiasf7W9ibLiaEsmWA/640?wx_fmt=png&from=appmsg)

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