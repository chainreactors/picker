---
title: Look out! Divergent representations are everywhere!
url: https://buaq.net/go-135073.html
source: unSafe.sh - 不安全
date: 2022-11-11
fetch_date: 2025-10-03T22:21:21.842783
---

# Look out! Divergent representations are everywhere!

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

![](https://8aqnet.cdn.bcebos.com/be4b9c17d9e1cc93284d40db14826abf.jpg)

Look out! Divergent representations are everywhere!

By Andreas KellasTrail of Bits recently published a blog post about a signed int
*2022-11-10 20:30:53
Author: [blog.trailofbits.com(查看原文)](/jump-135073.htm)
阅读量:17
收藏*

---

**By Andreas Kellas**

Trail of Bits recently published a [blog post](https://blog.trailofbits.com/2022/10/25/sqlite-vulnerability-july-2022-library-api/) about a signed integer overflow in certain versions of SQLite that can enable arbitrary code execution and result in a denial of service. While working on proof-of-concept exploits for that vulnerability, we noticed that the compiler’s representation of an important integer variable is semantically different in different parts of the program. These differences result in inconsistent interpretations of the variable when it overflows, which we call “divergent representations.” Once we found an example, we tried to find more—and discovered that divergent representations are actually quite common in compiled C code.

This blog post examines divergent representations of the same source code variable produced by compiler optimizations. We’ll attempt to define divergent representations and look at the SQLite vulnerability we discovered, which was made *easier to exploit* by the divergent representation of a source code variable (one exhibiting undefined behavior). We’ll then describe the binary and source code analyses that we used to find more divergent representations in existing open-source codebases. Finally, we’ll share some suggestions for eliminating the risk that a program will be compiled with divergent representations.

## A simple example

Here’s a simple example of a real-life code pattern that can result in divergent representations:

```
int index_of(char *buf, char target) {
    int i;
    for (i=0; buf[i] != target; i++) {}
    return i;
}
```

The `index_of` function receives a character array as input, loops through the array and increments `i` until it encounters the first target character, and returns the index of that target character. One might expect that `buf[index_of(buf, target)] == target`, but the evaluation of that statement can depend on the compiler’s optimization level. More specifically, it can depend on the compiler’s handling of undefined behavior when the value of `i` exceeds the maximum positive `int` value (`INT_MAX`, i.e., `0x7fffffff`).

If the target character appears in the first `INT_MAX` bytes of the buffer, the function will exhibit well-defined behavior, assuming that the platform uses 32-bit integers. If the function scans the first `INT_MAX` bytes of the array without finding the target character, `i` will be incremented beyond the maximum representable positive value for the `int` type, which is undefined behavior.

So how would the compiler handle that code—that is, code that could exhibit a signed integer overflow at runtime? Of course, because signed integer overflows are undefined behavior, the compiler could choose to do anything at all, including producing “[nasal demons](http://www.catb.org/jargon/html/N/nasal-demons.html).” This is a question about expectations, then: What would we expect a reasonable compiler to do? If `i` were incremented beyond `INT_MAX`, where would we expect `index_of` to try to read a character from memory?

We might expect the compiler to make one of two seemingly reasonable choices:

1. Represent `i` as a signed 32-bit value, causing `i` to wrap from `INT_MAX` (a positive value represented as `0x7fffffff`) to `INT_MIN` (a negative value represented as `0x80000000`), in which case the function would read the next byte from buf[INT\_MIN] as a negative array index
2. Represent `i` as an unsigned 64-bit value, causing `i` to increment to the unsigned value `0x80000000` and the function to read the next byte from `buf[0x80000000ul]`, which is the next contiguous byte in memory

In either case, if the next character read were the target byte, the `index_of` function would return `(int) 0x80000000`, which is `INT_MIN` (a negative number). However, in case 2, the memory location checked for the target character would not be `buf[INT_MIN]`. In other words, the expression `buf[index_of(buf, target)] == target` would not be true if the compiler chose to represent `i` as an unsigned 64-bit value—and that is exactly how [Clang compiles `index_of`](https://godbolt.org/z/rzMdEGb66) at optimization level -O1 and above:

```
index_of(char*, char):              # @index_of(char*, char)
        mov     eax, -1
.LBB0_1:                            # =>This Inner Loop Header: Depth=1
        inc     eax
        lea     rcx, [rdi + 1]
        cmp     byte ptr [rdi], sil
        mov     rdi, rcx
        jne     .LBB0_1
        ret
```

This is an example of a divergent representation of the same source code variable, `i`. The value of `i` returned by the function is represented by addition (`inc`) on the 32-bit `eax` register, while the value of `i` used to access the array buffer is represented by addition (`lea`) on the 64-bit `rdi` register. The source code makes no distinction between these two versions of `i`, as the programmer likely expected that the value used to index into the buffer would be the same one returned by the function. As we’ve shown, though, that is not the case.

## How do divergent representations appear?

A compiler can apply optimizations to a program to improve the program’s performance. Compilers must ensure the correctness of operations over well-defined inputs, but they can take arbitrary liberties to speed up the execution of undefined behavior. For example, to optimize code on a 64-bit platform, a compiler can replace 32-bit addition with 64-bit addition, because the defined behavior of addition on a 32-bit platform is also defined behavior on a 64-bit platform.

A divergent representation occurs when a compiler applies program optimizations that cause a single source variable to be represented with different semantics in the output program. The instances of divergent representations that we’ve observed all result from undefined behavior (particularly signed integer overflows). Since programmers shouldn’t write programs with undefined behavior, one could argue that divergent representations are a non-issue. However, we assert that programs ought to have consistent interpretations of the same value even in cases of undefined behavior.

A divergent representation occurs when a compiler applies program optimizations that cause a single source variable to be represented with different semantics in the output program. The instances of divergent representations that we’ve observed all result from undefined behavior (particularly signed integer overflows). Since programmers shouldn’t write programs with undefined behavior, one could argue that divergent representations are a non-issue. However, we assert that programs ought to have consistent interpretations of the same value even in cases of undefined behavior.

The divergent representations that we’ve found occur in code that fits the following pattern:

1. A signed integer variable is declared outside of a loop.
2. The variable is incremented or decremented in the loop and is allowed to overflow.
3. The variable is used in the loop to access an array.
4. The variable is used outside of the loop.

A 2011 discussion [on the LLVM developers mailing list](https://groups.google.com/g/llvm-dev/c/sDYaYV_ZF-g/m/5Ektu6vM_0oJ) provides fascinating insight into the representation of variables that may overflow, along with the effect that an...