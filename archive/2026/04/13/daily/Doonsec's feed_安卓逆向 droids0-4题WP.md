---
title: 安卓逆向 droids0-4题WP
url: https://mp.weixin.qq.com/s/eBEtzUm8orJrSp60Zmwijw
source: Doonsec's feed
date: 2026-04-13
fetch_date: 2026-04-14T04:41:08.566378
---

# 安卓逆向 droids0-4题WP

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/94kIPh1QgiaDwk41PgK5oAtMFPde28TK2ibS2XkYpjv88UGWRl4oOk9ywk8ic49pViaVJp5MeTZwk9UMxYXLvOS6eJXQ4Z69ia4pWcCibTJy4xRuQ/0?wx_fmt=jpeg)

# 安卓逆向 droids0-4题WP

原创

朝阳
朝阳

Sec朝阳

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# droids0

拿到题先上 JDAX 审计一遍。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaD8TLqqicsDFXoXgzvkDKpouYyvOOhwlmRbyqZuOp5TmSfMYNAW29r4uOboiaicnpt1zE3dW4mhGMup5HEWsG9ThcsPdPKkv0rOhc/640?wx_fmt=png&from=appmsg)

下面是题目提示，找日志相关内容。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaDu7TzY35HWibI2qWvqYwoWt85P1aeNDKZvN8dD9njDRuvrVY0ictx5ic4InRMdwc1yT03KX91hViahXTKlkF1hl8bcNFyuQYNiazzY/640?wx_fmt=png&from=appmsg)

简单审计一遍 Manifest，先看 Activity。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaDEjNoBL936d7u4icDD8QsA4eGib8s0fMHsVBaGviaqWE5NIpAeBKj7Rgcv54eRVoqIHHZyv6KPKxBnibmAEZXCuXV4IMOBpUwyQ6Q/640?wx_fmt=png&from=appmsg)

picoctf，我们这个题库的网站。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaBKiaVe5qzOSNzTf20PLzS6p7jppzOMO5P6sz6NP9Gg0IyRAG8ica1mqZA3nsfB6c1ON9QjpViacGYLe3jey8ehABhNicB1gGWKaq0/640?wx_fmt=png&from=appmsg)

ok啊，开启了一堆的可调式，备份、调试等操作。

这里我们可以 ADB 调试了，并且允许 ADB bakcup 备份了，根据我们这道题的描述，去找日志，大差不差是用备份功能找 flag。

分析这个程序主入口。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaD8yy3tf3S16K37QbJHzYHyibXtCicbS0AhgyNpzyenHAib1IxvgWFjDuO6pKJaJuUBXTsrZtpbV5xwzJVicZqvGiaj9Q3Eicmw6Awo4/640?wx_fmt=png&from=appmsg)

我们能看到会调用一个子类，并且能看到他的生命周期。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaCdvV9LqaLlwxByz0fo8zP4icDmV5SbSxnBAMC98siajrtsq1Re2le2u2VJtcWWBq8hiapvSquAdS2Scicok8LzzRNzDjQvnl9qXK8/640?wx_fmt=png&from=appmsg)

这个位置比较可疑。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaBcVUBgPZMJUJZQVicXrPhGYG80YpfINRFhxp8icAxo34G1pbickmlpvINuDXMN8OMhIIzR5PLrFnNZeXlFYtwyib1vURX2twKbWhQ/640?wx_fmt=png&from=appmsg)

看看这个程序，又是输入东西给 flag 的题。

我们审计了一遍，就这个 System.loadLibrary("hellojni")，这个是 Native Library 加载，意味着 App 在启动时加载了 libhellojni.so 这个 Native 库。

我们要找的 Flag 有可能在 Native 层。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaCicfz69CV5iakNVib332B2NLFqMwgTA4PR4VsnXKYwGic6LqQ1UF4BaLUGJRiajjePzAeAibXT3RjrfGnJdgRlXibr3nz2llTS6eZo10/640?wx_fmt=png&from=appmsg)

这里也是非常关键点，靠的是我们输入的数据来得到这个 Flag 了。我们去看这个 FlagstaffHill 类。很可能是个包装类，真正逻辑在 Native 层。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaDCEqJuMyzI2rjfma9oibqxgPjq0EeHC07ia1UFtsaFAQDIDc5FvdZ8v2ObZricKDs8s4WRzhhxsjickWKVc3F2gGmicaiaWOmFSdiaHw/640?wx_fmt=png&from=appmsg)

不出所料了，啥都没有，能看到是有个 native 字样。这段是回复功能了。

