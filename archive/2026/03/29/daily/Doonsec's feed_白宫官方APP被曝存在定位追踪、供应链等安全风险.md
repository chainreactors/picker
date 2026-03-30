---
title: 白宫官方APP被曝存在定位追踪、供应链等安全风险
url: https://mp.weixin.qq.com/s/iHVghiRYuzq3BRQF5EDtlg
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:38:41.141379
---

# 白宫官方APP被曝存在定位追踪、供应链等安全风险

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ibO9kiauylaDrRc4icCVKmBBx8ia8OVicicgLfBC0oBwHr8cHF3Mz58cib7NoZ6BBN0O5qFYu42BHibIpjuSzM7KrAYjkfmiaySqSibTewiabSCBRAek5w/0?wx_fmt=jpeg)

# 白宫官方APP被曝存在定位追踪、供应链等安全风险

原创

黑鸟
黑鸟

黑鸟

![]()

在小说阅读器中沉浸阅读

2026 年 3 月 27 日，美国白宫正式发布官方通稿，宣布上线全新的白宫官方移动应用。白宫在通稿中将该应用定位为美国民众对接特朗普政府的核心信息链路，宣称其能实现 “前所未有的特朗普政府信息触达能力”，可绕过媒体杂音，为用户提供来自官方信源的无过滤、实时更新内容。

根据白宫官方披露的信息，这款应用核心覆盖多项核心功能场景：包括针对重大公告、行政举措、核心施政优先级的突发新闻预警推送；白宫发布会、总统演讲、重大历史性事件的实时直播服务；汇集官方音视频、图片内容的动态媒体资源库；最新政策突破进展的同步更新通道；同时还开放了民众向政府直接传递声音与反馈的专属入口。白宫方面强调，这款集实时资讯、直播视频、高清图片、智能推送于一体的官方应用，是美国民众实时了解、深度参与特朗普政府相关事务最快捷、最权威的移动端载体。

该应用同步登陆苹果 App Store 与谷歌 Play 商店，上线后随即引发网络安全领域的关注。2026 年 3 月 28 日，即应用上线次日，国外安全研究者发布了针对该应用安卓版本的反编译审计报告，披露了其在数据合规、用户隐私保护、供应链安全等多个维度存在的一系列争议性问题，与白宫官方的宣传定位形成了显著反差。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/ibO9kiauylaDr81gcuPiaoiaR9aAbZMOIMvJh6ZnsH8ZDSDicSxJ2gXITPc2FcIhfCYw7HdSypcWM3q9LicOOFILjKmFzlH4U2RrLVBwevXdecicE0/640?wx_fmt=png&from=appmsg)

##

下文为安全研究者针对 2026 年白宫官方安卓 APP 发布的反编译审计报告，核心揭露了这款政府官方 APP 在**合规、隐私、供应链安全、基础安全**四大维度的安全问题，核心结论如下：

1. **合规违规风险**

   APP 内置 JS 注入器，对所有通过内置浏览器打开的第三方网站强行注入代码，移除 Cookie 合规提示、GDPR 授权弹窗、登录墙与付费墙，涉嫌违反欧盟 GDPR 等数据合规法规，同时侵犯第三方网站的正常运营权益。
2. **严重隐私风险**

   APP 号称禁用定位的插件完全失效，内置完整的 GPS 定位追踪链路，前台每 4.5 分钟、后台每 9.5 分钟可采集一次定位数据；同时通过 OneSignal SDK 实现了全维度用户画像与行为追踪，用户个人数据全量同步至第三方服务商服务器，而非政府可控基础设施。
3. **供应链风险**

   APP 从个人开发者的 GitHub Pages 站点加载可执行代码，存在账号被入侵后导致全量用户被植入恶意代码的极端风险；同时依赖多个第三方商业 SaaS 服务商的无沙箱 JS 代码，数据安全与代码安全完全不可控。
4. **基础安全能力严重缺失**

   未配置 SSL 证书固定，存在流量中间人攻击风险；生产版本残留大量开发调试产物，暴露开发环境信息，进一步扩大攻击面；权限配置存在缺陷，外置存储根目录被完全暴露，存在本地数据泄露风险。
5. **开发与管控失范**

   作为美国政府官方 APP，其核心代码、基础设施、数据处理均大量依赖第三方商业服务商与个人开发者，无有效的安全隔离与管控机制，开发流程存在明显的不规范问题，完全不符合政府级应用的安全标准。

# 国外安全研究者反编译白宫新版官方 APP情况原文链接：

# https://blog.thereallo.dev/blog/decompiling-the-white-house-app

#

核心内容如下：

