---
title: UPX manual unpack: ELF and EXE
url: https://fareedfauzi.github.io/2022/01/20/UPX-manual-unpack.html
source: Over Security
date: 2026-11-02
fetch_date: 2026-11-03T08:51:34.091401
---

# UPX manual unpack: ELF and EXE

xml version="1.0" standalone="no"?

[root@fareed:~#](/ "Personal blog for research, education and note purpose.
")

* [Cheatsheets](/cheatsheets.html)
* [Archive](/archive.html)
* [About](/about.html)

# UPX manual unpack: ELF and EXE

* [Reverse-Engineering](/archive.html?tag=Reverse-Engineering)
* [Malware](/archive.html?tag=Malware)

* Jan 20, 2022

# Introduction

Recently, I’ve come across a Golang malware sample which have been packed by UPX. The sample was made to be cannot be unpack using UPX tool. So, I thinks it’s good to write a blog/note to explain how the UPX manually unpacking works.

# UPX tool doesn’t work

In the figure below, there are certain situation when the malware author makes their packed malware cannot be unpack by the UPX tool to slow down the analyst. Therefore, we need to do the manually unpacking to unpack the malware.

![image](https://user-images.githubusercontent.com/56353946/183522418-bf74f4c2-295f-49a6-848f-2f61f6367d5f.png)

As described in the figure above, when we `strings` the binary, we can see a lot of “UPX” string indicate the file packed with UPX. But, when we try to unpack it with `-d` using UPX tool, the tool saying the file is not packed with UPX.

In another case, in figure below, the windows executable has been packed and cannot be unpack by the UPX tool automatically due to some alteration. In this case, if we know how to alter back to become the original will be good. But, somehow not everyone knows which bytes to be change or alter.

![image](https://user-images.githubusercontent.com/56353946/183522501-0c06dec3-8c73-46e3-ac0f-5d0afb9abddc.png)

So, to solve this problems, manual unpacking come to the rescue!

# Tools required

The required tools to unpack the ELF will be:

1. IDA Pro
2. Linux VM.
3. OllydumpEx plugin for IDA Pro

While, unpacking EXE we going to use:

1. x32Dbg
2. OllydumpEx
3. Scylla

# ELF unpacking

## Setup OllyDumpEx for IDA Pro

1. Download the plugin [here](https://low-priority.appspot.com/ollydumpex/)
2. Copy the files into IDA Pro directory plugins.

## Set-up IDA Pro debugger

In order to dynamic analysis using IDA for ELF, we need to copy IDA linux debug server file into our Linux VM and run it. The file location is at `%IDA installation directory%/dbgsrv/linux_server64`. After you did run the `./linux_server64` and it will start listening for the connection from the IDA Pro in your host.

While in IDA, open the packed sample and we can see there are 6 functions include `start` function which are very few functions indicate the binary is packed. Select the last function from the 6 function.

![image](https://user-images.githubusercontent.com/56353946/183522774-8bf2824b-3f02-415c-be08-741e85b0a5d7.png)

This function is actually being the first callee in the `start` function.

![image](https://user-images.githubusercontent.com/56353946/183522841-d4fd226a-985d-4b23-ae58-c6e029138cf9.png)

This function will invoke few functions like sysmap, sysmmap and sysmprotect to initialize the environment to unpack the code. Scrolling down through the function and find `jmp r13` instruction then put the breakpoint at that line.

![image](https://user-images.githubusercontent.com/56353946/183522898-1182374f-6b5f-4043-92a2-edace86b3679.png)

Basically, the code `jmp r13` will transfer the RIP to the address contain in r13.

We now can start debug the sample by choose the debugger. Select `Remote Linux debugger`.

![image](https://user-images.githubusercontent.com/56353946/183523096-0151f94b-c474-43c1-ae96-6d189aeccd05.png)

In the options, make sure you put the path based on your Linux VM, not your Windows. And for the IP address, fill in with your Linux VM IP address which I suggest to use Host-only network adapter.

![image](https://user-images.githubusercontent.com/56353946/183523129-128f2f0c-f2e0-430b-a419-c68418bc4c90.png)

After done setup the configuration, click OK and then run the debugger. It then will break at the breakpoint we setup previously. If a warning pop-up, just click OK.

## Manual unpacking

Soon we run the debugger. It will stop at the breakpoint `jmp r13`.

![image](https://user-images.githubusercontent.com/56353946/183523265-74fd5591-edc6-48b7-b0cd-33e23554a8d9.png)

`Step into` and it will transfer the RIP into a new code region which the first instruction is call function. `Step into` the call function.

![image](https://user-images.githubusercontent.com/56353946/183523298-ad4d6ed8-6a9a-4cf0-9ee4-d7141d82117b.png)

Now, we arrived at another region of code.

![image](https://user-images.githubusercontent.com/56353946/183523343-004acc0f-4227-4228-bc8d-7e936d6fbabf.png)

Scroll down until you see the following assembly instruction:

```
pop     rax
jmp     qword ptr [r14-8]
```

Breakpoint at the line `jmp qword ptr [r14-8]` and continue run. Step into the `JMP` instruction then `step over` until `retn` instruction.

![image](https://user-images.githubusercontent.com/56353946/183523415-63e28f9f-462c-429b-9881-e28fa577d21a.png)

`Step over` the retn will transfer our RIP to another region of code. At this part, breakpoint at the end of the line of the assembly code which is `jmp r12`.

![image](https://user-images.githubusercontent.com/56353946/183523444-344d5a49-b0f1-4a8f-8bef-182982c2b874.png)

In the below figure, you will see IDA prompts that the RIP has been changed, which means that we have to jump back to the real start function which are OEP of the unpacked sample.

![image](https://user-images.githubusercontent.com/56353946/183523461-e0c42152-3c8f-4de1-82d0-551f9cc3c34d.png)

Then you will see real start function like figure below. This indicate we have successfully arrived at OEP of the unpacked sample.

![image](https://user-images.githubusercontent.com/56353946/183523472-9784252c-8e98-48ad-b524-bc2a213a063d.png)

At this point, open OllyDumpEx plugin at `Edit > Plugins > OllyDumpEx`. Just click `Dump` button and save the unpack file in your Windows. And click `Finish`.

![image](https://user-images.githubusercontent.com/56353946/183523505-86bcca79-4e53-49bb-981d-03b7889cfa65.png)

Now, try to run the binary. If it can be run without any error like the packed version, it’s indicate that our unpacked binary successfully unpacked. Another indicator is, to compared functions detected in IDA between the packed and unpacked version of the sample. The unpacked version will have a lot of functions like below:

![image](https://user-images.githubusercontent.com/56353946/183523519-32ee02a1-213e-49a9-a430-4fd01d5d3c19.png)

# EXE unpacking

Manually unpacking Windows executable packed with UPX is easy. Just find the “tail jump” instruction and we can start dump the executable.

## Finding the tail jump

First, load the binary in the x32dbg. And the x32dbg will pause in the module ntdll.dll. At here, just click run and the debugger will automatically stop at entry point of the sample. The first instruction for UPX packed sample should be `pushad` instruction. This instruction will pushes the contents of the general-purpose registers onto the stack.

![image](https://user-images.githubusercontent.com/56353946/183523662-cd48d527-bb09-4637-a520-7a9ee01b20b4.png)

Normally, `pushad` instruction will be pairing with `popad` at the end of the function. So, for UPX packed sample, the tail jump can be identify by looking forward the `popad` instruction which usually the tail jump is made after the `popad` instruction.

![image](https://user-images.githubusercontent.com/56353946/183523699-c2f4aa00-f228-4a0b-bf97-a906d6fec9ef.png)

Or another alternative to find tail jump, just looks for a lot of `add byte ptr ds:[eax], al` and the one `jmp` before the first `add byte ptr ds:[eax], al` is the tail jump.

Breakpoint on the tail jump, run and step into the address. Now, we arrived into the Original Entry Point.

![image](https://user-images.githubusercontent.com/56353946/183523756-e5a0e6cd-28a0-48dd-8b34-d8b007780654.png)

## Dump process

The packed sample now has been unpa...