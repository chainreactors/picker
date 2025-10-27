---
title: PHP 静态分析漏洞挖掘：挑战、对策与研究进展综述
url: https://forum.butian.net/share/4308
source: 奇安信攻防社区
date: 2025-05-09
fetch_date: 2025-10-06T22:26:21.282950
---

# PHP 静态分析漏洞挖掘：挑战、对策与研究进展综述

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

### PHP 静态分析漏洞挖掘：挑战、对策与研究进展综述

* [安全工具](https://forum.butian.net/topic/53)

主要关注学术界使用SAST（Static Application Security Testing，静态应用安全测试）对PHP应用进行漏洞挖掘的一些研究，希望能够回答“在使用静态分析对PHP应用进行漏洞挖掘时，会面临哪些挑战以及对应的解决方案”。

静态应用安全测试 SAST（Static Application Security Testing）是指基于静态分析技术，在无需实际运行程序的情况下分析代码的语义和行为，找出潜在的漏洞从而保障软件的安全。本文关注过去学术界使用SAST针对PHP应用进行漏洞挖掘的研究，总结了其中遇到的主要挑战和相应的解决方法。
因为最早是在国外读书时的一个作业，有些段落原文用英文写的，读起来可能有点机翻味。
1.过程间污点分析
=========
污点分析旨在检查污点数据在程序中的传播路径，判断是否存在从 source 到sink 且未经 sanitizer 处理的数据流。这里我们将PHP的过程间污点分析（显然过程内的的污点分析不够实用）的实现方法分为两类：自顶向下方法(The Top-Down Approach)与自底向上方法(The Bottom-Up Approach)。本节暂时忽略对面向对象以及动态特性的处理，它们将专门在第2节和第3节讨论。
1.1 自顶向下方法
----------
自顶向下方法从程序的入口点出发，当遇到函数调用时，通过传递参数和全局变量的抽象值，递归地分析其调用的每个函数。这是传统基于格(Lattice Based) 的数据流分析的常用策略。
Pixy\[1\], \[2\], \[3\]是采用此方法的典型代表。它首先通过基于不动点迭代的过程间的到达定义分析（Reaching Definition Analysis）(其源码中也称为Dependency Analysis)，随后检查哪些定义能够最终到达 sink。Pixy 实现了 Sharir 和 Pnueli \[4\]提出的两种经典上下文敏感 (Context Sensitivity)实现策略：调用串 (call-string) 方法和函数式 (functional) 方法。调用串方法依据调用栈信息（即调用点序列）来区分同一函数的不同调用场景。为应对递归并避免调用链无限增长，通常会为上下文设置一个长度限制 \*k\*。下面的代码就展示了当 \*k=1\* 时，Pixy 的污点分析可能出现误报的情况：由于只追踪了最后一个调用点，对 `bar` 的两次调用被识别为同一上下文，导致第一次调用返回的污点值也传播给了第二次调用的返回值，从而错误地污染了`$x2`。
```php
<?php
// Pixy 中长度为 1 的调用串会引发一个误报
$y1 = $\_GET['x'];
$x1 = foo($y1);
$y2 = 'good';
$x2 = foo($y2);
echo $x2;
function foo($y)
{
return bar($y);
}
function bar($y) {
return $y;
}
```
与之相对，函数式方法则依据传入参数和全局变量的抽象值来区分上下文，从而实现更精确的分析。若某次函数调用的抽象值与先前某次调用完全一致，便可直接复用那次调用的分析结果（返回值）。在上面的例子里，由于每次调用 `foo` 和 `bar`时传入的参数和全局变量的抽象值都不同，因此这两个函数均需被分析两次。该方法的主要不足在于，生成的函数摘要（Function Summary）可能较难复用，容易导致上下文数量爆炸式增长。即使参数或全局变量的变化并不影响最终返回值，函数也可能被反复分析。Pixy在实验阶段就曾遇到此问题：在分析 MyBloggie项目时，函数式方法产生了过于复杂的上下文。为缓解该问题，他们转而尝试了长度为1的调用串方法。
TChecker等其他工具也采用了类似的自顶向下过程间污点分析思路\[5\]。其改进之处包括：当一个调用点可能对应多个目标函数时，采用启发式规则进行选择；忽略那些参数均未被污染的函数调用。目前我们还没有看到函数式方法的一种变体IFDS（Interprocedural Finite Distributive Subset Problem）\[6\]被用于PHP应用的污点分析。理论上讲，IFDS 相比现有自顶向下方法能够在不降低精度的前提下，带来更高的分析效率。
1.2 自底向上方法
----------
自底向上分析则从程序的叶子函数入手，逐步向上分析，并为每个函数生成可供更广泛重用的摘要信息。尽管为单个函数构建能涵盖所有可能调用场景的摘要成本较高，但一旦生成，这些摘要就非常易于复用\[7\]，且整个构建过程也易于并行化\[8\]。
PHPJoern\[9\]采用了自底向上的过程间污点分析策略。它首先构建代码属性图CPG（Code Property Graph），该图融合了抽象语法树 AST（Abstract Syntax Tree）、控制流图 CFG（Control Flow Graph）、程序依赖图 PDG（Program Dependence Graph） 以及调用图 CG（Call Graph）。其中 PDG 包含了每个过程内部的数据依赖图 DDG（Data Dependence Graph） 和控制依赖图 CDG（Control Dependence Graph）。DDG 由过程内的到达定义分析生成，并且会保守地处理函数调用。在下面的代码示例中，入口函数的DDG 会包含一条从 `$c` 到 `$e` 的、实际并不存在的数据依赖边。随后，PHPJoern 从 sink 出发，沿着数据依赖边和调用图边进行反向污点分析，从而能够排除掉如 `$c` 到 `$e` 这样的错误数据流。每个函数的 DDG 可以视为其函数摘要。这种方法的潜在缺点是可能存在一定冗余：即使某些函数从未被实际调用，在构建 CPG 的过程中也仍会被分析。但这与 Joern 的定位有关，它更像是一个基础性的代码分析框架，而非直接面向用户的 SAST 工具。
```php
<?php
function foo($a2,$b2) {
echo $a2;
return $b2."suffix";
}
function bar($c2) {
return "nothing";
}
$a = $\_GET['a'];
$b = $\_GET['b'];
$c = $\_GET['c'];
$d = foo($a, $b);
$e = bar($c);
echo $d;
echo $e;
```
Xie 和 Aiken\[10\]提出了一种混合分析方法，它融合了自顶向下（用于摘要构建）与自底向上（用于反向污点分析）的元素。Dahse和Holz在 RIPS\[11\]中扩展了这一思路。下面介绍 RIPS 的实现：
RIPS运用了两种摘要：块摘要和函数摘要。块摘要负责记录其对应基本块内的数据流信息，而函数摘要则由该函数内部所有块摘要组合而成。RIPS 从入口函数开始构建 CFG，在构建每个基本块的同时，也生成对应的块摘要。例如，对于语句 `$a = $\_GET['a'];`，会生成类似如下的块摘要：
```php
{
Dataflow: {
$a: ArrayDimFetch($\_GET,"a")
}
// 摘要其余部分暂略
}
```
当遇到一个对未被分析的函数的调用时（比如`$d = foo($a, $b);`），RIPS 会先为 `foo` 函数构建 CFG 和函数摘要，此时并不考虑传入的具体参数值。在分析到`foo`内部的sink `echo $a2`时，RIPS 会执行一次过程内的反向污点分析。这里的`$a2`来自于函数参数，需要考虑具体的调用才能知道是否形成了漏洞，因此它将被记录在`foo`的函数摘要中的 \*sensitiveParams\* 属性里。同时，函数摘要中的 \*returnValues\* 属性则会记录返回值的符号值。下面是 `foo` 函数摘要的一个示例：
```php
{
sensitiveParams: [
$a2
],
returnValues: Concat($b2, "suffix")
}
```
> RIPS会忽略掉CFG中循环造成的回边，因此生成函数摘要时不需要不动点迭代，但会造成一定的漏报。Xie 和 Aiken则明确提到了他们使用不动点迭代来生成函数摘要。
`foo` 的摘要构建完毕后将处理`$d = foo($a, $b);`，RIPS 会利用 `foo` 摘要中的 \*sensitiveParams\* 信息，对变量 `$a` 发起反向污点追踪。这次追踪能够成功找到污点 source `$\_GET['a']`，从而确认漏洞的存在。而 `$d` 的符号值则可以通过查询 `foo` 摘要的 \*returnValues\*，并将 `$b` 的符号值代入其中的`$b2` 来获得。之后若再次遇到对 `foo` 函数的调用，则能够直接复用已生成的摘要，避免重复的分析。
> RIPS 的开源版本相较于其研究论文中描述的实现有所简化，没有显式构建 CFG 和摘要，但其核心分析思路是类似的。
这种混合分析方法虽然整体上以自顶向下方法为主导，但也融入了自底向上的思想，从而在提升摘要的复用率和减少对死代码的冗余分析之间取得了更好的平衡。
2.面向对象
======
支持 PHP 的面向对象特性对于有效的 PHP 静态分析至关重要。对于过程间分析，必须获取对象类型才能分析出方法调用的目标方法，从而构建完整的调用图。与 Java 等语言不同，PHP 中的对象没有声明类型（虽然PHP 7.4+ 为属性和方法参数/返回类型引入了部分类型声明），这使得像 CHA（Class Hierarchy Analysis）这样简单的方法无法使用。此外，在污点分析和其他数据流分析中需要域敏感性（Field Sensitivity）以提高精度。我们将分别介绍基于指针分析（Pointer Analysis）和变量类型分析 VTA（Variable Type Analysis）来支持 PHP 面向对象特征的方法。
```php
<?php
class Container {
public $dependency;
}
class Sink {
private $dataToEcho;
public function setData($data) {
$this->dataToEcho = $data;
}
public function execute() {
echo $this->dataToEcho;
}
}
class FakeSink {
// This method will not be called.
public function execute() {
echo $\_GET['y'];
}
}
function triggerVulnerability($object) {
$object->execute(); // RIPS-A can't infer the type of $object here.
}
$container = new Container();
$container->dependency = new FakeSink(); // Initially set to a safe object.
$alias = $container; // Alias.
$alias->dependency = new Sink(); // Now it contains the vulnerable object (Sink).
$userInput = $\_GET['x'];
$container->dependency->setData($userInput);
$container->dependency->execute(); // Vuln 1
triggerVulnerability($alias->dependency); // Vuln 2
```
2.1 指针分析
--------
指针分析用于静态计算程序中变量在运行时可能指向的对象集合\[12\]。Dahse 等人在RIPS的拓展版本（TChecker\[5\]论文中称为 RIPS-A）中使用指针分析来支持 PHP 的 OOP 分析\[13\]。该版本的RIPS主要用于检测PHP的反序列化利用链，但也可以用于检测其他污点式漏洞。他们的方法是对上一节中描述的 RIPS 分析方法的拓展。
具体来说，他们在摘要中添加了新的符号 \*Object\*、\*PropertyFetch\* 和 \*PropertyWrite\* 以实现堆抽象和域敏感。在上面的例子中，入口函数前 4 行的模拟将导致块摘要包含：
```php
{
Dataflow: {
$container -> Object1,
$alias -> Object1
},
Object: [
Object(type: Container, properties: {
dependency -> Object3
}),
Object(type: FakeSink, properties: {}),
Object(type: Sink, properties: {})
]
}
```
和上一节介绍的类似，RIPS在生成方法摘要时并不考虑具体的调用。因此对参数，全局变量或者 `$this` 的属性进行访问时并不知道此时的接受者对象（Receiver Object）是哪一个，此时就需要使用到 \*PropertyWrite\* 和 \*PropertyFetch\*。比如在创建`Sink::setData`方法摘要时将生成：
```php
{
PropWrite: [
PropertyWrite($this, dataToEcho, $data)
]
}
```
之后对 `$container->dependency->setData($userInput);` 的处理将根据 \*PropWrite\* 缓存将`$userInput` 写入到 `$container->dependency` 指向的对象。类似地，`Sink::execute` 的方法摘要将使 `PropertyFetch`来表示对 `$this->dataToEcho` 的访问，并将其存储在 \*sensitiveParams\* 属性中。在分析到`$container->dependency->execute()`时将触发反向污点分析，此时将检查 `$container->dependency` 对象的 `dataToEcho`属性是否可由用户控制，从而检测到第一个漏洞。
不过 RIPS-A 仅仅实现了过程内的污点分析。在创建`triggerVulnerability` 方法摘要时`$object->execute();` 中 `$object` 类型是未知的。因此，`Sink::execute` 和 `FakeSink::execute` 都被认为是潜在的被调用者，导致它们的摘要被合并，造成误报。
RIPS-A 还支持了 PHP 的魔术方法特性，在实现堆抽象后这并不难实现。
2.2 对象类型分析
----------
TChecker\[5\]使用了一种基于类型而不是基于堆抽象的方式来支持PHP的面向对象。这种方法相对来说更加轻量级。它的分析分为调用图构建和污点分析两个阶段。在调用图构建阶段使用了过程间的对象类型分析\[14\]来获取对象的类型从而构建精确的调用图。这种方法与指针分析的区别在于没用进行堆抽象，仅仅依靠反向查找`new`关键字来确定对象的类型。理论上讲TChecker能够没有误报处理`triggerVulnerability`中`$object->execute();`的调用边，但会因为没有堆抽象无法正确添加`$container->dependency->execute();`的调用边。反向追踪`$container->dependency`的`new`初始化会将其类型视为`FakeSink`。
此外，TChecker 还使用了一种启发式规则来推断对象属性的类型，以此弥补缺乏完整堆抽象带来的限制。在下面的例子中，TChecker在分析 `$ev = $o->config;` 时无法直接通过反向分析追踪到 `$o->config` 的初始化位置。因为缺乏堆抽象，TChecker 无法精确跟踪 `$o` 指向的具体对象实例，也无法将外部变量 `$o` 与类方法（这里是构造函数）内部的 `$this` 进行关联，因此它无法直接判断出 `$this->config = new ConfigData();` 是对`$o->config`的赋值。为了解决这个问题，TChecker 对于 `$o->config` 这种对象属性的访问采用了一种启发式方法：
- 首先通过反向分析确定父对象 `$o` 的类型是 `AppContainer`
- 检查 `AppContainer` 类定义，确认：
- 是否存在 `config` 属性
- 该属性是否在类中（通常在方法如 `\_\_construct` 内）通过 `new` 表达式进行过赋值。
若...