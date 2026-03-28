---
title: 手游逆向全流程复盘：从 IL2CPP Dump 到 TCP 握手协议还原
url: https://mp.weixin.qq.com/s/tgcuPXdNB431uZE0xht8Qw
source: Doonsec's feed
date: 2026-03-27
fetch_date: 2026-03-28T04:15:25.978993
---

# 手游逆向全流程复盘：从 IL2CPP Dump 到 TCP 握手协议还原

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0n9gpDkibbiaS7icz4rtWB9BDibeYbYJR4WOySMn8uiagbebR6icRVHfBq8DXkIEdZYtRq5opSfkwliaTS92MZguicY6DicCUkKpiaDZk1k/0?wx_fmt=jpeg)

# 手游逆向全流程复盘：从 IL2CPP Dump 到 TCP 握手协议还原

梧桐生
梧桐生

看雪学苑

![]()

在小说阅读器中沉浸阅读

# 本文记录了对某款基于 Unity 引擎（IL2CPP 编译）手游的完整逆向分析过程，涵盖运行时 Dump、网络协议识别、加密逻辑还原、握手流程分析，以及隐藏在脚本引擎中的业务逻辑挖掘。

#

文章以过程复盘为主，保留了实际分析中的弯路与回溯，力求真实还原研究思路。目标游戏已脱敏处理。

**分析环境：**

* 设备：Android 物理机
* 抓包：SunnyNet抓包工具
* 主要工具：frida-il2cpp-bridge、CyberChef、Python（pycryptodome）

**0x01 初步抓包与流量特征识别**

启动游戏后第一步是被动观察流量，用 SunnyNet 抓取全量网络数据，确认游戏是否走 TCP。启动后很快能看到若干条 TCP 长连接建立，选取其中持续有数据交互的连接，结合游戏内操作（日常任务或者日常关卡等）观察流量是否随操作变化——数据量明显跟随操作波动，确认这条 TCP 连接就是游戏主逻辑信道。

看原始字节流，能很快发现一个规律：每个数据包前固定以`45 67`开头，结尾固定是`89 AB`，中间内容随操作变化且不可读。Magic 头尾明确，说明是自定义二进制协议，中间部分大概率经过加密或压缩处理。把这两个特征记下来，后续在代码里定位包结构时会直接用到。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K26twHOcsufaicbcVRrZo2VT578QY5D5uhgGfPibsqgcGRvgDV5zf4zpd53usXy1P5mrRWUX068RhVTAjBWgFIgy91DMm1fBEbRQ/640?wx_fmt=other&from=appmsg)

##

**0x02 APK 检查与 Dump 方案选择**

把 APK 解包后，第一步检查`global-metadata.dat`的文件头。标准未加固的 IL2CPP metadata 文件头是固定的 magic（`AF 1B B1 FA`），但这里头部字节不符，判断 metadata 要么被加密，要么做了自定义结构处理。走常规 Il2CppDumper 静态分析这条路行不通。

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2ETULSmMEMCenscsRsG1kSgog1UWRZp0Ra9fa9kZZK0SKib3AjKtbB95r3Tj5dRBgf2wPSPPDhwSB3K0ATLtJGFwykbw5icND6Q/640?wx_fmt=other&from=appmsg)![]()

转换思路，改用运行时 dump。注入 frida-il2cpp-bridge，等 IL2CPP runtime 在内存中完成自解密并初始化后，由脚本直接从内存里 dump 出`dump.cs`。注入时机很关键，太早 runtime 还没完成初始化，太晚可能触发反调试，需要根据游戏启动流程适当调整 attach 时机。最终成功拿到 cs 文件。

**0x03 从 dump.cs 定位数据包结构**

拿到`dump.cs`之后，回过头来用抓包看到的特征做索引。直接搜`4567`和`89AB`没有结果——想到这类常量在 C# 里可能以十进制保存，换算后搜对应十进制值，找到了：

```
// MoleMole.PacketDefine
constint HEAD_MAGIC = 17767;  // 0x4567
constint TAIL_MAGIC = 35243;  // 0x89AB
```

定位到`MoleMole`命名空间下，顺藤摸瓜翻相关类，重点关注两个工具类：`MoleMole.AesUtils`和`MoleMole.Crc32Utils`。

**0x04 动态验证加密位置**

## 写 Frida 脚本分别 hook 两个工具类的方法，打印调用日志，结合抓包时间线对比：

