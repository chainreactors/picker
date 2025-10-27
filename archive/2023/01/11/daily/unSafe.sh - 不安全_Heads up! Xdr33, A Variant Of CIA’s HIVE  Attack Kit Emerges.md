---
title: Heads up! Xdr33, A Variant Of CIA’s HIVE  Attack Kit Emerges
url: https://buaq.net/go-144968.html
source: unSafe.sh - 不安全
date: 2023-01-11
fetch_date: 2025-10-04T03:31:00.654467
---

# Heads up! Xdr33, A Variant Of CIA’s HIVE  Attack Kit Emerges

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

![](https://8aqnet.cdn.bcebos.com/086b67adff500b19a69f20c51b3192be.jpg)

Heads up! Xdr33, A Variant Of CIA’s HIVE Attack Kit Emerges

On Oct 21, 2022, 360Netlab's
*2023-1-10 22:0:37
Author: [blog.netlab.360.com(查看原文)](/jump-144968.htm)
阅读量:38
收藏*

---

On Oct 21, 2022, 360Netlab's honeypot system captured a suspicious ELF file `ee07a74d12c0bb3594965b51d0e45b6f`, which propagated via F5 vulnerability with zero VT detection, our system observces that it communicates with IP `45.9.150.144` using SSL with **forged Kaspersky certificates**, this caught our attention. After further lookup, we confirmed that this sample was adapted from the leaked Hive project server source code from CIA. **This is the first time we caught a variant of the CIA HIVE attack kit in the wild**, and we named it `xdr33` based on its embedded Bot-side certificate `CN=xdr33`.

To summarize, xdr33 is a backdoor born from the CIA Hive project, its main purpose is to collect sensitive information and provide a foothold for subsequent intrusions. In terms of network communication, xdr33 uses XTEA or AES algorithm to encrypt the original traffic, and uses SSL with Client-Certificate Authentication mode enabled to further protect the traffic; in terms of function, there are two main tasks: beacon and trigger, of which beacon is periodically report sensitive information about the device to the hard-coded Beacon C2 and execute the commands issued by it, while the trigger is to monitor the NIC traffic to identify specific messages that conceal the Trigger C2, and when such messages are received, it establishes communication with the Trigger C2 and waits for the execution of the commands issued by it.

The functional schematic is shown below.

[![](https://blog.netlab.360.com/content/images/2022/12/hive_function.png)](https://blog.netlab.360.com/content/images/2022/12/hive_function.png)

Hive uses the `BEACON_HEADER_VERSION` macro to define the specified version, which has a value of `29` on the Master branch of the source code and a value of `34` in `xdr33`, so perhaps xdr33 has had several rounds of iterative updates already. Comparing with the HIV source code, xdr33 has been updated in the following 5 areas:

* New CC instructions have been added
* Wrapping or expanding functions
* Structs have been reordered and extended
* Trigger message format
* Addition of CC operations to the Beacon task

These modifications to xdr33 are not very sophisticated in terms of implementation, and coupled with the fact that the vulnerability used in this spread is N-day, we tend to rule out the possibility that the CIA continued to improve on the leaked source code and consider it to be the result of a cyber attack group borrowing the leaked source code.

The md5 of the Payload we captured is `ad40060753bc3a1d6f380a5054c1403a`, and its contents are shown below.

[![](https://blog.netlab.360.com/content/images/2022/12/hive_logd.png)](https://blog.netlab.360.com/content/images/2022/12/hive_logd.png)

The code is simple and straightforward, and its main purpose is to

* Download the next stage of the sample and disguise it as `/command/bin/hlogd`.
* Install `logd` service for persistence.

We captured only one sample of xdr33 for the X86 architecture, and its basic information is shown below.

```
MD5:ee07a74d12c0bb3594965b51d0e45b6f
ELF 32-bit LSB executable, Intel 80386, version 1 (SYSV), statically linked, stripped
Packer: None
```

Simply put, when xdr33 runs in the compromised device, it first decrypts all the configuration information, then checks if it has root/admin permissions, if not, it prints “Insufficient permissions. try again... “and exit; otherwise initialize various runtime parameters, such as C2, PORT, runtime interval, etc. Finally, the two functions beacon\_start and TriggerListen are used to open the two tasks of Beacon and Trigger.

[![](https://blog.netlab.360.com/content/images/2022/12/hive_main.png)](https://blog.netlab.360.com/content/images/2022/12/hive_main.png)

The following article mainly analyzes the implementation of Beacon and Trigger from the perspective of binary inversion; at the same time, we also compare and analyze the source code to see what changes have occurred.

xdr33 decodes the configuration information by the following code snippet decode\_str, its logic is very simple, i.e., byte-by-byte inverse.

[![](https://blog.netlab.360.com/content/images/2022/12/hive_decode.png)](https://blog.netlab.360.com/content/images/2022/12/hive_decode.png)

In IDA you can see that decode\_str has a lot of cross-references, 152 in total. To assist in the analysis, we implemented the IDAPython script Decode\_RES in the appendix to decrypt the configuration information.

[![](https://blog.netlab.360.com/content/images/2022/12/hive_idaxref.png)](https://blog.netlab.360.com/content/images/2022/12/hive_idaxref.png)

The decryption results are shown below, including Beacon C2 `45.9.150.144`, runtime prompt messages, commands to view device information, etc.

[![](https://blog.netlab.360.com/content/images/2022/12/hive_config.png)](https://blog.netlab.360.com/content/images/2022/12/hive_config.png)

The main function of Beacon is to periodically collect PID, MAC, SystemUpTime, process and network related device information; then use bzip, XTEA algorithm to compress and encrypt the device information, and report to C2; finally wait for the execution of the commands issued by C2.

## 0x01: Information Collection

* MAC

  Query MAC by `SIOCGIFCON` or `SIOCGIFHWADDR`

  [![](https://blog.netlab.360.com/content/images/2022/12/hive_mac-1.png)](https://blog.netlab.360.com/content/images/2022/12/hive_mac-1.png)
* SystemUpTime

  Collects system up time via /proc/uptime

  [![](https://blog.netlab.360.com/content/images/2022/12/hive_uptime.png)](https://blog.netlab.360.com/content/images/2022/12/hive_uptime.png)
* Process and network-related information

  Collect process, NIC, network connection, and routing information by executing the following 4 commands

  [![](https://blog.netlab.360.com/content/images/2022/12/hive_netinfo.png)](https://blog.netlab.360.com/content/images/2022/12/hive_netinfo.png)

## 0x02: Information processing

Xdr33 combines different device information through the update\_msg function

[![](https://blog.netlab.360.com/content/images/2022/12/hive_compose.png)](https://blog.netlab.360.com/content/images/2022/12/hive_compose.png)

In order to distinguish different device information, Hive designed ADD\_HDR, which is defined as follows, and "3, 4, 5, 6" in the above figure represents different Header Type.

```
typedef struct __attribute__ ((packed)) add_header {
	unsigned short type;
	unsigned short length;
} ADD_HDR;
```

What does "3, 4, 5, 6" represent exactly? This depends on the definition of Header Types in the source code below. xdr33 is extended on this basis, with two new values 0 and 9, representing `Sha1[:32] of MAC`, and `PID of xdr33` respectively

[![](https://blog.netlab.360.com/content/images/2022/12/hive_type.png)](https://blog.netlab.360.com/content/images/2022/12/hive_type.png)

Some of the information collected by xdr32 in the virtual machine is shown below, and it can be seen that it contains the device information with head type 0,1,2,7,9,3.

It is worth mentioning that type=0, `Sha1[:32] of MAC`, which means that it takes the first 32 bytes of MAC SHA1. Take the mac in the above figure as an example, its calculation process is as follows.

```
mac:00-0c-29-94-d9-43,remove "-"
result:00 0c 29 94 d9 43

sha1 of mac:
result:c55c77695b6fd5c24b0cf7ccce3e464034b20805

sha1[:32] of mac:
result:c55c77695b6fd5c24...