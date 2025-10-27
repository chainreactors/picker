---
title: N1CTF-ezapk 解题思路
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458584139&idx=1&sn=356e4f25ebf567cce4a702e88dfdad3d&chksm=b18c34c186fbbdd7728e7ab5edeaa130f09e586fabfcc98592dce8fe1956b367abf6fabe9123&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-29
fetch_date: 2025-10-06T19:17:34.856632
---

# N1CTF-ezapk 解题思路

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HZ1qpdHbJnLTL6CddicV04gzRbWrweRUYia8nE7VJOvSjZDH9KSqTGz5OBdGDU4z6U3dhYIRnzjXOQ/0?wx_fmt=jpeg)

# N1CTF-ezapk 解题思路

SleepAlone

看雪学苑

本篇文章总下我的心路历程吧，包括但不限于：

1.ezapk的解体思路

2.环境问题搭建tips

3.完整的脚本

总之，完全是新手向的文章，遇到的坑，一步步怎么做，我都会说清楚，即使你是新手也没关系。这也是我第一次真真切切深入安卓逆向，之前只是静态反编译解决，这次学习了frida，CE（cheat engine），安卓模拟器等工具使用，写篇文章算是自己的一个阶段性总结。

看完这篇文章你将学到：

◆安卓逆向基本思路

* dex反编译
* frida hook
* CE 找出是谁在暗中修改函数

◆深入JNI机制

◆frida 环境搭建以及基本使用

◆CE 使用 以及 CE server 构建

## 题目背景

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HZ1qpdHbJnLTL6CddicV04gdZND9fR0Oa00qgIGl4JdWfib29XoIaIHMPZOgUUfpsGmgT11pokfBhg/640?wx_fmt=png&from=appmsg)

题目非常简单，输入n1ctf{flag}, 点击check检查，很正规的安卓题

##

## 开门见山-dex反编译

放入jadx-gui查看一下主逻辑：

```
public class MainActivity extends AppCompatActivity {
    private ActivityMainBinding binding;

    public native String enc(String str);

    public native String stringFromJNI();

    /* JADX INFO: Access modifiers changed from: protected */
    @Override // androidx.fragment.app.FragmentActivity, androidx.activity.ComponentActivity, androidx.core.app.ComponentActivity, android.app.Activity
    public void onCreate(Bundle bundle) {
        super.onCreate(bundle);
        ActivityMainBinding inflate = ActivityMainBinding.inflate(getLayoutInflater());
        this.binding = inflate;
        setContentView(inflate.getRoot());
        this.binding.CheckButton.setOnClickListener(new View.OnClickListener() { // from class: com.n1ctf2024.ezapk.MainActivity$$ExternalSyntheticLambda0
            @Override // android.view.View.OnClickListener
            public final void onClick(View view) {
                MainActivity.this.m157lambda$onCreate$0$comn1ctf2024ezapkMainActivity(view);
            }
        });
    }

    /* JADX INFO: Access modifiers changed from: package-private */
    /* renamed from: lambda$onCreate$0$com-n1ctf2024-ezapk-MainActivity, reason: not valid java name */
    public /* synthetic */ void m157lambda$onCreate$0$comn1ctf2024ezapkMainActivity(View view) {
        String obj = this.binding.flagText.getText().toString();
        if (obj.startsWith("n1ctf{") && obj.endsWith("}")) {
            if (enc(obj.substring(6, obj.length() - 1)).equals("iRrL63tve+H72wjr/HHiwlVu5RZU9XDcI7A=")) {
                Toast.makeText(this, "Congratulations!", 1).show();
                return;
            } else {
                Toast.makeText(this, "Try again.", 0).show();
                return;
            }
        }
        Toast.makeText(this, "Try again.", 0).show();
    }

    static {
        System.loadLibrary("native2");
        System.loadLibrary("native1");
    }
}
```

可以看到主要逻辑在enc中，enc 属于native 函数，通过JNI调用，enc位于通过System.loadLibrary()的两个so中。

## 迷雾重重-JNI逆向

ida 打开libnative.so反编译会发现有大量的类似指针数组的调用，其实这是JNI调用

`关于JNI调用可以看：`

`[https://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/jniTOC.html]`

`(https://docs.oracle.com/javase/7/docs/technotes/guides/jni/spec/jniTOC.html)`

native code 想要访问java VM的特性就需要调用JNI函数，调用JNI函数需要JNI interface pointer

并且JNI interface pointer是native函数的第一个参数，如下：

```
package pkg;

class Cls {

     native double f(int i, String s);

     ...

}
```

这里 double 会经过名称混淆变为Java\_pkg\_Cls\_f\_ILjava\_lang\_String\_2

