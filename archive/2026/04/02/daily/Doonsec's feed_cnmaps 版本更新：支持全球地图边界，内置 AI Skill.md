---
title: cnmaps 版本更新：支持全球地图边界，内置 AI Skill
url: https://mp.weixin.qq.com/s/F7g4aMvxmlJoUzcXk-gM_A
source: Doonsec's feed
date: 2026-04-02
fetch_date: 2026-04-03T04:21:51.620939
---

# cnmaps 版本更新：支持全球地图边界，内置 AI Skill

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/KtLeyFG8WBysDTZyxPXEHyy4AKeKPzaBqHxmmnj1joEkxNgGVIZ3W31HCRaMMZiamoJiaczGdAsw2JOb9mWkmDLdbXmy9ghYtk1R2KYvyrFeU/0?wx_fmt=jpeg)

# cnmaps 版本更新：支持全球地图边界，内置 AI Skill

原创

Clarmy
Clarmy

Clarmy吱声

![]()

在小说阅读器中沉浸阅读

## 背景

cnmaps 由于上游依赖 shapely 2.x 的大版本更新导致的兼容性问题一直没有得到解决，从2024年9月开始就进入了摆烂状态，至今已经将近2年。然而这期间各个包的版本都在更新迭代，以至于 cnmaps 积累的兼容性问题到今年已经逐渐变得积重难返。

然而最近迎来了转机，我开始尝试用 Codex 来解决 cnmaps 长期积累的问题，发现效果极好。Codex 不但帮我彻底解决了 shapely 兼容性的问题，还帮我清理了绝大部分遗留的 Issue，甚至替我实现了很多很早就规划了但是一直摆烂没有做的功能。在一周左右的密集开发之后，终于对 cnmaps 完成了一次大升级，发布了本次 `2.1` 版本的更新。下面我就来介绍一下最新版本有哪些新的功能。

## 1.解决遗留的兼容性问题

这是之前长期困扰很多用户的问题，一方面自己的开发环境里的各种模块包都需要随着时间的推移版本号在升高，而 cnmaps 锁死 shapely < 2.0 导致很多包版本冲突的问题日益严重，甚至最终可能无法正常使用。现在这个问题终于得到了彻底解决，现在 cnmaps 已经可以和最新版本的 shapely 完美兼容，用户不用再担心版本冲突的问题。只需要用 pip 把 cnmaps 升级到最新版本即可（conda 安装已废弃，无法用 conda 安装最新版本的 cnmaps，以后也不再提供支持）：

```
$ pip install -U cnmaps
```

## 2.支持全球国家边界

在 `1.x` 版本时期，cnmaps 只支持了中国的国家边界，对于其他国家，尤其是有领土争端的邻国并没有支持，这也长期制约了 cnmaps 的应用场景。而本次更新到 `cnmaps >= 2.1` 版本之后，用户就可以获取全球国家的国界线了，当然中国周边那些与中国有领土争端的邻国的国界线已经经过了处理，符合中国的领土主张。

```
import cartopy.crs as ccrs
import matplotlib.pyplot as plt

from cnmaps import draw_maps, get_adm_maps

fig = plt.figure(figsize=(12, 6))
proj = ccrs.PlateCarree(central_longitude=105)
ax = fig.add_subplot(111, projection=proj)
ax.set_global()

china = get_adm_maps(country="中国", level="国", only_polygon=True, record="first")
world = get_adm_maps(level="国", only_polygon=True)

draw_maps(world, ax=ax, linewidth=0.22, color="dimgray")
draw_maps([china], ax=ax, linewidth=0.75, color="crimson")

plt.savefig("world-countries-borders-flat.png", bbox_inches="tight")
plt.show()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KtLeyFG8WByias3wt03ZlBv9nqvCveUibKangN27QaIBjmdEY1EqOVV9f6dhrg8PJgSgWoia3abTjOkIpgGicfCLictqVFb38e4LHibBibUq00C7D4/640?wx_fmt=png&from=appmsg)

## 3.新的裁剪能力

在 `1.x` 时期，有一些图像类型的裁剪并没有支持，比如流线图和像素图。而本次更新新增了对流线图和像素图的裁剪能力，用户可以直接对风矢的流线图和地形阴影图按照矢量边界进行切割裁剪。

流线裁剪：

```
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from cnmaps import get_adm_maps, clip_streamplot_by_map, draw_map
from cnmaps.sample import load_wind

