---
title: WMPFDebugger 微信小程序调试神器
url: https://mp.weixin.qq.com/s/Vs4oPx7CwQKtk_ov3FHMYQ
source: Doonsec's feed
date: 2026-04-03
fetch_date: 2026-04-04T04:12:20.909286
---

# WMPFDebugger 微信小程序调试神器

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/0zk3Ye7cp03ACcJCklo3a1ibHWfYAKdZwOzA8EASTZwxerGVbFxpUmXDyKGmdOESDOvb3LVHbpFicoibgaStZtO4icS3gXkEGPUNQ7spd2vjc3M/0?wx_fmt=jpeg)

# WMPFDebugger 微信小程序调试神器

原创

攻防路
攻防路

攻防录

![]()

在小说阅读器中沉浸阅读

项目地址：https://github.com/Spade-sec/First

WMPFDebugger 微信小程序调试器：直接用 Frida 注入微信客户端，把小程序的调试协议劫持出来，再通过 CDP 代理桥接到 Chrome DevTools，整条链路就打通了。

---

## 它是怎么工作的

整个架构分三层：Frida 注入层、WebSocket 调试服务、CDP 代理服务。

**Frida 注入层**做的事情最底层。微信的 WMPF（WeChat Mini Program Framework）运行时里有一套过滤机制，专门屏蔽 DevTools 的接入。hook.js 里的 `patchCDPFilter` 函数找到这个过滤函数的内存偏移地址，把过滤状态从 `6`（拒绝）直接 patch 成 `0x0`（放行）：

```
// 拦截 CDP 过滤器，把 value=6 的过滤状态清零
if (inputValue.add(8).readU32() == 6) {
    inputValue.add(8).writeU32(0x0);
}
```

同时还有一个 `patchOnLoadStart`，hook 了 `AppletIndexContainer::OnLoadStart`，把加载来源的 Scene 值改写成 `1101`（开发者工具场景），骗过微信的场景校验。

这两处 patch 的偏移地址是版本相关的，工具内置了 28 个微信版本的地址表，从 11581 到 19027，基本覆盖了近两年的版本范围：

| 支持范围 | WMPF 版本区间 | 推荐微信版本 |
| --- | --- | --- |
| Windows | 11581 ~ 19027 | 4.1.0.30 |
| macOS | 需 DP 虚拟机 | - |

每个版本对应一个 `addresses.{version}.json`，引擎启动时从进程路径自动提取版本号，加载对应配置，不需要手动指定。

**WebSocket 调试服务**（默认端口 9421）负责和小程序运行时通信。微信内部用的是 protobuf 封装的 WebSocket 消息，工具里完整实现了 `WARemoteDebug_DebugMessage` 的序列化/反序列化，能把 CDP JSON 命令封进 protobuf 再发给小程序，把小程序回来的 protobuf 消息拆出 CDP 数据再转给 DevTools。

**CDP 代理服务**（默认端口 62000）是标准 WebSocket，Chrome DevTools 直接连这个端口就行。两个服务之间有一个 `DebugMessageBus` 做事件分发，互相解耦。

---

## 五个功能模块

工具在基础调试链路上叠了五个实用模块，做安全研究时基本都用得上。

### 路由枚举与导航

注入一段 JS 到小程序 window 里，读取 `__wxConfig` 拿到完整的页面路由列表、tabBar 配置、appId 等信息。拿到路由后可以一键跳转，或者批量访问所有页面（有延迟控制和取消机制）。还有个"防强制跳转"保护，可以记录被拦截的跳转事件——有些小程序会在你访问某些页面时强制跳走，开了这个就能看到到底跳去了哪。

![路由导航面板](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp03V0NG7ibH7LDJlficttdBBsfkSqicl18vEMiaPXhBqgU1ClIBmssKibCxMu5iaEiahcX4S4RkybM83iaJXnClQSxmt9jHmvH62mgZvYjI/640?wx_fmt=png&from=appmsg)

路由导航面板

### 云函数调用监控与参数分析

`CloudAuditor` 模块做两件事：一是运行时 hook，在 `wx.cloud.callFunction` 上打桩，记录每次云函数调用的函数名、参数、返回值；二是静态扫描，通过 `Debugger.getScriptSource` 把所有加载的 JS 脚本扒下来，用正则提取 `callFunction` 的 name 参数和 data 字段名，顺带扫数据库集合名（`.collection('xxx')`）和云存储操作（uploadFile/downloadFile 等）。

扫完能手动补一个调用测试，直接看接口有没有鉴权。

![云函数分析面板](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp01xZK4licDUxaUAKRwdKBOsyiaLsjvV0TDoibU4qHcMFHRzDyZqiaC2xqp1juK7yjtYTgYXo10jaUWtIwM8uEvlrR8ibu5mLSGv7Ln0/640?wx_fmt=png&from=appmsg)