去找 so 文件。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaDicUX1w8CBkENgoVnmoy8peYC9Af3hCnfDy4KpicfibVsQf99hg5A9icGHAGmF8aFkljX3AGlDsRB7PNVF62MkWxBD32yiczmNHklc/640?wx_fmt=png&from=appmsg)

接下来就是最擅长的逆向了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaAnhtINibBVvaYR05VgE7IlublJQKknibYjRSDkZYB4cb34dN3YZicYPibsZxKY4Nqn4ghDQ9ibjYEd2SeypmSa6tjFG3uTpSdY7LWU/640?wx_fmt=png&from=appmsg)

我们找到了这个 paprika 相关的函数，这个函数是调用 Flag 的，我们去看 marjoram()。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaARClm5uhs6iaT27K68JN8I3B8Gia2Wc4IZf3JE9tAjj52atFvbw8LcQQqDHV1ibnFENaUcZDcNyhUmiba8GD66jvvLwntkibMGSSFI/640?wx_fmt=png&from=appmsg)

这段函数，还要再追踪。

adb -s 127.0.0.1:5555 logcat

做到这里其实跑偏了，应该往日志靠的。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaDSRAwibgQV6ibNqVJwWAkggN1WTl0nQxKNZqYMuiapHemonudKTxbE2dsfVdia5iaXAx9qRcQdEib5v3JtVkhguibPK9WlXMU3wmXQiaU/640?wx_fmt=png&from=appmsg)

都在日志里。

# droids1

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaCZ5ksk8em4poxgKdKd2Ks0rcqDYhunB7TmZUnUze1eO9ia6VGQhbKWiah74RJ95icoLmPk9p0S7aoibkDj42K4DQYX6pynlSkoOvI/640?wx_fmt=png&from=appmsg)

ok啊，找密码。

依旧静态分析，眼睛看一遍。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaBibcsZdITXZ0WszVM0vTkWa2BpnLIQ6E0nEiaQRLWdCI5jrLMNgXHAO0xEaibGU8IMqoD5BosibBKKX8yw8KwibdfApZaQbGg5yGZE/640?wx_fmt=png&from=appmsg)

依旧是各种调试，但这道题是找密码，根据这个思路我们大概能找几种东西，Java 代码、so 库、日志、adb shell 等等。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaDr8Lxkntklc1r4cOib82uWOEeSsBrbtKBprU32pj4A0NlpAp6BszIVyQLRkRRBP2fZe6XEibxZSxuqepTgAjsVICEtMSynchtYY/640?wx_fmt=png&from=appmsg)

恶心，他们都一个界面。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaCF9kvcaUawYmoUz7Fib7CzteG3gJFy3eAd9gD4dGAYCGMd85G476bWnqOaxPwo3ZhaCJeNUDCKib3jOk3M0B9aviarSQE3LcE6ibc/640?wx_fmt=png&from=appmsg)

无比经典，我有点怀疑我是不是搞错文件了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaBcRRjVkjD5FVBfApq0dwLQZZaAT2KqfdDdXe71H1EhUYAiaOcTPfgoV9ndkR1vBbOiagxqvFV1wKttcHiaLpAzd8Q0m3rXphTibibg/640?wx_fmt=png&from=appmsg)

这里在判断我们密码是否正确啊。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaD99FicNWGicRhRFOo4vGcSzdlkY72t0rVEyHVibpsEdVniagKvoxoa2YKm2icrrAuborzLhHjiaUwTJXtyHxQMO9OjUicn0qrqPsM6iao/640?wx_fmt=png&from=appmsg)

adb shell 里面没找到，再看看别的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaBZYLVJOtU3kzbw2sQvH7icGFucyzvicMwibkY4pZpw7RwicSD9RLY27zy1x78x1KsNfQaBAYHQD6XjGA8WVScol8hAGXyMTxUtDVI/640?wx_fmt=png&from=appmsg)

恶心，这个位置。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaAnkAyR0rpupnsJia5iaECqnPiafP5YKptaQ39YmHdIdHfeEwYhAVs6ficcbiaibRia5SyskK3qRKgDhicqGsIUlhPxj9PhDic1J9iam4KLg/640?wx_fmt=png&from=appmsg)

# droids2

依然是找到密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaAa8rRxYYb2kPl9hWWTibNSLbrAWCAXXY2iacS6VlicXjdFd0S4lJibLmavmFXNGs5Nx9KicZqQlTsJbOcoW16Lna4ONx7m6wtcU3Xg/640?wx_fmt=png&from=appmsg)