```
jdouble Java_pkg_Cls_f__ILjava_lang_String_2 (
     JNIEnv *env,        /* interface pointer */
     jobject obj,        /* "this" pointer */
     jint i,             /* argument #1 */
     jstring s)          /* argument #2 */
{
     /* Obtain a C-copy of the Java string */
     const char *str = (*env)->GetStringUTFChars(env, s, 0);

     /* process the string */
     ...

     /* Now we are done with str */
     (*env)->ReleaseStringUTFChars(env, s, str);

     return ...
}
```

JNI interface pointer是一个pointer to pointer，具体来说就是一个指针数组，这个数组保存着JNI函数的地址，包括：

```
const struct JNINativeInterface ... = {

    NULL,
    NULL,
    NULL,
    NULL,
    GetVersion,

    DefineClass,
    //... 太长省略

    GetJavaVM,

    GetStringRegion,
    GetStringUTFRegion,
    //...
    GetObjectRefType
  };
```

但是ida中并没有JNIEnv等等结构体，一个个倒入自动识别太麻烦，手动计算又太蠢

该怎么办呢？

##

## 拨云见日-frida hook

### 定位enc

其实真正常用的JNI 函数就那几个，可以看到enc中传入了字符串，所以native函数想要获取这个字符串，会调用关于String的JNI调用 一般为GetStringUTFChars

`关于环境：我的pc是mac m1,手头也没有安卓设备，最后选择mu mu pro模拟器（啥都好，就是要花钱）`

在mu mu pro模拟器中安装好 frida server后，运行frida server后就可以hook了

```
Java.perform(() => {
    const MainActivity = Java.use("com.n1ctf2024.ezapk.MainActivity");

    MainActivity.enc.implementation = function(input) {
        console.log("enc called with input:", input);
        const result = this.enc(input);
        startHook();
        // startHooklib();
        console.log("enc returned:", result);

        return result;
    };
});

function startHook(){
    const lib_art = Process.findModuleByName('libart.so');
    const symbols = lib_art.enumerateSymbols();
    for (let symbol of symbols) {
        var name = symbol.name;
        if (name.indexOf("art") >= 0) {
            if ((name.indexOf("CheckJNI") == -1) && (name.indexOf("JNI") >= 0)) {
                if (name.indexOf("GetStringUTFChars") >= 0) {
                    console.log('start hook', symbol.name);
                    Interceptor.attach(symbol.address, {
                        onEnter: function (arg) {
                            console.log('GetStringUTFChars called from:\n' + Thread.backtrace(this.context, Backtracer.ACCURATE).map(DebugSymbol.fromAddress).join('\n') + '\n');
                        },
                        onLeave: function (retval) {
                            console.log('onLeave GetStringUTFChars:', ptr(retval).readCString())
                        }
                    })
                }
            }
        }
    }
}
```

运行结果

```
// frida -U -f com.n1ctf2024.ezapk -l hook.js
GetStringUTFChars called from:
0x6d55c7117c libnative1.so!0x1b17c
//没有 多点几次 hook和输出在一起 所有你需要hook了 再点几次
```

这里就知道sub\_1b148是enc了

### stacktrace

接下来，定位enc调用了哪些函数，还是hook

```
ava.perform(() => {
    const MainActivity = Java.use("com.n1ctf2024.ezapk.MainActivity");

    MainActivity.enc.implementation = function(input) {
        console.log("enc called with input:", input);
        const result = this.enc(input);
        //startHook();
        startHooklib();
        console.log("enc returned:", result);

        return result;
    };
});

function startHooklib(){

    var functions_lib1 = Module.enumerateExports("libnative1.so");
    functions_lib1 = []
    var functions_lib2 = Module.enumerateExports("libnative2.so");

    functions_lib1 = functions_lib1.map(item => {
        return { ...item, module: "libnative1.so" };
    })

    functions_lib2 = functions_lib2.map(item => {
        return { ...item, module: "libnative2.so" };
    })

    var functions = [...functions_lib1,...functions_lib2];

    // {
    //     "address": "0x6d56602ca8",
    //     "name": "aE7KMLpKuUbB",
    //     "type": "function"
    // }

    functions.forEach(function(func) {
        var moduleBase_lib1 = Module.findBaseAddress(func.module);
        var moduleBase_lib2 = Module.findBaseAddress(func.module);
        if ( moduleBase_lib1 && moduleBase_lib2) {
            var address = func.address
            // console.log("Attaching to function at " + func.module + "!" + func.addr);
            Interceptor.attach(address, {
                onEnter: function(args) {
                    console.log(func.module + " function called at "  + func.address + " " + func.name);
                },
                onLeave: function(retval) {
                    console.log(func.module + " function returned at "+ func.address + " " + func.name);
                }
            });
        } else {
            console.log("Module " + func.module + " not found!");
        }
    });
}
```

运行结果

```
libnative2.so function called at 0x6d55c0306c iusp9aVAyoMI
libnative2.so function returned at 0x6d55c0306c iusp9aVAyoMI
libnative2.so function called at 0x6d55c032c0 SZ3pMtlDTA7Q
libnative2.so function returned at 0x6d55c03...