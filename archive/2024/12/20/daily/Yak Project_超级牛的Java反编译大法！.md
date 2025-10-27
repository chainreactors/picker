---
title: 超级牛的Java反编译大法！
url: https://mp.weixin.qq.com/s?__biz=Mzk0MTM4NzIxMQ==&mid=2247527282&idx=1&sn=8679a0f23973f54b748acdc529c48013&chksm=c2d117d6f5a69ec07b7182b081d4c1d815251068d7775573d3040f27c6526cf97c1023955f58&scene=58&subscene=0#rd
source: Yak Project
date: 2024-12-20
fetch_date: 2025-10-06T19:39:37.094687
---

# 超级牛的Java反编译大法！

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzoHc79vE7AJb416iaqePgASTIe6K2985WZIwesbTMGqo3YTDpS8FpQibA/0?wx_fmt=jpeg)

# 超级牛的Java反编译大法！

原创

Yak

Yak Project

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZfCSs0zKcMmDXyJt76PDpGiataSbajd3BpbZnPXBCqFaA3icu2mY1LGqAmJHIiaCq5N9qCBv47ktQEYA/640?wx_fmt=gif&from=appmsg)

是日，北风萧萧，天寒地冻...

超级牛打开了他的秘籍宝典

“请选择你的功法——”

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcC8HPM9rKsYfB1uUPLiaAucPo5m3sj8l059x8OJ5NxHguY3KA6RGLiaN7hw3K5kWU9OnNiauW3iaicbPQ/640?wx_fmt=png&from=appmsg)

《渗透测试高级技巧》

《SYN扫描》

**《Java反编译》**

...

那么，Java反编译，启动！

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZc2zO33vicQKaDFfayD2ibHxu7j6S9W4W43aNseMgdyBDuYeaVicrVRGSctesNFBadrA5XcaiczLO75aw/640?wx_fmt=other&from=appmsg&tp=webp&wxfrom=5&wx_lazy=1&wx_co=1)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzwtnKcXibOylYcB3EjrpiczujVcNFxY4XrVbLDiawKFcgCpqjyJdNKnkow/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzoRXKwp1GDcmiav2icK5bUpHfayaotQohE0EBAQ0t5qeReDAhsh9UIeLA/640?wx_fmt=png&from=appmsg)

控制流图（control-flow graph）简称CFG，是计算机科学中的表示法，利用数学中图的表示方式，标示计算机程序执行过程中所经过的所有路径。控制流图中的每个顶点都对应一个基本块，也就是一段没有分支指令。

下面是两段python代码和对应的CFG

```
```
if x > 0:    print(1)else    print(0)
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzqmNqeZDOMnUw53OeNXLVT5F7VT2mQFPNO0rMF46ZnnWpYlByjtbZEQ/640?wx_fmt=png&from=appmsg)

```
```
while x > 0:    print(1)    x-=1
```
```

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzUNRDKly9AUsr3gicLImpQFIrQxrynicAgVgXpPoTePu4s3kWUhD52gtA/640?wx_fmt=png&from=appmsg)

通过CFG可以清晰的看到程序的所有执行路径，有助于后续分析。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzFsIq9Vl9y1qSoWdrZ9PQmYC4KsKjzQjXMZ8mFxd4uvSW13wiaiaRyH6Q/640?wx_fmt=png&from=appmsg)

**支配：**在控制流图（CFG）中，如果从入口节点到达基本块 N 的所有路径都必须经过基本块 M，则称 M 支配 N，记作 M dom N

**DF****N序：**在深度优先搜索（DFS）生成树中，节点的访问顺序被称为 DFN 序。根据 DFN 序的定义，如果 dfn(A)<dfn(B)，则在生成树上，节点 A 是节点 B 的祖先。

**后退边：**在对程序的 CFG 进行 DFS 时，生成的 DFS 树中，如果存在一条边 A->B，且 B 是 A 的祖先，则称该边为后退边。

**回边：**如果有一条边 A->B，且 B dom A，则称该边为回边。回边一定是后退边，但后退边不一定是回边。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzmsj04FkGnew0s5icN7xq1wYhFMAmFiaibo63f8AVHvg9vPcxwwrkAH4qQ/640?wx_fmt=png&from=appmsg)

对于Java代码，执行顺序是自上而下，如果将每一条语句视为执行单元，那也就不存在回边，java语句中可能导致回边的语句有循环语句、break、continue语句。

