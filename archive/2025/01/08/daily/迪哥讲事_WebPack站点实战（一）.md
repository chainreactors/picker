---
title: WebPack站点实战（一）
url: https://mp.weixin.qq.com/s?__biz=MzIzMTIzNTM0MA==&mid=2247496764&idx=1&sn=2656f1f8649ce812606a4d139437153a&chksm=e8a5fe5fdfd277499844d7c17ca8431872509acf0631e8c14c53d004a62a0921e76e6437597a&scene=58&subscene=0#rd
source: 迪哥讲事
date: 2025-01-08
fetch_date: 2025-10-06T20:11:47.780761
---

# WebPack站点实战（一）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/YmmVSe19Qj5X6ib8cIhCThoaWa5BjNOPVBscTiajwYp5vJs3LfYtoye2htOe2ChL4yYF0Piamqqqyc7VzBPt7ECZg/0?wx_fmt=jpeg)

# WebPack站点实战（一）

迪哥讲事

以下文章来源于一位不愿透露姓名的热心网友
，作者不愿透露姓名的热心网友

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM7EomoAliaxuCKn0blUwibX3ANtxXaSz0vFiaynokNXbMybQ/0)

**一位不愿透露姓名的热心网友**
.

不定时更新一些渗透、逆向及个人心得随笔。

![](https://mmbiz.qpic.cn/mmbiz_gif/Ljib4So7yuWhnpYbTI3NCk6jD5lg2KdJibeaN5NQqSa0CMH4B9aSoVicicrtQ5EO2xAw6yPpXxxicEmFCWv1S2gnJ7A/640?wx_fmt=gif)

文章配套B站视频，很多话语简略了，建议配着视频看。

地址：https://www.bilibili.com/video/BV13F411P7XB/

开始之前了，简单过一下下面几个方法加深印象，便于更好理解加载器。也可以直接从webpack标题开始看起。

## Function/函数/方法

常规的js函数命名方法：

```
//1. 常规function
var test = function(){
    console.log(123);
}

function test(){
    console.log(2);
}
```

今天的主角，自执行函数。

```
//2. 自执行function
!function(){
    console.log(1);
}()
// => function a(){} a()

//2.1
!function(e){
    console.log(e)
     var n={
    t:"txt",
    exports:{},
    n:function(){console.log("function n ")}
}
}("echo this")

//2.2
!function(e){
    console.log(e)
     var n={
    t:"txt",
    exports:{},
    n:function(){console.log("function n ")}}
}(
    {
        "test":function(){
                console.log("test")}
    }
)
//(["test":function(){console.log])
```

## call/apply Function

[Fcuntion prototype call and  applay ](Function.prototype.call() - JavaScript | MDN (mozilla.org))

> 允许为不同的对象分配和调用属于另一个对象的函数/方法。

call和apply的使用效果基本一致，可以让A对象调用B对象的方法：

让`Vx`对象调用`_x`对象的`say()`方法

```
var Vx={
       name:"一位不愿透露姓名的热心网友",
       age:"18cm"
};
var _x={
    name:"热心网友",
    age:"18mm",
    say:function(){console.log("name:"+this.name+" age:"+this.age)}
}
_x.say.call(Vx)
//name:一位不愿透露姓名的热心网友 age:18cm
```

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISaIQQrl156A8X1ibnux0VruE1V9x2YOevF6Uxj4GCnFnuo7l4DWyXNLP6Uhm29XIAleVJvZoqjbHdQ/640?wx_fmt=png)

## Webpack

> webpack 一个静态模块打包器，有入口、出口、loader 和插件，通过loader加载器对js、css、图片文件等资源进行加载渲染。

实战站点：https://spa2.scrape.center/

### WebPack 站点长什么样

方法1. 右键查看源码发现只会有js链接文件，没有其他多余的前端信息，f12看元素就会有很多数据。![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISaIQQrl156A8X1ibnux0VruECDO5EQJ9PKDmX2nf9CoygjE1CibEfbaVg6u3DG5d1Z6X6S1JZ3RnqMg/640?wx_fmt=png)

方法2. 看Js文件，一般会有一个app.xxxx.js或长得像MD5的文件名，然后js内容有很多a、b、c、d、n...的变量来回调用，反正就是看着乱。

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISaIQQrl156A8X1ibnux0VruEUMYSZh1e9VhgyTxNr0YH2kWtLXibWZib3TKokWSBUEO47AOFV0dN1XKg/640?wx_fmt=png)![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISaIQQrl156A8X1ibnux0VruEzWAicDXibLlT9y5Q6JiaAJYAGqYuKXpIeA3ibWlFmLUlykRxMuSeLUWKlQ/640?wx_fmt=png)

