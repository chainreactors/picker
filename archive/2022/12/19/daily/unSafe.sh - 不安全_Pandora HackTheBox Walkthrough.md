---
title: Pandora HackTheBox Walkthrough
url: https://buaq.net/go-140421.html
source: unSafe.sh - 不安全
date: 2022-12-19
fetch_date: 2025-10-04T01:53:21.767937
---

# Pandora HackTheBox Walkthrough

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

![](https://8aqnet.cdn.bcebos.com/938f0ccc839794133c799d5d29f7a52f.jpg)

Pandora HackTheBox Walkthrough

SummaryPandora is a Linux machine and is considered an easy box by the hack the bo
*2022-12-18 04:6:19
Author: [www.hackingarticles.in(查看原文)](/jump-140421.htm)
阅读量:29
收藏*

---

### **Summary**

Pandora is a Linux machine and is considered an easy box by the hack the box but indeed it is not. With this box, we will need to perform another port scan instead of being relied on only TCP ports results. Then we will dig into SNMP protocol and find out very interesting information for us which will lead us to an initial foothold to the target machine. Then we will need to perform Horizontal privilege escalation and local port forward to enumerate service running on the target’s internal port. Then we will exploit the admin console which is vulnerable to SQL injection and upload a malicious file to get a reverse shell as a different user. In the post-exploitation phase, we will abuse the SUID binary using path hijacking technique.

### **Table of Content**

**Initial Access**

* TCP Port Scan
* Enumeration
* UDP Port Scan
* SNMP Enumeration
* User Shell as Daniel

**Horizontal Privilege Escalation**

* Enumeration
* Port Forwarding
* CVE-2021-32099 SQL injection Exploitation
* File Upload
* User Flag

**Privilege Escalation**

* SSH Key Generate
* SUID Path hijack
* Root Flag

Let’s exploit it step by step.

### **Initial Access**

We are going to start the assessment with the TCP/IP port scanning.

#### **TCP Port Scan**

Let’s start with the port scan. We are using nmap to find out which ports are open so we can begin our port and service analyse. Nmap is a popular port scanning tool come with Kali Linux. In order to perform port scan, we have used **-sC** and **-sV** flags.

Flags features:

**-sC**   : Scans with default NSE scripts

**-sV**   :  Attempts to determine the service version

**Command used:**

```
nmap -sC -sV 10.129.26.243
```

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEggzEIOKKimE5TO1DEb1dOq1Ced9FfQ8yxFD_3qWtKitCIJhWX73NUNykwZV7qG1H-x_YZDGqQUagpjMCzorKJ21k4vkmh0BpM-cE_7qwPmeJqdTSS6qnmxwZZS_G7u7H8Yo9JH29XA5s1FfDUDZ1OYwTDsn7XrGgKuTEqOMd_S_PcwtYX0p40Yx7uoPg/s16000/1.png?w=640&ssl=1)

From the nmap scan, we have found there were only two ports open, which are port **80** and port **22**. As usual **HTTP service** is running on port 80 and the **SSH service** is running on port 22. Http service is used for Webhosting and the SSH service is used for remote connection. SSH version is the latest and does not look vulnerable and the possible attack we can perform against the SSH service at this stage is bruteforce only which we might not need to. Instead of thinking about the SSH bruteforce let’s start enumerating port 80.

#### **Enumeration**

We begin enumeration by accessing port 80 over the browser. The webpage does not have many interesting things, but we can see the domain name is available there which is **Panda.htb**. Next thing we can analyse what this website is made for, and what it does. Remember every website is created for some purpose with this mindset we assumed this website is serving games and network monitoring solutions.

```
htttp://10.129.26.243
```

**![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiqOXWdV-BU1atzeRt_jEHloQrnFNDjLuJdrer05e-OY-zJLwxnjpbd6eh5rRxVbDgjc4X2nY6E8cORDvyAy9Byn5GXrVPpmSRCvWYfWsEQjrWdLHx7zE2YZ7jg8Nb4uth35ULKEDAESt0ykZNiU1JxQKNh0ZdhBmJTZtsR5R84ZAL31y40rjRBwcMVug/s16000/2.png?w=640&ssl=1)**

#### **UDP Port Scan**

