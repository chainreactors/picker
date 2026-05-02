---
title: 一个定向窃取航空与关基GIS核心数据的黑客组织
url: https://mp.weixin.qq.com/s/Kvst_8zxOdxVhpDbYaPuGw
source: Doonsec's feed
date: 2026-05-01
fetch_date: 2026-05-02T04:54:29.800626
---

# 一个定向窃取航空与关基GIS核心数据的黑客组织

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDq7wvkcGttHrqSib8D0ddEYUq8Gs4pkk5iaiaLDCYVrNEEJvEd5YM2YZWyFjz8ibB9KUia3GcwBGibtgwCAdKk5JztL74qCGRpTPNm14/0?wx_fmt=jpeg)

# 一个定向窃取航空与关基GIS核心数据的黑客组织

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

2026 年 4 月，卡巴斯基发布最新威胁报告，披露了黑客组织HeartlessSoul针对航空工业及关键基础设施的持续攻击活动。

该组织自 2025 年 9 月起活跃，核心目标包括俄罗斯政府机构、工业企业、航空系统厂商及普通个人用户。

其攻击手段融合传统钓鱼、恶意广告与开源平台投毒，最终部署一套功能完备的JavaScript木马，可实现全维度数据窃取与系统控制，该组织的基础设施与APT组织GOFFEE存在明显重叠，两者可能存在协同攻击行为。

HeartlessSoul 采用多向量攻击策略，通过三种主流途径完成初始入侵，覆盖不同使用习惯的受害者群体。

### 钓鱼邮件：利用 LNK 漏洞隐藏恶意命令

攻击者发送携带恶意附件的钓鱼邮件，附件为包含 XLL、MSI 或 LNK 文件的压缩包。受害者解压并打开文件后，会自动触发恶意代码执行。

其中部分 LNK 文件利用了漏洞 ZDI-CAN-25373。该漏洞允许攻击者在快捷方式路径后添加大量空格或换行符，使 Windows 资源管理器仅显示路径的前半部分，从而隐藏后续的恶意 PowerShell 命令。所有恶意 LNK 文件均包含混淆后的 PowerShell 指令，核心逻辑为从 C2 服务器下载并执行后续载荷。

完整的初始感染链如下：

1. 受害者打开 LNK 文件，执行隐藏的 PowerShell 命令
2. PowerShell 自动下载并安装 Node.js 运行环境至用户本地目录

   ![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDr86BVicjeEQ5UOWfRrNTNYicTYficc2gKVUr89lu2X5LNRbtQmyFQHKCsEbATjsxCALoSGkrdz8AekPnNHRianryLU8MOCp3uEGJE/640?wx_fmt=png&from=appmsg)
3. 从 C2 服务器下载 JavaScript 加载器 index.js
4. 通过 node.exe 执行 index.js，完成初始加载

###

### 恶意广告：伪装航空专业软件

攻击者注册大量模仿航空主题的虚假域名，搭建高仿软件下载站，通过恶意广告引流目标用户。例如域名 battleflight.pro 提供伪装的飞行控制软件安装包 BattleFlight-Installer.exe。

该安装包运行后会在本地创建 helper.vbs 和 run-script.ps1 两个文件，通过 VBS 脚本调用 PowerShell，最终下载并执行 index.js 加载器，与钓鱼邮件的后续感染链完全一致。

### 开源平台投毒：SourceForge 上的恶意 GearUP

攻击者还利用知名开源平台 SourceForge 传播恶意代码。他们创建了伪装成游戏网络优化工具 GearUP 的虚假项目，上传恶意压缩包 GearUP-2.54.1-win.zip（MD5：b0a16ffa175f8273d71e2abd5d180593）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDrXuCNDZBaTqpVyJ9WTkumW1IGetJEK9iayzLSEibaCEyyCESdSbkJahibNdahKu6ETice8YqkGsYqOwlT1j1hfaRj73fYnRbUkvh8/640?wx_fmt=png&from=appmsg)

压缩包内包含 MSI 安装文件 GearUP-2.54.1-win.msi，安装时会自动执行内置的 install.ps1 脚本。该脚本同样会安装 Node.js 并加载 index.js，完成系统感染。截至 2025 年 12 月，该恶意包已被下载 74 次。

## 全内存加载：JavaScript 加载器的隐蔽持久化

