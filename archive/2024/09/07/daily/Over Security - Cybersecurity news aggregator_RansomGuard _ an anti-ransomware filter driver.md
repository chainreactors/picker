---
title: RansomGuard : an anti-ransomware filter driver
url: https://0mwindybug.github.io/RansomGuard/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-07
fetch_date: 2025-10-06T18:30:26.995131
---

# RansomGuard : an anti-ransomware filter driver

[Home](/)

* [About](/about/)
* [Posts](/posts/)

Toggle menu

![Windy Bug](/images/avatar.png)

### Windy Bug

Windows Internals & Driver Development

Follow

* [GitHub](https://github.com/0mWindyBug)
* [Twitter](https://twitter.com/0mWindyBug)

# RansomGuard : an anti-ransomware filter driver

42 minute read

## Intro

Ransomware is one of the simplest, yet significant threats facing organizations today. Unsuprisingly, the rise and continuing development of ransomware led to a plentitude of research aimed at detecting and preventing it. AV vendors, independent security reseachers and academies all proposing various solutions to mitigate the threat. In this blogpost we introduce RansomGuard, a filesystem minifilter driver designed to stop ransomware from encrypting files through the use of the filter manager. We also discuss the concepts and ideas that led to the design of RansomGuard, and the challenges we encountered in its implementation.
RansomGuard’s source can be found [here](https://github.com/0mWindyBug/RansomGuard)

## Overview

[The filter manager](#the-filter-manager)

* Introduction & the motivation behind the framework
* working with and managing contexts

[Detecting encryption](#Detecting-encryption)

[Ransomware variations](#Ransomware-variations)

[Tracking & Evaluating file handles](#Tracking--Evaluating-file-handles)

* Truncated files
* Cleanup vs Close
* FatCheckIsOperationLegal
* Filters walkthrough
* RansomGuard against WannaCry

[Filtering Memory Mapped I/O](#Filtering-Memory-Mapped-IO)

* Memory mapped files usage by Ransomwares
* Synchronous flush
* Asynchronous mapped page writer write
* Building asynchronous context
* Filtering Paging I/O
* “Blocking” a mapped page writer write
* RansomGuard against Maze

[Filtering file deletions](#Filtering-file-deletions)

* How NTFS & FAT handle file deletions
* Racing deletes
* Extending the driver
* RansomGuard against yet another ransomware variation

[Wrapping up](#Wrapping-up)

[Appendix](#Appendix-cached-write-operation)

## The filter manager

The filter manager (FltMgr.sys) is a system-supplied kernel-mode driver that implements and exposes functionality commonly required in file system filter drivers.
It provides a level of abstraction allowing driver developers to invest more time into writing the actual logic of the filter rather than writing a body of “boiler plate” code. Speaking of boiler plate code , writing a legacy file-system filter driver that **does nothing** can take up to nearly 6,000 lines of code. The filter manager essentially serves as a comprehensive “framework” for writing file system filter drivers. The framework provides the one legacy file system filter driver necessary in the system (fltmgr.sys), and as I/O requests arrive at the filter manager legacy filter device object, it invokes the registered minifilters using a call out model.
After each minifilter processes the request, the filter manager then calls through to the next device object in the device stack, if any.
Putting it simply, we can use the filter manager to register callbacks to be invoked pre and post a file-system operation as if our driver was part of the file-system device stack. In case you are not familiar with the filter manager API I suggest to review the related docs before proceeding with the article, mainly
[FLT\_REGISTRATION](https://learn.microsoft.com/en-us/windows-hardware/drivers/ddi/fltkernel/ns-fltkernel-_flt_registration).
It’s important to note that easy to write does not mean easy to design, which remains a fairly complex task with minifilters, of course - depending on the minifilter’s task in hand. Nevertheless it makes it possible to go from design to a working filter in weeks rather than months, which is great.

## Minifilter contexts

A context is a structure defined by a minifilter driver that can be associated with an object. The filter manager provides support for minifilter drivers to associate contexts with objects and preserve state across I/O operations.
Contexts are extremley useful, and can be attached to the following objects :
- Files
- Instances
- Streams
- Stream Handles (File Objects…)
- Transactions
- Volumes

Depending on the file system there are certian limitations for attaching contexts, e.g The NTFS and FAT file systems do not support file, stream, or file object contexts on paging files, in the pre-create or post-close path, or for IRP\_MJ\_NETWORK\_QUERY\_OPEN operations. A minifilter can call `FltSupports*Contexts` to check if a context type is supported for the given operation.

### Context managment

Context management is probably one of the most frustrating parts of maintaining a minifilter, your unload hangs? it’s often down to incorrect context managment. This is one (of many) reasons to why you should always enable driver verifier.
The filter manager uses reference counting to manage the lifetime of a minifilter context, whenever a context is successfully created, it’s initialized with a reference count of one. Whenever a context is referenced, for example by a successful context set or get call, the filter manager increments the reference count of the context by one. When a context is no longer needed, it’s reference count must be decremented. A positive reference count means that the context is usable, when the reference count becomes zero, the context is unusable, and the filter manager eventually frees it. Lastly, note the filter manager is the one responsible for derefencing the Set\* reference, it does that in the following conditions:

* The attached to system structure is about to go away. For example, when the file system calls `FsRtlTeardownPerStreamContexts` as part of tearing down the FCB, the Filter Manager will detach any attached stream contexts and dereference them.
* The filter instance associated with the context is being detached. Again taking the stream context example, during instance teardown after the InstanceTeardown callbacks have been made the filter manager will detach any stream contexts associated with this instance from their associated `ADVANCED_FCB_HEADER` and dereference them.

### Context registration

A minifilter passes the following structure to FltRegisterFilter to register context types

```
typedef struct _FLT_CONTEXT_REGISTRATION {
  FLT_CONTEXT_TYPE               ContextType;
  FLT_CONTEXT_REGISTRATION_FLAGS Flags;
  PFLT_CONTEXT_CLEANUP_CALLBACK  ContextCleanupCallback;
  SIZE_T                         Size;
  ULONG                          PoolTag;
  PFLT_CONTEXT_ALLOCATE_CALLBACK ContextAllocateCallback;
  PFLT_CONTEXT_FREE_CALLBACK     ContextFreeCallback;
  PVOID                          Reserved1;
} FLT_CONTEXT_REGISTRATION, *PFLT_CONTEXT_REGISTRATION;
```

The `ContextCleanupCallback` is called right before the context goes away , useful for releasing internal context resources

## Detecting encryption

To detect encryption of data we are going to leverage [Shannon Entropy](https://en.m.wikipedia.org/wiki/Entropy_%28information_theory%29). We will assume the entire file is going to be encrypted, whilst partial encryption is mentioned towards the end of the article. Two datapoints are needed - one that represents the initial state of the file and another that represents the modified state of the file. We will use the follwing measurement, which was based on statistical tests performed against a large set of files of different types. It takes into account the initial entropy of the file, limiting false positives that may arise due to high entropy file types. (e.g. archives).

```
// statistical logic to determine encryption
bool evaluate::IsEncrypted(double InitialEntropy, double FinalEntropy)
{
    if (InitialEntropy == INVALID_ENTROPY || FinalEntropy == INVALID_ENTROPY || InitialEntropy <= 0)
        return false;

    double EntropyDiff = FinalEntropy - InitialEntropy;

    // the lower the initial entropy is the higher the required diff to be considered encrypted
    double SuspiciousDI...