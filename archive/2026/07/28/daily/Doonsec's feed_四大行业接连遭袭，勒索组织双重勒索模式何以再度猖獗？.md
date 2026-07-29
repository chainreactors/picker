---
title: 四大行业接连遭袭，勒索组织双重勒索模式何以再度猖獗？
url: https://mp.weixin.qq.com/s/rjHiUDxzUiJy-JR8V4G41Q
source: Doonsec's feed
date: 2026-07-28
fetch_date: 2026-07-29T04:58:52.947538
---

# 四大行业接连遭袭，勒索组织双重勒索模式何以再度猖獗？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcdtEkOgTRMz6KdcHToZlaNTEianQXnlrOYcC5ts6oJicA3klCxXBmjMMokI6ugoMsKWYPaNe1xOdYgwylmD2Tiax1tDLWYjPjOias/0?wx_fmt=jpeg)

# 四大行业接连遭袭，勒索组织双重勒索模式何以再度猖獗？

走狗是狗哥
走狗是狗哥

安在

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_gif/5eH7xATwT3icpLmjpDSQkXx16oAygiaJncke0vYYJvIkuzECibrQJcUW4oAedTuib1G9m372rleJRDNXNs54fBEVicg/640?wx_fmt=gif&wxfrom=5&wx_lazy=1&tp=webp)

近期，以Qilin、INC\_RANSOM为代表的多个勒索组织持续在全球范围内发起攻击，医疗、制造、汽车、地产等行业机构接连成为目标。

攻击者普遍采用“数据窃取+系统加密”的双重勒索模式，将企业内部经营数据、客户个人信息作为核心要挟筹码，给众多机构的业务运转与数据安全带来严峻挑战。

这一轮攻击高发并非偶然，而是勒索黑产生态持续演化的结果。

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpe2ry4KettQcOOJEt0nK3W0QsibEyv6icyKAUgk9jA7qG7hQZv4cePicxZv7uoJwvonLtFCareABwQWiaQUdC64UMWxdwYmLVeHFQo/640?wx_fmt=png&from=appmsg)

过去几年，勒索软件即服务模式彻底降低了攻击门槛，开发者提供成熟的加密工具与谈判体系，下游攻击者只需租用服务即可发起行动。

随着LockBit等老牌头部团伙相继被执法部门打击，大量技术人员与附属团伙流向INC、Qilin等新兴平台，直接推高了后者的攻击频次与覆盖范围。

截至目前，INC组织公开宣称的受害机构已超过八百家，Qilin也保持着几乎每日新增受害者的攻击节奏，两者均跻身当前全球最活跃的勒索团伙行列。

在攻击手法上，双重勒索早已取代单纯加密成为行业标配。

随着企业数据备份意识的普及，仅靠加密系统已很难迫使受害者支付赎金。

而数据泄露带来的合规处罚、客户信任损失与商业机密风险，往往比业务停摆更具压迫力。

因此攻击者普遍会在加密前先批量窃取敏感数据，若企业拒绝支付赎金，便在暗网泄密站点分批公开数据，形成二次施压。

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfibOia9tfhNJFAcL8F8v9M2ml4letZbDJzicTbbtTPazHKboNdH0IIWvGsxgWwgV8KLqMfciasTpPZEWxGjdMfb4qcMGnCQIDse7s/640?wx_fmt=png&from=appmsg)

具体到入侵路径，Qilin团伙近期频繁利用PaloAltoVPN的身份认证绕过漏洞，在补丁发布后短短数天内就完成武器化并投入实战；

INC团伙则更倾向于通过钓鱼邮件、窃取的远程凭证进入内网，再通过组策略批量投放加密程序，同时专门针对Veeam等备份系统发起破坏，切断企业的恢复路径。

医疗、制造、汽车、地产之所以成为集中打击的目标，背后有着清晰的利益逻辑。

医疗机构掌握大量患者隐私数据，且诊疗业务不能长时间中断，面对勒索时妥协意愿最强；

制造业生产线高度依赖数字化系统，数小时停产就可能造成百万级损失，议价空间极小；

汽车行业供应链条长，核心零部件厂商一旦中招会波及整车生产；

地产行业则沉淀了海量业主个人信息与商业运营数据，泄露后的声誉与合规代价高昂。

这些行业共同的特点是数据价值高、业务连续性要求强，恰好契合勒索团伙的施压逻辑。

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfZF3UwkQ4XRkcarK9k6RoSqL5OvtVSrjm6PXwxicNXdgSOLndyEHJWDv0dQIBr5NCDZQA7IoZTPI8X5LoJpEvQE8mjUf3l4jog/640?wx_fmt=png&from=appmsg)

从行业视角看，这波攻击潮也释放出明确的警示信号。

首先，企业的防御思路必须从“防加密、靠备份”向“防入侵、控数据”升级，因为备份只能解决业务恢复问题，无法抵挡数据泄露带来的连锁风险。

其次，数据安全正在成为勒索防护的核心战场，对核心数据的分类分级、访问权限管控、外发流量监测，其重要性已经不亚于终端杀毒与边界防火墙。

最后，勒索攻击的常态化意味着单一技术产品无法形成有效防护，企业需要建立从边界入侵检测、内部横向防护到数据泄露监测的完整体系，同时配套应急响应预案与合规处置流程，才能在攻击发生时将损失降到最低。

