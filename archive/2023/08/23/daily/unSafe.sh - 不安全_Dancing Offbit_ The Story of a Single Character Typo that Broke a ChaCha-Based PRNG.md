---
title: Dancing Offbit: The Story of a Single Character Typo that Broke a ChaCha-Based PRNG
url: https://buaq.net/go-175110.html
source: unSafe.sh - 不安全
date: 2023-08-23
fetch_date: 2025-10-04T11:58:48.129768
---

# Dancing Offbit: The Story of a Single Character Typo that Broke a ChaCha-Based PRNG

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/ab41076b698e482540de9684fd0760fd.jpg)

Dancing Offbit: The Story of a Single Character Typo that Broke a ChaCha-Based PRNG

Random number generators are the backbone of most cryptographic protocols,
*2023-8-22 21:0:0
Author: [research.nccgroup.com(查看原文)](/jump-175110.htm)
阅读量:26
收藏*

---

Random number generators are the backbone of most cryptographic protocols, the crucial cornerstone upon which the security of all systems rely, yet they remain often overlooked. This blog post presents a real-world vulnerability discovered in the implementation of a Pseudo-Random Number Generator (PRNG) based on the ChaCha20 cipher.

## Discovery of a biased PRNG

During a recent engagement, we were tasked with reviewing a ChaCha20-based PRNG, following a design similar to the Rust [ChaCha20Rng](https://rust-random.github.io/rand/rand_chacha/struct.ChaCha20Rng.html). The implementation under review was written in Java and a first pass over the source implementation did not reveal any glaring issue.

Similarly, a glance over the output produced by the PRNG seemed normal at first. As an example, the PRNG produced the following 32-byte sequence when seeded with a random seed:

```
-69, -112, 94, -33, 51, 35, -123, 21, -20, -30, -93, -51, -128, -78, -62, 37, -108, 5, 72, 15, 15, -121, 90, 41, -96, -107, -94, -50, 39, -96, -116, 19
```

Note that since Java does not support unsigned primitive types, bytes are interpreted in [two’s complement](https://en.wikipedia.org/wiki/Two%27s_complement) representation and a byte can take any value from -128 to 127.

However, when generating longer outputs, some curious patterns started to emerge. Consider the following 128-byte output, seeded with the same random value as before:

```
-69, -112, 94, -33, 51, 35, -123, 21, -20, -30, -93, -51, -128, -78, -62, 37, -108, 5, 72, 15, 15, -121, 90, 41, -96, -107, -94, -50, 39, -96, -116, 19, 48, 41, 127, -90, -62, -31, -103, -59, -51, 82, 49, 72, 103, -112, 76, -67, 29, -88, 126, -101, -85, -1, -1, -1, 10, 81, 8, -76, -126, -1, -1, -1, -62, -21, 79, 104, -120, 55, -125, -70, 2, 108, -95, 74, -44, 89, -124, -20, 30, 76, -126, 90, 69, -1, -1, -1, 39, -110, -48, -34, 83, -1, -1, -1, 16, 41, 2, 115, -100, 96, 28, -65, -44, -73, 102, -123, 45, -11, -117, -128, 7, -55, -10, -50, -38, -1, -1, -1, 81, 127, -69, -22, 124, 82, 51, 112
```

Starting at byte 54, sequences of triplets of `-1` are repeated multiple times, too often for this pattern to be random. Note that `-1` is equivalent to the byte value `0xFF` (that is, the byte exclusively composed of 1-bits: `0b1111 1111`), but Java interprets and displays that value as `-1`.

## Identifying the root cause

Driven by the feeling that something was amiss, we delved into the code once more and eventually narrowed down the faulty code to the `rotateLeft32()` function, a critical building block of ChaCha20. This function is excerpted below for convenience.

```
private static int rotateLeft32(int x, int k) {
    final int n = 32;

    int s = k   (n - 1);
    return x << s | x >> (n - s);
}
```

At a first glance, this function seems to perform a fairly standard left rotation on 32-bit values. Since Java does not have a primitive type for unsigned integers, this function operates on signed integers. Upon more careful inspection, we discovered something wrong with the right shift operation performed in the return statement of the function. The `>>` operator used in the function above performs a *signed right shift* in Java (also known as an *arithmetic right shift*, or a *sign-propagating right shift* since it preserves the sign of the resulting number).

When shifting an integer by one with the `>>` operator, the most significant bit (i.e., the leftmost bit) is not unconditionally replaced by a zero, but by a bit corresponding to the sign bit of the shifted value (0 for a positive integer, 1 for a negative integer). Since the return value of the `rotateLeft32()` function is computed using a boolean “or” of that shifted quantity, a superfluous 1-bit resulting from shifting a negative input value will be propagated to the output. Hence, the `rotateLeft32()` function may produce incorrect results when performing the bitwise rotation of negative 32-bit integers.

In contrast, the operator `>>>` performs an *unsigned right shift* (or *logical right shift*) in Java, where the extra bits shifted off to the right are discarded and replaced with zero bits regardless of the sign of the original value. It is this operator that should have been used in the `rotateLeft32()` function. This subtle difference is very specific to Java. In Rust for example, the type of the value shifted dictates which shift variant to use, as explained in The Rust Reference book, in the section on [Arithmetic and Logical Binary Operators](https://doc.rust-lang.org/reference/expressions/operator-expr.html#arithmetic-and-logical-binary-operators):

> Arithmetic right shift on signed integer types, logical right shift on unsigned integer types.

## Impact

The impact of this issue in the rotation function could already be observed visually by the repeated presence of `-1`s. In order to understand why using a signed right shift results in an increased probability of generating `-1` bytes, let us look at the ChaCha function using that left rotation operation, namely the Quarter Round function, see [RFC 7539](https://www.rfc-editor.org/rfc/rfc7539):

```
a += b; d ^= a; d <<<= 16;
c += d; b ^= c; b <<<= 12;
a += b; d ^= a; d <<<= 8;
c += d; b ^= c; b <<<= 7;
```

For each call to the ChaCha Quarter Round function, internal state variables are left-rotated (using the `rotateLeft32()` function) by some fixed values, as highlighted above. Consider what happens when left-rotating a value with a single 1-bit using the function above. For illustration purposes, we’ll use the value `0x80000000` which corresponds to the quantity `10000000 00000000 00000000 00000000` (split into 8-bit chunks for clarity, and where obvious repeated sequences of `0`s are replaced with `...`).

```
 rotateLeft32(1000 ... 0000, 16)
 = 1000 ... 0000 << 16 | 1000 ... 0000 >> 16
 = 00 ... 0 | 1100 ... 0000 >> 15
 = 1110 ... 0000 >> 14
 = ...
 = 11111111 11111111 10000000 00000000
 = 0xFFFF8000
 = {-1, -1, -128, 0}
```

In this case, a value containing a single 1-bit as input results in an output consisting of seventeen (17) `1`s! This helps explain why the output that originally caught our eye contained so many `-1` bytes.

The usage of the incorrect shift operation is a damaging bias in the output distribution. To illustrate this bias, the figure below shows a plot of the output distribution of the ChaChaPRNG implementation when seeded with the same seed as in the examples, and used to generate a total of 10,000 32-byte samples. In the figure below, the bytes are normalized to be in the [0, 255] range. The most striking outlier is the value 255 (the `-1` discussed previously), which appears with probability over 20%. But other values also have significant biases, such as 0 (which appears with probability 2.46%) or 81 (which appears with probability 2.50%). In a truly random distribution, a given byte should appear with probability 1/256 = 0.390625.

![](https://i0.wp.com/research.nccgroup.com/wp-content/uploads/2023/05/biased.png?resize=1024%2C501&ssl=1)

Research has shown that leaking as little as [one bit of an ECDSA nonce](https://eprint.iacr.org/2020/615.pdf) could lead to full key recovery. Thus, using the output of this PRNG for cryptographic applications could completely break the security of the systems that rely upon it.

## The fi...