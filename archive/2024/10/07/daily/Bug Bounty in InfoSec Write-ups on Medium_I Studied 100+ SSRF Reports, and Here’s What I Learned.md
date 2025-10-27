---
title: I Studied 100+ SSRF Reports, and Here’s What I Learned
url: https://infosecwriteups.com/i-studied-100-ssrf-reports-and-heres-what-i-learned-1654c72ee2df?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-10-07
fetch_date: 2025-10-06T18:49:50.527608
---

# I Studied 100+ SSRF Reports, and Here’s What I Learned

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F1654c72ee2df&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-studied-100-ssrf-reports-and-heres-what-i-learned-1654c72ee2df&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-studied-100-ssrf-reports-and-heres-what-i-learned-1654c72ee2df&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-1654c72ee2df---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-1654c72ee2df---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# I Studied 100+ SSRF Reports, and Here’s What I Learned

[![Aditya Sawant](https://miro.medium.com/v2/resize:fill:64:64/1*tPIw8IKh8vKqtSRVYOtRCA.jpeg)](https://medium.com/%40adityasawant00?source=post_page---byline--1654c72ee2df---------------------------------------)

[Aditya Sawant](https://medium.com/%40adityasawant00?source=post_page---byline--1654c72ee2df---------------------------------------)

7 min read

·

Oct 6, 2024

--

8

Listen

Share

Press enter or click to view image in full size

![]()

After diving into over 100 write-ups and reports on Server-Side Request Forgery (SSRF), I’ve compiled the key insights and knowledge I’ve gained into this blog. Here, I aim to share a comprehensive overview of SSRF vulnerability

## Server-Side Request Forgery (SSRF)

Server-Side Request Forgery (SSRF) is a vulnerability that allows an attacker to send crafted requests from a vulnerable server to other internal or external resources. SSRF occurs when a web application accepts a URL or IP address input from a user and uses that input to make requests without properly validating or sanitizing it.

## Identifying SSRF Vulnerabilities

Identifying SSRF in a target application is about understanding how that application interacts with external resources, processes URLs, and handles user input. The first thing you want to do is take a step back and review all the functions in the target application that fetch external resources. This could be anything from loading images to fetching data from other servers. These spots are the most likely entry points for SSRF vulnerabilities.

**URL Import Features**: A common one. Think about functions where the application fetches something based on a URL — maybe an image importer or data fetcher. If the app is grabbing content from an external URL, you can bet it might be susceptible to SSRF, especially if there’s no proper validation. The idea here is to try feeding internal URLs like `http://localhost` or `http://127.0.0.1`

**File Upload Mechanisms**: Oh yes, file uploads. These can be sneaky. Imagine an application that lets users upload files — things like PDFs, SVGs, or even Office documents. If the backend processes these files, SSRF might be hiding here. You can try uploading files with embedded URLs pointing to internal services (Reference: [The PDF Trojan Horse: Leveraging HTML Injection for SSRF and Internal Resource Access](https://uchihamrx.medium.com/the-pdf-trojan-horse-leveraging-html-injection-for-ssrf-and-internal-resource-access-fbf69efcb33d)).

**Headless Browsers / HTML Rendering**: These are usually found in features that generate PDFs or images on the backend. When you find a target using a headless browser, try injecting URLs into areas that process HTML content. If you manage to make the backend fetch something unintended, you might have hit an SSRF goldmine! (Reference: [SSRF on a Headless Browser Becomes Critical](https://medium.com/%40Nightbloodz/ssrf-on-a-headless-browser-becomes-critical-c08daaa1017e)).

**Server Status and Monitoring Features:** Now, look for those features that allow you to check server status or application health. These functionalities often query internal services for status information — perfect spots for SSRF. If you find one, try manipulating the requests to hit internal endpoints or sensitive services (Reference: [31k SSRF in Google Cloud Monitoring](https://nechudav.blogspot.com/2020/11/31k-ssrf-in-google-cloud-monitoring.html)).

**Proxy Implementations:** Proxies are interesting because they route requests through the server. If the application lets you send requests through a proxy and doesn’t validate the URLs strictly, you’ve got a shot at SSRF. This is especially true if it doesn’t sanitize user-supplied URLs. Try sending requests to internal services or other unauthorized endpoints and see what happens (Reference: [Server-Side Request Forgery on Havoc C2](https://blog.chebuya.com/posts/server-side-request-forgery-on-havoc-c2/)).

**Vulnerabilities in Security Mechanisms:** It’s not just the app itself — sometimes, SSRF is hiding in the libraries and security mechanisms that the application uses. Authentication libraries, request-handling components, or other backend tools could have SSRF flaws. You’ll want to audit those, too, because these third-party systems often expose vulnerabilities you wouldn’t expect (Reference: [Digging for SSRF in Next.js Apps](https://www.assetnote.io/resources/research/digging-for-ssrf-in-nextjs-apps)).

**File Storage Integrations:** If your target integrates with third-party services like Google Drive, Amazon S3, or Dropbox, check if the app makes server-side requests to fetch or store files. These are excellent candidates for SSRF, as you can try manipulating the requests to fetch internal files or data from unauthorized services. By injecting a crafted URL into these integrations, you might access internal systems that were never meant to be exposed (Reference: [SSRF: Server-Side Request Forgery Worth $4,913](https://medium.com/techfenix/ssrf-server-side-request-forgery-worth-4913-my-highest-bounty-ever-7d733bb368cb)).

**Path Parameters and Host Headers:** Pay close attention to how path parameters and host headers are handled. If an application uses path parameters to construct server-side requests, that’s another spot to test for SSRF. Try manipulating the parameters to redirect requests to internal resources. Similarly, the host header might be leveraged to control where requests are sent. Test for any weaknesses here — you might be able to influence the destination of requests using the host header (Reference: [Host Header Injection to Complete Organization Takeover](https://medium.com/%40_yldrm/host-header-injection-to-complete-organization-takeover-67a8a2ddb188)).

## Blind SSRF

Blind SSRF is a vulnerability where you can send requests to internal hosts but only receive a status code in response, rather than the ...