---
title: How I Hacked McDonald's (Their Security Contact Was Harder to Find Than Their Secret Sauce Recipe)
url: https://bobdahacker.com/blog/mcdonalds-security-vulnerabilities
source: Over Security - Cybersecurity news aggregator
date: 2025-08-23
fetch_date: 2025-10-07T00:49:58.617802
---

# How I Hacked McDonald's (Their Security Contact Was Harder to Find Than Their Secret Sauce Recipe)

[bobdahacker](/)

☰

* [home](/)
* [blog](/blog)

# How I Hacked McDonald's (Their Security Contact Was Harder to Find Than Their Secret Sauce Recipe)

August 17, 2025

BobDaHacker

*They fixed the vulnerabilities after I literally had to cold-call their HQ pretending to know security employees. This is that story.*

## It Started With Free Nuggets

So I found out the McDonald's app wasn't checking server-side if you actually had enough reward points. Just client-side validation. I immediately tried to report it.

That turned into a whole saga. I managed to reach a software engineer who said he was "too busy" to take my report and would find someone else. I told him it was something for free food, so I guess he looked at the code and figured it out himself. The bug got fixed days later. Maybe he passed it along, maybe he fixed it himself - but at least it got patched.

## Then The Real Hunt Began

After that experience, I kept digging. And McDonald's security was... interesting.

### The Design Hub Situation

[The McDonald's Feel-Good Design Hub](https://design.mcdonalds.com/) is their central platform for brand assets and marketing materials - used by teams and agencies across 120 countries. It used to be "protected" by a client-side password. Yes, CLIENT-SIDE.

After I reported this, they took 3 months to implement a proper account system with different login paths for McDonald's employees (using their EID/MCID) and external partners.

Except there was still an issue.

All I had to do was change "login" to "register" in the URL:
`https://admin.me.mcd.com/feel-good-design/register`

![First attempt at registration](/static/images/blogs/mcdonalds/register_attempt1.png)

The endpoint was wide open. When you tried to register without all the fields, it would literally tell you what was missing. So I added them:

![Successful registration](/static/images/blogs/mcdonalds/register_success.png)
*"User has successfully registered" - That was surprisingly easy*

And here's the interesting part - they email you your password in plaintext:

![Password email](/static/images/blogs/mcdonalds/password_email.png)
*They email you the password in plaintext. In 2025.*

I just retested this to make sure, and it still works. If they want people accessing their confidential materials, I guess that's their choice, This is from a Video in the Design Hub:

![Confidentiality reminder from a McDonald's internal Video in the Design Hub](/static/images/blogs/mcdonalds/mcdonalds_confidential.png)
*"McDonald's highly confidential and proprietary information. For internal use by McDonald's system only and not for distribution."*

### API Keys in Plain Sight

In the Design Hub's JavaScript, they left their Magicbell API key and secret just sitting there. With these, someone could:

* List every user in their system
* Send official-looking McDonald's notifications to anyone
* Basically run a phishing campaign with McDonald's own infrastructure

They've since removed and rotated these keys after I reported them.

### Algolia Indexes: Data Exposure

While digging through their JavaScript, I also found their Algolia configuration. All their search indexes are listable, including ones with personal information of users who've requested access to various McDonald's systems. Names, emails, access requests - it's all there, searchable and exposed.

I reported this along with the other vulnerabilities.

## Crew Members in Executive Systems

McDonald's has different portals for different employee levels that you have to oauth into with [GAS](https://gas.mcd.com/) but basic crew member accounts could access executive systems. So my friend who was a Crew Member helped me by trying to login to several sites not meant for Crew Members with his crew account.

TRT (trt.mcd.com) was supposed to be corporate-only, but any crew member could:

* Search for ANY McDonald's employee globally (from Store Manager to CEO)
* See email addresses tied to McDonalds EIDs most of the time personal emails
* Look up everyone from store managers to executives (although weirdly, I saw some crew members in the list as well, but my friend couldnt find his friends accounts so my guess is its probably crew members that oauthed with internal mcdonalds applications they shouldnt have)

![TRT Impersonation Portal](/static/images/blogs/mcdonalds/trt_impersonation.png)
*TRT's "Start Impersonation" feature - accessible to crew members*

The interface has an "Impersonation" feature where you can search by EID or name and get employee details.

### The GRS Panel: No Authentication

GRS (Global Restaurant Standards) is a franchise owner tool that crew members could access. But more importantly - it had **NO authentication for admin functions**. They had a API that check3ed your role on the GRS platform after "logining in" by sending your email address to an endpoint with a query parameter.

Someone could update any page content with whatever HTML they wanted, via an api endpoint with no cookies.
![GRS Update Statement](/static/images/blogs/mcdonalds/grs_statement_endpoint.png)

To demonstrate this, we temporarily changed their homepage:

![GRS Homepage Defaced](/static/images/blogs/mcdonalds/grs_shrek.png)

We changed it back after a minute, but the fact that this was possible at all shows the lack of authentication.

### Internal Documents Access

They misconfigured Stravito in a way that crew members could read internal corporate documents.

## The CosMc's Bonus Round

Remember CosMc's, McDonald's new experimental restaurant? Found some issues there too.

First, they had a new member coupon that was supposed to be one-time use only. The client-side app would block you from using it again, but server-side? No validation. Someone could use the same "new member only" coupon unlimited times just by calling the API directly.

Then I found I could inject arbitrary data into orders, so I used this to try to get their attention:

![CosMc's Order Injection](/static/images/blogs/mcdonalds/cosmcs_order.png)
*Testing order field validation*

## The Absolute Challenge of Reporting This

Here's where it gets interesting. McDonald's HAD a security.txt file with contact info. But they removed it 2 months after adding it. I only found it through the Wayback Machine, and by then it was outdated.

So how do you report security vulnerabilities to a corporation with no security contact?

**I literally called McDonald's HQ and started dropping random security employee names I found on LinkedIn.**

The HQ hotline just asks you to say the name of the person you want to be connected to. So I kept calling, saying random security employee names until finally someone important enough called me back and gave me an actual place to report these issues.

## The Aftermath

They did fix most of the vulnerabilities (as far as I know). The way they handled it was interesting though:

* My friend who helped me research the OAuth vulnerabilities was let go for "security concerns from corporate"
* Never established a proper security reporting channel
* Some things (like that registration endpoint) might still be accessible

## To McDonald's

Thanks for addressing these issues. Some suggestions that might help:

* Keep your security.txt file up and current
* Have an actual security contact that doesn't require calling your HQ
* Consider a bug bounty program so researchers have a clear path for reporting

Better security reporting channels would benefit everyone - your company, your employees, and researchers trying to help.

---

*Still think about those nuggets sometimes. And my friend who lost their job. Corporate security is weird.*

[home](/)
[blog](/blog)

© 2025 bobdahacker