---
title: 一次某APP的修复之旅
url: https://mp.weixin.qq.com/s?__biz=MzI1NDg4MTIxMw==&mid=2247486673&idx=1&sn=f90677c655735bb6b172d59b8d478d79&chksm=ea3f3003dd48b915a63567c97894d6a9010ebede7545ba4aebb7c3389ce4855f379cf94d7879&scene=58&subscene=0#rd
source: 猎户攻防实验室
date: 2025-02-14
fetch_date: 2025-10-06T20:36:55.651376
---

# 一次某APP的修复之旅

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ic56Y1PMq5MW3dosLBsHHSsJmgsNUb8r8m7ParO8yPD9wE5pnBnoASS4KMM3kOyXCvsXmKnf16nTtZKbVEl3jeQ/0?wx_fmt=jpeg)

# 一次某APP的修复之旅

浮萍

猎户攻防实验室

> 字数 1386，阅读大约需 7 分钟

## 0x00 前言

最近发现某款APP无法正常使用，打开后地图页面是空白内容，无法显示和使用地图。经过排查，原来是开发者更新了百度地图的API Key，导致旧版本的APP无法正常访问地图服务。

## 0x01 问题分析

APP启动后地图界面呈现空白状态，选择定位也是空白，确认位置提示“请点击地图选择位置”。

