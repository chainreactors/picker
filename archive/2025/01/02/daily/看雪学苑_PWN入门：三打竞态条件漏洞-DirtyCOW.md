---
title: PWN入门：三打竞态条件漏洞-DirtyCOW
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458587913&idx=2&sn=98c0e76217bf3df9659f9e697ec2775d&chksm=b18c238386fbaa95240d646e4dd53c0b5349a023b47590b174b1ac0717f14609242a7e933442&scene=58&subscene=0#rd
source: 看雪学苑
date: 2025-01-02
fetch_date: 2025-10-06T20:08:48.710943
---

# PWN入门：三打竞态条件漏洞-DirtyCOW

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8F2tZpLR2NLoZibUSbxfiaBmFt7vRIe1b8wInTjicTDvP9uiaRNzoibTGR7Esg2qR0ibqzkpdNkrQicyIcaw/0?wx_fmt=jpeg)

# PWN入门：三打竞态条件漏洞-DirtyCOW

福建炒饭乡会

看雪学苑

```
一

脏牛漏洞
```

##

从动态链接库加载机制时，我们就知道了一个事情，Linux会将需要初始化操作推迟到真正使用时才会初始化，而不是在准备阶段就直接进行所有的初始化操作。

这一点也体现在进程的使用过程当中。

首先，上面提到过进程创建时会先复制父进程的内容然后再进行修改，然后就是假如我们通过`strace`追踪进程时会发现，进程在创建过程中使用大量的`mmap`。

要知道数据间可能是重复，如果只是读取的话，还可以继续使用父数据的所在内存，在没有修改数据的情况下，就给重复数据分配新的内存会消耗不少时间，显然只有写操作发生时，才有必要给子数据分配新的内存。所以Linux将数据的复制操作推迟到实际修改时，这一机制也被称作是写时复制`COW Copy On Write`。

那么这个延迟的COW机制会不会导致竞态条件漏洞出现呢？

## COW的实现

COW在Linux内核中使用颇为广泛，比如进程的创建、内存映射文件、虚拟化等等场景中都会用到，这里着重以`fork`创建进程的场景进行分析。

`copy_process`函数用于处理克隆进程的操作，该函数内部会复制许多东西，内存数据是其中之一，`copy_mem`函数标志着复制内存数据的开始，`copy_mem`函数会先通过`CLONE_VM`标志位判断子进程是否和父进程共用内存空间，如果共用内存空间就不会对内存进行复制。

```
SYSCALL_DEFINE2 clone3
    -> kernel_clone
        -> copy_process
            -> copy_mm
```

需要复制内存时会通过`dup_mm`函数进行复制，首先会通过`allocate_mm`函数分配`struct mm_struct`结构体需要的内存空间，`struct mm_struct`结构体会用于内存管理。

对于版本较高的Linux内核而言，它已经不再使用红黑树作为内存结构管理的数据结构了，当前使用的数据结构叫做Maple树`ma`，`dup_mmap`函数会依赖该数据结构遍历父进程全部的VMA。

如果希望某部分内存不被复制，可以使用`VM_DONTCOPY`标志位标明，`dup_mmap`函数会自动略过带有该标志的内存区域。

```
dup_mm
    -> allocate_mm
    -> dup_mmap

dup_mmap {
    ......
    MA_STATE(old_mas, &oldmm->mm_mt, 0, 0);
    MA_STATE(mas, &mm->mm_mt, 0, 0);
    ......
    mas_for_each(&old_mas, mpnt, ULONG_MAX) {
        ......
    }
    ......
}
```

找到可用的VMA时先通过`vm_area_dup`函数根据旧VMA分配出新VMA，之后`vma_dup_policy`函数会将旧VMA使用的策略延续到新的VMA中。

```
mas_for_each
    -> vm_area_dup
    -> vma_dup_policy
    -> dup_userfaultfd
    -> anon_vma_fork
    -> copy_page_range
```

`dup_userfaultfd`函数会设置新VMA的`userfaultfd`，`userfaultfd`作用是帮助用户态程序处理页错误，用户态程序可以通过系统调用注册自己的处理方法。

```
cat /usr/include/asm/unistd_64.h | grep fault
#define __NR_userfaultfd 323
```

`anon_vma_fork`会根据旧VMA的匿名内存设置新VMA的匿名内存，匿名内存机制的作用是将用户空间的虚拟内存映射到物理内存上，与常见的通过文件映射的区别在于，匿名内存映射不会与任何文件产生关系。

```
mmap映射匿名内存的选项：
MAP_PRIVATE | MAP_ANONYMOUS
```

处理好VMA的属性信息后，`copy_page_range`函数会正式开始复制内存数据。`is_cow_mapping`函数会判断当前VMA非共享内存且可写，如果符合就会当前VMA支持COW机制，然后就会通过`pgd_offset`函数获取新旧VMA的PGD，从这里开始内核会逐级遍历页表，直到最低的1级页表PTE。

```
copy_page_range
    -> is_cow_mapping
        -> copy_p4d_range
            -> copy_pud_range
                -> copy_pmd_range
                    -> copy_pte_range
```

