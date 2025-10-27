---
title: Run lguest on Linux kernel 4.4
url: http://terenceli.github.io/%E6%8A%80%E6%9C%AF/2024/09/08/lguest-44
source: 不忘初心 方得始终
date: 2024-09-09
fetch_date: 2025-10-06T18:22:21.484820
---

# Run lguest on Linux kernel 4.4

[不忘初心 方得始终](/)

* [Archive](/archive.html)
* [About Me](/aboutMe.html)
* [Pages](/pages.html)
* [Tags](/tags.html)
* [Categories](/categories.html)

# Run lguest on Linux kernel 4.4

2024-09-08

## Background

Recently, I am preparing to study the [PVM solution](https://github.com/virt-pvm) proposed by the Linux kernel expert Lai Jiangshan. After a brief review of the paper and the patch, I found that it needs a deep understanding of paravirtualization to understand it. When I entered the field of virtualization, KVM had already dominated the virtualization field, so I did not study the implementation of paravirtualization solutions like lguest/xen from a code perspective at that time. In order to learn PVM, I must gain a more thorough understanding of lguest and xen.

lguest is the simplest paravirtualization solution, which is very suitable for learning. It was integrated into the Linux kernel in version 2.6.23 and removed in version 4.14. With the spirit of “true engineers get their hands dirty,” I am ready to run lguest right away. Of course, it is not surprising that, following the documentation, I began to set up the environment and then encountered failures, which is typical for open-source projects. This article records the problems I encountered and how I resolved them. I hope it can provide some help to the people in the field of virtualization.

## The issue

I create a VirtualBox VM and install an Ubuntu 16.04 OS in it. I choose Ubuntu 16.04 because it uses 4.4 kernel version and is a LTS version.
In order to run lguest, we need prepare following:

* Prepare the host kernel(the lg module) and the guest kernel
* The initrd file and the rootfs file
* build lguest userspace tool(like qemu)

### Build kernel

Then I download Linux kernel 4.4 source code as 4.4 is the Ubuntu 16.04 shiped with 4.4 kernel.
Following the [instruction](http://lguest.ozlabs.org/lguest.txt). I build the same kernel as guest and host. Some of the configuration:

```
            ## CONFIG_EXPERIMENTAL=y // no available
            CONFIG_PARAVIRT=y
            CONFIG_LGUEST_GUEST=y
            CONFIG_HIGHMEM64G=n
            CONFIG_PHYSICAL_ALIGN=0x100000
            CONFIG_VIRTIO_BLK=m
            CONFIG_VIRTIO_NET=m
            CONFIG_TUN=m
            CONFIG_LGUEST=m
```

### Download initrd and rootfs file

I download initrd from [here](https://download.libvirt.org/CIM/extras/initrd-1.1-i386.img)
I download rootfs from [here](https://fs.devloop.org.uk/filesystems/CentOS-6.x/CentOS6.x-x86-root_fs.bz2)

### Run it

In the Linux kerne soruce tree tools/lguest, type ‘make’ to build lguest userspace tool. Using following command to run lguest.

```
            modprobe lg
            ./lguest 64m /home/test/linux-4.4/vmlinux --tunnet=192.168.19.1 --initrd=/home/test/lguest/initrd-1.1-i386.img --block=/home/test/lguest/CentOS6.x-x86-root_fs  root=/etc/vda
```

![](/assets/img/lguest44/1.png)

As we can see we get an error “lguest: Reinjecting trap 13 for fault at 0x1afaeaa: Invalid argument”.

## The solution

### First issue: general protection fault

After reading the code, I know this is the gpf error casued by the guest. When dispatched to lguest, it can’t emulate so report this error.
Let’s first print the instruction. Add following printf to lguest.c file.

```
            default:
                    /* OK, we don't know what this is, can't emulate. */
                    printf("can't emulate:%x %x %x\n", insn[0], insn[1], insn[2]);
                    goto no_emulate;
            }
```

![](/assets/img/lguest44/2.png)

Let’s disassemble vmlinux binary and find where this instruction comes.

```
            root@test-VirtualBox:~/lguest# objdump  -S /home/test/linux-4.4/vmlinux > vmlinux1.S
            root@test-VirtualBox:~/lguest# cat vmlinux1.S  | grep "65 a1 14"  | grep afaeaa
            c1afaeaa:	65 a1 14 00 00 00    	mov    %gs:0x14,%eax
```

It’s the prologue of function ‘load\_ucode\_intel\_bsp’. The fault instruction is ‘move %gs:0x14,%eax’.

![](/assets/img/lguest44/3.png)

After some investigation, I know this instruction is introduced about ‘stack protector’. So I just build another kernel without stack canary.

```
            make "KCFLAGS=-fno-stack-protector" -j6
```

After building, let’s try.

![](/assets/img/lguest44/4.png)

### Second issue: rdmsr

Another issue. Let’s just go to 0x1034c25 to see what it is.

![](/assets/img/lguest44/5.png)

It’s ‘rdmsr’ has 2 lenght instruction. Let’s just ignore this instruction. Add following code to lguest.c.

```
            if (insn[insnlen] == 0x0f) {
                    insnlen = 2;
                    printf("ignore readmsr\n");
                    goto skip_insn;
            }
```

After this patch, we finally run lguest successfully.

![](/assets/img/lguest44/6.png)

![](/assets/img/lguest44/7.png)

The rdmsr instruction is also called from ‘load\_ucode\_bsp’ call chain.

![](/assets/img/lguest44/8.png)

## Analysis

There are two questions I don’t understand currently.

* why ‘move %gs:0x14,%eax’ instruction cause gpf
* why the guest uses native\_rdmsr instead of pv rdmsr as ‘rdmsr’ is privileged instruction

For the first issue I read the SDM and found the clue at Volume 2 Chapter 4.3 Instruction(M-U).
At the MOV-Move part:

![](/assets/img/lguest44/9.png)

And in the function ‘lguest\_arch\_setup\_regs’:
Only the ‘cs/ds/es/ss’ is initialized and the ‘gs’ is not initialized.

![](/assets/img/lguest44/10.png)

For the second issue after look at the ‘load\_ucode\_bsp’ I know the reason.

![](/assets/img/lguest44/11.png)

Here ‘call load\_ucode\_bsp’ is called by the kernel entrypoint(startup\_32). And this function is called before the lguest initialization(lguest\_init). When ‘load\_ucode\_bsp’ is called, the gs segment is not initialized and then cause a gpf. Aslo this function call invoke the ‘native\_rdmsr’ directly and which execute the instruction ‘rdmsr’ and causes the second issue.

We can notice we can eliminate this function by set CONFIG\_MICROCODE=n. I have tried this, it can work without modifying any lguest code.

* [技术 108](/categories.html#技术-ref)

* [技术 12](/tags.html#技术-ref)
* [虚拟化 24](/tags.html#虚拟化-ref)

---

* [← Previous](/%E6%8A%80%E6%9C%AF/2024/05/25/chroot-escape "The anatomy of chroot escape")
* [Archive](/archive.html)
* [Next →](/%E6%8A%80%E6%9C%AF/2025/03/01/lguest-internals "lguest internals")

---

Please enable JavaScript to view the [comments powered by Disqus.](http://disqus.com/?ref_noscript)
[blog comments powered by Disqus](http://disqus.com)

---

© 2025 Terenceli
with help from [Jekyll Bootstrap](http://jekyllbootstrap.com "The Definitive Jekyll Blogging Framework")
and [Twitter Bootstrap](http://twitter.github.com/bootstrap/)