* `Crc32Utils`

  相关方法始终没有调用记录，排除 CRC 完整性校验的可能。
* `AesUtils`

  的加密/解密方法有稳定调用，且调用时机与抓包数据发出时间吻合。

交叉比对 hook 日志里的明文输入和抓包的密文输出，确认数据包中间的不可读部分确实是 AES 加密的结果。

```
import "frida-il2cpp-bridge";

Il2Cpp.perform(() => {

const Assembly = Il2Cpp.domain.assembly("Assembly-CSharp");

const AESUtils = Assembly.image.class('MoleMole.AESUtils');
const Encrpt = AESUtils.method('Encrpt');
const Decrpt = AESUtils.method('Decrpt');
// static System.Byte[] Decrpt(System.Byte[] encrypted, System.Byte[] key);
Decrpt.implementation = function (encrypted, key) {

console.log("=== AESUtils.Decrpt Hooked ===");

// 打印参数
const encBytes = arrayToBytes(encrypted);
const keyBytes = arrayToBytes(key);
console.log("Decrypting:", bytesToHex(encBytes));
console.log("Key:", bytesToHex(keyBytes));

// 调用原始函数
const result = Decrpt.invoke(encrypted, key);

// 打印结果
console.log("Decrypted:", bytesToHex(arrayToBytes(result)));
console.log("==============================");
return result
  };

Encrpt.implementation = function (encrypted, key) {

console.log("=== AESUtils.Encrpt Hooked ===");

// 打印参数
const encBytes = arrayToBytes(encrypted);
const keyBytes = arrayToBytes(key);
console.log("Encrypting:", bytesToHex(encBytes));
console.log("Key:", bytesToHex(keyBytes));

// 调用原始函数
const result = Encrpt.invoke(encrypted, key);

// 打印结果
console.log("Encrypted:", bytesToHex(arrayToBytes(result)));
console.log("==============================");
return result
  };
});
```

---

##

**0x05 IV 与 Key 分析**

### IV

重启游戏，多次打印`AesUtils`加密调用时类内的 IV 字段——每次启动值相同，确认 IV 是静态固定的。这里有两种验证手段：一是直接 hook`AesUtils`的方法打印类字段，二是下沉到 native 层 hook AES 初始化点（如`AES_init_ctx_iv`或 mbedtls 对应接口），两种方式拿到的值一致。

### Key

重启游戏后发现 key 每次不同，且没有明显规律，不像是简单的时间戳或随机种子生成。打印调用栈，发现收包和发包走的 key 不同，最终在`MoleMole.TcpAsyncClient`里找到两个字段：

```
MoleMole.TcpAsyncClient
    System.Byte[] session_read_key_;   // offset 0xa8
    System.Byte[] session_write_key_;  // offset 0xb0
```

读写 key 分离，说明是握手后协商的 session key。key 的来源悬而未决，需要从握手流程里继续找。

```
import "frida-il2cpp-bridge";

Il2Cpp.perform(() => {
const AesTransform = Il2Cpp.domain.assembly("System.Core").image.class("System.Security.Cryptography.AesTransform");
// Hook the constructor to capture key and IV
const ctor = AesTransform.method(".ctor");
  ctor.implementation = function (algo, encryption, key, iv) {
console.log("==============================");
console.log("[AesTransform Constructor]");
console.log("Encryption mode: " + encryption);
// Key and IV are Il2Cpp.Array<byte>
if (key) {
const keyBytes = new Uint8Array(key.handle.readByteArray(key.length));
console.log("Key (hex): " + bytesToHex(arrayToBytes(key)));
console.log("Key length: " + key.length);
    }
if (iv) {
const ivBytes = new Uint8Array(iv.handle.readByteArray(iv.length));
console.log("IV (hex): " + bytesToHex(arrayToBytes(iv)));
console.log("IV length: " + iv.length);
    }
console.log("==============================");
return this.method('.ctor').invoke(algo, encryption, key, iv);
  };
});
```

---

##

**0x06 组包结构还原**

从调用栈继续往上追，`AesUtils.Encrypt`的调用方是`MoleMole.NetPacket.SerializeSec`。这个函数内部大量通过`System.IO.MemoryStream`做字节拼接，但调用都是通过计算偏移间接发起的（IL2CPP 的 vtable 调用方式），没有直接可读的符号。

通过hook跳转点并减去libil2cpp地址可以得到函数地址来确定具体调用的函数。

