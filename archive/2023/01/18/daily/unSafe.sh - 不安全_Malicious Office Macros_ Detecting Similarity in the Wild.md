---
title: Malicious Office Macros: Detecting Similarity in the Wild
url: https://buaq.net/go-145945.html
source: unSafe.sh - 不安全
date: 2023-01-18
fetch_date: 2025-10-04T04:07:31.171550
---

# Malicious Office Macros: Detecting Similarity in the Wild

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

![](https://8aqnet.cdn.bcebos.com/bf0698b7f16aaac49832991d71b73ec1.jpg)

Malicious Office Macros: Detecting Similarity in the Wild

Many security solutions employ signature-based detection. To bypass this, attackers often rely o
*2023-1-17 20:7:19
Author: [perception-point.io(查看原文)](/jump-145945.htm)
阅读量:18
收藏*

---

Many security solutions employ signature-based detection. To bypass this, attackers often rely on existing malicious samples to create new samples that preserve the original malicious behavior but have distinct signatures. This is usually done with the help of malware toolkits which can perform various transformations such as: obfuscation, packing, name shuffling, patching, etc. The resulting samples are generated with a unique signature that is previously unseen, but may still be similar to known malicious samples.

Therefore, detecting similarity between samples is an important capability for modern security solutions for a few reasons. First, similarity detection can improve malware detection: If a given sample is similar enough to previously seen samples that were already flagged as malicious, then it is very likely to be malicious as well. Second, similarity detection can help to automate the task of identifying malicious campaigns, which are often based on similar variants of the same malicious sample.

In this blog, we focus on similarity in the context of Microsoft Office macros, which are widely exploited by attackers as a platform for delivering [malware](https://perception-point.io/blog/attack-trends/how-to-prevent-malware-attacks/). We will discuss several patterns of similarity based on *real-world* samples that we detected in the wild, and we will briefly describe our solution.

## Office Macros: Background

A macro is a special-purpose program embedded in a Microsoft Office document (Word, Excel, PowerPoint, etc.) which is used to automate various tasks such as keyboard strokes and mouse movements. A macro consists of modules written in VBA which is a powerful [imperative programming](https://en.wikipedia.org/wiki/Imperative_programming) language. A macro can access various machine resources: It can read and write to the file system, use the network, and execute commands. The execution of a macro is usually triggered by a callback function which is invoked when a specific event occurs. For example, the following macro is triggered when the (Word) document is opened, and executes a command that runs *calc.exe*:

![](https://perception-point.io/wp-content/uploads/1-13-e1673956622634.png)

The versatility and expressiveness of VBA is what attracts attackers to use macros as a component in the infection flow.

## Similarity Patterns: Examples

In this section, we will discuss several similarity patterns that we observed in samples from our clientsֵ’ traffic.

### Identifier Shuffling

One way to obtain different variants of the same malicious macro is by renaming identifiers: functions, variables, etc. This produces distinct macros which are semantically equivalent, that is, exhibit the same behavior. To illustrate this, let’s have a look at two malicious macros ([1], [2]) that we detected in our clients’ traffic. In both cases, the macro was contained in an Microsoft Office document that was delivered as an email attachment.

## ![](https://perception-point.io/wp-content/uploads/2-16-e1673956651873.png)

As you can see, these two macros are identical up to the names of some functions and variables. The matching identifiers are marked here in the same color. For example, the variable *KYjo* in the first macro (on the left) corresponds to the variable *kBHE* in the second macro (on the right).

Here, the identifier renaming has clearly no effect on the behavior. Both macros use the built-in callback function *Worksheet\_Change* to initiate the malicious flow which is obfuscated using various properties of the embedding document (page setup, spreadsheet cells, etc.).

After deobfuscation, the malicious flow can be described as follows:

First, an ActiveX object is created by invoking the *CreateObject* API with the *winmgmts:Win32\_Process* class (line X). Then, the arguments (*CommandLine* and *ProcessStartupInformation*) for the *Create* method of the WMI class are constructed (line X), where the *CommandLine* argument contains the command to be executed. Finally, the function *fkldf* is called and the method *Create* is invoked with the constructed arguments (line X), which leads to the execution of a PowerShell command that downloads and executes a malicious JavaScript payload.

### Modifying Constants

Another way to obtain different variants of the same malicious macro is by modifying constants (i.e. strings, integers, etc). Malicious macros often construct strings in an obfuscated manner, and then use them to execute commands or access the network in a later stage. This is done in the following sample ([3]), which was detected in one of our clients’ traffic:

![](https://perception-point.io/wp-content/uploads/3-14-e1673956683390.png)

In this macro, the function *TCONETC* first defines an obfuscated constant string (line X), and then uses the *Replace* API to perform several transformations (lines X) which eventually result in a PowerShell command that will be executed later in the function *Auto\_open* using the *Shell* API.

Such attacks often re-appear in slightly different configurations. The main logic for constructing the strings is reused, and only the initial input is patched in order to modify the parameters of the attack: network locations, executed commands, etc.

We observed that in other attacks that we prevented across different clients. In one of the detected samples ([4]), the macro differs from the previously mentioned macro ([3]) only in the first command of the function *TCONETC*:

![](https://perception-point.io/wp-content/uploads/4-12-e1673956734110.png)

As you can see, the difference is in the section of the initial string that corresponds to the URL, since here the attacker is trying to launch the attack using a different network location.

### Reusing Primitives

As we mentioned before, many malicious macros rely on obfuscation, which is typically implemented using a sequence of encoding or decoding operations. The macros that we discussed in the previous section use slightly different constants when constructing the obfuscated strings, but they use the same encoding and decoding procedures for obfuscating the PowerShell command. We observed that some malicious macros not only modify strings, but also use different encoding or decoding procedures for implementing the obfuscation mechanism.

This can be observed in the following two macros ([5] and [6]) which were detected in our clients’ traffic. The first one is a *Word* macro (on the left) and the second one is an *Excel* macro (on the right). Each of the macros first stores some obfuscated data in the variables *Based* and *Named*, then writes the value of *Based* to the file system using the function *writeBytes*, and finally executes a command using the value of *Named*. In this case, however, each of the macros uses a different encoding procedure, that is, a different sequence of operations, to construct the obfuscated data (the values of *Named* and *Based*).

![](https://perception-point.io/wp-content/uploads/5-10-e1673956796656.png)

Despite the differences in the encoding procedures, other parts of these macros reveal some interesting similarities. First, both macros use the same decoding procedure, the function decodeBase64, which performs a standard decoding of a base64-encoded string:

!...