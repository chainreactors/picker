---
title: App算法分析——适合进阶学习
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458569233&idx=1&sn=3a07a396aa8b08e4940e2136e444afc1&chksm=b18dfa9b86fa738dc50afb40381465176ff0f9835dfcc1251f34a7c3c7b6254081152a137c71&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-08-25
fetch_date: 2025-10-06T18:02:32.851195
---

# App算法分析——适合进阶学习

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E2aOoz2rCe9rSUic0CEnR6ibxQbq2ovaIHFsd0BuV0gN7BRZAHS1k1r3faR4iaAFs6gJ59IUGr9XDibg/0?wx_fmt=jpeg)

# App算法分析——适合进阶学习

YongG一G

看雪学苑

此贴主要还是对算法本身结构部分描述会多点，过去太久，很多逆向过程不一定能还原，所以可能有部分跳跃的内容，会给具体代码，但对应的偏移地址和具体信息没有，给大家一个锻炼自己的机会。

---

申明：本文涉及的内容是为给大家提供适合大家巩固基础及进阶更高的技术，别做不好的事情哦。

---

##

## 算法分析结构划分

1、查找java调用\*\*gs算法位置，frida主动调用获取参数；
2、unidbg模拟算法so执行；
3、枯燥的边调边复现算法；

---

##

## java调用部分

这部分直接参考其他佬的，挺详细的：https://bbs.kanxue.com/thread-276430.htm

## unidbg模拟执行\*\*gs流程

\*\*gs算法的unidbg模拟执行上面链接里的结果出现以下情况问题解决：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E2aOoz2rCe9rSUic0CEnR6ibB2CqtjroiceMhDyjPIPYdXGO0WeaDVudQRRxMSK2KfmurBIXrPQCT2Q/640?wx_fmt=other&from=appmsg)

###

### 问题一：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E2aOoz2rCe9rSUic0CEnR6ibTLp8Lh0XdmBeRVHQASlAicVQwI4lLgNMz8nuJwa4cwr34OdKQmJ9CibQ/640?wx_fmt=other&from=appmsg)

看到java层和so层都对i2出现了不同参数对应不同功能的分支就要打起精神了，需要判断在走i2=101主体算法获取\*\*gs结果之前是否有走其他流程，明显是的，它执行了i2=103的init初始化部分，你在分析java层调用\*\*gs native算法的时候会看到init部分，so层分析时也能看到i2值会走不同的分支。

所以需要在unidbg里提前执行一步init：

```
// **gs初始化
public void doInit()
{
    //init
    System.out.println("=== init begin ====");
    Object[] init_param = new Object[1];
    Integer init = 103;
    DvmObject<?> ret = module.callStaticJniMethodObject(
         emulator, "main(I[Ljava/lang/Object;)[Ljava/lang/Object;",
         init,
         ProxyDvmObject.createObject(vm, init_param));
    System.out.println("=== init end ====");
}
```

###

### 问题二：

\*\*gs算法过程会调用具体的两个资源文件，位置在解压文件夹assets里，后缀是.\*\*g.jpg和.\*\*g.xbt，通过unidbg自带的HookZz框架将这两个本地文件先入内存再写入到寄存器里（这部分我不贴代码了，新手可以练练手）。

### 问题三：

这个问题就是需要你手动去利用unidbg调试算法过程，去查看控制台报红日志代码位置点在哪，追溯为什么会走这个报红日志，去手动修改这些点，这里我就直接贴代码给大家：

