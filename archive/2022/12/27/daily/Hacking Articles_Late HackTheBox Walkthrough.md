---
title: Late HackTheBox Walkthrough
url: https://www.hackingarticles.in/late-hackthebox-walkthrough/
source: Hacking Articles
date: 2022-12-27
fetch_date: 2025-10-04T02:31:54.652328
---

# Late HackTheBox Walkthrough

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
»* [Late HackTheBox Walkthrough](https://www.hackingarticles.in/late-hackthebox-walkthrough/)
»

[CTF Challenges](https://www.hackingarticles.in/category/ctf-challenges/), [HackTheBox](https://www.hackingarticles.in/category/ctf-challenges/hackthebox/)

# Late HackTheBox Walkthrough

[December 26, 2022June 19, 2025](https://www.hackingarticles.in/late-hackthebox-walkthrough/) by [Raj](https://www.hackingarticles.in/author/raj/)

Late is a Linux machine and is considered as an easy box by the hack the box. On this box, we will begin with a basic port scan and move laterally based on the findings. Then we will enumerate HTTP services and hunt vulnerabilities present on the web page.  Laterally, we will exploit server-side template injection (SSTI) vulnerability to gain an initial foothold in the target system. Then we will be tasked to gain root access where we will exploit it by abusing file ownership and cron job.

### **Table of Content**

**Initial Access**

* Nmap TCP Port Scan
* Web Page Enumeration
* Vulnerability Assessment
* Server-Side Template Injection Exploitation
* User Flag

**Privilege Escalation**

* Find Privilege Escalation Vectors
* Escalate Privilege via owned file set to cron job
* Root Flag

Let’s exploit it step by step.

### **Initial Access**

We are going to start the assessment with regular TCP/IP port scanning.

#### **Nmap TCP Port Scan**

We begin with the port scan where we are using nmap to find out which ports are open and what services are running in the target host. Nmap is a popular port scanning tool comes with Kali Linux. To perform a port scan, we have used –**sV** flag which performs a service version against the target machine.

Flags features:

**-sV**:  Attempts to determine the service version

```
nmap -sV 10.129.227.134
```

From the nmap scan, we have found there were only two ports open, which is port **22** and port **80**. As usual **HTTP service** is running on port 80 and the **SSH service** is running on port 22.  HTTP service is used for webhosting where SSH service is used for remote connection. We did not find any vulnerabilities on SSH version 7.6p1 and the possible attack we can perform against the SSH service at this stage is bruteforce only which we might not need to. Instead of thinking about the SSH bruteforce let’s start enumerating port 80.

**![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxuy19MFOEaaSW8mVOtzd2NzaVpxhB7ZaKt7apYhpnbATt6-ijxr7U3yw7GZWKxASjW0n3iqiOnwiaGJkuU8n0cUtgLZ4Jpbhc2F35W-XNLdYxg5urN2NICr6g_A5i6aVlFDh-d17KaLbstxsGDTIpGIM9NgELsv9SCLdoFchCloAJC2f0snJHZ6MTWQ/s16000/1.png)**

#### **Web Page Enumeration**

We enumerate port 80 and access it over the browser shown an Image related website. Nothing looks interesting here on the web page, we saw a heading “**Worlds Simplest Image Utilities**” that works for graphics and the title “**late**” which can be a potential domain name.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqcEiLLMfUHovWDk6UtJaiaK01JgkbkxFJt7hBhl79w5mfWGCPTl2VKIbJomaC4mHGJqzSLeiSDQD1edITcmyg3MU0Vg4WYt3HE2rsyhf_fk5BR7qXd5CH08H1CKUrQ0sdNkaCs5SGr2Hr6sJM42z4YxSW3ze0riChl9xhOYxJj3675A5lRPdjWoaHpg/s16000/2.png)

Then we checked the source code of the web page as many times we find sensitive information in the comment section and URLs. There we found a domain name **http://images.late.htb/****.**

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZxyHwZUgFhti45C3fRgAwsK2MQbzaknA-ha2RGVY58m6E03Ki4u3aOpsG86D0KVM0tzMwHExwXnmkyCIzj_6wUDKMDxeI5bbMuxsxK0QbLrnRC1rbmEZYzHsWPzwf-rbKhQ5-2UN0eRCyFC94najGTYpgv-lL9rndvDsfdqhlnji_DRfs-4qe55zqzg/s16000/3.png)

Next, we added the domain name into the /etc/hosts file in our attacking machine to enumerate further about Domain. You can use any text editor to add the domain to hosts file.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiGg3vq7e-b9OGQQmwdBmr4QgsO1v4O8STxyIwonosFfWXTm06ck37wtp12zIfc6UZjVqSyjZp_sCkvr8Hefho2zzkm8ebEMplwIAwoKdqH0QjklW36tJbLEAiXmbPNzUqt64EFXU9xjaWJT4fARIsdQtIA14pfNoA1hmmeD9Ul0S3tkJYf2ZkRunwlA/s16000/4.png)

#### **Vulnerability Assessment**

After adding it to the hosts file, we accessed **http://image.late.htb** over the browser and we got a new web page where we can upload images. After analysing the functionalities of the web page, we found that the web page converts any image into text format. For example, if we have any text on an image then it will convert it to text format.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8zva_mkECtecn3YNU6iUbEpdofsY7yuI9qJVmhYogfmuHAw3Dzf1D8rxbOz-hKoLuG8I6N45bX_MUZs-xFecLpfudNuszsIxaKUqPbmdW-bCgJXN42hEtGhEGiH_jfVcn3pif-n4M7x4Eqy5rD8aeerOzrClIqkrrCDNE2lJu-ne0AnMjHaal5Q5mgA/s16000/5.png)

Then we decided to check how it functions and also created a Server-Side Template Injection (SSTI) payload and saved it as payload.png which makes sense as it converts images to text. We can write a payload using text editor and take a screenshot and save it as png format as well.

```
{{7*7}}
```

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIEeWntctIZiDt8jTB6klE4sgUnyH62CoCoJdghZ7CZ_P2LPU_v-QNwhJBi9Od3VwC7IZAWdxdQAMMGfGKdRc8M785ZzZfAE5J9lgyNGrtn-p01A1jrQZq8-DH7w4ukJ3DNVcJb6DdEobBlTRCSSYEuAzBRCObgM4eNMcX2tZnwCqysH9uwJO_yDFbOA/s16000/6.png)

After creating our payload, we uploaded it to the web page. You can click on the browse tab and upload it from the directory you have kept our payload.png file. We can see **Convertio** CMS is being used to convert image file to text files. **Convertio** is a popular open-sourced image-to-text convertor.

![](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjzMOjkBjqOKA9qjTlmPfGpLcI6m5Y0udT74v7wrCXmD07s7KOzmPBIU5hP34FbS0DhyofpMZuJQMyBxYEiQGcmBz9OyvFW5WK4H7i5QUh5Go_5IUrNgBuc5TbPZvVmO1-mXGqIxcvmUL2mXdTtBM8r_8acfvbtrYO4XD7U4mdPHuSaV81x6l81wjAhMg/s16000/7....