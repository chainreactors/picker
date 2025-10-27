---
title: Decrypting SHell Compiled (SHC) ELF files
url: https://www.hexacorn.com/blog/2023/01/13/decrypting-shell-compiled-shc-elf-files/
source: Hexacorn
date: 2023-01-14
fetch_date: 2025-10-04T03:52:20.471958
---

# Decrypting SHell Compiled (SHC) ELF files

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

[← Previous](https://www.hexacorn.com/blog/2023/01/08/excelling-at-excel-part-2/)
[Next →](https://www.hexacorn.com/blog/2023/01/21/yara-rules-pageant/)

# Decrypting SHell Compiled (SHC) ELF files

Posted on [2023-01-13](https://www.hexacorn.com/blog/2023/01/13/decrypting-shell-compiled-shc-elf-files/ "11:37 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

In its recent blog post [AhnLab](https://asec.ahnlab.com/en/45182/) described a campaign that relies on SHell Compiled (SHC) ELF files. I wanted to see if I can replicate their reverse engineering work and decrypt actual shell commands they had shared in their post. This turned out to be a bit more complicated than I thought, hence this post aiming at making it a bit easier for you.

Before I go into nitty-gritty details – when I try to crack new stuff I usually look for an existing body of work first. A really quick google search helped me to discover a tool called [UnSHC](https://github.com/yanncam/UnSHc) that helps to decrypt SHC ELF files in a generic way. And I must digress here for a moment – it’s an amazing hack of a tool really – a shell script engaging lots of CLI tools trying to discover the inner working of the encryption via automated code analysis, find the decryption routine and then actually produce the decrypted script as an output. While it didn’t work for me, I feel kudos to the author are in order. Studying the inner working of UnShc was a pure pleasure. Thumbs up!

Coming back to the AhnLab post. I was intrigued by the Alleged RC4 encryption used by SHC and thought — okay, I just need to load it into a debugger, step through it, maybe instrument it here and there, and then look at the decrypted buffers. So, I did that, then I realized that despite walking through the code, I could only decrypt part of the encrypted data. I could decrypt the ‘internal’ strings of SHC, but not the final shell code. I did correctly guess where the encrypted shell script is, I did instrument the debugger to go there, but while trying to decrypt the encrypted blob… I was getting another binary blob that looked like garbage.

Hmm something was really fishy there.

After staring at the code of the sample in IDA, I realized there is a routine where the executable is trying to retrieve a value of a particular environment variable. After studying it a bit more, I realized that the SHC author engaged a clever trick to make reversers’ life a bit harder. When the program is executed a tuple of an environment variable and its value derived from a process ID, number of arguments (argc), the actual routine itself (probably to detect ‘int 3’ opcodes in it, if debugged) are added to the process environment. The program then calls execve on its own file. This makes the program restart with the same pid (the ELF image is overwritten in memory and restarted). And this finally leads to the execution of the aforementioned routine again, and this time the required tuple of environment variable and its value are present. Only then the decryption of the actual embedded shell script is possible. From a debugging/instrumenting perspective it’s unpleasant, so I had to quickly devise a way to bypass it.

It turned out that it’s easier than expected.

The solution: the very same ‘environment-operating’ routine can be called twice. The first time it will look for the environment variable, and it won’t find it there, so it will add it. The second time we execute it via instrumentation, the environment variable will be there. So, it will read the value of the environment variable, set appropriate inner variables, and with that in place we can decrypt the main shell script within a single process instance.

Let’s have a look at the example: 256ab7aa7b94c47ae6ad6ca8ebad7e2734ebaa21542934604eb7230143137342.

We load it into edb first, and then make a breakpoint on 0x400FDD — this is prior to executing aforementioned ‘environment variable’ tinkering procedure. Then we run the program (F9). We should get a break here:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/edb_shc1.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/edb_shc1.png)

We step over it F8, F8 and now we end up in 0x400FE5.

We then re-run the code above to make it look like we execute it as if we were in the new instance of the process. So. we go back to 0x400FDD and set the RIP to ‘here’ — right click and ‘Set RIP to this instruction’, or CTRL+\*. We do F8, F8. And we are set.

All we have to do now is F8 many times until we reach 0x4011A7, at this stage point your dump window to the location rdi points to. Then execute decryption routine and you will see the decrypted shell script in the data dump window:

[![](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/edb_shc2.png)](https://www.hexacorn.com/blog/wp-content/uploads/2023/01/edb_shc2.png)

**Update**

Additionally, in 2023-12 [NtSuspendProcess(NtCurrentProcess())](https://twitter.com/hmm261120) contacted me to let me know of his script that uses a clever trick to achieve the same thing w/o using debugger.

See the script [here](https://github.com/kawaii-ghost/deshc/blob/main/deshc.sh).

This entry was posted in [De-everything, Un-everything](https://www.hexacorn.com/blog/category/de-everything-un-everything/), [elf](https://www.hexacorn.com/blog/category/elf/), [linux](https://www.hexacorn.com/blog/category/linux/), [shc](https://www.hexacorn.com/blog/category/shc/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2023/01/13/decrypting-shell-compiled-shc-elf-files/ "Permalink to Decrypting SHell Compiled (SHC) ELF files").

[Privacy Policy](https://www.hexacorn.com/blog/privacy-policy/) [Proudly powered by WordPress](https://wordpress.org/ "Semantic Personal Publishing Platform")