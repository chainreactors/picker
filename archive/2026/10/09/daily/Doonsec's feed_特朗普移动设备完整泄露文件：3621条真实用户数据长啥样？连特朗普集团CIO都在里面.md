---
title: 特朗普移动设备完整泄露文件：3621条真实用户数据长啥样？连特朗普集团CIO都在里面
url: https://mp.weixin.qq.com/s/U-eNAOcJHw-PNWHJcCs4LA
source: Doonsec's feed
date: 2026-10-09
fetch_date: 2026-10-10T07:55:57.968972
---

# 特朗普移动设备完整泄露文件：3621条真实用户数据长啥样？连特朗普集团CIO都在里面

# 特朗普移动设备完整泄露文件：3621条真实用户数据长啥样？连特朗普集团CIO都在里面

原创

暗网哨兵
暗网哨兵

暗网哨兵

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

2026年10月初，特朗普家族授权运营的移动通信品牌 Trump Mobile 遭遇数据泄露。黑客组织 BYOD 在暗网公开了包含姓名、邮箱、电话、住址、订单详情等完整信息的客户档案。媒体核实后确认数据真实，受影响人数约3600余人，其中还包括特朗普集团副总裁兼首席信息官。

### 一、事件分析

**1. 一个自称 BYOD 的新兴勒索/数据勒索组织，在其暗网泄露网站（发布文件，声称已窃取 Trump Mobile 的客户数据，并公布了完整档案。**

黑客在文件开头声称：他们事先通知了 Trump Mobile，对方回复“We have no team to handle this”（我们没有团队处理这件事），并称入侵者是“恐怖分子”。黑客随后直接公开了数据。

黑客平台上的日期是2026 年 9 月 29 日，但这是平台记录的攻击时间，并不代表黑客当天就公开披露了事件。

