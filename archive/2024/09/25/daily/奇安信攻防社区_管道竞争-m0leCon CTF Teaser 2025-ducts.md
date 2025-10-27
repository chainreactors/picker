---
title: 管道竞争-m0leCon CTF Teaser 2025-ducts
url: https://forum.butian.net/share/3818
source: 奇安信攻防社区
date: 2024-09-25
fetch_date: 2025-10-06T18:21:33.131275
---

# 管道竞争-m0leCon CTF Teaser 2025-ducts

#

[问答](https://forum.butian.net/questions)

*发起*

* [提问](https://forum.butian.net/question/create)
* [文章](https://forum.butian.net/share/create)

[攻防](https://forum.butian.net/community)
[活动](https://forum.butian.net/movable)

Toggle navigation

* [首页 (current)](https://forum.butian.net)
* [问答](https://forum.butian.net/questions)
* [商城](https://forum.butian.net/shop)
* [实战攻防技术](https://forum.butian.net/community)
* [漏洞分析与复现](https://forum.butian.net/articles)
  NEW
* [活动](https://forum.butian.net/movable)
* [摸鱼办](https://forum.butian.net/questions/Play)

搜索

* [登录](https://forum.butian.net/login)
* [注册](https://user.skyeye.qianxin.com/user/register?next=http://forum.butian.net/btlogin)

### 管道竞争-m0leCon CTF Teaser 2025-ducts

* [CTF](https://forum.butian.net/topic/52)

头次见到在用户态中的管道竞争，很好，学之

@\[toc\]
参考
==
[pipe(7) — Linux manual page](https://man7.org/linux/man-pages/man7/pipe.7.html)
[Ducts challenge write-up](https://matteoschiff.com/ducts-writeup/)
[管道读写规则和Pipe Capacity、PIPE\\_BUF](https://www.cnblogs.com/alantu2018/p/8477339.html)
[linux的阻塞和等待队列机制](https://www.cnblogs.com/gdk-0078/p/5172941.html)
头次见到在用户态中的管道竞争，很好，学之
> 衷心感谢tpus师傅和stc4k师傅的帮助
pipe
====
### 概述
`pipe(7)` 是 Linux 系统中关于管道（pipes）和命名管道（FIFOs）的概述手册页。管道提供了一种单向的进程间通信（IPC）通道，具有读端和写端。数据从写端写入，可以从读端读出。
### 创建管道
#### 无名管道（Anonymous Pipes）
- \*\*创建\*\*：
- 使用 `pipe(2)` 系统调用创建。
- 调用 `pipe(2)` 会创建一个新的管道，并返回两个文件描述符：一个用于读端（通常为 `pipefd[0]`），一个用于写端（通常为 `pipefd[1]`）。
- 无名管道通常用于父子进程之间的通信。
- \*\*示例\*\*：
```c
#include <unistd.h>
#include <stdio.h>
int main() {
int pipefd[2];
char buf[100] = "Hello, pipe!";
if (pipe(pipefd) == -1) {
perror("pipe");
return 1;
}
// 写入数据
write(pipefd[1], buf, sizeof(buf));
// 读取数据
char read\_buf[100];
ssize\_t n = read(pipefd[0], read\_buf, sizeof(read\_buf));
if (n == -1) {
perror("read");
return 1;
}
read\_buf[n] = '\0';
printf("Read: %s\n", read\_buf);
// 关闭文件描述符
close(pipefd[0]);
close(pipefd[1]);
return 0;
}
```
#### 命名管道（FIFOs）
- \*\*创建\*\*：
- 具有文件系统中的名称，使用 `mkfifo(3)` 函数创建。
- 调用 `mkfifo(3)` 时需要指定路径和权限模式。
- 使用 `open(2)` 系统调用打开，可以指定 `O\_RDONLY` 或 `O\_WRONLY` 标志。
- 任何进程都可以打开 FIFO，只要文件权限允许。
- \*\*示例\*\*：
```c
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
int main() {
const char \*fifo\_path = "/tmp/myfifo";
// 创建 FIFO
if (mkfifo(fifo\_path, 0666) == -1) {
perror("mkfifo");
return 1;
}
// 打开 FIFO 用于写入
int fd = open(fifo\_path, O\_WRONLY);
if (fd == -1) {
perror("open");
return 1;
}
// 写入数据
const char \*msg = "Hello, FIFO!";
write(fd, msg, strlen(msg));
// 关闭文件描述符
close(fd);
// 删除 FIFO
unlink(fifo\_path);
return 0;
}
```
### I/O 操作
- \*\*读写操作\*\*：
- \*\*读操作\*\*：
- 如果尝试从空管道读取，`read(2)` 会阻塞，直到有数据可读。
- 如果所有写端都被关闭，`read(2)` 会返回 0，表示文件结束。
- \*\*写操作\*\*：
- 如果尝试向已满管道写入，`write(2)` 会阻塞，直到有足够的空间。
- 如果所有读端都被关闭，`write(2)` 会生成 `SIGPIPE` 信号，并返回 -1，设置 `errno` 为 `EPIPE`。
- \*\*非阻塞 I/O\*\*：
- 可以通过 `fcntl(2)` 的 `F\_SETFL` 操作启用 `O\_NONBLOCK` 标志来实现非阻塞 I/O。
- 对于 FIFO，如果任何进程已经打开写端，读操作会返回 `EAGAIN`；否则，如果没有潜在的写进程，读操作会成功并返回空。
- \*\*原子性\*\*：
- 写入小于或等于 `PIPE\_BUF` 字节的数据是原子的，即数据作为一个连续的序列写入管道。
- 写入大于 `PIPE\_BUF` 字节的数据可能是非原子的，内核可能会将数据分成多个部分写入管道，这些部分之间可能会被其他进程的写操作插入数据。
- POSIX.1 要求 `PIPE\_BUF` 至少为 512 字节，Linux 中通常是 4096 字节。
### 配置选项
- \*\*/proc 文件系统\*\*：
- `/proc/sys/fs/pipe-max-size`：设置管道的最大容量（以字节为单位）。
- `/proc/sys/fs/pipe-user-pages-hard`：设置单个非特权用户可以分配给管道缓冲区的总页面数的硬限制。
- `/proc/sys/fs/pipe-user-pages-soft`：设置单个非特权用户可以分配给管道缓冲区的总页面数的软限制。
### 相关函数和系统调用
- \*\*创建和管理\*\*：
- `pipe(2)`：创建无名管道。
- `mkfifo(3)`：创建命名管道。
- `open(2)`：打开命名管道。
- `fcntl(2)`：管理文件描述符的属性。
- `dup(2)`：复制文件描述符。
- `close(2)`：关闭文件描述符。
- \*\*I/O 操作\*\*：
- `read(2)`：从管道读取数据。
- `write(2)`：向管道写入数据。
- `poll(2)` 和 `select(2)`：监控多个文件描述符的状态。
- `splice(2)` 和 `tee(2)`：高效地传输数据。
- `vmsplice(2)`：将用户空间内存区域的内容写入管道。
- \*\*其他\*\*：
- `stat(2)`：获取文件状态。
- `unlink(2)`：删除文件。
- `epoll(7)`：高效的 I/O 多路复用机制。
- `fifo(7)`：命名管道的详细信息。
### 通信语义
- \*\*字节流\*\*：
- 管道提供的通信通道是一个字节流，没有消息边界的概念。
- 数据按顺序写入和读取，但没有明确的消息分隔符。
### 示例代码
#### 无名管道示例
```c
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
int main() {
int pipefd[2];
pid\_t cpid;
char buf[100];
if (pipe(pipefd) == -1) {
perror("pipe");
exit(EXIT\_FAILURE);
}
cpid = fork();
if (cpid == -1) {
perror("fork");
exit(EXIT\_FAILURE);
}
if (cpid == 0) { // 子进程
close(pipefd[1]); // 关闭写端
ssize\_t n = read(pipefd[0], buf, sizeof(buf));
if (n == -1) {
perror("read");
exit(EXIT\_FAILURE);
}
buf[n] = '\0';
printf("Child: received '%s'\n", buf);
close(pipefd[0]);
exit(EXIT\_SUCCESS);
} else { // 父进程
close(pipefd[0]); // 关闭读端
const char \*msg = "Hello, child!";
write(pipefd[1], msg, strlen(msg));
close(pipefd[1]);
wait(NULL); // 等待子进程结束
exit(EXIT\_SUCCESS);
}
}
```
#### 命名管道示例
```c
#include <sys/types.h>
#include <sys/stat.h>
#include <fcntl.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
int main() {
const char \*fifo\_path = "/tmp/myfifo";
// 创建 FIFO
if (mkfifo(fifo\_path, 0666) == -1) {
perror("mkfifo");
exit(EXIT\_FAILURE);
}
// 父进程写入数据
int fd = open(fifo\_path, O\_WRONLY);
if (fd == -1) {
perror("open");
exit(EXIT\_FAILURE);
}
const char \*msg = "Hello, FIFO!";
write(fd, msg, strlen(msg));
close(fd);
// 子进程读取数据
pid\_t cpid = fork();
if (cpid == -1) {
perror("fork");
exit(EXIT\_FAILURE);
}
if (cpid == 0) { // 子进程
fd = open(fifo\_path, O\_RDONLY);
if (fd == -1) {
perror("open");
exit(EXIT\_FAILURE);
}
char buf[100];
ssize\_t n = read(fd, buf, sizeof(buf));
if (n == -1) {
perror("read");
exit(EXIT\_FAILURE);
}
buf[n] = '\0';
printf("Child: received '%s'\n", buf);
close(fd);
exit(EXIT\_SUCCESS);
} else { // 父进程
wait(NULL); // 等待子进程结束
unlink(fifo\_path); // 删除 FIFO
exit(EXIT\_SUCCESS);
}
}
```
### 参考资料
- `fcntl(2)`
- `intro(2)`
- `open(2)`
- `pipe(2)`
- `splice(2)`
- `tee(2)`
- `vmsplice(2)`
- `write(2)`
- `proc\_sys\_fs(5)`
- `fifo(7)`
- `signal(7)`
竞争点
===
[任意只读文件漏洞分析](https://xie.infoq.cn/article/c2bdf20841b48d407b1485c9a)
在于pipe\\_write
大概是第一个进程写完管道后然后放锁后其他进程都开始依次写，但都和第一个进程一样都阻塞到wait\\_event\\_interruptible\\_exclusive了，然后才轮到读进程开始读，读完后各个进程的wait\\_event\\_interruptible\\_exclusive都退出了，然后开始上锁再写。
那谁先能写就看哪个从wait\\_event\\_interruptible\\_exclusive退出到上锁快了
下面详细讲讲
互斥锁
---
当然，下面是关于 `mutex\_init`、`mutex\_lock` 和 `mutex\_unlock` 的详细解释，包括它们的工作原理和内部机制。
### 1. `mutex\_init`
#### 定义
```c
#define mutex\_init(mutex) \
do { \
static struct lock\_class\_key \_\_key; \
\
\_\_mutex\_init((mutex), #mutex, &\_\_key); \
} while (0)
```
#### 作用
`mutex\_init` 用于初始化一个互斥锁（mutex）。它确保互斥锁处于未锁定状态，并且准备好被使用。
#### 实现
```c
void \_\_mutex\_init(struct mutex \*lock, const char \*name, struct lock\_class\_key \*key)
{
atomic\_set(&lock->count, 1); // 将计数器设置为1，表示未锁定
spin\_lock\_init(&lock->wait\_lock); // 初始化自旋锁，用于保护等待队列
INIT\_LIST\_HEAD(&lock->wait\_list); // 初始化等待队列
mutex\_clear\_owner(lock); // 清除所有者信息
#ifdef CONFIG\_MUTEX\_SPIN\_ON\_OWNER
lock->spin\_mlock = NULL; // 初始化自旋锁指针（如果启用了相关配置）
#endif
debug\_mutex\_init(lock, name, key); // 调试信息初始化
}
```
#### 原理
- \*\*计数器初始化\*\*：`atomic\_set(&lock->count, 1)` 将互斥锁的计数器设置为1，表示互斥锁未被锁定。
- \*\*自旋锁初始化\*\*：`spin\_lock\_init(&lock->wait\_lock)` 初始化一个自旋锁，用于保护等待队列。
- \*\*等待队列初始化\*\*：`INIT\_LIST\_HEAD(&lock->wait\_list)` 初始化一个链表头，用于管理等待获取互斥锁的任务。
- \*\*清除所有者信息\*\*：`mutex\_clear\_owner(lock)` 清除互斥锁的所有者信息。
- \*\*调试信息初始化\*\*：`debug\_mutex\_init(lock, name, key)` 用于调试目的，记录互斥锁的名称和类键。
### 2. `mutex\_lock`
#### 定义
```c
void \_\_sched mutex\_lock(struct mutex \*lock)
{
might\_sleep(); // 提示编译器该函数可能会睡眠
/\*
\* The locking fastpath is the 1->0 transition from
\* 'unlocked' into 'locked' state.
\*/
\_\_mutex\_fastpath\_lock(&lock->count, \_\_mutex\_lock\_slowpath);
mutex\_set\_owner(lock);
}
```
#### 作用
`mutex\_lock` 用于获取一个互斥锁。如果互斥锁已经被其他任务持有，当前任务将进入睡眠状态，直到互斥锁可用。
#### 实现
- \*\*提示可能睡眠\*\*：`might\_sleep()` 提示编译器该函数可能会睡眠，确保调用者不会在禁止睡眠的上下文中调用该函数。
- \*\*快速路径\*\*：`\_\_mutex\_fastpath\_lock(&lock->count, \_\_mutex\_lock\_slowpath)` 尝试快速获取互斥锁。如果互斥锁未被锁定，则直接将计数器从1减到0，表示已锁定。如果互斥锁已被锁定，则调用慢速路径 `\_\_mutex\_lock\_slowpath`。
- \*\*设置所有者\*\*：`mutex\_set\_owner(lock)` 设置互斥锁的所有者为当前任务。
#### 原理
- \*\*快速路径\*\*：尝试原子地将计数器从1减到0。如果成功，表示互斥锁已被当前任务获取。
- \*\*慢速路径\*\*：如果快速路径失败（即互斥锁已被其他任务持有），调用慢速路径 `\_\_mutex\_l...