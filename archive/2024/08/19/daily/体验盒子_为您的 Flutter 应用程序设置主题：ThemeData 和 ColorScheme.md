---
title: 为您的 Flutter 应用程序设置主题：ThemeData 和 ColorScheme
url: https://www.uedbox.com/post/69692/
source: 体验盒子
date: 2024-08-19
fetch_date: 2025-10-06T18:03:29.699552
---

# 为您的 Flutter 应用程序设置主题：ThemeData 和 ColorScheme

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

# 为您的 Flutter 应用程序设置主题：ThemeData 和 ColorScheme

* 发表于 2024年08月18日
* [flutter](https://www.uedbox.com/design/flutter/)

在深入研究之前，我需要告诉你一些事情。在媒体和其他来源中有许多关于这个主题的文章，那么这篇文章的必要性是什么？

在本文中，我计划只关注
`ThemeData`
 小部件的关键点和我的开发经验中最常用的参数，您将获得有关每个参数如何在您的应用程序上执行操作的简要说明。

你好奇吗？继续阅读 🤗 。

目录表

Toggle

* [使用 ThemeData 的主要好处](#%E4%BD%BF%E7%94%A8_ThemeData_%E7%9A%84%E4%B8%BB%E8%A6%81%E5%A5%BD%E5%A4%84)
* [创建全局类](#%E5%88%9B%E5%BB%BA%E5%85%A8%E5%B1%80%E7%B1%BB)
* [ColorSheme](#ColorSheme)
* [创建 ThemeData](#%E5%88%9B%E5%BB%BA_ThemeData)
* [设置 ThemeData](#%E8%AE%BE%E7%BD%AE_ThemeData)

## 使用  `ThemeData`  的主要好处

**保持统一的外观和感觉：**定义一个
`ThemeData`
 对象，该对象封装应用的调色板、字体、形状和其他视觉元素。在所有屏幕上一致地应用此主题，确保具有凝聚力和可识别的品牌标识。

* 为不同的主题创建变体：为浅色和深色模式、应用部分或用户偏好设置定义多个 ThemeData 对象。
* **定义一次主题，并在任何地方使用它们：**无需手动为单个小部件设置视觉样式，而是在应用中应用适当的
  `ThemeData`
   样式。这样可以减少代码重复并简化维护。
* **集中控制和更新：**对
  `ThemeData`
   对象进行更改，这些更改会自动传播到整个应用中，从而确保一致性并减少重复编辑的需要。
* **创建可访问的变体：**为具有特定辅助功能需求的用户构建单独的
  `ThemeData`
   对象，例如为视障用户构建高对比度主题。**创建可访问的变体：**为具有特定辅助功能需求的用户构建单独的
  `ThemeData`
   对象，例如为视障用户构建高对比度主题。

那么，现在您已经熟悉
`了 ThemeData`
 它如何帮助您，那么如何在您的应用程序中实现它？请跟我😊在一起。

这是一个小指南，介绍如何在 Flutter 应用中为深色和浅色主题实现基本主题。

## 创建全局类

第一步是创建一个全局类，用于在应用程序中管理
`ThemeData`
。这包含一种使用
`ColorSheme`
 创建不同实例
`ThemeData`
 的方法。

|  |  |
| --- | --- |
| 1  2  3  4  5 | class GlobalThemData {  static ThemeData themeData(ColorScheme colorScheme, Color focusColor) {  return ThemeData(colorScheme: colorScheme, focusColor: focusColor);  }  } |

`focusColor`
 ：TextFields 和 TextFormField 等小部件使用此颜色来指示小部件具有主要焦点。

> > [**ColorSheme**](https://api.flutter.dev/flutter/material/ColorScheme-class.html) ：一组基于[材料规格](https://m3.material.io/styles/color/the-color-system/color-roles)的 30 种颜色，可用于配置大多数组件的颜色属性。

我们可以在本文后面更详细地讨论
`ColorSheme`
。

现在，我们可以创建可以直接从
`GlobalThemData`
 类访问的其他公共变量。

* **lightColorScheme**：包含浅色主题的
  `ColorSheme`
  。
* **darkColorScheme**：包含用于深色主题的
  `ColorSheme`
  。
* **lightThemeData**：保存浅色主题的
  `ThemeData`
  。
* **darkThemeData**：保存深色主题的
  `ThemeData`
  。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | class GlobalThemData {  static final Color \_lightFocusColor = Colors.black.withOpacity(0.12);  static final Color \_darkFocusColor = Colors.white.withOpacity(0.12);  static ThemeData lightThemeData = themeData(lightColorScheme, \_lightFocusColor);    static ThemeData darkThemeData = themeData(darkColorScheme, \_darkFocusColor);  static ThemeData themeData(ColorScheme colorScheme, Color focusColor) {  return ThemeData(colorScheme: colorScheme, focusColor: focusColor);  }  static const ColorScheme lightColorScheme = ColorScheme();  static const ColorScheme darkColorScheme = ColorScheme();  } |

如果你和我一起编码，你可能应该在
`ColorSheme（）`
 上收到一个必需的参数错误警告。

我们可以在下一步中修复此问题。

## ColorSheme

ColorSheme 中的颜色成对出现;第一个是颜色本身，第二个是可用于该颜色的颜色，例如文本和其他元素。

![为您的 Flutter 应用程序设置主题：ThemeData 和 ColorScheme](https://www.uedbox.com/wp-content/uploads/2024/08/1_lGY-8zc6x0fG-JCuO-5INA.webp)

这 10 种颜色对于为 Flutter ThemData 创建 ColorSheme 是必需的，每种颜色的值都是可选的。

* `primary`
   ：这是应用程序中最常用的颜色
* `onPrimary`
   ：此颜色用于为原色之上的元素着色，例如文本、图标等。
* `secondary`
   ：这定义了次要颜色，通常用于不太突出的元素，如滤镜芯片、切换按钮或背景元素，这些元素需要从主要颜色中脱颖而出，但又不能压倒它。
* `onSecondary`
   ：此颜色用于为辅助颜色顶部的元素着色。
* `error`
   ：这是用于错误消息或警报的颜色，例如闪烁的红灯表示问题。
* `onError`
   ：这是与
  `错误`
  颜色相配的文本颜色，例如红色符号上的白色文本，以便于阅读。
* `background`
   ：整个应用程序的主要背景色。可以将其视为放置所有其他 UI 元素的画布。
* `onBackground`
   ：此颜色用于在背景颜色之上为元素着色。
* `surface`
  ：用作提升的 UI 元素（如卡片、工作表、对话框等）的基色。
* `onSurface`
  ：用于在表面颜色之上为元素着色。

因此，我们可以按照如下方式设置
`lightColorScheme`
 和
`darkColorScheme`
 变量。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27 | static const ColorScheme lightColorScheme = ColorScheme(  primary: Color(0xFFB93C5D),  onPrimary: Colors.black,  secondary: Color(0xFFEFF3F3),  onSecondary: Color(0xFF322942),  error: Colors.redAccent,  onError: Colors.white,  background: Color(0xFFE6EBEB),  onBackground: Colors.white,  surface: Color(0xFFFAFBFB),  onSurface: Color(0xFF241E30),  brightness: Brightness.light,  );    static const ColorScheme darkColorScheme = ColorScheme(  primary: Color(0xFFFF8383),  secondary: Color(0xFF4D1F7C),  background: Color(0xFF241E30),  surface: Color(0xFF1F1929),  onBackground: Color(0x0DFFFFFF),  error: Colors.redAccent,  onError: Colors.white,  onPrimary: Colors.white,  onSecondary: Colors.white,  onSurface: Colors.white,  brightness: Brightness.dark,  ); |

因此，到目前为止，我们为浅色和深色主题设置了
`ColorScheme`
，现在我们如何在
`ThemeData`
 中使用它？

## 创建 ThemeData

我们需要在
`GlobalThemeData`
 中修改我们的
`themeData`
 方法，以使用将传递给它的适当值
`ColourScheme`
 构建
`ThemeData`
。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9 | static ThemeData themeData(ColorScheme colorScheme, Color focusColor) {  return ThemeData(  colorScheme: colorScheme,  canvasColor: colorScheme.background,  scaffoldBackgroundColor: colorScheme.background,  highlightColor: Colors.transparent,  focusColor: focusColor  );  } |

* `canvasColor`
  ：这是整个屏幕或应用窗口的背景颜色。它定义了放置所有其他 UI 元素的基色。
* `scaffoldBackgroundColor`
  ：这专门定义基架本身的背景颜色，包括应用栏、正文内容区域和底部导航栏（如果存在）。
* `highlightColor`
  ：此属性定义当用户点击并按住小组件时短暂显示的颜色。它向用户提供视觉反馈，表明交互已注册。
* `focusColor`
  ：此属性定义用于直观地指示当前具有焦点的元素的颜色，这意味着它是将接收键盘输入的元素。这对于突出显示当前活动的元素，将用户的注意力吸引到它上面非常有用。

这些只是示例，您需要探索
`ThemeData`
 上的大量其他选项。

因此，我们最终的
`GlobalThemeData`
 类应如下所示：

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38  39  40  41  42  43 | class GlobalThemData {  static final Color \_lightFocusColor = Colors.black.withOpacity(0.12);  static final Color \_darkFocusColor = Colors.white.withOpacity(0.12);    static ThemeData lightThemeData =  themeData(lightColorScheme, \_lightFocusColor);  static ThemeData darkThemeData = themeData(darkColorScheme, \_darkFocusColor);  static ThemeData themeData(ColorScheme colorScheme, Color focusColor) {  return ThemeData(  colorScheme: colorScheme,  canvasColor: colorScheme.background,  scaffoldBackgroundColor: colorScheme.background,  highlightColor: Colors.transparent,  focusColor: focusColor  );  }  static const ColorScheme lightColorScheme = ColorScheme(  primary: Color(0xFFB93C5D),  onPrimary: Colors.black,  secondary: Color(0xFFEFF3F3),  onSecondary: Color(0xFF322942),  error: Colors.redAccent,  onError: Colors.white,  background: Color(0xFFE6EBEB),  onBackground: Colors.white,  surface: Color(0xFFFAFBFB),  onSurface: Color(0xFF241E30),  brightness: Brightness.light,  );  static const ColorScheme darkColorScheme = ColorScheme(  primary: Color(0xFFFF8383),  secondary: Color(0xFF4D1F7C),  background: Color(0xFF241E30),  surface: Color(0xFF1F1929),  onBackground: Color(0x0DFFFFFF),  error: Colors.redAccent,  onError: Colors.white,  onPrimary: Colors.white,  onSecondary: Colors.white,  onSurface: Colors.white,  brightness: Brightness.dark,  );  } |

是的！我们刚刚为我们的应用程序创建了一个漂亮的主题。现在怎么办？

## 设置 ThemeData

在
`MaterialApp`
 中设置所需的主题。

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14 | class MyApp extends StatelessWidget {  const MyApp({super.key});  @override  Widget build(BuildContext context) {  return MaterialApp(  debugShowCheckedModeBanner: false,  title: ...