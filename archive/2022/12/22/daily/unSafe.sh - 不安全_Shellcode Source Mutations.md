---
title: Shellcode Source Mutations
url: https://buaq.net/go-140922.html
source: unSafe.sh - 不安全
date: 2022-12-22
fetch_date: 2025-10-04T02:11:37.231366
---

# Shellcode Source Mutations

* [unSafe.sh - дёҚе®үе…Ё](https://unsafe.sh)
* [жҲ‘зҡ„ж”¶и—Ҹ](/user/collects)
* [д»Ҡж—ҘзғӯжҰң](/?hot=true)
* [е…¬дј—еҸ·ж–Үз«](/?gzh=true)
* [еҜјиҲӘ](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [зј–з Ғ/и§Јз Ғ](/encode)
* [ж–Үд»¶дј иҫ“](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
й»‘еӨңжЁЎејҸ

![](https://8aqnet.cdn.bcebos.com/2352c1997629d2937daa46444b70c65f.jpg)

Shellcode Source Mutations

Skip to content
*2022-12-21 17:0:32
Author: [labs.nettitude.com(жҹҘзңӢеҺҹж–Ү)](/jump-140922.htm)
йҳ…иҜ»йҮҸ:40
ж”¶и—Ҹ*

---

[Skip to content](#content)

One of the main benefits of writing your shellcode in assembly is that you have full control over the structure of the shellcode.

For example, the content and order of the functions in the source file can (obviously) be changed and the code compiled to produce a new version of your shellcode. These changes donвҖҷt have to be functional however, we can use automated tools to mutate the shellcode source so that each time we compile it the functionality stays the same, but the contents are changed.

This then means that the resultant shellcode will have a different size, file hash, byte order etc, which will make it harder to reliably detect both statically and in memory.

This ability is orthogonal to shellcode encryption etc, as at some point encrypted and encoded shellcode needs to be decrypted and decoded and descrambled so that it can actually be executed, and at this point it may get detected.

LetвҖҷs make use of a concrete, if a little contrived, example.

## Test Case

We can take the nasm source code for some [MessageBox shellcode from Didier Stevens](https://blog.didierstevens.com/2009/06/30/messagebox-shellcode/), compile it as per his instructions and inject it and we successfully get a message box вҖ“ so far so good.

![Testing the default shellcode.](https://i0.wp.com/labs.nettitude.com/wp-content/uploads/2022/12/graphical-user-interface-text-description-automa.png?resize=1113%2C626&ssl=1)

If we were to extract this shellcode as a blue teamer and want to write detections to catch it, we may note the hash, examine the contents and the disassembly and then write a [yara](https://github.com/VirusTotal/yara) rule to be able to catch it in memory or on disk.

As show below, we can take a quick peek at the binary using binary refinery.

![Taking a quick peek at the binary using binary refinery.](https://i0.wp.com/labs.nettitude.com/wp-content/uploads/2022/12/a-picture-containing-calendar-description-automat.png?resize=1100%2C408&ssl=1)

We also note the sha256 hash is `a8fb8c2b46ab00c0c5bc6aa8d9d6d5263a8c4d83ad465a9c50313da17c85fcb3`.

Rizin can be used to examine the shellcode disassembly.

![Examining the shellcode disassembly using rizin.](https://i0.wp.com/labs.nettitude.com/wp-content/uploads/2022/12/text-description-automatically-generated.png?resize=1102%2C761&ssl=1)

If we were to write a very quick yara rule for this, we may choose to focus on the initial bytes which perform some setup. Replacing the offsets (e.g. `[rbx + 0x113]`) with wildcards and taking the bytes up to the second call at `0x0000001b` we can write a quick yara rule that matches the shellcode in memory and on disk, but nothing else in e.g. `C:\Windows\System32`В (testing for false positives).

![A quick-and-dirty yara rule for the shellcode.](https://i0.wp.com/labs.nettitude.com/wp-content/uploads/2022/12/text-description-automatically-generated-1.png?resize=1023%2C311&ssl=1)

The rule matches the shellcode on disk and in memory and triggers no false positives against anything in `C:\Windows\System32`.

![The rule matches the shellcode on disk and in memory and triggers no false positives against anything in C:\Windows\System32.](https://i0.wp.com/labs.nettitude.com/wp-content/uploads/2022/12/calendar-description-automatically-generated.png?resize=1095%2C199&ssl=1)

So we have a reliable yara rule and add it to our threat hunts, all good right?

## Shellcode Mutator

This is where the [Shellcode Mutator](https://github.com/nettitude/ShellcodeMutator) project comes in. This simple python script will parse nasm source code and insert sets of instructions at random intervals that вҖҳdo nothingвҖҷ, but will then alter and byte order and file hash of the shellcode at the cost of increased size.

The script is easy enough to use, taking a source code вҖҳtemplateвҖҷ, an out file, a morph percentage and a flag to set `x86` vs `x64` mode.

![Help text for shellcode mutator.](https://i0.wp.com/labs.nettitude.com/wp-content/uploads/2022/12/text-description-automatically-generated-2.png?resize=1124%2C433&ssl=1)

This script has some basic logic to check source lines but essentially has to sets of instructions that can be expanded upon, one for `x86` and one for `x64`. Each entry in these instruction sets should, after all instructions have executed, leave all registers and flags in the same state as before they were executed to ensure that the shellcode can continue without erroring.

![The default "no instructions" sets.](https://i0.wp.com/labs.nettitude.com/wp-content/uploads/2022/12/text-description-automatically-generated-3.png?resize=368%2C482&ssl=1)

Along with some other logic, the script will place these instruction sets at random intervals (dictated by the morph percentage) before the instructions specified in the `assembly_instructions` variable:

![Instructions that are used as triggers for the mutations.](https://i0.wp.com/labs.nettitude.com/wp-content/uploads/2022/12/a-screenshot-of-a-computer-description-automatica.png?resize=312%2C561&ssl=1)

If we run the script against our MessageBox shellcode, setting a morph percentage of 15% we get a source code file that is 57 lines instead of 53. Compiling that shellcode and executing the yara search shows that it is not caught and only the original shellcode matches.

![The mutated MessageBox shellcode no longer matches our yara rule.](https://i0.wp.com/labs.nettitude.com/wp-content/uploads/2022/12/text-description-automatically-generated-4.png?resize=1111%2C298&ssl=1)

Examining the disassembly of the binary file shows that it has inserted a nop (`0x90`) instruction into the bytes that we matched upon (in addition to at other places). This of course also changed the file hash.

![The instruction that caused our yara rule not to match.](https://i0.wp.com/labs.nettitude.com/wp-content/uploads/2022/12/graphical-user-interface-text-description-automa-1.png?resize=827%2C696&ssl=1)

There is an element of luck of course. We need to make sure that we change enough bytes that any yara rules will no longer match without actually knowing what those yara rules are (or any other detections). Increasing the morph percentage then will increase the number of alterations made and the likelihood of bypassing any rules at the cost of increased shellcode size.

Of course the big question is, does our shellcode still run?

![Testing the morphed shellcode still works!](https://i0.wp.com/labs.nettitude.com/wp-content/uploads/2022/12/graphical-user-interface-text-chat-or-text-messa.png?resize=927%2C334&ssl=1)

Winning!

## References

* <https://blog.didierstevens.com/2009/06/30/messagebox-shellcode/>
* <https://github.com/VirusTotal/yara>
* <https://github.com/binref/refinery/>
* <https://github.com/rizinorg/rizin>
* <https://github.com/nettitude/ShellcodeMutator>

ж–Үз« жқҘжәҗ: https://labs.nettitude.com/blog/shellcode-source-mutations/
 еҰӮжңүдҫөжқғиҜ·иҒ”зі»:admin#unsafe.sh

© [unSafe.sh - дёҚе®үе…Ё](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [е®үе…Ёй©¬е…Ӣ](https://aq.mk)
* [жҳҹйҷ…й»‘е®ў](https://xj.hk)
* [T00ls](https://t00ls.net)