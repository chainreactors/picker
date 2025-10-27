---
title: “Unstripping” binaries: Restoring debugging information in GDB with Pwndbg
url: https://blog.trailofbits.com/2024/09/06/unstripping-binaries-restoring-debugging-information-in-gdb-with-pwndbg/
source: Trail of Bits Blog
date: 2024-09-07
fetch_date: 2025-10-06T18:27:52.404472
---

# “Unstripping” binaries: Restoring debugging information in GDB with Pwndbg

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# “Unstripping” binaries: Restoring debugging information in GDB with Pwndbg

Jason An

September 06, 2024

[application-security](/categories/application-security/), [binary-ninja](/categories/binary-ninja/), [go](/categories/go/), [internship-projects](/categories/internship-projects/)

GDB loses significant functionality when debugging binaries that lack debugging symbols (also known as “stripped binaries”). Function and variable names become meaningless addresses; setting breakpoints requires tracking down relevant function addresses from an external source; and printing out structured values involves staring at a memory dump trying to manually discern field boundaries.

That’s why this summer at Trail of Bits, I extended [Pwndbg](https://github.com/pwndbg/pwndbg)—a plugin for GDB maintained by my mentor, [Dominik Czarnota](https://disconnect3d.pl/)—with two new features to bring the stripped debugging experience closer to what you’d expect from a debugger in an IDE. Pwndbg now integrates Binary Ninja for enhanced GDB+Pwndbg intelligence and enables dumping Go structures for improved Go binary debugging.

### Binary Ninja integration

To help improve GDB+Pwndbg intelligence during debugging, I integrated Pwndbg with [Binary Ninja](https://binary.ninja), a popular decompiler with a versatile scripting API, by installing an XML-RPC server inside Binary Ninja, and then querying it from Pwndbg. This allows Pwndbg to access Binary Ninja’s analysis database, which is used for syncing symbols, function signatures, stack variable offsets, and more, recovering much of the debugging experience.

![](/img/wpdump/7b477decdbb77de1f00d7125f6f21eca.png)

Figure 1: Pwndbg showing symbols and argument names synced from Binary Ninja in a stripped binary

For the decompilation, I pulled the tokens from Binary Ninja instead of serializing them to text first. This allows for fully syntax-highlighted decompilation, configurable to use any of [Binary Ninja’s 3 IL levels](https://docs.binary.ninja/dev/bnil-overview.html). The decompilation is shown directly in the Pwndbg context, with the current line highlighted, just like in the assembly view.

![](/img/wpdump/7413fabac6385d5325af79f7d7440e7f.png)

Figure 2: Decompilation pulled from Binary Ninja and displayed in Pwndbg

I also implemented a feature to display the current program counter (PC) register as an arrow inside Binary Ninja and a feature to set breakpoints from within Binary Ninja to reduce the amount of switching to and from Pwndbg involved.

![](/img/wpdump/cbe2efec6819c427c3f4c0fa9cc2f577.png)

Figure 3: Binary Ninja displaying icons for the current PC and breakpoints

The most involved component of the integration is syncing stack variable names. Anywhere a stack address appears in Pwndbg, like in the register view, stack view, or function argument previews, the integration will check if it’s a named stack variable in Binary Ninja. If it is, it will show the proper label. It will even check parent stack frames so that variables from the caller will still be labeled properly.

![](/img/wpdump/ab1da9d3e2afe630e33e7395e27731d5.png)

Figure 4: A demonstration of how stack variable labeling is displayed

The main difficulty in implementing this feature came from the fact that Binary Ninja only provides stack variables as an offset from the stack frame base, so the frame base needs to be deduced in order to compute absolute addresses. Most architectures, like x86, have a frame pointer register that points to the frame base, but most architectures, including x86, [don’t actually *need* the frame pointer](https://stackoverflow.com/q/14666665), so compilers are free to use it like any other register.

Fortunately, Binary Ninja has constant value propagation, so it can tell if registers are a predictable offset from the frame base. So, my implementation will first check if the frame pointer is actually the frame base, and if it’s not, it will see if the stack pointer advanced a predictable amount (which is usually true with modern compilers); otherwise, it will check every other general-purpose register to try to find one with a consistent offset. Technically, this approach won’t work all the time, but in practice, it should almost never fail.

### Go debugging

A common pain point when debugging executables compiled from non-C programming languages (and sometimes even C) is that they tend to have complex memory layouts that make it hard to dump values. A benign example is dumping a [slice in Go](https://go.dev/blog/slices-intro), which requires one command to dump the pointer and length, and another to examine the slice contents. Dumping a map, on the other hand, can require over ten commands for a small map, and hundreds for larger ones, which is completely impractical for a human.

That’s why I created the `go-dump` command. Using [the Go compiler’s source code](https://github.com/golang/go/tree/master/src/runtime) as a reference, I implemented dumping for all of Go’s built-in types, including integers, strings, complex numbers, pointers, slices, arrays, and maps. The built-in types are notated just like they are in Go, so you don’t need to learn any new syntax to use the command properly.

![](/img/wpdump/2cb2ebccec9f126cd654b1edbe1b7091.png)

Figure 5: Dumping a simple map type using the go-dump command

The `go-dump` command is also capable of parsing and dumping arbitrarily nested types so that every type can be dumped with just one command.

![](/img/wpdump/5fbed116c665fff821b62db8b5a8dff9.png)

Figure 6: Dumping a more complex slice of map types using the go-dump command

### Parsing Go’s runtime types

While Go-specific dumping is much nicer than manual memory dumping, it still poses many usability concerns. You need to know the full type of the value you’re dumping, which can be hard to determine and usually involves a lot of guesswork, especially when dealing with structs that have many fields or nested structs. Even if you have deduced the full type, some things are still unknowable because they have no effect on compilation, like struct field names and type names for user-defined types.

Conveniently, the Go compiler emits a runtime type object for **every** type used in the program (to be used with [the `reflect` package](https://pkg.go.dev/reflect)), which contains struct layouts for arbitrarily nested structs, type names, size, alignment, and more. These type objects can also be matched up to values of that type, as interface values store a pointer to the type object along with a pointer to the data, and heap-allocated values have their type object passed into their allocation function (usually `runtime.newobject`).

I wrote a parser capable of recursively extracting this information in order to process type information for arbitrarily nested types. This parser is exposed via the `go-type` command, which displays information about a runtime type given its address. For structs, this information includes the type, name, and offset of every field.

![](/img/wpdump/fb1f21d0a92a777a116ffa10772a5345.png)

Figure 7: Examining a struct type that consists of an int and a string

This can be used to dump values in two ways. The first, easier way only works for interface values, since the type pointer is stored along with the data pointer, making it easy to automatically retrieve. These can be dumped using Go’s any type for empty interfaces (ones with no methods), and the `interface` type for non-empty interfaces. When dumping, the command will automatically retrieve and parse the type, leading to a seamless dump without having to enter any type information.

![](/img/wpdump/6210ec28db24bd3ae4652941ec149659.png)

Figure 8: Dumping an interface value without specifying any type information

The second way works for all values but requires you to find and specify the pointer to...