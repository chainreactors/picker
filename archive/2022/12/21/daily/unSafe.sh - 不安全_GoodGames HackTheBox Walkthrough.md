---
title: GoodGames HackTheBox Walkthrough
url: https://buaq.net/go-140728.html
source: unSafe.sh - 不安全
date: 2022-12-21
fetch_date: 2025-10-04T02:04:21.040444
---

# GoodGames HackTheBox Walkthrough

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

![](https://8aqnet.cdn.bcebos.com/16ee153b53cf8921e5792d1fe162782f.jpg)

GoodGames HackTheBox Walkthrough

SummaryGoodGames is a Linux machine and is considered an easy box. but it was tric
*2022-12-20 17:43:45
Author: [www.hackingarticles.in(查看原文)](/jump-140728.htm)
阅读量:30
收藏*

---

### **Summary**

GoodGames is a Linux machine and is considered an easy box. but it was tricky indeed. On this box, we will begin with a basic port scan and move laterally. Then we will enumerate domain name and subdomains. Then we will exploit SQL Injection vulnerability using burp and SQLmap. Exploitation of the server-side template injection (SSTI) will give us an initial foothold into the target machine. Then we will be tasked to gain root access where we will exploit it by taking advantage of the special permissions and ownerships both in the server and the Docker. A successful binary abuse will give us a root shell of the target system.

### **Table of Content**

**Initial Access**

* TCP Port Scan
* Initial Enumeration
* Web Page Enumeration
* SQL Injection Exploitation with sqlmap
* Admin Console Enumeration
* Internal Sub Domain Enumeration
* Server-Side Template Injection (SSTI) Exploitation
* User Flag

**Privilege Escalation**

* Docker Enumeration
* SUID Permission abuse
* Root Flag

Let’s exploit it step by step.

### **Initial Access**

We are going to start assessment with the normal TCP/IP port scanning.

#### **TCP Port Scan**

Let’s start with the port scan. We are using nmap to find out which ports are open and what services are running in the target host. Nmap is a popular port scanning tool come with Kali Linux. In order to perform port scan, we have used –**sV** and **-sC** flags which performs a service version scan with NSE scripts against the target machine.

Flags features:

**-sV**:  Attempts to determine the service version

**-sC**:  Scans with default NSE scripts

```
nmap -sV -sC 10.129.33.160
```

From the nmap scan, we have found there was only one port open, which is port **80**. As usual **HTTP service** is running on its default port and the HTTP service is used for the webhosting. Let’s take some notes about our findings.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiO-B64vfMAIyV9rs-C-O6tVoSdRlCVPRvdAIVTaS3a0uXXqwl6DFXXaycI-fy5dhcZuUcEFUcbjL9ZwYzXKdl_vJrtJzvJU-i7x_cTaDA-OMMCop3Ejn-cjbYUikfZSA4xAXN3gMZtB16xowDOhy_ItF6tN7Q6F3jRuaTOKVzIMlg6NTGOip8He4aR6A/s16000/1.png?w=640&ssl=1)

#### **Initial Enumeration**

As we have only one port is open, we begin with port 80 enumerating by accessing it over the browser and found the web page. From the webpage interface, it looks like a video game online store. If we see our nmap result, we gathered earlier showing the http title as Goodgame community and store that makes sense.

**![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi3tk8AQUgjPLBloIyZfIYxFbeKEB0cQi8RcqxgYvo7jcSCCMboSLSZkwzHrbggDf9JxXrqMUkGaKqlKeEf_XsuOWxF1jBXCrEEPIu9qmNEGrR6Bmi4pIT3YHEPqAxGfPMBihZFg122Iv4e1jDbucMY-GKRzIcgTdJ-5PnlD7uySwSS1DRLrk2M5cZzzw/s16000/2.png?w=640&ssl=1)**

#### **Web Page Enumeration**

While enumerating webpage we found a login page. From the login in page, we can enumerate further by registering ourselves as a new member or if we have valid credentials, we can directly log in to do the same.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhi42DeSWIsnJLLk8p1jsI-d9uqrx1O2WeJMJJzgFlm9pmZT7gsAKS6zUG_gDTmKs-tnvYrRZL98eJ9lJM9liGznUapp7hkZ5Tyy5EshqwIz1CxLzN2PUB1EPNgwji5H3YeGPowVf9-uGJ4xP_6H2YSZx57FDLdllnq7eOq85A3DHjG7gqrWRX09S1_cQ/s16000/3.png?w=640&ssl=1)

