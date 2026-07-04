---
title: Chrome V8 沙箱逃逸漏洞
url: https://mp.weixin.qq.com/s/6vjFIzy6jTw66xoRmcispg
source: Doonsec's feed
date: 2026-07-03
fetch_date: 2026-07-04T05:46:24.499437
---

# Chrome V8 沙箱逃逸漏洞

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/7xtecWUgCRyvkr6FbspwcMV481fs1KO7NuYSvVQL3zic9DAA1Ol9iaPdLKcgF2wqZzAfQk3j8QuhHib6hBRB0erHgr4XBKprLwIfribOMicPaIQY/0?wx_fmt=jpeg)

# Chrome V8 沙箱逃逸漏洞

迪哥讲事

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

以下文章来源于骨哥说事
，作者骨哥说事

![](http://wx.qlogo.cn/mmhead/Tjnia6K0WAwymfmKQ4Vxu2yovHNIGmF3wZKN9Peic0bS16wzb8MQuwUX7HuGjlMO3NmmvxOcHnjSM/0)

**骨哥说事**
.

一个喜爱鼓捣的技术宅

|  |
| --- |
| ****声明：****文章中涉及的程序(方法)可能带有攻击性，仅供安全研究与教学之用，读者将其信息做其他用途，由用户承担全部法律及连带责任，文章作者不承担任何法律及连带责任。 |

#

#

# **防走失：****https://gugesay.com/**

**不想错过任何消息？设置星标****↓ ↓ ↓**

#

觉得内容太技术？可以先快速浏览我们的漏洞摘要。

阅读漏洞摘要 → https://nebusec.ai/buglist/CVE-2026-6307/

> Chrome V8 JavaScript 引擎配备了一个堆沙箱，旨在防止攻击者仅凭 JavaScript 引擎中的漏洞就在沙箱区域外进行写入。然而，Vega 在 JIT 编译器中发现了一个特殊的漏洞，允许攻击者仅凭此漏洞就在沙箱内获得任意读写原语，甚至能够逃离沙箱，向沙箱外写入。本报告将详细介绍该漏洞的技术细节。

## 概要

这个 V8 漏洞单凭自身就能实现以下所有目标：

* 以 100% 的成功率获取任意内存读写原语，无需任何内存布局技巧
* 仅凭此漏洞，无需其他漏洞辅助，即可实现 V8 堆沙箱逃逸和远程代码执行
* 影响从 Chrome 106 开始的版本，横跨 4 年时间

## 背景

为了理解这个漏洞，我们首先需要了解 TurboFan、它如何内联 JS-to-Wasm（JavaScript 到 WebAssembly）调用，以及其去优化元数据是如何决定在延迟去优化后应重建何种类型的值的。此外，我们还需要理解 V8 堆沙箱的工作原理，以及为什么这个单一漏洞能让攻击者同时做到两件事：1）在沙箱内获得任意读写原语；2）逃离沙箱，向沙箱外写入。

### TurboFan

TurboFan 是 V8 的优化编译器。当一个 JavaScript 函数运行足够多次后，V8 可以使用较低执行层级收集到的反馈来编译该函数的一个专门化版本。这些反馈包括诸如对象的形状、调用点观察到的目标，以及特定操作所使用的值的表示形式等信息。

V8 最初通过 Ignition 字节码执行一个函数，在 TurboFan 编译它之前，可能会通过其他层级。这些早期的执行过程填充了函数的反馈向量。TurboFan 将字节码和反馈转换为编译器图，应用高级 JavaScript 优化，并最终将图降低到机器操作层面。Turboshaft 是这个过程中使用的低级编译器表示形式，也是此漏洞涉及的值编号行为发生的地方。

从高层次看，TurboFan 的工作是：用专门的机器代码替换通用的 JavaScript 执行，同时保留返回正确通用执行的方式。它可以内联被调用者，专门化属性访问，并发出检查来守卫它基于反馈所做的假设。如果这些假设中的任何一个在之后被推翻，优化后的执行必须执行**去优化**。

#### 节点图 (Sea of Nodes)

TurboFan 将被编译的函数表示为一个图，通常被称为节点图。图不是简单的线性指令列表，操作由其依赖关系连接。一个节点可以依赖于值输入、控制输入和效果输入。这使得 TurboFan 可以在保留副作用和控制流所需顺序的同时，移动和简化操作。在传统的控制流图中，编译器会问：这条指令属于哪个基本块，以及它以什么顺序运行？但在节点图中，编译器会问：这个操作依赖于什么，以及它之后可以合法地放置在何处？这种差异很重要，因为节点图避免过早地固定指令的确切位置。例如：

```
function f(x, y, z) {
  let a = x + y;
  let b = y + z;

  if (a > 0) return b * 2;
  else return b * 3;
}
```

在控制流图中，你可能会这样表示：

```
B1:
  a = x + y
  b = y + z
  if a > 0 goto B2 else B3

B2:
  return b * 2

B3:
  return b * 3
```

这里，`b = y + z` 已经被放置在块 B1 中。

而在节点图中，`b = y + z` 只是一个依赖 `y` 和 `z` 的 Add 节点：

```
y     z
 \   /
  Add(b)
```

它不必立即属于某个基本块。之后，编译器可以决定是将其放置在分支之前、某个分支内部、提升它、下沉它、消除它，还是与另一个相同的计算共享它。这是关键优势：更高的优化自由度。节点图尤其适用于：公共子表达式消除、全局值编号、死代码消除、代码移动、边界检查消除。

最后，它将节点图调度到基本块中，将节点降低为机器指令，分配寄存器，移除诸如 Phi 节点等结构，然后发出线性的汇编/机器代码。

对于这个漏洞，重要的一点是：调用、检查和去优化元数据都存在于同一个图中。当 TurboFan 内联一个调用时，被调用者的操作会被插入到调用者的图中。如果内联的操作可能去优化，图中还会包含 `FrameState` 节点，用于描述如果优化执行无法继续时，应如何重建执行状态。

`FrameState` 节点是元数据，但它们仍然是具有输入和选项的图节点。它们不会像算术或内存操作那样执行，但优化过程仍然可以对它们进行推理。在后文中，这一点很重要，因为两个 JS-to-Wasm 延续 `FrameState` 节点对于图优化器来说可能看起来是等价的，尽管它们描述的是不同的 Wasm 返回类型。

#### JS-to-Wasm 调用的内联

与该漏洞相关的一个 TurboFan 优化是 **JS-to-Wasm 调用的内联**。JavaScript 和 WebAssembly 使用不同的调用约定和值表示形式，因此从 JavaScript 到 Wasm 的调用通常需要通过一个 JS-to-Wasm 包装器。该包装器将 JavaScript 参数转换为 Wasm 值，执行 Wasm 调用，并将 Wasm 结果转换回 JavaScript 值。

TurboFan 可以将该包装器内联到优化的 JavaScript 调用者中。这避免了单独的包装器调用，并将参数/结果转换代码暴露给优化器。V8 也可能内联足够小的 Wasm 函数体，但本漏洞并不需要完整的 Wasm 函数体内联，内联包装器就足够了。

在本报告中，JS-to-Wasm 调用是通过 JavaScript 属性访问器到达的。经过充分预热后，TurboFan 可以专门化该属性访问，检查接收者的形状，直接调用已知的访问器目标，并为该目标内联 JS-to-Wasm 包装器。如果同一个 JavaScript 函数看到两个接收者形状，优化后的图可以在一个已编译的函数中包含两个这样的访问器路径。

每个内联的包装器都是基于其 Wasm 函数的规范签名构建的。规范化允许 V8 用共享的签名对象来表示结构上等价的函数类型。签名包含参数和返回类型；因此，它比仅仅记录延续内置函数接收多少个值更为精确。

本漏洞涉及两种返回类型。Wasm 的 `i64` 在 JavaScript 中暴露为 `BigInt`，而 `externref` 是一个标记的 JavaScript 引用。

对于这个签名的 Wasm 函数：

```
(func (result i64))
```

机器返回值是一个原始的 64 位整数。包装器必须将该整数转换为 `BigInt` 才能返回给 JavaScript。对于这个函数：

```
(func (result externref))
```

返回寄存器中的值已经是一个标记的引用，必须按此处理。机器级别的返回位置可能相同，但位表示的含义由 Wasm 签名决定。

重要的细节是：包装器的签名决定了 Wasm 返回的位如何转换回 JavaScript。

### 去优化

去优化将一个**活动的优化栈帧**替换为一个或多个可以在较低层级继续的栈帧。为此，V8 必须恢复非优化函数所期望的状态：其参数、局部变量、上下文、当前字节码位置，以及任何内联的栈帧。

优化代码不一定将这些值保留在原始形式中。一个局部变量可能存储在寄存器中、被折叠为常量，或者被完全移除。因此，编译器在可能离开优化代码的点上附加了去优化元数据。在 TurboFan 和 Turboshaft 中，这种状态是使用 `FrameState` 节点表示的。

一个简化的 `FrameState` 包含：

* 重建栈帧所需的值，例如参数和局部变量。
* 当当前操作被内联到另一个函数中时，其外部的 `FrameState`。
* 一个 `FrameStateInfo`，描述栈帧的类型、其延续点以及函数特定的元数据。

编译器可以嵌套这些状态。如果一个访问器及其 JS-to-Wasm 包装器已经内联到优化的调用者中，那么内部的延续状态会指向外部的 JavaScript 状态。去优化器会遍历该链来重建逻辑调用栈，即使这些调用在优化的机器代码中已经不再作为单独的物理栈帧存在。

去优化可以通过两种相关的方式发生。

* **急切去优化**：当检查失败时立即发生。此时，重建栈帧所需的所有值在去优化点都可用。
* **延迟去优化**：与调用相关联。当另一个函数正在运行时，优化函数可能被标记为需要去优化，但实际转换只会在该调用返回时发生。

延迟去优化需要特别处理调用结果。结果在创建 `FrameState` 时并不存在，因此它不会被列为普通输入。相反，去优化器从机器返回寄存器中获取它，并将其添加到延续栈帧中。然后，执行通过一个延续内置函数恢复，就好像优化调用正常返回一样。

对于由 TurboFan 内联的 JS-to-Wasm 调用，V8 会创建一个内部延续 `FrameState`，其类型为 `kJSToWasmBuiltinContinuation`。其函数信息使用了一个派生类来存储 Wasm 签名：

```
class JSToWasmFrameStateFunctionInfo : public FrameStateFunctionInfo {
 public:
  const wasm::CanonicalSig* signature() const { return signature_; }

 private:
  const wasm::CanonicalSig* const signature_;
};
```

这个签名不仅仅是信息性的。在代码生成期间，V8 从其中派生出 Wasm 返回类型，并将该类型序列化到去优化数据中。如果发生延迟去优化，去优化器会使用记录的返回类型来具体化结果。

#### 具体化 Wasm 返回值

对于 JS-to-Wasm 延迟去优化，在机器码层面调用已经返回。因此，去优化器根据返回寄存器和记录的 Wasm 返回类型来重建调用结果：

```
TranslatedValue Deoptimizer::TranslatedValueForWasmReturnKind(
    std::optional<wasm::ValueKind> wasm_call_return_kind) {
if (wasm_call_return_kind) {
    switch (wasm_call_return_kind.value()) {
      case wasm::kI32:
        return TranslatedValue::NewInt32(
            &translated_state_,
            static_cast<int32_t>(input_->GetRegister(kReturnRegister0.code())));
      case wasm::kI64:
        return TranslatedValue::NewInt64ToBigInt(
            &translated_state_,
            static_cast<int64_t>(input_->GetRegister(kReturnRegister0.code())));
      case wasm::kF32:
        return TranslatedValue::NewFloat(
            &translated_state_,
            input_->GetFloatRegister(wasm::kFpReturnRegisters[0]).code());
      case wasm::kF64:
        return TranslatedValue::NewDouble(
            &translated_state_,
            input_->GetDoubleRegister(wasm::kFpReturnRegisters[0]).code());
      case wasm::kRefNull:
      case wasm::kRef:
        return TranslatedValue::NewTagged(
            &translated_state_,
            Tagged<Object>(input_->GetRegister(kReturnRegister0.code())));
      default:
        UNREACHABLE();
    }
  }
return TranslatedValue::NewTagged(&translated_state_,
                                    ReadOnlyRoots(isolate()).undefined_value());
}
```

去优化器不会询问原始 Wasm 函数它返回了什么；它信任从 `FrameState` 序列化而来的 `wasm_call_return_kind`。对于 `kI64` 和引用返回，它都读取同一个机器返回寄存器 `kReturnRegister0`。唯一的区别是如何解释这些位：`kI64` 将寄存器值强制转换为 `int64_t` 并将其装箱为 `BigInt`，而 `kRef` 和 `kRefNull` 将寄存器值包装为 `Tagged<Object>`。

这也是为什么当与 `i64` 混淆时，`externref` 情况会泄漏一个完整的 64 位标记值。指针压缩影响存储在堆字段中的许多标记值，但编译器图中的 Wasm 引用值使用标记的寄存器表示形式。在指针压缩的构建中，该寄存器表示形式是一个解压缩后的堆指针，或者一个 Smi。当去优化器读取 `kReturnRegister0` 时，没有单独的“32 位压缩指针加基址”对需要重建；寄存器已经包含了完整的标记值。

因此，如果记录的返回类型来自错误的 `FrameState`，去优化器会直接将相同的 64 位位模式重新解释为错误的 JavaScript 值类型。这就是 `externref` 可以被具体化为 `i64`，或者 `i64` 可以被具体化为对象引用的关键点。

#### `FrameState` 合并

一个微妙之处是：`FrameState` 节点在被序列化到去优化数据之前，仍然是编译器图中的节点。这意味着图优化也可以看到它们。这里相关的优化是**公共子表达式消除**，也称为**全局值编号**。

公共子表达式消除本身不是去优化器的一部分，但它可以影响去优化器稍后使用的元数据。如果两个图节点具有相同的输入和等价的元数据，编译器可以保留第一个节点，并用它替换第二个节点的使用。对于普通操作，这消除了冗余工作。对于 `FrameState` 节点，这意味着两个去优化状态可以被合并。

只有当两个 `FrameState` 节点在去优化时可以互换时，合并它们才是安全的。Turboshaft 首先使用一个快速哈希来定位可能的匹配项，然后使用相等性运算符进行完整比较。该比较必须包含影响栈帧重建方式的每个字段。

`FrameState` 的哈希特意只使用了元数据的一小部分，包括其弃绝 ID。哈希冲突是预期会发生的，其本身并不是漏洞：在找到具有相同哈希值的候选节点后，值编号会比较操作的输入和完整选项。因此，正确性的边界在于相等性比较。如果它认为语义上不同的去优化状态是相等的，一个就可以被另一个替换。

### V8 堆沙箱

V8 堆沙箱是一个进程内的软件故障隔离机制，它将源自不受信任的 JavaScript 或 WebAssembly 代码的内存破坏漏洞限制在进程虚拟地址空间的一个子集区域，即 V8 堆沙箱区域内。V8 堆沙箱假设攻击者可以通过典型的传统 V8 漏洞（addrof 和 fakeobj）任意且并发地读取和写入 V8 堆沙箱区域内的内存。

在不失一般性的前提下，V8 堆沙箱的实现可以被视为为寻址操作增加了一个额外的翻译层。

这让你想起了操作系统课程中的地址翻译吗？

V8 沙箱目前是一个 1 TB 大的区域，包含了所有 V8 堆（位于沙箱开头的 4GB V8 指针压缩笼中）、ArrayBuffer 后备存储和 Wasm 后备缓冲区。V8 堆沙箱中的寻址操作可以描述如下：

* 压缩指针：32 位指针，这是在 V8 堆沙箱中使用的指针表示形式。压缩指针笼分配在 V8 堆沙箱区域的开头。当解引用压缩指针时，引擎将压缩指针笼的基址加到压缩指针上，得到 V8 堆沙箱区域内的实际地址。
* 沙箱化指针：位于沙箱内的对象可以使用从沙箱基址开始的 40 位偏移量来引用。
* 指针表：V8 需要引用沙箱外的对象。这些对象通过指针表来引用，指针表也位于沙箱外，包括 `CodePointerTable`、`TrustedPointerTable` 和 `ExternalPointerTable`。指针表用于存储沙箱外对象的实际地址，并带有内联的类型标志。也通过在初始化期间为每个表预留固定...