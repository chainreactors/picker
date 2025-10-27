---
title: R0下一种简单的Irp包数据捕获方法
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589610&idx=1&sn=f333dbc708e83b89447698abe9b322eb&chksm=b18c292086fba036091e86730f40c21eeb8b300cc513b63eb54e75760da0ab3586c3b04a2cf0&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-02-15
fetch_date: 2025-10-06T20:37:29.242725
---

# R0下一种简单的Irp包数据捕获方法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sicO9KnmsO0g2WcicLDMH3pUqQmr2cXOLEr2za6cZ054d3RY6MULCjL2Q/0?wx_fmt=jpeg)

# R0下一种简单的Irp包数据捕获方法

moshuiD

看雪学苑

本文提出了一种方法可以在内核层使用“过滤”的方法来捕获Irp数据包。其中可以捕获到**进入目标驱动前**与**目标驱动处理完后**的Irp数据包。

```
1

Irp
```

##

现在很多驱动都在使用Irp包的方式来与R3的程序进行通信。Irp是一个结构，由一个管理器进行分配管理。Irp从不单独分配，它总是伴随着多个IO栈位置结构（`_IO_STACK_LOCATION`），所以一般的驱动程序在获取真正的数据时需要使用`IoGetCurrentIrpStackLocation`函数来获取其中的数据。

```
2

设备
```

Windows是以设备（`DEVICE_OBJECT`）为中心的，同时Windows**支持设备分层**。在多层设备的结构中，一个设备是堆叠在另一个设备的上面的，看起来就像一个栈一样，这组设备被称为设备栈。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sWlIdLz4fZfKibFicj04jtkv8SKzrT61PbwH5XcH8ubNxR4HyPZ4tKS1g/640?wx_fmt=other&from=appmsg)

```
3

方法
```

我使用堆叠设备栈的方式，来获取Irp数据包（写过过滤驱动的肯定熟悉）。所以我们需要`IoAttachDeviceToDeviceStack`函数来附加到目标设备，这样就会让调用来的时候，**先到我们的派遣函数**。

问题就变成了我们如何让目标驱动处理完后我们依然可以获取到数据呢？此时解决的关键就是`IoSetCompletionRoutine`函数了，它可以让下层的派遣函数调用`IoCompleteRequest`后到达指定的回调函数。

如下是一些关键代码：

```
VOID DriverUnload(PDRIVER_OBJECT pDriver) {
    PDEVICE_OBJECT deviceObject = pDriver->DeviceObject;
    IoDetachDevice(deviceObject->DeviceObjectExtension->AttachedTo);
    IoDeleteDevice(deviceObject);
    KdPrint(("[+] Release done.\r\n"));
}

NTSTATUS MyCompletionRoutine(PDEVICE_OBJECT DeviceObject, PIRP Irp, PVOID Context) {
    auto ioStack = IoGetCurrentIrpStackLocation(Irp);
    return STATUS_SUCCESS;
}

NTSTATUS Dispatch(_DEVICE_OBJECT* DeviceObject, _IRP* Irp) {

    auto ioStack = IoGetCurrentIrpStackLocation(Irp);
    KdPrint(("Func: %x\n", ioStack->MajorFunction));
    if (ioStack->MajorFunction == IRP_MJ_DEVICE_CONTROL) {
        KdPrint(("IRP_DEVICE_CONTROL\n"));
        KdPrint(("Code: %x\n", ioStack->Parameters.DeviceIoControl.IoControlCode));

        IoCopyCurrentIrpStackLocationToNext(Irp);
        IoSetCompletionRoutine(
            Irp,
            MyCompletionRoutine,
            NULL,
            TRUE,
            TRUE,
            TRUE
        );

    }
    return IoCallDriver(DeviceObject->DeviceObjectExtension->AttachedTo, Irp);
}

extern "C" NTSTATUS DriverEntry(PDRIVER_OBJECT pDriver, PUNICODE_STRING pReg) {
    if (pDriver) {
        pDriver->DriverUnload = DriverUnload;
    }

    UNICODE_STRING name;
    RtlInitUnicodeString(&name, L"设备名");
    PDRIVER_OBJECT targetDriver;

    NTSTATUS status = ObReferenceObjectByName(&name, OBJ_CASE_INSENSITIVE, nullptr, 0,
        *IoDriverObjectType, KernelMode, nullptr, (PVOID*)&targetDriver);

    pDriver->MajorFunction[IRP_MJ_DEVICE_CONTROL] = Dispatch;//这里我只想过滤这个函数。

    if (NT_SUCCESS(status)) {
        PDEVICE_OBJECT targetDevice = targetDriver->DeviceObject;

        PDEVICE_OBJECT fltDev;
        IoCreateDevice(
            pDriver,
            0,
            NULL,
            targetDevice->DeviceType,
            0,
            FALSE,
            &fltDev
        );

        IoAttachDeviceToDeviceStack(fltDev, targetDevice);
        fltDev->Flags &= ~DO_DEVICE_INITIALIZING;
        ObDereferenceObject(targetDriver);
    }
}
```

