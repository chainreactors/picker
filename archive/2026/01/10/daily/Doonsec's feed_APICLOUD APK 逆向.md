---
title: APICLOUD APK 逆向
url: https://mp.weixin.qq.com/s/DFSAzm1luBK70ri8v8Kjig
source: Doonsec's feed
date: 2026-01-10
fetch_date: 2026-01-11T03:35:49.416997
---

# APICLOUD APK 逆向

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/iboywic3CuCr20qXTPXOujJTicFicUO88DqUJPiaibDQ5XUvWkES3SVicBG5bDyGGOrmibEXKE2rYQQwVNic59ezmxMYphg/0?wx_fmt=jpeg)

# APICLOUD APK 逆向

原创

argyros

夺旗赛小萌新

![]()

在小说阅读器中沉浸阅读

## 前言

apicloud 打包的apk可以勾选是否加密，加密后的内容无法阅读。解密是分析和挖洞的前置条件，必不可少。

## gogogo

加密文件长下面这样

![](https://mmbiz.qpic.cn/mmbiz_png/iboywic3CuCr20qXTPXOujJTicFicUO88DqUUiaHFkMYcstLVgb9hO1aZGztkIW3N6esOe0iapxLuMxrKblDwP0icjBaQ/640?wx_fmt=png&from=appmsg)

全局搜索**shouldinterceptRequest**

**shouldinterceptRequest**是一个**webview**中实现拦截功能的接口

![](https://mmbiz.qpic.cn/mmbiz_png/iboywic3CuCr20qXTPXOujJTicFicUO88DqUjiaWyjbfejwKiatmmDOjbkR8nLNVQNO2FItQ1xmMZtbiaAFzdcPukj2Kw/640?wx_fmt=png&from=appmsg)

找到有实现方法的地方

![](https://mmbiz.qpic.cn/mmbiz_png/iboywic3CuCr20qXTPXOujJTicFicUO88DqUyv8MIy0WSCBk1U2zRdV4SfGXTiatxVia4tYN8hLibPTTAmYwGtk6n1kCQ/640?wx_fmt=png&from=appmsg)

发现返回是个三元表达式根据一个bool值判断，猜测是解密流程，和非解密流程，不急，先看下b，b = **com.uzmap.pkg.uzcore.e.b.b**(str);

```
    protectedfinalWebResourceResponseb(WebViewwebView, Stringstr, booleanz, booleanz2, Stringstr2, Map<String, String>map) {
        ala=al.a(str);
        if (a.o()) {
            returnk.a(a, map);
        }
        WebResourceResponseshouldInterceptRequest=WebShare.shouldInterceptRequest(webView, WebShare.makeRESRequest(webView, str, z, z2, str2, map));
        if (shouldInterceptRequest!=null) {
            returnshouldInterceptRequest;
        }
        if (!this.b) {
            returnnull;
        }
        Contextcontext=webView.getContext();
        StringmakeWebviewTag=WebShare.makeWebviewTag(webView);
        Stringb=com.uzmap.pkg.uzcore.e.b.b(str);
        return!com.uzmap.pkg.uzcore.e.b.c(b) ?b(context, str, b, makeWebviewTag) : a(context, str, b, makeWebviewTag);
    }
```

跟进到**com.uzmap.pkg.uzcore.e.b.b**

```
    publicstaticStringb(Stringstr) {
        returnl.a(str);
    }
```

继续跟**l.a**，发现是一个对字符串做处理获取文件扩展名的操作

```
    publicstaticStringa(Stringstr) {
        intlastIndexOf;
        if (d.a((CharSequence) str)) {
            return"";
        }
        intlastIndexOf2=str.lastIndexOf(35);
        // 35 = '#'
        if (lastIndexOf2>0) {
            str=str.substring(0, lastIndexOf2);
        }
        intlastIndexOf3=str.lastIndexOf(63);
        // 63 = '?'
        if (lastIndexOf3>0) {
            str=str.substring(0, lastIndexOf3);
        }
        intlastIndexOf4=str.lastIndexOf(47);
        // 47 = '/'
        if (lastIndexOf4>=0) {
            str=str.substring(lastIndexOf4+1);
        }
        return (str.isEmpty() || (lastIndexOf=str.lastIndexOf(46)) <0) ?"" : str.substring(lastIndexOf+1);
    }
```

我们接着看**com.uzmap.pkg.uzcore.e.b.c**这个判断函数做了什么

```
    publicstaticbooleanc(Stringstr) {
        returnl.g(str);
    }
```

跟**l.g**

```
    public static boolean g(String str) {
        return a.contains(str);
    }
```

a，发现是判断是不是这几种文件后缀

```
    static {
        ArrayListarrayList=newArrayList();
        a=arrayList;
        arrayList.add("js");
        a.add("css");
        a.add("html");
    }
```

判断前面有个!要注意

我们跟过来

```
    private WebResourceResponse a(Context context, String str, String str2, String str3) {
        if (!str.startsWith("contents:")) {
            return null;
        }
        String e = com.deepe.c.i.l.e(str2);
        String b = com.uzmap.pkg.uzcore.e.d.b(str);
        byte[] b2 = k.b(b, true, true);
        if (b2 != null) {
            return new com.uzmap.pkg.uzcore.i.a.c(e, new com.uzmap.pkg.uzcore.i.a.b(b2, b));
        }
        return null;
    }

    private WebResourceResponse b(Context context, String str, String str2, String str3) {
        if (!str.startsWith("contents:")) {
            return null;
        }
        String a = w.a(str, (UZWidgetInfo) null);
        String e = com.deepe.c.i.l.e(str2);
        byte[] b = k.b(a, false, true);
        if ((b != null ? b.length : 0) <= 0) {
            return null;
        }
        return new com.uzmap.pkg.uzcore.i.a.c(e, new com.uzmap.pkg.uzcore.i.a.b(b, a));
    }
```

发现无论是a方法还是b方法返回都是**com.uzmap.pkg.uzcore.i.a.c**函数

```
    public c(String str, InputStream inputStream) {
        super(str, "UTF-8", inputStream);
    }
```

发现是最终返回的了，得看他里面的内容

继续看**com.uzmap.pkg.uzcore.i.a.b**，b是他的构造函数，目测要么是bArr[] 要么是str的解密的内容了

```
public class b extends ByteArrayInputStream {
    private String a;

    public b(byte[] bArr, String str) {
        super(bArr);
        this.a = str;
    }

    public String toString() {
        return "forbiden";
    }
}
```

再回头看下a函数中的b，明显像是文件路径，那么bArr就是解密后的内容了

```

```

```
    public static final String b(String str) {
        int f;
        if (!com.uzmap.pkg.uzapp.a.g() || !str.startsWith("contents:")) {
            return str;
        }
        if (Build.VERSION.SDK_INT > 10 && (f = f.a().f(str)) > 0) {
            str = "contents://" + str.substring(f);
        }
        return str.replaceFirst("contents:", "file:");
    }
```

hook脚本如下

```
Java.perform(function () {
    var bClass = Java.use("com.uzmap.pkg.uzcore.i.a.b");

    bClass.$init.implementation = function (bytes, name) {
        console.log("=== Hook Triggered ===");

        try {
            // 获取应用上下文
            var ActivityThread = Java.use("android.app.ActivityThread");
            var context = ActivityThread.currentApplication().getApplicationContext();

            // 使用外部文件目录（不需要特殊权限）
            var externalDir = context.getExternalFilesDir(null);
            var privateDir = externalDir.getAbsolutePath() + "/hook_captures";

            var File = Java.use("java.io.File");
            var dirFile = File.$new(privateDir);
            if (!dirFile.exists()) {
                var created = dirFile.mkdirs();
                console.log("Created external dir: " + created);
            }

            // 处理文件名
            var simpleName = name.split('/').pop();
            var filePath = privateDir + "/" + simpleName;

            console.log("Saving to: " + filePath);

            // 写入文件
            var String = Java.use("java.lang.String");
            var FileOutputStream = Java.use("java.io.FileOutputStream");

            var content = String.$new(bytes, "UTF-8");
            var fos = FileOutputStream.$new(filePath);
            fos.write(content.getBytes("UTF-8"));
            fos.close();

            console.log("✓ Successfully saved to external files dir");

        } catch (error) {
            console.log("✗ Save failed: " + error.toString());
        }

        return this.$init(bytes, name);
    };
});
```

## 最终效果

![](https://mmbiz.qpic.cn/mmbiz_png/iboywic3CuCr20qXTPXOujJTicFicUO88DqU2UdcoMBDn4fMgvy3cQtiaJGFdfqJRA8lRW4YWiarxYQv2OB8dPSG8pEg/640?wx_fmt=png&from=appmsg)

解密后

![](https://mmbiz.qpic.cn/mmbiz_jpg/iboywic3CuCr20qXTPXOujJTicFicUO88DqUeozjX12eVXYlNeAOHwFlzaDGEpCtoJsCHyicL2ZEhj08ibtSCVQOwYDw/640?wx_fmt=jpeg&from=appmsg)

预览时标签不可点

修改于

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/iboywic3CuCr0rmWGJwodLtHmmA1LQTO1MicEgqLm6k16Nxf2HLVqriaQSSCa7jxbvCGUPN0SGPUZHYh3fAqDWgdtQ/0?wx_fmt=png)

夺旗赛小萌新

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/iboywic3CuCr0rmWGJwodLtHmmA1LQTO1MicEgqLm6k16Nxf2HLVqriaQSSCa7jxbvCGUPN0SGPUZHYh3fAqDWgdtQ/0?wx_fmt=png)

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