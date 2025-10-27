---
title: 利用Python的dis反汇编提取代码对象部分信息
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247506021&idx=1&sn=4251f43313f133c79f962495483210da&chksm=fa520ddbcd2584cdb5d0fc9ae87d5bd0f9c3c90c04186f739e3f1f4505d4860fcb2d2f075c3c&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2024-05-16
fetch_date: 2025-10-06T17:17:41.074588
---

# 利用Python的dis反汇编提取代码对象部分信息

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnSXbeiaMrYyWr1Jdu1UQH3OIzOlZe7GonMeZfnw8jawuXZIIRGZk5WZKFSTnwLdgibRZ8K7rDXa6rCg/0?wx_fmt=jpeg)

# 利用Python的dis反汇编提取代码对象部分信息

原创

c10udlnk

山石网科安全技术研究院

CTF比赛中，Reverse方向经常能遇见一种（可能是唯一一种）只给文本附件的题目，这种题目基本是靠人工阅读理清逻辑、并解出藏在其中的flag，费时费力又不难，因此广受各位出题人的喜爱。

这种题目就是经典的Python字节码文本（通常使用Python自带的dis输出）题，常作为各种比赛的签到题出现。

本文开发了一种手撕字节码工具，从Python的dis反汇编中提取出代码对象所需的信息，并结合xasm工具（https://github.com/rocky/python-xasm/tree/master/xasm）将字节码文本恢复为pyc，从而可以使用成熟的pyc反编译工具（如decompyle3/uncompyle6/pycdc等）获得字节码文本的Python源码。

工具已开源至github：https://github.com/c10udlnk/dis2xasm

## 手撕字节码

### xasm输入的文本格式

PyCodeObject对象的属性在[Python代码保护技术及其破解](https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247503165&idx=1&sn=f8e19feeb529a070422ce99a2120ef4e&scene=21#wechat_redirect)中有介绍，这里针对xasm所需的必要信息进行提取。

经过测试，xasm所需的输入格式如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXbeiaMrYyWr1Jdu1UQH3OIfHxfMPIiasKce5l53ulSNtYHU26ibuVVEpHWdj4zfL0tJmHVeqoMaPoA/640?wx_fmt=png&from=appmsg)

这些信息也是xasm必要的信息，如果缺失会直接导致反编译程序报错退出；其余信息如文件名、firstlineno等为非必要信息，缺失可能导致恢复出的pyc信息有遗漏、进而导致反编译结果不够准确，但测试下来也差别不大。

xasm目前仅支持3.9及以下版本的字节码的汇编，故该工具主要也是针对这些版本的字节码进行信息提取，暂未适配3.10+版本中新增的字节码特性。

### dis反汇编输出的文本格式

而Python自带的dis反汇编输出会剔除很多信息，只有主体的字节码部分，主打一个给人类阅读，不在乎机器能否解析，这也是很多出题人喜欢考它的原因。

Python 3.7+版本的dis新增了`_disassemble_recursive()`，可以递归反汇编co\_consts中的代码对象，因此题目通常使用Python 3.7+版本的`python3 -m dis temp.py`反汇编整个文件的输出作为文本附件。与上文同一个函数，dis的输出如下：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXbeiaMrYyWr1Jdu1UQH3OIibiafbTBz6NbE42PRdlhgtbUcGD3ZPgNVkriaXUCkkNeI4Gqc8AwDbiaOA/640?wx_fmt=png&from=appmsg)

第一行"Disassembly of..."中包含了该函数的函数名、代码对象ID、所属文件名和firstlineno，而剩下就只有字节码的反汇编了，对于其他xasm所需的信息都没有明显地列出。

因此，该工具的主要功能即**通过字节码反汇编提取/推断出Constants、Names、Varnames、Positional arguments、Free variables和Cell variables信息**。

### 信息提取

#### Constants、Names和Varnames

这三个元组的提取相对简单，通过Python自带的opcode可以拿到使用这些元组索引的字节码：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXbeiaMrYyWr1Jdu1UQH3OIIfIvSuJOg2Tlbh0SCiagX5h8wMIRnDmqPxlaHR8Qz8EF7auicic8UYpTg/640?wx_fmt=png&from=appmsg)

不过opcode模块只能获取当前运行的Python版本的信息，而有些时候字节码文本是不知道具体版本的，需要跨版本爆破，所以这里采用xdis（https://github.com/rocky/python-xdis）获取跨版本的opcode信息，在遍历字节码的过程中直接匹配提取即可：

