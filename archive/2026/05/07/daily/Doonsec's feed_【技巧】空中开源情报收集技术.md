---
title: 【技巧】空中开源情报收集技术
url: https://mp.weixin.qq.com/s/m_NekxOgLW-zoft_xxm82w
source: Doonsec's feed
date: 2026-05-07
fetch_date: 2026-05-08T04:49:43.018637
---

# 【技巧】空中开源情报收集技术

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/no8YFGgia2NFpR4By1hXe1HT22M5eicZP5I41I3rjeQ6d5GicKo7TZ5pGWdab0MyzJC7ibV16YZnuQIUqAp4IpLFpKNXT1RCHFQpXPyyueUKu6k/0?wx_fmt=jpeg)

# 【技巧】空中开源情报收集技术

原创

丁爸
丁爸

丁爸 情报分析师的工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 空中开源情报（OSINT）收集涉及分析来自卫星、无人机和飞机的公开图像和数据，以监测物理发展、基础设施和活动。关键技术包括利用商业卫星供应商（Maxar、Planet）、公共地图平台和无人机摄影来追踪军事调动、建筑施工或环境变化。

##

## 空中开源情报（OSINT）已从一项小众的军事能力转变为记者、研究人员和安全分析师的重要工具。该领域的发展将越来越依赖于**未经筛选的实时数据**和**人工智能增强的图像分析**。

##

**关键的空中开源情报收集技术**

* **商业卫星图像分析：利用**Google Earth、Planet Labs或Maxar等供应商提供的高分辨率图像来监测随时间推移发生的变化，例如军事设施的建设或部队的调动。
* **无人机（UAV）图像监测：**分析消费级或商用无人机拍摄的图像，这些图像越来越多地上传到社交媒体或公共平台。这些图像提供了特定位置的高分辨率实时信息。
* **合成孔径雷达（SAR）图像：**利用雷达数据（可以穿透云层并在夜间捕捉图像）来探测和分析物体或活动的物理特征。
* **公开可用的航空照片：从公共来源（例如**NASA，用于火灾跟踪；或 ESA，用于环境监测）获取航空、卫星和热成像图像。
* **地理标记社交媒体分析：**使用工具识别从飞机或高海拔地区拍摄并发布在社交媒体平台上的图像或视频。

**常用应用程序**

* **冲突监测：**跟踪军事集结、装备部署和敌对行动造成的损失。
* **基础设施分析：**监测核导弹发射井、边境检查站或工业场所的建设。
* **环境与灾害监测：**识别非法土地开垦、监测自然灾害和分析环境破坏。

**必备工具和平台**

* **Google Earth Pro / 地图：**用于查看历史和当前的卫星图像。
* **Sentinel Hub：**用于访问欧洲航天局卫星数据。
* **社交媒体平台：**Twitter（现已更名为 X）和专门用于发现用户上传的航拍内容的论坛。
* **GIS 地图工具：**用于地理定位和分析图像元数据。

正如CSIS报告中所解释的那样，这种学科经常被用来独立验证各种说法，例如美国科学家联盟等组织依靠商业卫星数据进行监测。

---

##

## 1. 主要收集方法和工具集

空中开源情报通常分为三个领域：**卫星图像**、**实时飞行跟踪**和**地面-空中关联**。

### A. 卫星图像与时间定位

该方法涉及分析高空捕获的数据，以监测基础设施、冲突地区或环境变化。

1、谷歌地球

https://earth.google.com/

高分辨率历史图像，可追踪数十年来的城市发展或地形变化。

![](https://mmbiz.qpic.cn/mmbiz_png/no8YFGgia2NE8RdchOZl3Pj22FUPVbLcQXHtHiaeYiboib7XYMALhD0icicuGXCjhwaNCnjyHX8oZKn71ia5HxEWd2hoYRzLp7dcSDfTyfrPX5UlKk/640?wx_fmt=png&from=appmsg)

2、欧洲航天局哥白尼浏览器-哨兵卫星影像

https://apps.sentinel-hub.com/eo-browser/

多光谱数据（10米分辨率），可监测森林火灾、作物健康状况或大规模军事行动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NHft4d8hegibvey5UP88rwJwpHGgowDzaUobZKquQmZvSDxeibJ5A4LnBnXhED2Nms7CmB80bt2vEZfCm5aKx8u0CWD1uRibxflZI/640?wx_fmt=png&from=appmsg)

https://eos.com/landviewer

