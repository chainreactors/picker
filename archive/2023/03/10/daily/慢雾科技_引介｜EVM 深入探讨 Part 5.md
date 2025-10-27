---
title: 引介｜EVM 深入探讨 Part 5
url: https://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247497104&idx=1&sn=85f08352d0abb5730fed8f6857b4e75e&chksm=fdde8b17caa902012781c59751443160c13bd75e88f54c6ddeb5f2ae3b4d22aadc3534ba6e74&scene=58&subscene=0#rd
source: 慢雾科技
date: 2023-03-10
fetch_date: 2025-10-04T09:10:40.297815
---

# 引介｜EVM 深入探讨 Part 5

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/qsQ2ibEw5pLaSkYibDfHge03xsEAyPdArxvW8ibTdDW20GbIKPVdZouWaZSaxCltJlt19sWqQdeY3mPyTHoDiaQJ1A/0?wx_fmt=jpeg)

# 引介｜EVM 深入探讨 Part 5

原创

慢雾安全团队

慢雾科技

By: Flush

# **导语**

这是 noxx “EVM 深入探讨” 系列的第五部分，这期我们将从 Solidity、EVM 和 Geth 客户端层的工作原理，详细解读 CALL 和 DELEGATECALL 这两个操作码。

在我们深入探讨之前，我们需要先了解合约执行上下文的概念。

# **执行上下文**

当以太坊虚拟机(EVM) 执行智能合约时，会为其创建一个上下文，由以下内容组成：

* **The Code**

合约的字节码是不可改变的，它被存储在链上，并使用合约地址进行引用。代码是存储指令的区域。存储在代码中的指令数据作为合约账户状态字段的一部分是持久的。外部拥有的账户（或 EOA）有空的代码区域。代码是智能合约执行期间由 EVM 读取、解释和执行的字节。代码是不可变的，这意味着它不能被修改，但它可以通过指令 CODESIZE 和 CODECOPY 来读取。一个合约的代码可以被其他合约读取，通过指令 EXTCODESIZE 和 EXTCODECOPY。

* **The Stack**

调用栈，每个 EVM 合约执行时都会初始化一个空的栈。栈是一个 32 字节的元素列表，用于存储智能合约指令的输入和输出。每个调用上下文创建一个栈，当调用上下文结束时，它被销毁。当一个新的值被放在栈区时，它被放在顶部，只有顶部的值才会被指令使用。目前，栈的最大限制是 1024 个值。所有的指令都与栈相互作用，但它可以直接用 PUSH1, POP, DUP1 或 SWAP1 等指令进行操作。

* **The Memory**

合约内存，是为每个 EVM 合约执行而初始化一个空的内存。EVM 的内存是不永久的，在调用上下文结束时被销毁。在调用上下文开始时，内存被初始化为 0。从内存中读和写通常分别用 MLOAD 和 MSTORE 指令完成，但也可以用其他指令如 CREATE 或 EXTCODECOPY 来访问。

* **The Storage**

存储区在执行过程中持久化，链上存储，根据合约地址和插槽寻址。合约存储是跨执行的，它存储在链上，通过合约地址和它的存储插槽被引用。存储器是一个 32 字节的插槽与 32 字节的值的映射。存储是智能合约的持久性内存：合约写入的每个值都会保留到调用完成后，除非其值被改为 0，或者执行 SELFDESTRUCT 指令。从未写入的密钥中读取存储的字节也会返回 0。每个合约都有自己的存储，不能读取或修改其他合约的存储。存储是用指令 SLAD 和 STORE 来读和写的。

* **The calldata**

交易传入的数据。calldata 区域是作为智能合约交易的一部分发送给交易的数据。例如，当创建一个合约时，calldata 将是新合约的构造器代码。值得注意的是，当一个合约执行 xCALL 指令时，它也会创建一个内部交易，在新的上下文中产生一个 calldata 区域。calldata 是不可改变的，可以用指令 CALLDATALOAD, CALLDATASIZE 和 CALLDATACOPY 来读取。当一个合约执行 xCALL 指令时，它也会创建一个内部事务。因此，当执行 xCALL 时，在新的上下文中有一个 calldata 区域。

