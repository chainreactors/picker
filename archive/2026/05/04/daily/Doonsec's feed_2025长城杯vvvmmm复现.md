---
title: 2025长城杯vvvmmm复现
url: https://mp.weixin.qq.com/s/I5r5mA3bFGSq-fh9WLHPQA
source: Doonsec's feed
date: 2026-05-04
fetch_date: 2026-05-05T04:59:51.879871
---

# 2025长城杯vvvmmm复现

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/g673ce4c7rmxGUTjqW9rOibYZ4GaAmSm3cYhp4yQRVBib2SvscvInKlLYwogflzPlzLCnB95Y6JAGuGyTzEptuzPYaXwefQyLNy4NgWnt9YS4/0?wx_fmt=jpeg)

# 2025长城杯vvvmmm复现

studying-egg
studying-egg

正在思考ing

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## 参考链接

https://www.cnblogs.com/x0rrrrr/p/19439591

## 前言

今天是五四青年节，这里祝奋斗在网络安全一线的兄弟们节日快乐！

VMP一直是让我头疼的考点😭，想起来长城杯初赛有一道VMP，这里简单复现一下。

## 复现

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmSPsYYesTCxGyQr1nTSUFicXrnFfS0FpPRYjibXw62XebQHp1NGSX9qrbjKuXEGibtnYNwjPCo7XXgaczOFEuS37bavqrtz1lTI0/640?wx_fmt=png&from=appmsg)

在字符串列表中看到`UC`和`qemu`，结合题目的名字可以推断出这道题考察的是`unicorn`的虚拟机

**什么是unicorn**

qemu是模拟不同处理器架构的虚拟机，unicorn是qemu框架下只用于模拟CPU执行的模块

这里做一个符号恢复

在Ubuntu中编译好的unicorn放入`IDA`最终进行分析，并保存，然后用`bindiff`导入`vvvmmm`中进行匹配

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmWtibm0bLuaUk01peicopc4f293zhGdr8ESicb8OuMysXJCc4ahJlU4fWBtH1ia8OaoCribtMC6u5RYhSf9hIKdKu2swpTCvBIkpkk/640?wx_fmt=png&from=appmsg)

应用这些匹配结果

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rmGvZHYQo4uKywm60cvmgFDgFfND8lTat5sJxWzACG9tlkmhXeHmyFiaiaRrVyKXg1jIVvKY2uiaibPanibaOFib1b7wxEOywSj06lRg/640?wx_fmt=png&from=appmsg)

unicorn程序中的一些API：

`uc_mem_map`:在unicorn中分配一段内存空间

`uc_mem_write`:在分配的内存空间中写入内容

`uc_reg_write`:给代码传入参数

`uc_emu_start`:运行程序

unicorn程序运行的逻辑一般为：分配空间 -> 写入字节码 -> 将参数写入寄存器 -> 运行程序

所以我们可以推断出`sub_407DD0`为`uc_reg_write`，`sub_4099D0`为`uc_emu_start`

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rkJONgrTXaUdB5XDsk1iaMVplpg1S2fL0artfMBSIXw4DDRXh6hm6Nn2CrEU2bPx8RFhFrNA28eskSsQhKDBVd99ZLqq6hG25iaE/640?wx_fmt=png&from=appmsg)

同时我们可以推断出第一个`uc_mem_write`写入的是字节码，后面两个`un_mem_write`写入的是传入程序的参数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rnhqe1AUo2oiaTibsPicHiaTznia1VWZk4c1OU3d29sPhADIH1Y5Hv4MQeUDJNwp6SFbFbpSBaIOW4JNKnsajr1utabuufsHl8lT8rM/640?wx_fmt=png&from=appmsg)

根据字符串可以得出这个模拟的是`riscv`架构 通过IDA python脚本将字节码dump出来

```
import ida_bytes
start_ea = 0x64C3F0
size =  662
output_file = r"C:\Users\lenovo\Desktop\test\code.bin"
data = ida_bytes.get_bytes(start_ea, size)
if data:
    with open(output_file, "wb") as f:
        f.write(data)
    print(f"[+] Success: Dumped {len(data)} bytes from {hex(start_ea)} to {output_file}")
else:
    print("[-] Error: Failed to get bytes. Check address.")
```

