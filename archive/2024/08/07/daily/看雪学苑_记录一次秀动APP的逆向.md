---
title: 记录一次秀动APP的逆向
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458566069&idx=2&sn=b9c5c93c634785f222b962942c8071e6&chksm=b18d8d3f86fa0429df2d175616666936657091d661e0f82fa048446e5a4564cb1eb7b00d5e7b&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-08-07
fetch_date: 2025-10-06T18:04:32.208705
---

# 记录一次秀动APP的逆向

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQyAJ5SUFnu0g1DF7xBP2d2Ck25UFPeNbiaFhe3KndV768rp5iaVdH3DOFQ/0?wx_fmt=jpeg)

# 记录一次秀动APP的逆向

mb\_qzwrkwda

看雪学苑

目标应用：秀动

目标版本：5.2.7

```
一

过掉Frida检测
```

###

### 使用魔改frida过检测（文件已打包）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQytAt2dSQYAB5icwRbbfT1UZL3xRL5SL0rjiaPGnKAWR0WBs34q9VOEjew/640?wx_fmt=png&from=appmsg)

frida启动后发现有检测，尝试使用魔改frida过掉检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQyf3UUQMjyUd5zuE1HWUibATF9MtucO6QNouYic7GSPic8SVYDbkSV4oDtg/640?wx_fmt=png&from=appmsg)

发现可以成功挂起。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQymoLxVC883w0JMocMh9oGTmeYQpYa9pCnjnZ9VcSgkuA75u6J3OxEoA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQyvOqlNDib3icyoNvdFCVTdqJQlZEWt3AIdYIG8CtEosp8BibokmccDXdyA/640?wx_fmt=jpeg&from=appmsg)

使用魔改frida成功过掉检测，现在开始分析具体的frida检测。

> 魔改frida已经随文件打包，大家可以去github支持下作者。

> [!tip]
>
> 注意，遇到有frida检测的样本尽量要-f挂起，如果-F可能造成手机卡死重启，耽误调试进度。

```
function hook_open() {
    // https://blog.csdn.net/a656343072/article/details/40539889
    /*
        函数原型：int open( const char * pathname, int oflags);
                int open( const char * pathname,int oflags, mode_t mode);

        mode仅当创建新文件时才使用，用于指定文件的访问权限。
        pathname 是待打开/创建文件的路径名；
        oflags用于指定文件的打开/创建模式，这个参数可由以下常量（定义于 fcntl.h）通过逻辑或构成。
        O_RDONLY       只读模式
        O_WRONLY      只写模式
        O_RDWR          读写模式
        以上三者是互斥的，即不可以同时使用。
    */
    var open_addr = Module.findExportByName("libc.so","open")
    var io_map = Memory.allocUtf8String("/proc/13585/maps");
    Interceptor.attach(open_addr, {
        onEnter: function (args) {
            console.log('targetFunction called from:\n' +
                Thread.backtrace(this.context, Backtracer.ACCURATE)
                    .map(DebugSymbol.fromAddress).join('\n') + '\n');
            if(args[0].readCString().indexOf("/proc/")!=-1 && args[0].readCString().indexOf("maps")!=-1){
                args[0] = io_map
                // ptr(args[0]).writePointer(Memory.allocUtf8String(args[0].readCString().replaceAll(/\d+/g,"1")))
                // args[0] = Memory.allocUtf8String("/proc/1/maps")
                // Memory.protect(ptr(args[0]), args[0].readCString().length, 'rwx');
                // var value_new_str = Memory.allocUtf8String("/proc/1/maps")
                // console.log("args0="+args[0].readCString())
                // ptr(args[0]).writeByteArray([0x2f,0x70,0x72,0x6f,0x63,0x2f,0x32,0x2f,0x6d,0x61,0x70,0x73,0x0])
                // console.log("args0="+args[0].readCString())
            }
            this.pathname = args[0]
            this.oflags = args[1]
            this.mode = args[2]

        },
        onLeave: function (retval) {
            console.log("retval="+retval+"---"+"pathname="+this.pathname.readCString()+"---oflags="+this.oflags)
            if(this.pathname.readCString().indexOf("libmsaoaidsec")!=-1){ // 过了惠头条
                retval.replace(0xffffffff)
            }
            console.log("open pathname="+this.pathname.readCString()+"---oflags="+this.oflags)
            if(this.pathname.readCString().indexOf("/proc/")!=-1 && this.pathname.readCString().indexOf("maps")!=-1){
                retval.replace(0x0)
            }
        }
    })
}
```

