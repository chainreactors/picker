---
title: 同样的算力集群，为什么别人的利用率更高？
url: https://mp.weixin.qq.com/s/Oz5dY6FNWREdHoGIBTGBWw
source: Doonsec's feed
date: 2026-07-14
fetch_date: 2026-07-15T04:44:41.490709
---

# 同样的算力集群，为什么别人的利用率更高？

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/xd7XLzz7r16qaMHqBJFibr31DbERdybzmDUia2osdEScORSjm1E3iamy07YdLNGiabemKibx05UN4Tfkt5RgQNad8BG2wAoY9xxbImAb9GxrBpGY/0?wx_fmt=jpeg)

# 同样的算力集群，为什么别人的利用率更高？

原创

安博通
安博通

安博通

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

“豆包，帮我写份述职报告”“DeepSeek，优化一下简历”。如今，大模型正以前所未有的速度融入日常办公与生产场景。数据显示，国内某主流大模型的日均Token使用量已突破180万亿。从智能客服到代码生成，从工业仿真到科学计算，AI正在重塑千行百业的运行逻辑，算力需求随之呈指数级膨胀。

然而，当各方竞相追逐GPU算力、大模型参数与算力中心规模之时，一个深层问题逐渐浮出水面：**算力堆砌是否等同于训练效率与应用体验的提升？答案是否定的**。

![](https://mmbiz.qpic.cn/mmbiz_jpg/xd7XLzz7r14fK9he353LwHpdBTsOvVRQxdw9xJJPEdu1qtFar1sRA2xbvGIT1DAmkoOpAXHRk26HxJWgia0nDCp5kibbxqIzJia3rzoibQcduCI/640?wx_fmt=jpeg&from=appmsg)

**Gartner调研显示，企业AI集群平均GPU利用率仅为30%至45%；IDC数据则更为触目惊心：通用算力中心利用率低至10%至15%，部分智算中心GPU利用率甚至不足30%**。AI大模型训练动辄投入千万级成本，但大量异构算力资源，譬如不同品牌芯片、跨地域集群、纷繁网络协议之间彼此割裂，难以协同。算力饥渴与资源闲置同时存在，企业迫切需要一套能够盘活存量、打通边界的调度系统。

在此背景下，**安博通“星斗”异网异构算力编排调度平台**应运而生。作为面向异构算力与泛在网络的全域调度中枢，该平台致力于打破硬件边界、穿透网络孤岛，让算力与安全资源像水电一样按需流动。

![](https://mmbiz.qpic.cn/mmbiz_png/xd7XLzz7r16z8zyiahicbDMeoj7p0zJcepibAysEibDQ2fxT36z6XrODYT9ic7dtVvSibtFgZbvjVMoJXicpN0uicIkE7Dqmb9mUWnNFOVl6J7kNicJc/640?wx_fmt=png&from=appmsg)

**盘活算力，统一调度**

“星斗”平台聚焦算力资源的全生命周期管理，具备以下五大核心能力：

**广泛兼容，异构纳管：**全面支持CPU、GPU等多种算力形态，兼容国内外主流芯片及加速卡，实现国产算力与英伟达等资源的统一纳管。

**打破边界，无缝连接：**支持异构网络环境下设备与用户的快速接入与通信，实现跨运营商、跨地域的算力访问与调度。

**智能调度，动态分配：**通过策略引擎驱动算力任务在不同区域、不同集群间自动分配与负载均衡，显著提升资源整体利用率。

**简化运维，自动管控：**提供可视化运维界面与智能告警机制，大幅降低人工干预成本，保障算力池常态化稳定运行。

**场景覆盖，底座坚实：**适用于人工智能训练、大数据分析、科学计算、实时推理等多种高负载应用场景，为企业数字化业务提供坚实底座。

**某高校多源异构算力资源池项目**

**客户挑战：**某高校生物信息学院在进行科研项目时长期采用裸机直算模式，多个科研项目并行开展时资源无法共享；大量老旧算力设备分散使用，缺乏统一管理手段，运维难度居高不下；随着教学与科研需求的持续深化，现有基础资源环境已逐渐显现瓶颈，急需新增算力资源。

**解决方案：**在学校数据中心新增1台节点图形运算服务器（RTX A 6000），并建设校级算力公共平台，构建多源异构算力资源池，统一纳管A6000与老旧国产算力卡。平台依托vGPU资源池化能力，动态分配不同计算任务并实施任务优先级管理，有效提高算力资源利用率，同时保障核心业务的计算资源与服务稳定性。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xd7XLzz7r16Zrw5NYVt0ubQyPge4VgeOF7PKiaGYoibwoz0ibDic58fIBxLX1ibXC1ibFNzJbMes6eM6Dib2GnJbXjwrmzSAco5MlcuBolHzVET60U/640?wx_fmt=png&from=appmsg)

**实现效果：**异构算力整合后整体利用率提升30%。算力资源由传统物理形态转变为虚拟资源池后，调配更加灵活；学校信息管理员可为每个应用系统、每位平台用户灵活分配资源配额，并随时根据实际使用情况进行动态调整，资源利用效率大幅提升。同时，各学院分散管理算力资源的局面得到根本改善，管理成本显著下降；学研团队可多项目并行推进，科研效率有效提升。

![](https://mmbiz.qpic.cn/mmbiz_png/Ljib4So7yuWiaCWXBm2jAVTOUiaZuVXnIYIdDcK2rosdItu6xWNneESojthhVibw11IamGslVFPKEvvbblQVklFsOA/640?wx_fmt=png)

安博通算力产品方案已全面服务于**城市算力网以及工业、能源、交通、医疗等行业**算力网建设，赋能千行百业的数字化转型升级，打造智能高效、普惠便捷、绿色低碳、安全稳定的算力网络，持续夯实“数字中国”的算力底座。

**安博通**

**，AI时代安全算力生态构建者**

近期热门文章

[你好，我是15岁的安博通，这是我的最新简历](https://mp.weixin.qq.com/s?__biz=MzIyNTA5Mzc2OA==&mid=2651139377&idx=1&sn=1eafe2b2d2d98efcdd1311da5e512b5f&scene=21#wechat_redirect)

[国安发文警示弹窗风险！安博通下一代AI防火墙实现立体防御](https://mp.weixin.qq.com/s?__biz=MzIyNTA5Mzc2OA==&mid=2651139348&idx=1&sn=88012886709b8617d31a8470b2faf00f&scene=21#wechat_redirect)

[网安“世界杯”8强登场！](https://mp.weixin.qq.com/s?__biz=MzIyNTA5Mzc2OA==&mid=2651139404&idx=1&sn=0530a16e172d37f268c5a591e44295b5&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_gif/cZkI8M0nbCnqFdBSZTPngyO5KHUZhk4AED9YficV2s0zic3EHmqH0icpiczkrKGdQKiaUciaiaDIP4R4gG6wdV3HoSRkw/640?wx_fmt=gif#imgIndex=17)

点击**阅读原文**，了解安博通

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/xd7XLzz7r14HALxbxiaFqaBHIbuVtdJB3vMZajv1YSc7r7rLEEa8V6OqykpYlicEial5kyiaQ0ceKPzhPZRSoagKR3NqZZRDfQfTvIMGnyvdY5s/0?wx_fmt=png)

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