处理PMD二级页表的`copy_pmd_range`函数中会先判断页表是否为SWAP页表、大页页表以及设备页表，如果是就对这些页表进行特殊处理。

反之如果是正常页表就会继续对一级页表进行处理。

```
copy_pmd_range
    -> is_swap_pmd || pmd_trans_huge || pmd_devmap
        -> copy_huge_pmd
    -> copy_pte_range
```

进入一级页表PTE后，`copy_pte_range`函数会针对当前PTE是否位于物理内存中，如果不在内存里面就会执行`copy_nonpresent_pte`函数，重新设置当前PTE。

反之则会进入`copy_present_pte`函数内部。

```
copy_pte_range
    -> 遍历pte
        -> copy_nonpresent_pte
        -> copy_present_pte
```

`copy_present_pte`函数首先会通过`vm_normal_page`接口获取物理页，如果物理页存在，那么就会进一步通过`PageAnon`判断是否为匿名页，如果是就会再检查该页是否已被固定，如果是就会立即通过`copy_present_page`函数进行实际的复制操作（大概率是不会执行的）。

接下来会判断VMA是否为私有可写的状态，且PTE是只读的。如果符合条件，就会设置父子进程的PTE为制度状态。

最后通过`set_pte_at`函数更新子进程的PTE。

```
copy_present_pte
    -> vm_normal_page
    -> page && PageAnon
        -> page_try_dup_anon_rmap
            -> copy_present_page、
    -> page
        -> get_page
        -> page_dup_file_rmap
    -> is_cow_mapping && pte_write
        -> ptep_set_wrprotect
        -> pte_wrprotect
    -> set_pte_at
```

从这里我们可以看到，复制进程内存的过程中大概率是不会产生内存数据的复制行为的，那么内存数据是怎么控制复制并写入的呢？

### 缺页异常

在上面提到过`xxx_wrprotect`函数会设置父子进程的PTE为只读状态，我们可能会疑惑，这样内存数据子进程是可能会修改的啊，设置成只读了还怎么改呢！

再仔细想一下，就应该这样啊！COW需要通知，收到通知后才会开始复制数据，向可写但只读的内存数据区域写入数据时，触发的缺页错误就是一种通知啊，而且这种通知还非常合理。

Linux内核处理缺页问题时，会先找到对应的PTE，然后再进行处理。

```
exc_page_fault
    -> handle_page_fault
        -> do_user_addr_fault
            -> lock_mm_and_find_vma
            -> handle_mm_fault
                -> __handle_mm_fault
                    -> handle_pte_fault
```

一级页表PTE会在`handle_pte_fault`内查找。

找到PTE后，会先判断PTE是否为空，如果是空的，就会针对是否为匿名页两种情况进行处理。

当PTE存在时，会先通过`pte_present`检查PTE是否位于内存当中，如果不在，就说明PTE位于伪内存`swap`交换分区当中，那么就会处理`swap`中的信息。在这个时候如果发现`folio`非合并页`KSM Kernel Samepage Merging`且被独占，标志位中含有`FAULT_FLAG_WRITE`存在，那么就会将`FAULT_FLAG_WRITE`清空。

接着，会检查NUM，如果内存数据位于CPU的本地缓存中，且VMA是可以访问的，那么就会将PTE交给`do_numa_page`函数处理。

最后就是检查VMF的标志位看缺页异常是不是首次出现，如果是，就继续检查PTE是否可写，如果不可写就会进入COW的处理函数`do_wp_page`，反之则会重置`_PAGE_DIRTY`位。

```
handle_pte_fault
    -> !pmd_none
        -> pte_offset_map
    -> !vmf->pte
        -> vma_is_anonymous
            -> do_anonymous_page
        -> !vma_is_anonymous
            -> do_fault
                -> !(vma->vm_flags & VM_SHARED)
                    -> do_cow_fault
                        -> finish_fault
                            -> do_set_pte
                                -> write
                                    -> maybe_mkwrite
    -> !pte_present
        -> do_swap_page
            -> folio_test_ksm && (exclusive || folio_ref_count == 1)
                -> vmf->flags & FAULT_FLAG_WRITE
                    -> ~FAULT_FLAG_WRITE
    -> pte_protnone && vma_is_accessible
        -> do_numa_page
    -> vmf->flags & (FAULT_FLAG_WRITE|FAULT_FLAG_UNSHARE)
        -> !pte_write
            -> do_wp_page
        -> vmf->flags & FAULT_FLAG_WRITE
            -> pte_mkdirty
```

从上面可以看到，有两个地方会进行COW处理，一是发现PTE不存在且非匿名页时会进入`do_fault`，`do_fault`函数发现VMA非共享状态时会处理COW，二是发现缺页异常非首次发生且触发原因是写操作时，就会进入`do_wp_page`函数。

`do_cow_fault`函数会分配新页并复制数据，而`do_wp_page`函数则会对共享页进行复制。

COW缺页的问题设置好后。内核会更新页表然后返回，进程继续执行时会发现内存页已经没有问题了，可以正常写入数据。

