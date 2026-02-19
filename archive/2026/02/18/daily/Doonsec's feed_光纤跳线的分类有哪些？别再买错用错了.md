---
title: 光纤跳线的分类有哪些？别再买错用错了
url: https://mp.weixin.qq.com/s/mzdTgMEQk-qXVHmiSzsZQA
source: Doonsec's feed
date: 2026-02-18
fetch_date: 2026-02-19T04:19:45.641172
---

# 光纤跳线的分类有哪些？别再买错用错了

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Dibzmm9niba06Jm9ibQdXfCTAerIGvaP0KKrL7jVfo5q6JWe5icU38NsHltELqYeMBKcCII5ncdd4R0meRdrr0aoOIgicIIXcjicPsWWKnGC2ZB7E/0?wx_fmt=jpeg)

# 光纤跳线的分类有哪些？别再买错用错了

原创

wljslmz瑞哥
wljslmz瑞哥

网络技术联盟站

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_gif/6OibpDQ66VYQNIyABHZrCWcZT6asQr23iaO5wvXibL4CtruQ1E2AY6iaaH3X4LxMnSrBXvjhQND7Y4ibRahz9FhPVBw/640?wx_fmt=gif)

> 公众号：网络技术联盟站

最近有同事问我：“跳线不就一根线两头插头吗？怎么这么多类型？”哈哈，这问题问得好！光纤跳线看着简单，分类门道多着呢，用错了轻则衰减大信号弱，重则链路不通烧模块。

今天就系统聊聊**光纤跳线的分类**。主要从三个维度：光纤类型（ITU-T G系列）、连接器类型、芯数分类。还会提到抛光方式等实用点。

## 先说说光纤跳线到底是个啥？

光纤跳线（Fiber Patch Cord/Jumper），就是两端带连接器的短光缆，用于设备间快速连接。比起熔接永久链路，它灵活、可插拔，是机房最常见的“耗材”。

常见长度1-50米，颜色区分单模（黄/蓝/绿）和多模（橙/水绿）。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba05MvTt54qat9U2cuu0hzY6C1BnXibhqibJlvh7cYHamAoAvG9fvjX4JYqSMySGXa7UAwNMp4SXxeibxia0AJ6JFu5SnfMKFoJ9szvw/640?wx_fmt=png&from=appmsg)

## 第一大类：按光纤类型分（ITU-T G系列标准）

这是最核心的分类，直接决定传输距离、速率、应用场景。ITU-T定义了G.651到G.657等标准。

### 1. 多模光纤跳线（主用G.651）

芯径50/125μm，波长850/1310nm。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba06GCI6OawGEO4X3vic5yGPcF6JpLiafh7Nialv7kkKf6QR8YqXH1jJpa5zRweaFfnNrCMJdLLhiamvlCNX4rXpNZgEYKQc3FSB0uhY/640?wx_fmt=png&from=appmsg)

**特点**：光在纤芯多模式传播，距离短（一般300-500米），但成本低、对接宽容。

**应用**：机房内部、数据中心短距互联、10G/40G/100G多模场景（OM3/OM4/OM5）。

**优缺点**：便宜、易施工，但距离远了色散大。现在400G以上基本淘汰多模。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba04bNwqAonic284Q4y0uajYK7EQRksxCtItMS6PLvsVd5T0NTyLbNvu8RviciagzUFSbBmcJNXooFsXziarv98g7ZQLV4u4q5TpZVKA/640?wx_fmt=png&from=appmsg)

我早期机房全是多模橙色跳线，便宜量大，但后来升级万兆就全换单模了。

### 2. 单模光纤跳线（最常用，G.652系列）

芯径9/125μm，波长1310/1550nm。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba05HaIQhFKIzfCTl8bYsIQv4XhHE9Ticqw7QsiawH3AM6fpPb6BXCzT5MfcCiaib6tj30e1Ov35rEEic26k1zqJC4UI9fpVpWiaDUTz7U/640?wx_fmt=png&from=appmsg)

**G.652**：标准单模（STD SMF），最广泛使用。零色散点在1310nm，低衰减。

**子类**：G.652D低水峰，兼容CWDM/DWDM。

**应用**：城域网、长途骨干、接入网、数据中心长距。几乎所有室外和长距都是它。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba04LxBo52xZBjekibuBTVV2z1pOUDBadoztHKgQuraWrbnh3feOjJjNk5RtU0w0j4numgKhVIfN1LSSupqhDviaAXVs0FviccbemFM/640?wx_fmt=png&from=appmsg)

**G.653**：色散位移（DSF），零色散移到1550nm，适合超长距单波传输。但不支持DWDM（四波混频），现在基本淘汰。

**G.654**：截止波长位移，低衰减（1550nm仅0.2dB/km），用于海缆超长距无中继。但贵，不支持DWDM。

**G.655**：非零色散位移（NZDSF），小非零色散，抑制非线性，支持DWDM长距骨干/海缆。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba06QPLIWUiaoWaf0ZWiaeG2KLKZrHbgZqJGUCC2ADdSwE1AkJRIdOZ6KjCiclQiadm42hsBGicuANwHSEZ76F9xhoTugfnW6NmC5Lb6M/640?wx_fmt=png&from=appmsg)

**G.656**：低斜率非零色散，确保宽波段DWDM传输，进一步扩展波长范围。