直接审计这一段吧。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaDnzImfwUyhCkGealwohAgZDQLE8XMdyNz75icWMC79dBvxaZg8g2zrsS9BgOfEhKbySnmWO2HHuLr5PSibFh5pHXXXYTxeicWN80/640?wx_fmt=png&from=appmsg)

这一段有意思了。

定义了一个数组 witches，0 是 weatherwax，1 是 ogg，以此类推，然后他做了一个计算， second = 0，third 为 1，fourth 是 2，然后fifth 是 5 ，sixth 是 4，这里猜测一下是不是顺序啊，还是啥东西。

看倒数第二行就行了。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaAa7gLeTPZRwchl6LxZevcVNiasW0ZFChdtRrJiauEc9HjLBkicFpO5AnwwSRXiaLkVDDnCwu84BiaADtHLUP7IuB6rbPbdseucFhDY/640?wx_fmt=png&from=appmsg)

这里面第一个 fifth 是 5，那他就是 dismass,然后用“.”拼接。

dismass.ogg.weatherwax.aching.nitt.garlick

最终密码。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaDD2ud8oIG4Zq2FjuUwKDNnI98zK7TYGnpHmz21YkjBkgZZ8gI9sib8Fib285ghScyiaO5JV68Zb6v5Lyy9SBKOGichgwHjmIS0V8g/640?wx_fmt=png&from=appmsg)

ok,一个简单的逻辑题。

# droids3

依旧是找密码。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaCBCwMgia6yqUH1DppnJOfMzSOqicdK5lWykGdlJVlWLW6wzkFtFDThEVaQ4icpEUBMFbt0ypa83RpOeOESJ69sEIfIeSA7YibkEjE/640?wx_fmt=png&from=appmsg)

勘验逻辑，还是去找一个密码。

这里尝试 Hook 一下。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaD8nzMfNAKF20HJds8eeX2foh6bZ20ahicUh1KPt2qrPQmPNYq73Gic7X2WE2BQ92PXM0tWlTs2IG5qaprzYibrppicCce7cukmibQA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaD6ImpqH2YczNK4oeZwNWIHpLrSwTgVpic0Mib6hTYV7urzA7HI9dA8DmyGEqIQRSZdwuxA2F0wA76vEjgRbIVuvvFa9BrXvktVs/640?wx_fmt=png&from=appmsg)

我们先启动我们的 Frida-server。

Java.perform(function () {

// 1. 找到我们要下手的类

var FlagstaffHill = Java.use("com.hellocmu.picoctf.FlagstaffHill");

// 2. 修改 getFlag 方法的实现 (implementation)

FlagstaffHill.getFlag.implementation = function (input, ctx) {

console.log("拦截成功");

console.log("输入: " + input);

// 3. 开发者调 nope()，强行调 yep()

var result = this.yep(input);

console.log("强行调用 yep() 后的结果是: " + result);

return result;

};

});

这里是这样的，我们加载了我们的 hook 脚本，然后在执行程序，他会在模拟器中重新启动，这时我们随意输入即可。

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaCpmfbTAmwcU7pQVuGNnAUibfQibjib9EaTENPtRS5y5fEykibibAuUT6fCvsg0ahEIIicIGm2s34ozAib2BcVLgKZ4B4NA5nzlwqAYHI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaCEJlibU3BLQ2Bs2b7labHqIicnDPD42uyPehPCfZLULDXYDBpYf3OVklcUZ5r7BibXGQic1h0GCKs8Et1gkFCvibn0V9rrfibotVjVk/640?wx_fmt=png&from=appmsg)

# droids4

![](https://mmbiz.qpic.cn/mmbiz_png/94kIPh1QgiaBNEU60Rd8w7wLSzEJB8cY7Xu3UCLhflt9uGniamiakREVPoNzYh3x2KfHaWKv0klSMl51gwkhXl3x3ZQk9y9Ckaxqr0nOZib1Otc/640?wx_fmt=png&from=appmsg)

这道题看着上难度了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaBmAPk0Yxargm3ApkTCbaicvq0wdEqeSJsmzxiasd1eibXhhjSiaibpfSb4icwfTnGHPl9ibbC8VYPU3nGPu7oicrGeq9ibusHiboibbfKrVI/640?wx_fmt=png&from=appmsg)

如果是计算解密的话，那在线算力大爆炸时代，这东西秒杀。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/94kIPh1QgiaAs5gb4Hg2unYCuh2javVxtUVFZeGrWssrLqgE5zrTgPaZIw1fSRVj3JYD4WutzUgzTYhDVYQZSW9uc1ia5VM45ibc65D5M3xOVw/640?wx_fmt=png&from=appmsg)

失败，这道题应该还是 Hook 了。

![](https://m...