```
# 匹配形同"LOAD_CONST      1 (3)"的反汇编行PTN_ARG = r"([A-Z_]+)\s+(\d+)\s+\((.+)\)"
for i in range(len(asm)): # 遍历字节码    reobj = re.search(PTN_ARG, asm[i])    if reobj is not None:        opcode, idx, arg = reobj.groups()        idx = int(idx)        if op.opmap[opcode] in op.hasconst:            co[CONSTS].update({idx: arg})        elif op.opmap[opcode] in op.hasname:            co[NAMES].update({idx: arg})        elif op.opmap[opcode] in op.haslocal:            co[VARNAMES].update({idx: arg})
```

#### Positional arguments

对于位置参数的识别主要包括两个部分：参数的识别，位置参数和关键字参数的区分。Varnames中按顺序依次包含三种变量名：位置参数、关键字参数和函数中新定义的局部变量（下文中简称局部变量）。所以可以先将Varnames中的参数识别出来，再通过定义和调用函数的字节码区分出关键字参数，剩下的就是位置参数了。

函数中的参数一般是外部传值进来的，不会像局部变量那样在使用之前一定会有STORE，所以我们可以在遍历的时候加一个判断，判断这个局部变量在使用时有没有STORE过，如果没有那说明很大概率就是函数参数，由于在Varnames中两种参数一定在局部变量前，所以记录这样检测出来的索引最大值即可：

```
for i in range(len(asm)):    reobj = re.search(PTN_ARG, asm[i])    if reobj is not None:        opcode, idx, arg = reobj.groups()        idx = int(idx)        # ...        elif op.opmap[opcode] in op.haslocal:            co[VARNAMES].update({idx: arg})            if "STORE" in opcode:                varState.append(idx)            elif idx not in varState: # 使用时检查该变量是否存储过                co[ARGMAX] = max(co[ARGMAX], idx)
```

同时为了提高推断的准确度，也会记录局部变量的索引最小值，已赋值的变量很大概率是局部变量（如果函数中重新赋值了参数，那相当于参数原本的值被覆盖了，此时可以看作是局部变量）。

```
co[LOCMIN] = min(varState) if varState else -1
```

正常情况下，参数索引最大值`ARGMAX`与局部变量索引最小值`LOCMIN`相差`1`（Varnames中参数和局部变量依次排列）。但如果参数或局部变量没有在函数中使用过，那么会有一部分索引对应的数据无法提取，也就无法精准地确定出参数个数，只能通过取`max(ARGMAX, LOCMIN-1)`来推断。值得注意的是，如果函数的参数直接被传入闭包中（而没有在函数中进行任何的调用），也会导致Varnames中参数索引对应的数据缺失。一般的Python程序也不会创建无用变量，所以此处推断的参数个数正常情况下还是很准的；且至于缺失的数据，只能用随机名暂代，可以在反编译后人工纠正。

参数的个数获取以后，接下来是关键字参数的区分。关键字参数会在两个地方出现：

1. 如果关键字参数有设置默认值，那么在`MAKE_FUNCTION`时标志位会设置0x02位：

   在运行栈中，TOS是函数的限定名称，TOS1是函数体的常量，TOS2开始就是标志位标识的常量，顺序为0x08的自由变量元组（下文分辨freevars和cellvars时同理）、0x04的标注字典、0x02的关键字参数默认值字典和0x01的其他参数默认元组。

   ![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXbeiaMrYyWr1Jdu1UQH3OIdejQyJvBjxOsS0ibEyCty1sTStQhn9KKFPg3wRXLicL6kKYOnf9iaRCGg/640?wx_fmt=png&from=appmsg)
2. 没有设置默认值的关键字参数，调用时一定需要指明变量名，所以可以寻找该函数被调用时的字节码，找到`CALL_FUNCTION_KW`前面指定的关键字参数名：

   ![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXbeiaMrYyWr1Jdu1UQH3OI2cmbtb6mHiaSSY8GeMzUQia87XVCXZpaoibjSH0kcfjnP6iaph1JyicBUHg/640?wx_fmt=png&from=appmsg)

如下是一个关键字参数的函数示例：

```
def f(a, b: int, h: int, i=9, *, c: str = "1", f, g=11):    # ...    return
```

查看dis反汇编，`MAKE_FUNCTION`标志位为7，即被设置了0x04、0x02、0x01。那就是往上数三个栈元素，偏移80的`LOAD_CONST`是TOS，偏移78的`LOAD_CONST`是TOS1，我们需要的关键字参数默认值字典是TOS3（设置0x04的标注字典在TOS2）。在这个默认值字典中，最后一次`LOAD_CONST`是涉及的关键字变量名，这里可以获得一部分关键字参数`c`和`g`：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXbeiaMrYyWr1Jdu1UQH3OINicxXhNDxZKvzVzNCTfszAbicHjJYFuHPHZORibVKpkjb78XI2XtluJAA/640?wx_fmt=png&from=appmsg)

