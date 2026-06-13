---
title: Penelope – A Modern Alternative to Netcat for Red Teamers
url: https://www.hackingarticles.in/penelope-a-modern-alternative-to-netcat-for-red-teamers/
source: Hacking Articles
date: 2026-06-12
fetch_date: 2026-06-13T06:10:07.312039
---

# Penelope – A Modern Alternative to Netcat for Red Teamers

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
»* [Penelope – A Modern Alternative to Netcat for Red Teamers](https://www.hackingarticles.in/penelope-a-modern-alternative-to-netcat-for-red-teamers/)
»

[Red Teaming](https://www.hackingarticles.in/category/red-teaming/)

# Penelope – A Modern Alternative to Netcat for Red Teamers

[June 12, 2026](https://www.hackingarticles.in/penelope-a-modern-alternative-to-netcat-for-red-teamers/) by [raj](https://www.hackingarticles.in/author/admin/)

### **Overview**

This article presents an end-to-end engagement built entirely around Penelope, an automated shell handler and post-exploitation framework. We catch an initial reverse shell on a Windows Server 2019 Domain Controller, drive Penelope’s modules to escalate privileges, dump credentials, harvest Active Directory data, and Kerberoast a service account, then hand off to Meterpreter and clean up our artefacts. From there, we pivot through the domain controller into a hidden subnet with Ligolo-ng, compromise a Linux host, and run a full sweep of Linux enumeration tooling. Finally, we explore Penelope’s operational backbone—custom listeners, tailored payload generation, bind-shell connections, multi-session management, port forwarding, file transfer, and a built-in HTTP file server. Together, these stages show how a single console can manage the complete post-exploitation lifecycle across both Windows and Linux.

### **Table of Contents:**

* Introduction
* Lab Environment
* Installing Penelope
* Starting the Listener
* Generating the Reverse Shell Payload
* Receiving the Reverse Shell
* Detaching the Session
* Listing the Available Modules
* Exploring the Help Menu
* Privilege Escalation Enumeration (Windows)
* Staging the Potato Exploits
* Credential Dumping
* Active Directory Tooling
* Spawning a Meterpreter Session
* Cleaning Up Artefacts
* Pivoting with Ligolo-ng
* Establishing the Pivot Route
* Scanning and Accessing the Hidden Host
* Catching and upgrading the Linux Shell
* Linux Privilege-Escalation Enumeration
* Collecting Forensic Artefacts
* Managing Multiple Sessions
* Forwarding a Loopback-Only Service
* Transferring Files to and From the Target
* Adding a Custom Listener
* Generating Payloads for the Listener
* Executing the Payload on the Target
* Catching the New Reverse Shell
* Connecting to a Bind Shell
* Spawning a Reverse Shell over SSH
* Serving Files over HTTP
* Mitigation Strategies
* Conclusion

### **Introduction**

Penelope is an automated, cross-platform shell handler designed to replace the bare “netcat” listener that most operators reach for by default. Beyond simply catching a reverse shell, it manages multiple concurrent sessions, logs every interaction to disk, upgrades raw shells to fully interactive PTYs, and exposes a rich library of post-exploitation modules. With a single command, an operator can stage privilege-escalation enumeration tools, credential-dumping utilities, Active Directory tradecraft, pivoting agents, and persistence mechanisms directly onto the target.

The framework also gives the operator precise control over how shells connect: it can add listeners on demand, generate matching payloads, connect to bind shells, forward ports through an existing session, and serve files over HTTP. Because Penelope automates the repetitive plumbing of an engagement—downloading the latest tooling, uploading it to the victim, executing it, and recording the output—it lets the operator concentrate on tradecraft rather than logistics. The walkthrough below follows that workflow from initial access through pivoting and operational control, entirely within a controlled lab and strictly for authorised testing and education.

### **Lab Environment**

The engagement uses an isolated VMware lab containing a Kali attacker and several targets across the IGNITE (ignite.local) domain. Pivoting through the domain controller exposes an additional internal subnet that is not directly reachable from Kali.

**![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhyITzn3lx5uJD2B02qup8qRpyei7Miqr4AMr2HBK4i0zHYRsXJ8dLzxkc57QQSF8oPoGYMFIR-jw54Qz0QYmn1QgUQlhi3l6iBQMA0BojRFKCNC_yTx4h-P7JxAN5knHYbma3-uUV1928FrE4ECSsT9-5PPrAoJBc2Wycd0ok1OWJIL9DJhCHw2u38MfLR/s16000/0.png)**

### **Installing Penelope**

We begin by installing Penelope directly from the Kali repositories. The package is lightweight—roughly 50 KB—and the APT resolver confirms a single new package will be installed from the kali-rolling main branch. Once installed, the “penelope” binary is available system-wide.

```
apt install penelope
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhRcK1CWog6aBAEXpRMcmvY9N69-SfiX9DK2O9mbGL-c-gh6OAYuSVJOTae0NfIjgR_S1h-FasNQhWHCldbYs3KUdj7KPfuaCV6SZ-G6n_g1ajIK4enlG-BkTqSkyQn1W2VbV7NFvaeU-lXH1lwtR_yxWpJ-Al9S5p0zoBaW5X9T-YUcJy2NQVt77S3oI4Q/s16000/2.png)

### **Starting the Listener**

Next, we launch Penelope and bind a listener to TCP port 5000. Penelope immediately reports that it is listening on 0.0.0.0:5000 and helpfully prints every interface address the operator might use as a callback—here including 192.168.1.17. The interactive prompt also surfaces shortcuts for the Main Menu, payload generation, screen clearing, and quitting.

```
penelope -p 5000
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEicO3xiV1VzDdFhRggxqoUJkB3dgcUWn4OSt0So3SgMhsHFUS13tzMwPsPF9WDOdwU4mQPldYY0fXL-Fg9ROwFVuN-Bf6aOdPf5CZAukOnggzctt_iTw6gUnDkecvIbXf35hlG3409vL1A9pP_vDU_z9c30h5zUVhEvc16SVVbbH4areOAP6OTDA1s0HZU4/s16000/3.png)

### **Generating the Reverse Shell Payload**

With the listener live, we craft the payload that the target will execute. Using the Reverse Shell Generator, we set the attacker IP to 192.168.1.17 and the port to 5000, then select the Windows “PowerShell #2” template. The generator produces a self-contained PowerShell one-liner that opens a TCP client back to our listener and streams an interactive shell over the connection.

The following PowerShell payload is delivered to the target. (It is wrapped here for readability; in practice, it runs as a single line.)

```
powershell -nop -c "command"
```

*![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiIZOcanRbxeR19YXSWMqZR7Z_6jYHMHRAP_T_tkWxLxY9so1HsW7SbKL2H4NZeavgnDpLs6KXQ7rDkwOUgWlG70MwMfote0E0aVp-uvFP3OwT_9iUwUFDXRelHCJwZ2sS8fMyYvvBOOBKpncgBJRLroetp0bfagrTdh6a2PY5FXepFoZlfGeDAsgdfoAgl/s16000/4.png)*

### **Receiving the Reverse Shell**

Once the payload runs on the victim, Penelope catches the connection instantly. It fingerprints the host and reports a new reverse shell from “DC” at 192.168.1.11, identifying it as a Microsoft Windows Server 2019 Standard Evaluation x64 machine. Penelope adds readline support, attaches us to Session 1, and writes a session log to disk for later review. A quick “whoami” confirms we are running as ignite\administrator—the built-in domain administrator on the DC.

```
whoami
```

**![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEic7TGPjsuz5hYbOv6189fW0v_cEvpd3T-gIuGUyuJY4OuNWsJmA32ggXldtqKlaxhr-RQ4H8-BGs9X2wndN3LAB0PUqnyknA6vMyRHwla5NO8jLXWAsHTVA2vO5wPbRHCfSzkpXUsTRB5wlhNrnooMIlAdTtrD_MKvDX933sMwFmp7tOzklX4FHihKuzrn/s16000/5.png)**

### **Detaching the Session**

Penelope lets us step back from an interactive shell without killing it. Pressing Ctrl-D detaches the current session and drops us back to t...