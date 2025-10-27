---
title: OLLVM控制流平坦化的改进
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458481271&idx=1&sn=72ef245c326f965937dd196fb02c5736&chksm=b18e42fd86f9cbeb69c571395982bba6bbf58515f44b68372458da468557d51b7696e5498241&scene=58&subscene=0#rd
source: 看雪学院
date: 2022-11-03
fetch_date: 2025-10-03T21:40:40.634291
---

# OLLVM控制流平坦化的改进

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6OsSiahyiaicWfMKkn19EV8J0pNosiaNf76UXtDvK3KEGut2ia4VPo7MU0iag/0?wx_fmt=jpeg)

# OLLVM控制流平坦化的改进

R1mao

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6mVVHugeNFlPF7GpFxSyqSnDtVbuTB5Aliawg4STBzLtIlpViauw7tWzw/640?wx_fmt=jpeg)

本文为看雪论坛精华文章

看雪论坛作者ID：R1mao

```
一

传统平坦化
```

控制流平坦化这个混淆方式第一次出现于Ollvm项目中，作为其中的三种混淆方式之一fla。该混淆方式主要思想就是以基本块为单位，通过一个主分发器来控制程序的执行流程。在这种结构下，原有的程序控制逻辑被打碎，通过其中的控制变量配合Switch结构来实现控制流的转移。

OLLVM是一款是由瑞士西北科技大学开发的一套开源的针对LLVM的代码混淆工具，旨在加强逆向的难度，整个项目包含数个包含独立功能的LLVM Pass，每个Pass会对应实现一种特定的混淆方式，这些Pass将在后面进行细说，通过这些Pass可以改变源程序的CFG和源程序的结构。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6VsoKOwAqJyYzOVuwX1kITv6DTM57w0Xrpg9QSDlAb0B8eqL8lR1iauw/640?wx_fmt=png)

具体的混淆流程如下：

1.收集原函数中所有的基本块，并初始化随机数种子。

2.对入口基本块进行处理，切分基本块保证入口基本块只有一个后继。

3.给每一个基本块分配一个随机数字，并新建一个变量var，在入口基本块中赋值为入口基本块后继基本块对应的数字。

4.构造出基本的switch结构和循环框架，使得switch链接所有原有基本块。

5.修正每个原有基本块的后继，使其跳转至switch结构，并在跳转之前根据后继和跳转条件构造对var的赋值语句。

而在原版的框架中，该混淆的普适性并不好。在针对于存在异常处理的C++代码中，是无法进行混淆的，同时由于该方案提出时间较早，早已有多种方法能够很好的去除该混淆，因此在该篇文章中，对原有的混淆进行改进，使其能够支持异常处理和防止被轻易去除。本文是基于控制流平坦化Pass的改进，主要提出的为改进原理，不会基于源码一行行分析，最后会将源码放出，可自行阅读。

#

#

```
二

支持异常处理
```

在传统的平坦化中，假定了每个函数的Terminator都是跳转指令BranchInst，然而在实际处理过程中并不一定是BranchInst，还有可能是SwitchInst，由于平坦化只处理后继小于等于2的情况，对于这种有多个后继的Terminator是无法处理的。针对于这种情况比较好处理，直接在上述第5步不修正其Terminator，让其保持原有的代码，直接continue即可，这样就可以保证其正常运行。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6lO7jkDC3W7mE3wAocpic43hv3lPaRibb7ctRGnZleAPD8icKwPBvTS2KQ/640?wx_fmt=png)
但是除此之外，有一个指令为InvokeInst指令，这个指令有两个后继，但是一个是正常的基本块处，另一个是跳转到unwind相关的逻辑中，这个unwind基本块的开头必须为LandingPadInst，且只能通过InvokeInst指令来到达。所以当LandingPadInst被插入到SwitchInst中去的时候，由于不是通过InvokeInst到达的，所以会报错。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT63WvuvloUlibTibyq05VYaCjaBic2ibILjIYxVrMznq65FqJjTZ8LdfD80w/640?wx_fmt=png)
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6O062ibSKMkXfnGRBxAIunrDGfzLGiaaYTyicseU0YCicZIfE5jA1xHFS7w/640?wx_fmt=png)

修正这种情况的思路也是非常的简单，首先需要确定每个基本块的Terminator是否是InvokeInst，是的话则从需要平坦化的基本块中剔除掉InvokeInst对应的UnwindBasicBlock。同时在进行第五步时判断当且仅当Terminator为BranchInst时才进行修正后继，否则不做任何处理。最后处理后结果如下所示。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6Aib8tTsiaqtkQ5ibC62mkGPeq2ZbOHS79kHKU7I2RsV4jKqmmIm4lIQ2A/640?wx_fmt=png)

