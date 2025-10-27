---
title: Chrome v8 pwn 前置
url: https://forum.butian.net/share/3804
source: 奇安信攻防社区
date: 2024-10-15
fetch_date: 2025-10-06T18:46:41.745110
---

# Chrome v8 pwn 前置

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

### Chrome v8 pwn 前置

Chrome v8

参考
==
[官方文档](https://v8.dev/docs/build-gn#v8gen)
[Chrome v8 pwn](https://blog.csdn.net/qq\_45323960/article/details/130124693)
[官方V8源码](https://chromium.googlesource.com/v8/v8/)
[浏览器入门之starctf-OOB](https://e3pem.github.io/2019/07/31/browser/%E6%B5%8F%E8%A7%88%E5%99%A8%E5%85%A5%E9%97%A8%E4%B9%8Bstarctf-OOB/)
[browser pwn入门（一](https://bbs.kanxue.com/thread-279859.htm)
[V8 Pwn Basics 2: TurboFan](https://blog.wingszeng.top/v8-pwn-basics-2-turbofan/#turbofan)
[V8 Pwn Basics 1: JSObject](https://blog.wingszeng.top/v8-pwn-basics-1-jsobject/#%E7%BC%96%E5%8F%B7%E5%B1%9E%E6%80%A7-elements)
简介
==
v8 是 Google 用 C++ 开发的一个开源 JavaScript 引擎. 简单来说, 就是执行 js 代码的一个程序. Chromium, Node.js 都使用 v8 解析并运行 js.
v8是chrome浏览器的JavaScript解析引擎,v8编译后二进制名称叫d8而不是v8
JavaScript 是解释语言, 需要先翻译成字节码后在 VM 上运行. V8 中实现了一个 VM. 出于性能考虑, 目前的引擎普遍采用一种叫做 Just-in-time (JIT) 的编译技术, V8 也是. JIT 的思想在于, 如果一段代码反复执行, 那么将其编译成机器代码运行, 会比每次都解释要快得多.
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-a5f93701b35f0d65f0d95b97e440e66b47fe3237.png)
V8引擎处理JavaScript代码的流程:
假设我们有以下JavaScript代码:
```javascript
function add(a, b) {
return a + b;
}
console.log(add(5, 3));
```
1. 解析(Parser):
Parser会将这段代码转换为抽象语法树(AST)。AST大致如下:
```php
Program
├── FunctionDeclaration (add)
│ ├── Params (a, b)
│ └── ReturnStatement
│ └── BinaryExpression (+)
│ ├── Identifier (a)
│ └── Identifier (b)
└── ExpressionStatement
└── CallExpression (console.log)
└── CallExpression (add)
├── NumberLiteral (5)
└── NumberLiteral (3)
```
2. 解释(Interpreter - Ignition):
Ignition解释器会将AST转换为字节码。简化的字节码可能如下:
```php
DEFINE\_FUNCTION add
GET\_ARG a
GET\_ARG b
ADD
RETURN
CALL add 5 3
CALL console.log
```
Ignition会在VM中执行这些字节码。
3. 非优化编译(Sparkplug):
如果函数被多次调用,Sparkplug会将字节码快速编译成简单的机器码,以提高执行速度。
4. 优化编译(Compiler - TurboFan):
如果函数被频繁调用,TurboFan会对其进行更深入的分析和优化,生成高度优化的机器码。例如,它可能会将add函数内联到调用处,消除函数调用开销。
环境搭建
====
[https://storage.googleapis.com/chrome-infra/depot\\_tools.zip](https://storage.googleapis.com/chrome-infra/depot\_tools.zip)
[https://blog.csdn.net/qq\\_61670993/article/details/135276209?ops\\_request\\_misc=%257B%2522request%255Fid%2522%253A%2522171940779116800184121422%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request\\_id=171940779116800184121422&amp;biz\\_id=0&amp;utm\\_medium=distribute.pc\\_search\\_result.none-task-blog-2~blog~first\\_rank\\_ecpm\\_v1~rank\\_v31\\_ecpm-1-135276209-null-null.nonecase&amp;utm\\_term=v8&amp;spm=1018.2226.3001.4450](https://blog.csdn.net/qq\_61670993/article/details/135276209?ops\_request\_misc=%257B%2522request%255Fid%2522%253A%2522171940779116800184121422%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fblog.%2522%257D&amp;request\_id=171940779116800184121422&amp;biz\_id=0&amp;utm\_medium=distribute.pc\_search\_result.none-task-blog-2~blog~first\_rank\_ecpm\_v1~rank\_v31\_ecpm-1-135276209-null-null.nonecase&amp;utm\_term=v8&amp;spm=1018.2226.3001.4450)
depot\\_tools和ninja
------------------
出现找不到vpython3和python3的情况是网络问题更换下代理,重试就好了
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-4bd6e314411c07e9954126b8c6095087caf08b7b.png)
使用ubuntu 20.04 搭建方便些 18.04很多东西搭环境麻烦
```c
sudo apt install bison cdbs curl flex g++ git python vim pkg-config
git clone https://chromium.googlesource.com/chromium/tools/depot\_tools.git
echo 'export PATH=$PATH:"/path/to/depot\_tools"' &gt;&gt; ~/.bashrc
cd depot\_tools
git reset --hard 138bff28
export DEPOT\_TOOLS\_UPDATE=0
gclient 建议每次 gclient 前设置环境变量 export DEPOT\_TOOLS\_UPDATE=0
cd ..
git clone https://github.com/ninja-build/ninja.git
cd ninja &amp;&amp; ./configure.py --bootstrap &amp;&amp; cd ..
echo 'export PATH=$PATH:"/path/to/ninja"' &gt;&gt; ~/.bashrc
fetch v8 或者fetch --force v8
cd v8
gclient sync -D git checkout 7.6.303.28 更换v8版本
./build/install-build-deps.sh 安装相关依赖，如果遇到下载字体未响应问题需要添加 --no-chromeos-fonts 参数
./tools/dev/v8gen.py x64.release 设置配置 最好选择 release 版本 因为 debug 版本可能会有很多检查
./tools/dev/v8gen.py x64.debug
ninja -C out.gn/x64.release 利用生成的配置来编译
ninja -C out.gn/x64.debug
```
ninja编译的最后在 ./out.gn/x64.debug/ 或 ./out.gn/x64.release/ 目录下
或者
```bash
执行 ./tools/dev/gm.py x64.release 可以使用预设的选项编译 release 版本, 将 release 换成 debug 可以编译 debug 版本. 这样编译出来的文件在 ./out/x64.release 或者 ./out/x64.debug 下.
也可以自行设置编译选项, 然后编译. 用 ./tools/dev/v8gen.py $target.$version -- options 来生成 $target 架构的 $version 版本的配置文件. 如 ./tools/dev/v8gen.py x64.release. 生成的文件会在 ./out.gn/ 下的对应目录里. 更多用法可以看 官方文档.
```
无论是用 gm 还是 v8gen, 生成的文件中包含一个编译选项. 在 ./out/ 或者 ./out.gn/ 对应目录下的 args.gn.
turbolizer
----------
完全卸载并重新安装 Node.js 和 npm： 首先，卸载现有的 Node.js：
然后，重新安装：
```bash
curl -fsSL https://deb.nodesource.com/setup\_lts.x | sudo -E bash -
sudo apt-get install -y nodejs
```
检查安装：
安装完成后，检查 Node.js 和 npm 的版本：
```bash
node -v
npm -v
```
```bash
cd v8/tools/turbolizer
npm i
npm run-script build
python -m SimpleHTTPServer
```
调试
==
```javascript
var a = [1,2,3,1.1];
%DebugPrint(a);
%SystemBreak();
```
```c
在 ~/.gdbinit 内添加以下两行可使用V8附带的调试插件：
source /path/to/v8/tools/gdbinit
source /path/to/v8/tools/gdb-v8-support.py
```
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-14b3b3755bb34a4decb0264e2a8c13033853bfd8.png)
```bash
jl 别名已经存在，查看 tools/gdbinit 发现：
#alias jlh = print-v8-local
alias jl = print-v8-local
```
```bash
gdb ./d8
set args --allow-natives-syntax ./exp.js
```
&gt; d8 带 --allow-natives-syntax 启动参数的话，则可以在 js 脚本中写一些调试用的函数，这些函数通常以 % 开头，如 %DebugPrint() 显示对象信息，%DebugPrintPtr() 显示指针指向的对象信息，%SystemBreak() 下断点等。在 src/runtime/runtime.h 中可以找到所有的 natives syntax。
调试的时候可以在js文件里面使用%DebugPrint();以及%SystemBreak();其中%SystemBreak();的作用是在调试的时候会断在这条语句这里，%DebugPrint();则是用来打印对象的相关信息，在debug版本下会输出很详细的信息。
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-db9dfb147ff3b70f0e48632f25c41d05bf2fbe8e.png)
&gt; is\\_debug = true 编译选项会设置 DCHECK 宏, 它负责一些简单的安全检查, 如判断数组是否越界. 而题目往往编译的 release 版本, 如果在利用中有这种行为, 不会有什么影响. 但是用 debug 版本调试时会直接 assert. 不幸的是没有选项能够取消设置 DCHECK. 如果还需要在 debug 版本下调试以获得良好体验的话, 可以手动 patch 一下. 在 src/base/logging.h 中找到 DCHECK 定义的地方:
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-b8225a7d9c5493e73650dc733d0f9c809a5cc791.png)
turbolizer使用
============
```javascript
function add(x, y) {
return x + y;
}
for (let i = 0; i &lt; 10000; i++) {
add(i, i + 1);
}
%OptimizeFunctionOnNextCall(add);
console.log(add(1, 2));
```
```bash
./d8 exp.js --allow-natives-syntax --trace-turbo
```
- --trace-turbo：
这是一个 V8 标志，用于启用 TurboFan（V8 的优化编译器）的跟踪功能。
它会生成详细的优化过程信息，包括中间表示（IR）图和各种优化阶段。
- --trace-turbo-path=/path/to/output：
这个标志指定了 Turbo 跟踪输出的路径。
/path/to/output 应该替换为你想保存输出文件的实际路径。
输出通常是一个 JSON 文件，包含了优化过程的详细信息。
- your\\_script.js：
这是你要运行和分析的 JavaScript 文件的名称。
d8 将执行这个文件，同时生成优化跟踪信息。
1. d8 加载并执行 your\\_script.js。
2. 在执行过程中，V8 引擎会对代码进行优化。
3. 由于启用了 --trace-turbo，V8 会记录优化过程中的各个阶段。
4. 这些记录会被保存到 --trace-turbo-path 指定的路径中。
5. 生成的 JSON 文件可以用 Turbolizer 工具来可视化和分析。
之后本地就会生成turbo.cfg和turbo-xxx-xx.json文件
然后启动服务提交json文件
![图片.png](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/09/attach-2bf6909cc4b9b55c4881f1e018021e79b066748e.png)
更多优化标志
```bash
--trace-opt 打印编译优化信息
--trace-deopt
--print-opt-code
```
结构
==
数组 Array
========
数组是JS最常用的class之一，它可以存放任意类型的js object。
有一个 length 属性，可以通过下标来线性访问它的每一个元素。
有许多可以修改元素的接口。
当元素为object时，只保留指针。
Array 示例:
```javascript
// 创建一个数组
let fruits = ['apple', 'banana', 'orange'];
// 使用下标访问元素
cons...