lons, lats, u, v = load_wind()

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
map_polygon = get_adm_maps(country='中国', record='first', only_polygon=True)

stream = ax.streamplot(
    lons[0, :],
    lats[:, 0],
    u,
    v,
    transform=ccrs.PlateCarree(),
    density=2.0,
    color='#1f77b4',
)

clip_streamplot_by_map(stream, map_polygon)
draw_map(map_polygon, color='k', linewidth=1)

plt.show()
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/KtLeyFG8WByLVKDg9UHiah0lCcPEIIrCXqTmLibOFqBWGCMyKolxkmY5qWC8351T042KwM4jGloVLwl1OWTsGBn43mwHBDBhYP3tQs4tt2vibU/640?wx_fmt=png&from=appmsg)

山地阴影裁剪：

```
import cartopy.crs as ccrs
import matplotlib.pyplot as plt
from matplotlib.colors import LightSource
from cnmaps import get_adm_maps, clip_imshow_by_map, draw_map
from cnmaps.sample import load_dem

lons, lats, dem = load_dem()
hillshade = LightSource(azdeg=315, altdeg=45).shade(
    dem,
    cmap=plt.cm.Greys,
    vert_exag=0.8,
    blend_mode='overlay',
)

fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection=ccrs.PlateCarree())
map_polygon = get_adm_maps(country='中国', record='first', only_polygon=True)

image = ax.imshow(
    hillshade,
    extent=[lons.min(), lons.max(), lats.min(), lats.max()],
    origin='lower',
    transform=ccrs.PlateCarree(),
)

clip_imshow_by_map(image, map_polygon)
draw_map(map_polygon, color='k', linewidth=1)
ax.set_extent(map_polygon.get_extent())

plt.show()
```

