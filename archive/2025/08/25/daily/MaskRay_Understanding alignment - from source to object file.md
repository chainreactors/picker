---
title: Understanding alignment - from source to object file
url: https://maskray.me/blog/2025-08-24-understanding-alignment-from-source-to-object-file
source: MaskRay
date: 2025-08-25
fetch_date: 2025-10-07T00:16:45.696610
---

# Understanding alignment - from source to object file

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2025-08-24](/blog/2025-08-24-understanding-alignment-from-source-to-object-file)

# Understanding alignment - from source to object file

Alignment refers to the practice of placing data or code at memory
addresses that are multiples of a specific value, typically a power of
2. This is typically done to meet the requirements of the programming
language, ABI, or the underlying hardware. Misaligned memory accesses
might be expensive or will cause traps on certain architectures.

This blog post explores how alignment is represented and managed as
C++ code is transformed through the compilation pipeline: from source
code to LLVM IR, assembly, and finally the object file. We'll focus on
alignment for both variables and functions.

## Alignment in C++ source code

[C++ [basic.align]](https://eel.is/c%2B%2Bdraft/basic.align)
specifies

> Object types have alignment requirements ([basic.fundamental],
> [basic.compound]) which place restrictions on the addresses at which an
> object of that type may be allocated. An alignment is an
> implementation-defined integer value representing the number of bytes
> between successive addresses at which a given object can be allocated.
> An object type imposes an alignment requirement on every object of that
> type; stricter alignment can be requested using the alignment specifier
> ([dcl.align]). Attempting to create an object ([intro.object]) in
> storage that does not meet the alignment requirements of the object's
> type is undefined behavior.

`alignas` can be used to request a stricter alignment. [[decl.align]](https://eel.is/c%2B%2Bdraft/dcl.align)

> An alignment-specifier may be applied to a variable or to a class
> data member, but it shall not be applied to a bit-field, a function
> parameter, or an exception-declaration ([except.handle]). An
> alignment-specifier may also be applied to the declaration of a class
> (in an elaborated-type-specifier ([dcl.type.elab]) or class-head
> ([class]), respectively). An alignment-specifier with an ellipsis is a
> pack expansion ([temp.variadic]).

Example:

|  |  |
| --- | --- |
| ``` 1 2 ``` | ``` alignas(16) int i0; struct alignas(8) S {}; ``` |

If the strictest `alignas` on a declaration is weaker than
the alignment it would have without any alignas specifiers, the program
is ill-formed.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 ``` | ``` % echo 'alignas(2) int v;' | clang -fsyntax-only -xc++ - <stdin>:1:1: error: requested alignment is less than minimum alignment of 4 for type 'int'     1 | alignas(2) int v;       | ^ 1 error generated. ``` |

However, the GNU extension `__attribute__((aligned(1)))`
can request a weaker alignment.

|  |  |
| --- | --- |
| ``` 1 ``` | ``` typedef int32_t __attribute__((aligned(1))) unaligned_int32_t; ``` |

Further reading: [What
is the Strict Aliasing Rule and Why do we care?](https://gist.github.com/shafik/848ae25ee209f698763cffee272a58f8)

## LLVM IR representation

In the LLVM Intermediate Representation (IR), both global variables
and functions can have an `align` attribute to specify their
required alignment.

[Global
variable alignment](https://llvm.org/docs/LangRef.html#global-variables):

> An explicit alignment may be specified for a global, which must be a
> power of 2. If not present, or if the alignment is set to zero, the
> alignment of the global is set by the target to whatever it feels
> convenient. If an explicit alignment is specified, the global is forced
> to have exactly that alignment. Targets and optimizers are not allowed
> to over-align the global if the global has an assigned section. In this
> case, the extra alignment could be observable: for example, code could
> assume that the globals are densely packed in their section and try to
> iterate over them as an array, alignment padding would break this
> iteration. For TLS variables, the module flag MaxTLSAlign, if present,
> limits the alignment to the given value. Optimizers are not allowed to
> impose a stronger alignment on these variables. The maximum alignment is
> 1 << 32.

Function alignment

> An explicit alignment may be specified for a function. If not
> present, or if the alignment is set to zero, the alignment of the
> function is set by the target to whatever it feels convenient. If an
> explicit alignment is specified, the function is forced to have at least
> that much alignment. All alignments must be a power of 2.

A backend can override this with a preferred function alignment
(`STI->getTargetLowering()->getPrefFunctionAlignment()`),
if that is larger than the specified align value. (<https://discourse.llvm.org/t/rfc-enhancing-function-alignment-attributes/88019/3>)

---

In addition, `align` can be used in parameter attributes
to decorate a pointer or [vector of pointers](https://reviews.llvm.org/D115161).

## LLVM back end representation

**Global variables**
`AsmPrinter::emitGlobalVariable` determines the alignment for
global variables based on a set of nuanced rules:

* With an explicit alignment (`explicit`),
  + If the variable has a section attribute, return
    `explicit`.
  + Otherwise, compute a preferred alignment for the data layout
    (`getPrefTypeAlign`, referred to as `pref`).
    Return
    `pref < explicit ? explicit : max(E, getABITypeAlign)`.
* Without an explicit alignment: return
  `getPrefTypeAlign`.

`getPrefTypeAlign` employs a heuristic for global variable
definitions: if the variable's size exceeds 16 bytes and the preferred
alignment is less than 16 bytes, it sets the alignment to 16 bytes. This
heuristic balances performance and memory efficiency for common cases,
though it may not be optimal for all scenarios. (See [Preferred
alignment of globals > 16bytes](https://discourse.llvm.org/t/preferred-alignment-of-globals-16bytes/24410) in 2012)

For assembly output, AsmPrinter emits `.p2align` (power of
2 alignment) directives with a zero fill value (i.e. the padding bytes
are zeros).

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` % echo 'int v0;' | clang --target=x86_64 -S -xc - -o -         .file   "-"         .type   v0,@object                      # @v0         .bss         .globl  v0         .p2align        2, 0x0 v0:         .long   0                               # 0x0         .size   v0, 4 ... ``` |

**Functions** For functions,
`AsmPrinter::emitFunctionHeader` emits alignment directives
based on the machine function's alignment settings.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 ``` | ``` void MachineFunction::init() { ...   Alignment = STI.getTargetLowering()->getMinFunctionAlignment();    // FIXME: Shouldn't use pref alignment if explicit alignment is set on F.   if (!F.hasOptSize())     Alignment = std::max(Alignment,                          STI.getTargetLowering()->getPrefFunctionAlignment()); ``` |

* The subtarget's minimum function alignment
* If the function is not optimized for size (i.e. not compiled with
  `-Os` or `-Oz`), take the maximum of the minimum
  alignment and the preferred alignment. For example,
  `X86TargetLowering` sets the preferred function alignment to
  16.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` % echo 'void f(){} [[gnu::aligned(32)]] void g(){}' | clang --target=x86_64 -S -xc - -o -         .file   "-"         .text         .globl  f                               # -- Begin function f         .p2align        4         .type   f,@function f:                                      # @f ...         .globl  g                               # -- Begin function g         .p2align        5         .type   g,@function g:                                      # @g ``` |

The emitted `.p2align` directives omits the fill value
argument: for code sections, this space is fi...