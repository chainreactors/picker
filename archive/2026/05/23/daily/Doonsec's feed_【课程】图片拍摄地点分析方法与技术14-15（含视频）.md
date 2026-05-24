---
title: 【课程】图片拍摄地点分析方法与技术14-15（含视频）
url: https://mp.weixin.qq.com/s/CdP_yttcjPkn280qBr-Yqw
source: Doonsec's feed
date: 2026-05-23
fetch_date: 2026-05-24T05:55:11.368115
---

# 【课程】图片拍摄地点分析方法与技术14-15（含视频）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/no8YFGgia2NEHQAP2Uicibv0zUUcL4UqV6A9kYD6ibENYuIVgZpzB3bAXPUvDhUKibbNoD4ibBY9SPWuHSGdNwGSJCsL0YkKWzXe3L1ia0hCs4O0Cc/0?wx_fmt=jpeg)

# 【课程】图片拍摄地点分析方法与技术14-15（含视频）

原创

丁爸
丁爸

丁爸 情报分析师的工具箱

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/mmbiz_png/no8YFGgia2NGVmja8LfhpCicOwYr6jk1CG0FVe1RiaHe9hY1g7QtTWGrRrIVGk8hRsXic3A1Ca0riavyW4lPSH2Pia9icK0NKAYxKESeEcX6bBZVDM/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NHxoCjo5TyLF4q4xF0WNIbicXTOd1lkUxuFLRGVAZ9ejHPPR66APxByiarNm4Q95CUN8MqOXWBwVGFibWljNSKhn2UibgWaqicHbUAs/640?wx_fmt=png&from=appmsg)

### 太阳几何学基础

#### 太阳高度角（Solar Elevation Angle）

**定义**：太阳高度角（记作*h*）是指太阳光线与地平线之间的夹角。通俗地说，就是你抬头看太阳时，视线与水平地面的夹角。

•**取值范围**：0°~90°

•**正午时分**：太阳高度角达到一天中的最大值（正午指地方时 12:00，非手表时间的 12:00）

•**日出日落**：太阳高度角为 0°

•**夜间**：太阳高度角为负值（太阳位于地平线以下）

**生活中的直观理解**：

夏季正午走在街上，太阳几乎在头顶正上方，影子很短——此时太阳高度角接近 90°；冬季傍晚，太阳低垂在地平线附近，影子被拉得很长——此时太阳高度角接近 0°。这种日常体验，正是我们进行时间推断的物理基础。

#### 太阳方位角（Solar Azimuth Angle）

**定义**：太阳方位角（记作*A*）是指太阳光线在水平面上的投影与正北方向之间的夹角。按照气象学惯例，通常以正北为 0°，顺时针方向增加：

|  |  |
| --- | --- |
| 方向 | 方位角 |
| 正北 | 0°（或 360°） |
| 正东 | 90° |
| 正南 | 180° |
| 正西 | 270° |

**注意**：不同学科领域对方位角的定义可能不同。天文学中有时以正南为 0°，使用时务必确认工具采用的约定。SunCalc 等工具一般采用”正北为 0°、顺时针增加”的约定。

**关键规律（北半球）**：

•上午：太阳位于东侧，方位角在 0°~180° 之间（通常 90°~180°）

•正午：太阳位于正南方向附近，方位角约 180°

•下午：太阳位于西侧，方位角在 180°~360° 之间

#### 地球自转与公转对光影的影响

**（一）昼夜更替与太阳视运动**

由于地球自西向东自转，我们在地面上观察到太阳”东升西落”的视运动。这一看似简单的现象，实际上蕴含了精确的时间信息：

•地球自转一周约 24 小时，转过 360°

•每小时转过 15°（360° / 24 = 15°/h）

•每 4 分钟转过 1°

这意味着：**太阳方位角的变化速率约为每小时 15°**（此数值为近似值，实际速率因纬度、季节而异）。

**（二）季节变化与太阳赤纬角**

