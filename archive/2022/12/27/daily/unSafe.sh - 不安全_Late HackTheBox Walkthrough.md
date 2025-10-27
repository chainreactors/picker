---
title: Late HackTheBox Walkthrough
url: https://buaq.net/go-141491.html
source: unSafe.sh - 不安全
date: 2022-12-27
fetch_date: 2025-10-04T02:32:07.341500
---

# Late HackTheBox Walkthrough

* [unSafe.sh - дёҚе®үе…Ё](https://unsafe.sh)
* [жҲ‘зҡ„ж”¶и—Ҹ](/user/collects)
* [д»Ҡж—ҘзғӯжҰң](/?hot=true)
* [е…¬дј—еҸ·ж–Үз«](/?gzh=true)
* [еҜјиҲӘ](/nav/index)
* [Github CVE](/cve)
* [Github Tools](/tools)
* [зј–з Ғ/и§Јз Ғ](/encode)
* [ж–Үд»¶дј иҫ“](/share/index)
* [Twitter Bot](https://twitter.com/buaqbot)
* [Telegram Bot](https://t.me/aqinfo)
* [Search](/search/search)

[Rss](/rss.xml)

[ ]
й»‘еӨңжЁЎејҸ

![](https://8aqnet.cdn.bcebos.com/497efb0c2a5da4997c75730e88af2486.jpg)

Late HackTheBox Walkthrough

SummaryLate is a Linux machine and is considered as an easy box by the hack the bo
*2022-12-26 17:59:57
Author: [www.hackingarticles.in(жҹҘзңӢеҺҹж–Ү)](/jump-141491.htm)
йҳ…иҜ»йҮҸ:31
ж”¶и—Ҹ*

---

### **Summary**

Late is a Linux machine and is considered as an easy box by the hack the box. On this box, we will begin with a basic port scan and move laterally based on the findings. Then we will enumerate HTTP services and hunt vulnerabilities present on the web page. В Laterally, we will exploit server-side template injection (SSTI) vulnerability to gain an initial foothold in the target system. Then we will be tasked to gain root access where we will exploit it by abusing file ownership and cron job.

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

LetвҖҷs exploit it step by step.

### **Initial Access**

We are going to start the assessment with regular TCP/IP port scanning.

#### **Nmap TCP Port Scan**

We begin with the port scan where we are using nmap to find out which ports are open and what services are running in the target host. Nmap is a popular port scanning tool comes with Kali Linux. To perform a port scan, we have used вҖ“**sV** flag which performs a service version against the target machine.

Flags features:

**-sV**:В  Attempts to determine the service version

```
nmap -sV 10.129.227.134
```

From the nmap scan, we have found there were only two ports open, which is port **22** and port **80**. As usual **HTTP service** is running on port 80 and the **SSH service** is running on port 22.В  HTTP service is used for webhosting where SSH service is used for remote connection. We did not find any vulnerabilities on SSH version 7.6p1 and the possible attack we can perform against the SSH service at this stage is bruteforce only which we might not need to. Instead of thinking about the SSH bruteforce letвҖҷs start enumerating port 80.

**![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgxuy19MFOEaaSW8mVOtzd2NzaVpxhB7ZaKt7apYhpnbATt6-ijxr7U3yw7GZWKxASjW0n3iqiOnwiaGJkuU8n0cUtgLZ4Jpbhc2F35W-XNLdYxg5urN2NICr6g_A5i6aVlFDh-d17KaLbstxsGDTIpGIM9NgELsv9SCLdoFchCloAJC2f0snJHZ6MTWQ/s16000/1.png?w=640&ssl=1)**

#### **Web Page Enumeration**

We enumerate port 80 and access it over the browser shown an Image related website. Nothing looks interesting here on the web page, we saw a heading вҖң**Worlds Simplest Image Utilities**вҖқ that works for graphics and the title вҖң**late**вҖқ which can be a potential domain name.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqcEiLLMfUHovWDk6UtJaiaK01JgkbkxFJt7hBhl79w5mfWGCPTl2VKIbJomaC4mHGJqzSLeiSDQD1edITcmyg3MU0Vg4WYt3HE2rsyhf_fk5BR7qXd5CH08H1CKUrQ0sdNkaCs5SGr2Hr6sJM42z4YxSW3ze0riChl9xhOYxJj3675A5lRPdjWoaHpg/s16000/2.png?w=640&ssl=1)

Then we checked the source code of the web page as many times we find sensitive information in the comment section and URLs. There we found a domain name **<http://images.late.htb/>****.**

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZxyHwZUgFhti45C3fRgAwsK2MQbzaknA-ha2RGVY58m6E03Ki4u3aOpsG86D0KVM0tzMwHExwXnmkyCIzj_6wUDKMDxeI5bbMuxsxK0QbLrnRC1rbmEZYzHsWPzwf-rbKhQ5-2UN0eRCyFC94najGTYpgv-lL9rndvDsfdqhlnji_DRfs-4qe55zqzg/s16000/3.png?w=640&ssl=1)

Next, we added the domain name into the /etc/hosts file in our attacking machine to enumerate further about Domain. You can use any text editor to add the domain to hosts file.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjiGg3vq7e-b9OGQQmwdBmr4QgsO1v4O8STxyIwonosFfWXTm06ck37wtp12zIfc6UZjVqSyjZp_sCkvr8Hefho2zzkm8ebEMplwIAwoKdqH0QjklW36tJbLEAiXmbPNzUqt64EFXU9xjaWJT4fARIsdQtIA14pfNoA1hmmeD9Ul0S3tkJYf2ZkRunwlA/s16000/4.png?w=640&ssl=1)

#### **Vulnerability Assessment**

After adding it to the hosts file, we accessed **http://image.late.htb** over the browser and we got a new web page where we can upload images. After analysing the functionalities of the web page, we found that the web page converts any image into text format. For example, if we have any text on an image then it will convert it to text format.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj8zva_mkECtecn3YNU6iUbEpdofsY7yuI9qJVmhYogfmuHAw3Dzf1D8rxbOz-hKoLuG8I6N45bX_MUZs-xFecLpfudNuszsIxaKUqPbmdW-bCgJXN42hEtGhEGiH_jfVcn3pif-n4M7x4Eqy5rD8aeerOzrClIqkrrCDNE2lJu-ne0AnMjHaal5Q5mgA/s16000/5.png?w=640&ssl=1)

Then we decided to check how it functions and also created a Server-Side Template Injection (SSTI) payload and saved it as payload.png which makes sense as it converts images to text. We can write a payload using text editor and take a screenshot and save it as png format as well.

```
{{7*7}}
```

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjIEeWntctIZiDt8jTB6klE4sgUnyH62CoCoJdghZ7CZ_P2LPU_v-QNwhJBi9Od3VwC7IZAWdxdQAMMGfGKdRc8M785ZzZfAE5J9lgyNGrtn-p01A1jrQZq8-DH7w4ukJ3DNVcJb6DdEobBlTRCSSYEuAzBRCObgM4eNMcX2tZnwCqysH9uwJO_yDFbOA/s16000/6.png?w=640&ssl=1)

