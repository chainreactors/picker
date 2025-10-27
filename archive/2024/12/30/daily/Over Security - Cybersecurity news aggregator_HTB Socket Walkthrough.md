---
title: HTB Socket Walkthrough
url: https://www.secjuice.com/htb-socket-walkthrough/
source: Over Security - Cybersecurity news aggregator
date: 2024-12-30
fetch_date: 2025-10-06T19:36:58.853471
---

# HTB Socket Walkthrough

[![Secjuice](https://www.secjuice.com/content/images/2018/12/Logo-1.png)](https://www.secjuice.com)

* [Donate](https://opencollective.com/secjuice)
* [About Us](https://secjuice.com/about-us/)
* [Technical](https://secjuice.com/tag/technical/)
* [OSINT](https://secjuice.com/tag/OSINT/)
* [Unusual Journeys](https://secjuice.com/tag/unusual-journeys-into-infosec/)
* [HoF](https://secjuice.com/secjuice-hall-of-fame/)
* [Write With Us](https://secjuice.com/join-secjuice-writing-team/)
* [Hire A Writer](https://secjuice.com/hire-infosec-cybersecurity-writer/)
* [Rankings](https://secjuice.com/secjuice-writers-ranking/)

[Sign in](#/portal/signin)
[Subscribe](#/portal/signup)

[TECHNICAL](/tag/technical/)

# HTB Socket Walkthrough

Learn how a vulnerability in a WebSocket application was discovered and exploited using SQL injection.

* [![Andy74](/content/images/size/w100/2020/01/avatar.png)](/author/andy74/)

#### [Andy74](/author/andy74/)

Dec 29, 2024
• 26 min read

![HTB Socket Walkthrough](/content/images/size/w2000/2024/12/fireworks--new-years-countdown-2025--and-python-code.png)

This picture of code and a 2025 New Year's celebration with fireworks was generated using Microsoft Copilot.

And welcome back, my friends, to this relatively simple but very interesting BOX, with a small reverse engineering section that I love so much and that I hope you will, too. Also interesting is the part about **privesc**, in which ChatGPT, as has recently happened, had a small contribution. But let's not get lost in chatter, and let's get started.

The **nmap** scan:

```
Starting Nmap 7.93 ( https://nmap.org ) at 2023-05-20 15:18 EDT
Nmap scan report for 10.10.11.206
Host is up (0.11s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.9p1 Ubuntu 3ubuntu0.1 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey:
|   256 4fe3a667a227f9118dc30ed773a02c28 (ECDSA)
|_  256 816e78766b8aea7d1babd436b7f8ecc4 (ED25519)
80/tcp open  http    Apache httpd 2.4.52
|_http-title: Did not follow redirect to http://qreader.htb/
|_http-server-header: Apache/2.4.52 (Ubuntu)
Service Info: Host: qreader.htb; OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 29.39 seconds
```

OK. The usual portal seems to have an unusual domain for an HTB BOX. Let's add it in the **/etc/hosts** file and try to navigate it.

![](https://www.secjuice.com/content/images/2023/06/img-00.png)

**Wappalyzer** identifies the technologies used in the portal, but at the moment, this information cannot help me that much.

![](https://www.secjuice.com/content/images/2023/06/img-01.png)

The portal displays **QRCode** conversion and processing functions. There are also two versions of the system in a software format for *windows* and *linux* that can be downloaded and use4d from a local computer. It looks like my first investigation will be one of my favorite activities, a good **reverse engineering** session. But first, let's start the program to understand at least the basic operation.

![](https://www.secjuice.com/content/images/2023/06/img-02.png)

The program is a user interface system. If we try the sample file supplied with the executable, it is possible to trace the text contained within the **QRCode**.

```
kavigihan
```

Let's immediately *disassemble* the application to understand if there is something hidden inside that can be useful. The program initialization block (you can reach it by clicking on the start function in the appropriate box) shows that the application main is started.

![](https://www.secjuice.com/content/images/2023/06/img-03.png)

So let's move to main (always selecting the function from the appropriate box) and following the "*jmp*" to the specific address. We find ourselves in the heart of the application.

![](https://www.secjuice.com/content/images/2023/06/img-04.png)

Looking at the flow itself, I understand that it could take me a long time just to understand what it does by reading the code (branches are enough), so I start debugging and follow a single flow, at least I'm sure I will quickly analyze the correct flow.

![](https://www.secjuice.com/content/images/2023/06/img-05.png)

Going with the flow, I soon get to a function call that immediately displays the dialog. Strangely, the variable preceding it points to the executable I'm already debugging.

![](https://www.secjuice.com/content/images/2023/06/img-06.png)

I restarted and proceeded with a new debug, this time by entering the function that started the app form. Apparently, an application forks.

![](https://www.secjuice.com/content/images/2023/06/img-07.png)

We should have two processes of the same app.

```
┌──(in7rud3r㉿in7rud3r-kali)-[~/Dropbox/hackthebox]
└─$ps -aux | grep qreader
in7rud3r 36498 5.7 0.0 2740 988 ? t 19:38 0:01 /home/in7rud3r/Downloads/app/qreader
in7rud3r 36548 2.3 0.9 962756 162472 ? Wl 19:38 0:00 /home/in7rud3r/Downloads/app/qreader
in7rud3r 36624 0.0 0.0 6304 2072 pts/5 S+ 19:38 0:00 grep --color=auto qreader
```

A block of code later, however, waits for the second thread to exit.

![](https://www.secjuice.com/content/images/2023/06/img-08.png)

Since I can't do much in this instance, it will be better to start the app without debugging and stick to the process being started.

Once started, we check who is the father of whom. The ID of the process should suffice (the older one is the child), but we leave nothing to chance.

```
┌──(in7rud3r㉿in7rud3r-kali)-[~/Dropbox/hackthebox]
└─$ pstree -p | grep qreader
           |              |-lightdm(921)-+-xfce4-session(955)-+-Thunar(1084)-+-qreader(38483)---qreader(38492)-+-{qreader}(38494)
           |              |              |                    |              |                                 |-{qreader}(38495)
           |              |              |                    |              |                                 |-{qreader}(38496)
           |              |              |                    |              |                                 |-{qreader}(38497)
           |              |              |                    |              |                                 |-{qreader}(38498)
           |              |              |                    |              |                                 `-{qreader}(38499)

┌──(in7rud3r㉿in7rud3r-kali)-[~/Dropbox/hackthebox]
└─$ ps -aux | grep qreader
in7rud3r   38483  2.4  0.0   2740   980 ?        S    19:45   0:01 /home/in7rud3r/Downloads/app/qreader
in7rud3r   38492  0.5  0.9 962792 162492 ?       Sl   19:45   0:00 /home/in7rud3r/Downloads/app/qreader
in7rud3r   38812  0.0  0.0   6304  2096 pts/5    R+   19:46   0:00 grep --color=auto qreader
```

OK. The opening and writing functions should use some imported standard IO functions, but I can't find anything in the import section. I should find the button handles to retrieve the image encoding and decoding functions. Then there are the two function versions that update in the "about" menu, which return a *connection error* message. Let's try to find the error strings to trace the calls it tries to make.

![](https://www.secjuice.com/content/images/2023/06/img-09.png)

The strings are there, but I can't debug them, and after a few attempts to add a **breakpoint** that doesn't activate. I decided on a more theoretical approach. The error message is clearly an indication of a bad network connection, so I'm aiming to check portions of code in which *network* features are exploited. After a few tries, I identified the "**socket**" function. For a change, I use a slightly less user-friendly tool, **gdb**.

I started the application and identifed the process that is being duplicated.

```
┌──(in7rud3r㉿in7rud3r-kali)-[~/Downloads/app]
└─$ pstree -ap | grep qreader
  |   |   `-qreader,10054
  |   |       `-qreader,10059
  |   |           |-{qreader},10060
  |   |   ...