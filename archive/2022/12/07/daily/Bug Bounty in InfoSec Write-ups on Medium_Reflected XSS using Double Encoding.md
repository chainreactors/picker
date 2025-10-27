---
title: Reflected XSS using Double Encoding
url: https://infosecwriteups.com/got-another-xss-using-double-encoding-e6493a9f7368?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-07
fetch_date: 2025-10-04T00:40:33.803092
---

# Reflected XSS using Double Encoding

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fe6493a9f7368&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgot-another-xss-using-double-encoding-e6493a9f7368&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fgot-another-xss-using-double-encoding-e6493a9f7368&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-e6493a9f7368---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-e6493a9f7368---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Reflected XSS using Double Encoding

## Bypassing XSS filters using Double Encoding

[![ag3n7](https://miro.medium.com/v2/resize:fill:64:64/1*a9R_2jXpqBZkrQ_fVuqzuA.jpeg)](https://ag3n7.medium.com/?source=post_page---byline--e6493a9f7368---------------------------------------)

[ag3n7](https://ag3n7.medium.com/?source=post_page---byline--e6493a9f7368---------------------------------------)

3 min read

·

Nov 17, 2022

--

3

Listen

Share

Hello Hackers,

Recently I started my bug hunting journey and got an XSS by Bypassing Cloudflare WAF (you can read about it [here](https://medium.com/%40ag3n7/how-i-bypassed-cloudflare-waf-to-get-my-first-bug-f02dab3a2d10)). Now I am back with another XSS by [Double Encoding](https://owasp.org/www-community/Double_Encoding).

> This attack technique consists of encoding user request parameters twice in hexadecimal format to bypass security controls or cause unexpected behavior from the application. It’s possible because the webserver accepts and processes client requests in many encoded forms.

Going directly into it…

If there is a will, there is a way. Like that if there is an input field, there is a ***chance*** of cross-site scripting. Currently, I am using very basic methods while trying to find bugs and improve myself by learning more methods and bugs. While going through some of the targets and testing input fields (like search boxes), I got an interesting input field, I just entered the usual input

![]()![]()

Search Bar

and checked the source code.

Press enter or click to view image in full size

![]()

source code

Then I added a single quote but it filtered the input and replaced it with *hello1&amp;* in some places and with ‘&’ in our target fields.

Press enter or click to view image in full size

![]()

I tried URL encoding there, Then also got the same output which means it decodes the input.

So I used [Double Encoding](https://owasp.org/www-community/Double_Encoding).
By using double encoding it’s possible to bypass security filters that only decode user input once. The second decoding process is executed by the backend platform or modules that properly handle encoded data, but don’t have the corresponding security checks in place.

Press enter or click to view image in full size

![]()

It works.

Then our basic payload ‘><script>alert(1)</script> with double encoding tried.

> %2527%253E%253Cscript%253Ealert%25281%2529%253C%252Fscript%253E

But it created an error

![]()

I searched for attributes of input tag to exploit using it.
[onfocus](https://www.w3schools.com/jsref/event_onfocus.asp) : The onfocus event occurs when an element gets focus.

‘ onfocus=’alert(1)’

> %2527%2520onfocus%253D%2527alert%25281%2529%2527%2520

Press enter or click to view image in full size

![]()

I clicked on the search bar, and the popup alert appeared.

![]()

But I thought of modifying it a little bit with autofocus which makes the text field automatically get focused upon page load and creates the popup alert while visiting the page itself.

‘ onfocus=’alert(1)’ autofocus=’

> %2527%2520onfocus%253D%2527alert%25281%2529%2527%2520autofocus%253D%2527

Press enter or click to view image in full size![]()

Press enter or click to view image in full size![]()

XSS

Yeah. It worked …

![]()

OpenBugBounty

You can also use payloads like

‘ onmouseover=’alert(1)’

> %2527%2520onmouseover%253D%2527alert%25281%2529%2527%2520

Thank You For Reading ….

## Follow me on :

Twitter: <https://twitter.com/ag3n7apk>

Linkedin: <https://www.linkedin.com/in/abhijith-pk-ag3n7/>

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Xss Filter Bypass](https://medium.com/tag/xss-filter-bypass?source=post_page-----e6493a9f7368---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----e6493a9f7368---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----e6493a9f7368---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----e6493a9f7368---------------------------------------)

[Cross Site Scripting](https://medium.com/tag/cross-site-scripting?source=post_page-----e6493a9f7368---------------------------------------)

--

--

3

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e6493a9f7368---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--e6493a9f7368---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--e6493a9f7368---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--e6493a9f7368---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--e6493a9f7368---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![ag3n7](https://miro.medium.com/v2/resize:fill:96:96/1*a9R_2jXpqBZkrQ_fVuqzuA.jpeg)](https://ag3n7.medium.com/?source=post_page---post_author_info--e6493a9f7368---------------------------------------)

[![ag3n7](https://miro.medium...