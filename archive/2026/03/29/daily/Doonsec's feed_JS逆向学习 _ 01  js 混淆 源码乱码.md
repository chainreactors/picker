---
title: JS逆向学习 | 01  js 混淆 源码乱码
url: https://mp.weixin.qq.com/s/OukApq_PS08tmWL4r6UTcg
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:38:53.696288
---

# JS逆向学习 | 01  js 混淆 源码乱码

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/oQ0sWhcqsVnT7CISN4wpEnMoDRHB2bibUySNgrKpdFclwYbWMhlFsPrZNOrpZI5DeKhzJyAP1NcwNOfdthBsffyD45DzADDbqWOg5WVCk5rw/0?wx_fmt=jpeg)

# JS逆向学习 | 01 js 混淆 源码乱码

原创

进击的HACK
进击的HACK

进击的HACK

![]()

在小说阅读器中沉浸阅读

> 字数 947，阅读大约需 5 分钟

## 前言

最近很多用Codex + mcp逆向JS的文章。

我个人而言，JS端逆向没有安卓端熟练，正好利用大模型把这一块补上。本文是我的解题思路。

我个人用的模型还是以免费居多。以后也尽量争取用免费模型来写文章做题。

链接：https://match.yuanrenxue.cn/match/1

我用TRAE CN + GLM 4.7调用mcp逆向，因为遇到混淆，给大模型卡住了，最后因为上下文太多停止继续运行了。

只能人工充当AI的润滑剂了。

+ 前言
+ bypass 反调试
+ 分析
+ 参考资料

## bypass 反调试

![5a928b0986445ea2acd4d98d3a2cd6ae.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVnGoic7lnaDg0QorA7cjverA4pkcbkQ3icl9EfOujttt9qIjds9Sjbvn6ZBQsoeJu6YUGf63hJYL5HaEkVSbaWoajicogTFYt5wts/640?from=appmsg "null")

5a928b0986445ea2acd4d98d3a2cd6ae.png

右键，Never pause here
![9a32839a43f6b4fbaf34994ba4c987e3.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnvCeFD6Ju4Nx9BlwibG3IDNUgl3VO5VauehKOLopL8B9V3IsrtGrZ41YUkMpor6Sy80KUJlou3YRPu16kYmDn4HxRty8nh5uwM/640?from=appmsg "null")

9a32839a43f6b4fbaf34994ba4c987e3.png

![b5bafe74dd3f21049690955226105d1b.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnuxibnTBwhicXHVwabtak15yU4TYtiapr8kWfla2ewHZjvrcIdGo5vhFEbCibJ3YsmdlkYJu6sK5ZbhoCTt5e3hR6SLCgA7StYesA/640?from=appmsg "null")

b5bafe74dd3f21049690955226105d1b.png

hook console.log

```
(function() {
  // 保存原始方法
  const originalLog = console.log;
  console.log = function(...args) {
    // 可选：不执行原日志，注释下面这行
    // return originalLog.apply(this, args);
  };
})();
```

解决打印**永不言弃**
![e1566fbea66c836bae0e4d2c015153f1.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVn6Qsa5n7HvFcSeP3MITmIt8j70YBvLIlh6WA7s6CAcuWAYTdeKXoDvjA8hXibjW7knBQ4GIHDWNskpJqG4mhymCtBlfkxVT6ZE/640?from=appmsg "null")

e1566fbea66c836bae0e4d2c015153f1.png

定位到代码后，把代码复制给大模型，我直接给豆包的，让她帮我过。

```
// 1. 保护原生 toString，让检测永远通过
const nativeToString = Function.prototype.toString;
Object.defineProperty(Function.prototype, 'toString', {
    value: function() {
        // 被检测时返回原生代码字符串
        if (this === eval || this === setInterval) {
            return `function ${this.name}() { [native code] }`;
        }
        return nativeToString.call(this);
    },
    configurable: true,
    writable: true
});

// 2. Hook console.error → 直接屏蔽所有报错
const originalError = console.error;
console.error = function(...args) {
    // 过滤所有报错输出
    return;
};

// 3. Hook debugger 关键字（防无限 debugger）
(() => {
    const _constructor = window.constructor;
    window.constructor = function() {
        return function(){};
    };
    window.constructor.constructor = _constructor;
})();

// 4. Hook setInterval 防止自身被检测
window.setInterval = (() => {
    const original = window.setInterval;
    return function(callback, time) {
        // 替换掉恶意回调，让它空跑
        const safeCallback = function() {};
        return original(safeCallback, time);
    };
})();
```

