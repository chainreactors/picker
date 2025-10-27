---
title: Makefile 简明指南 - potatso
url: https://www.cnblogs.com/potatso/p/18844501
source: 博客园 - potatso
date: 2025-04-25
fetch_date: 2025-10-06T22:03:56.601769
---

# Makefile 简明指南 - potatso

[![](https://img2024.cnblogs.com/blog/35695/202509/35695-20250929100304557-587378723.jpg)](https://qoder.com/)

* [![博客园logo](//assets.cnblogs.com/logo.svg)](https://www.cnblogs.com/ "开发者的网上家园")
* [会员](https://cnblogs.vip/)
* [众包](https://www.cnblogs.com/cmt/p/18500368)
* [新闻](https://news.cnblogs.com/)
* [博问](https://q.cnblogs.com/)
* [闪存](https://ing.cnblogs.com/)
* [赞助商](https://www.cnblogs.com/cmt/p/19081960)
* [HarmonyOS](https://harmonyos.cnblogs.com/)
* [Chat2DB](https://chat2db-ai.com/)

* ![搜索](//assets.cnblogs.com/icons/search.svg)
  ![搜索](//assets.cnblogs.com/icons/enter.svg)
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    所有博客
  + ![搜索](//assets.cnblogs.com/icons/search.svg)

    当前博客
* [![写随笔](//assets.cnblogs.com/icons/newpost.svg)](https://i.cnblogs.com/EditPosts.aspx?opt=1 "写随笔")
  [![我的博客](//assets.cnblogs.com/icons/myblog.svg)](https://passport.cnblogs.com/GetBlogApplyStatus.aspx "我的博客")
  [![短消息](//assets.cnblogs.com/icons/message.svg)](https://msg.cnblogs.com/ "短消息")
  ![简洁模式](//assets.cnblogs.com/icons/lite-mode-on.svg)

  [![用户头像](//assets.cnblogs.com/icons/avatar-default.svg)](https://home.cnblogs.com/)

  [我的博客](https://passport.cnblogs.com/GetBlogApplyStatus.aspx)
  [我的园子](https://home.cnblogs.com/)
  [账号设置](https://account.cnblogs.com/settings/account)
  [会员中心](https://vip.cnblogs.com/my)
  简洁模式 ...
  退出登录

  [注册](https://account.cnblogs.com/signup)
  登录

[potatso](https://www.cnblogs.com/potatso)

* [博客园](https://www.cnblogs.com/)
* [首页](https://www.cnblogs.com/potatso/)
* [新随笔](https://i.cnblogs.com/EditPosts.aspx?opt=1)
* [联系](https://msg.cnblogs.com/send/potatso)
* 订阅
* [管理](https://i.cnblogs.com/)

# [Makefile 简明指南](https://www.cnblogs.com/potatso/p/18844501 "发布于 2025-04-24 14:16")

# Makefile 简明指南

# 一. Makefile变量

在 Makefile 里，你可以通过不同方式来声明新变量 `ne`。在 Makefile 里，变量声明时等号（`=`、`:=`、`+=`、`?=`）两边的空格是可选的，加空格或者不加空格都不会影响变量的赋值。下面是常见的几种声明方式及其特点：

### **1. 递归展开变量赋值（`=`）**

在 Makefile 里，递归展开变量是借助 `=` 符号或者 `define` 指令来定义的。这种变量赋值方式的显著特点是：在定义变量时，所指定的值会按原样保存，若其中包含对其他变量的引用，这些引用不会马上展开，而是在该变量被使用（也就是在扩展其他字符串的过程中进行替换）时才会展开，这一过程被称作递归展开。

**基本的递归展开示例**

```
foo = $(bar)
bar = $(ugh)
ugh = Huh?

all:
    @echo $(foo)
```

在这个例子中，`foo` 被定义为 `$(bar)`，在定义时 `$(bar)` 不会展开。当 `make` 执行到 `@echo $(foo)` 时，`$(foo)` 会先展开为 `$(bar)`，接着 `$(bar)` 展开为 `$(ugh)`，最终 `$(ugh)` 展开为 `Huh?`。所以运行 `make` 后，输出结果为 `Huh?`。

**优点：组合变量值**

```
CFLAGS = $(include_dirs) -O
include_dirs = -Ifoo -Ibar

all:
    @echo "CFLAGS: $(CFLAGS)"
```

此例展示了递归展开变量的一个优点。当在规则里展开 `CFLAGS` 时，`$(include_dirs)` 会展开为 `-Ifoo -Ibar`，所以 `CFLAGS` 最终展开为 `-Ifoo -Ibar -O`。运行 `make` 后，输出结果为 `CFLAGS: -Ifoo -Ibar -O`。

**缺点：无限循环**

```
CFLAGS = $(CFLAGS) -O

all:
    @echo $(CFLAGS)
```

这体现了递归展开变量的一个主要缺点。`CFLAGS` 定义为 `$(CFLAGS) -O`，在展开 `CFLAGS` 时，由于它引用了自身，会造成无限循环。不过，`make` 能够检测到这种无限循环并报告错误。

递归展开变量虽然有组合变量值等优点，但也存在容易引发无限循环、函数多次执行导致结果不可预测和运行速度变慢等缺点。在编写 Makefile 时，需要根据具体需求谨慎使用递归展开变量。

### **2. Makefile 中的简单展开变量（`:=`）**

在 Makefile 里，简单展开变量是通过 `:=` 或 `::=` 来定义的。其核心特性为：在变量定义阶段，就会对变量值里引用的其他变量和函数进行展开，并且展开完成后，变量值便固定下来，后续使用时不会再次展开。

下面通过几个示例来深入理解简单展开变量：

**基本示例**

```
x := foo
y := $(x) bar
x := later

all:
    @echo "Value of y: $(y)"
```

在这个例子中，当定义 `y := $(x) bar` 时，`$(x)` 会立即展开为 `foo`，所以 `y` 的值是 `foo bar`。即便后续 `x` 被重新赋值为 `later`，`y` 的值也不会受到影响。运行 `make` 后，输出结果为 `Value of y: foo bar`。

**结合函数的示例**

```
files := $(wildcard *.c)
objects := $(patsubst %.c,%.o,$(files))

all:
    @echo "Source files: $(files)"
    @echo "Object files: $(objects)"
```

此例中，`files := $(wildcard *.c)` 会在定义时执行 `wildcard` 函数，将当前目录下所有 `.c` 文件的名称赋给 `files` 变量。接着，`objects := $(patsubst %.c,%.o,$(files))` 会执行 `patsubst` 函数，把 `files` 里的 `.c` 文件名替换为 `.o` 文件名，然后赋给 `objects` 变量。后续使用 `files` 和 `objects` 时，它们的值不会再次展开。

**避免无限循环示例**

```
CFLAGS := $(CFLAGS) -O

all:
    @echo "CFLAGS: $(CFLAGS)"
```

若使用递归展开变量（`=`），`CFLAGS = $(CFLAGS) -O` 会造成无限循环。但使用简单展开变量（`:=`），`CFLAGS` 初始为空，定义时展开后 `CFLAGS` 的值就是 `-O`，避免了无限循环问题。运行 `make` 后，输出结果为 `CFLAGS: -O`。

### **3. 追加赋值（`+=`）**

若你要在已有变量值的基础上追加内容，就可以使用追加赋值（`+=`）。

```
ne = first
ne += second
all:
    @echo $(ne)
```

在这个例子里，`ne` 变量最初的值是 `first`，使用 `+=` 后追加了 `second`，最终执行 `make all` 会输出 `first second`。

### **4. 条件赋值（`?=`）**

条件赋值（`?=`）只有在变量未被赋值时才会进行赋值操作。

```
ne ?= default
all:
    @echo $(ne)
```

在这个例子中，由于 `ne` 之前未被赋值，所以它会被赋值为 `default`。若 `ne` 之前已经有了值，那么使用 `?=` 就不会改变其原有的值。

# 二. 取消/删除Makefile变量

在 Makefile 中取消一个变量的声明（即清除变量的值），可以通过几种不同的方式来实现，下面为你详细介绍：

## **1. 使用空赋值**

最简单的方式是将变量赋值为空字符串。这样变量虽然仍然存在，但它的值为空。

```
# 声明变量
MY_VAR = some_value

# 取消变量的值
MY_VAR =

all:
    @echo "MY_VAR 的值为: $(MY_VAR)"
```

在上述代码中，首先给 `MY_VAR` 变量赋了值 `some_value`，之后通过 `MY_VAR =` 这一操作将其值清空。当执行 `make all` 时，输出的 `MY_VAR` 的值就是空的。

### **2. 使用 `undefine` 关键字**

`undefine` 关键字可以彻底移除变量的定义。与空赋值不同，使用 `undefine` 后，变量就不再存在于 Makefile 的作用域中。

```
# 声明变量
MY_VAR = some_value

# 取消变量的定义
undefine MY_VAR

all:
    @echo "MY_VAR 的值为: $(MY_VAR)"
```

这里，`undefine MY_VAR` 语句将 `MY_VAR` 变量的定义完全移除。当执行 `make all` 时，`$(MY_VAR)` 不会展开为任何内容，因为该变量已不存在。

### **3. 利用环境变量覆盖**

如果变量是从环境变量中继承而来，你可以通过在 Makefile 中重新赋值为空或者使用 `undefine` 来处理。另外，在调用 `make` 命令时也可以通过传递空值来覆盖环境变量的值。

```
# 假设 MY_VAR 是从环境变量继承而来
all:
    @echo "MY_VAR 的值为: $(MY_VAR)"
```

若要取消这个环境变量对 Makefile 的影响，可以这样调用 `make` 命令：

`make MY_VAR=`

这样，在 Makefile 执行过程中，`MY_VAR` 的值就为空。

### **4. 总结**

* **空赋值**：适合只是想清空变量的值，而保留变量的定义，后续还可能会重新赋值的情况。
* **`undefine` 关键字**：用于彻底移除变量的定义，若后续不再需要该变量，使用此方法更合适。
* **环境变量覆盖**：针对从环境变量继承的变量，可在调用 `make` 时传递空值来取消其影响。

# 三. 访问makefile变量

## **1. 基本变量引用**

使用 `$(var)` 或 `${var}` 来引用变量 `var` 的值。这是最常见的变量引用方式。

```
CC = gcc
CFLAGS = -Wall

all:
    $(CC) $(CFLAGS) -o test test.c
```

在这个例子中，`$(CC)` 引用了 `CC` 变量的值 `gcc`，`$(CFLAGS)` 引用了 `CFLAGS` 变量的值 `-Wall`。

## **2. 变量的嵌套引用**

可以在一个变量引用中嵌套另一个变量引用，以实现更复杂的操作。

```
src = main.c utils.c
obj = $(src:.c=.o)
CFLAGS = -Wall
CC = gcc

all: $(obj)
    $(CC) $(CFLAGS) -o my_program $(obj)

$(obj): %.o: %.c
    $(CC) $(CFLAGS) -c $< -o $@
```

这里，`$(obj)` 本身是通过后缀替换引用得到的，然后又在规则中被引用，同时规则里还引用了 `$(CC)` 和 `$(CFLAGS)` 变量。后面会有很多这种例子

## **3. 自动变量引用(默认变量)**

Makefile 提供了一些自动变量，用于在规则中引用目标文件、依赖文件等信息。

* `$@`：表示当前规则的目标文件。
* `$<`：表示当前规则的第一个依赖文件。
* `$^`：表示当前规则的所有依赖文件，以空格分隔。
* `$?`：代表当前规则中所有比目标文件更新的依赖文件，以空格分隔。

```
src = main.c utils.c
obj = $(src:.c=.o)
CC = gcc
CFLAGS = -Wall

all: my_program

my_program: $(obj)
    $(CC) $(CFLAGS) -o $@ $^

%.o: %.c
    $(CC) $(CFLAGS) -c $< -o $@
```

在 `my_program` 规则中，`$@` 代表 `my_program`，`$^` 代表 `main.o utils.o`；在 `%.o: %.c` 规则中，`$<` 代表对应的 `.c` 文件，`$@` 代表对应的 `.o` 文件。

## **4. 函数调用引用**

Makefile 支持使用函数来处理变量，通过函数调用的方式引用变量。

* `$(wildcard pattern)`：用于查找符合指定模式的文件列表。

```
src = $(wildcard *.c)
obj = $(src:.c=.o)
CC = gcc
CFLAGS = -Wall

all: my_program

my_program: $(obj)
    $(CC) $(CFLAGS) -o $@ $^

%.o: %.c
    $(CC) $(CFLAGS) -c $< -o $@
```

这里，`$(wildcard *.c)` 会查找当前目录下所有的 `.c` 文件，并将结果赋值给 `src` 变量。

* `$(patsubst pattern,replacement,text)`：用于对文本中的单词进行模式替换。

```
src = main.c utils.c
obj = $(patsubst %.c,%.o,$(src))
CC = gcc
CFLAGS = -Wall

all: my_program

my_program: $(obj)
    $(CC) $(CFLAGS) -o $@ $^

%.o: %.c
    $(CC) $(CFLAGS) -c $< -o $@
```

`$(patsubst %.c,%.o,$(src))` 会将 `src` 变量中的 `.c` 后缀替换为 `.o` 后缀，效果和后缀替换引用类似。

## **5. 环境变量引用**

Makefile 可以引用环境变量，使用 `$(VAR)` 或 `${VAR}` 来引用名为 `VAR` 的环境变量。

```
all:
    @echo $(HOME)
```

在这个例子中，`$(HOME)` 引用了系统环境变量 `HOME` 的值，通常是用户的主目录。

这些变量引用方式在 Makefile 中非常实用，可以帮助你更灵活地编写和管理项目的编译规则。

## **6. Makefile 后缀替换引用**

Makefile 中用于批量替换变量里单词后缀的语法。

格式：`$(var:a=b)`

* `var`：操作变量名
* `a`：待替换后缀
* `b`：替换后后缀

```
src = file1.c file2.c
obj = $(src:.c=.o)
all:
    @echo $(obj)
```

解释：将 `src` 里 `.c` 后缀替换为 `.o`，输出 `file1.o file2.o`。

**项目示例**

```
src = main.c utils.c
obj = $(src:.c=.o)
CC = gcc
CFLAGS = -Wall
all: my_program
my_program: $(obj)
    $(CC) $(CFLAGS) -o my_program $(obj)
%.o: %.c
    $(CC) $(CFLAGS) -c $< -o $@
clean:
    rm -f $(obj) my_program
```

解释：将 `src` 源文件列表转为 `obj` 目标文件列表，用于编译和链接生成 `my_program` 可执行文件。当然，%.o: %.c可以省略掉。

## **7. Makefile 中变量值的解析与处理**

在 Makefile 中，`SUBDIRS = subdir1 subdir2` 这样的赋值会将 `subdir1` 和 `subdir2` 作为一个整体字符串赋值给变量 `SUBDIRS`，多个值之间用空格分隔。但在后续使用中，Makef...