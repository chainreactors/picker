---
title: GDB Commands Cheatsheet
url: https://buaq.net/go-137241.html
source: unSafe.sh - 不安全
date: 2022-11-26
fetch_date: 2025-10-03T23:47:17.687333
---

# GDB Commands Cheatsheet

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

![]()

GDB Commands Cheatsheet

# Open a file with GDBgdb ./file#quitegdb -q .file#run the processrrun#run a processr 127
*2022-11-25 23:45:0
Author: [www.hackingdream.net(查看原文)](/jump-137241.htm)
阅读量:30
收藏*

---

```
# Open a file with GDB
gdb ./file

#quite
gdb -q .file
```

```
#run the process
r
run

#run a process
r 127.0.0.1 -c 1

#run PID; -q is for quiet mode
gdb -q -p 1200

#List the functions
info functions

#find functions using readelf; you can find "Entry point address:"
shell readelf -h DataTypes

#shows disassembly
disas [func name]

#setup breakpoint
break
break *0xaddress
break _start
break _functionName

#set a break point after a number of instructions of the function
break *&_start +59
break *&_FunctionName +LineNumber

#display content; func name, registers or variable
print [obj name]

#displays info about register
info [name]

#step over: into a program until it reaches next source line
step

#stepinto  - step into exactly one instruction
stepi

#Single step into program with just enter key
nexti

#display memory locations
x/[number of units][data type][location name]
b=bytes
h=word
w= double word

#displays 20 words strating from where esi points to
x/20w $esi
#displays 10 instructions starting fromwhere EIP points to
x/10i $eip

#change syntax high lighting
set disassembly-flavor intel

#run an exec with its core dump
 gdb -q ./vuln ./core

#view ecx
display /x $ecx
display /x $cx
display /x $cl

#view registers info
info registers

#show all registers
info all-registers

#list variables
info variables

#show memory processes mappings
break main
run
info proc mappings

#Get value of an address
x/s 0x80490a4
x/xb 0x80490a4
x/xb &var1

#Get sequence of 3 bytes
x/3xb &var1

#get the address of a variable/register
print &var1
print/x $eax
```

```
#Execute a set of commands automatically in GDB

#Execute commands whenever the program stops
define hook-stop
print/x $eax
print/x $ebx
print/x $ecx
x/8xb &sample
disassemble $eip,+10
end

-------------------
x/8xb $esp
x/4xh $esp
x/2xw $esp
disassemble $eip,+1
------------------------

#use display to print a set of instructions everytime a program stops
#display shows the register/lable name unlike print and not required to define hook
display/x $eax
display/x $ebx
display/x $ecx

define hook-stop
>print/x $eax
>x/xb &var1
>x/xh &var2
>x/xw &var3
>print $eflags
>disassemble $eip,+10
>end
```

```
#Get all shellcode on binary file from objdump
objdump -d ./PROGRAM |grep '[0-9a-f]:'|grep -v 'file'|cut -f2 -d:|cut -f1-6 -d' '|tr -s ' '|tr '\t' ' '|sed 's/ $//g'|sed 's/ /\\x/g'|paste -d '' -s |sed 's/^/"/'|sed 's/$/"/g'
```

文章来源: https://www.hackingdream.net/2022/11/gdb-commands-cheatsheet.html
 如有侵权请联系:admin#unsafe.sh

© [unSafe.sh - 不安全](https://unsafe.sh) Powered By [PaperCache](https://github.com/code-scan/PaperCache)

* admin#unsafe.sh
* [安全马克](https://aq.mk)
* [星际黑客](https://xj.hk)
* [T00ls](https://t00ls.net)