![](https://mmbiz.qpic.cn/mmbiz_png/KtLeyFG8WByBrNNlaHCntBDvpXaNWrohFIFg8THviajkB4wYV5LUicdzJQoYIKNSxpXibAj3JhL9SjuUj4jPHKSJd6SOP4IZo8bicWnpfzXHxGs/640?wx_fmt=png&from=appmsg)

## 4.同时查询多个边界的能力

在 `1.x` 版本中，查询边界数据只能一个一个地查询，如果要查多个地区就需要写循环，这并不符合程序员的优雅审美，于是在 `2.1` 版本中，我们增加了可以直接传入多个边界名称来一次性筛选出对应的边界数据的能力，从而避免重复循环，例如：

```
from cnmaps import get_adm_maps

jingjin = get_adm_maps(province=['北京市', '天津市'], level='省')
henan_cities = get_adm_maps(province='河南省', city=['郑州市', '洛阳市'], level='市')
east_asia = get_adm_maps(country=['中国', 'JPN', 'KOR'], level='国')
```

## 5.多边形中心点的获取

实际上这个功能之前 `1.x` 的版本理论上也支持，只不过并没有用一个更优雅的封装形式来暴露，目前最新的使用方法参考：

```
from cnmaps import get_adm_maps

china = get_adm_maps(country='中国', level='国', record='first')
print(china.longitude, china.latitude)

henan = get_adm_maps(province='河南省', record='first')
print(henan.longitude, henan.latitude)

nanyang = get_adm_maps(city='南阳市', record='first')
print(nanyang.longitude, nanyang.latitude)

haidian = get_adm_maps(district='海淀区', record='first')
print(haidian.longitude, haidian.latitude)
```

## 6.导出矢量文件的命令行

有时候用户其实并不需要 cnmaps 本身的画图功能，而只是想要这个包的矢量边界数据。现在我们已经实现了一个简单直接的命令行工具，不需要写代码和编程只需要敲一行命令就可以直接导出你需要的矢量边界，支持 shapefile 和 geojson 两种格式：

```
cnmaps export <output> [--country ...] [--province ...] [--city ...] [--district ...]
              [--level ...] [--source ...] [--provider ...] [--record {all,first}]
              [--engine ENGINE] [--encoding ENCODING] [--gcj02] [--simplify]
```

比如：

```
# 导出中国国家边界
$ cnmaps export china.shp --country 中国 --level 国 --record first

# 导出河南省级边界
$ cnmaps export china-provinces.geojson --province 河南省 --level 省

# 导出郑州市级边界
$ cnmaps export china-cities.shp --city 郑州市 --level 市
```

## 7.内置 AI Skill

这是我对 `2.1` 版本最新的一次尝试，在包里内置了 AI Skill 的定义，对于目前已经习惯于 vibe coding 工作模式的开发者来说，可以提供更好的 AI 支持。在安装了 `cnmaps >= 2.1` 版本之后，根据需要执行以下命令:

```
# 本地模式
$ cnmaps install-skill codex --mode local  # Codex 格式
$ cnmaps install-skill claudecode --mode local  # Claude Code 格式
$ cnmaps install-skill cursor --mode local # Cursor 格式（兼容 Claude Code 标准）
```

以上命令为“本地安装”模式，执行之后可以在当前目录生效，更换目录则无法识别需重新安装。如果要“全局安装”则按需执行以下命令：

```
# 全局模式
$ cnmaps install-skill codex --mode global  # Codex 格式
$ cnmaps install-skill claudecode --mode global  # Claude Code 格式
$ cnmaps install-skill cursor --mode global # Cursor 格式（兼容 Claude Code 标准）
```

当你安装之后，如果在对应软件的 Skill 列表里找到一个名为 `cnmaps-python-assistant` 的 Skill，则说明安装成功了，就可以直接指挥 AI 利用 cnmaps 的能力帮你写代码了，比如给 AI 发送：

```
帮我用 cnmaps 画一张全球国家的边界图。
```

目前这套 Skill 的定义仅支持 Codex、Claude Code、Cursor 以及兼容这三套标准（事实上可以认为是两套，因为 Cursor 目前完全兼容 Claude Code 标准）的其他 IDE。

## 8.支持自定义的矢量边界

之前有一个 Issue(#84) 提出希望可以读取自己自定义的 shapefile 文件来发挥 cnmaps 在图像处理方面的能力，但是由于2024年时期的技术水平，还难以实现让 cnmaps 很轻松地去兼容一套完全陌生的 shapefile 或 geojson 文件结构，因此这个 Issue 被长期搁置了下来。

而到了2026年的今天，受益于 AI 编程能力的大幅提升，这一需求的满足已经具有可行性。于是我就尝试开始解决这个问题，首先我制定了一个 shapefile/geojson 文件的内部架构标准，并集成在 Skill 的定义里，同时实现一个“检查工具”，用于判断该矢量文件是否达到了 cnmaps 可读的标准，最后实现一个函数读取符合可读标准的矢量文件。而至于如何把一个不符合标准的矢量数据文件转化为符合标准的数据文件，这就需要借助 AI 的编程能力了，因为 Skill 里定义了结构标准，AI 只要知道符合标准的文件是什么样的，就能自己想办法把用户自定义的 shapefile/geojson 转化为符合标准的结果供 cnmaps 读取。

比如当用户装好 Skill 之后，可以给 AI 发送这样一句提示词：

```
帮我把 <path/filename.shp> 转为符合 cnmaps 可识别格式的 shapefile/geojson 文件，并通过 cnmaps 的 check-boundary 检查。
```

当 AI 完成这项工作之后，理论上这个文件就可以读取和使用了，当然读取和画图也都可以让 AI 代劳。

## 写在最后

如果大家还有什么需求或者发现了什么 Bug，欢迎去 Github 仓库里提交 Issue，仓库地址：https://github.com/cnmetlab/cnmaps。另外更多的文档请参考官方文档：https://cnmaps.readthedocs.io/

另外打个广告，最近我们团队开发了一套气象数据查询网站，目前可以支持查询长周期的机场 METAR 报文数据、污染物历史数据以及单站天气雷达组合反射率的 NetCDF 格式数据，近期将继续上线基于国际交换站的长周期地面气象观测、探空和 DEM 数据集，欢迎大家访问：观天者数据站（该网站 Google 和 Bing 已收录可以搜索到，百度未收录无法搜到）。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/6ic2vGhXzWuSy7ULyQHzicfpCsunAxcFSdeE7ar1JQiceyhxibviaicSpeyAnaF0k1yxjAj2OsX31Gp2g5ZpNxhMp9iaw/0?wx_fmt=png)

Clarmy吱声

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/6ic2vGhXzWuSy7ULyQHzicfpCsunAxcFSdeE7ar1JQiceyhxibviaicSpeyAnaF0k1yxjAj2OsX31Gp2g5ZpNxhMp9iaw/0?wx_fmt=png)

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