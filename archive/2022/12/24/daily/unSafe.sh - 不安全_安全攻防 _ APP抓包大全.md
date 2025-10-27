---
title: 安全攻防 | APP抓包大全
url: https://buaq.net/go-141140.html
source: unSafe.sh - 不安全
date: 2022-12-24
fetch_date: 2025-10-04T02:24:52.033499
---

# 安全攻防 | APP抓包大全

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/c3b2e5831ec8ac64f35201fcd34f0a8b.jpg)

安全攻防 | APP抓包大全

以下文章来源于凌晨安全 ，作者Titan声明：本人坚决反对利用文章内容进行恶意攻击行为，一切错误行为必将受到惩罚，绿色网络需要靠我们共同维护，推荐大家在了解技术原理的前提下，更好的维护个人信息
*2022-12-23 16:34:49
Author: [www.secpulse.com(查看原文)](/jump-141140.htm)
阅读量:63
收藏*

---

以下文章来源于凌晨安全 ，作者Titan

声明：本人坚决反对利用文章内容进行恶意攻击行为，一切错误行为必将受到惩罚，绿色网络需要靠我们共同维护，推荐大家在了解技术原理的前提下，更好的维护个人信息安全、企业安全、国家安全。

最近工作中遇到一些比较奇葩的App，一边测试一边搜集整理出了比较全的姿势。如有错误之处，还请各位师傅多多指教。

*1*

不走代理的APP

**如何判断：连接Fiddler代理-->抓不到包-->关闭Fiddler后正常通信。**

解决方法：PC端模拟器+如下全局代理抓包工具，筛选出模拟器进程无需配置可以直接解密https流量

**(1) HTTPAnalyserv7**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194000-1671782574.png)

**(2) HTTPDebuggerpro**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194000-1671782576.png)

*2*

常规APP抓包

**（1）普通代理 Fiddler**

PS：fiddler 抓app仍是http代理抓包，容易被检测限制

可以在FiddlerScript 中的handle下配置 抓取websocket （多是明文）

```
static function OnWebSocketMessage(oMsg: WebSocketMessage) {
   // Log Message to the LOG tab
   FiddlerApplication.Log.LogString(oMsg.ToString());
}
```

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194000-1671782577.png)

**（2）Charles + postern 可以新建一个VPN配置socks5代理**

 从而绕过更多抓包限制，Charles处理https包更优秀，配置如下简图，也可自行百度高级用法。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194000-1671782579.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194000-1671782581.png)

去掉本地windows代理，只抓取移动端的流量

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194000-1671782583.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194000-1671782584.png)

手机端Postern左侧配置代理—添加代理服务器输入上图设置好的socks代理8889端口，代理类型选择socks5，再返回配置规则删除其他规则，添加匹配所有通过刚刚设置好的代理保存。如图：

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194000-1671782585.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194000-1671782586.jpeg)

开启postern，允许连接vpn，浏览器输入chls.pro这个网址下载安装证书。

Charles点击图中的第二步解密按钮，可解密https流量（8.0以上系统可以将证书放到系统证书目录下）

**（3）VPN手机端使用Httpcanary抓包**

使用VPN，流量会强制走VPN通道，可以抓到更多的包。

配置安装证书，有root权限可以把证书安装到系统证书下（7.1及以下系统默认信任用户证书）

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194000-1671782588.png)

点击右下的小飞机即可抓包，右上角有过滤选项可以只抓http tcp等

左边设置目标应用可以指定进程，方便只抓取想要的数据包

PS：安卓7.1及以上，抓取https流量，需要root后把fiddler、burp、charles等工具的的证书安装到系统根证书下

```
openssl x509 -inform PEM -subject_hash_old -in Desktop.pem |head -1  #获取hash值
用hash值.0重命名证书
adb push 重命名后证书 /sdcard/
mount -o rw,remount /      #挂载为可读写
mv /sdcard/证书 /etc/security/cacerts/      #系统证书路径
chmod 644 /etc/security/cacerts/证书  #修改权限644
# /data/misc/user/0/cacerts-added   #用户证书路径
```

*3*

代理证书校验绕过

**如何判断：0x02抓不到的有可能就是代理检测，更直观的判断就是App可以正常使用，打开httpcanary抓不到或者网络连接失败**

说到代理检测：先简单介绍下数字证书常见的检测机制

一般来说主要检测证书中｛证书链 签发关系 公钥 指纹｝等这些内容，所以我们绕过代理检测也要从这些方面入手。

所以实际抓包测试中hook掉系统自带的检测api和常见框架中的检测api即可。然后再利用0x02中的抓包姿势就O了。

下介绍两种方式：

**（1）Xposed框架+JustTrustMe (0.3)**

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194000-1671782589.png)

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-194000-1671782590.jpeg)

安装xp框架后直接安装justtrustme的apk，在模块里勾选中开启，然后一定！！重启模拟器/手机，打开关闭xp框架和模块一定要重启手机才能生效。

