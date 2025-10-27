---
title: Chrome V8 issue 1486342浅析
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458562487&idx=2&sn=b2d6ad2776d37f416933e1439f244430&chksm=b18d9f3d86fa162b5edfd1c8e616c9ea5460cf21afc5d41cfd8122fbc73830c61f125c8a4960&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-07
fetch_date: 2025-10-06T17:41:37.556675
---

# Chrome V8 issue 1486342浅析

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GZzGxZaAxFIdoJxv7yscBMeq13yqUjAIPXz3yAl3VicfvqU2JylH38Bkd4XAa5kibuzqX7M9X2RRzA/0?wx_fmt=jpeg)

# Chrome V8 issue 1486342浅析

coolboyme

看雪学苑

```
一

前言
```

首先，这是一个issue，不是一个漏洞。但不排除它可能可以被利用，通过issue（https://issues.chromium.org/issues/40282853）修复者的邮件回复可以印证这一观点。虽然它不是一个漏洞，但弄清它的前因后果，对理解turbofan的sea of nodes以及编译过程有极大的帮助，进一步有助于代码审计去发现新的漏洞、维护v8及各类浏览器的安全。接下来我将从这个思路出发，陆续分析多个issue，加深对v8的理解，以期发现新的安全问题。

这是一个系列文章，本文是第五篇。

◆第一篇：chrome v8漏洞CVE-2021-30632浅析（https://www.freebuf.com/vuls/394933.html）

◆第二篇：chrome v8漏洞CVE-2021-37975浅析（https://www.freebuf.com/vuls/400324.html）

◆第三篇：chrome v8漏洞CVE-2023-3420浅析（https://www.freebuf.com/vuls/401044.html）

◆第四篇：chrome v8漏洞CVE-2020-16040浅析（https://www.freebuf.com/vuls/402175.html）

```
二

正文
```

# POC

##

## 编译v8

```
# 推荐香港服务器，可以避免网络问题导致的编译失败。
git clone https://chromium.googlesource.com/chromium/tools/depot_tools.git
export PATH=/path/to/depot_tools:$PATH

mkdir ~/v8
cd ~/v8
fetch v8
cd v8

# 补丁前一笔提交
git checkout 24861cbefe4
gclient sync
alias gm=~/v8/tools/dev/gm.py
gm x64.release
gm x64.debug

# test
./out/x64.release/d8 --help
```

##

## 运行POC

```
// test.js
const o13 = {
  "maxByteLength": 5368789,
};
const v14 = new ArrayBuffer(129, o13);
const v16 = new Uint16Array(v14);

function f3(param) {
  for (let i = 0; i < 5; i++) {
    try {"resize".includes(v14); } catch (e) {}
    v14.resize(3.0, ..."resize", ...v16);
  }

  let f = function() { return param; }
}

%PrepareFunctionForOptimization(f3);
f3();
%OptimizeFunctionOnNextCall(f3);
f3();
// 运行./out/x64.deubg/d8 --allow-natives-syntax test.js，将会得到崩溃堆栈
```

#

#

```
三

背景
```

##

## sea of nodes

什么是sea of nodes？

1.Turbofan用它来表示js程序。

2.它由节点和边组成。一个节点代表一个compute。一条边代表control、value或者effect。
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GZzGxZaAxFIdoJxv7yscBMRntPqrMKU6suwKdVibf78ANyW0nb4iaK7S8uBNpjeKKbgKxE9gZRc9icA/640?wx_fmt=jpeg&from=appmsg)

◆compute可以表示：常量、参数、运算符、内存操作、函数调用等。

◆control表示控制流。

◆value表示值依赖，如图"+"这个compute值依赖"x"和"3"compute。

◆effect表示内存操作的先后依赖顺序。比如"i++"涉及load和store操作，store操作effect依赖于load操作，即：先执行load，然后执行+1，最后再执行store操作。

1. sea of nodes包含了CFG骨架，但不仅仅是CFG。

