---
title: 混淆 Pass 分析 - Flattening
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458572456&idx=3&sn=bb7abeeccca94754648d7f73d201d482&chksm=b18de62286fa6f34d96056166bdec3ff52be2c90928fb7582a6dbcb56a2e60c90794b946bfbf&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-09-12
fetch_date: 2025-10-06T18:28:41.280684
---

# 混淆 Pass 分析 - Flattening

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8Hljwtk29mb9ibibYBFsn2qhXSK4KYtBGf1cWUEzic0HtpQMC3SRHXvicaFp45HyGTiboAvf3wTqbZP3uA/0?wx_fmt=jpeg)

# 混淆 Pass 分析 - Flattening

ElainaDaemon

看雪学苑

```
一

概述
```

代码扁平化的目的是将原有的程序逻辑重新组合成复杂逻辑，其主要体现是把原来的`if else`语句转换成`switch`语句。`switch`结构体包含多个分支，各个分支的执行顺序是随机的，但并不影响真正的程序逻辑。然后在`switch`结构的外层，再套一个或多个`while`循环。

下面编写一段代码进行测试，代码的功能是在`main`函数中执行一个名称为`add`的自定义函数。`add`函数里会判断参数`num1`是否等于`100`，如果等于，则返回`0`，否则继续执行，而后将参数`num1`和`num2`相加，结果赋值给`num3`，并返回`num3`。具体代码如下：

```
int add(int num1, int num2){
    if (num1 == 100) {
        return 0;
    }
    int num3 = num1 + num2;
    return num3;
}

int main(){
   int num1 = 10;
   int num2 = 20;
   int num3 = add(num1,num2);
   return 0;
}
```

编译上面的代码，使用 IDA 反编译可执行文件，会看到代码的调用过程非常简单，很容易被分析，如图所示:

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8Hljwtk29mb9ibibYBFsn2qhXXEdnQL78Eg3gO0JHWp2HrtdQHFX3axqCuuCpIWzLbBjNZqf5caKv5w/640?wx_fmt=png&from=appmsg)

###

```
二

源码分析
```

obfuscator-llvm（https://github.com/obfuscator-llvm/obfuscator/blob/llvm-4.0/lib/Transforms/Obfuscation/Flattening.cpp）中有一个代码扁平化的 Pass，名称为 flattening，接下来我们抽丝剥茧，一步步分析 flattening是怎么做到代码扁平化的。

首先使用 opt 进行调试。打开 Flattening.cpp，从第 39 行可以看到注册的 Pass 名称是 flattening；第 45 行调用 toObfuscate判断需要处理的函数是否有 fla标识（为了调试方便，我们将这部分代码注释掉），如果判断有，就调用flatten函数，这个函数是我们分析的关键。Flattening.cpp 文件的内容如下：

```
namespace {
struct Flattening : public FunctionPass {
  static char ID;  // Pass identification, replacement for typeid
  bool flag;

  Flattening() : FunctionPass(ID) {}
  Flattening(bool flag) : FunctionPass(ID) { this->flag = flag; }

  bool runOnFunction(Function &F);
  bool flatten(Function *f);
};
}

char Flattening::ID = 0;
static RegisterPass<Flattening> X("flattening", "Call graph flattening");
Pass *llvm::createFlattening(bool flag) { return new Flattening(flag); }

bool Flattening::runOnFunction(Function &F) {
  Function *tmp = &F;
  // Do we obfuscate
  if (toObfuscate(flag, tmp, "fla")) {
    if (flatten(tmp)) {
      ++Flattened;
    }
  }

  return false;
}
```

在 flatten函数的入口设置断点，在 lldb 后面输入命令`po f->dump()`，打印参数 F，输出 add函数的所有中间层代码，代码如下，为了方便理解，每一行都做了相应注释：

