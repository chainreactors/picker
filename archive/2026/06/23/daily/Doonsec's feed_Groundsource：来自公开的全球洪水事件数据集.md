---
title: Groundsource：来自公开的全球洪水事件数据集
url: https://mp.weixin.qq.com/s/z79RMurKCSyQAIC0ouPKkA
source: Doonsec's feed
date: 2026-06-23
fetch_date: 2026-06-24T06:03:51.304322
---

# Groundsource：来自公开的全球洪水事件数据集

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/wETfmQfRQWIky1jE6QC0QJFZHek1QUjh6OWAErzPicnV2PXYHystgMh8whkn51icz6jsSpjOBDNwzQsdg5T0IS1s3D0ofniaXhic3U2wy3lOLno/0?wx_fmt=jpeg)

# Groundsource：来自公开的全球洪水事件数据集

原创

LSC6
LSC6

生态遥感监测笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

今日分享：

# Groundsource：来自公开的全球洪水事件数据集

Groundsource是一个开放获取的全球数据集，包含260万条高分辨率历史洪水事件记录，这些数据来自对超过150个国家/地区500多万篇新闻报道的自动化处理。该数据集填补了全球洪水观测基础设施的一个关键空白：与地震事件（由标准化传感器网络系统地记录）不同，水文气象灾害缺乏统一的全球观测系统。传统的物理水文站网络存在地理分布稀疏的问题，而卫星遥感数据则受到云层覆盖、过境频率以及对大型、持续时间长的洪水事件的偏好等因素的限制。

为了克服这些局限性，Groundsource流程利用Gemini大型语言模型（LLM）从非结构化的新闻文本中系统地提取结构化的时空数据。新闻文章通过谷歌的WebRef命名实体识别系统导入，经过洪水相关性筛选后，使用云翻译API翻译成英文，然后由Gemini进行处理，以对事件进行分类、提取洪水日期、识别精细的洪水淹没区域，并通过谷歌地图地理编码API将地名与标准化的地理数据库进行比对。最终得到的事件记录按时空聚合到一个扁平化的表格数据集中，该数据集具有每日时间分辨率和局部空间边界，涵盖2000年至今。

#### 数据属性特征：

* **总记录数：** 2,646,302 条独立洪水事件观测记录
* **时间跨度：** 2000 年至今（每日分辨率）
* **空间覆盖范围：**全球150多个国家。
* **平均空间占地面积：**每次活动 142 平方公里；82% 的活动占地面积小于50 平方公里。
* **已处理的源文章：**涵盖 80 种语言的超过 500 万篇新闻文章

#### 数据集模式：

数据属性表中的每一行代表一次独立的时空洪水观测。每条记录都包含以下字段：

* **uuid：**每个记录的唯一标识符
* **area\_km2：**所报告位置多边形的面积（平方公里）。
* **start\_date：**有文字记录证明持续洪水发生的初始日期（YYYY-MM-DD）。
* **end\_date：**有记录可查的洪水发生的最后一个连续日期（YYYY-MM-DD）；对于单日事件，end\_date 与 start\_date 相同。
* **几何形状：**所报告位置的空间边界，采用 WGS 84 (EPSG:4326) 坐标系，可以是复杂的多边形（例如，行政区）或缓冲区点（例如，特定的街道交叉口）。

请注意，该数据集是**基于实体的，而不是基于气象的**。一次大规模气象洪水可能会产生多个条目，分别对应于独立报告的被淹没的地理实体（社区、城镇、地区）。

#### 数据局限性和偏差：

该数据集有以下数据局限性：

