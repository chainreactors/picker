---
title: Win10 x64 APC的分析与玩法
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458497622&idx=1&sn=51722755c61ffa41c3f1b47d4460d29b&chksm=b18e82dc86f90bcab176d369766f5a41ff801847d611681782d8468ed0a620274a72ed5e6d5d&scene=58&subscene=0#rd
source: 看雪学院
date: 2023-03-11
fetch_date: 2025-10-04T09:16:17.637755
---

# Win10 x64 APC的分析与玩法

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hs2UeTibknNTXkSN2BibAcgYrVsUSgjicgVq2eb5OYrMXk1EcT6iceKOVTuptgyhSpLGxrUwzMP9QE0g/0?wx_fmt=jpeg)

# Win10 x64 APC的分析与玩法

icey\_

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hs2UeTibknNTXkSN2BibAcgYYiaqUYG0YXGWtGiaLACsf3TPHxNmrb76KuC0XoJuEuvpJtzFbaGt5M5g/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：icey\_

这段时间没啥事干，就断断续续把 Windows 的 APC机制给分析了一下，发现许多地方还是比较有趣的，例如：用户特殊APC一开始是插入到内核APC链表中的，然后再通过它的 kernelroutine 将APC插回用户APC链表。

还发现了我调试的这个win10版本在用户特殊APC执行的时候的存在的BUG。

APC的作用我这里就略了，可以百度一下。

Windows 10版本（同以前文章的版本）：

```
https://bbs.kanxue.com/thread-276036.htm
```

文档pdf版本和相关资料下载：

```
如果网络文档内的“跳转”无法使用，推荐阅读PDF版本链接：https://pan.baidu.com/s/1owtKjfL80f1WbQj4blIoKQ提取码：ICEY
```

#

#

```
一

APC结构
```

###

### \_KAPC\_STATE

```
ntdll!_KAPC_STATE   +0x000 ApcListHead      : [2] _LIST_ENTRY   +0x020 Process          : Ptr64 _KPROCESS   +0x028 InProgressFlags  : UChar   +0x028 KernelApcInProgress : Pos 0, 1 Bit   +0x028 SpecialApcInProgress : Pos 1, 1 Bit   +0x029 KernelApcPending : UChar   +0x02a UserApcPendingAll : UChar   +0x02a SpecialUserApcPending : Pos 0, 1 Bit   +0x02a UserApcPending   : Pos 1, 1 Bit
```

kthread.ApcState 指向 \_KAPC\_STATE

**ApcListHead：**

ApcListHead[0] 指向 内核APC链表

ApcListHead[1] 指向 用户APC链表

当 ApcListHead.Flink == ApcListHead.Blink == &ApcListHead.Flink 时，APC链表为空

否则 ApcListHead.Flink = & \_KAPC.ApcListEntry，ApcListHead.Blink = & \_KAPC.ApcListEntry

**Process：**

线程所属或者所挂靠的进程

**InProgressFlags：**

是否有APC正在执行 :

第0位置1：内核APC正在执行

第1位置1：特殊APC正在执行

**KernelApcPending：**

是否有内核APC正在等待

**UserApcPendingAll：**

用户APC正在等待

第0位置1：用户特殊APC正在等待

第1位置1：用户普通APC正在等待

###

### **\_KAPC**

```
ntdll!_KAPC   +0x000 Type             : UChar   +0x001 SpareByte0       : UChar   +0x002 Size             : UChar   +0x003 SpareByte1       : UChar   +0x004 SpareLong0       : Uint4B   +0x008 Thread           : Ptr64 _KTHREAD   +0x010 ApcListEntry     : _LIST_ENTRY   +0x020 KernelRoutine    : Ptr64     void   +0x028 RundownRoutine   : Ptr64     void   +0x030 NormalRoutine    : Ptr64     void   +0x020 Reserved         : [3] Ptr64 Void   +0x038 NormalContext    : Ptr64 Void   +0x040 SystemArgument1  : Ptr64 Void   +0x048 SystemArgument2  : Ptr64 Void   +0x050 ApcStateIndex    : Char   +0x051 ApcMode          : Char   +0x052 Inserted         : UChar
```

### Type和Size：内核层对象必须存在的常量值。

### Thread：目标线程内核对象。

### ApcListEntry：APC链表。

### KernelRoutine：无论那种APC，都会先执行这个函数（以内核的身份）。

### RundownRoutine：如果插入APC失败，则会调用这个函数（详情查看 APC插入 篇）。