After creating our payload, we uploaded it to the web page. You can click on the browse tab and upload it from the directory you have kept our payload.png file. We can see **Convertio** CMS is being used to convert image file to text files. **Convertio** is a popular open-sourced image-to-text convertor.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjzMOjkBjqOKA9qjTlmPfGpLcI6m5Y0udT74v7wrCXmD07s7KOzmPBIU5hP34FbS0DhyofpMZuJQMyBxYEiQGcmBz9OyvFW5WK4H7i5QUh5Go_5IUrNgBuc5TbPZvVmO1-mXGqIxcvmUL2mXdTtBM8r_8acfvbtrYO4XD7U4mdPHuSaV81x6l81wjAhMg/s16000/7.png?w=640&ssl=1)

Once we convert our file, we can download it by clicking on download tab and it will be saved as **results.txt** in our download directory. After downloading the file, we checked the result and found that Convertio is vulnerable to Server-Side Template Injection (SSTI). If we get the sum of the given argument, then it is quite promising that the server is vulnerable to SSTI. For example, we have given {{7\*7}}in our payload and received 49 as the sum of 7\*7.

В A server-side template injection (SSTI) vulnerabilityВ **occurs when user data is embedded directly in a template and then interpreted by the template engine**. This allows attackers to inject arbitrary directives to manipulate the template engine.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj_qOed2891k31muaO4YRFgDDXLYecmcP0P5r2zaXqPf_CLEtmnGKv6YgDFy85YI43H6jhBPHFfeMjVjNzgWdjJrir3nVr4RdDCG8QnK8UQ6KmCA1cuulkAv8g5c5VQ6qhk3pQlCLeTTJ0_fubfHmjEzJiSD-khGAH5DfzCT6L9ogvC7Pud-iOXLc-b_g/s16000/8.png?w=640&ssl=1)

Then we decided to check the users in the target system. The user file is available in the /etc/passwd file. SSTI works similarly as Local File inclusion vulnerability, but it has a different syntax which is available here:

**<https://github.com/swisskyrepo/PayloadsAllTheThings/tree/master/Server%20Side%20Template%20Injection>**

We created a new payload to read /etc/passwd file from the target system and repeated the same process.

```
{{ get_flashed_messages.__globals__.__builtins__.open("/etc/passwd").read() }}
```

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhLVW7CalF_TwctPTjegYAXGo_P_58VHx8Y0RwzAWppRx53_qbI...