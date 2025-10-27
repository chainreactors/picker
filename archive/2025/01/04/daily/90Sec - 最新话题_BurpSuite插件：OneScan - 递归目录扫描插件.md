---
title: BurpSuite插件：OneScan - 递归目录扫描插件
url: https://forum.90sec.com/t/topic/2484
source: 90Sec - 最新话题
date: 2025-01-04
fetch_date: 2025-10-06T20:09:02.143065
---

# BurpSuite插件：OneScan - 递归目录扫描插件

[90Sec](/)

# [BurpSuite插件：OneScan - 递归目录扫描插件](/t/topic/2484)

[账号审核](/c/account/11)

[vay](https://forum.90sec.com/u/vay)

2025 年1 月 3 日 08:30

1

各位师傅元旦快乐！祝各位师傅新的一年挖的漏洞翻倍，收入翻倍，开心翻倍～

# OneScan - 递归目录扫描插件

OneScan 是一款用于递归目录扫描的 BurpSuite 插件，为发现更深层次目录下隐藏的漏洞赋能

项目地址：<https://github.com/vaycore/OneScan>

## 项目介绍

OneScan 插件的思路由 One 哥提供，我负责编码将思路变现；后续有段时间我没参与开发，由 Rural.Dog 哥担下更新功能的重任；在 Github 开源之后，我继续项目的维护和升级工作。

OneScan 项目升级维护了近两年，感谢这期间师傅们积极的反馈意见和提供优化建议，让我有机会发现 OneScan 在实战中遇到的更深层次的问题，从而精准定位问题点并修复，优化使用体验上的不足；除此之外，针对师傅们反馈的特殊测试场景，新增了一些实战中必要的功能，欢迎各位师傅安装体验。

### 使用场景

OneScan 起初是为了发现站点深层目录下的 `Swagger-API` 接口文档，后面随着功能完善和使用姿势的增加，目前可以完成如下测试工作：

* 发现隐藏 API 接口
* 发现敏感信息泄漏
* 测试未授权、越权漏洞

### 安装说明

> 因为之前有萌新在群里问过，所以简单过一下。大佬们可跳过此步骤

前往 <https://github.com/vaycore/OneScan/releases> 下载插件最新版本 JAR 包：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/7/7e2806505a43ce88ed7cef81385ad91ea7863caa_2_690x337.png)

image920×450 34 KB](https://forum.90sec.com/uploads/default/original/2X/7/7e2806505a43ce88ed7cef81385ad91ea7863caa.png "image")

以 BurpSuite v2024.3.1.3 版本为例。首先切换到 `Extensions` 标签下的 `Installed` 页面，然后点击 `Add` 按钮，准备添加 OneScan 插件：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/c/c60d4b53e288f657c8d9d2655092b350119347e0_2_690x369.jpeg)

image1280×686 49.7 KB](https://forum.90sec.com/uploads/default/original/2X/c/c60d4b53e288f657c8d9d2655092b350119347e0.jpeg "image")

在打开的 `Load Burp extension` 窗口中点击 `Select file...` 按钮：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/9/907fbb6a3bdd6cc62b1f5c133b54faad74cae0c8_2_660x500.jpeg)

image951×720 61.7 KB](https://forum.90sec.com/uploads/default/original/2X/9/907fbb6a3bdd6cc62b1f5c133b54faad74cae0c8.jpeg "image")

选择下载完成的 OneScan 插件 JAR 包，点击打开：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/6/6388b87364fbb097bb4146dd0492e880ec9886f9_2_690x422.png)

image1177×720 67.9 KB](https://forum.90sec.com/uploads/default/original/2X/6/6388b87364fbb097bb4146dd0492e880ec9886f9.png "image")

然后点击窗口右下角 `Next` 按钮，输出如下信息，并且没有报错，即表示安装成功：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/1/13854391f6944ee08048a4a12dbc97a4699f95ac_2_660x500.jpeg)

