---
title: lguest internals
url: http://terenceli.github.io/%E6%8A%80%E6%9C%AF/2025/03/01/lguest-internals
source: 不忘初心 方得始终
date: 2025-03-02
fetch_date: 2025-10-06T21:57:05.480705
---

# lguest internals

[不忘初心 方得始终](/)

* [Archive](/archive.html)
* [About Me](/aboutMe.html)
* [Pages](/pages.html)
* [Tags](/tags.html)
* [Categories](/categories.html)

# lguest internals

2025-03-01

lguest is the simpliest x86 virtualization solution. It is a paravirt hypervisor. In this post I will dive deep into the internals of lguest.

## Related files

tools/lguest/lguest.c， lguest userspace tool just like QEMU.

drivers/lguest/core.c, the core code of lguest hypervisor, including the module initialization.

drivers/lguest/hypercalls.c, hypercall related handler.

drivers/lguest/interrupts\_and\_traps.c，guest interrupt code.

drivers/lguest/lguest\_user.c, the /dev/lguest devices related code to interact with the userspace tool.

drivers/lguest/page\_table.c, mostly the shadow page table management.

drivers/lguest/segments.c, the guest idt/gdt related code.

drivers/lguest/x86/core.c, the x86 arch code, the regs setup the entry to switcher.

drivers/lguest/x86/switcher\_32.S, switcher code.

drivers/lguest is just like kvm code in kernel.

arch/x86/lguest is the guest code.

arch/x86/lguest/boot.c, lguest guest related code, like subarch init, pv ops.

arch/x86/lguest/head\_32.S, the assembly code of lguest guest.

## lguest architecture overview

Following pic shows the architecture of lguest. It contains three key components: the guest, the switcher and the lg.ko.

![](/assets/img/lguestinternals/1.png)

The guest kernel runs on hardware ring 1 and the guest userspace runs on hardware ring 3.
The switcher is used to ‘switching’ the worlds between host, guest user and guest kernel. The world switches can be triggered by a set of events such as interrupts and exceptions. The switcher comprises efficient and concise assembly code maped to identical address within host and guest kernel address spaces.
The lg.ko contains the the core hypervisor code. It exposes interface(/dev/lg) to userspace. It prepare guest environment and launch the guest and also process the guest exit events.

## Switcher

Swticher is used to do world switch. It must be located at identical virtual address in guest kernel and host. The guest user and kernel share the same page table just like the traditional Linux.
When load lg.ko, it will call ‘map\_switcher’ to map the switcher code to host. The allocation contains TOTAL\_SWITCHER\_PAGES pages.

```
            #define TOTAL_SWITCHER_PAGES (1 + 2 * nr_cpu_ids)

            static __init int map_switcher(void)
            {
            ...
                    lg_switcher_pages = kmalloc(sizeof(lg_switcher_pages[0])
                                            * TOTAL_SWITCHER_PAGES,
                                            GFP_KERNEL);
            ...
            }
```

Every physical CPU will has two pages, these two pages is used to load and store vCPU state.
Following show lg\_switcher\_pages layout.

![](/assets/img/lguestinternals/2.png)

The really switcher page is just one page, and following it is per cpu two pages.

```
            /* We have two pages shared with guests, per cpu.  */
            struct lguest_pages {
                    /* This is the stack page mapped rw in guest */
                    char spare[PAGE_SIZE - sizeof(struct lguest_regs)];
                    struct lguest_regs regs;

                    /* This is the host state & guest descriptor page, ro in guest */
                    struct lguest_ro_state state;
            } __attribute__((aligned(PAGE_SIZE)));

            /* This is a guest-specific page (mapped ro) into the guest. */
            struct lguest_ro_state {
                    /* Host information we need to restore when we switch back. */
                    u32 host_cr3;
                    struct desc_ptr host_idt_desc;
                    struct desc_ptr host_gdt_desc;
                    u32 host_sp;

                    /* Fields which are used when guest is running. */
                    struct desc_ptr guest_idt_desc;
                    struct desc_ptr guest_gdt_desc;
                    struct x86_hw_tss guest_tss;
                    struct desc_struct guest_idt[IDT_ENTRIES];
                    struct desc_struct guest_gdt[GDT_ENTRIES];
            };
```