* **The Return Data**

合约调用的返回数据。The Return Data 是智能合约在调用后可以返回一个值的方式。它可以由合约调用通过 RETURN 和 REVERT 指令设置，也可以由调用合约通过 RETURNDATASIZE 和 RETURNDATACOPY 读取。

在阅读后面的内容时，请记住以上内容。我们将从 Smart Contract Programmer

(https://solidity-by-example.org/delegatecall/) 的 DELEGATECALL 合约实例讲起。

# **Solidity 实例**

下图显示了同一个合约上两个函数调用的执行情况，一个使用 DELEGATECALL，另一个使用 CALL。

我们将运行这两个函数并比较它们的不同之处。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaSkYibDfHge03xsEAyPdArxqEl3nRe6dDjbeiaePXtrtX4HiaIYVOOw36C0eKlpgLIbf0eQ28Dh1mTw/640?wx_fmt=png)

以下是这次交互的一些信息（如果我们在 remix 中自己执行的话，数据将会有所不同）：

我们部署两个合约，名为合约 A 和 B，以及使用一个 EOA 地址，数据如下：

* EOA 地址：0x5B38Da6a701c568545dCfcB03FcB875f56beddC4
* 合约 A 的地址：0x7b96aF9Bd211cBf6BA5b0dd53aa61Dc5806b6AcE
* 合约 B 的地址：0x3328358128832A260C76A4141e19E2A943CD4B6D

##

## 现在把 Contract B 的地址，一个 uint 值 12 以及 1000000000000000000 Wei（也就是 1 ETH）参数传入，来调用 Contract A 里的两个函数，setVarsDelegateCall 和 setVarsCall。

* **Delegate Call**

1. EOA 地址将合约 B 的地址，一个 uint 值 12 以及 1000000000000000000 Wei 传入，调用合约 A 的 setVarsDelegateCall，由 delegatecall 调用合约 B 执行 setVars(uint256)，参数为 12。

2. 该 delagatecall 调用执行了合约 B 的 setVars(uint256) 代码，但更新了合约 A 的存储。执行时的存储、msg.sender 和 msg.value 与它的父调用 setVarsDelegateCall 相同。

3. 这些值被设置在合约 A 的存储中，12 为 num，调用者 EOA 地址(0x5B38) 为 sender，100000000000000 为 value。尽管 setVars(uint256) 被合约 A 调用，但当我们检查 msg.sender 和 msg.value 时，我们得到了原 setVarsDelegateCall 的值。

执行这个函数后，检查合约 A 和 B 的 num, sender 和 value 状态，我们能看到合约 B 没有被初始化，而所有的值都在合约 A 中设置。

* ## **Call**

1. EOA 地址将合约 B 的地址，一个 uint 值 12 以及 1000000000000000000 Wei 传入，调用合约 A 的 setVarsCall，由 call 调用合约 B 执行 setVars(uint256)，参数为 12。

2. 该 call 调用执行合约 B 的 setVars(uint256) ，不改变（本合约的）存储区、msg.sender 和 msg.value。

3. 合约 B 的存储区写入数据：num = 12，sender = 合约 A 地址以及 value = 0（1000000000000000000 Wei 被传进了父调用 setVarsCall）。

在这个函数执行后，我们可以再次检查合约 A 和 B 的 num, sender 和 value 状态。我们看到情况正好相反，合约 A 中没有值被初始化，而合约 B 中所有的值都被设置。

从概念上讲，delegatecall 实际上允许从另一个合约中复制粘贴一个函数到当前合约中。它将被运行，就像它被你的合约执行一样，并且可以访问相同的存储、msg.sender 和 msg.value。

