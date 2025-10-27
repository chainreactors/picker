---
title: View and analyze Electron crashes on macOS
url: http://bugs.cc/posts/view-and-analyze-electron-crashes-on-macos/
source: Kevin Cui's Blog
date: 2024-10-16
fetch_date: 2025-10-06T18:53:51.101591
---

# View and analyze Electron crashes on macOS

[# Kevin Cui's Blog](/)[Home](/)
[Posts](/posts/)
[Docs](https://docs.bugs.cc)
[RSS](https://bugs.cc/index.xml)
[zh-CN 🇨🇳](/zh/posts/view-and-analyze-electron-crashes-on-macos/)

# View and analyze Electron crashes on macOS

2024-10-15

When developing an Electron application, you might encounter crashes. However, for various reasons, the application may not have integrated Sentry or other crash analysis platforms. In such cases, you need to manually check the crash logs to identify the issue.

## [Locating Local Crash Logs](#locating-local-crash-logs)

Since Electron is based on Chromium, the crash-related operations are largely consistent with Chromium.

In the [Chromium crash-reports](https://www.chromium.org/developers/crash-reports/#on-mac), we can see that crash files are stored in the `~/Library/Application\ Support/Chromium/Crashpad/completed` directory. However, since we are using an Electron application and there is no “submission” process, the crash files are kept in the `~/Library/Application\ Support/Chromium/Crashpad/pending` directory.

Before searching, remember to replace `Chromium` in the above directories with your application name, such as `OOMOL Studio`.

If you have encountered many crashes, you’ll find numerous \*.dmp files in this directory. Generally, we only need to analyze the most recent crash, so the latest file is the one we require.

## [Analyzing Crash Files](#analyzing-crash-files)

### [Using `breakpad`](#using-breakpad)

breakpad is an open-source crash analysis tool developed by Google, specifically for Chromium. We can use this tool to analyze our *dmp* files.

```
git clone https://chromium.googlesource.com/breakpad/breakpad
cd breakpad
./configure
make
# Optional
make install
```

After executing the above command, you can parse the dmp using `./src/processor/minidump_stackwalk`, or you can directly use `minidump_stackwalk` (if you executed `make install`).

The basic usage method is:

```
minidump_stackwalk /path/to/your.dmp [/path/to/symbols]
```

If you use `minidump_stackwalk /path/to/your.dmp`, the output you get will only be addresses, and you won’t be able to see the function names. Therefore, we need to provide a symbol file in order to see the function names.

You can download the symbol file by running: `wget https://github.com/electron/electron/releases/download/<ELECTEON_VERSION>/electron-<ELECTEON_VERSION>-darwin-arm64-symbols.zip`. For my own case, I downloaded:

```
wget https://github.com/electron/electron/releases/download/v30.5.1/electron-v30.5.1-darwin-arm64-symbols.zip
```

This file is specifically prepared for `breakpad`, so we can directly unzip it to a certain directory and then use that directory as a parameter to pass to `minidump_stackwalk`.

```
minidump_stackwalk ./0c6d2547-6694-4109-b82e-cc3e6331885f.dmp ./electron-v30.5.1-darwin-arm64-symbols/breakpad_symbols
```

Next, you will be able to see the detailed crash information. In my case, the result I got is:

```
Operating system: Mac OS X
                  14.6.1 23G93
CPU: arm64
     12 CPUs

GPU: UNKNOWN

Crash reason:  EXC_BREAKPOINT / 0x00000001
Crash address: 0x1129666c8
Process uptime: 0 seconds

Thread 0 (crashed)
 0  Electron Framework!v8::base::OS::Abort() [platform-posix.cc : 699 + 0x0]
     x0 = 0x0000000000000000    x1 = 0x0000000000000000
     x2 = 0x00000000000120a8    x3 = 0x00000001117656e0
     x4 = 0x00000001804b5a5f    x5 = 0x000000016b046af0
     x6 = 0x000000000000000a    x7 = 0x0000000000000000
     x8 = 0x0000000000000001    x9 = 0x00000001e83ff610
    x10 = 0x0000000000000002   x11 = 0x00000000fffffffd
    x12 = 0x0000010000000000   x13 = 0x0000000000000000
    x14 = 0x0000000000000000   x15 = 0x0000000000000000
    x16 = 0x00000001805657d4   x17 = 0x00000001f2af63e0
    x18 = 0x0000000000000000   x19 = 0x0000013c002cf000
    x20 = 0x0000000115675980   x21 = 0x0000013c002c0000
    x22 = 0x000000016b04fc28   x23 = 0x000000000000ded0
    x24 = 0x000000016b04fd0e   x25 = 0x000000016b047448
    x26 = 0x0000000000010820   x27 = 0x000000000000e838
    x28 = 0x0000013c002d0540    fp = 0x000000016b0473e0
     lr = 0x000000011295e6ec    sp = 0x000000016b0473e0
     pc = 0x00000001129666c8
    Found by: given as instruction pointer in context
 1  Electron Framework!v8::base::FatalOOM(v8::base::OOMType, char const*) [logging.cc : 94 + 0x0]
    x19 = 0x0000013c002cf000   x20 = 0x0000000115675980
    x21 = 0x0000013c002c0000   x22 = 0x000000016b04fc28
    x23 = 0x000000000000ded0   x24 = 0x000000016b04fd0e
    x25 = 0x000000016b047448   x26 = 0x0000000000010820
    x27 = 0x000000000000e838   x28 = 0x0000013c002d0540
     fp = 0x000000016b047400    sp = 0x000000016b0473f0
     pc = 0x000000011295e6ec
    Found by: call frame info
 2  Electron Framework!v8::Utils::ReportOOMFailure(v8::internal::Isolate*, char const*, v8::OOMDetails const&) [api.cc : 341 + 0x0]
    x19 = 0x0000013c002cf000   x20 = 0x0000000115675980
    x21 = 0x0000013c002c0000   x22 = 0x000000016b04fc28
    x23 = 0x000000000000ded0   x24 = 0x000000016b04fd0e
    x25 = 0x000000016b047448   x26 = 0x0000000000010820
    x27 = 0x000000000000e838   x28 = 0x0000013c002d0540
     fp = 0x000000016b047420    sp = 0x000000016b047410
     pc = 0x000000010f5c66f4
    Found by: call frame info
 3  Electron Framework!v8::internal::V8::FatalProcessOutOfMemory(v8::internal::Isolate*, char const*, v8::OOMDetails const&) [api.cc : 301 + 0xc]
    x19 = 0x0000000115e75e8d   x20 = 0x0000000115675980
    x21 = 0x0000013c002c0000   x22 = 0x000000016b04fc28
    x23 = 0x000000000000ded0   x24 = 0x000000016b04fd0e
    x25 = 0x000000016b047448   x26 = 0x0000000000010820
    x27 = 0x000000000000e838   x28 = 0x0000013c002d0540
     fp = 0x000000016b050150    sp = 0x000000016b047430
     pc = 0x000000010f5c6638
    Found by: call frame info
 4  Electron Framework!v8::internal::(anonymous namespace)::InitProcessWideCodeRange(v8::PageAllocator*, unsigned long) [code-range.cc : 458 + 0x14]
    x19 = 0x0000013c000c1a40   x20 = 0x0000000010000000
    x21 = 0x0000013c000c1a80   x22 = 0x0000013c002cf2d8
    x23 = 0x0000000000000000   x24 = 0x0000000000000000
    x25 = 0x0000013c002c0110   x26 = 0x0000000000010820
    x27 = 0x000000000000e838   x28 = 0x0000013c002d0540
     fp = 0x000000016b050180    sp = 0x000000016b050160
     pc = 0x000000010f71ce70
    Found by: call frame info
 5  Electron Framework!v8::base::CallOnceImpl(std::__Cr::atomic<unsigned char>*, std::__Cr::function<void ()>) [function.h : 428 + 0x8]
    x19 = 0x0000000116de0e90   x20 = 0x0000013c000d0b40
    x21 = 0x0000013c002cdec0   x22 = 0x0000013c002cf2d8
    x23 = 0x0000000000000000   x24 = 0x0000000000000000
    x25 = 0x0000013c002c0110   x26 = 0x0000000000010820
    x27 = 0x000000000000e838   x28 = 0x0000013c002d0540
     fp = 0x000000016b0501a0    sp = 0x000000016b050190
     pc = 0x0000000112962d28
    Found by: call frame info
 6  Electron Framework!v8::internal::CodeRange::EnsureProcessWideCodeRange(v8::PageAllocator*, unsigned long) [once.h : 101 + 0x10]
    x19 = 0x000000016b0501b8   x20 = 0x0000013c000d0b40
    x21 = 0x0000013c002cdec0   x22 = 0x0000013c002cf2d8
    x23 = 0x0000000000000000   x24 = 0x0000000000000000
    x25 = 0x0000013c002c0110   x26 = 0x0000000000010820
    x27 = 0x000000000000e838   x28 = 0x0000013c002d0540
     fp = 0x000000016b0501f0    sp = 0x000000016b0501b0
     pc = 0x000000010f71cd64
    Found by: call frame info
 7  Electron Framework!v8::internal::Heap::SetUp(v8::internal::LocalHeap*) [heap.cc : 5530 + 0x4]
    x19 = 0x0000013c002cded0   x20 = 0x0000000010000000
    x21 = 0x0000013c002cdec0   x22 = 0x0000013c002cf2d8
    x23 = 0x0000000000000000   x24 = 0x0000000000000000
    x25 = 0x0000013c002c0110   x26 = 0x0000000000010820
    x27 = 0x000000000000e838   x28 = 0x0000013c002d0540
     fp = 0x000000016b0502a0    sp = 0x000000016b050200
     pc = 0x000000010f791418
    Found by: call frame info
 8  Electron Framework!v8::internal::Isolate::Init(v8::internal::SnapshotData*, v8::intern...