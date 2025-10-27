---
title: 野蛮fuzz：快照与代码覆盖率
url: https://mp.weixin.qq.com/s?__biz=MjM5NTc2MDYxMw==&mid=2458580271&idx=1&sn=a0a61704458f4a11ae3f9b0e560517a2&chksm=b18dc5a586fa4cb3fc19cc6c41d986e6c51038d53203bd890ef3f0f810f27c2a87552ee235ff&scene=58&subscene=0#rd
source: 看雪学苑
date: 2024-11-06
fetch_date: 2025-10-06T19:18:32.104276
---

# 野蛮fuzz：快照与代码覆盖率

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/1UG7KPNHN8HagHlk4zibwq7tOTETbicdgjGo28l6cDxDsvuKUxjaZFxx5robwwBEnfZRwvMW1brbQxJ1nt5J4ia8Q/0?wx_fmt=jpeg)

# 野蛮fuzz：快照与代码覆盖率

pureGavin【译】

看雪学苑

##

```
一

介绍
```

上次我们写博客时，我们有一个简单的模糊测试器，它会测试一个故意有漏洞的程序，该程序会对文件进行一些检查，如果输入文件通过了检查，它会继续进行下一个检查，如果输入通过了所有检查，程序就会发生段错误。我们发现了代码覆盖的重要性，以及它如何帮助将模糊测试过程中指数级罕见的事件减少为线性罕见的事件。让我们直接进入如何改进我们的简单模糊测试器！

特别感谢@gamozolabs的所有内容，让我对这个话题产生了兴趣。

##

```
二

性能
```

首先，我们的简单模糊测试器非常慢。如果你还记得，我们的简单模糊测试器平均每秒大约进行1,500次模糊测试。在我的测试中，AFL在QEMU模式下（模拟没有可用的源代码进行编译插桩）每秒大约进行1,000次模糊测试。这是有道理的，因为AFL做的事情远比我们的简单模糊测试器多，尤其是在QEMU模式下，我们在模拟CPU并提供代码覆盖。

我们的目标二进制文件（*https://gist.github.com/h0mbre/db209b70eb614aa811ce3b98ad38262d*）会执行以下操作：

* 从磁盘上的文件中提取字节到缓冲区；
* 对缓冲区执行3次检查，查看检查的索引是否与硬编码值匹配；
* 如果通过所有检查则发生段错误，如果有一个检查失败则退出。

我们的简单模糊测试器会执行以下操作：

* 从磁盘上的有效jpeg文件中提取字节到字节缓冲区；
* 通过随机字节覆盖变异缓冲区中2%的字节；
* 将变异后的文件写入磁盘；
* 通过在每次模糊测试迭代中执行`fork()`和`execvp()`将变异后的文件传递给目标二进制文件。

如你所见，这涉及大量的文件系统交互和系统调用。让我们在我们的漏洞二进制文件上使用`strace`，看看二进制文件发出了哪些系统调用（为了便于测试，在这篇文章中，我已经将`.jpeg`文件硬编码到漏洞二进制文件中，这样我们就不必使用命令行参数）：