你也可以查看团队之前的文章来对 call 和 delegatecall 进行了解：[智能合约安全审计入门篇 —— delegatecall (1)](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247495630&idx=1&sn=f7ccb4e1a30d5b78679a8335053a9d32&chksm=fdde9149caa9185f32baa92132a841030c68fe622e1f21365255e8c3b3d5d23783b6d0e2cef0&scene=21#wechat_redirect)。

**Delegate Call 和内存布局**

在上述的例子中，你可能会注意合约 B 第 5 行的注释 “NOTE: storage layout must be the same as contract A（注意：内存布局需要和合约 A 一样）”。

合约里的每一个函数都映射到一些静态字节码，这些静态字节码由编译时计算出。当我们从 Solidity 代码来看时，是一个个变量，如：num, sender 和 value。但是字节码并不是这样来识别的，它只认存储插槽，而声明变量的时候就把插槽定下来了（有所遗忘的话可以在之前的 [Part 3](http://mp.weixin.qq.com/s?__biz=MzU4ODQ3NTM2OA==&mid=2247496759&idx=1&sn=b2ed9ce466803dbee59b390ab9d0b1f4&chksm=fdde8ab0caa903a6e48cb7da529c6a1f8271fb39d89382f3114bccf3c11f24fbdd01150abdaf&scene=21#wechat_redirect) 再回顾一下）。

合约 B 的 setVars(uint256) 函数中，"num = \_num" 是要把 \_num 存进插槽 0。当我们看一个 DELEGATECALL 的时候我们不应该单纯考虑 num → num，sender → sender 的映射，因为在字节码的层面并不是这样的，而是需要认识到这是 slot 0 → slot 0, slot 1 → slot 1 的映射。

下图显示了这种映射，以及相对应的变量名称。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaSkYibDfHge03xsEAyPdArx3cia2bE1gdd3pDljaL0v28UicUPwHD9HF5J53LxZIs3icrKgmXR0eiaibnw/640?wx_fmt=png)

如果我们改变了定义状态变量的顺序，会发生什么呢？

这将改变存储插槽位置，同时也改变了 setVars(uint256) 函数的字节码。如果我们通过互换第 6 行的 num 和第 8 行的 value 来更新合约 B，将首先声明 "value" 状态变量，再声明 "num" 状态变量。

这意味着 setVars(uint256) 中的第 11 行 "num = \_num" 将 \_num 存入存储插槽 2，第 13 行 "value = msg.value" 将 msg.value 存储在存储插槽 0 中。合约 A 和 B 之间的变量映射将不再与它们的存储插槽相匹配。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaSkYibDfHge03xsEAyPdArxoQZxvK07jr2X3KsnwHmM2DZ40baEy7naODwWjzMm523tRKmWVo1VRw/640?wx_fmt=png)

当我们调用 DELEGATECALL 时，num 变量将被存储在合约 A 的存储插槽 2 中，该槽映射到 "value" 状态变量。同样地，当 "value" 被存储时，它将被更新到 0 号插槽，该插槽映射到 "num" 状态变量。这也是为什么使用 DELEGATECALL 可能存在风险的原因之一。我们可能会不小心地用 value 值把 num 覆盖了，用 num 值把 value 覆盖了。但黑客不会，他们会有预谋有目的地对此进行攻击。

试想一下我们有一个合约，存在一个开放式的 delegatecall，同时也知道此合约的 owner 存放在哪个插槽。这时我们就能够构建一个带有相同状态变量布局的合约。然后写一个更新 owner 的方法，并通过 delegatecall 这个更新方法来改变该合约的 owner。

下面看一看操作码层面。

**Opcodes**

我们对 DELEGATECALL 的工作原理有了大致的了解，接下来深入了解一下 DELEGATECALL 和 CALL 的操作码。

对于 DELEGATECALL，有以下输入变量：

* gas：执行所需要消耗的 gas 费。
* address ：需要执行的账户。
* argsOffset：输入内存中数据(calldata) 的字节偏移量。
* argsSize：需要复制数据(calldata) 的字节大小。
* retOffset：输出内存中数据(return data) 的字节偏移量。
* retSize：需要复制数据(return data) 的字节大小。

CALL 与 DELEGATECALL 相比有完全相同的输入变量，但多出一个附加值 value。

* value：以 Wei 为单位的 value 数量的以太币发送到账户（仅限 call）。

