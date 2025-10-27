---
title: Sanitize your C++ containers: ASan annotations step-by-step
url: https://blog.trailofbits.com/2024/09/10/sanitize-your-c-containers-asan-annotations-step-by-step/
source: Trail of Bits Blog
date: 2024-09-11
fetch_date: 2025-10-06T18:27:15.196721
---

# Sanitize your C++ containers: ASan annotations step-by-step

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Sanitize your C++ containers: ASan annotations step-by-step

[Dominik Czarnota](https://x.com/disconnect3d_pl), Dominik Klemba

September 10, 2024

[application-security](/categories/application-security/), [llvm](/categories/llvm/)

AddressSanitizer (ASan) is a compiler plugin that helps detect memory errors like buffer overflows or use-after-frees. In this post, we explain how to equip your C++ code with ASan annotations to find more bugs. We also show our work on ASan in GCC and LLVM. In LLVM, Trail of Bits added annotations to the libc++ `std::string` and `std::deque` containers, enabled custom allocators for container annotations, and fixed bugs in libc++!

### Container overflows

As mentioned in our [“Understanding AddressSanitizer” blog post](https://blog.trailofbits.com/2024/05/16/understanding-addresssanitizer-better-memory-safety-for-your-code/), ASan cannot automatically detect invalid memory accesses into allocated memory. Instead, it provides an API for users to mark memory regions as accessible or inaccessible. The C++ standard libraries leverage those APIs to annotate STL containers, which helps ASan find [container overflow](https://github.com/google/sanitizers/wiki/AddressSanitizerContainerOverflow) bugs.

This is shown in action in figure 1, where we compile with ASan and no optimizations (`-O0 -fsanitize=address -D_GLIBCXX_SANITIZE_VECTOR` flags). This functionality is supported by both clang++ and g++. Also, if libc++ is used (`-stdlib=libc++`), the GLIBCXX macro can be omitted since libc++ (the LLVM’s C++ standard library) enables container annotations by default.

Figure 2 shows the result of running this code, where we can see that the invalid memory access was detected as a container-overflow error (since the shadow memory was poisoned with the “fc” byte).

```
#include <vector>
int main() {
    std::vector<char> v;

    // Set capacity to 8, the size remains 0
    v.reserve(8);

    // Access vector past its size, but before its capacity (8)
    return *(v.data());
}
```

Figure 1: [Example of container overflow detection](https://godbolt.org/#g:!((g:!((g:!((h:codeEditor,i:(filename:'1',fontScale:14,fontUsePx:'0',j:1,lang:c%2B%2B,selection:(endColumn:1,endLineNumber:12,positionColumn:1,positionLineNumber:12,selectionStartColumn:1,selectionStartLineNumber:12,startColumn:1,startLineNumber:12),source:'%23include+%3Cvector%3E%0A%0Aint+main()+%7B%0A++++std::vector%3Cchar%3E+v%3B%0A%0A++++//+Set+capacity+to+8%0A++++v.reserve(8)%3B%0A%0A++++//+Access+vector+past+its+size+(0)+but+before+its+capacity+(8)+%0A++++return+*(v.data())%3B%0A%7D%0A'),l:'5',n:'1',o:'C%2B%2B+source+%231',t:'0')),k:37.70984875273814,l:'4',n:'0',o:'',s:0,t:'0'),(g:!((h:executor,i:(argsPanelShown:'1',compilationPanelShown:'0',compiler:g141,compilerName:'',compilerOutShown:'0',execArgs:'',execStdin:'',fontScale:14,fontUsePx:'0',j:1,lang:c%2B%2B,libs:!(),options:'-O0+-fsanitize%3Daddress+-D_GLIBCXX_SANITIZE_VECTOR',overrides:!(),runtimeTools:!(),source:1,stdinPanelShown:'1',wrap:'1'),l:'5',n:'0',o:'Executor+x86-64+gcc+14.1+(C%2B%2B,+Editor+%231)',t:'0')),k:26.785748471824373,l:'4',n:'0',o:'',s:0,t:'0'),(g:!((h:executor,i:(argsPanelShown:'1',compilationPanelShown:'0',compiler:clang1701,compilerName:'',compilerOutShown:'0',execArgs:'',execStdin:'',fontScale:14,fontUsePx:'0',j:2,lang:c%2B%2B,libs:!(),options:'-O0+-fsanitize%3Daddress+-stdlib%3Dlibc%2B%2B',overrides:!(),runtimeTools:!(),source:1,stdinPanelShown:'1',wrap:'1'),l:'5',n:'0',o:'Executor+x86-64+clang+17.0.1+(C%2B%2B,+Editor+%231)',t:'0')),k:35.504402775437484,l:'4',n:'0',o:'',s:0,t:'0')),l:'2',n:'0',o:'',t:'0')),version:4) (Note: we do not show MSVC on CompilerExplorer since it does not have [ASan installed yet](https://github.com/compiler-explorer/compiler-explorer/issues/6662))

```
==1==ERROR: AddressSanitizer: container-overflow on address 0x502000000010 at pc
0x000000401315 bp 0x7ffdd7e0c670 sp 0x7ffdd7e0c668
READ of size 1 at 0x502000000010 thread T0
    #0 0x401314 in main /app/example.cpp:10
    #1 0x7a47d5229d8f  (/lib/x86_64-linux-gnu/libc.so.6+0x29d8f)
    #2 0x7a47d5229e3f in __libc_start_main (/lib/x86_64-linux-gnu/libc.so.6+0x29e3f)
    #3 0x401174 in _start (/app/output.s+0x401174)
…

Shadow bytes around the buggy address:
=>0x502000000000: fa fa[fc]fa fa fa fa fa fa fa fa fa fa fa fa fa

Shadow byte legend (one shadow byte represents 8 application bytes):
  Container overflow:      fc
```

Figure 2: ASan detecting the bug from figure 1. The output is truncated to show only relevant information.

However, the C++ standard libraries have varying levels of support for detecting container overflows. The table below summarizes current support for this detection.

| **Library** | **Annotated containers** | **Comment** |
| --- | --- | --- |
| libstdc++ (GCC) | `std::vector` ([GCC 8](https://gcc.gnu.org/gcc-8/changes.html#:~:text=AddressSanitizer%20integration%20for%20std%3A%3Avector%2C%20detecting%20out%2Dof%2Drange%20accesses%20to%20the%20unused%20capacity%20of%20a%20vector.)) | Requires `-D_GLIBCXX_SANITIZE_VECTOR` macro during compilation. For `std::string` and `std::deque`, see the “GCC / libstdc++ annotations” section below. |
| libc++ (LLVM) | `std::vector` ([LLVM 3.5](https://github.com/llvm/llvm-project/commit/5c520bd985ee51472d2396fe28a3ef8b30eb5a6c)), `std::deque` (LLVM17), long `std::string` (LLVM18), short `std::string` (not yet released) | Container annotations are enabled by default. Can be disabled with environment variable `ASAN_OPTIONS=detect_container_overflow=0` (does not require recompilation) |
| msvc++ | `std::vector` and `std::string` ([Visual Studio 2022 17.2 and 17.6](https://learn.microsoft.com/en-us/cpp/sanitizers/error-container-overflow?view=msvc-170)) | Container annotations are enabled by default. Can be disabled with `-D_DISABLE_VECTOR_ANNOTATION -D_DISABLE_STRING_ANNOTATION`. |

### AddressSanitizer API

The recommended way to annotate memory is using the `ASAN_POISON_MEMORY_REGION(addr, size)` and `ASAN_UNPOISON_MEMORY_REGION(addr, size)` macros, which set the appropriate values in shadow memory. (If ASan is not enabled during compilation, then those macros only evaluate their arguments without calling annotation functions).

As shown in figure 3, we can find more details on using the `ASAN_POISON_MEMORY_REGION` macro by reading the docstring of the underlying `_asan_poison_memory_region` function.

```
/// Marks a memory region ([addr, addr+size)) as unaddressable.
///
/// This memory must be previously allocated by your program. Instrumented
/// code is forbidden from accessing addresses in this region until it is
/// unpoisoned. This function is not guaranteed to poison the entire region -
/// it could poison only a subregion of [addr, addr+size) due to ASan
/// alignment restrictions.
///
/// \note This function is not thread-safe because no two threads can poison or
/// unpoison memory in the same memory region simultaneously.
///
/// \param addr Start of memory region.
/// \param size Size of memory region.
void __asan_poison_memory_region(void const volatile *addr, size_t size);
```

Figure 3: [A comment describing \_\_asan\_poison\_memory\_region](https://github.com/gcc-mirror/gcc/blob/8637aecd5aea70bb13c08b5b96d3cb24f5afcead/libsanitizer/include/sanitizer/asan_interface.h#L21-L34)

Apart from those macros, the [asan\_interface.h](https://github.com/llvm/llvm-project/blob/1b7285bf3ee73975fa63acfc5301a9b57a53fca2/compiler-rt/include/sanitizer/asan_interface.h) file provides functions that allow for customizing the value set in shadow memory and helping with annotating certain containers, such as the `__sanitizer_annotate_contiguous_container` and `__sanitizer_annotate_double_ended_contiguous_container` functions. The documentation for the former function is shown in figure 4.

```
/// \note  Use this function with caution ...