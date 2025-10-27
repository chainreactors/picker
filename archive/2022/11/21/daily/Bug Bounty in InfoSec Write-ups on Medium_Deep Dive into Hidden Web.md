---
title: Deep Dive into Hidden Web
url: https://infosecwriteups.com/deep-dive-into-hidden-web-a5110a9c65e7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-21
fetch_date: 2025-10-03T23:19:09.573758
---

# Deep Dive into Hidden Web

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fa5110a9c65e7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdeep-dive-into-hidden-web-a5110a9c65e7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fdeep-dive-into-hidden-web-a5110a9c65e7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-a5110a9c65e7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-a5110a9c65e7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Deep Dive into Hidden Web

## How to perform Pentest Recon using Gobuster.

[![Anmol Shah](https://miro.medium.com/v2/resize:fill:64:64/1*ZBMgiM1mNEzteerTV9rPng.jpeg)](https://medium.com/%40anmol.sh?source=post_page---byline--a5110a9c65e7---------------------------------------)

[Anmol Shah](https://medium.com/%40anmol.sh?source=post_page---byline--a5110a9c65e7---------------------------------------)

3 min read

·

Nov 20, 2022

--

Listen

Share

The first step to start attacking a web application is to perform recon on your target. Recon stands for reconnaissance of the target web application. Recon refers to the process in which hackers and penetration testers dig deep into an application to gather information and discover the additional content that is not normally exposed to the user.

An inportant step is to discover hidden content like obsecure subdomains, secret directories, and virtual hosts. Today, let’s talk about a recon tool that help us accomplish these goals: GoBuster.

GoBuster is a tool for brute-forcing to discover subdomains, hidden directories and files (URIs), and virtual hostnames on the target web applications.

## **Installing GoBuster**

Let’s start by installing GoBuster! You can find GoBuster’s project [*here*](https://github.com/OJ/gobuster)*.*

You most likely will not need to build the project from source. On most Linux distributions, you can istall GoBuster via the apt-get command.

`apt-get install gobuster`

Otherwise, if you have a Go language enviroment ready, then you can use:

`go install -v github.com/OJ/gobuster dns`

## Using GoBuster

Now that you have program installed, let’s jump right into performing recon using GoBuster! GoBuster has three available modes: “dns” , “dir”, and “vhost”. They are used to brute-force subdomains, hidden directories and files, and virtual hosts respectively.

### DNS Mode

The DNS mode is used for DNS subdomain brute-forcing. You can use it to find subdomains for a given domain. In this mode, you can use the flag “-d” to specify the domain you want to brute-force and “-w” to specify the wordlist you want to use.

`gobuster dns -d <target domain> -w <wordlist>`

You can use your own custom wordlists for this, but a good option is to use a wordlist published online. For example, the Seclist Github Repository has a pretty extensive wordlist for subdomain brute-forcing: [danielmiessler/SecLists](https://github.com/danielmiessler/SecLists/blob/master/Discovery/DNS/namelist.txt).

### Dir mode

The Dir mode is used to find addition content on a specific domain or subdomain. This includes hidden directories and files.

In this mode, you can use the flag “-u” to specify the target domain you want to brute-force and “-w” to specify the wordlist you want to use.

`gobuster dir -u <target.com> -w <wordlist>`

You can find a list of web content wordlist to use here: [SecList](https://github.com/danielmiessler/SecLists/tree/master/Discovery/Web-Content).

### Vhost mode

Lastly, you can use the Vhost mode to find virtual host of a target server.

Virtual Hosting is when a organization host multiple domain names on a single server or cluster of server. This allows one server to share its resouces with multiple hostnames. Finding virtual hostname on a server can reveal additional web content belonging to an organization.

`gobuter vhost -y <target url> -w <wordlist>`

For brute-forcing virtual hosts, you can use the same wordlist as brute-forcing subdomain va the DNS mode.

### Advance Options

For exaple, in dir mode, you can brute-force files with specific file extension using the “ -x ” flag.

`gobuster dir -u <target-url> -w <wordlist> -x .php`

For dir and vhost modes, you can use -k to skip SSL certificate verification and supress SSL errors.

`gobuster dir -u <target-url> -w <wordlist> -k`

And for both dir and vhost modes, you can even use the “ -c “ flag to spacify the cookies that should accoumpany you requests.

`gobuster dir -u <target-url> -w <wordlist> -c 'sssion=123456'`

END!!

**Happy Hacking**

Good Recon skills are one of the keys to being to successful as a hacker or a penetration tester. And GoBuster is a simple and powerfull tool to add to your recon toolkit!

Until then;

WAKE | EAT | HACK | REPEAT🔥

![]()

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Hacking](https://medium.com/tag/hacking?source=post_page-----a5110a9c65e7---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----a5110a9c65e7---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----a5110a9c65e7---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a5110a9c65e7---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--a5110a9c65e7---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--a5110a9c65e7---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--a5110a9c65e7---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--a5110a9c65e7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub ...