---
title: 学网安不会rust怎么行，rust学习day1
url: https://mp.weixin.qq.com/s/bsYKjX8GL11VDMiewHieeQ
source: Doonsec's feed
date: 2026-03-29
fetch_date: 2026-03-30T04:41:21.849310
---

# 学网安不会rust怎么行，rust学习day1

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/mHCXPnia0dm1HplKRS5icQibAlwnqATJhyquNP5QFoyV9W2r3xpNsEMfAfOAicY77ic7C4dbcKyejzb1rmLibNS0oouJibqIQ8guanmtg6BYia5hCZs/0?wx_fmt=jpeg)

# 学网安不会rust怎么行，rust学习day1

原创

M0t0y
M0t0y

moonbeautSec

![]()

在小说阅读器中沉浸阅读

这几年来用 Rust 编写的恶意软件数量显著增长，从勒索软件、后门到信息窃取程序都有它的身影。

Rust 的三大优势：

#### 核心优势一：天然的“反分析”能力

这是 Rust 受到攻击者青睐的最重要原因。Rust 的一些特性，意外地为恶意软件穿上了“隐形衣”：

* **复杂的二进制结构，让传统工具“失灵”**：Rust 编译出的二进制文件通常**静态链接**所有依赖，导致文件体积巨大、包含海量函数。例如，一个简单的 C++ 程序可能只有不到 100 个函数、20KB 大小，而功能相同的 Rust 程序却有近 10,000 个函数、超过 3MB。这让安全分析师在 IDA Pro、Ghidra 等传统反编译工具中，难以从海量的 Rust 标准库代码里，定位到攻击者自己写的核心恶意代码。即使微软这样的巨头，也需要专门开发像 **RIFT** 这样的新工具来辅助分析 Rust 恶意软件。
* **内存安全特性，让程序行为更“规整”**：Rust 引以为傲的**所有权模型**和**生命周期检查**，消除了 C/C++ 中常见的指针错误和内存碎片，使程序执行路径非常清晰。这对正常开发是巨大的优点，但放到恶意软件分析里，就**抹去了许多因内存错误导致的“混乱”特征**，让分析人员更难找到突破口。
* **更强的反调试和混淆手段**：Rust 允许开发者使用 `unsafe` 关键字和内联汇编 (`asm!`)，直接操作内存和硬件。攻击者可以利用这些特性，在代码中**轻易地实现复杂的字符串混淆和 API 调用隐藏**，让静态分析举步维艰。

#### 核心优势二：卓越的“跨平台”能力，让攻击范围更广

Rust 的生态支持**轻松交叉编译**，一套代码库可以毫无障碍地编译成 Windows、Linux、macOS 甚至 Android 等多个平台的可执行程序。

这意味着，攻击者可以开发一个跨平台的木马，对使用 Windows 的办公电脑和使用 Linux 的服务器进行无差别攻击，极大地提升了攻击效率。像臭名昭著的伊朗 APT 组织 **MuddyWater**，就在其最新的攻击活动中，弃用了过去的 PowerShell 脚本，转而使用 Rust 开发的 **RustyWater** 后门，目的就是为了更好地跨平台运行并规避检测。

#### 核心优势三：优秀的“性能与稳定性”，让恶意软件更“可靠”

Rust 的性能媲美 C/C++，且没有垃圾回收机制，内存占用可控。对于需要高效执行、稳定运行的勒索软件或后门来说，Rust 能确保它们在被感染的主机上“安静”且“可靠”地工作，不易因自身崩溃而被发现。例如，臭名昭著的 **BlackCat (ALPHV)** 勒索软件是最早一批用 Rust 编写的重量级恶意软件之一，其运行效率极高。

用 Rust 编写恶意软件，也代表了一种工具链的全面“现代化升级”。一些知名的恶意软件家族正在进行“技术栈更新”：

