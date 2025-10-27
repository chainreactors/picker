---
title: Password Reset Poisoning with Host Header Injection
url: https://infosecwriteups.com/password-reset-poisoning-with-host-header-injection-345b902a9ca5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-07
fetch_date: 2025-10-04T05:50:52.438396
---

# Password Reset Poisoning with Host Header Injection

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F345b902a9ca5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpassword-reset-poisoning-with-host-header-injection-345b902a9ca5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fpassword-reset-poisoning-with-host-header-injection-345b902a9ca5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-345b902a9ca5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-345b902a9ca5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Password Reset Poisoning with Host Header Injection

[![Bharat Singh](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*SLUmV3MPNVcuzAnQFICGyg.gif)](https://bharat-singh.medium.com/?source=post_page---byline--345b902a9ca5---------------------------------------)

[Bharat Singh](https://bharat-singh.medium.com/?source=post_page---byline--345b902a9ca5---------------------------------------)

3 min read

·

Feb 3, 2023

--

1

Listen

Share

Press enter or click to view image in full size

![]()

Hey folks, I am [Bharat Singh](https://twitter.com/zingzangoo) a Security researcher and Bug Hunter. I am here with an amazing writeup about Password Reset Poisoning with Host Header Injection Vulnerability which I recently found on a VDP and got rewarded with a HOF.

Press enter or click to view image in full size

![]()

> **What is Host Header Injection?**
>
> Host Header injection is a type of vulnerability that allows an attacker to manipulate the host header sent in an HTTP request. By manipulating the host header, an attacker can direct the web server to serve a different website or application. This can be used to perform various types of attacks, such as phishing, cross-site scripting (XSS), or even redirecting a user to a malicious website with password reset poisoning.

Now lets dive into the main story about how I found that bug and how you guys can find and exploit this vulnerability.

### Story of the Bug

I was hunting on a VDP (Vulnerability Disclosure Program), it was a video streaming platform where you can watch movies and series. I tested that webapp for about 1 hour but got no luck and finally decided to test the password reset functionality, but I was not expecting to find any vulnerability there.

After clicking on forgot password option, I entered my email address and intercepted that request in my Burp Suite and send that request to the repeater.

I decided to play with that request and changed the Host to evil.com but the response throws an error. So I added an additional parameter below the Host parameter that is X-Forwarded-Host with value evil.com, like this:

> Host: target.com
>
> X-Forwarded-Host: evil.com

![]()

And it gave me a 200 OK response which I usually got, but in most of the cases password reset link remains same, as it does not change on the backend. But in this case I got the modified password reset link on my email address with host evil.com :

> [https://evil.com/account/change-password/token=token](https://evil.com/account/change-password/token%3Dtoken)

**Here are some ways you can find Password Reset Poisoning with Host Header Injection:**

>> Try directly changing the password reset request’s Host

> Host: evil.com

>> Or try by adding X-Forwarded-Host

> Host: target.com
>
> X-Forwarded-Host: evil.com

>> Try to add another Host header with different value

> Host: target.com
>
> Host: evil.com

**Steps to Reproduce:**

1. Go to reset password page and enter the email for password reset link.

2. Now intercept the request in Burp Suite and send it to repeater.

3. Add a parameter X-Forwarded-Host below the Host parameter with any host. **(Also try the above techniques mentioned)**

4. If you receive a password reset link from the injected host then you got the bug.

**Impact:**

An attacker can redirect users to a malicious site,which will leak the user’s password reset link/token leading to full account takeover or an attacker can send malware to the user’s system via the malicious link.

**End:**

If you find this writeup helpful then do hit that 👏 clap button multiple times, also don’t forgot to connect with me on [**TWITTER**](https://twitter.com/zingzangoo) and [**LINKEDIN**](https://www.linkedin.com/in/bharat-s1ngh/) to get regular updates.

## Your support means everything to me! If you found my blog valuable and would like to show your appreciation, please consider leaving a tip [HERE](https://www.paypal.me/BHARATS1NGH).

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----345b902a9ca5---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----345b902a9ca5---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page-----345b902a9ca5---------------------------------------)

[Bugbounty Writeup](https://medium.com/tag/bugbounty-writeup?source=post_page-----345b902a9ca5---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--345b902a9ca5---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--345b902a9ca5---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--345b902a9ca5---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--345b902a9ca5---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--345b902a9ca5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Bharat Singh](https://miro.medium.com/v2/resize:fill:96:96/1*SLUmV3MPNVcuzAnQFICGyg.gif)](https://bharat-singh.medium.com/?source=post_page---post_author_info--345b902a9ca5---------------------------------------)

[![Bharat Singh](https://miro.medium.com/v2/resize:fill:128...