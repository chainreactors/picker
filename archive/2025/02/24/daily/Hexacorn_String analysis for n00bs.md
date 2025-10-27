---
title: String analysis for n00bs
url: https://www.hexacorn.com/blog/2025/02/23/string-analysis-for-n00bs/
source: Hexacorn
date: 2025-02-24
fetch_date: 2025-10-06T20:33:45.627164
---

# String analysis for n00bs

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

[← Previous](https://www.hexacorn.com/blog/2025/02/22/good-exports-are-real/)
[Next →](https://www.hexacorn.com/blog/2025/02/24/dexray-v2-35/)

# String analysis for n00bs

Posted on [2025-02-23](https://www.hexacorn.com/blog/2025/02/23/string-analysis-for-n00bs/ "2:06 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

I like to demo this little [windows executable](https://hexacorn.com/d/sample.exe) to everyone who thinks they are doing the reverse engineering bit right, by using available automated static and dynamic analysis tools, and trusting them blindly.

The sample is a PE32 that is 2560 bytes long. Running ‘strings’ over it produces these results:

```
!This program cannot be run in DOS mode.
Rich
.text
`.rdata
@.data
8/u
ExitProcess
GetCommandLineA
kernel32.dll
GetStdHandle
WriteFile
Hello World!
```

Running it from a CLI gives us the following text being printed out to the STDOUT:

```
Hello World!
```

One can say that both static and dynamic analysis give us the same output. Based on this info it’s kinda obvious to conclude that this small binary is a simple CLI program that prints out ‘Hello World!’ when executed.

Except, only code analysis can help us to determine that the program behaves differently if we pass a ‘/h’ argument to it.

In such case, the dynamic analysis will show that the following string is being printed out to the STDOUT:

```
Hello Baby!!
```

Static analysis was done right. Default dynamic analysis was done right. And code analysis was done right too. It’s just the automation that failed.

Just a reminder that we can’t blindly trust the automation, because it only sees the obvious. And command line arguments are not the only way to trigger execution of a different branch of code. It could be a guard rail of any sort: time of the day, locale of the OS, delayed payload, payload downloaded from a site that is not available atm, etc.

in the interest of full disclosure: I have not ‘analyzed’ this sample with any AI framework, so am still hopeful that at least some of them would see through this little mischief.

This entry was posted in [Anti-Forensics](https://www.hexacorn.com/blog/category/anti-forensics/), [Malware Analysis](https://www.hexacorn.com/blog/category/malware-analysis/), [Tips & Tricks](https://www.hexacorn.com/blog/category/tips-tricks/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2025/02/23/string-analysis-for-n00bs/ "Permalink to String analysis for n00bs").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")