初始感染阶段下载的 index.js 是经过高度混淆的 JavaScript 加载器，负责完成持久化部署与核心 RAT 载荷的加载。其设计注重隐蔽性与抗检测能力，核心功能包括以下几点。

### 双模式 C2 地址解析

###

加载器支持两种 C2 地址获取方式，提升攻击基础设施的生存能力：

1. 优先读取系统环境变量 SNS\_DOMAIN，通过 Solana Name Service（SNS）解析获取备用 C2 地址
2. 若解析失败，则使用硬编码在代码中的默认 C2 域名

**Solana 是一条公链，是一个开源的、去中心化的区块链网络，支持智能合约和去中心化应用（DApp）。SNS 是 Solana 上的 “域名系统”，类似于互联网的 DNS（把**`google.com` 解析为 IP 地址），SNS 把人类可读的域名（如 `malicious.sol`）解析为链上地址或其他数据。

这种基于区块链域名服务的解析机制，使得传统的域名黑名单防护手段难以完全阻断攻击通信。

HeartlessSoul 使用的 C2 域名主要通过 Tucows Domains Inc. 注册，服务器分布在多个国家的虚拟专用服务器上。攻击者注册了大量模仿合法服务的虚假域名用于传播恶意软件。

###

### 基础监控与信息收集功能

###

**screenshot**

捕获整个屏幕截图，转换为 Base64 编码后回传 C2 服务器。实现时会先调用 Windows API 设置进程 DPI 感知，确保截图完整

**clip**

实时监控系统剪贴板内容，每 3 秒检查一次，当检测到新的文本内容且长度不超过 12 个单词时，立即回传数据

**keylogger**

启动键盘记录器，记录所有按键操作。相关 PowerShell 代码从 C2 服务器动态加载

**get-meta**

收集系统详细信息，包括用户名、主机名、操作系统版本、CPU 与内存参数、域名信息、用户权限与 UAC 设置，以 JSON 格式发送至 C2

**get-location**

调用 Windows 地理位置 API 获取设备的经纬度坐标

###

### 专项数据窃取功能

###

这是 HeartlessSoul 攻击的核心目标，尤其针对航空与工业领域的敏感数据。

1. **通用文件窃取（FileUploadingCommand）**自动扫描本地磁盘，窃取以下扩展名的文件：

   办公文档：doc、docx、xls、xlsx、ppt、pptx、odt、ods、odp、pdf、txt、rtf

   压缩包：zip、rar、7z、cab

   地理信息系统（GIS）文件：kml、kmz、gpx、shp、dbf、geojson、mxd、qgs、qgz、dem、tif、tiff、img

   .kml、.kmz、.gpx — GPS 数据与地图文件

   .shp、.dbf — GIS shapefile 文件（用于制图系统）

   .geojson — JSON 格式的地理数据

   .mxd — ArcGIS 地图文档

   .qgs、.qgz — QGIS 项目文件

   .dem — 数字高程模型

   .tif、.tiff、.img — 常用于存储地理空间栅格图像

   配置文件：conf、set、ldk、csv

   其中 GIS 文件是攻击者的重点目标，这类文件包含道路、工程管网、地形地貌及战略设施的地理数据，对航空与工业企业具有极高的机密价值。
2. **浏览器数据窃取（BrowserCommand）**针对 Google Chrome、Microsoft Edge、Yandex Browser 与 Opera 浏览器，窃取以下数据：网络 Cookie 文件Local State 文件（包含浏览器主密钥加密信息）Local Storage 目录下的 leveldb 数据库

   攻击者还会下载.NET 工具 ArtifactsCollector.exe（内部名称 GetCookiesKey.exe），用于解密浏览器的主密钥，保存为 master\_key.txt 后回传。
3. **即时通讯与邮件数据窃取**

   **TelegramCommand**

   复制 Telegram Desktop 的 tdata 目录，打包后上传至 C2 服务器

   **dump-outlook**

   导出 Outlook 邮箱的所有本地数据

### GIS（地理信息系统），Geographic Information System，是一种采集、存储、管理、分析、显示与应用地理空间数据的计算机系统。

它将地理空间坐标与属性数据（如名称、类型、参数）深度绑定，实现对现实世界地理实体的数字化建模与空间分析。

**用途为航空领域用于机场规划、航线设计、导航系统建设；工业领域用于油气管道、电力电网、水利工程的全生命周期管理；国防领域用于战场环境分析、军事设施部署。**

