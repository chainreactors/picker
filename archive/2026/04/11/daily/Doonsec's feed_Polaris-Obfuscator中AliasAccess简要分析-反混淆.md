---
title: Polaris-Obfuscator中AliasAccess简要分析-反混淆
url: https://mp.weixin.qq.com/s/FYZ-MS0_dd2sBO0e4N7S2Q
source: Doonsec's feed
date: 2026-04-11
fetch_date: 2026-04-12T04:43:15.771163
---

# Polaris-Obfuscator中AliasAccess简要分析-反混淆

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Cpo2XCpI7K19ibCsRPZb6tQPsPzkssdjdwYicJtyHeFhZQqqPEZicIoVcqOJwiakfKEccaKldz8vP3bvfalFEicshYHdqicKYBwS7fhMx3XkM7jW0/0?wx_fmt=jpeg)

# Polaris-Obfuscator中AliasAccess简要分析-反混淆

Taardisaa
Taardisaa

看雪学苑

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

## AliasAccess pass 的核心思路是：把函数里的局部变量（alloca）藏进随机生成的 struct 里，再通过一条多跳的间接指针链来访问它们，而不是直接引用。

##

原本的代码：

```
int x = 42;
use(x);
```

经过混淆后，变量`x`被塞进某个 struct 的某个随机字段里，访问时变成：

```
// 穿过若干层 getter 调用，最终 GEP 到那个字段
v9 = getter_1(v50);         // transit hop 1
v10 = getter_2(*v9);        // transit hop 2
*(int*)(*v10 + offset) = 42; // 最终写入 raw struct 的字段
```

反编译出来的伪代码大概是这样：

```
v9 = (_QWORD *)sub_1BE0(v50);
*(_DWORD *)(*(_QWORD *)sub_1BF0(*v9) + 28LL) = 42;
```

其中每一个`sub_1Bxx`都是一个 getter 函数，`+28`是该变量在 raw struct 里的字段偏移。

混淆 Pass 的实现

实现代码见`src/llvm/lib/Transforms/Obfuscation/AliasAccess.cpp`，`process()`函数分 7 个阶段完成混淆。

### 数据结构

每个节点用`ReferenceNode`表示：

```
struct ReferenceNode {
    AllocaInst *AI;                                      // 对应的 alloca 指令
bool IsRaw;                                          // 是否是叶节点（raw node）
unsigned Id;
    std::map<AllocaInst *, ElementPos> RawInsts;         // raw node 专用：alloca -> 字段位置
    std::map<unsigned, ReferenceNode *> Edges;           // 出边：slot index -> 子节点
    std::map<AllocaInst *, std::vector<unsigned>> Path;  // 可达性：alloca -> 到达它所需的 slot 序列
};
```

* **Raw node**

  （`IsRaw = true`）：叶节点，真正存储变量数据的地方。其`AI`是一个自定义 struct 的 alloca，该 struct 里混杂了真实字段和`i8*`dummy 字段。
* **Transit node**

  （`IsRaw = false`）：中间节点，不存储任何变量数据，只持有指向其他节点的指针。其`AI`是`TransST`的 alloca，`TransST`本质上就是`{ i8* slot[BRANCH_NUM] }`。

### Phase 1：收集 alloca

遍历函数所有指令，收集对齐 <= 8 的`AllocaInst`，这些是待混淆的候选变量。

```
for (BasicBlock &BB : F) {
  for (Instruction &I : BB) {
    if (isa<AllocaInst>(I)) {
      AllocaInst *AI = (AllocaInst *)&I;
      if (AI->getAlign().value() <= 8) {
        AIs.push_back((AllocaInst *)&I);
      }
    }
  }
}
```

### Phase 2：构造 TransST

构造一个固定的 transit struct 类型，本质上就是`{ i8* slot[BRANCH_NUM] }`。每个 slot 要么指向下一个节点，要么为 null。BRANCH\_NUM 控制每个 transit 节点最多有几条出边。

```
for (unsigned i = 0; i < BRANCH_NUM; i++) {
  Slots.push_back(PtrType);
}
TransST->setBody(Slots);
```

### Phase 3：随机分桶

把所有 alloca 随机分配到`AIs.size()`个 bucket 里，分布不均匀，其中同一个 bucket 里的 alloca 会被打包进同一个 raw struct。

