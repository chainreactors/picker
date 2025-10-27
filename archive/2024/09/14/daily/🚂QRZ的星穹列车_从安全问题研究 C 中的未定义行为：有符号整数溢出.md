---
title: 从安全问题研究 C 中的未定义行为：有符号整数溢出
url: https://5ec.top/00-notes/0b-programming-language-and-compiler/c-lang/UB-Signed-Overflow-make-code-unsafe-1
source: 🚂QRZ的星穹列车
date: 2024-09-14
fetch_date: 2025-10-06T18:27:31.376950
---

# 从安全问题研究 C 中的未定义行为：有符号整数溢出

## [🚂QRZ的星穹列车](../../..)

搜索

Search

暗色模式亮色模式

阅读模式

## 探索

[📑Tags](/tags)[🪪About](/misc/about)[📻Radio](/z6-life/ham-radio/index)[🧑‍🤝‍🧑Friends](/misc/friends)[🚇开往](https://www.travellings.cn/go.html)

---

[Home](../../../)

❯

[笔记](../../../00-notes/)

❯

[程序语言与编译](../../../00-notes/0b-programming-language-and-compiler/)

❯

[c lang](../../../00-notes/0b-programming-language-and-compiler/c-lang/)

❯

从安全问题研究 C 中的未定义行为：有符号整数溢出

# 从安全问题研究 C 中的未定义行为：有符号整数溢出

2024年9月13日11分钟阅读

* [compiler/gcc](../../../tags/compiler/gcc)
* [programming-language/c](../../../tags/programming-language/c)

### 目录

* [问题引入](#问题引入)
* [优化流程](#优化流程)
* [Early Value Range Propagation Pass](#early-value-range-propagation-pass)
* [救一下？](#救一下)
* [修复策略](#修复策略)
* [总结思考](#总结思考)
* [参考资料](#参考资料)

> 更新历史
>
> 2024-10-12：修改文章中的一些错误，补充一些内容。

最近偶然间看到一个编译器优化导致的[问题](https://github.com/OpenSIPS/opensips/security/advisories/GHSA-c6j5-f4h4-2xrq)，感觉比较有趣，自己还没有分析过类似的问题，正好分析一下。

## 问题引入

gcc 在 -O2 以上级别的优化中会将有符号整数溢出完全忽略，在上面的问题中，作者的本意是希望通过溢出之后的负值来判断是否存在溢出：

```
while (p<end && *p>='0' && *p<='9') {
    number = number*10 + (*p)-'0';
    if (number<0) {
        LM_ERR("number overflow at pos %d in len number [%.*s]\n",
            (int)(p-buffer),(int)(end-buffer), buffer);
        return 0;
    }
    size ++;
    p++;
}
```

但是编译器却执行坏了：

![](https://r2blog.qrz.today/d935ca13d4210ec46b9350ef318aa47b.20240908122828.png)

可以看到，在 gcc14 上用 O3 级别的优化会把整个判断干掉，但用 O0 级别的优化就不会：

![](https://r2blog.qrz.today/edef0df25604aa1047d4a59ba0546224.20240908125316.png)

用 clang 的 O3 优化也不会：

![](https://r2blog.qrz.today/c25a4272fe695ef0432de65104354145.20240908125441.png)

那么问题显然出现在 gcc 的优化过程中。最开始我和同事认为可能哪里出现了隐式的无符号扩展，但经过多次测试之后发现并非如此。

我在网上搜索一番之后发现了 Hacker News 上的[讨论](https://news.ycombinator.com/item?id=11146384)，这居然是一个 [feature](https://kristerw.blogspot.com/2016/02/how-undefined-signed-overflow-enables.html) 而不是一个 bug。简单来说，有符号整数溢出在 C 的标准中是一个未定义行为（Undefined Behavior），gcc 的处理是，在进行高级别优化的时候会将所有的有符号溢出认为是不可能发生的，并在优化时去除这些“死代码”。

## 优化流程

那么我感兴趣的问题之一是，gcc 是怎么一步一步将这一段代码优化掉的呢？

在学过编译原理后，我们知道 gcc 的优化流程大概是这样子的：

```
               +-----+
             +-| cc1 |--------------------------------------------------+
             | +-----+                                                  |
             |                                                          |
             |  C frontend          Optimizer          x86_64 backend   |
C source ====+==============>  IR =============> IR  ===================+==> x86_64 asm
             |                                                          |
             +----------------------------------------------------------+
```

我们关注的就是 IR 的变化。gcc 提供了一些可以查看中间优化过程的[选项](https://gcc.gnu.org/onlinedocs/gcc-6.3.0/gcc/Developer-Options.html)，这里用到了：

* `-fdump-tree`，可以将中间树保存到文件中；
* `-fdump-ipa`，可以将过程间分析树保存到文件中；
* `-fdump-rtl`，可以将 RTL IR 保存到文件中。

我们通过下面的命令：

```
gcc -S replay.c -O3 -fverbose-asm -fdump-tree-all -fdump-ipa-all -fdump-rtl-all
```

将所有中间语言树都保存下来，大概会保存成 `{source code}.{pass number}{type}.{passname}` 这样的形式。其中：

* `pass number` 指的是当前的轮次
* `type` 指的是分析的形式，可能包含：
  + `i`：程序间分析树；
  + `l`：特定语言；
  + `r`：RTL IR；
  + `t`：中间分析树。

> Note
>
> gcc 还提供了生成 CFG 的功能，我们可以通过
>
> ```
> gcc -S replay.c -O3 -fverbose-asm -fdump-tree-all-graph -fdump-ipa-all-graph -fdump-rtl-all-graph
> ```
>
> 生成 CFG。

在分析之后，可以发现在第 37 个 pass fre1 还是正常的：

![](https://r2blog.qrz.today/175437ae4226c4c11086dc6aa5285819.37.svg)

接下来在 evrp 这个 pass 中将这个判断干掉了：

![](https://r2blog.qrz.today/4dfafa5da872dc26d1f94247f7b69c7e.38.svg)

根据 gcc 参数的介绍，我猜测是 `-O2` 以上默认开启的 `-ftree-vrp` ~~和 `-fstrict-overflow`~~ 参数导致的：

* `-ftree-vrp`：机翻一下介绍。
  + 对树执行值范围传播。这与常量传播传递类似，但传播的不是值，而是值的范围。这样，优化程序就能移除不必要的范围检查，如数组绑定检查和空指针检查。在 -O2 及更高版本中，默认启用此功能。只有启用 `-fdelete-null-pointer-checks` 时，才能消除空指针检查。
* ~~`-fstrict-overflow`~~：这个参数会假设有符号整数溢出不会发生，以优化代码。

> Attention
>
> 参考 [3.11 Options That Control Optimization](https://gcc.gnu.org/onlinedocs/gcc/Optimize-Options.html)，O2 并没有开启 `-fstrict-overflow`
>
> 而如果我们在 O1 的基础上开启 `-ftree-vrp` 则会发生和 O2 一样的剪枝。

### Early Value Range Propagation Pass

ftree-vrp，也就是 evrp pass 本质上做的是早期值域转播的工作。这里不深究它实现的细节，只关注这个过程中都做了什么。根据我们输出的中间信息，首先它推断了 pass 37 过程中各个变量的范围：

```
Value ranges after Early VRP:

_1: long unsigned int [0, 10]
_2: int VARYING
number_3: int [number_13, number_13]
_4: int [48, 57]
_5: int [-2147483600, +INF]
_7: int [0, 10]
_8: long int VARYING
_9: int VARYING
_10: char VARYING
p_11: char * [1B, +INF]  EQUIVALENCES: { p_12 } (1 elements)
p_12: char[11] * [&buffer, +INF]
number_13: int VARYING
size_14: int [0, +INF]
_19: signed long [0, 10]
end_22: char[11] * [1B, +INF]
number_23: int [-INF, 2147483599]
size_24: int [1, +INF]
p_25: char * [1B, +INF]
_32: int VARYING
_33: int VARYING
```

在推断出范围之后，对基本块做了一些操作：

```
Removing basic block 4
Merging blocks 3 and 5
Merging blocks 9 and 10
```

看一下被移除的 4 号基本块，它就是我们判断整数溢出的那个逻辑。而稍微向上追溯一下影响到它的变量，会发现是 `number_23`。有趣的事情出现了，既然在上文的值域传播中推断出 `number_23` 的值域是 `int [-INF, 2147483599]`，为什么接下来就移除了 4 号基本块呢？在哪里对 `number_23` 的值域进一步进行判断了呢？

在阅读 gcc 参数文档之后，我发现可以通过下面的命令获得更详细的输出：

```
gcc -S replay.c -O3 -fverbose-asm -fdump-tree-all-all -fdump-ipa-all-all -fdump-rtl-all-all
```

仔细看一下：

```
Removing basic block 4
;; basic block 4, loop depth 0
;;  pred:
# p_11 = PHI <>
_19 = (signed long) _1;
_7 = (int) _1;
_8 = p_11 - &buffer;
_9 = (int) _8;
_32 = __printf_chk (1, "Number overflow at pos %d in len number [%.*s]\n", _9, _7, &buffer);
// predicted unlikely by early return (on trees) predictor.
buffer ={v} {CLOBBER};
goto <bb 10>; [INV]
;;  succ:       10
```

根据注释推测是被 early return (on trees) predictor 去除了，对应的源码中的宏应该是 `PRED_TREE_EARLY_RETURN`。更深的原因可能需要去分析 gcc 的源码了，等以后有机会再继续分析吧。

## 救一下？

除了在 `-O2` 以上默认开始的 `-fstrict-overflow` 之外，gcc 也提供了其他控制整数溢出的选项，例如 `-fno-strict-overflow` 和 `-fwrapv`。不过参考 [wiki](https://gcc.gnu.org/wiki/boringcc)，从 gcc8 以来 `-fno-strict-overflow` 和 `-fwrapv` 是一样的了。而对于 `-fwrapv`，它仍然会允许一些整数溢出的情况，恰好就和本文所描述的一致，所以还是救不了：

> See also the -fwrapv option. Using -fwrapv means that integer signed overflow is fully defined: it wraps. When -fwrapv is used, there is no difference between -fstrict-overflow and -fno-strict-overflow for integers. With -fwrapv certain types of overflow are permitted. For example, if the compiler gets an overflow when doing arithmetic on constants, the overflowed value can still be used with -fwrapv, but not otherwise.

## 修复策略

回到开头的问题，作者们的修复方式也值得讨论一下。

[第一次修复](https://github.com/OpenSIPS/opensips/commit/7cab422e2fc648f910abba34f3f0dbb3ae171ff5)时只是简单地判断，让 number 最终小于 2147483647。

```
while (p<end && *p>='0' && *p<='9') {
	/* do not actually cause an integer overflow, as it is UB! --liviu */
	if (number > 214748363) {
		LM_ERR("integer overflow risk at pos %d in len number [%.*s]\n",
			(int)(p-buffer),(int)(end-buffer), buffer);
		return 0;
	}

	number = number*10 + (*p) -'0';
	size ++;
	p++;
}
```

但注意它的修复细节，在 `number = number*10 + (*p)-'0';` 这一段，如果我们先输入一个较大的值，先加 `(*p)` 也就是数字的 ascii 码再去减 0 的 ascii 码虽然可以得到正确的答案，但是在计算的中间会发生有符号整数溢出，这是一个未定义的行为，因此被 OSS Fuzz 用 UBSan 抓住了（`-fsanitize=undefined`），产生了第二次修复。

[第二次修复](https://github.com/OpenSIPS/opensips/commit/837263b47dcb33909b109b5cc050c1ab4a6c64a2)就很正常了，首先用 `INT_MAX` 替换 `214748363` 避免不同平台上 int 定义不一致的问题，接下来给 `((*p)-'0')` 加上括号，避免计算中间的 UB：

```
while (p<end && *p>='0' && *p<='9') {
	/* do not actually cause an integer overflow, as it is UB! --liviu */
	if (number >= INT_MAX/10) {
		LM_ERR("integer overflow risk at pos %d in length value [%.*s]\n",
			(int)(p-buffer),(int)(end-buffer), buffer);
		return NULL;
	}

	number = number*10 + ((*p)-'0');
	size ++;
	p++;
}
```

## 总结思考

有符号整数溢出也算是一个老生常谈的问题了，不过在现实中由于种种原因还是会出现各种问题。开发者应当谨慎对待未定义的行为，避免造成更大的危害。

* 对于开发者，应该少实现依赖未定义行为的逻辑和代码。不同的编译器对未定义行为的处理可能是不一致的。
* 对于安全人员，在审计分析开源项目的代码时也可以考虑对二进制进行测试，例如本文开头提到的安全问题就是通过 Fuzzing 捕获的。

感谢 [Lancern’s Treasure Chest](https://t.me/lancern_chest) 群组的大佬们，为我的分析提供了诸多帮助。

## 参考资料

* [ISO/IEC 9899:TC3 J.2 Undefined behavior](https://www.open-std.org/jtc1/sc22/wg14/www/docs/n1256.pdf)
* [Should I use Signed or Unsigned Ints In C? (Part 1)](https://blog.robertelde...