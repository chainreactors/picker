---
title: Param Hunting to Injections
url: https://infosecwriteups.com/param-hunting-to-injections-4365da5447cf?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2022-12-17
fetch_date: 2025-10-04T01:45:50.632709
---

# Param Hunting to Injections

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F4365da5447cf&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fparam-hunting-to-injections-4365da5447cf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fparam-hunting-to-injections-4365da5447cf&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-4365da5447cf---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-4365da5447cf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Param Hunting to Injections

## Hey hackers! How’s your week going?

[![TheBountyBox](https://miro.medium.com/v2/resize:fill:64:64/1*O8DiVc0Ht1q6OwzOiHuUKg.png)](https://thebountybox.medium.com/?source=post_page---byline--4365da5447cf---------------------------------------)

[TheBountyBox](https://thebountybox.medium.com/?source=post_page---byline--4365da5447cf---------------------------------------)

4 min read

·

Dec 16, 2022

--

2

Listen

Share

Here we are back with another blog.

Today we are going to discuss Effective Param-Hunting to Injections

![]()

So recently we have been working on a private project . Let’s call it *redacted.com* .

Since there were a lot of subdomains, we thought of filtering the subdomains based on the *content-length* to find domains which offer a large number of functionalities.

Press enter or click to view image in full size

![]()

So after filtering, we landed on <Sub.redacted.com> which had a login page.

Initially, we were looking for BAC; meanwhile, we noticed that when we enter invalid credentials on the login page, it responds with an error parameter in the url.

So briskly we started to inject *XSS* payloads to generate an *XSS* but no luck since we were unable to bypass the filtering.

![]()

Soon after we started to test the password reset functionality .

Here we noticed that after entering any invalid email there was no error param generated in the url so we thought of manually adding this param .

To our surprise the param was actually reflecting .

Again we tried injecting the *XSS* payloads but WAF was blocking everything.

Finally we thought of balancing using the </div> tag since the and boom here comes **HTML Injection** .

We know what you’re thinking, yeah **IFRAME** did the rest of the work .

![]()

Press enter or click to view image in full size

![]()

**Finding Hidden Parameters :**

There are a lot of tools like Paramminer , Arjun ,x8 etc that help us in finding hidden parameters but unfortunately in our case neither tool worked because the parameter might not be present in the default word list .

**Active Param Hunting :**

Active Param Hunting helps in detecting all the params and generating a custom target specific wordlist .

For Creating a custom wordlist we need to extract all the parameters related to the domain and for this we will use this beautiful tool [*getAllParams*](https://github.com/xnl-h4ck3r/GAP-Burp-Extension) .

### Steps :

1. Download and configure [getAllParams](https://github.com/xnl-h4ck3r/GAP-Burp-Extension) extension in your burp suite
2. Now start crawling the website automatically as well as manually .

A combination of manually testing and automation will always provide you with better results than blinding using the scripts

3. Now Target -> Sitemap -> Choose the target->Right Click-> Extensions -> Get All Params (GAP)

4. Save all the extracted params in a file

5. You can also gather all the urls using *gau* , *wayback* , *Katana* or any other tool and then extract all the parameters from the extracted urls .

We have written a very basic script which can extract all the parameters from the urls gathered from various tools :

[*Param-Extract*](https://github.com/302Found1/Param-Extract) *(Yeah lazy script but works also we will update it later)*

Press enter or click to view image in full size

![]()

Alternatively you can also use the below one-liner to extract the urls using unfurl tool :

> cat urls | unfurl format %q | cut -d “=” -f1 | sort -u > params.txt

6. Now merge both the param files and sort -u

7. Once you have created a custom wordlist with all the params you can easily use the Paraminer burp extension to discover the hidden params .

8. Once you have identified the hidden parameters you can test for various injection or other bugs based on the case scenarios .

Happy Hunting !!!!

### From Infosec Writeups: A lot is coming up in the Infosec every day that it’s hard to keep up with. [Join our weekly newsletter](https://weekly.infosecwriteups.com/) to get all the latest Infosec trends in the form of 5 articles, 4 Threads, 3 videos, 2 GitHub Repos and tools, and 1 job alert for FREE!

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----4365da5447cf---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----4365da5447cf---------------------------------------)

[Infosec](https://medium.com/tag/infosec?source=post_page-----4365da5447cf---------------------------------------)

[Testing](https://medium.com/tag/testing?source=post_page-----4365da5447cf---------------------------------------)

[Ethical Hacking](https://medium.com/tag/ethical-hacking?source=post_page-----4365da5447cf---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4365da5447cf---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--4365da5447cf---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--4365da5447cf---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--4365da5447cf---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--4365da5447cf---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com...