---
title: Backdoor HackTheBox Walkthrough
url: https://buaq.net/go-141277.html
source: unSafe.sh - 不安全
date: 2022-12-25
fetch_date: 2025-10-04T02:29:02.448781
---

# Backdoor HackTheBox Walkthrough

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

![](https://8aqnet.cdn.bcebos.com/f0a9ab8c2c7f648280a43ab926ff39e1.jpg)

Backdoor HackTheBox Walkthrough

SummaryBackdoor is a Linux machine and is considered an easy box the hack the box.
*2022-12-24 23:17:54
Author: [www.hackingarticles.in(查看原文)](/jump-141277.htm)
阅读量:33
收藏*

---

### Summary

Backdoor is a Linux machine and is considered an easy box the hack the box. On this box we will begin with a basic port scan and move laterally. Then we will enumerate the WordPress webpage.  Then we will do a vulnerability assessment and exploit directory traversal vulnerability. From the running process, we will be exploiting the GDB server and gain an initial foothold in the target system. Then we will be tasked to gain root access where we will exploit SUID is set to screen.

### Table of Content

**Initial Access**

* Nmap TCP Port Scan
* Web Page Enumeration
* Searching For the WordPress eBook Exploit
* Directory Traversal Vulnerability Exploit
* Enumerate Running process in the target system
* Searching for the GDB Server Exploit
* GDB Server RCE Exploitation
* User Flag

**Privilege Escalation**

* SUID-Screen Exploitation
* Root Flag

Let’s exploit it step by step.

### Initial Access

We are going to start the assessment with the normal TCP/IP port scanning.

#### **Nmap TCP Port Scan**

Let’s start with the port scan. We are using nmap to find out which ports are open and what services are running in the target host. Nmap is a popular port scanning tool comes with Kali Linux. To perform port scan, we have used –**sV** and **-p-** flag which performs a service version and full port scan against the target machine.

Flags features:

**-sV**:  Attempts to determine the service version

**-p-**:  Attempts to full port scan

```
nmap -p- -sV 10.129.96.68
```

From the nmap scan, we have found there were only three ports open, which is port **22,80** and port **1337**. As usual **HTTP service** is running on port 80, **SSH service** is running on port 22 and we do not know about 1337 now. HTTP service is used for webhosting and the SSH service is used for remote connection. SSH version is latest, and we did not find any vulnerabilities on SSH version 8.2p1 and the possible attack we can perform against the SSH service at this stage is bruteforce only which we might not need to do. Instead of thinking about the SSH bruteforce let’s start enumerating port 80.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiXT8BKzvQenSDShrQsjmUbdom0gIf5Eb5kO36-qplnUXGw-3ESHIAAsaWMU2evNlNAiia_dTzGyftb6dNLu6Kc3-hLM6bNkKZWqyDeIgtoFeF1joqw_qsfZRr6kWHpcdceru3geYPHx4o8Sw9o48M50Coogayw7FfaCL0E8Zv6x2hKMbrJOcOWbFqrHQ/s16000/1.png?w=640&ssl=1)

#### **Web Page Enumeration**

We begin with enumerating port 80 and access it over the browser shown on a WordPress site. Nothing looks interesting here in the web page, we saw a backdoor title of the machine name backdoor. The backdoor could be the domain name here.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEit2s47GBiweoAvmqfql7A5vB554W3pWUCLnN7u-xGUre2UDC-tZmT8cWemdDiauaJBQa3jbGsI0f5iBqDxVmyr5VuGZ4deeVM4yPh6EoUt5B4l8yH3T5YoZ5zISzuhHnCyqEOtX0b_dWVryYDheY9KvNzdhsNGmURtpKEwZsxZY_9y5tI1SMuzTDKaCw/s16000/2.png?w=640&ssl=1)

Then we decided to check its plugin using default directories. A list of the default WordPress directories can be available here:

<https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/wordpress>

The default plugin directory path is:

```
/wp-content/plugins/
```

We saw an **ebook-download** directory is present there. We can check if there are any public exploits available for the eBook WordPress plugin.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjYGqREUbvtsd43rmCmbZ61WdMGcNK3-zoYGH7xUwuNhWL70Pv0u-_0qZpnWniR5qtwGCFkX-jv75DBwsxF11geBPAZZ3h2THQnZ-OzrixL64axlEsOvNUvH0nQhi57WquwLxLUOrXgrnTpZpH3cD4d1eevGdG2RviuecS0ttYisDvd_qFA-ILtaPyzdw/s16000/3.png?w=640&ssl=1)

