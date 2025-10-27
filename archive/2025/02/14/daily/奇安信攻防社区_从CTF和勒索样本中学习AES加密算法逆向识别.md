---
title: 从CTF和勒索样本中学习AES加密算法逆向识别
url: https://forum.butian.net/share/4136
source: 奇安信攻防社区
date: 2025-02-14
fetch_date: 2025-10-06T20:33:45.802685
---

# 从CTF和勒索样本中学习AES加密算法逆向识别

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 从CTF和勒索样本中学习AES加密算法逆向识别

* [CTF](https://forum.butian.net/topic/52)

如何IDA静态识别AES，帮助工作中有个快速定位算法的方法

AES(Advanced Encryption Standard)又称为Rijndael加密法，AES的出现是为了取代DES，因为DES分组相对较小，最终Rijndael算法获选AES。
它满足如下条件：
1、分组大小为128的分组密码。
2、支持三种密码标准：128位、192位和256位。
3、软硬件实现高效。
对于不同的密钥长度，加密方式类似，只是128位循环10次，192位循环12次，256位循环14次。其中明文长度必须事16的倍数，如果不是16的倍数需要对明文数据进行填充后进行加密。这里的位数表示密钥可选的位数，密钥大小和明文数据大小必须是32的倍数。但是运算时被加密的数据块只能被切割成4\\*4=16字节的矩阵。
填充模式有以下几种：
NONE、PKC37、ZERO、ANSI923、IOS7816\\_4、IOS10126
AES中用到了一个S盒（S-BOX），是由加密者提供给被加密数据的一个替换表，用于SubBytes操作中，将每个字节根据码表替换。
AES加密描述
=======
整个加密过程的语言描述
```php
明文数据填充
根据密钥进行拓展密钥算法计算轮密钥
初始轮（1）
AddRoundKey 第一轮将State（明文矩阵）与第一轮的轮密钥进行异或
中间轮（2~9）
SubBytes：将数据块中的数据，映射到 Rijndael S-box，主要为了消除特征
ShiftRows：将数据块按“行”移位，以达到混淆的目的
MixColumns：将数据块按“列”与一个由多项式构成的 matrix，做矩阵乘法。目的是将单个错误扩散到整体，从而达到雪崩效应的预 期，使其更难被破解
AddRoundKey：将本轮的 轮密钥与数据块进行异或
最终轮（10）
SubBytes
ShiftRows
AddRoundKey
```
图解完整加密流程
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-affc348daeb80b8d8d5b974e379f1e20bc5782bb.png)
使用的轮数和扩展密钥 EK 的大小取决于所提供原始密钥的大小。下表显示了原始密钥长度、循环次数和扩展密钥长度之间的相关性：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-3cc6fb119597af46bf08e8aaeafa0389391db88f.png)
State(状态矩阵)
===========
在分组密码中经常会提到State的概念，其本质就是我们上述的分组明文数据，把明文数据分成多个4\\*4的数据块。第一个字节将位于第一列第一行，第二个字节将位于第一列第二行。如下图所示， P 表示明文数组， Px 表示明文数组索引 x 处的字节：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-191df0e34cc8025bc6fd7fc17c4018fedb28c40d.png)
key Expansion(密钥拓展)
===================
AES 的扩展密钥是一个由原始密钥派生的四字节字组成的列表。数组中的第一个字与原始密钥相同。例如，密钥数组中的前四个字节就是扩展密钥中的第一个字 EK ，如下所示：
```python
key = [0x00, 0x11, 0x22, 0x33, 0x44, 0x55, 0x66, 0x77, 0x88, 0x99, 0xaa, 0xbb, 0xcc, 0xdd, 0xee, 0xff]
expanded\_key = [0x00112233,
0x44556677,
0x8899aabb,
0xccddeeff,
...]
```
每个附加字都是前一个字与索引 i - NK 处的字进行 XOR 的结果，其中 i 是当前索引， NK 是原始密码密钥字的数量(一个字占4字节，4字/128位、6字/192位 或 8字/256位，取决于密钥的位数）。当当前索引是 NK 的倍数时，前一个字会在进行 XOR 之前被转换。这包括将字向左旋转一个（即 0xAABBCCDD 变为 0xBBCCDDAA ），然后将每个字节替换为 AES 的替换盒（S-Box）--一个 256 字节数组--中的一个值。然后，新的四字节字与 "循环常数" RCON 进行 XOR。舍入常数 RCON 可以通过算法计算得出（该数学公式不做过深讨论）：。对于标准 AES-128 算法，还可以使用以下值对轮常量进行硬编码：
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-e0390c0ae0988ab44cd33fc9aa7a02fdd4dbf76b.png)
整个 AES-128 密钥扩展算法看起来就像下面的 Python 代码：
```php
# Round Constants
# 定义的轮常量用于编码拓展密钥，标准AES-128可以将下列值转换为字单位数据与拓展密钥转换的字数据进行异或
RCON = [None, 0x01, 0x02, 0x04, 0x08, 0x10, 0x20, 0x40, 0x80, 0x1B, 0x36]
# 该函数用于将输入的数据流转换成多个字数组，用于后续与轮常量进行异或
# AES中，该输入为拓展密钥（EK），将拓展密钥从字节流转换成字数组形式并于S-Box进行替换
def subword(self, word):
"""AES SubWord Method.
Args:
word (list): Word to transform
Returns:
int: Transformed word
"""
bs = struct.pack('&gt;I', word)
nw = []
for b in bs:
nw.append(self.s\_box[b])
nw = struct.unpack('&gt;I', bytes(nw))[0]
return nw
# 该函数用于
def rotword(self, word):
"""AES RotateWord Method.
Args:
word (list): Word to transform
Returns:
int: Transformed word
"""
bs = list(struct.pack('&gt;I', word))
bs.append(bs.pop(0))
nw = struct.unpack('&gt;I', bytes(bs))[0]
return nw
# 根据轮常量生成拓展密钥
def key\_expansion(self, key):
"""AES Key Expansion Algorithm.
Args:
key (bytes): Key to expand
Returns:
list: List of words for expanded key
"""
ek = []
i = 0
# 把原始密钥保存到拓展密钥开头，128位保存4个字，192保存6个字，256保存8个字，循环分别对应4、6、8
while i &lt; 4:
b = bytes(key[i\*4:(i\*4)+4])
w = struct.unpack('&gt;I', b)[0]
ek.append(w)
i += 1
# 根据密钥长度生成拓展密钥EK，如128生成44个字的拓展密钥数组，192生成72个字数组，256生成112个字数组
while i &lt; 44:
# 将上一个运算结果存储到tmp用于后续运算，因为前面的4轮所以进入该循环时i=4
tmp = ek[i-1]
# 这里nk = 4，因为AES-128原始密钥长度只能生成4个字。
if i % 4 == 0:
# 把轮常量转换成字数组，用于与拓展密钥数据进行异或。不足的地方补0
rcon\_val = struct.unpack('&gt;I',
bytes([self.RCON[i//4], 0, 0, 0]))[0]
# 按照编码流程对拓展密钥进行编码运算
tmp = self.subword(self.rotword(tmp)) ^ rcon\_val
# 将tmp生成的值按照上面描述的运算方法进行异或生成最终的拓展密钥字
nw = tmp ^ ek[i-4]
ek.append(nw)
i += 1
return ek
```
AddRoundKey（轮密钥加）
=================
本质上就是将数据矩阵与密钥矩阵进行逐个字节异或。下图所示P为明文数据，K为密钥矩阵。将32倍数的明文分割成多个4\\*4=16字节的矩阵，用于轮密钥加运算。
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-483b93cc59a4376e8055892492f059e0e7702f94.png)
数据层面转换如下
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-139e2513a36725e8bbd9aa53430bfcc8d0e3a1f2.png)
AES 之所以保证安全的关键，是对每个数据块执行多轮加密，对于 128 bits 的密钥块，至少需要 6+128/32=10 轮。
这里除数 32 是由于 Rijndael 的数据块、密钥块大小必须是 32 的倍数，最小 128，最大 256，只是 AES 仅选择了其中的 128、192、256 三组作为密钥块大小，数据块则固定为 128。
进行轮密钥加就是对矩阵中每个元素一一对应进行异或
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-8adce6134dfd0106d688624282e0d5f6851a1e2b.png)
代码实现
```js
def add\_round\_key(s,k):
for i in range(4):
for j in range(4):
s\_box[i][j] ^= k[i][j]
```
SubByte(字节替换)
=============
在这里，引入一个S盒(S-box)，也就是一个替换表，如下。
按照数学逻辑的二维矩阵数学逻辑替换
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-419d2e39033c5f79192b81e8d31c5aade6985c21.png)
代码层面可以按照1维数组的逻辑图
![image.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2025/01/attach-02250359d926e4bdd7e8f8c3904c62c5ad46bec6.png)
加密的时候使用的是S-BOX，解密的时候也有一个与其对应的S-BOX表。AES给出的现成加解密S-BOX分别如下。s\\_box用于加密，s\\_box\\_inv用于解密。
```js
s\_box = [
[0x63, 0x7c, 0x77, 0x7b, 0xf2, 0x6b, 0x6f, 0xc5, 0x30, 0x01, 0x67, 0x2b, 0xfe, 0xd7, 0xab, 0x76],
[0xca, 0x82, 0xc9, 0x7d, 0xfa, 0x59, 0x47, 0xf0, 0xad, 0xd4, 0xa2, 0xaf, 0x9c, 0xa4, 0x72, 0xc0],
[0xb7, 0xfd, 0x93, 0x26, 0x36, 0x3f, 0xf7, 0xcc, 0x34, 0xa5, 0xe5, 0xf1, 0x71, 0xd8, 0x31, 0x15],
[0x04, 0xc7, 0x23, 0xc3, 0x18, 0x96, 0x05, 0x9a, 0x07, 0x12, 0x80, 0xe2, 0xeb, 0x27, 0xb2, 0x75],
[0x09, 0x83, 0x2c, 0x1a, 0x1b, 0x6e, 0x5a, 0xa0, 0x52, 0x3b, 0xd6, 0xb3, 0x29, 0xe3, 0x2f, 0x84],
[0x53, 0xd1, 0x00, 0xed, 0x20, 0xfc, 0xb1, 0x5b, 0x6a, 0xcb, 0xbe, 0x39, 0x4a, 0x4c, 0x58, 0xcf],
[0xd0, 0xef, 0xaa, 0xfb, 0x43, 0x4d, 0x33, 0x85, 0x45, 0xf9, 0x02, 0x7f, 0x50, 0x3c, 0x9f, 0xa8],
[0x51, 0xa3, 0x40, 0x8f, 0x92, 0x9d, 0x38, 0xf5, 0xbc, 0xb6, 0xda, 0x21, 0x10, 0xff, 0xf3, 0xd2],
[0xcd, 0x0c, 0x13, 0xec, 0x5f, 0x97, 0x44, 0x17, 0xc4, 0xa7, 0x7e, 0x3d, 0x64, 0x5d, 0x19, 0x73],
[0x60, 0x81, 0x4f, 0xdc, 0x22, 0x2a, 0x90, 0x88, 0x46, 0xee, 0xb8, 0x14, 0xde, 0x5e, 0x0b, 0xdb],
[0xe0, 0x32, 0x3a, 0x0a, 0x49, 0x06, 0x24, 0x5c, 0xc2, 0xd3, 0xac, 0x62, 0x91, 0x95, 0xe4, 0x79],
[0xe7, 0xc8, 0x37, 0x6d, 0x8d, 0xd5, 0x4e, 0xa9, 0x6c, 0x56, 0xf4, 0xea, 0x65, 0x7a, 0xae, 0x08],
[0xba, 0x78, 0x25, 0x2e, 0x1c, 0xa6, 0xb4, 0xc6, 0xe8, 0xdd, 0x74, 0x1f, 0x4b, 0xbd, 0x8b, 0x8a],
[0x70, 0x3e, 0xb5, 0x66, 0x48, 0x03, 0xf6, 0x0e, 0x61, 0x35, 0x57, 0xb9, 0x86, 0xc1, 0x1d, 0x9e],
[0xe1, 0xf8, 0x98, 0x11, 0x69, 0xd9, 0x8e, 0x94, 0x9b, 0x1e, 0x87, 0xe9, 0xce, 0x55, 0x28, 0xdf],
[0x8c, 0xa1, 0x89, 0x0d, 0xbf, 0xe6, 0x42, 0x68, 0x41, 0x99, 0x2d, 0x0f, 0xb0, 0x54, 0xbb, 0x16]
]
s\_box\_inv = [
[0x52, 0x09, 0x6a, 0xd5, 0x30, 0x36, 0xa5, 0x38, 0xbf, 0x40, 0xa3, 0x9e, 0x81, 0xf3, 0xd7, 0xfb],
[0x7c, 0xe3, 0x39, 0x82, 0x9b, 0x2f, 0xff, 0x87, 0x34, 0x8e, 0x43, 0x44, 0xc4, 0xde, 0xe9, 0xcb],
[0x54, 0x7b, 0x94, 0x32, 0xa6, 0xc2, 0x23, 0x3d, 0xee, 0x4c, 0x95, 0x0b, 0x42, 0xfa, 0xc3, 0x4e],
[0x08, 0x2e, 0xa1, 0x66, 0x28, 0xd9, 0x24, 0xb2, 0x76, 0x5b, 0xa2, 0x49, 0x6d, 0x8b, 0xd1, 0x25],
[0x72, 0xf8, 0xf6, 0x64, 0x86, 0x68, 0x98, 0x16, 0xd4, 0xa4, 0x5c, 0xcc, 0x5d, 0x65, 0xb6, 0x92],
[0x6c, 0x70, 0x48, 0x50, 0xfd, 0xed, 0xb9, 0xda, 0x5e, 0x15, 0x46, 0x57, 0xa7, 0x8d, 0x9d, 0x84],
[0x90, 0xd8, 0xab, 0x00, 0x8c, 0xbc, 0xd3, 0x0a, 0xf7, 0xe4, 0x58, 0x05, 0xb8, 0xb3, 0x45, 0x06],
[0xd0, 0x2...