得到的二进制文件放入IDA中，选择`Risc-V`架构，可以得到程序逻辑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rlUpHT0uk3PPNyCqqmGNjCrHsNzd9fwDVMpkX6zibnLj3XTPpJp6BNzYpYEhHTzPaj3iby9TRhga5D3OxlxRyXKAXicuDedIdgXIc/640?wx_fmt=png&from=appmsg)![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rl3gxtDmk6YfMBDxiaDrviaedriaRAJYfOtyfqicurx2bs4iayPmlBuJibuv46EicUkI8q6553G2JDHgOahMsuUr9fkmdAPO9HqVxo9Xo/640?wx_fmt=png&from=appmsg)

通过分析程序可以得到逻辑：密钥→哈希→PRNG 流→XOR 解密→与期望值比对

传入的两个参数，一个是输入值，另外一个是密钥

之前提到的两个参数，其中`byte_64C6C0`指向密钥

![](https://mmbiz.qpic.cn/sz_mmbiz_png/g673ce4c7rmsiaYtJS9uQup7r8ibPSNRlunjuicyFnlEkBQBHkGklghzuRricd2V5U3fTW5PwXe03mOgiaSYUkm4jo3EMSSBaHEeX5dj3Y7fq5iaI/640?wx_fmt=png&from=appmsg)

最终的返回值会保存在`rdi`中

![](https://mmbiz.qpic.cn/mmbiz_png/g673ce4c7rlI7aHCcnckU8yjnDjEzDkFtvyEH7uW7eiatQ2fbqetsQuzxaNc7ictCodtkhEIhFpyAwINO37rFNNxGMFwf9nOOyUuNUExguO9c/640?wx_fmt=png&from=appmsg)

**为什么我不直接追踪 uc\_reg\_write 传入的参数**

通过跟踪发现传入的值是虚拟内存中的地址，无法找到具体密钥（可能是我方法不对）

根据上述内容，最终可以生成解密脚本

```
import struct

KEY = "e4Y8YRXVzg2HRrCUy35CM0Txq91HzMGZ"

MOD = 0x13579BDF

MASK64 = (1 << 64) - 1

EXPECTED = [

    0x45034F63, 0x534762D2, 0x44B36D04, 0x44C3ED6A,

    0x79BB60B0, 0x42A1E767, 0x3EDB7E6C, 0x30E1551D,

    0x4D3ABAA4, 0x6AA29948, 0x51CE8847, 0x51623FAF,

]

def key_hash(key: str) -> tuple[int, int]:

    """Hash key string in 64-bit arithmetic. Returns (v5, v4)."""

    v4 = 1

    for ch in key:

        v4 = ((v4 * 31) + ord(ch)) & MASK64

    return (v4 >> 16) & 0xFFFFFFFF, v4 & 0xFFFFFFFF

def generate_stream(v5: int, v4: int) -> list[int]:

    """Generate 12 PRNG 32-bit words."""

    stream = []

    for _ in range(6):

        v8 = v5 % MOD

        v9 = v4 % MOD

        v5 = pow(v8, 13, MOD)

        v4 = pow(v9, 13, MOD)

        stream.append(v5)

        stream.append(v4)

    return stream

def decrypt(key: str) -> bytes:

    """Recover original input by XORing expected values with PRNG stream."""

    v5, v4 = key_hash(key)

    stream = generate_stream(v5, v4)

    data = b""

    for i in range(12):

        word = EXPECTED[i] ^ stream[i]

        data += struct.pack("<I", word)

    return data

if __name__ == "__main__":

    result = decrypt(KEY)

    print(f"Found: flag{{{result.decode('ascii')}}}")

# flag{fANUES0XtUXBDEbOXs4xFcXDb3Q5kMU87bZLMZJfuRnCvfwX}
```

## 结语

复现过程中我遇到最大的难题是符号恢复（之前一直没用过bindiff😢）。这里非常感谢W0w1F师傅的指导💐

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/sz_mmbiz_png/UKpIYGnLasKiaktndBsK1icZCdPnhD70PLW8D6ENptOZOHNIAIibQMqKTqqlcBxISjgOkp9Z28up1Puv1aXxObxeA/0?wx_fmt=png)

正在思考ing

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

![作者头像](http://mmbiz.qpic.cn/sz_mmbiz_png/UKpIYGnLasKiaktndBsK1icZCdPnhD70PLW8D6ENptOZOHNIAIibQMqKTqqlcBxISjgOkp9Z28up1Puv1aXxObxeA/0?wx_fmt=png)

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