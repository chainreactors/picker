---
title: Defeating Anti-Reverse Engineering: A Deep Dive into the ‘Trouble’ Binary
url: https://binary.ninja/2026/01/23/reversing-linux-anti-re.html
source: Binary Ninja
date: 2026-01-23
fetch_date: 2026-01-24T03:30:45.807887
---

# Defeating Anti-Reverse Engineering: A Deep Dive into the ‘Trouble’ Binary

[![](/images/binary-ninja-logo.svg)](/)

* [Features](/features/)
* [Enterprise](/enterprise/)
* [Sidekick](https://sidekick.binary.ninja)
* [Cloud](https://cloud.binary.ninja)
* [Training](/training/)
* [Support](/support/)

  [Extended Support](/support/extended.html)
  [Documentation](/support/#documentation)
  [License/Installer Recovery](/recover/)
  [Renew Current License](/renew/)
  [Slack Signup](https://slack.binary.ninja/)
  [FAQ](/faq/)
  [Sponsorship Information](/sponsorship/)
  [Portal](https://portal.binary.ninja/)
  [Contact Us](/support/)
* [Blog](/blog/)
* [Gear](https://shop.binary.ninja)

[Free](/free)
[Purchase](/purchase)

Binary Ninja [5.2, codename Io, is out](/2025/11/13/binary-ninja-5.2-io.html) and includes bitfield support, containers, hexagon, and much more.

# Binary Ninja Blog

## Defeating Anti-Reverse Engineering: A Deep Dive into the 'Trouble' Binary

* [Xusheng Li](https://github.com/xusheng6)
* 2026-01-23
* [reversing](/tag/reversing)

In this blog post, we will take a close look at a Linux binary loaded with various anti-reverse-engineering techniques.
The binary is the final boss from the book Programming Linux Anti-Reversing Techniques by Jacob Baines. I will also
take this opportunity to show off some Binary Ninja tricks that can speed up your daily analysis!

In this walkthrough, you will learn how to:

* Handle malformed ELF headers and segment tricks
* Work with encrypted and obfuscated code (XOR and RC4)
* Navigate Binary Ninjaâs segment and section editing capabilities
* Use powerful selection and transformation features
* Understand the design decisions behind Binary Ninjaâs analysis heuristics
* Apply practical workflows for analyzing real-world malware and CTF challenges

## Letâs Get Into âTroubleâ

The Linux anti-RE book âteaches the reader how to code and analyze well known anti-reversing techniques for Linuxâ.
I particularly like the coding part because it gives the reader hands-on experience with the techniques discussed in the book.
It is a classic read but still relevant today. It covers many interesting techniques and is definitely worth [checking
out](https://leanpub.com/anti-reverse-engineering-linux).

As a Binary Ninja developer, I canât wait to see how our tool reacts to these tricks! Conveniently, at the end of the book, the author
created a binary that combines the techniques discussed throughout the book. It is called `trouble` and can be found on
[VirusTotal](https://www.virustotal.com/en/file/a39b83850757ca85a4ddd049226662ecf9f3644a29fb862ad27751b090a468b5/analysis/),
[MalShare](https://malshare.com/sample.php?action=detail&hash=a39b83850757ca85a4ddd049226662ecf9f3644a29fb862ad27751b090a468b5), or
[GitHub](https://github.com/Vector35/binja_blog_binaries/blob/main/linux_anti_re/a39b83850757ca85a4ddd049226662ecf9f3644a29fb862ad27751b090a468b5).

The author also shared the source code of the binary and the build script. As the
[README](https://github.com/antire-book/dont_panic) says, it is a password-protected bind shell. The task is to
analyze the binary and find out the password, which would grant you access to the shell.

*(The code was written in 2016 â if you wish to build it yourself, be prepared for some rough edges!)*

Let us see how much `trouble` it causes!

## First Obstacles: Malformed ELF Headers

The binary is an ELF and only 27KB in size, but it immediately looks unusual after we open it. We can see two entries in the Log window:

```
[BinaryView.ElfView] ELF endianness automatically overridden to little-endian for x86/x86_64 (header specified big-endian)
[BinaryView.ElfView] Section 2 has a size (0xfffffffffffffff6) larger than file size (0x68eb), skipping creation
```

The first line is a classic technique to defeat RE tools, though it has become a bit too popular in CTF challenges to be particularly novel anymore. The ELF header contains an `encoding` field that reports the binaryâs endianness. This byte can be altered so that the binary will be interpreted with the wrong endianness, causing parsing to fail. However, the program will still execute just fine because the Linux kernel does not reply on this field.

![ELF endianness byte](/blog/images/linux-anti-re/1.png)

On recent Binary Ninja builds (>= 5.3.8794), this is defeated automatically since the ELF parser recognizes this is an x86/x64 binary and must therefore be little-endian, despite the header reporting big-endian. This behavior is controlled by the setting `files.elf.overrideX86Endianness`, which is enabled by default. If you are using an older build, you simply need to patch the 5th byte of the binary and change its value to 0x1.

The second log message defeats an attempt to cause chaos by faking a huge section. As we can see from the memory map, the `.data` section is abnormally large, which could exhaust RAM if we blindly created a buffer to represent it. Luckily, it does not work because the section is larger than the binary itself. This heuristic has worked better than having an arbitrary value as the maximally allowed section size.

![Giant .data section](/blog/images/linux-anti-re/2.png)

Even with all these (and potentially more!) tricks defeated, the code still does not make sense. The UI navigates to
the `_init` function by default, and the HLIL is odd:

![Odd HLIL of _init](/blog/images/linux-anti-re/3.png)

Dropping to the disassembly and noting the address of the function, we can see it starts at the 1st byte of the ELF header â no wonder the code does not make sense! This turns out to be another anti-RE technique: the binary reports a fake init function at the start of the ELF. We simply need to press `U` to undefine it.

![_init function overlaps ELF header](/blog/images/linux-anti-re/4.png)

## Hidden Code: The Segment Gap Trick

Note that we still do not have any reasonable code to read yet! For cases like this, starting from the `_start` function is always a good idea since it will be the first instruction the binary executes. I double-clicked on the `_start` symbol from the symbols view, but the UI navigated to the middle of nowhere:

![Navigation To _start](/blog/images/linux-anti-re/5.png)

I thought it was a glitch and repeated the operation, but still got the same behavior. I had a closer look at the symbol and started to understand what was going on:

![_start In Symbols View](/blog/images/linux-anti-re/6.png)

The `_start` symbol is displayed with a lighter color because it is a bare symbol, and most importantly, its address
`0x405e9c` is not a valid address! Comparing it with the `Segments` in the `Memory Map` widget, we can see the segment
ends exactly at `0x405e9c`, cutting the bytes at the `_start` off.

![Segment Ends Before _start](/blog/images/linux-anti-re/7.png)

This is another technique commonly used in malware and CTF challenges. Letâs check how the segments are mapped. For the first segment, its data offset starts at 0x0 and ends at 0x5e9c. This means the segmentâs content is loaded from bytes 0x0-0x5e9c of the ELF file. For the second segment, it consumes bytes 0x5fe0-0x6200. The bytes 0x5e9c-0x5fe0 are not used. We can check their contents from the `Raw` view, and they look like valid instructions:

![Bytes At Start In The Raw View](/blog/images/linux-anti-re/8.png)

The binary is abusing the fact that when the OS loads the binary, it always does so at a page boundary, which is usually 4KB. So the bytes between 0x5e9c-0x5fe0 get mapped for free even though they are not technically in the range specified by the segment boundary. This makes the program execute just fine even though it looks malformed in Binary Ninja.

There are a couple of ways to fix it, but the easiest is to just add a new segment with the correct range:

![Add New Segment](/blog/images/linux-anti-re/9.png)

Now we can navigate to `_start` and we can see the bytes are correct:

![Bytes At _start Showing Up](/blog/images/linux-anti-re/10.png)

There is no function at the addr...