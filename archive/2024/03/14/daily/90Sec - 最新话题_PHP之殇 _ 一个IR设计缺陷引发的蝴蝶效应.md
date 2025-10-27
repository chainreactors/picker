---
title: PHP之殇 : 一个IR设计缺陷引发的蝴蝶效应
url: https://forum.90sec.com/t/topic/2422
source: 90Sec - 最新话题
date: 2024-03-14
fetch_date: 2025-10-04T12:07:45.030931
---

# PHP之殇 : 一个IR设计缺陷引发的蝴蝶效应

[90Sec](/)

# [PHP之殇 : 一个IR设计缺陷引发的蝴蝶效应](/t/topic/2422)

[技术文章](/c/article/6)

[maplgebra](https://forum.90sec.com/u/maplgebra)

2024 年3 月 13 日 12:32

1

[原文地址](https://m4p1e.com/2024/03/13/bad_php_ir/)

## 0x01 IR设计中的问题

### 1.1 问题来源

[鸟哥](https://www.laruence.com/) (Laruence) [1]是所有国内PHPer应该都知道的一个人。鸟哥的博客是我早期学习PHP内核的时候经常会去的地方。在2020年的时候，鸟哥发了一篇《深入理解PHP7内核之HashTable》的文章[2]，在文章的结尾提到了一个问题:

> 在实现zend\_array替换HashTable中我们遇到了很多的问题，绝大部份它们都被解决了，但遗留了一个问题，因为现在arData是连续分配的，那么当数组增长大小到需要扩容到时候，我们只能重新realloc内存，但系统并不保证你realloc以后，地址不会发生变化，那么就有可能：
>
> ```
> <?php
> $array = range(0, 7);
>
> set_error_handler(function($err, $msg) {
>     global $array;
>     $array[] = 1; //force resize;
> });
>
> function crash() {
>     global $array;
>     $array[0] += $var; //undefined notice
> }
>
> crash();
> ```
>
> 比如上面的例子， 首先是一个全局数组，然后在函数crash中， 在+= opcode handler中，zend vm会首先获取array[0]的内容，然后+$var, 但var是undefined variable， 所以此时会触发一个未定义变量的notice，而同时我们设置了error\_handler, 在其中我们给这个数组增加了一个元素， 因为PHP中的数组按照2^n的空间预先申请，此时数组满了，需要resize，于是发生了realloc，从error\_handler返回以后，array[0]指向的内存就可能发生了变化，此时会出现内存读写错误，甚至segfault，有兴趣的同学，可以尝试用valgrind跑这个例子看看。
>
> 但这个问题的触发条件比较多，修复需要额外对数据结构，或者需要拆分add\_assign对性能会有影响，另外绝大部分情况下因为数组的预先分配策略存在，以及其他大部分多opcode handler读写操作基本都很临近，这个问题其实很难被实际代码触发，所以这个问题一直悬停着。

直到今天这个问题还是**悬停**着。对于普通PHP开发者而言，这可能确实不算是一个很大的问题，但对于做安全的人来说，这里可能隐藏一个很严重的安全问题。因为它是我见过为数不多出现在PHP VM中的问题，而不是平时出现在各种PHP native libraries中的问题。一旦可以被利用，影响将非常之大。所以这个问题一直就放在了我的心上，它也一直以`crash.php` [3] 在我的PHP-exploit repo中放了4年. 特别地，只要你用PHP7或者8运行它就会出现segmentfault，也不知道有没有人去尝试过。

### 1.2 修复该问题的阻力

鸟哥出给的解释非常清晰明了，这里我试着用更加通俗的伪代码来进一步帮助不熟悉PHP内部的读者, 去理解PHP VM在第11行这里到底做了什么:

```
// array = [0, 1, 2, 3, 4, 5, 6, 7]
arr_base = get_base_addr_of(array)
elem_addr = get_addr_by_index(array_base, index)
elem = get_elem_from_addr(elem_addr)
// elem is ok
check_var(var)
// is elem ok?
res = add(elem, var)
assign_var_to_elem(elem, res)
```

这里做了这样几件事:

1. 首先我们获取这个`array`存储元素内存区域的起始地址;
2. 根据`index`获取我们指定元素的内存地址;
3. 从`elem_addr`读取元素到`elem`;
4. 检查`var`的合法性, 更具体一点， 当`var`是一个PHP代码中显式变量(i.e., `$a`)的时候， 检查它是否被定义过。 如果`var`是一个未定义的PHP变量, 那么VM会将var的值初始化为`null`. 因为VM不能直接将`undefined` (类似JS中的特殊值)， 暴露给用户代码；
5. 对`elem`和`var`做算术加法得到结果`res`;
6. 最后将`var`赋值给`elem`。

而问题出现在第6行这里，`check_var(var)`可能会产生副作用(side-effects)，从而**clobber the world**。这个词我是从JavaScriptCore (WebKit的JS引擎) 中学到的，副作用的出现可能会导致之前的计算结果变得的不可信，在这种不确定地情况下，我们是不能直接使用这些计算结果的。这里的`elem`是否还依然正确地指向待写入的目标元素呢？ 在第6行之后我们是不能确定的，因为它指向的内存地址可能已经被释放了，而正确的目标元素位置已经被搬到了其他内存上。

以上其实就是PHP opcode `ZEND_ASSIGN_DIM_OP`的大致解释过程，完整的解释过程你可以在[4]中找到。那么这个问题为什么一直没有被修复呢？ 好问题。我们从几个直觉上可行的简单修复方法开始，来讲一下修复的阻力在哪里。这里我用`array->arData`表示指向第1个元素的内存地址，其余`array`其他元素都顺序地落在其后.

**简单方法1: 在第6行之后检查`elem`是否还落在`array->arData`相对位置上**

这样做只能确保`array->arData`没有发生变化，但是你如何保证ABA问题 ? 比如`array`存储元素区域被释放了，然后被其他内存结构抢占了，然后又被释放了，再被布置为原本`array`存储元素区域的布局 (另外一个和它结构相同的`array2`把这块区域抢占了)。

**简单方法2: 把`check_var`放在最前面**

那么你考虑如下形式:

```
$array['a']['b'] = $var;
```

这段代码会被翻译成类似如下的中间代码:

```
L0 : V2 = FETCH_DIM_W CV0($array) string("a")
L1 : ASSIGN_DIM V2 string("b")
L2 : OP_DATA CV1($var)
```

这里我们考虑不带二元运算的`ZEND_ASSIGN_DIM`。以上代码等同于:

```
V2 &= $array['a'];
V2['b'] = $var;
```

其中`V2`是指向`$array`中index为`'a'`元素的位置，所以这里我用`&=`，来强调`V2`不是`$array['a']`。那么问题来了，如果第2行中的副作用导致在`$array`被resized了，那么这个`V2`就指向的位置就不对了。

这个问题注定了不能简单地被修复。

### 1.3 unset 和 reassign

你可以试着将前面的resize操作换成unset或者reassign，如下:

```
<?php
$array = range(0, 7);

set_error_handler(function($err, $msg) {
 global $array;
 // $array = 2;
 unset($array);
});

function crash() {
 global $array;
 $array[0] += $var; //undefined notice
}

crash();
```

两个情况有些不太一样:

1. `unset($array)`，只是将`$array`在当前function scope内给"清理"掉了，并不影响全局变量中的`$array`，所以这里没有问题。
2. `$array = 2`会影响到所有引用到它的地方，因此这里产生了和resize一样的问题。

有趣地是，官方已经注意到这样的问题，比如它对undefined `index` (i.e., `$arr[$undef_var] = 1`)产生的副作用做出了检查。而对要写入的值没有做检查。

1. 这里它首先让`ht` (`HashTable`是`zend_array`的别名) 引用计数加1，把这个array hold住。
2. 等错误处理函数返回之后，再减去这个前面加上的引用计数，如果引用计数没有发生变化，说明array没有被释放。

```
static zend_never_inline zend_uchar slow_index_convert(HashTable *ht, const zval *dim, zend_value *value EXECUTE_DATA_DC)
{
	switch (Z_TYPE_P(dim)) {
		case IS_UNDEF: {
			/* The array may be destroyed while throwing the notice.
			 * Temporarily increase the refcount to detect this situation. */
			 if (!(GC_FLAGS(ht) & IS_ARRAY_IMMUTABLE)) {
				GC_ADDREF(ht);
			}
			ZVAL_UNDEFINED_OP2();
			if (!(GC_FLAGS(ht) & IS_ARRAY_IMMUTABLE) && !GC_DELREF(ht)) {
				zend_array_destroy(ht);
				return IS_NULL;
			}
            // ...
```

### 1.4 可能的修复方法

将`ZEND_ASSIGN_DIM`或者`ZEND_ASSIGN_DIM_OP` (同时包括所有的array fetch操作) 改成支持**multi-index**, 是我觉得最直接的手法。比如前面的`$array['a']['b'] = $var;`会被翻译为

```
L0 : V2 = FETCH_DIM_W CV0($array) string("a")
L1 : ASSIGN_DIM V2 string("b")
L2 : OP_DATA CV1($var)
```

那么现在直接翻译为

```
L0 : ASSIGN_DIM CV0($array) [string("b"), string("b")]
L1 : OP_DATA CV1($var)
```

并且再此之前把所有的indexs和带待写入的var对应的表达式全部计算完成。注意这并不会改变现在PHP求值顺序. 考虑如下代码

```
<?php

function func1() {
	echo "func1\n";
	return 1;
}

function func2() {
	echo "func2\n";
	return 2;
}

$a = [];
set_error_handler(function($err, $msg){echo $msg."\n";});
echo $a[func1()][func2()];
/* output at PHP 8.3.3:
func1
func2
Undefined array key 1
Trying to access array offset on null
*/
```

可以看到`index`也是全部是先计算完成的。

## 0x02 三只蝴蝶 (butterfly)

TL;DR. 如果不想听故事可以跳过这一章节。

四年前，在知道了这个问题之后，我就开始了探索应该如何利用它。非常可惜，我不太聪明，四年都没有能想出个招。这四年，我的工作也和PHP紧密结合在一起，在PHP里面写了大概有40-50k行代码吧，以至于我近乎写出了一个全新的PHP解释器，很难想象这是一个做安全的人在做的事情。所以我对PHP要稍微了解那么多一点点。

我能完成这篇文章，是因为有三只蝴蝶。第一只蝴蝶，教会我了一些新的方法; 第二只蝴蝶，让我发现了新大陆; 第三只蝴蝶，带我走出了困境。

之前，我其实一直被困在一个误区里面。我的基本想法是:

1. `array`会被resize。
2. 然后我马上拿到`array`释放的内存，这样就可以造一个UAF出来。

这里没有问题。

这里贴一下前面的关于`ZEND_ASSIGN_DIM_OP`类似的`ZEND_ASSIGN_DIM`的伪代码:

```
// array = [0, 1, 2, 3, 4, 5, 6, 7]
arr_base = get_addr_of(array)
elem_addr = get_addr_of(array_base, index)
elem = get_elem_from_addr(elem_addr)
check_var(var)
assign_var_to_elem(elem, var)
```

但是问题来了，其中`assign_var_to_elem`只能像目标内存写一个特殊的`null` (前面提到`var`会被初始化为`null`)值, 并且过程中需要对`elem`进行检查。换句话说目标内存需要有比较苛刻的memory layout. 其次受鸟哥代码中的`a[0] += $var`影响，我觉得这个`null`只能在这块内存稍前的位置写入。这就是我的误区。结合以上原因一直让我找不到一个合适的structure来hold这块内存。

过去我逐渐地其实不太关注PHP里面的安全了，有时候写代码也会发现一些问题，但也觉得就那么回事。直到最近看见了关于LockBit的新闻，突然有了兴趣，才有了《CVE-2023-3824: 幸运的Off-by-one (two?)》[5] 一文。在文章写完后的几天，我又去逛逛了安全圈看看大家都在研究什么，在这过程中发现那三只蝴蝶。

首先发现了一篇《WebAssembly安全研究总结》[6]。 这篇文章中重要介绍了如何通过构造恶意的bytecode来攻击Wasm引擎，挺有趣的，也行PHP opcache中的也有类似的问题。我个人比较喜欢解释器和编译器上的一些安全研究，然后我就想去看看有没有关于Wasm更深入一点研究，搜索了一下作者其他的文章。

**第一只蝴蝶**

我又发现了作者有许多关于JavaScriptCore (jsc) 的研究，我之前是没有接触过jsc，只短暂接触过V8。感觉似乎挺有趣的，那就来感受一下吧。在文章[7]和系列文章[8]的帮助下，使得我的博客中又多了一篇《CVE-2018-4262: Apple Safari RegExp Match Type Confusion by JIT》。在这过程中积累了一点点关于jsc的姿势。特别地，里面的部分构造(box/unbox)让我大开眼界，可谓是相当之精彩，以至于后面在PHP的构造中我都想重现它。 jsc里面有一个用来作为存储JSObject的properties和elements特殊结构叫butterfly, 因为其内存结构像一只带翅膀的蝴蝶，顾名butterfly。ascii graph来自[9]

```
--------------------------------------------------------
.. | propY | propX | length | elem0 | elem1 | elem2 | ..
--------------------------------------------------------
                            ^
                            |
            +---------------+
            |
  +-------------+
  | Some Object |
  +-------------+
```

在jsc的利用中都频繁地使用到了这个结构，包含我前面提到的box/unbox技术。这是第一只蝴蝶。

**第二只蝴蝶**

在看[9]的过程中，我又看到了saelo(前google project zero成员, 目前V8 JS引擎的安全负责人)的博客中《Pwning Lua through 'load'》[10]。 真苦恼，都是我喜欢读的东西，那就看吧。让我比较惊讶的Lua竟然没有bytecode verifier，文章内容和第一篇攻击Wasm引擎的内容比较相似。然后我又想看看Lua上的一些安全研究，搜索了到一系列来自bigshaq关于LuaJIT方面的安全研究[11]，在里面遇到了第二只蝴蝶。LuaJIT的jit complier会将收集到的trace翻译成的IR放在一个类似butterfly结构中。形如

```
    -----------------------------------------
          |      |      |     |     |
          |const2|const1|inst1|inst2|
          |      |      |     |     |
    --------------------▲-----------─---------
                        │
                        │
       ┌──────┐         │
       │ ir_p ├─────────┘
       └──────┘
```

instructions在一边翅膀，而constants在另一边翅膀。在这短暂的LuaJIT之旅中，又积累了一些关于LuaJIT的知识，但是我觉得最后研究的安全问题太刻意，毕竟是CTF的题，可以理解嘛。不过利用JIT code中的guarded assertions来固定shellcode的技术确实不错。

**最后一只蝴蝶**

PHP 8中的JIT技术深受LuaJIT影响。以至于bigshaq博客在一篇关于PHP文章中，给PH...