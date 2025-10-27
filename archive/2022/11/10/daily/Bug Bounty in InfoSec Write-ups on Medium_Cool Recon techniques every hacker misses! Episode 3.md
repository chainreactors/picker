---
title: Cool Recon techniques every hacker misses! Episode 3
url: https://infosecwriteups.com/cool-recon-techniques-every-hacker-misses-episode-3-3812e7da3425?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-10
fetch_date: 2025-10-03T22:13:44.256509
---

# Cool Recon techniques every hacker misses! Episode 3

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F3812e7da3425&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcool-recon-techniques-every-hacker-misses-episode-3-3812e7da3425&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcool-recon-techniques-every-hacker-misses-episode-3-3812e7da3425&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-3812e7da3425---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-3812e7da3425---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Cool Recon techniques every hacker misses! Episode 3🔥🔥

[![TheBountyBox](https://miro.medium.com/v2/resize:fill:64:64/1*O8DiVc0Ht1q6OwzOiHuUKg.png)](https://thebountybox.medium.com/?source=post_page---byline--3812e7da3425---------------------------------------)

[TheBountyBox](https://thebountybox.medium.com/?source=post_page---byline--3812e7da3425---------------------------------------)

4 min read

·

Nov 8, 2022

--

3

Listen

Share

Welcome to the 3rd Episode of Cool Recon Techniques. We are back with some more cool recon techniques which we think hackers out there usually miss out on! If you haven’t read the first Episode [here](/cool-recon-techniques-every-hacker-misses-1c5e0e294e89)’s the link! And here is the link to the [second](https://medium.com/bugbountywriteup/cool-recon-techniques-every-hacker-misses-episode-2-8024e8338756) Episode

And Here we Go!!

![]()

> **Technique 15: Enumerate GitHub Repositories for a particular username**

While doing GitHub Recon, it is very difficult to find the exact organization name and its repositories to find sensitive data. [enumerepo](https://github.com/trickest/enumerepo) will help you out to list all the repositories for a valid GitHub account. All you have to do is simply submit account names and see the magic!

> **Command:** enumerepo -token-string GITHUB\_TOKEN -usernames accounts.txt -o output file

Press enter or click to view image in full size

![]()

> **Technique 16: Say a big Hi to Katana**

Woah! Woah! Project Discovery’s new tool is over here! Say Bye to all the different tools such as waybackurls, gau, subjs and hi to [Katana](https://github.com/projectdiscovery/katana)

Press enter or click to view image in full size

![]()

Katana is an advanced web crawler which crawls all the endpoints. It comes up with various different filters such as JavaScript parsing/crawling, field scopes, crawl scopes, crawling for known files, automatic form fill. It also provides various display options to filter output. And not just this you can infact store field values which can be later useful to build wordlists.

Press enter or click to view image in full size

![]()

The table below describes all features and commands of katana.

Press enter or click to view image in full size

![]()

**Katana to nuclei — One Liner**

cat subdomains.txt | httpx ––silent >> alive.txt && cat alive.txt | katana ––silent >> endpoints.txt && cat endpoints.txt | nuclei -t <YOUR\_TEMPLATES>

> **Technique 17: Query DNS to get IPs and Subdomains using RapidDNS**

Increase your attack surface by querying DNS to find IP Addresses using [RapidDNS](https://rapiddns.io/). RapidDNS is a DNS query tool with more than 3 billion data and more being added daily.

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

> **Technique 18: Large Scope Application Recon Issues?**

Ever found a large scope domain with huge assets in scope and don't know how to find the entire information? No worries 3klCon comes to the rescue. [3klCon](https://github.com/eslam3kl/3klCon) is an automation Recon tool which works with Large & Medium scopes. It performs more than 20 tasks and gets back all the results in separated files.

> **Technique 19:** S3 Bucket Weakness Discovery

Wanna find S3 buckets from a domain and discover weaknesses in them. Then say hi to [Festin](http://github.com/cr0hn/festin). A tool which finds S3 buckets using various techniques such as crawling, DNS crawling, S3 Response analysis, etc. The best part you do not require any AWS credentials. It also allows to download bucket objects.

Press enter or click to view image in full size

![]()

> **Technique 20: Wordpress Recon**

Ever came across a Wordpress website and do not know how to start the recon? No worries! [WPRecon](https://github.com/AngraTeam/wprecon) is here for you. WPRecon, is a tool for the recognition of vulnerabilities and blackbox information for wordpress.

Simply add your domain name on <https://wprecon.com/> and gain all the different information.

Press enter or click to view image in full size

![]()

We hope that these recon techniques might help you to add and update your methodology. Do share your recon methodology in the comments section.

Happy Hunting!

From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----3812e7da3425---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----3812e7da3425---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----3812e7da3425---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----3812e7da3425---------------------------------------)

[Penetration Testing](https://medium.com/tag/penetration-testing?source=post_page-----3812e7da3425---------------------------------------)

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--3812e7da3425---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--3812e7da3425---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--3812e7da3425---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--3812e7da3425-----------------------------------...