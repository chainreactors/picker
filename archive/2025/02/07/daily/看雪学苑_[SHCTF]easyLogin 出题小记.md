---
title: [SHCTF]easyLogin 出题小记
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589327&idx=2&sn=163feb4414326003fc3f84b95ee8b8f6&chksm=b18c280586fba11395ed4f42ce23bd939ce52fd80208ef328b6c4ceb597e9f41b69b9776a33d&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-02-07
fetch_date: 2025-10-06T20:37:22.575268
---

# [SHCTF]easyLogin 出题小记

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxkonehrh1AkrIUUSrPSWEcibqsQycYWMyVCtgHBRS8TByLYHvKial7w9TA/0?wx_fmt=jpeg)

# [SHCTF]easyLogin 出题小记

Shangwendada

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxkTJjwJMBdyiaBmoa0e0ian8E3toqckMTK3GKrJ6oqKd4Gvexia6EQxLvTA/640?wx_fmt=other&from=appmsg)

附上源码，感兴趣的师傅可以看看
*https://github.com/SHangwendada/SHCTF-easyLogin/tree/main*

## 方法1：

改机APP直接改，梭哈。

## 方法2：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxk5P1EiaaAZVWQmZouF2KBU6boPiaxPXch7q367ozGFN5X4FHHk2qDelQA/640?wx_fmt=png&from=appmsg)

直接看主体逻辑，其实就是发送了Username以及password还有passticket，username和password都给我们了，但是passticket并没有给我们，因此需要去逆向，首先根据下面Toast的代码告诉了我们这个可能和设备有关，这个时候需要考虑的验证是否新设备是否使用到设备id之类的。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxkkeVuFcnCM3Om6ibb7aA7nxDwWoBx28kH8DFeRH6K4weKicib9ibnhNtgqQ/640?wx_fmt=png&from=appmsg)

getPassticket注册于easyLogin，那么我们需要使用IDA直接分析easyLogin。

这里我的设备为Arm64 因此我分析的为arm64-v8a，（注意不同设备接下来的操作可能不尽相同，但是原理逻辑基本一致）。

函数列表中没有发现Jni\_Onload，可以确定为静态注册，静态注册直接搜索函数名字就好了：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxkMCqDjfuE5PwePqepZA4DQyayDsxhDzB4y5t9ibXNVlWEL1UI8d0lOUQ/640?wx_fmt=png&from=appmsg)

这里需要注意参数类型变换，可能需要手动更改：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxkLxmk1KzZPrMZO0WQ8MXuwkOK5Z9VBgayhTjGyiamX2QOgFjM4fVVw2A/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxk9xQ6Oadb6GWzO71OPwMSjE117n5wic48ugPDxVCAfYql9dYU2JMRXRw/640?wx_fmt=png&from=appmsg)

可以发现这里有输出Device ID的字样。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxkr7150gn6mRDXrhdr7q8wchMU0CXvLaqrXUG3Gm5kiaFicX6shibfr8Tqw/640?wx_fmt=png&from=appmsg)

那么根据提示，我们的主要目标就是替换掉这个device id。

查看一下数据包：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxka5v2RoMXm7yV1F4GlicmsicYOZ6DaeTkFJAkrBJN0iasTz58Ou2arspRQ/640?wx_fmt=png&from=appmsg)

可以发现passticket上传的并不是设备id，二十哈希之后的设备id，并且显然不是md5值。

这个时候要么分析这个passticket 要么 复现这个哈希算法。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxkrfcicwNt8RHl1kpfm9a50yHibS3dEOfkPjQ7WjLQyuuthDavC9z9nS6w/640?wx_fmt=png&from=appmsg)

看到这里基本也不会有想去逆向哈希算法的思路了。

只有调试或者FridaHook了，但是程序存在hook检测。

主要看init Array段中的一些内容：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxkDiaPAJxZT0o0d1QGqxHqxMA3VQ3Yyh3SchymZpMibHfBPnUt0Tic9VXhQ/640?wx_fmt=png&from=appmsg)

创建了两个线程：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxk6Zu1Nj2T0OB6Zn8w8qibA8CtTvgibvLMjkpCRp08dexT3WxJXOW4Za1Q/640?wx_fmt=png&from=appmsg)

检测IDA的我们不用看，直接撸检测frida的：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxkKtw7Q3hRtfAF1s40oA6E2TBbTCERshJdQKJT6FWxCwtQK7jGiauibopw/640?wx_fmt=png&from=appmsg)

比较了本地和系统的libc中 signal 的前8个字符是否一致，不一致则认为被hook，这里hook点可以在v13==v12。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxkCLBpOlOQwVxsEnqJmickpibnwsibTEjnyr7WqUJk0oB8CFkPkyLnaCUnw/640?wx_fmt=png&from=appmsg)