2.节点可以有若干输入和输出，输入和输出均为边。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GZzGxZaAxFIdoJxv7yscBMQZibPnTuSm701FsREXLntkgicckzbENsB9MHlibPjTVciapyDINmziabP2Q/640?wx_fmt=jpeg&from=appmsg)

◆上图为函数 function get\_number(x) { return x > 0 ? 1 : 0;} 的sea of nodes。

◆return有4个输入依赖，分别为：
a. NumberConstant\_0节点：value依赖。表示return的第一个固定参数，含义暂时不介绍。
b. Phi节点：value依赖。表示返回的值。Phi节点表示一个未决的值，这里是0或者1。
c. SpeculativeNumberLessThan节点：effect依赖。表示return的内存操作需要在SpeculativeNumberLessThan之后执行，SpeculativeNumberLessThan表示x和0的大小判断操作。
d. Merge节点：control依赖。表示return的执行需要在Merge之后。Merge节点表示iftrue和iffalse分支节点的结合处。

◆return 有1个输出，为control边。它是End节点的control输入。表示return执行完之后，就执行End。

1.turbofan的编译是基于节点的。根据节点及其输入输出，结合编译优化策略，对节点及其输入输出进行调整和替换，从而实现了编译。

2.编译优化分为下面几个阶段，每个阶段又涉及不同的编译优化选项。其本质就是对节点组成的图(sea of nodes)进行修改。

◆TurboFan各个编译阶段

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GZzGxZaAxFIdoJxv7yscBMHkRxJfOmuzjd6q490v1bY6RqZ2cZXrPRJZJVXnqYelBKAmwYKKPZOg/640?wx_fmt=jpeg&from=appmsg)

◆Inlining阶段的各个优化选项，见pipeline.cc

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GZzGxZaAxFIdoJxv7yscBMFLcIfDcOBet1BFmM7p1icfvhavM5mOOCylXyeicuPIalSeagWJUUj41g/640?wx_fmt=jpeg&from=appmsg)

1.查看sea of nodes

```
function get_number(x) {
    return x > 0 ? 1 : 0;
}
// 多次执行get_number，触发优化
for (var i = 0; i < 20000; i++) {
    get_number(3);
}

get_number(3);
/*
    ./out/x64.deubg/d8 --allow-natives-syntax --trace-turbo test.js
    --trace-turbo 将生成turbo-get_number-1.json文件， v8提供了一个在线查看工具：https://v8.github.io/tools/head/turbolizer/index.html，加载turbo-get_number-1.json 可以查看sea of nodes
*/
```

##

## 结合源码理解TurboFan编译过程

以函数get\_number为例，来观察turbofan Inlining阶段 CommonOperatorReducer优化策略。

```
function get_number(x) {
    return x > 0 ? 1 : 0;
}
```

优化前它的sea of nodes图如下：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GZzGxZaAxFIdoJxv7yscBMLCpl8p00Iq8QdK6AJkXvRH09EuDarXcdYbJKDlqlZlkPYTicMHgHicDA/640?wx_fmt=jpeg&from=appmsg)

优化后如下：
![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GZzGxZaAxFIdoJxv7yscBMuicMyjtlSSU8fE1seEgmEBicUgUv3QKJqrKzXiaBCuD9hn7NxRUcU9zMg/640?wx_fmt=jpeg&from=appmsg)

对比优化前后，可以发现是将merge节点(21, 25)删除，将return(27)删除。新建两个return节点(32,33)，分别采用ifture和iffalse的输出作为control输入，同时输出control边到end。接下来看代码。