image951×720 69.1 KB](https://forum.90sec.com/uploads/default/original/2X/1/13854391f6944ee08048a4a12dbc97a4699f95ac.jpeg "image")

## 配置HaE插件

> 注意：OneScan 加载 HaE 后，作用域也只限于 OneScan 插件（仅用于提取并展示高亮数据），不会影响到 BurpSuite 安装的 HaE 插件的正常功能

首先，前往 <https://github.com/gh0stkey/HaE/releases> 下载 HaE 插件最新版本 JAR 包：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/e/eafe0f47ac07f5f32a58ce93831d8ab4b4e60a85_2_690x302.jpeg)

image2100×920 128 KB](https://forum.90sec.com/uploads/default/original/2X/e/eafe0f47ac07f5f32a58ce93831d8ab4b4e60a85.jpeg "image")

切换到 OneScan 插件配置下的其他配置页面，在 HaE 配置项，点击 “选择文件...” 按钮：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/d/d3c3ad9b5e38dae48d333ca1ce53fdc020f45865_2_690x422.png)

image1176×720 70 KB](https://forum.90sec.com/uploads/default/original/2X/d/d3c3ad9b5e38dae48d333ca1ce53fdc020f45865.png "image")

选择下载完成的 HaE 插件 JAR 文件的路径：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/0/0b681d4986d9e0cd523262efd0df0823a41c68be_2_690x488.png)

image1000×708 37 KB](https://forum.90sec.com/uploads/default/original/2X/0/0b681d4986d9e0cd523262efd0df0823a41c68be.png "image")

确认后，提示 HaE 加载成功，即表示配置完成：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/4/4584ec75bacc54b4f6d115cdf60b8cd1ce8fd9dc_2_690x373.jpeg)

image1920×1040 82.6 KB](https://forum.90sec.com/uploads/default/original/2X/4/4584ec75bacc54b4f6d115cdf60b8cd1ce8fd9dc.jpeg "image")

配置 HaE 需要注意：

* 由于 HaE 3.0 版本开始采用 `Montoya API` 进行开发，使用新版 HaE 需要升级你的 BurpSuite 版本（>= 2023.12.1）
* 如果您的 BurpSuite 版本低于 2023.12.1 版本，且不想升级 BurpSuite 版本，可考虑下载 <https://github.com/gh0stkey/HaE/releases/tag/2.6.1> 低版本 HaE 继续使用

## 基本使用

介绍一下 OneScan 插件的常见用法

### 主动扫描

首先，在数据看板中打开 “目录扫描” 开关：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/8/8902aa095d2af7d1f5fe779d99d56925419e841c_2_690x345.png)

image1280×640 42.4 KB](https://forum.90sec.com/uploads/default/original/2X/8/8902aa095d2af7d1f5fe779d99d56925419e841c.png "image")

在 BurpSuite 其他模块中，可以把请求包发送到 OneScan 插件主动扫描：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/4/41f978fe69c8bcd827843c8b29a6792e1c3cf2ca_2_690x233.jpeg)

image1280×433 108 KB](https://forum.90sec.com/uploads/default/original/2X/4/41f978fe69c8bcd827843c8b29a6792e1c3cf2ca.jpeg "image")

如果配置了多个字典，会激活 “使用其它字典扫描” 菜单项，可以选择使用其它字典进行主动扫描：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/0/01de9cac84998dfb8a86b05bbd012b3257d5ca19_2_690x233.jpeg)

image1280×433 110 KB](https://forum.90sec.com/uploads/default/original/2X/0/01de9cac84998dfb8a86b05bbd012b3257d5ca19.jpeg "image")

扫描示例如下：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/c/cab1c319379c4a0a9cf7dd581f9c2e4d252cf02b_2_690x349.jpeg)

image1776×900 176 KB](https://forum.90sec.com/uploads/default/original/2X/c/cab1c319379c4a0a9cf7dd581f9c2e4d252cf02b.jpeg "image")

> 注意：主动扫描的请求包，不会被主机允许/阻止列表拦截

### 被动扫描

首先，在 OneScan 数据看板中打开 “监听代理请求”、“目录扫描” 开关：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/7/70fd0c097b0706de1be8766b87ecea8ef8eb16a3_2_690x345.jpeg)

