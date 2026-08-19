---
title: 理事动态丨达梦数据×湖北银行丨联合实验室：拆旧换新，大型模块化微服务重构对公信贷系统
url: https://mp.weixin.qq.com/s/k7b9gURcqNp4ujfkOHWMmA
source: Doonsec's feed
date: 2026-08-18
fetch_date: 2026-08-19T02:53:40.577806
---

# 理事动态丨达梦数据×湖北银行丨联合实验室：拆旧换新，大型模块化微服务重构对公信贷系统

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/qM42Jic4O616HTThRyVfDDrtV1OROfClukR0QVAfjiciabIriaBlqlrymeywVS7ox90TfuX4ZO8qFbibMglvjFw4053Szc1dd3UNicwdaWiaZfV1dg/0?wx_fmt=jpeg)

# 理事动态丨达梦数据×湖北银行丨联合实验室：拆旧换新，大型模块化微服务重构对公信贷系统

武汉网络安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![图片](https://mmbiz.qpic.cn/mmbiz_png/bL2iaicTYdZn6xia9ep49RicrT5OEnGGic4KZ4TaJucHxwTyU8G2DFHrKz3vgE69yKzy7kZy1HpGdzWns5ZibqCrbYFg/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=0)

**点击上方蓝字 关注武汉网络安全**

![图片](https://mmbiz.qpic.cn/mmbiz_png/bL2iaicTYdZn6xia9ep49RicrT5OEnGGic4KZWo09t2MA3L4rPHia34pbYeJ0f4Otp9qIMC9ghF6kj9we0orNMmibEiadQ/640?wx_fmt=png&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=1)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/qM42Jic4O617vGSn34UygcLqQgNUkDS7FjD0tsPMUjjqKxVNHGnIaXYrh9rsmicEULco9RqBeIfaNib02nxPWY1qDoWibkNyqLsTBVspC7Gice44/640?wx_fmt=gif&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=2)

2025年4月，达梦数据与湖北银行成立联合实验室，构建金融科技自主创新试验田。

在过去的一年里，联合实验室以湖北银行各类业务系统为原型，针对金融业多种代表性的业务场景探索不同的解决方案。对公信贷系统就是本次联合实验室系列解决方案的代表。

**为什么要换，三大核心问题**

作为承载企业授信、贷款发放、额度管理、押品登记等关键业务的系统，湖北银行对公信贷系统长期采用“大型单体应用+某国外数据库（小型机）”架构。随着业务的发展，这一架构逐渐暴露出三大核心问题：

**架构僵化**

系统功能模块多且复杂，调度关系耦合度极高，任何微小变更都可能牵一发而动全身，无法满足业务快速迭代的要求。

**技术依赖**

核心数据库依赖国外数据库，在技术自主的背景下，必须寻求替代方案。

**性能瓶颈**

系统部署于小型机，纵向扩展已达上限，无法满足业务增长的需要。

**解决方案

大型模块化微服务+企业级数据库**

为解决以上问题，联合实验室进行对公信贷系统改造。对公信贷系统具有“SQL复杂、并发较低、数据量较大且分布不均”的特点，要求数据库具备高HTAP能力，能够支持复杂SQL，且必须满足7×24小时不间断运行。

**为此，联合实验室采用了“大型模块化微服务+企业级数据库”方案。**

遵循“避免分布式事务、支持复杂事务”两大设计原则，将原单体应用拆分为6大能力中心：对公信贷、额度管理、押品管理、资产保全、统一门户、内联服务。每个能力中心配套独立的达梦数据守护集群（DMDataWatch），形成主备高可用架构。

微服务模块和数据库集群一一对应，模块间独立开发运维、互不干扰，消除单点故障和耦合风险。且方案充分调用达梦数据库的原生HTAP能力，一套架构内，交易处理与分析查询可同时运行。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ytG5W1XREibhXEE2JJDiavNubF75mfAEwkqqP0EDxppibQwU0EmGRGVfpykIu6eOOXcWgYl5pRkADxr3G6ExTJS4EDO09lZogYhIfRGXibOhwsc/640?wx_fmt=jpeg&from=appmsg#imgIndex=1)

**改造成效

性能、可用性、安全性三重验证**

✅ **性能表现**

复杂信贷业务SQL场景实测1000 TPS，并具备后续无缝升级为达梦数据共享集群DMDSC以支撑更高并发的能力。

✅ **高可用保障**

主备架构方案解除单点故障风险，保障业务7×24小时连续运行。

✅ **安全性与性价比**

摆脱国外技术依赖，实现安全自主，并以高兼容性优势极大节省开发资源。

**结 语**

达梦与湖北银行联合实验室对公信贷系统的升级改造，验证了一条可行的技术路径：以模块化微服务解耦业务复杂性，以达梦数据守护集群承接数据高可用与HTAP能力，在避免分布式事务的前提下实现弹性扩展。这一实践为金融行业对公信贷等关键业务系统的国产升级提供了可复用的参考范式。

***往期回顾***

[省科技厅关于2026年拟入库湖北省科创 “新物种”企业名单的公示](https://mp.weixin.qq.com/s?__biz=MzA3OTEyODAxMw==&mid=2247512645&idx=1&sn=5dc44a9d67dc5ed24d3294e7f3c894dd&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/lJWhyqdP0InESjialRqLe4YX1BgUibDDJPTjUE610fJOZ4pp3e7ciaUld2XDm60kUFVZ7U8k5FqL97MklicYsgZ9cg/640?wx_fmt=png&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=7)

[抗量子密码安全芯片在汉发布 安创会华中网络安全生态峰会顺利举办](https://mp.weixin.qq.com/s?__biz=MzA3OTEyODAxMw==&mid=2247512699&idx=1&sn=e2d748ff4b75108b1ab5dbe5c385e403&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_png/lJWhyqdP0Ik4PHkkM8joHyW0zVCrduFqELx420fspZeiao4p6B65MGsHzLibEqsLkxlRpeR9RHdN4Q4UVXJydodA/640?wx_fmt=png&from=appmsg)

[武汉发布全国首个“双安认定”网络安全团体标准](https://mp.weixin.qq.com/s?__biz=MzA3OTEyODAxMw==&mid=2247512668&idx=1&sn=2a7e1f64c5cd68074d7f0f9ceda4f7cc&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_png/qM42Jic4O617vCviaP7SiaRdPzHiaf9hsGCcLr7vuX2y3yHjvG1BeS4FaB3TqTlklqIrbiaLibT287J6b0BVc7jZ3DqwM5IoM7mJauLqAibhb1hWeU/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=9)

![](https://mmbiz.qpic.cn/mmbiz_png/qM42Jic4O617yedic9FDiaXYtAh6GvpyC5sJIpvMVCHhXUSJickW4DOOph3EVQnz5TGONI76s1scQjCme9icsjZ0k5TSNYHHaoupjUYUGB1Os7Bc/640?wx_fmt=png&from=appmsg)

预览时标签不可点

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/lJWhyqdP0Inib7gFln8HMiaedowUpdURAEPu6gLq67vIbDna2ZBCCxYG7MZoyfpUJMWJ0p5yCJic8Asxu4XdeicXcw/0?wx_fmt=png)

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