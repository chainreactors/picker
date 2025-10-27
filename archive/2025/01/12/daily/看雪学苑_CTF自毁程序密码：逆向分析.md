---
title: CTF自毁程序密码：逆向分析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458588573&idx=1&sn=c40b84e0094dfcbca49818f166d4c1f8&chksm=b18c251786fbac0172b4c573bca3dbdc17e0efad3bf6e5dace210a9b96023fdf89feccf64ba1&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-12
fetch_date: 2025-10-06T20:09:11.465807
---

# CTF自毁程序密码：逆向分析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Evr07bQdfia9LpR5iaEy5kq9xr9nicF0LpEGA7ITAwqdspxYzHvkbyISMicMNTRgKmF1sgTvydyRicFPw/0?wx_fmt=jpeg)

# CTF自毁程序密码：逆向分析

西贝巴巴

看雪学苑

```
一

背景
```

##

这一题很有迷惑性，看似简单的代码逻辑，一眼看到的答案，其实并不是真相，重点在他的反检测。大多数的时候我们通过静态分析（java层还是so层）找到他的加密算法，再逆向还原其算法就能找到最终的答案，但是这道题不是，接下来我们我们会用到**frida、AndroidNativeEmu、unidbg、IDA动静态调试**。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Evr07bQdfia9LpR5iaEy5kq99nl4ELmZxZHzzuWSuZWvibXEbVlgE2RQhzGIYVPF0riaF9wEMILIjNqQ/640?wx_fmt=other&from=appmsg)

```
二

静态分析
```

#### java层分析

从代码可以看出，输入的密码调用方法securityCheck(String str)，满足true则成功。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Evr07bQdfia9LpR5iaEy5kq9WE65hHxr67EXHWN6ZUYMhPy11TkWWibdLpBMMuqNP8T6q7p2icTQjnWg/640?wx_fmt=other&from=appmsg)

####

#### so层静态分析

找到Java\_com\_yaotong\_crackme\_MainActivity\_securityCheck函数

1.初始化检查
byte\_6359 和 byte\_635A: 可能是静态变量，表示某些初始化是否已经完成。
sub\_2494 和 sub\_24F4: 两个子函数，分别在第一次执行时被调用，可能用于解密或初始化全局变量。
结果: 如果两个字节标志未设置，会调用这两个函数并设置标志位，确保只初始化一次。

2.获取 Java 字符串的 UTF-8 值 v5 = (\*a1)->GetStringUTFChars(a1, a3, 0);

3.字符串比较
比较 Java 层传入的字符串 a3 是否与硬编码字符串 off\_628C 匹配。如果匹配，返回 1，否则返回 0。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Evr07bQdfia9LpR5iaEy5kq9SVJVKCW3bzjbUyicXiaE7ibawiaPLXbSP74UOt7OPq9nibiafK5fZxYuH66w/640?wx_fmt=other&from=appmsg)

分析结果：v6 = off\_628C; 就是我们需要的值，aWojiushidaan

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Evr07bQdfia9LpR5iaEy5kq9Kf5yqy4uc16icZa8qMxaotrgOTfKlbVNkwuBCuy7VgB11t7h1DMkjvA/640?wx_fmt=other&from=appmsg)

但是我们输入该值到APP中提示是不正确的，那么由此可以猜测，必然是APP启动后，有程序修改了off\_628C的值。

```
三

AndroidNativeEmu模拟调用
```

##

验证下aWojiushidaan在静态下模拟调用，是否可以安全调用。

```
import logging
import sys
from unicorn import UC_HOOK_CODE, UC_HOOK_MEM_READ, UC_HOOK_MEM_WRITE
from unicorn.arm_const import *
from androidemu.emulator import Emulator

# Configure logging
logging.basicConfig(
    stream=sys.stdout,
    level=logging.DEBUG,
    format="%(asctime)s %(levelname)7s %(name)34s | %(message)s"
)

logger = logging.getLogger(__name__)

# Initialize emulator 实例化虚拟机
emulator = Emulator(vfp_inst_set=True)

# 加载Libc库
emulator.load_library("../example_binaries/32/libc.so", do_init=False)

# 加载要模拟的库
lib_module = emulator.load_library("libcrackme.so", do_init=False)

# 定义内存回调函数以监控变量 0x12A0 的变化
target_address = 0x4450+0xa009b000
string_length =100  # 假设最大字符串长度为 32 字节
# Show loaded modules 打印已经加载的模块
logger.info("Loaded modules:")
for module in emulator.modules:
    logger.info("[0x%x] %s" % (module.base, module.filename))

def memory_read_hook(uc, access, address, size, value, user_data):
    if address == target_address:
        # 获取当前值
        # print(uc.mem_read(address, string_length).decode('ascii', errors='ignore'))
        current_value = uc.mem_read(address, string_length).split(b'\0', 1)[0].decode('ascii', errors='ignore')
        print(f"【READ】 Address: 0x{address:X}, Current Value: {current_value}")

def memory_write_hook(uc, access, address, size, value, user_data):
    if address == target_address:
        # 获取写入的新值
        new_value = uc.mem_read(address, string_length).split(b'\0', 1)[0].decode('ascii', errors='ignore')
        print(f"【WRITE】 Address: 0x{address:X}, New Value: {new_value}")

# 注册指令和内存访问钩子
emulator.uc.hook_add(
    UC_HOOK_MEM_READ,  # 捕获内存读取
    memory_read_hook,
    None,
    target_address,
    target_address + string_length
)
emulator.uc.hook_add(
    UC_HOOK_MEM_WRITE,  # 捕获内存写入
    memory_write_hook,
    None,
    target_address,
    target_address + string_length
)

# 模拟运行函数
result1 = emulator.call_symbol(
    lib_module,
    'Java_com_yaotong_crackme_MainActivity_securityCheck',
    emulator.java_vm.jni_env.address_ptr,
    0,
    "wojiushidaan",//123
    is_return_jobject=False
)

# 输出结果
print("jnicheck result : {}".format(result1))
```