* **时间上的近期性偏差：**约 64% 的记录事件发生在 2020 年至 2025 年之间，这反映的是数字化在线新闻的指数级增长，而非洪水发生频率的实际增加。较早的事件由于数字化存档新闻的相对稀缺和链接失效而未被充分记录。
* **空间媒体偏差：**事件密度与区域数字新闻基础设施相关。数字媒体稀少或本地新闻使用 Read Aloud API 支持的 80 种语言之外的语言发布的地区，其新闻报道量系统性地偏低。巴布亚新几内亚的召回率降至 39%（GDACS），加蓬降至 50%，而美国则高达 96%。
* **事件严重程度与回忆率相关：**影响较大的事件更容易被新闻媒体报道，从而更容易被记录下来。对全球灾害预警和控制中心（GDACS）红色预警事件的回忆率达到99%，而对绿色预警事件（国家可控事件）的回忆率则为82%。
* **非独立同分布错误：**地理编码错误可能在空间上聚集（例如，特定语言或地区中的歧义地名），这意味着错误率在不同地理区域可能不均匀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wETfmQfRQWI15r7UBlGqZpc6W8sRmibqMIibllrJRtJBEnQULtQo8DZYXNtWJWsFQeHjZnbayxCrWX3NlmEVdCEtPzLaknMAN0nHvV0a0wltg/640?wx_fmt=png&from=appmsg)

01

—

GEE部分下载代码

```
// Import GLWD v2 layers
var groundsource = ee.FeatureCollection("projects/sat-io/open-datasets/groundsource_2026");
// ============================================// PLASMA PALETTE — 27 evenly sampled stops// purple → pink → orange → yellow (old → recent)// ============================================var years = [  '2000','2001','2002','2003','2004','2005','2006','2007','2008','2009',  '2010','2011','2012','2013','2014','2015','2016','2017','2018','2019',  '2020','2021','2022','2023','2024','2025','2026'];

var palette = [  '0d0887','2b0596','46039f','5b01a5',  '6f01a5','8305a7','9512a1','a62098',  'b5318d','c24281','cc5374','d4647a',  'dc7566','e38653','e99646','eda72f',  'f0b81c','f2c90e','f4d711','f5e425',  'f7f230','f8f54b','f9f871','fafa7f',  'fcfb8f','fefea0','f0f921'];
// ============================================
// 每年增加一层
// ===========================================for (var i = 0; i < years.length; i++) {  var subset = groundsource.filter(    ee.Filter.stringStartsWith('start_date', years[i])  );  Map.addLayer(    subset,    { color: palette[i] },    'Floods ' + years[i],    true  );}
// ============================================// MAP SETUP// ============================================Map.setCenter(20, 20, 3);Map.setOptions('HYBRID');
// ============================================// LEGEND// ============================================var legend = ui.Panel({  style: {    position:        'bottom-left',    padding:         '8px',    backgroundColor: 'rgba(255,255,255,1)',    width:           '220px'  }});
legend.add(ui.Label({  value: '洪水事件',  style: { fontWeight: 'bold', fontSize: '13px', margin: '0 0 4px 0' }}));legend.add(ui.Label({  value: '首次有记录的洪水事件年份',  style: { fontSize: '11px', color: '#555', margin: '0 0 8px 0' }}));
var colorBar = ui.Thumbnail({  image: ee.Image.pixelLonLat().select('longitude')    .visualize({ min: 0, max: 1, palette: palette }),  params: { bbox: [0, 0, 1, 0.1], dimensions: '196x16' },  style: { stretch: 'horizontal', margin: '0 0 4px 0' }});legend.add(colorBar);
legend.add(ui.Panel({  widgets: [    ui.Label('2000', { fontSize: '10px', color: '#555' }),    ui.Label('2013', { fontSize: '10px', color: '#555', textAlign: 'center', stretch: 'horizontal' }),    ui.Label('2026', { fontSize: '10px', color: '#555', textAlign: 'right' })  ],  layout: ui.Panel.Layout.flow('horizontal'),  style: { stretch: 'horizontal', margin: '0 0 10px 0' }}));
legend.add(ui.Label({  value: 'Dataset overview',  style: { fontWeight: 'bold', fontSize: '11px', color: '#333', margin: '2px 0' }}));
var statLabels = ['Total records','Countries','Coverage','Avg. footprint','Precision'];var statValues = ['2.6 million','150+','2000 – present','142 km²','82% practical'];
for (var s = 0; s < statLabels.length; s++) {  legend.add(ui.Panel({    widgets: [      ui.Label(statLabels[s], { fontSize: '10px', color: '#555', margin: '1px 0', stretch: 'horizontal' }),      ui.Label(statValues[s], { fontSize: '10px', fontWeight: 'bold', color: '#222', margin: '1px 0' })    ],    layout: ui.Panel.Layout.flow('horizontal'),    style: { stretch: 'horizontal' }  }));}
legend.add(ui.Label({  value: 'Mayo et al. (2026) · Zenodo',  style: { fontSize: '9px', color: '#888', margin: '8px 0 0 0' },  targetUrl: 'https://doi.org/10.5281/zenodo.18647054'}));
Map.add(legend);

var snazzy = require("users/aazuspan/snazzy:styles");snazzy.addStyle("https://snazzymaps.com/style/38/shades-of-grey", "Greyscale");

// ============================================// PRINT SUMMARY// ============================================print('总洪水事件:', groundsource.size());print('样本记录:', groundsource.first());
// ExportExport.table.toDrive({  collection: groundsource.filterBounds(geometry),  description: 'groundsource',  folder: 'groundsource',  fileFormat: 'SHP',})
```