**安在企业（用户）会员服务**

**助力全生命周期安全意识提升**

“安在企业（用户）会员服务”，为所有企业提供一站式的网络安全支援服务，包括意识宣传、培训教育、效果检验、专业圈子、知识社区、专业培训、参选评奖等多个板块，助力网安从业者高效履职，实现个人与企业安全能力同步升级。

**[小投入大防护！安在推出企业（用户）会员服务](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)，点击标题阅读详情。**

深度贴合企业不同规模、安全水平投入以及员工安全意识的不同发展阶段，特设5级安全意识培训服务体系，为企业用户量身匹配适配的安全意识解决方案。

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpfxauQUKv5E2gfFrpMBAz1Um7FAY4ontydFQQ1ZKtH1AnXs3kfYxtOYX55xrRBM2pFYicz2sqACyjd4u1CO2iaAFCYLIbgMGS58M/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpevFQuuGbgqzRQXxpZt2NQG9gkeSfhrKIBL6NVagjD9IYhtko4pjEdkrmiaAFfGAYPQN06Cs2MSLG4HGqExqL1OJ9n0ZSmibwO9Q/640?wx_fmt=jpeg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

本文展示所有类型素材，均包含在企业（用户）会员服务中，如有意向，欢迎垂询。

**加入诸子云知识星球**

获取更多“安全意识资料”和“网络安全报告”

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8C1NLS8ickpevtB5U1iad3jHVWSBznd4wGSnt15KjDpDvdDAzWfLewNRoKHVyCNTCEIVkuJAZOyUvKSibQZJfe43xQsofxEKuB4xuj2gzBG4EM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/8C1NLS8ickpfphwUVRfsnQ4tHXQicImFKOyric81wyOR6UtibaU9W2nPpF2bIflBltg8S0vJMmYEDrEkWN30lpxicg5YUyLDu0fAlCgX3ibJBX8Ys/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcHLAPdhJaKhut2fLyfnDD0ofblclhTxwQtdjZ9Wnsgw7qtANaolbmpYLhf9mCW9ib2vDial19qZnEibibEZkAcOVPZVTA9QsD5EeY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpcaBf7luDbkibnkcG6SFanyicuIePMSYCXyZ4dpRTDOuRkj4IwafHmia3a61q1QmasWkERH6vhD4eicgePFZCERRib6zAefEHxWz3cY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcoibvzpu3KUfibMYf9yTU7VWPXP10LBBkle2fQKqqdVk7zLYiaoh0bHWxmovw4aqY0icMXYfqY2TW0LibL3W2NVG5u6ibA9aDyzsF8I/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpfHuRbxczmKK36HLRfSVxysIgBAQMVFSdVGCDascdwN2jmE6LickWQ9nyK1k0fVcibLIYwaseCvT2VtXEoVubWyMLdmf9jRo59JY/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8C1NLS8ickpd5O3toB6xb2AkuS2RcTBYTLu0nY8LibtS5iaZCyjdwbYYvsFA52ib67sdZdjG5Irwcs962K5KttO7qbKW4eEBYNtKkJUKBfHGI0s/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpd8PSnWIlP6x8ytDuhBpQc307z6BWzOD6flZLjlIYYXXU1NKpN5gXPjeq2mAPqgJm6Bd82h2IOL1rNSU0REl8Z7LOmpoU1NjS4/640?wx_fmt=jpeg&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_jpg/8C1NLS8ickpcGyRCee3d61E6ibYFh5VeHPicnicIloE3Iia6Bvud9Ok8cJOYYu0s4aIIXNltmfiagic87u2yvKdIDY6Px4iaaFwOh1h0B17rs0nibSlo/640?wx_fmt=jpeg&from=appmsg)

**<**

**滑动查看下一张图片**

**>**

****END**

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AAfIzicyojXwPTCxD0QGZHhyRcRicJAHhUv382sYFibICoxjzktlJwEEPag/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT3ibILU2vpTY8kPMvg2uyDyibiaFibHCDibF1vCIjn2tNAKdNicq3Y45vuYuWNUDICSF8dZ206dy1Kzrehug/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=3)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247651222&idx=1&sn=0674c7e57249a57240b5ed0fcd6cdcf2&scene=21#wechat_redirect)

[![图片](https://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT38j3Ndib8YhjyiaBQhdzUe1AApXU9ib7vkMD4KMHhjVfkTqOCUrDibUaBDoH0OGGCMasLLJyv5xppK6rA/640?wx_fmt=png&wxfrom=5&wx_lazy=1&tp=webp)](https://mp.weixin.qq.com/s?__biz=MzU5ODgzNTExOQ==&mid=2247652102&idx=1&sn=8af8808f9055f99fa71020922d80058c&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/5eH7xATwT38HPkvxLkOy5rLCeVBtj8H9SUbVPNZbibc4N2knPCDFjTKduRLhiaAZVQShUa2IZqsBShI2GG2dpqBg/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&tp=webp)

点击这里阅读原文**

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/5eH7xATwT39OIA4MxWIQmVzjc3H2rbMa0sv6no7gMEXOV63OW7hvwk4EDjOaurIkrnPOjBpCmIN00ELKRf16qg/0?wx_fmt=png)

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