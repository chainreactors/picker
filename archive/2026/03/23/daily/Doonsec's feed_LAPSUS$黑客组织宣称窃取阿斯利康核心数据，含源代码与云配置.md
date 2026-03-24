---
title: LAPSUS$黑客组织宣称窃取阿斯利康核心数据，含源代码与云配置
url: https://mp.weixin.qq.com/s/v2cjLdWYJrFeE5o0fN9iPw
source: Doonsec's feed
date: 2026-03-23
fetch_date: 2026-03-24T04:15:22.534887
---

# LAPSUS$黑客组织宣称窃取阿斯利康核心数据，含源代码与云配置

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX11UdNuGGMHicibK7KqYnXiaKocctDxV8Djbr48sugkOEF9Wsxk1RnA49vJB1o1S5A3ZmicicpaeV3Y1n3QX89MkSk8lOav3A75aWicw/0?wx_fmt=jpeg)

# LAPSUS$黑客组织宣称窃取阿斯利康核心数据，含源代码与云配置

FreeBuf

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1LlWYiaQl73EqROBkiczE2cyzNlT46POic55xuFNJdvibSttCDZ11mh6xTmzpLntwsFasibUsYyx6rMuGDvGgB2DjTDh3icotXw3qKY/640?wx_fmt=png&from=appmsg)

##

臭名昭著的黑客组织 LAPSUS$ 近日再度现身，宣称对跨国制药与生物技术公司阿斯利康（AstraZeneca）的重大数据泄露事件负责。目前，该威胁组织正试图出售一个 3GB 的压缩内部数据包，此举可能标志着其勒索手段正向"付费访问"模式转变。

此前因针对多家大型科技公司实施高调攻击而闻名的 LAPSUS$，此次似乎通过入侵阿斯利康内部系统重新活跃。该组织已在非法论坛发布窃取数据的片段，详细说明了 .tar.gz 压缩包内容，并提供了截图作为证据。

##

**Part01**

## ****数据泄露详情****

威胁行为者正试图通过安全通讯应用 Session 吸引潜在买家联系他们进行交易谈判。目前尚未有完整数据被免费公开泄露，这表明该组织此次主要动机是通过直接出售数据获利，而非立即进行公开勒索。攻击者还提供了包含经过编辑的机密信息的密码保护粘贴链接，作为向潜在买家证明其访问权限的进一步证据。截至 2026 年 3 月 20 日，阿斯利康尚未就该事件发表评论，也未发布任何官方声明。

根据威胁行为者在入侵论坛上的声明，3GB 的数据包包含大量高度敏感的知识产权和基础设施配置信息：

![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX2sqAMye49XxCibbWiadmbdSp2MndITFLW9BT6PBUtwnm6BjROiaibp6uaR9o9iaftoDAKibiawZ2rQ7S4WsuhfQDtaDTXMOh1ibeKPkp8/640?wx_fmt=png&from=appmsg)

**Part02**

## ****泄露数据影响范围****

为证实其主张，攻击者已公开部分样本，披露了特定的内部仓库结构和项目细节。暴露的目录树显示存在名为 AZU\_EXFIL 的根文件夹，其中包含一个被标识为 als-sc-portal-internal 的关键供应链门户仓库。

该内部门户似乎管理着药品分销相关的多项核心物流功能，包括：

* 需求预测系统
* 库存追踪系统
* 产品主数据管理系统
* SAP 系统集成接口
* 准时足量（OTIF）交付指标系统

这些被泄露的细节表明，如果此次入侵属实，可能会对阿斯利康的内部供应链运营和整体云基础设施安全产生深远影响。

**参考来源：**

AstraZeneca Data Breach – LAPSUS$ Group Allegedly Claims Access to Internal Data

https://cybersecuritynews.com/astrazeneca-data-breach/

---

###

###

###

**推荐阅读**

[![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3cSYwf9JzGtDoYs4CGx2ljpXcZ5TfjHRz5qAcyWh8toRsxBf4Ws4INjebjWXk6Qtea2QViaicbkU4heohT9o1D194ib91F38VGUY/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NjA0NjgyMA==&mid=2651335912&idx=1&sn=f7c9c36f910a122eb9bb727adcf9e89d&scene=21#wechat_redirect)

### **电报讨论**![](https://mmbiz.qpic.cn/mmbiz_png/icBE3OpK1IX3hCYIDd7a8icmhzic2aMTw0bics6BfDdhRCQCsKTwXSAB6wXtEwI4OK9jdlFfFFNQJa4JUiapxxu56BjXl4gx3LEXYU1GMRkpiawgA/640?wx_fmt=png&from=appmsg)

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