![无法显示地图](https://mmbiz.qpic.cn/sz_mmbiz_png/ic56Y1PMq5MW3dosLBsHHSsJmgsNUb8r8Zmb8Ql4osUqIkJ3LCY2yD07fsornm6vxpeO53uiasUfSOnNpqUvTDrA/640?wx_fmt=png&from=appmsg)

通过抓包，提示"APP Mcode码校验失败"。

![校验失败](https://mmbiz.qpic.cn/sz_mmbiz_png/ic56Y1PMq5MW3dosLBsHHSsJmgsNUb8r88ZhDDl0eFKG961f2s9YlUcLQRicqQWiaz4oL4VqZQAvOic8uVYz82vReg/640?wx_fmt=png&from=appmsg "null")

说明该APP的百度地图APIKey与SHA1不匹配导致的，解决方法是替换为对应的APIKey和SHA1即可。

这里有几种解决方案，每种方法都有其优缺点，可以根据实际需求选择最适合的方式。解决方案：

**1.反编译并替换APIKey**（较为复杂，不推荐）：

* • 步骤：解压APK文件，找到`AndroidManifest.xml`文件中的`com.baidu.lbsapi.API_KEY`值，替换为正确的APIKey。然后重新打包并签名APK。
* • 缺点：该APP具有签名校验机制，重新打包后可能导致APP无法正常运行，且后续修改较为复杂。因此，此方法不推荐使用。

**2.抓包软件拦截替换**（简单）：

* • 步骤：使用抓包工具（如小黄鸟）拦截APP发出的网络请求，将请求中的ak参数（即APIKey）替换为新的APIKey。
* • 优点：实现简单，无需修改APP本身。
* • 缺点：每次使用APP时都需要开启抓包工具。

**3.HOOK技术动态修改**（较复杂，但使用最方便）：

* • 步骤：使用HOOK框架（如Xposed）动态修改APP中百度地图APIKey的获取逻辑，使其返回正确的APIKey。
* • 优点：一旦实现，后续使用无需额外操作，体验最为流畅。

## 0x02 过程

无论是上面的哪种方案，都首需要获取正确的APIKey。APIKey可以自己申请，也可以查看新版本的APP中的APIKey是什么，然后进行替换。

自己申请的话，需要注册、认证百度地图开放平台 https://lbsyun.baidu.com/apiconsole/key ，然后创建一个Android应用。

![APIKey申请](https://mmbiz.qpic.cn/sz_mmbiz_png/ic56Y1PMq5MW3dosLBsHHSsJmgsNUb8r8nx6dfoyO6kdibAr3WNtgT0mV0h2Oj94OdniaFEegs43uGfCfcB9Uu9Tg/640?wx_fmt=png&from=appmsg "null")

选择一些所需的服务，需要有定位和地图SDK。

![APIKey申请](https://mmbiz.qpic.cn/sz_mmbiz_png/ic56Y1PMq5MW3dosLBsHHSsJmgsNUb8r8AQY8610icxXAnLnFPICtf3p1kllOOiafsvicerx0RjOsQB52HIINg0bDg/640?wx_fmt=png&from=appmsg "null")

填写发布版SHA1和PackageName

* • **发布版SHA1**：0E:A9:54:9F:05:C4:35:4C:52:D2:53:48:9D:8A:21:15:25:CA:4A:13
* • **PackageName**：com.lerist.\*\*\*tion （该应用的包名）

这里的SHA1是抓包的时候请求里面的，也可以手动计算。

```
unzip Fxxxx1.3.5BETA_xxx.apk -d FK
cd FK/META-INF
keytool -printcert -file FAKELOCA.RSA
```

![计算SHA1](https://mmbiz.qpic.cn/sz_mmbiz_png/ic56Y1PMq5MW3dosLBsHHSsJmgsNUb8r8L65q6sJmjicXPzIvTWkRGCAMsaCpFSVJmWtvKnMsKaFLOvsDnCPM29A/640?wx_fmt=png&from=appmsg "null")

用自己申请的APIKey进行测试。

![APIKey申请](https://mmbiz.qpic.cn/sz_mmbiz_png/ic56Y1PMq5MW3dosLBsHHSsJmgsNUb8r8yibZWmV3ibnpNf2LZN9Lw9dialRQ13nm4bHzlbJibqc6svRhIpzKokbcXA/640?wx_fmt=png&from=appmsg "null")

发现是可以正常使用了。

如果不想自己申请SDK，也可以用新版本中的APIKey进行替换。

我们下载新版本进行查看

![新版本Key](https://mmbiz.qpic.cn/sz_mmbiz_png/ic56Y1PMq5MW3dosLBsHHSsJmgsNUb8r8F2xoMTcSL8v8opmCvrQHZKPwOML3z1fybnXBY6epibvHJNLUliafbicnQ/640?wx_fmt=png&from=appmsg)

新版本的APIKey是 `kGdfeSE3SeAUkeGtur7g8uIXbCx4alFN` 。

同样测试一下新版本中的APIKey，也是可以正常使用的。

![验证新APIKey](https://mmbiz.qpic.cn/sz_mmbiz_png/ic56Y1PMq5MW3dosLBsHHSsJmgsNUb8r8L1VSv2zMbPhhLwBuBhTzaAaoPPfFyMia0zF2GjmMWh7WsadxwLYtJSg/640?wx_fmt=png&from=appmsg "null")

接下来用可以使用的APIKey进行替换，这里以新版本中的APIKey为例。

### 1.抓包替换

这里采用的抓包工具是小黄鸟（需安装证书，否则无法抓包），打开小黄鸟，开启抓包，运行APP。

找到请求`https://api.map.baidu.com/sdkcs/verify` ，长按选择重写功能。

![抓包](https://mmbiz.qpic.cn/sz_mmbiz_png/ic56Y1PMq5MW3dosLBsHHSsJmgsNUb8r8xu2iaXSMsw2YGyDxFMlujF1l0tSDyyXibiaBGfX55l2mFPy9Ad5EttL7A/640?wx_fmt=png&from=appmsg)

修改请求体，选择在线编辑或规则替换。

![请求体](https://mmbiz.qpic.cn/sz_mmbiz_png/ic56Y1PMq5MW3dosLBsHHSsJmgsNUb8r8dwE59xhBk92qTaJ9N8BOqWtTt6fbnSicer3O8nO7IG992f5RJxHLj5A/640?wx_fmt=png&from=appmsg)

替换ak参数（即APIKey），修改为新的APIKey。

![替换参数](https://mmbiz.qpic.cn/sz_mmbiz_png/ic56Y1PMq5MW3dosLBsHHSsJmgsNUb8r8LhcmuQTJ1pjXaqrcOU0BwaSuRFoCpfZD4UOAUEInqeogB9MyNINxaA/640?wx_fmt=png&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ic56Y1PMq5MXZqt7tQYtI8F8JSmqo65GeapTpQWHVJBBdtOUiaibVZPx3p9hibUFaQRLIWtbScgReERUmeDBz6GmJg/0?wx_fmt=png)

猎户攻防实验室

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ic56Y1PMq5MXZqt7tQYtI8F8JSmqo65GeapTpQWHVJBBdtOUiaibVZPx3p9hibUFaQRLIWtbScgReERUmeDBz6GmJg/0?wx_fmt=png)

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