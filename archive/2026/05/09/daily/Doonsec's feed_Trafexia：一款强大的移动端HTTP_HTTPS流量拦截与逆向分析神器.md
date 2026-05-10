---
title: Trafexia：一款强大的移动端HTTP/HTTPS流量拦截与逆向分析神器
url: https://mp.weixin.qq.com/s/4OlukkenBTFaW5cfY8eoqg
source: Doonsec's feed
date: 2026-05-09
fetch_date: 2026-05-10T05:35:07.009146
---

# Trafexia：一款强大的移动端HTTP/HTTPS流量拦截与逆向分析神器

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KysoJFiczHUsZ9cIqiazVRDlGfYTD2W8767Q3NtMfr5wfTCGBib4hnlVVXayZ43hSNgOo689ejGrf25G07drcAoMzkNmRn9ibKG88plFbt1pL0c/0?wx_fmt=jpeg)

# Trafexia：一款强大的移动端HTTP/HTTPS流量拦截与逆向分析神器

柠檬赏金猎人

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

### 概述

Trafexia 是一款功能强大的桌面应用程序，专为从移动设备上拦截和分析 HTTP/HTTPS 流量而设计。它基于 Electron、Vue 3 和 TypeScript 构建，旨在为安全研究人员、移动开发者和逆向工程师提供一个一体化的流量分析工具箱。该工具不仅能够捕获网络请求，还集成了 SSL Pinning 绕过、APK 修改、Frida Gadget 注入、以及针对超安全应用的 Root/模拟器检测规避等高级功能，甚至无需 Root 设备即可完成深度的流量分析。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/KysoJFiczHUty6xkCTrZeI7NjH8W1xbBjAGIfFWfCzzSibWR5y2blQnbEM3uX0owpjP2iaarhicFJib0Vf5ia4FDDQBbKsMkYVDdYxXknYDpD5jXo/640?wx_fmt=jpeg)

项目地址：https://github.com/danieldev23/trafexia

### 技术/功能

Trafexia 集合了多种实用的技术特性，以下是其核心功能模块：

| 功能 | 描述 |
| --- | --- |
| **MITM 代理服务器** | 在端口 `8888` 上启动中间人代理，截获移动设备流量。 |
| **SSL Pinning 绕过** | 内置针对 OkHttp3、Conscrypt、WebView、Flutter、React Native 等常用库的自动绕过脚本。 |
| **APK 修补与 Frida 注入** | 无需 Root 设备，即可将 Frida Gadget 和 SSL 绕过脚本直接注入到 APK 文件中。 |
| **Root 与模拟器检测规避** | 针对像 Shopee 等高度安全的应用，通过高级系统钩子（Hooks）来绕过 Root/模拟器检测，从而进行深度分析。 |
| **自动 CA 证书生成** | 自动为 HTTPS 拦截生成并管理 SSL 证书。 |
| **扫码连接** | 支持通过扫描二维码快速配置移动设备代理。 |
| **实时请求捕获** | 实时显示捕获的 HTTP/HTTPS 请求，无需手动刷新。 |
| **高级过滤与搜索** | 支持按请求方法、状态码、Host 地址、内容类型进行过滤，快速定位目标请求。 |
| **请求详情分析** | 提供请求/响应头、请求/响应体、请求时间轴等详细信息，并支持语法高亮。 |
| **图案与令牌识别** | 自动识别 JWT Token、API 密钥、Base64 编码等敏感信息。 |
| **导出功能** | 支持将捕获的请求导出为 HAR 文件、cURL 命令、Python 代码、Postman 集合。 |

### 使用示例

**1. 项目环境搭建与运行**

```
# 克隆仓库

git clone https://github.com/danieldev23/trafexia.git

cd trafexia

# 安装依赖（推荐使用 npm）

npm install

# 启动开发环境

npm run dev
```

**2. 基础流量拦截步骤**

* **启动代理**：打开 Trafexia 应用，点击“Start Proxy”按钮，应用将在本机 `0.0.0.0:8888` 端口启动 MITM 代理服务器。
* **扫描二维码**：在应用界面上会显示一个二维码。使用你的移动设备（Android/iOS）扫描此二维码，以快速获取代理服务器地址和端口。
* **配置移动设备代理**：
  + **Android**：进入 设置 → WiFi → 长按当前连接的网络 → 修改网络 → 高级选项 → 代理 → 选择“手动”，填入显示的代理 IP 和端口 (`8888`)。
  + **iOS**：进入 设置 → 无线局域网 → 点击当前网络旁的 `(i)` 图标 → 配置代理 → 选择手动，填入 IP 和端口。
* **安装 CA 证书**：根据应用内指引，下载并安装 Trafexia 生成的 CA 证书到移动设备上，以便拦截 HTTPS 流量。
* **开始捕获**：配置完成后，移动设备上的网络请求就会出现在主界面的请求列表中。你可以进行过滤、查看详情、导出等操作。

**3. APK 注入（修补模式，无需 Root）**

如果你需要分析某个 Android 应用，且该应用使用了 SSL Pinning，可以尝试使用 APK 修补功能。

1. 在 Trafexia 中找到“APK Patcher”相关功能。
2. 选择要修补的 APK 文件。
3. 勾选需要注入的模块（如 Frida Gadget 或 SSL 绕过脚本）。
4. 点击“Patch”按钮，工具会自动解包 APK、注入相关文件并重新签名。
5. 将修补后的 APK 安装到你的设备上进行逆向分析。

### 注意事项

* **安全风险**：安装 CA 证书后，您的网络流量将会被监控。**请仅将此工具用于您自己拥有的、或明确授权测试的设备上，用于开发、学习或逆向工程。** 业务结束后请务必将设备上的 CA 证书移除，以防产生安全漏洞。
* **法律合规**：请确保使用 Trafexia 的行为符合当地法律法规。未经授权拦截他人网络通信或恶意使用该工具是违法的。
* **网络环境**：确保您的桌面端与移动端设备在同一局域网下，且防火墙允许端口 `8888` 的入站连接。
* **系统兼容性**：该工具基于 Electron 构建，适用于 macOS、Windows 和 Linux。如需跨平台开发，请确保本地环境已安装 Node.js 18 或更高版本。

### 参考链接

* Trafexia GitHub 仓库
* Trafexia 项目主页
* 最新版本下载页

---

仅限交流学习使用，如您在使用本工具或代码的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。“如侵权请私聊公众号删文”。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/OkRKg4J9smV0q1aJxxA7GF9uXFH0S6D3QRb0jNcE13icxpHvErdgibarS4mwYYE2aicga15MMmcOCdTazgj9ibn0RA/0?wx_fmt=png)

柠檬赏金猎人

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/OkRKg4J9smV0q1aJxxA7GF9uXFH0S6D3QRb0jNcE13icxpHvErdgibarS4mwYYE2aicga15MMmcOCdTazgj9ibn0RA/0?wx_fmt=png)

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