---
title: [SUCTF2025] SU_APP、SU_Harmony 出题小记
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589294&idx=1&sn=9843c5f997dc4268b2cceefeef11c2d9&chksm=b18c28e486fba1f2def30ae2ad36fb881a2d6b3ae21e83fb24cd04f74d14f7fbfae69daac012&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-28
fetch_date: 2025-10-06T20:10:02.900196
---

# [SUCTF2025] SU_APP、SU_Harmony 出题小记

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXXiaO1j6GoerDxOugHlibyBVPtxxbq93rwdZFF7f2nsUHADC7fYk53o2w/0?wx_fmt=jpeg)

# [SUCTF2025] SU\_APP、SU\_Harmony 出题小记

Shangwendada

看雪学苑

本次SUCTF主要提供了两道赛题，分享一下出题思路，以及解题思路。

```
一

SU_APP
```

##

本题主要是自定义linker加固so，然后还有一个ffi动态调用的，剩下的就是常见的约束求解了。linker来自于ngiokweng，不得不说ngiokweng大佬对于ELF加载流程的熟练度是真的高。

自实现linker加固详情可见：*https://bbs.kanxue.com/thread-282316.htm*

另外：这题我主要还是想考动态的一些处理方式，比如说过hook检测去hook那个魔改的md5结果或者直接拿到RC4处理后的Sbox的，所以就诞生了那个md5的魔改，并不是我为了魔改而魔改（师傅们别骂辣）

另外本题存在一些释放静态资源的行为，可能高版本的手机必须得弹窗请求授权才可以，所以会导致崩溃，但其实这样的话手动释放一下assets可能就可以避免这个问题了。还有一些奇奇怪怪的崩溃问题也可能是inlinehook误检测导致的，其实在这里整个APP的log我是没有删除的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXQnxWaYfKMup6CMYE6gXFibDFDBfzSkP9kYT6Xic6u1th0RZf9OKbtRGw/640?wx_fmt=png&from=appmsg)

如果在logcat中能看到GO!那么基本是检测问题。

由于我只有RedMi 10X和Pixel2可以测试，就没有适配更多的收集了（考虑的不够周到，给各位磕一个。

言归正传，接下来从出题人的设计思路上去看看如何解决这道题。

### Java层分析

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXwoh0plf6wQrIRe2NVTPch8XIpm7vKGnS8BLhXcuDUFKiaW4jtRiaFy2A/640?wx_fmt=png&from=appmsg)

很简单可以发现，Java层其实就只是做了一下签名验证，释放静态资源，以及调用Native层的验证方法，主要逻辑都在于Native层中，注册了一个叫做Check的方法。

### Native层分析

#### 静态分析so的处理过程

首先对于这个Native层，可以看到一个MainActivty\_check，不知道大家有没有被骗到呢。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXQovq2zIlzFYBib7JwljvYEENabp9NkHiaKZ6TUX1ib8F1wuUUvwd1rIiaA/640?wx_fmt=png&from=appmsg)

其实不难发现这个MainActivty\_check少了点东西，相较于正常的少了一个"i"

那么其实我们需要，去分析JniOnload:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXIhg07dClvcQbHliaVV7icJaR13Nic1OrbaiajZ57umk5ibE0IcCGMbNTRDw/640?wx_fmt=png&from=appmsg)

在JniOnload里面找到了一个注册的方法，我们看看具体逻辑。

如下函数进行了一个loader行为：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjX6PCfFBmN7ANGeTEGwmicR3KdJgNeRZWGstjZ08y75gRRYic6hzRnzEqw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjX5vibJagQibtlWhM4Tj19ee5E49vicibicysJF7dJCvPFV8bawGicQYVwsfhg/640?wx_fmt=png&from=appmsg)

根据下面的特征等也可以发现是一个自定义的linker：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXBqlDiaEAkFM2uy2w9Z0lM6AgOs8DO8GRxYTbacibHVCW6xDkOcUcibThA/640?wx_fmt=png&from=appmsg)

那么loader了什么呢？

在之前的代码中其实已经体现出来了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXj1TnBuaetHQE1GZ8z2yhicY6uvuLWDeL3MZ4wRtFFXxMibtPpJfhG5BA/640?wx_fmt=png&from=appmsg)

files下面的main，那么这个是哪儿来的呢？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXCv1K8NfHMaibXIwaNrNek3tXqichibjU9YuQqUAicaqSes3e99ePiaFLtWw/640?wx_fmt=png&from=appmsg)

欸嘿，其实就是asssets里的main辣。

好，那么我们继续看一看main是个什么玩意。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXKbzdgiciblXKn49oC8X1miaibpRUMDrkV6gAYHdjQTahvicHubpcUH4HmMw/640?wx_fmt=png&from=appmsg)

教练，怎么是个x86？

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjX2kzLfanumXc8G1UNtU3YRLYf5viaUU2G93iag1vFIvMDibjdrcgSFQ5KA/640?wx_fmt=png&from=appmsg)

且听我细细道来：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXlBX28dkUCwCLdVibGXs6kr9YicprtPibJN91bCP5ibrEWAVGj0L0ZWDktg/640?wx_fmt=png&from=appmsg)

大家可以关注一下ngiokweng的自实现linker的代码，我在其代码上做了一部分的改动。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXBKKhiajxacAaibUYuSygBqTyicAzDTyibUkCqYUZzev96Wtf50mbpyZlcA/640?wx_fmt=png&from=appmsg)

可以看到最主要的改动在映射main的内存的时候，这里其实跳过了前面0x91f0字节的映射，恰恰这个0x91f0的大小就是前面的x86程序的大小。

在IDA中的试图如下：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXeKfveQk1YIeH8pEdGd30QwxOKGAQmIky9HJycUCjql9PDRGEL2NibuA/640?wx_fmt=png&from=appmsg)

