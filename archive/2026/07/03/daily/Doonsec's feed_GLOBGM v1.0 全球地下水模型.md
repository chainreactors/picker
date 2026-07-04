---
title: GLOBGM v1.0 全球地下水模型
url: https://mp.weixin.qq.com/s/wOEObFk-aythVhYCTnmeXQ
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:47:39.084074
---

# GLOBGM v1.0 全球地下水模型

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/wETfmQfRQWI7kl1zgubXtic2w81ibbDwf3AxpWF03kAUsVc7CnNWPo9QMn9Atg0Mv1HvaM1fW058yg4fSuYWFGc2DlnbTKTMOibSM3sGaiaBJxY/0?wx_fmt=jpeg)

# GLOBGM v1.0 全球地下水模型

LSC6
LSC6

生态遥感监测笔记

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 今日分享：

GLOBGM v1.0 全球地下水模型

GLOBGM v1.0 数据集是全球地下水建模领域的一个重要里程碑，它提供了 30 弧秒 PCR-GLOBWB-MODFLOW 模型的并行实现。该数据集由 Jarno Verkaik 等人开发，以赤道附近约 1 公里的空间分辨率，全面展现了全球地下水动态。该数据集利用两个模型层和 MODFLOW 6 框架，使用现有的 30 角秒 PCR-GLOBWB 数据驱动模拟，使研究人员能够探索全球尺度的地下水流动动态。计算实现采用消息传递接口进行并行化，从而在分布式内存并行集群上实现高效处理。

数据结构：

该表提供了 GLOBGM 数据集的模型栅格输出的结构化概述，包括文件路径和每个文件的描述。

| 文件路径 | 描述 |
| --- | --- |
| /steady-state/globgm-heads-lower-layer-ss.tif | 计算得到的下层模型稳态地下水头[m] |
| /steady-state/globgm-heads-lower-layer-ss.tif | 计算得到的上层模型稳态地下水头[m] |
| /steady-state/globgm-wtd-ss.tif | 计算得到的地下水位深度[米]（从上层到下层采样） |
| /transient\_1958-2015/globgm-wtd-.tif | 计算得到的地下水位深度[米]（从上层到下层采样） |
| /transient\_1958-2015/globgm-wtd-bot-\*.tif | 计算得到的地下水位深度[米]（仅限下层） |

引用方式：

```
Verkaik, Jarno, Edwin H. Sutanudjaja, Gualbert HP Oude Essink, Hai Xiang Lin, and Marc FP Bierkens. "GLOBGM v1. 0: a parallel implementation of a 30arcsec PCR-GLOBWB-MODFLOW global-scale groundwater model." Geoscientific Model Development 17, no. 1 (2024): 275-300.
```

