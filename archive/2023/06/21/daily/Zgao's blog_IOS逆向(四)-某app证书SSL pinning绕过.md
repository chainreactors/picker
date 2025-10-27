---
title: IOS逆向(四)-某app证书SSL pinning绕过
url: https://zgao.top/ios%e9%80%86%e5%90%91%e5%9b%9b-%e6%9f%90app%e8%af%81%e4%b9%a6ssl-pinning%e7%bb%95%e8%bf%87/
source: Zgao's blog
date: 2023-06-21
fetch_date: 2025-10-04T11:44:18.605581
---

# IOS逆向(四)-某app证书SSL pinning绕过

# [Zgao's blog](https://zgao.top/)

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

Toggle navigation

* [工具箱](https://zgao.top/tool/)
* [文章归档](https://zgao.top/archives/)
* [关于我](https://zgao.top/about-me/)
* [github](https://github.com/zgao264)
* Gmail

# IOS逆向(四)-某app证书SSL pinning绕过

* [首页](https://zgao.top)
* [IOS逆向(四)-某app证书SSL pinning绕过](https://zgao.top:443/ios%E9%80%86%E5%90%91%E5%9B%9B-%E6%9F%90app%E8%AF%81%E4%B9%A6ssl-pinning%E7%BB%95%E8%BF%87/)

[6月 20, 2023](https://zgao.top/2023/06/)

### IOS逆向(四)-某app证书SSL pinning绕过

作者 [Zgao](https://zgao.top/author/zgao/)
在[[逆向](https://zgao.top/category/%E9%80%86%E5%90%91/)](https://zgao.top/ios%E9%80%86%E5%90%91%E5%9B%9B-%E6%9F%90app%E8%AF%81%E4%B9%A6ssl-pinning%E7%BB%95%E8%BF%87/)

![](https://zgao.top/wp-content/uploads/2023/06/image-18.png)

渗透测试中经常会遇到app存在SSL证书校验，此时就没办法抓包。需要对ios的SSL pinning的函数进行hook来绕过检测。本文对某app使用frida和objection进行绕过。

文章目录

[ ]

* [难度](#%E9%9A%BE%E5%BA%A6 "难度")
* [工具](#%E5%B7%A5%E5%85%B7 "工具")
* [分析思路](#%E5%88%86%E6%9E%90%E6%80%9D%E8%B7%AF "分析思路")
* [Appsdump砸壳](#Appsdump%E7%A0%B8%E5%A3%B3 "Appsdump砸壳")
* [IDA分析过程](#IDA%E5%88%86%E6%9E%90%E8%BF%87%E7%A8%8B "IDA分析过程")
* [objection ios sslpinning disable](#objection_ios_sslpinning_disable "objection ios sslpinning disable")
* [frida 绕过脚本](#frida_%E7%BB%95%E8%BF%87%E8%84%9A%E6%9C%AC "frida 绕过脚本")

## 难度

★☆☆☆☆

## 工具

* 越狱IOS 14.4
* AppsDump
* frida
* objection
* IDA 7.7
* HTTP Catcher

## 分析思路

![](https://zgao.top/wp-content/uploads/2023/06/IMG_7D3BFBE13B64-1.jpeg)

![](https://zgao.top/wp-content/uploads/2023/06/IMG_47AC7A9614BB-1.jpeg)

我们在ios上使用HTTP Catcher进行抓包，当开启SSL Pinning Bypass（代理为localhost生效）的时候，是可以正常抓到包的。但是我们做测试需要把流量抓到mac上的burp，这时SSL Pinning Bypass是不生效的。

虽然知道是证书校验的问题，我们可以直接用SSL Unpinning的脚本进行hook，但还是用IDA简单分析一下，了解其原理。

## Appsdump砸壳

![](https://zgao.top/wp-content/uploads/2023/06/IMG_8B35A20F73D5-1.jpeg)

最近发现一个IOS上砸壳非常方便的app，Appsdump。支持IOS15的系统，原理就是基于trollstore来进行砸壳的，关键是非越狱的状态下也可以砸壳。

支持单脱主程序，然后使用airdrop隔空投送到mac，是真的太方便了！

## IDA分析过程

既然是证书问题，把maco扔进IDA中分析完成后，直接搜索证书的关键字来定位关键函数。

![](https://zgao.top/wp-content/uploads/2023/06/image-19.png)

双击来的字符串的位置。

![](https://zgao.top/wp-content/uploads/2023/06/image-20-1024x477.png)

查看引用该字符串的方法。

![](https://zgao.top/wp-content/uploads/2023/06/image-21-e1687241902811-1024x445.png)

来到-[UASessionOperation URLSession:didReceiveChallenge:completionHandler:]方法，F5。

![](https://zgao.top/wp-content/uploads/2023/06/image-22-751x1024.png)

`SecTrustEvaluateWithError`是iOS平台上的系统函数。这个函数来自于`Security.framework`，它是用于评估一个SecTrust对象是否可以被系统信任。

该函数返回一个布尔值，如果为true，证书可以被信任；如果为false，证书不能被信任。如果评估失败，会通过第二个参数返回一个包含错误详情的CFErrorRef对象。这个函数在iOS 13.0及更高版本上可用，因此可以看到在代码中有一个版本检查部分，根据设备的系统版本来选择使用`SecTrustEvaluateWithError`或者旧版本的`SecTrustEvaluate`函数。

## objection ios sslpinning disable

objection是基于frida封装的命令行hook工具，可以不写代码，使用非常方便。

```
objection -g <bundleID> explore
ios sslpinning disable
```

![](https://zgao.top/wp-content/uploads/2023/06/image-23-1024x588.png)

## frida 绕过脚本

SSL Pinning的绕过脚本网上有很多现成的，就没必要自己写了。和分析的基本一致，都是hook ssl证书校验的关键系统函数。

```
// Disables SSL pinning by replacing functions with no-ops.
function unpin() {
  var SecTrustEvaluate_handle = Module.findExportByName('Security', 'SecTrustEvaluate');
  var SecTrustEvaluateWithError_handle = Module.findExportByName('Security', 'SecTrustEvaluateWithError');
  var SSL_CTX_set_custom_verify_handle = Module.findExportByName('libboringssl.dylib', 'SSL_CTX_set_custom_verify');
  var SSL_get_psk_identity_handle = Module.findExportByName('libboringssl.dylib', 'SSL_get_psk_identity');
  var boringssl_context_set_verify_mode_handle = Module.findExportByName('libboringssl.dylib', 'boringssl_context_set_verify_mode');

  if (SecTrustEvaluateWithError_handle) {
      var SecTrustEvaluateWithError = new NativeFunction(SecTrustEvaluateWithError_handle, 'int', ['pointer', 'pointer']);

      Interceptor.replace(
          SecTrustEvaluateWithError_handle,
          new NativeCallback(function (trust, error) {

              console.log('[*] Called SecTrustEvaluateWithError()');
              SecTrustEvaluateWithError(trust, NULL);
              Memory.writeU8(error, 0);
              return 1;
          }, 'int', ['pointer', 'pointer'])
      );

      console.log('[+] SecTrustEvaluateWithError() hook installed.');
  }

  if (SecTrustEvaluate_handle) {
      var SecTrustEvaluate = new NativeFunction(SecTrustEvaluate_handle, 'int', ['pointer', 'pointer']);

      Interceptor.replace(
          SecTrustEvaluate_handle, new NativeCallback(function (trust, result) {
              console.log('[*] Called SecTrustEvaluate()');
              SecTrustEvaluate(trust, result);
              Memory.writeU8(result, 1);
              return 0;
          }, 'int', ['pointer', 'pointer'])
      );
      console.log('[+] SecTrustEvaluate() hook installed.');
  }

  if (SSL_CTX_set_custom_verify_handle) {
      var SSL_CTX_set_custom_verify = new NativeFunction(SSL_CTX_set_custom_verify_handle, 'void', ['pointer', 'int', 'pointer']);

      var replaced_callback = new NativeCallback(function (ssl, out) {
          console.log('[*] Called custom SSL verifier')
          return 0;
      }, 'int', ['pointer', 'pointer']);

      Interceptor.replace(
          SSL_CTX_set_custom_verify_handle,
          new NativeCallback(function (ctx, mode, callback) {
              console.log('[*] Called SSL_CTX_set_custom_verify()');
              SSL_CTX_set_custom_verify(ctx, 0, replaced_callback);
          }, 'int', ['pointer', 'int', 'pointer'])
      );

      console.log('[+] SSL_CTX_set_custom_verify() hook installed.')
  }

  if (SSL_get_psk_identity_handle) {
      Interceptor.replace(
          SSL_get_psk_identity_handle,
          new NativeCallback(function (ssl) {
              console.log('[*] Called SSL_get_psk_identity_handle()');
              return 'notarealPSKidentity';
          }, 'pointer', ['pointer'])
      );

      console.log('[+] SSL_get_psk_identity() hook installed.')
  }

  if (boringssl_context_set_verify_mode_handle) {
      var boringssl_context_set_verify_mode = new NativeFunction(boringssl_context_set_verify_mode_handle, 'int', ['pointer', 'pointer']);

      Interceptor.replace(
          boringssl_context_set_verify_mode_handle,
          new NativeCallback(function (a, b) {
              console.log('[*] Called boringssl_context_set_verify_mode()');
              return 0;
          }, 'int', ['pointer', 'pointer'])
      );

      console.log('[+] boringssl_context_set_verify_mode() hook installed.')
  }
}

unpin()
```

将上面的脚本保存为 ssl-pinning-bypass.js 文件。

```
frida -UF -l ssl-pinning-bypass.js
```

执行结果如下：

![](https://zgao.top/wp-content/uploads/2023/06/image-24-1024x645.png)

然后就可以正常的抓包了。

[](https://zgao.top/wp-content/uploads/2023/06/屏幕录制2023-06-20-14.45.45.mp4)

Post Views: 3,863

赞赏

![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114105.jpeg)微信赞赏![](https://zgao.top/wp-content/uploads/2022/02/QQ图片20201028114100.jpeg)支付宝赞赏

###### Zgao

愿有一日，安全圈的师傅们都能用上Zgao写的工具。

### 目前为止有一条评论

###### 匿名 发布于12:00 上午 - 11月 20, 2024

很棒

[回复](https://zgao.top/ios%E9%80%86%E5%90%91%E5%9B%9B-%E6%9F%90app%E8%AF%81%E4%B9%A6ssl-pinning%E7%BB%95%E8%BF%87/?replytocom=9061#respond)

### 发表评论 [取消回复](/ios%E9%80%86%E5%90%91%E5%9B%9B-%E6%9F%90app%E8%AF%81%E4%B9%A6ssl-pinning%E7%BB%95%E8%BF%87/#respond)

Δ

版权©2020 Author By : Zgao