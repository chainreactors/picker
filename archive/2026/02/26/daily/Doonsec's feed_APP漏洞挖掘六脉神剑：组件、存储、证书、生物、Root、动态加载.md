---
title: APP漏洞挖掘六脉神剑：组件、存储、证书、生物、Root、动态加载
url: https://mp.weixin.qq.com/s/iXbGLS3F6SKmfnFhZoK2iA
source: Doonsec's feed
date: 2026-02-26
fetch_date: 2026-02-27T04:06:16.499428
---

# APP漏洞挖掘六脉神剑：组件、存储、证书、生物、Root、动态加载

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/3oR6eMARh6y6Gibp0p5TN4sJiapicQ528fJEnAcQJb8k75hWibSOjMGefxicuUXjrDtoYza4icSMWBLQRyD2JvJuZ331x7cDyz0aTmOTkGn4nnibCk/0?wx_fmt=jpeg)

# APP漏洞挖掘六脉神剑：组件、存储、证书、生物、Root、动态加载

sec0nd安全

![]()

在小说阅读器中沉浸阅读

以下文章来源于逍遥子讲安全
，作者逍遥

![](http://wx.qlogo.cn/mmhead/naPHoFY2n5T1dyry62h352tUwxDvKDibwloicSNw3zl7W7LkPqQbpAPmnUvcVqYOYVEhtKCJmJq3U/0)

**逍遥子讲安全**
.

安全引路 | 红队渗透测试丨内网渗透 | SRC漏洞挖掘等安全技术

**一个反编译的wxapkg文件，可能藏着整个云服务的密钥；一个被Hook的指纹验证，可能让千万级用户认证形同虚设。**

2025年，某SRC年度报告显示：移动端漏洞（小程序+APP）占所有提交漏洞的**43%**，但平均奖金比Web端高出**60%**。不是因为移动端更难，而是因为**大部分猎人的认知还停留在Web层面**，对小程序反编译、APP脱壳、客户端绕过一无所知。

我见过最值钱的移动端漏洞，是一个被硬编码在`wxapkg`里的**阿里云AccessKey**——攻击者通过小程序反编译拿到密钥，直接接管了整个生产环境的OSS存储。**奖金：12,000元**。也见过最亏的，一个APP的**生物识别绕过**漏洞提交者只拿了2000元——他不知道这个漏洞可以组合成**任意用户登录+资金窃取**。

本文将首次完整公开我的**小程序+APP双端深度狩猎体系**——从信息收集、逆向分析、协议抓包到业务逻辑漏洞挖掘，涵盖6大类核心手法、9个真实案例、全套武器库，全是干到拧不出水的干货。

## 第一章 移动端攻击面的“三重维度”

### 1.1 小程序 vs APP：攻击面的本质差异

| 维度 | 微信/支付宝小程序 | 原生APP | 混合应用（React Native/Flutter） |
| --- | --- | --- | --- |
| **代码获取** | 可直接反编译wxapkg | 需脱壳、砸壳 | JS bundle可直接提取 |
| **调试难度** | 微信开发者工具可调试 | 需代理、证书配置 | Chrome DevTools可调试 |
| **本地存储** | Storage、IndexedDB | SharedPreferences、Keychain | 取决于框架实现 |
| **协议抓包** | HTTPS需配置证书 | 同左，部分有证书锁定 | 同左 |
| **关键风险点** | 前端密钥硬编码、sessionkey泄露 | 组件暴露、动态注入、Root检测绕过 | JS bundle泄露、bridge漏洞 |

**核心认知**：移动端挖掘不是“Web测试的延伸”，而是一个全新的战场——**客户端不可信**是基本原则，**一切客户端逻辑都能被逆向和篡改**。

### 1.2 小程序专属攻击面

小程序运行在宿主APP（微信/支付宝/抖音等）的WebView中，但多了**原生能力调用**的通道：

* **云开发环境**：直接集成云函数、云数据库，密钥常硬编码在前端
* **用户登录态**：`sessionkey`、`openid`、`unionid`的传递与存储
* **小程序码**：scene参数传递、扫码跳转逻辑
* **插件机制**：第三方插件引入带来的供应链风险
* **支付功能**：唤起支付参数可篡改

### 1.3 APP专属攻击面

APP拥有更底层的系统权限，攻击面更广：

* **组件暴露**：Android的Activity/ContentProvider/Service导出
* **本地存储**：数据库、SharedPreferences、Keychain中的敏感信息
* **动态代码加载**：DEX加载、JNI调用、热更新机制
* **证书锁定**：SSL Pinning绕过
* **生物识别**：指纹/面容验证逻辑绕过
* **Root/越狱检测**：检测逻辑可被Hook绕过

## 第二章 信息收集：移动端资产测绘的“四步走”

### 2.1 小程序信息收集：从搜索到反编译

**第一步：批量发现目标小程序**

使用`wechat_app_search.py`批量搜索关键词相关的小程序：

```
bashpython wechat_app_search.py -k "目标公司名/业务关键词"
```

该脚本可收集小程序的名称、AppID、描述、图标等基础信息。

**第二步：获取小程序包（wxapkg）**

微信小程序的代码包存储在手机本地路径：

* Android：`/data/data/com.tencent.mm/MicroMsg/[32位hash]/appbrand/pkg/`
* iOS：需越狱后访问对应沙盒目录

**提取方法**：

1. 手机root/越狱，直接复制wxapkg文件
2. 使用备份工具提取
3. 通过PC版微信的缓存目录获取（`WeChat Files/Applet/`）

**第三步：反编译wxapkg**

使用`wechat_wxapkg_infoget.py`从wxapkg中提取敏感信息：

```
bashpython wechat_wxapkg_infoget.py -f target.wxapkg
```

该工具内置多种匹配规则，可提取：

* 手机号、身份证
* JWT令牌
* URL、IP、域名
* API密钥
* 用户名密码
* 云服务密钥（AWS/Aliyun等）

**实战案例**：某政务小程序反编译后，在`config.js`中发现硬编码的阿里云AccessKey，直接接管OSS存储桶，获取10万+用户身份证照片。**奖金：8,000元**。

**第四步：域名关联分析**

使用`wechat_domains_search.py`批量搜索小程序使用的域名：

```
python wechat_domains_search.py -i target_appid
```

分析域名可发现：

* API接口地址
* 云开发环境域名
* 第三方服务调用

### 2.2 APP信息收集：从APK/IPA到源码分析

**Android端（APK）**：

```
bash# 1. 反编译apktool d target.apk -o output/# 2. 查看AndroidManifest.xml（组件暴露）# 3. 查看classes.dex（可进一步反编译为Java）dex2jar target.apk -o target.jarjd-gui target.jar
```

**iOS端（IPA）**：

```
bash# 1. 解压IPAunzip target.ipa -d output/# 2. 查看Mach-O二进制（需砸壳，越狱设备）# 3. 查看资源文件中的plist配置
```

**敏感信息自动化扫描**：

```
bash# MobSF - 移动安全框架docker run -p 8000:8000 opensecurity/mobile-security-framework-mobsf# 上传APK/IPA，自动扫描敏感信息、漏洞、权限等
```

**重点关注**：

* `strings.xml`、`plist`中的硬编码字符串
* `AndroidManifest.xml`中的exported组件
* `build.gradle`中引用的第三方库版本（是否存在已知漏洞）
* `local.properties`中的SDK路径（可能泄露开发者信息）

## 第三章 小程序漏洞挖掘的“七种武器”

### 3.1 sessionkey泄露：一键登录任意账号

**漏洞原理**：小程序登录流程中，前端通过`wx.login()`获取code，后端用code换取`sessionkey`和`openid`。若某个接口返回了`sessionkey`，攻击者可利用它伪造用户身份。

**挖掘方法**：

1. 拦截小程序登录、手机号一键登录等请求
2. 关注返回包中的`sessionkey`、`session_key`、`openid`字段
3. 用获取的sessionkey构造请求头：`X-Wx-SessionKey: xxx`或`Cookie: session=xxx`

**实战案例**（来自CN-SEC投稿）：

某旅游类小程序使用手机号一键登录功能。测试发现，一键登录接口的返回包中除了正常的登录态外，还包含明文的`phoneNumber`和`purePhoneNumber`。

text

```
{"phoneNumber":"182****1234", "purePhoneNumber":"18212341234"}
```

攻击者拦截返回包，将这两个参数修改为目标的手机号（如`166****5678`），然后放包——**直接登录成功，无需验证码！**

该漏洞可导致任意用户登录，攻击者可用他人账号查看订单、个人信息等。

**进阶技巧**：sessionkey加密传输时，需分析前端解密逻辑（通常写在JS中）。将加密算法本地复现，即可伪造任意用户的session。

### 3.2 云开发环境密钥泄露

**漏洞原理**：小程序云开发使用`wx.cloud.init()`初始化，常硬编码`env`、`traceUser`等参数。若开发者误将`secret`也写入前端，可直接操作云数据库。

**挖掘方法**：

1. 反编译wxapkg，搜索`cloud.init`、`env`、`secret`关键词
2. 找到云环境ID后，尝试用官方工具连接
3. 若未配置安全规则，可直接读写数据库

**实战案例**：某电商小程序反编译后，在`app.js`中发现：

```
javascriptwx.cloud.init({  env: 'prod-7g8h9j0k',  traceUser: true,  secret: 'f7d8g9h0j1k2l3'  // 硬编码的密钥！});
```

使用该密钥初始化云开发SDK，成功连接生产数据库，获取全部用户订单记录（含收货地址、手机号）。**奖金：5,000元**。

### 3.3 小程序码scene参数注入

**漏洞原理**：小程序码的scene参数用于传递自定义信息，常被用于用户标识、订单ID等。若scene参数未严格校验，可被篡改实现越权。

**挖掘方法**：

1. 生成小程序码，截取scene参数
2. 修改scene值为其他用户ID/订单ID
3. 扫码进入小程序，观察是否可越权访问他人数据

**实战案例**：某点餐小程序，每个订单生成专属小程序码，scene中包含`orderId`。攻击者将orderId修改为其他用户的订单号，扫码进入后直接看到他人订单详情（含地址、电话）。**奖金：3,000元**。

### 3.4 小程序WebView组件XSS

**漏洞原理**：小程序使用`web-view`组件嵌入H5页面。若H5页面存在XSS，攻击者可利用它调用小程序原生能力（需配置`jsapi`）。

**挖掘方法**：

1. 遍历小程序页面，找到`web-view`组件
2. 分析其src是否可控（如从URL参数读取）
3. 尝试注入XSS payload，调用`wx.miniProgram.navigateTo`等接口

**限制**：小程序限制了`web-view`可调用的API，但仍可能造成信息泄露。

### 3.5 小程序支付参数篡改

**漏洞原理**：小程序唤起支付时，参数由前端生成（或后端返回但前端参与签名）。若签名逻辑可绕过，可篡改支付金额。

**挖掘方法**：

1. 拦截下单接口，分析返回的支付参数
2. 尝试修改`total_fee`、`body`等字段
3. 若服务端未二次校验，可实现0.01元支付

**实战案例**：某商城小程序下单时，前端计算`total_fee`并参与签名。攻击者Hook前端计算函数，将100元改为0.01元，成功支付。**奖金：6,000元**。

## 第四章 APP漏洞挖掘的“六种武器”

### 4.1 组件暴露：Android的“后门”

**漏洞原理**：Android的Activity、ContentProvider、Service若设置`exported=true`，可被其他应用直接调用，绕过权限校验。

**挖掘方法**：

```
bash# 从AndroidManifest.xml提取所有exported组件grep -r "android:exported=\"true\"" AndroidManifest.xml# 使用drozer测试组件暴露run app.activity.info -a 包名run app.activity.start --component 包名 Activity名
```

**实战案例**：某银行APP的`LoginActivity`设置`exported=true`，且包含`com.example.LOGIN`自定义action。攻击者编写恶意APP，发送隐式意图直接拉起登录页——但这只是开始。更严重的是，该APP的`FileProvider`也导出，攻击者可读取内部存储文件。**奖金：4,000元**。

### 4.2 本地存储敏感信息泄露

**Android端检查**：

```
bash# 查看SharedPreferencesadb shell run-as 包名 cat /data/data/包名/shared_prefs/*.xml# 查看数据库adb shell run-as 包名 sqlite3 /data/data/包名/databases/数据库.db# 查看外部存储adb shell ls /sdcard/Android/data/包名/
```

**iOS端检查**（需越狱）：

```
bash# 查看plist文件plutil -p /var/mobile/Containers/Data/Application/包名/Library/Preferences/*.plist# 查看Keychain# 需使用Keychain-dumper工具
```

**常见问题**：

* 明文存储登录令牌
* 缓存用户身份证照片
* 保存支付密码（罕见但存在）

### 4.3 证书锁定绕过

**漏洞原理**：APP使用SSL Pinning固定证书或公钥，防止中间人攻击。但若实现不当，可通过Hook绕过。

**绕过方法**：

```
bash# 使用Frida脚本绕过证书锁定frida -U -l frida-android-repinning.js -f 包名# 使用JustTrustMe（Xposed模块）# 安装Xposed框架和JustTrustMe模块
```

**工具推荐**：

* **Objection**：基于Frida的运行时移动探索工具
* **Inspeckage**：动态分析Android应用的工具

### 4.4 生物识别绕过

**最新漏洞案例**：`cap-go/capacitor-native-biometric`库的认证绕过（CVE暂无，GHSA-VX5F-VMR6-32WF）

**漏洞原理**：该库在处理指纹认证时，`onAuthenticationSucceeded()`方法未验证`CryptoObject`，攻击者可直接Hook该方法伪造认证成功。

```
java@Overridepublic void onAuthenticationSucceeded(    @NonNull BiometricPrompt.AuthenticationResult result) {    super.onAuthenticationSucceeded(result);    finishActivity("success");}
```

**利用方法**（Frida脚本）：

```
javascriptJava.perform(function () {    hookBiometricPrompt();});function hookBiometricPrompt() {    var biometricPrompt = Java.use('android.hardware.biometrics.BiometricPrompt')['authenticate'].overload(        'android.os.CancellationSignal',         'java.util.concurrent.Executor',         'android.hardware.biometrics.BiometricPrompt$AuthenticationCallback'    );    biometricPrompt.implementation = function (cancellationSignal, executor, callback) {        var authenticationResultInst = getBiometricPromptResult();        callback.onAuthenticationSucceeded(authenticationResultInst);    }}
```

**后果**：任何使用该库的APP的指纹认证均可被绕过，攻击者无需指纹即可登录。

### 4.5 Root/越狱检测绕过

**挖掘思路**：APP通常会在启动时检查设备是否Root/越狱，若检测到则退出或限制功能。攻击者可Hook检测函数，强制返回false。

**常用Hook点**：

* Android：`RootBeer`、`Su`检测、`build.TAGS`检测
* iOS：`Cydia`、`apt`检测、`fork()`检测

**Frida绕过示例**：

```
javascriptJava.perform(function() {    var RootBeer = Java.use('com.scottyab.rootbeer.RootBeer');    RootBeer.isRooted.implementation = function() {        return false;    };});
```

### 4.6 动...