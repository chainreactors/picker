---
title: ctfplus-逆向每周练习-easyApp、rand_py、BabyJar、ez_pyyy、Minesweeper
url: https://mp.weixin.qq.com/s/UHvCBEzAM0jcMX5dCHW4bA
source: Doonsec's feed
date: 2026-06-21
fetch_date: 2026-06-22T07:16:02.871342
---

# ctfplus-逆向每周练习-easyApp、rand_py、BabyJar、ez_pyyy、Minesweeper

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/6nhGiavBDP4ZxcXV9XQfHwicjY1WicSOnZkVWojqpsYh1KoK8mdzVF9nuU37OM2PWuMX7xhAGgoyCLLxC2fSLbWUGmfPzvicJEib2LMoLVrbRylI/0?wx_fmt=jpeg)

# ctfplus-逆向每周练习-easyApp、rand\_py、BabyJar、ez\_pyyy、Minesweeper

原创

李北辰
李北辰

SPEEDCoding

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4YzFoiaqN2DdwBTrxdpkWN4Rj5GUPVqkicO1rCFN8UjhLsq0c7v8sEq9R7FYjhWrq27UHWmcZVXQhes3X1I0fCVQfuX1yMMXJiaa8/640?wx_fmt=png&from=appmsg)

#

# 1.easyApp

是一个apk文件，拖入模拟器中运行需要输入flag进行判断，然后拖入jadx中静态分析MainActivity中的代码：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4YxVuQ297t5uaj2pSwWCVJsy9lWjsQOdiaSUHuga6fgaicmc43Jx4yxlmpzg08ezuUKuzcaDicXiaykFNGarJQCWlumbGLsAkMWg6U/640?wx_fmt=png&from=appmsg)

可以看到首先读取了dex.zip文件（在assets里面，导出后再用jadx加载即可），然后判断输入的flag是否长度是42，再截取前26位，进行base64编码，编码后需要等于：MHhHYW1le0RvX3kwdV9sMHYzX2FuZHIwMWQ=，把这个base64解码即可得到flag的前面部分：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4azsqD7ibzyyt59Okv9uallt6OHRPVKZA5LPSsiaFicSOqlejKLfQetz4zAgTzTuUssictVRB0icEmDXxVcV3kx08q61rag8oXAWZw4/640?wx_fmt=png&from=appmsg)

然后再读取输入字符串从第26个字符到末尾转换为字节数组，以hexstring的形式传入刚才动态加载的dex.zip中的Secret.Check方法中，接下来把dex.zip直接拖入jadx，查看Secret.Check方法：

```
package com.example.easyapp; import java.math.BigInteger; /* loaded from: dex.bin */public class Secret { public static boolean check(String str) { BigInteger bigInteger = new BigInteger(str.substring(0, 16), 16); BigInteger bigInteger2 = new BigInteger(str.substring(8, 24), 16); BigInteger bigInteger3 = new BigInteger(str.substring(16, 32), 16); return bigInteger2.add(bigInteger.multiply(new BigInteger(”3”))) .subtract(new BigInteger(”27454419028250566601”)) .equals(BigInteger.ZERO) &&  bigInteger3.multiply(new BigInteger(”2”)) .subtract(bigInteger2.multiply(new BigInteger(”5”))) .add(new BigInteger(”20616666104378640363”)) .equals(BigInteger.ZERO) &&  bigInteger.add(bigInteger3.multiply(new BigInteger(”4”))) .subtract(new BigInteger(”1dce62be9f0fa2f6c”, 16)) .equals(BigInteger.ZERO); }}
```

前面截取了26到42的字符串，一共16个字符串，转换成hexstring正好32个字节，这里第一个16字节数为0-16字节，第二个16字节数为8-24字节，第三个16字节数为16-32字节，然后需要满足下面的方程：

```
(big2+(big1*3))-27454419028250566601 = 0big3*2 - big2*5 + 20616666104378640363 = 0big1 + big3*4 - 0x1dce62be9f0fa2f6c = 0
```

使用python的sympy库求解并输出，脚本如下：

