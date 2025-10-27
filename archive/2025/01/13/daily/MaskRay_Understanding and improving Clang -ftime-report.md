---
title: Understanding and improving Clang -ftime-report
url: https://maskray.me/blog/2025-01-12-understanding-and-improving-clang-ftime-report
source: MaskRay
date: 2025-01-13
fetch_date: 2025-10-06T20:08:24.689376
---

# Understanding and improving Clang -ftime-report

# [MaskRay](/blog/)

[Home](/blog/)
[Archives](/blog/archives/)
[Feeds](/blog/../feeds/)
[TIL](/blog/../til/)
[Presentations](/blog/../presentations/)

[![](/icon/github.svg)](https://github.com/MaskRay "GitHub")
[![](/icon/twitter.svg)](https://twitter.com/HaskRay "Twitter")



[2025-01-12](/blog/2025-01-12-understanding-and-improving-clang-ftime-report)

# Understanding and improving Clang -ftime-report

Clang provides a few options to generate timing report. Among them,
`-ftime-report` and `-ftime-trace` can be used to
analyze the performance of Clang's internal passes.

* `-fproc-stat-report` records time and memory on spawned
  processes (`ld`, and gas if
  `-fno-integrated-as`).
* `-ftime-trace`, introduced in 2019, generates Clang
  timing information in the Chrome Trace Event format (JSON). The format
  supports nested events, providing a rich view of the front end.
* `-ftime-report`: The option name is borrowed from
  GCC.

This post focuses on the traditional `-ftime-report`,
which uses a line-based textual format.

## Understanding `-ftime-report` output

The output consists of information about multiple timer groups. The
last group spans the largest interval and encompasses timing data from
other groups.

Up to Clang 19, the last group is called "Clang front-end time
report". You would see something like the following.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 ``` | ``` % clang -c -w -ftime-report ~/Dev/testsuite/sqlite3.i ... ===-------------------------------------------------------------------------===                          Miscellaneous Ungrouped Timers ===-------------------------------------------------------------------------===     ---User Time---   --System Time--   --User+System--   ---Wall Time---  --- Name ---    0.2993 ( 71.5%)   0.1069 ( 93.5%)   0.4062 ( 76.3%)   0.4066 ( 76.2%)  Code Generation Time    0.1190 ( 28.5%)   0.0074 (  6.5%)   0.1264 ( 23.7%)   0.1270 ( 23.8%)  LLVM IR Generation Time    0.4183 (100.0%)   0.1143 (100.0%)   0.5326 (100.0%)   0.5336 (100.0%)  Total ... ===-------------------------------------------------------------------------===                           Clang front-end time report ===-------------------------------------------------------------------------===   Total Execution Time: 0.7780 seconds (0.7788 wall clock)     ---User Time---   --System Time--   --User+System--   ---Wall Time---  --- Name ---    0.6538 (100.0%)   0.1241 (100.0%)   0.7780 (100.0%)   0.7788 (100.0%)  Clang front-end timer    0.6538 (100.0%)   0.1241 (100.0%)   0.7780 (100.0%)   0.7788 (100.0%)  Total ``` |

The "Clang front-end timer" timer measured the time spent in
`clang::FrontendAction::Execute`, which includes lexing,
parsing, semantic analysis, LLVM IR generation, optimization, and
machine code generation. However, "Code Generation Time" and "LLVM IR
Generation Time" belonged to the default timer group "Miscellaneous
Ungrouped Timers". This caused confusion for many users. For example, <https://aras-p.info/blog/2019/01/12/Investigating-compile-times-and-Clang-ftime-report/>
elaborates on the issues.

To address the ambiguity, I revamped the output in Clang 20.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` ... ===-------------------------------------------------------------------------===                                Clang time report ===-------------------------------------------------------------------------===   Total Execution Time: 0.7685 seconds (0.7686 wall clock)     ---User Time---   --System Time--   --User+System--   ---Wall Time---  --- Name ---    0.2798 ( 42.4%)   0.0966 ( 89.6%)   0.3765 ( 49.0%)   0.3768 ( 49.0%)  Machine code generation    0.2399 ( 36.3%)   0.0045 (  4.2%)   0.2445 ( 31.8%)   0.2442 ( 31.8%)  Front end    0.1179 ( 17.8%)   0.0067 (  6.2%)   0.1246 ( 16.2%)   0.1246 ( 16.2%)  LLVM IR generation    0.0230 (  3.5%)   0.0000 (  0.0%)   0.0230 (  3.0%)   0.0230 (  3.0%)  Optimizer    0.6606 (100.0%)   0.1079 (100.0%)   0.7685 (100.0%)   0.7686 (100.0%)  Total ``` |

The last group has been renamed and changed to cover a longer
interval within the invocation. It provides timing information for four
stages:

* Front end: Includes lexing, parsing, semantic analysis, and
  miscellnaenous tasks not captured by the subsequent timers.
* LLVM IR generation: The time spent in generating LLVM IR.
* LLVM IR optimization: The time consumed by LLVM's IR optimization
  pipeline.
* Machine code generation: The time taken to generate machine code or
  assembly from the optimized IR.

The `-ftime-report` output further elaborates on these
stages through additional groups:

* "Pass execution timing report" (first instance): A subset of the
  "Optimizer" group, providing detailed timing for individual optimization
  passes.
* "Analysis execution timing report": A subset of the first "Pass
  execution timing report". In LLVM's new pass manager, analyses are
  executed as part of pass invocations.
* "Pass execution timing report" (second instance): A subset of the
  "Machine code generation" group. (This group's name should be updated
  once the legacy pass manager is no longer used for IR
  optimization.)
* "Instruction Selection and Scheduling": This group appears when
  SelectionDAG is utilized and is part of the "Instruction Selection"
  timer within the second "Pass execution timing report".

Examples:

"Pass execution timing report" (first instance)

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 ``` | ``` ===-------------------------------------------------------------------------===                           Pass execution timing report ===-------------------------------------------------------------------------===   Total Execution Time: 3.0009 seconds (3.0016 wall clock)     ---User Time---   --System Time--   --User+System--   ---Wall Time---  --- Name ---    0.9626 ( 32.7%)   0.0162 ( 26.6%)   0.9788 ( 32.6%)   0.9790 ( 32.6%)  InstCombinePass    0.3203 ( 10.9%)   0.0056 (  9.2%)   0.3259 ( 10.9%)   0.3263 ( 10.9%)  InlinerPass    0.3123 ( 10.6%)   0.0068 ( 11.1%)   0.3190 ( 10.6%)   0.3187 ( 10.6%)  SimplifyCFGPass ... ``` |

When `-ftime-report=per-run-pass` is specified, a timer is
created for each pass object. This can result in significant output,
especially for modules with numerous functions, as each pass will be
reported multiple times.

## Clang internals

As `clang -### -c -ftime-report` shows, clangDriver
forwards `-ftime-report` to Clang cc1. Within cc1, this
option sets the codegen flag
`clang::CodeGenOptions::TimePasses`. This flag enables eth
uses of `llvm::Timer` objects to measure the execution time
of specific code blocks.

From Clang 20 onwards, the placement of the timers can be understood
through the following call tree.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 ``` | ``` cc1_main   ExecuteCompilerInvocation                           // "Front end" minus the following timers     ... all kinds of initialization     CompilerInstance::ExecuteAction       FrontendAction::BeginSourceFile       FrontendAction::Execute         FrontendAction::ExecutionAction           ASTFrontendAction::ExecuteAction             ParseAST               BackendConsumer::HandleTranslationUnit                 clang::emitBackendOutput                   EmitAssemblyHelper::emitAssembly                     RunOptimizationPipeline           // "Optimizer"                     RunCodegenPipeline                // "Machine code generation"       FrontendAction::EndSourceFile ``` |

The measured interval does not cover the whole invocation. integrated
cc1 `clang -c -ftime-report a.c`

## LLVM internals

`LLVM/lib/Support/Time.cpp` implements the timer feature.
`Timer` belongs to a `TimerGroup`.
`Timer::startTimer` and `Timer::stopTimer`
generate a `TimeRecord`. In
`clang/tools/driver/cc1_main.cpp`,
`llvm::TimerGroup::printAll(llvm::errs());` dumps these
`TimerGroup` and `TimeRecord` information to
stderr.

There are a few ...