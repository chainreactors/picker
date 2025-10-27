---
title: linux kernel 结构体利用 — tty,seq
url: https://mp.weixin.qq.com/s?__biz=MzUzMDUxNTE1Mw==&mid=2247497382&idx=1&sn=3af9f1d3e1410968f4e79f8c7d4cb7af&chksm=fa522318cd25aa0eb27a7479db7ec889df08778b302a41279fd355e15546fada4813fefcb96c&scene=58&subscene=0#rd
source: 山石网科安全技术研究院
date: 2022-11-08
fetch_date: 2025-10-03T21:58:35.535744
---

# linux kernel 结构体利用 — tty,seq

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/Gw8FuwXLJnTounJPKmdQOVKAwavLpbagfCAN5icxiblOgDu8ibXEnSLyaUJn33gQbezwiahiccAvChicu5xTWvra0LyQ/0?wx_fmt=jpeg)

# linux kernel 结构体利用 — tty,seq

原创

工控安全实验室

山石网科安全技术研究院

![](https://mmbiz.qpic.cn/mmbiz_gif/Gw8FuwXLJnTounJPKmdQOVKAwavLpbagTibrq9FubyjJ8lEmJspUyxAvTyfVumJ58XvATFmq35aiadggfTXLUg9Q/640?wx_fmt=gif)

**背景知识**

**堆喷射**

![](https://mmbiz.qpic.cn/mmbiz_gif/Gw8FuwXLJnTounJPKmdQOVKAwavLpbagTibrq9FubyjJ8lEmJspUyxAvTyfVumJ58XvATFmq35aiadggfTXLUg9Q/640?wx_fmt=gif)

堆喷是啥？

堆喷射（Heap Spraying），通过大量重复的操作，申请多个相同的堆块或者构造大量指针从而提高碰撞到该堆块或利用到该指针的概率。

具体可以是存在一个 uaf 保存了一个已经 free 掉的指针，通过申请大量相同的结构体，从而提高该指针命中结构体的概率。

**tty设备结构体**

![](https://mmbiz.qpic.cn/mmbiz_gif/Gw8FuwXLJnTounJPKmdQOVKAwavLpbagTibrq9FubyjJ8lEmJspUyxAvTyfVumJ58XvATFmq35aiadggfTXLUg9Q/640?wx_fmt=gif)

当我们打开 tty 设备时内核中便会创建一个 tty\_struct，也就是说，打开 `/dev/ptmx` 会在内核中分配一个 tty\_struct 结构体，相应地当我们将其关闭时该结构体便会被释放回 slab/slub 中

tty\_struct  结构体定义如下

```
struct tty_struct {
    int    magic;
    struct kref kref;
    struct device *dev;    /* class device or NULL (e.g. ptys, serdev) */
    struct tty_driver *driver;
    const struct tty_operations *ops;
    int index;

    /* Protects ldisc changes: Lock tty not pty */
    struct ld_semaphore ldisc_sem;
    struct tty_ldisc *ldisc;

    struct mutex atomic_write_lock;
    struct mutex legacy_mutex;
    struct mutex throttle_mutex;
    struct rw_semaphore termios_rwsem;
    struct mutex winsize_mutex;
    /* Termios values are protected by the termios rwsem */
    struct ktermios termios, termios_locked;
    char name[64];
    unsigned long flags;
    int count;
    struct winsize winsize;        /* winsize_mutex */

    struct {
        spinlock_t lock;
        bool stopped;
        bool tco_stopped;
        unsigned long unused[0];
    } __aligned(sizeof(unsigned long)) flow;

    struct {
        spinlock_t lock;
        struct pid *pgrp;
        struct pid *session;
        unsigned char pktstatus;
        bool packet;
        unsigned long unused[0];
    } __aligned(sizeof(unsigned long)) ctrl;

    int hw_stopped;
    unsigned int receive_room;    /* Bytes free for queue */
    int flow_change;

    struct tty_struct *link;
    struct fasync_struct *fasync;
    wait_queue_head_t write_wait;
    wait_queue_head_t read_wait;
    struct work_struct hangup_work;
    void *disc_data;
    void *driver_data;
    spinlock_t files_lock;        /* protects tty_files list */
    struct list_head tty_files;

#define N_TTY_BUF_SIZE 4096

    int closing;
    unsigned char *write_buf;
    int write_cnt;
    /* If the tty has a pending do_SAK, queue it here - akpm */
    struct work_struct SAK_work;
    struct tty_port *port;
} __randomize_layout;

/* Each of a tty's open files has private_data pointing to tty_file_private */
struct tty_file_private {
    struct tty_struct *tty;
    struct file *file;
    struct list_head list;
};

/* tty magic number */
#define TTY_MAGIC        0x5401
```

其中定义了结构体 魔数 TTY\_MAGIC 0x5401，可以通过这个魔数判断该堆块是否是tty结构体，另外结构体中有一个函数表 \*tty\_operations\* ，tty\_op 为一个内核地址，可以通过它来泄露内核地址，我们在使用 read ioctl等操作的时候，也会通过 tty\_op 里保存的函数来实现对应的功能

tty\_operations 结构体定义如下

```
struct tty_operations {
    struct tty_struct * (*lookup)(struct tty_driver *driver,
            struct file *filp, int idx);
    int  (*install)(struct tty_driver *driver, struct tty_struct *tty);
    void (*remove)(struct tty_driver *driver, struct tty_struct *tty);
    int  (*open)(struct tty_struct * tty, struct file * filp);
    void (*close)(struct tty_struct * tty, struct file * filp);
    void (*shutdown)(struct tty_struct *tty);
    void (*cleanup)(struct tty_struct *tty);
    int  (*write)(struct tty_struct * tty,
              const unsigned char *buf, int count);
    int  (*put_char)(struct tty_struct *tty, unsigned char ch);
    void (*flush_chars)(struct tty_struct *tty);
    unsigned int (*write_room)(struct tty_struct *tty);
    unsigned int (*chars_in_buffer)(struct tty_struct *tty);
    int  (*ioctl)(struct tty_struct *tty,
            unsigned int cmd, unsigned long arg);
    long (*compat_ioctl)(struct tty_struct *tty,
                 unsigned int cmd, unsigned long arg);
    void (*set_termios)(struct tty_struct *tty, struct ktermios * old);
    void (*throttle)(struct tty_struct * tty);
    void (*unthrottle)(struct tty_struct * tty);
    void (*stop)(struct tty_struct *tty);
    void (*start)(struct tty_struct *tty);
    void (*hangup)(struct tty_struct *tty);
    int (*break_ctl)(struct tty_struct *tty, int state);
    void (*flush_buffer)(struct tty_struct *tty);
    void (*set_ldisc)(struct tty_struct *tty);
    void (*wait_until_sent)(struct tty_struct *tty, int timeout);
    void (*send_xchar)(struct tty_struct *tty, char ch);
    int (*tiocmget)(struct tty_struct *tty);
    int (*tiocmset)(struct tty_struct *tty,
            unsigned int set, unsigned int clear);
    int (*resize)(struct tty_struct *tty, struct winsize *ws);
    int (*get_icount)(struct tty_struct *tty,
                struct serial_icounter_struct *icount);
    int  (*get_serial)(struct tty_struct *tty, struct serial_struct *p);
    int  (*set_serial)(struct tty_struct *tty, struct serial_struct *p);
    void (*show_fdinfo)(struct tty_struct *tty, struct seq_file *m);
#ifdef CONFIG_CONSOLE_POLL
    int (*poll_init)(struct tty_driver *driver, int line, char *options);
    int (*poll_get_char)(struct tty_driver *driver, int line);
    void (*poll_put_char)(struct tty_driver *driver, int line, char ch);
#endif
    int (*proc_show)(struct seq_file *, void *);
} __randomize_layout;
```

在使用 write 时，rdi寄存器的值为其结构体本身，因此可以通过使用 gadget 进行栈迁移

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTounJPKmdQOVKAwavLpbagUQyh5xGzfC2cLZu6dfbAkfWsSQfeDhvX0us7fOmickEpIRx3qxP2OAg/640?wx_fmt=png)

调用 ioctl 时 ，rdi寄存器为结构体本身，  rcx 寄存器为 tty\_operations

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTounJPKmdQOVKAwavLpbag4RxUg8iblWZwYqzg8vQpOu6SIGaJlwEPsRpMLe2hNZlAkEXXwYrejFA/640?wx_fmt=png)

**seq序列文件借口**

![](https://mmbiz.qpic.cn/mmbiz_gif/Gw8FuwXLJnTounJPKmdQOVKAwavLpbagTibrq9FubyjJ8lEmJspUyxAvTyfVumJ58XvATFmq35aiadggfTXLUg9Q/640?wx_fmt=gif)

序列文件接口（Sequence File Interface）是针对 procfs 默认操作函数每次只能读取一页数据从而难以处理较大 proc 文件的情况下出现的，其为内核编程提供了更为友好的接口。

```
struct seq_file {
    char *buf;
    size_t size;
    size_t from;
    size_t count;
    size_t pad_until;
    loff_t index;
    loff_t read_pos;
    struct mutex lock;
    const struct seq_operations *op;
    int poll_event;
    const struct file *file;
    void *private;
};
```

其中 seq\_operations 结构体动态分配，该结构体只有4个函数指针，大小仅为 0x20 ，其中在 read 时会通过调用链来调用 start 指针

```
struct seq_operations {
    void * (*start) (struct seq_file *m, loff_t *pos);
    void (*stop) (struct seq_file *m, void *v);
    void * (*next) (struct seq_file *m, void *v, loff_t *pos);
    int (*show) (struct seq_file *m, void *v);
};
```

![](https://mmbiz.qpic.cn/mmbiz_gif/Gw8FuwXLJnTounJPKmdQOVKAwavLpbagTibrq9FubyjJ8lEmJspUyxAvTyfVumJ58XvATFmq35aiadggfTXLUg9Q/640?wx_fmt=gif)

**题目讲解**

**qwb2021notebook**

**漏洞分析**

启动脚本如下

```
#!/bin/sh
stty intr ^]
exec timeout 300 qemu-system-x86_64 -m 64M -kernel bzImage -initrd rootfs.cpio -append "loglevel=3 console=ttyS0 oops=panic panic=1 kaslr" -nographic -net user -net nic -device e1000 -smp cores=2,threads=2 -cpu kvm64,+smep,+smap -monitor /dev/null 2>/dev/null -s
```

保护全开，并且是多核，内核版本 4.15.8 ，因此可以使用 userfaultfd

模块为经典菜单

ioctl程序如下，其中gift可以白给出堆地址，程序很多地方用了锁，但是很多锁没啥意义。

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTounJPKmdQOVKAwavLpbagKxOdZvuiaicYeHWAic00vBAibE9E7sBhkW8kfltHic4n1tSGN1v68dYVsKw/640?wx_fmt=png)

edit如下

![](https://mmbiz.qpic.cn/mmbiz_png/Gw8FuwXLJnTounJPKmdQOVKAwavLpbag8AWm1OOQYicexDZl7o821pfQ4Yib2h2kKWxpOB07LVYiaBKicAvKLuWDrQ/640?wx_fmt=png)

使用了 realloc，其 realloc 和用户态的类似，size 为 0 时可以释放堆块，我们可以看到，程序中有很多地方都有 copy\_from\_user(name, v4, 0x100LL); 这其实是方便我们使用 userfaultfd 机制的，因此程序可以卡在刚 free 后的地方，而后续如果没有继续运行下去就会造成一个 uaf

add 同样也用了读锁，各个读锁，因此 edit 卡着的过程中 是可以使用 add 的

而 read write 都没有用到锁。

**漏洞利用**

1. 使用 userfaultfd...