### NormalRoutine：我们想让线程执行的函数（内核函数 或 用户函数）。

### NormalContext：第0个参数。

### SystemArgument1：第1个参数。

### SystemArgument2 ：第2个参数。

### ApcMode：APC的类型：0内核APC 1用户APC。

### Inserted：一个布尔标志，指示 APC 是否已插入。

#

#

```
二

APC插入
```

##

## **R3**

我们就不讨论QueueUserAPC这个函数了，因为他最后是调用NtQueueApcThread进入R0的。

**QueueUserAPC调用栈如下：**

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIX5Eib0321vlmCpHvcqGZEh1pzIndMWicQ3h2yoXBtiatpvV49GtuC4l8Q/640?wx_fmt=png)

所以呀，我们直接 干R0的NtQueueApcThread就行啦！

##

## R0:

```
NTSTATUS __stdcall NtQueueApcThread(        HANDLE ThreadHandle,        PKNORMAL_ROUTINE ApcRoutine,        PVOID NormalContext,        PVOID SystemArgument1,        PVOID SystemArgument2){  return NtQueueApcThreadEx(ThreadHandle, 0i64, ApcRoutine, NormalContext, SystemArgument1, SystemArgument2);//通过NtQueueApcThread申请的APC全是用户普通APC}
```

##

## 我们可以发现！NtQueueApcThread里面只是调用了NtQueueApcThreadEx。

说明NtQueueApcThread就是一个被阉割功能的函数。

注意1：当用户APC触发时，返回的一定是R3的ntdll!KiUserApcDispatcher，然后ntdll!KiUserApcDispatcher再调用ApcRoutine。

注意2：QueueUserApc在插入APC调用NtQueueApcThread时，参数ApcRoutine是 ntdll!RtlDispatchAPC，并不是我们提供给QueueUserApc的函数指针。我们的函数指针需要由ntdll!RtlDispatchAPC再次分发执行。

及 NtQueueApcThread的第二个参数为ntdll!RtlDispatchAPC，第三个参数才是我们我们提供给QueueUserApc的函数指针。

QueueUserApc简直就是NtQueueApcThreadEx的二次阉割函数。（）

我们继续分析NtQueueApcThreadEx：

###

### **NtQueueApcThreadEx：**

```
NTSTATUS __fastcall NtQueueApcThreadEx(        void *ThreadHandle,            //需要插入的线程句柄        BOOLEAN flag,                //0：用户普通APC  1：用户特殊APC        __int64 ApcRoutine,            //需要执行的APC函数指针        __int64 NormalContext,        //需要执行的APC函数的第零个参数        __int64 SystemArgument1,    //需要执行的APC函数的第一个参数        __int64 SystemArgument2)    //需要执行的APC函数的第二个参数
```

###

### 这个函数首先会判断一些参数是否正确，例如：会判断我们给的ApcRoutine地址合不合理。不允许给0。

说明从R3调用函数插入用户APC，APC的NormalRoutine不能为0，非常可惜。少了很多玩法。

####

#### 内部分析1（节选）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppI8axDVUy7P2jtibiaYhpeJEQRjwRw4iaCAcN7XhcMq7axUibMB84NvahNbg/640?wx_fmt=png)

可以看出，如果(flag != 0 && flag != 1)，那么就会执行这段代码。

这个类型的APC不同于一般的用户APC（用户普通APC 和 用户特殊APC）

主要的区别就是 \_KAPC的地址空间是通过特殊手段申请和释放的，并且 KernelRoutine 和 RundownRoutine 和一般的用户APC不同。

####

#### 内部分析2（节选）：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIccA95N3n83Gk6gicD3Fb3RNlTwlSltv90o1ianXrCwNMnibxE2ibNeOeIw/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIy5L9acWPZibgYOcxuatadS3RFqC0WoicDhnhZPgy5iaOXPwrqjMdOUuLA/640?wx_fmt=png)

可以看出：

1、一般的用户APC的\_KAPC都是通过ExAllocatePoolWithQuotaTag申请，且大小为0x58。

2、用户普通APC的 KernelRoutine = SC\_ENV::Free；而用户特殊APC的 KernelRoutine = KeSpecialUserApcKernelRoutine；

3、用户普通APC和用户特殊APC的 RundownRoutine = ExFreePool;

如果插入失败！则会调用RundownRoutine释放申请的 \_KAPC 的内存。

####

#### **KeInitializeApc：**

填充\_KAPC的各个成员。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIAJQe7qPCnS2QEB8E5TV1ibp8MibdbUBy2IQ4OWDg26vKVpnkCjb5TJ4g/640?wx_fmt=png)