* 代码修改如下(新增了判断Terminator是否为BranchInst)：
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6xR0ujdw7NrCsgeVFTAS2vaiaI5PhjERY9yIrYDmr8Lfc42LVC8NIw4A/640?wx_fmt=png)
* 同时去除了LandingPad所在的基本块。
  ![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT64C7LE6srB7X2e255nb9S1fEfwt6R4UibYtwo12K59VA1GYIAoJvkgqg/640?wx_fmt=png)

#

#

```
三

增强反反混淆效果
```

#

# 在现存的对抗思路中，无外乎就是模拟执行和静态分析两种思路。模拟执行首先需要定位到混淆后的控制流图中的真实块，即原控制流图中的基本块，然后从每个基本块开始模拟执行，给所有真实块(原函数中的基本块)下断点，当从基本块A出发，位于B中的断点触发，便能很容易的确定基本块后继(B是A的后继)，如果遇到存在两个后继的情况则将对应的条件判断取反，从而使其获得两条路径，这样的思路往往采用angr或者unicorn实现，已经存在很多脚本了。而静态分析往往更加的困难，需要定位到对应的控制变量，并根据程序逻辑，找出每个基本块对应的值，并通过判断计算出每个基本块对应的后继。

#

# 对于静态分析，更加偏向于经验化，通过少量的修改即可使得其适用性降低，因此静态方法去除控制流平坦化的思路往往被使用的较少，且普适性较差。

#

# 而对于模拟执行，为了实现恢复的完整性，往往都是单独的从一个基本块出发，设下断点，确定该基本块的后继是什么。(当然也存在动态trace整个程序的执行流程，只要确定真实块即可简单的trace恢复执行流程，但是往往程序逻辑的触发条件是复杂的，有可能并不能覆盖所有的分支，因此这里不做讨论)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6zgBm5qtIZ9YSBK1EgS4ZILcCJe6dyVeACW1ibZHWW1bI3bzI2Mca7Jw/640?wx_fmt=png)

这里主要针对第二种思路进行对抗，即模拟执行。在模拟执行中，存在两个关键点，一是真实块的确定，二是后继的确定。由于大部分思路都是从某个基本块直接出发确定，这个方法能够正确运行的原因，是因为在去除混淆时，我们并不关心原有代码基本块之间的运行关系，程序状态并不会影响控制流的转移。换句话说控制流平坦化中，由于完全依靠一个变量简单确定后继，且每个真实块中该变量的赋值并没有蕴含基本块之间的关系，因此可以单独的确定每个基本块的后继。

基于此，如果构造出一种能够实现控制流的转移需要基于现在已执行基本块的信息的方式，即可很好的防护这种逐个击破的攻击方式。

对于一个函数的控制流图，如果需要运行到节点(基本块)B，存在一些必定经过的节点，而这些节点即必经节点。

> 定义如果从起点E出发，要到达节点B必须经过节点A，则可称A支配节点B。

通过支配节点的定义，不难构造出一个方案来防御逐个击破的手段：

每个节点都存在一个标志位，用于标记每个节点(基本块)是否被访问。

如果运行到某个节点B，支配B的节点的标志位必定被设置为1(被访问)。

每个节点存在一个key变量，只有通过这个正确的key才能计算出正确的后继。

一个节点B被第一次执行时会更新其他节点的key，这些其他节点被节点B支配。

例如下图，每个节点都有一个变量来标记是否被经过，都有数组v存储，v[A]=1代表A已经被访问，且初始化结果都为0，因为刚开始时所有节点都没有被访问。

当一个节点A执行时，会赋值v[A]=1，如果发现它被赋值前为0的话说明为第一次经过，那么就根据自身分配到的随机值修改其他节点的key值，这些其他节点都是被A支配的节点。
![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8HOE7XGJ8oN1oR9rHNlWkT6zbUuJNfaky3QsibKmJkfoU1DtV8rltc5O476vN3ib73tGic2wwoICOXeg/640?wx_fmt=png)

所以在这种情况下，在程序具体执行中的每个节点的key是一个特定的值(因为一个节点有固定多个必经节点，当节点被执行时，其必经节点也必然被执行，且保证了每个节点只会更新一次其他节点的key值)，如果将节点单独抽取出来执行的话，没有必经节点更新他的key值，则必然与具体执行中的key不一样。

由于该特性，计算出每个节点的特定的值，并对原有的控制流平坦化中的控制变量switchVar进行异或运算，只有key是正确的才能保证switchVar的值是正确的，从而跳转到正确的后继节点。而如果单纯的抽出某个节点开始执行的话，由于没有执行节点的必经节点，导致其key值不正确，因此switchVar也是错误的，从而无法获得正确的后继，从而保护代码防止被去混淆。