```
import sympy as spimport base64 big1, big2, big3 = sp.symbols('big1 big2 big3')eq1 = sp.Eq(big2 + 3*big1, 27454419028250566601)eq2 = sp.Eq(big3 * 2 - big2 * 5, -20616666104378640363)eq3 = sp.Eq(big1 + big3*4, 0x1dce62be9f0fa2f6c)solution = sp.solve((eq1, eq2, eq3), (big1, big2, big3))print(solution[big1])print(solution[big2])print(solution[big3]) big1 = solution[big1]big2 = solution[big2]big3 = solution[big3]str1_hex = hex(big1)str2_hex = hex(big2)str3_hex = hex(big3)print(str1_hex)print(str2_hex)print(str3_hex)str1 = base64.b16decode(str1_hex[2:].encode(), casefold=True)print(str1)str2 = base64.b16decode(str2_hex[2:].encode(), casefold=True)print(str2)str3 = base64.b16decode(str3_hex[2:].encode(), casefold=True)print(str3)
```

输出：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/6nhGiavBDP4YpdBHEyCaqIxIXbrricUIibzbicY57nA4jp7cvF4nGr0KtROiaJwFq0JtUibAQkzQKE7ZsSIZ6scWzIBk8KQFibEzscao5LiakrnJmBc/640?wx_fmt=png&from=appmsg)

跟前面的flag进行拼接即可（注意这里需要去掉交叉字符串）：0xGame{Do\_y0u\_l0v3\_andr01d\_4nd\_dex\_loader}

## 2.rand\_py

这是一个pyinstaller打包的exe程序，首先使用pyinstxtrator.py提取出pyc文件：

```
python pyinstxtractor.py D:\桌面\rand_py\rand_py.exe
```

然后找到提取出来的pyc文件：rand\_py.pyc，再使用pycdc.exe转换为python代码：

```
pycdc.exe rand_py.pyc > rand_py.py
```

成功提取出python代码：

```
 # Source Generated with Decompyle++# File: rand_py.pyc (Python 3.10) import randomenc_flag = [ 5554865, 8824328, 9324119, 2254831, 5757818, 2986985, 1878515, 9324119, 6857238, 5690625, 9073978, 3189766, 4267438, 9923116, 5042226, 4263793, 7510142, 3443924, 4569572, 5690625, 9923116, 4263793, 7510142, 3443924, 9923116, 5554865, 2464675, 6002055, 1327718, 4569572, 7510142, 5073474]user_input = input('Check your flag:')for i in range(len(user_input)): random.seed(ord(user_input[i])) num = random.randint(1000000, 9999999) if num != enc_flag[i]: print('WRONG!!!!!!') exit(1)print('YEAH,you are right!!!')
```

这里通过random.seed设置伪随机数种子，然后enc\_flag列表里面的每个数字都是根据flag对应下标位置字符串生成的伪随机数，直接写python脚本爆破即可：

```
import randomenc_flag = [ 5554865, 8824328, 9324119, 2254831, 5757818, 2986985, 1878515, 9324119, 6857238, 5690625, 9073978, 3189766, 4267438, 9923116, 5042226, 4263793, 7510142, 3443924, 4569572, 5690625, 9923116, 4263793, 7510142, 3443924, 9923116, 5554865, 2464675, 6002055, 1327718, 4569572, 7510142, 5073474]flag = ''for i in range(len(enc_flag)): for seed in range(0x20, 0x7f): random.seed(seed) num = random.randint(1000000, 9999999) if num == enc_flag[i]: flag += chr(seed) breakprint(flag)
```

输出得到flag：

```
PDSCTF{Simple_random_and_Python}
```

## 3.BabyJar

题目是一个jar包文件，使用jd-gui进行反编译查看java源码：