### loader加载器

Webpack站点与普通站点的JS代码扣取是不一样的，因为Webpack站点的资源加载是围绕着加载器进行的，然后把静态资源当作模块传入调用，传入的模块就是参数，需要加载什么就运行什么模块。

先简单看一下加载器长相。

```
!function(e){
    var t={}
    function d(n){
        if (t[n])
            return t[n].exports;
        console.log(n)
        var r = t[n] = {
            i:n,
            l:!1,
            exports:{}
            };
        return e[n].call(r.exports,r,r.exports,d),
        r.l = !0;
        r.exports
    }

    d(1)

}(
    [
    function(){console.log("function1");console.log(this.r.i)},
    function(){console.log("function2")}
    ]
);
```

#### 加载器分析

将加载器拆分为两部分：

* 函数方法部分：

```
!function(e){
    var t={}
    function d(n){
        if (t[n])
            return t[n].exports;
        var r = t[n] = {
            i:n,
            l:!1,
            exports:{}
            };
        return e[n].call(r.exports,r,r.exports,d),
        r.l = !0;
        r.exports
    }

    d(1)
```

* 参数部分：

```
(
    [
    function(){console.log("function1");console.log(this.r.i)}
    ,
    function(){console.log("function2")}
    ]
)
/* 这里的参数可以是传入数组，也可以是对象，都是经常看见的。
*/
(
    {
    "1":function(){console.log("function1");console.log(this.r.i)}
    ,
   "2":function(){console.log("function2")}
    }
)
```

这里的加载器是将参数作为一个数组【】传入的，格式为：`!function(e){}(数组)`  参数e就是传入的数组， 接着看：

```
  var t={}
  function d(n){
        if (t[n])
            return t[n].exports;
        var r = t[n] = {
            i:n,
            l:!1,
            exports:{}
            };
        return e[n].call(r.exports,r,r.exports,d),
        r.l = !0;
        r.exports
    }
 d(1)
```

上述代码声明了一个d方法并执行，传入`1`作为参数，`d`方法中的`if (t[n])`并没有实际意义，因为`t`本来就没有声明的，可以缩减为：

```
function d(n){
        var r = t[n] = {
            i:n,
            l:!1,
            exports:{}
            };
        return e[n].call(r.exports,r,r.exports,d),
        r.l = !0;
        r.exports
    }
 d(1)
```

那么`r=t[n]={ xxxx}`  可以变成 `var r = { xxx}`，现在就剩下一句：

`return e[n].call(r.exports,r,r.exports,d)`

前面说过了，`e`是传入的参数，也就是数组；`n`是`d(1)`传入的值，为`1`。

`r.exports` 就是`r`对象里的`exports`属性为空对象`{}`。

转化代码：

```
return 数组[1].call({},r对象,{},d函数自己)

--> 继续转换：

function(){
console.log("function2")
}.call({},r对象,{},d函数)
```

由于`call()`方法是用于调用方法的，所以其他参数可以忽略，缩减为：

```
function(){
console.log("function2")
}.call(d函数)
```

加载器并没有太多实际的意义，就是自己调用自己，只是用来混淆的；

经过分析后代码可以直接缩减为（当然，只是针对现在这个例子）：

```
!function(e){
    var t={}
    console.log("自执行传入的参数是："+e)
    function d(n){

        return e[n].call(d)
    }

    d(1)

}(
    [
    function(){console.log("function1");console.log()},
    function(){console.log("function2")}
    ]
);
```

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISaIQQrl156A8X1ibnux0VruEZmCibnnt2Klb8ArkQFeicfCSRQSaLicQcHhDiatBIKEQ9QaEQkFH5OkpPA/640?wx_fmt=png)

#### 分离加载

在模块较多的情况下，webpack会将模块打包成一整个JS模块文件；并使用`Window`对象的`webpackJsonp`属性存储起来。然后通过`push()`方法传入模块。

如下：

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISaIQQrl156A8X1ibnux0VruEWy9L11icoQ48bfW7Paqne6T2q7GsegvRxeeHPlL19dOksYFehemVvng/640?wx_fmt=png)

格式为：

