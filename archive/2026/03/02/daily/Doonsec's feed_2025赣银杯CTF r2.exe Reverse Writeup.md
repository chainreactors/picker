---
title: 2025赣银杯CTF r2.exe Reverse Writeup
url: https://mp.weixin.qq.com/s/EndYBXYsUyHOPVhokWHMQw
source: Doonsec's feed
date: 2026-03-02
fetch_date: 2026-03-03T04:07:46.229380
---

# 2025赣银杯CTF r2.exe Reverse Writeup

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/FT3A8r9icDymanyBBhJABXWfEgb1hic6XHoo6e5pVP9Qc2UKibRoOJ5xzycbHNnLKACGlo6zTFdf0LS4Y6VNeIyQsJeQ9BZsuZ5bXNFuMjsehw/0?wx_fmt=jpeg)

# 2025赣银杯CTF r2.exe Reverse Writeup

ListSec

![]()

在小说阅读器中沉浸阅读

# 2025 赣银杯 CTF: r2.exe Reverse Writeup

## 一、 题目基本信息

* • **文件名**: `r2.exe`
* • **文件格式**: x64 可执行程序 (Windows PE 格式)
* • **保护机制**: 存在较为明显的 OLLVM (Obfuscator-LLVM) 控制流平坦化混淆。

## 二、 逆向分析过程

### 1. 入口与字符串初步定位

通过查壳工具查看程序无额外压缩壳，或者直接拖入 IDA Pro 9.0 中进行分析。 在 `Strings` 选项卡中检索通常的 CTF 关键字符，例如 “flag”,“wrong”,“correct” 等。如果检索不到明显线索，可以找一些诸如 “flag!” 的可疑格式化字符串。

利用 IDA 的交叉引用 (Xrefs) 找到了核心校验函数 `main` 函数，地址位于 `0x1400020e0`。

### 2. OLLVM 混淆与常量还原

查看 `main` 的反汇编和伪代码发现，代码被拆分成了诸多利用状态机 `switch-case` 跳转的代码块（控制流平坦化）。在这个被拉伸的伪代码中，存在大量的状态流转与字节数组操作：

* • 通过分析某一个分支处的常量拼接逻辑（或运行时 dump），能够找到硬编码的目标密文数组：前 6 个字节实际上是用数字的转码形式，与后续拼凑出的字节常量一起构成了一个 32 字节长的验证数组：

```
cipher_bytes = [92, 48, 135, 133, 200, 107, 126, 102, 179, 245, 80, 205, 181, 96, 6, 202, 94, 87, 102, 157, 187, 52, 50, 64, 235, 213, 130, 241, 244, 219, 13, 243]
```

* • 从上文变量初始化中发现了长度为 `DWORD[4]` 的密钥：

  ```
  key = [15000, 89894, 17, 223123]
  ```

### 3. 用户输入与核心加密算法识别

在平坦化的块里藏着对用户的输入读取，通常为带安全隐蔽性的 `scanf`，程序吸取了长 32 的用户字符串流转给接下来的核心算法 `sub_140001250`。

双击研究 `sub_140001250`，伪代码中包含以下明显的位运算特征：

```
z >> 5 ^ y << 2
y >> 3 ^ z << 4
sum ^ y
key[(p & 3) ^ e] ^ z
......
```

这是典型的 **XXTEA** (微型加密算法) 的加密运算。进一步观察到外层循环次数（通过 DELTA 处理的轮数计算），确认为：

* • **加密轮数**: `12` 轮
* • **加密 Delta**: `0x33445566` (XXTEA 非标常见固定常量，一般标准为 0x9E3779B9)

程序将 32 字节（划分为 8 个 `DWORD` 四字节块）的用户明文通过 `XXTEA` 算法加密后，拿结果和之前还原的目标 `cipher_bytes` 进行逐字节的比较判断，如果全部一致则会导向输出成功（或者直接对齐组装并显示输出 `right flag`）。

## 三、 解题思路与解密脚体

基于上述分析，我们只需要将获得的 `XXTEA` 算法逻辑反转（解密操作），以常量 `cipher_bytes` （密文表）作为输入，利用同样的 `key`、`Delta` 及 `rounds` 进行逆向还原即可。

这里使用 Python 编写解密脚本：

```
import struct

defdecrypt(cipher_bytes, key, rounds=12, delta=0x33445566):
# 将密文字节数组转换为长度为 8 的 32位无符号整数数组
    v = list(struct.unpack("<IIIIIIII", bytes(cipher_bytes)))
    n = len(v)

# 获取加密时的最终 sum (加解密对称)
sum = (delta * rounds) & 0xffffffff
    y = v[0]

while rounds > 0:
        e = (sum >> 2) & 3
# 逆序遍历
for p inrange(n - 1, 0, -1):
            z = v[p - 1]
            v[p] = (v[p] - (((z >> 5 ^ y << 2) + (y >> 3 ^ z << 4)) ^ ((sum ^ y) + (key[(p & 3) ^ e] ^ z)))) & 0xffffffff
            y = v[p]

        p = 0
        z = v[n - 1]
        v[0] = (v[0] - (((z >> 5 ^ y << 2) + (y >> 3 ^ z << 4)) ^ ((sum ^ y) + (key[(0 & 3) ^ e] ^ z)))) & 0xffffffff
        y = v[0]

# 递减 sum 并减少轮次
sum = (sum - delta) & 0xffffffff
        rounds -= 1

# 解包重组回字符串
return struct.pack("<IIIIIIII", *v)

if __name__ == '__main__':
    key = [15000, 89894, 17, 223123]
    cipher_bytes = [92, 48, 135, 133, 200, 107, 126, 102, 179, 245, 80, 205, 181, 96, 6, 202,
94, 87, 102, 157, 187, 52, 50, 64, 235, 213, 130, 241, 244, 219, 13, 243]

# Python3 输出解码结果
print("Flag:", decrypt(cipher_bytes, key).decode('utf-8'))
```

## 四、 最终 Flag 结果

运行解密脚本输出的结果即为答案本体：

> **`f8fd708c923817076dc3ff56c535ec7b`**

预览时标签不可点

作者提示: 内容由AI生成

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

ListSec

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/GPsT7FaPGw5uQIpWOXmtw3tpIcv79XQaeOzFgThibkpMw28zSicDFgOumVJfHnfM533DBb7ibM1KnqkShD3Wtt3BA/0?wx_fmt=png)

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