白宫官方安卓 APP 内置了 Cookie / 付费墙绕过注入器，每 4.5 分钟追踪一次用户 GPS 定位，还会从个人 GitHub Pages 站点加载 JavaScript 可执行代码。

白宫在苹果 App Store 和谷歌 Play 商店上线了这款官方 APP，同时发布相关博客，称其能让用户 “前所未有地接触特朗普政府的相关信息”。

一名安全研究者使用 ADB 工具耗时数分钟提取了这款 APP 的 APK 安装包，并通过 JADX 反编译工具完成拆解，以下为其完整的审计发现。

### APP 基础信息

这是一款基于 Expo（SDK 54）构建的 React Native 应用，运行在 Hermes JavaScript 引擎上，后端采用搭载自定义 REST API 的 WordPress 搭建。

```
// sources/gov/whitehouse/app/BuildConfig.java
publicfinalclassBuildConfig {publicstaticfinalStringAPPLICATION_ID="gov.whitehouse.app";publicstaticfinalStringBUILD_TYPE="release";publicstaticfinalbooleanDEBUG=false;publicstaticfinalbooleanIS_HERMES_ENABLED=true;publicstaticfinalbooleanIS_NEW_ARCHITECTURE_ENABLED=true;publicstaticfinalintVERSION_CODE=20;publicstaticfinalStringVERSION_NAME="47.0.1";}
```

根据 Expo 配置文件，该 APP 由名为`forty-five-press`的主体开发。APP 的核心业务逻辑被编译进一个 5.5MB 的 Hermes 字节码包中，原生 Java 层仅作为轻量化封装容器。

```
// resources/assets/app.config
{  "name": "White House",  "slug": "white-house",  "owner": "forty-five-press",  "version": "47.0.1",  "scheme": "whitehouse",  "sdkVersion": "54.0.0",  "newArchEnabled": true,  "plugins": [    ["expo-router", {"sitemap": false}],    ["onesignal-expo-plugin", {"mode": "production"}],    "./plugins/withOkHttpFix",    "./plugins/withResizeableActivity",    "./plugins/withNoBackgroundAudio",    "./plugins/withEdgeToEdge",    "./plugins/withStripPermissions",    "./plugins/withNoLocation"  ],  "updates": {    "enabled": false,    "url": "https://u.expo.dev/1590bd5c-74a2-4dd4-8fe6-ff5552ca15b6",    "checkAutomatically": "NEVER"  },  "extra": {    "eas": {      "projectId": "1590bd5c-74a2-4dd4-8fe6-ff5552ca15b6"    }  }}
```

Expo 配置中有两个关键插件格外醒目：`withNoLocation`（号称禁用定位）、`withStripPermissions`（号称权限剥离），这两个插件在后续审计中被发现存在核心功能矛盾；OTA 在线更新功能处于禁用状态，Expo 更新框架虽被编译进安装包，但并未启用。

### APP 核心业务功能

该研究者从 Hermes 字节码包中提取了全量字符串，筛选出对应的 URL 与 API 接口。APP 的内容全部来自`whitehouse.gov`域名下、带自定义`whitehouse/v1`命名空间的 WordPress REST API，核心接口覆盖首页、新闻文章、直播流、图片库、政策议题、施政成果、媒体偏见板块、X/Twitter 信息流代理等。

