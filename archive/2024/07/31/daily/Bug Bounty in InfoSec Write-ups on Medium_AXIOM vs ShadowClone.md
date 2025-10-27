---
title: AXIOM vs ShadowClone
url: https://infosecwriteups.com/axiom-vs-shadowclone-147a26878c7c?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-07-31
fetch_date: 2025-10-06T17:42:10.895463
---

# AXIOM vs ShadowClone

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F147a26878c7c&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faxiom-vs-shadowclone-147a26878c7c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faxiom-vs-shadowclone-147a26878c7c&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-147a26878c7c---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-147a26878c7c---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# AXIOM vs ShadowClone

[![Ott3rly](https://miro.medium.com/v2/resize:fill:64:64/1*3wMPJmhJUNOpqobsPBkS8g.jpeg)](https://ott3rly.medium.com/?source=post_page---byline--147a26878c7c---------------------------------------)

[Ott3rly](https://ott3rly.medium.com/?source=post_page---byline--147a26878c7c---------------------------------------)

4 min read

·

Jul 22, 2024

--

Listen

Share

Looking for a powerful tool to revolutionize your bug bounty recon? Today, we’re comparing [AXIOM](https://github.com/pry0cc/axiom) and [ShadowClone](https://github.com/fyoorer/ShadowClone/) — two of the most robust recon orchestration tools. Let’s explore their key use cases, weigh the pros and cons, and uncover the most effective strategies!

## Introduction to Tools

Let’s begin by understanding the technical foundation of our two tools. Both AXIOM and ShadowClone are designed to distribute the bug bounty tool workload across the cloud. The key difference lies in their infrastructure choices. AXIOM operates primarily through virtual machines or VPS, while ShadowClone leverages AWS Lambda functions, which, while potentially more scalable and cost-effective, come with certain inherent limitations. If you encounter difficulties installing ShadowClone, check out my [video](https://www.patreon.com/posts/shadowclone-108004318?utm_medium=clipboard_copy&utm_source=copyLink&utm_campaign=postshare_creator&utm_content=join_link) on Patreon for a detailed guide

## Pros and Cons

AXIOM’s VM-based approach offers great customizability and control. It’s ideal for handling intensive tasks and long operations. However, it requires more setup and maintenance. VMs might also be less cost-effective for smaller or intermittent tasks due to continuous resource allocation.

![]()

ShadowClone uses AWS Lambda functions, enabling rapid deployment and automatic scalability. This can be more economical, as you only pay for the compute time used. It’s perfect for quick starts with minimal setup. However, Lambda functions have a maximum runtime limit, which can restrict long tasks. They also have memory and compute capacity limits, making them less suitable for very resource-intensive tasks.

Press enter or click to view image in full size

![]()

## Features Comparison

AXIOM uses a modular approach, allowing you to edit files as different modules and add your own. This makes it highly adaptable to various recon scenarios. It supports multiple cloud providers, giving you more options for deploying workloads. It is highly customizable with features like backups, saving files to VMs, and many more. AXIOM is also maintained more frequently, with many contributors on GitHub.

Press enter or click to view image in full size

![]()

ShadowClone focuses on simplicity. You can start recon tasks almost immediately. Its auto-scaling feature handles tasks efficiently without manual intervention. While it lacks some of AXIOM’s customization options, ShadowClone has its own thing — simplicity. Remember, some cloud providers can be more expensive with ShadowClone, so watch your costs even when using Lambdas!

Press enter or click to view image in full size

![]()

## Use Cases

Choosing the right tool depends on your specific bug bounty scenarios. AXIOM is great for detailed recon tasks that need a lot of customization and time. For example, tools for domain crawling like Katana and GoSpider, or gathering wayback data with gau or Waymore, can take a long time to finish. AXIOM is also ideal for using Nuclei with multiple templates or groups of templates, as these scans take much longer to complete. These tasks take longer due to the large amount of data they process, making AXIOM’s robust setup more suitable.

ShadowClone, on the other hand, is best for quick and scalable tasks. Think of security research of a single vulnerability. It’s perfect for gathering subdomains with tools like Subfinder and Amass, or checking alive hosts with HTTPX or Httprobe. You can also use Nuclei with limited or single templates. These tasks are faster and need less processing time, making ShadowClone’s Lambda-based setup ideal. Its easy setup and cost-effective model are great for these simpler tasks.

## Conclusion and Final Thoughts

To conclude, both AXIOM and ShadowClone are powerful tools for bug bounty recon. AXIOM is best for detailed, long-term tasks like domain crawling and vulnerability scanning. It offers great customization and processing power. ShadowClone excels in quick, scalable tasks such as subdomain gathering and checking alive hosts. It provides rapid deployment and cost efficiency. Choose the tool that fits your specific needs.

If you find this information useful, please share this article on your social media, I will greatly appreciate it! I am active on [Twitter](https://ott3rly.com/twitter), check out some content I post there daily! If you are interested in video content, check my [YouTube](https://ott3rly.com/youtube). Also, if you want to reach me personally, you can visit my [Discord](https://ott3rly.com/discord) server. Cheers!

*Originally published at* [*https://ott3rly.com*](https://ott3rly.com/axiom-vs-shadowclone/) *on July 22, 2024.*

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----147a26878c7c---------------------------------------)

[Bug Bounty Tips](https://medium.com/tag/bug-bounty-tips?source=post_page-----147a26878c7c---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----147a26878c7c---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----147a26878c7c---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----147a26878c7c---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--147a26878c7c--...