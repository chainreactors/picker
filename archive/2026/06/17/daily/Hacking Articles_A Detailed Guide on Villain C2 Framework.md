---
title: A Detailed Guide on Villain C2 Framework
url: https://www.hackingarticles.in/a-detailed-guide-on-villain-c2-framework/
source: Hacking Articles
date: 2026-06-17
fetch_date: 2026-06-18T06:49:48.285713
---

# A Detailed Guide on Villain C2 Framework

[Skip to content](#content)

# [Hacking Articles](https://www.hackingarticles.in/)

Raj Chandel’s Blog

Menu

* [Courses We Offer](https://www.hackingarticles.in/courses-we-offer/)
* [CTF Challenges](https://www.hackingarticles.in/ctf-challenges-walkthrough/)
* [Penetration Testing](https://www.hackingarticles.in/penetration-testing/)
* [Web Penetration Testing](https://www.hackingarticles.in/web-penetration-testing/)
* [Red Teaming](https://www.hackingarticles.in/red-teaming/)
* [Donate us](https://www.hackingarticles.in/donate-us/)

* [Home](https://www.hackingarticles.in/)
»* [Red Teaming](https://www.hackingarticles.in/category/red-teaming/)
»* [A Detailed Guide on Villain C2 Framework](https://www.hackingarticles.in/a-detailed-guide-on-villain-c2-framework/)
»

[Command and Control](https://www.hackingarticles.in/category/red-teaming/command-and-control/), [Red Teaming](https://www.hackingarticles.in/category/red-teaming/)

# A Detailed Guide on Villain C2 Framework

[June 17, 2026](https://www.hackingarticles.in/a-detailed-guide-on-villain-c2-framework/) by [raj](https://www.hackingarticles.in/author/admin/)

### **Overview**

Villain is an open-source command-and-control (C2) framework developed by t3l3machus that turns a single operator console into a full collaborative attack platform. It generates reverse-shell and HoaxShell payloads for both Windows and Linux, manages multiple concurrent sessions, and — most distinctively — chains independent Villain instances together as **sibling servers**, letting operators share captured shells across machines in real time.

This article delivers a complete, hands-on walkthrough of that workflow inside a controlled lab. We deploy Villain on a Kali Linux attacker (192.168.1.17), compromise a Windows host (192.168.1.12) and a Linux host (192.168.1.11), upgrade the shells, and federate a second Villain server running on an Ubuntu machine (192.168.1.9). Along the way we demonstrate encoded payload generation, interactive shell access, ConPtyShell upgrades, pivot discovery, server synchronisation, and full session lifecycle management — closing with practical defensive measures security teams can use to detect and disrupt this activity.

### **Table of Contents**

* Overview
* Introduction
* Lab Environment
* Cloning the Villain Repository
* Inspecting the Project Files
* Launching Villain
* Generating an Encoded Windows Payload
* Entering the Windows Pseudo-Shell
* Upgrading to a Fully Interactive ConPtyShell
* Generating a Linux Payload
* Capturing the Linux Session and Discovering a Pivot
* Preparing the Sibling Server Host
* Connecting to the Sibling Server
* Accepting the Connection and Synchronising Sessions
* Verifying the Sibling Relationship
* Reviewing Active Backdoors
* Inspecting Shell Redirectors
* Aliasing Sessions for Readability
* Terminating a Session
* Purging Stored Metadata
* Mitigation Strategies
* Conclusion

### **Introduction**

Once an attacker gains a foothold on a target, the real challenge begins: maintaining reliable access, managing several compromised hosts at once, upgrading fragile shells into usable interactive sessions, and coordinating the operation across a team. Villain is purpose-built for exactly this post-exploitation phase. Rather than juggling separate listeners and one-off reverse-shell one-liners, an operator drives everything from one console.

Under the hood, Villain leans heavily on **HoaxShell**, an HTTP/HTTPS-based reverse-shell technique that blends C2 traffic into ordinary web requests to evade conventional detection. It ships with multi-handlers for reverse TCP and HoaxShell payloads, a built-in HTTP file smuggler for staging tools, and ConPtyShell integration for fully interactive Windows shells. Its signature capability, however, is the **sibling server** model: two or more Villain instances on different machines can federate, synchronize their captured sessions, and route shell traffic between one another — enabling genuine multi-operator, multi-host collaboration.

Throughout this article we exercise these features against a purpose-built lab, demonstrating each command in sequence so the workflow is reproducible from start to finish.

### **Lab Environment**

The walkthrough uses an isolated lab consisting of a Kali Linux attacker, two victim hosts, and a second Ubuntu machine that runs a federated Villain instance. All activity is performed against systems we own and control. The table below summarizes each role, system, and address used across the engagement.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiFOTfHNYdnk8MH6pGVPlkF8PvHFe4YCw6K5t9SBIGGkPCF95kt-VciWpXEoSlVCMjt6OdrNcsFUbsjjFANB9KPiMSzScu6iwHvUym-X74OIBotwfe-bfnqZH-d9AGr2tZ2hxYpLmDiXV8k7fFCFIxz5L9Mfp96zwsjjx6J170oX8wsl_Gney30ittKRwhV/s16000/0.png)

### **Cloning the Villain Repository**

We begin with the Kali attacker by pulling the Villain source straight from its official GitHub repository. The clone retrieves the entire project — roughly 1,400 objects — into a local **villain** directory. The output confirms a clean download, with every object received and all deltas resolved.

```
git clone https://github.com/t3l3machus/villain
```

### ![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiflUwOy3l8tG76yK8DZIw_eGWS02BHVvqVuLD0CGDJQGfbsOj4rj0-hcRfT9CwmGyAjZP-pt3Cc3ZyLBbgrB9nTnbce5k4A3tBVT3fAVNpEwRazUdg7siPYPRzleDn5msSQQoZmYMPku0q0QgMfiAwZYb2Kf1QjK2vB7cRs5JDW4eF3ZcMvJlL8r0uWkfW/s16000/1.png)

### **Inspecting the Project Files**

With the repository on disk, we move into the project directory and list its contents. The layout reveals the framework’s structure: a **Core** module that houses Villain’s engine, the LICENSE and README files, requirements manifest, a usage guide, and the **Villain.py** entry point we will execute next.

```
cd villain
ls -al
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi-fIlOVCeQ5I9el-R2WSxCkvPY78WkR8qjQu7Am5rPSeTMKaPjAjYrLbZOi2HqgiLOO5N72p9I7cw-1XWdpGZwgtCylWMSsKvOVVttok33HyENoS52tVi0A-TIsYGGXlMrb3AiK0EzS3RSAOM6i9nRFQwQwTjuKXXanrlPzyUsF1ZKFJg4v3TDhTRrpxRr/s16000/2.png)

### **Launching Villain**

Running the entry-point script starts the framework. Villain prints its banner and immediately initialises four background services: a Team Server on port 6501 for sibling federation, a Reverse TCP Multi-Handler on 4443, a HoaxShell Multi-Handler on 8080, and an HTTP File Smuggler on 8888.

Typing **help** enumerates every command available at the main prompt and inside the interactive pseudo-shell — covering payload generation, session control, traffic redirection, file transfer, and sibling chat.

```
python Villain.py
help
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXMIr2Ee2XKRICiFoEzA5PEuf9i2wpPIVMgsiMHjh3urVs-Ciwmy456Euk5JwHc_bwz2TUAFvCNG8fu9RnDaTiBBWjWmAVfKLPWGxodSPFnvhNLsPicxtVpYH5csSO4KqNT2Of_njpExr901SPoNPdR-v7agHDaOWEzDBFLT4ABdiH7N_ydSClmiLthyIS/s16000/3.png)

### **Generating an Encoded Windows Payload**

Villain’s **generate** command builds ready-to-run implants. Here we request a Base64-encoded PowerShell reverse-TCP payload bound to the eth0 interface, so the implant calls back to Kali automatically. Villain prints the one-liner, copies it to the clipboard, and — once the operator runs it on the Windows target — reports a new session from 192.168.1.12 belonging to IGNITE\administrator. The **sessions** command then lists the freshly captured shell.

```
generate payload=windows/reverse_tcp/powershell lhost=eth0 encode
sessions
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgvmyfAmMH7D9gcm15eCxa0zdWv3uDdCBtS2_RL7WNo1u2Tb1ekNebKRUfheDs52Xnsb5FiLALKshghe9ObuePVMctci0Gkz_gx_mxvk_CByQItZxLrm17KisvAfheQ6jx7iso1y_cK2ENgSGDLdw6QKgopF6_qX5FAQdV5SLn4Kp_UG98-FGh5_W_fLucl/s16000/4.png)

### **Entering the Windows Pseudo-Shell**

To interact with the captured host, we attach to its session ID using the **shell** command. Villain activates an interactive pseudo-shell, ...