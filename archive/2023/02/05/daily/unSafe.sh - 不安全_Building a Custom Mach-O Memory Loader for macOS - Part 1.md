---
title: Building a Custom Mach-O Memory Loader for macOS - Part 1
url: https://buaq.net/go-147946.html
source: unSafe.sh - 不安全
date: 2023-02-05
fetch_date: 2025-10-04T05:44:59.120691
---

# Building a Custom Mach-O Memory Loader for macOS - Part 1

* [unSafe.sh - 不安全](https://unsafe.sh)
* [我的收藏](/user/collects)
* [今日热榜](/?hot=true)
* [公众号文章](/?gzh=true)
* [导航](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [编码/解码](/encode)
* [文件传输](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
黑夜模式

![](https://8aqnet.cdn.bcebos.com/af802a40dd50ee89eb0ad6bf3e58b184.jpg)

Building a Custom Mach-O Memory Loader for macOS - Part 1

« Back to home In the last post we looked at how we could patc
*2023-2-4 18:3:31
Author: [blog.xpnsec.com(查看原文)](/jump-147946.htm)
阅读量:36
收藏*

---

[« Back to home](https://blog.xpnsec.com "Back to homepage")

In the [last post](https://blog.xpnsec.com/restoring-dyld-memory-loading/) we looked at how we could patch dyld to restore in-memory execution. One of the advantages of this method is that we delegate many of the intricacies of loading Mach-O binaries to macOS. But what about if we wanted to stay clear of messing with dyld, and instead roll-up our sleeves and build our own loader? How does all of this byte mapping actually work?

In this blog we’ll look at what it takes to construct an in-memory loader for Mach-O bundles within MacOS Ventura without using dyld. We’ll walk through the lower-level details of what makes up a Mach-O file, how dyld processes load commands to map areas into memory, and how we can emulate this to avoid writing payloads to disk. I also recommend reading this post alongside the code published [here](https://github.com/xpn/DyldDeNeuralyzer/blob/main/DyldDeNeuralyzer/MachoLoader/macholoader.m) to fully understand the individual areas called out.

In keeping with Apple’s migration to ARM architecture, this post will focus on the AARCH64 version of MacOS Ventura and XCode targeting macOS 12.0 and higher. With that said, let’s dig in.

## What Makes a Mach-O File?

To begin we’ll need to understand the layout of a Mach-O file. One of the best resources out there to help us to get our head around the many bits of a Mach-O container is the [Mach-O File Format Reference](https://github.com/aidansteele/osx-abi-macho-file-format-reference) from [Aidan Steele](https://twitter.com/__steele) which I recommend reviewing.

As we’re dealing with the ARM version of MacOS, we will assume that the Mach-O that we’re looking at isn’t encapsulated in the [Universal 2](https://en.wikipedia.org/wiki/Universal_binary#:~:text=Universal%202%20allows%20applications%20to,the%20transition%20to%20Apple%20silicon.) format (or has been lipo’d), so the first thing that we’ll encounter at the beginning of the file is the `mach_header_64`:

```
struct mach_header_64 {
    uint32_t    magic;
    cpu_type_t  cputype;
    cpu_subtype_t    cpusubtype;
    uint32_t    filetype;
    uint32_t    ncmds;
    uint32_t    sizeofcmds;
    uint32_t    flags;
    uint32_t    reserved;
};
```

To construct our loader, we’ll need to sanity check a few of these fields:

* `magic` - This field should hold a value of `MH_MAGIC_64`.
* `cputype` - For M1, this should be `CPU_TYPE_ARM64`.
* `filetype` - We’re going to be checking for `MH_BUNDLE` type for this post but loading different types should be easy as well.

Once we’re happy that the Mach-O is sane, we move onto processing the load commands which immediately follow the `mach_header_64` struct.

## Load Commands

A load command, as the name suggests, is a data structure used to instruct dyld on how it should load an area of the Mach-O.

Each load command is represented by the `load_command` struct:

```
struct load_command {
    unsigned long cmd;
    unsigned long cmdsize;
};
```

The `cmd` field ultimately determines what the `load_command` actually represents. For example, let’s take a very simple `load_command` of `LC_UUID` which is used to associate a UUID with the binary. This has the layout:

```
struct uuid_command {
   uint32_t cmd;
   uint32_t cmdsize;
   uint8_t uuid[16];
};
```

As you can see, this overlaps with the `load_command` struct, which is why we have the matching fields. This is the case for the various load command supported as we’ll see.

## Mach-O Segments

One of the first `load_command`‘s that we’re going to deal with when loading a Mach-O is `LC_SEGMENT_64`.

The segment command tells dyld how to map an area of the Mach-O into virtual memory, what size it should be, what protection is should have, and where the contents of the file are. Let’s look at its structure:

```
struct segment_command_64 {
    uint32_t    cmd;
    uint32_t    cmdsize;
    char        segname[16];
    uint64_t    vmaddr;
    uint64_t    vmsize;
    uint64_t    fileoff;
    uint64_t    filesize;
    vm_prot_t   maxprot;
    vm_prot_t   initprot;
    uint32_t    nsects;
    uint32_t    flags;
};
```

For our purposes, we’re going to be paying attention to:

* `segname` - The name of the segment, for example, `__TEXT`.
* `vmaddr` - The virtual address where the segment should be loaded. For example, if this is set to `0x4000`, then we’d load the segment at the allocated base of memory + `0x4000`.
* `vmsize` - The size of virtual memory to be allocated.
* `fileoff` - The offset from the beginning of the file to the contents of the Mach-O that should be copied to virtual memory.
* `filesize` - The number of bytes to copy from the file.
* `maxprot` - The maximum memory protection value that should be assigned to the region of virtual memory.
* `initprot` - The initial memory protection that should be assigned to the region of virtual memory.
* `nsects` - The number of sections which will follow this segment structure.

At this point we should note that while [dyld relies](https://github.com/apple-oss-distributions/dyld/blob/c8a445f88f9fc1713db34674e79b00e30723e79d/dyld/Loader.cpp#L1274) on `mmap` to pull in segments of a Mach-O into memory, if our initial process is executing as a hardened process (and doesn’t have something like `com.apple.security.cs.allow-unsigned-executable-memory` in the entitlements), using `mmap` isn’t going to be possible unless the bundle we provide is signed using the same developer certificate as the surrogate app. Also, we’re trying to build a memory loader, so pulling in the binary from disk in this case wouldn’t make much sense.

To work around this, in our POC we will allocate our blob of memory up front and copy it over, for example:

```
vm_allocate(mach_task_self(), (vm_address_t*)&baseAlloc, maxVirtMemSize, VM_FLAGS_ANYWHERE);
if (baseAlloc == NULL) {
    printf("[!] Error allocating %llx bytes of memory\n", maxVirtMemSize);
    return;
}
```

As with our dyld post [previously](https://blog.xpnsec.com/restoring-dyld-memory-loading/), we will need to use the correct entitlements in the host binary to allow unsigned executable memory.

## Sections

So, as you can see from the fields above, another reference exists within a segment load command, and that’s a section.

As the section resides within a segment, while it will inherit its memory protection, it has its own size and file content to be loaded. The data structure for each segment is appended to the segment command and its structure is:

```
struct section_64 {
    char        sectname[16];
    char        segname[16];
    uint64_t    addr;
    uint64_t    size;
    uint32_t    offset;
    uint32_t    align;
    uint32_t    reloff;
    uint32_t    nreloc;
    uint32_t    flags;
    uint32_t    reserved1;
    uint32_t    reserved2;
    uint32_t    reserved3;
};
```

Again, we’ll just focus on a few of these fields which are useful for our immediate purpose of constructing a loader:

* `sectname` - The name of the section, for example, `__text`.
* `segname` - The name of the segment associated with this section.
* `addr` - The virtual address offset to be used for this section.
* `size` - The size of the section in the file (and in virtual memory).
* `offset` - The offset to the contents of the section in the Mach-O file.
* `flags` - Flags can be assigned to a ...