```
execve("/usr/bin/vuln", ["vuln"], 0x7ffe284810a0 /* 52 vars */) = 0
brk(NULL)                               = 0x55664f046000
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
access("/etc/ld.so.preload", R_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/etc/ld.so.cache", O_RDONLY|O_CLOEXEC) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=88784, ...}) = 0
mmap(NULL, 88784, PROT_READ, MAP_PRIVATE, 3, 0) = 0x7f0793d2e000
close(3)                                = 0
access("/etc/ld.so.nohwcap", F_OK)      = -1 ENOENT (No such file or directory)
openat(AT_FDCWD, "/lib/x86_64-linux-gnu/libc.so.6", O_RDONLY|O_CLOEXEC) = 3
read(3, "\177ELF\2\1\1\3\0\0\0\0\0\0\0\0\3\0>\0\1\0\0\0\260\34\2\0\0\0\0\0"..., 832) = 832
fstat(3, {st_mode=S_IFREG|0755, st_size=2030544, ...}) = 0
mmap(NULL, 8192, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7f0793d2c000
mmap(NULL, 4131552, PROT_READ|PROT_EXEC, MAP_PRIVATE|MAP_DENYWRITE, 3, 0) = 0x7f079372c000
mprotect(0x7f0793913000, 2097152, PROT_NONE) = 0
mmap(0x7f0793b13000, 24576, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_DENYWRITE, 3, 0x1e7000) = 0x7f0793b13000
mmap(0x7f0793b19000, 15072, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_FIXED|MAP_ANONYMOUS, -1, 0) = 0x7f0793b19000
close(3)                                = 0
arch_prctl(ARCH_SET_FS, 0x7f0793d2d500) = 0
mprotect(0x7f0793b13000, 16384, PROT_READ) = 0
mprotect(0x55664dd97000, 4096, PROT_READ) = 0
mprotect(0x7f0793d44000, 4096, PROT_READ) = 0
munmap(0x7f0793d2e000, 88784)           = 0
fstat(1, {st_mode=S_IFCHR|0620, st_rdev=makedev(136, 0), ...}) = 0
brk(NULL)                               = 0x55664f046000
brk(0x55664f067000)                     = 0x55664f067000
write(1, "[>] Analyzing file: Canon_40D.jp"..., 35[>] Analyzing file: Canon_40D.jpg.
) = 35
openat(AT_FDCWD, "Canon_40D.jpg", O_RDONLY) = 3
fstat(3, {st_mode=S_IFREG|0644, st_size=7958, ...}) = 0
fstat(3, {st_mode=S_IFREG|0644, st_size=7958, ...}) = 0
lseek(3, 4096, SEEK_SET)                = 4096
read(3, "\v\260\v\310\v\341\v\371\f\22\f*\fC\f\\\fu\f\216\f\247\f\300\f\331\f\363\r\r\r&"..., 3862) = 3862
lseek(3, 0, SEEK_SET)                   = 0
write(1, "[>] Canon_40D.jpg is 7958 bytes."..., 33[>] Canon_40D.jpg is 7958 bytes.
) = 33
read(3, "\377\330\377\340\0\20JFIF\0\1\1\1\0H\0H\0\0\377\341\t\254Exif\0\0II"..., 4096) = 4096
read(3, "\v\260\v\310\v\341\v\371\f\22\f*\fC\f\\\fu\f\216\f\247\f\300\f\331\f\363\r\r\r&"..., 4096) = 3862
close(3)                                = 0
write(1, "[>] Check 1 no.: 2626\n", 22[>] Check 1 no.: 2626
) = 22
write(1, "[>] Check 2 no.: 3979\n", 22[>] Check 2 no.: 3979
) = 22
write(1, "[>] Check 3 no.: 5331\n", 22[>] Check 3 no.: 5331
) = 22
write(1, "[>] Check 1 failed.\n", 20[>] Check 1 failed.
)   = 20
write(1, "[>] Char was 00.\n", 17[>] Char was 00.
)      = 17
exit_group(-1)                          = ?
+++ exited with 255 +++
```

你可以看到，在目标二进制文件的处理过程中，我们在打开输入文件之前运行了大量代码。查看strace的输出，我们甚至在打开输入文件之前已经运行了以下系统调用：

```
execve
brk
access
access
openat
fstat
mmap
close
access
openat
read
opeant
read
fstat
mmap
mmap
mprotect
mmap
mmap
arch_prctl
mprotect
mprotect
mprotect
munmap
fstat
brk
brk
write
```

在所有这些系统调用之后，我们终于从磁盘打开文件并读取字节，以下是`strace`输出中的一行：

```
openat(AT_FDCWD, "Canon_40D.jpg", O_RDONLY) = 3
```

所以请记住，我们的简单模糊测试器在每次模糊测试迭代中都会运行这些系统调用。我们的简单模糊测试器（*https://gist.github.com/h0mbre/0873edec8346122fc7dc5a1a03f0d2f1*）每次迭代都会将一个文件写入磁盘，并通过`fork()`和`execvp()`生成目标程序的一个实例。漏洞二进制文件每次迭代都会运行所有的启动系统调用，最终从磁盘读取文件。

因此，每次模糊测试迭代都会有几十个系统调用和两次文件系统交互。难怪我们的简单模糊测试器如此之慢。

##

```
三

基本的快照机制
```

我开始思考如何在模糊测试这样一个简单的目标二进制文件时节省时间，并认为如果我能找到一种方法在程序从磁盘读取文件并将内容存储在堆中之后拍摄其内存快照，我可以保存该进程状态，并手动插入一个新的模糊测试用例替换目标读取的字节，然后让程序运行直到它到达`exit()`调用。一旦目标到达exit调用，我会将程序状态倒回到拍摄快照时的状态，并插入一个新的模糊测试用例，然后再重复这一过程。

你可以看到这将如何提高性能。我们将跳过所有目标二进制文件的启动开销，并完全绕过所有文件系统交互。一个巨大的区别是我们只会调用一次`fork()`，这是一个昂贵的系统调用。假设进行100,000次模糊测试迭代，我们将从200,000次文件系统交互（一次是简单模糊测试器在磁盘上创建一个变异的.jpeg文件，一次是目标读取变异的.jpeg文件）和100,000次`fork()`调用减少到0次文件系统交互和仅一次初始`fork()`。

总而言之，我们的模糊测试过程应如下所示：

1.启动目标二进制文件，但在任何操作运行之前在第一条指令上中断

