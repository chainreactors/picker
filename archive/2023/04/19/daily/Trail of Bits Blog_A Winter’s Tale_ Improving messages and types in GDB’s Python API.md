---
title: A Winter’s Tale: Improving messages and types in GDB’s Python API
url: https://blog.trailofbits.com/2023/04/18/a-winters-tale-improving-types-and-messages-in-gdbs-python-api/
source: Trail of Bits Blog
date: 2023-04-19
fetch_date: 2025-10-04T11:33:30.906306
---

# A Winter’s Tale: Improving messages and types in GDB’s Python API

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# A Winter’s Tale: Improving messages and types in GDB’s Python API

Matheus Branco Borella, University of São Paulo

April 18, 2023

[internship-projects](/categories/internship-projects/)

As a winter associate at Trail of Bits, my goal was to make two improvements to the GNU Project Debugger (GDB): make it run faster and improve its Python API to support and improve tools that rely on it, like [Pwndbg](https://github.com/pwndbg/pwndbg/). The main goal was to run symbol parsing in parallel and better use all available CPU cores. I ultimately [implemented three changes that enhanced GDB’s Python API](https://inbox.sourceware.org/gdb-patches/?q=Matheus+Branco+Borella).

Beyond the actual code, I also learned about upstreaming patches in GDB. This process can take a while, has a bit of a learning curve, and involves a lot of back and forth with the project’s maintainers. I’ll discuss this in the post, and you can also follow along as my work [is still being debated in the GDB patches mailing list](https://sourceware.org/pipermail/gdb-patches/2023-January/).

## Why make GDB faster?

GDB has three ways to load DWARF symbols from a program:

1. **Partial symbol table loader**: The index loader is responsible for loading in symbol names and connecting them to their respective compilation units (CUs), leaving the parsing and building of their symbol tables to the full loader. Parsing will be done later only when full information about the symbol is required.
2. **Full symbol table loader**: Finishes the work the index loader has left for later by parsing the CUs and building their symbol tables as needed. This loader fully parses the DWARF information in the file and stores it in memory.
3. **Index parser**: ELFs can have a special .gdb\_index section, added either with the [–gdb-index linker](https://reviews.llvm.org/D24267) flag or with the [gdb-add-index](https://sourceware.org/gdb/onlinedocs/gdb/Index-Files.html) tool provided by GDB. The tool stores an index for the internal symbol table that allows GDB to skip the index construction pass, significantly reducing the time required to load the binary in GDB.

The original idea was to port the parallel parsing approach in [drgn](https://github.com/osandov/drgn), Meta’s open-source debugger, to GDB. Parallel parsing had already been [implemented for the index loader](https://tromey.com/blog/?p=1084), leaving only the full loader and the index parser as potential next candidates in line for parallelization.

You can think of GDB’s parsing routines as split into concurrent tasks on a per-CU basis since they’re already invoked sequentially once per CU. However, this understanding has a major issue: despite the ostensive separation of the data, it is not separated into data that is fully read-write, partially read-write with implicit synchronization, and read-only. The parsing subroutines fully expect all of these data structures to be read-write, at least to a degree.

While solving most of these is a simple case of splitting the values into separate read-write copies (one owned by each thread), things like the registries, the caches, and particularly the obstacks are much harder to move to a concurrent model.

## What’s an obstack?

General purpose allocations, like `malloc()`, are time-consuming. They may not be efficient when users need to allocate many small objects as quickly as possible since they store metadata within each allocation.

Enter allocation stacks. Each new object is allocated on the top and freed from the top in order. The GNU Obstack, an implementation of such an allocator, is used heavily in GDB. Each reasonably long-lived container object, including `objfile` and `gdbarch`, has its instance of an obstack and is used to hold the objects it references and frees them all at once, together with the object itself.

If you’re knowledgeable on object lifetime tracking—be it dynamic, like you’d get with `std::shared_ptr`, or static, like with references in Rust—the last paragraph will have sounded familiar. Judging by how obstack allocations are used in GDB, someone might assume there is a way to guarantee that objects will live as long as the container that owns them.

After discussing this with others in the [IRC and mailing list](https://sourceware.org/pipermail/gdb-patches/2022-December/194993.html), I reached two conclusions: it would take a considerable amount of time to investigate it, and I was better off prioritizing the Python API so that I could have a chance at completing the improvements on time. Ultimately, I spent most of my time on those attainable goals.

## GDB objects \_\_repr\_\_ methods

The first change is fairly simple. It adds `__repr__()` implementations to a handful of types in the GDB Python API. This change makes the messages we get from inspecting types in the Python REPL more informative about what those types represent.

Previously, we would get something like this, which is hardly helpful (note: pi is the GDB command to run the Python REPL):

```
(gdb) pi
>>> gdb.lookup_type("char")
<gdb.Type object at 0x7ff8e01aef20>
```

Now, we can get the following, which tells us what kind of type this is, as well as its name, rather than where the object is located in memory:

```
(gdb) pi
>>> gdb.lookup_type("char")
<gdb.Type code=TYPE_CODE_INT name=char>
```

This also applies to `gdb.Architecture`, `gdb.Block`, `gdb.Breakpoint`, `gdb.BreakpointLocation`, and `gdb.Symbol`.

This helped me understand how GDB interfaces with Python and how the Python C API generally works. It allowed me to add my own functions and types later.

## Types ahoy!

The second change adds the ability to create types from the Python API, where previously, you could only query for existing types using `gdb.lookup_type()`. Now you can directly create any primitive type supported by GDB, which can be pretty handy if you’re working on code but don’t have the symbols for it, or if you’re writing plugins to help people work with that sort of code. Types from weird extra binaries need not apply!

GDB supports a [fairly large number of types](https://github.com/bminor/binutils-gdb/blob/master/gdb/type-codes.def). All of them can be created directly using `gdb.init_type` or one of the specialized `gdb.init_*_type` functions, which let you specify parameters relevant to the type being created. Most of them work similarly, except for `gdb.init_float_type`, which has its own new `gdb.FloatFormat` type to go along with it. This lets you specify how the floating point type you’re trying to create is laid out in memory.

An extra consideration that comes with this change is where exactly the memory for these new types comes from. Since these functions are based on functions already available internally in GDB, and since these functions use the obstack from a given objfile, the obstack is the memory source for these allocations. This has one big advantage: objects that reference these types and belong to the same objfile are guaranteed never to outlive them.

You may already have realized a significant drawback to this method: any type allocated on it has a high chance of not being on the top of the stack when the Python runtime frees it. So regardless of their real lifetime requirements, types can be freed only along with the objfile that owns them. The main implication is that unreachable types will leak their memory for the lifetime of the objfile.

Keeping track of the initialization of the type by hand would require a deeper change to the existing type object infrastructure. This is too ambitious for a first patch.

Here are a few examples of this method in action:

```
(gdb) pi
>>> objfile = gdb.lookup_objfile("servo")
>>>
>>> # Time to standardize integer extensions. :^)
>>> gdb.init_type(objfile, gdb.TYPE_CODE_INT, 24, "long short int")
<gdb.Type code=TYPE_CODE_INT name...