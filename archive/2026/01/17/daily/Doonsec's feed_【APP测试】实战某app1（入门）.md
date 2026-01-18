---
title: 【APP测试】实战某app1（入门）
url: https://mp.weixin.qq.com/s/GKoBwnpcKUZZqz7iR6NobQ
source: Doonsec's feed
date: 2026-01-17
fetch_date: 2026-01-18T03:35:41.349587
---

# 【APP测试】实战某app1（入门）

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyfPmU99vdnlh3IzrTic1HWn3RStkPakqfxPujgib5wvqvowBGb2kichmiaQ/0?wx_fmt=jpeg)

# 【APP测试】实战某app1（入门）

原创

d0n9x1e
d0n9x1e

蝉SEC

![]()

在小说阅读器中沉浸阅读

## 首先先尝试一波算法自吐脚本

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfy4pl5aoIBShV6QjPTXo1FJAxNU5QsdhYkjl0NLFwaThibVKJfKAHHJJQ/640?wx_fmt=png&from=appmsg)

点击登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyJJ9SRoHhnywV03Bqy7AyMC9lSGJjq8ibA4icnYjQ5IbTSULksibU3Mfwg/640?wx_fmt=png&from=appmsg)

在小黄鸟中查看加密后字符，然后去log.txt里搜

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyg9IKCWO3kUicrFrCvlR4Ixj01fRD6IkHWFPW7vLyFEG1gtJCibkQIRjA/640?wx_fmt=png&from=appmsg)

手机号，验证码，sign各种信息都搜一下，没搜到

这时就需要进行逆向分析了

## objection一把梭

### 注入

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfym3vLunSvfmBibZ5Fn9ckVRaXI7HuP987gLqHkvTpdX63T000xLGlCxA/640?wx_fmt=png&from=appmsg)

### hook一个常用点

9.String的getBytes、isEmpty方法

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfytCUIdhiaVEXCeGYMaT2x373IaIyITP2qZ2895Zhb8VZHb8WOOxiaLNAg/640?wx_fmt=png&from=appmsg)

接着点击登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyDxicHrqTKjp9ic5PUgRlicgVrWtUrZnuLOibicykcunEej3ZAyjLkhpCa3g/640?wx_fmt=png&from=appmsg)

### 打印参数和返回值

会发现他确实是触发了这个点，接着我们可以打印参数和返回值以及堆栈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfySSsxeDlLl6ib4akTSllu8TT5J6OX4icWaYcPcURwoRBf6OZZcAVd4LDg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyL7n8yicB9EF7nWhfyjyF5lVvBjyt476ULlBZpicIpPcfwc2wzfaiagUeg/640?wx_fmt=png&from=appmsg)

返回值是一个对象，这里没解析，参数是UTF-8，那么我们就关心一下堆栈

### 分析堆栈

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyGTVoD6KUheZCVibWBEbelpbxq0TRMic4XN7FkpF12sVibFlusP8C1cbYw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfynj8RwxaQmMmK4wAwUSHjiantLC5sjUXD1icHNXDbsSRicYd4DZhBFIHWg/640?wx_fmt=png&from=appmsg)

跟到可疑的类com.sichuanol.cbgc.util.LogShutDown.getAppsign

中，发现这是一个native方法（中间需要脱壳，可以找脱壳机或一些工具进行脱壳）

进cn.thecover.lib.http.data.entity.HttpRequestEntity.getsign中查看

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyMdboaSxPm781HDicTYA364QCAuowx688Sn3by3VFLcT1RvwoQZunKrQ/640?wx_fmt=png&from=appmsg)

看到了和账号密码，token相关的信息，hook他看看到底有没有经过这边

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfy04ITfiaichwzwCBvZ01NjPpoHibjDglia08sQKI43KYGrOicOicia2cicTyYpQ/640?wx_fmt=png&from=appmsg)

hook之后点击登录

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfynaQrXK2zLSOam9412TrTyicYxolCdxibvnNFZYozKY4oibwF0UAa3wVEg/640?wx_fmt=png&from=appmsg)