```
//patch C0 53 00 B5, 将反转条件跳转CBZ-->CBNZ  会报：[main]E/**G: [make_header:491] [-] Error pp not init
        byte[] CBNZ = new byte[]{(byte) 0xC0, (byte)0x53, (byte)0x00, (byte)0xB5};
        UnidbgPointer p = UnidbgPointer.pointer(emulator,dm.getModule().base + 地址);
        p.write(CBNZ);
        MyDbg.addBreakPoint(dm.getModule(), 地址, (emulator, address) -> {
            System.out.println("====== patch 反转条件跳转CBZ-->CBNZ ======");
            return true;
        });

        //干掉一个free  （这个会影响结果） 会报：[main]E/**G: [make_header:491] [-] Error pp not init
        byte[] NOP = new byte[]{(byte)0xC1F, (byte)0xC20, (byte)0xC03, (byte)0xD5};
        UnidbgPointer p = UnidbgPointer.pointer(emulator,dm.getModule().base + 地址 );
        p.write(NOP);
        MyDbg.addBreakPoint(dm.getModule(), 地址, (emulator, address) -> {
            System.out.println("======= 干掉一个free =======");
            return true;
        });
```

这些问题主要还是动手能力的体现，就算天赋异禀，也要老老实实的动手。

最终会看到满意的结果：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E2aOoz2rCe9rSUic0CEnR6ibibEoJ4UnzUgmE5zdTzTepofcjr054BqIlu2BTyp1AV3sPP8Xlbp3RMQ/640?wx_fmt=other&from=appmsg)

##

## \*\*gs算法分析

首先看下\*\*gs的结果：

```
{
"b1":".**g.xbt文件名",
"b2":"***",
"b3":"***",
"b4":"yY8lbpaUOZeQ3fyCiccRrM66O+Nzo/mhwP4wIa8C8JOZ6aJgSdfTJl2a6Q4oeMBx+2P4ySmoN/AtDHutJNGd/lImZaXQkwd00ZyfFGn2PmTk4uorMcnQUrKbmPRHlcKx6iOwmt8RoYf9C7l7bGWQ/COl6HcUT199wCWGjI5+u4mxfvLmiCSqhJ8qbLgVx9KQrRLXW1oDY1sf1RdNl1cYe6GfpF8kwgNMQJif9EIUBw0Td64cduT7MKAFjA3oew02IyWX2aSJaOuWaULTUqO4al9SIyRYojxQCEiMzF5UMxV6Zwu2lw1uZ6+22fJgxbEBv2LeGUpPPzXGF6E2vC0vb9sE5in3CkrKHwM+QfA5CasSPwpAmzQyr5iGyl9o6g==",
"b5":"7e640fcb8293d390b3758974b75e9dad5082bed9",
"b7":"1724176633106",
"b6":"30ed898f8d129b6d16c3f0c49efae07e8de4ee0e"}
```

通过重复抓包和执行，确定固定值b1（.\*\*g.xbt文件名）、b2、b3、b7(时间戳，分析过程通过hook固定)。

需要分析b4、b5、b6，其实实际走完算法，主要是考验你对标准算法的熟悉程度（ida脚本Findcrypt），因为并没有出现魔改算法，自定义算法也没混淆，难度不大，但详细写篇幅有点大了，适合新手进阶，所以我说下算法具体实现，就不参照ida和unidbg调试过程手摸手复现。

### 分析前固定时间戳

经验之谈，分析算法过程，时间戳一般都是在算法中主要变动参数之一，为了减小分析影响，我们可以选择固定时间戳值：

so直接搜索获取时间戳的常见函数名进行回溯找到时间戳生成位置：

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8E2aOoz2rCe9rSUic0CEnR6ibVoeSuMsZxsjpE4EMQ3XfhrDGlDu9tNLA8c7V5IlIJXx4ZMWibYpMb7A/640?wx_fmt=other&from=appmsg)

然后通过unidbg的HookZz实现固定。

```
// 固定时间戳 修改获取毫秒时间戳系统函数返回值十六进制
        hook.replace(dm.getModule().base + 地址, new ReplaceCallback() {
            @Override
            public HookStatus onCall(Emulator<?> emulator, long originFunction) {
                return super.onCall(emulator, originFunction);
            }

            @Override
            public HookStatus onCall(Emulator<?> emulator, HookContext context, long originFunction) {
                System.out.println("\n=========== HooZz 修改固定时间戳 =========\n");
                return super.onCall(emulator, context, originFunction);
            }

            @Override
            public void postCall(Emulator<?> emulator, HookContext context) {
                long a = (long) emulator.getBackend().reg_read(Arm64Const.UC_ARM64_REG_X0);
                System.out.println("修改前时间戳："+Long.toHexString(a));
                emulator.getBackend().reg_write(Arm64Const.UC_ARM64_REG_W0,0x18f70ef8d12L);
                System.out.println("修改后时间戳："+ Long.toString(0x18f70ef8d12L,16));
            }
        },true);
```

