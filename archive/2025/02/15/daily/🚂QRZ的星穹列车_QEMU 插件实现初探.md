---
title: QEMU 插件实现初探
url: https://qrz.today/00-notes/qemu/plugins/0.0.how-plugin-works-1
source: 🚂QRZ的星穹列车
date: 2025-02-15
fetch_date: 2025-10-06T20:36:44.793412
---

# QEMU 插件实现初探

## [🚂QRZ的星穹列车](../../..)

搜索

Search

暗色模式亮色模式

阅读模式

## 探索

[📑Tags](/tags)[🪪About](/misc/about)[📻Radio](/z6-life/ham-radio/index)[🧑‍🤝‍🧑Friends](/misc/friends)[🚇开往](https://www.travellings.cn/go.html)

---

[Home](../../../)

❯

[笔记](../../../00-notes/)

❯

[qemu](../../../00-notes/qemu/)

❯

[plugins](../../../00-notes/qemu/plugins/)

❯

QEMU 插件实现初探

# QEMU 插件实现初探

2025年2月14日6分钟阅读

* [qemu/plugins](../../../tags/qemu/plugins)

### 目录

* [编译方法](#编译方法)
* [使用方式](#使用方式)
* [机制分析](#机制分析)
* [插件加载](#插件加载)
* [插件示例](#插件示例)
* [注册机制](#注册机制)
* [插件触发](#插件触发)
* [参考资料](#参考资料)

> Info
>
> 目标 QEMU 版本为 5.2.0/5.2.50，主要分析 user mode 下的插件加载。

## 编译方法

在编译阶段，用户可以使用 `--enable-plugins` 参数启用插件功能。

* 添加该参数会向 Makefile 添加参数 `CONFIG_PLUGIN=y`。
* 在开启该参数时还会添加 `ld_dynamic_list` 或 `ld_exported_symbols_list` 参数。
  + 如果添加了 `ld_dynamic_list` 参数，则将 `plugins/qemu-plugins.symbols` 复制到 `build/qemu-plugins-ld.symbols`；
  + 如果添加了 `ld_exported_symbols_list` 参数，则会搜索 `plugins/qemu-plugins.symbols` 中所有带有 `qemu_` 的行，并进行如下操作：
    1. 去除该行的分号 `;`；
    2. 移除行首的空格，并在符号前加上 `_`

## 使用方式

以 drcov 插件为例，可以通过下面的方式使用：

```
qemu-x86_64 -plugin ./build/contrib/plugins/libdrcov.so,arg=filename=/tmp/target.drcov.trace <target> <args>
```

## 机制分析

### 插件加载

参数解析流程为：

```
main
  +-> handle_arg_plugin(const char *arg)
    +-> qemu_plugin_opt_parse(optarg, head)
      +-> plugin_add(opaque, name, value, errp)
```

`plugin_add` 函数会解析参数中的 `file` 和 `args`，并将其添加进 `qemu_plugin_desc` 结构体中，而 `qemu_plugin_desc` 结构体则会被添加进 `QemuPluginList plugins` 中。

在解析参数后，在 `main` 函数中会通过 `qemu_plugin_load_list` 加载插件，流程为：

```
qemu_plugin_load_list(QemuPluginList *head, Error **errp)
  +-> plugin_load(struct qemu_plugin_desc *desc, const qemu_info_t *info,
                  Error **errp)
    +-> g_module_symbol(ctx->handle, "qemu_plugin_install", &sym);
    +-> install = (qemu_plugin_install_func_t) sym;
    +-> g_hash_table_lookup(plugin.id_ht, &ctx->id);
    +-> QTAILQ_INSERT_TAIL(&plugin.ctxs, ctx, entry);
    +-> install(ctx->id, info, desc->argc, desc->argv);
```

这里的 `ctx` 是 `qemu_plugin_ctx` 结构体，保存了 plugin 的具体实现。插件中最重要的函数为 `qemu_plugin_install`，在找到该符号后，qemu 会将插件的 ctx 信息保存到 `qemu_plugin_state plugin` 的链表和哈希表中。在最后会调用 `qemu_plugin_install` 函数实现插件的初始化。

### 插件示例

接下来以 drcov 插件（`contrib/plugins/drcov.c`）为例研究初始化的逻辑。它的主要逻辑为：

```
qemu_plugin_install
  +-> qemu_plugin_register_vcpu_tb_trans_cb(id, vcpu_tb_trans);
  +-> qemu_plugin_register_atexit_cb(id, plugin_exit, NULL);
```

这里注册了两个接口，分别是 `qemu_plugin_register_vcpu_tb_trans_cb` 和 `qemu_plugin_register_atexit_cb`。qemu plugin 目前能够使用的所有接口可以在 `plugins/qemu-plugins.symbols` 中找到。

对于 drcov 插件在 install 中注册的两个回调：

* `qemu_plugin_register_vcpu_tb_trans_cb` 注册的 `vcpu_tb_trans` 函数会在 `qemu_plugin_tb_trans_cb` 中调用；
* `qemu_plugin_register_atexit_cb` 注册的 `plugin_exit` 函数会在 `qemu_plugin_atexit_cb` 中调用。

总的来说，该插件的工作逻辑为：

* QEMU 初始化
  + 分配 `blocks` 和 `modules`。
* QEMU 运行
  + 翻译阶段：
    - 获取当前 pc 所在 `module`；
    - 为每个 TB 创建 `bb_entry_t` 并保存到 `blocks` 数组；
    - 注册回调函数 `vcpu_tb_exec`，其参数为 `bb_entry_t`。
  + 执行阶段
    - 设置传入的 `bb_entry_t` 为已执行。
* QEMU 退出
  + 生成 drcov 文件
    - 遍历 `blocks` 数组，根据 `bb->exec` 情况生成覆盖率信息。

### 注册机制

接下来研究一下 drcov 插件所使用的两个回调的注册机制。

`qemu_plugin_register_vcpu_tb_trans_cb` 的逻辑为：

```
qemu_plugin_register_vcpu_tb_trans_cb(id, vcpu_tb_trans)
  +-> qemu_plugin_register_vcpu_tb_trans_cb(id, vcpu_tb_trans)
    +-> plugin_register_cb(id, QEMU_PLUGIN_EV_VCPU_TB_TRANS, cb)
      +-> do_plugin_register_cb(id, ev, func, NULL)
```

`qemu_plugin_register_atexit_cb` 的逻辑为：

```
qemu_plugin_register_atexit_cb(id, plugin_exit, NULL)
  +-> plugin_register_cb_udata(id, QEMU_PLUGIN_EV_ATEXIT, cb, udata)
    +-> do_plugin_register_cb(id, ev, func, udata)
```

在 `do_plugin_register_cb` 函数中，QEMU 会将回调函数 `func` 保存在插件对应 `qemu_plugin_ctx` 的 `qemu_plugin_cb` 结构中。

> `qemu_plugin_ctx` 和 `qemu_plugin_cb` 的获取方式
>
> ```
> ctx = plugin_id_to_ctx_locked(id);
> ... ...
> struct qemu_plugin_cb *cb = ctx->callbacks[ev];
> ```
>
> `cb` 是 `ctx` 中对应 `ev` 的数组。`ev` 即对应于 `plugin_register_cb*` 传入的事件。QEMU 提供了若干个事件的支持：
>
> include/qemu/plugin.h
>
> ```
> /*
>  * Events that plugins can subscribe to.
>  */
> enum qemu_plugin_event {
>     QEMU_PLUGIN_EV_VCPU_INIT,
>     QEMU_PLUGIN_EV_VCPU_EXIT,
>     QEMU_PLUGIN_EV_VCPU_TB_TRANS,
>     QEMU_PLUGIN_EV_VCPU_IDLE,
>     QEMU_PLUGIN_EV_VCPU_RESUME,
>     QEMU_PLUGIN_EV_VCPU_SYSCALL,
>     QEMU_PLUGIN_EV_VCPU_SYSCALL_RET,
>     QEMU_PLUGIN_EV_FLUSH,
>     QEMU_PLUGIN_EV_ATEXIT,
>     QEMU_PLUGIN_EV_MAX, /* total number of plugin events we support */
> };
> ```

### 插件触发

#### vcpu\_tb\_trans

在 QEMU 翻译执行时就会在特定位置触发插件的回调函数。以 drcov 插件实现的 `vcpu_tb_trans` 为例，在翻译阶段带插件的逻辑为：

accel/tcg/translator.c:translator\_loop

```
translator_loop
  +-> plugin_enabled = plugin_gen_tb_start(...)
  +-> while (true)
    +-> plugin_gen_insn_start(cpu, db)
    +-> translate_insn(db, cpu)
    +-> plugin_gen_insn_end()
  +-> gen_tb_end(db->tb, db->num_insns - bp_insn)
  +-> plugin_gen_tb_end(cpu)
```

在上面的逻辑中，`plugin_gen_tb_start`、`plugin_gen_insn_start`、`plugin_gen_insn_end` 这几个插件接口函数主要用于插入桩函数，它们最后都会调用 `plugin_gen_empty_callback`：

```
plugin_gen_tb_start
  +-> plugin_gen_empty_callback(PLUGIN_GEN_FROM_TB)
plugin_gen_insn_start
  +-> plugin_gen_empty_callback(PLUGIN_GEN_FROM_INSN)
plugin_gen_insn_end
  +-> plugin_gen_empty_callback(PLUGIN_GEN_AFTER_INSN)
```

`plugin_gen_tb_end` 主要做桩函数的替换，其基本逻辑为：

```
plugin_gen_tb_end
  +-> qemu_plugin_tb_trans_cb(cpu, ptb)
  +-> plugin_gen_inject(ptb)
```

`qemu_plugin_tb_trans_cb` 函数会遍历 `QEMU_PLUGIN_EV_VCPU_TB_TRANS` 事件对应插件的函数并执行：

```
/*
 * Disable CFI checks.
 * The callback function has been loaded from an external library so we do not
 * have type information
 */
QEMU_DISABLE_CFI
void qemu_plugin_tb_trans_cb(CPUState *cpu, struct qemu_plugin_tb *tb)
{
    struct qemu_plugin_cb *cb, *next;
    enum qemu_plugin_event ev = QEMU_PLUGIN_EV_VCPU_TB_TRANS;

    /* no plugin_mask check here; caller should have checked */

    QLIST_FOREACH_SAFE_RCU(cb, &plugin.cb_lists[ev], entry, next) {
        qemu_plugin_vcpu_tb_trans_cb_t func = cb->f.vcpu_tb_trans;

        func(cb->ctx->id, tb);
    }
}
```

正是在这个位置执行了上文 drcov 插件注册的 `vcpu_tb_trans` 函数。该函数最后会调用 `qemu_plugin_register_vcpu_tb_exec_cb` 函数，它会注册 `vcpu_tb_exec` 函数，该函数将在翻译块执行的时候运行。

而 `plugin_gen_inject` 则会向模拟执行的代码中注入插件的代码，等到 QEMU 执行 tb 的时候，就会调用上文注册的 `vcpu_tb_exec` 函数。这一段逻辑和 QEMU JIT 代码有关，较为复杂，这里只记录大概逻辑而不进行更为详细的分析。

#### plugin\_exit

`plugin_exit` 函数在 `QEMU_PLUGIN_EV_ATEXIT` 事件发生时触发，它在两个位置调用：

1. QEMU 插件功能初始化时（`plugins/core.c:plugin_init`）通过 `atexit` 函数调用；
2. 在触发退出信号时（例如 `TARGET_NR_exit` 或 `TARGET_NR_exit_group`）通过 `preexit_cleanup` 函数调用。

## 参考资料

* [QEMU TCG Plugins](https://www.qemu.org/docs/master/devel/tcg-plugins.html)
* [qemu plugin基本逻辑分析](https://wangzhou.github.io/qemu-plugin%E5%9F%BA%E6%9C%AC%E9%80%BB%E8%BE%91%E5%88%86%E6%9E%90/)

---

### 目录

* [编译方法](#编译方法)
* [使用方式](#使用方式)
* [机制分析](#机制分析)
* [插件加载](#插件加载)
* [插件示例](#插件示例)
* [注册机制](#注册机制)
* [插件触发](#插件触发)
* [参考资料](#参考资料)

### 关系图谱

### 反向链接

* [欢迎！](../../../)

---

Made with ❤️ by QRZ using [Obsidian](https://obsidian.md/) and [Quartz](https://quartz.jzhao.xyz/), © 2025. [RSS Feed](https://qrz.today/index.xml)