发现确实出现了一些数据，配合抓到的包发现是包中加密的内容

其实到这一步就不需要再分析了，直接rpc调用一下就好了，后面的内容作为深入分析，不需要看

## so

hook   com.sichuanol.cbgc.util.LogShutDown.getAppsign

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyPibUzwzNcZk4NpeJ14qSlt7J2lMxsKHbicIXGcxLplFzB3oia1iaox9t9A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyRNXCcspjdLBDWh3Tmv1UPlnWiapS8RIKE7wNRWvudichVlHYIfN9ibYkw/640?wx_fmt=png&from=appmsg)

可以看到这个点传入的参数只有时间戳

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfykLdXbYxbLvdTduYwnLibiaukEaeGLg2EjSoQibpazz2bk6sk8PbtdKpSA/640?wx_fmt=png&from=appmsg)

并且和包中数据相同，也就是说这个签名之和时间戳有关，这就很简单了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfy9EDbb9osDFjYPvFMt55at36yAbe805ianwQg16ibZoa7ibjkfL0rNl7zQ/640?wx_fmt=png&from=appmsg)

由上面分析过程可以得知，我们要分析的只有这个函数了

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyiaR1a5fUz9AuYKSOVFgxCyoOVtCCEmnvYgoHybErSarzCoUnMIssdog/640?wx_fmt=png&from=appmsg)

打开这个静态注册的函数

gpt一把梭？

这段代码是一个用C语言编写的JNI（Java Native Interface）函数，用于在Android平台上生成一个签名字符串。以下是对代码的逐步分析和解释：

### 函数签名

```
jstring __fastcall Java_com_sichuanol_cbgc_util_SignManager_getSign(
        JNIEnv *a1,
        jobject a2,
        void *a3,
        void *a4,
        int time)
```

* `JNIEnv *a1`

  ：JNI环境指针，用于调用JNI的各种方法。
* `jobject a2`

  ：Java对象的引用，通常在JNI中用于访问Java类实例。
* `void *a3`**和**`void *a4`

  ：这两个参数是Java传入的字符串对象，具体含义需要结合上下文理解（可能是“账号”和“令牌”）。
* `int time`

  ：时间戳参数，用于签名生成。
* **返回值**

  ：`jstring`，即生成的签名字符串。

### 主要逻辑

1. **查找Java类和方法**

   ：

```
v8 = (*a1)->FindClass(a1, "com/sichuanol/cbgc/util/LogShutDown");
```

+ 查找名为 `com.sichuanol.cbgc.util.LogShutDown` 的Java类。
+ 如果类不存在，会打印错误日志并返回 `"wtf"`。

2. **调用静态方法获取应用签名**

   ：

```
if ((*a1)->GetStaticMethodID(a1, v8, "getAppSign", "()Ljava/lang/String;"))
```

+ 获取 `LogShutDown` 类中的静态方法 `getAppSign`。
+ 如果方法不存在，会打印错误日志并返回 `"wtf"`。

3. **获取Java字符串的UTF-8表示**

   ：

```
v10 = (const char *)((int (__fastcall *)(JNIEnv *))(*a1)->GetStringUTFChars)(a1);
v11 = (*a1)->GetStringUTFChars(a1, a3, 0);
v12 = (*a1)->GetStringUTFChars(a1, a4, 0);
```

+ 将Java字符串对象转换为C风格的UTF-8字符串。
+ `v10`

  是应用签名，`v11` 是账号，`v12` 是令牌。

4. **拼接字符串**

   ：

```
v18 = (char *)v24 - ((strlen(v14) + v17 + 7) & 0xFFFFFFF8);
memset(v18, 0, v21 + strlen(v14));
strcat(v18, v10);
strcat(v18, v11);
strcat(v18, v12);
strcat(v18, v14);
```

+ 动态分配内存用于拼接字符串。
+ 将应用签名、账号、令牌和时间戳拼接成一个完整的字符串。

