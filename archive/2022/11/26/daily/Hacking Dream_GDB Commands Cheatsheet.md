---
title: GDB Commands Cheatsheet
url: https://www.hackingdream.net/2022/11/gdb-commands-cheatsheet.html
source: Hacking Dream
date: 2022-11-26
fetch_date: 2025-10-03T23:49:37.580443
---

# GDB Commands Cheatsheet

* [Home](http://www.hackingdream.net)
* [About Author](http://www.hackingdream.net/p/about-author.html)
* [Contact US](http://www.hackingdream.net/p/contact-us.html)

[# ![Hacking Dream](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgI3MZul9awsB7xmLlAs9J9xDOsiYxbMQoa4EQkvg9T9oe4q5zkZRqV0W4UN2KhrQQWPLveTvQ9kkuHu2HfrahqY0Gc53G1cVCwQNY2G3MVkEOJoDvLIK9lFtBUc-HhRciiteWdHYV4SaE/s1600/Size-Modified.png)](https://www.hackingdream.net/)

Main menu

close

* [Home](http://www.hackingdream.net)
* [AI Sec](https://www.hackingdream.net/search/label/AI)
* [AI Pentest](http://www.hackingdream.net/search/label/AI%20Attacks)
* [Cheatsheets](https://www.hackingdream.net/search/label/Cheatsheet)
* [Pentest](https://www.hackingdream.net/search/label/Pentest)
* [\_Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)
* [\_Linux](http://www.hackingdream.net/search/label/Kali%20Linux)
* [\_Wireless](http://www.hackingdream.net/search/label/Wifi%20Hacking)
* [\_Target Hacking](http://www.hackingdream.net/search/label/Target%20Hacking)
* [Purple Team](https://www.hackingdream.net/search/label/Purple%20Team)
* [Bin Exp](https://www.hackingdream.net/search/label/Exploitation)
* How To
* [\_Blogging](http://www.hackingdream.net/search/label/Blogging)
* [\_Solved Problems](http://www.hackingdream.net/search/label/Solved%20Problems)
* [\_Money Making](http://www.hackingdream.net/search/label/Money%20Making)
* [\_Top Ten](http://www.hackingdream.net/search/label/Top%20Ten)
* [\_Gaming](http://www.hackingdream.net/search/label/Games)

### GDB Commands Cheatsheet

[November 25, 2022](https://www.hackingdream.net/2022/11/gdb-commands-cheatsheet.html "permanent link")

[![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2GN0KXCOSkSZY_-8Xccz70AQTzEzdF6YuIW1L9q1OV14Xadcq_9x1gnpPF7i0w6-Rud5qi-Z-6CjK2Z9Yud2SiBLZ7MIBGf254skyU6czr1EGi2HqIn2WNiP1qdh5LZE_xfXVDF2CAUB5aPE__6AUgcOor0oqAdDR_2jstHgTDMI5h00ZEEP8NNJWWDQ/w640-h366/GDB-commands-Cheatsheet.jpg)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj2GN0KXCOSkSZY_-8Xccz70AQTzEzdF6YuIW1L9q1OV14Xadcq_9x1gnpPF7i0w6-Rud5qi-Z-6CjK2Z9Yud2SiBLZ7MIBGf254skyU6czr1EGi2HqIn2WNiP1qdh5LZE_xfXVDF2CAUB5aPE__6AUgcOor0oqAdDR_2jstHgTDMI5h00ZEEP8NNJWWDQ/s1024/GDB-commands-Cheatsheet.jpg)

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
break _FuncName+500

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

#list the string inside of a register
display /s $eax
x/s $eax

#list the decimal
display /d $eax

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

[![](https://img1.blogblog.com/img/icon18_email.gif)](https://www.blogger.com/email-post/7320167475718896234/3407913677178182957 "Email Post")

[Cheatsheet](https://www.hackingdream.net/search/label/Cheatsheet)

By:
Bhanu Namikaze

![](//lh5.googleusercontent.com/-5klQY__bhSE/AAAAAAAAAAI/AAAAAAAAFfc/f8794NZCX3M/s512-c/photo.jpg)

##### Bhanu Namikaze

Bhanu Namikaze is an Ethical Hacker, Security Analyst, Blogger, Web Developer and a Mechanical Engineer. He Enjoys writing articles, Blogging, Debugging Errors and Capture the Flags. Enjoy Learning; There is Nothing Like Absolute Defeat - Try and try until you Succeed.

#### No comments:

#### Post a Comment

## Search for a Post

## Recent Posts

[Recent Posts Widget](http://www.hackingdream.net/2015/12/recent-post-widgets-for-blogger-with-thumbnails.html)
Your browser does not support JavaScript!

## Popular Posts

[Recent Posts Widget](http://www.hackingdream.net/2015/12/recent-post-widgets-for-blogger-with-thumbnails.html)
Your browser does not support JavaScript!

* [facebook](http://www.facebook.com/HackingDream)
* [twitter](http://www.twitter.com/HackingDream)
* [youtube](https://www.youtube.com/channel/UCKgOUVTaT-6LKLvUQhfBhig)

## About us

![about footer](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgPNiXyJNB8w-IovFpOQWeftMUoBrVjS1T-fL9Xe9iixFQvIijmZC4TC0j8Y8E384vrStxGn58Etcw-KbG-ISpaK5eL3payYyjd84WHa9Ps9GQUFd0qToRbnLzW4Sz4R5s46i73WmcJvPQb/s1600/Size-Modified.png)

## Labels

[Active Directory](https://www.hackingdream.net/search/label/Active%20Directory)

[AI](https://www.hackingdream.net/search/label/AI)

[AI Attacks](https://www.hackingdream.net/search/label/AI%20Attacks)

[Andriod](https://www.hackingdream.net/search/label/Andriod)

[Android](https://www.hackingdream.net/search/label/Android)

[AppSec](https://www.hackingdream.net/search/label/AppSec)

[BackTrack](https://www.hackingdream.net/search/label/BackTrack)

[Blogging](https://www.hackingdream.net/search/label/Blogging)

[Buffer Overflow](https://www.hackingdream.net/search/label/Buffer%20Overflow)

[C Programs](https://www.hackingdream.net/search/label/C%20Programs)

[Certifications](https://www.hackingdream.net/search/label/Certifications)

[Cheatsheet](https://www.hackingdream.net/search/label/Cheatsheet)

[Courses](https://www.hackingdream.net/search/label/Courses)

[Cracked Softwares](https://www.hackingdream.net/search/label/Cracked%20Softwares)

[Cracking Passwords](https://www.hackingdream.net/search/label/Cracking%20Passwords)

[Cyber Security](https://www.hackingdream.net/search/label/Cyber%20Security)

[Ethical Hacking](https://www.hackingdream.net/search/label/Ethical%20Hacking)

[Exploitation](https://www.hackingdream.net/search/label/Exploitation)

[Facebook Hacking](https://www.hackingdream.net/search/label/Facebook%20Hacking)

[Facebook Tricks](https://www.hackingdream.net/search/label/Facebook%20Tricks)

[Featured](https://www.hackingdream.net/search/label/Featured)

[Forensics](https://www.hackingdream.net/search/label/Forensics)

[Games](https://www.hackingdream.net/search/label/Games)

[Hacking](https://www.hackingdream.net/search/label/Hacking)

[Hacking News](https:/...