![](https://mmbiz.qpic.cn/mmbiz_png/iaNqLNrWSicIrRUicnd7QRlRSQh6IU2JgP6Wyw00fApb6Q4nF2yaeCpznQs8thsN7cQibnVtgqianDEjAR5K60c0cIjVXg0PGhNeSWQHVbt1eKXs/640?wx_fmt=png&from=appmsg)

**2. 美国媒体 Straight Arrow News（记者 Mikael Thalen）于2026年10月05日最早报道此事。记者下载了数据，并直接联系文件中的部分用户进行核实。多名用户确认信息准确，包括订单取消记录、预购押金等细节。记者还与黑客通过加密通讯软件 Session 进行了对话，黑客提供了后台仪表盘截图等证据。**

**3. 入侵路径（黑客自述 + 媒体记录）**

BYOD 向媒体表示：

* 他们通过远程访问木马（RAT）感染了佛罗里达州 Liberty Mobile 一名员工的电脑。
* Liberty Mobile 是为 Trump Mobile 提供网络支持的 MVNO（虚拟移动网络运营商）。
* 获得初始权限后，进一步转向相关子域名，提取了客户数据。
* 黑客称当时使用该 MVNO 服务的用户总量就是约3615人，因此只窃取了这些记录（与预购手机订单数量不同）。

**4. 受影响范围**

黑客宣称 3615 条记录。实际流出文件约有 3621 条有效数据行，与宣称数字高度接近。

### 二、泄露文件详细分析

下面对已流出的 CSV 文件进行了结构化解析。

**文件基本结构：**

字段包括：

* CustomerNumber（客户编号）
* FirstName / LastName（姓名）
* Email（电子邮箱）
* ContactPhone（联系电话）
* Address / City / State / Zip（完整住址）
* Order\_DateCreated（订单创建时间）
* Order\_OrderId、Order\_Status、Order\_Total（订单ID、状态、金额）
* Order\_Lotnum、Order\_ProductID、Order\_Mdn、Order\_ESIM、Order\_QRCode（产品与eSIM相关信息）
* Line\_Mdn、Line\_PhoneStatus、Line\_PlanName、Line\_CustServiceId、Line\_ICCID、Line\_ActivationDate、Line\_PUK（线路与激活相关信息）

**数据规模与分布统计（基于文件实际内容）：**

* 有效数据行约 **3621 条**。
* 订单状态大致分布：

+ Payment Processed（已支付处理）：约 2447 条
+ New（新建）：约 470 条
+ Cancelled（已取消）：约 402 条
+ Provision（开通中）：约 143 条
+ 其他或空值：约 159 条

* 套餐情况：

+ 明确标记为 “30 Day Unlimited Talk Text Data”（30天无限通话+短信+流量）的记录约 1031 条。
+ 大量记录套餐字段为空（多为仅预购手机、未完成服务开通的用户）。

* 地理分布（州/地区前几名，文件中大小写混杂）：

+ 加利福尼亚（CA/Ca）最多
+ 佛罗里达（FL/Fl）
+ 得克萨斯（TX/Tx）
+ 纽约、亚利桑那、新泽西等紧随其后

* 订单时间主要集中在 **2025年6月至7月**，对应 Trump Mobile 预购与初期运营阶段。

**高敏感字段示例：**

部分记录包含：

* eSIM 二维码字符串（格式如 LPA:1$t-mobile.idemia.io$...）
* ICCID（SIM 卡识别码）
* PUK 码
* 激活日期与线路状态

**已核实的高调人物：**

文件中明确出现：

```
CustomerNumber: 25063456姓名：Eric Brunnett邮箱：eric.brunnett@trumporg.com电话：9176084053地址：115 Eagle Tree Terrace, Jupiter, FL订单状态：Provision套餐：30 Day Unlimited Talk Text Data
```

```
这与 Straight Arrow News、PCMag 等媒体报道的“特朗普集团副总裁兼首席信息官埃里克·布伦内特信息被泄露”完全一致。
```

文件中还包含大量普通用户记录，部分用户此前已向媒体确认自己曾与 Trump Mobile 有过交互（预购、开通或取消服务），信息匹配。

### 三、媒体核实情况

* **Straight Arrow News**

  最早报道，记者亲自联系文件中的用户，多人确认信息真实；并与黑客直接对话。
* **PCMag**

  联系了至少三名用户，确认他们曾与 Trump Mobile 互动，其中一人准确匹配了取消“30 Day Unlimited Talk Text Data”套餐的记录。
* **其他媒体**

  （The Verge、Forbes、Cybernews 等）：均引用上述核实结果，并指出文件中包含中途放弃订阅的潜在客户信息。

### 四、总结

这份由 BYOD 公开的文件，用实际数据证明了此前媒体报道的核心内容：约3600余条真实客户档案被完整泄露，字段详细到订单状态、eSIM 配置甚至部分激活信息，且包含特朗普集团内部高层。

事件暴露出 Trump Mobile 作为品牌授权方、其 MVNO 合作伙伴 Liberty Mobile 在员工终端安全与数据保护上的短板。从黑客感染员工电脑，到最终公开完整客户档案，整个链条清晰可见。事件仍在持续发酵，黑客组织目前仍在暗网活跃，并已将矛头指向其他目标。

【相关图片示例】

![](https://mmbiz.qpic.cn/sz_mmbiz_png/iaNqLNrWSicIp4PRCvhQGePBib4pgicgxeK1ibyYIy5W9NO8BaCN1TffXU8K7IWSQiaKWd92Rj5fOBmyssdcr4S7DcnbFlicdmPF1UosXvib0swjnvM/640?wx_fmt=png&from=appmsg)

历史文章

[日本一周20多家企业沦陷！烧肉金王、Times Car等累计超2000万信息外泄](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247486743&idx=1&sn=28e13d5454857bd162894d23c3b8ad72&scene=21#wechat_redirect)

[微软疑遭大规模内部工单数据泄露：约800万条记录、130GB数据被曝](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247486730&idx=1&sn=616268d9be82c614100409f76f91a836&scene=21#wechat_redirect)

[近期暗网重大泄露事件概览【20260930】](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247486710&idx=1&sn=be57482e466b36dcf6ab1a4706c702a9&scene=21#wechat_redirect)

[全球三大飞机发动机制造商之一数据泄露](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247486688&idx=1&sn=85f83eae314334cff512c319a951d1f7&scene=21#wechat_redirect)

[国内某留学招生平台数据疑遭曝光：1510万行记录涉及申请人护照、住址及财务信息](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247486681&idx=1&sn=276d912eee2d63e08ad6b13e86a693d2&scene=21#wechat_redirect)

[FBI又泄露了？黑客声称公开1,000万份FBI案件数据，涉及CIA、特勤局等敏感信息](https://mp.weixin.qq.com/s?__biz=MzcwMjIzMzAyNQ==&mid=2247486676&idx=1&sn=c2616ad305d840177f46673b0c0c67e6&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iaNqLNrWSicIrdzOzKicrEnqsQkLjp0wVFjwO1Pk5zRb4Pz2kv2h0vmiaPgqhYlL9CP2rAO9zthDeia7GJofYMLd80ayVHjJ510Fr3SpG88pcibH0/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=webp#imgIndex=15)

我们的服务

![图片](https://mmbiz.qpic.cn/mmbiz_png/iaNqLNrWSicIpljicQuictNklfCGhtUSic7s3OJHMvNBrh1fFicQHgrzU2RqicrEOM7Gmx1Zck1iavTKAKgC4n2psX5fic2I7pRYsicibtPuYyicFmMub6w/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=webp#imgIndex=16)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibBuy6MBMkBOjLcRoq5z6HJGh2YFWNrGpT2OCnicLfK2icJCTPNlutcb2gVia57NfRqrhN8KcI7NI4A16MZyY7zHrIiawZJ032vs7yqLKiapr5fbQ/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=18)

***01 **暗网监控与风险预警*****

7×24小时持续监控全球暗网论坛、数据交易市场、黑客社区、泄露平台及地下渠道，及时发现与客户相关的数据泄露、账号泄露、敏感信息曝光、勒索软件活动等风险事件，并提供预警通报与分析服务。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibBuy6MBMkBMXUKEibMPGptpmTfDG2hHvFy9t5aziaf6ics8ffhLv9uPHWnUKINx7HBD0fFdsMFS4fXb9FEOjWEqyicGEFZQggbnwOa8Pc43ZrPg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=22)

***02 **定向数据采集服务*****

根据客户业务需求，提供定制化数据收集与整理服务。支持：指定网站数据采集，指定行业数据采集，指定国家地区数据采集，以及其他相关数据采集服务。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_gif/ibBuy6MBMkBOOhYOtiaZoc57SOOribQLoLehLt5UDV9fct4m2zg4SFVmicYCCuJ2Cw99UTFEwBsWHuvWvBxkic7MjOIiavlvUfXXDh9maNib3M6T5o/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=26)

***03 定制化情报服务***

针对客户个性化需求提供专项支撑。例如：舆情监测、目标画像分析，行业情报研究。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iaNqLNrWSicIqiboREoXNFCmsNBBUCZuErwH8sYFL1QGialibRLkRyLv1zdQgdn7TKDFbNH0fV3EzO3naPQ7m6gzLKs630WjoIcibOuPkicHiaXWMs4/640?wx_fmt=other&from=appmsg&wxfrom=5&wx_lazy=1&watermark=1&tp=webp#imgIndex=31)

**内部社区交流群**

**加入方式**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/iaNqLNrWSicIonSEx8DIdAl8k2oiaprdCzGEiaBo6ibichD2zDbKiagcP9Dq6Cic7E6ETPe1rmxicflcliaq0nlAVBzC1Op7JZTmu8FN6ETIMdZwzA5ibw/640?wx_fmt=png&from=appmsg&watermark=1&tp=webp&wxfrom=5&wx_lazy=1#imgIndex=12)

![图片](https://mmbiz.qpic.cn/mmbiz_gif/HaJr68L1tTTyCC8O1Oa7QCNiaQwscfJqPCZib6GkcFrg9UiazicTe9PZdDEwZ111UTxdTXXrgeUzibuo6AQiaMuKTpNg/640?wx_fmt=gif&from=appmsg&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=10)

点点关注不迷路

预览时标签不可点

不喜欢

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iaNqLNrWSicIrrWGp3fibB8Ya39P5JtKp5ADwdziakKyGLkbVsT6BUht87anj0zvgkFtYt7XPJ7tFsQsQ0AdQnRdqDngo8RAfmTuqTjNicwawvjM/0?wx_fmt=png)

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