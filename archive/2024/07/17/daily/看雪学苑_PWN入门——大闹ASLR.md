---
title: PWN入门——大闹ASLR
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458563721&idx=2&sn=372555a953b873c8285e2cbae581f143&chksm=b18d840386fa0d1526cc9ea5c3850398c5eed5c66fce6676d46f213120df72edb29e97a7f648&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-07-17
fetch_date: 2025-10-06T17:41:53.436840
---

# PWN入门——大闹ASLR

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8EDOEyyAjIYqJ7ZShibj1sPqxJiacR9sGRA7QLCYiccBSOTwaRYwFEAU73nrE2bXpLqQfIf2VmbH16mg/0?wx_fmt=jpeg)

# PWN入门——大闹ASLR

福建炒饭乡会

看雪学苑

当ASLR（地址空间布局随机化`Address Space Layout Randomization`）机制关闭时，程序每次运行时的内存布局都是相同的，当该机制处于打开状态时，程序每次运行时的内存布局都会发生变化。

```
0：完全关闭
1：部分开启（堆、栈、MMAP、动态链接库）
2：完全开启（BRK、堆、栈、MMAP、动态链接库）

echo xxx | sudo tee -a /proc/sys/kernel/randomize_va_space
```

在之前的PWN过程中，ASLR机制都是关闭的，并且在`exploit`一定会设置绝对内存地址，此时完成PWN是在假定知道内存布局的情况下完成的。

下面以栈所在内存空间为例，展示了ASLR开启后的内存布局变化。

```
第一次运行：
7ffd1b667000-7ffd1b688000 rw-p 00000000 00:00 0                          [stack]

第二次运行：
7ffd7024c000-7ffd7026d000 rw-p 00000000 00:00 0                          [stack]
```

#

```
一

ASLR的实现
```

程序加载到内存中的内存布局是由操作系统决定的，通过上面的ASLR开关方式也可以知道，用户空间可以借助内核提供的`proc`虚文件对ASLR进行控制。

## 1.1 虚文件系统

Linux中秉承着一切皆文件的理念，考虑到文件系统类型的多样性，为了避免用户空间程序操作文件时仍需要考虑不同文件系统带来的差异问题，Linux提供了一个统一的接口供用户空间使用，它就是VFS（虚拟文件系统`Virtual File System`）。

VFS为了支持各种文件系统，它定义一套所有文件系统都支持的接口和数据结构，用于支持各类文件系统和VFS协同工作。

```
struct file_system_type {
    const char *name;
    int fs_flags;
#define FS_REQUIRES_DEV		1
#define FS_BINARY_MOUNTDATA	2
#define FS_HAS_SUBTYPE		4
#define FS_USERNS_MOUNT		8	/* Can be mounted by userns root */
#define FS_DISALLOW_NOTIFY_PERM	16	/* Disable fanotify permission events */
#define FS_ALLOW_IDMAP         32      /* FS has been updated to handle vfs idmappings. */
#define FS_RENAME_DOES_D_MOVE	32768	/* FS will handle d_move() during rename() internally. */
    int (*init_fs_context)(struct fs_context *);
    const struct fs_parameter_spec *parameters;
    struct dentry *(*mount) (struct file_system_type *, int,
               const char *, void *);
    void (*kill_sb) (struct super_block *);
    struct module *owner;
    struct file_system_type * next;
    struct hlist_head fs_supers;

    struct lock_class_key s_lock_key;
    struct lock_class_key s_umount_key;
    struct lock_class_key s_vfs_rename_key;
    struct lock_class_key s_writers_key[SB_FREEZE_LEVELS];

    struct lock_class_key i_lock_key;
    struct lock_class_key i_mutex_key;
    struct lock_class_key invalidate_lock_key;
    struct lock_class_key i_mutex_dir_key;
};
```

Linux内文件系统需要设置`file_system_type`信息，然后将设置好的信息提交给`register_filesystem`函数进行注册，只有完成注册的文件系统才能被VFS操控。

