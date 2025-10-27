---
title: Qemuafl 实现分析
url: https://qrz.today/00-fuzz/2020-qemuafl/0.0.how-qemuafl-works
source: 🚂QRZ的星穹列车
date: 2025-02-22
fetch_date: 2025-10-06T20:37:03.742421
---

# Qemuafl 实现分析

## [🚂QRZ的星穹列车](../..)

搜索

Search

暗色模式亮色模式

阅读模式

## 探索

[📑Tags](/tags)[🪪About](/misc/about)[📻Radio](/z6-life/ham-radio/index)[🧑‍🤝‍🧑Friends](/misc/friends)[🚇开往](https://www.travellings.cn/go.html)

---

[Home](../../)

❯

[模糊测试](../../00-fuzz/)

❯

[2020 qemuafl](../../00-fuzz/2020-qemuafl/)

❯

Qemuafl 实现分析

# Qemuafl 实现分析

2025年2月21日11分钟阅读

* [fuzz/qemuafl](../../tags/fuzz/qemuafl)
* [qemu](../../tags/qemu)

### 目录

* [初始化流程](#初始化流程)
* [afl\_setup](#afl_setup)
* [afl\_forkserver](#afl_forkserver)
* [persistent mode](#persistent-mode)
* [afl\_persistent\_loop](#afl_persistent_loop)
* [插桩流程](#插桩流程)
* [afl\_gen\_trace](#afl_gen_trace)
* [afl\_maybe\_log\*](#afl_maybe_log)
* [总结](#总结)
* [附录](#附录)
* [A. qemu TCG runtime](#a-qemu-tcg-runtime)
* [B. QEMU helper 机制](#b-qemu-helper-机制)
* [参考资料](#参考资料)

> 概述 by ChatGPT
>
> 本文从 `qemuafl` 的初始化、持久模式到插桩流程详细解析了其核心机制，包括 `afl_setup` 的环境变量配置、`afl_forkserver` 的与 AFL++ 的交互，及 `afl_gen_trace` 的插桩逻辑。还分析了持久模式核心函数如 `afl_persistent_loop` 的运行逻辑及其与共享内存和寄存器快照的关系，揭示了 `qemuafl` 高效模糊测试的实现原理。

## 初始化流程

在 `qemuafl/accel/tcg/translator.c` 的 `translator_loop` 函数中，如果要翻译的基本块中包含 `afl_entry_point` 则调用 `afl_setup` 函数进行初始化：

qemuafl/accel/tcg/translator.c

```
void translator_loop(const TranslatorOps *ops, DisasContextBase *db,
                     CPUState *cpu, TranslationBlock *tb, int max_insns)
{
        ... ...
        if (db->pc_next == afl_entry_point) {

            static bool first = true;
            ...
            if (first) {
                afl_setup();
                ...
                tb_flush(cpu);
                first = false;
            }
            gen_helper_afl_entry_routine(cpu_env);
        }
```

在初始化之后会刷新缓存，结合注释信息，我的理解是在初始化之前有可能已经对一些基本块做了翻译，而 qemuafl 初始化之后会加入一些其他信息，因此在这里刷新 CPU 缓存且只刷新一次。之后调用 `gen_helper_afl_entry_routine` 生成入口点代码，该函数留在后面分析。

### afl\_setup

`afl_setup` 会进行一些初始化操作，包括：

* `AFL_INST_RATIO`：设置插桩比例（`afl_inst_rms` 变量）；
* `__AFL_SHM_ID`：初始化共享内存；
* `AFL_QEMU_DISABLE_CACHE`：判断是否禁用缓存；
* `___AFL_EINS_ZWEI_POLIZEI___`：判断是否开启 cmplog forkserver；
* 设置插桩范围
  + `AFL_INST_LIBS`：设置是否完全插桩；
  + `AFL_CODE_START`、`AFL_CODE_END`：设置特定起始结束位置；
  + `AFL_QEMU_INST_RANGES`：设置自定义的插桩范围；
  + `AFL_QEMU_EXCLUDE_RANGES`：设置自定义的插桩排除范围；
* `AFL_DEBUG`：是否开启调试；
* `AFL_QEMU_COMPCOV`：是否启用 x86 和 x86\_64 中所有 cmp 和 sub 的 CompareCoverage 跟踪。
  + 从 `AFL_COMPCOV_LEVEL` 获取 CompareCoverage 等级，默认为 1。
* `AFL_QEMU_PERSISTENT_HOOK`：是否开启 persistent mode
  + 如果上文开启了 `AFL_QEMU_COMPCOV` 会和 persistent 冲突；
  + 如果是静态编译的 QEMU，无法使用持久测试，退出；
  + 从持久测试的 lib 库中获取一些关键函数：
    - `afl_persistent_hook_init`：声明是否使用内存进行模糊测试（`sharedmem_fuzzing`）；
    - `afl_persistent_hook`：用户自定义的函数，在每次模糊测试之前可以覆盖要解析的缓冲区和内存，并正确设置长度；
  + `AFL_QEMU_PERSISTENT_ADDR`：persisent 模式下需要有一个起始地址；
  + `AFL_QEMU_PERSISTENT_RET`：在执行到这个地址时恢复（保存的）状态；
  + `AFL_QEMU_PERSISTENT_GPR`：是否保持寄存器一致；
  + `AFL_QEMU_PERSISTENT_MEM`：是否保持内存一致；
  + `AFL_QEMU_PERSISTENT_RETADDR_OFFSET`：是否设置返回地址相对起始地址的偏移；
  + `AFL_QEMU_PERSISTENT_CNT`：设置持久测试的次数；
  + `AFL_QEMU_PERSISTENT_EXITS`：是否强制 QEMU 将 pc 设置为 START，而不是执行 `exit_group` 系统调用并退出程序；
  + `AFL_QEMU_SNAPSHOT`：等价于开启了上面的
    - `AFL_QEMU_PERSISTENT_GPR`
    - `AFL_QEMU_PERSISTENT_MEM`
    - `AFL_QEMU_PERSISTENT_EXITS`

在 `afl_setup` 后会执行 `gen_helper_afl_entry_routine` 生成入口点的 TCG 代码。在执行到该代码时，最终会调用 `afl_forkserver` 函数。

### afl\_forkserver

`afl_forkserver` 主要流程如下：

* 如果不在老版本 forkserver 下（`AFL_OLD_FORKSERVER`），则：
  + 设置 `lkm_snapshot` 状态；
  + 设置 `sharedmem_fuzzing` 状态；
* 和 AFL++ 交互，这一部分可以看我之前绘制的[通信流程图](../../00-fuzz/2013-afl/AFL-runtime-images)，这里不再赘述。
  + 在这一部分多出了一块 `sharedmem_fuzzing` 的逻辑，如果开启了共享内存模糊测试，则会调用到 `afl_map_shm_fuzz` 函数中从共享内存中获得输入。

### persistent mode

在持久模式下，初始化的位置在每个架构实现的 `disas_insn` 最开始，例如 i386/x64 的实现就位于 `qemuafl/target/i386/tcg/translate.c`：

qemuafl/target/i386/tcg/translate.c

```
static target_ulong disas_insn(DisasContext *s, CPUState *cpu)
{
    ...

    AFL_QEMU_TARGET_I386_SNIPPET
```

在这个位置插入了一段 SNIPPET，用于持久模式的实现，它的逻辑为：

* 在持久模式起始地址（`afl_persistent_addr`）的操作：
  + 生成持久 fuzz 栈帧恢复的 TCG 代码；
    - 在未保存 GPR 且未设置 `afl_persistent_ret_addr` 的条件下恢复栈指针；
  + 生成持久测试的 TCG 代码（ `afl_persistent_routine`）
  + 如果没有设置持久化的返回地址，则将 `afl_persistent_addr` 这个持久化函数入口地址写入栈中作为返回地址；
* 如果设置了持久化的返回地址，且执行到了返回地址，则生成跳转到返回地址的 TCG 代码。

其他架构的处理逻辑类似，这里不再赘述。

### afl\_persistent\_loop

上文的 `HELPER(afl_persistent_routine)` 最终会在代码运行时执行到 `afl_persistent_loop` 函数，在这里对每次持久模式都会做一些初始化操作。该函数的逻辑为：

* 如果是第一次持久测试：
  + 重置共享内存 `afl_area_ptr`；
  + 设置内存或寄存器快照；
  + 执行用户定义的 `afl_persistent_hook` 函数；
* 如果是第二次或之后的持久测试：
  + 调用 `afl_persistent_iter`，这个函数主要功能为：
    - 如果到达了用户设定的持久化循环次数，则：
      * 恢复内存或寄存器快照
      * 处理未禁用 cache 的逻辑，本质上还是[通信流程图](../../00-fuzz/2013-afl/AFL-runtime-images)中向 AFL 发送返回值的流程；
      * 在上述过程后，可以开启新一轮 fuzz 了，重新执行 `afl_persistent_hook` 并恢复寄存器快照。

## 插桩流程

### afl\_gen\_trace

QEMU 会在 `tb_gen_code` 函数中执行翻译流程，qemuafl 会在 qemu 翻译一个新的代码块之前调用 `afl_gen_trace` 函数生成 TCG 代码：

qemuafl/accel/tcg/translate-all.c

```
tcg_func_start(tcg_ctx);

tcg_ctx->cpu = env_cpu(env);
afl_gen_trace(pc);
gen_intermediate_code(cpu, tb, max_insns);
tcg_ctx->cpu = NULL;
max_insns = tb->icount;

trace_translate_block(tb, tb->pc, tb->tc.ptr);
```

`afl_gen_trace` 会进行以下操作：

* 检查是否需要对当前位置进行插桩；
  + 注：这一步可以避免 qemuafl 初始化之前的插桩，也是初始化后需要刷新 cpu 缓存的原因。
* 计算当前地址哈希作为插桩 ID，检查当前地址是否超过插桩比例；
* 判断是否记录不稳定的基本块，通过 `gen_helper_afl_maybe_log*` 生成插桩代码。

### afl\_maybe\_log\*

在调用到 `afl_maybe_log*` 函数时，该函数会向共享内存中写入覆盖率信息：

qemuafl/accel/tcg/translate-all.c

```
void HELPER(afl_maybe_log)(target_ulong cur_loc) {
  register uintptr_t afl_idx = cur_loc ^ afl_prev_loc;

  INC_AFL_AREA(afl_idx);

  // afl_prev_loc = ((cur_loc & (MAP_SIZE - 1) >> 1)) |
  //                ((cur_loc & 1) << ((int)ceil(log2(MAP_SIZE)) -1));
  afl_prev_loc = cur_loc >> 1;
}

void HELPER(afl_maybe_log_trace)(target_ulong cur_loc) {
  register uintptr_t afl_idx = cur_loc;
  INC_AFL_AREA(afl_idx);
}
```

可以看到，在正常记录时 `afl_idx=cur_loc ^ afl_prev_loc`，而记录不稳定的代码块时只会使用 `afl_idx=cur_loc`。除此之外，原本的 `afl_prev_loc` 计算方式较为复杂，而后来实现的则更为简单，查看 git 日志时说明的原因是为了提高执行效率。

`INC_AFL_AREA` 就是写入覆盖率信息的具体实现：

qemuafl/qemuafl/common.h

```
#if (defined(__x86_64__) || defined(__i386__)) && defined(AFL_QEMU_NOT_ZERO)
  #define INC_AFL_AREA(loc)           \
    asm volatile(                     \
        "addb $1, (%0, %1, 1)\n"      \
        "adcb $0, (%0, %1, 1)\n"      \
        : /* no out */                \
        : "r"(afl_area_ptr), "r"(loc) \
        : "memory", "eax")
#else
  #define INC_AFL_AREA(loc) afl_area_ptr[loc]++
#endif
```

## 总结

根据[附录 A](#a-qemu-tcg-runtime)，在上文分析了 [afl\_entry\_routine](#afl_forkserver)、[afl\_persistent\_routine](#afl_persistent_loop)、[afl\_maybe\_log\*](#afl_maybe_log) 系列函数，但还有一个功能未分析，也就是 CompareCoverage 功能，可以参考 [Compare coverage for AFL++ QEMU](https://andreafioraldi.github.io/articles/2019/07/20/aflpp-qemu-compcov.html) 这篇文章。

## 附录

### A. qemu TCG runtime

`tcg-runtime.h` 中包含一些 tcg 中使用的 afl 函数：

qemuafl/accel/tcg/tcg-runtime.h

```
DEF_HELPER_FLAGS_1(afl_entry_routine, TCG_CALL_NO_RWG, void, env)
DEF_HELPER_FLAGS_1(afl_persistent_routine, TCG_CALL_NO_RWG, void, env)
DEF_HELPER_FLAGS_1(afl_maybe_log, TCG_CALL_NO_RWG, void, tl)
DEF_HELPER_FLAGS_1(afl_maybe_log_trace, TCG_CALL_NO_RWG, void, tl)
DEF_HELPER_FLAGS_3(afl_compcov_16, TCG_CALL_NO_RWG, void, tl, tl, tl)
DEF_HELPER_FLAGS_3(afl_compcov_32, TCG_CALL_NO_RWG, void, tl, tl, tl)
DEF_HELPER_FLAGS_3(afl_compcov_64, TCG_CALL_NO_RWG, void, tl, tl, tl)
DEF_HELPER_FLAGS_3(afl_cmplog_8, TCG_CALL_NO_RWG, void, tl, tl, tl)
DEF_HELPER_FLAGS_3(afl_cmplog_16, TCG_CALL_NO_RWG, void, tl, tl, tl)
DEF_HELPER_FLAGS_3(afl_cmplog_32, TCG_CALL_NO_RWG, void, tl, tl, tl)
DEF_HELPER_FLAGS_3(afl_cmplog_64, TCG_CALL_NO_RWG, void, tl, tl, tl)
DEF_HELPER_FLAGS_1(afl_cmplog_rtn, TCG_CALL_NO_RWG, void, env)
```

### B. QEMU helper 机制

在[附录 A](#a-qemu-tcg-runtime) 中出现了很多类似 `DEF_HELPER_FLAG_*` 的宏，后面的数字显然是参数的数量，以 `gen_helper_<function name>` 的形式调用。这类 helper 可以用来生成 TCG 代码，这里简单研究一下它的实现逻辑。

以 `DEF_HELPER_FLAGS_1` 为例，它实际上有三处定义位置：

* `helper-proto.h`
  + 生成辅助函数的原型声明，用于编译器类型检查和链接。

qemuafl/include/exec/helper-proto.h

```
#define DEF_HELPER_F...