```
std::vector<std::vector<AllocaInst *>> Bucket;
for (unsigned i = 0; i < AIs.size(); i++) {
  Bucket.push_back(std::vector<AllocaInst *>());
}
for (AllocaInst *AI : AIs) {
unsigned Index = getRandomNumber() % AIs.size();
  Bucket[Index].push_back(AI);
}
```

### Phase 4：构造 Raw Node

对每个非空 bucket，创建一个 raw node。struct 的 slot 数为`Items.size() * 2 + 1`：

* 真实字段：`Items.size()`个，类型是对应 alloca 的原始类型，放在随机选的位置
* Dummy 字段：剩余位置填`i8*`，纯粹是迷惑性 padding

下面是一个例子：

```
struct RawST {
i8     *dummy_0;   // padding
    int32_t real_x;    // <- 真正的变量 x，放在随机位置
i8     *dummy_2;   // padding
    float   real_y;    // <- 真正的变量 y
i8     *dummy_4;   // padding
};
```

其中，5个字段里面，有两个是真的有用的；剩下的dummy只用于增加逆向时的难度。

```
ReferenceNode *RN = new ReferenceNode();
RN->IsRaw = true;
StructType *ST = StructType::create(F.getContext());
unsigned Num = Items.size() * 2 + 1;

// 随机选 Items.size() 个不重复的位置放真实字段
getRandomNoRepeat(Num, Items.size(), Random);
for (unsigned i = 0; i < Items.size(); i++) {
  AllocaInst *AI = Items[i];
  unsigned Idx = Random[i];
  Slots[Idx] = AI->getAllocatedType();  // 真实类型
  ElementPos EP;
  EP.Type = ST;
  EP.Index = Idx;
  RN->RawInsts[AI] = EP;  // 记录 alloca -> 字段位置的映射
}
// 剩余位置填 i8* dummy
for (unsigned i = 0; i < Num; i++) {
if (!Slots[i]) Slots[i] = PtrType;
}
ST->setBody(Slots);
RN->AI = IRB.CreateAlloca(ST);
```

### Phase 5：构造 Transit Node

创建`Graph.size() * 3`个 transit 节点，形成一个有向无环图（DAG）。每个 transit 节点随机选几条出边，指向已有的节点（raw 或 transit），并在函数入口处 emit store 指令把子节点指针写入对应的 slot。同时，**Path 自底向上传播可达性**：一个 transit 节点知道"从我的 slot[N] 出发，能到达哪些 alloca"，这是 Phase 6 use-site 改写的依据。

```
unsigned Num = Graph.size() * 3;
for (unsigned i = 0; i < Num; i++) {
  ReferenceNode *Parent = new ReferenceNode();
  AllocaInst *Cur = IRB.CreateAlloca(TransST);
  Parent->AI = Cur;
  Parent->IsRaw = false;
  unsigned BN = getRandomNumber() % BRANCH_NUM;  // 随机决定出边数量
getRandomNoRepeat(BRANCH_NUM, BN, Random);       // 随机选 BN 个不重复的 slot index
for (unsigned j = 0; j < BN; j++) {
    unsigned Idx = Random[j];
    ReferenceNode *RN = Graph[getRandomNumber() % Graph.size()];  // 随机选子节点
    Parent->Edges[Idx] = RN;
// 运行时：Cur->slot[Idx] = RN->AI
    IRB.CreateStore(RN->AI,
        IRB.CreateGEP(TransST, Cur, {IRB.getInt32(0), IRB.getInt32(Idx)}));
// 传播可达性到 Parent->Path
if (RN->IsRaw) {
for (auto Iter = RN->RawInsts.begin(); Iter != RN->RawInsts.end(); Iter++)
        Parent->Path[Iter->first].push_back(Idx);
    } else {
for (auto Iter = RN->Path.begin(); Iter != RN->Path.end(); Iter++)
        Parent->Path[Iter->first].push_back(Idx);
    }
  }
  Graph.push_back(Parent);  // push_back 在末尾，保证不会有环
}
```

> 原本本人以为这样的链式结构有可能会意外引入环，导致无限死循环；然而后面仔细观察发现，Transit 节点只能指向比自己**更早**加入 Graph 的节点，`push_back`在 for 循环末尾执行，天然保证了 DAG 结构，链条一定终止于 raw leaf.

### Phase 6：改写 Use-Site

对每个用到原始 alloca 的操作数，in-place 替换成 chain 计算的结果：

* 从 Graph 中随机选一个能到达该 alloca 的入口节点
* 沿 Path 逐跳 emit getter 调用（每跳一次`CreateCall`+`CreateLoad`），直到到达 raw node
* 在 raw node 上 emit GEP，取得该 alloca 对应的字段地址
* `U.set(VP)原地替换操作数`

