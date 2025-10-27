---
title: 1 little known secret of ShellExec_RunDLL
url: https://www.hexacorn.com/blog/2024/11/30/1-little-known-secret-of-shellexec_rundll/
source: Hexacorn
date: 2024-12-01
fetch_date: 2025-10-06T19:36:42.390836
---

# 1 little known secret of ShellExec_RunDLL

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2024/11/29/mapping-the-api-mapping-code-redundancy/)
[Next →](https://www.hexacorn.com/blog/2024/12/06/execcmd64-lolbin/)

# 1 little known secret of ShellExec\_RunDLL

Posted on [2024-11-30](https://www.hexacorn.com/blog/2024/11/30/1-little-known-secret-of-shellexec_rundll/ "10:40 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

The *ShellExec\_RunDLL* API is now exposed by both *shell32.dl*l and *[windows.storage.dll](https://www.hexacorn.com/blog/2024/11/28/windows-storage-lol/)*.

It is not the only curiosity about this function. Analysing its code one can discover that is accepts a secret command line argument.

If we provide a question mark in the command line argument, the function will interpret the string that follows the question mark as a number. It will then convert that numerical value into a number using StrToIntExW with a STIF\_SUPPORT\_HEX flag (accepts either decimal or hexadecimal number), and then add that value to 0x100 (SEE\_MASK\_NOASYNC/SEE\_MASK\_FLAG\_DDEWAIT). Finally, use the resulting total to set the SHELLEXECUTEINFO.fMask value passed to *ShellExecuteEx*. The function then searches for the second question mark and then uses the position following that question mark as a place where the actual command line passed to *ShellExecuteEx* starts:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2024/11/ShellExec_RunDLL.png)](https://www.hexacorn.com/blog/wp-content/uploads/2024/11/ShellExec_RunDLL.png)

If it sounds too complicated, the basic idea is that function can be invoked in 2 modes:

* regular invocation

```
shell32.dll, ShellExec_RunDLL <cmd line argument>
windows.storage.dll, ShellExec_RunDLL <cmd line argument>
```

* invocation that modifies fmask

```
shell32.dll, ShellExec_RunDLL <?fmaskvalue?> <cmd line argument>
windows.storage.dll, ShellExec_RunDLL <?fmaskvalue?> <cmd line argument>
```

f.ex.:

```
ShellExec_RunDLL ?100?calc.exe
```

And if you are looking for a better example:

```
ShellExec_RunDLL ?0x00800000?<file>
```

can be used to bypass *Zone.Identifier* checks (0x00800000 = SEE\_MASK\_NOZONECHECKS) for the executed *file*.

Since the parsing of the fmask value is done with a code that allows for many different inputs, many interesting invocations are possible:

```
ShellExec_RunDLL ?100?calc.exe
ShellExec_RunDLL ? 100 ?calc.exe
ShellExec_RunDLL ? 0x100 0x200 ?calc.exe
ShellExec_RunDLL ?0x100 notepad.exe?calc.exe
ShellExec_RunDLL ?0x100 format c: ?calc.exe
ShellExec_RunDLL ?0x100 https://google.com ?calc.exe
ShellExec_RunDLL ?0x100 c:\programdata\malware\calc.exe ?calc.exe
```

Every single one of them will launch Calculator.

This entry was posted in [little known secrets](https://www.hexacorn.com/blog/category/little-known-secrets/), [Living off the land](https://www.hexacorn.com/blog/category/living-off-the-land/), [LOLBins](https://www.hexacorn.com/blog/category/living-off-the-land/lolbins/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2024/11/30/1-little-known-secret-of-shellexec_rundll/ "Permalink to 1 little known secret of ShellExec_RunDLL").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")