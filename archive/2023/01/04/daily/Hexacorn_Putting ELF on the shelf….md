---
title: Putting ELF on the shelf…
url: https://www.hexacorn.com/blog/2023/01/03/putting-elf-on-the-shelf/
source: Hexacorn
date: 2023-01-04
fetch_date: 2025-10-04T02:59:03.239550
---

# Putting ELF on the shelf…

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

[← Previous](https://www.hexacorn.com/blog/2023/01/01/a-bunch-of-old-school-rce-tricks/)
[Next →](https://www.hexacorn.com/blog/2023/01/07/excelling-at-excel-part-1/)

# Putting ELF on the shelf…

Posted on [2023-01-03](https://www.hexacorn.com/blog/2023/01/03/putting-elf-on-the-shelf/ "12:20 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In my [last post](https://www.hexacorn.com/blog/2023/01/01/a-bunch-of-old-school-rce-tricks/) I referred to something what I call “putting elf on the shelf”. The idea is simple — Windows is a very rich environment when it comes to reversing and it provides us with many good quality tools that help us with code analysis, both static and dynamic, while other platforms (f.ex. Linux) are not providing so much in this space (I dare to say ‘yet’, but also: ‘I may simply don’t know what is available and am choosing the worst possible path, please correct me!’).

Here’s the trick: as long as the code we analyze is for the same CPU (typically Intel) we can make an effort to statically and dynamically analyze that Linux code under Windows.

But… how, why, omg, bbq…

Enter the whimsical instrumentation world. World full of ‘data is code’ and ‘code is data’, full of exceptions, faults, and code broken into pieces. Yet, it works, most of the time.

Imagine receiving this [ELF](https://www.hexacorn.com/elf/test.7z) file (password: test).

It’s a very simple, 64-bit ELF file generated from a really stupid C program listed below:

```
#include <stdio.h>
 int main (int argc, char * argv[])
 {
     char enc[]= {'H' ^ '2', 'e' ^ '0', 'l' ^ '2', 'l' ^ '3', 'o' ^ '!'};
     char key[] = { "2023!" };
     char dec[6] ={};
     for (int i=0; i< 5; i++)
     {
         dec[i] =  enc[i] ^ key[i];
     }
 }
```

Now that you know the code it’s really simple to analyze it, but.. what if the decryption was more complicated? Under normal circumstances, at this stage most of reversers would try to immediately port the decryption algo to C, python, ruby, idapython and see where it takes them… it’s the best way to do it, but it’s not the most optimal in time-sensitive cases.

Why?

Let’s use this basic example as an excuse to introduce the technique from the title of this post, even if a bit obscure… First of all, yes, we can load the ELF file under gdb, but it’s painful. Secondly, yes, we can port/write decryptors based off ‘seen in code’ algos, but there are always gotchas: slightly modified typical algo constants, missed iteration, unusual decryption or decompression routines, and porting requires a lot of troubleshooting and debugging cycles (again, please note: by no means it’s a criticism or judgment: quite the opposite, the more cycles we spend on understanding these algos, the easier it is to decrypt next generations or malware samples, their DGAs, network protocols, etc.). Again, ROI is everything and you need to work it out with your managers.

Coming back to the actual example I posted earlier. Instead of Linux, why don’t we look at the code under Windows?

We start by converting that ELF file into a [shellcode](https://www.hexacorn.com/blog/2015/12/10/converting-shellcode-to-portable-executable-32-and-64-bit/), first. Yes, embedding an ELF as a shellcode inside a PE file sounds like a stupid idea at first, until you realize that we are not going to run it “just like this”. We are going to instrument it. The only reason we convert it to PE file is so that we can load it under a GOOD visual debugger f.ex. xdbg w/o any hassle:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/elf_shellcode-1024x246.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/elf_shellcode.png)

Okay, now that we loaded the executable under xdbg, what’s next?

Well, we find the code we want to instrument — at this stage it helps to have the original ELF loaded under IDA so that we can find bytes that are of interest, in our case (if you know xdbg shortcut keys, you will ALT+M, CTRL+B to search for binary patterns: 55 48 89 E5 48 83 EC 30):

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/elf_is_pe1-1024x774.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/elf_is_pe1.png)

All you have to do now is to point xdbg to resume code execution in a place we desire aka ‘Set New Origin here’ or ‘Ctrl+\*’ and we are game! Okay, let me step back — debugger can execute instruction at any address we tell it to run, so we can simply skip all the prologues, including Linux-oriented code ran at the beginning of each ELF, and instead jump directly to the juicy part, where the decryption takes place. Yup, once you start instrumenting the code, you can immediately see the results:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/elf.gif)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/elf.gif)

We live in a world that has changed a lot and many times — from reversing perspective, that is — it is of paramount importance that we leverage all the tools in our toolbox to deliver the best ROI possible. Knowing tools, knowing tricks, learning from others is the best way going forward. We can’t, and we won’t know everything. And that’s why we need to cheat, cut corners, but only because we know we can.

This entry was posted in [Malware Analysis](https://www.hexacorn.com/blog/category/malware-analysis/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2023/01/03/putting-elf-on-the-shelf/ "Permalink to Putting ELF on the shelf…").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")