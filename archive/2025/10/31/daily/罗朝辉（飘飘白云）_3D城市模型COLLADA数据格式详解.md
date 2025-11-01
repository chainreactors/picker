---
title: 3D城市模型COLLADA数据格式详解
url: https://blog.csdn.net/kesalin/article/details/154195093
source: 罗朝辉（飘飘白云）
date: 2025-10-31
fetch_date: 2025-11-01T03:11:11.100042
---

# 3D城市模型COLLADA数据格式详解

# 3D城市模型COLLADA数据格式详解

原创
已于 2025-10-31 17:39:57 修改
·
191 阅读

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Active.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/newHeart2023Black.png)

3

·
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollect2.png)
![](https://csdnimg.cn/release/blogv2/dist/pc/img/tobarCollectionActive2.png)

5
·

CC 4.0 BY-SA版权

版权声明：本文为博主原创文章，遵循 [CC 4.0 BY-SA](http://creativecommons.org/licenses/by-sa/4.0/) 版权协议，转载请附上原文出处链接和本声明。

文章标签：

[#3d](https://so.csdn.net/so/search/s.do?q=3d&t=all&o=vip&s=&l=&f=&viparticle=&from_tracking_code=tag_word&from_code=app_blog_art)

于 2025-10-31 17:38:16 首次发布

[![](https://i-blog.csdnimg.cn/columns/default/20201014180756913.png?x-oss-process=image/resize,m_fixed,h_224,w_224)

3D技术
专栏收录该内容](https://blog.csdn.net/kesalin/category_165386.html "3D技术")

22 篇文章

订阅专栏

## 3D城市模型COLLADA数据格式详解

### 1. 概述

本文档基于`3D`城市模型`COLLADA`数据规范（v1.8），结合旧金山（`San Francisco`）实际数据集，详细说明该数据格式的组织结构、文件命名规范、数据内容及使用方法。

#### 1.1 数据源

* **数据标准**: `COLLADA` 1.4.1
* **城市**: 美国加利福尼亚州旧金山

#### 1.2 数据特点

* 基于瓦片（Tile）的城市3D模型数据
* 包含建筑物、地形、道路、水体等城市要素
* 支持多细节层次（`LOD`）：LOW、STANDARD、HIGH
* 使用`PNG`纹理贴图
* 采用横轴墨卡托（Transverse Mercator）投影坐标系统

### 2. 目录结构

```
SAN_FRANCISCO/
├── CM_USA_CA_SAN_FRANCISCO_XXX_YYY_B2.DAE     # 边界元数据文件
├── CM_USA_CA_SAN_FRANCISCO_XXX_YYY_M.DAE      # 主模型数据文件
├── 3D_LANDMARKS/                              # 地标建筑目录
│   ├── [建筑名称]/
│   │   ├── LOW/                              # 低细节模型
│   │   │   ├── [建筑名称]_L.DAE
│   │   │   └── [建筑名称]_L.PNG
│   │   └── STANDARD/                         # 标准细节模型
│   │       ├── [建筑名称]_S.DAE
│   │       └── [建筑名称]_S.PNG
├── ASSETS/                                    # 辅助资产文件
│   ├── CM_USA_CA_SAN_FRANCISCO.csgis          # 压缩的GIS元数据（zlib格式）
│   ├── CM_USA_CA_SAN_FRANCISCO.dbf            # Shapefile数据库文件（dBASE格式）
│   ├── CM_USA_CA_SAN_FRANCISCO.plorg          # 压缩的数据组织信息（zlib格式）
│   ├── CM_USA_CA_SAN_FRANCISCO.prj            # 投影坐标系统定义（WKT格式）
│   ├── CM_USA_CA_SAN_FRANCISCO.shp            # Shapefile几何数据（ESRI格式）
│   └── CM_USA_CA_SAN_FRANCISCO.shx            # Shapefile索引文件
└── TEXTURES/                                  # 纹理资源目录
    └── HERE/
        ├── HIGH/                             # 高质量纹理
        ├── LOW/                              # 低质量纹理
        └── STANDARD/                         # 标准质量纹理
            └── DAY/
                ├── ARROWS/                   # 道路箭头标识
                ├── BUILDINGS/                # 建筑纹理
                │   ├── B2/                   # 二维建筑纹理（238张）
                │   ├── B3/                   # 三维建筑纹理（100张）
                │   └── COMMON/               # 通用纹理（屋顶等）
                └── OTHER/                    # 其他纹理（地形、道路等）
```

### 3. 文件命名规范

#### 3.1 瓦片文件命名

**格式**: `CM_[国家]_[州]_[城市]_XXX_YYY_[类型].DAE`

**示例**: `CM_USA_CA_SAN_FRANCISCO_000_000_M.DAE`

**字段说明**:

* `CM`: City Model（城市模型）
* `USA`: 国家代码（美国）
* `CA`: 州代码（加利福尼亚）
* `SAN_FRANCISCO`: 城市名称
* `XXX`: 瓦片X索引（3位数字，从000开始）
* `YYY`: 瓦片Y索引（3位数字，从000开始）
* `类型`:
  + `B2`: 二维边界数据文件
  + `M`: Main（主模型数据文件）
  + `S`: Spline（样条曲线文件，如道路中心线）

#### 3.2 瓦片网格系统

数据采用规则网格瓦片组织：

* **瓦片尺寸**: 400m × 400m
* **索引方式**: XXX（列）× YYY（行）
* **覆盖范围**: 旧金山数据集包含约8×16的瓦片网格

**示例瓦片索引**:

```
000_000 | 001_000 | 002_000 | ...
000_001 | 001_001 | 002_001 | ...
000_002 | 001_002 | 002_002 | ...
...
```

#### 3.3 地标建筑命名

**格式**: `[国家]_[州]_[城市]_[建筑名称]`

**示例**:

* `USA_CA_SANFRANCISCO_TRANSAMERICAPYRAMID` （泛美金字塔大厦）
* `USA_CA_SANFRANCISCO_COITTOWER` （科伊特塔）
* `USA_CA_SANFRANCISCO_FERRYBUILDING` （渡轮大厦）

**细节层次后缀**:

* `_L.DAE`: Low（低细节）
* `_S.DAE`: Standard（标准细节）

### 4. 文件类型详解

#### 4.1 B2文件（Building文件）

**用途**: 存储建筑物的边界信息和元数据

**内容**:

* 瓦片基本信息（瓦片ID、尺寸）
* 最小边界矩形（MBR）
* 投影坐标系统定义
* 地理坐标系统参数

**示例**: `CM_USA_CA_SAN_FRANCISCO_000_000_B2.DAE`

```
<visual_content_metadata
    tile_id="000_000"
    tile_width="400"
    tile_height="400"
    spline_curve_file="CM_USA_CA_SAN_FRANCISCO_000_000_S.DAE"
    dtm_integrated="false"/>
<minimum_bounding_rectangle
    XMax="-3635.11768"
    XMin="-4035.11768"
    YMax="-2799.99976"
    YMin="-3199.99976"/>
```

#### 4.2 M文件（主模型文件）

**用途**: 包含瓦片内的所有3D几何模型和场景数据

**内容**:

* 地形（TERRAIN）
* 道路（ROAD, feature\_type: 9999999）
* 水体（WATER, feature\_type: 507116）
* 人行横道（PEDESTRIAN\_CROSSWALK）
* 转向箭头标识（TURN\_ARROW\_DECAL）
* 植被覆盖（Grass, Park, feature\_type: 900150）
* 其他地物

**特点**:

* 包含完整的COLLADA库（images、effects、materials、geometries、visual\_scenes）
* 文件大小从几KB（空旷区域）到数MB（密集城区）
* 包含纹理引用和材质定义

#### 4.3 ASSETS文件（辅助资产文件）

ASSETS 目录包含城市模型的辅助元数据和空间索引文件：

##### 4.3.1 投影坐标系统文件

| 文件 | 格式 | 说明 |
| --- | --- | --- |
| `.prj` | WKT文本 | 投影坐标系统定义（Well-Known Text格式） |

**示例内容**（CM\_USA\_CA\_SAN\_FRANCISCO.prj）:

```
GEOGCS["GCS_WGS_1984",DATUM["D_WGS_1984",SPHEROID["WGS_1984",6378137.0,298.257223563]],PRIMEM["Greenwich",0.0],UNIT["Degree",0.0174532925199433]]
```

此文件定义了数据集使用的地理坐标系统（WGS 84）。

##### 4.3.2 Shapefile 文件组

| 文件 | 格式 | 说明 |
| --- | --- | --- |
| `.shp` | ESRI Shapefile | 存储几何图形（点、线、面） |
| `.shx` | Shapefile索引 | 加速空间查询的索引文件 |
| `.dbf` | dBASE III+ | 属性数据表 |

**用途**: 存储城市模型的边界多边形（Polygon）和相关属性。

**注意**: 旧金山数据集中的 Shapefile 仅包含 1 条记录，表示整个城市模型的外边界范围。

### 5. COLLADA文件结构

#### 5.1 基本结构

```
<?xml version="1.0" encoding="UTF-8"?>
<COLLADA xmlns="http://www.collada.org/2005/11/COLLADASchema" version="1.4.1">
    <asset>...</asset>                      <!-- 元数据 -->
    <library_images>...</library_images>    <!-- 图像库 -->
    <library_effects>...</library_effects>  <!-- 效果库 -->
    <library_materials>...</library_materials>  <!-- 材质库 -->
    <library_geometries>...</library_geometries>  <!-- 几何库 -->
    <library_visual_scenes>...</library_visual_scenes>  <!-- 场景库 -->
    <scene>...</scene>                      <!-- 场景实例 -->
    <extra>...</extra>                      <!-- 扩展信息 -->
</COLLADA>
```

#### 5.2 Asset节点（元数据）

```
<asset>
    <contributor>
        <author>HERE</author>
        <copyright>Copyright 2022 HERE</copyright>
    </contributor>
    <created>2022-04-08T23:49:00.0Z</created>
    <modified>2022-04-08T23:49:00.0Z</modified>
    <revision>1.4.1</revision>
    <unit/>
    <up_axis>Z_UP</up_axis>  <!-- Z轴向上 -->
</asset>
```

**关键字段**:

* `author`: 数据提供商（HERE）
* `created/modified`: 创建和修改时间（UTC格式）
* `up_axis`: 坐标系统上方向（Z\_UP表示Z轴向上）
* `unit`: 长度单位（米）

#### 5.3 Library\_images（图像库）

定义所有纹理图像资源：

```
<library_images>
    <image id="file-terrain_grass_color" name="file-terrain_grass_color">
        <init_from>./TEXTURES/HERE/HIGH/DAY/OTHER/USA_L_GRASS-COLOUR_5.PNG</init_from>
    </image>
    <image id="file-roads_street_solid" name="file-roads_street_solid">
        <init_from>./TEXTURES/HERE/HIGH/DAY/OTHER/USA_R_STREET-SOLID.PNG</init_from>
    </image>
    <!-- 更多图像... -->
</library_images>
```

**纹理路径格式**: `./TEXTURES/HERE/[质量]/DAY/[类别]/[文件名].PNG`

#### 5.4 Library\_effects（效果库）

定义材质的视觉效果（着色模型、纹理采样等）：

```
<effect id="terrain_grass_color-fx">
    <profile_COMMON>
        <newparam sid="file-terrain_grass_color-surface">
            <surface type="2D">
                <init_from>file-terrain_grass_color</init_from>
                <format>A8R8G8B8</format>  <!-- 32位ARGB格式 -->
            </surface>
        </newparam>
        <newparam sid="file-terrain_grass_color-sampler">
            <sampler2D>
                <source>file-terrain_grass_color-surface</source>
                <wrap_s>WRAP</wrap_s>       <!-- 水平环绕 -->
                <wrap_t>WRAP</wrap_t>       <!-- 垂直环绕 -->
                <minfilter>LINEAR_MIPMAP_LINEAR</minfilter>
                <magfilter>LINEAR</magfilter>
            </sampler2D>
        </newparam>
        <technique sid="common">
            <lambert>  <!-- Lambert着色模型 -->
                <emission><color>0 0 0 1</color></emission>
                <ambient><color>1 1 1 1</color></ambient>
                <diffuse>
                    <texture texture="file-terrain_grass_color-sampler" texcoord="TEX0"/>
                </diffuse>
            </lambert>
        </technique>
    </profile_COMMON>
</effect>
```

**着色模型**: 使用Lambert漫反射模型

#### 5.5 Library\_...