---
title: OSINT：使用 Overpass Turbo 查找监控摄像头
url: https://mp.weixin.qq.com/s/7mOyIgF_1Fo0mI-QX_GTeQ
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:22:34.227338
---

# OSINT：使用 Overpass Turbo 查找监控摄像头

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OicPTzQkpEk3dHCqQiaqCicJ5e3RrXT3AVSNsicVGjiaDPQ7icaWrR5QrZm8kJULDtdlV3hKVeb4oZNzxuY182sbdNqeTgRXXTDs9IIdOVy9GzSKs/0?wx_fmt=jpeg)

# OSINT：使用 Overpass Turbo 查找监控摄像头

原创

NEkill
NEkill

情报分析站

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_jpg/OicPTzQkpEk1UW6W2ABxich7xoBcibaRA7B8oh0DuV8pKma0dXuPQO1vyXV0x6lxMHBiaK74A8yiafcTHGvUl1AtadPmHWc9bt1MBSBHwIRsZTI4/640?wx_fmt=webp&from=appmsg)

在任何安全项目的侦察阶段，信息收集至关重要，今天，让我们将关注点从卫星OSINT转向基于地图的侦察。许多读者已经熟悉Google Maps及其替代方案，例如OpenStreetMap（OSM）。但您是否知道，通过一款名为**Overpass Turbo**的工具，您可以轻松从OSM中提取特定数据，例如监控摄像头或Wi-Fi热点？

让我们来探索如何利用这一强大的侦察工具。

## ****步骤 #1：了解 Overpass Turbo 的基础知识****

##

Overpass Turbo 可通过 https://overpass-turbo.eu 访问，无需安装或注册。它提供了一个基于网页的界面，用于查询 Overpass API——即 OpenStreetMap 的数据提取引擎。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OicPTzQkpEk0NaXQXJjibxMUZicVcd7Ewybxeac0AwPpQmLfG6r1taPfsruCsc947ZclTyQyND4x44tkq42IbQyRzbhNuYYWU2aUeY3BlRGy0A/640?wx_fmt=webp&from=appmsg)

该界面由三个主要组件构成：

1. 查询编辑器（左侧）：您可以在此使用 Overpass 查询语言（QL）编写查询
2. 交互式地图（右侧）：以地理形式显示查询结果
3. 工具栏（顶部）：包含“运行”按钮、向导、导出选项和设置

首次访问 Overpass Turbo 时，您会看到编辑器中已加载了一个默认查询。地图显示当前视口，您可以通过平移和缩放来聚焦感兴趣的区域。

查询向导

对于初学者，向导工具（可通过工具栏访问）提供了一个简化的界面。您可以输入通俗的英语搜索词，向导会将其转换为正确的 Overpass QL 语法。例如：

输入：amenity=atm in London

