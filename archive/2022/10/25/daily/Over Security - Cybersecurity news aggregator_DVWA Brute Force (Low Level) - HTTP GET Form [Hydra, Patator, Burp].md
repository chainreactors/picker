---
title: DVWA Brute Force (Low Level) - HTTP GET Form [Hydra, Patator, Burp]
url: https://blog.g0tmi1k.com/dvwa/bruteforce-low/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:59.332004
---

# DVWA Brute Force (Low Level) - HTTP GET Form [Hydra, Patator, Burp]

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# DVWA Brute Force (Low Level) - HTTP GET Form [Hydra, Patator, Burp]

This post is a "how to" for the **"brute force" module** set to **"low" level security** inside of **[Damn Vulnerable Web Application (DVWA)](http://dvwa.co.uk/)**. There are separate posts for the [medium level (time delay)](https://blog.g0tmi1k.com/dvwa/bruteforce-medium/) and [high setting (CSRF tokens)](https://blog.g0tmi1k.com/dvwa/bruteforce-high/). There is a related post for the [login screen](https://blog.g0tmi1k.com/dvwa/login/) as it was also brute forced (HTTP POST form with CSRF tokens).

![Brute Force DVWA Low Level](/images/dvwa-bruteforce-low.png "Brute Force DVWA Low Level")

Once more, let's **forget the credentials** we used to login to DVWA with (`admin`:`password`).

Let's **not try the default login** for the web application.

Let's **play dumb and brute force** DVWA... *again*.

---

**TL;DR**: Quick copy/paste

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` CSRF=$(curl -s -c dvwa.cookie "192.168.1.44/DVWA/login.php" | awk -F 'value=' '/user_token/ {print $2}' | cut -d "'" -f2) SESSIONID=$(grep PHPSESSID dvwa.cookie | awk -F ' ' '{print $7}') curl -s -b dvwa.cookie -d "username=admin&password=password&user_token=${CSRF}&Login=Login" "192.168.1.44/DVWA/login.php"  hydra  -L /usr/share/seclists/Usernames/top_shortlist.txt  -P /usr/share/seclists/Passwords/rockyou-40.txt \   -e ns  -F  -u  -t 1  -w 10  -v  -V  192.168.1.44  http-get-form \   "/DVWA/vulnerabilities/brute/:username=^USER^&password=^PASS^&Login=Login:S=Welcome to the password protected area:H=Cookie\: security=low; PHPSESSID=${SESSIONID}"  patator  http_fuzz  method=GET  follow=0  accept_cookie=0  --threads=1  timeout=10 \   url="http://192.168.1.44/DVWA/vulnerabilities/brute/?username=FILE1&password=FILE0&Login=Login" \   1=/usr/share/seclists/Usernames/top_shortlist.txt  0=/usr/share/seclists/Passwords/rockyou-40.txt \   header="Cookie: security=low; PHPSESSID=${SESSIONID}" \   -x quit:fgrep='Welcome to the password protected area' ``` |

---

Table of Contents

* + [Objectives](#Objectives)
  + [Setup](#Setup)
  + [Tools](#Tools)
  + [What is brute force?](#What.is.brute.force.)
  + [Creating a Session Cookie](#Creating.a.Session.Cookie)
  + [Information Gathering](#Information.Gathering)
    - [Form HTML Code](#Form.HTML.Code)
    - [Generating a Baseline](#Generating.a.Baseline)
    - [Test lab vs Production target](#Test.lab.vs.Production.target)
    - [Blacklisting vs Whitelisting](#Blacklisting.vs.Whitelisting)
    - [Usernames & Wordlists](#Usernames..amp..Wordlists)
    - [Threads & Timeouts](#Threads..amp..Timeouts)
  + [**Hydra**](#L.strong.Hydra..strong.)
    - [Hydra Documentation](#Hydra.Documentation)
    - [Debugging Hydra with Burp Proxy](#Debugging.Hydra.with.Burp.Proxy)
    - [Burp's Invisible Proxy Mode](#Burp.s.Invisible.Proxy.Mode)
    - [**Hydra Attack Command**](#L.strong.Hydra.Attack.Command..strong.)
  + [**Patator**](#L.strong.Patator..strong.)
    - [Patator Documentation](#Patator.Documentation)
    - [Debugging Patator](#Debugging.Patator)
    - [**Patator Attack Command**](#L.strong.Patator.Attack.Command..strong.)
  + [**Burp Proxy**](#L.strong.Burp.Proxy..strong.)
  + [Failed Attempts](#Failed.Attempts)
    - [Medusa](#Medusa)
    - [Nmap](#Nmap)
    - [Ncrack](#Ncrack)
    - [Metasploit Framework](#Metasploit.Framework)
  + [Proof of Concept Scripts](#Proof.of.Concept.Scripts)
    - [Bash Template](#Bash.Template)
    - [Python Template](#Python.Template)
  + [Summary](#Summary)
    - [Hydra vs Patator Syntax](#Hydra.vs.Patator.Syntax)
    - [Benchmark](#Benchmark)
    - [Conclusion](#Conclusion)

## Objectives

* The goal is to **brute force an HTTP login** page.
  + **GET requests** are made via a **form**.
  + The web page is in a **sub folder**.
* **[Low](https://blog.g0tmi1k.com/dvwa/bruteforce-low/)**
  + **Straight forward HTTP GET** brute force attack via a **web form**.
  + Bonus: **SQL injection** (~~[See here for more information](#*comingsoon*)~~).
* [Medium](https://blog.g0tmi1k.com/dvwa/bruteforce-medium/)
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
  + Could also use wget (`wget -qO -`) instead.
  + Or using Burp/Iceweasel, however, it is harder to automate them due to them being graphical, which makes doing repetitive stuff boring.
* [THC-Hydra v8.1](https://www.thc.org/thc-hydra/) - A brute force tool.
* [Patator v0.5](https://github.com/lanjelot/patator) - An alternative brute force tool.
* [Burp Proxy v16.0.1](https://portswigger.net/burp/proxy.html) - Debugging requests & brute force tool
  + Using [FoxyProxy](https://getfoxyproxy.org/) to switch proxy profiles in Iceweasel.
* [SecLists](https://github.com/danielmiessler/SecLists) - General wordlists.
  + These are common, default and small wordlists.
  + Instead of using a custom built wordlist, which has been crafted for our target (e.g. generated with [CeWL](https://digi.ninja/projects/cewl.php)).
* Failed brute force tools:
  + [Medusa v2.1.1](http://foofus.net/goons/jmk/medusa/medusa.html) - segmentation faults when sending a custom header and HTTP 200 response.
  + [Metasploit v4.11.4-2015090201](https://www.metasploit.com/) - `auxiliary/scanner/http/http_login` does HTTP basic authentication, not web forms.
  + [Ncrack v0.4 ALPHA](https://nmap.org/ncrack/) - HTTP module only supports HTTP basic access authentication, not web forms.
  + [Nmap v6.49 BETA5](https://nmap.org/) - `http-form-brute` lacks required options to-do the attack (as it cannot send custom headers).

---

## What is brute force?

For the people who are unaware of "brute force attacks", here is an overview of the most common points:

* Brute forcing is a **trial and error method of repeatedly trying out a task**, sequentially changing a value each time, until a certain result is achieved.
  + So it forces its way in, and does not take "no" for an answer.
* The values used in the attack may be **predefined in a file** (often ca...