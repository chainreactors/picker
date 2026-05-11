---
title: Fastjson反序列化（一）
url: https://mp.weixin.qq.com/s/i-4BVrFRBdTF9iX1FnJiLQ
source: Doonsec's feed
date: 2026-05-10
fetch_date: 2026-05-11T05:53:02.417520
---

# Fastjson反序列化（一）

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/utQFxwk9I8AjZVX3D8jLxNXYgdkfNomVzAQxNU1IxMCAW0U1qyv7PsbhmCibHd1GmEVJr8nPjcc6pMGpKlVfBqHKXYGgnCB9b0GSVGtmh9Xc/0?wx_fmt=jpeg)

# Fastjson反序列化（一）

原创

oLy
oLy

小趴菜网安学习路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 首先，文末打个广告，团队招新，有意向师傅欢迎扫码申请

# Fastjson原理

# `fastjson比较经典，链子也比较多，不说废话了，直接分析吧。`

fastjson 最普遍的用法，传入一个字符串，然后使用`parseObject`把字符串解析成一个 json 可以根据 key 值拿到任意一个 value

```
package org.example;
import com.alibaba.fastjson.JSON;import com.alibaba.fastjson.JSONObject;import com.alibaba.fastjson.parser.Feature;import com.alibaba.fastjson.serializer.SerializerFeature;import javax.imageio.plugins.jpeg.JPEGImageReadParam;
public class JSONUnser {    public static void main(String[] args) throws Exception {        String s = "{\"param1\":\"aaa\",\"param2\":\"bbb\"}";
        // 解析 JSON 字符串为 JSONObject        JSONObject jsonObject = JSON.parseObject(s);
        System.out.println(jsonObject);    }}
```