云函数分析面板

### UserScript 自动注入

把 .js 放到 `userscripts/` 目录就行，支持按 URL 匹配和 `run-at` 时机控制（`document-start` / `document-idle` / `document-end`）。工具在小程序连接时用 `Page.addScriptToEvaluateOnNewDocument` 注册持久化脚本，同时在 `setupContext` 事件里再做一次即时注入（`Runtime.evaluate`），确保切换小程序后脚本也能生效。

另外注入时会自动发 `Debugger.setSkipAllPauses(true)`，小程序里那些 `debugger` 反调试断点都会被跳过。

### 安全扫描

`js_analyzer.py` 是从 HeartK-1.1.1 完整移植过来的规则引擎，共 702 条 Nuclei Key Name 规则加 24 条自定义规则，匹配手机号、身份证号、邮箱、IP、JWT、各类 API Key 等敏感信息。URL 提取分四种模式（单段/多段 × 有无危险后缀），还有 OSS 域名检测（阿里/腾讯/AWS/华为/七牛等 13 个云厂商的存储域名）。

扫描结果写入 `scan_reports/` 目录，按时间戳命名。

### GUI 与 CLI 双模式

GUI 用 PySide6 写的，支持深色/浅色主题切换，各模块都有独立面板，适合交互操作。

![主界面控制面板](https://mmbiz.qpic.cn/mmbiz_png/0zk3Ye7cp00Jx13OBG3qILxgCcuym335sVgsuHOY7VFS8qPckf95oDhf423I2s3ibFjBq7bCluMebic9t56Zic8XU6LiaU8ushS4hDiau2zE5Uh0/640?wx_fmt=png&from=appmsg)

主界面控制面板

CLI 更适合脚本集成，参数如下：

```
--debug-port    Frida 调试服务端口（默认 9421）
--cdp-port      CDP 代理服务端口（默认 62000）
--debug-main    开启主服务详细日志
--debug-frida   开启 Frida 详细日志
--scripts-dir   UserScript 目录（默认 ./userscripts）
--script        手动指定单个脚本文件（可多次使用）
```

---

## 快速上手

**环境要求**

* Windows（macOS 用 DP 虚拟机）
* 推荐微信版本 4.1.0.30，下载地址：https://github.com/vs-olitus/wx-version/releases/tag/4.1.0.30
* Python 3.x + frida、websockets、PySide6 等依赖

**1. 安装依赖**

```
git clone https://github.com/Spade-sec/First
cd First
pip install -r requirements.txt
```

**2. 启动调试（GUI 模式）**

```
python gui.py
```

或者直接双击目录里的 `启动.bat`，在主界面点「启动调试」即可。

> 注意：点「启动调试」之前不要打开小程序，启动成功后再打开，这样 Frida 才能正确 hook 到连接时机。

**3. 启动调试（CLI 模式）**

```
# 默认端口
python main.py

# 自定义端口
python main.py --debug-port 9421 --cdp-port 62000

# 开启详细日志
python main.py --debug-main --debug-frida
```

**4. 连接 Chrome DevTools**

启动后在 Chrome 地址栏输入：

```
devtools://devtools/bundled/inspector.html?ws=127.0.0.1:62000
```

打开后能看到熟悉的 DevTools 界面，Sources、Console、Network 全都可以用。

**5. 打包成可执行文件**

```
pyinstaller WMPFDebugger.spec
```

---

## 几个典型场景

**场景一：找未授权云函数接口**

进入云函数审计页，先点「静态扫描」等几秒，工具会遍历所有 JS 脚本提取云函数名称列表。拿到列表后逐个点「发起调用」，看返回是正常数据还是权限错误。没鉴权的接口就这么找出来了。

**场景二：路由越权测试**

点「枚举路由」拿到完整路由表，把不应该直接访问的页面（比如管理员页面、支付确认页）加进测试队列，一键批量访问。配合 UserScript 注入，可以在每个页面加载时自动执行自定义检查逻辑。

**场景三：敏感信息扫描**

打开一个目标小程序，在安全扫描页点「开始扫描」，工具会把当前加载的所有 JS 文件跑一遍规则匹配，结果分类展示：API Key、数据库 URL、OSS 地址等。

欢迎关注“攻防录”✨

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/7vAmdAO11X4lmHfibkjicia7MkfgkmAZCoKicD7poPsfAkjB9o6vqFNE8stLqAYa4gaHHLSmU42FMuYrNiab6mWBWTg/0?wx_fmt=png)

攻防录

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/7vAmdAO11X4lmHfibkjicia7MkfgkmAZCoKicD7poPsfAkjB9o6vqFNE8stLqAYa4gaHHLSmU42FMuYrNiab6mWBWTg/0?wx_fmt=png)

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