这里补充一个非常离谱的设定：

通过NtQueueApcThreadEx插入用户APC时：

当初始用户普通APC时，传入a7 = 1，用户特殊APC时，传入a7 = 0。

然后ApcMode的值竟然由 a7 来确定！

那么说明我们注册的 用户特殊APC，它的 ApcMode 竟然是 0 ！

也就是说待会插入时，是插入的内核APC链表。（详情见下文）

####

#### **KeInsertQueueApc：**

这个函数主要作用就是上锁，填充APC的两个参数指针。

然后调用函数将APC插入 \_KTHREAD.\_KAPC\_STATE（内核APC和用户APC都是通过这个函数插入！）。

然后解锁。

**上锁部分：（略）**

填充参数指针、插入APC部分：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppILqD03NhTncZ4T2enjVctqybxEF6vQrxsFLVmGXpLqmQLd1qic8yuNxg/640?wx_fmt=png)

KiDeliverApc把这个用户特殊APC视作内核APC，并执行它的KernelRoutine = KeSpecialUserApcKernelRoutine，

KeSpecialUserApcKernelRoutine会把这个用户特殊APC重新插入到用户APC链表内。

####

#### **KiInsertQueueApc：**

这个函数的功能就是将 \_KAPC 插入 \_KTHREAD.\_KAPC\_STATE。

用户APC 插入 \_KAPC.ApcListHead[1]

内核APC插入\_KAPC.ApcListHead[0]

#####

##### 第一步：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIRLKc4oGFhARhxdHGa53ibyRE9ILdrZlFicHKzPa6mh8QrJ4Jpbp4Ue0w/640?wx_fmt=png)

\_KTHREAD.ApcStateIndex表示这个线程当前是否附加到其他进程。0：没有、1：附加到了其他进程。

\_KTHREAD.ApcState是这个线程当前需要执行的APC。

\_KTHREAD.SaveApcState是这个线程的备份APC。

当需要插入的 \_KAPC.ApcState != 0时，直接插入线程的ApcState。

当需要插入的\_KAPC.ApcState == 0 && 需要插入的线程未附加到其他进程时，直接插入线程的ApcState。

当需要插入的\_KAPC.ApcState == 0 && 需要插入的线程已经附加到其他进程时，插入线程的SaveApcState。

关于\_KTHREAD.ApcStateIndex、\_KTHREAD.ApcState、\_KTHREAD.SaveApcState三者的关系:

设：

有两个进程：进程A、进程B。和一个线程A\_T是属于进程A的。

此时：A\_T(\_KTHREAD).ApcStateIndex = 0。

接下来，线程A\_T将要执行KeStackAttachProcess附加到进程B，那么会发生：（代码节选自KiAttachProcess）

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppImWUYibE3GvwJOP038f8mzak7BiaibT7Nicrdc9W8m8cN8JYTd9TosSfnKQ/640?wx_fmt=png)

将原有的ApcState备份到SaveApcState，然后将用户APC清空，再将 ApcState置1。当然了，解除附加状态的时候，会把SaveApcState恢复到ApcState，然后将ApcState置0（代码就不贴图了）。

#####

##### 第二步：

插入APC，插入方式分为两类（插入链表头部、插入链表尾部）：

用户普通APC 和 内核普通APC 和 用户特殊APC第一次 的插入方式：

插入链表头部。

注意！一开始用户特殊APC的 ApcMode = 0，也就是说，这个时候，用户特殊APC 插入的是内核APC链表！

用户特殊APC第一次插入也是通过这段代码插入，插入到内核APC链表。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppIxhmWjR6P2BZjaDL7KFeGqww4WMXMia6KOw8O68qyDz4pDhxuZPTSxKA/640?wx_fmt=png)

那用户特殊APC插入到了内核APC链表，这不是乱套了吗？其实并没有，阿三哥这个地方整了一手骚操作：还记得 用户普通APC的 KernelRoutine = KeSpecialUserApcKernelRoutine吗？

它会将这个APC重新插入用户APC链表。（下文详解）

用户特殊APC！第二次！插入方式：

（KeSpecialUserApcKernelRoutine会将APC重新插入到 用户APC链表）

将 ApcState.UserApcPendingAll or 1 后，将此APC插入链表尾部。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EyFXPvbXzlric8fjr0FKppI2V4dPR2DtWF6SYod5fzCjtibRR35IlIgUqldRwuGKbg0cIyNY6dX9QA/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_pn...