修改他们的比较结果即可，这里值的注意的是由于时机问题可以直接hook pthread\_create来hook这个点位。

```
function passAnti1() {
    Interceptor.attach(Module.getExportByName(null, "pthread_create"), {
        onEnter: function (args) {
            this.funAddr = args[2];
            var instruction = Instruction.parse(this.funAddr.add(0x2b4));
            if (instruction.mnemonic === "cmp") {
                Interceptor.attach(this.funAddr.add(0x2b4), {
                    onEnter: function (args) {
                            this.context.x25 = this.context.x24;
                    }
                });
            }
        },
        onLeave: function (retval) {

            console.log("pthread_create returned");
        }
    });
}
```

或者重定向fread：

```
function hook_memcmp_addr() {
    //hook反调试
    var memcmp_addr = Module.findExportByName("libc.so", "fread");
    if (memcmp_addr !== null) {
       // console.log("fread address: ", memcmp_addr);
        Interceptor.attach(memcmp_addr, {
            onEnter: function (args) {
                this.buffer = args[0];   // 保存 buffer 参数
                this.size = args[1];     // 保存 size 参数
                this.count = args[2];    // 保存 count 参数
                this.stream = args[3];   // 保存 FILE* 参数
            },
            onLeave: function (retval) {
              //  console.log(this.count.toInt32());
                if (this.count.toInt32() == 8) {
                    Memory.writeByteArray(this.buffer, [0x50, 0x00, 0x00, 0x58, 0x00, 0x02, 0x1f, 0xd6]);
                    retval.replace(8); // 填充前8字节
                  //  console.log(hexdump(this.buffer));
                }
            }
        });
    } else {
        console.log("Error: memcmp function not found in libc.so");
    }
}
```

最后我们的脚本还需要注意时机，这里给出完整的重定向的代码：

```
function hook_memcmp_addr() {
    var memcmp_addr = Module.findExportByName("libc.so", "fread");
    if (memcmp_addr !== null) {
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
        console.log("Error: memcmp function not found in libc.so");
    }
}

function NativeHook() {
    var base = Module.getBaseAddress("libeasylogin.so");
    console.log("[Base]->", base);

    Interceptor.attach(base.add(0x1F250), {
        onEnter: function (args) {
            try {
                var originalStr = this.context.x0.readCString();
                console.log("Original x0:", originalStr);
                var newValue = "a24256ec5983b4a8";

                if (newValue.length <= originalStr.length) {
                    Memory.writeUtf8String(this.context.x0, newValue);

                    console.log("Modified x0:", this.context.x0.readCString());
                } else {
                    console.warn("New string is longer than the original. Skipping write to avoid overflow.");
                }
            } catch (e) {
                console.error("Error modifying x0 content:", e);
            }
        }
    });
}

function Hookdlopenext() {
    hook_memcmp_addr();
    var dlopen = Module.findExportByName(null, "android_dlopen_ext");
    Interceptor.attach(dlopen, {
        onEnter: function (args) {
            var filePath = args[0].readCString();
            console.log("[android_dlopen_ext] -> ", filePath);
            if (filePath.indexOf("libeasylogin") != -1) {
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

本题没有标准解，师傅们可以打开思维，需求更多的破解方式，体会Re的乐趣。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HLLM8qZjL9RwTabxunibQxkBCtNW1OMQcSsrTUQjFsNdhLoDz1xhcXWaS1icMy12vzRribaHKibY8hlA/640?wx_fmt=png&from=appmsg)

看雪ID：Shangwendada

*https://bbs.kanxue.com/user-home-979679.htm*

\*本文为看雪论坛优秀文章，由 Shangwendada 原创，转载请注明来自看雪社区

# 往期推荐

1、[PWN入门-SROP拜师](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579476&idx=2&sn=4f9adc1e7d61c7357bdc85ba654f24cb&chksm=b18dc29e86fa4b88c483a581131de043b076918cd7c7436a82e9bb56bc37c8f1edf6c87d8350&scene=21#wechat_redirect)

2、[一种apc注入型的Gamarue病毒的变种](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579387&idx=1&sn=9d6fbf25f11b3d99c92c5ac8de0587d5&chksm=b18dc13186fa4827ae7a7bf909e0d2b9490c6df4417c1d7eebc27127133daa9771c212b4f310&scene=21#wechat_redirect)

3、[野蛮fuzz：提升性能](http://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458579145&idx=1&sn=9134327916f678cfe7e2bc3371cedeaf&chksm...