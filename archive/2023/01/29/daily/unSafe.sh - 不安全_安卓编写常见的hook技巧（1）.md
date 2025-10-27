---
title: 安卓编写常见的hook技巧（1）
url: https://buaq.net/go-146950.html
source: unSafe.sh - 不安全
date: 2023-01-29
fetch_date: 2025-10-04T05:07:10.276439
---

# 安卓编写常见的hook技巧（1）

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

![](https://8aqnet.cdn.bcebos.com/34fd9c92d483934192921073cb8193f3.jpg)

安卓编写常见的hook技巧（1）

在开始编写hook的脚本之前，需要知道搭配frida进行hook常见js方法一、基础框架// 写js代码hook java代码java.perform(fu
*2023-1-28 15:13:0
Author: [xz.aliyun.com(查看原文)](/jump-146950.htm)
阅读量:30
收藏*

---

在开始编写hook的脚本之前，需要知道搭配frida进行hook常见js方法

## 一、基础框架

```
// 写js代码hook java代码
java.perform(function(){
    var utils = Java.use('要hook的类名');
    var class = Java.use('java.lang.Class')

    // hook 普通方法
    utils.类的方法名.implementation = funtion( 方法的参数a,b ){
        console.log(a); // 输出信息 参数a 也可使用 arguments[0] 输出方法的参数
        send();  // 也可输出信息
        // this 表示当前类
        return this.xxx方法; // 为hook的代码返回值，可以是当前方法，也可以是其他
    }
}
```

## 二、重载方法

```
// hook 重载方法
utils.类的方法名.overload(填写重载方法参数类型(若非常规类型，需填写该类型完整位置，如com.xx.xx.自定义类)如："int","java.lang.String").implementation = funtion( 方法的参数a,b ){
        console.log(a); // 输出信息 参数a 也可使用 arguments[0] 输出方法的参数
        send();  // 也可输出信息
        // this 表示当前类
        return this.xxx方法; // 为hook的代码返回值，可以是当前方法，也可以是其他
 }
```

## 三、构造对象参数（即创建一个对象）

```
// hook 构造对象参数（即创建一个对象）
utils.$init.implementation = funtion( 方法的参数a,b ){
        console.log(a); // 输出信息 参数a 也可使用 arguments[0] 输出方法的参数
        send();  // 也可输出信息

        // 创建utils对象，可将该对象传递给hook的方法，有些方法的参数是对象类型，需要创建对应的对象
        var cls = utils.$new(参数);

        // this 表示当前类
        return this.xxx方法; // 为hook的代码返回值，可以是当前方法，也可以是其他
    }
```

## 四、类属性

```
// hook 类属性
utils.$init.implementation = funtion( 方法的参数a,b ){
        console.log(a); // 输出信息 参数a 也可使用 arguments[0] 输出方法的参数
        send();  // 也可输出信息

        // 获取类属性的值
        var val = $utils.属性.value;
        $utils.属性.value = val

        // 也可通过反射的方法获取类属性的值
        var val = Java.cats(获取到对应的类utils.getClass(),clazz).getDeclaredField(要hook的属性);
        // 设置属性可访问
        val.setAccessible(true);
        var value = val.get(从哪个类中获取utils);
        val.set(为哪个类中设置utils,value);

        // this 表示当前类
        return this.xxx方法; // 为hook的代码返回值，可以是当前方法，也可以是其他
    }
```

以上四种为在处理常见的app进行编写hook的过程中会用到的方法（有一些app例外，需要用到其他frida提供的api等共同进行hook）

## 案例1

一个直播软件的抓包以及对其中的通信过程中加密的字符串进行解密和hook，该软件为没有加壳。

```
new StringBody(a2, Charset.forName("UTF-8"))
```

追踪函数的调用看到了，这里就是对数据进行加密处理之后的数据a2

```
String a2 = com.showself.f.a.a(str2, Utils.h());
```

跟踪com.showself.f.a.a方法，在方法中看不出啥。接着对class a中对方法a的b进行追踪
![](https://xzfile.aliyuncs.com/media/upload/picture/20230128143615-10631c02-9ed6-1.png)
来到了com.showself.f.b下的方法b
![](https://xzfile.aliyuncs.com/media/upload/picture/20230128143625-165f0314-9ed6-1.png)
看到数据就是通过这里进行加密之后传送过去,而key的方法为
![](https://xzfile.aliyuncs.com/media/upload/picture/20230128143634-1bbb886e-9ed6-1.png)
既然知道了整个的加密过程，接下来就开始编写hook。
知道com.showself.f.b.b(java.lang.String)，是加密前的数据。因此对其进行hook，完整的hook脚本为

```
function hook() {
    Java.perform(function () {
    var b=Java.use("com.showself.f.b");
    b.b.overload("java.lang.String").implementation= function(a){
        console.log(a);
        var ret=this.b(a)
        return a;
    }
    });
}
setImmediate(hook);
```

## 案例二

一个没有加壳的动漫软件app

### 分析点

在放到夜神模拟器进行抓包，看到的数据包中均存在App-Info参数的字眼。在观察数据包的发现其可能存在对用户校验判断的数据在里面。
![](https://xzfile.aliyuncs.com/media/upload/picture/20230128143725-39ef333a-9ed6-1.png)
同时该app存在的SSL校验，在之后的测试中已经绕过。

### 参数分析

以该参数为搜索点，通过全局搜索，在AppInfoModel的class中。

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128143748-47b658ea-9ed6-1.png)

最终定位到了该class下进行了重写

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128143756-4c7ff16a-9ed6-1.png)

是通过base64进行加密

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128143803-50b73482-9ed6-1.png)

而其中的visitor\_sign参数

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128143809-54469dc2-9ed6-1.png)

跟踪跳转到

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128143815-57c5ff56-9ed6-1.png)

