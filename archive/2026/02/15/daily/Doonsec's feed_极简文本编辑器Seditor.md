---
title: 极简文本编辑器Seditor
url: https://mp.weixin.qq.com/s/h7EoaE1s4MHIhBlxyd2g5A
source: Doonsec's feed
date: 2026-02-15
fetch_date: 2026-02-16T04:17:48.266166
---

# 极简文本编辑器Seditor

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FTLowEmGFibplXkrLfOVicOKnGIf0YmbqDzRsc8e86KSoPbGPia6U0iayHibI4MnU4kw3EDv1YKVfYm2Fia6GXkFMzkbnEMz38ibrP3stjqAhOJTY8/0?wx_fmt=jpeg)

# 极简文本编辑器Seditor

原创

1ns1ght
1ns1ght

知行之树

![]()

在小说阅读器中沉浸阅读

一直以来我都有一个近乎“洁癖”的需求：希望有一款极简风格、功能的文件编辑器，但又不喜欢用操作系统内置的文本编辑器，哈哈哈，我对它的核心要求只有：自动保存、行号显示、占用资源少。这两天借助 Codex 的能力，将它实现了。由于我的主力电脑是 Mac M4 Pro，操作系统版本为26.3 (25D125)，所以目前只在该操作系统下进行了测试。代码已上传GitHub 仓库，https://github.com/want2live233/Seditor。

马上过年了，平台送了红包封面的额度，我做了一款送给大家，希望大家能够喜欢，一共 300 个，数量有限，先到先得，可以直接划到文末领取。

以下是编辑器相关的内容，按需阅读。

原生 `AppKit`极简文本编辑器，面向个人使用，强调小体积、低资源占用、良好 CJK 输入体验。

## 已实现

* 左侧行号 + 右侧滚动条
* 原生触控板手势滚动
* 自动保存（0.8 秒防抖，写入 `~/Library/Application Support/Seditor/autosave.txt`）
* 打开/保存文件

+ `Cmd+O`打开
+ `Cmd+S`保存
+ `Shift+Cmd+S`另存为

* 多标签

+ `Cmd+T`新建标签
+ `Cmd+W`关闭当前标签
+ `Shift+Cmd+]`/ `Shift+Cmd+[`切换标签
+ 顶部右侧 `+`按钮新建标签

* 仅渲染可视区行号（大文件更省资源）
* 主题切换（System/Light/Dark）
* 字体大小调整（View 菜单）

## 运行

```
swift run Seditor
```

## 打包 .app（固定图标）

项目已包含固定图标资源：

* `/Users/x/Documents/Seditor/Assets/AppIcon.icns`

一键打包：

```
cd "/Users/x/Documents/Seditor"
./scripts/build_app.sh
```

输出位置：

* `/Users/x/Documents/Seditor/dist/Seditor.app`

## 工具链问题排查

如果你遇到 `Swift`编译器和 SDK 版本不匹配（`this SDK is not supported by the compiler`），先检查并对齐工具链：

```
xcode-select -p
xcodebuild -version
swift --version
sudo xcode-select -s /Applications/Xcode.app/Contents/Developer
```

## 核心文件

* `/Users/x/Documents/Seditor/Package.swift`
* `/Users/x/Documents/Seditor/Assets/AppIcon.icns`
* `/Users/x/Documents/Seditor/scripts/build_app.sh`
* `/Users/x/Documents/Seditor/Sources/Seditor/App/Main.swift`
* `/Users/x/Documents/Seditor/Sources/Seditor/App/AppDelegate.swift`
* `/Users/x/Documents/Seditor/Sources/Seditor/Core/EditorSession.swift`
* `/Users/x/Documents/Seditor/Sources/Seditor/Core/EditorTheme.swift`
* `/Users/x/Documents/Seditor/Sources/Seditor/Views/EditorTextView.swift`
* `/Users/x/Documents/Seditor/Sources/Seditor/Views/GutterView.swift`

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hzdtIC9ogHaiccWhvTOBCB5gutaJ8Uw3bKcjbcynuFesmxia8VGyTHrLiaNokIFhChhYsLozcRMX8dZ97x18XECiaQ/0?wx_fmt=png)

知行之树

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hzdtIC9ogHaiccWhvTOBCB5gutaJ8Uw3bKcjbcynuFesmxia8VGyTHrLiaNokIFhChhYsLozcRMX8dZ97x18XECiaQ/0?wx_fmt=png)

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