---
title: uniapp apk 抓包与获取JS
url: https://mp.weixin.qq.com/s/P5wBgWQEOQZiXj6WzCYn1A
source: Doonsec's feed
date: 2026-06-29
fetch_date: 2026-06-30T06:05:11.817900
---

# uniapp apk 抓包与获取JS

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/oQ0sWhcqsVn4qHQQVrhZPvnAQpsNQFhPBZtCFrzzgn3WJbMkr2LbBtBVpV866skE8YMicUPTyTNsWzHhn7LC1NcperkFLUicNhynpsiaw4VXfg/0?wx_fmt=jpeg)

# uniapp apk 抓包与获取JS

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 字数 909，阅读大约需 5 分钟

## 前言

之前写的 uniapp 文章的翻新，最近做项目遇到了 uniapp 的，发现还能用。文章只是简单做了整合。

文章内容：使用 uniapp 框架的 apk 的常见特征、在存在客户端证书校验的情况下，如何通过 frida 脚本抓包。

## uniapp apk 的特征识别

APK 包解压缩之后，根目录下存在`dc/squareup`
![3c4bd4af1f79441d8efa32e6b2106273.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnBXZK9JpYKkiaibxAUWfZSRyqjTr4R107icxccmmI3GFfWcWlJ63EP17MwMC5nOib2BWXLlmtnurhF3ibhCEl7ic8cZs7WM8ViaWwl2s/640?from=appmsg "null")

3c4bd4af1f79441d8efa32e6b2106273.png

解压缩的 apk 目录中，常见以`uni-`开头的文件名
![b9f69f3daac2ae0b308d0ed71705b906.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmsib8JOHQKr2w15FVPSb4yucUV93gLGjFD6Q3HNRZW6kqFcm0tibTRSmpWAF1fiaZ1iciaV2Q6ib0pMEAR7icbqB6Z9qysR6qJG2jtus/640?from=appmsg "null")

b9f69f3daac2ae0b308d0ed71705b906.png

## jadx 反编译

AndroidManifest.xml 查看入口 Activity
`io.dcloud.PandoraEntry`
![44f6a0db3f9bfdb49c7ff8beb9587029.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmNicXDScbp0UxZfJdpIulxzFJiaTibkzCmt6u9fX9ORZgFWg8qZsa4hG6W98mAZzWcO0w3nPNp7k6wpAnaC5fAVuTDLc6onz7njM/640?from=appmsg "null")

44f6a0db3f9bfdb49c7ff8beb9587029.png

```
adb shell dumpsys window | findstr CurrentFocus
```

![3b9e6d25229dac0df8a5b78915770979.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkj8NEIJmcCJGIcQATro47EFfC4bzQ15R6bicjibdce2ZP2Na81OmtpWxRNLssHF7mme5ialGQugmpmL1oNNQrPpFG49AppgUng2E/640?from=appmsg "null")

3b9e6d25229dac0df8a5b78915770979.png

在该 APP 中，基座采用的是 HbuilderX 中自带的，自定义的是 uniapp 框架的 js 代码，所以常规的很难找到对应的入口。

解压 APK，常见的 uniapp 框架的 js 代码，一般是从服务器上获取，打包进 apk 的只是一部分用于加载 js 的代码。

但本次是直接将 ruoyi-app 的代码放在前端。
在`assets\apps\__UNI__F04D7C1\www`下就能看到源码
![f74e9871543d0c79835cbb90fbe78307.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVn9ia3InLvJ7Ehh4iadMpPlia9WiaGNt3wE1Ricq2MjkQyl3xjK1VG3kLMJwiaX25qGEEQRufciaEBPjRuEcptt42mSCSSH7Iu56MlmXY/640?from=appmsg "null")

f74e9871543d0c79835cbb90fbe78307.png

## 抓包-未证书校验

