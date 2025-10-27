---
title: IOS逆向(三)-去除某app谷歌广告
url: https://zgao.top/ios%e9%80%86%e5%90%91%e4%b8%89-%e5%8e%bb%e9%99%a4%e6%9f%90app%e8%b0%b7%e6%ad%8c%e5%b9%bf%e5%91%8a/
source: Zgao's blog
date: 2023-05-20
fetch_date: 2025-10-04T11:36:37.832459
---

# IOS逆向(三)-去除某app谷歌广告

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# IOS逆向(三)-去除某app谷歌广告

* [首页](https://zgao.top)
* [IOS逆向(三)-去除某app谷歌广告](https://zgao.top:443/ios%E9%80%86%E5%90%91%E4%B8%89-%E5%8E%BB%E9%99%A4%E6%9F%90app%E8%B0%B7%E6%AD%8C%E5%B9%BF%E5%91%8A/)

[5月 19, 2023](https://zgao.top/2023/05/)

### IOS逆向(三)-去除某app谷歌广告

作者 [Zgao](https://zgao.top/author/zgao/)
在[[逆向](https://zgao.top/category/%E9%80%86%E5%90%91/)](https://zgao.top/ios%E9%80%86%E5%90%91%E4%B8%89-%E5%8E%BB%E9%99%A4%E6%9F%90app%E8%B0%B7%E6%AD%8C%E5%B9%BF%E5%91%8A/)

![](https://zgao.top/wp-content/uploads/2023/05/image-25-1024x437.png)

在应用商店随便找的一个免费piano应用，通过逆向分析去除应用中的谷歌广告。

文章目录

[ ]

* [难度](#%E9%9A%BE%E5%BA%A6 "难度")
* [工具环境](#%E5%B7%A5%E5%85%B7%E7%8E%AF%E5%A2%83 "工具环境")
* [思路分析](#%E6%80%9D%E8%B7%AF%E5%88%86%E6%9E%90 "思路分析")
* [IDA分析应用广告代码](#IDA%E5%88%86%E6%9E%90%E5%BA%94%E7%94%A8%E5%B9%BF%E5%91%8A%E4%BB%A3%E7%A0%81 "IDA分析应用广告代码")
  + [frida替换广告加载函数](#frida%E6%9B%BF%E6%8D%A2%E5%B9%BF%E5%91%8A%E5%8A%A0%E8%BD%BD%E5%87%BD%E6%95%B0 "frida替换广告加载函数")
* [reveal分析广告UI](#reveal%E5%88%86%E6%9E%90%E5%B9%BF%E5%91%8AUI "reveal分析广告UI")
* [frida-trace拦截域名解析请求](#frida-trace%E6%8B%A6%E6%88%AA%E5%9F%9F%E5%90%8D%E8%A7%A3%E6%9E%90%E8%AF%B7%E6%B1%82 "frida-trace拦截域名解析请求")

## 难度

★★☆☆☆

## 工具环境

* 越狱IOS 14.4
* frida-ios-dump
* frida
* frida-trace
* IDA 7.7
* reveal

## 思路分析

移除app内部的广告有很多种方法。

* IDA分析maco文件，定位广告代码直接移除。
* frida hook网络请求，拦截广告请求。
* reveal分析应用的UI，隐藏广告的view。
* 拦截域名解析请求并重定向。

## IDA分析应用广告代码

砸壳后扔进IDA分析，在函数列表搜索广告的关键词adver。

![](https://zgao.top/wp-content/uploads/2023/05/image-26.png)

从方法名可以判断createAdvertisementBannerView应该是创建广告视图的方法。

![](https://zgao.top/wp-content/uploads/2023/05/image-27-1024x372.png)

查看交叉引用，分析上层的调用函数。

![](https://zgao.top/wp-content/uploads/2023/05/image-28-1024x452.png)

上层函数中代码中有许多操作包括初始化类、调用方法、存取对象属性和一些内存管理操作（比如objc\_retain和objc\_release）。

1. 创建一个AdvertisementIdentifiers对象，并使用多个参数来初始化。
2. 创建一个AdvertisementBannerViewConfiguration对象。
3. 获取应用的代理，可能是为了取得根视图控制器。
4. 通过AdvertisementManager类创建一个广告横幅视图（BannerView）。
5. 根据某些条件判断，会获取应用的主屏幕尺寸并设置到广告横幅视图（BannerView）上。

![](https://zgao.top/wp-content/uploads/2023/05/image-29-1024x502.png)

### frida替换广告加载函数

```
var baseAddr = Module.findBaseAddress('ThePiano');
console.log("The Piano base address: " + baseAddr);

var targetFunctionAddr = baseAddr.add(0x6E854);
console.log("Target function address: " + targetFunctionAddr);

const targetFunction = new NativeFunction(targetFunctionAddr, 'void', []);

Interceptor.replace(targetFunctionAddr, new NativeCallback(function () {
    console.log("跳过广告加载的偏移地址 0x6E854");
}, 'void', []));

const targetFunctionAddrRootVC = baseAddr.add(0x864A8);

Interceptor.attach(targetFunctionAddrRootVC, {
    onEnter: function (args) {
        console.log('进入广告加载函数的调用函数');
    },
    onLeave: function (retval) {
        console.log('退出广告加载函数的调用函数');
    }
});
```

效果如下：

```
 frida -U -f com.impalastudios.pianofree -l piano.js
```

[](https://zgao.top/wp-content/uploads/2023/05/8d0c2618ef54ecb8756a139bbd7f2612_0_1684413839.mp4)

## reveal分析广告UI

在设置的reveal中开应用的调试。

![](https://zgao.top/wp-content/uploads/2023/05/image-30-1024x617.png)

然后在mac上连接越狱ipad。

![](https://zgao.top/wp-content/uploads/2023/05/image-31-1024x381.png)

在reveal中隐藏广告的视图。

![](https://zgao.top/wp-content/uploads/2023/05/image-32-1024x502.png)

## frida-trace拦截域名解析请求

```
frida-trace -U -f com.impalastudios.pianofree -i "getaddrinfo"
```

通过拦截app内的域名解析，将其重定向到127.0.0.1。修改frida-trace的脚本如下：

```
{
  onEnter(log, args, state) {
    var hostname = Memory.readUtf8String(args[0]);
    // log('Intercepted call to getaddrinfo for ' + hostname);
    // 如果域名中包含google就进行重定向
    if (hostname.includes('google')) {
        log('Redirecting request for ' + hostname + 'to 127.0.0.1');
        args[0] = Memory.allocUtf8String('127.0.0.1');
    }
  },
  onLeave(log, retval, state) {
  }
}
```

![](https://zgao.top/wp-content/uploads/2023/05/image-33-1024x419.png)

Post Views: 1,365

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 目前为止有一条评论

###### ala 发布于2:52 下午 - 5月 30, 2023

厉害

[回复](https://zgao.top/ios%E9%80%86%E5%90%91%E4%B8%89-%E5%8E%BB%E9%99%A4%E6%9F%90app%E8%B0%B7%E6%AD%8C%E5%B9%BF%E5%91%8A/?replytocom=5363#respond)

### 发表评论 [取消回复](/ios%E9%80%86%E5%90%91%E4%B8%89-%E5%8E%BB%E9%99%A4%E6%9F%90app%E8%B0%B7%E6%AD%8C%E5%B9%BF%E5%91%8A/#respond)

Δ

版权©2020 Author By : Zgao