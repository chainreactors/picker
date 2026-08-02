---
title: Active Directory Enumeration with BloodHound-Python
url: https://www.hackingarticles.in/active-directory-enumeration-with-bloodhound-python/
source: Hacking Articles
date: 2026-08-01
fetch_date: 2026-08-02T05:10:32.061110
---

# Active Directory Enumeration with BloodHound-Python

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
»* [Active Directory Enumeration with BloodHound-Python](https://www.hackingarticles.in/active-directory-enumeration-with-bloodhound-python/)
»

[Domain Enumeration](https://www.hackingarticles.in/category/red-teaming/domain-enumeration/), [Red Teaming](https://www.hackingarticles.in/category/red-teaming/)

# Active Directory Enumeration with BloodHound-Python

[August 1, 2026August 1, 2026](https://www.hackingarticles.in/active-directory-enumeration-with-bloodhound-python/) by [raj](https://www.hackingarticles.in/author/admin/)

### Overview

BloodHound-python delivers a fast, cross-platform way to map the attack paths hidden inside an Active Directory environment. Instead of manually querying LDAP, dumping group memberships, and correlating sessions by hand, a penetration tester runs a single ingestor that collects the raw relationship data and hands it to BloodHound for graph analysis. This article walks through the tool end to end inside an isolated lab built on the ignite.local domain. Each demonstration uses a different collection method or authentication mechanism, so by the end you will understand not only how to run the ingestor, but also which switch to reach for during a real assessment. Every command targets the domain controller at 192.168.1.9, and every run drops timestamped JSON files that BloodHound consumes directly.

### Table of Contents:

* Introduction to BloodHound-Python
* Default Collection Method
* Output of the Default Collection
* LoggedOn Collection Method
* Output of the LoggedOn Collection
* DCOnly Collection Method
* Output of the DCOnly Collection
* Authentication with Pass-the-Hash
* Authentication with a Kerberos AES Key
* Authentication with a Kerberos Ticket (ccache)
* Packaging Output with the Zip Option
* Conclusion

### Introduction to BloodHound-Python

BloodHound-python (also called bloodhound-python or the Python ingestor) is an open-source data collector that gathers Active Directory information over the network and serializes it into the JSON format that BloodHound expects. The original SharpHound collector runs natively on Windows, but the Python ingestor removes that constraint entirely: it runs on Linux, executes straight from a Kali attack box, and never requires a foothold on a domain-joined machine. It authenticates against LDAP and SMB using standard domain credentials and pulls users, groups, computers, group policy objects, organisational units, containers, trusts, sessions, and local administrator relationships.

Install it from the Kali repositories or pip with pip install bloodhound, then invoke it with bloodhound-python. The core switches used throughout this article are -u and -p for the username and password, -d for the target domain, and -ns to point the resolver at the domain controller acting as the DNS server. The -c flag selects the collection method, which controls exactly how much and what kind of data the tool retrieves.

The collection methods matter because each one balances stealth, speed, and completeness differently. Default performs a broad sweep that touches domain objects and live hosts. LoggedOn focuses purely on identifying which users are signed in to remote machines. DCOnly pulls everything obtainable from the domain controller through LDAP alone, never touching individual workstations, which makes it quiet and quick. All combines DC-based and host-based collection for the most complete dataset. The tool also supports several authentication modes beyond a cleartext password, including pass-the-hash with an NT hash, Kerberos AES keys, and cached Kerberos tickets, each of which this article demonstrates in turn.

### Default Collection Method

The first run uses the Default collection method, which represents the most common starting point. Here the tester authenticates as the domain user raaz with the password Password@1, sets ignite.local as the target domain, and directs name resolution to the domain controller at 192.168.1.9. As the tool runs, it locates the AD domain, requests a Kerberos ticket-granting ticket, and connects to the LDAP server on DC1.ignite.local. The output confirms that it discovered one domain, three computers, thirty-one users, and fifty-three groups before enumerating each computer in turn and finishing in a single second.

```
bloodhound-python -u raaz -p Password@1 -ns 192.168.1.9 -d ignite.local -c Default
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoG09Pnn99ZEK5dOAmEJULD1Z0NiA119UW_m12-1mQgUVZEovUjE_0CnN5m24uC0kjlDZs9qkwaheLWOj75m4CeYbfM4hcuAMyxPp2uvUqB9NTAfYK1p4mtTNvNAX2gM7d7IZH8aWn32va4bQ7xKCAhUAUM2mUie8BRriEYU5UH2B_zzZAPFS8hphBBg_C/s1600/1.png)

### Output of the Default Collection

Listing the working directory after the Default run reveals the artifacts the ingestor produced. The tool writes four timestamped JSON files covering computers, domains, groups, and users. The shared timestamp prefix keeps every file from a single collection grouped together, which prevents confusion when multiple runs accumulate in the same folder. These files import directly into the BloodHound GUI to render the attack graph.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgj8AwxVyeJVgRUO9LWMeOPEXFDbPyTBDzYfm7pOUJ7o1zzwjQlkTfT-n4kcy-mbjhVtCop4rALEx9WzouDAPaiXcEZ7jQXrR3OtcIy0ExCYu2UnfDzAndvF6NPOkIDEIvv-W88vm1aLrxNoThAuSu9ivhzX4xjRTkI2vAQpX5CrzVivBnN1rxCgUsfJSoB/s1600/2.png)

### LoggedOn Collection Method

Switching the -c flag to LoggedOn narrows the focus to active user sessions. This method skips the broad object enumeration and instead queries each computer to discover who is currently signed in, which is invaluable for planning lateral movement toward a privileged account. In this run, the tool reports that a user with the SID ending in 500, the built-in Administrator, is logged in on DC1.ignite.local. Session data like this exposes exactly where high-value credentials sit in memory and are ripe for extraction.

```
bloodhound-python -u raaz -p Password@1 -ns 192.168.1.9 -d ignite.local -c LoggedOn
```

**![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjJNljeXReCZFLfX-V1AsgrhUnUw-Qf6DLi5UxGIOwPje3_inSI2Q-rH01qusxSAl26kSR2F0GAmNsMRfPr9t2jfPRX2RmvOO2vzFkrIqAzq16SM2q8hUbom3Gb8Lfgwtdh3pe6HD0sGs9PoBn_7Os0NteGFmZsK6uf-Si8d6aEhAffTByV9O9qgGZmp6ET/s1600/3.png)**

### Output of the LoggedOn Collection

Because LoggedOn concentrates solely on session information tied to computers, it produces a single JSON file rather than the full set. The directory listing shows one computers.json file, confirming that this lightweight method carries a much smaller footprint than a full collection while still delivering the session intelligence a tester needs.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhbxbX25zkQwSS_LI10EpNPfan2KZeUT7yP2pqvS-ZOYh1INfbawg4ZWJGXgjgUiHOU0wZ0tk1ieKWvzV9AVDG5yJU2xado1OgiUO-eUsvJzO4KRL6cyWRJ6zY2LKMJ_jZh022NGetC3DGdQmUt9IRKgoDP5tJlez7Jq-qo1fngjtu2u1tUcLPnoC5Sc4BE/s1600/4.png)

### DCOnly Collection Method

The DCOnly method gathers everything reachable through the domain controller over LDAP without ever connecting to individual workstations, which makes it both fast and comparatively stealthy. This run retrieves thirty-one users, fifty-three groups, three GPOs, two OUs, nineteen containers, and three computers, then completes almost ins...