整体逻辑是生成4567，然后拿到调用`MoleMole.NetPacket`的`k__BackingField`字段做cmdid，接下来调用`MoleMole.NetPacket`的`Head`的`CalculateSize`函数确定part1的长度并转成字节，然后通过调用`MoleMole.NetPacket`的`Body`的`get_Length`函数确定part2的长度并转成字节，接着拼接`Head`和`Body`后调用`MoleMole.AESUtils`的`Encrpt`加密，再生成89ab后将前面所有的内容都用`System.IO.MemoryStream`的`Write`拼接到一起。

```
// Assembly-CSharp
class MoleMole.NetPacket : System.Object, System.IDisposable
{
    System.UInt16 <cmdId>k__BackingField; // 0x10
    Baseproto.PacketHead Head; // 0x18
    System.IO.MemoryStream Body; // 0x20
```

```
__int64 __fastcall sub_2CDB4C0(__int64 a1, __int64 *a2, __int64 *a3){
  __int64 v6; // x0
  __int64 result; // x0
  __int64 v8; // x22
  __int64 v9; // x23
unsignedint v10; // w24
  __int64 v11; // x22
  __int64 v12; // x23
unsignedint v13; // w24
unsignedint v14; // w0
  __int64 v15; // x22
unsignedint v16; // w24
  __int64 v17; // x23
unsignedint v18; // w24
  __int64 v19; // x22
unsignedint v20; // w0
  __int64 v21; // x22
unsignedint v22; // w24
  __int64 v23; // x23
unsignedint v24; // w24
  __int64 v25; // x22
  __int64 v26; // x21
  __int64 v27; // x0
  __int64 v28; // x20
  __int64 v29; // x21
  __int64 v30; // x0
  __int64 v31; // x21
  __int64 v32; // x19
  __int64 v33; // x20
unsignedint v34; // w21

if ( (byte_A5674D1 & 1) == 0 )
  {
sub_292804C(69884);
    byte_A5674D1 = 1;
  }
if ( (IsPatched_3702264(2967, 0) & 1) != 0 )
  {
    v6 = sub_37021C4(2967, 0);
if ( !v6 )
sub_2954148();
return sub_2A1F5DC(v6, a1, a2, a3, 0);
  }
else
  {
    result = *a2;
if ( *a2 )
    {
if ( *(a1 + 0x20) )
      {
        (*(*result + 760LL))(result, 0, *(*result + 768LL));
if ( !*a2 )
sub_2954148();
        (*(**a2 + 504LL))(*a2, 0, *(**a2 + 512LL));
        v8 = *a2;
if ( (*(qword_A43BEB8 + 295) & 2) != 0 && !*(qword_A43BEB8 + 216) )
il2cpp_runtime_class_init_0(qword_A43BEB8);
        v9 = GetBytesNetworkdThread(0x4567u);
if ( (*(qword_A426770 + 295) & 2) != 0 && !*(qword_A426770 + 216) )
il2cpp_runtime_class_init_0(qword_A426770);
        v10 = sub_45C78DC(0x4567, System_Int32);
if ( !v8 )
sub_2954148();
        (*(*v8 + 808LL))(v8, v9, 0, v10, *(*v8 + 816LL));
        v11 = *a2;
        v12 = GetBytesNetworkdThread(*(a1 + 0x10));
        v13 = sub_45C78DC(*(a1 + 0x10), System_Int32);
if ( !v11 )
sub_2954148();
        (*(*v11 + 808LL))(v11, v12, 0, v13, *(*v11 + 816LL));
if ( !*(a1 + 0x18) )
sub_2954148();
        v14 = CalculateSize(*(a1 + 0x18));
        v15 = *a2;
        v16 = v14;
        v17 = GetBytesNetworkdThread(v14);
        v18 = sub_45C78DC(v16, System_Int32);
if ( !v15 )
sub_2954148();
        (*(*v15 + 808LL))(v15, v17, 0, v18, *(*v15 + 816LL));
        v19 = *(a1 + 0x20);
if ( !v19 )
sub_2954148();
        v20 = (*(*v19 + 0x1D8LL))(*(a1 + 0x20), *(*v19 + 0x1E0LL));
        v21 = *a2;
        v22 = v20;
        v23 = GetBytesNetworkdThread_0(v20);
        v24 = sub_45C79C0(v22, qword_A4A6F50);
i...