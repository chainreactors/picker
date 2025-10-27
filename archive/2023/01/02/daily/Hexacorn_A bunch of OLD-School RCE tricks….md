---
title: A bunch of OLD-School RCE tricks…
url: https://www.hexacorn.com/blog/2023/01/01/a-bunch-of-old-school-rce-tricks/
source: Hexacorn
date: 2023-01-02
fetch_date: 2025-10-04T02:52:13.553994
---

# A bunch of OLD-School RCE tricks…

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

[← Previous](https://www.hexacorn.com/blog/2022/12/30/beyond-good-ol-run-key-part-140/)
[Next →](https://www.hexacorn.com/blog/2023/01/03/putting-elf-on-the-shelf/)

# A bunch of OLD-School RCE tricks…

Posted on [2023-01-01](https://www.hexacorn.com/blog/2023/01/01/a-bunch-of-old-school-rce-tricks/ "12:44 am")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Every once in a while I come across questions from RCE analysts who are asking how to analyze samples when either existing tools don’t work, or when they (analysts) get stuck…

Truth be told… These are VERY good times to become a reverser. So many tools, so many tutorials available, and of course, so many people reversing stuff every day that you can network with and end up helping each other. Then you have the [GPT-3](https://openai.com/api/) as well which makes us all feel a bit redundant… Yet, many day to day tricks, often used more as a matter of ‘muscle memory’ than anything else are not discussed, perhaps because many are very old, and not really needed in many cases… until they are.

Let’s try jotting some of them down:

* In 2022 there is almost certainly more than one tool to do the same thing… – google it, stackoverflow it, github it and ask around – on Twitter, Mastodon, Slack, Discord, old-school mailing lists! THERE ARE MANY TOOLS TO DO AND ACHIEVE THE SAME THING/RESULT OR a similar, but slightly DIFFERENT THING/RESULT. There are many file identifiers/viewers/editors, disassemblers, decompilers, binary difference analysis tools, carving tools, etc. Just ASK AROUND.
* If the tool doesn’t accept your file format, or fails on that particular sample – try to convert the sample to a different format; this will enable you to analyze them with different tools, often very old ones; it works especially well with Office formats:
  + DOC/OLE vs DOCX/ZIP, XLS/OLE vs XLSX/ZIP, but also
  + DOC vs DOCX, DOC/DOCX vs RTF, and
  + XLSX vs CSV
* For Office files in general:
  + Try older versions of Office – you will be surprised that sometimes they open files that newer versions Office struggle with
  + Try Libre/Open Office and its clones/spin-off projects
  + Load macro into VBA editor/debugger (ALT+F11 on Windows)
    - Use VBA environment and its debugger for analysis! debug/trace/write loops enumerating existing objects, shapes, etc and print out the document properties as ‘VBA sees it’
    - Even if the office macro autoruns, you can very often not only inspect the content of the macro, but also edit it, disable automacros in a VM session, and re-open it again in a new session — toy around with the Office environment settings!
* Speaking of VM sessions – save VM snapshots before you try something and revert to it when it fails; it’s the best debugger’s help ever!
* Not too many people know that clamav [decompiles](https://twitter.com/SmugYeti/status/1089919472444624896) autoit scripts
* Not too many people know that 64-bit AutoIT compiled executables can be ported to 32-bit interpreter and [Exe2AUT](https://www.hexacorn.com/blog/2015/01/08/decompiling-compiled-autoit-scripts-64-bit-take-two/) still works!
* If a sample kills your tools e.g. Procmon, Process Explorer, Process Hacker (maybe even System Informer!), Olly, XDBG – manually change process name, class/window name strings inside these program binaries and re-use them in the future (these techniques are so obsolete in 2022 that it’s quite rare to come across it, but always…)
* If sample spawns a child process and you want to debug that child process, and nothing else works you can always:
  + pause your debug session before the remote thread execution, thread resuming or before the thread context changes: breakpoints on CreateProcessInternalW, ResumeProcess, ResumeThread, debug APIs, etc. help
  + locate an entry point in a child process, or any other place where the execution is going to resume in a remote process, then you can patch it with a never-ending loop (EB FE in its simplest form — easy to use Process Hacker/System Informer to modify that code)
  + run/resume the parent process, making the child process run as well (it will get stuck in a never-ending loop)
  + then attach new debugger to that child process
  + (un)patch the never-ending loop by patching it back to what it used to be before the EB FE patch
  + you can now start analyzing the remote code under debugger (again, use VM snapshots to preserve the moment, so if it ‘escapes’ you can revert to the moment you start analysing the child process right after patch)
* Focus on buffers; if there is anything worth dumping from a sample apart from static strings it is its dynamically allocated buffers; whether it is a string (file name, mutex/mutant, malware version, etc), (de)compressed/encrypted data, passwords, data read/written from/to files/streams/whatever – in most cases this will answer many DFIR questions w/o you actually you doing tedious static analysis – also, monitoring Heap, Virtual memory allocation functions, CryptDecrypt, and any string APIs are your friends here — see my Frida [monitor](https://www.hexacorn.com/blog/2022/02/20/delphi-api-monitoring-with-frida-part-3/)
* Comb twitter, github for new forensic tools, especially within a very demanding DFIR space – there is a lot of parsers for many file types that may help you to analyze samples — parsers and carvers are literally the best tools in any reversers’ arsenal, apart from a traditional disassembler, decompiler or strace/api monitor
* If the code is for Linux (ELF executable), some parts of it can also run under Windows… yes, it’s a concept that is hard to grasp at first, but when you realize the OSes share the same instruction set it will suddenly make a lot of sense… Yes, that is… You can load any encryption/decryption routine from (intel) Linux under (intel) Windows and make it work…
  How?
  Put the ELF on the shelf — convert your ELF file to a [shellcode](https://www.hexacorn.com/blog/2015/12/10/converting-shellcode-to-portable-executable-32-and-64-bit/), load it under xdbg, find the code you want to instrument (search for its binary signature), and suddenly you are cracking hard Linux problems using many, very versatile Windows tools available… !!!
  Note here: xdbg has a really cool feature to allocate new memory RW buffer within a debugee, and you can copy read-only data from the loaded ELF-shellcoded image into this newly allocated buffer; then just need to change the decryption/decompression buffer address/register values to start decrypting/decompressing into that new buffer!
  this is embarrassingly amazing… really… sky is the limit… would you rather use a cumbersome gdb or absolutely-amazing full-featured xdbg to decrypt this data? Code is just a code… be creative with it. Switch to a better debugging world if you can.
* don’t write idapython/python for EVERYTHING… if you can cheat, do it… dump from memory, instrument, use VM snapshots… I was once asked to decrypt like 10-15 config files of a malware family — I had no idea how the decryption algo worked, and it was too time-consuming to analyze the proprietary algorithm used by the malware; what I did was simple – by using vm snapshot/reverse to snapshot function I was able to decrypt them all w/o knowing how the algo worked. How? I saved the snapshot of VM where I had a register pointing to a filename buffer, ready to read data from its ‘current’ config file, then decrypt it, and have it available in memory for dumping — again, I didn’t even care how the config decryption works; both the in...