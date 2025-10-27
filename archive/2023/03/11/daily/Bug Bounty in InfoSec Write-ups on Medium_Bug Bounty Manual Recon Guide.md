---
title: Bug Bounty Manual Recon Guide
url: https://infosecwriteups.com/bug-bounty-manual-recon-guide-57e1e5a06dd7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-11
fetch_date: 2025-10-04T09:13:35.146140
---

# Bug Bounty Manual Recon Guide

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F57e1e5a06dd7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-manual-recon-guide-57e1e5a06dd7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbug-bounty-manual-recon-guide-57e1e5a06dd7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-57e1e5a06dd7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-57e1e5a06dd7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Bug Bounty Recon Guide

[![Thee Eclipse](https://miro.medium.com/v2/resize:fill:64:64/1*QPGkCrXe0vC8iTg4lnR4Cg.png)](https://medium.com/%40TheeEclipse?source=post_page---byline--57e1e5a06dd7---------------------------------------)

[Thee Eclipse](https://medium.com/%40TheeEclipse?source=post_page---byline--57e1e5a06dd7---------------------------------------)

6 min read

·

Feb 26, 2023

--

Listen

Share

![]()

Bug Bounty Recon

Ever felt like you need a specific guide / approach to your bug bounty targets so that you do not miss anything during the hunt? Well, there are several tools that can do the recon for you but how efficient are they when it comes to enumerating all possible recon details from a target. I share the approach I use on any target for bug bounty ensuring effective recon on critical bug surfaces on technology stacks.

We will use our target as: ***a.com*** for the guide.

**Step 1: Identify the root domain of the target / organization.**

Why is this important? Because all the digital infrastructure of the organization lies in the root domain and it is from the root / primary domain that you dig subdomains and sub-sub domains. The root domain is the one that mostly serves the main webpage for the target and all digital records will mostly point to it *i.e* From acquisitions, news, blogs, references and company digital history and this is important.

So we define a.com as the root domain for our target

**Step 2: Acquisitions and Company History**

Identify all the company growth details and history with basis on acquisitions and services change or termination of services over time. What do I mean? Check if the company acquired any other smaller companies like b.com,c.com e.t.c and as well check if the company had a change in services it offers over time and from what to what and this leaves a trail of the possible infrastructure and technologies ever used by the target. Now , acquisition helps identify other root domains and services under the same target company and this increases your hunt / attack surface. Acquisition data can be found on Crunchbase(https://www.crunchbase.com/), Wikipedia , Google and others. This contributes to IP ASN(Autonomous System Numbers) that are useful in mapping the companies infrastructure

**Step 3: Reverse Whois Checkup**

Find all the domain owners and key company signatories with details like names, emails, abuse reports (from domain rules by ICANN to local digital rules in company home country), mailing blacklists(Can be obtained from mxtoolbox(<https://mxtoolbox.com/>)) , managers, CEO , workers etc. Public mails can be auto scanned on terminal with The Harvester tool.

The reverse whois can be done using just google search or the <https://whoxy.xom> tool amongst others. Take note of all details gathered here

This helps identify the company structure and who is trusted with what and who are they and as well the company digital footprints over time.

**Step 4: Analytics and Technology**

Identify the main technology stack of the company where you find certain companies only use WordPress or Shopify or AWS e.t.c and take note of that and what are the recent technology updates not done. Do this on the root/primary domain without being much into subdomains or sub subdomains yet. Here you can use Wappalizer extension(https://www.wappalyzer.com/), Builtwith.com extension , Shodan and others for more verbose profiling and recon. This enables you to narrow down the attack surface to specific technologies and infrastructure endpoints.

**Step 5: Subdomain Enumeration**

Here you now crawl, brute-force and enumerate all subdomains of the target domain and the acquisitions or sub services under the company name . You can use: Gospider, Harkrawler , Subdomanizer , Amass , Sublist3r , DNS Dumpster ,Mass dns , Github search, subdomain bruteforcer ,Alt dns tool to make wordlists , commonspeak tool, shuffle dns, nikto, dirb , <https://subdomainfinder.c99.nl/> and any other efficient tool or web application and here make sure you dig even old subdomains not just existing ones and save this to a basic .txt file .You can have ChatGPT make you a custom tool if you wish or use @jahddiz/all.txt subdomain brute-force wordlist on Github(<https://gist.github.com/jhaddix>) . This is now your attack scope and at first might seem a huge list of targets but we are narrowing down to specifics or what is more interesting.

First from your target , a.com : Read the bug bounty rules for in-scope items and remove the rest from your subdomain and domains list and the list gets smaller.

**Step 6: ASN Enumeration.**

Here we gather all the Autonomous System Numbers(An Autonomous System is a set of routers, or IP ranges, under a single technical administration) for the target domain IP and save this data somewhere. A tool like amass lists for you the ASN after subdomain enumeration and it is more efficient than even most web applications for subdomain enumeration.

This gives you detailed grouping of the IT infrastructure for large organizations mostly and here you can use tools like: Amass , asn enum tool, Metabigor , <https://bgp.he.ne> etc

**Step 7: Port Scanning**

Now that you have subdomains and narrowed down to the In-scope subdomains. It is time to do the hunting for each. We start with port scanning for the selected subdomain target and enumerate all the open ports and services running on them. Nmap does a perfect job at this and is available by default to linux installations.

<https://nmap.org/>

Nmap also has a vulnerability scanner and uses basic in terminal commands like :

```
nmap –-script=vuln a.com(or its IP)
```

and lists all public possible exploits from its database .

From open ports and services now check all possible exploitations for the services e.g apache with their versions and what open ports should not be open. This can be by basic google search or OSINT .

More details: <https://www.hackerone.com/vulnerability-management/what-vulnerabi...