我们来hook一下open函数 并打印堆栈，自下而上找到frida检测逻辑代码的点，并学习此检测。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQyNm3ib2xpIXicW8qcNDm7LmoZ7sb0cwbfAYMSZVP9P8vycyMNqUx05bJA/640?wx_fmt=png&from=appmsg)

发现有一个so在不断获取/proc下的状态信息。

```
retval=0x7b---pathname=/proc/13205/status---oflags=0x0
open pathname=/proc/13205/status---oflags=0x0
targetFunction called from:
0x7bfdefd314 libmonochrome_64.so!0x3c0b314
0x7bfdefd314 libmonochrome_64.so!0x3c0b314
0x7bfdefd314 libmonochrome_64.so!0x3c0b314
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQys3OegH16vF0yHu0QseibyTeV35Tibypibfiad73mRTBZHf1w3XAAK8GOiag/640?wx_fmt=png&from=appmsg)

搜索发现这貌似是一个sdk的附属so，不是作者自写so。

据搜集发现，应该是和webview的实现有关。

故pass。

> [!tip]
>
> 逆向工程中搜集信息是一个非常重要的环节，不要吝惜你的谷歌不用。
>
> 有很多大佬已经给你铺好了路。
>
> 这句话写给你们，也写给我自己，这真的很重要。

###

### 使用线程法定位anti位置（目前通用，不排除日后新的框架出现导致复杂情况出现）

> [!note]
>
> 在寻找frida的各种方法中，我们分为两条路线:
>
> 一种是以anti-frida-su.js为主的，去**满足正常环境**的要求，去各种抹除掉frida注入后的种种痕迹，但是这是致命的，因为frida有无数种特征，你无论如何是**抹除不完**的，不如重新按照frida写一个自己的HOOK工具。但是幸运的是，有无数大佬为我们铺路，例如非虫大佬的11个patch，能够过掉市场上百分之70的检测，但这是远远不够的。
>
> CRC检测的出现让魔改的frida也无法招架得住。例如，**对libart.so的prettymethod的方法的不可规避的注入**，让frida无处遁形。我们该怎么办？
>
> 非虫大佬已经给出了答案：修改hook pretymthod的hook时机，这样能过掉百分之5左右的样本（为了节约用户硬件资源，启屏后就会关闭），**但是大部分样本还是通过开启线程进行crc循环检测**
>
> 第一种方法变得更加曲折起来，必须要配合魔改rom以及linux内核来进行进一步隐藏。

**但是请注意，crc检测必须要开启线程来检测，我们来讨论第二种过掉的方法，patch线程**

在正式操作之前，我想和大家讨论检测粒度问题：

> [!note]
>
> 请大家思考，frida的检测粒度一般在什么级别，我们先做假设，假
>
> 如我是一个开发人员，我在进行界面跳转，再或者数据请求后，加几句话，对23946端口的检测（frida检测一个例子，当然没有那么简单），那么frida检测我们可以认为是语句级别的粒度，因为只有几行代码，我们也无法避免，因为我们要进行操作。
>
> 接上部分，我们公司有安全开发人员，给了我一个函数，我不用考虑别的，直接调用即可，那frida检测我们可以认为是函数级别的粒度
>
> 如果我们公司没有开发人员怎么办，当然是外包啦，引入一个安全公司的so，打钱打钱。

接上面的讨论，第一种情况几乎不存在，我既要懂业务也要懂安全，除非我自己是全栈（这种适用于mini App）各大H播软件可能会出现。

第二种情况可能存在，也就是业务代码与安全代码掺杂，也是我们不希望看到的情况，一个线程里既有检测代码，也有业务逻辑代码。即patch掉线程业务也无法运行。

第三种情况是最常见的，一些安全的sdk，对设备评估，基本数据请求加密，以及反调试的实现。

第三种情况也要分两种方式讨论。第一种，纯检测so，没有任何加密行为。我给他归结为so粒度的，那么直接跳过so加载即可。第二种，安全公司提供的so，内部有设备id等加密方式计算，那么跳过就不是那么简单了 我们可以定位so加载的头部位置，在怀疑后，检测so的各个段的加载，定位so大致位置，来进行patch反调试。

使用spawn方法启动frida（不要使用魔改的，看不到退出时间点）。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQykDicN3UK67Se6jaePyu4Yvicf6Vu3YJ8Ub1xwPdd63J8vle417S6Hf6A/640?wx_fmt=png&from=appmsg)

发现开启

```
normal find thread func offset libshell-super.com.showstartfans.activity.so 0x765f7450d0 360656 580d0
```

这条线程的时候，软件挂掉了。

我们增加脚本的过滤条件：

```
else if(so_name.indexOf("libshell-super.com.showstartfans.activity.so")>-1&& offset==360656){

        }
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQyCM43qOmyMQlU3ibZ1QscyAHTK1Xqj63F5eia0jvhqDPS6nwh5TvrGl6A/640?wx_fmt=png&from=appmsg)

