---
title: frida-labs经典12道题目
url: https://mp.weixin.qq.com/s/I64LwJ5vXkQtjMVhm5-7uw
source: Doonsec's feed
date: 2026-04-14
fetch_date: 2026-04-15T04:39:16.266817
---

# frida-labs经典12道题目

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6nhGiavBDP4bRibY2iayquMxtakGpWOXI81TiaXu31HknPpNs1kZ5kqibmCt9HYm7b4DEJnHhW11vde8Ip5q4RORa5aH8u6cAV51n4wKw3XhUNCs/0?wx_fmt=jpeg)

# frida-labs经典12道题目

原创

李北辰
李北辰

SPEEDCoding

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

frida-labs下载链接：

```
https://github.com/DERE-ad2001/Frida-Labs
```

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4bNfAGXhk4eibWuxziaAqjQTYOzN7jibhsqvqIrkqBy6ibOG5dgdic9c2e6ibUPJYgPOfibKpYfTELCtIftsDGCPhYKKgic4BibJnTNGzIY/640?wx_fmt=png&from=appmsg)

一、Frida 0x1：hook一个方法

反编译后代码如图，用户输入的字符串必须是数字，然后生成一个随机数，要求是随机数乘2加4等于用户输入的数字才可以输出flag。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4biccdp91iag1rSxmt68A9CKtzqsZRDf0J6jLiaavQWO6IzOTcvahwicmJ53Ueia2H3FmTsSedmTL22XOXmneF6gGRCrdKfQS0dLllc/640?wx_fmt=png&from=appmsg)

本题练习的是使用Frida来hook一个方法，然后修改输入参数使满足条件。首先hook掉check方法，把输入的两个参数直接修改成符合条件的，然后hook掉TextView的setText方法，使该方法在调用同时在控制台打印flag值。hook脚本代码如下：

```
1.hook掉check方法；2.修改check方法的参数；3.hook掉TextView的setText方法；
```

```
Java.perform(function () {    var mainActivity=Java.use("com.ad2001.frida0x1.MainActivity");    mainActivity.check.implementation=function (p0, p1) {        console.log("check() is called, 修改前:p0: "+p0+", p1: "+p1);        p0=1;        p1= (p0*2) +4;        console.log("check() is called, 修改后:p0: "+p0+", p1: "+p1);        this.check(p0, p1);    }    var textView=Java.use("android.widget.TextView");    textView.setText.overload("java.lang.CharSequence").implementation=function (p0) {        console.log("setText() is called, p0: "+p0);        this.setText(p0);    }})
```

执行结果如下，hook成功：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4bmbVqibp1icicPM1wU1alSDdia8IX0FlXCanibBJPco7tPPrQic6wx1PNnQvKemZjtdKz9ELPcRPNYC6XrKgIp8NJnomEWWLPJib0micU/640?wx_fmt=png&from=appmsg)

二、Frida 0x2：通过hook主动调用一个方法

反编译后代码如图，单纯就是一个简单页面，什么交互都没有，查看反编译后的代码，发现有一个静态方法get\_flag没有调用。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aicFwrmQhBWZ9jxLcgyfONXLvDKfAlO5c55w0qG1cJO9BMFqOOicibs2BTXg9QGA46VDwzpibduW0jP5ueDia8I7fEGJnLVZysFRLA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4bvCIyCIAP1icesfoyfGgiayuYFuomxe9DKLQb19BYyWkYXHebz1vjOT67MxNg76SyKvYPiacJFv6ohRfRqV4WmkgXOApW6LfH7dM/640?wx_fmt=png&from=appmsg)

本题需要将onCreate方法hook掉，然后主动调用在源码中未使用的静态方法get\_flag。

```
1.hook掉onCreate方法；2.主动调用get_flag方法；3.hook掉TextView的setText方法；
```

hook代码如下：

```
Java.perform(function () {    var mainActivity=Java.use("com.ad2001.frida0x2.MainActivity");    mainActivity.onCreate.implementation=function (p0) {        console.log("onCreate() is called");        this.onCreate(p0);        this.get_flag(4919);    }    var textView=Java.use("android.widget.TextView");    textView.setText.overload("java.lang.CharSequence").implementation=function (p0) {        console.log("setText() is called, p0: "+p0);        this.setText(p0);    }})
```

hook成功，执行结果如下：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4aRjkEMnoQogML87CiclWXWHubesZns9ZmicXkXibHNiazSwraYYJl8ItHeGNxZzop5yWe9WBAJ7m7hCJAu4oKoGx6xEibvtGB6YMxg/640?wx_fmt=png&from=appmsg)

三、Frida 0x3：通过hook修改类的静态变量

反编译后的代码如下，按钮绑定了一个onClick方法，点击后对Checker类下的静态变量code进行判断，需要等于512才可以输出flag。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4aRhrvXRKGRQvMJ03YyoC3RTiacTHdUG5yFtuDEJg8xvcTnQBPoaOXjVicLKakYepDtnQ6rP6Giag3GqMjYYgaMGjCzYpVicKMqLJI/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YcR555xeIH31bMPFZD78rgSLAKW19TKCLsEjHn88KtCLFo3kbnJxIxUQmz33PaPicfe6gKYYjHhgqTLY9mzvicEqP2SFHRWhTx0/640?wx_fmt=png&from=appmsg)

本题我们hook掉onClick方法，在调用前修改Checker.code的值为512，然后调用onClick方法即可。

```
1.hook掉onClick方法；2.在onClick方法调用前修改Checker.code的值为512；3.hook掉TextView的setText方法；
```

hook脚本如下：

