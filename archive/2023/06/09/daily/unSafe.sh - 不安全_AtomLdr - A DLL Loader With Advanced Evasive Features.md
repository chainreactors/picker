---
title: AtomLdr - A DLL Loader With Advanced Evasive Features
url: https://buaq.net/go-167902.html
source: unSafe.sh - 不安全
date: 2023-06-09
fetch_date: 2025-10-04T11:46:05.696426
---

# AtomLdr - A DLL Loader With Advanced Evasive Features

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

![](https://8aqnet.cdn.bcebos.com/e71144e32795581a9892010acba7f224.jpg)

AtomLdr - A DLL Loader With Advanced Evasive Features

A DLL Loader With Advanced Evasive Features Features: CRT library independent. The final
*2023-6-8 20:30:0
Author: [www.kitploit.com(查看原文)](/jump-167902.htm)
阅读量:92
收藏*

---

[![](https://blogger.googleusercontent.com/img/a/AVvXsEh6w-S5jz5-SwP0kiJW4feqOTiVSPZO6_kRMrF-nwktScR1d5Tqo5Y0OVzKVTp_YJnb1m1ze_kGa8fUKQV0G5Re4iala8m94u7by9cqsFu2BkDfmUpZZtt32HhboOggiiERgARYhzX2B4lMQFPtzYnE2-FpVocO59o5HvsY5nlsMn2usX7t8WddpkDe8w=w640-h582)](https://blogger.googleusercontent.com/img/a/AVvXsEh6w-S5jz5-SwP0kiJW4feqOTiVSPZO6_kRMrF-nwktScR1d5Tqo5Y0OVzKVTp_YJnb1m1ze_kGa8fUKQV0G5Re4iala8m94u7by9cqsFu2BkDfmUpZZtt32HhboOggiiERgARYhzX2B4lMQFPtzYnE2-FpVocO59o5HvsY5nlsMn2usX7t8WddpkDe8w)

A DLL Loader With Advanced Evasive Features

### Features:

* CRT library independent.
* The final DLL file, can run the payload by loading the DLL (executing its entry point), or by executing the exported `"Atom"` function via the command line.
* DLL unhooking from \KnwonDlls\ directory, with **no RWX** sections.
* The encrypted payload is saved in the resource section and retrieved via custom code.
* AES256-CBC Payload [encryption](https://www.kitploit.com/search/label/Encryption "encryption") using custom no table/data-dependent branches using [ctaes](https://github.com/bitcoin-core/ctaes "ctaes"); this is one of the best custom AES implementations I've encountered.
* Aes Key & Iv Encryption.
* Indirect syscalls, utilizing [HellHall](https://github.com/Maldev-Academy/HellHall "HellHall") with *ROP* gadgets (for the unhooking part).
* Payload [injection](https://www.kitploit.com/search/label/Injection "injection") using APC calls - alertable thread.
* Payload execution using APC - alertable thread.
* Api hashing using two different implementations of the `CRC32` string hashing algorithm.
* The total Size is 17kb + payload size (multiple of 16).

### How Does The Unhooking Part Work

AtomLdr's unhooking method looks like the following

[![](https://blogger.googleusercontent.com/img/a/AVvXsEgs9aHVWFAaOCgPwCYVc2LN5UamBAkrfeDjPBwqnSMuVSRN-XUFJiYcy9y12ELRw377Oej5QrKXG0ZILLqd0c1Gg2Ui5_13_ryejrFkEugG6gxJmi3_Rr1lduS9Djj9xTqTfVFTNT7movDXBpI4u3FNX3gWOXHXWeDQHLVtfPjL82bhIn71qEbyEFjOMg=w640-h460)](https://blogger.googleusercontent.com/img/a/AVvXsEgs9aHVWFAaOCgPwCYVc2LN5UamBAkrfeDjPBwqnSMuVSRN-XUFJiYcy9y12ELRw377Oej5QrKXG0ZILLqd0c1Gg2Ui5_13_ryejrFkEugG6gxJmi3_Rr1lduS9Djj9xTqTfVFTNT7movDXBpI4u3FNX3gWOXHXWeDQHLVtfPjL82bhIn71qEbyEFjOMg)

the program Unhooking from the \KnwonDlls\ [directory](https://www.kitploit.com/search/label/Directory "directory") is not a new method to bypass user-land hooks. However, this loader tries to avoid allocating **RWX** memory when doing so. This was obligatory to do in [KnownDllUnhook](https://github.com/NUL0x4C/KnownDllUnhook "KnownDllUnhook") for example, where **RWX** permissions were needed to replace the text section of the hooked modules, and at the same time allow execution of functions within these text sections.

This was changed in this loader, where it suspends the running threads, in an attempt to block any function from being called from within the targetted text sections, thus eliminating the need of having them marked as **RWX** sections before unhooking, making **RW** permissions a possible choice.

This approach, however, created another problem; when unhooking, `NtProtectVirtualMemory` syscall and others were using the syscall instruction inside of ntdll.dll module, as an indirect-syscall approach. Still, as mentioned above, the unhooked modules will be marked as **RW** sections, making it impossible to perform indirect syscalls, because the syscall instruction that we were jumping to, can't be executed now, so we had to jump to another *executable* place, this is where `win32u.dll` was used.

`win32u.dll` contains some [syscalls](https://www.kitploit.com/search/label/Syscalls "syscalls") that are GUI-related functions, making it suitable to jump to instead of ntdll.dll. win32u.dll is loaded (statically), but not included in the unhooking routine, which is done to insure that win32u.dll can still execute the syscall instruction we are jumping to.

The suspended threads after that are resumed.

It is worth mentioning that this approach may not be that efficient, and can be unstable, that is due to the thread suspension trick used. However, it has been tested with multiple processes with positive results, in the meantime, if you encountered any problems, feel free to open an issue.

AtomLdr - A DLL Loader With Advanced Evasive Features
![AtomLdr - A DLL Loader With Advanced Evasive Features](https://blogger.googleusercontent.com/img/a/AVvXsEh6w-S5jz5-SwP0kiJW4feqOTiVSPZO6_kRMrF-nwktScR1d5Tqo5Y0OVzKVTp_YJnb1m1ze_kGa8fUKQV0G5Re4iala8m94u7by9cqsFu2BkDfmUpZZtt32HhboOggiiERgARYhzX2B4lMQFPtzYnE2-FpVocO59o5HvsY5nlsMn2usX7t8WddpkDe8w=s72-w640-c-h582)
Reviewed by Zion3R
on
8:30 AM
Rating: 5

文章来源: http://www.kitploit.com/2023/06/atomldr-dll-loader-with-advanced.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)