然后
![f9650d2c4c6410b9e063ef263de332df.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlCuOXsQJlIg8f5jnonAXfbEe5VQrCDf3bVAQH4wgHR6icCZFAA0HuUjsUYRUoFPNtVr0oYIAzp505mgOtQVAiaoWMgjmcAickzibQ/640?from=appmsg "null")

f9650d2c4c6410b9e063ef263de332df.png

## 分析

链接
![54462aa11ea0bdbe8862a559aa0f08ae.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmVp4HkY1Kv1NH1qsbJqzaaRQm3Bak9VusPGRAzrHlBuiblmtxVvYsoVZNpUPo0UJmtfKpCWKo9NicQ6dWI3n3scD3rkzLX4ffJM/640?from=appmsg "null")

54462aa11ea0bdbe8862a559aa0f08ae.png

主要参数值就是m
下XHR断点
![9b65c0c60796cb485cdcb6a4a42accab.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkh8JX6yuFpRibgl67G66oZTaaWodvrg0wOo8GsCBicRibicfSXJZ4ICjAnIMlgSo12wbJ9L3TVOfN2bZWs6ffVibERqAjajhnGEERY/640?from=appmsg "null")

9b65c0c60796cb485cdcb6a4a42accab.png

分析堆栈
![9ad734aff9fb5f46be5f0ffa9c9a4625.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnXe4MkDWWrWxBxg24Cmlsq4MtOVy54j5JBwongYQGjOhxsFPdzqRbP1iaH6lOib4volfnCuxFxXtPYUd8e8rDGTEI8wVAYCiaYpc/640?from=appmsg "null")

9ad734aff9fb5f46be5f0ffa9c9a4625.png

m: window.match1
![a1d81f9726bc716eeb45b2ed29a0a868.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVn7IqOMdqENFpWHlgQuOCbKicnFcbPFUTNsxx4xcKcKXVJ79yCH2lzluAIS1aiaYCUUicwUCZU5PImZYZfdMaJfZIZGmb4NFjPciaI/640?from=appmsg "null")

a1d81f9726bc716eeb45b2ed29a0a868.png

搜索 match1
![c89ae187760b6356847858a3be7d301b.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlQ2j9ibJs5j9QENibNDD8gI60Q1rydXDXtf48YHyPKq0uXa6abQVNcGOyzMNt1K3OgQdjm402meoBUcq2lqE2T7LstexnGGwcf4/640?from=appmsg "null")

c89ae187760b6356847858a3be7d301b.png

此处下断点
![369d840609da2bdb55e7cce266acf858.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVl8fO4k5BxkN0GHZdozYKMbt7wNkNMUIpQvujLBpIAoBtU7UqytNDsWCrNoPk0G1eKzIxtlpZO9yYiaIIib3yIptjl8m1DJvyOLQ/640?from=appmsg "null")

369d840609da2bdb55e7cce266acf858.png

进入了VM当中
![3573aa55a070c5a84a820b0af0b686d3.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkehyica2iatovbiaheBYv9iaK9TubeveRxnV1aCrfHH7P8WpficYAV5LtulxkiczDwPdmyBB4J6SeA5cFnWs7DN62TmHJWbmibImmdoU/640?from=appmsg "null")

3573aa55a070c5a84a820b0af0b686d3.png

其中的十六进制转义，console打印
![7e78006a7df4d8f46c6255fffe824be8.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVneLFicESIZ2jUq3gfWoEsAEWU0DM0yszBkMJCfR247lzcVcdLPusIGKSJDEyOl2U9pcmN530vAqB90KBEKxIzvsdOIexQl9tiaQ/640?from=appmsg "null")

7e78006a7df4d8f46c6255fffe824be8.png

甩给豆包
![6e4100fd25b1e5f1f05f787b9980655d.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVldhKQOVPepjoibicexHGfMQ3yGfgBPa7Xhm2NpnMhDwbmicTXY4OfEftpMcuJlUiaNliadqreKNIEQNbqFPw6uK3BIkPsmAbYADcUo/640?from=appmsg "null")