JustTrustMe的源码<可自行编译>（文末有编译好的apk等本文工具打包下载）

```
项目地址：https://github.com/Fuzion24/JustTrustMe
```

从项目代码中可以看到作者hook了很多常见的系统函数、常见框架（okhttp等）HttpsURLConnection 下的API X509TrustManager、HostnameVerifier(域名验证)，setSSLSocketFactory()中的sslcontext里的checksevercertificate()，setHostnameVerifier() 方法；okhttp/okhttp3框架中证书Pinner，certificatePinner 下的 check 方法， 设置通信组件中的setSSLSocketFactory() 方法等。

**（2）Frida + Hook.js**

Frida请自行安装，可以参考https://www.jianshu.com/p/c349471bdef7

Frida：hook中常用的两个命令：

```
frida -UF -l .hook.js   #注入最前端的进程（当前的app）
frida -U --no-pause -f com.xxx.xxx(包名) -l .Hook.js  #启动前注入
```

下面的JS代码类似于frida下的增强版的justtrustme ，Hook了下述的一些系统api和框架

 1.SSLcontext

 2.okhttp

 3.webview

 4.XUtils

 5.httpclientandroidlib

 6.JSSE

 7.network\_security\_config (android 7.0+)

 8.Apache Http client (support partly)

 9.OpenSSLSocketImpl

 10.TrustKit

 11.Cronet

```
Java.perform(function () {    /*    hook list:    1.SSLcontext    2.okhttp    3.webview    4.XUtils    5.httpclientandroidlib    6.JSSE    7.network\_security\_config (android 7.0+)    8.Apache Http client (support partly)    9.OpenSSLSocketImpl    10.TrustKit    11.Cronet    */
    // Attempts to bypass SSL pinning implementations in a number of    // ways. These include implementing a new TrustManager that will    // accept any SSL certificate, overriding OkHTTP v3 check()    // method etc.    var X509TrustManager = Java.use('javax.net.ssl.X509TrustManager');    var HostnameVerifier = Java.use('javax.net.ssl.HostnameVerifier');    var SSLContext = Java.use('javax.net.ssl.SSLContext');    var quiet_output = false;
    // Helper method to honor the quiet flag.
    function quiet_send(data) {
        if (quiet_output) {
            return;        }
        send(data)    }

    // Implement a new TrustManager    // ref: https://gist.github.com/oleavr/3ca67a173ff7d207c6b8c3b0ca65a9d8    // Java.registerClass() is only supported on ART for now(201803). 所以android 4.4以下不兼容,4.4要切换成ART使用.    /*06-07 16:15:38.541 27021-27073/mi.sslpinningdemo W/System.err: java.lang.IllegalArgumentException: Required method checkServerTrusted(X509Certificate[], String, String, String) missing06-07 16:15:38.542 27021-27073/mi.sslpinningdemo W/System.err:     at android.net.http.X509TrustManagerExtensions.<init>(X509TrustManagerExtensions.java:73)        at mi.ssl.MiPinningTrustManger.<init>(MiPinningTrustManger.java:61)06-07 16:15:38.543 27021-27073/mi.sslpinningdemo W/System.err:     at mi.sslpinningdemo.OkHttpUtil.getSecPinningClient(OkHttpUtil.java:112)        at mi.sslpinningdemo.OkHttpUtil.get(OkHttpUtil.java:62)        at mi.sslpinningdemo.MainActivity$1$1.run(MainActivity.java:36)*/    var X509Certificate = Java.use("java.security.cert.X509Certificate");    var TrustManager;    try {        TrustManager = Java.registerClass({            name: 'org.wooyun.TrustManager',            implements: [X509TrustManager],            methods: {                checkClientTrusted: function (chain, authType) { },                checkServerTrusted: function (chain, authType) { },                getAcceptedIssuers: function () {                    // var certs = [X509Certificate.$new()];                    // return certs;                    return [];                }            }        });    } catch (e) {        quiet_send("registerClass from X509TrustManager >>>>>>>> " + e.message);    }    // Prepare the TrustManagers array to pass to SSLContext.init()    var TrustManagers = [TrustManager.$new()];
    try {        // Prepare a Empty SSLFactory        var TLS_SSLContext = SSLContext.getInstance("TLS");        TLS_SSLContext.init(null, TrustManagers, null);        var EmptySSLFactory = TLS_SSLContext.getSocketFactory();    } catch (e) {        quiet_send(e.message);    }
    send('Custom, Empty TrustManager ready');
    // Get a handle on the init() on the SSLContext class    var SSLContext_init = SSLContext.init.overload(        '[Ljavax.net.ssl.KeyManager;', '[Ljavax.net.ssl.TrustManager;', 'java.security.SecureRandom');
    // Override the init method, specifying our new TrustManager    SSLContext_init.implementation = function (keyManag...