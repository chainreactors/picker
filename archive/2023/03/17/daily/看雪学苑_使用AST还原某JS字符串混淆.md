---
title: 使用AST还原某JS字符串混淆
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458498394&idx=2&sn=fd306d032aba8028122dc633283eb96b&chksm=b18e85d086f90cc6e7088ff30c61834f8543f3a3885530ba0574437d944211838a1eb18f707b&scene=58&subscene=0#rd
source: 看雪学苑
date: 2023-03-17
fetch_date: 2025-10-04T09:51:31.443937
---

# 使用AST还原某JS字符串混淆

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HvP8HqSZmCQ9Uic7eeeictibPvxsRYcnrmBAhO2d4F6bzhWIRXdRaibsBliaADGTk2O7wfMZRdwRqGomw/0?wx_fmt=jpeg)

# 使用AST还原某JS字符串混淆

DiamondH

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8ER9iaUnzyhu9ol1tfUQH7aian05eibafPxn1dmWFwo6vDic8tbWybIVIfJSTtKKzxl6VyYYanHNVjYpQ/640?wx_fmt=jpeg)

本文为看雪论坛优秀文章

看雪论坛作者ID：DiamondH

背景：在分析某站点接口时发现以前发现漏洞的JS修复后进行了强混淆，看起来十分抽象。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8ER9iaUnzyhu9ol1tfUQH7aialVMaEjhhawWapch44cYRtBteiaibkqpicmAE0OSehHAZZZJ7ia7MKk0epQ/640?wx_fmt=png)

于是乎搁置在一边没有继续分析，直到前几日在图书馆发现了小肩膀大佬写的爬虫混淆AST对抗，书中描述的几种混淆方式与该站点使用的十分相似，遂尝试使用AST对该JS进行一定程度的还原。

本篇针对该JS中的字符串混淆进行还原。

###

### **字符串是如何混淆的**

####

#### 解密方式

想要对字符串反混淆就要先分析该样本是如何对字符串进行混淆的。

以一个字符串的解密为例子，可以发现他将字符串解密拆分成一串函数调用并对立即数进行减法操作来防止通用解密。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8ER9iaUnzyhu9ol1tfUQH7aiaIkOX0WFTnWQVyViaVSMeEN72PZzVFCXOClFSA8uPnhma656fZFVmOLQ/640?wx_fmt=png)

而处于全局作用域的\_0x1f1a68实际上也是对另一个函数的调用。

```
function _0x1f1a68(_0x1be822, _0x79fd7, _0x340561, _0x170aa8, _0x35407a) {    return _0x4903(_0x35407a - 0x252, _0x340561);}
```

经过在VSCode中对每个字符串解密函数查找定义，发现所有的字符串解密最终都是调用的\_0x4903。

由于每个函数的调用时机跟作用域都不同，获取每一个字符串解密函数的结果是不明智的。

于是这里需要实现的第一个功能就是将每一个字符串的解析还原成对\_0x4903的调用，也就是将不同字符串解密函数的调用替换成对最根本的解密函数\_0x4903的幂等形式。

###

### **还原**

####

#### 函数调用还原实现

举个例子：

```
function _0x3cb10b(_0x9056d3, _0xd6da67, _0x4e8aa3, _0x575cfa, _0x50067e) {     return _0x1f1a68(_0x9056d3 - 0x1ca, _0xd6da67 - 0x97, _0x4e8aa3, _0x575cfa - 0x13c, _0xd6da67 - 0x119); }function _0x362f86(_0xeb8495, _0x2bb06b, _0x3bc6ce, _0x59c29b, _0x141499) {    return _0x3cb10b(_0xeb8495 - 0x1a0, _0xeb8495 - -0x370, _0x3bc6ce, _0x59c29b - 0x19c, _0x141499 - 0x120);}function _0x1f1a68(_0x1be822, _0x79fd7, _0x340561, _0x170aa8, _0x35407a) {    return _0x4903(_0x35407a - 0x252, _0x340561);}
```

我们的目标是将

\_0x362f86(0x9a3, 0xef2, '1vkx', 0x369, 0xb40)

转换成

\_0x3cb10b(0x9a3- 0x1a0, 0x9a3 - -0x370, '1vkx', 0x369 - 0x19c, 0xb40 - 0x120);

继而转换成

\_0x1f1a68(0x9a3- 0x1a0 - 0x1ca, 0x9a3 - -0x370 - 0x97, '1vkx', 0x369 - 0x19c - 0x13c, 0x9a3 - -0x370 - 0x119);

最终转换成

\_0x4903(0x9a3 - -0x370 - 0x119 - 0x252, '1vkx');

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8ER9iaUnzyhu9ol1tfUQH7aiaWKvnSkoM603lD8FrpnuxyCFQQjy2ZWicBM6FJaTjo3EenJFt89hZM3g/640?wx_fmt=png)

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8ER9iaUnzyhu9ol1tfUQH7aiakMxUCEXoFck4KwUvKsExQo3p3ZYYiaajYGYLKfxLE1MXSzsiby3vmImQ/640?wx_fmt=png)

那么如何使用AST实现呢，为了尽可能实现上下文无关减少状态，这里采用像示例中的一样一层一层的处理。

在代码实现上我将其分为了多个部分。

```
function replaceArgsToIndex(funcargs, arg) {        if (arg.type == "BinaryExpression") {            return replaceArgsToIndex(funcargs, arg.left);        }        if (arg.name.startsWith("arg")) {            return true;        }        for (let i = 0; i < funcargs.length; i++) {            if (funcargs[i].name == arg.name) {                arg.name = "arg" + i;                return true;            }        }        console.log("not found arg " + arg.name + " at " + arg.loc?.start.line);        return false;}
```

