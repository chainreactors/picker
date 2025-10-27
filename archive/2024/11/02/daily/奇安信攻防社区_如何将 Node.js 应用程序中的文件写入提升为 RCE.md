---
title: 如何将 Node.js 应用程序中的文件写入提升为 RCE
url: https://forum.butian.net/share/3833
source: 奇安信攻防社区
date: 2024-11-02
fetch_date: 2025-10-06T19:16:01.721987
---

# 如何将 Node.js 应用程序中的文件写入提升为 RCE

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

### 如何将 Node.js 应用程序中的文件写入提升为 RCE

* [渗透测试](https://forum.butian.net/topic/47)

在这篇博文中,我们将强调代码安全基础的重要性。我们会展示一个技术案例:攻击者如何能够把 Node.js 应用中的文件写入漏洞转化为远程代码执行,即便目标系统的文件系统是以只读方式挂载的。这个技术通过利用暴露的管道文件描述符来获得代码执行能力,从而绕过了这类加固环境中的限制。

基础设施加固确实能增强应用程序抵御攻击的能力。这些安全措施提高了攻击者的门槛,使漏洞利用变得更加困难。但是,我们不能把它当作解决一切问题的银弹,因为执着的攻击者仍然可以利用源代码中的漏洞实现突破。
在这篇博文中,我们将强调代码安全基础的重要性。我们会展示一个技术案例:攻击者如何能够把 Node.js 应用中的文件写入漏洞转化为远程代码执行,即便目标系统的文件系统是以只读方式挂载的。这个技术通过利用暴露的管道文件描述符来获得代码执行能力,从而绕过了这类加固环境中的限制。
文件写入漏洞
======
在我们主要针对Web的漏洞研究过程中，经常会遇到各种不同类型的漏洞，比如跨站脚本(XSS)、SQL注入、不安全的反序列化、服务器端请求伪造(SSRF)等等。这些漏洞的影响程度和利用难度各不相同，但有一些类型的漏洞一旦被发现，几乎可以确定整个应用都会被攻陷。
\*\*任意文件写入\*\*就是这样一种严重的漏洞类型。虽然攻击者还需要想办法确定写入什么内容以及写入到哪里，但通常有很多方式可以把它转化为代码执行，从而完全控制应用服务器：
- 在网站根目录写入PHP、JSP、ASPX等类型的文件
- 覆盖会被服务端模板引擎处理的模板文件
- 写入配置文件(比如uWSG的.ini文件或Jetty的.xml文件)
- 添加Python的站点特定配置钩子
- 使用通用手法,如写入SSH密钥、添加定时任务或覆盖用户的.bashrc文件
这些例子说明，攻击者通常能找到简单的方法把任意文件写入漏洞转化为代码执行。为了减少此类漏洞的危害，应用的底层基础设施往往会进行加固。这确实增加了攻击者利用的难度，但并非完全无法利用。
加固环境中的文件写入
==========
我们最近发现了一个Node.js应用中的任意文件写入漏洞，这个漏洞的利用并不那么容易。虽然漏洞本身比较复杂，但可以简化为以下的代码片段：
```php
app.post('/upload', (req, res) => {   const { filename, content } = req.body;   fs.writeFile(filename, content, () => {       res.json({ message: 'File uploaded!' });   });});
```
这段代码中的`fs.writeFile`函数用于写入文件，其中`filename`和`content`这两个参数都可以被用户完全控制。因此，这里存在一个任意文件写入漏洞。
在评估这个漏洞的影响时，我们注意到运行该应用的用户只对特定的上传文件夹有写入权限。\*\*文件系统的其他部分都是只读的\*\*。虽然这看起来像是漏洞利用的死胡同，但它引发了我们一个有趣的研究问题：
\*\*在目标系统的文件系统以只读方式挂载的情况下，是否可能将任意文件写入漏洞转化为代码执行？\*\*
只读环境下的文件写入
==========
在Linux这样的Unix系统中，一切皆文件。不同于ext4这样存储数据在物理硬盘上的传统文件系统，还有一些文件系统服务于不同的目的。procfs虚拟文件系统就是其中之一，它通常挂载在`/proc`目录下，充当了探察内核内部运作的窗口。procfs并不存储实际的文件，而是提供了对运行中进程、系统内存、硬件配置等实时信息的访问。
procfs提供的一个特别有趣的信息是运行中进程的打开文件描述符，可以通过`/proc/<pid>/fd/`来查看。进程打开的文件不仅包括传统文件，还包括设备文件、套接字和管道。例如，可以用下面的命令列出Node.js进程打开的文件描述符：
```php
user@host:~$ {% mark yellow %}ls -al /proc/`pidof node`/fd{% mark %}total 0dr-x------ 2 user user 22 Oct 8 13:37 .dr-xr-xr-x 9 user user  0 Oct 8 13:37 ..lrwx------ 1 user user 64 Oct 8 13:37 0 -> /dev/pts/1lrwx------ 1 user user 64 Oct 8 13:37 1 -> /dev/pts/1lrwx------ 1 user user 64 Oct 8 13:37 2 -> /dev/pts/1lrwx------ 1 user user 64 Oct 8 13:37 3 -> 'anon\_inode:[eventpoll]'lr-x------ 1 user user 64 Oct 8 13:37 4 -> 'pipe:[9173261]'l-wx------ 1 user user 64 Oct 8 13:37 5 -> 'pipe:[9173261]'lr-x------ 1 user user 64 Oct 8 13:37 6 -> 'pipe:[9173262]'l-wx------ 1 user user 64 Oct 8 13:37 7 -> 'pipe:[9173262]'lrwx------ 1 user user 64 Oct 8 13:37 8 -> 'anon\_inode:[eventfd]'lrwx------ 1 user user 64 Oct 8 13:37 9 -> 'anon\_inode:[eventpoll]'...
```
从上面的输出可以看到，这里包含了匿名管道(比如`pipe:[9173261]`)。与在文件系统上有具体文件名的命名管道不同，由于缺少引用，通常无法直接写入匿名管道。但是，procfs文件系统允许我们通过`/proc/<pid>/fd/`中的条目来引用管道。与procfs下的其他文件相比，这种文件写入不需要root权限，运行Node.js应用的低权限用户就可以执行：
```php
user@host:~$ echo hello > /proc/`pidof node`/fd/5
```
即使procfs以只读方式挂载(比如在Docker容器中)，写入管道仍然是可能的，因为管道由内核内部使用的一个单独的文件系统`pipefs`处理。
这为能够写入任意文件的攻击者打开了新的攻击面，因为他们可以向从匿名管道读取数据的事件处理器输送数据。
Node.js与管道
==========
Node.js构建在V8 JavaScript引擎之上，是单线程的。但Node.js提供了异步非阻塞的事件循环。为此，它使用了一个叫libuv的库。这个库使用匿名管道来发送和处理事件，正如我们在上面的输出中看到的，这些管道通过procfs暴露出来。
当一个Node.js应用存在文件写入漏洞时，攻击者可以自由地写入这些管道，因为这些管道对运行应用的用户来说是可写的。那么，写入管道的数据会发生什么呢？
在审计相关的libuv源码时，一个名为`uv\_\_signal\_event`的处理器引起了我们的注意。它假定从管道读取的数据是`uv\_\_signal\_msg\_t`类型的消息：
```php
static void {% mark yellow %}uv\_\_signal\_event{% mark %}(uv\_loop\_t\* loop,                             uv\_\_io\_t\* w,                             unsigned int events) {  {% mark yellow %}uv\_\_signal\_msg\_t\*{% mark %} msg;  // [...]  do {    r = {% mark yellow %}read{% mark %}(loop->{% mark yellow %}signal\_pipefd[0]{% mark %}, {% mark yellow %}buf{% mark %} + bytes, sizeof(buf) - bytes);    // [...]    for (i = 0; i < end; i += sizeof(uv\_\_signal\_msg\_t)) {      {% mark yellow %}msg = (uv\_\_signal\_msg\_t\*) (buf + i);{% mark %}      // [...]
```
这个`uv\_\_signal\_msg\_t`数据结构只包含两个成员：一个`handle`指针和一个名为`signum`的整数：
```php
typedef struct {  {% mark yellow %}uv\_signal\_t\* handle;{% mark %}  int signum;} uv\_\_signal\_msg\_t;
```
`handle`指针的`uv\_signal\_t`类型是`uv\_signal\_s`数据结构的别名，其中包含了一个特别有趣的成员`signal\_cb`：
```php
struct uv\_signal\_s {  UV\_HANDLE\_FIELDS  uv\_signal\_cb signal\_cb;  int signum;  // [...]
```
`signal\_cb`成员是一个函数指针，它指向了一个回调函数的地址。当事件处理器中两个数据结构的`signum`值匹配时，这个回调函数会被调用：
```php
      // [...]      handle = msg->handle;      if (msg->signum == handle->signum) {        assert(!(handle->flags & UV\_HANDLE\_CLOSING));        handle->signal\_cb(handle, handle->signum);      }
```
也就是说，如果我们能够精心构造写入管道的数据，让它包含合适的`handle`指针和`signum`值，就有机会让事件处理器执行我们指定的代码。这为漏洞利用打开了一个新的思路。
下图显示了事件处理程序所需的数据结构：
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-86c4e408edf182e4bf306945a8b72a7f0ec616b2.png)
这对攻击者来说是一个非常有希望的情况：他们可以向管道写入任意数据，而且有一条直接通往函数指针调用的路径。事实上，我们并不是第一个注意到这一点的研究者。在8月8日，HackerOne公开了来自Lee Seunghyun的一份精彩报告，他描述了一个不同的场景，在这个场景中他能够利用Node.js程序内的开放文件描述符绕过任何模块和进程级别的权限限制 - 基本上就是一种沙箱逃逸。
即便在他描述的场景中（这不是我们最初考虑的情况），这也不被认为是一个安全漏洞，该报告被标记为信息性报告并关闭。这意味着我们接下来要描述的技术仍然适用于最新版本的Node.js，而且在近期可能也不会改变。
构建数据结构
======
攻击者利用文件写入漏洞来利用这个事件处理器的一般策略可能是这样的：
- 向管道写入一个伪造的`uv\_signal\_s`数据结构
- 将`signal\_cb`函数指针设置为想要调用的任意地址
- 向管道写入一个伪造的`uv\_\_signal\_msg\_t`数据结构
- 将`handle`指针指向之前写入的`uv\_signal\_s`数据结构
- 为两个数据结构设置相同的`signum`值
- 获得任意代码执行能力
假设攻击者只能写入文件，这一切都需要在一次写入中完成，而且无法预先读取任何内存。
事件处理器的缓冲区相当大，这让攻击者可以轻松地将两个数据结构写入管道。但是这里有一个障碍：由于写入管道的所有数据都存储在栈上，数据结构的地址是未知的：
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-620b4da046258fcf4953dace9ac149bd6c5a3963.png)
因此，攻击者无法让`handle`指针引用伪造的`uv\_signal\_s`数据结构。这就引出了一个问题：是否还有任何数据是攻击者可以引用的？
通过ASLR(地址空间布局随机化)，栈、堆和所有库的地址都是随机化的。但是，让人意外的是，Node.js二进制文件本身的段并没有启用PIE(位置无关可执行文件)。我们可以看到官方Linux版本的Node.js的安全特性：
```php
user@host:~$ checksec /opt/node-v22.9.0-linux-x64/bin/node [\*] '/opt/node-v22.9.0-linux-x64/bin/node'    Arch:     amd64-64-little    RELRO:    Full RELRO    Stack:    No canary found    NX:       NX enabled    PIE:      No PIE (0x400000)
```
这样做的原因显然是出于性能考虑，因为PIE的间接寻址会带来一些额外开销。对攻击者来说，这意味着他们可以引用Node.js段中的数据，因为这个地址是已知的。
这一发现为构建利用链提供了重要的基础，因为攻击者可以利用这个固定的地址空间来定位和引用所需的数据结构。
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-582374b0bbbc22067393a59ee87bd6ac8be6bc71.png) 接下来的问题是：攻击者如何能在Node.js的段中存储一个伪造的`uv\_signal\_s`数据结构？一种思路是寻找让Node.js在静态位置存储攻击者控制的数据的方法（比如从HTTP请求读取的数据），但这看起来相当具有挑战性。
一个更简单的方法是直接利用已有的数据。通过检查Node.js的内存段，攻击者可以在现有数据中找到适合用作`uv\_signal\_s`伪结构的数据。
攻击者理想中的数据结构应该是这样的：
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-143749893ab6daec9c652b1008487a1af78f8426.png)
攻击者需要在Node.js的二进制段中找到一个满足这些条件的数据片段，这样就可以复用这些已存在的数据，而不是试图注入新的数据。
这个数据结构以一个命令字符串(`"touch /tmp/pwned"`)开始，后面紧跟着`system`函数的地址，这个地址正好与`signal\_cb`函数指针重叠。攻击者只需要让`signum`值与伪造的`uv\_signal\_s`数据结构匹配，回调函数就会被调用，从而实际执行了`system("touch /tmp/pwned")`。
这种方法需要在Node.js的段中存在`system`函数的地址。全局偏移表(GOT)通常是一个候选位置。但是，Node.js并不使用`system`函数，所以它的地址并不在GOT中。即使地址存在，生成的伪造`uv\_signal\_s`数据结构的开头可能也只是GOT中的另一个条目，而不是一个有用的命令字符串。
因此，另一个方法似乎更可行：经典的ROP链(Return-Oriented Programming，返回导向编程)。
搜索数据结构片段
========
每个ROP链的开始都是搜索有用的ROP片段(gadget)。用于搜索ROP片段的工具通常会解析磁盘上的ELF文件，然后确定所有可执行段。`.text`段通常是最大的可执行段，因为它存储了程序本身的指令：
![](https://cdn-yg-zzbm.yun.qianxin.com/attack-forum/2024/10/attach-34a80fab1e87fdf26a38ec52b7971534729221b8.png)
这个工具会遍历这个段中的字节，寻找比如`ret`指令这样适合作为ROP片段末尾的指令。然后工具会从表示`ret`指令的字节开始，逐字节向前搜索，以找出所有可能有用的ROP片段：
```php
位置A:  pop rdi          ; 设置第一个函数参数  ret             ; 返回到下一个片段位置B:  mov rax, [rsp]   ; 从栈上读取数据  ret             ; 返回到下一个片...