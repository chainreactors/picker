---
title: Heap_Detective - The Simple Way To Detect Heap Memory Pitfalls In C++ And C
url: https://buaq.net/go-148194.html
source: unSafe.sh - 不安全
date: 2023-02-07
fetch_date: 2025-10-04T05:50:02.792635
---

# Heap_Detective - The Simple Way To Detect Heap Memory Pitfalls In C++ And C

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

![](https://8aqnet.cdn.bcebos.com/ef6781b5d8b075a9dd2b619b0bf8a051.jpg)

Heap\_Detective - The Simple Way To Detect Heap Memory Pitfalls In C++ And C

This tool uses the taint analysis technique for static analysis and aims to identify points
*2023-2-6 19:30:0
Author: [www.kitploit.com(查看原文)](/jump-148194.htm)
阅读量:32
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhXzEx0lfIl2G6FQanfjqdXtP-OGNviAwG2WrU3lOb4_e6GoM7jRU_rN5VsPAcisF5OUGvOERdmiN5d94K8l6M-7maSVUGVOlROfg5mdqyVmgCpcmdZNNHC-YIEMSO9OlkKOILdY7GF1IU-oOrUe54KB-F6_LVkop9Jjh5HPvpmZ609wEekfzGxNRVpgw=w640-h402)](https://blogger.googleusercontent.com/img/a/AVvXsEhXzEx0lfIl2G6FQanfjqdXtP-OGNviAwG2WrU3lOb4_e6GoM7jRU_rN5VsPAcisF5OUGvOERdmiN5d94K8l6M-7maSVUGVOlROfg5mdqyVmgCpcmdZNNHC-YIEMSO9OlkKOILdY7GF1IU-oOrUe54KB-F6_LVkop9Jjh5HPvpmZ609wEekfzGxNRVpgw)

This tool uses the [taint analysis](https://www.kitploit.com/search/label/Taint%20Analysis "taint analysis") technique for [static analysis](https://www.kitploit.com/search/label/Static%20Analysis "static analysis") and aims to identify points of heap memory usage [vulnerabilities](https://www.kitploit.com/search/label/vulnerabilities "vulnerabilities") in C and C++ languages. The tool uses a common approach in the first phase of static analysis, using tokenization to collect information.

The second phase has a different approach to common lessons of the legendary dragon book, yes the tool doesn't use AST or resources like LLVM following parsers' and standard tips. The approach present aims to study other ways to detect vulnerabilities, using custom vector structures and typical recursive traversal with ranking following taint point. So the result of the sum of these [techniques](https://www.kitploit.com/search/label/Techniques "techniques") is the Heap\_detective.

The tool follows the KISS principle "Keep it simple, stupid!". There's more than one way to do a SAST tool, I know that. Yes, I thought to use graph database or AST, but this action cracked the KISS principle in the context of this project.

[https://antonio-cooler.gitbook.io/coolervoid-tavern/detecting-heap-memory-pitfalls](https://antonio-cooler.gitbook.io/coolervoid-tavern/detecting-heap-memory-pitfalls "https://antonio-cooler.gitbook.io/coolervoid-tavern/detecting-heap-memory-pitfalls")

* C and C++ tokenizer
* List of heap static routes for each source with taint points for analysis
* Analyser to detect double free vulnerability
* Analyser to detect use after free vulnerability
* Analyser to detect memory leak

To test, read the [directory](https://www.kitploit.com/search/label/Directory "directory") samplers to understand the context, so to run look that following:

```
$ git clone https://github.com/CoolerVoid/heap_detective

$ cd heap_detective

$ make

Note: tested in GCC 9 and 11
```

The first argument by command is a directory for recursive analysis. You can study bad practices in directory "samplers".

* Analyser to detect off-by-one vulnerability
* Analyser to detect wild pointer
* Analyser to detect heap overflow vulnerability

## Overview

[![](https://blogger.googleusercontent.com/img/a/AVvXsEhXzEx0lfIl2G6FQanfjqdXtP-OGNviAwG2WrU3lOb4_e6GoM7jRU_rN5VsPAcisF5OUGvOERdmiN5d94K8l6M-7maSVUGVOlROfg5mdqyVmgCpcmdZNNHC-YIEMSO9OlkKOILdY7GF1IU-oOrUe54KB-F6_LVkop9Jjh5HPvpmZ609wEekfzGxNRVpgw=w640-h402)](https://blogger.googleusercontent.com/img/a/AVvXsEhXzEx0lfIl2G6FQanfjqdXtP-OGNviAwG2WrU3lOb4_e6GoM7jRU_rN5VsPAcisF5OUGvOERdmiN5d94K8l6M-7maSVUGVOlROfg5mdqyVmgCpcmdZNNHC-YIEMSO9OlkKOILdY7GF1IU-oOrUe54KB-F6_LVkop9Jjh5HPvpmZ609wEekfzGxNRVpgw)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEilxON0KhIoalJVR9O72BA3RdeJLaKitYIQzyYF4MxWfiGFQHv0WTfMM8kst3D9O7OCZi5PFKQMzvr8XnREPGmYMV1eapuxrkJPKoUQJV9MhUsztAcWOckfBuptpqW4Yofy3a_0NGMVfrhBF4jZU4FnbHJmEmVEEtsmuErBLnRroa3wKGOO4crze4vcxQ=w640-h424)](https://blogger.googleusercontent.com/img/a/AVvXsEilxON0KhIoalJVR9O72BA3RdeJLaKitYIQzyYF4MxWfiGFQHv0WTfMM8kst3D9O7OCZi5PFKQMzvr8XnREPGmYMV1eapuxrkJPKoUQJV9MhUsztAcWOckfBuptpqW4Yofy3a_0NGMVfrhBF4jZU4FnbHJmEmVEEtsmuErBLnRroa3wKGOO4crze4vcxQ)

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgja7XrMms2DZ715yVfwinu5SzlkR-6AJJ3kAvQzvrZjT-Apn-3duMv5cPcs-qR2J7cvHBSw1rohNgpxayYtuINEsUHuqDyFm00UYVr2-ppGxvorEucVzTU5Y0XAoVaYydQUfMOFYnwemETGHCCJIHoerVcgmdBxRMux2wdxmQGpMFbDnCWgpMZtQ3k-w=w508-h640)](https://blogger.googleusercontent.com/img/a/AVvXsEgja7XrMms2DZ715yVfwinu5SzlkR-6AJJ3kAvQzvrZjT-Apn-3duMv5cPcs-qR2J7cvHBSw1rohNgpxayYtuINEsUHuqDyFm00UYVr2-ppGxvorEucVzTU5Y0XAoVaYydQUfMOFYnwemETGHCCJIHoerVcgmdBxRMux2wdxmQGpMFbDnCWgpMZtQ3k-w)

Output example:

```
Collect action done

...::: Heap static route :::...
File path: samplers/example3.c
Func name: main
Var name: new
line: 10:	array = new obj[100];
Sinks:
	 line: 10:	array = new obj[100];
	 Taint:  True
	 In Loop: false

...::: Heap static route :::...
File path: samplers/example3.c
Func name: 	while
Var name: array
line: 27:	array = malloc(1);
Sinks:
	 line: 27:	array = malloc(1);
	 Taint:  True
	 In Loop: false
	 line: 28:	array=2;
	 Taint: false
	 In Loop: false
	 line: 30:	array = malloc(3);
	 Taint:  True
	 In Loop: false

...::: Heap static route :::...
File path: samplers/example5.c
Func name: main
Var name: ch_ptr
line: 8:	ch_ptr = malloc(100);
Sinks:
	 line: 8:	ch_ptr = malloc(100);
	 Taint:  True
	 In Loop: false
	 line: 11:	free(ch_ptr);
	 Taint:  True
	 In Loop: false<   br/>	 line: 12:	free(ch_ptr);
	 Taint:  True
	 In Loop: false

...::: Heap static route :::...
File path: samplers/example1.c
Func name: main
Var name: buf1R1
line: 13:    buf1R1 = (char *) malloc(BUFSIZER1);
Sinks:
	 line: 13:    buf1R1 = (char *) malloc(BUFSIZER1);
	 Taint:  True
	 In Loop: false
	 line: 26:    free(buf1R1);
	 Taint:  True
	 In Loop: false
	 line: 30:    if (buf1R1) {
	 Taint: false
	 In Loop: false
	 line: 31:	free(buf1R1);
	 Taint:  True
	 In Loop: false

...::: Heap static route :::...
File path: samplers/example2.c
Func name: main
Var name: ch_ptr
line: 7:	ch_ptr=malloc(100);
Sinks:
	 line: 7:	ch_ptr=malloc(100);
	 Taint:  True
	 In Loop: false
	 line: 11:		ch_ptr = 'A';
	 Taint: false
	 In Loop:  True
	 line: 12:		free(ch_ptr);
	 Taint:  True
	 In Loop:  True
	 line: 13:		printf("%s\n", ch_pt   r);
	 Taint: false
	 In Loop:  True

...::: Heap static route :::...
File path: samplers/example4.c
Func name: main
Var name: ch_ptr
line: 8:	ch_ptr = malloc(100);
Sinks:
	 line: 8:	ch_ptr = malloc(100);
	 Taint:  True
	 In Loop: false
	 line: 13:		ch_ptr = 'A';
	 Taint: false
	 In Loop: false
	 line: 14:		free(ch_ptr);
	 Taint:  True
	 In Loop: false
	 line: 15:		printf("%s\n", ch_ptr);
	 Taint: false
	 In Loop: false

...::: Heap static route :::...
File path: samplers/example6.c
Func name: main
Var name: ch_ptr
line: 8:	ch_ptr = malloc(100);
Sinks:
	 line: 8:	ch_ptr = malloc(100);
	 Taint:  True
	 In Loop: false
	 line: 11:	free(ch_ptr);
	 Taint:  True
	 In Loop: false
	 line: 13:	ch_ptr = malloc(500);
	 Taint:  True
	 In Loop: false

...::: Heap static route :::...
File path: samplers/example7.c
Fu   nc name: special
Var name: ch_ptr
line: 8:	ch_ptr = malloc(100);
Sinks:
	 line: 8:	ch_ptr = malloc(100);
	 Taint:  True
	 In Loop: false
	 line: 15:		free(ch_ptr);
	 Taint:  True
	 In Loop: false
	 line: 16:		ch_ptr = malloc(500);
	 Taint:  True
	 In Loop: false
	 line: 17:		ch_ptr=NULL;
	 Taint: false
	 In Loop: false
	 line: 25:	char *ch_ptr = NULL;
	 Taint: false
	 In Loop: false

...::: Heap static route :::...
File path: samplers/example7.c
Func name: main
Var name: ch_ptr
line: 27:	ch_ptr = malloc(100);
Sinks:
	 line: 27:	ch_ptr = malloc(100);
	 Taint:  True
	 In Loop: false
	 line: 30:	free(ch_ptr);...