在`do_cow_fault`函数的最终阶段，`finish_fault`函数会设置PMD和PTE，并把信息更新到MMU，在`do_set_pte`函数设置PTE的过程中，我们可以看到各种`mkxx`和`addxxx`设置PTE信息，唯独写状态例外叫做`maybe_mkwrite`，写就写呗，什么叫做可能写？

查看`maybe_mkwrite`函数可以发现，PTE的写标志位原来需要根据VMA的状态进行设置，这样就明白了，它是要保证虚拟内存和物理内存在可写状态上保持一致。

```
static inline pte_t maybe_mkwrite(pte_t pte, struct vm_area_struct *vma)
{
    if (likely(vma->vm_flags & VM_WRITE))
        pte = pte_mkwrite(pte);
    return pte;
}

static inline pte_t pte_mkwrite(pte_t pte)
    { pte_val(pte) |= _PAGE_WRITABLE; return pte; }
```

###

### 总结

COW机制通过标记共享内存区域为只读的方式作为通知信号，写操作触发缺页异常时，缺页处理函数发现可写私有页被尝试写入内容时就会判定为COW，COW机制此时会正式开始运转，先复制内存数据再进行修改。

## 用户态程序申请内存的方式

用户态申请内存的方式可以分成`LazyAlloc`、`PreAlloc`、`Ondemand`三类。

◆`LazyAlloc`只会分配虚拟内存，当进程真正访问虚拟内存时才会分配物理内存，优点是内存资源可以得到合理的利用，缺点是首次访问内存时速度较慢。

◆`PreAlloc`会在申请虚拟内存时就建立好物理内存的映射，采用这种方式申请内存，如果申请的内存不能被充分的利用起来，就会造成浪费。

◆`Ondemand`是`LazyAlloc`和`PreAlloc`的折中方案，它的作用是在程序申请完内存后，控制内存的映射，严格来说它是一种申请内存管理方式变更的接口。

```
LazyAlloc的申请方式
    mmap不使用MAP_POPULATE标志
PreAlloc申请内存方式：
    mmap使用MAP_POPULATE标志
Ondemand设置内存的方式：
    ioctl、mlock、madivse
```

### madivse弃用内存

用户态程序获得可用的虚拟内存后，可以通过`madivse`系统调用向内核提供内存区域的处理建议。在C语言中，可以通过GLibC提供的`madivse`接口进行快速处理，第三个参数`advice`是处理建议的类型。

```
系统调用：
#define __NR_madvise 28
#define __NR_process_madvise 440

GLibC封装：
#include <sys/mman.h>
int madvise(void *addr, size_t length, int advice);
```

众多建议中有一个名为`MADV_DONTNEED`的选项，值得我们为了脏牛漏洞进行特别的关注。该选项的作用是告诉内核弃用指定区域的内存，内核收到该建议后，会对内存区域进行回收。

那么丢弃内存会起到什么作用呢？为什么脏牛漏洞因为它而产生呢？

## 内核你能访问吗！（GUP机制初探）

在Linux中缺页可能并没有想的那么严重，因为它可以被看作是内核分配物理内存的一种方式。看上去很完美了，但是啊，假设用户态程序申请了一段虚拟内存（尚未映射到物理内存），当用户态程序触发写操作时，首先面临不存在的物理内存页的角色是内核啊，内核既要处理不存在的物理页还要想其中写入数据。

假如你对内核开发有一些了解，就应该会知道作为内核即使拥有着高特权，也是不能直接操作用户空间中数据的，内核需要借助`copy_to_user`接口和`copy_from_user`接口与用户空间进行数据上的交互。

用户空间和内核空间之间访问越界的问题，是硬件实现监控的，在x86架构下该机制叫做`SMAP Supervisor Mode Access Preventio`，arm架构下该机制叫做`PAN Privilege Access Never`，Linux内核提供了接口用于开启或关闭这种机制。

```
x86：
    关闭SMAP：clac
    开启SMAP：stac

arm：
    关闭PAN：uaccess_save_and_enable(void)
    开启PAN：uaccess_restore(unsigned int flags)
```

内核需要安全的访问未映射物理内存的用户态虚拟内存，出于这种需求，内核创建了`GUP Get User Page`机制，它的作用是总是假设用户态内存是没有映射到物理内存上的。

在GUP机制的作用下，内核访问用户态虚拟的内存步骤就变成了先判断在处理，内核会通过`follow_page_mask`判断当前页是否已经完成映射，如果是就逐级查找页表进行处理，反之则触发缺页错误进程处理。

`faultin_page`函数准备进程缺页处理时，有一个很重要的错误，就是添加各种类型的缺页异常标志，比如如果发现发起者希望进行写操作，就会添加`FAULT_FLAG_WRITE`标志位，如果发现内存不是共享的，就添加`FAULT_FLAG_UNSHARE`标志位。

完成缺页处理后，如果已经正常处理，内核会再次回到`follow_page_mask`函数处执行。此时发现物理页后，就会开始逐级查找页表了。

```
get_user_pages
    -> __gup_longterm_locked
        -> __get_user_pages_locked
            -> __get_user_pages
                -> follow_page_mask
                -> page
                    -> follow_p4d_m...