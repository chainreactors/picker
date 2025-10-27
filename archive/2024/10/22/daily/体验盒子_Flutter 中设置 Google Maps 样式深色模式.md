---
title: Flutter 中设置 Google Maps 样式深色模式
url: https://www.uedbox.com/post/69760/
source: 体验盒子
date: 2024-10-22
fetch_date: 2025-10-06T18:51:23.475852
---

# Flutter 中设置 Google Maps 样式深色模式

[![体验盒子](https://www.uedbox.com/wp-content/themes/UB2019/imgs/logo.png)](https://www.uedbox.com)

* [博文](https://www.uedbox.com/blog/ "博文")
* [设计开发](https://www.uedbox.com/design/ "设计开发")
* [网络安全](https://www.uedbox.com/web-security/ "网络安全")
* [观点](https://www.uedbox.com/entertainment/ "观点")
* [服务](https://www.uedbox.com/service/ "服务")
* [AI导航](https://www.uedbox.com/aihub/ "AI导航")
* 更多
  + [关于](https://www.uedbox.com/about/ "关于")
  + [分享](https://www.uedbox.com/share/ "分享")
  + [老电影](https://www.uedbox.com/movie/ "老电影")
  + [搜索语法/SHDB](https://www.uedbox.com/shdb/ "搜索语法/SHDB")
  + [Exploits](https://www.uedbox.com/exploits/ "Exploits")
  + [SecTools](https://www.uedbox.com/tools/ "SecTools")
  + [UserAgent解析](https://www.uedbox.com/useragentparser/ "UserAgent解析")
  + [地理坐标在线转换](https://www.uedbox.com/geocoordinate/ "地理坐标在线转换")

# Flutter 中设置 Google Maps 样式深色模式

* 发表于 2024年10月21日
* [flutter](https://www.uedbox.com/design/flutter/)

您是否希望通过引入更复杂的外观或将其与应用程序的整体主题无缝对齐来增强 Flutter 应用程序中 Google Maps 集成的外观？

新的插件版本将 *setMapStyle* 方法添加到 *GoogleMapController* 类中。此方法将自定义样式的 String 表示形式作为输入。为了以 JSON 格式创建此样式，Google 创建了一个方便的工具：<https://mapstyle.withgoogle.com/>。您可以使用任何预制的主题，也可以详细创建自己的样式。创建样式后，单击 **finish（完成**），然后您可以复制生成的 JSON。以下 JSON 表示将 water color 设置为 grey 并将 roads 设置为白色的简单样式

现在，您可以尝试将此 JSON 放在引号中，并将其直接提供给 *GoogleMapController*的 *setMapStyle* 方法。我将提出一种在我看来更方便的替代方法，将样式视为一种资产。

在本文中，我将展示完成此任务所涉及的步骤。

目录表

Toggle

* [创建您的Google Maps样式](#%E5%88%9B%E5%BB%BA%E6%82%A8%E7%9A%84Google_Maps%E6%A0%B7%E5%BC%8F)
* [使用 Styling Wizard 地图样式工具生成 Json](#%E4%BD%BF%E7%94%A8_Styling_Wizard_%E5%9C%B0%E5%9B%BE%E6%A0%B7%E5%BC%8F%E5%B7%A5%E5%85%B7%E7%94%9F%E6%88%90_Json)
* [导入样式](#%E5%AF%BC%E5%85%A5%E6%A0%B7%E5%BC%8F)
  + [<2.6.0 版本设置方法](#i)
  + [>=2.6.0 版本设置方法](#%3E260_%E7%89%88%E6%9C%AC%E8%AE%BE%E7%BD%AE%E6%96%B9%E6%B3%95)

## 创建您的Google Maps样式

有两种方法可以设置 Google 地图的样式：使用 [Styling Wizard](https://mapstyle.withgoogle.com/) 或使用 [Google Cloud Console](https://console.cloud.google.com/)。选择 Styling Wizard 时，该过程涉及导入包含样式要求的 JSON 信息。相反，Cloud Console 提供了一个用于创建和发布样式的平台，无缝反映应用程序中的更改。

由于可用的自定义选项众多，设置您的谷歌地图样式可能是一项有些艰巨的任务。

地图上的每个功能都可以通过更改
`几何图形`
或标签元素来自定义，而
`标签`
元素又可以通过
`填充`
或
`描边`
属性进行自定义，这些属性还具有单独的自定义选项，例如
`颜色`
和
`饱和度`
。

在这种情况下，一线希望是，当您进行这些自定义时，可以实时观察到更改。

![Flutter 中设置 Google Maps 样式深色模式](https://www.uedbox.com/wp-content/uploads/2024/10/styling-google-maps11.png)

## 使用 Styling Wizard 地图样式工具生成 Json

在本文中，我将向您展示如何使用 [Styling Wizard](https://mapstyle.withgoogle.com/)。使用 Styling Wizard 我最喜欢的一点是，有预先自定义的主题可供您使用或构建。例如，如果您想让 Google 地图与应用的夜间主题融为一体。您可以选择 Dark、Night 或 Aubergine 中的任何一个。

如前所述，您可以通过更改
`geometry`
 或
`label`
 元素的属性来完成您想要进行的自定义。完成并对结果感到满意后，单击 完成。

![Flutter 中设置 Google Maps 样式深色模式](https://www.uedbox.com/wp-content/uploads/2024/10/StylingWizard-2024-10-21-17.38.12.png)

之后，您应该在上面看到这一点，接下来是复制 JSON，这本质上是有关您所做的自定义的信息。

## 导入样式

接下来是打开你的 Flutter 项目，确保你已经将 [google\_maps\_flutter](https://pub.dev/packages/google_maps_flutter) 添加到你的项目中。

接下来，在 Flutter 项目的
`assets`
目录中创建一个名为
`map_styles.json`
的文件，并将 JSON 粘贴到其中。

然后将其添加到你项目的
`pubspec.yaml`
 文件中，

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | # The following section is specific to Flutter packages.  flutter:  uses-material-design: true    assets:  - assets/map\_style.json |

添加后，运行
`flutter pub get`
，以便 Flutter 知道这个新添加的资源。

首先，创建一个
`GoogleMapController`
 变量，该变量将提供对
`GoogleMap`
 小部件的访问，它将使您能够做各种有趣的事情，例如在本例中添加自定义地图样式。

### <2.6.0 版本设置方法

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19 | import 'package:flutter/services.dart' show rootBundle;  String \_mapStyle;    @override  void initState() {  super.initState();    rootBundle.loadString('assets/map\_style.txt').then((string) {  \_mapStyle = string;  });  }    GoogleMapController mapController;  GoogleMap(  onMapCreated: (GoogleMapController controller) {  mapController = controller;  mapController.setMapStyle(\_mapStyle);  }  ); |

### >=2.6.0 版本设置方法

新版本废弃了
`setMapStyle`
，而是在创建
`GoogleMap`
组件时直接指定
`style`
：

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13 | GoogleMap(  onMapCreated: \_onMapCreated,  initialCameraPosition: CameraPosition(  target: \_currentPosition,  zoom: 14.0,  ),  style: \_mapStyleString,  markers: \_markers,  myLocationEnabled: true,  myLocationButtonEnabled: false,  onCameraMove: \_onCameraMove,  onCameraIdle: \_updateMarkers,  ) |

在提供的代码片段中，
`GoogleMap`
 样式在
`onMapCreated`
 函数中设置，以保证在应用样式之前创建地图。

最后，运行您的代码，您应该会看到您的地图看起来不错。

点赞(1)

打赏

分享

标签：[flutter](https://www.uedbox.com/post/tag/flutter/) , [google](https://www.uedbox.com/post/tag/google/) , [google maps](https://www.uedbox.com/post/tag/google-maps/)  原文连接：**[Flutter 中设置 Google Maps 样式深色模式](https://www.uedbox.com/post/69760/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[解决WordPress上传svg/ico/webp，您无权上传此文件类型](https://www.uedbox.com/post/69734/ "解决WordPress上传svg/ico/webp，您无权上传此文件类型") [Mos macOS下平滑鼠标滚动/滚动方向小工具](https://www.uedbox.com/post/69767/ "Mos macOS下平滑鼠标滚动/滚动方向小工具")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![百度哥，全能的主](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

百度哥，全能的主](https://www.uedbox.com/post/1275/ "百度哥，全能的主")

[![每天更新的纯净版 Chromium OS 镜像下载](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

每天更新的纯净版 Chromium OS 镜像下载](https://www.uedbox.com/post/2382/ "每天更新的纯净版 Chromium OS 镜像下载")

[![在睡前感谢google](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

在睡前感谢google](https://www.uedbox.com/post/1298/ "在睡前感谢google")

[![本地管理 Google Docs 工具(iGoSyncDocs)](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

本地管理 Google Docs 工具(iGoSyncDocs)](https://www.uedbox.com/post/1791/ "本地管理 Google Docs 工具(iGoSyncDocs)")

[![测试版 Gmail for Android APK 安装包下载](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

测试版 Gmail for Android APK 安装包下载](https://www.uedbox.com/post/1815/ "测试版 Gmail for Android APK 安装包下载")

[![Google 发布新产品“Streaming”](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Google 发布新产品“Streaming”](https://www.uedbox.com/post/1828/ "Google 发布新产品“Streaming”")

[![AdSense 增加广告类别过滤器](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

AdSense 增加广告类别过滤器](https://www.uedbox.com/post/1514/ "AdSense 增加广告类别过滤器")

[![Google 将 Instantiations 制作的 JAVA 开发工具全部免费放出](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Google 将 Instantiations 制作的 JAVA 开发工具全部免费放出](https://www.uedbox.com/post/2018/ "Google 将 Instantiations 制作的 JAVA 开发工具全部免费放出")

[![Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Nginx 利用 fail2ban 自动封禁乱扫的 IP](https://www.uedbox.com/post/119731/ "Nginx 利用 fail2ban 自动封禁乱扫的 IP")

[![最新 绕过Cloudflare最佳实践](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

最新 绕过Cloudflare最佳实践](https://www.uedbox.com/post/119716/ "最新 绕过Cloudflare最佳实践")

[![NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

NinjiaTag，兼容Apple Find My网络的开源防丢神器](https://www.uedbox.com/post/119688/ "NinjiaTag，兼容Apple Find My网络的开源防丢神器")

[![好用的Mac清理卸载软件推荐](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

好用的Mac清理卸载软件推荐](https://www.uedbox.com/post/119673/ "好用的Mac清理卸载软件推荐")

[![AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

AutoGen Studio 容器化部署与维护指南](https://www.uedbox.com/post/119359/ "AutoGen Studio 容器化部署与维护指南")

[![肌理解剖师：中年人的小确幸](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

肌理解剖师：中年人的小确幸](https://www.uedbox.com/post/119356/ "肌理解剖师：中年人的小确幸")

[![🔥 最新免费域名资源大全 | 永久免费域名获取](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

🔥 最新免费域名资源大全 | 永久免费域名获取](https://www.uedbox.com/post/119352/ "🔥 最新免费域名资源大全 | 永久免费域名获取")

[![Cursor agent ask manual区别](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Cursor agent ask manual区别](htt...