当我们分别输入 123 和 wojiushidaan 看返回的结果

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Evr07bQdfia9LpR5iaEy5kq96XZd0B8W4pOnpRuiahmJUCjqZpps3LSHMtN2NGQPnGuxyNyeoNJmiatw/640?wx_fmt=other&from=appmsg)

结论：我们可以很确定v6 = off\_628C值就是我们输入的值。

```
四

解法（1）frida hook该函数
```

###

在不考虑风控的前提下，明确了目标值用frida hook，是最快的方式，那就来吧，验证下。

```
function hook_so() {
    Java.perform(function(){
        var addr = Module.findBaseAddress("libcrackme.so");
        var v1 = addr.add(0x4450);
        console.log(v1.readCString());

    });
}
function main() {
     hook_so()
}

setTimeout(main,4000)
```

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Evr07bQdfia9LpR5iaEy5kq9M4shCt25lkozP5sibiaPFib35pwZsLECydCVqJhzVZJLpp7jsbDsHPOqg/640?wx_fmt=other&from=appmsg)

得到值 : aiyou,bucuoo 输入该值验证成功

```
五

解法（2）unidbg 模拟执行，打印关键参数
```

##

```
package com.yaotong.crackme;

import com.github.unidbg.AndroidEmulator;
import com.github.unidbg.Module;
import com.github.unidbg.arm.backend.DynarmicFactory;
import com.github.unidbg.linux.android.AndroidEmulatorBuilder;
import com.github.unidbg.linux.android.AndroidResolver;
import com.github.unidbg.linux.android.dvm.AbstractJni;
import com.github.unidbg.linux.android.dvm.DalvikModule;
import com.github.unidbg.linux.android.dvm.DvmObject;
import com.github.unidbg.linux.android.dvm.VM;
import com.github.unidbg.memory.Memory;
import com.github.unidbg.pointer.UnidbgPointer;

import java.nio.charset.Charset;
import java.io.File;

public class MainActivity extends AbstractJni {
    private final AndroidEmulator emulator;
    private final VM vm;
    private final Module module;
    private final Memory memory;

    MainActivity() {
        // 创建模拟器
        emulator = AndroidEmulatorBuilder.for32Bit().addBackendFactory(new DynarmicFactory(true)).build();
        // 内存
        memory = emulator.getMemory();
        // 设置SDK
        memory.setLibraryResolver(new AndroidResolver(23));
        // 创建虚拟机
        vm = emulator.createDalvikVM(new File("unidbg-android/src/test/java/com/yaotong/crackme/you.apk"));
        //设置jni
        vm.setJni(this);
        //打印日志
        vm.setVerbose(true);
        // 运行so文件
        DalvikModule dalvikModule = vm.loadLibrary(new File("unidbg-android/src/test/java/com/yaotong/crackme/libcrackme.so"), true);
        //module
        module = dalvikModule.getModule();
        // 调用JNI——onload
//        dalvikModule.callJNI_OnLoad(emulator);
        vm.callJNI_OnLoad(emulator, module);
        HookAddr();

    }

    /**
     * 打印 Hex Dump 格式的数据
     *
     * @param data 要打印的字节数组
     */
    private static void printHexDump(byte[] data) {
        int bytesPerLine = 16; // 每行打印16个字节

        for (int i = 0; i < data.length; i += bytesPerLine) {
            // 打印当前行的地址（偏移量）
            System.out.printf("%08X  ", i);
            // 打印当前行的十六进制数据
            for (int j = 0; j < bytesPerLine; j++) {
                if (i + j < data.length) {
                    System.out.printf("%02X ", data[i + j]);
                } else {
                    System.out.print("   "); // 如果剩余字节不足16个，填充空格
                }
            }
            System.out.print("  |");
            // 打印当前行的字符内容（ASCII）
            for (int j = 0; j < bytesPerLine; j++) {
                if (i + j < data.length) {
                    byte b = data[i + j];
                    if (b >= 32 && b <= 126) {
                        System.out.print((char) b); // 打印可打印字符
                    } else {
                        System.out.print("."); // 打印不可打印字符
                    }
                } else {
                    System.out.print(" "); // 填充空格
                }
            }
            System.out.println("|");
        }
    }

    public static void main(String[] args) {
        MainActivity test = new MainActivity();
        System.out.println(test.getSName());
    }

    public void HookAddr() {
        // 目标地址，这里是示例地址 0x628C 0x4450
        long targetAddress = module.base + 0x4450;

        // 使用 UnidbgPointer 来获取目标地址的数据
        UnidbgPointer pointer = UnidbgPointer.pointer(emulator, targetAddress);

        // 读取目标地址的数据，假设它是一个字符串，长度为 16 字节
        byte[] data = pointer.getByteArray(0, 16); // 读取16个字节
        printHexDump(data);
        // 将读取的...