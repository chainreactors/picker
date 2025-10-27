---
title: Your Domain, My Playground: Hijacking Your Link Previews ‍
url: https://infosecwriteups.com/your-domain-my-playground-hijacking-your-link-previews-fdca8272bb4e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-09-06
fetch_date: 2025-10-02T19:44:12.605788
---

# Your Domain, My Playground: Hijacking Your Link Previews ‍

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ffdca8272bb4e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fyour-domain-my-playground-hijacking-your-link-previews-fdca8272bb4e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fyour-domain-my-playground-hijacking-your-link-previews-fdca8272bb4e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-fdca8272bb4e---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-fdca8272bb4e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# 🤯🔐 Your Domain, My Playground: Hijacking Your Link Previews 👨‍💻😈

[![Shubhang Borkar](https://miro.medium.com/v2/resize:fill:64:64/1*kfZi6uSEe0GWNshlU7vGhw.png)](https://shubhangborkar.medium.com/?source=post_page---byline--fdca8272bb4e---------------------------------------)

[Shubhang Borkar](https://shubhangborkar.medium.com/?source=post_page---byline--fdca8272bb4e---------------------------------------)

6 min read

·

Aug 21, 2025

--

Listen

Share

**What if an attacker could publish a link on your domain and you had no way to revoke it, leaving it live forever for phishing, scams, or brand abuse?**

Press enter or click to view image in full size

![]()

Non-member? [Click to read for free](https://shubhangborkar.medium.com/fdca8272bb4e?sk=6ca79d1b816f5b168a4561495477e6c1).

In my previous blog, [Your Domain, My Playground: How I Created Links on Your Site Without Permission](/your-domain-my-playground-how-i-created-links-on-your-site-without-access-9a77b712ac31), I revealed how attackers could generate shortened URLs on any Firebase-connected domain**.** This allowed them to create links that looked legitimate but redirected users to attacker-controlled sites, all without touching the domain owner’s servers.

Following that disclosure, Google introduced an important mitigation by strongly encouraging project owners to configure an “Allowed Domains” list, prominently highlighting it in the Firebase console, sending reminder emails, and urging adoption to limit which domains shortened links can redirect to. While not mandatory, this significantly helped reduce attackers’ ability to arbitrarily redirect users to malicious external sites.

But does that mean the problem is solved? Unfortunately… no. It’s like locking the front door while leaving the windows wide open.

## What Exactly Are Firebase Dynamic Links?

Firebase Dynamic Links (FDL) are more than just URL shorteners. They’re designed to provide a seamless experience when sharing links that open in mobile apps or websites, with support for “deep linking” directly into specific app content.

Beyond simply redirecting URLs, FDL allows developers to **attach metadata** to each link. This metadata can include:

* A **title** (headline shown in link previews)
* A **description** (summary text)
* A **thumbnail image** (preview picture)

This metadata is what you see when a link is shared in messaging apps, social media feeds, or browsers. It makes links more attractive, informative, and trustworthy to users.

![]()

Metadata when you share a canva.com link

## **The Dark Side of Link Metadata**

Even with an Allowed Domains list in place, I could still create links on your domain that point to any site within that list. At first, that might not sound dangerous. After all, it’s an approved destination. But what if I could make that link preview look like something completely different?

Here’s where it gets interesting. If I can create short links **on your domain** (thanks to it being on your Allowed Domains list) *and* set my own metadata, I can make that link look like anything I want, even if the actual destination is completely safe and hosted by you.

Imagine you get a link in WhatsApp, LinkedIn, or Slack that looks like this:

![]()

Sample image with Metadata

* The title says: ***“*Independence Day Offer — Book today & Get Full Refund*”***
* The description reads: ***“*Only for today. Explore breathtaking Switzerland at Zero Cost. First 100 customers only*”***
* The thumbnail: **A stunning picture of the Swiss Alps with the MakeMyTrip logo placed in the corner, just like an official promo banner.**
* The URL shows your domain: **makemytrip.com**

*Note: MakeMyTrip is just a stand-in for this demonstration. In reality, they don’t use Firebase Dynamic Links and weren’t vulnerable. The example is only to help you visualise how this could play out.*

Everything checks out. The link? Not some random xyz.com. It’s makemytrip.com. Looks safe enough… right?

You click it and, just as promised, it takes you to the real MakeMyTrip website, even opens the app if installed. It all looks legitimate. The Switzerland package is right there.

You pay lakhs for the dream holiday, confident you’ll get the full refund as advertised. You wait a day, a week… nothing. Finally, you call customer support, only to hear the chilling words:

> *“Sir, we don’t have any such offer. That link didn’t come from us.”*

The payment went directly to MakeMyTrip, but the false promise in the preview was enough to trick you into making the purchase.

And it’s not just about fake travel deals. The same trick works on other major platforms too, even Google’s own apps that use Dynamic Links, like Google Maps.

I created a link that opens the Google Maps Timeline app on Android with a customised title and image. This is a real example generated on the Google Maps domain.

![]()

Imagine the damage. Not just fake offers, but scathing headlines or fabricated news plastered right under the company’s own domain. One click, and the brand’s trust can crumble, even though the site itself is doing nothing wrong. The attacker controls the story. The company only finds out once the reputational fire has already started burning.

## **So, how would I even know if someone is misusing my domain?**

You might think, *“Well, I can just check my Firebase Dynamic Links dashboard. If someone’s creating shady links on my domain (or maybe even did so in the past before I set up allowed domains), I’ll see them there, right?”*

Wrong.

The Dynamic Links console only shows links that **you** create from the console itself. Any links generated through the API, which is exactly how an attacker would do it, never show up there.

In other words, you could have dozens of malicious links floating around on your verified domain, and you’d have **no clue** unless you stumble upon them by accident.

Here is a screenshot of my console where I have c...