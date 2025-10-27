---
title: Subdomain Takeover: When Your Own Domain Becomes Your Enemy ️‍♂️
url: https://infosecwriteups.com/subdomain-takeover-when-your-own-domain-becomes-your-enemy-%EF%B8%8F-%EF%B8%8F-8c80e650aeea?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-27
fetch_date: 2025-10-06T23:17:28.850367
---

# Subdomain Takeover: When Your Own Domain Becomes Your Enemy ️‍♂️

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F8c80e650aeea&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsubdomain-takeover-when-your-own-domain-becomes-your-enemy-%25EF%25B8%258F-%25EF%25B8%258F-8c80e650aeea&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsubdomain-takeover-when-your-own-domain-becomes-your-enemy-%25EF%25B8%258F-%25EF%25B8%258F-8c80e650aeea&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8c80e650aeea---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8c80e650aeea---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Subdomain Takeover: When Your Own Domain Becomes Your Enemy 🕵️‍♂️

[![Het Patel](https://miro.medium.com/v2/resize:fill:64:64/1*0xmi1m3lKtIdhh3vz8hFsA.jpeg)](https://hettt.medium.com/?source=post_page---byline--8c80e650aeea---------------------------------------)

[Het Patel](https://hettt.medium.com/?source=post_page---byline--8c80e650aeea---------------------------------------)

6 min read

·

Jul 5, 2025

--

1

Listen

Share

Press enter or click to view image in full size

![]()

*A comprehensive guide to understanding, detecting, and preventing one of the web’s most overlooked vulnerabilities — Subdomain Takeover* 🚨

![]()

## When LinkedIn News Became our Goldmine 🚨

Picture this: It’s just another random day when I’m scrolling through LinkedIn and stumble upon a post about a company’s financial troubles — half of their online services were reportedly going offline due to unpaid dues. While most people felt sympathy for the employees, my “evil mind” (as I like to call it) immediately saw an opportunity.

*“If their services are shutting down, what happens to their subdomains?”*

![]()

That single thought led me and my friend — Kaif down a rabbit hole that perfectly demonstrates how business disruptions create cybersecurity vulnerabilities. Within minutes, we were running subdomain enumeration:

```
sudo subfinder -d target.com -o subfinder.txt && \
sudo httpx-toolkit -l subfinder.txt -o httpx.txt -cname -ip -title -sc && \
subjack -w subfinder.txt -t 100 -timeout 30 -ssl -c ~/Downloads/fingerprints.json -v
```

**The result?** We found `gcdn.target.com` flagged as potentially vulnerable to S3 bucket takeover.

![]()

A quick dig command revealed the smoking gun:

Press enter or click to view image in full size

![]()

Though we were not able to take over the subdomain this time, the presence of proper **TXT records** and correct configurations helped the domain owner secure it just in time.

![]()

We felt a little disappointed — but in a good way! After all, the ultimate goal is always **security first**, not exploitation.

## What Exactly is a Subdomain Takeover? 🔍

A subdomain takeover occurs when an attacker gains control of a subdomain by claiming an external service that the subdomain was pointing to, but which has been abandoned or misconfigured.

A **subdomain takeover** occurs when a subdomain (like `support.example.com`) points to an external service (e.g., GitHub Pages, AWS S3, Heroku) that has been deleted or is unclaimed.

Because the DNS record still exists but the service behind it does not, an attacker can claim the service and take control of the subdomain.

![]()

> In simpler words: your company “forgot” to turn off a signpost pointing to an empty lot — and a hacker decided to build a trap there.

## How Subdomain Takeovers Actually Take Place: A Step-by-Step Breakdown 🔧

Understanding the mechanics behind subdomain takeovers is crucial for both attackers and defenders. Let’s walk through the exact process of how these vulnerabilities unfold in the real world.

## The Setup Phase: Creating the Vulnerability 🏗️

**Step 1 — Legitimate Service Setup:** A company sets up a subdomain pointing to an external service:

```
# Company creates DNS record
blog.company.com -> CNAME -> company.github.io
```

**Step 2 — Service Configuration:** The company configures their GitHub Pages, AWS S3 bucket, or other service:

```
# GitHub Pages setup
Repository: company/company.github.io
Custom domain: blog.company.com
```

**Step 3: The Critical Mistake** Time passes, and the company either:

* Deletes the GitHub repository
* Cancels the AWS S3 bucket
* Removes the Heroku app
* Stops paying for the service

**But here’s the problem**: They forget to remove the DNS record!

## The Attack Phase: Exploiting the Dangling DNS 🎯

**Step 1: Discovery**

An attacker discovers the vulnerable subdomain through various tools described below in the blog. (Sub-finder, crt.sh, AssetFinder, etc)

**Step 2: Verification**

The attacker verifies the service is unclaimed:

```
# Check if GitHub Pages exists
curl -I https://company.github.io
# Returns: 404 Not Found

# Check DNS still points to service
dig CNAME blog.company.com
nslookup blog.company.com
# Still returns company.github.io
```

**Step 3: Service Claiming** Now comes the actual takeover:

**For GitHub Pages:**

```
# Attacker creates repository
git clone https://github.com/attacker/company.github.io
echo "<h1>Subdomain Taken Over!</h1>" > index.html
git add . && git commit -m "Takeover" && git push

# Configure custom domain in GitHub Pages settings
# Add blog.company.com as custom domain
```

**For AWS S3:**

```
# Create bucket with exact name
aws s3 mb s3://company-bucket-name

# Upload malicious content
echo "<h1>Subdomain Compromised</h1>" > index.html
aws s3 cp index.html s3://company-bucket-name/
aws s3 website s3://company-bucket-name --index-document index.html
```

**For Heroku:**

```
# Create new Heroku app with same name
heroku create company-app-name

# Deploy malicious content
git init && git add . && git commit -m "Takeover"
heroku git:remote -a company-app-name
git push heroku master
```

## Why is it Dangerous? ⚔️

![]()

* 🟢 Phishing attacks using a trusted domain.
* 🟢 Brand and reputation damage.
* 🟢 Malware or malicious scripts hosting.
* 🟢 Hard to detect and monitor.

## How Does It Happen? 🧩

![]()

1. Subdomain points to external service (GitHub Pages, AWS, etc.).
2. Service resource gets deleted or is unclaimed.
3. DNS record remains active.
4. Attacker claims the resource.
5. Attacker now controls the subdomain.

## Tools & Automation 🧰

![]()

* Subjack
* Subzy (Not much efficient)
* Nuclei (subdomain takeover templates)
* Subfinder + custom checks

## Our Approach

Sometimes the best vulnerabilities aren’t found through traditional scanning — they’re discovered through intelligence gatheri...