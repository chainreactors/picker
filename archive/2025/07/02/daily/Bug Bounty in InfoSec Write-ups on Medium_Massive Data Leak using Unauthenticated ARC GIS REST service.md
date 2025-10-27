---
title: Massive Data Leak using Unauthenticated ARC GIS REST service
url: https://infosecwriteups.com/massive-data-leak-using-unauthenticated-arc-gis-rest-service-7a59ca13ca28?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-02
fetch_date: 2025-10-06T23:50:16.401709
---

# Massive Data Leak using Unauthenticated ARC GIS REST service

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7a59ca13ca28&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmassive-data-leak-using-unauthenticated-arc-gis-rest-service-7a59ca13ca28&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fmassive-data-leak-using-unauthenticated-arc-gis-rest-service-7a59ca13ca28&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7a59ca13ca28---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7a59ca13ca28---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Massive Data Leak using Unauthenticated ARC GIS REST service

[![Ronak Patel](https://miro.medium.com/v2/resize:fill:64:64/1*yV1aLbdrDBM9XZBdntF_kQ.jpeg)](https://ronak-9889.medium.com/?source=post_page---byline--7a59ca13ca28---------------------------------------)

[Ronak Patel](https://ronak-9889.medium.com/?source=post_page---byline--7a59ca13ca28---------------------------------------)

3 min read

·

Jul 1, 2025

--

Listen

Share

Hello Everyone! Hope You are doing Great!!!

This write-up is about my recently resolved bug as it belongs to Private program and with their permission i am writing this blog with redacted details.

I started working with recon on this domain, I would call “example.com” ,I generally use tools like assetfinder,subfinder,sublister to find the subdomains then sort their output in a single file for the unique result.

```
sort -u asset_example.txt sublister_example.txt subfinder_example.txt > rec_example.txt
```

I filter this output with the httpx to get the live subdomain as below

```
cat rec_example.txt | httpx > rec_httpx.txt
```

In this particular case rec\_example.txt contained around six subdomains only so i decided to inspect each entry instead of relying on httpx.

One subdomain found was “gis.example.com”. Upon browsing it gave me status code 503 service unavailable. so as usual we skip to next subdomain but i did perform nuclei scan on this subdomain which reveled result

Rest endpoint at “gis.example.com/server/rest/services”

I immediately fired this endpoint and it was containing ARC GIS 11.1 server Rest endpoint.

Press enter or click to view image in full size

![]()

REST SERVICES

As you can see it contains different endpoints like country ,utilities and more. I tried to access Country endpoint and it brought me to login endpoint and gave me 503 service unavailable as below.

Press enter or click to view image in full size

![]()

But if we see directory there is service ExportCSV as seen below

Press enter or click to view image in full size

![]()

ExportCSV

Upon exploring this option brought me to the Task submitting UI so that does mean it allowed unauthenticated user.

Press enter or click to view image in full size

![]()

Next i submitted the task and it generated output in zip file

Press enter or click to view image in full size

![]()

Press enter or click to view image in full size

![]()

As this is the Insurance company the output contained massive data of the farm profiles like location of the farms, crops ,third party auditing status ,soil health ,property name, tenancy and more data.

This bug was marked with the severity of 7.5 (High) and i was rewarded with Bounty accordingly.

Takeaway: After this finding i though if i relied on httpx output than i would have missed this bug as subdomain was giving 503 status. Always rely in multiple ways to recon.

Disclaimer: This research was part of the Bug bounty program. If someone does unauthorized activity on unauthorized asset inspiring by this than i am not responsible.

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----7a59ca13ca28---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----7a59ca13ca28---------------------------------------)

[Information Security](https://medium.com/tag/information-security?source=post_page-----7a59ca13ca28---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----7a59ca13ca28---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7a59ca13ca28---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7a59ca13ca28---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--7a59ca13ca28---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--7a59ca13ca28---------------------------------------)

·[Last published 3 hours ago](/actuator-unleashed-a-guide-to-finding-and-exploiting-spring-boot-actuator-endpoints-29252dcd9d79?source=post_page---post_publication_info--7a59ca13ca28---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ronak Patel](https://miro.medium.com/v2/resize:fill:96:96/1*yV1aLbdrDBM9XZBdntF_kQ.jpeg)](https://ronak-9889.medium.com/?source=post_page---post_author_info--7a59ca13ca28---------------------------------------)

[![Ronak Patel](https://miro.medium.com/v2/resize:fill:128:128/1*yV1aLbdrDBM9XZBdntF_kQ.jpeg)](https://ronak-9889.medium.com/?source=post_page---post_author_info--7a59ca13ca28---------------------------------------)

[## Written by Ronak Patel](https://ronak-9889.medium.com/?source=post_page---post_author_info--7a59ca13ca28---------------------------------------)

[419 followers](https://ronak-9889.medium.com/followers?source=post_page---post_author_info--7a59ca13ca28---------------------------------------)

·[21 following](https://medium.com/%40ronak-9889/following?source=post_page---post_author_info--7a59ca13ca28---------------------------------------)

Cybersecurity Researcher

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----7a59ca13ca28---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----7a59ca13ca28...