###

### b4

首先传参拼接一串json：e1:参数三eid，e2：参数二finger和一些常量，e3：时间戳。

这一串json会进行压缩操作，返回值：comp\_json。

```
# 压缩算法
    def fun_compress(self, json):
        # json_len=len(json)
        # # 使用compressBound计算压缩后的最大可能字节数
        # comp_bound = zlib.compressBound(json_len)
        # 使用compress方法压缩数据
        comp_data = zlib.compress(json.encode('utf-8'))
        return bytearray(comp_data)
```

接下来是获取一块0x100自定义加密数据:buf\_sf\_0x100。

```
# salt = 时间戳+一段0x28固定值
    def fun_sf(self, salt):
        salt = bytearray(salt, "utf-8")
        # 使用列表推导式创建一个从0到255的整数列表
        int_list = [i for i in range(256)]
        # 将整数列表转换为 bytearray
        ret_arr = bytearray(int_list)  # X0

        var2 = 0  # W11

        salt_len = len(salt)  # W10
        for i in range(0x100):
            # print(f"{i:02x}")
            salt_chunk = int(i / salt_len)  # W13                       SDIV            W13, W10, W2
            ret_i = ret_arr[i]  # W12                                   LDRB            W12, [X0,X10]
            salt_chunk = i - salt_chunk * salt_len  # W13               MSUB            W13, W13, W2, W10
            salt_chunk = salt[salt_chunk]  # W13                        LDRB            W13, [X1,W13,UXTW]
            var2 = ret_i + var2  # W11                                  ADD             W11, W12, W11
            var2 = var2 + salt_chunk  # W11                             ADD             W11, W11, W13

            salt_chunk = var2 & 0xff  # X13                             AND             X13, X11, #0xFF
            ret_arr[i] = ret_arr[salt_chunk]  # W14                     LDRB            W14, [X0,X13]
            #                                                           W13   STRB            W14, [X0,X10]
            ret_arr[salt_chunk] = ret_i  # W12                          STRB            W12, [X0,X13]

        return ret_arr
```

然后将buf\_sf\_0x100和comp\_json进行处理获得新的：comp\_json。

```
# 寄存器格式为dword格式
 def tool_range0xff(self, var):
        return var & 0xff
 def fun_xor(self, buf_sf, comp_json):
        buf_sf.append(0)  # 扩容到0x102
        buf_sf.append(0)  # 扩容到0x102
        self.**gstools.tool_bytearray2str(buf_sf)
        comp_json_len = len(comp_json)
        i = 0
        # try:
        while True:
            comp_json_len -= 1  # SUBS            X10, X10, #1            ; X0=X0-1=--len
            buf_0x100 = self.**gstools.tool_range0xff(
                buf_sf[0x100])  # LDRB            W11, [X0,#0x100]        ; W11=X0[0x100]=buf[0x100]
            buf_0x101 = self.**gstools.tool_range0xff(
                buf_sf[0x101])  # LDRB            W12, [X0,#0x101]        ; W12=buf_0x101 =X0[0x101]=*(buf + 0x101);

            buf_0x100_i = self.**gstools.tool_range0xff(
                buf_0x100 + 1)  # ADD             W11, W11, #1            ; W11=W11+1=buf[0x100]+1

            buf_sf[0x100] = buf_0x100_i  # STRB            W11, [X0,#0x100]        ; X0[0x100]=W11

            buf_0x100_i = buf_0x100_i & 0xff  # AND             X11, X11, #0xFF       ...