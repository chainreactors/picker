---
title: Cobalt Strike 4.8: (System) Call Me Maybe
url: https://buaq.net/go-152449.html
source: unSafe.sh - 不安全
date: 2023-03-08
fetch_date: 2025-10-04T08:54:15.538790
---

# Cobalt Strike 4.8: (System) Call Me Maybe

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

![](https://8aqnet.cdn.bcebos.com/0ad114d60e827b9b9fbedf1016f7e2ec.jpg)

Cobalt Strike 4.8: (System) Call Me Maybe

Cobalt Strike 4.8 is now available. This release sees support for system calls, options to spec
*2023-3-7 22:56:48
Author: [www.cobaltstrike.com(查看原文)](/jump-152449.htm)
阅读量:158
收藏*

---

Cobalt Strike 4.8 is now available. This release sees support for system calls, options to specify payload guardrails, a new token store, and more.

We had originally planned to get this release out late in 2022 but progress was stymied due to the [4.7.1](https://www.cobaltstrike.com/blog/out-of-band-update-cobalt-strike-4-7-1/) and [4.7.2](https://www.cobaltstrike.com/blog/out-of-band-update-cobalt-strike-4-7-2/) patch releases that we had to put out to fix vulnerabilities that were reported in the 4.7 release. We spent a few development cycles performing a security review of the code and working on some technical debt, and then it was the holiday season. It’s here now though, and better late than never!

Before getting into the details of this release, I just wanted to mention that you should now start to see much more content from us to supplement main product releases. [William Burgess recently released his first blog post since joining the Cobalt Strike team](https://www.cobaltstrike.com/blog/behind-the-mask-spoofing-call-stacks-dynamically-with-timers/) and he will be playing a key role in providing technical guidance on the future direction of the product. We have more blog posts and tooling coming over the next few weeks and months, starting with a series on UDRL development (the first of which should drop next week). Coming later in the year are some **huge** changes to Cobalt Strike itself. More details on that will come in a follow-up blog post soon. We know that our users are struggling with evasion and have reported other pain points. As I mentioned in my [roadmap update](https://www.cobaltstrike.com/blog/cobalt-strike-roadmap-update/) last year, we have been aggressively building out our R&D team and while it’s taken a while to do that and get all of our ducks in a row, you’ll now really start to see the benefits of those behind-the-scenes changes. Now, back to the 4.8 release.

### System Calls Support

This release sees the addition of support for direct and indirect system calls. We have added support for a number of system calls, specifically:

* *CloseHandle*
* *CreateFileMapping*
* *CreateRemoteThread*
* *CreateThread*
* *GetThreadContext*
* *MapViewOfFile*
* *OpenProcess*
* *OpenThread*
* *ResumeThread*
* *SetThreadContext*
* *UnmapViewOfFile*
* *VirtualAlloc*
* *VirtualAllocEx*
* *VirtualFree*
* *VirtualProtect*
* *VirtualProtectEx*
* *VirtualQuery*

The stageless Beacon payload generation dialog has been updated to allow you to specify the system call method to be used at execution time. The available options are:

**None**: Use the standard Windows API function

![](https://www.cobaltstrike.com/wp-content/uploads/2023/03/image-2.png)

It is important to note that there are some commands and workflows that inject or spawn a new Beacon that do not allow you to set the initial system call method. Those commands/workflows are:

* *elevate*
* *inject*
* *jump*
* *spawn*
* *spawnas*
* *spawnu*
* *teamserver responding to a stageless payload request*
* *teamserver responding to an External C2 payload request*

The **stage.syscall\_method** in the MalleableC2 profile controls the method used at execution time, and you can use the **syscall-method [method]** command to modify the method that will be used for subsequent commands. Additionally, **syscall-method** without any arguments will query and return the current method.

System call support is something that we intend to continue to update and enhance in future releases. Your feedback on this is welcomed.

### Generate Payloads With Built-In Guardrails

Support has been added for payload guardrails, which can be set at the listener level and then, if required, overridden when generating a payload.

Guardrails can be set based on the following criteria:

* **IP address**: This can be a single IP address or a range using a wildcard to replace the rightmost octet(s). For example, 123.123.123.123, 123.123.123.\*, 123.123.\*.\* and 123.\*.\*.\* are all valid inputs. 123.\*.123.\* is not.
* **Username**: This can be a specific username, or you can prefix/suffix a wildcard (i.e. \*user or user\*). The username field is case insensitive.
* **Server name**: Again, this can be a specific server name, or you can prefix/suffix a wildcard (i.e. \*server or server\*). The server name field is case insensitive.
* **Domain**: As with username and server name, the domain field can either be a specific domain or you can prefix/suffix a wildcard (i.e. \*domain or domain\*). The domain name field is also case insensitive.

The listener dialog has a new “Guardrails” option at the bottom of the screen that allows you to set and update guardrails for that listener.

![](https://www.cobaltstrike.com/wp-content/uploads/2023/03/image-5.png)
![](https://www.cobaltstrike.com/wp-content/uploads/2023/03/image-3.png)

When generating a payload, the guardrails value from the associated listener is used as a default value.

![](https://www.cobaltstrike.com/wp-content/uploads/2023/03/image-8.png)
![](https://www.cobaltstrike.com/wp-content/uploads/2023/03/image-7.png)

You can use the default values or override them to set specific values for the payload being created. Setting specific values here does not change the default values set at the listener level.

### Multi-Byte Support For Obfuscating Beacon’s Reflective DLL’s Import Table

We have made a change to the obfuscation routine used for the **stage.obfuscate** MalleableC2 option which relates to how Beacon’s Reflective DLL’s import table is obfuscated.

Part of this process involved moving from a fixed, single byte XOR key to a randomly generated multi-byte XOR key. The single byte XOR mask was easily signatured and caught by tools such as YARA. Moving to a randomly generated multi-byte XOR key should help address those issues.

### Sleep Mask Updates

A number of updates have been made to the Sleep Mask. The main change is that the Sleep Mask size limit has been increased from 8192 to 16384 bytes. Other changes include:

* Support for the use of system calls with the MASK\_TEXT\_SECTION capability
* The addition of define tags for the Windows API functions to remove the need for LIBRARY$Function syntax
* The implementation of evasive sleep via stack spoofing (x64 only). Related changes include the addition of a bypass for Control Flow Guard (CFG), as well as the addition of a helper utility (*getFunctionOffset*)

### Token Store

One change that we’ve had on the backlog for a while was the addition of a token store, to facilitate the hot swapping of access tokens. Windows tokens are process specific; hence each Beacon has its own token store with its own tokens. Please be aware that those tokens are therefore only available to be used by that specific Beacon.

The token store is based around the new **token-store** command. The command supports a number of options that perform specific functions (all supported by tab completion). Available functions are as follows:

**token-store steal [pid,…] <OpenProcessToken access mask>**
This steals the token(s) from the specificed PID(s). Use commas to separate each PID. This command will steal the token and put it into the token store, but will not impersonate straight away. The **steal-and-use** command should be used for that purpose (although it should be noted that **...