5. **计算MD5摘要**

   ：

```
MD5Digest(v18, v22, v30);
```

+ 使用MD5算法对拼接后的字符串计算摘要。
+ `v30`

  是MD5摘要的16字节结果。

6. **将MD5摘要转换为32位字符串**

   ：

```
get32MD5String(v30, v29);
```

+ 将16字节的MD5摘要转换为32位的十六进制字符串。

7. **打印日志**

   ：

```
_android_log_print(
  6,
  "theCover",
  "app sign :%s \naccount : %s\ntoken : %s\nts : %s\nsrc %s \n result %s",
  v10,
  v11,
  v12,
  v14,
  v18,
  v29);
```

+ 打印调试日志，包含输入参数和最终结果。

8. **返回结果**

   ：

```
return (*a1)->NewStringUTF(a1, v29);
```

+ 将32位MD5字符串转换为Java字符串并返回。

OK分析结束我们就应该知道要hook的函数就是MD5Digest，get32MD5String

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyQp7vc6WwIPfiaxBUibJLJus1fcOQ0oF1HTeHOMVfIX7j8dTDUARRo8hA/640?wx_fmt=png&from=appmsg)

直接在这里tab

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyHeE6icAP7ialKDBmt9X7JGzwVaicwZxdTNvGGO2XsvGM1L5lX7zrkpSqw/640?wx_fmt=png&from=appmsg)

发现是一个BLX指令，所以这不是我们要hook的点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyJ2DDRXGNrXUy6lvam14EuozWNDSReOgNCFNWmsqia8NuMuDhOw7CCwA/640?wx_fmt=png&from=appmsg)

双击该函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyZPs2VaL8Yl7NIQibF5ktoxs29dFm6fVa2jfkYmnM9ojrCWcYP6egkew/640?wx_fmt=png&from=appmsg)

再双击这个返回函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfyPZ3UpaPzct8VcEh3Nn0RLLPwq4nJQGj73ojLBN2e6YJg20KM1nniaOQ/640?wx_fmt=png&from=appmsg)

这里就是我们要hook的点

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfybCuC7HEMso1jVq63qTr35oZ5ic0ibmjF7zTPbWBibTmadt15jRibibE8BdQ/640?wx_fmt=png&from=appmsg)

C90

另外一个也是同理

![](https://mmbiz.qpic.cn/sz_mmbiz_png/8nIFQgfd1WjfOGV93cHX8NEqn81KRmfynkbqMo7Le6P9Ld1EAq4pcKzgmPX3GngXojhsHF5tDp2ZvSX1u0libAQ/640?wx_fmt=png&from=appmsg)

8BC

### 给出hook脚本

```
// 枚举导入表
// var improts = Module.enumerateImports("libencryptlib.so");
// for(let i = 0; i < improts.length; i++){
//     //console.log(JSON.stringify(improts[i]));
//     console.log(improts[i].name + " " + improts[i].address);
// }

// 枚举导出表
// var exports = Module.enumerateExports("libencryptlib.so");
// for(let i = 0; i < exports.length; i++){
//     console.log(exports[i].name + " " + exports[i].address);
// }

// 枚举符号表
// var symbols = Module.enumerateSymbols("libencryptlib.so");
// for(let i = 0; i < symbols.length; i++){
//     console.log(symbols[i].name + " " + symbols[i].address);
// }

// 枚举进程中已加载的模块
// var modules = Process.enumerateModules();
// console.log(JSON.stringify(modules[0].enumerateExports()[0]));

// 导出函数的hook
// var funcAddr = Module.findExportByName("libencryptlib.so", "_ZN7MD5_CTX11MakePassMD5EPhjS0_");
// console.log(funcAddr);
// Interceptor.attach(funcAddr, {
//     onEnter: function (args) {
//         console.log("funcAddr onEnter args[1]: ", hexdump(args[1]));
//         console.log("funcAddr onEnter args[2]: ",...