---
title: SameSite Lax Bypass through Method Override | 2023
url: https://infosecwriteups.com/samesite-lax-bypass-through-method-override-2023-46fa30535410?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-11
fetch_date: 2025-10-04T06:20:06.769920
---

# SameSite Lax Bypass through Method Override | 2023

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F46fa30535410&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsamesite-lax-bypass-through-method-override-2023-46fa30535410&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fsamesite-lax-bypass-through-method-override-2023-46fa30535410&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40cyberw1ng)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-46fa30535410---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-46fa30535410---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# SameSite Lax Bypass through Method Override | 2023

## Portswigger’s CSRF lab Simple Solution | Karthikeyan Nagaraj

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/da:true/resize:fill:64:64/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---byline--46fa30535410---------------------------------------)

[Karthikeyan Nagaraj](https://cyberw1ng.medium.com/?source=post_page---byline--46fa30535410---------------------------------------)

3 min read

·

Feb 9, 2023

--

Listen

Share

Press enter or click to view image in full size

![]()

### Lab Description:

* This lab’s change email function is vulnerable to CSRF. To solve the lab, perform a CSRF attack that changes the victim’s email address.
* You should use the provided exploit server to host your attack.
* You can log in to your own account using the following credentials: `wiener:peter`

### Note

The default [SameSite](https://portswigger.net/web-security/csrf/bypassing-samesite-restrictions) restrictions differ between browsers. As the victim uses Chrome, we recommend using Chrome (or Burp’s built-in Chromium browser) to test your exploit.

### Analysis:

1. Go to My-Account and Log In to the account with the above credentials and change your email address.
2. Send the `POST /my-account/change-email` request to Burp Repeater.

Press enter or click to view image in full size

![]()

3. Study the `POST /my-account/change-email` request and notice that this doesn't contain any unpredictable tokens so may be vulnerable to CSRF if you can bypass the SameSite cookie restrictions.

![]()

4. Look at the response to your `POST /login` request. Notice that the website doesn't explicitly specify any SameSite restrictions when setting session cookies. As a result, the browser will use the default `Lax` restriction level.

![]()

5. Recognize that this means the session cookie will be sent in cross-site `GET` requests, as long as they involve top-level navigation.

6. In Burp Repeater, right-click on the request and select **Change request method**. Burp automatically generates an equivalent `GET` request.

![]()

7. Send the request. Observe that the endpoint only allows `POST` requests.

8. Try overriding the method by adding the `_method` parameter to the query string:

`/my-account/change-email?email=foo%40web-security-academy.net&_method=POST`

9. Send the request. Observe that this has been accepted by the server.

Press enter or click to view image in full size

![]()

10. In the browser, go to the exploit server.

11. In the **Body** section, create an HTML/JavaScript payload that induces the viewer’s browser to issue the malicious `GET` request. Remember that this must cause top-level navigation in order for the session cookie to be included. The following is one possible approach:

`<script> document.location = "https://YOUR-LAB-ID.web-security-academy.net/my-account/change-email?email=pwned@web-security-academy.net&_method=POST"; </script>`

12. Store and view the exploit yourself. Confirm that this has successfully changed your email address on the target site.

Press enter or click to view image in full size

![]()

13. Deliver the exploit to the victim to solve the lab

Press enter or click to view image in full size

![]()

Feel Free to Ask Queries via [LinkedIn](https://www.linkedin.com/in/karthikeyan-nagaraj) and to Buy me Coffee : )

Thank you for Reading!!

Happy Hunting ~

```
Author: Karthikeyan Nagaraj ~ Cyberw1ng
```

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----46fa30535410---------------------------------------)

[Csrf](https://medium.com/tag/csrf?source=post_page-----46fa30535410---------------------------------------)

[Portswigger](https://medium.com/tag/portswigger?source=post_page-----46fa30535410---------------------------------------)

[Hacking](https://medium.com/tag/hacking?source=post_page-----46fa30535410---------------------------------------)

[Web](https://medium.com/tag/web?source=post_page-----46fa30535410---------------------------------------)

--

--

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--46fa30535410---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--46fa30535410---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--46fa30535410---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--46fa30535410---------------------------------------)

·[Last published 5 days ago](/how-to-find-p1-bugs-using-google-in-your-target-part-1-e37455324dc1?source=post_page---post_publication_info--46fa30535410---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/resize:fill:96:96/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---post_author_info--46fa30535410---------------------------------------)

[![Karthikeyan Nagaraj](https://miro.medium.com/v2/resize:fill:128:128/1*MQN6JztXVcWsGNXCfJGlgw.gif)](https://cyberw1ng.medium.com/?source=post_page---post_author_info--46fa30535410---------------------------------------)

[## Written by Karthikeyan Nagaraj](https://cyberw1ng.medium.com/?source=post_page---post_author_info--46fa30535410---------------------------------------)

[12.8K followers](https://cyberw1n...