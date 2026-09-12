---
title: ProcDump-for-Linux v3.5.3
url: https://kitploit.com/en/posts/github-microsoft-procdump-for-linux-353
source: Kitploit
date: 2026-09-11
fetch_date: 2026-09-12T06:48:07.441841
---

# ProcDump-for-Linux v3.5.3

[Skip to content](#main-content)

[![Kitploit](/_next/image?url=%2Flogo.png&w=64&q=75)KITPLOIT](/en)[Tools](/en/tools)[Blog](/en/blog)Categories

EN

[Submit](/en/submit)

[Tools](/en/tools)[Blog](/en/blog)Categories

[Submit](/en/submit)

EN

Hacking, PenTest, and Cybersecurity Tools for Your Security Arsenal!

[Back to updates](/en/updates)

![](https://assets.kitploit.com/production/public/tools/1584/d8ba746dc3678e33d5a274bb44d88537114fa7e4513bfccc6b9453a5d7f1b353.png)

New releaseSep 11, 2026

# ProcDump-for-Linux v3.5.3

A Linux version of the ProcDump Sysinternals tool

Share

# ProcDump [![Build Status](https://dev.azure.com/sysinternals/Tools/_apis/build/status/Sysinternals.ProcDump-for-Linux?branchName=master)](https://dev.azure.com/sysinternals/Tools/_build/latest?definitionId=341&branchName=master)

ProcDump is a Linux and Mac reimagining of the classic ProcDump tool from the Sysinternals suite of tools for Windows. ProcDump provides a convenient way for Linux and Mac developers to create core dumps of their application based on performance triggers. ProcDump for Linux and Mac is part of [Sysinternals](https://sysinternals.com).

![ProcDump in use](https://assets.kitploit.com/production/public/readmes/1584/273234fe53dbe4139a6d977f02b323255904a02de480dc6c1cb6eb905df3088f.gif "Procdump in use")

# Installation & Usage

## Requirements

* Minimum Linux OS:
  + Red Hat Enterprise Linux / CentOS 7
  + Fedora 29
  + Ubuntu 16.04 LTS
  + `gdb` >= 7.6.1
* Minimum Mac OS: Sierra

## Install ProcDump

Please see installation instructions [here](https://github.com/microsoft/procdump-for-linux/blob/master/INSTALL.md).

## Build

Please see build instructions [here](https://github.com/microsoft/procdump-for-linux/blob/master/BUILD.md).

## Usage

**BREAKING CHANGE** With the release of ProcDump 1.3 the switches are now aligned with the Windows ProcDump version.
Please note that the [Mac](https://github.com/microsoft/ProcDump-for-Mac) version currently has a limited set of triggers.

root@kitploit:~

```
Capture Usage:
   procdump [-n Count]
            [-s Seconds]
            [-c|-cl CPU_Usage]
            [-m|-ml Commit_Usage1[,Commit_Usage2...]]
            [-gcm [<GCGeneration>: | LOH: | POH:]Memory_Usage1[,Memory_Usage2...]]
            [-gcgen Generation]
            [-restrack [nodump]]
            [-sr Sample_Rate]
            [-tc Thread_Threshold]
            [-fc FileDescriptor_Threshold]
            [-sig Signal_Number1[,Signal_Number2...]]
            [-e]
            [-f Include_Filter,...]
            [-fx Exclude_Filter]
            [-mc Custom_Dump_Mask]
            [-pf Polling_Frequency]
            [-o]
            [-log syslog|stdout]
            {
             {{[-w] Process_Name | [-pgid] PID} [Dump_File | Dump_Folder]}
            }

Options:
   -n      Number of dumps to write before exiting.
   -s      Consecutive seconds before dump is written (default is 10).
   -c      CPU threshold above which to create a dump of the process.
   -cl     CPU threshold below which to create a dump of the process.
   -m      Memory commit threshold(s) (MB) above which to create dumps.
   -ml     Memory commit threshold(s) (MB) below which to create dumps.
   -gcm    [.NET] GC memory threshold(s) (MB) above which to create dumps for the specified generation or heap (default is total .NET memory usage).
   -gcgen  [.NET] Create dump when the garbage collection of the specified generation starts and finishes.
   -restrack Enable memory leak tracking (malloc family of APIs). If used without other triggers, use 't' to manually capture a restrack report. When used with other triggers, the 'nodump' option can be used to prevent dump generation and only produce restrack report(s).
   -sr     Sample rate when using -restrack.
   -tc     Thread count threshold above which to create a dump of the process.
   -fc     File descriptor count threshold above which to create a dump of the process.
   -sig    Comma separated list of signal number(s) during which any signal results in a dump of the process.
   -e      [.NET] Create dump when the process encounters an exception.
   -f      Filter (include) on the content of .NET exceptions (comma separated). Wildcards (*) are supported.
   -fx     Filter (exclude) on the content of -restrack call stacks. Wildcards (*) are supported.
   -mc     Custom core dump mask (in hex) indicating what memory should be included in the core dump. Please see 'man core' (/proc/[pid]/coredump_filter) for available options.
   -pf     Polling frequency.
   -o      Overwrite existing dump file.
   -log    Writes extended ProcDump tracing to the specified output stream (syslog or stdout).
   -w      Wait for the specified process to launch if it's not running.
   -pgid   Process ID specified refers to a process group ID.
```

### Resource Tracking

The -restrack switch activates resource tracking, allowing for the monitoring and reporting of any resource allocations that have not been freed at the time of generating the core dump. The results are saved to a file with a '.restrack' extension. Currently, the following resource allocation/deallocation functions are tracked:

Allocation:

* malloc
* calloc
* realloc
* reallocarray
* mmap

Deallocation:

* free
* munmap

The Mac version does not currently implement resource tracking.

### Examples

> The following examples all target a process with pid == 1234

The following will create a core dump immediately.

root@kitploit:~

```
sudo procdump 1234
```

The following will create 3 core dumps 10 seconds apart.

root@kitploit:~

```
sudo procdump -n 3 1234
```

The following will create 3 core dumps 5 seconds apart.

root@kitploit:~

```
sudo procdump -n 3 -s 5 1234
```

The following will create a core dump each time the process has CPU usage >= 65%, up to 3 times, with at least 10 seconds between each dump.

root@kitploit:~

```
sudo procdump -c 65 -n 3 1234
```

The following will create a core dump each time the process has CPU usage >= 65%, up to 3 times, with at least 5 seconds between each dump.

root@kitploit:~

```
sudo procdump -c 65 -n 3 -s 5 1234
```

The following will create a core dump when CPU usage is outside the range [10,65].

root@kitploit:~

```
sudo procdump -cl 10 -c 65 1234
```

The following will create a core dump when CPU usage is >= 65% or memory usage is >= 100 MB.

root@kitploit:~

```
sudo procdump -c 65 -m 100 1234
```

The following will create a core dump when memory usage is >= 100 MB followed by another dump when memory usage is >= 200MB.

root@kitploit:~

```
sudo procdump -m 100,200 1234
```

The following will create a memory leak report (no dumps) every time the user presses 't':

root@kitploit:~

```
sudo procdump -restrack 1234
```

The following will create 3 memory leak reports (no dumps) 5 seconds apart:

root@kitploit:~

```
sudo procdump -n 3 -s 5 -restrack nodump 1234
```

The following will create a core dump and a memory leak report when memory usage is >= 100 MB

root@kitploit:~

```
sudo procdump -m 100 -restrack 1234
```

The following will create a memory leak report (no dumps) when memory usage is >= 100 MB

root@kitploit:~

```
sudo procdump -m 100 -restrack nodump 1234
```

The following will create a core dump and a memory leak report when memory usage is >= 100 MB by sampling every 10th memory allocation.

root@kitploit:~

```
sudo procdump -m 100 -restrack -sr 10 1234
```

The following will create a core dump and a memory leak report when memory usage is >= 100 MB and exclude any call stacks that contain frames with the string "cache" in them

root@kitploit:~

```
sudo procdump -m 100 -restrack -fx *cache* 1234
```

The following will create a core dump when the total .NET memory usage is >= 100 MB followed by another dump when memory usage is >= 200MB.

root@kitploit:~

```
sudo procdump -gcm 100,200 1234
```

The following will create a core dump when .NET memory usage for generation 1 is >= 1 MB followed by another dump ...