image1280×640 31.8 KB](https://forum.90sec.com/uploads/default/original/2X/7/70fd0c097b0706de1be8766b87ecea8ef8eb16a3.jpeg "image")

切换到 OneScan 插件配置标签下的主机配置页面，配置主机允许/阻止列表（也就是黑/白名单，如果配置为空表示不启用黑/白名单）：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/d/de238f31412a5d5131aac33f7c6ecebccce09d96_2_690x390.png)

image1273×720 59 KB](https://forum.90sec.com/uploads/default/original/2X/d/de238f31412a5d5131aac33f7c6ecebccce09d96.png "image")

然后在浏览器访问允许列表里的目标即可（规则外的流量不会扫描），示例如下：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/7/76e01bbf74aaf3e6a3a2d5bc210a292893074488_2_690x390.png)

image1273×720 263 KB](https://forum.90sec.com/uploads/default/original/2X/7/76e01bbf74aaf3e6a3a2d5bc210a292893074488.png "image")

### 测试未授权、越权接口

数据看板中的 “移除请求头”、“替换请求头” 功能开关分别用于测试未授权和越权漏洞。如果有些目标特殊，可以使用 “请求包处理” 功能进行处理

#### 测试未授权

首先，切换到 OneScan 插件配置标签下的请求配置页面，配置要移除的请求头，示例如下：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/c/cb39ea945b0d122fda78885ab484c40ec1795362_2_690x384.jpeg)

image1280×714 41.4 KB](https://forum.90sec.com/uploads/default/original/2X/c/cb39ea945b0d122fda78885ab484c40ec1795362.jpeg "image")

配置完成后，在数据看板里打开 “移除请求头” 开关：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/7/7f129eac4a2fa4ef5e8e6b63c55e32ad2c2ac9a1_2_690x293.png)

image1280×544 39.1 KB](https://forum.90sec.com/uploads/default/original/2X/7/7f129eac4a2fa4ef5e8e6b63c55e32ad2c2ac9a1.png "image")

将如下请求包发送到 OneScan 插件：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/0/008091ac2d4d0c98526a1f13ac7c6ff8b9c38c1d_2_690x300.png)

image1280×558 97.1 KB](https://forum.90sec.com/uploads/default/original/2X/0/008091ac2d4d0c98526a1f13ac7c6ff8b9c38c1d.png "image")

结果如下所示，可以发现已自动移除 `Cookie`、`Authorization` 请求头：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/d/da556387f927148f4742f50fbfdfecdfaa9a44af_2_690x350.png)

image1280×650 107 KB](https://forum.90sec.com/uploads/default/original/2X/d/da556387f927148f4742f50fbfdfecdfaa9a44af.png "image")

> 实战过程中，可以打开 “监听代理请求”、“移除请求头” 开关，然后登录目标站点，过一遍站点的功能，之后在 OneScan 中检测是否存在未授权的接口。

#### 测试越权

首先，切换到 OneScan 插件配置标签下的请求配置页面，配置要替换的请求头（一般登录 A 账号的话，这里配置 B 账号的权限），示例如下：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/b/b19be93dbf1ab9611c4bc29385eb2e13ced6c19d_2_690x420.jpeg)

image1182×720 37.9 KB](https://forum.90sec.com/uploads/default/original/2X/b/b19be93dbf1ab9611c4bc29385eb2e13ced6c19d.jpeg "image")

配置完成后，在数据看板里打开 “替换请求头” 开关：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/7/7ad4328514ed40473288ecfbb9978137ba50deda_2_690x253.png)

image1280×471 42.9 KB](https://forum.90sec.com/uploads/default/original/2X/7/7ad4328514ed40473288ecfbb9978137ba50deda.png "image")

将如下请求包发送到 OneScan 插件：

[![image](https://forum.90sec.com/uploads/default/optimized/2X/4/43437...