地球公转轨道面（黄道面）与赤道面存在约 23.5° 的夹角（黄赤交角），这导致太阳直射点在一年中在南北回归线之间移动。

**太阳赤纬角（Declination，记作 δ）**：太阳直射点所在的纬度。一年中在 +23.5°（夏至）到 -23.5°（冬至）之间变化。

|  |  |  |
| --- | --- | --- |
| 日期 | 节气 | 赤纬角δ |
| 3 月 21 日前后 | 春分 | 0° |
| 6 月 22 日前后 | 夏至 | +23.5° |
| 9 月 23 日前后 | 秋分 | 0° |
| 12 月 22 日前后 | 冬至 | -23.5° |

#### 太阳高度角计算公式

太阳高度角的精确计算涉及球面天文学中的基本公式。对于情报分析工作，我们主要使用以下核心公式：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NGgFcu8b4kqoC6ZkHtylq8YjGwGwFy4xPCZ1ic429MbCthIvsJbB4qt25fLtwtpAqF6sVdyby1JxKoG6yibesZibRS5Uva2j64ETc/640?wx_fmt=png&from=appmsg)

**各参数含义**：

|  |  |  |
| --- | --- | --- |
| 符号 | 含义 | 说明 |
| *h* | 太阳高度角 | 待求量，输出范围 [-90°, 90°] |
| *φ*（phi） | 观测点纬度 | 北半球为正，南半球为负 |
| *δ*（delta） | 太阳赤纬角 | 当日太阳直射点纬度 |
| *ω*（omega） | 时角 | 正午为 0°，每小时变化 15°，上午为负、下午为正 |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NFia3DyXN6P0sh0KTRAFLfQibFJalbWgaeY2dkmYpONOSbjWNtvAoS8zaUOx6Dq7oCWBd9ky7Kf531YpMCia5lY1icBuzUHc5TLQXE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NELkj9VS465STY0y4icBiclQsk4XTwUYicPhsGVdm6ibBIZtHt5ZZLC0UMWPy2u09VWRRY4nf8k3CM5cKJKydQLNSjGDZPgl4CU7ZU/640?wx_fmt=png&from=appmsg)

### 影子分析法

本节是实战应用的核心。建议从”影子的方向告诉你什么”“影子的长度告诉你什么”两个问题切入，引导学生建立”影子即信息”的分析意识。

#### 影子方向与太阳方位角的关系

影子的方向与太阳方位角存在严格的反方向关系：**影子指向太阳所在位置的反方向**。

**北半球的影子规律**：

|  |  |  |
| --- | --- | --- |
| 时间段 | 太阳方位 | 影子方向 |
| 上午 | 东南方向（方位角 90°~180°） | 指向西北 |
| 正午 | 正南方向（方位角约 180°） | 指向正北 |
| 下午 | 西南方向（方位角 180°~270°） | 指向东北 |

**关键观察**：在北半球，正午前后物体的影子**大致指向北方**。这一规律是进行方向判断和纬度推断的重要依据。

**南半球的影子规律**：

由于南半球太阳正午位于正北方向，因此影子**大致指向南方**，与北半球相反。

**赤道地区的特殊情况**：

在赤道（φ = 0°），春秋分日太阳直射头顶，正午影子几乎消失；其他日期影子可能偏北或偏南，取决于太阳直射点的位置。

#### 影子长度与太阳高度角的关系

影子长度与太阳高度角之间存在简单的三角函数关系：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NHEGQ6qA9fhIF0Q3qHBt3hib6jp1ql4EEVUBtfzZgcTswFdPZueeicY8FZibibAfJckC42pQ6AG7biblbwibXljCRuibjkBy8uHR8M5K8/640?wx_fmt=png&from=appmsg)

**各参数含义**：

|  |  |
| --- | --- |
| 符号 | 含义 |
| *L* | 影子长度 |
| *H* | 物体高度 |
| *h* | 太阳高度角 |

**核心推论**：

太阳高度角越高，影子越短；太阳高度角越低，影子越长