根据推论：**如果程序中不存在从循环外跳到循环内的goto语句，那么这个程序的控制流图就是可规约的。**可以得出，Java的控制流图是可规约的，而对于可规约图，回边集合和后退边集合相同。由此可以推理得到：

**如果存在一条边 A->B，且dfn(B)<dfn(A)，那么这条边就是回边。**

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzTEDAEUYs6vqD0sSkRLrlkwl99uh32ia9t4q6pF4yJibmC8RAyG2CVbXQ/640?wx_fmt=png&from=appmsg)

由于Java的CFG是可规约的，所以图中的循环也一定是自然循环。**所有循环都至少具有一条回边**，回边的目标节点就是循环头。所以只要找出所有回边就可以分析出相应的循环语句。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzH5jG1CkgWsyWe3uq0oo8RicMhWcCDu81N3iaibxzviaV6VemddyIyzMYFg/640?wx_fmt=png&from=appmsg)

**直接支配节点：**在控制流图中，节点 A 支配的除自身外最近的节点称为 A 的直接支配节点，通常记作 idom(A)。

通过直接配置节点构建出来的树就是支配树。

上述两个案例的支配树如下：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzHyMyCUwLJfmPmfqg0xibMvGzfa7hcJFjHpwjG2UrDX7NMF2whPcYGJw/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzqUOFgqtCOlYdGIhOlibtY6ohYVTaSczCa43xZxYAsibN0EnBrzAShjHg/640?wx_fmt=png&from=appmsg)

支配树可以展现出程序的所有代码执行路径和支配关系，清晰看出程序结构，便于后续分析。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDztUibgEdZzzLx2aQUH96l27Z7YlmsYGFibEKYibAZ8CVdDb85xJb5ZQiawQ/640?wx_fmt=png&from=appmsg)

反编译过程中首要目标是将字节码解析恢复为等价的源码，对于一些表达式的简化，语法糖的优化可以放到后面处理。那主要任务就是将CFG规约为一条线性的链表形式。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzCkx8ot1bDpwaMHvfCz27xXKjVZFORPJDicVchnF9yUJaaYOu9M9FzWQ/640?wx_fmt=png&from=appmsg)

一个class 的构成包括：class的描述、成员、函数。其中的函数的code属性就是函数体编译后的字节码。反编译过程主要任务就是解析函数的code属性。

code属性解析出来后是一个线性的指令列表、每个元素就是指令+操作数，如

```
```
0: aload_01: invokespecial #1                  // Method java/lang/Object."<init>":()V4: aload_05: new           #2                  // class java/lang/Object8: dup9: invokespecial #1                  // Method java/lang/Object."<init>":()V12: putfield      #3                  // Field lock:Ljava/lang/Object;15: return
```
```

JVM是基于栈基实现的，所以在运行时存在一个操作数栈，用于储存临时数据。例如计算a=1+1的字节码：

```
0: iconst_1 // 将1存到操作数栈1: iconst_1 // 将1存到操作数栈2: iadd // 从栈中取出两个integer类型值，进行加法运算后将结果push到栈3: istore_1 // 从栈中取出值存到局部变量表中
```

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzlMAWvrZibFcL1gWIourhRlZDSoHjWEiaDajYqwicNYL2FVCSUibL38eh9w/640?wx_fmt=png&from=appmsg)

在jvm执行时，会为每个栈帧开辟一个操作数栈和局部变量表。这个变量表是一个线性列表，可以通过索引访问，这个变量表是忽略变量类型的。

如0号槽位可以存引用，也可以存int类型变量。在jvm执行时不存在作用域的概念，可以理解为所有变量在同一作用域。

对变量a赋值等价于存到变量表n号位，对变量a取值等价于从n号位取值。对于生命周期结束的变量，变量表会用新变量直接覆盖。由此可以推出，局部变量表中的变量与存活的变量是一一对应的。

### **恢复类型**

由于字节码不存在声明指令，需要推理变量声明操作，可以通过下面算法找出声明操作集合：

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzJVq3BeSHeDLYNmZbWKAicm23Cy2iaRQfsahJuwVicyVNyFoLvOhJjhEmQ/640?wx_fmt=png&from=appmsg)

### **恢复变量名**

按照声明顺序将变量名设置为var0、var1......

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDz08ZknxBmOrGLT5fNS6mef0gcZYeV6YZTvKFzeMT2eDicLSkWO2PDmyg/640?wx_fmt=png&from=appmsg)

下面是一段if语句的字节码