```
for (Use &U : I.operands()) {
  AllocaInst *AI = (AllocaInst *)Opnd;
  IRB.SetInsertPoint(&I);
  std::shuffle(Graph.begin(), Graph.end(), std::default_random_engine());
// 找一个能到达 AI 的入口节点
  ReferenceNode *Ptr = nullptr;
for (ReferenceNode *RN : Graph) {
if (RN->Path.find(AI) != RN->Path.end() ||
        (RN->IsRaw && RN->RawInsts.find(AI) != RN->RawInsts.end())) {
      Ptr = RN; break;
    }
  }
  Value *VP = Ptr->AI;
// 沿链逐跳 emit getter 调用
while (!Ptr->IsRaw) {
    std::vector<unsigned> &Idxs = Ptr->Path[AI];
    unsigned Idx = Idxs[getRandomNumber() % Idxs.size()];
if (Getter.find(Idx) == Getter.end())
      Getter[Idx] = buildGetterFunction(*F.getParent(), TransST, Idx);
    VP = IRB.CreateLoad(PtrType, IRB.CreateCall(FunctionCallee(Getter[Idx]), {VP}));
    Ptr = Ptr->Edges[Idx];
  }
// 到达 raw node，GEP 取字段地址
  ElementPos &EP = Ptr->RawInsts[AI];
  VP = IRB.CreateGEP(EP.Type, VP, {IRB.getInt32(0), IRB.getInt32(EP.Index)});
  U.set(VP);  // 原地替换操作数
}
```

控制流、基本块结构不变，只是操作数从直接引用 alloca 变成了一串 call chain 的结果。

### Phase 7：清理

删除原始的 alloca 指令（已被 struct 字段替代），释放 graph 节点内存。

```
for (AllocaInst *AI : AIs)
AI->eraseFromParent();
for (auto Iter = Graph.begin(); Iter != Graph.end(); Iter++)
delete *Iter;
```

### Getter 函数

Getter 函数由`buildGetterFunction`生成，签名为`i8*(i8*)`：

```
i8* getter(i8* ptr) {
return &((TransST*)ptr)->slot[Index];
}
```

**关键弱点**：`Index`是编译期静态确定的常量，直接 baked 进 GEP 的 immediate 里。每个唯一的 index 对应一个独立的 getter 函数，lazy 创建并缓存在`Getter`map 里。这是一个潜在的反混淆突破口。

混淆效果分析

两层叠加：

* **Struct 内部：真假字段混杂，字段位置随机。**
* **Struct 之间：多跳指针链，每个 use-site 的入口节点随机选取，call chain 深度不固定**

源码片段：

```
print_hash_value = 1;
```

从混淆后binary反编译的伪代码来看（IDA Pro 示例，O0优化）：

```
// 访问 print_hash_value = 1，实际经过两跳
v9  = (_QWORD *)sub_1BE0(v50);                          // transit hop 1
*(_DWORD *)(*(_QWORD *)sub_1BF0(*v9) + 28LL) = 1;      // transit hop 2 + GEP(offset=0x1c)
```

其中：

* `v50是某个 transit node 的 alloca（栈上的local_xxx）`
* `sub_1BE0/sub_1BF0是 getter 函数（或其 inline 展开）`
* `+28（0x1c）是print_hash_value在 raw struct 里的字段偏移`

### 在high level optimization下的表现

我又在O2优化下进行了一次测试：

```
int __fastcall main(int argc, const char **argv, const char **envp)
{
    // 省略variable declarations

if ( argc == 2 )
  {
    v3 = strcmp(argv[1], "1");
    v4 = v3 != 0;
    v5 = v3 == 0;
  }
else
  {
    v5 = 0;
    v4 = 1;
  }
  si128 = _mm_load_si128((const __m128i *)&xmmword_2010);
  v7 = 0LL;
  v8 = _mm_load_si128((const __m128i *)&xmmword_2020);
  v9 = _mm_load_si128((const __m128i *)&xmmword_2030);
  do
  {
    v10 = _mm_srai_epi32(_mm_slli_epi32(si128, 0x1Fu), 0x1Fu);
    v11 = _mm_srli_epi32(si128, 1u);
    v12 = _mm_or_si128(_mm_and_si128(_mm_xor_si128(v11, v8), v10), _mm_andnot_si128(v10, v1...