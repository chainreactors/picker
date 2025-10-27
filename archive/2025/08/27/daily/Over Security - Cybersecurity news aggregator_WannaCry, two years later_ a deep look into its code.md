---
title: WannaCry, two years later: a deep look into its code
url: https://blog.kartone.ninja/malware-analysis-a-wannacry-sample-found-in-the-wild-2/
source: Over Security - Cybersecurity news aggregator
date: 2025-08-27
fetch_date: 2025-10-07T00:49:18.732632
---

# WannaCry, two years later: a deep look into its code

[Kartone Infosec Blog](https://blog.kartone.ninja)

* [Home](https://blog.kartone.ninja/)
* [About me](https://blog.kartone.ninja/aboutme/)

By [Mario Ciccarelli](/author/mario/)
in
[malware analysis](https://blog.kartone.ninja/tag/malware-analysis/)
—
23 May 2019

# WannaCry, two years later: a deep look into its code

My own reverse engineering of a WannaCry sample.

![WannaCry, two years later: a deep look into its code](/content/images/size/w1200/2019/05/wannacry-screencap_thumb800-2.jpg)

My own technical analysis of the malware that, in 2017, spread like wildfire encrypting thousands of computers, using one of the tools leaked from the National Security Agency by the group named ShadowBrokers.

Almost two years passed after that weekend of May 2017, when the crypto-worm WannaCry infested the net thanks to the EternalBlue exploit. In roughly two days, WannaCry spread itself all over the world infecting almost 230.000 computers in over 150 countries:

![](https://blog.kartone.ninja/content/images/2019/05/Countries_initially_affected_in_WannaCry_ransomware_attack.svg)

By TheAwesomeHwyh

At that time, working as an Information Security Officer, with my colleagues, especially the guys from IT Infrastructure dept., worked hard to keep the entire Company perimeter safe. Luckily for us, we were not hit by the ransomware, but a lot of effort was spent explaining to the rest of the Company what happened.

### Flash forward to 2019

Since this January, I've been running my own Dionaea honeypot that keeps catching a huge number of WannaCry samples. Just to give you some numbers, within two months, the 445 port was hit almost half a million times and I was able to collect roughly 18.000 of its samples at the rate of almost 300 samples per day.

![](https://blog.kartone.ninja/content/images/2019/05/image.png)![](https://blog.kartone.ninja/content/images/2019/05/image-1.png)

If you notice from the file size, all these samples are all the same, and everyone of them is a WannaCry sample, delivered right to the 445 port in a DLL fashion.

![](https://blog.kartone.ninja/content/images/2019/05/image-2.png)

Just to make a contribution to the WannaCry story, though small and useless, I thought it would be fun to analyze the internals of this malware as I wasn't able to do it back in the days. I will concentrate the analysis on its various layers and the most important parts of the code that make this malware unique.

## Peeling the onion

First look at one of these samples, confirms that we're dealing with a malicious DLL and it's worth to note its compilation timestamp. Let's call this as `launcher.dll` because of the evidence found in a string inside the code.

![](https://blog.kartone.ninja/content/images/2019/05/image-3.png)![](https://blog.kartone.ninja/content/images/2019/05/image-12.png)

Luckily for us, this sample is not packed. We can check its **Import and Export Address Table** to get an idea of what this sample is able to do.

![](https://blog.kartone.ninja/content/images/2019/05/image-4.png)

Easily enough, checking the imported API, we can assume that the malware uses something in its **resource** **section** and supposedly create a file and run a process. Commonly, DLL malware exports functionalities to the outside via its **Export Address Table**. We can see only one exported function and it's called **PlayGame***:*

![](https://blog.kartone.ninja/content/images/2019/05/image-5.png)

As noted above, malware imported some specific APIs to manage its resource section, like `FindResourceA` and `LoadResource`. We can easily recognize the *magic numbers* of a Portable Executable file - a Windows executable file - stored inside this section. We can dump it easily with tools like ResourceHacker:

![](https://blog.kartone.ninja/content/images/2019/05/image-6.png)

But before analyzing it, we need to get rid of *some* bytes in the header, we'll come to these bytes later.

![](https://blog.kartone.ninja/content/images/2019/05/image-7.png)

So now, we can open it and check its sections like we just did with the aforementioned DLL. Interestingly this new dumped executable seems 7 years older than the first one, its compile timestamp is dated November 2010 but, be aware that this date can be easily fake.

![](https://blog.kartone.ninja/content/images/2019/05/image-8.png)

We can get an idea of what its purpose is by checking out the imported libraries:

![](https://blog.kartone.ninja/content/images/2019/05/image-10.png)

We have to expect much more complexity in this stage than the DLL. We have a bunch of standard libraries like `KERNEL32.dll` or `WININET.dll` and `iphlpapi.dll`. This DLL was unknown for me so I found, from [MSDN](https://docs.microsoft.com/en-us/windows/desktop/iphlp/ip-helper-start-page), that:

> *Purpose*
> The Internet Protocol Helper (IP Helper) API enables the retrieval and modification of network configuration settings for the local computer.
> The IP Helper API is applicable in any computing environment where programmatically manipulating network and TCP/IP configuration is useful. Typical applications include IP routing protocols and Simple Network Management Protocol (SNMP) agents.

![](https://blog.kartone.ninja/content/images/2019/05/image-9.png)

A quick look suggests that this executable operates with Windows services configuration, manages files and resources and also, has network capabilities:

![](https://blog.kartone.ninja/content/images/2019/05/image-11.png)

### The Plan

My plan is to give a deep look inside all various stages that the malware extracts during its execution, analyzing its code and how it interacts with internal Windows subsystems.

For this reason, we're now stepping back to analyze and understand how the DLL extracts this executable in the first place. Then we'll give a look inside the debugger to see how things happen in realtime and then, we will analyze and try to understand what this executable is going to do once it infects the system.

### Analysis of the first layer: launcher.dll

The purpose of this DLL is exactly what we supposed thanks to the analysis of the imported libraries. The only exported function `PlayGame` is easily disassembled by IDAPro.

![](https://blog.kartone.ninja/content/images/2019/05/image-13.png)

The first call to `sprintf` compose the `Dest` string as `C:\WINDOWS\mssecsvc.exe`. Then it calls two functions, `sub_10001016` that extracts, from its resource section, the executable we dumped before and then, saves it into a new file named as `Dest` string; after that `sub_100010AB` runs the file. Notice that we have just gained our first **host-based indicator**: **`C:\WINDOWS\MSSECSVC.EXE`** for this malware detection.

#### Function `sub_10001016` aka `ExtractAndCreate`

For better reading and understanding this function, we can rename it as `ExtractAndCreate` and we can split it into two parts: the *extract* part and the *create file* part.

![](https://blog.kartone.ninja/content/images/2019/05/image-14.png)

Disassembled extract part

During this phase, the malware uses four API calls, that are completely covered inside the MSDN.

* `FindResourceA`: *Determines the location of a resource with the specified type and name in the specified module.*
* `LoadResource`: *Retrieves a handle that can be used to obtain a pointer to the first byte of the specified resource in memory.*
* `LockResource`: *Retrieves a pointer to the specified resource in memory.*
* `SizeOfResource`: *Retrieves the size, in bytes, of the specified resource.*

That being said, we can now analyze step by step this simple four blocks of code. First function prototype is:

```
HRSRC FindResourceA(
  HMODULE hModule,
  LPCSTR  lpName,
  LPCSTR  lpType
);
```

We have three function parameters that, as per calling convention, must be pushed in reverse order, so:

```
push    offset Type ; "W"
push    65h ; lpName
push    hModule ; hModule
call    ds:FindResourceA
```

Parameter `hModule` is being populated in...