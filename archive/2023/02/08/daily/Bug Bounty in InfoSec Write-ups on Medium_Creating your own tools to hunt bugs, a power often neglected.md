---
title: Creating your own tools to hunt bugs, a power often neglected
url: https://infosecwriteups.com/create-your-own-tools-for-hunting-bugs-a-power-often-neglected-186213e4d206?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-08
fetch_date: 2025-10-04T05:57:59.035519
---

# Creating your own tools to hunt bugs, a power often neglected

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F186213e4d206&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcreate-your-own-tools-for-hunting-bugs-a-power-often-neglected-186213e4d206&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcreate-your-own-tools-for-hunting-bugs-a-power-often-neglected-186213e4d206&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-186213e4d206---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-186213e4d206---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Creating your own tools to hunt bugs, a power often neglected

[![Rachid.A](https://miro.medium.com/v2/resize:fill:64:64/1*ozPqF_1nHwMgPECyOySdDA.png)](https://medium.com/%40zhero_?source=post_page---byline--186213e4d206---------------------------------------)

[Rachid.A](https://medium.com/%40zhero_?source=post_page---byline--186213e4d206---------------------------------------)

4 min read

·

Jan 20, 2023

--

1

Listen

Share

Press enter or click to view image in full size

![]()

Credit : Pinterest

Creating your own tools based on the needs encountered while hunting bugs is often a **power** that is overlooked…

As you know, there are many different security tools on GitHub and it’s not necessary to re-code what already exists because as they say: “*Developers don’t reinvent the wheel*”.

But what about the wheel that hasn’t been invented yet? 🧪

## **Automation**

There is no perfect and absolute methodology in bug hunting, and everyone tries to find their way according to their skill level and preferred attack vectors. However, everyone can agree that **anything that repeats itself or does not require much thinking should be automated**.

The competition for bug bounty programs is fierce, **it’s essential to optimize your time and automate what can be done** so that you can focus on tasks that require manual tests and deep thinking. Whether you are a full-time hunter or not, *your time is your capital*, use it wisely and always strive to maximize your “chances” of success.

Whenever you identify a task that needs to be automated, start by doing some research to make sure that an existing tool has not already been created for this purpose — which will likely be the case most of the time as the infosec community is large and its contributors are many.

## Stepping out of the beaten path

However, if existing tools are incomplete, too slow, or don’t suit you in any way, **roll up your sleeves and get into code**. You can either choose to customize the existing wheel according to your taste, or create a new one differently **that will satisfy your expectations where the first one failed**.

If the desired tool does not exist, there is no question anymore: it must be created from scratch. **The time invested in creating a tool will most likely pay off later**, whether there are tangible results or not — as the time formerly spent on these tasks manually will eventually be “refunded” when using the tool.

Sometimes it can be interesting — even necessary — to create “*throwaway*” tools to exploit specific vulnerabilities (race condition for example) that are unique to certain use cases with peculiar configurations on a program.

## I created my own reconnaissance tool

After using some of the most popular reconnaissance tools — all wonderful — for a while, **some details bothered me a bit** : sometimes slow because scans are big, having to use multiple different tools while crossing the results of different scans, visuals sometimes not pleasant while displaying results… Of course, this is only my opinion **but it’s what pushed me** — *among other things* —to start creating my humble tool : **Gank recon. 🏹**

![]()

*Subdomains enumeration, various scans, and testing of some vulnerabilities.*

⚙️ **Its features are as follows (\*)**:

* Enumeration of subdomains from a domain name
* Checking if a subdomain is takeoverable
* Checking if an inaccessible subdomain is bypassable via HTTP verb tampering or custom header
* Basic Auth bruteforce 🆕
* Search for secrets (API keys, tokens, passwords, etc.) in the subdomain and its javascript files 🆕
* Port scan
* Recording of results and notifications of changes between each execution of the program (new subdomain/open ports/HTTP code)
* Ergonomic listing of the different active subdomains sorted by HTTP code with the information related to them (open ports, vulnerabilities, changes)

> More features are coming soon, don’t hesitate to leave a star at the repo to see when they are uploaded

Press enter or click to view image in full size

![]()

Output example from Gank recon.

**(\*)** For more information on **Gank recon**. check the repository here : <https://github.com/cold-try/Gank-RECON>

The creation of tools is not limited to reconnaissance tools, and if this interests some I will put other of my tools online.

**Thank you for reading me**, if you have any questions do not hesitate to let me know. Happy *hunting* 🏹

* **My Twitter account :** <https://twitter.com/zhero___>
* **My Linkedin account** : <https://www.linkedin.com/in/rachid-allam-65477718a/>

> **Take a look at my previous write-up titled***: HTML injection in an email template*
>
> <https://medium.com/bugbountywriteup/html-injection-in-an-email-template-f1a3fe77012c>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----186213e4d206---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----186213e4d206---------------------------------------)

[Development](https://medium.com/tag/development?source=post_page-----186213e4d206---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----186213e4d206---------------------------------------)

[Pentesting](https://medium.com/tag/pentesting?source=post_page-----186213e4d206---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--186213e4d206---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--186213e4d206---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_p...