---
title: How i Find Database Credentials via Mass Recon & Recon Scoping on Gcash
url: https://infosecwriteups.com/how-i-find-database-credentials-via-mass-recon-recon-scoping-on-gcash-f43a0dae3ec1?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-10-28
fetch_date: 2025-10-06T18:48:10.994426
---

# How i Find Database Credentials via Mass Recon & Recon Scoping on Gcash

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff43a0dae3ec1&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-find-database-credentials-via-mass-recon-recon-scoping-on-gcash-f43a0dae3ec1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-find-database-credentials-via-mass-recon-recon-scoping-on-gcash-f43a0dae3ec1&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f43a0dae3ec1---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f43a0dae3ec1---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How i Find Database Credentials via Mass Recon & Recon Scoping on Gcash

[![Ph.Hitachi](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*WZn-64UUVRL95-ov)](https://ph-hitachi.medium.com/?source=post_page---byline--f43a0dae3ec1---------------------------------------)

[Ph.Hitachi](https://ph-hitachi.medium.com/?source=post_page---byline--f43a0dae3ec1---------------------------------------)

6 min read

·

Apr 22, 2024

--

10

Listen

Share

Hi guys,

so iwill share this second finding on gcash VDP Channel & share tips on some recon methodologies such as **subdomain enumation**, **wappalyzer mapping, mass recon** & **scoping** with **automated tools**.

### **What is recon scoping?**

Reconnaissance (or recon) scoping is the initial phase of a vulnerability assessment or penetration testing engagement. It involves identifying and gathering information about the target systems, networks, and infrastructure. The primary goal is to understand the scope of the environment to be tested and to gather intelligence that might be useful during subsequent phases of the assessment.

### Start:

before we start my recon methodologies mostlikely separated per categories, so i created multiple directory on my local machine by running this:

```
mkdir -p gcash.com ~/recon/targets/gcash.com/subdomains/
mkdir -p gcash.com ~/recon/targets/gcash.com/endpoints/
mkdir -p gcash.com ~/recon/targets/gcash.com/aws/
mkdir -p gcash.com ~/recon/targets/gcash.com/dns/
```

### Recon workflow:

- subdomain enumeration
- information gathering (network, dns, tech, ports)
- automated testing

### Subdomain mapping/enumeration:

Subdomain gathering is very crucial interms of bug bounty/pentesting, you need to gather a subdomains as you can, so will show you how to find a subdomains with different methods with correct tools.

**Note**: some method will not work all the time you use it on any target, but i will show the methods here that i commonly use to gather subdomains.

**Tools:**
**s**[**ubfinder**](https://github.com/projectdiscovery/subfinder): passive and active methods
[**assetfinder**](https://github.com/tomnomnom/assetfinder): certificate transparency logs
[**alterx**](https://github.com/projectdiscovery/alterx): dynamic & permutation/alterations
[**asnmap**](https://github.com/projectdiscovery/asnmap): to map ASN and find subdomains
[**ffuf**](https://github.com/ffuf/ffuf): to find subdomains on vhosts

```
# passive & active subdomain enumation using subfinder
subfinder -d gcash.com -o ~/recon/targets/gcash.com/subdomains/subfinder.txt
```

```
# subdomain enumeration via certificate transparency logs with assetfinder
assetfinder --subs-only gcash.com >> ~/recon/targets/gcash.com/subdomains/assetfinder.txt
```

```
# dynamic subdomain enumeration with alterx
echo gcash.com | alterx -enrich | dnsx > ~/recon/targets/gcash.com/subdomains/alterx-dynamic.txt

# for high chance to find subdomain
# you can generate patterns based on existing subdomains
subfinder -d tesla.com | alterx | dnsx
```

```
# subdomain enumaration via Permutation/Alterations with alterx
echo gcash.com | alterx -pp 'word=subdomains-top1million-50000.txt' | dnsx > ~/recon/targets/gcash.com/subdomains/alterx-permutation.txt
```

```
# subdomain enumeration via ASMapping
asnmap -d gcash.com | dnsx -silent -resp-only -ptr > ~/recon/targets/gcash.com/subdomains/dnsx.txt
```

```
# subdomain enumeration via vhost
cat subdomains-top1million-50000.txt | ffuf -w -:FUZZ -u http://gcash.com/ -H 'Host: FUZZ.gcash.com' -ac
```

after we enumerate subdomains using different tools their are some duplicates subdomains, to optimize the subdomains we will merge it using [anew](https://github.com/tomnomnom/anew) and will it actively remove duplicate subdomains.

```
# Merging subdomains from ~/recon/targets/gcash.com/subdomains/* into one file and remove duplicates
cat ~/recon/targets/gcash.com/subdomains/*.txt | anew ~/recon/targets/gcash.com/subdomains/subdomains.txt
```

after we merge subdomains we need to filter live subdomains using [httpx](https://github.com/projectdiscovery/httpx) to filter https/http on lists of subdomain.

```
# Probe for live HTTP/HTTPS servers
cat ~/recon/targets/gcash.com/subdomains/subdomains.txt | httpx -o ~/recon/targets/gcash.com/subdomains/httpx.txt
```

### Information Gathering:

after we filter live subdomains we will start a information gathering using [httpx](https://github.com/projectdiscovery/httpx) to gather infomation about the domains using **wappalyzer mapping** *techniques* to identify technologies that are used to websites.

Press enter or click to view image in full size

![]()

### Automated testing:

after we gather information about tech we will start using [nuclei](https://github.com/projectdiscovery/nuclei).

> Nuclei is used to send requests across targets based on a template, leading to zero false positives and providing fast scanning on a large number of hosts. Nuclei offers scanning for a variety of protocols, including TCP, DNS, HTTP, SSL, File, Whois, Websocket, Headless, Code etc. With powerful and flexible templating, Nuclei can be used to model all kinds of security checks.

using nuclei i scan all subdomains using this code:

```
cat ~/recon/targets/gcash.com/subdomains/httpx.txt | nuclei -config ~/nuclei-templates/config/custom.yml
```

in nuclei i build my own custom configurations for scoping, its include finding senstive informations (e.g, secret keys, tokens, credentials) on configurations and compiled assets like javascript or tcp (e.g, docker misconfig) and some type of fuzzing overall, this configurations focused on finding sensitive data, you can also make custom config for **wappalyzer** using nuclei to detect technologies.

```
# nuclei -config ~/nuclei-templates/config/custom.yml -list target_list_to_scan.txt

severity:
  - critical
  - high
  - medium
  - low

type:
  - http
  - tcp
  - javascript

incl...