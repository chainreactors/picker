---
title: Reverse Engineering Walkthrough | Analyzing A Sample Of Arechclient2
url: https://buaq.net/go-172259.html
source: unSafe.sh - 不安全
date: 2023-07-18
fetch_date: 2025-10-04T11:52:41.516496
---

# Reverse Engineering Walkthrough | Analyzing A Sample Of Arechclient2

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

![](https://8aqnet.cdn.bcebos.com/e86aea2119a193ef6cf395654d1d7e75.jpg)

Reverse Engineering Walkthrough | Analyzing A Sample Of Arechclient2

In partnership with vx-underground, SentinelOne recently ran its first Malware Research Challenge,
*2023-7-17 22:23:4
Author: [www.sentinelone.com(查看原文)](/jump-172259.htm)
阅读量:32
收藏*

---

In partnership with [vx-underground](https://twitter.com/vxunderground), SentinelOne recently ran its first [Malware Research Challenge](https://www.sentinelone.com/lp/vx-s1/), in which we asked researchers across the cybersecurity community to submit their research to showcase their talents and bring their insights to a wider audience.

In today’s post, Millie Nym demonstrates a problem-solving approach to reverse engineering a malware sample, highlighting not just the practical steps taken but also the logical reasoning conducted as the investigation unfolded. The post offers a fascinating insight into how researchers tackle the challenges in front of them and a perfect example for anyone wishing to learn or develop their reverse engineering skills.

![](https://www.sentinelone.com/wp-content/uploads/2023/07/RE-Walkthrough-Analyzing-A-Sample-Of-Arechclient2.jpg)

In this post, I will be going over my process of analyzing a sample of ArechClient2. Including initial analysis, deobfuscation and unpacking of the loader. Followed by the analysis of the .NET payload revealing its config and C2 information.

It began with [this tweet](https://twitter.com/Gi7w0rm/status/1614440406405496836) by [@Gi7w0rm](https://twitter.com/Gi7w0rm). They mentioned me and a few others asking for help analyzing this sample. I decided to look into the sample. After publishing some threat intel and a few updates on my progress on Twitter, I decided to write this report for a more detailed documentation of my analysis. The original sample can be found [here](https://tria.ge/230115-by7fcscb6w).

## Initial Analysis

The sample consists of two files, an executable and an `a3x` file. After some quick research, I found that `a3x` is a “compiled” form of AutoIt script. The executables icon is the logo of AutoIt and the copyright information says it’s AutoIt. This leads me to believe that this executable is the runtime required to execute the `a3x` file.

I ran the file in a Windows Sandbox for some quick intel and immediately got a Windows Defender hit for `MSIL:Trojan`, which indicates that this AutoIt part is just a loader for a second stage .NET binary. In case you are not familiar with the terms, “MSIL” stands for Microsoft Intermediate Language, which is the bytecode that .NET binaries are compiled to.

The `a3x` script is human-readable, so after putting it into Visual Studio Code I saw this.

![](https://www.sentinelone.com/wp-content/uploads/2023/07/MillieNym_6.jpg)

It looks pretty messy at first but taking a closer look I found something that stuck out: The calls to the function called `DoctrineDrama` look suspiciously like string decryption. So my next step was to find that function. I used the search function to look for its name until I found the actual implementation. All functions start with the keyword `Func` and end with the keyword `EndFunc`, making it easy to identify them. I copied the code of the `DoctrineDrama` function to a separate file. The code is obfuscated and seems to contain some junk code. My first step was to indent the code for easier readability.

![](https://www.sentinelone.com/wp-content/uploads/2023/07/MillieNym_7.jpg)

Looking at the switch cases inside the loops, I realized that only the branches that use `ExitLoop` are of importance. Taking a look at the switch conditions confirmed that suspicion. At the beginning of the function, the second variable is the loop condition,  initialized with a value of `921021`. Looking at the switch, it matches the case that exits the loop, meaning the other cases are dead code and can be ignored. I removed the dead branches, cleaned up the unnecessary loops and got rid of the unused variables:

![](https://www.sentinelone.com/wp-content/uploads/2023/07/MillieNym_13.jpg)

After cleaning up we are left with this code. Reading this we can deduce some more fitting variable names, the first argument seems to be the encrypted input, and the second argument is the key. The first variable is the resulting string.

To understand the rest of the code I looked at the documentation of AutoIt. The `StringSplit` function takes the following arguments:

* a string
* a delimiter char
* an optional argument for the delimiter search mode

So the second local variable in `DoctrineDrama` is an array of strings split from the input.

Next, the code iterates through all the elements of that array and appends a new character to the output string with every iteration. We see a call to a function called `Chr`, which according to documentation converts a numeric between 0-255 value to an ASCII character. But something is off, what is going on inside that call to `Chr`? Subtraction on a string, how does that work? I wondered about that but after a quick web search, I found out that in AutoIt digit strings seem to be auto-converted to a number if you perform any arithmetic operation on them. Once the loop is finished, the output string is returned.

![](https://www.sentinelone.com/wp-content/uploads/2023/07/MillieNym_14.jpg)

Looking at this fully cleaned-up version, I reimplemented the decryption routine in C# to build a simple deobfuscator.

```
static string Decrypt(string input, int key)
{
    var buffer = input.Split('h');
    var builder = new StringBuilder();
    for (int i = 0; i < buffer.Length; i++)
    {
        builder.Append((char)(Convert.ToInt32(buffer[i]) - key));
    }
    return builder.ToString();
}
```

The deobfuscator uses a simple regex pattern to match every call to `DoctrineDrama` and replace it with the decrypted string. It also outputs a list of all decrypted strings. The full deobfuscator code can be found [here](https://gist.github.com/dr4k0nia/447fb1c5c7e8791ee877fd1090a6f5e5).

## Dumping the Payload

After deobfuscating all the strings, I searched the string dump for some Windows API function names that I would expect from a loader. I found a few hits on `NtResumeThread`, `CreateProcessW` and `NtUnmapViewOfSection`. These three in combination give a huge hint towards process hollowing. After searching the string dump for `.exe` I found the suspected injection target `\Microsoft.NET\Framework\v4.0.30319\jsc.exe`, a utility of `.NET` Framework 4.x which comes with every standard Windows 10 install.

My next step was to debug the executable using x64Dbg. I set a breakpoint on `CreateProcessW`, to ensure we break before the injection process is started. After running past the entry point I was greeted with this nice little message.

![](https://www.sentinelone.com/wp-content/uploads/2023/07/MillieNym_5.jpg)

The message box claims I violated a EULA which I never read nor agreed to. I guess we can’t debug the malware any further, how unfortunate. Luckily for us, x64Dbg has a built-in AutoIt EULA bypass, it’s called Hide Debugger (PEB). You can find it under **Debug>Advanced>Hide Debugger** (PEB). Make sure to run x64Dbg in elevated mode.

After dealing with the rather simple anti-debug, we let it run. When debugged, the executable spawns a file dialog asking for an `a3x` file, when run without a debugger it automatically finds the script file. After pointing it to the script file, we let it run until the breakpoint for `CreateProcessW` is hit. At this point, `jsc.exe` will be started in suspended mode.

Checking Process Explorer confirm...