该函数被调用时，`CALL_FUNCTION_KW`上方的元组就是关键字参数名，这里可以获得剩下的关键字参数`f`（`c`重复）：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXbeiaMrYyWr1Jdu1UQH3OIDSicZhJyDicaz2F2k6FiaYz6wJib3IBxRHPXhPE9qib1ibcj1uM410iaqibfmg/640?wx_fmt=png&from=appmsg)

通过这种方法，我们可以记录函数的关键字参数，把他们的个数从参数个数中减去即可：

```
argidx = max(co[ARGMAX], co[LOCMIN] - 1)if fn in self.fkwDict.keys():    # ...    argidx -= len(self.fkwDict[fn])co[POSARGS] = argidx
```

Free variables和Cell variables

在字节码中cellvars和freevars位于同一索引列表（该索引列表为cellvars+freevars拼接而成），可以使用xdis中对应版本opcode的hasfree属性筛选出所有的freevars和cellvars：

```
for i in range(len(asm)):    reobj = re.search(PTN_ARG, asm[i])    if reobj is not None:        opcode, idx, arg = reobj.groups()        idx = int(idx)        # ...        elif op.opmap[opcode] in op.hasfree:            co[CELLVARS].update({idx: arg}) # cellvars and freevars
```

freevars是传进闭包函数中供其使用的外部变量，在`MAKE_FUNCTION`时会以元组的形式列出：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXbeiaMrYyWr1Jdu1UQH3OIIRO1ia4HXMZ9397Y5IptqxiaiaqQk4j1cFppBKF99AQDV5P9xGj7UFhsQ/640?wx_fmt=png&from=appmsg)

因此只要遍历到`MAKE_FUNCTION`的标志位设置了0x08位，那么在TOS2就是组成了freevars的元组，例如这里的`(b2, b3, a3, c)`是函数`ccc`的freevars。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXbeiaMrYyWr1Jdu1UQH3OIQZE1iaEuOfnnqnSzF0bSJuA8zicvRNB7YI5wx2KqfxzEAk1G5baZzoAg/640?wx_fmt=png&from=appmsg)

freevars确定以后，就可以将其从cellvars中区分出来：

```
if fn in self.fvDict.keys():    idx_list = [next(k for k, v in co[CELLVARS].items() if v == fv) for fv in self.fvDict[fn]]    idx = min(idx_list)    for k, v in list(co[CELLVARS].items()):        if k >= idx:            co[FREEVARS][k-idx] = v            del co[CELLVARS][k]
```

#### 处理字节码

xasm的字节码格式同dis的相比有一些不同，主要是把同名的函数加了ID做区分（这也导致反编译以后程序可能不能正常运行），去除每行前的偏移值，跳转的">>"符号也被去除，其余差别不影响后续的汇编和反编译，这里简单调整即可：

```
def _adjust_asm(self, asm):    def repl(o):        name, addr = o.groups()        s = list(o.group())        if addr in self.funcMap.keys():            assert name == self.funcMap[addr][0]            name = self.funcMap[addr][1]            ib, ie = [t[1]-t[0] for t in zip(o.regs[0], o.regs[1])]            s[ib:ie] = name        return ''.join(s)    newAsm = asm.replace(">>", "  ")    newAsm = re.sub(PTN_CO, repl, newAsm)    newAsm = re.sub(PTN_LNO, lambda o: f"\n{o.group(1)}:\n", newAsm)    newAsm = re.sub(PTN_BOFF, "\n", newAsm)    return newAsm.strip("\n")
```

### 汇编

xasm工具做的是将这些信息整合起来，最后生成一个CodeType：

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnSXbeiaMrYyWr1Jdu1UQH3OIrb96Ata6icSLl2TXg49bdXiaakROaPLeI6C16H6zUfojSEcoJDiayNWag/640?wx_fmt=png&from=appmsg)

但xasm优秀的地方在于其版本之间的兼容做得非常好，例如Python不同版本之间的CodeType属性不同，如果自己写只能这样，用各个版本的opcode生成对应版本的版本信息，在运行时再读取：

```
try:    with open('version_{}_{}_info.txt'.format(_v[0], _v[1]), 'r') as f:        data = f.read().strip()    def _get_info():        for l in data.split('\n'):            yield l    info = _get_info()    self.argnames = literal_eval(next(info))    attrs = ['hascompare', 'hasconst', 'hasfree', 'hasjabs', 'hasjrel', 'haslocal', 'hasname', 'hasnargs', 'HAVE_ARGUMENT', 'opmap']    for x in attrs:        s...