The ‘spare’ and ‘regs’ field combines the stack for switcher. The ‘regs’ contains the guest register value.
The ‘state’ field is used to store host and guest state information.

## CPU virtualization

Without hardware support, the guest traps to host in two ways: hypercall and interrupt/execption. The hypercall is implemented via interrupt.

Following pic shows the process of VM Exit and VM Entry. When the guest execute interrupt such as interrupt-based syscall or execption, the CPU transitions to swithcher code (in h\_ring0) through the pre-defined handler in IDTR. In the switcher it first store the guest state and then restore the host state and then switch to host by calling switch\_to\_host. After completing the exit events the host call the switcher function switch\_to\_guest to enter guest, this will store the host state and load guest state.

![](/assets/img/lguestinternals/3.png)

### VM entry

In ‘lguest\_arch\_host\_init’ the ‘lguest\_entry’ struct is initialized as following:

```
            lguest_entry.offset = (long)switch_to_guest + switcher_offset();
            lguest_entry.segment = LGUEST_CS;
```

The ‘offset’ is set to ‘switch\_to\_guest’ address.
Then in ‘run\_guest\_once’, it will be used as the operand of lcall instruction.

```
            asm volatile("pushf; lcall *%4"
                    /*
                    * This is how we tell GCC that %eax ("a") and %ebx ("b")
                    * are changed by this routine.  The "=" means output.
                    */
                    : "=a"(clobber), "=b"(clobber)
                    /*
                    * %eax contains the pages pointer.  ("0" refers to the
                    * 0-th argument above, ie "a").  %ebx contains the
                    * physical address of the Guest's top-level page
                    * directory.
                    */
                    : "0"(pages),
                    "1"(__pa(cpu->lg->pgdirs[cpu->cpu_pgd].pgdir)),
                    "m"(lguest_entry)
                    /*
                    * We tell gcc that all these registers could change,
                    * which means we don't have to save and restore them in
                    * the Switcher.
                    */
                    : "memory", "%edx", "%ecx", "%edi", "%esi");
```

This lcall will goto ‘switch\_to\_guest’ which is some assembly code. These code will do the host-guest switch.
Before lcall is executed, ‘pushf’ pushs the elfags into host stack. The ‘lcall’ instruction will push ‘cs’ and ‘eip’ to host stack. At the start of ‘switch\_to\_guest’ the ‘es/ds/gs/fs/ebp’ is pushed into host stack and the ‘esp’ is stored in ‘lguest\_pages’ state->host\_cr3. After this, the host state is stored. Then we will load the guest state.

![](/assets/img/lguestinternals/4.png)

First we change the stack to switcher’s stack.

```
            movl	%eax, %edx
            addl	$LGUEST_PAGES_regs, %edx
            movl	%edx, %esp
```

Here ‘eax’ points the beginning of ‘lguest\_pages’. After these instruction, the ‘esp’ point to beginning of ‘lguest\_regs’.
Then the switcher loads the guest IDT/GDT/TSS, the most usage of TSS is used to specify the ss/esp when the guest exit to host.

```
            // The Guest's GDT we so carefully
            // Placed in the "struct lguest_pages" before
            lgdt	LGUEST_PAGES_guest_gdt_desc(%eax)

            // The Guest's IDT we did partially
            // Copy to "struct lguest_pages" as well.
            lidt	LGUEST_PAGES_guest_idt_desc(%eax)

            // The TSS entry which controls traps
            // Must be loaded up with "ltr" now:
            // The GDT entry that TSS uses
            // Changes type when we load it: damn Intel!
            // For after we switch over our page tables
            //...