**G.657**：弯曲不敏感单模，神器！弯曲半径可小到7.5mm甚至5mm而不增加衰减。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba07rl8CBiaDWdrGzE4G37bahrlvSCUDnrwwP1bcHbDE9z4I1wyhic3rEGGprKicGwYXkNXVFNFDC7hKhgSSvxydukPQbl6QdFGJFdY/640?wx_fmt=png&from=appmsg)

**子类**：G.657A1（弯径15mm）、A2（7.5mm）、B3（5mm）。

**应用**：FTTH入户、室内布线，拐弯多不怕断或衰减大。

我现在FTTH项目全用G.657A2，家里布线再也不用小心翼翼绕大弯了。

单模 vs 多模核心区别总结表：

| 类型 | 芯径 | 波长 | 距离 | 成本 | 应用场景 |
| --- | --- | --- | --- | --- | --- |
| 多模 | 50/62.5μm | 850/1310nm | <2km | 低 | 机房短距 |
| 单模G.652 | 9μm | 1310/1550nm | >10km | 中 | 城域/长途/接入 |
| 单模G.657 | 9μm | 1310/1550nm | >10km | 中高 | FTTH/室内弯曲场景 |

## 第二大类：按连接器类型分

跳线两端头决定兼容性，常见有这些：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba078npEBqSh2LHV94836HiaWNrXAGfpzYuvIMWT5rsricnoJCSXc376sCmx5pc3ak2vcwhEvdTd9jJvTCVlKHzlgKHzTo2aUBYgjM/640?wx_fmt=png&from=appmsg)

* **FC**：螺纹锁紧，圆形金属头，老设备多（光模块、老交换机）。衰减低但插拔麻烦。
* **SC**：卡扣方形，推拉式，最常见早期标准。机房配线架多用。
* **LC**：小方形，密度高（SC一半大小），现在数据中心王者。SFP/SFP+模块标配。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba07JSx7nMJYSxAu2BA9lAodYcgdb42OWxUKb0rAjMLicNtVD5QnFWibvfepPVDGXmU1d1kal626xnYIZCtttMsTXhYBC3kNA86rK0/640?wx_fmt=png&from=appmsg)

* **ST**：卡口圆形，老式，基本淘汰。
* **MTRJ**：小型双芯，老式少见。
* **MPO/MTP**：多芯（8/12/24/48芯），高密度并行光互联神器。40G/100G/400G必备。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba06Tv7qjiciaO5icq5rYXNI37SicfChNKwcoEC9ic1JxCQkhicNw5nXKWfrOolWPY72f5ibtEaHRVqA5ZCRt4OvmX1fb1o2adSeMspfUlw/640?wx_fmt=png&from=appmsg)

MPO现在火爆，12芯OM4支持100G，省空间省成本。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba05trHSlPickGOxXFkicdPyicX8Q3bMM9Naywl3oh92KHP3449tiadu8rK2ncvOjlf98zX3O80HRYqFibOwicOl8jM7njgGhpaibducm1Q/640?wx_fmt=png&from=appmsg)

另外抛光方式：UPC（蓝头，衰减<0.3dB）、APC（绿头8度角，衰减<0.2dB，回波损耗更好），后者用于对反射敏感的场景（如CATV）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba07iaG2EOHyuAGlhWG8lSeJxumk3x0W5vNyIlPxaceBrKiaV1DANXh92XrwBnjgSHThX85mtg5iahJlr9xJmiaxc0xJaVfHic8HvLexE/640?wx_fmt=png&from=appmsg)

## 第三大类：按芯数分

* **单芯（Simplex）**：一根纤，只单向传。少见。
* **双芯（Duplex）**：两根纤，双向传。最常见，LC/SC双工跳线。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/Dibzmm9niba05nzSJMplcSh0NPmicVt9WRqPGict7ovyZCkp6OWSt1hJsPcficRkE9vPaicJDsT1lOXc0ibX8EY4uG4efFsUgrVxhAGgnwKQic0MkVM/640?wx_fmt=png&from=appmsg)

* **多芯（Ribbon/MPO）**：8/12/16/24芯并行，主要MPO头。用于高密度数据中心。

![](https://mmbiz.qpic.cn/mmbiz_png/Dibzmm9niba05Bp3zdqx0McHqSoO5KwxdgoFLicOkR8rnuyFt3xeRp0KNicOTtPWcVu9ERANldx4nMNu3xBsID4oja4vaf8tLMnj4icJj4icNnvvs/640?wx_fmt=png&from=appmsg)

我参与一个400G数据中心项目，全是24芯MPO，机柜背面干净太多。

光纤跳线分类清楚了，采购和布线就不慌。机房整齐、链路稳定，全靠选对跳线。

你们项目常用哪种跳线？遇到过什么奇葩问题？

**喜欢就****分享**

**认同就****点赞**

**支持就****在看**

**一键四连，你的技术也四连**

![](https://mmbiz.qpic.cn/mmbiz_gif/6OibpDQ66VYRJ20XxicqZhK1qicQFqicZN3BDMEIvovHPnsWicnRgkibCNOtcZf7icVkErP0b18JZia29GVKLkhR5IJ1ibQ/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

网络技术联盟站

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6OibpDQ66VYQdKtmFWjIKQdYm1shR9hptHpKR1MvcbyFLHAW2Yh1Gc3ERB1TmfBEcicdvrud4Dmf4yR2Brd0VTfA/0?wx_fmt=png)

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