![](https://mmbiz.qpic.cn/mmbiz_png/utQFxwk9I8BpibPmxVdDeKJAgXcZHWx0rx0OF9RMjvwmOHUW8RVWlLCGz4zsJQMMficSEC40ABP83YQPs648So2fAFibIKflogwvm6pDodSSibQ/640?wx_fmt=png&from=appmsg)

本来就是一个解析字符串的功能，那为什么会产生反序列化漏洞？

主要是因为 fastjson 支持将 json 字符串解析为 javabean ，javabean 并不是在代码层面有什么特殊的限制，只是一种格式，存在一些属性，这些属性存在对应的`get`/`set`方法，这就是一个 javabean

```
package org.example;
public class Person {    private int age;    private String name;
    public Person(){
    }
    public Person(int age, String name) {        this.age = age;        this.name = name;    }
    public int getAge() {        return age;    }
    public void setAge(int age) {        this.age = age;    }
    public String getName() {        return name;    }
    public void setName(String name) {        this.name = name;    }}
```

![](https://mmbiz.qpic.cn/mmbiz_png/utQFxwk9I8DHqibtRvkrsCySJs18VmnQV5sSvTX8cYZLkVINlEkciaIaTW7qZNPbC8aHHjbaTgYHcCLPHRPZvxI4YPLgQhtNFS7jRAwklknBA/640?wx_fmt=png&from=appmsg)

这里又将一个字符串，解析成一个 java 对象，而且还能调用解析成 java 对象的方法

这里的话构造函数肯定调用了，因为其实例化了一个对象出来，并且自动调用了两个参数的`set`方法，传入了自定义字符串的两个值，赋值给对象

也就是说，这个对象当中是有这两个值的，要么使用反射去修改，要么使用`set`方法去修改

目前的话，还是比较正常的，因为就是指定了`Person`类，不会有什么问题

![](https://mmbiz.qpic.cn/mmbiz_png/utQFxwk9I8BDGuos82aJcmMib7SBMLhozmovDMD0mftD5bbVNc27AaRyDzZb1uQtCCYL4IZicDl7nS3G9qCCTkrrkBK1Vlq6aB2wC6icayoLia4/640?wx_fmt=png&from=appmsg)

但是其中有一个特性，如果传入的字符串当中存在﻿@type﻿这个字段，就可以指定一个类，让它去解析指定的类，也就是这个功能导致了很多安全问题

![](https://mmbiz.qpic.cn/sz_mmbiz_png/utQFxwk9I8Cn4oQzHR08iaGic7CLt11yUlsqzxZWC4HK1KaiclwhEKL85QZkJDeoqCrIc3O2E9vSQa1myAnoyZUJFaQBERRHlJmJE6MkYLsLEE/640?wx_fmt=png&from=appmsg)

下断点调试一下

![](https://mmbiz.qpic.cn/sz_mmbiz_png/utQFxwk9I8DPHMjJ3FbdGYDsBkJ0z4jQrO184KwcVnIuGQunojWHwLuCk3H2Kt5EsAnVwDelX1eOZLxgWXpmqbqN2ErIib1Doq25095jic5iaM/640?wx_fmt=png&from=appmsg)

它会调用只接收﻿String﻿类型的﻿parseObject﻿方法，首先就是调用了﻿parse﻿方法去解析字符串返回一个对象，最后又将 Java 对象转换为 Fastjson 的 JSONObject 对象

![](https://mmbiz.qpic.cn/sz_mmbiz_png/utQFxwk9I8Depvc37BkKZfgmIh6aTVTRPczVEuibRhapNe2hTqG6GRlKEvz9YDUWT9Ot5TiaHj2AB5QTqyte9xP0t0NcWRRpeQoWTItqAYvHk/640?wx_fmt=png&from=appmsg)

它接收字符串，﻿JSONObject﻿必定是﻿Map﻿类型的

![](https://mmbiz.qpic.cn/mmbiz_png/utQFxwk9I8Dxh57q7G1kiawKgcAZ6Zib78cpCSO9E1LJ8LNDmzE9rQPiaSl05Zn5x570sEAovFVibTZ0Su1711My5Admsv7R3VWW4X0Ortqhqwk/640?wx_fmt=png&from=appmsg)

跟到这里，会调用﻿DefaultJSONParser﻿类，其作用就是将传入的﻿json﻿字符串使用﻿Parser﻿进行解析

后面又用﻿parser.parse﻿继续解析，核心逻辑都是在﻿parse﻿里面

![](https://mmbiz.qpic.cn/sz_mmbiz_png/utQFxwk9I8AE3hiam5qLMhBcDvpRKuUh5iaK7kAsGDn13LU5kib0sGfFib2aPnMRSfYDho9qEdH93oBOHMcgfXUmWDNkfoBp0nfTIfP9TWtBwjw/640?wx_fmt=png&from=appmsg)

它会根据字符串的格式去识别字符串，首先就是判断是左大括号，是一个 json 对象的开始

![](https://mmbiz.qpic.cn/sz_mmbiz_png/utQFxwk9I8D2xykVFDeEYBs845wSlcE3KYPpdxzmPMC2SW6M1NqXWePKFo2zQfW0p4P4kdgRpt0M76QUpYoSm6Bwawqk30FVKCPY2ibNV84s/640?wx_fmt=png&from=appmsg)

这里新建的﻿object﻿是空的

![](https://mmbiz.qpic.cn/mmbiz_png/utQFxwk9I8DDtwZXCicwZ7kHb8E5zuYTwyHNLwW30hOO9bZ0v4jSNrXuFMzzf0a5I9PrlX3nqxORTP9z2ViaQmEfRib7iaO3tTibdlGxTKva693g/640?wx_fmt=png&from=appmsg)

然后继续往下走，调用﻿parseObject﻿，接收Map，依旧是先去处理字符串

![](https://mmbiz.qpic.cn/sz_mmbiz_png/utQFxwk9I8AcFmZlhiaJE6fqRDUgx0bkwUlIMHRCsFiaFM9EQibbB8oWaDVTaeb2CSlFgCHsiaOwI8pz6IPZ5dCgibGkGsR1TFTJZpra7pBrUgrk/640?wx_fmt=png&from=appmsg)

上面这部分代码就是用来处理 key 值，首先字符串开始是﻿"﻿，后面就进行了各种判断字符的判断，先是检查了﻿逗号

![](https://mmbiz.qpic.cn/mmbiz_png/utQFxwk9I8DzXXjITAEsNhmWNd2zxEQdsC6ewf8qBKw1pTaeicMe7ZRHfAYu3neHrmfavpPib4sBKpk31C8ib0dfGrxgSfknPZumaZm8lnJGnU/640?wx_fmt=png&from=appmsg)

到这里判断当前为﻿"﻿，两个双引号之间是﻿@type﻿，最后将 key 值读取出来﻿@type

![](https://mmbiz.qpic.cn/sz_mmbiz_png/utQFxwk9I8ByeDfKnwlLH2Ga1z0FQVZkKWicgT0VtQ3P0DPwPOX3xXdxlmzSfU4HAbWJj63zxZhAFl08CxdvNtfbYXRXdpiaiaCNaOTEcRkEMU/640?wx_fmt=png&from=appmsg)

跟到这里，它还会对 key 进行一些特殊处理，如果是﻿JSON.DEFAULT\_TYPE\_KEY﻿常量值为﻿@type﻿，就进入第一个﻿if﻿，如果是﻿$ref﻿引用对象进入第二个﻿if﻿，这里我们传入的就是﻿@type﻿，会进入第一个﻿if

![](https://mmbiz.qpic.cn/mmbiz_png/utQFxwk9I8Cg9vANl86CheXeV3FvIKibHQrd2BqOmnkrLvmZQ5WP6Axt0TiaID3ZtwDfWH1B9DXx3fgmzdkrSaJm70Sm0dv0UJXf3G9pHDawk/640?wx_fmt=png&from=appmsg)

首先它要加载这个类

![](https://mmbiz.qpic.cn/sz_mmbiz_png/utQFxwk9I8C2QiboumibN9rxW8j6d41ZywlsTF0bhLIxxjOicsl1dLdRQiaQGkNtyE5rfViaUcjbNU1oLsmicc54ibJ4FZhPSuWqAn8lk7ADvCM6Do/640?wx_fmt=png&from=appmsg)

进入﻿loadClass﻿之后，﻿mappings﻿是从缓存里面获取这个类，之后判断是否以﻿[﻿或者﻿L﻿开头(这两个后面版本用来绕过)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/utQFxwk9I8Bwic3KZfOpEf9ozlL5vINJFicMgSQ2TGSibNPfI7ZoReHflAMBSZ7gy1Q3NIkK7B4rhzOBE6PHA2sAtQJLlkON4szntOLo3bVTRg/640?wx_fmt=png&from=appmsg)

最后获取了类的上下文之后，﻿mappings.put﻿放入到缓存里面返回这个类

![](https://mmbiz.qpic.cn/mmbiz_png/utQFxwk9I8CtkIqYjicd4wFMO1EqmANL4oEzdzIIppgEcOoKKdlE1IV3ic8xZ6lFchfBVmrebLoj9ibfQW4E5yXnP5DPCSTMXctfMTC90xmF3Y/640?wx_fmt=png&from=appmsg)

继续往下走，这里的判断就是每加载完一轮 key & value 的键值对就会放入到之前新建的空的﻿object﻿里面

最重要的就是﻿ObjectDeserializer﻿，第一步是用﻿DefaultJSONParser﻿解析器去解析，解析这一部分都还是基于﻿json﻿字符串的操作，﻿ObjectDeserializer﻿就是下一步用来解析﻿json﻿字符串之后的﻿java﻿对象，和原生的反序列化不同；第一步就是﻿config.getDeserializer﻿获取反序列化器，第二步就是通过反序列化器来反序列化，执行完这一步：﻿deserializer.deserialze﻿，返回的就是﻿Person﻿了

![](https://mmbiz.qpic.cn/mmbiz_png/utQFxwk9I8AIfMAScSpnBV70uy0y9QxTe0jMjGicvwpfT1smknYBsucSqtL1guA2V06xbuE1U1kW2JeqZXwVBjRrkibHnjUAz3XDbzE3pqZjM/640?wx_fmt=png&from=appmsg)

接下来就要跟一下﻿getDeserializer﻿里面调用的什么进行反序列化的

可以看到﻿derializer﻿通过﻿derializers.get﻿赋值，而﻿derializers﻿是从缓存中获取，为什么说这里的﻿derializers﻿是缓存呢，﻿derializers﻿ 本质上就是一个以 Type 为键、ObjectDeserializer 为值的本地缓存表，目的是避免为同一个 Type 反复创建反序列化器，提升性能。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/utQFxwk9I8CH1orsBSzcKRZuX1kglMGibOlHtNwH2VvrOmshlusjB33wOibbFC2jm9ZHU8du5iaRo8HwsP7X8cB8aHZR1gyNDH8iavMnZtMj9zE/640?wx_fmt=png&from=appmsg)

为什么说以Type 为键、ObjectDeserializer 为值呢，可以看到其构造方法，它会把很多系统的内置类都会对应一个对应类的反序列化器，这些内置的东西会提前放在﻿derializers﻿缓存表中，当前是自定义的类，肯定是没有的

![](https://mmbiz.qpic.cn/sz_mmbiz_png/utQFxwk9I8DY6pwP8exsmgMzSnN3flSfoPOqUTEhcTCNhZU8cOUuxdvxNdLdZzg8ZXI7jKxa5J8HHHGn0MmwJsElS6NKs3W1EBtibU9NvaMs/640?wx_fmt=png&from=appmsg)

继续往下走，会走到第二个﻿if﻿的﻿getDeserializer﻿方法，来到﻿JSONType﻿这里，这是﻿JSONType﻿的注解，意思就是说，如果说写代码时候，写了﻿JSONType﻿注解的话，相当于自己写了一个反序列化，最后返回自己写的反序列化器，这就是简单说明，因为这里并不可控，也不会去多余思考研发是否会在这里做文章，大致了解即可

![](https://mmbiz.qpic.cn/mmbiz_png/utQFxwk9I8DtyscFTPohzezOibBkZPibrBVraY4yS6Psdz6GoibFctNOroKzYHtpLYouiaczLJMhygr6oGdw1Z5n5g0K6icceqPmmGmJKJoZUJ4c/640?wx_fmt=png&from=appmsg)

在漏洞之前，代码本身就存在一些黑名单，可以看到对于漏洞利用来说，都是一些无关紧要的黑名单，基本都是都是基于性能方面的调整

![](https://mmbiz.qpic.cn/sz_mmbiz_png/utQFxwk9I8C3xhrapWdcNAypC5HNIzzUt1vrbqibbGVx6CiczxwwoaGjFW71QMzlxpqoo2ibTaiaO6PkvAKrIpRFB5LVsa7jAIfxsoUp4lWyOSo/640?wx_fmt=png&from=appmsg)

这期间还会存在一堆 if 匹配，但都不会匹配到我们当前加载的类，直接走到461行，一直没有匹配到，它自己创建了一个﻿javabean﻿的反序列化器

![](https://mmbiz.qpic.cn/mmbiz_png/utQFxwk9I8BvpoK1WDBatXbhibbNZGyfKV52EkJpYz1muKSezRvVib75WOVoPpw2JdM389ibTicdAYZnA20HAdbYy0sGBc3OtdTMxTghzNdWwfg/640?wx_fmt=png&from=appmsg)

跟进来之后，它首先是存在一个﻿asmEnable﻿，﻿asm﻿是动态创造代码的机制，java底层的动态创建类，动态加载，asmEnable﻿默认是﻿true

![](https://mmbiz.qpic.cn/mmbiz_png/utQFxwk9I8CWwGk1yQr18VoibQqmcaYG5sPm5qVP8PlDcrZow0CEplsG6oWdZjJLlK1o0D9X3N5fslXhrycv4ib9zHJE4LzPONZKsZ4xHhQLw/640?wx_fmt=png&from=appmsg)

主要看这里，﻿JavaBeanInfo.build﻿，在上面一些代码中也是根据﻿asmEnable﻿的布尔值去做一些﻿if﻿判断，一直到526行

![](https://mmbiz.qpic.cn/sz_mmbiz_png/utQFxwk9I8Cj51VIriaJFYdKQu9iaYKWrZ6m1MoQ77zTy...