发现成功过掉了frida检测。

失败案例：

没有过滤offset==360656，软件直接发生了崩溃，反正鼓励大家多试试。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EcFGAXff9ZIVgda4axWaQy5t4VJOK2t8GV7cH86IR0NywmdYlyPBCgicBpibyeDYozD2DPgiaKhDG3Q/640?wx_fmt=png&from=appmsg)

```
二

进行抓包，并过掉抓包检测
```

ps:本文章不讨论脱qiao，脱qiao好的已经在根目录了，请大家合法使用。

打开抓包后提示网络异常，关闭后就不异常了，确定为抓包检测。

> [!tip]

这一步抓包检测（非证书教研式），有一种特殊方式，需要软路由。

以及透明代理（非证书教研式），考虑到第一种需要设备，第二种需要docker云手机，这里不做讨论。

如何进行抓包检测定位？首先找到登陆的activity，找到登陆函数，一步一步往下跟。

```
var jclazz = null;
var jobj = null;

function getObjClassName(obj) {
    if (!jclazz) {
        var jclazz = Java.use("java.lang.Class");
    }
    if (!jobj) {
        var jobj = Java.use("java.lang.Object");
    }
    return jclazz.getName.call(jobj.getClass.call(obj));
}

function watch(obj, mtdName) {
    var listener_name = getObjClassName(obj);
    var target = Java.use(listener_name);
    if (!target || !mtdName in target) {
        return;
    }
    // send("[WatchEvent] hooking " + mtdName + ": " + listener_name);
    target[mtdName].overloads.forEach(function (overload) {
        overload.implementation = function () {
            //send("[WatchEvent] " + mtdName + ": " + getObjClassName(this));
            console.log("[WatchEvent] " + mtdName + ": " + getObjClassName(this))
            return this[mtdName].apply(this, arguments);
        };
    })
}

function OnClickListener() {
    Java.perform(function () {
        //以spawn启动进程的模式来attach的话
        Java.use("android.view.View").setOnClickListener.implementation = function (listener) {
            if (listener != null) {
                watch(listener, 'onClick');
            }
            return this.setOnClickListener(listener);
        };

        //如果frida以attach的模式进行attch的话
        Java.choose("android.view.View$ListenerInfo", {
            onMatch: function (instance) {
                instance = instance.mOnClickListener.value;
                if (instance) {
                    console.log("mOnClickListener name is :" + getObjC...