```
```
79: iload         981: ifeq          9484: getstatic     #8                  // Field java/lang/System.out:Ljava/io/PrintStream;87: iconst_188: invokevirtual #9                  // Method java/io/PrintStream.println:(I)V91: goto          10194: getstatic     #8                  // Field java/lang/System.out:Ljava/io/PrintStream;97: iconst_298: invokevirtual #9                  // Method java/io/PrintStream.println:(I)V101: return
```
```

ifeq是条件跳转语句,goto是跳转语句，对于jvm在运行时直接跳转到相应代码执行。仔细读一下代码可以勉强理解：加载一个变量，如果它的值是true那就执行94号之后的代码，否则执行84号之后的代码，到91号时再跳转到101号，画个图直观看一下

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzag9f3sic1vEicIlPRR5Acy9ZKbvOaefYZSTjtfopetrpg8HYbuPWMG3g/640?wx_fmt=png&from=appmsg)

翻译成现代编程语言应该是这样

```
```
if var0 {    getstatic    iconst_1    ...}else{    getstatic    iconst_2    invokevirtual}return
```
```

反编译过程就是将这个思路转换为代码，大概流程是通过代码语言对字节码列表进行约束，如：

* 存在if指令
* if指令下存在goto指令p1跳转到p2
* if指令跳转到目标地址为p3，那么p3小于等于p2

符合上述条件的语句就可以翻译为if语句，其中if指令到p1之间为if body，p3到p2之间是else body。

但这种方案抗干扰性比较弱，需要较多的限制条件，如当存在break、continue语句时，还需要特殊处理。

另一种方案是基于图2进行描述：

* 存在if指令
* if节点有两个后继基本块
* 两个后继基本块具有汇合点

对于下面这种不存在else body的情况，也同样可以描述

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDz8iaSlIgkMqC9CeBKOl4J53c9s8KdMf0QpmiaIvicFaiaZ1sK9dJRzKkYOQ/640?wx_fmt=png&from=appmsg)

第二种描述方法显然描述的更准确，且更抗干扰。所以后面实现都是基于图的。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDz2LLfrD6ZQicdC72rUNv81QEO8GeJapZ7C04NG5dh8s6ZCgJpcVsatHg/640?wx_fmt=png&from=appmsg)

java字节码的入口就是字节码序列的第一条指令，而出口是return指令，但return指令可以有多个，导致结束节点不统一。所以为了方便分析，可以添加一条虚拟指令end，让所有return指令指向end指令。

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDzYBAOVe6wGEqdwWHquibsiaNS9vzr8UJmLOdJO34ebdwhlWcvZTGfibuEw/640?wx_fmt=png&from=appmsg)

本篇作为Java反编译系列的开篇，介绍了一些背景知识和实现思路，明确了后面对于变量、控制流的分析方法。后面会更新针对每种语句的具体分析方法。

**END**

**Yakit使用小tips**

**Yaklang函数用法**可至**YakRunner帮助文档**查询⬇️

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcCDzMhyf5yRXVicEvEibKnDz6PH9JialshvhVdKgYbPNTFciaib9lpK0P4DTK2ib6XPeyKZqE8rBgIm2jw/640?wx_fmt=png&from=appmsg)

**YAK官方资源**

Yak 语言官方教程：
*https://yaklang.com/docs/intro/*
Yakit 视频教程：
*https://space.bilibili.com/437503777*
Github下载地址：
*https://github.com/yaklang/yakit*
Yakit官网下载地址：
*https://yaklang.com/*
Yakit安装文档：
*https://yaklang.com/products/download\_and\_install*
Yakit使用文档：
*https://yaklang.com/products/intro/*
常见问题速查：
*https://yaklang.com/products/FAQ*

![](https://mmbiz.qpic.cn/mmbiz_png/f7AtEgJhMZcGEibOlRNlz6ZPic3cWicMDwdqZLq9q0hibDYiaICia6nncspoDTRnjPXFGTr3VWd9FlV4YSXRStoabxbg/640?wx_fmt=png&from=appmsg)

![](https://mmbiz.qpic.cn/mmbiz_gif/f7AtEgJhMZeX0EdicJxBOjGjQuecg0TvCvRgqibPwyOUp8untXs9Cl5XKux2yQQf27ibgZ0ic0Fm2yicdbYg6c4xUJg/640?wx_fmt=gif&from=appmsg)

预览时标签不可点

![]()

微信扫一扫
关注该公众...