我简单画了个区域，在GIS打开显示如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wETfmQfRQWJFRcFECsr1YDAXkuVvWibxJgY34wYoejCPdHW0lFvdwshFXHYt3ZfXRVXRgDD6ibwfmssF8eMWO5xyqgfbH3VHfnYCsfRMbKvtU/640?wx_fmt=png&from=appmsg)

属性表包含开始日期，结束日期，洪水发生区域范围

![](https://mmbiz.qpic.cn/mmbiz_png/wETfmQfRQWJN5DYAibD546KtBsHFLI15MW2WjFYT76saa1m8TRo2zDgvHNMCUpfm9f3J8wics5ibu2DUBegtL8icicbKEAHtqhSbDbVc9Tm65KZI/640?wx_fmt=png&from=appmsg)

02

—

结果展示

![](https://mmbiz.qpic.cn/mmbiz_png/wETfmQfRQWIXRQeJq9sYoyWsyzRIfJX9mSKYwDiabFHb3Y6Vn9qYnicVlsYliacMlX0ricoiaQDQSoRb6Uu8zEFl4U8xamHxDHsPGCakbbWoQxOs/640?wx_fmt=png&from=appmsg)

2025年随机区域洪水发生事件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wETfmQfRQWLSqLUEPMt4gsb3r1UiaG7tnibYKQEz9P6hxrZrPeicJGtByvq8FZqadyiaUrxwDqyuElWMfZJurKdJF8b9iaX0deEvOib02hibZpKxWc/640?wx_fmt=png&from=appmsg)

2020年随机区域洪水发生事件

![](https://mmbiz.qpic.cn/mmbiz_png/wETfmQfRQWIH1dc4HPIEkdsI41xpnrpvhJnKBxjvicEDP0FPRticN4LzWtCl6lGeErx7ksbWU1kHF9zGgcRoCibAxo78d2giasBXRGOl9XoQYBs/640?wx_fmt=png&from=appmsg)

2015年随机区域洪水发生事件

![](https://mmbiz.qpic.cn/mmbiz_png/wETfmQfRQWKkJcPlaQ96HsKpqWNhCc0XAQ3S1k524Kf7xEDMMETM0ibY4leMO9USdSPjeC1ZicdYkcUDCRSjhqyibQPSQddhONyCPnUNg88Qrc/640?wx_fmt=png&from=appmsg)

2010年随机区域洪水发生事件

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wETfmQfRQWKDREr3ltiaUYvwKpC4gKFvs8zL1S4wP3lnyhELaoBK82PrbrlzftGOP5gJpe5v8a17aPbb2MYTPOQicMp9lzW1ItBweclIe2qFY/640?wx_fmt=png&from=appmsg)

2005年随机区域洪水发生事件

代码完整链接请在微信公众号后台私信“

Groundsource数据集”

感谢关注，欢迎转发！

声明：仅供学习使用！

希望关注的朋友们转发，如果对你有帮助的话记得给小编点个赞或者在看！

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/fficOnIgz71dADS9JVHTlzYKG7ibaITl8ia4ibhpE8PAaAJIskTgpyUrhzZVcPsG9bThrTVCflc0hYJiaeyRCKp8bWQ/0?wx_fmt=png)

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