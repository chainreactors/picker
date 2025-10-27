---
title: Shell Script Compiler (shc)
url: https://dfir.ch/posts/shell_script_compiler/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-14
fetch_date: 2025-10-06T19:43:04.797320
---

# Shell Script Compiler (shc)

[Home](https://dfir.ch/)
[ ]

Menu

* [Home](/)
* [Posts](/posts/)
* [Talks](/talks/)
* [Tweets](/tweets/)
* |

LIGHT

DARK

# Shell Script Compiler (shc)

11 Dec 2024

**Table of Contents**

* [Introduction](#introduction)
* [strace](#strace)
* [Forensic traces](#forensic-traces)
* [Conclusion](#conclusion)

## Introduction

> After installing the payload, the shell script inst.sh runs a backdoor binary that matches the target deviceâs architecture. The backdoor is a shell script compiled using an open-source project called Shell Script Compiler (shc), and enables the threat actors to perform subsequent malicious activities and deploy additional tools on affected systems."

**Source:** [IoT devices and Linux-based systems targeted by OpenSSH trojan campaign, Microsoft Threat Intelligence](https://www.microsoft.com/en-us/security/blog/2023/06/22/iot-devices-and-linux-based-systems-targeted-by-openssh-trojan-campaign/)

In this blog post, we will analyze Shc - `A generic shell script compiler`, mentioned by Microsoft in the linked blog post above.

> Shc takes a script specified on the command line and produces C source code. The generated source code is then compiled and linked to produce a stripped binary executable. [..] Upon execution, the compiled binary will decrypt and execute the code with the shell -c option.

**Source:** <https://github.com/neurobin/shc>

For creating an untraceable binary (which prevents strace, ptrace etc.), `shc` uses the following command:

```
shc -U -f script.sh -o binary
```

The -U flag ensures the resulting binary is untraceable, leveraging a technique that makes debugging difficult. Once compiled, the binary executes the encrypted script transparently, mimicking the behavior of the original shell script.

## strace

How does shc make the binary untraceable? With a rather old technique that is still working today. By calling `ptrace` with the `PTRACE_TRACEME` option, a process can detect if it’s being debugged and execute different instructions. This is an effective anti-debugging technique. Here is the relevant source code from the `shc` repository:

```
if(pid==0) {
//Start tracing to protect from dump & trace
    if (ptrace(PTRACE_TRACEME, 0, 0, 0) < 0) {
        kill(getpid(), SIGKILL);
        _exit(1);
}
```

The child process calls ptrace(PTRACE\_TRACEME) to inform the kernel that it wants to be traced by its parent. The primary purpose here is to ensure the child process isn’t already being traced by an external debugger. If this call fails (returns a value < 0), it typically means: The process is already being traced by a debugger.

If ptrace(PTRACE\_TRACEME) fails, the process sends the `SIGKILL` signal to the process itself. This is an uncatchable signal that immediately terminates the process. And indeed, when we try to trace our `shc_ncat` binary, the tracing is prohibited, i.e. the process is terminated:

```
# strace ./shc_ncat
execve("./shc_ncat", ["./shc_ncat"], 0x7ffebda8f110 /* 24 vars */) = 0
[..]]
mprotect(0x741967d45000, 4096, PROT_READ) = 0
mprotect(0x5952394e3000, 4096, PROT_READ) = 0
mprotect(0x741967d80000, 8192, PROT_READ) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
munmap(0x741967d3b000, 24823)           = 0
clone(child_stack=NULL, flags=CLONE_CHILD_CLEARTID|CLONE_CHILD_SETTID|SIGCHLD, child_tidptr=0x741967d38a10) = 3191019
wait4(3191019, ./shc_ncat: Operation not permitted
 <unfinished ...>)       = ?
+++ killed by SIGKILL +++
Killed
```

However, if the binary is executed before attaching the tracer (e.g., `strace -p <pid>`), tracing may still succeed, bypassing the initial `ptrace` check.

## Forensic traces

For our testing, we created a simple netcat bind shell generated with [revshells.com](https://www.revshells.com/):

![Reverse shell generator](/images/shc/reverse_shell_generator.png "Reverse shell generator")

Figure 1: Reverse shell generator

**Process list**

Although `shc` obfuscates shell commands in the binary, forensic analysis reveals traces of the original script once the binary is running:

![ps aux](/images/shc/ps_aux.png "ps aux")

Figure 2: Output of ps aux

**Command line in /proc**

The same command appears in the `cmdline` file within the `/proc` directory of the process:

![cmdline in the /proc folder](/images/shc/cmdline.png "cmdline in the /proc folder")

Figure 3: cmdline in the /proc folder

## Conclusion

`shc` is not a true compiler but rather a tool for obfuscating and encrypting shell scripts into binary form. While it employs anti-debugging measures using `ptrace`, these can be partially circumvented in certain scenarios. Forensic analysis demonstrates that while `shc` obfuscates the script at rest, traces of the original command are still relatively easy to find.

Â© 2025 .
Powered by [Hugo blog awesome](https://github.com/hugo-sid/hugo-blog-awesome).