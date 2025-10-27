---
title: JWT Authentication Bypass leads to Admin Control Panel
url: https://infosecwriteups.com/jwt-authentication-bypass-leads-to-admin-control-panel-dfa6efcdcbf5?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-10-28
fetch_date: 2025-10-06T18:48:00.857066
---

# JWT Authentication Bypass leads to Admin Control Panel

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fdfa6efcdcbf5&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fjwt-authentication-bypass-leads-to-admin-control-panel-dfa6efcdcbf5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fjwt-authentication-bypass-leads-to-admin-control-panel-dfa6efcdcbf5&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-dfa6efcdcbf5---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-dfa6efcdcbf5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# JWT Authentication Bypass leads to Admin Control Panel

[![Hohky](https://miro.medium.com/v2/resize:fill:64:64/1*mQc4HKPJno__5LkmgFIjLg.png)](https://medium.com/%40hohky_?source=post_page---byline--dfa6efcdcbf5---------------------------------------)

[Hohky](https://medium.com/%40hohky_?source=post_page---byline--dfa6efcdcbf5---------------------------------------)

3 min read

·

Oct 14, 2024

--

2

Listen

Share

🍪From a simple cookie it became a benchmark and then an Accont takeover 😈

➡️For legal reasons, I will not reveal the website or the Bug Bounty program.

I found this vulnerability about a few months ago, it was a “simple” mistake that I managed to access the Admin panel of a very well-known site. And I have permission to publish this…

## What is a JWT? (Resume)

For those who don’t know, the **JWT** (*JSON Web Token*) is an authentication method widely used for authentication, formerly cookies (still used) but usually a JWT is more common, they can be accompanied (and should all be) with a signature that is signed by the server, and it is this signature that validates that the JWT is in fact valid

Press enter or click to view image in full size

![]()

JWT Format

* **Header**: Defines the type of token and the signature algorithm.
* **Payload**: Contains valuable information such as authentication information
* **Signature**: Signs the token using a secret key that the server uses to validate it.

Normally a JWT comes encoded in base64…

```
eyJzdWIiOiAiMTIzNDU2Nzg5MCIsICJuYW1lIjogIkpvaG4gRG9lIiwgImVtYWlsIjogImpvaG5kb2VAZXhhbXBsZS5jb20iLCAiYWRtaW4iOiB0cnVlLCAiaWF0IjogMTYwOTQ1OTIwMH0
```

Decoded (from the example above):

```
{
  "sub": "1234567890",
  "name": "John Doe",
  "email": "johndoe@example.com",
  "admin": true,
  "iat": 1609459200
}
```

You’re probably wondering what could be done… If someone changed something like that. But that’s where it gets complicated, because the server, as I said, checks by subscription.

Let’s get practical!

### The question of the day is… Is it still possible for something as basic as a JWT to be vulnerable in 2024?

When you enter our domain, you usually get a “default” ID, such as guest or anonymous, which is to be expected…

> GET https://www.example.com/

Press enter or click to view image in full size

![]()

Response

No JWT comes, normal, we’re not logged in or anything that needs a JWT

But of course the server would start tagging us with something…

```
<script>var atlasCode = "eyJhIjo5NDk2LCJjIjo0NDQ3MzM2NCwibiI6MjEsInMiOjI0MSwiZSI6ODUzLCJwIjozfQ==";</script>
```

This isn’t for authentication, it’s more to track where the user is, on which page, more like a tracker…

## Here it begins

After I created an account, a cookie was set to validate that I am me because I am me.

```
Set-Cookie: MDH=%21eyJvX2dlbmRlciI6IkEiLCJpc0xvZ2dlZCI6Im4iLCJscGFnZWlkIjo3LCJra0lEIjo4OTg3NiwibGFuZyI6InVzIiwibGFuZCI6ImRlIiwiU0lEIjoiMCIsIkNPTiI6IjE0MTYwMTAwMCIsIkxPR0lOIjoiaiIsIk1ESF9VX0lEIjoiMTMwOTgyMDUxIiwibmljayI6ImhvaGt5dGVzdCIsImVtYWlsIjoiaG9oa3lAYnVnY3Jvd2RuaW5qYS5jb20iLCJnZW5kZXIiOiJNIiwiTE9HSU5USU1FIjoxNzI4OTA4MzY3fQ%3D%3D%24f46a10d0ab6db8eebcd4c7afac6a4d332be8b4bf;
```

Let’s make it simple… 🥸

Using a tool from [Burp Suite](https://portswigger.net/bappstore/f923cbf91698420890354c1d8958fee6), I can visualize what’s in the JWT more clearly:

![]()

JWT Decoded

I can’t just change a parameter like ‘*u\_id’* because that will change the JWT and the **signature won’t be valid.**

**The signature is valid. If I don’t change it.**

Press enter or click to view image in full size

![]()

On the right-hand side, I have a few attacks to try out and a ***simple change*** like changing the nickname and the “*u\_id*”…

![]()

**THE JWT KEEP VALID!!!**

I did an admin action with no real impact on the server or users, just on me, and it worked…

![]()

It’s my ID

Press enter or click to view image in full size

![]()

The body of request & response

## Conclusion

I apologize that the post was very illustrated and lacked technical details. 😪

I hope I’ve helped someone or reminded them that something simple is still valid!

🫠Changes to a JWT can make a difference, such as not adding an algorithm, as in this vulnerability.

[Hacking](https://medium.com/tag/hacking?source=post_page-----dfa6efcdcbf5---------------------------------------)

[Bug Bounty Writeup](https://medium.com/tag/bug-bounty-writeup?source=post_page-----dfa6efcdcbf5---------------------------------------)

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page-----dfa6efcdcbf5---------------------------------------)

[Account Takeover](https://medium.com/tag/account-takeover?source=post_page-----dfa6efcdcbf5---------------------------------------)

[Jwt Token](https://medium.com/tag/jwt-token?source=post_page-----dfa6efcdcbf5---------------------------------------)

--

--

2

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dfa6efcdcbf5---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--dfa6efcdcbf5---------------------------------------)

Follow

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--dfa6efcdcbf5---------------------------------------)

[71K followers](/followers?source=post_page---post_publication_info--dfa6efcdcbf5---------------------------------------)

·[Last published 3 hours ago](/baby-dfc2547dc387?source=post_page---post_publication_info--dfa6efcdcbf5---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to...