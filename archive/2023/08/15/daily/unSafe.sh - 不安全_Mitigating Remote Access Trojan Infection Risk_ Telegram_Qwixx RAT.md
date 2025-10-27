---
title: Mitigating Remote Access Trojan Infection Risk: Telegram/Qwixx RAT
url: https://buaq.net/go-174429.html
source: unSafe.sh - 不安全
date: 2023-08-15
fetch_date: 2025-10-04T11:59:42.761963
---

# Mitigating Remote Access Trojan Infection Risk: Telegram/Qwixx RAT

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

![](https://8aqnet.cdn.bcebos.com/5226c6430bfbc17f36de27da94cf4221.jpg)

Mitigating Remote Access Trojan Infection Risk: Telegram/Qwixx RAT

A new threat has emerged in the realm of cybersecurity, referred to
*2023-8-14 21:2:16
Author: [www.uptycs.com(查看原文)](/jump-174429.htm)
阅读量:208
收藏*

---

A new threat has emerged in the realm of cybersecurity, referred to as QwixxRAT.  Both businesses and individual users are at risk, as this Trojan silently infiltrates devices, casting a wide net of data extraction.

Ever vigilant for threats like the Remote Access Trojan (RAT), the Uptycs Threat Research team discovered QwixxRAT (aka Telegram RAT) in early August 2023. The threat actor is widely distributing this malicious tool through Telegram and Discord platforms.

Once installed on the victim’s Windows platform machines, the RAT stealthily collects sensitive data, which is then sent to the attacker's Telegram bot, providing them with unauthorized access to the victim's sensitive information.

## A far-reaching RAT

QwixxRAT is meticulously designed to harvest an expansive range of information from browser histories and credit card details to keylogging insights.

Its presence became notably alarming in recent evaluations of compromised systems, hinting at its potential rise. While its origin and primary target zones remain under investigation, the Trojan's reach seems global, leaving no user truly safe.

Beyond mere data theft, QwixxRAT wields formidable remote administrative tools, enabling attackers to control victim devices, launch commands, and even destabilize systems. In this blog, we aim to comprehensively explore its features, workings, and the preventative steps that can be taken against it.

## Marketing and distribution tactics of QwixxRAT

The scheme is orchestrated via a threat actor utilizing both Telegram and Discord platforms to market the RAT tool. They offer the tool for sale, specifying its cost, and additionally provide a limited free version.

Price list (Russian currency):
Permanent access - 500 rubles
Access for a week - 150 rubles

Upon any threat actor's purchase of the RAT, the team establishes a separate channel dedicated to accessing the acquired data.

![Figure 1 – QwixxRAT Telegram channel](https://www.uptycs.com/hs-fs/hubfs/Imported%20images/Fig1.jpg?width=736&height=556&name=Fig1.jpg)

## QwixxRAT Workflow

Figure 2 depicts the QwixxRAT workflow.

![Figure 2 – Workflow of QwixxRAT](https://www.uptycs.com/hs-fs/hubfs/Imported%20images/Fig2.jpg?width=872&height=896&name=Fig2.jpg)*Figure 2 – Workflow of QwixxRAT*

## Technical analysis

The RAT file is a C# compiled binary, functioning as a 32-bit executable file designed for CPU operations. The figure shows that the threat actor employed two distinct names for the same Remote Access Trojan (RAT). One alias used was "Qwixx Rat," while the other was identified as "TelegramRAT."

![Figure 3 – QwixxRAT code](https://www.uptycs.com/hs-fs/hubfs/Imported%20images/Fig3.jpg?width=1908&height=729&name=Fig3.jpg)*Figure 3 – QwixxRAT code*

The main function consists of a total of 19 individual functions, each serving a unique purpose. We will now examine them one by one.

The RAT is equipped with a configuration function that determines its behavior on the target machine. This configuration function contains various values, which can be in the form of booleans, file extensions, or other types of data. Based on these values, the RAT adapts its actions accordingly.

### Function 1: HideConsoleWindow

As this is a CPU program, the threat actor conceals the console to remain covert.

### Function 2: CheckMutex

The threat actor employs a mutex value check to prevent duplicate execution. They generate an MD5 value for the string "995716229" and additionally verify if the current login user has administrative privileges. If the user is an admin, the threat actor creates a new mutex using the string "ADMIN:21de6ebf2e182b19a589c154562979b4." By doing so, the actor ensures that only one instance of the program runs on the target machine.

![Figure 4 – Mutex check](https://www.uptycs.com/hs-fs/hubfs/Imported%20images/Fig4.jpg?width=820&height=320&name=Fig4.jpg)*Figure 4 – Mutex check*

### Function 3: SecurityProtocol

This code snippet sets the “ServicePointManager.SecurityProtocol” property to enable support for multiple secure network protocols. The application ensures backward compatibility and broader compatibility with various servers and clients by including SSL 3.0, TLS 1.0, TLS 1.1, and TLS 1.2. This configuration allows the application to securely communicate with servers requiring different SSL/TLS versions to establish secure connections.

### Function 4: Elevate Privileges

The code attempts to elevate the current application's privileges to run with administrative rights by relaunching itself(Hidden Attribute) with the "runas" verb. If the user denies the elevation or if the configure AdminRightsRequired setting prevents it, the while loop will continue, allowing for further attempts to elevate privileges.

### Function 5: Sleep

To evade AV/EDR/Sandbox detection, the threat actor incorporates the sleep function to introduce a delay in the execution process.

### Function 6: runAntiAnalysis

The threat actor employed three methods for anti-analysis purposes: [Sandboxie, VirtualBox](https://attack.mitre.org/techniques/T1497/), and Debugger.

![Figure 5 – Anti analysis check](https://www.uptycs.com/hs-fs/hubfs/Imported%20images/Fig5.jpg?width=1277&height=164&name=Fig5.jpg)*Figure 5 – Anti analysis check*

* **Sandbox check:**

The code includes a check to determine whether the current application is operating within a sandbox environment. This check involves looking for specific DLLs, namely SbieDll.dll, SxIn.dll, Sf2.dll, snxhk.dll, and cmdvrt32.dll, which are commonly associated with sandboxing software. If any of these DLLs are detected as loaded within the current process by GetModuleHandle API, the attacker instantly terminates the code execution, understanding that it is running in a sandbox environment.

* **VirtualBox**

To identify if the file is running within a virtual environment, the threat actor utilized two [WMI queries](https://attack.mitre.org/techniques/T1047/). Firstly, they employed the query "Select \* from Win32\_ComputerSystem" to inspect the "Manufacturer" and "Model" fields. If any of the strings match the keyword "virtual" or "vmware" or "VirtualBox" the process is promptly terminated.

Secondly, the actor employed the query "SELECT \* FROM Win32\_VideoController" to check the "Name" property using GetPropertyValue.If any of the strings match the keyword "VMware " or "VBox ", the process is terminated as well.

* **Debugger**

The code implements a method to identify if the current application is being run under a debugger. It does this by introducing a brief delay and subsequently checking if the elapsed time during this delay is less than 10 ticks, equivalent to 1 microsecond. The underlying assumption is that the presence of a debugger might induce additional delays, resulting in a smaller time difference. The process is terminated as a security measure if such a scenario is detected.

### Function 7: installSelf

The threat actor attempts to locate the file at "C:\Users\Chrome\rat.exe". If the file is not found in the specified path, the code retrieves the executable path and copies itself to "C:\Users\Chrome\rat.exe". Subsequently, the actor modifies the file attributes to make it [hidden](https://attack.mitre.org/techniques/T1564/001/) in the system.

### Function 8: setAutorun

A [scheduled task](https://at...