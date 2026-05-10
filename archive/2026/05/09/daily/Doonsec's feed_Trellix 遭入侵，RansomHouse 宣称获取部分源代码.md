---
title: Trellix 遭入侵，RansomHouse 宣称获取部分源代码
url: https://mp.weixin.qq.com/s/M6gL6RvBPOH5lDkSzf-R6w
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:30:17.250347
---

# Trellix 遭入侵，RansomHouse 宣称获取部分源代码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/icBE3OpK1IX0t3Ep4rLUw87BwJYT0SrHHnVnrZVBtjmtYWJvRv4yqsJEfzmYiadic2cWSchWaOFRGO9QzsibkbFzXtGzDwZqrynS01xa5uH8cvw/0?wx_fmt=jpeg)

# Trellix 遭入侵，RansomHouse 宣称获取部分源代码

FreeBuf

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/qq5rfBadR38jUokdlWSNlAjmEsO1rzv3srXShFRuTKBGDwkj4gvYy34iajd6zQiaKl77Wsy9mjC0xBCRg0YgDIWg/640?wx_fmt=gif)

## ![](https://mmbiz.qpic.cn/sz_mmbiz_png/icBE3OpK1IX1k9BnoDnbEeopczS3Cpvn3N4dvhiajh1MNX1bm4IE9yibG4v2XMJvvuCJcEgLvrV1oC2IibYmwqZpSHLsz5iadsjvujaaaUdhxpUk/640?wx_fmt=png&from=appmsg)

##

由 McAfee Enterprise 与 FireEye 合并组建的全球网络安全公司 Trellix 确认其部分源代码仓库遭遇未授权访问，勒索组织 RansomHouse 已正式宣称对此次攻击负责。

**Part01**

## ****事件时间线****

Trellix 于 2026 年 5 月 2 日左右公开披露了这起涉及源代码仓库的数据泄露事件。根据调查，入侵实际发生于 2026 年 4 月 17 日。发现入侵后，Trellix 立即聘请顶级取证专家展开调查，并向执法部门通报了相关情况。

![](https://mmbiz.qpic.cn/mmbiz_jpg/icBE3OpK1IX2p1f5vCjeY9S0cJknLes8WuR8vU9aNuRnaxZ3ibuvB0e7H864TMHF5FH66j2wf36D8fIiaEXIltZOxO3c3uAIVhI798djm3G0yg/640?wx_fmt=jpeg&from=appmsg)

**Part02**

**攻击者特征**

RansomHouse 在其暗网泄露网站上公开了据称能证明访问 Trellix 内部服务和管理控制台的多张截图，但未说明外泄数据的具体数量和性质。值得注意的是，该组织将入侵状态标记为"证据取决于您"，这是其惯用的施压手段——在公开泄露数据前迫使受害者进行谈判。

该组织作为成熟的勒索软件即服务（RaaS）运营方，以部署独特的 Mario ESXi 勒索软件变种而闻名。其代码与泄露的 Babuk 勒索软件源代码存在关联，并配备名为 MrAgent 的工具，可同时攻击 Windows 和 Linux 虚拟化环境。RansomHouse 通常瞄准 VMware ESXi 基础设施，利用薄弱的域凭证和监控系统获取特权访问权限。

**Part03**

## ****事件影响评估****

Trellix 在官网声明中强调："截至目前调查显示，没有证据表明我们的源代码发布或分发流程受到影响，也未发现源代码被利用的情况。"初步调查显示，软件分发渠道和客户终端产品均未遭篡改。但数据泄露的完整范围尚未明确，Trellix 也未确认除源代码外是否涉及企业或客户数据。

此次事件凸显了勒索组织将网络安全厂商作为攻击目标的新趋势。这些企业持有的专有源代码若被武器化，可能对全球企业防御体系造成深远影响。RansomHouse 的独特之处在于其自诩为"专业调解社区"，通常以删除数据而非解密数据作为勒索条件。

**参考来源：**

Trellix Breach – RansomHouse Claims Access to Parts of Source Code

https://cybersecuritynews.com/trellix-breach/

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