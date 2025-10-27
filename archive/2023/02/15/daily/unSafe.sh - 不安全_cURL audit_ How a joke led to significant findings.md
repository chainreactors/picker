---
title: cURL audit: How a joke led to significant findings
url: https://buaq.net/go-149374.html
source: unSafe.sh - 不安全
date: 2023-02-15
fetch_date: 2025-10-04T06:36:06.966669
---

# cURL audit: How a joke led to significant findings

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

![](https://8aqnet.cdn.bcebos.com/a1bcd3fcf2f4c3cf2549d036f6bb245b.jpg)

cURL audit: How a joke led to significant findings

By Maciej DomanskiIn fall 2022, Trail of Bits audited cURL, a widely-used comman
*2023-2-14 21:0:14
Author: [blog.trailofbits.com(查看原文)](/jump-149374.htm)
阅读量:26
收藏*

---

***By Maciej Domanski***

In fall 2022, Trail of Bits audited cURL, a widely-used command-line utility that transfers data between a server and supports various protocols. The project coincided with a Trail of Bits maker week, which meant that we had more manpower than we usually do, allowing us to take a nonstandard approach to the audit.

While discussing the threat model of the application, one of our team members jokingly asked, “Have we tried `curl AAAAAAAAAA…` yet”? Although the comment was made in jest, it sparked an idea: we should fuzz cURL’s command-line interface (CLI). Once we did so, the fuzzer quickly uncovered memory corruption bugs, specifically use-after-free issues, double-free issues, and memory leaks. Because the bugs are in libcurl, a cURL development library, they have the potential to affect the many software applications that use libcurl. This blog post describes how we found the following vulnerabilities:

* [CVE-2022-42915](https://curl.se/docs/CVE-2022-42915.html) – Double free when using HTTP proxy with specific protocols. Fixed in [cURL 7.86.0](https://curl.se/changes.html#7_86_0)
* [CVE-2022-43552](https://curl.se/docs/CVE-2022-43552.html) – Use-after-free when HTTP proxy denies tunneling SMB/TELNET protocols. Fixed in [cURL 7.87.0](https://curl.se/changes.html#7_87_0)
* [TOB-CURL-10](https://gist.github.com/bagder/6be7df7ea5ce17ca7f6ab0981de12f13#use-after-free-while-using-parallel-option-and-sequences-tob-curl-10) – Use-after-free while using parallel option and sequences. Fixed in [cURL 7.86.0](https://curl.se/changes.html#7_86_0)
* [TOB-CURL-11](https://gist.github.com/bagder/6be7df7ea5ce17ca7f6ab0981de12f13#memory-leaks-tob-curl-11) – Unused memory blocks are not freed, resulting in memory leaks. Fixed in [cURL 7.87.0](https://curl.se/changes.html#7_87_0)

## Working with cURL

cURL is continuously fuzzed by the OSS-Fuzz project, and its harnesses are developed in the separate [curl-fuzzer](https://github.com/curl/curl-fuzzer) GitHub repository. When I consulted the `curl-fuzzer` repository to check out the current state of cURL fuzzing, I noticed that cURL’s command-line interface (CLI) arguments are not fuzzed. With that in mind, I decided to focus on testing cURL’s handling of arguments. I used the [AFL++](https://aflplus.plus/) fuzzer (a fork of AFL) to generate a large amount of random input data for cURL’s CLI. I compiled cURL using collision-free instrumentation at link time with `AddressSanitizer` and then analyzed crashes that could indicate a bug.

cURL obtains its [options](https://curl.se/docs/manpage.html) through command-line arguments. As cURL follows the C89 standard, the `main()` function of a program can be defined with no parameters or with two parameters (`argc` and `argv`). The `argc` argument represents the number of command-line arguments passed to the program (which includes the program’s name). The `argv` argument is an array of pointers to the arguments passed to the program from the command line.

The standard also states that in a hosted environment, the `main()` function takes a third argument, char `*envp[]`; this argument points to a null-terminated array of pointers to `char`, each of which points to a string with information about the program’s environment.

The three parameters can have any name, as they are local to the function in which they are declared.

cURL’s `main()` function in the `curl/src/tool_main.c` file passes the command-line arguments to the `operate()` function, which parses them and sets up the global configuration of cURL. cURL then uses that global configuration to execute the operations.

## Fuzzing argv

When I started the process of attempting to fuzz cURL, I looked for a way to use AFL to fuzz its argument parsing. My search led me to a [quote](https://groups.google.com/g/afl-users/c/ZBWq0LdHBzw/m/zBlo7q9LBAAJ) from the creator of AFL (Michal Zalewski):

> “AFL doesn’t support argv fuzzing because TBH, it’s just not horribly useful in practice. There is an example in experimental/argv\_fuzzing/ showing how to do it in a general case if you really want to.”

I looked at that [experimental AFL feature](https://github.com/google/AFL/blob/master/experimental/argv_fuzzing/argv-fuzz-inl.h) and its [equivalent](https://github.com/AFLplusplus/AFLplusplus/tree/stable/utils/argv_fuzzing) in AFL++. The `argv` fuzzing feature makes it possible to fuzz arguments passed to a program from the CLI, instead of through standard input. That can be useful when you want to cover multiple APIs of a library in fuzz testing, as you can fuzz the arguments of a tool that uses the library rather than writing multiple fuzz tests for each API.

## How does the AFL++ argvfuzz feature work?

The [argv-fuzz-inl.h](https://github.com/AFLplusplus/AFLplusplus/blob/stable/utils/argv_fuzzing/argv-fuzz-inl.h) header file of `argvfuzz` defines two macros that take input from the fuzzer and set up `argv` and `argc`:

* The `AFL_INIT_ARGV()` macro initializes the `argv` array with the arguments passed to the program from the command line. It then reads the arguments from standard input and puts them in the `argv` array. The array is terminated by two `NULL` characters, and any empty parameter is encoded as a lone `0x02` character.
* The `AFL_INIT_SET0(_p)` macro is similar to `AFL_INIT_ARGV()` but also sets the first element of the `argv` array to the value passed to it. This macro can be useful if you want to preserve the program’s name in the `argv` array.

Both macros rely on the `afl_init_argv()` function, which is responsible for reading a command line from standard input (by using the `read()` function in the `unistd.h` header file) and splitting it into arguments. The function then stores the resulting array of strings in a static buffer and returns a pointer to that buffer. It also sets the value pointed to by the `argc` argument to the number of arguments that were read.

To use the `argv-fuzz` feature, you need to include the `argv-fuzz-inl.h` header file in the file that contains the `main()` function and add a call to either `AFL_INIT_ARGV` or `AFL_INIT_SET0` at the beginning of `main()`, as shown below:

[![](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/argv.png?resize=690%2C261&ssl=1)](https://i0.wp.com/blog.trailofbits.com/wp-content/uploads/2023/02/argv.png?ssl=1)

curl/src/tool\_main.c

## Preparing a dictionary

A fuzzing dictionary file specifies the data elements that a fuzzing engine should focus on during testing. The fuzzing engine adjusts its mutation strategies so that it will process the tokens in the dictionary. In the case of cURL fuzzing, a fuzzing dictionary can help `afl-fuzz` more effectively generate valid test cases that contain options (which start with one or two dashes).

To fuzz cURL, I used the `afl-clang-lto` compiler’s autodictionary feature, which automatically generates a dictionary during compilation of the target binary. This dictionary is transferred to `afl-fuzz` on startup, improving its coverage. I also prepared a custom dictionary based on the cURL [manpage](https://curl.se/docs/manpage.html) and passed it to `afl-fuzz` via the -x parameter. I used the following Bash command to prepare the dictionary:

```
$ man curl | grep -oP '^\s*(--|-)\K\S+' | sed 's/[,.]$//' | sed 's/^/"&/; s/$/&"/'  | ...