![](https://mmbiz.qpic.cn/mmbiz_png/ibO9kiauylaDqeJfpL3wxkRXAfaAOQ00zK5w0eSL4ew0IWANJibXOpMtuT253lSe1MjaAKGoRW3ImtciboGXncZiaOybiaoCYFZKArSRmNSr5o8uk/640?wx_fmt=png&from=appmsg)

字节码包中还包含大量硬编码字符串，例如"THE TRUMP EFFECT""Greatest President Ever!""Text President Trump""Send a text message to President Trump at 45470""Visit TrumpRx.gov""Visit TrumpAccounts[.]gov"

翻译过来： “特朗普效应”“史上最伟大的总统！”“给特朗普总统发短信至 45470”“访问 TrumpRx[.]gov” 等。

甚至在这款资讯类 APP 中，直接嵌入了美国移民与海关执法局（ICE）的举报表单链接（ice[.]gov/webform/ice-tip-form）。

本质上，这是一个内容门户，整合了新闻、直播、图片库、政策页面、社交媒体嵌入内容与政府施政宣传内容，全部由 WordPress 驱动。

### Cookie / 付费墙绕过注入器

###

APP 内置了用于打开外部链接的 WebView 网页组件，**每次有页面在该 WebView 中加载时，APP 都会自动注入一段 JavaScript 代码**。

```
(function() {  var css = document.createElement('style');  css.textContent = [    '[class*="cookie"], [id*="cookie"], [class*="Cookie"], [id*="Cookie"]',    '[class*="consent"], [id*="consent"], [class*="Consent"], [id*="Consent"]',    '[class*="gdpr"], [id*="gdpr"], [class*="GDPR"]',    '[class*="privacy-banner"], [id*="privacy-banner"]',    '[class*="onetrust"], [id*="onetrust"]',    '[class*="cc-banner"], [class*="cc-window"]',    '[aria-label*="cookie" i], [aria-label*="consent" i]',    '[class*="login-wall"], [class*="loginWall"], [class*="LoginWall"]',    '[class*="signup-wall"], [class*="signupWall"]',    '[class*="upsell"], [class*="Upsell"]',    '.cmpboxBtnYes, .cmpbox, #cmpbox, .cmpboxBG',    '[class*="banner-cookie"], [class*="CookieBanner"]',  ].join(',') + '{ display: none !important; visibility: hidden !important; }';  css.textContent += 'body { overflow: auto !important; }';  document.head.appendChild(css);
  var observer = new MutationObserver(function() {    var els = document.querySelectorAll(      '[class*="cookie" i], [class*="consent" i], [class*="gdpr" i], '      + '[id*="cookie" i], [id*="consent" i]'    );    els.forEach(function(el) { el.style.display = 'none'; });  });  observer.observe(document.body, { childList: true, subtree: true });})();true;
```

这段代码的核心作用是：

1. 强制隐藏 Cookie 提示横幅、GDPR 同意弹窗、OneTrust 授权弹窗、隐私提示横幅、登录 / 注册拦截墙、增值服务推广弹窗、付费墙元素、同意管理平台（CMP）弹窗；
2. 强制恢复被同意弹窗锁定的页面滚动功能；
3. 设置持续监听的 MutationObserver，实时清除页面动态加载的所有授权相关元素。

简言之，这款美国政府官方 APP，会向所有第三方网站注入 CSS 和 JavaScript 代码，强行移除网站的合规授权提示、登录门槛与付费墙。

```
// sources/com/reactnativecommunity/webview/RNCWebViewManagerImpl.java
public final void setInjectedJavaScript(        RNCWebViewWrapper viewWrapper, String injectedJavaScript) {    viewWrapper.getWebView().injectedJS = injectedJavaScript;}
```

```
// sources/com/reactnativecommunity/webview/RNCWebView.java
public void callInjectedJavaScript() {    String str;    if (!getSettings().getJavaScriptEnabled()            || (str = this.injectedJS) == null            || TextUtils.isEmpty(str)) {        return;    }    evaluateJavascriptWithFallback("(function() {\n" + this.injectedJS + ";\n})();");}
```

原生层代码也证实，该注入逻辑通过 React Native WebView 的`injectedJavaScript`属性实现，APP 内浏览器的每一次页面加载，都会通过安卓系统的`evaluateJavascript()`方法执行这段注入代码。

### 完整的定位追踪基础设施

###

Expo 配置中号称要剥离定位功能的`withNoLocation`插件完全失效，**OneSignal SDK 的原生定位追踪代码被完整编译进了 APK 安装包**。

```
// sources/com/onesignal/location/internal/common/LocationConstants.java
public final class LocationConstants {    public static final String ANDROID_BACKGROUND_LOCATION_PERMISSION_STRING =        "android.permission.ACCESS_BACKGROUND_LOCATION";    public static final String ANDROID_COARSE_LOCATION_PERMISSION_STRING =        "android.permission.ACCESS_COARSE_LOCATION";    public static final String ANDROID_FINE_LOCATION_PERMISSION_STRING =        "android.permission.ACCESS_FINE_LOCATION";    public static final long BACKGROUND_UPDATE_TIME_MS = 570000;    public static final long FOREGROUND_UPDATE_TIME_MS = 270000;    public static final long TIME_BACKGROUND_SEC = 600;    public static final long TIME_FOREGROUND_SEC = 300;}
```

代码中硬编码了定位间隔：前台 270000 毫秒 = 4.5 分钟，后台 570000 毫秒 = 9.5 分钟。

```
// sources/com/onesignal/location/internal/LocationManager.java
// Gate 1: _isShared must be true (defaults to false in SharedPreferences)boolean r7 = r6.get_isShared()if (r7 != 0) goto L42kotlin.Unit r7 = kotlin.Unit.INSTANCEreturn r7  // bail out if location sharing is off
```

定位追踪并非静默启动，设置了三道启动门槛：

1. `_isShared`

   标志位必须为 true（默认...