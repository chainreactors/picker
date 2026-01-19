---
title: CISCN 2018 - SM 密码学题目深度技术解析
url: https://mp.weixin.qq.com/s/LjU3OWXhOfZY3lMxnjDSnQ
source: Doonsec's feed
date: 2026-01-18
fetch_date: 2026-01-19T03:42:43.991763
---

# CISCN 2018 - SM 密码学题目深度技术解析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/xs4jYLrrdZO2ocnQUypep3x5EGc6qrjyYxdWMg9NngsicUpW2QNTbvF9P7tqwHGJA9L7OUfPMftViapxYibFKEScw/0?wx_fmt=jpeg)

# CISCN 2018 - SM 密码学题目深度技术解析

原创

破镜安全
破镜安全

破镜安全

![]()

在小说阅读器中沉浸阅读

# CISCN 2018 - SM 密码学题目深度技术解析

## 前言

本文将深入分析CISCN 2018中的一道密码学题目SM。这道题目巧妙地结合了异或运算、线性代数和AES加密，展示了线性密码系统的数学特性。通过本文的分析，读者将学习到如何将密码学问题转化为数学问题，并通过算法求解。

## 题目环境

题目提供了以下文件：

* sm.py：加密脚本源代码
* ps：包含512个大整数的文件
* r：一个大整数
* ef：Base64编码的加密数据

我们的目标是通过分析加密逻辑，从已知数据中恢复密钥，最终解密得到flag。

## 第一步：分析加密脚本

首先，我们需要仔细阅读sm.py的源代码，理解整个加密流程。

### 1.1 加密脚本的主函数分析

加密脚本的核心是run()函数，让我们逐行分析：

```
def run():
    choose=getPrime(512)
    ps=gen512num()
    print "gen over"
    bchoose=bin(choose)[2:]
    r=0
    bchoose = "0"*(512-len(bchoose))+bchoose
    for i in range(512):
        if bchoose[i]=='1':
            r=r^ps[i]
    flag=open("flag","r").read()

    key=long_to_bytes(int(hashlib.md5(long_to_bytes(choose)).hexdigest(),16))
    aes_obj = AES.new(key, AES.MODE_ECB)
    ef=aes_obj.encrypt(flag).encode("base64")

    open("r", "w").write(str(r))
    open("ef","w").write(ef)
    gg=""
    for p in ps:
        gg+=str(p)+"\n"
    open("ps","w").write(gg)
```

从代码中可以看出加密流程：

1. 生成一个512位的素数choose作为密钥
2. 调用gen512num()生成512个特殊构造的数字，存入ps数组
3. 将choose转换为512位的二进制字符串bchoose
4. 根据bchoose的每一位，如果是'1'，就将对应的ps[i]异或到r中
5. 使用choose的MD5哈希值作为AES密钥，加密flag
6. 将r、ef（加密后的flag）、ps数组写入文件

### 1.2 核心加密逻辑分析

加密的核心在于这段代码：

```
for i in range(512):
    if bchoose[i]=='1':
        r=r^ps[i]
```

这段代码的含义是：

* 遍历choose的512个二进制位
* 如果第i位是1，就将ps[i]异或到r中
* 最终得到的r是若干个ps[i]的异或结果

用数学表达式表示：

```
r = ps[i₁] ⊕ ps[i₂] ⊕ ... ⊕ ps[iₖ]
```

其中i₁, i₂, ..., iₖ是bchoose中值为1的位置。

这个加密方案的关键问题是：**已知ps数组和r，能否反推出choose？**

### 1.3 gen512num函数深度分析

gen512num函数是理解本题的关键，让我们仔细分析：

```
def gen512num():
    order=[]
    while len(order)!=512:
        tmp=randint(1,512)
        if tmp not in order:
            order.append(tmp)
    ps=[]
    for i in range(512):
        p=getPrime(512-order[i]+10)
        pre=bin(p)[2:][0:(512-order[i])]+"1"
        ps.append(int(pre+"0"*(512-len(pre)),2))
    return ps
```

这个函数的执行过程：

**第一步：生成随机排列**

```
order=[]
while len(order)!=512:
    tmp=randint(1,512)
    if tmp not in order:
        order.append(tmp)
```

生成一个包含1到512的随机排列，每个数字出现且仅出现一次。

**第二步：构造特殊数字**

```
for i in range(512):
    p=getPrime(512-order[i]+10)
    pre=bin(p)[2:][0:(512-order[i])]+"1"
    ps.append(int(pre+"0"*(512-len(pre)),2))
```

对于每个ps[i]，构造过程如下：

1. 生成一个素数p
2. 取p的二进制表示的前(512-order[i])位
3. 在后面添加一个"1"
4. 再在后面填充0，使总长度达到512位

**关键发现：每个ps[i]的二进制结构**

让我们用一个具体例子来理解。假设order[0]=5，那么ps[0]的二进制结构是：

