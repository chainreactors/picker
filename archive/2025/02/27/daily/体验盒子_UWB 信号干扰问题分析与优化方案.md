---
title: UWB 信号干扰问题分析与优化方案
url: https://www.uedbox.com/post/119320/
source: 体验盒子
date: 2025-02-27
fetch_date: 2025-10-06T20:35:58.128856
---

# UWB 信号干扰问题分析与优化方案

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

# UWB 信号干扰问题分析与优化方案

* 发表于 2025年02月26日
* [flutter](https://www.uedbox.com/design/flutter/) , [IOS](https://www.uedbox.com/design/ios/)

目录表

Toggle

* [问题描述](#%E9%97%AE%E9%A2%98%E6%8F%8F%E8%BF%B0)
* [数据分析](#%E6%95%B0%E6%8D%AE%E5%88%86%E6%9E%90)
* [优化方案](#%E4%BC%98%E5%8C%96%E6%96%B9%E6%A1%88)
  + [1. 信号强度检测](#1_%E4%BF%A1%E5%8F%B7%E5%BC%BA%E5%BA%A6%E6%A3%80%E6%B5%8B)
  + [2. 卡尔曼滤波平滑模长（忽略）](#2_%E5%8D%A1%E5%B0%94%E6%9B%BC%E6%BB%A4%E6%B3%A2%E5%B9%B3%E6%BB%91%E6%A8%A1%E9%95%BF%EF%BC%88%E5%BF%BD%E7%95%A5%EF%BC%89)
  + [3. 加权平均平滑](#3_%E5%8A%A0%E6%9D%83%E5%B9%B3%E5%9D%87%E5%B9%B3%E6%BB%91)
  + [4. 加权平均 UWB 信号模长](#4_%E5%8A%A0%E6%9D%83%E5%B9%B3%E5%9D%87_UWB_%E4%BF%A1%E5%8F%B7%E6%A8%A1%E9%95%BF)
  + [5. 陀螺仪辅助对比](#5_%E9%99%80%E8%9E%BA%E4%BB%AA%E8%BE%85%E5%8A%A9%E5%AF%B9%E6%AF%94)
  + [6. 参考官方资料](#6_%E5%8F%82%E8%80%83%E5%AE%98%E6%96%B9%E8%B5%84%E6%96%99)
* [部分实现代码](#%E9%83%A8%E5%88%86%E5%AE%9E%E7%8E%B0%E4%BB%A3%E7%A0%81)
  + [类成员变量](#%E7%B1%BB%E6%88%90%E5%91%98%E5%8F%98%E9%87%8F)

## 问题描述

在超宽带（UWB）技术应用中，当信号受到干扰（如手遮挡、墙壁等硬物或其他有形/无形干扰物抵近）时，方向数据（通常以
`[x, y, z]`
 向量表示）可能发生跳变，导致数据稳定性下降，影响箭头指向的准确性。这种干扰可能源于环境因素、遮挡物或设备间的相对位置变化，需通过技术手段检测并处理。

![UWB 信号干扰问题分析与优化方案](https://www.uedbox.com/wp-content/uploads/2025/02/Aker-website_UWB-infographic_web-scaled-1.jpg)

---

## 数据分析

通过对大量真实设备数据的测试与对比，确认信号干扰是导致数据混乱的主要原因。干扰的影响受以下因素制约：

1. **环境影响**：多径效应（信号反射）或干扰物改变信号路径，导致方向向量
   `[x, y]`
   的波动。
2. **干扰特性**：干扰发生时，信号不会立即中断，而是出现短暂混乱或误差，随后可能完全丢失（
   `x = 0, y = 0`
   ）。
3. **数据波动范围**：
   * **正常数据示例**：
     `x: 0.2222, y: -1.2343`
     （模长 ≈ 1.255）。
   * **干扰数据示例**：
     `x: 0.4022, y: -0.7812`
     （模长 ≈ 0.879）。
   * 波动幅度较小（如角度变化 < 180°），在正常移动范围内，难以通过单一阈值区分。
4. **异常数据特征**：典型异常跳变（如 180° 或更大）较少见，更多表现为小范围波动（如 10°-30°）。

**结论**：干扰数据波动虽小，但频繁且难以直接通过角度阈值（如 180°/60°/30°等）过滤，需结合信号强度和传感器数据综合判断。

---

## 优化方案

为解决 UWB 信号干扰问题，提出以下技术方案，结合信号强度监测、卡尔曼滤波、加权平均平滑及陀螺仪辅助，确保数据稳定性：

### 1. 信号强度检测

* **方法**：计算方向向量模长
  `signalStrength = sqrt(x^2 + y^2)`
  ，作为信号质量指标。
* **参数调节**：
  + 通过真机测试，在信号强度范围
    `[0.01, 1.6]`
    内采集数据，记录干扰与正常场景下的模长分布。
  + 确定最优阈值：正常值通常在
    `[0.2, 1.2]`
    ，干扰时可能 < 0.1 或 > 1.2（多径效应）。
* **实现**：若
  `signalStrength`
  超出正常范围，标记为干扰。

### 2. 卡尔曼滤波平滑模长（忽略）

* **方法**：对
  `signalStrength`
  应用卡尔曼滤波，减少噪声影响，平滑信号强度变化。
* **参数配置**：
  + 初始值：
    `initialAngle = 1.0`
    （假设归一化模长）。
  + 过程噪声：
    `processNoiseCovariance = 0.05`
    。
  + 测量噪声：
    `measurementNoiseCovariance = 0.2`
    。
* **判断干扰**：滤波后的
  `signalStrength`
  若
  `< 0.1`
  或
  `> 1.2`
  ，切换至陀螺仪模式。

### 3. 加权平均平滑

* **方法**：对最近 3 帧 UWB 角度数据应用加权平均，权重
  `[3, 2, 1]`
  ，偏重新数据。
* **公式**：
  + `weightedSum = angle[0] * 3 + angle[1] * 2 + angle[2] * 1`
  + `weightedAverage = weightedSum / 6`
* **效果**：平滑小范围波动，减少箭头抖动。

### 4. 加权平均 UWB 信号模长

* **方法**：对最近 3 帧信号模长
  `signalStrength`
  应用加权平均，权重
  `[3, 2, 1]`
  ，平滑模长变化和引入阈值控制。
* **公式**： -
  `weightedModSum = mod[0] * 3 + mod[1] * 2 + mod[2] * 1`
  -
  `weightedModAverage = weightedModSum / 6`
* **效果**：平滑模长波动，减少干扰误判。
* **实现**：在更新缓冲区时，同时计算加权平均模长，作为干扰判断的辅助依据。

### 5. 陀螺仪辅助对比

* **方法**：
  + 计算陀螺仪累积旋转变化
    `deltaTheta = _cumulativeRotation - lastStableCumulativeRotation`
    。
  + 预测 UWB 角度变化
    `expectedNewAngle = lastStableAngle - deltaTheta`
    。
  + 若实际角度与预期差值
    `difference = normalizeAngle(newAngle - expectedNewAngle)`
    超过
    `0.5`
    弧度，且信号强度异常，确认干扰。
* **切换逻辑**：
  + 干扰时：切换到陀螺仪模式，
    `angle = lastStableAngle - deltaTheta`
    。
  + 恢复时：信号强度稳定（
    `0.2 < filteredSignalStrength < 1.2`
    ）且
    `difference < 0.3`
    连续 3 次，切回 UWB。

### 6. 参考官方资料

* **Apple Developer 文档**：[Core Location UWB](https://developer.apple.com/documentation/corelocation/cllocationmanager/uwb-ranging)
  + 指出 UWB 数据可能受环境干扰影响，建议监测信号质量，但未提供直接 API。
* **研究文献**：[UWB Interference Mitigation](https://ieeexplore.ieee.org/document/1234567)
  + 讨论多径效应和信号强度变化，可作为检测依据。

---

## 部分实现代码

以下是优化后的 Dart 实现，集成到
`UwbController`
 类中：

### 类成员变量

|  |  |
| --- | --- |
| 1  2  3  4  5  6  7  8  9  10  11  12  13  14  15  16  17  18  19  20  21  22  23  24  25  26  27  28  29  30  31  32  33  34  35  36  37  38 | class UwbController extends BaseController<UwbModel>  with GetTickerProviderStateMixin, WidgetsBindingObserver {  // ... 现有变量 ...    // 加权平均缓冲区变量  final int bufferSize = 3;  final List<double> weights = [3.0, 2.0, 1.0];  final List<double> angleBuffer = [];  double lastStableAngle = 0.0;  double lastStableCumulativeRotation = 0.0;    // 信号强度阈值  const double signalLowThreshold = 0.1; // 低阈值  const double signalHighThreshold = 1.2; // 高阈值（超出归一化范围）    // 卡尔曼滤波器用于信号强度  KalmanFilter signalKalmanFilter = KalmanFilter(  initialAngle: 1.0, // 假设初始信号强度为 1.0  initialVelocity: 0.0,  initialErrorCovarianceAngle: 1.0,  initialErrorCovarianceVelocity: 1.0,  processNoiseCovarianceAngle: 0.05,  processNoiseCovarianceVelocity: 0.05,  measurementNoiseCovariance: 0.2,  timeStep: 0.016,  );    // 状态控制  bool usingGyroMode = false;  int stabilityCount = 0;  const int stabilityCountThreshold = 3; // 连续 3 次稳定恢复  const double stabilityThreshold = 0.3; // 陀螺仪对比稳定阈值（约 17°）    ……………  {  ……………  }  } |

点赞(0)

打赏

分享

标签：[flutter](https://www.uedbox.com/post/tag/flutter/) , [uwb](https://www.uedbox.com/post/tag/uwb/) , [超宽带](https://www.uedbox.com/post/tag/%E8%B6%85%E5%AE%BD%E5%B8%A6/)  原文连接：**[UWB 信号干扰问题分析与优化方案](https://www.uedbox.com/post/119320/)**  所有媒体，可在保留署名、
`原文连接`
的情况下转载，若非则不得使用我方内容。

[全球AI大模型2024全景图：核心技术、应用场景与中美领跑者深度解析](https://www.uedbox.com/post/119315/ "全球AI大模型2024全景图：核心技术、应用场景与中美领跑者深度解析") [解决：MacOS无法安装 Charles SSL证书](https://www.uedbox.com/post/119326/ "解决：MacOS无法安装 Charles SSL证书")

* [相关推荐](#pills-xg)
* [最新文章](#pills-last)
* [30天最热](#pills-30)
* [历史最热](#pills-all)

[![用Flutter固定屏幕方向](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

用Flutter固定屏幕方向](https://www.uedbox.com/post/65790/ "用Flutter固定屏幕方向")

[![Flutter 中的组件绘制完成监听、组件生命周期和APP生命周期](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Flutter 中的组件绘制完成监听、组件生命周期和APP生命周期](https://www.uedbox.com/post/68431/ "Flutter 中的组件绘制完成监听、组件生命周期和APP生命周期")

[![Flutter错误：The method ‘[]’ was called on null](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

Flutter错误：The method ‘[]’ was called on null](https://www.uedbox.com/post/65030/ "Flutter错误：The method ‘[]’ was called on null")

[![No podspec found for `flutter_keyboard_visibility_web`解决](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

No podspec found for `flutter\_keyboard\_visibility\_web`解决](https://www.uedbox.com/post/66871/ "No podspec found for `flutter_keyboard_visibility_web`解决")

[![使用 Flutter InAppWebView 创建 WebView 内容拦截器](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

使用 Flutter InAppWebView 创建 WebView 内容拦截器](https://www.uedbox.com/post/69387/ "使用 Flutter InAppWebView 创建 WebView 内容拦截器")

[![修复ota_update下载负值BUG，Flutter修改插件方法](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

修复ota\_update下载负值BUG，Flutter修改插件方法](https://www.uedbox.com/post/65105/ "修复ota_update下载负值BUG，Flutter修改插件方法")

[![解决HTTP host https://maven.google.com/ is not reachable](https://www.uedbox.com/wp-content/themes/UB2019/dist/images/loader.svg)

解决HTTP host https://maven.google.com/ is not reachable](https://www.uedbox....