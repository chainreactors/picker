---
title: 复现某APP的最新版本签名算法分析
url: https://buaq.net/go-146916.html
source: unSafe.sh - 不安全
date: 2023-01-29
fetch_date: 2025-10-04T05:07:11.700043
---

# 复现某APP的最新版本签名算法分析

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

![](https://8aqnet.cdn.bcebos.com/1a55456d698d37b777d60c09a7f463bf.jpg)

复现某APP的最新版本签名算法分析

目标安卓版本10.0.2，对其进行抓包并探索sign签名算法分析通过全局搜索sign=在com.jingdong.sdk.gatewaysign和com
*2023-1-28 14:31:0
Author: [xz.aliyun.com(查看原文)](/jump-146916.htm)
阅读量:31
收藏*

---

**目标**

```
function hook(){
    Java.perform(function (){
        var hookclass = Java.use("javax.crypto.spec.SecretKeySpec");
        hookclass.$init.overload('[B','java.lang.String').implementation = function (a,b){
            var result = this.$init(a,b);
            console.log("算法为： "+ b);
            console.log(a);
            return result;
        }
    });
}
setImmediate(hook);
```

通过返回得知

```
>>>算法为： HmacSHA256
>>>51,52,54,54,57,99,54,54,97,101,56,51,52,53,55,97,57,97,56,101,55,98,52,100,48,52,49,55,102,48,50,102
>>>算法为： AES
>>>92,71,-78,37,6,27,-125,-92,21,103,84,15,88,-112,-80,45
```

将算法为HmacSHA256进行加密得到

```
aed1ebaab9e61fcc51ec0ab97fb522f13deea2b57958533c4bd511871806d5b0
```

这与抓到的位数不同
**另寻他路**
通过全局搜索没有找到组装reqest参数的代码，判断组装代码在so文件中。在so文件libjdbitmapkit.so,通过全局搜索sign的关键词，得到了
![](https://xzfile.aliyuncs.com/media/upload/picture/20220313145114-f9852f5e-a299-1.png)
在逐一查看的时候，发现地址00012EB0和00012C4E都写到了该调用的代码
![](https://xzfile.aliyuncs.com/media/upload/picture/20220313145152-10901326-a29a-1.png)
1**最终**
在方法中发现其调用者
![](https://xzfile.aliyuncs.com/media/upload/picture/20220313145219-20b3c3ec-a29a-1.png)
即Java\_com\_jingdong\_common\_utils\_BitmapkitUtils\_getSignFromJni
![](https://xzfile.aliyuncs.com/media/upload/picture/20220313145237-2b1c2e8c-a29a-1.png)
在这个function中追踪到了代码包com.jingdong.common.utils，而调用该方法的getSignFromJni
![](https://xzfile.aliyuncs.com/media/upload/picture/20220313145256-368e19d8-a29a-1.png)
因此，hook为

```
function hook(){
    Java.perform(function (){
        var hookclass = Java.use('com.jingdong.common.utils.BitmapkitUtils');
        hookclass.getSignFromJni.implementation = function(a,b,c,d,e,f){
            var result = this.getSignFromJni(a,b,c,d,e,f);
            console.log(">>> hook = " + b + ' / ' + c + ' / ' + d + ' / ' + d + ' / ' + f + ' \n rc= ' + result);
            return result;
        }
    });
}
setImmediate(hook);
```

文章来源: https://xz.aliyun.com/t/12073
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)