```
Java.perform(function () {    var mainActivity$1=Java.use("com.ad2001.frida0x3.MainActivity$1");    var checker=Java.use("com.ad2001.frida0x3.Checker");    mainActivity$1.onClick.implementation=function (p0) {        console.log("onClick() is called");        console.log("修改前:Checker.code = "+checker.code.value);        checker.code.value=512;        console.log("修改后:Checker.code = "+checker.code.value);        this.onClick(p0);    }    var textView=Java.use("android.widget.TextView");    textView.setText.overload("java.lang.CharSequence").implementation=function (p0) {        console.log("setText() is called, p0: "+p0);        this.setText(p0);    }})
```

注意hook方法onClick时，使用的是匿名类MainActivity$1下的方法，而不是直接MainActivity下的方法。

执行结果如图：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4aRia0icZvTsn1JHool2erNicTHLjjOUM9f9ho87boQChQvNMXWSyhLxJbqiasUfrQEQWiaHnnfzcFP8MWm09jTBMwk2eRJpvlmk64U/640?wx_fmt=png&from=appmsg)

四、Frida 0x4：通过hook实例化一个类并调用该类的方法

反编译代码如图，app启动后只是设置了一下textView的值，没有任何其他操作，然后查看Check类，里面包含了get\_flag方法。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4Ylma74dj02iccWraEnXhRUula6icxJO75fl0fh9EAXVLRYN0xGrlaRBASRBcbwFgZwCHaOsxqRd9J7AOaEtZ0IyKIicfRzS64KRk/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4bzx2rmbczQRmhtLIUkaUB4lV6Ebh6Q2icsxXTSvxje5vqkkFfu15KY18lHktMd1gX4HQsXnHic6PmxPdKJOMncIfolAIJkBVBpI/640?wx_fmt=png&from=appmsg)

我们需要hook掉onCreate方法，然后实例化一个类，再调用该类的get\_flag方法，最后控制台打印输出值。

```
1.hook掉onCreate方法；2.实例化一个类；3.调用该类的get_flag方法；4.打印输出；
```

hook脚本如下：

```
Java.perform(function () {    var mainActivity=Java.use("com.ad2001.frida0x4.MainActivity");    mainActivity.onCreate.implementation=function (p0) {        console.log("onCreate() is called");        this.onCreate(p0);        var checkInstance=Java.use("com.ad2001.frida0x4.Check").$new();        var flag=checkInstance.get_flag(1337);        console.log("flag: "+flag);    }    var textView=Java.use("android.widget.TextView");    textView.setText.overload("java.lang.CharSequence").implementation=function (p0) {        console.log("setText() is called, p0: "+p0);        this.setText(p0);    }})
```

执行结果如图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZUVEPw60Howl7rM7ZPnELHOxBExDO8rbstWHd1mSQh40tPcyHIZ2cR84Rf7UkDeCRnBJQeWJtuDChNeZgrk68TvDnClbxTeHg/640?wx_fmt=png&from=appmsg)

五、Frida 0x5：还是通过hook主动调用一个方法

反编译后代码如图，依旧是通过hook掉onCreate方法然后主动调用flag方法。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YDvgoRGdQfV8OuxwUrooNpH9064Dgxdj6NNZ7Pej50I9TroTYXLiaaaMiarYXJFy4RYXkvHRduyojUZpTNJNWQH3ibbIIooHIqe0/640?wx_fmt=png&from=appmsg)

比较简单，跟上面第二题差不多，hook脚本如下：

```
Java.perform(function () {    var mainActivity=Java.use("com.ad2001.frida0x5.MainActivity");    mainActivity.onCreate.implementation=function (p0) {        console.log("onCreate() is called");        this.onCreate(p0);        this.flag(1337);    }    var textView=Java.use("android.widget.TextView");    textView.setText.overload("java.lang.CharSequence").implementation=function (p0) {        console.log("setText() is called, p0: "+p0);        this.setText(p0);    }})
```

执行结果如图：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4a9iaMEaxYHibtlHicaQJqD3uibVsYglV7hM5cbUxPFhicqhDcicgNx7IgDWZbocef6nGIoKMkbtibFlHyjCv73UeGaJyz7ZaeibYqYFxQ/640?wx_fmt=png&from=appmsg)

六、Frida 0x6：被hook的方法参数为实例化类

反编译后代码如图，此时需要被我们hook的方法get\_flag里面的参数是一个实例化的类，需要修改该实例化类的成员变量值。

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4aliak0ia4reo0r8lmZHSTmvO6Ay9vVSJn9B4LvxevNX9HCGlW07dKDHaOxdTkH5vBTKNQsPPpRicic07LffokABn0nj8stPrqibPIg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4ZYr2e2ql9cr7EibQbuxfW7iayfbNVvgUjDTuJ3FgW9GibIEPaVlW6wIVvxj055eXTibZLzkDpzZUW35rqkhyibPiaSicq8pWKiaRBoribU/640?wx_fmt=png&from=appmsg)

本题目需要首先hook掉onCreate方法，然后实例化一个Checker类，设置好要求的成员变量值，再实现对get\_flag方法的主动调用，传入刚才设置好的Checker实例化类即可。

```
1.hook掉onCreate方法；2.实例化一个Checker类，设置要求的成员变量值；3.对get_flag方法主动调用；
```

hook脚本如下：

```
Java.perform(function () {    var mainActivity=Java.use("com.ad2001.frida0x6.MainActivity");    mainActivity.onCreate.implementation=function (p0) {        console.log("onCreate() is called");        this.onCreate(p0);        var checkerInstance=Java.use("com.ad2001.frida0x6.Checker").$new();        checkerInstance.num1.value=1234;        checkerInstance.num2.value=4321;        this.get_flag(checkerInstance);    }    var textView=Java.use("android...