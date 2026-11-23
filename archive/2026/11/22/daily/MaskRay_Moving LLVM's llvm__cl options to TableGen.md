---
title: Moving LLVM's llvm::cl options to TableGen
url: https://maskray.me/blog/moving-llvm-cl-options-to-tablegen
source: MaskRay
date: 2026-11-22
fetch_date: 2026-11-23T10:02:24.742453
---

# Moving LLVM's llvm::cl options to TableGen

[Skip to content](#main-content)

[MaskRay](https://maskray.me/blog/)

* [Archives](https://maskray.me/blog/archives)
* [tags](https://maskray.me/blog/tags)
* [Feeds](https://maskray.me/feeds/)
* [TIL](https://maskray.me/til/)
* [Presentations](https://maskray.me/presentations/)

# Moving LLVM's llvm::cl options to TableGen

[MaskRay](https://maskray.me/blog "MaskRay")
* 22nd Nov 2026
* â¢9 min read
* â¢Tags:
* [llvm](https://maskray.me/blog/tags/llvm/)

### Table of Contents

* [What is wrong with llvm::cl::opt](#what-is-wrong-with-llvm-cl-opt)
* [An llvm/Option based RFC](#an-llvm-option-based-rfc)
* [Declaring options](#declaring-options)
* [Reading options: the owner binds once](#reading-options-the-owner-binds-once)
* [Parsing into a context](#parsing-into-a-context)
* [What embedders need to change](#what-embedders-need-to-change)
* [How the design changed](#how-the-design-changed)
* [Spellings](#spellings)
* [Cleaning up cl:: first](#cleaning-up-cl-first)
* [Cost and benefit](#cost-and-benefit)
* [Where it stands](#where-it-stands)
* [Acknowledgments](#acknowledgments)

Since September, the number of `llvm::cl::` option definitions in `llvm/lib` dropped from about 2,860 on release/23.x to about 1,070 on main.
Most of the difference moved from global `llvm::cl::opt` objects into per-library structs declared in TableGen and stored per `LLVMContext`; the rest were deleted.
This post covers why, the design, what it cost, what embedders need to change, and what is left before the LLVM 24 branch.

## What is wrong with `llvm::cl::opt`

A developer knob in an LLVM library is a namespace-scope global:

```
static cl::opt<bool>
    EnableCmovConverter("x86-cmov-converter",
                        cl::desc("Enable the X86 cmov-to-branch optimization."),
                        cl::init(true), cl::Hidden);
```

Each one is a dynamic initializer that registers the option into a `StringMap`.
It costs about 200 bytes of `.bss`, a couple of dynamic relocations, and about 1K instructions at startup and exit.
Multiplied by a few thousand options, every tool that links LLVM pays this before `main`, whether or not it parses a command line.

The values are process-wide.
Two `LLVMContext`s in one process cannot use different values, which matters to every embedder that compiles more than one thing at a time:
rustc's per-session `-Cllvm-args`, JITs that compile modules in parallel (Intel's graphics compiler, raised in the RFC thread), and NVIDIA, for whom removing global state was "the most important thing" (Reid Kleckner).

Options also leak across library boundaries: 48 `extern cl::opt` declarations read another library's option, some through a public header.

2,589 of the 2,939 options (88%) were already `cl::Hidden`: they are developer knobs, not user-facing options, and nothing outside the library needs to see them as globals.

## An `llvm/Option` based RFC

On 2026-09-20 I posted [[RFC] Declare library command line options in TableGen, one struct per library](https://discourse.llvm.org/t/rfc-declare-library-command-line-options-in-tablegen-one-struct-per-library/91877).
The idea is to reuse `llvm/Option`, the OptTable library behind the clang, lld, and llvm-objcopy drivers.
LLVMOption is both a data representation and a parsing library; this design uses the data representation.

Steffen Larsen was "preliminarily fine" with it.
James Henderson and Jan Svoboda preferred it; Jan noted that clang's own option structs duplicate defaults between a header and the marshalling `.td`, and generating the struct from TableGen removes that.
Alexis Engelke asked for compile-time tracker numbers before going further.

If OptTable is to replace `cl::opt`, it has to be cheaper, not just tidier.
Four patches starting with [#218845](https://github.com/llvm/llvm-project/pull/218845) shrank `OptTable::Info` from 88 to 16 bytes with no dynamic relocations, by replacing string pointers with `StringTable` offsets and moving rarely used fields into a deduplicated side table.
clang's `DriverOptions.cpp.o` went from 96,968 to 72,400 bytes at the last step alone.

## Declaring options

Each library owns a `.td` file in its own directory.
A target usually has two: one for the code generator, bound by its `TargetMachine`, and one in `MCTargetDesc/` for the MC layer, which llvm-mc and `clang -cc1as` use without a `TargetMachine`.
Here are excerpts of X86's, `llvm/lib/Target/X86/X86Options.td`:

```
include "llvm/Option/LibraryOptions.td"

def X86Options : OptionsStruct<prefix = "x86-">;

...
// X86CmovConversion.cpp
defm : BoolField<"x86-cmov-converter", "true",
  "Enable the X86 cmov-to-branch optimization">;
defm : BoolField<"x86-cmov-converter-force-all", "false",
  "Convert all cmovs to branches">;
defm : BoolField<"x86-cmov-converter-force-mem-operand", "true",
  "Convert cmovs to branches whenever they have memory operands">;
defm : ValueField<"x86-cmov-converter-threshold", "unsigned", "4",
  "Minimum gain per loop (in cycles) threshold">;
...
```

and `llvm/lib/Target/X86/MCTargetDesc/X86MCOptions.td`:

```
include "llvm/Option/LibraryOptions.td"

def X86MCOptions : OptionsStruct<prefix = "x86-">;

...
defm : ValueField<"x86-pad-max-prefix-size", "std::optional<unsigned>", "std::nullopt",
  "Maximum number of prefixes to use for padding">;

// MCTargetDesc/X86MCAsmInfo.cpp
defm : EnumField<"x86-asm-syntax", "X86::AsmWriterFlavorTy", "X86::ATT",
  "att,intel", ["X86::ATT", "X86::Intel"],
  "Select the assembly style for input">;
```

`llvm-min-tblgen -gen-opt-parser-defs` emits the option table, a struct with default member initializers, and an `apply` function that sets the member an argument names:

```
struct X86MCOptions {
  bool experimental_lvi_inline_asm_hardening{false};
  std::optional<StringRef> align_branch{std::nullopt};
  std::optional<unsigned> align_branch_boundary{std::nullopt};
  bool branches_within_32B_boundaries{false};
  bool pad_for_align{false};
  bool pad_for_branch_align{true};
  std::optional<unsigned> pad_max_prefix_size{std::nullopt};
  X86::AsmWriterFlavorTy asm_syntax{X86::ATT};
  bool mark_data_regions{true};

  static const llvm::opt::OptTable &optTable();
  bool apply(const llvm::opt::Arg &A, llvm::BumpPtrAllocator &Alloc);

private:
  friend class llvm::cl::LibraryOptionsContext;
  friend class llvm::opt::LibraryOptionsParser;

  static const X86MCOptions Default;
};
```

Member names are snake\_case spellings with the struct's `prefix` stripped.
A `std::optional` member replaces a `getNumOccurrences()` check: `x86-pad-max-prefix-size` is unset unless given.
`Default` is constant-initialized and private, so code cannot read options without going through a context.

There are also list fields, whose members are `ArrayRef`s so the structs stay trivially destructible.
`let Condition = AssertsOnly in` declares options that exist only in assertion builds.
The full vocabulary is in [CommandLine.md](https://llvm.org/docs/CommandLine.html), section "Declaring a Library's Options in TableGen".

A library's struct is private: the `.td` and the header live in `lib/X`, never in `include/`.
Another library that needs a value calls a function or takes a parameter, and an embedder gets knobs through API structs (`PipelineTuningOptions`, `TargetOptions`, `lto::Config`).

Targets register their structs from `LLVMInitializeXXXTarget()` and `LLVMInitializeXXXTargetMC()` with a function-local static, so a target's options cost no dynamic initializer:

```
extern "C" LLVM_C_ABI void LLVMInitializeX86TargetMC() {
  static opt::RegisterLibraryOptions<X86MCOptions> O;
  ...
```

## Reading options: the owner binds once

Values live in `cl::LibraryOptionsContext`.
Each layer reaches it through an object it already has, and an owner binds the struct once:

* IR passes ask the function's context: `F.getContext().getLibraryOptions().get<InstCombineCLOptions>()`.
* A `TargetMachine` binds its struct in the constructor, and subtargets and passes read it through `getCLOpts()`...