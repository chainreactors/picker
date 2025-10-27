---
title: LL(1) 文法
url: https://www.o2oxy.cn/4342.html
source: print("")
date: 2025-01-05
fetch_date: 2025-10-06T20:08:02.263721
---

# LL(1) 文法

![print("")](https://www.o2oxy.cn/wp-content/themes/JieStyle-Two/images/avatar.jpg)

### print("")

* [Home](http://www.o2oxy.cn)
* [信息安全](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8)
* [WEB前端](https://www.o2oxy.cn/category/web%E5%89%8D%E7%AB%AF)
* [linux](https://www.o2oxy.cn/category/linux)
* [python](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93)
* [监控](https://www.o2oxy.cn/category/%E7%9B%91%E6%8E%A7)
* [生活](https://www.o2oxy.cn/category/%E7%94%9F%E6%B4%BB)
* [Java学习](https://www.o2oxy.cn/category/%E5%AE%89%E5%85%A8/java)
* [宝塔面板最新活动](https://www.bt.cn/huodong)
* [Author](https://www.o2oxy.cn/tags)

# 词法分析 |LL(1) 文法

作者: print("")
分类: [编译原理](https://www.o2oxy.cn/category/%E6%95%B0%E6%8D%AE%E5%BA%93/%E7%BC%96%E8%AF%91%E5%8E%9F%E7%90%86)
发布时间: 2025-01-05 00:43
阅读次数: 5,743 次

**一、LL(1) 文法介绍**

第一个L代表 分析时从左向右扫描

第二个L代表分析过程将最左推导

1 代表只需要向右看一个符号

## **二、NULLABLE****集合**

nullable 介绍

非终结符 X 属于集合 NULLABLE，当且仅当：

基本情况：X -> ε
归纳情况：X -> Y1 … YnY1, … , Yn 是 n 个非终结符，且都属于 NULLABLE 集

所以，对于如下给出的两个例子，都不属于 NULLABLE：

1. X -> a
2. X -> β1 … βn。 βi 是终结符，但是存在一个 βj 可以推出 a。（推出结果中必定存在一个字符）

伪代码

```
NULLABLE = {};
while (nullable is still changing)
    foreach (production p: X -> β)
        if (β == ε)
            NULLABLE U= {X}
        if (β == Y1 ... Yn)     // 非终结符
            if (Y1 ∈ NULLABLE && ... && Yn ∈ NULLABLE)
                NULLABLE U= {X}
```

对于给定的产生式规则如下所示，其分析表得到如下：

```
Z -> d
   | X Y Z
Y -> c
   |
X -> Y
   | a
```

|  |  |  |  |
| --- | --- | --- | --- |
| NULLABLE | 0 | 1 | 2 |
|  | {} | {Y,X} | {Y,X} |

第一次循环得到了{Y,X}  因为和第0次循环的结果发生了变化触发了第二次循环。第二次循环还是{Y,X} 就得到了{Y,X}

## 三、FIRST 集合

FIRST(N) = 从非终结符N开始推导的出句子开头的所有可能终结符号集合

公式：

[![](https://www.o2oxy.cn/wp-content/uploads/2025/01/微信图片_20250105002707.png)](https://www.o2oxy.cn/wp-content/uploads/2025/01/%E5%BE%AE%E4%BF%A1%E5%9B%BE%E7%89%87_20250105002707.png)

简单理解为:就是找终结符

```
对 N-> a ....
FIRST(N) U ={a}

如果把a换成一个变量M  M代表终结符例如a 或者b 或者 c 或者n
对 N-> M ....
FIRST(N) U ={M}
```

一个简单的例子

```
例如
S -> N
N --> A C
A -->| b
C --> a
那么FIRST(A)={b,a}
```

#### **3.1 FIRST不动点****算法**

FIRST 集合的完整计算公式

```
基本情况
X -> a
FIRST(X) U= {a}
归纳情况
X -> Y1 ... Yn
FIRST(X) U= FIRST(Y1)
if Y1 ∈ NULLABLE, FIRST(X) U= FIRST(Y2)
if Y1, Y2 ∈ NULLABLE, FIRST(X) U= FIRST(Y3)
......
```

FIRST 集的完整不动点算法

```
foreach (nonterminal N)
    FIRST(N) = {}

while (some set is changing)
    foreach (production p: N -> β1 ... βn)
       foreach (βi from β1 upto βn)
            if (β1 == a ...)   // 最右推导  β1
                FIRST(N) U= {a}
                break
            if (β1 == M ...)
                FIRST(N) U= FIRST(M)
                if(M is not in NULLABLE)
                    break
```

对于给定的产生式规则如下所示，其分析表得到如下：

```
Z -> d
   | X Y Z
Y -> c
   |
X -> Y
   | a
```

得到如下的FIRST分析表

|  |  |  |  |
| --- | --- | --- | --- |
| N\FIRST | 0 | 1 | 2 |
| Z | {} | {d} | {a,c,d} |
| Y | {} | {c} | {c} |
| X | {} | {c,a} | {c,a} |

## ***五、FOLLOW集合***

FOLLOW 集合的定义

对于一个非终结符 A，FOLLOW(A) 定义为可能在任何句型中紧跟着 A 出现的终结符的集合。如果 A 是某个句型的最右符号，则将结束符 $（或 #）加入 FOLLOW(A)。

计算 FOLLOW 集合的步骤：

对于文法的开始符号 S： 将 $ 加入 FOLLOW(S)。这是因为分析过程总是从开始符号开始，并以 $ 结束。

1、对于文法的开始符号 S： 将 $ 加入 FOLLOW(S)。这是因为分析过程总是从开始符号开始，并以 $ 结束

2.、对于产生式 A -> αBβ

    将 FIRST(β) – {ε} 加入 FOLLOW(B)。也就是说，如果 B 后面跟着 β，那么 β 的 FIRST 集合中除了 ε 之外的所有终结符都可能紧跟着 B

    如果 ε ∈ FIRST(β)，或者 β 是空串，则将 FOLLOW(A) 加入 FOLLOW(B)。也就是说，如果 B 后面的符号可以为空，那么任何可以跟在 A 后面的符号也都可以跟在 B 后面。

**通过例子详细说明：**

```
S -> A B
A -> a | ε
B -> b | ε
```

计算过程

```
1. FOLLOW(S) 由于 S 是开始符号,将 $ 加入 FOLLOW(S) 因此，FOLLOW(S) = {$}。
2. FOLLOW(A)：A 出现在产生式 S -> A B 中。
	将 FIRST(B) - {ε} 加入 FOLLOW(A)。FIRST(B) = {b, ε}
	所以 FIRST(B) - {ε} = {b}。因此，将 b 加入 FOLLOW(A)
	由于 ε ∈ FIRST(B)，根据规则 2 的第二部分，
	将 FOLLOW(S) 加入 FOLLOW(A)。FOLLOW(S) = {$}。
	因此，FOLLOW(A) = {b, $}。
3.  FOLLOW(B):根据规则 2, B 出现在产生式 S -> A B 中。
	由于 B 是产生式的最右符号（β 是空串），
	根据规则 2 的第二部分，将 FOLLOW(S) 加入 FOLLOW(B)。
	FOLLOW(S) = {$}。因此，FOLLOW(B) = {$}

FOLLOW(S) = {$}
FOLLOW(A) = {b, $}
FOLLOW(B) = {$}
```

## FOLLOW 集的不动点算法

```
foreach (nonterminal N)
    FOLLOW(N) = {}
while (some set is changing)
    foreach (production p: N -> β1 ... βn)
        temp = FOLLOW(N)     // temp 记录在 βn 的后面
        foreach (βi from βn downto β1)   // 逆序 !!! 逆序的 FOLLOW。
            if(βi == a...)  // terminal
                temp = {a}
            if (βi == M ...)    // nonterminal
                FOLLOW(M) U= temp
                if(M is not NULLABLE)
                    temp = FIRST(M)
                else temp U= FIRST(M)
```

对于给定的产生式规则如下所示，其分析表得到如下：

```
Z -> d
   | X Y Z
Y -> c
   |
X -> Y
   | a
```

得到如下的分析表

|  |  |  |  |
| --- | --- | --- | --- |
| N\FOLLOW | 0 | 1 | 2 |
| Z | {} | {} | {} |
| Y | {} | {a,c,d} | {a,c,d} |
| X | {} | {a,c,d} | {a,c,d} |

## ***六、SELECT集合***

*SELECT 集合的定义*

*对于一个产生式 A → α，其 SELECT 集合定义为：在输入流的当前符号为 a 的情况下，如果 a 属于 SELECT(A → α)，那么可以选择该产生式进行推导。*

*更具体地，SELECT 集合的定义分为两种情况：*

1. *****如果 α 不能推导出 ε（空串）：** SELECT(A → α) = FIRST(α)。也就是说，如果 α 不能推导出空串，那么其 SELECT 集合就是 α 的 FIRST 集合。***
2. *****如果 α 可以推导出 ε（空串）：** SELECT(A → α) = (FIRST(α) – {ε}) ∪ FOLLOW(A)。也就是说，如果 α 可以推导出空串，那么其 SELECT 集合是 α 的 FIRST 集合（去除 ε）和 A 的 FOLLOW 集合的并集。***

*伪代码*

```
foreach (production p)
    FIRST_S(p) = {}
calculte_FIRST_S (production p: N -> β1 ... βn)
    foreach (βi from β1 to βn)
        if(βi == a...)  // terminal
            FIRST_S(p) U= {a}
            return;
        if (βi == M ...)    // nonterminal
            FIRST_S(p) U= FIRST(M)
                if(M is not NULLABLE)
                    return;
    FIRST_S(p) U= FOLLOW(N)
```

如上我们已经有了三个集合、整理到一起

NULLABLE={X,Y}

|  |  |  |  |
| --- | --- | --- | --- |
|  | X | Y | Z |
| FIRST | {a,c} | {c} | {a,c,d} |
| FOLLOW | {a,c,d} | {a,c,d} | {} |

****根据伪代码可以计算出********SELECT 集合如下****

|  |  |  |  |  |  |  |
| --- | --- | --- | --- | --- | --- | --- |
|  | 0 | 1 | 2 | 3 | 4 | 5 |
| SELECT | {d} | {a,c,d} | {c} | {a,c,d} | {a,c,d} | {a} |

## **七、LL(1)表**

```
0: Z -> d
1:   | X Y Z
2: Y -> c
3:   |
4: X -> Y
5:   | a
```

**根据上述已经完成的SELECT 集合可以构造出LL(1) 表**

|  |  |  |  |
| --- | --- | --- | --- |
|  | a | c | d |
| Z | 1 | 1 | 0,1 |
| Y | 3 | 2,3 | 3 |
| X | 4,5 | 4 | 4 |

**转成成文法的LL(1)表**

|  |  |  |  |
| --- | --- | --- | --- |
|  | a | c | d |
| Z | Z->X Y Z | Z->X Y Z | Z-d,Z->X Y Z |
| Y | Y-ε | Y->c,Y-ε | Y-ε |
| X | X->Y,X-a | X->Y | X->Y |

## ********八******、LL(1)******表*******冲******突*********

如上Z,d 值中的0,1   和Y,c 的值2,3  X,a 值是 4,5  这就出现了冲突。可以通过消除左递归的方式进行解决冲突

## 一、消除左递归

## 例如：一个文法如下

```
0:  E -> E+ T
1:       |  T
2:  T -> T *F
3:       |  F
4:   F -> n
```

我们构造出来的LL(1)表会如下

|  |  |  |  |
| --- | --- | --- | --- |
|  | n | + | \* |
| E | 0,1 |  |  |
| T | 2,3 |  |  |
| F | 4 |  |  |

主要的原因是由于存在左递归、使得0条语句和第1条语句存在交集、第2条语句和第3条语句存在交集

那么就需要去掉交集、例如

```
0:  E -> E+ T
1:       |  T
```

他的交集是T+T+T+T+T+T+T+T+T+T+T    这种方式 那么可以把第一个T提取出来

构造如下的

```
0:  E -> T E'
1:  E' -> T E'
2:       |
```

通过这样的方式就可以消除交集、生成新的规则

```
0:  E -> T E'
1:  E' -> T E'
2:       |
3:  T ->  F T'
4:  T' -> * F T'
5:        |
6:  F -> n
```

那么构造出新的LL(1) 表如下

|  |  |  |  |
| --- | --- | --- | --- |
|  | n | + | \* |
| E | 0 |  |  |
| E’ |  | 1 |  |
| T | 3 |  |  |
| T’ |  | 5 | 4 |
| F | 6 |  |  |

那么通过消除左递归后就发现表中是没有冲突的。

## 二、提取左公因子

 例如如下的文法

```
0: X -> a Y
1:      | a Z
2: Y -> b
3: Z -> c
```

主要是思想是把相同的进行合并例如 第0 行和1 行都出现了a 那么可以把a 提取出来。然后Y  Z 合并  如下

```
0:  X ->  a X'
1:  X' -> Y
2:       |  Z
```

## ********九、练习1********

```
1: lexp -> atom | list
2: atom -> number | identifier
3: list -> (lexp-seq)
4: lexp-seq -> lexp-seq lexp | lexp
```

要求

```
(a) Remove the left recursion
(b) Construct the First and Follow set of the nonterminals of the resulting grammar.
(c) Construct the LL(1) table for the resulting grammar.
(d) Show the actions of the corresponding parser, given the following input string (a(b(2))(c)).
```

首先需要消除左递归、在第四行中lexp-seq -> lexp-seq lexp | lexp  这个存在递归、可以采用消除左递归的方式修改

简化一下一下。可以当做为

```
X -> X A | A
```

那么就可以这样操作提取出A 再引入一个新的变量X’

```
X -> A X'
X'-> A X'
     | ε
```

换到当前的这个例子中如下就变成了这样的

```
1: lexp -> atom | list
2: atom -> number | ident...