#### **Searching For the WordPress eBook Exploit**

We are using a kali inbuilt tool searchsploit to find out if any exploits are available in the public exploit database. From the searchsploit result, we found that WordPress eBook download has a **directory** **traversal** vulnerability. Then we downloaded the exploit to analyse how it works. We can download it using **-m** flag on searchsploit.  After analysing the exploit code, we found a vulnerable path parameter which is vulnerable to File inclusion.

```
searchsploit ebook wordpress
searchsploit -m 39575
cat 39575.txt
```

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhX2V3EzxDOzvZL7K8qI2M2TPBTeMYJ42-YJBZfmMdKTbWhFA-XkpQSEM32_-28bp4L16BUwBxMyRPL6SDTvsUlcJI-5c_E_TKRZufcp4ZmMJ6fChCIbDvZIJASuk9o3YSX9qdDA2FYuYBlR-ifnoqhEPIWjkyVeNvHAaDivZErLdhlbpqzubR4x15Q4g/s16000/4.png?w=640&ssl=1)

#### **Directory Traversal Vulnerability Exploit**

As we have the vulnerable parameter, now we are in a position to exploit it. We tried to exploit the WordPress configuration file (wp-config) which has sensitive information such as database credentials of the WordPress. As expected, we got the WordPress database username and password but it did not work with any available service.

```
Curl 10.129.96.68/wp-content/plugins/ebook-download/filedownload.php?ebookdownloadurl=../../../wp-config.php
```

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjXhupVNfXqw9tdI5rpKxvoLRAar7Udtrpp1Auz3pepcA4ZhWGB4CgxJ5gjdDMO4rwMAArGExAtWpfAv7XhJ4vYgeTHhUFpIcEYShStiik_QX6bj8fdenIDj6STJ_hOSjuPyCXHj9saaOgElUR0piQP6ZYmqveqIygnPSbON0qrzmVOKdI6FgjPRghfKQ/s16000/5.png?w=640&ssl=1)

Then we decided to list the users in the target system. It is available in the **/etc/passwd** file in Linux systems. We saw a user named **user** is available in the target system and we tried log in via SSH with the obtained password and again failed to gain access.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEj5IbvrNbanscf3ParCvZVdfJjikvQ93GFB7rTJjvM70v71AGCkW4j0PdIVfZMUso1SIXHCm0xivB5Lc55WpRrTr_MEW34ftTd8pB0cLqDQmP9y8kI-PVZBMxHtTZzuKV8fEovwjfRvCYAbNy05fKhRB30QvNfF28k4cATAcuA7Wo670cC6tIxnMQ_gLw/s16000/8.png?w=640&ssl=1)

Many attempts of gaining a foothold in the target system failed. Then we decided to enumerate further. Then we created a bash script to find out what **processes** are running on the target system because sometimes third-party applications may have some vulnerabilities which could lead an attacker to gain access to the target system.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEglDgpS0CQ8HtQm_oZ7xexji1cFQ09-mGdmHfesQ5k5rmEp0tVpcAunMUi6I_QKhPWciqCiAawcL2-PJdnKBDRY6OqpZFrEBGYeYE9jityIB_xP_Ns4ogspU8L5hGEfZrJZ0EseLefxVdM-vwSWdqt8td-NoOms3Nv0w5_PVohYi5jjD9ATxBgCQpyvHA/s16000/9.png?w=640&ssl=1)

As we can see a GDB server is running on the target system. We can check whether we can find any vulnerabilities available for the GDB server. There are possibilities to have some other application installed which is also vulnerable to remote code execution.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjsXv6JSvl1GP1_9kvAvLy2l3EHiNynXvX_FgNsrMz4KRu5SS5MjsGlDfxCP2nT_9IeC69WFnBOOgatlK-wgWtBDJ3EQnYy51prMsty6vcYehPS4R9WkrihIuE1XdVgj_lomT5XxNw5gu7TlMVGw-NO4pLLZEG2FZyEz0oSBa_xn_XejNjcVxgBlj2Csw/s16000/10.png?w=640&ssl=1)

**Alternative:**

We can also check the running process manually, below file can be used to check it. Just need to replace the file name with /proc/sched\_debug on the vulnerable parameter.

```
/proc/sched_debug
```

#### **Searching For the GDB Server Exploit**

We are again us...