HeartlessSoul 组织将其作为首要目标，本质是瞄准了地理数据的**战略级价值，**这些数据可直接转化为对关键基础设施的精确打击能力，威胁国家国土安全与经济命脉。

矢量数据用点、线、面等几何元素表示地理实体，具有精度高、数据量小、便于编辑分析的特点，是 GIS 中最核心的数据类型。

### 1. shp（Shapefile）

**定义**：ESRI 公司开发的行业标准矢量数据格式，由.shp（几何数据）、.shx（索引数据）、.dbf（属性数据）等多个配套文件组成。**典型存储内容**：

* 航空：机场跑道、滑行道、停机坪的精确坐标与尺寸，导航台站、信标机的位置，航线的走向与拐点
* 工业：油气管道、电力线路、通信光缆的精确走向与埋深，泵站、变电站、阀门室的位置
* 政府：军事禁区、涉密单位的边界，应急避难场所、物资储备库的分布**风险隐患**：这是 HeartlessSoul 最优先窃取的文件格式。精确的矢量坐标可让攻击者实现**厘米级定位**，例如：用无人机携带爆炸物精准打击机场跑道的关键起降段；找到油气管道的薄弱焊缝位置进行破坏；规划避开监控的入侵路线进入涉密设施。

### 2. dbf（dBase 数据库文件）

###

Shapefile 的配套文件，用于存储与几何数据对应的属性信息，是矢量数据的 "说明书"。

**存储有道路的名称、宽度、等级；管道的材质、管径、输送介质、建设时间；建筑物的高度、用途、承重能力。**

单独的几何坐标只能告诉攻击者 "哪里有什么"，而 dbf 文件能告诉攻击者 "它是什么、有多脆弱"。

例如：知道某段输油管道是老旧的铸铁管且已运行 30 年，攻击者可针对性选择破坏点，造成最大规模的泄漏事故；知道某变电站的供电范围覆盖整个航空工业区，可通过破坏它导致整个区域瘫痪。

### 3. kml/kmz（Keyhole 标记语言）

Google 开发的基于 XML 的地理数据格式，kmz 是 kml 的压缩版本，主要用于在 Google Earth 等地图软件中展示地理数据。

**存储内容为**无人机的飞行航线与任务区域、航空测绘的航迹、地标点的详细描述、应急疏散路线。**风险隐患**：在航空领域，kml 文件常被用于存储**无人机任务计划**。

一旦泄露，攻击者可完全掌握无人机的飞行时间、路线、侦察目标，甚至可以干扰或劫持无人机；在军事领域，kml 文件可能包含军事演习的区域划分、火力点位置等机密信息。

### 4. gpx（GPS 交换格式）

基于 XML 的 GPS 数据交换格式，用于存储 GPS 设备采集的轨迹、航点、路线数据。

**存储内容为**车辆行驶轨迹、无人机飞行轨迹、人员巡逻轨迹、测绘人员的外业采集路线。

gpx 文件泄露会暴露目标的**活动规律**。例如：获取关键设施安保人员的巡逻轨迹，可找到巡逻的时间间隙进行入侵；获取测绘车辆的行驶路线，可推断出正在进行的涉密测绘项目的范围与内容。

GIS 工程文件本身不存储原始地理数据，但包含了所有数据的组织方式、连接关系与显示配置，是攻击者定位高价值数据的 "导航图"。

### 1. mxd（ArcGIS 工程文件）

ESRI ArcGIS Desktop 软件的地图文档格式，是目前行业内应用最广泛的 GIS 项目文件。

**存储内容为**地图的图层结构、数据连接路径、符号样式、标注规则、布局模板、空间分析工具的参数设置。

mxd 文件会暴露整个 GIS 项目的**数据资产清单**。攻击者可通过分析 mxd 文件，快速识别出哪些图层包含敏感数据（如 "军事禁区边界"、"油气管道走向"），以及这些数据存储在哪个服务器、哪个数据库中。这能大幅提高数据窃取的效率，避免盲目扫描。

### 2. qgs/qgz（QGIS 工程文件）

开源 GIS 软件 QGIS 的项目文件格式，qgs 是文本格式，qgz 是压缩格式。

**存储内容为**与 mxd 文件类似，包含图层设置、数据连接、符号样式、分析模型等。

与 mxd 文件风险完全一致。由于 QGIS 是开源软件，在中小企业和科研机构中应用广泛，这些单位的安全防护能力通常较弱，更容易成为 HeartlessSoul 组织的攻击目标。