那么其实使用010打开main我们就能发现端倪了。

看到0x91f0的位置出现了一个SUCTF{You\_Find\_Me}，这好像也不太对，我们继续往后看。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXuYB5fnRaOPRcYSiczN2XH60lO07hw8h7IeHP0e9BQFFcvJJ9xV14rqQ/640?wx_fmt=png&from=appmsg)

我们查看偏移后的内存被传到哪儿去了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXxtwl64fVWSLP1Pt3U3kkWescic0z6cVrI2Sy94Fpiag8gRESJ8AG1BHw/640?wx_fmt=png&from=appmsg)

会发现在sub\_21EE4里面有一个非常可以的操作：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXic9Q1P1GMScNFbEsicAPdxoEiczZzTMPkvnDSQq1m80RR6Xqnia2IolnUA/640?wx_fmt=png&from=appmsg)

这里veorq\_s8

是个非常典型的向量操作，我们看看他都干些啥：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXEYaIj6UKP8PHSpRQIs2Fg9sRicAdrb5tmCCicjUpicbFHrj6icjcwvavBQ/640?wx_fmt=png&from=appmsg)

主要做了一个异或操作，在代码中显然就是异或0x3c，我们看看这个stru异或之后是什么呢

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjX6N4RDklwGfmkvnlMlxjtn0lhlksy8w2uGRe6CE3dDIyXpic4RNjHLkQ/640?wx_fmt=png&from=appmsg)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXrwyK2uw2ZuRNX7Wia5BnR1icOW1KkoGzFCoqN6eNiaXVr2z4k8792r8vw/640?wx_fmt=png&from=appmsg)

7f 45 4c 哈哈哈，ELF头！

那么其实解密头就是在这里了

[小声说]：其实这个ELF头是专门留给大家修复这个so文件，不用大家去计算偏移地址啥的修复elf头了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXw88z3ugGJVtaIF8YjphGyadxX7HOpKSTSXhSf7I7nrMGqHME96Z3iaw/640?wx_fmt=png&from=appmsg)

下面有一个504长度的赋值就不用我多说了吧，修复完elf头的话你看到程序头数量有9个其实504正好就是9\*0x38这个就是在回填我们的程序头了。

做完这些其实我们的ELF文件就能修好了，但是这里是首先带大家静态分析一下，那么其实还是有动态一把梭的办法的。

#### frida dumpso

首先针对一下这个frida检测，其实就是一个inlinehook的检测检测的libc中的signal，其实这就是frida的一个小特征了。可能有一些类似于vivo之类的厂商他们启动崩溃可能就存在厂商自己魔改了或者啥的可能性，这里我没有响应的手机，就不太好测试了。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXcqwg4zO9I1yEh9CrgAHKsbFmZ8ibvzbNF6gBia5uCiaWvelYMSRzxSMyA/640?wx_fmt=png&from=appmsg)

比较点在这里，其实只需要hook掉这个点就OK了。

下面是一个hook fread的通用方法：

```
function hook_memcmp_addr() {
    var memcmp_addr = Module.findExportByName("libc.so", "fread");
    if (memcmp_addr !== null) {
        console.log("fread address: ", memcmp_addr);
        Interceptor.attach(memcmp_addr, {
            onEnter: function (args) {
                this.buffer = args[0];
                this.size = args[1];
                this.count = args[2];
                this.stream = args[3];
            },
            onLeave: function (retval) {
                if (this.count.toInt32() == 8) {
                    Memory.writeByteArray(this.buffer, [0x50, 0x00, 0x00, 0x58, 0x00, 0x02, 0x1f, 0xd6]);
                    retval.replace(8);
                }
            }
        });
    } else {

    }
}
```

有了这个之后我们就是一套很基础的流程来hook了：

首先hook android\_dlopne\_ext 来hook，libsuapp。

Native hook什么逻辑咱先不说

```
function Hookdlopenext() {
    hook_memcmp_addr()

    var dlopen = Module.findExportByName(null, "android_dlopen_ext");
    Interceptor.attach(dlopen, {
        onEnter: function (args) {
            var filePath = args[0].readCString();

            if (filePath.indexOf("suapp") != -1) {
                this.isCanHook = true;

            }
        }, onLeave: function (retValue) {
            if (this.isCanHook) {
                this.isCanHook = false;
                NativeHook();

            }
        }
    })
}

setImmediate(Hookdlopenext);
```

这一套hook上了之后我们尽量是稍等一下在进行dump操作。

dump的代码：

```
function dump_so(so_name) {
    var libso = Process.getModuleByName(so_name);
    console.log("[name]:", libso.name);
    console.log("[base]:", libso.base);
    console.log("[size]:", ptr(libso.size));
    console.log("[path]:", libso.path);
    var file_path = "/sdcard/Download/" + libso.name + "_" + libso.base + "_" + ptr(libso.size) + ".so";
    var file_handle = new File(file_path, "wb");
    if (file_handle && file_handle != null) {
        Memory.protect(ptr(libso.base), libso.size, 'rwx');
        var libso_buffer = ptr(libso.base).readByteArray(libso.size);
        file_handle.write(libso_buffer);
        file_handle.flush();
        file_handle.close();
        console.log("[dump]:", file_path);
    }

}
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXlXYGYXrKLxXUE8CJPhJxGiaQVaXQyDp10wO0QdkCQuN53uriazfQFh7A/640?wx_fmt=png&from=appmsg)

dump下来之后我们再从dump的路径里面pull下来

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8E4gvpb3vgYVWnRWiamTMSjXWYeQjNkoZeG7YdOXEhjcSkhSwAlVYQCmudsibD8fa...