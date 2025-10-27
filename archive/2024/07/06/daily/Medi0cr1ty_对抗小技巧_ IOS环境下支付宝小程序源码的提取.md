---
title: 对抗小技巧: IOS环境下支付宝小程序源码的提取
url: https://mp.weixin.qq.com/s?__biz=Mzg5ODE3NTU1OQ==&mid=2247484418&idx=2&sn=f9b75f7d4868bf2f96a1104e88ca45ad&chksm=c067c32af7104a3c6ba0a3240f77569d8406c22eb5796f1849fafa261172f004bca7db725629&scene=58&subscene=0#rd
source: Medi0cr1ty
date: 2024-07-06
fetch_date: 2025-10-06T17:44:27.325477
---

# 对抗小技巧: IOS环境下支付宝小程序源码的提取

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWgo1caeTr6atZAztglibEKSdRsyyozNcIIfFepU4c9EPiaibcEH19j0MWHDwonhhoSvj24YbcwawQ65g/0?wx_fmt=jpeg)

# 对抗小技巧: IOS环境下支付宝小程序源码的提取

原创

duckbubi

Medi0cr1ty

### 简要说明

* • 需要有巨魔/越狱环境,以及类似Filza这样的工具。
* • 和常见的安装包一样，此源码非彼源码，是压缩混淆后产出。
* • 安卓环境参考：https://www.52pojie.cn/forum.php?mod=viewthread&tid=1050690 是否仍效未经过验证。

### 操作方法

1.找到支付宝的应用目录，参考Filza的->收藏夹->App管理器->App

```
/var/mobile/Containers/Data/Application/UUID/
```

2.小程序的tar实际上可以在应用目录下`./Documents/NAMAPP_UNZIP/`找到，但这里的命名全是hash,用完也就无了。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWgo1caeTr6atZAztglibEKSd1zicQKA2uzE5ZeszLAh9jdsvBibeorGmUc9U716cPbhb9CRLTpNBH0xg/640?wx_fmt=jpeg&from=appmsg)

3.找到应用目录下的`/Documents/NebulaAppBiz/xriver.db`,导入电脑打开或Filza执行sql

```
SELECT name,package_url FROM "main"."nebulax_resource_app_table" WHERE name = '小程序名称'
```

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWgo1caeTr6atZAztglibEKSdxMFxm3p35ZW4AS7Mjb9HmHJbdDIJs0HuHIHBJpzGwS6fQiaDfP4NKibQ/640?wx_fmt=jpeg&from=appmsg)

本质上就是一个tar，下完解压一下即可。

![](https://mmbiz.qpic.cn/mmbiz_jpg/ZiaGB6iaicqkWgo1caeTr6atZAztglibEKSd1w3DVGSOUAhfXzaWuBkOhCmxicRicGyTnaODT1MKnNuljTNFXlxiboS6g/640?wx_fmt=jpeg&from=appmsg)

### 写在后面

没啥好说的，有需求单没现成的文章供参考，顺手定位一下，顺手分享经验。

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWgZe1vrPKR3r2nK86bn8RL2HDnIDFEaKzCPlQK7xaCdRWMhf1zcP8uuDpfEPJEVomeD43vvLljORQ/0?wx_fmt=png)

Medi0cr1ty

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/ZiaGB6iaicqkWgZe1vrPKR3r2nK86bn8RL2HDnIDFEaKzCPlQK7xaCdRWMhf1zcP8uuDpfEPJEVomeD43vvLljORQ/0?wx_fmt=png)

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