此外栅格数据由像素矩阵组成，每个像素代表一个地理区域的属性值，适合表示地形、影像等连续的地理现象。

### 1. dem（数字高程模型）

Digital Elevation Model，通过有序数值阵列模拟地面地形的高程数据，是对地表形态的数字化表达。

**应用于**地形分析、坡度坡向计算、通视分析、流域分析、三维建模、无人机地形匹配导航。

高精度 DEM 数据（分辨率 1 米及以上）泄露是**极其严重的国家安全事件**。攻击者可利用 DEM 数据：

* 进行通视分析，找到军事设施的最佳观察点和打击点
* 规划无人机的超低空突防路线，避开雷达探测
* 分析水利大坝的地形条件，计算溃坝后的洪水淹没范围
* 设计针对山区油气管道的破坏方案，利用地形放大灾害影响

### 2. tif/tiff（标签图像文件格式）

一种通用的位图格式，在 GIS 领域主要用于存储遥感影像、航空摄影像片、扫描地图等栅格数据。

**存储内容为**卫星遥感影像、航空摄影测量像片、数字化的纸质地形图、正射影像图。

高分辨率遥感影像（分辨率 0.5 米及以下）可清晰显示地面目标的细节。例如：识别机场停机坪上的飞机型号与数量；观察军事基地的车辆调动与设施建设；查看关键基础设施的安保布局与薄弱环节。HeartlessSoul 组织窃取这些数据后，可对目标进行**非接触式的详细侦察**。

### 3. img（ERDAS 影像文件）

ERDAS IMAGINE 遥感图像处理软件的专用栅格格式，常用于存储多光谱、高光谱遥感影像。

**存储内容为**多光谱卫星影像、高光谱航空影像、雷达影像。

高光谱影像可识别地面物体的材质与成分，探测普通光学影像无法发现的目标。例如：识别伪装的军事设施；探测地下油气管道的泄漏点；分析土壤的成分与湿度。这些数据在军事和工业领域具有极高的情报价值。

### GeoJSON

基于 JSON 的轻量级地理数据交换格式，支持点、线、面等几何类型，广泛用于 Web GIS 和移动应用。

**典型应用为**Web 地图服务、移动 GIS 应用、不同系统间的数据交换。**风险**

**与 shp 文件类似，GeoJSON 包含地理实体的精确坐标与属性信息。由于它是纯文本格式，无需专用软件即可打开和解析，攻击者可快速提取其中的敏感数据。此外，Web 应用中使用的 GeoJSON 文件常存在未授权访问漏洞，容易被攻击者批量爬取。**

HeartlessSoul 组织专门针对上述所有 GIS 文件格式设计窃取逻辑，绝非偶然。这些数据共同构成了一个**完整的数字孪生地球**，从宏观的地形地貌到微观的设施细节，从静态的地理实体到动态的活动轨迹，无所不包。一旦这些数据落入敌对势力或恐怖组织手中，将直接威胁：

**国土安全**

军事设施暴露、边境防线被突破、导弹打击精度大幅提升

**关键基础设施安全**

油气管道、电力电网、水利大坝等被精准破坏

**航空安全**

机场被袭击、无人机被劫持、航班飞行计划泄露

**经济安全**

工业生产瘫痪、能源供应中断、重大工程项目受阻

这也是为什么 GIS 数据安全已成为当前网络空间安全的核心战场之一。

参考链接:

https://securelist.ru/tr/heartlesssoul-campaign-javascript-rat/115376/

往期:[国际刑警DDoS蜜罐意外曝光：安全研究员意外逼停执法行动](https://mp.weixin.qq.com/s?__biz=MzAxOTM1MDQ1NA==&mid=2451186588&idx=1&sn=3e514339e3d45c42a379538fe33bd556&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ibO9kiauylaDqicDvERLTuy6Yo2PUS5sCSLCWBlXcichCYke51phlZqJvemVicckicq5cDX67WMuDvDmWX3HQaiaFCeKnMRuEVv2jsQCv90kc27HwE/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cnIDqLXBbescHHicaricGUU0tHjJ4BqISKw/0?wx_fmt=png)

黑鸟

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/V9abY6oHTkqrJPe3BMSmUuUaQMPJDnWTSrtbtXBAZSMfj0iaxiaMvM6cn...