![](https://mmbiz.qpic.cn/mmbiz_png/no8YFGgia2NGKNYGxmhpNs5uzc7jdUsS9DSVHiaMz6XicEckkB95wfLwBTUiaN4v80Yl3ux0xTokZhvibcdgNjDPWzhUKUGSQHGib8K616MH2quAw/640?wx_fmt=png&from=appmsg)

https://browser.dataspace.copernicus.eu/

![](https://mmbiz.qpic.cn/mmbiz_png/no8YFGgia2NEZW8IJp8B37xg2hxv4sqBjLzKvaDNP3eKfTKc2MPNEicneVOfL0aicbFKCMX35shYL60xZZD77yU9ibXxElP9uaEy13utmTu3s00/640?wx_fmt=png&from=appmsg)

3、ArcGIS Location

https://location.arcgis.com/

可对比图像，对特定地点进行“前后对比”分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NGrZu4UdQDWbiaaTOk3EJpMZ3eZKxu5LMeLdgfIibHW6FzXSptRUdkbVnrpu4VB1J79E0XbgzQX60IibkolapuOMtKjCGSaWR6OmQ/640?wx_fmt=png&from=appmsg)

4、**美国地质调查局地球探索者**

https://earthexplorer.usgs.gov/

超过40年的NASA/USGS数据，可进行长期环境和地质研究。

![](https://mmbiz.qpic.cn/mmbiz_png/no8YFGgia2NFwqK1n5wVfuQHETd71E9sy7HJXFVIZlzFDfGau7jA6A07iaZ7lfC3JPWMqpORV2YCxXe1sU1Fro56wmRG9gWstn7IbA5a6ORXk/640?wx_fmt=png&from=appmsg)

### B. 未经过滤的航班跟踪

与尊重亿万富翁或军事实体隐私要求的商业应用程序（例如 FlightRadar24）不同，**未经过滤的**平台会显示通过 ADS-B 广播的每一个信号。

ADS-B

https://globe.adsbexchange.com/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NGcsph6GiaWeMUZ4JGBSFcEv3Q9PsD7pqbVzia0DcAwSBZQGQJxESrp2PBbibOY5ghY0xYnbEZAW7wBY6Gp70VmIibhoAib6vHVYDKo/640?wx_fmt=png&from=appmsg)

* **收集的信息：** ICAO 十六进制代码、注册号、高度、垂直速率和应答机代码（ADS-B 交换，无日期）。
* **主要优势：**它可以追踪隐藏在其他地方的“被封锁”的飞机——军用喷气式飞机、私人豪华飞机和监视无人机。

##

## 2. 高级技巧与指导

### 通过阴影分析进行时间定位（SunCalc）

如果你有一张航拍照片，但不知道拍摄时间，你可以利用阴影的长度和方向来确定确切时间。

https://www.suncalc.org/

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NGJ78TAJEjcIRANQmTRaTvtRsfusbBMONgs5nMHAJhSMXibYv9fSD1v6Xgj4yrficmHjfp3IwhIf99kcdepl5RNslSw0iaMtPO19U/640?wx_fmt=png&from=appmsg)

确定位置：找到坐标

* **测量阴影：**使用该工具输入物体的估计高度（例如，10米高的杆子）。
* **调整日期/时间：**滑动时间条，直到模拟阴影方向和长度与源图像匹配。
* **数学关系：**太阳高度角决定了高度与阴影的比值：$h = s \cdot \tan(\alpha)$， 在哪里$h$是身高，$s$是阴影长度，$\alpha$是太阳的高度角。

###

### 地形匹配（PeakVisor）

用于对无人机拍摄的视频或航拍照片进行地理定位，其中只能看到山脉或地平线。

* **使用方法：**将照片上传到 PeakVisor 的**PhotoFit**工具。它会将 3D 地形模型叠加到您的图像上。您可以调整纬度、经度和倾斜度，直到数字地平线与照片完全吻合。

https://peakvisor.com/

## 3. 案例研究

[【情报实战】在我国周边频繁活动的电子战飞机活动规律及其部队信息](https://mp.weixin.qq.com/s?__biz=MzI2MTE0NTE3Mw==&mid=2651126086&idx=1&sn=0ae4c2b1fe22faf56e0df0e4455d42c0&scene=21#wechat_redirect)

[【资料】追踪瓦格纳老板失事飞机信息](https://mp.weixin.qq.com/s?__biz=MzI2MTE0NTE3Mw==&mid=2651138300&idx=1&sn=99ac5bcf164e087e0024cf8e5b93a6dd&scene=21#wechat_redirect)

### [【情报实战】实时发现俄乌战争期间在欧洲活动的北约军用飞机](https://mp.weixin.qq.com/s?__biz=MzI2MTE0NTE3Mw==&mid=2651128644&idx=1&sn=8a443733d1af3e4272c935419eaa0c58&scene=21#wechat_redirect)

### [【技巧】如何查询一家CIA运输承包商有多少架飞机？这些飞机都去过哪些地方？](https://mp.weixin.qq.com/s?__biz=MzI2MTE0NTE3Mw==&mid=2651123510&idx=1&sn=57b48b79af153b0cae581ecf0354562b&scene=21#wechat_redirect)

###

---

## 4. 法律和伦理方面的考量

虽然开源情报（OSINT）使用公开数据，但调查人员必须始终注意**数据保护法**，这些法律法规要求组织对其如何验证和处理情报负责。此外，自动抓取数据也可能违反某些卫星服务提供商的服务条款，从而导致法律风险。

**长按识别下面的二维码可加入星球**

**里面已有万余篇资料供下载**

**续费五折优惠**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/no8YFGgia2NFQBRS1jcMcibKx50Es8RWWy8TyVPHn3zCHw3ONjksulXeIfo2fkXP50Z70W316IM3G8pOyzKR4TgKvvjCib6FxEparCichN6Jppw/640?wx_fmt=jpeg&from=appmsg&watermark=1&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=2)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NFESZibsC7Dx12Z6vvEDg99uEsCAvGHwbf50FqMe83gZyVraKI9lPm2jOBuchjNKJPS16RBW7WeTJq8TrOaMe82iaScO3GaaKKaY/0?wx_fmt=png)

丁爸 情报分析师的工具箱

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NFESZibsC7Dx12Z6vvEDg99uEsCAvGHwbf50FqMe83gZyVraKI9lPm2jOBuchjNKJPS16RBW7WeTJq8TrOaMe82iaScO3GaaKKaY/0?wx_fmt=png)

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