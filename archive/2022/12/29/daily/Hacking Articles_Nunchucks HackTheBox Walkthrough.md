---
title: Nunchucks HackTheBox Walkthrough
url: https://www.hackingarticles.in/nunchucks-hackthebox-walkthrough/
source: Hacking Articles
date: 2022-12-29
fetch_date: 2025-10-04T02:38:22.112717
---

# Nunchucks HackTheBox Walkthrough

[Skip to content](#content)

Hacking Articles

## Recent Posts

* [AWS: IAM CreateLoginProfile Abuse](https://www.hackingarticles.in/aws-iam-createloginprofile-abuse/)
* [Privacy Protection: Encrypted DNS](https://www.hackingarticles.in/privacy-protection-encrypted-dns/)
* [Privacy Protection: Windows Privacy](https://www.hackingarticles.in/privacy-protection-windows-privacy/)
* [Privacy Protection: Browsers](https://www.hackingarticles.in/privacy-protection-browsers/)
* [Privacy Protection: Password Manager](https://www.hackingarticles.in/privacy-protection-password-manager/)

## Most Used Categories

* [CTF Challenges](https://www.hackingarticles.in/category/ctf-challenges/) (504)
  + [VulnHub](https://www.hackingarticles.in/category/ctf-challenges/vulnhub/) (311)
  + [HackTheBox](https://www.hackingarticles.in/category/ctf-challenges/hackthebox/) (164)
* [Penetration Testing](https://www.hackingarticles.in/category/penetration-testing/) (408)
* [Red Teaming](https://www.hackingarticles.in/category/red-teaming/) (126)
* [Website Hacking](https://www.hackingarticles.in/category/website-hacking/) (64)
* [Cyber Forensics](https://www.hackingarticles.in/category/cyber-forensics-tricks/) (68)
* [Privilege Escalation](https://www.hackingarticles.in/category/privilege-escalation/) (59)
* [Hacking Tools](https://www.hackingarticles.in/category/collection-of-hacking-tools/) (33)
* [Pentest Lab Setup](https://www.hackingarticles.in/category/pentest-lab-setup/) (29)

# [Hacking Articles](https://www.hackingarticles.in/)

Raj Chandel’s Blog

Search for:

Menu

* [Courses We Offer](https://www.hackingarticles.in/courses-we-offer/)
* [CTF Challenges](https://www.hackingarticles.in/ctf-challenges-walkthrough/)
* [Penetration Testing](https://www.hackingarticles.in/penetration-testing/)
* [Web Penetration Testing](https://www.hackingarticles.in/web-penetration-testing/)
* [Red Teaming](https://www.hackingarticles.in/red-teaming/)
* [Donate us](https://www.hackingarticles.in/donate-us/)

* [Home](https://www.hackingarticles.in/)
»* [CTF Challenges](https://www.hackingarticles.in/category/ctf-challenges/)
»* [Nunchucks HackTheBox Walkthrough](https://www.hackingarticles.in/nunchucks-hackthebox-walkthrough/)
»

[CTF Challenges](https://www.hackingarticles.in/category/ctf-challenges/), [HackTheBox](https://www.hackingarticles.in/category/ctf-challenges/hackthebox/)

# Nunchucks HackTheBox Walkthrough

[December 28, 2022June 19, 2025](https://www.hackingarticles.in/nunchucks-hackthebox-walkthrough/) by [Raj](https://www.hackingarticles.in/author/raj/)

Nunchucks is a Linux machine and is considered an easy box by the hack the box. On this box, we will begin with a basic port scan and move laterally based on the findings. Then we will enumerate HTTP services and hunt vulnerabilities present on the web page.  Laterally, we will exploit server-side template injection (SSTI) vulnerability to gain an initial foothold in the target system. Then we will exploit Perl capabilities to gain a root shell.

### Table of content

**Initial Access**

* Nmap TCP Port Scan
* Web Page Enumeration
* Directory Bruteforce
* Vulnerability Assessment
* Server-Side Template Injection Exploitation
* User Flag

**Privilege Escalation**

* Find Privilege Escalation Vectors
* Escalate Privilege exploiting Perl capabilities
* Root Flag

Let’s exploit it step by step.

### Initial Access

We are going to start the assessment with the normal TCP/IP port scanning.

#### **Nmap TCP Port Scan**

We begin with the port scan where we are using nmap to find out which ports are open and what services are running in the target host. Nmap is a popular port scanning tool that comes with Kali Linux. To perform port scan, we have used –**sV** and **-an sC** flag which performs a service version with default NSE scripts against the target machine.

Flags features:

-sV:  Attempts to determine the service version

-sC: Scans with default NSE scripts

```
nmap -sV -sC 10.129.30.114
```

From the nmap scan, we have found there were only three ports open, which are port **22,80** and port **443**. As usual **HTTP and HTTPS service** is running on port 80 and 443 and **SSH service** is running on port 22.  HTTP and HTTPS service is used for Webhosting whereas SSH service is used for remote connection. We did not find any vulnerabilities on SSH version 8.2p1 and the possible attack we can perform against the SSH service at this stage is Bruteforce only which we might not need to do. Furthermore, it is hosted on **nginx 1.18.0**, and we can see that port HTTP is redirecting to HTTPS. Also, we found a domain name which is **nunchucks.htb.**

**![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiTjqBREHNq9yK9uvxehPNaIgnLFDDp5RWuxT9blS4_Yo6HzcF8s0uXAzHo90-eizhN0-Kr2Ienqn4idiXlRYUehLZcOSVzXz_4v488rkK6BGKlkhSb88EUXimwbWYpnNMk7FRexUvv123mLgmPWAoVPboqEaRH7DB0M7q8WwLoDXQCJGQOwYkaWENjGQ/s16000/1.png)**

We added **nunchucks.htb** to our /etc/host file for further analysis.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgjZVJFqYRbnAzqXR-fRtskQqQKZ36FgkJ0YPdYFiCaR-2JDcYxPVcM6-ROIgApzzMsNnixqjQOv2fGotCVLf0oNcTstfIFMjA8LEfVFDocmYDcjltjoccMnQK_W_aeutqXfTbbk_JX7lqNtKq7N5cwt2Rt1adt0WvVd95t1P_a17k_rwFhb1uWdqxeNw/s16000/2.png)

#### **Web Page Enumeration**

We enumerate port 443 and access it over the browser showing an online shopping website which comes with eCommerce features. Nothing looks interesting here on the web page, so we decided to go with the subdomain fuzzing as we already have a target domain name.

**![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgMiDQtb_s-5WjlV0DchPEIHiHYkp3EOg_HF1Dg16Sq8rFvH0pUWil5XQZ2CqcUvm86bCKUFck6XRBA9CunOSh94DRIgQzE0x0ZClAlFkBL8j-eN1FS1rcUWsaj2VuVf7d83UFnoYh8RkavUglmSlXePsbfUl4T33t_OcCoZUGhMVUOZiPxaEHkRzcasg/s16000/3.png)**

#### **Directory Bruteforce**

We used wffuz tool to find any potential subdomains as the webpage is related to an online shop, there are high chances to find other subdomains which are working with the primary domain. Here we are using common wordlists and set **–hw** flag to hide responses with the specified words. If we do not use this flag, then we will get a lengthy output. Then we set the fuzzing point on the domain which comes before the domain name. As expected, we found a subdomain **store.nunchucks.htb.**

```
wfuzz -c -w /usr/share/wordlists/dirb/common.txt -t30 --hw 2271 -H "Host:FUZZ.nunchucks.htb" https://nunchucks.htb/
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj0BpEobOUX-8xPexI-tbw1easpfA0eLjFGN1hhTV8z2m0WqnLaJbywHCypjGCb4KlgRrAzcIQAZrbe5vqBXbA1wLHgsquaR8up5SjSZ3diH42uAkaTabdrpFXlaAffidnI5_MtoFMCYQqkM5Yi2Gsc4XCxcge2UKyrC9KJRGp2XqLXy4ln6akFoE5xLQ/s16000/4.png)

Next, we added subdomain into the /etc/hosts file in our attacking machine to enumerate further. You can use any text editor to add domain to hosts file.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiCAFXnvmI_0hQbmsVbTxXwqthuL340uksm4TRDIiD64ySlCznHZDHK_4Ds2z4vvAO3M6ljfg9XJ04jmdixU2mDSR3A-sn_NQDra2u-SCmoFewELqEAGR01Ps5QuEVmGEU5Juv2SKdyn8VKPKnu0LNfCJ3yFIG-OoXC18Dk678tx1YOJTINd1HZicZbMA/s16000/6.png)

#### **Vulnerability Assessment**

After adding it to the hosts file, we accessed **https://store.nunchucks.htb** over the browser and we got a new web page. The webpage looks normal as other web pages. We checked the source code and all available pages but did not find anything interesting there. Then we went to the main page and saw a user input field which is made to receive notifications. If we give our email address in the “Your email here” field, then we will receive a notification from https://store.nunchucks.htb but we do not want that. Our primary goal is to find vulnerabilities here.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjZoj6RUY5NAomZQSNN_VtSagSHQKY7uN5clLs-bxMWomQdO4bBQnzMAugjLyAngWlZKN2MqQQ6U4n3xcA7Bp_BKu-8yFe5HICCn-M8_cqbAyLoD-y0bI1T6ycZp2sTFV4YJxOeQ-k0-PFXC2f35pU3zbdDLYrQiGOcCkUf...