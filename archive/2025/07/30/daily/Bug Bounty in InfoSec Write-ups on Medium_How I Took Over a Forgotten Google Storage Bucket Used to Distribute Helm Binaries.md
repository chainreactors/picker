---
title: How I Took Over a Forgotten Google Storage Bucket Used to Distribute Helm Binaries
url: https://infosecwriteups.com/how-i-took-over-a-forgotten-google-storage-bucket-used-to-distribute-helm-binaries-374ae959179f?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-30
fetch_date: 2025-10-06T23:28:39.903580
---

# How I Took Over a Forgotten Google Storage Bucket Used to Distribute Helm Binaries

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F374ae959179f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-took-over-a-forgotten-google-storage-bucket-used-to-distribute-helm-binaries-374ae959179f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-took-over-a-forgotten-google-storage-bucket-used-to-distribute-helm-binaries-374ae959179f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-374ae959179f---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-374ae959179f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I Took Over a Forgotten Google Storage Bucket Used to Distribute Helm Binaries

[![Arshad Kazmi](https://miro.medium.com/v2/resize:fill:64:64/0*gAjmVBOIzADzdg_U.)](https://medium.com/%40arshadkazmi42?source=post_page---byline--374ae959179f---------------------------------------)

[Arshad Kazmi](https://medium.com/%40arshadkazmi42?source=post_page---byline--374ae959179f---------------------------------------)

3 min read

·

Jul 22, 2025

--

Listen

Share

A deprecated GCS bucket used to install Helm was still referenced in 1000s of GitHub projects — and I took it over.

*This post builds on my earlier two write-ups about broken link hijacking and GitHub username hijacks. In case you missed them:*

* 👉 [Part 1: How I Made $20K+ From Broken Link Hijacking](https://medium.com/%40arshadkazmi42/how-i-made-20k-from-broken-link-hijacking-on-github-repos-67d8917912f7)
* 👉 Part 2: Hijacking Renamed GitHub Usernames for Bounties

While scanning more GitHub repos for broken URLs, I came across this strange-looking Helm repository link:

> <https://kubernetes-helm.storage.googleapis.com>

It was returning a 404, but it wasn’t just any broken URL.

It was used in official-looking install scripts — and when I dug deeper, I found that it was part of how users used to **download and install the Helm binary**.

## 🧠 What This Bucket Was

This was a **Google Cloud Storage (GCS)** bucket originally used by the Helm maintainers to distribute Helm binary releases — probably before they moved to GitHub Releases or another domain.

The bucket URL appeared in:

* Shell scripts (curl | bash)
* Dockerfiles
* CI/CD setup guides
* Automation install instructions
* Public blog posts and tutorials

It was everywhere — **and it was broken.**

So I checked on Google Cloud…

And the bucket was **unclaimed**.

## 📦 Taking Control

I registered the GCS bucket:

> kubernetes-helm.storage.googleapis.com

and hosted a harmless takeover.html file to verify that I could control its responses.

I then ran a GitHub-wide search and found:

* 100s of open-source projects still referencing this exact bucket.
* Dozens of bug bounty-eligible companies either using or forking those projects.
* Many automated scripts relying on this link to install Helm.

## 💥 Why This Was Dangerous

This wasn’t a broken documentation link — this was a **binary distribution source**.

If a malicious actor had claimed the bucket, they could:

* Serve fake Helm binaries during install
* Inject malicious code into CI/CD setups
* Exploit systems blindly running curl | bash instructions

This was a **classic supply chain vulnerability** — quietly sitting in install paths.

## 💰 Reporting & Bounties

I responsibly disclosed the issue to affected companies and maintainers, especially those with bounty programs.

Some:

* Acknowledged the impact as **high** or **critical**
* Paid bounties accordingly
* Updated their install scripts to safer, verified sources

Others silently patched it — but the bucket references remained scattered across forks, blog posts, and archived CI files.

This bucket alone brought in **multiple bounties**, some small, a few significantly larger.

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

A few of the H1 Bounties

## ⚠️ I Still Own the Bucket

As of writing this, the bucket is still mine:

> kubernetes-helm.storage.googleapis.com

Even now, I occasionally see new traffic to it — likely from old CI setups or install guides that are still being run.

Across my scanning projects in 2021 — broken links, GitHub username hijacks, and forgotten cloud buckets — I earned around **$50,000** in bug bounties.

It all started with simple Bash scripts, creative thinking, and scanning what others overlooked.

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----374ae959179f---------------------------------------)

[Hackerone](https://medium.com/tag/hackerone?source=post_page-----374ae959179f---------------------------------------)

[Bugcrowd](https://medium.com/tag/bugcrowd?source=post_page-----374ae959179f---------------------------------------)

[Bucket Takeover](https://medium.com/tag/bucket-takeover?source=post_page-----374ae959179f---------------------------------------)

[Storage Bucket](https://medium.com/tag/storage-bucket?source=post_page-----374ae959179f---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--374ae959179f---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--374ae959179f---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--374ae959179f---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--374ae959179f---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--374ae959179f---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Arshad Ka...