delegatecall 不需要 value 值输入，因为它是从它的父调用中继承。执行上下文的存储空间与它的父调用相同的存储区、msg.sender 和 msg.value。他们都是有一个布尔返回值 "success"，为 0 为执行失败，反之为 1。

如果调用位置没有合约或者没有代码，那么 Delegatecall 将返回成功 "True"。如果在代码设计上我们期望 delegatecall 函数在不能执行时返回 "False"，这可能会导致出现 bug。

为了理解这个操作码，让我们检查一下前面的例子中合约 A 和合约 B 是如何执行 DELEGATECALL 的。

**通过 Remix 检查 DELEGATECALL 操作码**

下面是 Remix 中调用 DELEGATECALL 操作码的截图。对应 Solidity 代码的 24 - 26 行。我们可以看到栈和内存的条目以及它们是怎么传进 DELEGATECALL 的。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaSkYibDfHge03xsEAyPdArxOwI4QMc5aSNJ20wEfEmMYbSGwzPiaFsjdnMRn9mPCH9dWGbsibrwevsg/640?wx_fmt=png)

下面将从 “操作码 → 栈 → 内存 → calldata” 的顺序来讲解。

1. Solidity 代码的 24 行，使用了 delegatecall 调用合约 B

的 setVars(unit256)，调用执行 DELEGATECALL 操作码。

2. DELEGATECALL 操作码从栈中取出的 6 个输入：

* gas = 0x45eb；
* address = 0x3328358128832A260C76A4141e19E2A943CD4B6D（合约 B 的地址）；
* argsOffset = 0xc4；
* argsSize = 0x24；
* retOffset = 0xc4；
* retSize = 0x00。

3. argsOffset 和 argsSize 代表了将被传递给合约 B 的 calldata。这两个变量表示从内存位置 0xc4 开始，并复制下一个 0x24（十进制的 36）字节作为 calldata。

4. 我们得到了

0x6466414b000000000000000000000000000000000000000000000000000000000000000c，可以拆分成 0x6466414b 和

0x00000000000000000000000000000000000000000000c，前者是

setVars(uint256) 的函数签名，后者是十进制的 12，代表我们对 num 的输入值。

5. 这对应了 Solidity 代码的 25 行

abi.encodeWithSignature("setVars(uint256)", \_num)。

因为 setVars(uint256) 并不返回任何值，所以 retSize 等于 0。如果存在返回值的情况，retSize 的值将被更新，返回的值将被存储在 retOffset 中。以上操作应该让我们对这个操作码的底层逻辑了解的深一点，也同 Solidity 代码联系起来了。

接下来现在让我们来看看 Geth 客户端的实现。

# **Geth 实现**

我们来看一下 Geth 里 DELEGATECALL 的一个特定部分，目的是展示 DELEGATECALL 操作码在存储范围层面上与 CALL 操作码有什么不同，以及这与 LOAD 操作码有什么关系。

下边的图看起来会显得很复杂，但是我们拆解开来一步一步做，在结束的时候会对 DELEGATECALL 和 CALL 有更深刻的认识了。

![](https://mmbiz.qpic.cn/mmbiz_png/qsQ2ibEw5pLaSkYibDfHge03xsEAyPdArxsrSibYk8TGMwpZxvEPhNlfX7ibQS6iaQXLmLgdVKMEfs9rhgVH2xNKxFg/640?wx_fmt=png)

我们在左侧标注了 DELEGATECALL 和 CALL 操作码，在右下方标注了 LOAD 操作码。让我们看看它们是如何联系起来的。

1. 图中两个 [1] 为 instructions.go 中的代码，分别对应了 DELEGATECALL 和 CALL 操作码的 Geth 函数。我们可以看到从栈中弹出的那几个变量，之后看到调用 interpreter.evm.DeleagteCall 和 interpreter.evm.Call 这两个函数，并带有栈中的值、“to 地址” 和当前的合约范围。

2. 图中两个 [2] 为 evm.go 中的代码，分别对应了 evm.DelegateCall 和 evm.Call 执行的函数代码。图中省略了函数代码的内容，重点关注 NewC...