```
; Function Attrs: noinline nounwind ssp uwtable
define i32 @add(i32 %num1, i32 %num2) #0 {

entry:  ;第 1 个 BasicBlock，名称是 entry
    %retval = alloca i32, align 4    ;为返回值分配 4 字节空间
    %num1.addr = alloca i32, align 4 ;为变量 num1.addr 分配 4 字节空间
    %num2.addr = alloca i32, align 4 ;为变量 num2.addr 分配 4 字节空间
    %num3 = alloca i32, align 4 ;为变量 num3 分配 4 字节的空间
    store i32 %num1, i32* %num1.addr, align 4 ;将变量 num1 保存到 num1.addr
    store i32 %num2, i32* %num2.addr, align 4 ;将变量 num2 保存到 num2.addr
    %0 = load i32, i32* %num1.addr, align 4 ;将变量 num1.addr 保存到变量 0
    %cmp = icmp ne i32 %0, 100 ;比较变量 0 是否等于 100
    br i1 %cmp, label %if.then, label %if.end ;如果条件比较成立则会跳转到 if.then

if.then:  ;第 2 个 BasicBlock，名称是 if.then ; preds = %entry
    store i32 0, i32* %retval, align 4
    br label %return   ;跳转到 return

if.end:  ;第 3 个 BasicBlock，名称是 if.end   ; preds = %entry
    %1 = load i32, i32* %num1.addr, align 4  ;将变量 num1.addr 保存到变量 1
    %2 = load i32, i32* %num2.addr, align 4  ;将变量 num2.addr 保存到变量 2
    %add = add nsw i32 %1, %2 ;将变量 1 和变量 2 相加，结果保存到变量 add
    store i32 %add, i32* %num3, align 4 ;将变量 add 保存到变量 num3
    %3 = load i32, i32* %num3, align 4  ;将变量 num3 保存到变量 3
    store i32 %3, i32* %retval, align 4 ;将变量 3 保存到变量 retval
    br label %return ;跳转到 return

return: ;第 4 个 BasicBlock，名称是 return     ; preds = %if.end, %if.then
    %4 = load i32, i32* %retval, align 4
    ret i32 %4
}
```

可以看出，一共有 4 个 BasicBlock，分别是`entry`、`if.then`、`if.end`和`return`。第 63 行是`flatten`
函数要执行的第一条代码，第 63 行和第 64 行的作用是生成随机数（下方代码），这个在后面会用到：

```
62 //生成随机数
63 char scrambling_key[16];
64 llvm::cryptoutils->get_bytes(scrambling_key, 16);
```

第 68 行和第 69 行的作用是将代码中的`switch`语句转换成`if`语句：

```
67  //转换 switch 语句
68 FunctionPass *lower = createLowerSwitchPass();
69 lower->runOnFunction(*f);
```

紧接着，第 72 行到第 80 行的作用是保存原始的`BasicBlock`到`origBB`容器：

```
71  //保存所有原始的 BasicBlock
72  for (Function::iterator i = f->begin(); i != f->end(); ++i) {
73      BasicBlock *tmp = &*i;
74      origBB.push_back(tmp);
75
76      BasicBlock *bb = &*i;
77      if (isa<InvokeInst>(bb->getTerminator())) {
78          return false;
79      }
80  }
```

第 88 行的作用是清空`origBB`容器里的第一个`BasicBlock`，因为第一个`BasicBlock`需要单独处理：

```
87  //清空第一个 BasicBlock
88  origBB.erase(origBB.begin());
89
90  //获取指向第一个 BasicBlock 的指针
91  Function::iteratortmp = f->begin();  //++tmp;
92  BasicBlock *insert = &*tmp;
93
```

第 95 行到第 98 行的作用是判断第一个`BasicBlock`是否含有条件语句，如果有，就获取条件语句的内容，并赋给`br`变量：

```
94  //如果第一个 BasicBlock 含有条件语句
95  BranchInst *br = NULL;
96  if (isa<BranchInst>(insert->getTerminator())) {
97      br = cast<BranchInst>(insert->getTerminator());
98  }
```

获取的内容如下：

```
br i1 %cmp, label %if.then, label %if.end
```

第 100 行到第 107 行的作用是获取第一个`BasicBlock`的倒数第二行：

```
100  if ((br != NULL && br->isConditional()) ||
101      insert->getTerminator()->getNumSuccessors() > 1) {
102      BasicBlock::iterator i = insert->end();
103      --i;
104
105      if (insert->size() > 1) {
106          --i;
107      }
108
```