第一步是将函数内的参数名转换成参数下标，这样就可以从CallExpression中直接用下标获取对应的参数进行表达式替换，这里处理了BinaryExpression是因为参数中存在减法表达式的情况，但变量永远在第一位，所以递归到最左面的变量再进行处理，同时如果参数已经被转化成argN的形式便不做处理。

这里放一下关于二值表达式的表示：

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8ER9iaUnzyhu9ol1tfUQH7aiaxIpNmDINefuxiadKcowGXqK0EbibaTNaDPsAiby25wcYZPqQgK4dtKgbw/640?wx_fmt=png)

如图，每个红框都是一个二值表达式，外层的二值表达式将内层的二值表达式作为左值，所以当变量为

xxx - 0x123 -0x456 -0x789

形式时我们要递归的获取左值。

转换后的形式为：

```
function _0x1f1a68(_0x1be822, _0x79fd7, _0x340561, _0x170aa8, _0x35407a) {    return _0x4903(arg4 - 0x252, arg2);}
```

这样就可以检测所有对0x1f1a68的调用，获取其中的第5个参数和第三个参数并把其放入\_0x4903调用的对应位置，然后将0x1f1a68替换为\_0x4903。

将参数下标替换成参数的代码如下：

```
function convertIndexToArg(funcargs, arg) {        if (arg.type == "BinaryExpression") {            return btypes.binaryExpression(arg.operator, convertIndexToArg(funcargs, arg.left), arg.right);        }        if (arg.name.startsWith("arg")) {            let index = parseInt(arg.name.substr(3));            if (index < funcargs.length) {                return funcargs[index];            } else {                console.log("not found arg index with name " + arg.name + " at " + arg.loc?.start.line);            }        } else {            return arg;        }}
```

其中funcargs为CallExpression中的参数,该函数同样递归处理二值表达式。

实现函数展开只需要遍历所有的函数定义，判断是否满足混淆函数的格式，然后通过binding寻找他的调用表达式进行处理，下面为代码实现：

```
let doFlatten = {        FunctionDeclaration(path) {            let refBinding = path.scope.getBinding(path.node.id?.name);            if (!refBinding.referenced) {                path.remove(); //如果函数没有被引用则直接删除并更新作用域                path.scope.crawl();                return;            }            if (path.node.body.body.length != 1) return;            let body = path.node.body.body[0];            if (!btypes.isReturnStatement(body)) return;            let callExp = body.argument;            if (!btypes.isCallExpression(callExp)) return;            //以上三个判断是否满足混淆函数的格式            let calleeArgs = callExp.arguments; //混淆函数里面调用函数的参数            let funcArgs = path.node.params; //混淆函数的参数            for (let arg of calleeArgs) {                let type = arg.type;                switch (arg.type) {                    case "BinaryExpression":                        replaceArgsToIndex(funcArgs, (arg as btypes.BinaryExpression).left as btypes.Identifier); //这里可以不case,已经在replaceArgsToIndex中实现了递归，这里case是为了防止有未预期的形式，但是经过测试不存在该情况                        break;                    case "Identifier":                        replaceArgsToIndex(funcArgs, arg as btypes.Identifier);                        break;                    default:                        console.log("callee arg not recognizable at line: " + path.node.loc?.start.line);                        return;                }            }             let { id } = path.node;            let binding = path.scope.getBinding((id as btypes.Identifier).name);            for (let refer_path of binding!.referencePaths) {                //获取所有调用                if (!btypes.isCallExpression(refer_path.parent)) {                    console.log("abnormal reference at line: " + refer_path.node.loc?.start.line);                    continue;                }                let args = (refer_path.parent as btypes.CallExpression).arguments;                let newArgs: btypes.Expression[] = []; //重组的表调用参数                let argExp: btypes.Expression;                for (let arg of calleeArgs) {                    let type = arg.type;                    switch (arg.type) {                        case "BinaryExpression":                            argExp = convertIndexToArg(args, (arg as btypes.BinaryExpression).left as btypes.Identifier);                            let exp = btypes.binaryExpression((arg as btypes.BinaryExpression).operator, argExp, (arg as btypes.BinaryExpression).right)                            newArgs.push(exp);                            //处理重组，按照嵌套二值表达式的方式组装并把变量参数放在最左边                            break;                        case "Identifier":                            argExp = convertIndexToArg(args, arg as btypes.Identifier);                            newArgs.push(argExp);                            break;                    }                }                let newCallExp = btypes.callExpression(callExp.callee, newArgs);                refer_path.parentPath.replaceWith(newCallExp);//替换callExpression            }            path.parentPath.scope.crawl();            //console.log("modified code: " + codegen["default"](path.node).code);            //path.remove();        }    };    traverse["default"](root, doFlatten);
```

由于每次我们仅处理一层，所以这里多次处理，这样就不必为先后顺序发愁。

```
for (let level = 0; level < 3; level++) {  removeConstFunc(root)}
```

####

#### 字符串函数调用

上一步中我们将字符串混淆替换成了形似\_0x4903(0x9a3 - -0x370 - 0x119 - 0x252, '1vkx');的调用，这一步中我们要将对该函数的调用还原为字符串。

以下为\_0x4903的实现：

```
function _0x4903(_0x41f1e9, _0x3130bc) {    var _0x5e7ec4 = _0x8976();     return _0x4903 = function (_0x899a2d, _0x5835f7)...