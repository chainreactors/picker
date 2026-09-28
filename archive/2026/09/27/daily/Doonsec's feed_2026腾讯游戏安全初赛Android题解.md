---
title: 2026腾讯游戏安全初赛Android题解
url: https://mp.weixin.qq.com/s/241TU2CWLYsSIWAfN0CIGw
source: Doonsec's feed
date: 2026-09-27
fetch_date: 2026-09-28T07:54:14.204505
---

# 2026腾讯游戏安全初赛Android题解

# 2026腾讯游戏安全初赛Android题解

318
318

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在公众号小说中沉浸阅读

虽然没有进决赛但还是记录一下吧，比起去年UE做的已经很多了。

**1.dump libsec2026**

拿到题是一个godot引擎加godot-cpp扩展的游戏。

引擎版本是4.5.1（关系到后面对应哪一版源码，虽然每版改动应该也不大吧）
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K25TllLIMlgblomPIDbPe04ADFoen3KE1KetAoLKJVbKiaVuGLBOdBNs8DicF9scdlzdzrB1oGgOxYQsaQnm8CYMicYlOnfjk7BUA/640?wx_fmt=other&from=appmsg)![]()

assets目录下可以看到有.gdc脚本，应该有主要相关逻辑写在trigger.gdc\token.gdc等，但.gdc被加密，不能用GDRE工具直接解。

观察两个so文件：libgodot-android.so; libsec2026.so

libsec2026.so套了壳，用脚本dump一下：

```
function dump_so(libName) {
Java.perform(() => {
// // 1. 更可靠地获取模块信息
var libso = Process.getModuleByName(libName);
if (!libso) {
var modules = Process.enumerateModules();
console.log("[+] 已加载的 SO 文件列表 (" + modules.length + " 个):");
            modules.forEach(function(m, i) {
console.log("  [" + i + "] " + m.name + "  base=" + m.base + "  size=" + m.size + "  path=" + m.path);
            });
console.error("[!] 错误：未找到模块 libil2cpp.so");
return;
        }

// 2. 验证基地址和大小是否合理
console.log("[+] 模块基址: " + libso.base);
console.log("[+] 模块大小: " + libso.size);
if (libso.size <= 0 || libso.size > 0x10000000) { // 大小合理性检查，例如大于256MB则可疑
console.error("[!] 模块大小异常，可能获取失败");
return;
        }

// 3. 安全地设置内存权限并读取
try {
// 修改内存权限为可读
// var originProtection =
Memory.protect(libso.base, libso.size, 'r--');

// 关键改进：分块读取内存，避免不连续映射区域导致崩溃
var chunkSize = 0x1000; // 每次读取4KB
var totalSize = libso.size;
var file_path = "/sdcard/download/" + libso.name + "_" + libso.base + "_" + ptr(totalSize) + ".so";
var file_handle = new File(file_path, "wb");

if (file_handle) {
for (var offset = 0; offset < totalSize; offset += chunkSize) {
var bytesToRead = Math.min(chunkSize, totalSize - offset);
try {
// 读取内存块
var chunk = libso.base.add(offset).readByteArray(bytesToRead);
if (chunk !== null) {
                            file_handle.write(chunk);
                        } else {
console.warn("[!] 读取的内存块为空，跳过写入");
                        }
                    } catch (e) {
// 如果某一块读取失败，用0填充并继续
console.warn("[!] 偏移 0x" + offset.toString(16) + " 处读取失败，用0填充");
var zeroBuffer = new ArrayBuffer(bytesToRead);
                        file_handle.write(zeroBuffer);
                    }
                }
                file_handle.flush();
                file_handle.close();
console.log("[dump] 成功: " + file_path);
            }
        } catch (e) {
console.error("[!] dump_so 过程中发生异常: " + e.message);
        }
    });
}
console.log("[+] 脚本加载时间: " + new Date().toLocaleTimeString());

setTimeout( () => {
console.log("[+] 回调执行时间: " + new Date().toLocaleTimeString());
console.log("[+] 延迟后开始 dump...");
dump_so("libsec2026.so");

}, 10000); // 延迟500毫秒，可根据实际情况调整
```

从so文件的大小和字符串信息可以判断出 libgodot\_android.so是godot引擎库，libsec2026.so是godot-cpp扩展部分和native方法实现。

**2.找到 godot-key**