6e4100fd25b1e5f1f05f787b9980655d.png

可以知道m的组成
![93b04d263163bc84631c9e60af60feaa.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVnkeutGkGlv0MqYupZOXftj9TENqB7rpf50wMRDMbnHticnlyqjrTjSuXmruluSGDgM3Lum3WkyCiaiaZ8MqjobSYbbhlBHDOdiaOc/640?from=appmsg "null")

93b04d263163bc84631c9e60af60feaa.png

```
var encryptStr = oo0O0(calcTime.toString()) + window.f;
```

调试中，可知前者返回是空，主要是后面的window['f']，它是怎么来的
![f0ce6127892e5c220f11d6a1fb573d2e.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVmHqArfeA08W5meJtv9ahfaWWNEvg1NZHibwk8nZtJzzGG6eER6wP4ib38YIxIeo6TSo68K92EdulwGmjawwlKqYMKJMEfRlm1tA/640?from=appmsg "null")

f0ce6127892e5c220f11d6a1fb573d2e.png

结果
![aceef2e7cec2ee547202a17bd2eb03ec.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVkhxWWy3aXXLKdzWtyiaXPCvXFlFhppQNlPsiajvLRpiaGJNFQVj9FcRt4gzeN1ycmTtFrQJWR6f7oHdQibVWsqlzQZEmY5bZ5S6rI/640?from=appmsg "null")

aceef2e7cec2ee547202a17bd2eb03ec.png

JS格式化：https://www.toolhelper.cn/Format/JavaScript

![58af0787848780a7dc1f65aa57726c74.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVl9VuCVhynYcNLDIsFkY0V212Ry7dcRO3DSKtspgTPwVXmOxRFJqmAPcvmFLrOia9leOElC1672U3iajqk3rGibL3MyXf6XRqAjUU/640?from=appmsg "null")

58af0787848780a7dc1f65aa57726c74.png

在其中发现window['f']
![5bf10bf6103bd30d965fbafff7e86a06.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVlic5nWtfqDeb63SPWa28uz72Y1abI89HvPgDKPWgib1TibJQm6ibpnca2FzoWxJ1icicalygDsLz55c4dZeAhVGoyqZVHen8BwO46vE/640?from=appmsg "null")

5bf10bf6103bd30d965fbafff7e86a06.png

传入的参数

```
var calcTime = now + (16798545 - 72936737 + 156138192);
```

在代码前面补上

```
var window = window || {};
```

最后打印

```
console.log(window.f)
```

结果
![5b98cb36660dfb063eebb370f8769dac.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVk0U0rHrGrP9xvlJaMrg5zMaQPBricDFyOvyl4xQDzcJRcL4E1zibCAtQDHNE9b6HAkmicvSGibicWTQplbwIAM1gLkU265EnE6Nhdk/640?from=appmsg "null")

5b98cb36660dfb063eebb370f8769dac.png

生成的和m的请求中的完全一样
![75f0a66f793d8dbb28960ec61df857fb.png](https://mmbiz.qpic.cn/sz_mmbiz_png/oQ0sWhcqsVkWlf594xiasKOrVCRcicecQbG0Piags87KzRYnaLylhoJSKTzNp9icyQCVWwzwYnbD2fDOQ7wWTyicTmT2dDxrBIypHHMjUa1Aq9ec/640?from=appmsg "null")

75f0a66f793d8dbb28960ec61df857fb.png

验证
![c47932ed0693629e480f402f31c1873e.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVlT5OBWhzM7Ynqh2X9J90afmASr2KHpXtAdEPTJWoibDCicdicm6qQkJZ37R0jG8sej5iaS5CoMlWyzAmwmWcLNiaU5jqYZxcUwC0Kk/640?from=appmsg "null")

c47932ed0693629e480f402f31c1873e.png

成功获取结果
![51682f9a8d754c799519ed52ba308477.png](https://mmbiz.qpic.cn/mmbiz_png/oQ0sWhcqsVm2RKSnkOogj5Ziah24CuNhD4h5b5LDIuNZzBrCBv1Df3VzY4YWbwooFUfdMhKKSTPuyqIWxo5Khs1QwjZ8JaG73jBRmdQiaScH0/640?from=appmsg "null...