获取的内容如下：

```
%cmp = icmp ne i32 %0, 100
```

第 109 行的作用是对`BasicBlock`进行分割，第 110 行是将分割后的内容放入`origBB`容器的第一条记录中，还记得第88 行清空了`origBB`容器的第一条记录吧？

```
109      BasicBlock *tmpBB = insert->splitBasicBlock(i, "first");
110      origBB.insert(origBB.begin(), tmpBB);
111  }
112
```

分割后`tmp`得到的内容如下：

```
first:                                   ; preds = %entry
    %cmp = icmp ne i32 %0, 100
    br i1 %cmp, label %if.then, label %if.end
```

分割后`insert`的内容如下：

```
entry:
    %retval = alloca i32, align 4
    %num1.addr = alloca i32, align 4
    %num2.addr = alloca i32, align 4
    %num3 = alloca i32, align 4
    store i32 %num1, i32* %num1.addr, align 4
    store i32 %num2, i32* %num2.addr, align 4
    %0 = load i32, i32* %num1.addr, align 4
    br label %first
```

第 114 行是移除跳转语句，也就是将`br label%first`移除：

```
113  // 移除跳转
114  insert->getTerminator()->eraseFromParent();
```

第 117 行到第 122 行的作用是创建`switch`语句需用的变量`switchVar`，变量的值就是最前面第 63 行和第 64 行随机生成的`scrambling_key`：

```
116  //创建 switchVar，并按其进行设置
117  switchVar = new AllocaInst(Type::getInt32Ty(f->getContext()), 0, "switchVar", insert);
118
119  new StoreInst(
120      ConstantInt::get(Type::getInt32Ty(f->getContext()),
121                       llvm::cryptoutils->scramble32(0, scrambling_key)),
122                       switchVar, insert);
```

创建好`switchVar`之后，再打印`insert`，可以看到其内容的最后多了两条语句：

```
%switchVar = alloca i32
 store i32 1207049111, i32* %switchVar
```

第 125 行的作用是创建`loopEntry`和`loopEnd`，此时里面的代码还是空的。第 128 行是创建一条`load`指令，将`switchvar`放入`loopEntry`中。

```
124  //创建主循环
125  loopEntry = BasicBlock::Create(f->getContext(), "loopEntry", f, insert);
126  loopEnd = BasicBlock::Create(f->getContext(), "loopEnd", f, insert);
127
128  load = new LoadInst(switchVar, "switchVar", loopEntry);
129
130  //在顶部移动第一个 BasicBlock
131  insert->moveBefore(loopEntry);
132  BranchInst::Create(loopEntry, insert);
133
134  //从 loopEnd 跳转到 loopEntry
135  BranchInst::Create(loopEntry, loopEnd);
136
137  BasicBlock *swDefault = BasicBlock::Create(f->getContext(), "switchDefault", f, loopEnd);
138
139  BranchInst::Create(loopEnd, swDefault);
140
141  //创建 switch 语句本身，并设置条件
142  switchI = SwitchInst::Create(&*f->begin(), swDefault, 0, loopEntry);
143  switchI->setCondition(load);
144
145  //移除第一个BasicBlock 中的跳转分支，并且创建一个到 while 循环的跳转
146  f->begin()->getTerminator()->eraseFromParent();
147
148  BranchInst::Create(loopEntry, &*f->begin()); //添加上 br label %loopEntry
```

第 151 行到第 164 行的作用是给`origBB`里每个的`BasicBlock`填充`switch`分支：

```
150  //把所有 BasicBlock 都放入 switch 分支
151  for (vector<BasicBlock *>::iterator b = origBB.begin(); b != origBB.end();
152       ++b) {
153      BasicBlock *i = *b;
154      ConstantInt *numCase = NULL;
155
156      //把 BasicBlock 移动到 switch 内（只是视觉上的，不涉及代码逻辑）
157      i->moveBefore(loopEnd);
158
159      //给 switch 添加 case，switchVar 是随机数
160      numCase = cast<ConstantInt>(ConstantIn...