![](https://mmbiz.qpic.cn/mmbiz_png/wETfmQfRQWKkSftI4ZMkFDpgaZ2icyWbMQ4rAia2Dpo3BGrc4jwju2yG3GgO63jJDMmzbadFJ0MVyYtuGiatR26zTQZqBLDibZUKetTaJkviacpk/640?wx_fmt=png&from=appmsg)

数据引用：

```
Verkaik, J., Hughes J.D., Langevin, C.D., (2021). Parallel MODFLOW 6.2.1 prototype release 0.1 (6.2.1_0.1). Zenodo.
```

![](https://mmbiz.qpic.cn/mmbiz_gif/wETfmQfRQWLqolpGD0vxwW6IPLPqbiavmf3L51zFPtqaDuxoJVrx2uOEibOSqsw8QkXIicOEWOSib6QSu2NQZMUpqtwKpLmRsKibE1pBpFeK4jPk/640?wx_fmt=gif&from=appmsg)

数据集构建方法：

基于 MODFLOW 的 5角分（5 角分，赤道附近约为 10 公里）PCR-GLOBWB 2（PCRaster 全球水量平衡模型）地下水模型的升级版，使用非结构化网格和基于消息传递接口并行化的 MODFLOW 6 原型版本。构建了总共包含 2.78 亿个活动单元的独立非结构化网格，以消除所有冗余的海陆单元，同时满足所有必要的边界条件。这些网格分布在三个大陆尺度的地下水模型中（1.68 亿个单元——亚非大陆；7700 万个单元——美洲；1600 万个单元——澳大利亚），以及一个用于较小岛屿的模型（1700 万个单元）。这四个地下水模型中的每一个都被划分为多个互不重叠的子模型，这些子模型在 MODFLOW 线性求解器中紧密耦合。每个子模型都被唯一地分配给一个处理器核心，相关的子模型数据在预处理期间使用数据块并行写入。

为了预先平衡并行工作负载，我们以两种方式应用了广泛使用的METIS图划分器：直接应用于所有（横向）模型网格单元，以及以基于区域的方式应用于分配给子模型的HydroBASINS流域，以便预先分类，最终与地表水耦合。利用荷兰国家超级计算机Snellius上进行一项实验，模拟1958年至2015年，时间步长为每日，输入数据为每月，并包含20年的预热期。考虑到串行模拟需要约 4.5个月的运行时间，我们设定了一个假设的目标，即最大模拟运行时间不超过16小时。

利用美国地质调查局（USGS）国家水信息系统（NWIS）提供的美国本土水头观测数据，对模型输出进行了有限的评估。结果表明，将分辨率从5 ′提高到30 ″ ，与5 ′ PCR-GLOBWB地下水模型相比，GLOBGM模型在稳态模拟方面取得了显著改进。

GLOBGM v1.0 开源软件介绍：

GLOBGM v1.0 是开源软件，GLOBGM 的开发模型工具可在 GitHub获取。地址如下：

```
https://github.com/UU-Hydro/GLOBGM
```

开源模型代码在github公布，可以公开使用：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wETfmQfRQWI1n7rLPEWic8S5hibNUdsguRI1K1SKrJQ0LQibiafxQVYWdu1Z4vV5dpNHV3rRAIibXAa8eZsFr61UQp4tSLK2Rqib1kFt360nd9dcs/640?wx_fmt=png&from=appmsg)

如何安装：

* 1.对于“写入分块参数数据”预处理，需要安装 PCR-Raster Python， PCR-GLOBWB Python 模型文件位于model\_tools\_src/python/pcr-globwb/ 目录中。
* 2.GLOBGM 预处理步骤“准备模型分区”和“分区并写入模型输入”需要使用 Fortran 编译）位于model\_tools\_src/fortran/ 目录下的工具。
* 3.要运行模型（“运行模型”），并行 MODFLOW 6 代码应该使用 Fortran 编译器进行编译，并与消息传递接口库链接。

后期处理方面，提供了两种主要工具：

mf6ggmpost：用于读取 GLOBGM 输出的 Fortran 工具，用于 MODFLOW 并写入水头或地下水位深度、聚合数据（例如水头下降斜率）以及采样时间序列。

analyze\_gw\_head：用于评估美国本土 GLOBGM 结果的 R 脚本，数据来自 NWIS 观测井。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wETfmQfRQWK8EHCqdkjdmCochw7kqlZM6p6YGVibbXUdmQHcg4X1wnHJduNVFE2Nnvk69I4fMNeLxCUia6iagS1hvXqDo5Y24RolATfRtHq72o/640?wx_fmt=png&from=appmsg)

01

—

GEE部分下载代码

