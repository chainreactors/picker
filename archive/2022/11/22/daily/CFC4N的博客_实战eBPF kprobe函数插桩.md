---
title: 实战eBPF kprobe函数插桩
url: https://www.cnxct.com/using-ebpf-kprobe-to-file-notify/
source: CFC4N的博客
date: 2022-11-22
fetch_date: 2025-10-03T23:23:44.358737
---

# 实战eBPF kprobe函数插桩

Toggle navigation

[CFC4N的博客](https://www.cnxct.com/ "CFC4N的博客")
希望与理想是最令人珍惜的部分!

* 作品
  + [eCapture旁观者–HTTPS/TLS抓包](https://ecapture.cc "eCapture旁观者--HTTPS/TLS抓包")
  + [Golang eBPF Manager](https://github.com/gojue/ebpfmanager "Golang eBPF Manager")
  + [eBPF技术精选资料](https://github.com/gojue/ehids-slide "eBPF技术精选资料")
  + [League Of legends启动器](https://github.com/cfc4n/lol_launcher "League Of legends启动器")
  + [eBPF HIDS主机入侵检测](https://github.com/gojue/ehids-agent "eBPF HIDS主机入侵检测")
* [归档](https://www.cnxct.com/archives/ "归档")
* [关于我](https://www.cnxct.com/about/ "关于我")
* [工作机会](https://www.cnxct.com/jobs/ "工作机会")

# 实战eBPF kprobe函数插桩

[2022/11/212022/11/21](https://www.cnxct.com/using-ebpf-kprobe-to-file-notify/)  [CFC4N](https://www.cnxct.com/author/admin/)

### 文章目录

1. [插桩的程序类型选择](#ftoc-heading-1)
2. [如何获取插桩函数中第 6 个参数](#ftoc-heading-2)
3. [插桩函数超过 6 个参数怎么办](#ftoc-heading-3)
4. [Linux Amd64 调用约定](#ftoc-heading-4)
   1. [demo 验证](#ftoc-heading-5)
   2. [eBPF 字节码反汇编](#ftoc-heading-6)
   3. [用户空间程序调用](#ftoc-heading-7)
   4. [寄存器堆栈状态](#ftoc-heading-8)
   5. [实战 kprobe 获取 6 个以上参数](#ftoc-heading-9)
5. [参考文献：](#ftoc-heading-10)

本文内容，如非特殊说明，均基于 4.18 内核，x86-64 CPU 架构。

### 插桩的程序类型选择

说起 eBPF 大家都不陌生，就内核而言，hook 会尽可能选在 tracepoint，如果没有 tracepoint，会考虑使用 kprobe。

tracepoint 的范围有限，而内核函数又太多，基于各种需求场景，kprobe 的出场机会较多；但需要注意的，并不是所有的内核函数都可以选做 hook 点，inline 函数无法被 hook，static 函数也有可能被优化掉；如果想知道究竟有哪些函数可以选做 hook 点，在 Linux 机器上，可以通过`less /proc/kallsyms`查看。

使用 eBPF 时，内核代码 kprobe 的书写范例如下：

```
SEC("kprobe/vfs_write")
int kprobe_vfs_write(struct pt_regs *regs)
{
    struct file *file
    file = (struct file *)PT_REGS_PARM1(regs);
    // ...
}
```

其中 pt\_regs 的结构体如下：

```
struct pt_regs {
/*
 * C ABI says these regs are callee-preserved. They aren't saved on kernel entry
 * unless syscall needs a complete, fully filled "struct pt_regs".
 */
    unsigned long r15;
    unsigned long r14;
    unsigned long r13;
    unsigned long r12;
    unsigned long bp;
    unsigned long bx;
/* These regs are callee-clobbered. Always saved on kernel entry. */
    unsigned long r11;
    unsigned long r10;
    unsigned long r9;
    unsigned long r8;
    unsigned long ax;
    unsigned long cx;
    unsigned long dx;
    unsigned long si;
    unsigned long di;
/*
 * On syscall entry, this is syscall#. On CPU exception, this is error code.
 * On hw interrupt, it's IRQ number:
 */
    unsigned long orig_ax;
/* Return frame for iretq */
    unsigned long ip;
    unsigned long cs;
    unsigned long flags;
    unsigned long sp;
    unsigned long ss;
/* top of stack page */
};
```

通常来说，我们要获取的参数，均可通过诸如 PT\_REGS\_PARM1 这样的宏来拿到，宏定义如下：

```
#define PT_REGS_PARM1(x) ((x)->di)
#define PT_REGS_PARM2(x) ((x)->si)
#define PT_REGS_PARM3(x) ((x)->dx)
#define PT_REGS_PARM4(x) ((x)->cx)
#define PT_REGS_PARM5(x) ((x)->r8)
```

可以看到，上述的宏只能获取 5 个参数；但是在最近的一个项目中，就遇到了如何获取超过 5 个参数的难题，这也是本文的由来，如果你也有类似的困惑，本文也许是为你准备的。

### 如何获取插桩函数中第 6 个参数

上述的 5 个宏已经可以覆盖大多数的获取小于 5 个参数的需求，不知道大家有没有想过，使用 eBPF 时如果获取的参数个数大于 5 个怎么办呢？

如下的内核函数`__get_user_pages`（幸运的是，该 static 函数并未被优化掉）：

```
static long __get_user_pages(struct task_struct *tsk, struct mm_struct *mm,
        unsigned long start, unsigned long nr_pages,
        unsigned int gup_flags, struct page **pages,
        struct vm_area_struct **vmas, int *nonblocking)
```

在希望对这个函数进行 hook 的时候犯了难，该函数总共有 8 个参数，如果想拿到最后 3 个参数，该如何操作呢？

且看 BCC 是如何操作的。

BCC 代码中明确表明：只支持寄存器参数。那什么是寄存器参数呢？其实就是内核函数调用约定中的前 6 个参数要通过寄存器传递，只支持这前六个寄存器参数。

```
constexpr int MAX_CALLING_CONV_REGS = 6;
const char *calling_conv_regs_x86[] = {
  "di", "si", "dx", "cx", "r8", "r9"
};

bool BTypeVisitor::VisitFunctionDecl(FunctionDecl *D) {
    if (D->param_size() > MAX_CALLING_CONV_REGS + 1) {
      error(GET_BEGINLOC(D->getParamDecl(MAX_CALLING_CONV_REGS + 1)),
            "too many arguments, bcc only supports in-register parameters");
      return false;
    }
}
```

BCC 中使用如下的代码对用户写的`BPF text`进行`rewrite`，覆盖的参数刚好是前 6 个参数，分别保存于`di, si, dx, cx, r8, r9`寄存器：

```
const char *calling_conv_regs_x86[] = {
  "di", "si", "dx", "cx", "r8", "r9"
};

void BTypeVisitor::genParamDirectAssign(FunctionDecl *D, string& preamble,
                                        const char **calling_conv_regs) {
  for (size_t idx = 0; idx < fn_args_.size(); idx++) {
    ParmVarDecl *arg = fn_args_[idx];

    if (idx >= 1) {
      // Move the args into a preamble section where the same params are
      // declared and initialized from pt_regs.
      // Todo: this init should be done only when the program requests it.
      string text = rewriter_.getRewrittenText(expansionRange(arg->getSourceRange()));
      arg->addAttr(UnavailableAttr::CreateImplicit(C, "ptregs"));
      size_t d = idx - 1;
      const char *reg = calling_conv_regs[d];
      preamble += " " + text + " = (" + arg->getType().getAsString() + ")" +
                  fn_args_[0]->getName().str() + "->" + string(reg) + ";";
    }
  }
}
```

看到这里，大家应该明白，之所以能使用 BCC 提供的如此简便的 python 接口（**内核函数前面加上前缀 kprobe\_\_，第一个参数永远是`struct pt_regs *`，然后需要使用几个内核参数就填写几个**）来做一些监控工作，是因为 BCC 在幕后做了大量的 rewirte 工作，respect！

```
int kprobe__tcp_v4_connect(struct pt_regs *ctx, struct sock *sk) {
    [...]
}
```

之前总是由于 eBPF 给的限制（按照 eBPF 的 calling convention，只有 5 个参数可以传递），以为更多的参数是无法获取的。实际上可以回忆下，实际上按照 amd64 的调用约定，最多是可以通过寄存器传递 6 个参数的。

这么看下来，获取第 6 个参数的方案其实也是很简单，手动添加如下的宏即可：

```
#define PT_REGS_PARM6(x) ((x)->r9)
```

## 插桩函数超过 6 个参数怎么办

amd64 的调用约定同样规定了，超过 6 个的参数，都会在栈上传递，具体可以参考`regs_get_kernel_argument`

那么如果参数超过 6 个，处理方案呼之欲出：从栈上获取。

`regs_get_kernel_argument`该函数在新版本的内核中才有，实现如下：

```
static inline unsigned long regs_get_kernel_argument(struct pt_regs *regs,
                             unsigned int n)
{
    static const unsigned int argument_offs[] = {
#ifdef __i386__
        offsetof(struct pt_regs, ax),
        offsetof(struct pt_regs, dx),
        offsetof(struct pt_regs, cx),
#define NR_REG_ARGUMENTS 3
#else
        offsetof(struct pt_regs, di),
        offsetof(struct pt_regs, si),
        offsetof(struct pt_regs, dx),
        offsetof(struct pt_regs, cx),
        offsetof(struct pt_regs, r8),
        offsetof(struct pt_regs, r9),
#define NR_REG_ARGUMENTS 6
#endif
    };

    if (n >= NR_REG_ARGUMENTS) {
        n -= NR_REG_ARGUMENTS - 1;
        return regs_get_kernel_stack_nth(regs, n);
    } else
        return regs_get_register(regs, argument_offs[n]);
}
```

从上述的代码可以看到，常用的前 6 个参数，确实是在寄存器中获取，分别是`di, si, dx, cx, r8, r9`，这也印证了我们之前的想法，且和 BCC 中的行为是一致的。

从`regs_get_kernel_argument`中也可以看到，从第 7 个参数开始，便开始从栈上获取了，关键函数为：`regs_get_kernel_stack_nth`，这个函数在 4.18 内核中也有，如下：

```
static inline unsigned long regs_get_kernel_stack_nth(struct pt_regs *regs, unsigned int n)
{
    unsigned long *addr = (unsigned long *)kernel_stack_pointer(regs);
    addr += n;
    if (regs_within_kernel_stack(regs, (unsigned long)addr))
        return *addr;
    else
        return 0;
}

// 等价于bpf提供的帮助宏 #define PT_REGS_SP(x) ((x)->sp)
static inline unsigned long kernel_stack_pointer(struct pt_regs *regs)
{
    return regs->sp;
}
```

`regs_get_kernel_stack_nth`是标准的栈上操作获取，只不过内核提供了一些地址合法性的检查，不考虑这些的话，在 eBPF 中其实可以一步到位；使用如下函数，便能返回栈上的第 n 个参数（从 1 开始）。

```
static __always_inline unsigned long regs_get_kernel_stack_nth(struct pt_regs *regs,
                              unsigned int n)
{
    unsigned long *addr;
  unsigned long val;

    addr = (unsigned long *)PT_REGS_SP(x) + n;
    if (addr) {
        bpf_probe_read(&val, sizeof(val), addr);
        return val;
    }
    return 0;
}
```

捎带提一句，在 amd64 中，eBPF calling ABI 使用了 R1-R5 来传递参数，且做了如下的寄存器映射约定，方便 jit 转换为 native code，提高效率。

```
R0 – rax      return value from function
R1 – rdi      1st argument
R2 – rsi      2nd argument
R3 – rdx      3rd argument
R4 – rcx      4th argument
R5 – r8       5th argument
R6 – rbx      callee saved
R7 - r13      callee saved
R8 - r14      callee saved
R9 - r15      callee saved
R10 – rbp     frame pointer
```

而 R0 – R10，是 bpf 虚拟机的内部的特殊标识符（函数调用等地方使用），如果 jit 可用，bpf code 会被翻译为`native code`。

## Linux Amd64 调用约定

#### demo 验证

那 Amd64 的 ABI 是如何操作的呢？可以使用如下的代码进行验证:

```
# cat myfunc.c
i...