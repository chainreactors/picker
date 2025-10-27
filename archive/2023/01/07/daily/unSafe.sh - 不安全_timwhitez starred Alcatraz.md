---
title: timwhitez starred Alcatraz
url: https://buaq.net/go-144473.html
source: unSafe.sh - 不安全
date: 2023-01-07
fetch_date: 2025-10-04T03:13:43.610182
---

# timwhitez starred Alcatraz

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

![](https://8aqnet.cdn.bcebos.com/b0b7962a315c224f1ecfabcf9bd74a07.jpg)

timwhitez starred Alcatraz

Alcatraz is a x64 binary obfuscator that is able to obfuscate various different pe fil
*2023-1-6 18:40:25
Author: [github.com(жҹҘзңӢеҺҹж–Ү)](/jump-144473.htm)
йҳ…иҜ»йҮҸ:48
ж”¶и—Ҹ*

---

Alcatraz is a x64 binary obfuscator that is able to obfuscate various different pe files including:

* .exe
* .dll
* .sys

* [Alcatraz](#alcatraz)
* [Requirements](#requirements)
* [Usage](#usage)
* [Features](#features)
  + [Obfuscation of immediate moves](#obfuscation-of-immediate-moves)
  + [Control flow flattening](#control-flow-flattening)
  + [ADD mutation](#add-mutation)
  + [Entry-point obfuscation](#entry-point-obfuscation)
  + [Lea obfuscation](#lea-obfuscation)
  + [Anti disassembly](#anti-disassembly)
  + [Import obfuscation](#import-obfuscation)
  + [Final result](#final-result)

Install: <https://vcpkg.io/en/getting-started.html>

`asmjit`: vcpkg.exe install asmjit:x64-windows

[![imgbefore](https://github.com/weak1337/Alcatraz/raw/master/images/gui.PNG)](https://github.com/weak1337/Alcatraz/blob/master/images/gui.PNG)
1.) Load a binary by clicking `file` in the top left corner.
2.) Add functions by expanding the `Functions` tree. (You can search by putting in the name in the searchbar at the top)
3.) Hit `compile` (note: obfuscating lots of functions might take some seconds)

In the following showcase all features (besides the one being showcased) are disabled.

### Obfuscation of immediate moves

If an immediate value is moved into a register, we obfuscate it by applying multiple bitwise operations. Let's take a look at the popular function `_security_init_cookie`.
Before:
[![imgbefore](https://github.com/weak1337/Alcatraz/raw/master/images/const_before.PNG)](https://github.com/weak1337/Alcatraz/blob/master/images/const_before.PNG)
After:
[![imgafter](https://github.com/weak1337/Alcatraz/raw/master/images/const_after.PNG)](https://github.com/weak1337/Alcatraz/blob/master/images/const_after.PNG)

### Control flow flattening

By removing the tidy program structure the compiler generated and putting our code into new generated blocks, we increase the complexity of the program. Lets take this simple function `main` as example (optimization for this program is disabled):
[![imgmain](https://github.com/weak1337/Alcatraz/raw/master/images/flatten_function.PNG)](https://github.com/weak1337/Alcatraz/blob/master/images/flatten_function.PNG)
If we throw this into IDA 7.6 the decompiler will optimize it:
[![imgmainnoobf](https://github.com/weak1337/Alcatraz/raw/master/images/flatten_func_noobf.PNG)](https://github.com/weak1337/Alcatraz/blob/master/images/flatten_func_noobf.PNG)
Now let's flatten its control flow and let IDA analyze it again:
[![imgmainobf](https://github.com/weak1337/Alcatraz/raw/master/images/flatten_func_obf.PNG)](https://github.com/weak1337/Alcatraz/blob/master/images/flatten_func_obf.PNG)
As you can see, the complexity increased by a lot even though I only show a small portion of the generated code. If you want to know what the cfg looks like:
[![imgmaincfg](https://github.com/weak1337/Alcatraz/raw/master/images/flatten_func_cfg.PNG)](https://github.com/weak1337/Alcatraz/blob/master/images/flatten_func_cfg.PNG)

### ADD mutation

If a register (eg. RAX) is added to another register (eg. RCX) we will mutate the instruction. This means that the syntax changes but not the semantic.
The instruction `ADD RCX, RAX` can be mutated to:

```
push rax
not rax
sub rcx, rax
pop rax
sub rcx, 1
```

If you want to learn more about mutation take a look at [perses](https://github.com/mike1k/perses).

### Entry point obfuscation

If the PE file is a .exe (.dll support will be added) we will create a custom entry point that decrypts the real one on startup (!!! doesn't work when beeing manual mapped).
[![imgmaincfg](https://github.com/weak1337/Alcatraz/raw/master/images/customentry.PNG)](https://github.com/weak1337/Alcatraz/blob/master/images/customentry.PNG)

### Lea obfuscation

The lea obfuscation is quite simple yet effective. We move a different location into the register and decrypt it afterwards. This way, reverse engineers can't cross reference certain data / functions.
Let's say we find the following instruction: `lea rcx, [0xDEAD]`
We will mutate it to:

```
pushf
lea rcx, [1CE54]
sub rcx, EFA7
popf

rcx -> 0xDEAD
```

### Anti disassembly

If we find an instruction that starts with the byte 0xFF we will put a 0xEB infront of it.
We do this because 0xEB 0xFF encodes to jmp rip + 1 which, in the end, jumps to our actual first 0xFF. This will throw off tools that decode instructions in a linear way.
Before:
[![imgffbefore](https://github.com/weak1337/Alcatraz/raw/master/images/ffbefore.PNG)](https://github.com/weak1337/Alcatraz/blob/master/images/ffbefore.PNG)
After:
[![imgffafter](https://github.com/weak1337/Alcatraz/raw/master/images/ffafter.PNG)](https://github.com/weak1337/Alcatraz/blob/master/images/ffafter.PNG)

From time to time we can insert:

IDA will try to decode the 0xE8 (call) but won't have any success:
[![imgjz](https://github.com/weak1337/Alcatraz/raw/master/images/jzobf.PNG)](https://github.com/weak1337/Alcatraz/blob/master/images/jzobf.PNG)

### Import obfuscation

There is no "proper" IAT obfuscation at the moment. The 0xFF anti disassembly trick takes care of it for now. Proper implementation is planned here:
[iat.cpp](https://github.com/weak1337/Alcatraz/blob/master/Alcatraz/obfuscator/misc/iat.cpp)

### Final result

This is a snippet of our `main` function with everything except anti disassembly enabled (so IDA can create a function):
[![imgfinal](https://github.com/weak1337/Alcatraz/raw/master/images/final.PNG)](https://github.com/weak1337/Alcatraz/blob/master/images/final.PNG)

ж–Үз« жқҘжәҗ: https://github.com/weak1337/Alcatraz
 еҰӮжңүдҫөжқғиҜ·иҒ”зі»:admin#unsafe.sh

© [unSafe.sh - дёҚе®үе…Ё](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [е®үе…Ёй©¬е…Ӣ](https://aq.mk)
* [жҳҹйҷ…й»‘е®ў](https://xj.hk)
* [T00ls](https://t00ls.net)