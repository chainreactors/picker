---
title: How I Found an Email Verification Bypass on an AI Freelance Platform
url: https://infosecwriteups.com/how-i-found-an-email-verification-bypass-on-an-ai-freelance-platform-6ad76663b658?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-01
fetch_date: 2026-07-02T05:56:47.223583
---

# How I Found an Email Verification Bypass on an AI Freelance Platform

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-an-email-verification-bypass-on-an-ai-freelance-platform-6ad76663b658&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-an-email-verification-bypass-on-an-ai-freelance-platform-6ad76663b658&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-6ad76663b658---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-6ad76663b658---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# How I Found an Email Verification Bypass on an AI Freelance Platform

[![Hangga Aji Sayekti](https://miro.medium.com/v2/resize:fill:64:64/1*Sv16cditVCn4Wdh76amCEg.png)](https://hangga-aji-sayekti.medium.com/?source=post_page---byline--6ad76663b658---------------------------------------)

[Hangga Aji Sayekti](https://hangga-aji-sayekti.medium.com/?source=post_page---byline--6ad76663b658---------------------------------------)

7 min read

·

19 hours ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D6ad76663b658&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-an-email-verification-bypass-on-an-ai-freelance-platform-6ad76663b658&source=---header_actions--6ad76663b658---------------------post_audio_button------------------)

Share

*A simple implementation flaw allowed email verification to be completed without ever opening the verification email.*

Press enter or click to view image in full size

![]()

A few weeks ago, I was browsing LinkedIn looking for freelance opportunities when I came across an AI-powered platform looking for freelancers. The platform looked interesting, so I decided to create an account and see how everything worked.

Press enter or click to view image in full size

![]()

This wasn’t a bug hunting session. I was simply signing up as a normal user.

That said, I have one habit that’s hard to get rid of.

Whenever I register on a new website, I usually keep Chrome DevTools open and watch the network traffic. It’s something I’ve been doing for years, partly out of curiosity and partly because it helps me understand how an application is built.

Sometimes I don’t find anything interesting.

Sometimes I learn how the application works.

And occasionally… I find something the developers didn’t intend.

This turned out to be one of those occasions.

## Responsible Disclosure

Before we dive into the technical details, here’s a quick note.

I responsibly reported this issue to the platform’s security team. The report was acknowledged, and the issue has since been fixed.

Press enter or click to view image in full size

![]()

To avoid exposing the affected platform, I’ve redacted its name, domain, screenshots, and any other identifying information throughout this article.

Interestingly, while investigating this issue, I also came across another security weakness. That’s a story for another day.

## Looking at the Registration Flow

For the registration, I used a temporary email address. I usually do this when trying a new service, especially if I’m not sure whether I’ll continue using it.

Before clicking **Sign Up**, I opened Chrome DevTools and switched to the **Network** tab.

More specifically, the **Fetch/XHR** requests.

Once the registration completed, I started reviewing the requests and responses generated by the application.

Most of the traffic looked exactly as I’d expect.

The registration request returned basic account information, a few status fields, and something else.

Press enter or click to view image in full size

![]()

The `token` value was clearly a JWT.

At this point, nothing looked particularly suspicious.

Many modern applications automatically authenticate users immediately after registration, so returning a JWT isn’t unusual. Depending on the application’s architecture, it can be a perfectly valid design choice.

I simply made a mental note of it and continued observing the registration flow.

A few seconds later, the verification email arrived.

Press enter or click to view image in full size

![]()

Like most verification emails, it contained a button that pointed to a URL similar to this:

```
https://[REDACTED]/verify-email?token=<JWT>
```

Again, nothing unusual.

Until I looked a little closer.

The token inside the verification URL looked very familiar.

I went back to the registration response, copied both values, and compared them.

They were exactly the same.

Press enter or click to view image in full size

![]()

That immediately raised a simple question.

> ***If I already have this token from the registration response, do I actually need the verification email?***

The only way to answer that question was to test it.

So I registered another account.

## Testing the Hypothesis

Rather than clicking the verification link from the email, I decided to repeat the registration process using another temporary email address.

The goal was simple.

Could I verify the account **without ever opening the verification email?**

After registering the second account, I watched the registration response again and copied the JWT returned by the API.

This time, I completely ignored the inbox.

Instead, I manually constructed the verification URL using the same format I had seen in the email.

```
https://[REDACTED]/verify-email?token=<JWT>
```

I pasted the URL into the browser and pressed **Enter**.

The account was verified immediately.

Press enter or click to view image in full size

![]()

At that point, the hypothesis was confirmed.

The verification email wasn’t actually required.

As long as the registration response exposed the same JWT used by the verification endpoint, anyone registering an account already possessed everything needed to verify it.

The email merely contained information the client had already received.

## Why This Happened

It’s important to point out that the problem wasn’t JWT itself.

JWT (JSON Web Token) is widely used across modern web applications for authentication and securely transmitting signed information between systems.

Returning a JWT after registration is also not inherently insecure. Many applications automatically sign users in immediately after creating an account.

The issue here was much simpler.

The application reused the same token for two different purposes.

The JWT returned by the registration API was also accepted by the email verification endpoint.

As a result, the verification email stopped ...