Got stuck for some time as we did not get any lead to get a foothold into the target system, we decided to perform a UDP port scan. When we do a normal nmap scan, it only scans TCP ports but not UDP so many time UDP ports may lead us to interesting findings. After the completion of the UDP port scan, we found that **SNMP** port is open on its default port which is **port 161**. Now we can go for further enumeration against the SNMP port but let’s talk about SNMP first.

**What is SNMP and what it is used for?**

Simple Network Management Protocol (SNMP) is a networking protocol used for the monitoring and management of the network-connected end devices in the internet protocol networks. It is embedded in multiple local devices such as routers, switches, servers, firewalls, and wireless access points using IP addresses. It runs on **UDP protocol** and uses port **161** and **162** as its default port.

```
nmap -sU 10.129.26.243
```

Flags features:

**-sU**: Scans UDP ports

**![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgrMrWF_XbDQb-hOAxMz3E_V4OjNuGTJJ2XJZ_UsAj4nAwIlDXyDhcXL5Skzqa_T7gvd_EX26O4iQJa73hr8RmJfRpcfeMTTjI7apvP4GENN0X1tLC9J7grBbUuQf4O83VzQkQnTjaKL0PIcBMm-asrIp6WSVx9hsU1qqNWuDxozAaP1VlHpn4ns4IHPQ/s16000/3.png?w=640&ssl=1)**

#### **SNMP Enumeration**

 Once we found that the SNMP service is running and the port is open on 161, we are in the position to go for the further enumeration process. In order to enumerate SNMP service, we need to know what we are going to enumerate on that service which will give us important information that will be useful for future analysis and assessment. Whenever we come to enumerate SNMP, we need to focus on a couple of things such as **Community Strings** and **versions.** In most of cases, community strings is **public** and the version may be different in each case. There are three versions in the SNMP, which are V1, V2 and V3 which are differentiated by their features. In the table below we can see each version has different security features from weak to encrypted.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgbJbPdiNTUmeELwvJAHrw1zkMb926A1K7UNtdX-m6TuzP64-S0NfYp4M_ZRgnD5596Kun3_qNXay0_YWV8fRlNqDvETybuNyORPpNHHLxEk6ixYTNQb95K12gGzCmjPT3tWtyRLrhltbBmJjYc1ct02V9xTBG3YUx0H_QPvXQMXkvFRK1ojyU-0-ZYsQ/s16000/50.png?w=640&ssl=1)

We will enumerate community strings and the version with **snmp-check.**

```
snmp-check 10.129.26.243
```

With snmp-check, we have found that SNMPv1 is used, and the community string is public. Now we are in a position to enumerate further based on the community strings and the version. For that, we will use **snmpwalk.**

```
snmpwalk -c public -v1 10.129.26.243
```

Snmpwalk has given an interesting finding here, if we scroll down, we will see there a username **daniel** and password **HotelBabylon23** is there. From here, we can think about login in via SSH as SSH port is open and we can test with found credentials.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgz5_wXSsESof1EcSHqAeEVVLcP3K4o5P1XNUJTug5twycEhpeG-FaTZV0BlNN5PANFDr7kuDkE8A1s5GnFkzDP3k6qKqu3p9E5GI5yXHQp4F6bmgcCdJtXoTy0153MA32MDu2xxiQQgU3Yx6pvXA6oZXaJ5t_hLsvWfJfvFbTzUgXmE_yKWHwFRY_0IA/s16000/4.png?w=640&ssl=1)

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhIzhQc0atLMGu29RRqRXWw4aBoit3DSKfIscJ_nkVseoLGm7OfR9_TdUigJLJYiN9UMaOn1YtcnBVsSJlJ7Ct5h-3-Zd6wxg8XYvpYzOA8KlHj7N9YivOLB7_PIFBoOEBlRdQqDBpHtHnBQyBr0l2VrV1KTXQRR8evLJ20TuPca6M3WGnd8yUeMJ6dVQ/s16000/5.png?w=640&ssl=1)

#### **User Shell as Daniel**

We have successfully logged in as Daniel and tried to retrieve our user flag but unfortunately, we do not have permission to get the user flag as it is belonging to user **matt**. To retrieve the user flag, we need to compromise matt account then only it is possible to retrieve the flag contents?

```
ssh [email protected]
cd /home
cd matt
ls
cat user.txt
```

**![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgNqb2KiKWgPSu5AzLSuu3...