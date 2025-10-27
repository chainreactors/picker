---
title: Recon like a Pro!
url: https://infosecwriteups.com/recon-like-a-pro-594845934fd0?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-07-05
fetch_date: 2025-10-04T11:53:48.572189
---

# Recon like a Pro!

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F594845934fd0&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frecon-like-a-pro-594845934fd0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Frecon-like-a-pro-594845934fd0&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40sup26)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-594845934fd0---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-594845934fd0---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Recon like a Pro!

[![Suprajabaskaran](https://miro.medium.com/v2/resize:fill:64:64/1*qv5PO65J3cFJJHpIoEa8EA.png)](https://medium.com/%40suprajabaskaran8?source=post_page---byline--594845934fd0---------------------------------------)

[Suprajabaskaran](https://medium.com/%40suprajabaskaran8?source=post_page---byline--594845934fd0---------------------------------------)

5 min read

·

Jun 25, 2023

--

1

Listen

Share

Hey there, fellow bug hunters and curious minds! Are you ready to dive into the fascinating world of reconnaissance?

In this blog post, we’re going to embark on an exciting journey into the realm of reconnaissance. Whether you’re an aspiring ethical hacker, a bug bounty hunter, or simply someone eager to learn about the art of gathering information, this article will equip you with the essential tools and techniques to become a true recon ninja.

Press enter or click to view image in full size

![]()

Source: <https://www.udemy.com/>

**Definition:**

> Imagine you’re planning an adventure or a mission to a new place. Before you embark on your journey, wouldn’t it be helpful to gather as much information as possible about the destination?

That’s where **reconnaissance** comes into play. In the world of offensive security, reconnaissance is like conducting thorough research and scouting before launching an attack or defending against one.

Reconnaissance involves gathering information about a target, such as a website, network, or organization. It’s like playing the role of a detective, seeking clues and understanding the terrain before making a move. Its techniques can include searching for publicly available data, analyzing website structures, scanning for open ports, or even observing social media accounts.

By performing reconnaissance, experts can gain insights into potential vulnerabilities, weaknesses, or valuable information that may help them protect systems or identify potential threats. It’s an essential step in the pentesting process, providing a foundation for planning and making informed decisions.

**Objective:**

1. ***Information Gathering:***

* Collecting crucial data
* Identifying target details
* Understanding the landscape

2. ***Vulnerability Assessment:***

* Analyzing weaknesses
* Discovering entry points
* Assessing security gaps

3. ***Target Profiling:***

* Creating a profile
* Understanding behavior
* Mapping interconnectedness

4. ***Strategic Planning:***

* Formulating attack strategies
* Developing countermeasures
* Making informed decisions

Here, I will provide a list of Recon tools to start with:

1. ***Domain Name Information Lookup:***

* [**whois**](https://www.whois.com/) or [**https://whois.arin.net**](https://whois.arin.net/) — Gives target IP range.
* [**viewdns info**](https://viewdns.info/reversewhois/) — obtain detailed information about a target domain, including DNS records, WHOIS data, IP geolocation.
* [**nslookup**](https://linux.die.net/man/1/nslookup) — gather information about a target domain, such as IP addresses, DNS records, and other details that aid in understanding the target’s infrastructure.
* [**YouGetSignal**](/www.yougetsignal.com)— Get other sites on the same domain.
* [**DNS dumpster**](https://dnsdumpster.com/) — web-based service for users to search and analyze historical DNS records, providing insights into subdomains, DNS changes, and potential security issues.
* [**Search DNS**](https://searchdns.netcraft.com/)— online tool for users to search and retrieve DNS information, such as DNS records, IP addresses, and domain registration details, for a specific domain or hostname.

2. ***Service enumeration:***

* [nmap](https://nmap.org/) — discover hosts, open ports, and gather information about systems, providing insights into network security.

3. S***ub-domain enumeration (and sub-domain of sub-domains):***

* **gobuster** — <https://github.com/OJ/gobuster>
* **sublist3r —** <https://github.com/aboul3la/Sublist3r>
* **Amass —** <https://github.com/owasp-amass/amass/>
* **dnsrecon —** <https://github.com/darkoperator/dnsrecon>
* **Knockpy —** <https://github.com/guelfoweb/knock>
* **SubBrute —** <https://github.com/TheRook/subbrute>
* **altdns —** <https://github.com/infosec-au/altdns>
* **EyeWitness —** <https://github.com/ChrisTruncer/EyeWitness>

4. ***Check certificates:***

* [**crt.sh**](http://crt.sh/) **—** information about SSL/TLS certificates associated with a target domain.
* [**testssl.sh**](https://github.com/drwetter/testssl.sh) —checks a server’s service on any port for the support of TLS/SSL ciphers.
* [**SSLyze**](https://github.com/nabla-c0d3/sslyze) — analyze the SSL/TLS configuration of a server by connecting to it to ensure that it uses strong encryption settings.

5. ***Check malicious IP reputation:***

* [**AbuseIPDB**](https://www.abuseipdb.com/) — an online platform that allows users to report and check IP addresses for malicious activity.
* [**Cisco Talos Intelligence**](https://www.talosintelligence.com/) — Lookup reputation for IP, domain, or network owner for real-time threat data.
* [**VirusTotal**](https://www.virustotal.com) — online service that analyzes files and URLs, checking them against multiple antivirus engines and other scanning tools, providing insights on potential malware infections.

6. ***OSINT (Open Source Intelligence):***

* [**Wayback Machine**](https://archive.org/web/) — An internet archive that allows you to view historical versions of websites, helping you uncover past information, changes, and potentially sensitive data. This can be automated by using these GitHub gists — [waybackurls.py](https://gist.github.com/mhmdiaa/adf6bff70142e5091792841d4b372050) and [waybackrobots.py](https://gist.github.com/mhmdiaa/2742c5e147d49a804b408bfed3d32d07).
* [**Google Dorks**](https://www.freecodecamp.org/news/google-dorking-for-pentesters-a-practical-tutorial/) **—** Customized search queries that leverage advanced search operators to uncover hidden or...