查找godot相关加解密，应该是要找一个32位的AES密钥，加密模式是CFB，发现教程说关键函数是core/io/file\_access\_pack.cpp。

相关教程都是用字符串定位这个构造函数去拿到script\_encryption\_key：
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K0gLt4Axic8XBETZE8Y1C7m81Xwu0Xw8C28fPNYpmBTDPpjnZzJDDwnQT2fiaRVY9k4Qe7QRd8gZls1quXE5nqscLRISgl4heMk0/640?wx_fmt=other&from=appmsg)![]()

但是，出题人肯定不能出这么简单，已经把这种字符串信息抹去了。

但是，本人虽笨却非常的勤快，决定尝试照着源码硬推，这种字符串没有，总有别的字符串，（且秉持着恩师的源码在一起的函数和文件，汇编也会在附近。

一番搜索下定位到了pck\_packer.cpp：
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K19RG9iaGf0OlORIrYTVJLIe94kRkZkibxFN6OnxibKTekFNHuMeHKqCU13W7Doygax50T7GCmpib1IqK8xqG7iaWIscibFDjAHa9SxU/640?wx_fmt=other&from=appmsg)![]()

file\_access\_pack.cpp是解包部分逻辑，而pck\_packer.cpp是打包部分逻辑，二者一定会有关联：二者都跟FileAccessEncrypted::open\_and\_parse有关，这就缩小查找范围了，可以直接把pck\_packer的地址和源码给ai让它去帮我们找这个构造函数了。

后面发现还有一些办法：

1.用魔术头“GDPC”定位try\_and\_open函数

2.用“res://”的交叉引用定位排查等等（不太推荐，很多地方引用

总之在ai强大的能力和努力下，成功地获得一系列相关函数地址：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K15ZocOWibTupPWYCN6lwSXPNibl4tBlxmqSklqwZCBibxVBTNaRTFFKIKHpJfricfjNlEKrLC5icXL0XhCGxkVgSTlcIr8bBzsEZRg/640?wx_fmt=other&from=appmsg)![]()

也自然可以直接定位到我们要的key，这里出题人非常非常善良啊，key不是动态生成的，直接就给了：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/Cpo2XCpI7K0wUm7kDCsIgEhr2upu7RNnfZiaOVos38plnjRzpH2nACBbpCX1whSMUhkydibCzPWdyQmKsYDW25FMajocrogwZyo8WJhmA5DIA/640?wx_fmt=other&from=appmsg)

![]()

**3.拿到gd脚本**

但是把key输入GDRE还是解密失败了，于是就再次利用ai分析加解密流程，肯定是中间有地方魔改了：
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1rFQMvQ8gvL8aCHqCFJSibhTv6VXwhgosJCsTRmc9gdGeyWouOMAqsaE8icddJSibRHfr2Mic1ltnOicKsD7mxlRIPLAM1rozhrdN0/640?wx_fmt=other&from=appmsg)![]()

于是再让ai搓了一个解密脚本：

```
#!/usr/bin/env python3
"""Godot 4.x 单文件解密 (修改版 AES-256-CFB)"""

import struct, sys, hashlib
from Crypto.Cipher import AES

KEY = bytes.fromhex("ce4df8753b59a5a39ade58ac07ef947a3da39f2af75e3284d51217c04d49a061")

def decrypt_modified_cfb(key: bytes, iv: bytes, ciphertext: bytes) -> bytes:
"""修改版 CFB: plain[i] = keystream[pos] ^ (cipher[i] ^ pos), pos = i % 16"""
    aes = AES.new(key, AES.MODE_ECB)
    iv_block = bytearray(iv)
    plaintext = bytearray(len(ciphertext))
pos = 0
for i in range(len(ciphertext)):
if pos == 0:
            keystream = bytearray(aes.encrypt(bytes(iv_block)))
        c = ciphertext[i]
        modified = c ^ pos
        plaintext[i] = keystream[pos] ^ modified
        iv_block[pos] = modified
pos = (pos + 1) & 0xF
return bytes(plaintext)

def decrypt_file(data: bytes, key: bytes) -> bytes:
"""解密 FileAccessEncrypted 格式: [16B md5][8B length][16B iv][ciphertext]"""
    md5_exp = data[:16]
length = struct.unpack_from('<Q', data, 16)[0]
    iv = data[24:40]
    ds = length + (16 - length % 16) if length % 16 else length
    plain = decrypt_modified_cfb(key, iv, data[40:40 + ds])[:length]
if hashlib.md5(plain).digest() != md5_exp:
        raise ValueError("MD5 校验失败 — 密钥错误或数据损坏")
return plain
```

