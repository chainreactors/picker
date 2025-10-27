---
title: 使用 MediaQuery 和 LayoutBuilders 在 Flutter 中创建手机/平板电脑布局
url: https://www.uedbox.com/post/68695/
source: 体验盒子
date: 2023-01-19
fetch_date: 2025-10-04T04:18:08.565782
---

# 使用 MediaQuery 和 LayoutBuilders 在 Flutter 中创建手机/平板电脑布局

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

# 使用 MediaQuery 和 LayoutBuilders 在 Flutter 中创建手机/平板电脑布局

* 发表于 2023年01月18日
* [flutter](https://www.uedbox.com/design/flutter/)

本文将向您展示如何创建根据用户设备（手机或平板电脑）运行的布局。在这里，我们将创建两个 GridView，一个用于手机，另一个用于平板电脑。

![使用 MediaQuery 和 LayoutBuilders 在 Flutter 中创建手机/平板电脑布局](https://www.uedbox.com/wp-content/uploads/2023/01/phone-tablet-flutter.png)

让我们先创建返回两个 GridView 的函数。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41 | gridviewForPhone() {  return Padding(  padding: EdgeInsets.all(5.0),  child: GridView.count(  crossAxisCount: 2,  childAspectRatio: 1.0,  mainAxisSpacing: 4.0,  crossAxisSpacing: 4.0,  children: List.generate(100, (index) {  return Card(  child: Container(  alignment: Alignment.center,  color: Colors.red[100 \* (index % 9)],  child: Text('$index'),  ),  );  }),  ),  );  }    gridviewForTablet() {  return Padding(  padding: EdgeInsets.all(5.0),  child: GridView.count(  crossAxisCount: 4,  childAspectRatio: 1.0,  mainAxisSpacing: 4.0,  crossAxisSpacing: 4.0,  children: List.generate(100, (index) {  return Card(  child: Container(  alignment: Alignment.center,  color: Colors.green[100 \* (index % 9)],  child: Text('$index'),  ),  );  }),  ),  );  } |

在这里，Phone GridView 将每行显示 2 个单元格，而平板电脑将每行显示 4 个。

目录表

Toggle

* [使用 MediaQuery](#%E4%BD%BF%E7%94%A8_MediaQuery)
* [使用 LayoutBuilder](#%E4%BD%BF%E7%94%A8_LayoutBuilder)

## 使用 MediaQuery

首先，我们使用 MediaQuery 来确定布局。为此，我们将声明三个变量。
我们假设 600.0 作为平板电脑的边界。

|  |  |
| --- | --- |
| 1  2  3 | final double shortestSide = MediaQuery.of(context).size.shortestSide; // get the shortest side of device  final bool useMobileLayout = shortestSide < 600.0; // check for tablet  final Orientation orientation = MediaQuery.of(context).orientation; // get the orientation |

现在我们的构建方法将更改为

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15 | @override  Widget build(BuildContext context) {    final double shortestSide = MediaQuery.of(context).size.shortestSide; // get the shortest side of device  final bool useMobileLayout = shortestSide < 600.0; // check for tablet  final Orientation orientation = MediaQuery.of(context).orientation; // get the orientation    return Scaffold(  appBar: AppBar(  title: Text(widget.title),  ),  body: useMobileLayout  ? gridviewForPhone(orientation)  : gridviewForTablet(orientation),  ... |

现在我们将方法更改为

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | gridviewForPhone(Orientation orientation) {  ...  GridView.count(  crossAxisCount: orientation.portrait ? 2 : 4  ...  }    gridviewForTablet(Orientation orientation) {  ...  GridView.count(  crossAxisCount: orientation.portrait ? 4 : 6  } |

## 使用 LayoutBuilder

这是进行比较的示例

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8 | LayoutBuilder(  builder: (BuildContext context, BoxConstraints constraints) {  if (constraints.maxWidth < 600.0) {  return gridviewForPhone();  } else {  return gridviewForTablet();  }  }, |

为了简单起见，我们只是使用构建器约束检查设备的最大宽度。
因此，一旦您的设备超过 600.0 的最大宽度，可能在横向模式下它最终会显示平板电脑的 GridView。

完整[代码](https://bitbucket.org/vipinvijayan1987/tutorialprojects/raw/b756e01a99c7ba429f150e62988f280d380b2b71/FlutterTutorialProjects/flutter_demo1/lib/widgets/layout_builder/layout_builder.dart)。

点赞(1)

打赏

分享

标签：[flutter](https://www.uedbox.com/post/tag/flutter/)  原文连接：**[使用 MediaQuery 和 LayoutBuilders 在 Flutter 中创建手机/平板电脑布局](https://www.uedbox.com/post/68695/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[口才培养：超实用的采访技巧](https://www.uedbox.com/post/68691/ "口才培养：超实用的采访技巧") [自媒体短视频必备10个无版权免费图片/视频资源网站](https://www.uedbox.com/post/68698/ "自媒体短视频必备10个无版权免费图片/视频资源网站")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![‘AMapSearch-NO-IDFA’ uses the unencrypted ‘http’ protocol to transfer the Pod解决](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

‘AMapSearch-NO-IDFA’ uses the unencrypted ‘http’ protocol to transfer the Pod解决](https://www.uedbox.com/post/66472/ "‘AMapSearch-NO-IDFA’ uses the unencrypted ‘http’ protocol to transfer the Pod解决")

[![Flutter中使用16进制Hex颜色值](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Flutter中使用16进制Hex颜色值](https://www.uedbox.com/post/68812/ "Flutter中使用16进制Hex颜色值")

[![Flutter setState() called after dispose()内存泄露解决](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Flutter setState() called after dispose()内存泄露解决](https://www.uedbox.com/post/65064/ "Flutter setState() called after dispose()内存泄露解决")

[![解决could not find included file ‘Pods/Target Support Files/Pods-Runner/Pods-Runner](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

解决could not find included file ‘Pods/Target Support Files/Pods-Runner/Pods-Runner](https://www.uedbox.com/post/66960/ "解决could not find included file ‘Pods/Target Support Files/Pods-Runner/Pods-Runner")

[![Flutter使用JsBridge方式处理Webview与H5通信](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Flutter使用JsBridge方式处理Webview与H5通信](https://www.uedbox.com/post/69699/ "Flutter使用JsBridge方式处理Webview与H5通信")

[![Flutter动态权限方案之permission_handler](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Flutter动态权限方案之permission\_handler](https://www.uedbox.com/post/65424/ "Flutter动态权限方案之permission_handler")

[![卡在Running Gradle task ‘assembleTgRelease’.很久的解决方案](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

卡在Running Gradle task ‘assembleTgRelease’.很久的解决方案](https://www.uedbox.com/post/67823/ "卡在Running Gradle task ‘assembleTgRelease’.很久的解决方案")

[![macOS命令行创建Android模拟器](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

macOS命令行创建Android模拟器](https://www.uedbox.com/post/64969/ "macOS命令行创建Android模拟器")

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

[![Cursor agent ask manual区别](https:...