| 恶意软件家族 | 原始语言 | Rust 重写版本/变种 | 主要变化 |
| --- | --- | --- | --- |
| **AsyncRAT** | C# | RustyAsyncRAT | 功能基本不变，但逆向分析难度陡增，且处于积极开发中 |
| **Buer** | C | RustyBuer | 核心功能不变，但成功绕过了许多针对 C 语言版本的检测规则 |
| **Xworm** | 未明确 | Rust Loader + Xworm | 加载器用 Rust 编写，用于下载并注入最终的后门载荷 |
| **未知信息窃取器** | - | EDDIESTEALER | 完全用 Rust 编写，使用了复杂的字符串和 API 混淆，通过伪造验证码页面传播 |

Rust 本身的**内存安全**设计是为了**防止开发者犯错**，写出更安全的系统软件。问题在于，这些优秀的设计理念，被攻击者“滥用”到了恶意软件开发中，变成了保护自己恶意代码的利器。

学习rust也是网络安全中必要的一环吧只能说

上来先关闭vscode的代码补全，不然全给我补全了，我还学个蛋

![image-20260329103055473](https://mmbiz.qpic.cn/sz_mmbiz_png/mHCXPnia0dm2MsQJUjPOXh0yL2sZShaw2cYrpoNqjQwbYHwvGS2cWtAxHDRicRib33teWLia16hrrRluWAW4CMp5IrsEAYaziaUS5lIfUdH3ib4a0/640?wx_fmt=png&from=appmsg)

image-20260329103055473

我是先看了菜鸟教程的rust基础语法后大概学习了一下

环境安装这里就不写了，网上教程也很多

不动手是不行的，自己开始动手编写，这里我让`deepseek`给我制定了第一天的计划，我还用了`gemini`，两个给的建议其实差不多

首先是

![image-20260329111539933](https://mmbiz.qpic.cn/mmbiz_png/mHCXPnia0dm1n3CG6SjhhmJMqhsH9bO9G7rD9fISE3muibzmrDsG9u2zZvldevbGxwoiaIDgmhZqz7SaZ9oVjXaHGadQsgODfY1YYuIq7u6BW4/640?wx_fmt=png&from=appmsg)

image-20260329111539933

新建项目，编写第一个打印字符串

```
fn main(){
    println!("Hello, world!");
}
```

第一种方式

编译

```
rustc .\first_rust_program.rs
```

运行

```
.\first_rust_program.exe
```

![image-20260329105000029](https://mmbiz.qpic.cn/mmbiz_png/mHCXPnia0dm2xSLz0WJpJnaKibvxXuQ4fC2B7pdpJTICHf7ia93DzrLbWdk49pW5olagW7NulXvs8DiaUb9ibNoIOaHDcDYicibdhfrTWFJ3ib00BicA/640?wx_fmt=png&from=appmsg)

image-20260329105000029

第二种方式

创建新项目

```
cargo new day1
```

运行

```
cargo run .\src\main.rs
```

![image-20260329105256747](https://mmbiz.qpic.cn/mmbiz_png/mHCXPnia0dm22etaVEEic3Hw7cznX9dZqictUnTReu5R3bria8VyAXJKcqajpFQtoDicB48yBq8djJPB7Ciao8GN8vBrxT2BJWEfFrx5iaiaZCbTHjk/640?wx_fmt=png&from=appmsg)

image-20260329105256747

既然 `rustc` 可以直接编译代码，为什么还要用 `cargo`？

**`rustc` 是编译器，负责把单个文件变成可执行文件；而 `cargo` 是项目构建工具和包管理器，负责管理整个项目的方方面面**。

可以把 `rustc` 想象成“砌墙的砖刀”，而 `cargo` 则是“完整的施工队+物料管理系统”。

---

#### Cargo 的核心优势

##### 1. **自动管理依赖**

当需要用到第三方库（在 Rust 中叫 **crate**）时，比如处理 JSON、网络请求等，`cargo` 只需你在 `Cargo.toml` 里写一行：

```
[dependencies]
serde = "1.0"
```

然后运行 `cargo build`，它会自动下载、编译并链接这个库及其所有依赖。
如果用 `rustc`，你需要手动下载源码、配置库路径、链接库文件，非常繁琐且容易出错。

##### 2. **统一项目结构，约定优于配置**

Cargo 约定了标准的项目目录：

```
my_project/
├── Cargo.toml      # 配置文件
├── src/
│   └── main.rs     # 源码
└── target/         # 编译产物
```

所有 `Rust` 项目都长这样，你打开任何一个开源 `Rust` 项目都能立刻明白结构。不需要自己创建 `Makefile` 或配置复杂的编译参数。

##### 3. **一键执行常见任务**

* `cargo run` – 编译并运行
* `cargo test` – 运行所有测试
* `cargo build --release` – 生成优化后的发布版本
* `cargo doc --open` – 生成并打开项目文档
* `cargo fmt` – 自动格式化代码
* `cargo clippy` – 代码风格检查

这些命令背后可能涉及多个编译步骤、环境变量设置、测试执行等，但 `cargo` 帮你全部封装好了。

##### 4. **跨平台一致性**

无论在 Windows、macOS 还是 Linux 上，`cargo` 的命令和行为完全一致。你不需要为不同平台编写不同的编译脚本。

##### 5. **便于分享和复用**

通过 `cargo publish` 可以把自己的库发布到 crates.io，全世界的 Rust 开发者都能轻松使用你的代码。

---

##### 什么时候可以只用 `rustc`？

虽然 `cargo` 是主流，但在极少数情况下 `rustc` 更合适：

* 写一个单文件的极简脚本（比如几十行的测试代码）
* 学习编译器底层，想看看 `rustc` 的输出
* 嵌入式环境或特殊构建需求（但即便这些场景，往往也会用 `cargo` 配合 `.cargo/config.toml`）

也是入门rust了，hhh

接下来就是学习rust中的基础数据类型和变量

![image-20260329111815010](https://mmbiz.qpic.cn/sz_mmbiz_png/mHCXPnia0dm0dNpgwXz8gNbygIeZauxc9xoSxMp8PY3xEYkWpCk5icQWs4u7RUwVKNibC5hNy8ftAQtfVaicWr1xHEAD8TjxqbDGn2HseibTxKeI/640?wx_fmt=png&from=appmsg)

image-20260329111815010

首先要知道Rust 中变量**默认是不可变的**。可变变量需要使用 `let mut` 声明，这样设计是为了安全和并发考虑的。

Rust 是强类型语言，但具有自动判断变量类型的能力。这很容易让人与弱类型语言产生混淆。

如果要声明变量，需要使用 **let** 关键字。例如：

```
let a = 123;
```

默认情况下，Rust 中的变量是不可变的，除非使用 mut 关键字声明为可变变量。

```
let a = 123;       // 不可变变量
let mut b = 10;  // 可变变量
```

那这里既然不可变变量是不可变的，那不就是常量吗？为什么叫变量？

变量和常量还是有区别的。在 Rust 中，以下程序是合法的：

```
let a = 123;   // 可以编译，但可能有警告，因为该变量没有被使用
let a = 456;
```

但是如果 a 是常量就不合法：

```
const a: i32 = 123;
let a = 456;
```

变量的值可以"重新绑定"，但在"重新绑定"以前不能私自被改变，这样可以确保在每一次"绑定"之后的区域里编译器可以充分的推理程序逻辑。 虽然 Rust 有自动判断类型的功能，但有些情况下声明类型更加方便：

```
let a: u64 = 123;
```

这里声明了 a 为无符号 64 位整型变量，如果没有声明类型，a 将自动被判断为有符号 32 位整型变量，这对于 a 的取值范围有很大的影响。

这里需要注意的是：

当你使用 `let` 声明变量时，Rust 编译器会启用了**类型推导**。它看到等号右边是一个整数 `1`，就会自动推断出 `a` 的类型是 Rust 默认的 32 位有符号整数（`i32`）。

```
let a = 1;   // 合法的
```

所以编译器在底层把代码补全成了：

```
let a: i32 = 1;
```

对于 `const`，Rust 的设计哲学是“明确且绝对安全”。常量通常会被定义在全局作用域中，供程序的各个模块使用。为了保证编译速度和代码的绝对清晰，Rust 强制要求：**定义常量时，必须显式地写出数据类型，绝不让编译器去猜。**

正确的常量定义方式必须加上类型注解：

```
const A: i32 = 1; // 这是合法的
```

数据类型

Rust 是静态类型语言，在变量声明时可以显式指定类型，但通常可以依赖类型推断。

**基本类型:** i32 (32位有符号整数), u32 (32位无符号整数), f64 (64位浮点数), bool (布尔类型), char (字符)

```
let x: i32 = 1;
let y: f64 = 3.14;
let is_true: bool = true;
let letter: char = 'A';
```

其他的函数定义控制流和其他语言也差不多

Rust 函数通过 **fn** 关键字定义，函数的返回类型通过箭头符号 **->** 指定。

```
fn add(a: i32, b: i32) -> i32 {
    a + b
}
```

如果函数没有返回值，类型默认为 ()（即空元组）。

理论先到这里，然后安装`Rustlings`练习

安装教程：

我这里自动安装就是不成功，我还是选择手动安装了，根据官方中文文档安装了半天，怎么都启动不了，搞半天是文档不是最新的

我服了，这里搞了半天发现文档没更新，本地下载的老版本（v5.5.1）有冲突，

在终端里直接运行这行命令：

```
cargo install rustlings
```

*这会自动下载最新版，最新版已经彻底修复了这个依赖冲突。*

或者是

运行：`cargo update`

然后再运行你的安装命令：`cargo install --force --path .`

![image-20260329123015991](https://mmbiz.qpic.cn/mmbiz_png/mHCXPnia0dm0WQGbvj8uibNFl5Vh57vskUg7bT10ibAeaClbOvonQGRKPuhDTCCjGVs31WggJukHFrNwAF3XCs0CHSkwke2eibc0Cu2nvaCy9x0/640?wx_fmt=png&from=appmsg)

image-20260329123015991

安装完成后

**新建一个纯英文的练习文件夹并进去**

```
mkdir rust_practice
cd rust_practice
```

在这个干净的目录下初始化题库

```
rustlings init
```

*(这时候它会在 `rust_practice` 里新建一个叫做 `rustlings` 的文件夹，并把最新的题目拉取下来。)*

进入题库目录，正式启动！

```
cd rustlings
rustlings
```

![](https://mmbiz.qpic.cn/sz_mmbiz_png/mHCXPnia0dm2ATvCT3q5WssXAvXuX1Wu1mBsHwJ1AAacwr282q2O0ibOQAwHhJywD9CzqGwvegmJ6C7RFKHDoPfn2ufZem2FwYjRsJTLxYFLs/640?wx_fmt=png&from=appmsg)

终于可以启动了

接下来在`vscode`中打开这个文件来进行修改

第一关：

![image-20260329124347809](https://mmbiz.qpic.cn/sz_mmbiz_png/mHCXPnia0dm30n8J43YIzpe3QH9392jZBkbvq68IFxuNSLribIABAhzib0TECFhK2oGASypvAicrJuB74r91UFicQ8qw8ib0k84cZmQicXY8gyAjME/640?wx_fmt=png&from=appmsg)

image-20260329124347809

应该是`println!`而不是`printline!`

修改后保存，`rustlings`会自动检测到文件的更改并重新运行该练习。如果所有错误都被修复了，`Rustlings` 会提示你进入下一题。

![image-20260329124511568](https://mmbiz.qpic.cn/mmbiz_png/mHCXPnia0dm0qYjxNKQS8mcZo7EHqWR98KJ0FB3Z1ibj7mAbd1qTlItlWcD6KiaFhGNQtRHIIbsbthubwurjDhY3gIFKOGpsXGiaDuiaX2SvkmqU/640?wx_fmt=png&from=appmsg)

image-20260329124511568

第二关

![image-20260329124735584](https://mmbiz.qpic.cn/mmbiz_png/mHCXPnia0dm18xBuibktyibYEfiaZUY0IvWFibx4e7wGhOhAwIgoicrT4QU7fgybmmIL1zcvmo0eaQmMQnFWktfuBzcDRehcicbLFRyo1YiabDun2j8/640?wx_fmt=png&from=appmsg)

image-20260329124735584

这里有两种方式

第一种将`x`定义为常量

```
const x: i32 = 5;
```

也是可以成功通过的

![image-2026032912492...