Before registering a new user account let’s capture the login request on the burp. Here we are using a random email and password. You can use any random credentials to capture request for testing purpose.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEijaKZJG5g9iefocLWc8Hkc2Vz3fl4U6aDsLJOK-YYOUjM1kCrBkKk5WlG-9Vgysyjib8iNP5JpX-_yafrUcYz_V7b8dXjaTHO4wJ8Sp2xzlWIqx10a059pVrDKny5XZQmLPZzDrXKS_qZo1Zia_ZO7bSHmUL2A0bZwtGLOsBLsPj73Fy7dZOqSBjTeJA/s16000/4.png?w=640&ssl=1)

We are capturing login request on burp to check if there is any SQL injection vulnerability present in the target system. We captured the request and saved as **sqlfile**.  The reason we are checking SQL injection vulnerability as there is a login page and it is worth checking SQL injection in login pages and on any user input field. Most of the time, SQL injection vulnerabilities found in user input fields in the web application.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgch5WualdeC0S0xYwGLfrtlsdXbADB94nXVREwDRtL0eDi1Tzi6qx-X9m8sUqtsWEGm3mvXCW-6WLIiDRn7lwxi8cjL4n8tWENavhEp71HVaAAiGgmsV6tGzit9HtlsxErWv3c2TsRzruBKnRy9D19BMnOTHOAy_fvl7UEjBkrIJoVfMdAmjS6M77Wyw/s16000/5.png?w=640&ssl=1)

#### **SQL Injection Exploitation with sqlmap**

Next, we are going to check the database name by loading the login request that we captured on burp. In the below picture, we have loaded **sqlfile** on sqlmap which will be going to find out the database name if the web application login parameter is vulnerable to SQL injection. Full functions of the flags are given below.

```
sqlmap -r sqlfile –dbs --batch
```

**–dbs**: Enumerate DBMS databases

–**-batch**: Never ask for user input, use the default behaviour

**-r**: Request

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjqgpjO4xXhQgO2VX_4JtZrA3pMr-zxokPH17d4gmgfV4XMW0EdinVGA7jeRf9Ah6FZEsNg3kYh3eFbCzxjN8R9E5-vZIxrNPdVh3dafIqjOGmKskDCTcIwpRcTKEOZjdeTMCe2zEgJDc-1XysUNqAhKw4y0Dlm6kWnYzdUSjvmDPWXOYXwuacRJz0BYQ/s16000/6.png?w=640&ssl=1)

Once we get the database name then we will dump all the contents that the database is containing by issuing a request file, and database name.

```
sqlmap -r sqlfile -D main –dbs --batch
```

**–dump-all**: Dump all**-D**: Database name

–**-batch**: Never ask for user input, use the default behaviour

**-r**: Request

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitfYAhZTLwUpzNVprfZca0NXVzVy7VEdTkDOBoC0k9_WdsqUeC4Fs5f2leGqWyWPDtgpFFPa83vWRMui48PjXR5fGfR3Z78J_f5oiCnDfWQ5oEugv1nYmP5dnivOLtric6Y5eN_CoYyHTVMD6GYtpxrGJ2-W4oXV8iNEnK8Q-W3lu_egNGwzkvBzWJ5A/s16000/7.png?w=640&ssl=1)

After dumping all the contents from the **main** database, we found the username, email and password hash. Here we are going to keep a note of dumped information.

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgkIHln11-frTWCTX5llD_PZ4_XZbRQMwP1SDr4kzvocpJxhtVQq-tdZYLDt157CXB67-pOcHbuLaASu9sftLPNleAasU_XV88cD1JE3ZLKsYz8pPo2wYO4NT4zkep3onx4qIS0TfpoqMTWHk3bC05__yUjQ6gt5F89DAaDX59ePP2foBVTZVNr-8SuQw/s16000/8.png?w=640&ssl=1)

It looks like an md5 hash but what can we do with this hash? Until we have a plain text password, we cannot proceed further. So, we simply copy the full hash and pasted google gave us a plain texted password of md5hash. What else we could do if we did not get a plain texted password from google? Then we can use crackstation website to crack hash or hashcat and john tools to crack the hash offline.

**Password**: superadministrator

![](https://i0.wp.com/blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHYpZ74OcMU96yYl2MqGFrZ5hJ0ebCe4j-bJ8LcqiGAvsj_OOnNuCUd61-Lnj5ElKYvARKL6BG9FRYyELOGdIEl2xN5S-fT-wf-5cDiYFKxeuydBNjFEwY5bykO6n1bVas5fxBFIaOLmyyvp3I9nBU6L2kYydPQaYzwL5DHYlU0WINn9Q_774_MNmdaQ/s16000/9.png?w=640&ssl=1)

#### **Admin Console Enumeration**

As we have admin user password in the plain texted form, we can try log in as admin user in the web console for further assessment.

![](https:...