```
extern int register_filesystem(struct file_system_type *);
```

`file_system_type`本身定义是非常简单的，主要就是定义获取和删除`super_block`的接口及属性信息，不同文件系统间的`file_system_type`之间通过链接进行管理。

话又说回来，`super_block`是个什么东西呢？

`super_block`是一个更加复杂的结构体，它定义了文件系统的具体信息和对应文件系统的操作接口，是实际管理文件系统的数据结构。

```
struct super_block {
    struct list_head	s_list;		/* Keep this first */
    dev_t			s_dev;		/* search index; _not_ kdev_t */
    unsigned char		s_blocksize_bits;
    unsigned long		s_blocksize;
    loff_t			s_maxbytes;	/* Max file size */
    struct file_system_type	*s_type;
    const struct super_operations	*s_op;
    const struct dquot_operations	*dq_op;
    const struct quotactl_ops	*s_qcop;
    const struct export_operations *s_export_op;
    unsigned long		s_flags;
    unsigned long		s_iflags;	/* internal SB_I_* flags */
    unsigned long		s_magic;
    struct dentry		*s_root;
    struct rw_semaphore	s_umount;
    int			s_count;
    atomic_t		s_active;
    ......
    spinlock_t		s_inode_wblist_lock;
    struct list_head	s_inodes_wb;	/* writeback inodes */
} __randomize_layout;
```

下面展示了`proc`文件系统是如何进行注册的。

```
static struct file_system_type proc_fs_type = {
    .name			= "proc",
    .init_fs_context	= proc_init_fs_context,
    .parameters		= proc_fs_parameters,
    .kill_sb		= proc_kill_sb,
    .fs_flags		= FS_USERNS_MOUNT | FS_DISALLOW_NOTIFY_PERM,
};

void __init proc_root_init(void)
{
    ......
    register_filesystem(&proc_fs_type);
}
```

`proc`是进程文件系统，属于Linux中伪文件系统的一种，它没有对应真实的磁盘或硬盘，而是提供给用户空间便利的使用Linux系统资源的接口。常见的伪文件系统有`proc`、`sys`、`dev`等等。通过`proc`可以方便的查看进程信息，比如进程的内存布局、CPU信息等等。

```
ls /proc/1/
attr       clear_refs       cpuset   fd       limits     mem         net        oom_score      personality  schedstat  smaps_rollup  status   timerslack_ns
autogroup  cmdline          cwd      fdinfo   loginuid   mountinfo   ns         oom_score_adj  projid_map   sessionid  stack         syscall  uid_map
auxv       comm             environ  gid_map  map_files  mounts      numa_maps  pagemap        root         setgroups  stat          task     wchan
cgroup     coredump_filter  exe      io       maps       mountstats  oom_adj    patch_state    sched        smaps      statm         timers
```

##

## 1.2 proc

进行Linux驱动开发时，可以借助`proc_ops`结构体、`proc_create`接口、`proc_remove`接口对`proc`进行创建和控制。

`proc_ops`结构体中有两个较为重要的成员，即`proc_read`和`proc_write`，它们分别会响应虚文件被用户空间读写时的操作。下面给出了创建`proc`虚文件的示例代码。

