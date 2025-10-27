---
title: Typos that omit security features and how to test for them
url: https://blog.trailofbits.com/2023/04/20/typos-that-omit-security-features-and-how-to-test-for-them/
source: Trail of Bits Blog
date: 2023-04-21
fetch_date: 2025-10-04T11:33:41.160108
---

# Typos that omit security features and how to test for them

[The Trail of Bits Blog](/ "The Trail of Bits Blog")

[![Trail of Bits Logo](/img/tob.png)](https://trailofbits.com "Trail of Bits")

# Typos that omit security features and how to test for them

[Dominik Czarnota](https://x.com/disconnect3d_pl)

April 20, 2023

[audits](/categories/audits/), [mitigations](/categories/mitigations/)

During a security audit, I discovered an easy-to-miss typo that unintentionally failed to enable \_FORTIFY\_SOURCE, which helps detect memory corruption bugs in incorrectly used C functions. We searched, found, and fixed twenty C and C++ bugs on GitHub with this same pattern. Here is a list of some of them related to this typo:

* [microsoft/binskim#777](https://github.com/microsoft/binskim/pull/777)
* [PowerShell/PowerShell-Native#88](https://github.com/PowerShell/PowerShell-Native/pull/88)
* [apple-open-source/macos#3](https://github.com/apple-open-source/macos/pull/3): Though this is an unofficial fork, so I reported this further in [Apple’s Feedback Assistant](https://feedbackassistant.apple.com/)
* [trailofbits/cb-multios#96](https://github.com/trailofbits/cb-multios/pull/96) (Yeah, we also had this issue!)
* [lavabit/libdime#49](https://github.com/lavabit/libdime/pull/49)
* [lavabit/magma#155](https://github.com/lavabit/magma/pull/155)
* [Jackysi/advancedtomato#454](https://github.com/Jackysi/advancedtomato/pull/454)
* [adaptivecomputing/torque#474](https://github.com/adaptivecomputing/torque/pull/474)
* [gstrauss/mcdb#14](https://github.com/gstrauss/mcdb/pull/14)
* [Homegear/Homegear#364](https://github.com/Homegear/Homegear/pull/364)
* [sergey-dryabzhinsky/dedupsqlfs#235](https://github.com/sergey-dryabzhinsky/dedupsqlfs/pull/235)
* [randlabs/algorand-windows-node#5](https://github.com/randlabs/algorand-windows-node/pull/5)
* [rpodgorny/unionfs-fuse#131](https://github.com/rpodgorny/unionfs-fuse/pull/131)
* [cgaebel/pipe#15](https://github.com/cgaebel/pipe/pull/15)
* [jkrh/kvms#48](https://github.com/jkrh/kvms/pull/48)
* [angaza/nexus-embedded#8](https://github.com/angaza/nexus-embedded/pull/8)
* [hashbang/book#24](https://github.com/hashbang/book/pull/24)

We’ll show you how to test your code to avoid this issue that could make it easier to exploit bugs.

## How source fortification works

The source fortification is a security mitigation that replaces certain function calls with more secure wrappers that perform additional runtime or compile-time checks.

Source fortification is enabled by defining a special macro, “\_FORTIFY\_SOURCE=”, with a value of 1, 2, or 3 and [compiling a program with optimizations](https://github.com/bminor/glibc/blob/c923cd8c496c7f253f327361a65c737233c7ebbd/include/features.h#L411-L412). The higher the value, the more functions fortified or checks performed. Also, the libc library and compiler must support the source fortification option, which is the case for glibc, Apple Libc, gcc, and LLVM/Clang, but not [musl libc](https://wiki.musl-libc.org/roadmap.html#:~:text=Enhanced%20LSB/glibc%20ABI%2Dcompat%2C%20especially%20fortify%20__*_chk%20symbols) and [uClibc-ng](https://elixir.bootlin.com/uclibc-ng/v1.0.42/source/include/features.h#L213). The implementation specifics may also vary. For example, level value 3 was only recently added in [glibc 2.34](https://developers.redhat.com/articles/2022/09/17/gccs-new-fortification-level), but it does not seem to be available in [Apple Libc](https://github.com/apple-oss-distributions/Libc/blob/Libc-1534.40.2/include/secure/_common.h).

The following example shows source fortification in action. Whether or not we enable the mitigation, the resulting binary will call either the strcpy function or its `__strcpy_chk` wrapper:

[![](/img/wpdump/019c18ef460eef3193065b6fc922461b.jpg)](/img/wpdump/019c18ef460eef3193065b6fc922461b.jpg)

*Figure 1: [Compiler Explorer](https://godbolt.org/#g:!((g:!((g:!((h:codeEditor,i:(filename:'1',fontScale:17,fontUsePx:'0',j:1,lang:c%2B%2B,selection:(endColumn:24,endLineNumber:5,positionColumn:24,positionLineNumber:5,selectionStartColumn:24,selectionStartLineNumber:5,startColumn:24,startLineNumber:5),source:'%23include+%3Cstring.h%3E%0A%0Aint+main(int+c,+char*+argv%5B%5D)+%7B%0A++char+buf%5B10%5D%3B%0A++strcpy(buf,+argv%5B0%5D)%3B%0A%7D'),l:'5',n:'0',o:'C%2B%2B+source+%231',t:'0')),k:23.529370801505742,l:'4',m:17.92452830188679,n:'0',o:'',s:0,t:'0'),(g:!((h:compiler,i:(compiler:g122,deviceViewOpen:'1',filters:(b:'0',binary:'1',commentOnly:'0',demangle:'0',directives:'0',execute:'0',intel:'0',libraryCode:'0',trim:'1'),flagsViewOpen:'1',fontScale:16,fontUsePx:'0',j:5,lang:c%2B%2B,libs:!(),options:'-O2',selection:(endColumn:24,endLineNumber:7,positionColumn:24,positionLineNumber:7,selectionStartColumn:24,selectionStartLineNumber:7,startColumn:24,startLineNumber:7),source:1),l:'5',n:'0',o:'+x86-64+gcc+12.2+(Editor+%231)',t:'0')),header:(),l:'4',m:25.39308176100629,n:'0',o:'',s:0,t:'0'),(g:!((h:compiler,i:(compiler:g122,deviceViewOpen:'1',filters:(b:'0',binary:'1',commentOnly:'0',demangle:'0',directives:'0',execute:'0',intel:'0',libraryCode:'0',trim:'1'),flagsViewOpen:'1',fontScale:16,fontUsePx:'0',j:1,lang:c%2B%2B,libs:!(),options:'-D_FORTIFY_SOURCE%3D2+-O2',selection:(endColumn:6,endLineNumber:1,positionColumn:6,positionLineNumber:1,selectionStartColumn:6,selectionStartLineNumber:1,startColumn:6,startLineNumber:1),source:1),l:'5',n:'0',o:'+x86-64+gcc+12.2+(Editor+%231)',t:'0')),header:(),l:'4',m:56.68238993710691,n:'0',o:'',s:0,t:'0')),k:100,l:'3',n:'0',o:'',t:'0')),version:4) comparison of the assembly generated by the compiler.*In this case, the `__strcpy_chk` wrapper function is implemented by glibc ([source](https://github.com/bminor/glibc/blob/48b74865c63840b288bd85b4d8743533b73b339b/debug/strcpy_chk.c#L24-L33)):

```
/* Copy SRC to DEST and check DEST buffer overflow*/
char * __strcpy_chk (char *dest, const char *src, size_t destlen) {
    size_t len = strlen (src);
    if (len >= destlen)
    __chk_fail ();
    return memcpy (dest, src, len + 1);
}
```

*Figure 2: The `__strcpy_chk` function from glibc*As we can see, the wrapper takes one more argument—the destination buffer size—and then checks if the length of the source is bigger than the destination. If it is, the wrapper calls the `__chk_fail` function, which aborts the process. Figure 1 shows that the compiled code passes the correct length of the dest destination buffer in the `mov edx, 10` instruction.

## Tpying is hard

Since a preprocessor macro determines source fortification, a typo in the macro spelling effectively disables it, and neither the libc nor the compiler catches this issue, unlike typos made in other security hardening options enabled with compiler flags instead of macros.

Effectively, if you pass in “`-DFORTIFY_SOURCE=2 -O2`” instead of “`-D_FORTIFY_SOURCE=2 -O2`” to the compiler, the source fortification won’t be enabled, and the wrapper functions will not be used:

[![](/img/wpdump/31c19649e6672cc80168637b1b61a60f.jpg)](/img/wpdump/31c19649e6672cc80168637b1b61a60f.jpg)

*Figure 3: Assembly when making a typo in the \_FORTIFY\_SOURCE macro (created with [Compiler Explorer](https://godbolt.org/#g:!((g:!((g:!((h:codeEditor,i:(filename:'1',fontScale:17,fontUsePx:'0',j:1,lang:c%2B%2B,selection:(endColumn:2,endLineNumber:6,positionColumn:2,positionLineNumber:6,selectionStartColumn:2,selectionStartLineNumber:6,startColumn:2,startLineNumber:6),source:'%23include+%3Cstring.h%3E%0A%0Avoid+example(char*+source)+%7B%0A++char+dest%5B10%5D%3B%0A++strcpy(dest,+source)%3B%0A%7D'),l:'5',n:'0',o:'C%2B%2B+source+%231',t:'0')),k:23.529370801505742,l:'4',m:13.827545152240196,n:'0',o:'',s:0,t:'0'),(g:!((h:compiler,i:(compiler:g122,deviceViewOpen:'1',filters:(b:'0',binary:'1',commentOnly:'0',demangle:'0',directives:'0',execute:'0',intel:'0',libraryCode:'0',trim:'1'),flagsViewOpen:'1',fontScale:16,fontUsePx:'0',j:5,lang:c%2B%2B,libs:!(),options:'-DFORTIFY_SOURCE%3D2+-O2',selection:(endColumn:1,endLineNumber:1,positionColumn:1,positionLineNumber:1,selectionStart...