解密后的.gdc文件头就正常了，放进GDRE工具里就可以反编译了。

flag生成逻辑就是先异或一下然后传进native层加密：
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K1FKl4pUgCFnMmwjeuZibcUzeK8dws0g9jMRJUo4X4nicGicntIZUyQ6CN71pJAqKlk3Mbh6jds6w63FhIpXR1Y0v4WiatqFMibmSFo/640?wx_fmt=other&from=appmsg)![]()

##

**4.重打包游戏**

但拿到flag这一步，其实根本不需要去看native层加密逻辑。

这里有了godotscript脚本，虽然因为有cpp扩展的缘故不能直接放回引擎直接运行修改，但可以修改gd脚本重打包，而且我只是修改，连parsepck索引文件都不用重新生成，只用把trigger.gd改一下再用GDRE编译一下.gdc再套刚那套魔改AES加密回去就行了！

这里其实还想了一种更难的方法，如果能找到godot引擎load -> call 一个gd函数的调用链，然后找到对应地址可以构造出一个任意gd代码注入执行器？太复杂了没尝试。

回到trigger.gd，真的非常好改啊，连文件大小都不用变啊，只用把两个碰撞判断的对象调换一下，1改成2，这样碰到黄色方块就是拿到flag，碰到绿色才是示例flag~
改完重打包签名，得到“开挂版”：

下载链接：重打包apk

![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2NmeS0h9F9YyicM9zSrjbb6YZ6xNgUug53X8ZSbSxWUicTUiazyhdshAju8rpzOMTNBfutFicGsia4cIE0YEiat3EMDq343KicswC4dM/640?wx_fmt=other&from=appmsg)

![]()

**5.找加密函数地址**

接下来就是在libsec2026.so里找加密函数了。

从字符信息里已经知道godot-cpp扩展部分也在这个so里，所以再次对应源码分析函数。

之前研究过unity，感觉godot挺像，就是gd脚本去调cpp肯定是有个调用链的，比如有一个表存了所有函数地址，然后通过一个接口找到对应地址巴拉巴拉。

所以就是要hook这个调用链去拿到函数地址，然后就能看加密逻辑了。

大概就是classdb是一个关键的类，最关键的注册方法的函数是classdb\_register\_extension\_class\_method（ClassDB::bind\_method\_godot会调用）

定位godot.cpp简单，然后根据godot.cpp里有引用ClassDB::deinitialize，推到classdb的范围再从函数特征定位到ClassDB::bind\_method\_godot，再让ai分析这个函数：
![](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K2EbLa39QtKdnrhP5urdvn7nnn5XBUESbOhbcq7z9DaUWSKGz6YD8odgsFGEicGqtnUm747xKzoZa1icmibweRstictzxH2pe1EzIc/640?wx_fmt=other&from=appmsg)![]()

就拿到了classdb\_register\_extension\_class\_method的偏移，然后就可以hook这个函数拿到调用的加密函数的地址减去base基址获得加密函数的偏移：

我这里hook都写一起了，最后再放完整版吧，这个版本也是几次拿到回显然后让ai调整后的：

```
const CLASSDB_REG_METHOD_GLOBAL = 0xEDD10;

// GDExtensionClassMethodInfo 结构体布局 (ARM64):
//   +0x00  name              (StringName*)
//   +0x08  method_userdata   (MethodBind*)
//   +0x10  call_func         (bind_call)
//   +0x18  ptrcall_func      (bind_ptrcall)
//   +0x20  method_flags      (u32)
//   +0x24  has_return_value   (u8)
//   +0x28  return_value_info  (ptr)
//   +0x30  return_value_metadata (i32)
//   +0x34  argument_count    (u32)

function readPtrAt(addr) {
var lo = addr.readU32() >>> 0;
var hi = addr.add(4).readU32() >>> 0;
return ptr("0x" + hi.toString(16) + ("00000000" + lo.toString(16)).slice(-8));
}

function off(p) {
return "0x" + p.sub(base).toString(16);
}

var base;

function hookRegistration() {
var globalAddr = base.add(CLASSDB_REG_ME...