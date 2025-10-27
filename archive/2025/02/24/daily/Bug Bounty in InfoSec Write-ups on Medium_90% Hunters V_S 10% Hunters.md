---
title: 90% Hunters V/S 10% Hunters
url: https://infosecwriteups.com/90-hunters-v-s-10-hunters-fa9089523181?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-02-24
fetch_date: 2025-10-06T20:33:48.571408
---

# 90% Hunters V/S 10% Hunters

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ffa9089523181&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F90-hunters-v-s-10-hunters-fa9089523181&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2F90-hunters-v-s-10-hunters-fa9089523181&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-fa9089523181---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-fa9089523181---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 90% Hunters V/S 10% Hunters

[![Spectat0rguy](https://miro.medium.com/v2/resize:fill:64:64/1*wpYFLRnrUXdfWlb_RZ_JbQ.jpeg)](https://bitpanic.medium.com/?source=post_page---byline--fa9089523181---------------------------------------)

[Spectat0rguy](https://bitpanic.medium.com/?source=post_page---byline--fa9089523181---------------------------------------)

4 min read

·

Feb 22, 2025

--

1

Listen

Share

![]()

Image by Freepik

I am gonna start this post by asking some questions :

> What is Bug Bounty?
>
> What are the advantages of Bug Bounty Career over other traditional Car-eer paths?
>
> How competitive does bug bounty seem to you ?
>
> What are you doing to overthrow the competition?

You know the answers to 3 Questions perfectly and you are correct about it , but you are stuck at Question 4 and you can’t answer it perfectly because It’s always gonna be wrong.

> Why?

Before answering this question I am gonna point some things to you that you can’t see.

In this surge of bounty hunting we are facing immense competition and because of that we have assumed some things about Top Bounty Hunters and one of them is :

> They are born to be Bounty Hunters.
>
> They are Skilled at what they do.

So How did it happen?

Because you are doing the same thing they are doing and following the same fundamentals and what are you doing wrong that , you aren’t there at the Top.

The answer to this question is hidden in Question 4 :

> What are you doing to overthrow the competition?

Following are the things that separate the 10% from 90% :

## 1. Mindset & Approach

### 🔴 90% Hunters:

Follow automated tools blindly (Burp Suite, Nuclei, SQLmap).

Hunt for basic XSS, SQLi, and open directories.

Get frustrated when a program is heavily tested.

### 🟢 10% Elite Hunters:

Focus on logic-based vulnerabilities like IDOR, SSRF, and Business Logic Flaws.

Think like a developer, not just a hacker.

Use custom automation but validate results manually.

## 2. Target Selection

### 🔴 90% Hunters:

Chase big bounty programs (Google, Apple, Microsoft).

Go for publicly known vulnerabilities (CVE-based testing).

Use the same bug bounty platforms as everyone else.

### 🟢 10% Elite Hunters:

Find under-tested private programs.

Hunt on less crowded platforms (HackerOne Private, Intigriti, VDPs).

Go for smaller startups with weak security but high impact.

## 3. Recon & Discovery

### 🔴 90% Hunters:

Run one-liner recon commands and expect magic.

Use basic subdomain enumeration (subfinder, assetfinder).

Rely on default wordlists (SecLists).

### 🟢 10% Elite Hunters:

Create custom wordlists from JS files & API docs.

Analyze wayback data, GitHub leaks, and cloud misconfigurations.

Chain multiple tools into a custom pipeline.

## 4. Vulnerability Hunting

### 🔴 90% Hunters:

Focus on low-hanging fruit (Reflected XSS, outdated software).

Ignore business logic bugs.

Submit duplicate reports frequently.

### 🟢 10% Elite Hunters:

Find high-impact, unique bugs (OAuth misconfigurations, IDOR-to-Account Takeover).

Exploit API vulnerabilities (GraphQL, JWT, BOLA).

Chain multiple bugs into a full exploit (e.g., Open Redirect → SSRF → AWS Access).

## 5. Reporting & Presentation

### 🔴 90% Hunters:

Write basic reports with no proof-of-concept (PoC).

Submit one-line explanations with no impact analysis.

Get rejected due to lack of clarity.

### 🟢 10% Elite Hunters:

Write detailed, well-structured reports with PoC videos.

Explain real-world impact (e.g., "This can lead to account takeover").

Suggest a fix, increasing the chance of acceptance.

## 6. Automation vs. Manual Testing

### 🔴 90% Hunters:

Rely 100% on Nuclei, Burp Intruder, SQLmap.

Don't analyze results properly.

Miss edge-case vulnerabilities.

### 🟢 10% Elite Hunters:

Use tools for automation, but manually validate findings.

Write custom scripts for fuzzing and API testing.

Combine recon + logic-based attacks for deeper exploitation.

## 7. Persistence & Learning

### 🔴 90% Hunters:

Give up after one recon scan.

Complain about duplicate reports & no findings.

Keep using the same methods without improvement.

### 🟢 10% Elite Hunters:

Stay persistent, testing the same target multiple times.

Learn new techniques daily (Reverse engineering, AI-assisted fuzzing).

Analyze past successful reports to improve their methodology.

## 8. How They Approach Bug Bounties

### 🔴 90% Hunters:

Treat bug bounty like a lottery—scan, submit, and hope.

Give up if they don’t find a bug in 30 minutes.

Chase high-paying programs without a plan.

### 🟢 10% Elite Hunters:

Treat bug bounty like a business—consistent recon & strategy.

Have a structured methodology: recon → analysis → manual testing.

Focus on undiscovered attack surfaces, not just popular ones.

## 9. Understanding the Target

### 🔴 90% Hunters:

Just look at the main website (www.target.com).

Don't research how the business works.

Run the same subdomain enumeration tools as everyone else.

### 🟢 10% Elite Hunters:

Explore less tested assets: mobile apps, APIs, third-party integrations.

Read documentation, changelogs, API docs for hints.

Check acquisitions, subdomains, old infrastructure for weak points.

📌 Example: Instead of targeting www.target.com, they go for:

help.target.com (support systems)

old.target.com (legacy applications)

partner.target.com (third-party integrations)

## 10. Bug Hunting Strategy

### 🔴 90% Hunters:

Focus only on XSS, SQLi, Open Redirect.

Spam low-quality duplicate reports.

Use Burp Suite Intruder without any logic.

### 🟢 10% Elite Hunters:

Focus on business logic bugs (IDOR, BOLA, mass assignment).

Test OAuth misconfigurations, JWT manipulation, GraphQL exploits.

Understand how permissions work and find broken access controls.

📌 Example:

Instead of looking for basic XSS, an elite hunter will:

Check if account deletion endpoints can be abused.

Look for privilege escalation by modifying role permissions.

Exploit weak JWT implementations for authenticatio...