为进行签名校验时，可以正常抓包
抓包，代理到 yakit 上
![bdaaa3eb847488f9c3a4dd8cc8b4ffa2.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmhdsuU5COKlEiaZcAZkxuYfcXvSenPibj2ibW8Yr6aiaD3GuV4J7reG17uLLW5jSbWx06MRkibGYv3R0lOlh31ylumCtjOViaajsPK8/640?from=appmsg "null")

bdaaa3eb847488f9c3a4dd8cc8b4ffa2.png

在 app-server.js 中可以看到相关的 API 接口
![7f3e94956b282453a40753e2442ebd7c.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlOiayZbomDuWtnZSlEPBrw5cFzQMyooMoibJoGzv1VE9fv94KP8zMz1ZTroYTnBJpGyklCjB8wI8Jh7plKZFcmibKsv3MWcqDjA8/640?from=appmsg "null")

7f3e94956b282453a40753e2442ebd7c.png

![21e4527c8fd603fb90b55d8190303100.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlf8an35ugTLWOiamib9qZyBAro1bBVo45Xlylia1SI8iaX29rfjksO6RicqNrBGVJtLld9iapibibLSbe3ZHh3N1364Rke9bWpkpaskMo/640?from=appmsg "null")

21e4527c8fd603fb90b55d8190303100.png

## 抓包-证书校验

从网站`https://vue.ruoyi.vip/login`导出 crt 证书，然后 crt 转 cer
参考：

* • 导出证书 https://blog.csdn.net/c5113620/article/details/80384660
* • 证书转换 https://www.zhihu.com/question/401504013

在`RuoYi-App-v1.2.0\utils\request.js`中配置单向证书校验
![7a5cbb99414dfd91901b854baa62ddb6.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkLGmqqickqISketWLahJLqaz5AeLa6Wh4DPFibm1rgNcHhEWI1KEy3rnpueoxkH31843JicKrqK0x0ibRC0RlzNswlYsE4DKbPtP8/640?from=appmsg "null")

7a5cbb99414dfd91901b854baa62ddb6.png

```
uni.configMTLS({
  certificates: [{
      'host': 'vue.ruoyi.vip',
      'server': ['/static/ruoyi.cer'],
  }],
  success ({code}) {}
});
```

Hbuilder 运行代码到 Android 设备，未代理到 yakit 时
![e808ec87033b8e4b57a8968ebfef0025.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkjnp4TAzvKNUial4Okv9MohuXrK8pAh00fJibEk1doUCn6YqoQGJAUOEE9zWPzzgeZMxVtft0ibGgxk6hCEQG3xRqrGE8NUrg4bM/640?from=appmsg "null")

e808ec87033b8e4b57a8968ebfef0025.png

代理到 yakit 抓包时
![a07774569957372e09a7270b607481a3.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnB7wJSYkFFA9GtNAYVnQMS0B6Bup9Niay3Uyx9z6E4azHAZtkNGNJFDEfpEatWccOic2JD1Kibibjl9JLdKtQMz46ia7Hvatm3iaJJk/640?from=appmsg "null")

a07774569957372e09a7270b607481a3.png

## uniapp 抓包

Frida 脚本：https://github.com/windy-purple/uni\_app-Packet-capture

项目中的 uni-app.js 脚本，有一点需要注意的，就是在函数`printResponse`。该函数的目的是打印响应包，但在打印响应体的时候，用到了

```
var bodystr = bufferobj.readUtf8();
```

而在**OkHttp**中，response.body().source().readUtf8() 这种读取方式是一次性的，一旦你读取了数据流，它就不会再被应用程序读取到了。直接使用上述的脚本，app 无法正常接收响应包。

替换脚本中的函数`printResponse`，新代码如下：

