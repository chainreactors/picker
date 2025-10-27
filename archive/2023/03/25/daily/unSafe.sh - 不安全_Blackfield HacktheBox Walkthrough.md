---
title: Blackfield HacktheBox Walkthrough
url: https://buaq.net/go-155145.html
source: unSafe.sh - 不安全
date: 2023-03-25
fetch_date: 2025-10-04T10:36:15.448262
---

# Blackfield HacktheBox Walkthrough

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

![](https://8aqnet.cdn.bcebos.com/d1b5994251d135ac6801b9c25e4cc8b1.jpg)

Blackfield HacktheBox Walkthrough

SummaryBlackfield is a windows Active Directory machine and is considered as hard
*2023-3-24 20:45:57
Author: [www.hackingarticles.in(查看原文)](/jump-155145.htm)
阅读量:52
收藏*

---

### Summary

Blackfield is a windows Active Directory machine and is considered as hard box by the hack the box. This box has various interesting vulnerabilities, and security misconfigurations were placed. As usual, we began with a basic nmap scan as a part of enumeration and noticed smb null session was enabled. Then we discovered a pre-authentication disabled account and performed AS-Rep Roasting, and cracked the obtained hash. With the extracted password, we were able to enumerate the users available in the AD using RPC Client.

Moving laterally, we used bloodhound and noticed that a user could change another user’s password, which could be done using RPC Client. After changing the password of another user, we accessed the shared folder, where we found an interesting file as memory-dumped data. Using mimikatz, we extracted the NTLM hash of the backup user from the lsass memory. The further enumeration in order to find the privilege escalation vector, we discovered the current user belongs to the backup operator group, and the sebackup privilege was enabled. With the privileged assigned to the current user, we were able to copy ntds.dit file and system hive.

 Lastly, we used the impacket secretdump tool to extract the administrator hash from the ntds.dit file with the help of the system hive. After obtaining the administrator hash, we logged in as an administrator and collected the root flag. So, without spoiling it more, let’s exploit it step by step.

### Table of Content

**Initial Access**

* Initial Nmap TCP Port Scan
* SMB Share Enumeration
* Searching for the No Pre Auth (NPU) configured users
* Krb5asrep hash cracking with john
* RPC Client Enumeration
* Setting up Neo4j Console
* Export JSON files in Ne04j Console for the analysis
* Analysing AD Hidden Relationship with other users
* Attempt to change user password using RPC Client
* Workgroup enumeration of audit2020 user
* Extract data from the lsass.DMP file
* User Shell

**Privilege Escalation**

* Exploiting Enabled Dangerous Privileges
* Transfer disk shadowing DOS file to the target system
* Copy ntds.dit file using assigned privilege
* Make a copy of the system hive
* Dump password hash from ntds.dit file Root flag

Let’s exploit it step by step.

### Initial Access

We are going to start the assessment with the normal TCP/IP port scanning.

### **Initial Nmap TCP Port Scan**

We begin with the port scan, where we use nmap to find out which ports are open and what services are running in the target host. Nmap is a popular port scanning tool that comes with Kali Linux. To perform a port scan, we have used –**sV** flag against the target system, which scans the top 1000 ports with the service version.

Flags features:

**-sV**:  Attempts to determine the service version

From the nmap scan, we have found eight ports are open where most of the services belong to the Active Directory environment. Any of these services can lead us toward any protocol-based vulnerabilities or any security misconfiguration, which is common in an active directory environment. Also, it is showing the domain name as **BLACKFIELD.local**.

```
nmap -sV 10.129.45.226
```

**![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEh8l95O-Hc7TNJ30UpPkk04ILBAp3nKuRkFthNRSYSCpiruFA6aFujz1rFDKj7uCHVMbdR2QTzFjMvzEXv7LU08LBdETFyeLQ5uR9a3XnyEqS6K81qnF1zpemV64Rp1w2zqqbdiaSnOPROgDcMJC-OKZK6-e3hdDA0nwWTq6AqDJoDLcLhSfBC3NXGk1g/s16000/1.png?w=640&ssl=1)**

### **SMB Share Enumeration**

The Server Message Block (SMB) protocol is a network file-sharing protocol that allows applications on a computer to read and write to files and request services from server programs in a computer network. It can be seen in the internal network that smb share is enabled for the null session, which means a user can access that shared folder without authentication or with no password. Firstly, we listed all available shares using smbclient tools, which come with kali Linux by default. From the output, we noticed that **$profiles** directory has no comment, and we attempted to log in without a password and successfully logged in. After logging into smb share, we found there are so many directories we can access where all directories look empty as the size is showing its bytes in **0**.

```
smbclient -L 10.129.45.226
```

### **![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgDvJIyoGgGfw7qevhbrVQwJh1Y_TYnrUyuC4FrrjUXeCqgHwJm_qO25TgM1r4IhLucIDTz7nZXJpswGBUxOY411sgZvQ7cxU_vD7qD7EV8OrIgvDfrxzpG_bacMCeMrI8opOHDEST1b8YfPXDpatvcJV8iL1vKFF3cwyW4Ze6HuYpSgyHP6OBLW_-uVQ/s16000/2.png?w=640&ssl=1)**

 We added the domain name **BLACKFIELD.local** in our /etc/host file before continuing further enumeration. To do that, we can use any text editor such as leafpad, nano, gedit.etc.

### **![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjVemtyy54uOd-YZ5OB7ekT3KPFz67qSFew2LGFSPbgpvZzimYIUUZeJnZmr45Cb6wtprw90f0dMj5BE0orOOcyDV2JmvN4kPXHWtPCDLI1QiVuDA83zkcDUhhAXz4R4S4nHrTnw2HgCzgbYeMcQ3e7HptNhwquw7dNlqZI4cLkCIqovzeQgS-fLAHw0g/s16000/3.png?w=640&ssl=1)**

### **Searching for the No Pre Auth (NPU) configured users**

As a threat actor, we are going to test all potential vulnerabilities that exist in an Active Directory environment. Suppose an admin has configured an account with no pre-authentication required; then the user does not need to request KDC to access any service or resources where an attacker can take advantage of the configuration and try to steal password hashes of the user that have Kerberos pre-authentication disabled. Then the attacker can try extracting a plain text password from the obtained hash. This attack is also known as AS-REP Roasting. Similarly, we tried to obtain any user’s password hash using the impacket library **GetNPUsers** and stored the result in the result.txt file. As a result, we found that the **support** account has no pre-authentication set and extracted its password hash. After obtaining the hash, we can try to crack it using offline tools such as john and hashcat.

In the below command, we have used the –dc-ip flag for the domain IP address with the domain name and the **-userfile** flag to give a list of potential users. Then we used the grep utility to filter our results.

```
impacket-GetNPUsers -dc-ip 10.129.45.226 blackfield.local/ -usersfile username.txt > result.txt
```

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiOuIDUjOyrh9ci2AqZ9iBX0JlD5M_JTjCvkh3a1lKpxEUIy7HWqKfMPwcjioGP7iu3oRvQoQHoFrD7YkVnDOfIo3xDisLsPJaC4slYyFOw3Rk86i0rM3iIgKPuqa85pr9iIvPnjrG5uosfvQ8F6byeLFmZr2ZR1K4OBmRiHCxr4oIxqTJgwGT02VnonA/s16000/4.png?w=640&ssl=1)

### **Krb5asrep hash cracking with john**

We stored the obtained hashes in a hash file. Then we used john to crack the hashes in a plain text format issuing breached password wordlists that come with Kali Linux. Rockyou.txt file contains a list of commonly used password words. This file contains over 14,341,564 passwords that were previously leaked in data breaches. The tool did its job very well and cracked the hashes into human-readable form.

**Cracked password:** #00^BlackKnight

```
john --wordlist=/usr/share/wordlists/rockyou.txt hash
```

**![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhmaJDk4wkh6PjbxED0_v0tND1jyt42tX72KNeqmGa8YPdSWyr2JYxb7...