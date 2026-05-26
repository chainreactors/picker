---
title: APKPure 上的 Telegram 被植入后门
url: https://mp.weixin.qq.com/s/gdRD4Ix20fRvI2uXvdL04Q
source: Doonsec's feed
date: 2026-05-25
fetch_date: 2026-05-26T06:02:47.752922
---

# APKPure 上的 Telegram 被植入后门

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/exLpzP8D7NZTqzweDQu1LGYbbJDibWunM52WENXjwXYNz7AqyZibst29wL5KUHCAxHna3l7ZcCmdibjHgJqDPzeThOjs4oxEKjrBrtreiaticFZs/0?wx_fmt=jpeg)

# APKPure 上的 Telegram 被植入后门

原创

visionsec
visionsec

安全视安

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

---

**声明****：该公众号分享的安全工具和项目均来源于网络，仅供安全研究与学习之用，如用于其他用途，由使用者承担全部法律及连带责任，与工具作者和本公众号无关。**

---

最近，安全研究人员披露了一起非常危险的安卓供应链投毒事件：部分用户从 APK 下载平台 APKPure 获取的 Telegram 12.6.5 安装包，被人恶意重新打包并植入了完整的间谍后门框架。

从目前公开的分析结果来看，这已经不是普通的广告插件或者灰色 SDK，而是一个具备“全面信息窃取能力”的移动端间谍程序。

![](https://mmbiz.qpic.cn/mmbiz_png/exLpzP8D7NbuslYlxIf6AFsRITBmGYzwolmTHYElHEXh5pCE5esfY3CrUdQlzuXYBANZkKZZX35diaMFcq9YwyxxeTIGMJFegMvHIs0766ek/640?wx_fmt=png&from=appmsg)

从逆向截图中可以看到，在 APK 内部新增了一个名为 `DataCollector` 的模块，并且被打入 `classes3.dex` 中。整个恶意框架代码量超过 3000 行，说明这并不是临时拼接的简单木马，而是一套成熟的移动端数据采集系统。

根据代码分析，这个后门能够获取的信息范围非常广，包括：

* Telegram 全部聊天记录
* 历史消息内容
* 手机通讯录
* 本地相册图片
* 文档文件
* GPS 定位信息
* SIM 卡数据
* 设备基础指纹

更值得注意的是，恶意程序在数据上传前还使用了 AES-GCM 加密。这意味着攻击者不仅仅是在“偷数据”，而是在刻意规避网络检测与安全审计。

从代码中暴露出的接口来看，恶意数据会被上传至如下 C2 服务器：

```
38.190.225.166
```

其中包含多个 API 接口，例如：

* `/api/collect`
* `/api/image`
* `/api/avatar`
* `/api/config`
* `/api/collect_batch`

这种结构已经非常接近商业化移动间谍平台的设计模式。

很多人一直以为，“只要不是从乱七八糟的网站下载 APK，就不会出问题”。但这次事件再次说明：即使是知名 APK 分发平台，只要其分发链条被污染，用户依然会中招。

这也是典型的“供应链攻击”。

攻击者并不需要直接入侵你的手机，而是先污染你下载的软件源。当用户以为自己安装的是 Telegram 官方客户端时，实际上运行的已经是一个被重新签名、重新封装过的恶意版本。

对于安卓生态来说，这种攻击尤其危险。

因为安卓允许侧载安装 APK，只要用户关闭限制，就可以绕过官方应用市场的安全审核。而许多第三方 APK 平台为了“提供破解版”“去地区限制”“加速下载”等功能，本身就存在重新打包行为，这给攻击者提供了天然土壤。

从技术角度来看，这类恶意 APK 通常具备几个明显特征：

* 安装包签名与官方不一致
* 多出异常 dex 文件
* 引入未知网络通信模块
* 存在数据采集类命名
* 与境外 IP 建立长期通信
* 请求超出正常范围的权限

而这次暴露出来的 `DataCollector`，几乎把这些特征全部占满。

很多用户可能会忽略一个问题：

Telegram 本身已经是高权限应用。

它拥有：

* 通讯录权限
* 文件访问权限
* 通知权限
* 网络权限
* 相册权限

一旦客户端本身被投毒，攻击者实际上等于直接进入了用户的“核心数据层”。

这也是为什么移动端供应链攻击越来越受到重视。

因为相比传统 PC 木马，手机里存放的数据更加敏感：

* 社交关系
* 银行验证码
* 工作文件
* 身份信息
* 私密照片
* 地理轨迹

这些数据一旦被长期窃取，影响远远超过单纯的账号泄露。

对于普通用户而言，当前最重要的是立即检查自己的 Telegram 来源。

如果你安装的是来自第三方 APK 平台的 Telegram，尤其是非 Google Play、非 Telegram 官方渠道的版本，建议立即卸载，并重新安装官方版本。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/Pf9NC3AaQF6Ceuo3ZCjemDo0mPDNTyoUJ1GhrE8u8odwIKUZVtKHuLfynEO1oM8fhqzOF05HAHz0BZI9OxqDkA/0?wx_fmt=png)

安全视安

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/Pf9NC3AaQF6Ceuo3ZCjemDo0mPDNTyoUJ1GhrE8u8odwIKUZVtKHuLfynEO1oM8fhqzOF05HAHz0BZI9OxqDkA/0?wx_fmt=png)

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