```
    function printResponse(response) {
        var code = response.code();
        var Headers = response.headers();
        var message = response.message();
        var Protocol = response.protocol();

        var content_type = Headers.get("Content-Type");
        var headers = Headers.toString();
        var protocol = Protocol.toString();

        console.log("[Response]:")
        console.log(protocol + " " + code + " " + message);
        console.log(headers);

        var responseBody = response.body();
        if (!responseBody) return response;

        var source = responseBody.source();
        var Long = Java.use("java.lang.Long");
        source.request(Long.MAX_VALUE.value); // 缓冲整个内容

        var buffer = source.buffer().clone();      // 克隆一个新的缓存，不消耗原有的

        if (ContentTypeIsPrint(content_type) == 1) {
            console.log(buffer.readUtf8());
        } else {
            console.log(buffer.readByteString().hex());
        }
        return response;
    }
```

执行脚本：

```
frida -U -f com.ruoyi.labs -l uni-app.js
```

成功打印了请求和响应
![17a41cdc9de2189338e2fe91ee371222.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlXBiauEvmibiaicURMv2Yib9iclnwYXEW08VQoMpk5t85Uj26Z8ibXZ4WibfOtVWibeDus4qpdUctMvuN0WZIWNY2tW7MaqbIVz680cS6E/640?from=appmsg "null")

17a41cdc9de2189338e2fe91ee371222.png

除此之外，我们还可以用`ecapture`
在 Android 设备上运行

```
./ecapture tls
```

也可以抓包包
![9aa776e24e00afedfe400aa8f89d0318.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlNShwib8OBB5bfICe5iaw08PGaibLHgMzwTPPiaVEicsN8FQ7OFczpryz0Ggsp8TbJNGZJ0jhNHiaRu1fiaIFD2BUMnoQo7Mznibzz4ic8/640?from=appmsg "null")

9aa776e24e00afedfe400aa8f89d0318.png

## uniapp 导出 JS 文件

原本

```
if (Java.available) {
    Java.perform(function () {
        let WXSDKInstance = Java.use("com.taobao.weex.WXSDKInstance");
        WXSDKInstance["render"].overload('java.lang.String', 'java.lang.String', 'java.util.Map', 'java.lang.String', 'com.taobao.weex.common.WXRenderStrategy').implementation = function (str, str2, map, str3, wXRenderStrategy) {
            console.log(`WXSDKInstance.render is called: str=${str}, str2=${str2}, map=${map}, str3=${str3}, wXRenderStrategy=${wXRenderStrategy}`);
            this["render"](str, str2, map, str3, wXRenderStrategy);
        };
    });
}
```

![4b2ca0632afeace727e89a9e1a3ac01e.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVmadjfXrnYcEnH3VchMiaD5UnwW1Q8iaEwCAdFKTZnkZVJ95sLRoenAQaabe0Kdj9xOal7tDgytuRg7eicuRXIIMV4ADIjicUvnoEo/640?from=appmsg "null")

4b2ca0632afeace727e89a9e1a3ac01e.png

**保存到本地**

创建文件

```
mkdir /sdcard/Download/demo-js
chmod 777 /sdcard/Download/demo-js
```

Frida 脚本

```
if (Java.available) {
  Java.perform(function () {
    let WXSDKInstance = Java.use('com.taobao.weex.WXSDKInstance')
    WXSDKInstance['render'].overload(
      'java.lang.String',
      'java.lang.String',
      'java.util.Map',
      'java.lang.String',
      'com.taobao.weex.common.WXRenderStrategy'
    ).implementation = function (str, str2, map, str3, wXRenderStrategy) {
      // console.log(`WXSDKInstance.render is called: str=${str}, str2=${str2}, map=${map}, str3=${str3}, wXRenderStrategy=${wXRenderStrategy}`);
      this['render'](str, str2, map, str3, wXRenderStrategy)
      write_file_1(str3, str2)
    }
  })
}

function sanitizeFileName(fileName) {
  // 移除路径分隔符等非法字符
  return fileName.replace(/[\/\\:*?"<>|{}]/g, '_')
}

function trimUnderscores(str) {
  // 先去除空白字符，再去去除下划线
  return str.trim().replace(/^_+|_+$/g, '')
}

function write_file_1(filename, data) {
  //frida 的api来写文件
  filename = sanitizeFileName(filename)
  filenam...