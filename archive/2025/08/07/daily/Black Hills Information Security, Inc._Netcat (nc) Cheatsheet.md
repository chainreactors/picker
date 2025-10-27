---
title: Netcat (nc) Cheatsheet
url: https://www.blackhillsinfosec.com/netcat-cheatsheet/
source: Black Hills Information Security, Inc.
date: 2025-08-07
fetch_date: 2025-10-07T00:48:23.162907
---

# Netcat (nc) Cheatsheet

[![Black Hills Information Security, Inc.](https://www.blackhillsinfosec.com/wp-content/uploads/2025/03/BHIS_TEXT_BHIS.png)](https://www.blackhillsinfosec.com "Black Hills Information Security, Inc.")

[RSS](https://www.blackhillsinfosec.com/feed/)

* [All Services](https://www.blackhillsinfosec.com/services/)
  + [Complete Service Guide](https://www.blackhillsinfosec.com/services/complete-service-guide/)
  + [Active SOC](https://www.blackhillsinfosec.com/services/active-soc/)
  + [AI Security Assessments](https://www.blackhillsinfosec.com/services/ai-security-assessments/)
  + [Blockchain Security](https://www.blackhillsinfosec.com/services/blockchain-security/)
  + [Blue Team Services](https://www.blackhillsinfosec.com/services/blue-team-services/)
  + [Continuous Penetration Testing](https://www.blackhillsinfosec.com/services/antisoc/)
  + [High-Profile Risk Assessments](https://www.blackhillsinfosec.com/services/high-profile-risk-assessments/)
  + [Incident Response](https://www.blackhillsinfosec.com/services/incident-response/)
  + [Penetration Testing](https://www.blackhillsinfosec.com/services/)
* [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Contact Us](https://www.blackhillsinfosec.com/contact-us/)
  + [Email Sign-Up](https://mailchi.mp/blackhillsinfosec.com/bhis-sign-up)
* [About Us](https://www.blackhillsinfosec.com/who-we-are/)
  + [Security Consultants](https://www.blackhillsinfosec.com/about/security-analysts/)
  + [Admin](https://www.blackhillsinfosec.com/about/admin-staff/)
  + [SOC Team](https://www.blackhillsinfosec.com/about/soc-team/)
  + [BHIS Family of Companies](https://www.blackhillsinfosec.com/bhis-tribe-of-companies/)
* [Free Resources](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Blogs](https://www.blackhillsinfosec.com/blog/)
  + [Free Cybersecurity Tools](https://www.blackhillsinfosec.com/free-cybersecurity-tools/)
  + [Free Cybersecurity Webcasts](https://www.blackhillsinfosec.com/free_cybersecurity_webcasts/)
  + [Podcasts](https://podcasts.apple.com/us/podcast/black-hills-information-security/id1410835265)
  + [RITA](https://www.activecountermeasures.com/free-tools/rita/)
* [Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [BHIS & Antisyphon Training](https://www.blackhillsinfosec.com/bhis-and-antisyphon-training/)
  + [WWHF Conference](https://wildwesthackinfest.com)
* [Online Community](https://blackhillsinfosec.com/community)
  + [Discord](https://discord.gg/BHIS)
  + [LinkedIn](https://www.linkedin.com/company/black-hills-information-security/)
  + [YouTube](https://www.youtube.com/c/BlackHillsInformationSecurity/videos)
  + [Bluesky](https://bsky.app/profile/bhinfosecurity.bsky.social)
  + [Twitter/X](https://twitter.com/BHinfoSecurity)
  + [Upcoming Events](https://blackhillsinfosec.com/events)
* [Fun Stuff](https://spearphish-general-store.myshopify.com/)
  + [Backdoors & Breaches](https://www.blackhillsinfosec.com/tools/backdoorsandbreaches/)
  + [Merch, Zines & More](https://spearphish-general-store.myshopify.com/)
  + [PROMPT# Zine](https://www.blackhillsinfosec.com/prompt-zine/)
  + [REKCAH](https://www.blackhillsinfosec.com/rekcah/)
  + [Books](https://www.blackhillsinfosec.com/tools/books/)

6
Aug
2025

[Informational](https://www.blackhillsinfosec.com/category/informational/), [InfoSec 101](https://www.blackhillsinfosec.com/category/infosec-101/), [Red Team Tools](https://www.blackhillsinfosec.com/category/red-team/tool-red-team/)
[Infosec for Beginners](https://www.blackhillsinfosec.com/tag/infosec-for-beginners/), [InfoSec Survival Guide](https://www.blackhillsinfosec.com/tag/infosec-survival-guide/), [netcat](https://www.blackhillsinfosec.com/tag/netcat/)

# [Netcat (nc) Cheatsheet](https://www.blackhillsinfosec.com/netcat-cheatsheet/)

Written by [Rachi](https://www.linkedin.com/in/rach1tarora/)[t Arora](https://www.linkedin.com/in/rach1tarora/) || Revised by [Dave Blandford](https://www.blackhillsinfosec.com/team/david-blandford/)

![](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/BLOG_cheatsheet_2.png)

**This blog is part of **Offensive Tooling Cheatsheets: An Infosec Survival Guide Resource**. You can learn more and find all of the cheatsheets HERE:** **<https://www.blackhillsinfosec.com/offensive-tooling-cheatsheets/>**

**Netcat (nc) Cheatsheet**: [PRINT-FRIENDLY PDF](https://www.blackhillsinfosec.com/wp-content/uploads/2025/08/CheetSheet_Netcat.pdf)

Find the tool here —

*UNIX version:*

* [https://nc110.sourceforge.io/](https://nc110.sourceforge.io/%20%20)

* <https://sourceforge.net/p/nc110/git/ci/master/tree/>

*GNU Netcat version:*

* [https://netcat.sourceforge.net/](https://netcat.sourceforge.net/%20%20)

* <https://sourceforge.net/p/netcat/code/HEAD/tree/>

---

Netcat is a network utility tool that has earned the nickname “The Swiss Army Knife” of networking. It can be used for file transfers, chat/messaging between systems, port scanning, and much more. Netcat operates by reading and writing data across network connections using TCP and UDP.

## **How to Install:**

### **Kali Linux**

Netcat is available in multiple versions. You can choose one depending on your needs:

*Ncat (Nmap’s Netcat reimplementation):*

```
sudo apt install ncat
```

*OpenBSD Netcat:*

```
sudo apt install netcat-openbsd
```

*Traditional Netcat:*

```
sudo apt install netcat-traditional
```

### **Arch Linux**

GNU Netcat:

```
sudo pacman -S gnu-netcat
```

OpenBSD Netcat:

```
sudo pacman -S openbsd-netcat
```

### **MacOS**

Install using Homebrew:

```
brew install netcat
```

### **Windows**

Your best bet is to use **Ncat**, which is included with the Nmap suite:

* <https://nmap.org/download.html#windows>

*Ensure the Ncat checkbox is selected when installing Nmap.*

## **Explanation of Flags:**

|  |  |
| --- | --- |
| `-z` | Zero-I/O mode, used for scanning ports without sending data. |
| `-v` | Verbose mode, displays additional details of the connection. |
| `-vv` | Very verbose, shows even more detailed information. |
| `-n` | Numeric-only IP addresses, no DNS resolution. |
| `-u` | Use UDP. |
| `-l` | Listen mode, allows Netcat to wait for incoming connections. |
| `-p <port>` | Specifies the local port to use for the connection; not just for listening. |
| `-e <program>` | Executes the specified program (like /bin/bash) upon connection. |
| `-w <seconds>` | Specifies a timeout in seconds for connections. |
| `-X <proxy_type>` | Use a proxy (CONNECT, SOCKS4, SOCKS5) to route Netcat traffic. *Note: This flag is supported in the OpenBSD version of Netcat (and tools like Ncat from Nmap), but not in the traditional GNU version.* |
| `-x <proxy_ip:proxy_port>` | Defines the proxy IP and port for tunneling traffic.  *Same note: Available in OpenBSD Netcat and Ncat, not in GNU Netcat-traditional.* |

### **1. Basic Connectivity**

Check if a specific port is open or closed:

```
nc -zv <target_ip> <port>
```

Scan multiple ports on a target:

```
nc -zv <target_ip> 20-100
```

Scan all ports with a timeout:

```
nc -zv -w1 <target_ip> 1-65535
```

### **2. Establishing Connections**

Connect to a TCP service:

```
nc <target_ip> <port>
```

Connect to a UDP service:

```
nc -u <target_ip> <port>
```

Listen for incoming TCP connections:

```
nc -lvp <port>
```

Listen for incoming UDP connections:

```
nc -ulvp <port>
```

### **3. Sending and Receiving Messages**

Send a message to a Netcat listener:

```
echo "Hello, Netcat" | nc <target_ip> <port>
```

Receive messages on a listening Netcat server:

```
nc -lvp <port>
```

### **4. File Transfer Using Netcat**

Send a file over Netcat (sender):

```
cat file.txt | nc <target_ip> <port>
```

Receive a file with Netcat (receiver):

```
nc -lvp <port> > received.txt
```

### **5. Netcat as a Chat Server**

Start a simple chat server (listener):

```
nc -lvp <port>
```

Connect to the chat server (client):

```
nc <server_ip> <port>
```

When one Netcat instance connec...