#

```
4

实验
```

我们针对WinARK的`DeviceIoControl`的数据来进行过滤测试。

为了验证我们数据的正确性，我们查看源码选择获取驱动派遣函数的这个功能进行测试。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sfNofabd0ic1Iq1plg2YoJUzyiahGSQwqlxcKnqEm4Pqfrsl2W0Yc5O5g/640?wx_fmt=other&from=appmsg)

如上是该功能的源码，传入的是设备名字，传回去的是派遣函数数组。

安装好我们的测试驱动后 查看一下自己的派遣函数列表就能捕获到如下信息：

```
IRP_DEVICE_CONTROL
Code: 80002060
systemBuff:0x5c,0x0,0x64,0x0,0x72,0x0,0x69,0x0,0x76,0x0,0x65,0x0,0x72,0x0,0x5c,0x0,0x41,0x0,0x6e,0x0,0x74,0x0,0x69,0x0,0x52,0x0,0x6f,0x0,0x6f,0x0,0x74,0x0,0x6b,0x0,0x69,0x0,0x74,0x0,0x0,0x0
return:0xa0,0x1a,0x91,0x4e,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xa0,0x1a,0x91,0x4e,0x2,0xf8,0xff,0xff,0x60,0x4f,0x91,0x4e,0x2,0xf8,0xff,0xff,0xd0,0x50,0x91,0x4e,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xb0,0x1c,0x91,0x4e,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0x4f,0x91,0x4e,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff,0xc0,0xf9,0xb1,0x32,0x2,0xf8,0xff,0xff
```

经观察可以发现传入的内容的确为`L"\\driver\\AntiRootkit"`，传出的内容则是派遣函数列表（总长度为0x1b \* 8）。已第一个为例则是`0xFFFFF8024E911AA0`，对比发现无误。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sJmvOFJxU3peIQJm8aKbArx4Y0lUI6f6sorksQJvmQaAWHjB9dBibolw/640?wx_fmt=other&from=appmsg)

![图片](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sHpuictBC4hHxibK105X2Qbl2aRH2BXSAEfLreajmbrw8L2BAyE2vw3uQ/640?wx_fmt=png&from=appmsg)

看雪ID：moshuiD

*https://bbs.kanxue.com/user-home-932553.htm*

\*本文为看雪论坛优秀文章，由 moshuiD 原创，转载请注明来自看雪社区

# 往期推荐

1、[关于PAN-OS DoS(CVE-2024-3393)的研究](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589341&idx=1&sn=c57db95a9d3d5f4d3d5993b9e4d2398e&scene=21#wechat_redirect)

2、[某cocos2djs游戏jsc以及资源文件解密](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589336&idx=1&sn=bb18ed6fc3311db3e80bc5435a837817&scene=21#wechat_redirect)

3、[[SHCTF]easyLogin 出题小记](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589327&idx=2&sn=163feb4414326003fc3f84b95ee8b8f6&scene=21#wechat_redirect)

4、[车机OTA包解密](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589307&idx=1&sn=f7c4f8fab0e756cd0249e052d5c9e9fe&scene=21#wechat_redirect)

5、[浅析代码重定位技术](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589301&idx=1&sn=f8b5a4c4740123d4431ccb68a9063f17&scene=21#wechat_redirect)

6、[关于PAN-OS DoS(CVE-2024-3393)的研究](https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458589300&idx=2&sn=e9f874ab1024ce5d7a8a2a424b891a7f&scene=21#wechat_redirect)

![图片](https://mmbiz.qpic.cn/mmbiz_jpg/Uia4617poZXP96fGaMPXib13V1bJ52yHq9ycD9Zv3WhiaRb2rKV6wghrNa4VyFR2wibBVNfZt3M5IuUiauQGHvxhQrA/640?wx_fmt=other&wxfrom=5&wx_lazy=1&wx_co=1&tp=webp)

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sOP1la9rjSnIVk6jqzDqP5eWKzqayD4KAfiaCevicJroDJLZXXO7YgEog/640?wx_fmt=gif&from=appmsg)

**球分享**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sOP1la9rjSnIVk6jqzDqP5eWKzqayD4KAfiaCevicJroDJLZXXO7YgEog/640?wx_fmt=gif&from=appmsg)

**球点赞**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9sOP1la9rjSnIVk6jqzDqP5eWKzqayD4KAfiaCevicJroDJLZXXO7YgEog/640?wx_fmt=gif&from=appmsg)

**球在看**

![](https://mmbiz.qpic.cn/sz_mmbiz_gif/1UG7KPNHN8GBLT7N6TtAJXhEaibHU8J9st2udk9oxgGec5phHNnQqmmiasj6lYtxN4eCmibahImXUSqa3qib1H3L8Q/640?wx_fmt=gif&from=appmsg)

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/1UG7KPNHN8EGLfh77kFmnicd9WOic2ibvhCibFdB4bL4srJCgo2wnvdoXLxpIvAkfCmmcptXZB0qKWMoIP8iaibYN2FA/0?wx_fmt=png)

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