![](https://mmbiz.qpic.cn/sz_mmbiz_png/OicPTzQkpEk0hq1ibPonCaoicpias0cXApbUAvG5UrTeYm9F2KFiayHOnwj7icKo5UuIX4dt9TeTUAR5pOUIicHzl3mK8OWDq7ziaPEeVY392YJTiaA0/640?wx_fmt=png&from=appmsg)

点击“构建并运行查询”。

向导会生成相应的查询语法并自动执行。

![](https://mmbiz.qpic.cn/mmbiz_jpg/OicPTzQkpEk0gqvAqz6BXI6Xe7ssP4znWglenqBbm6Z12icpCZ5ObjNiayTgbsrNCMy0Urf6C7P3Zzv64DloDlibibbC1ZdosBV2SP6yFtCCk0RY/640?wx_fmt=webp&from=appmsg)

结果，我们可以看到一张伦敦自动取款机分布图。

步骤 #2：编写 Overpass 查询

Overpass 查询语言遵循特定的结构。让我们来分析一下向导生成的查询的构成：

```
[out:json][timeout:25];

// fetch area “London” to search in

{{geocodeArea:London}}->.searchArea;

// gather results

nwr["amenity"="atm"](area.searchArea);

// print results

out geom;
```

虽然其中已包含注释，但为了更好地理解，让我们深入探讨一下。

**[out:json][timeout:25]– 将输出格式设为 JSON，并将服务器端执行时间限制为 25 秒。**

**{{geocodeArea:London}}→.searchArea; – 一个宏，用于解析伦敦的行政边界（其 OSM 关系）。结果存储在一个名为 .searchArea 的临时集合中，供后续引用。**

nwr[“amenity”=“atm”](area.searchArea); – 代表节点、路径和关系。nwr

OpenStreetMap 有三种元素类型：

• 节点：单点位置（例如摄像头、WiFi 接入点）

• 路径：线段和闭合形状（例如道路、建筑轮廓）

• 关系：节点和路径的集合（例如建筑群、校园）

该过滤器筛选出所有标记为 ATMs 的 OSM 元素，并将搜索范围限制在先前定义的伦敦区域内。[“amenity”=“atm”](area.searchArea)

out geom; – 输出匹配的元素，包括其完整的几何信息 ()——带有经纬度的点、包含节点列表的路径，以及包含成员几何信息的关联。geom

标签过滤器

标签过滤器是您侦察查询的核心。OSM 中的标签遵循 key=value 结构。

node[“key”=“value”]

通过访问 ：https://wiki.openstreetmap.org/wiki/Map\_features

您可以查看所有可能的键值列表。从技术人员的视角出发，您可以检查 man\_made 键来发现与监控相关的选项。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/OicPTzQkpEk3IEgEgfecazgR6AmEjI06ACn24RRRRiaqwEIibuMbSgjl4iajwxnLDXKjS3PMEbpTqPjtZicDYfyYW3ljv9XNpiaxZJkKn4ZaHB1ZI/640?wx_fmt=webp&from=appmsg)

现在，让我们修改查询，尝试查找加利福尼亚州的监控摄像头。

```
[out:json][timeout:25];

{{geocodeArea:California}}->.searchArea;

nwr["surveillance"="camera"](area.searchArea);

out geom;
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/OicPTzQkpEk0lycko6n8vg5VM4C9OX9FdVoIBzTP2t74p4KLiahQQ4Rg4aJgBF4G3qnFVkI3lribmU4fNA4ib3VAJB3Picialn7MH5Pem97yicDs1s/640?wx_fmt=webp&from=appmsg)

现在，让我们尝试查找莫斯科的数据中心。

```
[out:json][timeout:25];

{{geocodeArea:Moscow}}->.searchArea;

nwr["building"="data_center"](area.searchArea);

out geom;
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/OicPTzQkpEk3N8w4H3c2gy7LjXTBicIqxAA4VjpJT739aice4ia3FxCcnEic6gib8zuvIDacEiaibX0BXibGvuWOjxibKuHZd49loTcAEtJcgHJ1Wn9lM/640?wx_fmt=webp&from=appmsg)

总结

通过查询和可视化 OpenStreetMap 的众包数据，调查人员可以显著提高工作效率。Overpass Turbo 特别适用于追踪城市发展、考察监控设施分布以及许多其他应用场景。在每种用例中，用户都可以精确定制查询，从 OpenStreetMap 上庞大的地理信息库中提取特定的数据点。

**END**

[知识星球](https://mp.weixin.qq.com/s?__biz=MzkxMDIwMTMxMw==&mid=2247494304&idx=1&sn=3cd95698536c65890e73167f02949273&scene=21#wechat_redirect)**已有817份文档，对每一个文档逐步进行翻译，进入知识星球的费用不定时会做出调整**

![图片](https://mmbiz.qpic.cn/sz_mmbiz_jpg/71FNwicgZ35ejUoJOv6pS48h19eMhibCAvlqJU8K7f5GIxFdLRjaYZbj2ZD1UQ8mkGNRTNp1MadMhInmzNvLbxTA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&tp=webp#imgIndex=3)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/71FNwicgZ35c7KuyVhVhNcwfBKhon32hZE4rGARefz8xU5Ubs8y7eIsiak6khGH2icPb68c7bvkYo2oQQdzt0BGag/0?wx_fmt=png)

情报分析站

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/71FNwicgZ35c7KuyVhVhNcwfBKhon32hZE4rGARefz8xU5Ubs8y7eIsiak6khGH2icPb68c7bvkYo2oQQdzt0BGag/0?wx_fmt=png)

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