具体的修改代码如下：

插入一个函数，通过给定的随机值更新其他节点的key值。

```
Function *buildUpdateKeyFunc(Module *m){  std::vector<Type*> params;  params.push_back(Type::getInt8Ty(m->getContext()));         params.push_back(Type::getInt32Ty(m->getContext()));  params.push_back(Type::getInt32Ty(m->getContext())->getPointerTo());  params.push_back(Type::getInt32Ty(m->getContext())->getPointerTo());  params.push_back(Type::getInt32Ty(m->getContext()));  FunctionType *funcType=FunctionType::get(Type::getVoidTy(m->getContext()),params,false);  Function *func=Function::Create(funcType,GlobalValue::PrivateLinkage,Twine("ollvm"),m);  BasicBlock *entry=BasicBlock::Create(m->getContext(),"entry",func);  BasicBlock *cond=BasicBlock::Create(m->getContext(),"cond",func);  BasicBlock *update=BasicBlock::Create(m->getContext(),"update",func);  BasicBlock *end=BasicBlock::Create(m->getContext(),"end",func);  Function::arg_iterator iter=func->arg_begin();  Value *flag=iter;  Value *len=++iter;  Value *posArray=++iter;  Value *keyArray=++iter;  Value *num=++iter;  IRBuilder<> irb(entry);  Value *i=irb.CreateAlloca(irb.getInt32Ty());  irb.CreateStore(irb.getInt32(0),i);  irb.CreateCondBr(irb.CreateICmpEQ(flag,irb.getInt8(0)),cond,end);   irb.SetInsertPoint(cond);  irb.CreateCondBr(irb.CreateICmpSLT(irb.CreateLoad(i),len),update,end);   irb.SetInsertPoint(update);   Value *pos=irb.CreateLoad(irb.CreateGEP(posArray,irb.CreateLoad(i)));  Value *key=irb.CreateGEP(keyArray,pos);  irb.CreateStore(irb.CreateXor(irb.CreateLoad(key),num),key);  irb.CreateStore(irb.CreateAdd(irb.CreateLoad(i),irb.getInt32(1)),i);  irb.CreateBr(cond);   irb.SetInsertPoint(end);  irb.CreateRetVoid();  return func;}
```

插入标记数组和key数组，计算出每个基本块的key值数组(key\_map)，为每个基本块分配一个随机值用于更新其他节点的key，并在基本块后添加更新标记数组和key数组的代码。

```
IRBuilder<> irb(&*oldEntry->getFirstInsertionPt());                                // generate context info key for each blockValue *visitedArray=irb.CreateAlloca(irb.getInt8Ty(),irb.getInt32(origBB.size()));Value *keyArray=irb.CreateAlloca(irb.getInt32Ty(),irb.getInt32(origBB.size()));irb.CreateMemSet(visitedArray,irb.getInt8(0),origBB.size(),(MaybeAlign)0);irb.CreateMemSet(keyArray,irb.getInt8(0),origBB.size()*4,(MaybeAlign)0);int idx=0;std::vector<unsigned int> key_list;DominatorTree tree(*f);std::map<BasicBlock*,unsigned int> key_map;std::map<BasicBlock*,unsigned int> index_map;for(std::vector<BasicBlock *>::iterator b=origBB.begin();b!=origBB.end();b++){  BasicBlock *block=*b;  unsigned int num=getUniqueNumber(&key_list);  key_list.push_back(num);  key_map[block]=0;}for(std::vector<BasicBlock *>::iterator b=origBB.begin();b!=origBB.end();b++,idx++){  BasicBlock *block=*b;  std::vector<Constant*> doms;  int i=0;  for(std::vector<BasicBlock *>::iterator bb=origBB.begin();bb!=origBB.end();bb++,i++)  {      BasicBlock *block0=*bb;      if(block0!=block && tree.dominates(block,block0))      {          doms.push_back(irb.getInt32(i));          key_map[block0]^=key_list[idx];      }   }  irb.SetInsertPoint(block->getTerminator());  Value *ptr=irb.CreateGEP(irb.getInt8Ty(),visitedArray,irb.getInt32(idx));  Value *visited=irb.CreateLoad(ptr);  if(doms.size()!=0)  {      ArrayType *arrayType=ArrayType::get(irb.getInt32Ty(),doms.size());      Constant *doms_array=ConstantArray::get(arrayType,ArrayRef<Constant*>(doms));      GlobalVariable *dom_variable=new GlobalVariable(*(f->getParent()),arrayType,false,GlobalValue::Linkage...