```
#include <linux/proc_fs.h>

static struct proc_dir_entry* lde_proc_entry = NULL;

static ssize_t lde_proc_read(struct file* file, char __user* ubuf, size_t count, loff_t* data)
{
    printk(KERN_INFO "%s called file 0x%px, buffer 0x%px count 0x%lx off 0x%llx\n",
        __func__, file, ubuf, count, *data);

    return 0;
}

static ssize_t lde_proc_write(struct file* file, const char __user* ubuf, size_t count, loff_t* data)
{
    printk(KERN_INFO "%s called legnth 0x%lx, 0x%px\n",
        __func__, count, ubuf);

    return count;
}

static struct proc_ops lde_proc_ops = {
    .proc_read = lde_proc_read,
    .proc_write = lde_proc_write
};

int lde_proc_create(void)
{
    int ret;

    ret = SUCCEED;

    lde_proc_entry = proc_create("lde_proc", 0, NULL, &lde_proc_ops);
    if (!lde_proc_entry) {
        printk(KERN_ERR "%s create proc entry failed\n", __func__);

        ret = PROC_CREATE_FAILED;
    }

    return ret;
}

void lde_proc_remove(void)
{
    if (lde_proc_entry == NULL) {
        printk(KERN_INFO "%s proc not exists\n", __func__);
        goto TAG_RETURN;
    }

    proc_remove(lde_proc_entry);

TAG_RETURN:
    return;
}
```

通过读写虚文件，可以在`dmesg`中看到相关的打印信息。

```
cat /proc/lde_proc
echo test | sudo tee -a /proc/lde_proc

[  440.396298] starting from 0xffffffffc0af6090 ...
[  446.024481] lde_proc_read called file 0xffff9626c2931400, buffer 0x000077aeb6db8000 count 0x40000 off 0x0
[  459.392387] lde_proc_write called legnth 0x5, 0x00007fff783f3090
[  476.345011] exiting from 0xffffffffc0af60f0 ...
```

##

## 1.3 randomize\_va\_space变量的设置

`proc`除了支持访问进程信息外，它还支持在Linux内核运行时对内核参数进行修改，该机制也被称作`sysctl`。

`/proc/sys/kernel/`中的虚文件会通过`kern_table`进行定义，每个模块都会定义一个处理函数和数据对象，处理函数会负责处理虚文件被读写时进行的操作，而数据对象则是被操作的数值。`randomize_va_space`指定的处理函数是`proc_dointvec`，其作用是读取整数值或写入整数值，待处理的数据对象是`randomize_va_space`，它是一个整型的全局变量。

当向`/proc/sys/kernel/randomize_va_space`写入数值时，`randomize_va_space`变量的数值就会被`proc_dointvec`函数更改。

```
static struct ctl_table kern_table[] = {
......
#if defined(CONFIG_MMU)
    {
        .procname	= "randomize_va_space",
        .data		= &randomize_va_space,
        .maxlen		= sizeof(int),
        .mode		= 0644,
        .proc_handler	= proc_dointvec,
    },
#endif
......
}
```

##

## 1.4 内存布局的随机化设置

当程序启动时，负责加载ELF文件的`load_elf_binary`函数会根据`randomize_va_space`变量设置标志位，当标志位完成设置后，才会正式开始BRK、MMAP、堆、栈、动态链接库、vDSO的地址随机化，随机化的主要操作就是根据随机值对地址进行偏移。

static int load\_elf\_binary(struct linux\_binprm \*bprm)
{
......
if (!(current->personality & ADDR\_NO\_RANDOMIZE) && randomize\_va\_space)
current->flags |= PF\_RANDOMIZE;

```
setup_new_exec(bprm);

/* Do this so that we can load the interpreter, if need be.  We will
   change some of these later */
retval = setup_arg_pages(bprm, randomize_stack_top(STACK_TOP),
             executable_stack);
......
mm = current->mm;
mm->end_code = end_code;
mm->start_code = start_code;
mm->start_data = start_data;
mm->end_data = end_data;
mm->start_stack = bprm->p;

......

if (!first_pt_load) {
        elf_flags |= MAP_FIXED;
    } else if (elf_ex->e_type == ET_EXEC) {
        elf_flags |= MAP_FIXED_NOREPLACE;
    } else if (elf_ex->e_type == ET_DYN) {
        if (interpreter) {
            load_bias = ELF_ET_DYN_BASE;
            if (current->flags & PF_RANDOMIZE)
                load_bias += arch_mmap_rnd();
            alignment = maximum_ali...