```
  (window["webpackJsonp"] =
   window["webpackJsonp"] || [] ).push([
       ["xx"], {
                              "module":function(){}
  }
  ]);
```

运行结果：可以理解为appen追加内容，向webpackJsonp属性追加了[xx],和mod数组

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISaIQQrl156A8X1ibnux0VruEX5EyZpD9FJ6CAtGdefIEVJgu8uEKpsbjuOjIYWLANFNsaDv58hZpAg/640?wx_fmt=png)

### 总结

> 通过两个加载器的两个例子可以看出，加载器的重要性；webpack站点能否成功解析，是围绕着loader加载器和模块资源进行的，加载器好比是一口锅，而模块好似食材；将不一样的食材放入锅中，烹饪的结果都是不一样的。

## WebPack实战

### 分析加密

Webpack站点分析的思路主要以下两点：

1. 首先找到食材，也就是定位到加密模块
2. 其次找到锅，loader加载器
3. 使用加载器去加载模块

在这里的的难点就是定位加密模块，因为调用加密的地方肯定是只有固定的一两个点，如：登录提交。而加载器则什么地方都在调用（网站图片、css、js等资源  都是通过加载器加载出来的）

在上一文《[JS逆向｜40分钟视频通杀大厂登陆加密](https://mp.weixin.qq.com/s?__biz=MzkzODEzNjA3MQ==&mid=2247485456&idx=1&sn=839bffe306d8fa8563bce289cf352791&scene=21#wechat_redirect)》视频中已经讲解了常规加密的快速定位办法，在webpack站点中使用这种定位办法也有概率可能会有效，其实加密点也是有规律的，如：

```
//1.
xxxxx{
    a:e.name,
    data:e.data,
    b:e.url,
    c:n
}
```

这种键值对格式的跟ajax请求长得很相似，有可能是请求赋值的地方，也不绝对，只是大家注意就好。

访问站点右键源码就能发现这是一个webpack网站，数据并不存在于源码之中，是通过XHR获取的JSON数据。

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISaIQQrl156A8X1ibnux0VruEdFpmBBN3SiczU69cib92deBKsAMncMZ3w1R0X5LtdJymgDhLhSRdwWicg/640?wx_fmt=png)

发现是这么一个URL请求的：

```
https://spa2.scrape.center/api/movie/?limit=10&offset=0&token=ODkxMjNjZGJhYjExNjRkYTJiMmQzMWY3NGY2NTE5YjZlNGIyN2M5YiwxNjU5MzM4MDg4
```

翻页观察发现，`limit`固定不变，`offset`每次增加`10`。两个参数分别是展示的数量与展示的开始位置，`token`是什么信息暂时未知，但是是必须要解开是。

通过XHR网络断点对所有XHR请求URL进行匹配，只要URL内包含`api/movie`关键词就进行下断。

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISaIQQrl156A8X1ibnux0VruEjBHxTG39ias5ibqg4FqbG1HzeQzlDxqyDXPOwciacch3DEp6bwicsQia9bw/640?wx_fmt=png)

成功断下会展示具体在哪个uRL断的

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISaIQQrl156A8X1ibnux0VruEsM4KoVKhgya2UZbWMRIkw7ctfRTquqUoXfT4Jx2h5mXSLiaqtepiaQbg/640?wx_fmt=png)

观察堆栈挨个找

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISaIQQrl156A8X1ibnux0VruE9tcFsib8qliahAxYicOVXB6jh1ibicv9SibO0tq1OoNQfe0daE1icMQ0Mo7QQ/640?wx_fmt=png)

具体找法视频内会详细讲，文字太麻烦了 :sleepy:，一系列操作之后，定位到了加密位置`onFetchData`:

```
Object(i["a"])(this.$store.state.url.index, a)
```

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISaIQQrl156A8X1ibnux0VruEOhnTkI4JxwM3OBoL411qJiakPRKjdNu0c2icaO6zrAM4551tR300WUicQ/640?wx_fmt=png)

`this.$store.state.url.index`和`e`分别是 `/api/movie`，`0`（`url`中的`offset`翻页值）

![](https://mmbiz.qpic.cn/mmbiz_png/gh2J6kIbISaIQQrl156A8X1ibnux0VruEQwpDE4gd06ibyia1ia8VDjcjWXqFymJ8LFzBibcrSe3Mq8L35Q6iaACcOuA/640?wx_fmt=png)

加密算法也就是：`Object...