```
var wtd = ee.ImageCollection("projects/sat-io/open-datasets/GLOBGM/TRANSIENT/WTD"),    globgm_wtd_ss = ee.Image("projects/sat-io/open-datasets/GLOBGM/STEADY-STATE/globgm-heads-upper-layer-ss"),    globgm_heads_lower_layer_ss = ee.Image("projects/sat-io/open-datasets/GLOBGM/STEADY-STATE/globgm-heads-lower-layer-ss"),    globgm_heads_upper_layer_ss = ee.Image("projects/sat-io/open-datasets/GLOBGM/STEADY-STATE/globgm-wtd-ss"),    wtd_bt = ee.ImageCollection("projects/sat-io/open-datasets/GLOBGM/TRANSIENT/WTD-BOTTOM");
print(wtd.limit(1000).aggregate_array('system:index'))
//根据日期增加年份的函数function addyear(image){  var year = ee.Date(image.get('system:time_end')).get('year')  return image.set('year',year)}

print(wtd.map(addyear).aggregate_histogram('year'))var palette = ["#1a1a4b", "#203387", "#254bb3", "#2b63e0", "#4673e6", "#6083ec", "#7a94f2", "#95a4f7", "#afb4fd", "#c8c5ff", "#dcb3f5", "#df96e2", "#e47ac0", "#e95da0", "#ec407f", "#ee265f", "#f00a3f", "#f20027", "#f30015", "#f30000"];
Map.addLayer(wtd.sort('system:time_start').first(),{min:-2,max:1200,palette:palette},'计算得出的地下水位埋深 [m]（从上层至下层采样）1958')Map.addLayer(wtd.sort('system:time_start',false).first(),{min:-2,max:1200,palette:palette},'计算得出的地下水位埋深 [m]（从上层至下层采样）2015年')
var diff = ["#0000FF", "#001AEB", "#0035D7", "#004FC3", "#006AAF","#00849B", "#009F87", "#00B973", "#00D45F", "#00EF4B","#00FF37", "#29FF2E", "#52FF25", "#7BFF1C", "#A4FF13","#CDFF0A", "#F6FF00", "#FFD300", "#FFA600", "#FF7900"]Map.addLayer((wtd.sort('system:time_start').first()).subtract(wtd.sort('system:time_start',false).first()),{min:-40,max:60,palette:diff},'Difference',false)
Map.addLayer(wtd_bt.sort('system:time_start').first(),{min:-2,max:1200,palette:["001219","005f73","0a9396","94d2bd","e9d8a6","ee9b00","ca6702","bb3e03","ae2012","9b2226"]},'计算得出的地下水位埋深 [m]（仅限下层）1958')Map.addLayer(wtd_bt.sort('system:time_start',false).first(),{min:-2,max:1200,palette:["001219","005f73","0a9396","94d2bd","e9d8a6","ee9b00","ca6702","bb3e03","ae2012","9b2226"]},'计算得出的地下水位埋深 [m]（仅限下层）2015年')
```

数据集是从1958年至2015年的逐月数据

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wETfmQfRQWJzsbK7r3hzlicogRIE6zicIbKJlpzP9D5T9hBvhfjgqOwn6DUVrdian8x9FYGkJ8h6v8ibGqr2PNtkQdRHuxTOY0a6QGpganmkKzk/640?wx_fmt=png&from=appmsg)

02

—

结果展示

![](https://mmbiz.qpic.cn/mmbiz_png/wETfmQfRQWLp1ic4LibyHaibBAbSV4qjU8aGo0kCOr6vuDO9cLkKhugNL8l8zbicVUDHacqO7OsI7KZV6reFlJcoBhFCT5zPgTTBib2dYv6Gahgo/640?wx_fmt=png&from=appmsg)

1958年计算得到的地下水位(下层采样)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wETfmQfRQWJ7lMxOUpHq1iaiassX5DbOia7bg7bd1OVU0MgpBwiapjqt743ic7fD7MKIAUk0J7tUXyBlpD4yCg4z2wwf4qBRZuQYkxHcBIFLV75A/640?wx_fmt=png&from=appmsg)

1958年计算得到的地下水位深度（从上层到下层采样）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wETfmQfRQWJKsswIYjOdAuibficGGD2dibicFbwmyK099MHuuZXDNf29CicKdJF7ZILYKsL9Uoib4aiblWppnuL1vCpnic1a99bS7htwXrXu9ibQoneQ/640?wx_fmt=png&from=appmsg)

2015年计算得到的地下水位(下层采样)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/wETfmQfRQWKLhtYDqhRxtLfhwkhxc3pw3I8jfklIWiasRzZMiaicGfwLj0OIzYpDzDqicdu8ibw9vJt2XZQcl5rr0BaOJibXHfNmTenawibKAQuxNI/640?wx_fmt=png&from=appmsg)

2015年计算得到的地下水位深度（从上层到下层采样）

![](https://mmbiz.qpic.cn/mmbiz_png/wETfmQfRQWIzezPUhbauo5sabuxkbsiaRwGja3icSvCW6VncwGSnFbVzNGdXUe9yuDQN2bodrVv6jz0OHibZG2d39ibXm334ib6FbvckPbPQUO5w/640?wx_fmt=png&from=appmsg)

地下水位变化值分布

代码完整链接**请在微信公众号后台私信“**

GLOBGM v1.0 全球地下水模型

”

感谢关注，欢迎转发！

**声明：仅供学习使用！**

******希望关注的朋友们转发，**如果对你有帮助的话记得给小编点个赞**或者在看**！****

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