其中MDUtils方法，为md5加密

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128143821-5b69d8bc-9ed6-1.png)

通过objection得到方法a的值

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128143828-5ff6d420-9ed6-1.png)

直接将参数进行解密会因为复杂性而无法解密得出来，对加密前的原参数进行跟踪

#### Client.p()

通过运行是参数的获取

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128143845-69a44fc0-9ed6-1.png)

得到其方法的值为A:34f770f3177f0146

#### Client.o()

通过运行是参数的获取

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128143851-6db5e736-9ed6-1.png)

得到其方法的值为34f770f3177f0146

### 验证

由a2可以得到在加密前的值为visiter=A:34f770f3177f0146&y-device=34f770f3177f0146经过在线的md5进行加密之后

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128143900-7295ee22-9ed6-1.png)

## 案例三

来自对京东的算法进行分析。

### 目标

安卓版本10.0.2，对其进行抓包并探索sign签名算法

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128144000-96c5e0cc-9ed6-1.png)

### 分析

通过全局搜索sign=

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128144015-9f744f92-9ed6-1.png)

在com.jingdong.sdk.gatewaysign和com.jingdong.jdsdk.network.toolbox中发现对sign的操作

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128144021-a35a0bf6-9ed6-1.png)

由此直接hook最先的加密的class，即javax.crypto.spec.SecretKeySpec
hook构造函数，和普通的函数是有区别的，要用$init这种形式，并且要return this.$init(arg1,arg2)调用原始的函数实现

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

### 另寻他路

通过全局搜索没有找到组装reqest参数的代码，判断组装代码在so文件中。在so文件libjdbitmapkit.so,通过全局搜索sign的关键词，得到了

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128144140-d232c332-9ed6-1.png)

在逐一查看的时候，发现地址00012EB0和00012C4E都写到了该调用的代码

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128144146-d5a434b0-9ed6-1.png)

### 最终

在方法中发现其调用者

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128144159-dd87a644-9ed6-1.png)

即Java\_com\_jingdong\_common\_utils\_BitmapkitUtils\_getSignFromJni

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128144206-e173af14-9ed6-1.png)

在这个function中追踪到了代码包com.jingdong.common.utils，而调用该方法的getSignFromJni

![](https://xzfile.aliyuncs.com/media/upload/picture/20230128144212-e530dd2a-9ed6-1.png)

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

文章来源: https://xz.aliyun.com/t/12075
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)