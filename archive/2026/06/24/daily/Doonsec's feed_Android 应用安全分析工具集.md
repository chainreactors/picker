---
title: Android 应用安全分析工具集
url: https://mp.weixin.qq.com/s/ZBqg6LQuy2N_DHhsJAaN0A
source: Doonsec's feed
date: 2026-06-24
fetch_date: 2026-06-25T06:06:30.219084
---

# Android 应用安全分析工具集

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/HqolA1dQic68J3U7ibericNjUToALYwojqKrcaDASakfsP6KY0ySMZD6mZ2yiaicyLicAFBS8pz4fib6RN9hdnfqtGWlmgGNSDyCS7A5kja1DucnZY/0?wx_fmt=jpeg)

# Android 应用安全分析工具集

jenn619
jenn619

HACK之道

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 项目简介

基于 Frida 的 Android 应用安全分析工具集，运行时自动捕获加密/哈希参数，监控网络请求、WebView、动态加载等行为，并内置 Root/模拟器检测绕过。

## 功能特性

| 模块 | 功能 |
| --- | --- |
| **加密自吐** | 自动输出 Cipher（AES/DES/RSA）、MessageDigest（MD5/SHA）、HMAC 的算法名、密钥、IV、明文、密文 |
| **HTTP 拦截** | 拦截 OkHttp3 / HttpURLConnection / Apache HttpClient 的请求 URL、Headers、Body |
| **WebView 监控** | 捕获 loadUrl / loadData / addJavascriptInterface，检测 XSS、JS Bridge RCE 等安全风险 |
| **安全绕过** | Bypass Root 检测、模拟器检测、调试器检测、FLAG\_DEBUGGABLE、签名校验 |
| **行为监控** | DexClassLoader 动态加载、SharedPreferences、SQLite、Intent 跳转、剪贴板、Log 输出 |
| **SSL Bypass** | 绕过 Android < 7 TrustManager + OkHTTPv3 CertificatePinner |
| **防退出** | 拦截 Runtime.exit / Process.killProcess，防止 App 自杀退出 |
| **Native 监控** | Hook SO 层导出函数、JNI RegisterNatives 注册监控 |

## 环境要求

* **Frida**

  : Python 端 `pip install frida frida-tools`
* **设备**

  : 已 root 的 Android 设备或模拟器（如雷电模拟器），已安装并运行 `frida-server`
* **ADB**

  : 设备可通过 adb 连接
* **Python**

  : 3.6+

## 快速开始

### 方式一：Python 启动（推荐）

```
# 1. 修改 Crypto.py 中的目标包名TARGET_PACKAGE = "com.target.app"
# 2. 运行python Crypto.py
```

### 方式二：Frida 命令行

```
# Attach 模式（附加到已运行进程）frida -U -n com.target.app -l main.js
# Spawn 模式（启动时注入，适合 early hook）frida -U -f com.target.app -l main.js --no-pause
```

## 配置

### Crypto.py 配置

```
# 修改顶部配置区域ADB_PATH = r"D:\path\to\adb.exe"     # adb 路径TARGET_PACKAGE = "com.target.app"     # 目标包名MODE = "attach"                       # "attach" 或 "spawn"# 模块开关（按需开启/关闭）MODULES = {    "Utils.js":           True,       # 工具函数（必须）    "Hash.js":            True,       # 哈希算法    "Mac.js":             True,       # HMAC    "Cipher.js":          True,       # 加密算法    "HttpMonitor.js":     True,       # HTTP 拦截    "WebViewMonitor.js":  True,       # WebView 安全检测    "RootBypass.js":      True,       # Root/模拟器绕过    "DexMonitor.js":      True,       # 动态加载 + 行为监控    "String.js":          False,      # String 监控（噪音较多）    "Native.js":          False,      # Native SO 层监控}
```

### 查看目标包名

```
# 列出所有应用包名adb shell pm list packages
# 查看当前前台应用adb shell "dumpsys activity | grep mFocusedActivity"
```

## 项目结构

```
├── Crypto.py            # Python 启动器（模块管理 + 自动连接 + 输出记录）├── main.js              # Frida 命令行入口（精简版，含防退出）├── Utils.js             # 工具函数（Hex/Base64/UTF8 编解码、调用栈打印）│├── Cipher.js            # javax.crypto.Cipher 加密算法自吐├── Cipher2.js           # 增强版：更多 Cipher.init 重载 + SecretKeySpec├── Hash.js              # MessageDigest 哈希算法监控├── Mac.js               # javax.crypto.Mac HMAC 监控├── String.js            # java.lang.String 操作监控├── Native.js            # Native SO 层函数 Hook│├── HttpMonitor.js       # OkHttp / HttpURLConnection / Apache HTTP 拦截├── WebViewMonitor.js    # WebView 安全检测（XSS/JS Bridge/跨域）├── RootBypass.js        # Root/模拟器/调试器检测绕过├── DexMonitor.js        # 动态加载 + SP/SQLite/Intent/剪贴板/Log 监控│├── ssl.js               # SSL 证书校验绕过（TrustManager + OkHTTPv3）└── exit.js              # 防应用自杀退出
```

项目地址

https://github.com/jenn619/frida\_Hook\_tools\_Android

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GzdTGmQpRic1orFibqtmBJd06F33KoWTM6qEUAG7ZbwicA5MhTqx9stelHv8cMgibthiahUBTtgbPgn3ia2bYLpBElTQ/0?wx_fmt=png)

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