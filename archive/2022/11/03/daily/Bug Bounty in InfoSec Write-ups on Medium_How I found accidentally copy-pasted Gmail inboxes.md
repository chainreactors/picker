---
title: How I found accidentally copy-pasted Gmail inboxes
url: https://infosecwriteups.com/how-i-found-accidentally-copy-pasted-gmail-inboxes-49fcb8da5b8a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-11-03
fetch_date: 2025-10-03T21:38:33.545648
---

# How I found accidentally copy-pasted Gmail inboxes

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F49fcb8da5b8a&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-accidentally-copy-pasted-gmail-inboxes-49fcb8da5b8a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-accidentally-copy-pasted-gmail-inboxes-49fcb8da5b8a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-49fcb8da5b8a---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-49fcb8da5b8a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I found accidentally copy-pasted Gmail inboxes

## It all started with this text in my own Gmail:

[![Ethicalhacker](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*PQrD24begsRIad0E)](https://medium.com/%40melderanoniemnl?source=post_page---byline--49fcb8da5b8a---------------------------------------)

[Ethicalhacker](https://medium.com/%40melderanoniemnl?source=post_page---byline--49fcb8da5b8a---------------------------------------)

2 min read

·

Oct 31, 2022

--

Listen

Share

![]()

Label in Gmail

I read about ethical hackers searching with Google Dorks based on information from known content, like login pages. Above text did sound promising to check on Google. To my suprise I got some results in Google. The results in Google showed like 30 hits with the searched text.

After I clicked on 1 of the links I discovered it looked like the Gmail inbox of a person. But it wasn’t the “live” Gmail inbox. It was a copy from an earlier moment. It seems the person accidentially copy-pasted their Gmail page when they probably just wanted to copy an image or text.

Press enter or click to view image in full size

![]()

I clicked on Show Page Source to check for interesting data. What I found was very interesting, it seems the JSON of all the emails in the email folder of the account was included in the HTML source.

Press enter or click to view image in full size

![]()

These mails could contain personal and confidential information, like customer conversations, personal data and passwords.

**I have notified most of the email inboxes I found, so they could remove the file which contains the copy-pasted Gmail data from their website.**

Google Dorks to use to find copy-pasted Gmail inboxes:

1. “Index of /wp-content/uploads’ “gmail.htm”
2. intitle:Gmail — (no subject)
3. inurl:[@gmail](http://twitter.com/gmail).com — Gmail.htm
4. Click to teach Gmail this conversation is not important
5. GM\_SUPPORTED\_GECKO\_VERSION=”2.0.0";
6. “Belangrijk volgens ons tovermiddel”

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Infosec](https://medium.com/tag/infosec?source=post_page-----49fcb8da5b8a---------------------------------------)

[Vulnerability](https://medium.com/tag/vulnerability?source=post_page-----49fcb8da5b8a---------------------------------------)

[Gmail](https://medium.com/tag/gmail?source=post_page-----49fcb8da5b8a---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----49fcb8da5b8a---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----49fcb8da5b8a---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--49fcb8da5b8a---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--49fcb8da5b8a---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--49fcb8da5b8a---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--49fcb8da5b8a---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--49fcb8da5b8a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Ethicalhacker](https://miro.medium.com/v2/resize:fill:96:96/0*PQrD24begsRIad0E)](https://medium.com/%40melderanoniemnl?source=post_page---post_author_info--49fcb8da5b8a---------------------------------------)

[![Ethicalhacker](https://miro.medium.com/v2/resize:fill:128:128/0*PQrD24begsRIad0E)](https://medium.com/%40melderanoniemnl?source=post_page---post_author_info--49fcb8da5b8a---------------------------------------)

[## Written by Ethicalhacker](https://medium.com/%40melderanoniemnl?source=post_page---post_author_info--49fcb8da5b8a---------------------------------------)

[5 followers](https://medium.com/%40melderanoniemnl/followers?source=post_page---post_author_info--49fcb8da5b8a---------------------------------------)

·[1 following](https://medium.com/%40melderanoniemnl/following?source=post_page---post_author_info--49fcb8da5b8a---------------------------------------)

## No responses yet

[Help](https://help.medium.com/hc/en-us?source=post_page-----49fcb8da5b8a---------------------------------------)

[Status](https://status.medium.com/?source=post_page-----49fcb8da5b8a---------------------------------------)

[About](https://medium.com/about?autoplay=1&source=post_page-----49fcb8da5b8a---------------------------------------)

[Careers](https://medium.com/jobs-at-medium/work-at-medium-959d1a85284e?source=post_page-----49fcb8da5b8a---------------------------------------)

Press

[Blog](https://blog.medium.com/?source=post_page-----49fcb8da5b8a---------------------------------------)

[Privacy](https://policy.medium.com/medium-privacy-policy-f03bf92035c9?source=post_page-----49fcb8da5b8a---------------------------------------)

[Rules](https://policy.medium.com/medium-rules-30e5502c4eb4?source=post_page-----49fcb8da5b8a---------------------------------------)

[Ter...