```
// common-operator-reducer.cc
// ReduceReturn 优化return 节点
Reduction CommonOperatorReducer::ReduceReturn(Node* node) {
  ...
  // return节点的effect输入
  Node* effect = NodeProperties::GetEffectInput(node);
  // return节点的第一个value输入
  Node* pop_count = NodeProperties::GetValueInput(node, 0);
  // return节点的第二个value输入，get_number函数里它为phi(1|0)
  Node* value = NodeProperties::GetValueInput(node, 1);
  // control输入
  Node* control = NodeProperties::GetControlInput(node);
  if (value->opcode() == IrOpcode::kPhi &&
      NodeProperties::GetControlInput(value) == control &&
      control->opcode() == IrOpcode::kMerge) {
    /* 3个条件均满足，参考sea of nodes图
    1. value类型为phi
    2. value的control输入 跟 return的control输入 是同一个节点
    3. control输入是一个merge节点
    */

    // control为merge节点(25)，control_inputs代表了merge节点的两个输入：iftrue, iffalse
    Node::Inputs control_inputs = control->inputs();
    Node::Inputs value_inputs = value->inputs();
    DCHECK_NE(0, control_inputs.count());
    DCHECK_EQ(control_inputs.count(), value_inputs.count() - 1);
    DCHECK_EQ(IrOpcode::kEnd, graph()->end()->opcode());
    DCHECK_NE(0, graph()->end()->InputCount());
    // control作为node和value的输入，满足
    // value作为node的输入，满足
    if (control->OwnedBy(node, value) && value->OwnedBy(node)) {
      // control_inputs: iftrue, iffalse两个分支
      for (int i = 0; i < control_inputs.count(); ++i) {
        // newNode(操作码，pop_count, value_input, effect_input, control_input)
        // newNode函数参数如上，使用newNode创建两个新的return节点
        Node* ret = graph()->NewNode(node->op(), pop_count, value_inputs[i],
                                     effect, control_inputs[i]);
        // 将新建return节点的输出control指向end节点
        MergeControlToEnd(graph(), common(), ret);
      }
      // merge节点丢弃
      Replace(control, dead());
      // 原来的return节点丢弃
      return Replace(dead());
    }
    ...
  }
  return NoChange();
}
```

结合sea of nodes图，看上述代码注释，可以更加清晰的了解。

```
四

issue分析
```

先来看issue的patch，它位于src/compiler/js-call-reducer.cc文件ReduceArrayIterator函数，属于Inlining阶段call\_reducer优化选项，当出现数组迭代器指令的时候，对这个内置函数进行优化。

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8GZzGxZaAxFIdoJxv7yscBMJTWkywNfQUY4ll3rOYg1UWHRBdoQefQticjicoqfMU7mzAZ5UsHURqHA/640?wx_fmt=jpeg&from=appmsg)

patch逻辑很简单，把RelaxControls(node);替换成ReplaceWithValue(node, node, node, control);
RelaxControls代码如下：

```
void RelaxControls(Node* node) {
    ReplaceWithValue(node, node, node, nullptr);
  }
  /*
    也就是说patch是将
    ReplaceWithValue(node, node, node, nullptr);
    替换成
    ReplaceWithValue(node, node, node, control);
  */
```

我们再来看看ReplaceWithValue函数，它的代码如下：

```
void ReplaceWithValue(Node* node, Node* value, Node* effect = nullptr,
                        Node* control = nullptr) {
    DCHECK_NOT_NULL(editor_);
    editor_->ReplaceWithValue(node, value, effect, control);
  }
```

这个函数的作用是修正node输出的边。参数分别node本身，node的value输出、effect输出、control输出。当effect或者control传递nullptr的时候，将不会发生替换。假设node A和node B存在control的边，这条边为node A的输出，B的输入。

此时执行ReplaceWithValue(nodeA, nodeA, nodeA, nodeC)，那么A的输出将不再为B的输入，而nodeC和nodeB之间将建立边，为C的输出，B的输入。

再回过头去看补丁，补丁前的代码将node的输出设置为空(即不变)，而应该是control。结合补丁前面的代码查看：

```
Reduction JSCallReducer::ReduceArrayIterator(Node* node,
                                             ArrayIteratorKind array_kind,
                                             IterationKind iteration_kind) {
  ...
  if (array_kind == ArrayIteratorKind::kTypedArray) {
    // Make sure we deopt when the JSArrayBuffer is detached.
    if (!dependencies()->DependOnArrayBufferDetachingProtector()) {
      CallParameters const& p = CallParametersOf(node->op());
      if (p.speculation_mode() == SpeculationMode::kDisallowSpeculation) {
        retur...