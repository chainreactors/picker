---
title: Advanced Phobia
url: https://labs.yarix.com/2022/12/advanced-phobia/
source: Over Security - Cybersecurity news aggregator
date: 2022-12-23
fetch_date: 2025-10-04T02:21:14.101565
---

# Advanced Phobia

[![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)![YLabs](//labs.yarix.com/wp-content/uploads/2021/01/yarix_logo.png)![YLabs](//labs.yarix.com/wp-content/uploads/2025/01/Logo_Yarix.png)](https://labs.yarix.com/ "YLabs - Research & Development")

* [Home](https://labs.yarix.com/)
* [Blog](https://labs.yarix.com/category/blog/)
* [Advisories](https://labs.yarix.com/advisories/)
* [Careers](https://www.yarix.com/job-opportunity/)

# Advanced Phobia

* [Home](https://labs.yarix.com "Go to Home Page")
* Advanced Phobia

[Back to Posts](https://labs.yarix.com)

![](https://labs.yarix.com/wp-content/uploads/2022/12/Blog-1140x445.jpg)

22Dec22/12/2022

## Advanced Phobia

[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")2022-12-22T17:02:55+01:00

By
[Ylabs](https://labs.yarix.com/author/ylabs/ "Posts by Ylabs")

Reading Time:   8 minutes

# Ransomware Gang Details

Phobos ransomware, first discovered in December 2018, is another notorious cyber threat actor which targets businesses.

Phobos is popular among threat actors because of its simple design. In addition, the Greek god Phobos was thought to be the incarnation of fear and panic: the gang’s name was likely inspired by him.

Phobos is a ransomware infection that spreads through hijacked Remote Desktop (RDP) connections. This isn’t surprising, given that hacked RDP servers are a cheap commodity on the underground market and can be an appealing and cost-effective distribution route for threat actors.

Additionally, Phobos is not packed or obfuscated, unlike the majority of malware which is secured by a crypter. Although the absence of packing is not frequent in the general population of malware, it is widespread among malware that is manually distributed by attackers.

##### Observed Targets Industries

Unlike other gangs that look for medium/enterprise targets, Phobos team usually go after smaller firms that don’t have the financial wherewithal to pay massive ransoms. Phobos is standard ransomware that offers little in innovation. They do not use the double extortion approach, indeed there have been no reports of any underground leak sites revealing confidential information about their targets. This threat is most likely inserted to influence the victim, capitalizing on worries sparked by other high-profile ransomware attacks.

# INTRODUCTION

##### Yarix Response Team First Engagement

Yarix’s Research Labs (YLABS) in a previous blog post called “Phobia” has analyzed a specific binary related to Phobos ransomware to check if it does only decrypt the data encrypted by it; as expected the payload turned out to be a funny one, full of insidious functionalities that can be seen only through advanced techniques.

In this article the task is to pick up where it has been left off in the previous post, uncovering what still remains obscure.

Now let’s dive into it!

# Malware Analysis

The analysis of the malware found by the YIR team (Yarix Incident Response Team) has been divided in two articles, you can find the first part that comprehend “Static” and “Dynamic” analysis by clicking [HERE](https://labs.yarix.com/2022/11/phobia/).

If you already read the first article and want to dive into the “nerdy stuff”, keep reading.

## Advanced Dynamic Analysis (Functions Walkthrough)

### Anti-Debugging Function

After the execution started and some code has already been executed the payload starts to look for injected code or debuggers through a dedicated function that has been highlighted with the “DEBUGGER AWARE FUNCTION” comment as you can see in the screenshot below

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x52.jpg)

Advanced Dynamic Analysis – Anti-Debugging & Code Injection Function

To avoid that check the binary has been patched with a “jmp” instruction to the next code section.

### Keyboard Language Detection Routine

As we know, every advanced malware always does some checks on the infected target’s environment. Also in this case some nice Keyboard Language Checks could not be missing in order to determine the origin of the infected host; following screenshots show some of the methods that have been found during debugging activities

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x13.jpg)

Advanced Dynamic Analysis – GetKeyboardType

GetKeyboardType call as the name says, gets some informations about the keyboard layout and settings

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x15.jpg)

Dynamic Analysis – language value check (Reg – HKCU)

Some checks in the registry were made in the current user hive to retrieve additional informations about utilized Keyboard

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x21.jpg)

Advanced Dynamic Analysis – language value check (Reg – HKLM)

Additionally, the following strings has been found inside the binary

```
ANSI_CHARSET, DEFAULT_CHARSET, SYMBOL_CHARSET, MAC_CHARSET, SHIFTJIS_CHARSET, HANGEUL_CHARSET, JOHAB_CHARSET, GB2312_CHARSET, CHINESEBIG5_CHARSET, GREEK_CHARSET, TURKISH_CHARSET, HEBREW_CHARSET, ARABIC_CHARSET, BALTIC_CHARSET, RUSSIAN_CHARSET, THAI_CHARSET, EASTEUROPE_CHARSET, OEM_CHARSET, DEFAULT_CHARSET
```

Anyway, those charsets strings have never been compared during the observed malware execution. However many advanced malware samples utilize “noise” code and functions just to misdirect payload’s debugging; so the analysts gets to follow rabbit holes that make analysis longer in terms of time and harder to comprehend.

### File Patching Routine

During debugging and reverse engineering operations many hidden functions have been highlighted by the defenses implemented to protect them like infinite loop functions and methods that throw an exception if certain conditions are not met during execution. One of these “Hidden Routines” is the “File Patching Routine” that basically takes a x86 Binary and appends two payloads inside it, effectively creating a matryoshka where the malware from that moment on will puppet the execution of the real infected file.

Let’s see how it works step by step!

The biggest portion of the malicious code resides on top of the file meanwhile the second one closes the original binary with some uncommon B64 artifacts

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x267.jpg)

Advanced Dynamic Analysis – Patched file structure

Looking at the process with a common “Process Monitor” like sysinternal’s one we can see how it takes the current binary that has to be patched, moves it into temp, applies the patches and then it proceed by copying it in the original location

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x47.jpg)

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x46.jpg)

Advanced Dynamic Analysis – Process Monitor File Patching routine

The function that does this dirty work is located deep inside the malware routines and it is referenced with a “7-zip” string.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x28.jpg)

Advanced Dynamic Analysis – Decompression RoutineOnce the method has gone through all the instructions, we can finally appreciate the “top” payload come to light

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x46.jpg)

Advanced Dynamic Analysis – “Top” Payload

And in the same manner the one that goes at the end of the infected file gets injected into the (at this point) infected binary.

![](https://labs.yarix.com/wp-content/uploads/porto_placeholders/100x54.jpg)

Advanced Dynamic Analysis – Infected file structure differences

It’s not hard at this point to see the differences from a good binary and an infected one, below are the changes that are made by the whole file patching routine:

* Malicious resources are being copied from the infecting payload to the patched one
  + “CX” is the actual Phobos Ransomware decryption tool

![](https://labs.yarix.com/wp-content/uploads/porto_...