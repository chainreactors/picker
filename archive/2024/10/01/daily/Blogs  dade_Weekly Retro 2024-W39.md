---
title: Weekly Retro 2024-W39
url: https://0xda.de/blog/2024/09/weekly-retro-2024-w39/
source: Blogs  dade
date: 2024-10-01
fetch_date: 2025-10-06T18:51:50.596598
---

# Weekly Retro 2024-W39

[>
cd /0xda.de/](https://0xda.de/)

[ ]

* [About](https://0xda.de/about/)
* [Blog](https://0xda.de/blog/)
* [Garden](https://0xda.de/garden/)
* [Speaking](https://0xda.de/speaking/)
* [Music](https://0xda.de/music/)
* [Consulting](https://room641a.com)
[Tor](http://dadehacks5p4qrui2wy2bcfp37wgtycysqhxuwa2o7k2t34rryrzhdqd.onion/blog/2024/09/weekly-retro-2024-w39/ "Tor")

[0xdade](https://0xda.de/)
![Photo of the site's author](https://0xda.de/img/dade-transparent-logo.png)

Seasonal Influencer. Python dev, security engineer, former red team, former SSD engineer. Hacker, rapper, writer. he/him

6 minutes

# [Weekly Retro 2024-W39](https://0xda.de/blog/2024/09/weekly-retro-2024-w39/)

---

* [One Week an iPhone User](#one-week-an-iphone-user)
* [MFA and Password Managers](#mfa-and-password-managers)
* [Sephiroth](#sephiroth)
* [CFP Submission](#cfp-submission)
* [Interesting Links](#interesting-links)
* [Upcoming Projects](#upcoming-projects)

---

I spent the week getting familiar with my iPhone, writing about the relationship between MFA and Password Managers, identified a few areas for improvement for Sephiroth, and submitted to a CFP.

## One Week an iPhone User

I’ve been using my iPhone for a week now, and I have a few thoughts. In no particular order:

* The notification customization capabilities are great, but somehow fall short in a way that I feel like is obvious. The most apparent example of this, for me, was the Twitter app. I want notifications when I get DMs, and no other time. But the badge was still showing up even when I had likes or replies, because the badge isn’t a “push notification” in the Twitter configuration. I ended up just turning the badge off for Twitter altogether.
* I got woken up yesterday morning because my phone vibrated. It was in bedtime focus, but apparently you have to explicitly say “No notifications from any apps” separately from listing the people you will accept notifications from. This appears to have been user error on my part, but I kinda like Android’s bedtime mode better.
* The general idea of Focus modes is great, way more customizable than Android.
* I turned on Advanced Data Protection and it was pretty easy. I think it’s pretty neat that they have a mechanism for recovery contacts to help you recover access if you get locked out.
* I love how fine grained a lot of the permission controls can be, even if it was kind of annoying to get things setup the first time.
* My Tailscale connectivity seems way more reliable than it was on my Pixel 5a. I haven’t had an issue with it all week, whereas on my old phone, if I left Tailscale on and switched between cellular and WiFi, it would often cause DNS errors that resulted in no internet access for most apps until I cycled Tailscale.
* I like that I can sync photos to iCloud, Google, and my Synology all automatically.
* Overall apps feels generally more polished, with the one exception being that Brave for iOS doesn’t have tab groups. Tab groups are great, get it together.
* It was easy to set my default password manager experience to 1Password and disable the Passwords app from getting in the way.

## MFA and Password Managers

I wrote this week about [MFA and your Password Manager](https://0xda.de/blog/2024/09/mfa-and-your-password-manager/). TL;DR is that the threats they are designed to mitigate against are pretty similar, and that I no longer think it’s so bad to store 2FA tokens in your password manager vault. If you’re more likely to turn on 2FA because it works well with your password manager, that’s considerably better than just not turning it on.

But you should still use strong 2FA like a yubikey to protect access to sensitive accounts like your Google, Apple, Microsoft accounts, as well as to protect access to your password manager itself.

## Sephiroth

[Sephiroth](https://github.com/0xdade/sephiroth) is an old project of mine from my red team days, the primary purpose of which is to make it easy to create blocklists or allow lists for whole classes of IP addresses. Examples might be “I want to block all of AWS with nginx” or “I want to block all Tor exit nodes with iptables.” It’s called Sephiroth because it’s The Cloud Blocker.

I was helping someone this week and Sephiroth seemed like a useful tool for them, at least in part. Sephiroth is broken up into two main components - the provider and the template. Providers contain the logic needed to fetch all of the IP addresses for a given cloud provider (as well as ASN lookups, files containing IP ranges, and Tor exit nodes), and templates convert that standardized data into the format needed for whatever software you want to use it with. So if you wanted an example of how to programmatically fetch all the IP ranges for AWS, Google, Azure, etc, you could just go look at the corresponding Sephiroth provider.

Offering up help got me to go look at some other places that might publish their IP ranges, and I identified three potential candidates and created new issues for them. [Salesforce](https://github.com/0xdade/sephiroth/issues/84), [IBM Cloud](https://github.com/0xdade/sephiroth/issues/83), and [Vultr](https://github.com/0xdade/sephiroth/issues/82).

These are probably of mixed value, but if nothing else, I can capture information about how to find those IP ranges.

## CFP Submission

I submitted to a CFP for a private conference this week. I don’t want to describe the CFP topic just yet, but it is related to some of the writing I’ve done this year. I think I’d also like to submit the talk to (the final) Shmoocon, but want to flesh it out a bit further first.

## Interesting Links

* [PyPDF’s Succession Planning](https://pypdf.readthedocs.io/en/stable/meta/taking-ownership.html) - I was looking at PyPDF’s documentation for a small project I was helping someone with, and noticed they have this page outlining how to take ownership of the project if something should happen to the maintainer. Thsi is a really smart thing to do, and I wish more projects did it.
* [Alan Kay on Messaging (1998)](https://wiki.c2.com/?AlanKayOnMessaging) - I may have a more unique experience with this than a lot of folks, but my objects professor taught us entirely in Smalltalk, and really drove messaging as the magic of object oriented programming from my very first introduction to the concept. It’s worth reading this brief email. Also one time I changed a base class in my Smalltalk project for school which accidentally rendered the whole UI unable to do anything and I had to start from scratch. So pros and cons of your development environment also being your runtime environment, I guess.
* [A Taxonomy of Tech Debt](https://technology.riotgames.com/news/taxonomy-tech-debt) - Riot Games with a blog post from 2018 about a model for discussing tech debt. The idea of “contagion” is fantastic and something that I’ve been proactive about at work, even though I didn’t have a good name for it until now. Well-contained tech debt is easy to postpone work on. Poorly-contained tech debt needs to be addressed before it infects every design and development decision.
* [Windows Recall gets a rearchitect](https://blogs.windows.com/windowsexperience/2024/09/27/update-on-recall-security-and-privacy-architecture/) - I still am not interested in using it, but I’m glad to see they went back to the drawing board on this one and came back with something less laughable.
* [LaurieWired talks about EPSS](https://x.com/lauriewired/status/1839410977814790406) - I’d not really considered alternate scoring systems before, but Laurie has a thread outlining the benefits of using this alternate scoring system and how it can be more efficient.
* [What Public Health Can Teach Us About How to Give Better Security Advice](https://free-dissociation.com/blog/posts/2017/04/public-health-and-security-advice/) - I think more of the security community needs to look outside of itself to get more insight on how we should approach problems. Security within a larger s...