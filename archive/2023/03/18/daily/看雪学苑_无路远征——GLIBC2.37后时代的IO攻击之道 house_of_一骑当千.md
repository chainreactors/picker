---
title: 无路远征——GLIBC2.37后时代的IO攻击之道 house_of_一骑当千
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458498685&idx=1&sn=2a422ec7d8df18d4a00a08ae00d6bcf9&chksm=b18e86f786f90fe1ee9a94f9d71e76900091e6d7f9ba8f0bb9f86613e4fbd84c9434c4ca6ab6&scene=58&subscene=0#rd
source: 看雪学苑
date: 2023-03-18
fetch_date: 2025-10-04T09:58:44.645312
---

# 无路远征——GLIBC2.37后时代的IO攻击之道 house_of_一骑当千

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchNSx2ujUawcMS7UumN5fJrphyTr0UicTIZbxjxRGsGUsAExN8Y6RMtWxA/0?wx_fmt=jpeg)

# 无路远征——GLIBC2.37后时代的IO攻击之道 house\_of\_一骑当千

我超啊

看雪学苑

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8EGhnFtJH2ysic4o9sUdFchNH9T0A8q8UuIibGoCHPLkyFP6SogCicEfWJ11tRLf9YYDdF1Nb4jcuBfQ/640?wx_fmt=png)

本文为看雪论坛精华文章

看雪论坛作者ID：我超啊

沙盒是现在pwn题中绕不过的砍，前面提出的house\_of\_魑魅魍魉 和 house\_of\_琴瑟琵琶都没有提供绕过沙盒的方法，尤其是house\_of\_琴瑟琵琶只能控制一个参数，目前看来基本上无法绕过沙盒。而house\_of\_一骑当千是一种只用setcontext就定能绕过沙盒攻击手法。

#

#

```
一

setcontext+53之殇
```

setcontext+53是打pwn中常用的技术，主要是依靠程序中如下代码段来实现寄存器赋值。在2.31后变成了setcontext+61，主要控制的寄存器也从rdi变成了rdx。setcontext+53是执行orw的重要攻击手段，由于属于常见方式就不再赘述。