```
位置: 511 510 ... 6  5  4  3  2  1  0
值:   x   x  ... x  1  0  0  0  0  0
```

从右往左数（从最低位开始），第5位是1，第0到第4位都是0。

这意味着：**每个ps[i]都有一个唯一的"最低有效1位"位置，这个位置就是order[i]**。

这个特殊构造是解题的关键！

## 第二步：数学建模与问题转化

### 2.1 异或运算的数学性质

在深入分析之前，我们需要理解异或运算的基本性质：

1. **交换律**：a ⊕ b = b ⊕ a
2. **结合律**：(a ⊕ b) ⊕ c = a ⊕ (b ⊕ c)
3. **自反性**：a ⊕ a = 0
4. **恒等性**：a ⊕ 0 = a
5. **按位独立**：异或运算在每一位上独立进行

第5点非常重要：这意味着我们可以将一个512位的异或问题分解为512个独立的1位问题。

### 2.2 问题的数学表达

设choose的二进制表示为c = (c₀, c₁, c₂, ..., c₅₁₁)，其中cᵢ ∈ {0, 1}

设ps[i]的二进制表示为pᵢ = (pᵢ,₀, pᵢ,₁, ..., pᵢ,₅₁₁)

那么r的第j位可以表示为：

```
rⱼ = c₀·p₀,ⱼ ⊕ c₁·p₁,ⱼ ⊕ ... ⊕ c₅₁₁·p₅₁₁,ⱼ
```

在GF(2)（二元有限域）上，这等价于：

```
rⱼ = Σ(cᵢ × pᵢ,ⱼ) mod 2
```

这实际上是一个线性方程组！我们有512个方程（对应r的512位），512个未知数（对应choose的512位）。

但是，一般的线性方程组可能无解或有多解。这道题为什么可解呢？关键就在于gen512num函数的特殊构造。

### 2.3 下三角矩阵结构的发现

回忆gen512num的构造：每个ps[i]的最低有效1位位置是唯一的。

如果我们按照最低有效1位的位置对ps数组重新排序，会发生什么？

假设我们将ps数组按照最低有效1位的位置从小到大排序，得到新的数组P。那么：

* P[0]的最低有效1位在第0位，第0位是1，第0位之前（右边）没有位
* P[1]的最低有效1位在第1位，第1位是1，第0位是0
* P[2]的最低有效1位在第2位，第2位是1，第0-1位都是0
* ...
* P[i]的最低有效1位在第i位，第i位是1，第0到i-1位都是0

这形成了一个下三角矩阵结构！用矩阵表示：

```
        位0  位1  位2  ...  位i  ...
P[0]:   1    ?    ?   ...   ?   ...
P[1]:   0    1    ?   ...   ?   ...
P[2]:   0    0    1   ...   ?   ...
...
P[i]:   0    0    0   ...   1   ...
```

这个矩阵的对角线全是1，对角线下方全是0，这就是下三角矩阵的特征。

## 第三步：推导解题算法

### 3.1 为什么下三角矩阵可以逐位求解

对于下三角矩阵，我们可以使用前向替换法（Forward Substitution）求解。

考虑第i位的方程：

```
rᵢ = C[0]·P[0][i] ⊕ C[1]·P[1][i] ⊕ ... ⊕ C[511]·P[511][i]
```

由于下三角矩阵的性质：

* 当j > i时，P[j][i] = 0（因为P[j]的第0到j-1位都是0）
* 当j = i时，P[i][i] = 1（这是标志位）
* 当j < i时，P[j][i]可能是0或1

因此方程可以简化为：

```
rᵢ = C[0]·P[0][i] ⊕ ... ⊕ C[i-1]·P[i-1][i] ⊕ C[i]·1
```

移项得到：

```
C[i] = rᵢ ⊕ (C[0]·P[0][i] ⊕ ... ⊕ C[i-1]·P[i-1][i])
```

这就是递推公式！当我们求解第i位时，第0到i-1位已经求解完毕，可以直接代入计算。

### 3.2 算法步骤总结

基于以上分析，我们的解题算法如下：

**步骤1**：读取ps数组，将每个数字转换为二进制并反转（让最低位在前）

**步骤2**：找到每个ps[i]的最低有效1位位置，按此位置排序

**步骤3**：读取r值，同样转换为二进制并反转

**步骤4**：从第0位开始，逐位求解choose的每一位

**步骤5**：将排序后的结果恢复到原始顺序

**步骤6**：构建完整的choose值，用于解密flag

## 第四步：实现解密脚本

### 4.1 数据预处理函数

首先定义一个辅助函数，用于将大整数转换为二进制并反转：

```
def tobinrev(str_num):
    """将数字字符串转换为二进制并反转"""
    return bin(int(str_num))[2:][::-1]
```

这个函数的作用：

