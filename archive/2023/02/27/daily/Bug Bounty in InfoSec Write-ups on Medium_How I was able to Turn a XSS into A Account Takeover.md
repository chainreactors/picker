---
title: How I was able to Turn a XSS into A Account Takeover
url: https://infosecwriteups.com/how-i-was-able-to-turn-a-xss-into-a-account-takeover-ae0c478640e7?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2023-02-27
fetch_date: 2025-10-04T08:10:39.905740
---

# How I was able to Turn a XSS into A Account Takeover

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fae0c478640e7&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-was-able-to-turn-a-xss-into-a-account-takeover-ae0c478640e7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-was-able-to-turn-a-xss-into-a-account-takeover-ae0c478640e7&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ae0c478640e7---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ae0c478640e7---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I was able to Turn a XSS into a Account Takeover

[![Josh Fam](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)](https://pullerjsecu.medium.com/?source=post_page---byline--ae0c478640e7---------------------------------------)

[Josh Fam](https://pullerjsecu.medium.com/?source=post_page---byline--ae0c478640e7---------------------------------------)

6 min read

·

Feb 3, 2021

--

2

Listen

Share

Press enter or click to view image in full size

![]()

To begin,this is a vulnerability that I found during a bug bounty engagement.I would split this into two parts, or two separate vulnerabilities. The First part was a web cache poisoning via X Headers.This part allowed me to achieve XSS on every endpoint with a combination of two Headers.The next part was a OAuth flow flaw that allowed me to leverage my previously given XSS capabilities into an account takeover through a technique I call cookie overriding.Before I begin explaining this exploit chain, I have to say that since this is a private program I can’t disclose the site that it was found on.

Web Cache Poisoning:

This vulnerability is well documented on Portswigger by James Kettle, and this is where I had first heard about it, so for a more in-depth introduction I recommend reading that article.However for a quick primer,web cache poisoning is a vulnerability that allows an attacker to poison a HTTP response by injecting malicious code into a non keyed HTTP request header. A web cache is basically a way for websites to lower the load on their servers by replaying resources to users without asking the server multiple times.They look for specific keys in the the HTTP request to determine if they have already cached the resource and if they have, that’s what any user that matches that request gets served.These cache keys could be anything ranging from the URI to the Accept HTTP request headers.However there are certain HTTP request headers that are not keyed and can introduce reflected output onto a HTTP response depending on the code implemented. A popular one and the one that’ll be exploited in this report is the X-Forwarded-Host header.This header can populated with a XSS payload and used to reflect a XSS payload into a HTTP response. After the cache gets this response and saves it without the unkeyed header, you can consider the cache poisoned and it will pass the response to every user that visits that URL.That’s the basis of the attack, but this can be supplemented with another unkeyed header to increase the severity so that you can poison the cache for every URL on the site. This Header is the X-Rewrite-Url header, and this basically rewrites the URN that is being cached. So lets say the URN in a HTTP request is /home, the cache thinks its saving this HTTP response. But if you add the X-Rewrite-Url header, it’ll actually load the malicious HTTP response at /evil.The header is usually unkeyed so it’ll serve the poisoned response to any user that requests for /home.

Press enter or click to view image in full size

![]()

The Exploit Chain(part 1):

What happened is that I found a site that supports both of these headers and had a page that reflected the X-Forwarded-Host header in a JavaScript variable on one of its pages.Using the combination of the X-Forwarded Host and the X-Rewrite-Url headers I was able to gain XSS on every page on the site without user interaction.However it was really only cached for about 3 minutes.To increase the severity I made a script to automate the poisoning, stating that I could just poison the home page endpoint every 3 minutes to infect every user that visits the site.However the team that the report was submitted to wanted to keep it a medium severity.This wasn’t something I was trying to see so I went looking for another way to increase the severity. Which leads me to the second portion of this post, an Account takeover due to a flaw in their Oauth Flow.

OAuth Flow Flaw:

If you not familiar with OAuth, this section will cover the flow of an Authorization Grant which was the grant used in this case. There are four major entities to this grant,the Application,the User, the Authorization server and the Resource Provider.The first step is the User requests access to a Resource.The Application or OAuth Client sees this request and redirects the user to the Authorization server.The User validates their credentials with the Authorization server and if approved, gets an access code. After this the User is redirected back to the application and the client takes this access code.The Application then takes this code and validates it with the Authorization server and finally gets an access token. This access token is used to retrieve data from the Resource Provider on behalf of the user. The issue on this site was after the code was sent back it was processed by an URL which took a value in a cookie that was another trusted OAuth callback URL and appended the code to the end of this url after a hash fragment and redirected the browser to this location.This allows for anyone that changes the cookie value to redirect the code to an arbitrary location.After that the attacker could just submit the code to the Authorization server and get a access token on behalf of the targeted user.

Press enter or click to view image in full size

![]()

Cookie Overriding: Normally this wouldn’t be a issue due to two factors,the cookie was HTTPOnly and number two, the URL in the cookie was whitelisted to only trusted sites.The second problem was already solved in my case, since the cache poisoning XSS was already on a trusted subdomain. The first problem was the problem that had to get solved.How do you use a XSS to change a cookie value that’s HTTPOnly? The answer is that you don’t, you make a cookie that looks like the HTTPOnly cookie, and set the path parameter to a certain URN where the cookie was being used.If a browser sees two cookies of the same ...