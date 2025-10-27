---
title: Understanding AddressSanitizer: Better memory safety for your code
url: https://blog.trailofbits.com/2024/05/16/understanding-addresssanitizer-better-memory-safety-for-your-code/
source: Trail of Bits Blog
date: 2024-05-17
fetch_date: 2025-10-06T17:15:47.191780
---

# Understanding AddressSanitizer: Better memory safety for your code

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Understanding AddressSanitizer: Better memory safety for your code

[Dominik Czarnota](https://x.com/disconnect3d_pl), Dominik Klemba

May 16, 2024

[application-security](/categories/application-security/), [compilers](/categories/compilers/), [fuzzing](/categories/fuzzing/), [llvm](/categories/llvm/), [memory-safety](/categories/memory-safety/)

This post will guide you through using [AddressSanitizer (ASan)](https://github.com/google/sanitizers/wiki/AddressSanitizer), a compiler plugin that helps developers detect [memory issues](https://media.defense.gov/2022/Nov/10/2003112742/-1/-1/0/CSI_SOFTWARE_MEMORY_SAFETY.PDF) in code that can lead to remote code execution attacks (such as [WannaCry](https://en.wikipedia.org/wiki/WannaCry_ransomware_attack) or [this WebP implementation bug](https://www.theregister.com/2023/09/12/chrome_browser_webp_exploit/)). ASan inserts checks around memory accesses during compile time, and crashes the program upon detecting improper memory access. It is widely used during fuzzing due to its ability to detect bugs missed by unit testing and its [better performance compared to other similar tools](https://developers.redhat.com/blog/2021/05/05/memory-error-checking-in-c-and-c-comparing-sanitizers-and-valgrind).

ASan was designed for C and C++, but it can also be used with [Objective-C](https://developer.apple.com/documentation/xcode/diagnosing-memory-thread-and-crash-issues-early), [Rust](https://doc.rust-lang.org/beta/unstable-book/compiler-flags/sanitizer.html), [Go](https://tip.golang.org/doc/go1.18#go-build-asan), and [Swift](https://developer.apple.com/documentation/xcode/diagnosing-memory-thread-and-crash-issues-early). This post will focus on C++ and demonstrate how to use ASan, explain its error outputs, explore implementation fundamentals, and discuss ASan’s limitations and common mistakes, which will help you grasp previously undetected bugs.

Finally, we share a concrete example of a real bug we encountered during an audit that was missed by ASan and can be detected with our changes. This case motivated us to research ASan bug detection capabilities and contribute dozens of upstreamed commits to the [LLVM](https://llvm.org/) project. These commits resulted in the following changes:

* Extended container sanitization ASan API in LLVM16 by [adding support for unaligned memory buffers](https://github.com/llvm/llvm-project/commit/dd1b7b797a116eed588fd752fbe61d34deeb24e4) and [adding a function for double-ended contiguous containers](https://github.com/llvm/llvm-project/commit/1c5ad6d2c01294a0decde43a88e9c27d7437d157). Thanks to that, since LLVM17, [`std::vector` annotations work with all allocators by default](https://github.com/llvm/llvm-project/commit/c08d4ad25cf3f335e9b2e7b1b149eb1b486868f1).
* Added [`std::deque` annotations](https://github.com/llvm/llvm-project/commit/10ec9276d40024c23a481e6671dad1521151dd85) in LLVM17. For details, check the [libc++ 17 release notes](https://releases.llvm.org/17.0.1/projects/libcxx/docs/ReleaseNotes/17.html).
* Added annotations for the [long string case of `std::string`](https://github.com/llvm/llvm-project/pull/72677) in LLVM18 (with all [allocators by default](https://github.com/llvm/llvm-project/pull/75845)). Check the [libc++18 release notes](https://libcxx.llvm.org/ReleaseNotes/18.html) for more details.
* We have recently upstreamed [short string annotations](https://github.com/llvm/llvm-project/pull/79536) (read about “[short string optimization](https://stackoverflow.com/questions/21694302/what-are-the-mechanics-of-short-string-optimization-in-libc)”), and there is a high probability that they will be included in libc++19, assuming no new concerns or issues arise. Keep an eye on the [libc++19 release notes](https://libcxx.llvm.org/ReleaseNotes/19.html).

### Getting started with ASan

ASan can be enabled in LLVM’s Clang and GNU GCC compilers by using the `-fsanitize=address` compiler and linker flag. The Microsoft Visual C++ (MSVC) compiler supports it via the [`/fsanitize=address` option](https://learn.microsoft.com/en-us/cpp/build/reference/fsanitize?view=msvc-170). Under the hood, the program’s memory accesses will be instrumented with ASan checks and the program will be linked with ASan runtime libraries. As a result, when a memory error is detected, the program will stop and provide information that may help in diagnosing the cause of memory corruption.

AddressSanitizer’s approach differs from other tools like [Valgrind](https://valgrind.org/), which may be used without rebuilding a program from its source, but has [bigger performance overhead (20x vs 2x) and may detect fewer bugs](https://github.com/google/sanitizers/wiki/AddressSanitizerComparisonOfMemoryTools).

### Simple example: detecting out-of-bounds memory access

Let’s see ASan in practice on a simple buggy C++ program that reads data from an array out of its bounds. Figure 1 shows the code of such a program, and figure 2 shows its compilation, linking, and output when running it, including the error detected by ASan. Note that the program was compiled with debugging symbols and no optimizations ([`-g3` and `-O0` flags](https://gcc.gnu.org/onlinedocs/gcc/Debugging-Options.html)) to make the ASan output more readable.

```
  1    #include <iostream>
  2
  3    void out_of_bounds(char const *buf) {
  4       for (int i = 0; i <= 4; ++i)
  5          std::cout << "buf[" << i << "] = " << buf[i] << std::endl;
  6    }
  7
  8    int main() {
  9       char *buf = new char[4]{"Hey"};
 10       out_of_bounds(buf);
 11    }
```

Figure 1: [Example program](https://godbolt.org/#g:!((g:!((g:!((h:codeEditor,i:(filename:'1',fontScale:14,fontUsePx:'0',j:1,lang:c%2B%2B,selection:(endColumn:1,endLineNumber:15,positionColumn:1,positionLineNumber:15,selectionStartColumn:1,selectionStartLineNumber:15,startColumn:1,startLineNumber:15),source:'%23include+%3Ciostream%3E%0A%23include+%3Ccstring%3E%0A%0A%0Avoid+out_of_bounds(char+const+*buf)+%7B%0A+++for+(int+i+%3D+0%3B+i+%3C%3D+4%3B+%2B%2Bi)%0A++++++std::cout+%3C%3C+%22buf%5B%22+%3C%3C+i+%3C%3C+%22%5D+%3D+%22+%3C%3C+buf%5Bi%5D+%3C%3Cstd::endl%3B%0A%7D%0A%0A%0Aint+main()+%7B%0A+++char+*buf+%3D+new+char%5B4%5D%7B%22Hey%22%7D%3B%0A+++out_of_bounds(buf)%3B%0A%7D%0A'),l:'5',n:'0',o:'C%2B%2B+source+%231',t:'0')),k:50,l:'4',m:100,n:'0',o:'',s:0,t:'0'),(g:!((h:executor,i:(argsPanelShown:'1',compilationPanelShown:'0',compiler:clang1701,compilerName:'',compilerOutShown:'0',execArgs:'',execStdin:'',fontScale:14,fontUsePx:'0',j:1,lang:c%2B%2B,libs:!(),options:'-fsanitize%3Daddress+-O0+-g3',overrides:!(),runtimeTools:!(),source:1,stdinPanelShown:'1',wrap:'1'),l:'5',n:'0',o:'Executor+x86-64+clang+17.0.1+(C%2B%2B,+Editor+%231)',t:'0')),header:(),k:50,l:'4',n:'0',o:'',s:0,t:'0')),l:'2',n:'0',o:'',t:'0')),version:4) that has an out-of-bounds bug on the stack since it reads the fifth item from the buf array while it has only 4 elements (example.cpp)

```
$ clang++ -fsanitize=address -O0 -g3 ./example.cpp
$ ./a.out
buf[0] = H
buf[1] = e
buf[2] = y
buf[3] =
Program stderr
=================================================================
==1==ERROR: AddressSanitizer: heap-buffer-overflow on address 0x502000000014 at pc
0x5591ad37f523 bp 0x7ffe6acc8e70 sp 0x7ffe6acc8e68
READ of size 1 at 0x502000000014 thread T0
    #0 0x5591ad37f522 in out_of_bounds(char const*) /app/example.cpp:5:45
    #1 0x5591ad37f59a in main /app/example.cpp:10:4
    #2 0x7f8882a29d8f  (/lib/x86_64-linux-gnu/libc.so.6+0x29d8f) (BuildId:
c289da5071a3399de893d2af81d6a30c62646e1e)
    #3 0x7f8882a29e3f in __libc_start_main
(/lib/x86_64-linux-gnu/libc.so.6+0x29e3f) (BuildId:
c289da5071a3399de893d2af81d6a30c62646e1e)
    #4 0x5591ad2a4324 in _start (/app/output.s+0x2c324)
```

Figure 2: Running the program from figure 1 with ASan

When ASan detects a bug, it prints out a best guess of the e...