* 将字符串形式的大整数转换为整数
* 转换为二进制字符串（去掉'0b'前缀）
* 反转字符串，使最低位在最前面

### 4.2 读取并排序ps数组

```
dic = {}
dic_value = [0 for i in range(512)]

with open("ps", "r") as f:
    lines = f.readlines()
    for i in range(512):
        line = lines[i].strip()
        bin_rev = tobinrev(line)
        index = bin_rev.find('1')
        dic[index] = i
        dic_value[index] = bin_rev
```

这段代码的作用：

* `dic`字典：存储"最低有效1位位置"到"原始索引"的映射
* `dic_value`数组：按位置排序后的二进制字符串
* `bin_rev.find('1')`：找到第一个1的位置，即最低有效1位
* 通过这种方式，我们实现了按最低有效1位位置的排序

### 4.3 处理r值

```
r = open("r", "r").read().strip()
r_rev = tobinrev(r)
```

将r值读取并转换为反转的二进制字符串，便于后续逐位处理。

### 4.4 核心算法：逐位求解choose

```
tmp_result = [0 for i in range(512)]
for i in range(512):
    tmp = 0
    for j in range(i):
        tmp ^= (int(dic_value[j][i]) * tmp_result[j])
    tmp_result[i] = int(r_rev[i]) ^ tmp
```

这段代码实现了前向替换算法：

**外层循环**：遍历第0到511位

**内层循环**：计算已知部分的贡献

* `dic_value[j][i]`：排序后第j个数字的第i位
* `tmp_result[j]`：已经求解出的choose的第j位
* 两者相乘再异或，累积到tmp中

**求解当前位**：`tmp_result[i] = int(r_rev[i]) ^ tmp`

* r的第i位异或掉已知部分的贡献，得到choose的第i位

### 4.5 恢复原始顺序

```
ans = [0 for i in range(512)]
for i in range(512):
    ans[dic[i]] = tmp_result[i]
```

将排序后的结果映射回原始ps数组的顺序。

### 4.6 构建choose值

```
choose = ""
for i in ans:
    choose += str(i)
choose = int(choose, 2)
```

将512个二进制位拼接成字符串，然后转换为整数。

### 4.7 解密flag

```
import base64
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import hashlib

flag_encrypted = open("ef", "r").read().strip()
key = long_to_bytes(int(hashlib.md5(long_to_bytes(choose)).hexdigest(), 16))
aes_obj = AES.new(key, AES.MODE_ECB)
ef = aes_obj.decrypt(base64.b64decode(flag_encrypted))
print("Flag:", ef.decode())
```

解密步骤：

1. 读取Base64编码的加密flag
2. 计算choose的MD5哈希值，转换为16字节的AES密钥
3. 使用AES ECB模式解密
4. 输出解密后的flag

### 4.8 完整解密脚本

将以上所有步骤整合，得到完整的解密脚本：

```
from Crypto.Cipher import AES
from Crypto.Util.number import long_to_bytes
import hashlib
import base64

def tobinrev(str_num):
    return bin(int(str_num))[2:][::-1]

# 步骤1: 读取并排序ps数组
dic = {}
dic_value = [0 for i in range(512)]

with open("ps", "r") as f:
    lines = f.readlines()
    for i in range(512):
        line = lines[i].strip()
        bin_rev = tobinrev(line)
        index = bin_rev.find('1')
        dic[index] = i
        dic_value[index] = bin_rev

# 步骤2: 处理r值
r = open("r", "r").read().strip()
r_rev = tobinrev(r)

# 步骤3: 逐位求解choose
tmp_result = [0 for i in range(512)]
for i in range(512):
    tmp = 0
    for j in range(i):
        tmp ^= (int(dic_value[j][i]) * tmp_result[j])
    tmp_result[i] = int(r_rev[i]) ^ tmp

# 步骤4: 恢复原始顺序
ans = [0 for i in range(512)]
for i in range(512):
    ans[dic[i]] = tmp_result[i]

# 步骤5: 构建choose值
choose = ""
for i in ans:
    choose += str(i)
choose = int(choose, 2)

# 步骤6: 解密flag
flag_encrypted = open("ef", "r").read().strip()
key = long_to_bytes(int(hashlib.md5(long_to_bytes(choose)).hexdigest(), 16))
aes_obj = AES.new(key, AES.MODE_ECB)
ef = aes_obj.decrypt(base64.b64decode(flag_encrypted))
print("Flag:", ef.decode())
```

## 第五步：运行验证

运行解密脚本后，成功获得结果：

```
Flag: flag{shemir_alotof_in_wctf_fun!}
```

恢复的choose值为：

```
0xd9acf82cc8d757b5b11b851079a6b65f7d04d6ba592cb24381f4cf7c11e58404ba1fdbda4424067facabb7ca3a00ae57c8ecf613a79be6974628cbc97ae68e71
```

这是一个512位的大整数，正是加密时使用的密钥。

## ...