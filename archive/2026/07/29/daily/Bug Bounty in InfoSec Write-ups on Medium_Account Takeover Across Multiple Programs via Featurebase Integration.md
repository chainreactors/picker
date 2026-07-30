---
title: Account Takeover Across Multiple Programs via Featurebase Integration
url: https://infosecwriteups.com/account-takeover-across-multiple-programs-via-featurebase-integration-32214666123e?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-07-29
fetch_date: 2026-07-30T04:51:11.760821
---

# Account Takeover Across Multiple Programs via Featurebase Integration

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccount-takeover-across-multiple-programs-via-featurebase-integration-32214666123e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccount-takeover-across-multiple-programs-via-featurebase-integration-32214666123e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-32214666123e---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-32214666123e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Bug Bounty

Bugbounty Writeup

Bug Bounty Tips

Bug Bounty Writeup

Account Takeover

# Account Takeover Across Multiple Programs via Featurebase Integration

[![JEETPAL](https://miro.medium.com/v2/resize:fill:64:64/1*3UJihM4VvA-DeZOgGnYqLg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---byline--32214666123e---------------------------------------)

[JEETPAL](https://jeetpal2007.medium.com/?source=post_page---byline--32214666123e---------------------------------------)

3 min read

·

23 hours ago

--

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D32214666123e&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Faccount-takeover-across-multiple-programs-via-featurebase-integration-32214666123e&source=---header_actions--32214666123e---------------------post_audio_button------------------)

Share

In this blog, I am going to share an account takeover vulnerability in a third-party provider widely used by many bug bounty programs.

I discovered this issue during a bug bounty engagement in October 2025. I discovered an IDOR leading to Account Takeover (ATO) in a third-party provider that works with many organizations.

before this Let me clear the concept first:

The provider is: <https://featurebase.app/>

Featurebase provides a feedback and feature request platform used by many organizations.

The common way to figure out if your target is using this provider or not is by visiting the following subdomain on target

```
feedback.example.com
```

You can identify many deployments using Google dorks or Shodan

```
site:feedback.*.*
```

This is how the page will look

Press enter or click to view image in full size

![]()

Feedback vulnerable page

Now the Question arises how we are going to exploit this vulnerability.

**Step 1 (Via IDOR)**

* We have to register an account on any target `feedback.example.com`
* Check for the following endpoints

```
POST /api/v1/user/identify
```

and also, in request body it should be

```
{
  "organization":"example",
  "email":"victim@example.com",
  "name":"Jeet Pal",
  "userId":"733244",
  "profilePicture":"https://..."
}
```

Here we have to modify the `userId` for the someone else to takeover account via email change functionality.

## Get JEETPAL’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

In response then you can view the Email changed after that you can ask for reset password and then takeover the account.

( it was consider as medium due to third party)

Press enter or click to view image in full size

![]()

After this I got to know about that if we just change the name from the Setting page or make a request towards the following path

```
POST /api/v1/user (during account modification)
```

We can have the access token of the user too. which you can use to make a request for modify the settings at

```
PATCH /api/v1/user
```

From here you have the access token of user and takeover the account too.

Currently the vulnerability is not totally being fixed via feature base as their reply was this is not our issue instead it should be fix by websites owner. but here is alternative path which feature base provide to secure the site using JWT you can read more about them here [Secure your installation (required by default) — Featurebase](https://help.featurebase.app/en/articles/5402549-secure-your-installation-required-by-default)

**Root Cause**

The application trusted client-controlled identity attributes without validating whether the supplied `userId` actually belonged to the authenticated user. This allowed an attacker to impersonate another Featurebase account.

New articles Dropping soon

**Connect with me**
**Linkedin**: <https://www.linkedin.com/in/jeet-pal-22601a290/>
**Instagram:** <https://www.instagram.com/jeetpal.2007/>
**X/Twitter:** <https://x.com/Mr_mars_hacker>

## And here’s something special for you! 🚨

Join a community of 40**00+ security researchers** on our **Discord server**, where we discuss **Web3 vulnerabilities, audits, and much more!** 🚀
👉 **Join the server here! :** <https://discord.gg/Y467qAFM4X>

Bug Bounty

Bugbounty Writeup

Bug Bounty Tips

Bug Bounty Writeup

Account Takeover

--

--

1

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:96:96/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--32214666123e---------------------------------------)

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:128:128/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_info--32214666123e---------------------------------------)

[## Published in InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---post_publication_info--32214666123e---------------------------------------)

[87K followers](/followers?source=post_page---post_publication_info--32214666123e---------------------------------------)

·[Last published 21 hours ago](/how-i-hacked-a-video-game-vault-and-found-the-hidden-flag-924fc1a47053?source=post_page---post_publication_info--32214666123e---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![JEETPAL](https://miro.medium.com/v2/resize:fill:96:96/1*3UJihM4VvA-DeZOgGnYqLg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--32214666123e---------------------------------------)

[![JEETPAL](https://miro.medium.com/v2/resize:fill:128:128/1*3UJihM4VvA-DeZOgGnYqLg.jpeg)](https://jeetpal2007.medium.com/?source=post_page---post_author_info--32214666123e---------------------------------------)

[## Written by JEETPAL](https://jeetpal2007.medium.com/?source=post_pa...