![](https://mmbiz.qpic.cn/sz_mmbiz_png/1UG7KPNHN8GMjqO82AGRWSJrIX9Umhlnsic5XJoLswqPJhuDpsoibDicJW0KH74Nj7o8deDKFw26cesXB6apPBeKQ/640?wx_fmt=png)

setcontext+53作为常用的攻击手段，在版本迭代中主要参数已经从rdi修复成rdx，rdx是一个函数的第3个参数。但是，在实际攻击过程中，只能控制一个参数，所以rdx不可控。目前，很多利用的方法，例如house\_of\_KIWI house\_of\_cat等中rdx都是编译级别的利用方式，可以很容易被修复，或者编译器发生变化也可能不再能使用。 house\_of\_KIWI出现很大一部分是解决了rdx的问题。house\_of\_emma也必须借助 house\_of\_KIWI才能绕过seccomp。

以2.37以后还能使用的house\_of\_cat为例，对比源码和汇编可以发现，rdx之所以可控是因为，编译器在处理比较时使用了rdx。

```
int_IO_switch_to_wget_mode (FILE *fp){    // 编译器在处理这一段时使用 rdx  if (fp->_wide_data->_IO_write_ptr > fp->_wide_data->_IO_write_base)    if ((wint_t)_IO_WOVERFLOW (fp, WEOF) == WEOF)      return EOF;  ......}
```

```
► 0x7f4cae745d30 <_IO_switch_to_wget_mode>       endbr64  0x7f4cae745d34 <_IO_switch_to_wget_mode+4>     mov    rax, qword ptr [rdi + 0xa0]  0x7f4cae745d3b <_IO_switch_to_wget_mode+11>    push   rbx  0x7f4cae745d3c <_IO_switch_to_wget_mode+12>    mov    rbx, rdi  0x7f4cae745d3f <_IO_switch_to_wget_mode+15>    mov    rdx, qword ptr [rax + 0x20]  0x7f4cae745d43 <_IO_switch_to_wget_mode+19>    cmp    rdx, qword ptr [rax + 0x18]  0x7f4cae745d47 <_IO_switch_to_wget_mode+23>    jbe    _IO_switch_to_wget_mode+56                <_IO_switch_to_wget_mode+56>   0x7f4cae745d49 <_IO_switch_to_wget_mode+25>    mov    rax, qword ptr [rax + 0xe0]  0x7f4cae745d50 <_IO_switch_to_wget_mode+32>    mov    esi, 0xffffffff  0x7f4cae745d55 <_IO_switch_to_wget_mode+37>    call   qword ptr [rax + 0x18]
```

因为setcontext是汇编所写（下面会详写），显然rdi修复成rdx也是GNU有意而为，今后也可能被修改成rcx甚至r15，靠编译级别的攻击手段显然不能长久。如何能够完美绕过沙盒呢？

#

#

```
二

ucontext函数族分析
```

##

## 1.函数族

研究setcontext之前，我们要知道一个函数族，就是ucontext 函数族，它包括以下函数。

```
int getcontext(ucontext_t *ucp);int setcontext(const ucontext_t *ucp)void makecontext(ucontext_t *ucp, void (*func)(), int argc, ...);int swapcontext(ucontext_t *restrict oucp,const ucontext_t *restrict ucp);
```

> 1. getcontext用来获取用户上下文，
> 2. setcontext用来设置用户上下文
> 3. makecontext操作用户上下文，可以设置执行函数，本质调用`setcontext``
> 4. swapcontext进行两个上下文的交换

显然，虽然说用户上下文这么高深的词语，其实就是一块内存中存储了一些必要的数据。

##

## **2.setcontext**

以我们关注的setcontext为例 ，它是由汇编所写，在 /sysdeps/unix/sysv/linux/x86\_64/setcontext.S中。剥离复杂的宏之后发现，除了信号量系统调(\_\_NR\_rt\_sigprocmask)用外，无非就是一些赋值操作。（代码虽然很长，但为了展现全貌我就不做删减了，大家关注中文注释的地方）

```
ENTRY(__setcontext)    /* Save argument since syscall will destroy it.  */    pushq    %rdi    cfi_adjust_cfa_offset(8)     /* Set the signal mask with       rt_sigprocmask (SIG_SETMASK, mask, NULL, _NSIG/8).  */    leaq    oSIGMASK(%rdi), %rsi    xorl    %edx, %edx    movl    $SIG_SETMASK, %edi    movl    $_NSIG8,%r10d    movl    $__NR_rt_sigprocmask, %eax    syscall    /* Pop the pointer into RDX. The choice is arbitrary, but       leaving RDI and RSI available for use later can avoid       shuffling values.  */    popq    %rdx   # 这是就是 rdi 向 rdx转换的关键。    cfi_adjust_cfa_offset(-8)    cmpq    $-4095, %rax        /* Check %rax for error.  */    jae    SYSCALL_ERROR_LABEL    /* Jump to error handler if error.  */     /* Restore the floating-point context.  Not the registers, only the       rest.  */    movq    oFPREGS(%rdx), %rcx    fldenv    (%rcx)    ldmxcsr oMXCSR(%rdx)      /* Load the new stack pointer, the preserved registers and       registers used for passing args.  */    cfi_def_cfa(%rdx, 0)    cfi_offset(%rbx,oRBX)    cfi_offset(%rbp,oRBP)    cfi_offset(%r12,oR12)    cfi_offset(%r13,oR13)    cfi_offset(%r14,oR14)    cfi_offset(%r15,oR15)    cfi_offset(%rsp,oRSP)    cfi_offset(%rip,oRIP)    /* 这里往下就是 setcontext+61 的地方*/    movq    oRSP(%rdx), %rsp    movq    oRBX(%rdx), %rbx    movq    oRBP(%rdx), %rbp    movq    oR12(%rdx), %r12    movq    oR13(%rdx), %r13    movq    oR14(%rdx), %r14    movq    oR15(%rdx), %r15 #if SHSTK_ENABLED    /* Check if shadow stack is enabled.  */    testl    $X86_FEATURE_1_SHSTK, %fs:FEATURE_1_OFFSET    jz    L(no_shstk)     /* If the base of the target shadow stack is the same as the       base of the current shadow stack, we unwind the shadow       stack.  Otherwise it is a stack switch and we look for a       restore token.  */    movq    oSSP(%rdx), %rsi    movq    %rsi, %rdi     /* Get the base of the target shadow stack.  */    movq    (oSSP + 8)(%rdx), %rcx    cmpq    %fs:SSP_BASE_OFFSET, %rcx    je    L(unwind_shadow_stack) L(find_restore_token_loop):    /* Look for a restore token.  */    movq    -8(%rsi), %rax    andq    $-8, %rax    cmpq    %rsi, %rax    je    L(restore_shadow_stack)     /* Try the next slot.  */    subq    $8, %rsi    jmp    L(find_restore_token_loop) L(restore_shadow_stack):    /* Pop return address from the shadow stack since setcontext       will not return.  */    movq    $1, %rax    incsspq    %rax     /* Use the restore stoken to restore the target shadow stack.  */    rstorssp -8(%rsi)     /* Save the restore token on the old shadow stack.  NB: This       restore token may be checked by setcontext or swapcontext       later.  */    saveprevssp     /* Record the new shadow stack base that was switched to.  */    movq    (oSSP + 8)(%rdx), %rax    movq    %rax, %fs:SSP_BASE_OFFSET L(unwind_shadow_stack):    rdsspq    %rcx    subq    %rdi, %rcx    je    L(skip_unwind_shadow_stack)    negq    %rcx    shrq    $3, %rcx    movl    $255, %esiL(loop):    cmpq    %rsi, %rcx    cmovb    %rcx, %rsi    incsspq    %rsi    subq    %rsi, %rcx    ja    L(loop) L(skip_unwind_shadow_stack):    movq    oRSI(%rdx), %rsi    movq    oRDI(%rdx), %rdi    movq    oRCX(%rdx), %rcx    movq    oR8(%rdx), %r8    movq    oR9(%rdx), %r9     /* Get the return address set with getcontext.  */    movq    oRIP(%rdx), %r10     /* Setup finally %rdx.  */    movq    oRDX(%rdx), %rdx     /* Check if return address is valid for the case when setcontext       is invoked from __start_context with linked context.  */    rdsspq    %rax    cmpq    (%rax), %r10    /* Clear RAX to indicate success.  NB: Don't use xorl to keep       EFLAGS for jne.  */    movl    $0, %eax    jne    L(jmp)    /* Return to the new context if return address valid.  */    pushq    %r10    ret L(jmp):    /* Jump to the new context directly.  */    jmp    *%r10 L(no_shstk):#endif    /* The following ret should return to the address set with    getcontext.  Therefore push the address on the stack.  */    movq    oRIP(%rdx), %rcx    pushq    %rcx     movq    oRSI(%rdx), %rsi    movq    oRDI(%rdx), %rdi    movq    oRCX(%rdx), %rcx    movq    oR8(%rdx), %r8    movq    oR9(%rdx), %r9     /* Setup finally %rdx.  */    movq    oRDX(%rdx), %rdx     /* End FDE here, we fall into another context.  */    cfi_endproc    cfi_startproc     /* Clear rax to indicate success.  */    xorl    %eax, %eax    retPSEUDO_END(__setcontext) weak_alias (__setcontext, setcontext)
```

#

#

```
三

ucontext结构体
```

从ucontext函数族中可以看到存在ucontext类型的结构体，也就是传入setcontext的rdi。这个结构体如下。

```
typedef struct ucontext_t  {    unsigned long int __ctx(uc_flags); // 1个字长    struct ucontext_t *uc_link;//1个字长    stack_t uc_stack; //3个字长    mcontext_t uc_mcontext; //操作部分1    sigset_t uc_sigmask; //操作部分2    struct _libc_fpstate __fpregs_mem; //操作部分3     __extension__ unsigned long long int __ssp[4];//操作部分4  } ucontext_t;
```

在setcontext函数中，除了对mcontext\_t uc\_mcontext; sigset\_t uc\_sigmask; struct \_libc\_fpstate \_\_fpregs\_mem \_\_ssp这4个进行操作外，并没有对其他部分操作，也就是我们可以不关心其他的值。

##

#...