2.在“开始”和“结束”位置设置断点（开始将在程序从磁盘读取字节之后，结束将在`exit()`的地址）

3.运行程序直到它到达“开始”断点

4.将进程的所有可写内存段收集到一个缓冲区中

5.捕获所有寄存器状态

6.将我们的模糊测试用例插入堆中，覆盖程序从磁盘读取的字节

7.恢复目标二进制文件，直到它到达“结束”断点

8.将进程状态倒回到“开始”时的状态

9.从第6步开始重复

我们只需要执行步骤1-5一次，所以这个过程不需要非常快。步骤6-9是模糊测试器将花费99%时间的地方，所以我们需要这个过程非常快。

使用Ptrace编写一个简单的调试器，为了实现我们的快照机制，我们需要使用非常直观但显然缓慢且有约束的`ptrace()`接口。当我几周前开始编写模糊测试器的调试器部分时，我主要参考了Eli Bendersky（*https://twitter.com/elibendersky*）的这篇博客文章（*https://eli.thegreenplace.net/2011/01/23/how-debuggers-work-part-1*），这是一个很好的`ptrace()`入门教程，展示了如何创建一个简单的调试器。

##

```
四

断点
```

我们代码中的调试器部分实际上不需要太多功能，它只需要能够插入和删除断点。使用`ptrace()`设置和删除断点的方法是覆盖地址处的单字节指令，使用`int3`操作码`\xCC`。然而，如果你在设置断点时直接覆盖该值，将无法删除断点，因为你不知道那里原本持有的值是什么，因此你不知道用什么来覆盖`\xCC`。

要开始使用`ptrace()`，我们使用`fork()`生成第二个进程。

```
pid_t child_pid = fork();
if (child_pid == 0) {
    //we're the child process here
    execute_debugee(debugee);
}
```

现在我们需要让子进程自愿被父进程“跟踪”。这是通过使用`PTRACE_TRACEME`参数完成的，我们将在`execute_debugee`函数中使用它：

```
// request via PTRACE_TRACEME that the parent trace the child
long ptrace_result = ptrace(PTRACE_TRACEME, 0, 0, 0);
if (ptrace_result == -1) {
    fprintf(stderr, "\033[1;35mdragonfly>\033[0m error (%d) during ", errno);
    perror("ptrace");
    exit(errno);
}
```

函数的其余部分不涉及`ptrace`，但我会继续在这里展示，因为有一个重要的函数可以强制在被调试进程中禁用ASLR（地址空间布局随机化）。这是至关重要的，因为我们将利用静态地址的断点，这些地址不能在不同进程间变化。我们通过调用带有`ADDR_NO_RANDOMIZE`的`personality()`来禁用ASLR。另外，我们会将`stdout`和`stderr`重定向到`/dev/null`，这样我们就不会因为目标二进制文件的输出弄乱我们的终端。

```
// disable ASLR
int personality_result = personality(ADDR_NO_RANDOMIZE);
if (personality_result == -1) {
    fprintf(stderr, "\033[1;35mdragonfly>\033[0m error (%d) during ", errno);
    perror("personality");
    exit(errno);
}

// dup both stdout and stderr and send them to /dev/null
int fd = open("/dev/null", O_WRONLY);
dup2(fd, 1);
dup2(fd, 2);
close(fd);

// exec our debugee program, NULL terminated to avoid Sentinel compilation
// warning. this replaces the fork() clone of the parent with the
// debugee process
int execl_result = execl(debugee, debugee, NULL);
if (execl_result == -1) {
    fprintf(stderr, "\033[1;35mdragonfly>\033[0m error (%d) during ", errno);
    perror("execl");
    exit(errno);
}
```

所以首先，我们需要一种方法在插入断点之前抓取地址处的单字节值。对于模糊测试器，我开发了一个头文件和源文件，称为`ptrace_helpers`，以帮助简化使用`ptrace()`的开发过程。为了抓取该值，我们将抓取地址处的64位值，但只关心最右边的字节。（我使用类型`long long unsigned`，因为在`<sys/user.h>`中寄存器值是这样定义的，我希望保持一致）。

```
long long unsigned get_value(pid_t child_pid, long long unsigned address) {

    errno = 0;
    long long unsigned value = ptrace(PTRACE_PEEKTEXT, child_pid, (void*)address, 0);
    if (value == -1 && errno != 0) {
        fprintf(stderr, "dragonfly> Error (%d) during ", errno);
        perror("ptrace");
        exit(errno);
    }

    return value;
}
```

所以这个函数将使用`PTRACE_PEEKTEXT`参数读取子进程（`child_pid`）中位于地址处的值，这是我们的目标。现在我们有了这个值，可以将其保存并插入我们的断点，代码如下：

```
void set_breakpoint(long long unsigned bp_address, long long unsigned original_value, pid_t child_pid) {

    e...