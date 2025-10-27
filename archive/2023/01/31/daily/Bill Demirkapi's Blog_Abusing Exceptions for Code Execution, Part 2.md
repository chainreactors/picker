---
title: Abusing Exceptions for Code Execution, Part 2
url: https://billdemirkapi.me/abusing-exceptions-for-code-execution-part-2/
source: Bill Demirkapi's Blog
date: 2023-01-31
fetch_date: 2025-10-04T05:16:56.574055
---

# Abusing Exceptions for Code Execution, Part 2

[Bill Demirkapi's Blog](https://billdemirkapi.me)

* [Home](https://billdemirkapi.me/)
* [About](https://billdemirkapi.me/about/)

[Subscribe](#/portal/signup)

[Security Research](https://billdemirkapi.me/tag/security-research/)

# Abusing Exceptions for Code Execution, Part 2

In this article, we'll explore how the concepts behind Exception Oriented Programming can be abused when exploiting stack overflow vulnerabilities on Windows.

* [![Bill Demirkapi](/content/images/size/w100/2021/02/lrVO7WoC_400x400-1.jpg)](/author/bill/)

#### [Bill Demirkapi](/author/bill/)

Jan 30, 2023
• 50 min read

![Abusing Exceptions for Code Execution, Part 2](/content/images/size/w2000/2023/01/eop2_header.png)

*Full disclosure- Microsoft hired me following part 1 of this series. This research was conducted independently, and a vast majority of it was completed before I joined. Obviously, no internal information was used, and everything was built on public resources.*

In [*Abusing Exceptions for Code Execution, Part 1*](https://billdemirkapi.me/exception-oriented-programming-abusing-exceptions-for-code-execution-part-1), I introduced the concept of Exception Oriented Programming (EOP), which was a method of executing arbitrary operations by chaining together code from legitimate modules. The primary benefit of this approach was that the attacker would never need their shellcode to be in an executable region of memory, as the technique relied on finding the instructions of their shellcode in existing code.

The last article primarily focused on abusing this technique when you already have some form of code execution. Although powerful for obfuscation and evasion, the use cases provided would only be relevant when an attacker had already compromised an environment. For example, how does EOP compare to existing exploitation techniques such as Return Oriented Programming (ROP)? In this article, we'll explore how the concepts behind Exception Oriented Programming can be abused when exploiting stack overflow vulnerabilities on Windows.

# Background

Before we can get into how EOP can help exploit stack-based attacks, it's important to know the history of the mitigations we are up against. I assume you already have familiarity with the OS-agnostic basics, such as ASLR and DEP.

## Security Cookies

Security cookies (aka "stack canaries") are a compiler mitigation introduced around two decades ago. [Here](https://learn.microsoft.com/en-us/cpp/build/reference/gs-buffer-security-check) is a helpful summary from Microsoft's documentation:

> On functions that the compiler recognizes as subject to buffer overrun problems, the compiler allocates space on the stack before the return address. On function entry, the allocated space is loaded with a  *security cookie*  that is computed once at module load. On function exit, and during frame unwinding on 64-bit operating systems, a helper function is called to make sure that the value of the cookie is still the same. A different value indicates that an overwrite of the stack may have occurred. If a different value is detected, the process is terminated.

Security cookies are relatively straightforward. By placing a "random" cookie next to the return address on the stack, attackers exploiting stack overflow vulnerabilities face a significant problem- how do you modify the return address without failing the cookie check?

Over the years, there has been lots of work put into bypassing these security cookies. I found [this helpful overview](https://www.corelan.be/index.php/2009/09/21/exploit-writing-tutorial-part-6-bypassing-stack-cookies-safeseh-hw-dep-and-aslr/) from the Corelan team written in 2009. Let's review some of the techniques they discuss that are still relevant to this day:

1. This mitigation is irrelevant if you have an overflow vulnerability in a function that does not have a security cookie check (i.e. because there are no string buffers).
2. If you have an information disclosure primitive, you could attempt to leak the security cookie for the current function from the stack *or* the security cookie in the `.data` section.
   * For example, if you had a string buffer and a method of getting the application to "print" that string, you could overflow the buffer up to the security cookie such that there is no NULL terminator. When the string is "printed", all the bytes of the cookie until a NULL terminator would be returned as a part of the string.
3. If you already have an arbitrary "write-what-where" primitive and know the location of the security cookie, you can overwrite it with your own, allowing you to predict the "correct" value to place on the stack.
4. You can still overwrite local variables on the stack to hijack control flow.
   * For example, if a pointer was stored on the stack (before the overflow'd variable) used in a desirable operation like `memcpy` *after* the overflow occurs, you could overwrite this pointer without corrupting the security cookie.
   * Another example would be objects with "virtual tables" on the stack that we can overwrite. If an object's virtual table is used after the overflow occurs, an attacker could influence the target of those virtual calls. Of course, this would likely be subject to control-flow integrity mitigations like [Control Flow Guard](https://learn.microsoft.com/en-us/windows/win32/secbp/control-flow-guard) (or xFG) on Windows.

Outside of these approaches, there has been extensive research into abusing exception handling. Before mitigations such as SafeSEH and SEHOP, which we will discuss soon, attackers in the context of 32-bit applications could modify "exception registration records" on the stack. The Corelan team covered this path of exploitation in [a separate blog](https://www.corelan.be/index.php/2009/07/25/writing-buffer-overflow-exploits-a-quick-and-basic-tutorial-part-3-seh/). More recently, however, [@\_ForrestOrr](https://twitter.com/_forrestorr) wrote in detail about SEH hijacking in [his article](https://www.cyberark.com/resources/threat-research-blog/a-modern-exploration-of-windows-memory-corruption-exploits-part-i-stack-overflows) about memory corruption bugs on Windows.

## SEH Hijacking and the Mitigations Against It

In 32-bit applications, exception registration records contain a pointer to the "next" SEH record on the stack and a pointer to the exception handler itself. Back in the day, attackers could hijack control flow even with security cookies by:

1. Replacing the exception handler on the stack with their own.
2. Triggering an exception before the security cookie check.

This would allow the attacker to call an arbitrary handler with partial control over the passed arguments.

### SafeSEH

To protect against this technique, Microsoft introduced a mitigation called [SafeSEH](https://learn.microsoft.com/en-us/cpp/build/reference/safeseh-image-has-safe-exception-handlers). At a high level, "legitimate" exception handlers are built into the binary at compile-time. Although an attacker can still replace the exception handler on the stack, if it is not in the module's list of exception handlers, a `STATUS_INVALID_EXCEPTION_HANDLER` exception is raised.

### SEHOP

[SEH Overwrite Protection](https://msrc-blog.microsoft.com/2009/02/02/preventing-the-exploitation-of-structured-exception-handler-seh-overwrites-with-sehop/) (SEHOP) is another mitigation that would protect 32-bit applications from having their exception handlers overwritten- without requiring them to be recompiled. This approach works by adding an exception registration record at the bottom of the chain and making sure it is "reachable" when an exception occurs. Remember that besides the exception handler, the registration record contains a pointer to the "next" SEH record. If an attacker corrupts this "next" pointer, the chain is broken, and this final item is not reachable, preventing the attack. Of course, if an attacker can predict the "next" pointer successfully, this mitigation ca...