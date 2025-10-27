---
title: Fastly Subdomain Takeover $2000
url: https://infosecwriteups.com/fastly-subdomain-takeover-2000-217bb180730f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-23
fetch_date: 2025-10-03T23:29:28.124723
---

# Fastly Subdomain Takeover $2000

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F217bb180730f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffastly-subdomain-takeover-2000-217bb180730f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Ffastly-subdomain-takeover-2000-217bb180730f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-217bb180730f---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-217bb180730f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Fastly Subdomain Takeover $2000

## Bug Bounty — From zero to HERO

[![ValluvarSploit](https://miro.medium.com/v2/resize:fill:64:64/1*-5JvzvZVZgQx7K2XSgzu_w.jpeg)](https://medium.com/%40valluvarsploit?source=post_page---byline--217bb180730f---------------------------------------)

[ValluvarSploit](https://medium.com/%40valluvarsploit?source=post_page---byline--217bb180730f---------------------------------------)

5 min read

·

Nov 21, 2022

--

11

Listen

Share

### WHOAMI

My name is Alexandar Thangavel AKA ValluvarSploit, a full-time bug hunter and trainer. I love recon. I am the founder and CEO of ValluvarSploit Security. At ValluvarSploit Security, we are providing Bug Bounty training in one-to-one online session. For more information, please check our LinkedIn page.

### OBJECTIVE

Today, I am going to share how I found Fastly subdomain takeover vulnerability and earn my first four digits bounty. Let’s get started.

### **BACKSTORY**

This was started on October 2nd, 2022 Sunday. The day started as usual. I woke up at 6 AM, finished routine work, checked my Mobile data balance (1.3 GB was remaining), enabled my Mobile Hotspot, connected my Laptop, and resumed hunting on a private program. I spent a few hours on the target application but found nothing so took a short break. I used to revisit my old private programs at least once in six months. So, I reviewed my private invites, picked an old program and started performing subdomain enumeration (Let’s call our target as redacted.com).

### **SUBDOMAIN TAKEOVER**

Subdomain takeover occurs when an attacker take control over a subdomain of a domain. It happens because of DNS misconfiguration / mistakes.

### SUBDOMAIN ENUMERATION

I started subdomain enumeration with Google Dorking, [OWASP Amass](https://github.com/OWASP/Amass) and [Gobuster](https://github.com/OJ/gobuster) tools.

```
# Passive Subdomain Enumeration using Google Dorking
site:*.redacted.com -www -www1 -blog
site:*.*.redacted.com -product

# Passive Subdomain Enumeration using OWASP Amass
amass enum -passive -d redacted.com -config config.ini -o amass_passive_subs.txt

# Subdomain Brute force using Gobuster
gobuster dns -d redacted.com -w wordlist.txt - show-cname - no-color -o gobuster_subs.txt
```

After enumerating subdomains, removed duplicate entries and merged them into a single file (subdomains.txt) using the [Anew](https://github.com/tomnomnom/anew) tool.

```
# Merging subdomains into one file
cat google_subs.txt amass_passive_subs.txt gobuster_subs.txt | anew subdomains.txt
```

Then passed the subdomains.txt file to my cname.sh shell script, enumerated CNAME records and stored in cnames.txt.

```
# Enumerate CNAME records
./cname.sh -l subdomains.txt -o cnames.txt

# We can use HTTPX tool as well
httpx -l subdomains.txt -cname cnames.txt
```

Then passed the subdomains.txt file to the [HTTPX](https://github.com/projectdiscovery/httpx) tool. probed live websites and stored in servers\_details.txt.

```
# Probe for live HTTP/HTTPS servers
httpx -l subdomains.txt -p 80,443,8080,3000 -status-code -title -o servers_details.txt
```

### ANALYSIS

I started analyzing the cnames.txt file and found one subdomain that was pointing to two different CNAME records. I ran dig command on the subdomain and got followings,

```
dig next.redacted.com CNAME
```

Press enter or click to view image in full size

![]()

DNS query for CNAME record

This subdomain had two CNAME records. The first CNAME record was pointing to webflow.io domain and the second CNAME record was pointing to fastly.net (Fastly Service) domain. Whenever we have multiple CNAME records, the first CNAME record will redirect us to next CNAME record and so on. The redirection would continue until we reach last CNAME record.

I started analyzing the servers\_details.txt file for interesting stuff and found this line. Notice status code and website title.

```
https://next.redacted.com [500] [246] [Fastly error: unknown domain next.redacted.com]
```

The status code was “500" and the title was “Fastly error: unknown domain next.redacted.com”. By taking a look at CNAME record (“redacted.fastly.net”) and website fingerprint “Fastly error: unknown domain”, we can confirm that this is Fastly Subdomain Takeover. If a website has this fingerprint then it may be vulnerable. However, I came across this Fastly fingerprint many times before and it was not vulnerable. It’s vulnerable only when certain conditions are met, so it’s an edge case.

In most cases, we cannot takeover the Fastly service. For example below case,

Press enter or click to view image in full size

![]()

But if the domain is not already taken by another customer then we can claim the domain and takeover the subdomain completely.

### CONFIRMING THE VULNERABILITY

I went to Fastly official website and performed below steps,
1. I created an account on [fastly.com](https://www.fastly.com/) using a temporary mail.
2. Logged in to my Fastly Dashboard and clicked on the “Create a Delivery Service” button.
3. Entered target subdomain name(next.redacted.com) and clicked on Add button.

I was expecting the error message (“domain is already taken by another customer”) to appear but there was no error message. I was redirected to the next page “Hosts page”. I was surprised.

Press enter or click to view image in full size

![]()

Claimed domain on Fastly

### POC CREATION STEPS

Once the vulnerability was confirmed, I logged into my VPS server and created a directory called “hosting”. Then within the “hosting” directory created a simple HTML file called “index.html”.

```
mkdir hosting

cd hosting

nano index.html
```

“index.html” file contains below code,

```
<!DOCTYPE html>

<html>
    <head><title>STO PoC</title></head>
    <body>
        <h1>ValluvarSploit PoC</h1>
    </body>
</html>
```

After that, I started a simple Python web server on port 80 within the current working directory,

```
python3 -m http.server 80
```

Then I went to the Fastly dashboar...