---
title: 网络安全行业，为什么会存在安全优先还是业务优先的矛盾
url: https://mp.weixin.qq.com/s/AjhuAtJSccalj6etynahSw
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:54:34.042712
---

# 网络安全行业，为什么会存在安全优先还是业务优先的矛盾

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/sF8ZCSicrH3WY2I3P76pz3jxy0iaPaFcqnj5viaDxImVWZSRHZ8cStYRfIJ5MAnNmZ4L5GIF0aLe2qRASpiabI7QUg/0?wx_fmt=jpeg)

# 网络安全行业，为什么会存在安全优先还是业务优先的矛盾

原创

JUN哥
JUN哥

君说安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/sF8ZCSicrH3WYWmfDLDTqrW5PNAwrdyF8hD8H2dtYcaejKFPHJicJaxoAv7NXpDDcoz3AIg3S187nIib9khvj34dg/640?wx_fmt=jpeg)

****分享网络安全资讯，提升网络安全认知！****

---

**“** 其实安全优先与业务优先的矛盾一直并未解决**”**

![](https://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3WTg2icZ0OXGsKcpFVPPxwSFDzRyfJMoGFTEMSAy987hwjb5GeQ3S7ueOSrtVtEa072XG2iayTc3asQ/640?wx_fmt=png&from=appmsg)

---

大家好，我是Jun哥。

昨天发了一篇数据安全相关的文章，写的有点杂，想到哪里就写哪里了，其中提到了安全与业务这个矛盾。

究竟是安全优先还是业务优先？刚好昨天圈子里看到一个帖子截图，拿出来跟大家分享和讨论下。

![](https://mmbiz.qpic.cn/mmbiz_jpg/sF8ZCSicrH3WY2I3P76pz3jxy0iaPaFcqnwCqleVoAjU4PENmYx77j5k5TKVL6rfx9g1RBLbBaQcnedIc8LSnTYg/640?wx_fmt=jpeg&from=appmsg)

|  |
| --- |
| 有个做互联网金融的朋友吐槽，他们公司新来了一个安全总监,年薪120万。    这哥们一来就搞“零信任”架构，把内网隔离得像监狱一样。    开发查个生产日志要走三级审批，数据库连SELECT权限都回收了,必须通过堡垒机敲命令,还不能复制粘贴.    结果就是查Bug的效率直线下降。    以前几分钟能定位的问题，现在要折腾半天申请权限。    有时候线上出故障，开发因为权限不够进不去服务器，只能干着急，眼睁睁看着损失扩大。    安全部门是免责了，锅全甩给了研发响应慢。    安全当然重要，但安全不能以牺牲业务连续性为代价。    过度的安全合规，往往是一种懒政。好的安全架构应该是在不打扰正常工作流的前提下做无感知的防护，而不是把所有的门都焊死，最后把业务也给憋死了。 |

这个案例充分说明了几个问题，大家可以认真思考下：

（1）安全优先还是业务优先？

（2）纸上谈兵还是生搬硬套？

（3）过度合规还是懒政行为？

对于这三个问题，我聊一聊自己的看法。

![图片](https://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3W4EHyUwzch09q3ZN66Ib4m1fR9eYqsIkzlzmotk53kic7VxM4dszLlNOoK8dpUkUIVkeHSk6K4Z5w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)  01 安全优先还是业务优先？

这个问题，其实对于不同的组织，其安全需求也是不一样的。对于数据敏感度较高的部门，对数据安全要求高的必然是安全优先；

但对于一般的组织，数据保密性没有那么高的，处于业务发展期的，应该还是以业务优先为主。

我个人的看法是，安全要搞到什么程度，如何有效进行网络安全管控，应该依据企业的实际状况来定制合适的网络安全策略，但等级保护和安全合规是底线。

我的历史经验告诉我，没有百分之百的安全，也没有一劳永逸的解决方案，组织的网络安全，一定是遵循戴明环原则的（即PDCA）不断完善。

因此，安全一定要结合业务的实际情况来制定，比如拓扑结构，业务的数据流，相关系统和产品的重要程度还制定实际的安全解决方案和安全策略的。

![图片](https://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3W4EHyUwzch09q3ZN66Ib4m1fR9eYqsIkzlzmotk53kic7VxM4dszLlNOoK8dpUkUIVkeHSk6K4Z5w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)  02 纸上谈兵还是生搬硬套？

纸上谈兵是夸夸其谈，实际上既解决不了业务问题，也解决不了安全问题；生搬硬套的做法更是离谱，每个人的过往经验都是幸存者偏差，抛开实际场景，不谈业务需求和安全需求，照搬照抄更是错的离谱。

安全行业有一句话非常重要，即安全是发展的前提，发展是安全的保障。这句话其实充分说明了安全和发展的辩证关系，他们相互依存，相互促进。

对于组织来讲，选择什么样的安全策略应当是结合企业实际的发展状况和安全需求来考量，而优秀的网络安全解决方案通常是能够做到这点的。

然而在现实中，尤其是现在职场比较恶劣的竞争环境下，拿来主义优先是一个现状，很多售前，销售其实都存在拿来即用的思想和实践的，因此引发部分项目的信任危机也好，交付失败也好，也都是类似的问题。

![图片](https://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3W4EHyUwzch09q3ZN66Ib4m1fR9eYqsIkzlzmotk53kic7VxM4dszLlNOoK8dpUkUIVkeHSk6K4Z5w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)  03 过度合规还是懒政行为？

其实没有所谓过度合规，等级保护的诸多测评项，判定标准当前规定下也只有三种，符合、不符合和不适用。

所以，Jun哥认为，其实这是安全懒政行为，是拿来主义下的安全懒政行为。

图片中的案例明显是生搬硬套和拿来主义，并没有结合企业的实际业务和当下的安全需求来做方案，这一定会导致各种问题出现。

网络安全的重要性不言而喻，但对于具体的安全策略，应当结合组织的业务现状来制定，不同的部门，人员的安全权限也应当有区别。

安全合规是底线，安全和业务之间应当要有平衡，对大部分组织来讲，安全应该是要给业务服务的，因为业务是生存线，发展好了才能更高的保障安全。

当然，这也不是说只要业务，不要安全，如何做好有效的安全，还是需要结合组织实际的现状来制定策略并且要遵循实际变化的原则，因此没有一劳永逸的安全解决方案。

把网络安全需求融入组织的业务流程，制定针对性的管控点和安全策略，或者优化业务流程才是有效的解决方案。

安全优先还是业务优先，对所有组织来讲其实一直都在，这个矛盾一直并未解决，也不可能完全解决，无论是以前还是未来都会存在。

---

全文完，喜欢**请三连**，这对我**很重要！**

---

**-End-**

****免责声明：****本文相关素材均来自互联网，仅为传递信息之用。****

****如有侵权，请联系作者删除。****

---

**★****点赞，转发，设为星标**★

**与你一起分享网络安全职场故事**

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3Wbibleujm785ib7tmND84FBJjMueVpPCeQ7mSYeh9ugVYsmv5LhX1qAAI9OicjlyuvGsBrr8BiaYnv4w/0?wx_fmt=png)

君说安全

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/sF8ZCSicrH3Wbibleujm785ib7tmND84FBJjMueVpPCeQ7mSYeh9ugVYsmv5LhX1qAAI9OicjlyuvGsBrr8BiaYnv4w/0?wx_fmt=png)

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