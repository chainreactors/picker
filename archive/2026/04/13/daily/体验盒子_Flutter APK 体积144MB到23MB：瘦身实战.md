---
title: Flutter APK 体积144MB到23MB：瘦身实战
url: https://www.uedbox.com/post/119797/
source: 体验盒子
date: 2026-04-13
fetch_date: 2026-04-14T04:44:31.596029
---

# Flutter APK 体积144MB到23MB：瘦身实战

[![体验盒子](https://www.uedbox.com/wp-content/themes/UB2019/imgs/logo.png)](https://www.uedbox.com)

* [博文](https://www.uedbox.com/blog/ "博文")
* [设计开发](https://www.uedbox.com/design/ "设计开发")
* [网络安全](https://www.uedbox.com/web-security/ "网络安全")
* [观察](https://www.uedbox.com/entertainment/ "观察")
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

# Flutter APK 体积144MB到23MB：瘦身实战

* 发表于 2026年04月13日
* [flutter](https://www.uedbox.com/design/flutter/)

> 本文记录了一个真实 Flutter 项目（含 MediaKit 视频播放器、QuickJS 引擎、InAppWebView 等重量级插件）从 144MB 优化到 23MB 的全过程，涵盖 AGP 压缩策略、ABI 分包、代码混淆、Dart AOT 分析等多个维度。

目录表

Toggle

* [背景](#%E8%83%8C%E6%99%AF)
* [TL;DR 优化效果](#TLDR_%E4%BC%98%E5%8C%96%E6%95%88%E6%9E%9C)
* [第一刀：单 ABI 构建（-97MB）](#%E7%AC%AC%E4%B8%80%E5%88%80%EF%BC%9A%E5%8D%95_ABI_%E6%9E%84%E5%BB%BA%EF%BC%88-97MB%EF%BC%89)
  + [问题](#%E9%97%AE%E9%A2%98)
  + [方案：通过 --target-platform 指定单 ABI](#%E6%96%B9%E6%A1%88%EF%BC%9A%E9%80%9A%E8%BF%87_-target-platform_%E6%8C%87%E5%AE%9A%E5%8D%95_ABI)
* [第二刀：恢复代码混淆（-2.9MB）](#%E7%AC%AC%E4%BA%8C%E5%88%80%EF%BC%9A%E6%81%A2%E5%A4%8D%E4%BB%A3%E7%A0%81%E6%B7%B7%E6%B7%86%EF%BC%88-29MB%EF%BC%89)
  + [问题](#%E9%97%AE%E9%A2%98-2)
  + [验证：Flutter Gradle 插件确实读取此属性](#%E9%AA%8C%E8%AF%81%EF%BC%9AFlutter_Gradle_%E6%8F%92%E4%BB%B6%E7%A1%AE%E5%AE%9E%E8%AF%BB%E5%8F%96%E6%AD%A4%E5%B1%9E%E6%80%A7)
  + [方案：使用标准 Gradle 属性](#%E6%96%B9%E6%A1%88%EF%BC%9A%E4%BD%BF%E7%94%A8%E6%A0%87%E5%87%86_Gradle_%E5%B1%9E%E6%80%A7)
* [第三刀：GBK 映射表去重（-1.1MB）](#%E7%AC%AC%E4%B8%89%E5%88%80%EF%BC%9AGBK_%E6%98%A0%E5%B0%84%E8%A1%A8%E5%8E%BB%E9%87%8D%EF%BC%88-11MB%EF%BC%89)
  + [问题](#%E9%97%AE%E9%A2%98-3)
  + [方案](#%E6%96%B9%E6%A1%88)
* [第四刀：关键转折——useLegacyPackaging（-19.4MB）](#%E7%AC%AC%E5%9B%9B%E5%88%80%EF%BC%9A%E5%85%B3%E9%94%AE%E8%BD%AC%E6%8A%98%E2%80%94%E2%80%94useLegacyPackaging%EF%BC%88-194MB%EF%BC%89)
  + [问题定位](#%E9%97%AE%E9%A2%98%E5%AE%9A%E4%BD%8D)
  + [根因](#%E6%A0%B9%E5%9B%A0)
  + [方案](#%E6%96%B9%E6%A1%88-2)
  + [效果](#%E6%95%88%E6%9E%9C)
  + [兼容性评估](#%E5%85%BC%E5%AE%B9%E6%80%A7%E8%AF%84%E4%BC%B0)
  + [选择策略建议](#%E9%80%89%E6%8B%A9%E7%AD%96%E7%95%A5%E5%BB%BA%E8%AE%AE)
* [第五刀：highlight 按需导入（-0.4MB）](#%E7%AC%AC%E4%BA%94%E5%88%80%EF%BC%9Ahighlight_%E6%8C%89%E9%9C%80%E5%AF%BC%E5%85%A5%EF%BC%88-04MB%EF%BC%89)
  + [问题](#%E9%97%AE%E9%A2%98-4)
  + [方案](#%E6%96%B9%E6%A1%88-3)
* [附：如何分析你的 Flutter APK 体积](#%E9%99%84%EF%BC%9A%E5%A6%82%E4%BD%95%E5%88%86%E6%9E%90%E4%BD%A0%E7%9A%84_Flutter_APK_%E4%BD%93%E7%A7%AF)
  + [方法一：Flutter 官方 --analyze-size](#%E6%96%B9%E6%B3%95%E4%B8%80%EF%BC%9AFlutter_%E5%AE%98%E6%96%B9_-analyze-size)
  + [方法二：Python 脚本分析 APK 压缩状况](#%E6%96%B9%E6%B3%95%E4%BA%8C%EF%BC%9APython_%E8%84%9A%E6%9C%AC%E5%88%86%E6%9E%90_APK_%E5%8E%8B%E7%BC%A9%E7%8A%B6%E5%86%B5)
  + [方法三：解析 --analyze-size JSON 各包体积](#%E6%96%B9%E6%B3%95%E4%B8%89%EF%BC%9A%E8%A7%A3%E6%9E%90_-analyze-size_JSON_%E5%90%84%E5%8C%85%E4%BD%93%E7%A7%AF)
* [最终 APK 组成](#%E6%9C%80%E7%BB%88_APK_%E7%BB%84%E6%88%90)
* [libapp.so 内部各包体积 Top 15](#libappso_%E5%86%85%E9%83%A8%E5%90%84%E5%8C%85%E4%BD%93%E7%A7%AF_Top_15)
* [总结：优化检查清单](#%E6%80%BB%E7%BB%93%EF%BC%9A%E4%BC%98%E5%8C%96%E6%A3%80%E6%9F%A5%E6%B8%85%E5%8D%95)

## 背景

项目是一个多功能影视聚合应用，技术栈：

* **Flutter 3.35.0** / Dart 3.9.0
* **MediaKit**（libmpv 视频播放）、**QuickJS**（JS 引擎）、**InAppWebView**
* **AGP 8.6.1** / Kotlin 2.1.0 / Gradle 8.11.1
* 目标：通过 OTA 和仓库分发 APK

某次升级 AGP 和 Kotlin 版本后，APK 从 **~25MB 暴涨到 ~47MB**——几乎翻倍。排查发现问题并非代码膨胀，而是 **一个被忽视的 native library 压缩策略变更**。

## TL;DR 优化效果

| 阶段 | APK 大小 | 节省 |
| --- | --- | --- |
| 初始（3 ABI 全包） | 144.3 MB | — |
| 单 ABI 构建 | 46.9 MB | -97.4 MB |
| 恢复代码混淆 | 44 MB | -2.9 MB |
| GBK 映射表去重 | 42.9 MB | -1.1 MB |
| **启用 useLegacyPackaging** | **23.5 MB** | **-19.4 MB** |
| highlight 按需导入 | **23.1 MB** | -0.4 MB |

## 第一刀：单 ABI 构建（-97MB）

Flutter 默认构建包含多个 CPU 架构的 native 库。对于 APK 直接分发场景，没必要把三种架构塞进同一个包。

### 问题

|  |  |
| --- | --- |
| 1  2  3  4 | <em># 默认构建会包含 armeabi-v7a + arm64-v8a + x86\_64</em>  flutter build apk --release  <em># 输出：144.3 MB</em> |

### 方案：通过  `--target-platform`  指定单 ABI

|  |  |
| --- | --- |
| 1  2  3  4  5  6 | <em># 32位 ARM（覆盖绝大多数设备）</em>  flutter build apk --release --target-platform android-arm    <em># 64位 ARM（新设备，性能更优）</em>  flutter build apk --release --target-platform android-arm64 |

但
`--target-platform`
 只控制 Flutter 引擎和 Dart AOT 产物的架构，不影响第三方插件 AAR 中打包的 native 库（如 libmpv.so）。需要在
`build.gradle`
 中配合 ABI filter 和 packaging excludes：

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25 | android {  defaultConfig {  ndk {  <em>// 通过构建参数动态控制，默认 v7a</em>  if (project.hasProperty('targetAbi')) {  abiFilters project.property('targetAbi')  } else {  abiFilters 'armeabi-v7a'  }  }  }    <em>// 关键：排除插件 AAR 中非目标架构的 .so</em>  packaging {  jniLibs {  def targetAbi = project.hasProperty('targetAbi') ?  project.property('targetAbi') : 'armeabi-v7a'  def allAbis = ['armeabi-v7a', 'arm64-v8a', 'x86\_64', 'x86']  allAbis.findAll { it != targetAbi }.each { abi ->  excludes += ["lib/${abi}/\*\*"]  }  }  }  } |

> **为什么需要
> `packaging.jniLibs.excludes`
> ？**
> `ndk.abiFilters`
>  只控制 CMake/ndk-build 编译的产物。像 media\_kit 这类通过 JAR 分发预编译 .so 的插件，其多架构库会通过 Gradle 依赖解析进入 APK，不受
> `abiFilters`
>  约束。

## 第二刀：恢复代码混淆（-2.9MB）

### 问题

项目原先通过
`gradle.properties`
 配置混淆：

|  |  |
| --- | --- |
| 1  2 | extra-gen-snapshot-options=--obfuscate |

升级 AGP 后此配置被注释掉，改为依赖构建命令行参数。但常常忘记加
`--obfuscate`
。

### 验证：Flutter Gradle 插件确实读取此属性

查看 Flutter SDK 源码
`FlutterPlugin.kt`
：

|  |  |
| --- | --- |
| 1  2  3  4  5 | val extraGenSnapshotOptionsValue: String? =  project.findProperty("extra-gen-snapshot-options")?.toString()  <em>// ...</em>  extraGenSnapshotOptions = extraGenSnapshotOptionsValue |

### 方案：使用标准 Gradle 属性

比起旧的
`extra-gen-snapshot-options`
，Flutter 的 Gradle 插件还支持更语义化的属性：

|  |  |
| --- | --- |
| 1  2  3  4 | <em># gradle.properties</em>  dart-obfuscation=true  split-debug-info=build/debug-info |

这样无论构建命令是否带
`--obfuscate`
，混淆都会自动生效。
`split-debug-info`
 配合使用可保留符号映射用于崩溃日志还原。

## 第三刀：GBK 映射表去重（-1.1MB）

### 问题

项目中 **三个位置** 各自嵌入了一份 23,943 条的 GBK-UTF16 映射表：

* `lib/utils/decode_body.dart`
  （24,047 行）
* `lib/utilsv2/decode_body.dart`
  （24,051 行）
* `package:fast_gbk`
  （依赖库自带）

三份映射表在 AOT 编译后占用
`libapp.so`
 约 **6MB**。

### 方案

统一使用
`fast_gbk`
 包，删除两处嵌入的映射表：

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12 | <em>// lib/utilsv2/decode\_body.dart — 从 24,051 行精简到 92 行</em>  import 'package:fast\_gbk/fast\_gbk.dart';    class DecodeBody {  String decode(Uint8List bodyBytes, String? contentType) {  if (\_isGBK(contentType)) {  return gbk.decode(bodyBytes, allowMalformed: true);  }  return utf8.decode(bodyBytes, allowMalformed: true);  }  } |

|  |  |
| --- | --- |
| 1  2  3 | <em>// lib/utils/decode\_body.dart — 从 24,047 行精简到 3 行</em>  export '../utilsv2/decode\_body.dart'; |

## 第四刀：关键转折—— `useLegacyPackaging` （-19.4MB）

**这是本文最核心的优化，也是最容易被忽视的。**

### 问题定位

通过
`python3 + zipfile`
 分析 APK 内部压缩情况时，发现所有
`.so`
 文件的压缩率竟然是 **100%**（即完全未压缩）：

|  |  |
| --- | --- |
| 1  2  3  4 | libapp.so:    18.33MB raw -> 18.33MB compressed (100%)  libmpv.so:    10.76MB raw -> 10.76MB compressed (100%)  libflutter.so: 7.56MB raw ->  7.56MB compressed (100%) |

37.8MB 的 native 库占了 APK 的 86%，却一字节都没有压缩。

### 根因

**AGP 8.x + minSdkVersion ≥ 23** 时，默认行为变为
`extractNativeLibs=false`
：

* `.so`
  文件以\*\*未压缩、页面对齐（16KB aligned）\*\*的方式存入 APK
* Android 6.0+ 系统可直接从 APK mmap 加载 .so，无需解压
* 优势：安装后磁盘占用小（不需要 APK + 解压两份），安装速度快
* 劣势：**APK 下载体积显著增大**

旧版 AGP 8.3.2 +
`minSdkVersion 21`
 时默认压缩 .so，升级 AGP 8.6.1 +
`minSdkVersion`
 改为
`flutter.minSdkVersion`
（值...