同一地点、同一时刻，不同高度的物体，其影子长度与高度成正比

通过测量影长与物高的比值，可反推太阳高度角：*h* = arctan(*H*/*L*)

**实际应用技巧**：

在照片中，即使不知道物体的实际高度，也可以利用”影长/物高”的比例关系。例如，一个标准身高（1.7m）的人站在建筑物旁，通过像素级测量，可以建立照片中像素高度与实际高度的比例尺，进而推算出建筑物的实际高度和影长对应的太阳高度角。

#### 拍摄时间推断技术

**方法一：通过影子方向判断大致时间**

在照片中确定影子的方向（相对于正北的方向）

反推太阳方位角（与影子方向相反）

根据太阳的视运动规律，将方位角映射为地方时

**简化估算公式**：

在北半球中纬度地区，可近似认为太阳方位角与时角呈线性关系。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NEsqOXQTuWPrnV5M10ryyOf7XoSuHdZbVp8Wpic6C00iav8f7U22FxC8KHm7VGWgcwVIFiaJ1ZF2ClWpUXBgwkcJRm8NxTbqeX8Mk/640?wx_fmt=png&from=appmsg)

**方法二：通过影子长度推算季节**

测量影子长度与物体高度的比值

计算太阳高度角*h* = arctan(*H*/*L*)

假设拍摄时间为正午，反推赤纬角δ

根据赤纬角确定一年中的大致日期范围

#### 纬度推断原理

**北回归线（约 23.5°N）以南地区**：

在北回归线以南，一年中某些时段太阳位于天顶以北，正午影子可能指向南方。具体规律：

•当太阳直射点纬度δ > φ（当地纬度）时，正午太阳位于北方，影子指向南方

•当δ < φ 时，正午太阳位于南方，影子指向北方

这意味着：**若观察到正午影子有时偏南、有时偏北，可判定拍摄地点位于南北回归线之间**。

**南回归线（约 23.5°S）以南地区**：

与北半球对称，正午影子通常指向南方。在南回归线以南的高纬度地区，正午太阳始终位于北方天空。

**纬度范围缩小的逻辑链**：

|  |  |
| --- | --- |
| 观察现象 | 推断的纬度范围 |
| 正午影子始终指向北方 | 北回归线以北（φ > 23.5°N） |
| 正午影子有时偏南、有时偏北 | 南北回归线之间（ |
| 正午影子始终指向南方 | 南回归线以南（φ < -23.5°） |
| 正午可出现无影（太阳直射头顶） | 南北回归线之间（ |

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NG7t9U4NF17E4t3xkZ3xjns5IeUrcRLs4jnzuO1icJkmqefp88GHwbdTiaWiav2bo3ywse3TW0rIgnAd0bkmcNUfOUxW1V0X8gRXw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/no8YFGgia2NEMVBnrKBC3dnPAqMxfyQYXYdCGjFIpSsmbPtA7ib2H765PNBnwjn8sFTZbNtYJyTUeLGEzHqx9mRM4qMocvnTjNQQIEDQibVFZE/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/no8YFGgia2NHoVMzVIQY3jpktC7DGt8iaqMZsF1HVHjUqiaKuN51FjeKHmQBlm9oLFmsmT8DPuK46EvXXXSXK0sE9CIUVWvpQ5kMocN2r9khao/640?wx_fmt=png&from=appmsg)

长按识别下面的二维码可加入星球

里面已有万余篇资料可供下载

续费五折优惠

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/B0AKMb5va5zKJ6IvDm7zH8uGKMLmpkqKYLbkAVHcDIy1pTdjbsOlqh0GOYj7RhhMsfCLtUtWfwEicsFibUicCMwnw/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=3)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/B0AKMb5va5weznr59sOFnfjlug4lPdXGst2Ppk4z9iaENOniczwktxLNyvXJU4y0ibGic51MrKtiaicscLW3JbrYhauA/640?wx_fmt=jpeg&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp#imgIndex=4)

预览时标签不可点

作者提示: 内容由AI生成

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