![](https://mmbiz.qpic.cn/mmbiz_png/6nhGiavBDP4ZOd1tzAWicm0F67YqM7aUtfOE0glOnq0T96QraeRIqlzNco4ibBNDQjBt1v8BrlribxUQ3z3b9FhqRsJcexdyIibyjicJ9O5sLZqAw/640?wx_fmt=png&from=appmsg)

先看BabyJar.class，首先实例化了一个Encrypt类e，然后定义了一个enc字符串，应该是base编码，然后获取到用户输入的flag，再对输入的flag调用e.encrypt方法得到返回值，返回值再跟enc字符串做比较。

```
package com.BabyJar.demo; import java.util.Scanner; public class BabyJar { public static void main(String[] args) { Encrypt e = new Encrypt(); Scanner input = new Scanner(System.in); String enc = ”QsY1V5cX9jJyF2JSAgdikwfCEneTAgICUpNnd1Iyk8IXUkJ3QhcyZ8J3YpY=”; System.out.println(”Please input your flag:”); String flag = input.nextLine(); String Encrypted_flag = e.encrypt(flag); if (Encrypted_flag.equals(enc)) { System.out.println(”Congratulations!!”); } else { System.out.println(”Try Again!!”); }  }}
```

然后看Encrypt类，先把输入的字符串转换为字节数组，然后每个字节先跟key异或得到temp，然后temp的高4位和低4位互相交换，得到加密后的字节数组，再进行base64编码得到刚才的enc字符串。

```
package com.BabyJar.demo; import java.util.Base64; public class Encrypt { int key = 20;
 public String encrypt(String text) { byte[] originalBytes = text.getBytes(); byte[] encryptedBytes = new byte[originalBytes.length]; for (int i = 0; i < originalBytes.length; i++) { byte c = originalBytes[i]; byte temp = (byte)(c ^ this.key); encryptedBytes[i] = (byte)((temp & 0xF0) >> 4 | (temp & 0xF) << 4); }  return Base64.getEncoder().encodeToString(encryptedBytes); }}
```

只需要把enc字符串使用base64解码，然后再对每个字节重新交换高四位和低四位，然后跟20异或，即可解密，python解密脚本如下：

```
import base64 enc = ”QsY1V5cX9jJyF2JSAgdikwfCEneTAgICUpNnd1Iyk8IXUkJ3QhcyZ8J3YpY=”enc_bytes = base64.b64decode(enc)enc_byte_array = bytearray(enc_bytes)key = 20flag = b''for i in range(len(enc_byte_array)): temp = ((enc_byte_array[i] & 0xf0) >> 4) | ((enc_byte_array[i] & 0x0f) << 4) temp = temp ^ key flag += bytes([temp])print(flag)
```

运行后成功得到输出：

```
b'0xGame{73e214d2-d85c-4441-bc17-8e10c0e7b8c2}'
```

## 4.ez\_pyyy

题目给的是一个pyc文件，直接pycdc转换为py源码：

```
pycdc.exe ____python_______.pyc > result.py
```

得到的python源码为：

```
 # Source Generated with Decompyle++# File: ____python_______.pyc (Python 3.8) cipher = [ 48, 55, 57, 50, 53, 55, 53, 50, 52, 50, 48, 55, 101, 52, 53, 50, 52, 50, 52, 50, 48, 55, 53, 55, 55, 55, 50, 54, 53, 55, 54, 55, 55, 55, 53, 54, 98, 55, 97, 54, 50, 53, 56, 52, 50, 52, 99, 54, 50, 50, 52, 50, 50, 54] def str_to_hex_bytes(s = None): return s.encode('utf-8')  def enc(data = None, key = None): return None((lambda .0 = None: [ b ^ key for b in .0 ])(data))  def en3(b = None): return b << 4 & 240 | b >> 4 & 15  def en33(data = None, n = None): '''整体 bitstream 循环左移 n 位''' bit_len = len(data) * 8 n = n % bit_len val = int.from_bytes(data, 'big') val = (val << n | val >> bit_len - n) & (1 << bit_len) - 1 return val.to_bytes(len(data), 'big') if __name__ == '__main__': flag = '' data = str_to_hex_bytes(flag) data = enc(data, 17) data = bytes((lambda .0: [ en3(b) for b in .0 ])(data)) data = data[::-1] data = en33(data, 32) if data.hex() == cipher: print('Correct! ') else: print('Wrong！！！！！！！！')
```

这段代码先把flag以utf8编码成字节数组，然后再调用enc函数进行第一次加密，针对每个字节跟key进行异或，得到的结果再每个字节调用en3函数，对每个字节低4位和高4位互换位置，然后再倒序排序字节数组，再调用en33函数最后加密得到cipher，参考题目的python源码写解密脚本：

```
import ...