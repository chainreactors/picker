---
title: One SSRF to Rule Them All
url: https://infosecwriteups.com/one-ssrf-to-rule-them-all-f6563afce506?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-07-04
fetch_date: 2025-10-06T23:50:09.741130
---

# One SSRF to Rule Them All

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Ff6563afce506&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fone-ssrf-to-rule-them-all-f6563afce506&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fone-ssrf-to-rule-them-all-f6563afce506&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-f6563afce506---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-f6563afce506---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# One SSRF to Rule Them All

[![Ott3rly](https://miro.medium.com/v2/resize:fill:64:64/1*3wMPJmhJUNOpqobsPBkS8g.jpeg)](https://ott3rly.medium.com/?source=post_page---byline--f6563afce506---------------------------------------)

[Ott3rly](https://ott3rly.medium.com/?source=post_page---byline--f6563afce506---------------------------------------)

5 min read

·

Jul 3, 2025

--

2

Listen

Share

*From one single callback, to full control of the server.*

![]()

I was at a coffee shop, laptop open, just starting my day. Nothing special — until I found something more energizing than caffeine.

One of the SaaS platforms I was exploring had a built-in file editor and its own scripting language. I’d seen setups like this before — great for data analysts, but even better for bug hunters.

![]()

## Initial Recon & The First Clue

At first, it didn’t look like much. The environment was heavily sandboxed, with strict limits on every function. Most inputs were locked down, and direct system access was off the table.

After trying for some obvious low hanging fruits like OS Command injection, my next question was: *“How about data interaction? If it’s meant for data analysts, there must be data imports in place.”*.

But one thing stood out — a function that could fetch external data via URL. Finding it previously would’ve taken ages of digging through dry documentation pages. But luckily my AI companion helped me a lot, as I have asked the right question like this: *“Can this custom language fetch data from external URLs?”*

And just like that, I had my answer - *func http*:

Press enter or click to view image in full size

![]()

## Initial Struggles

Of course, it wasn’t instant success. It almost never is! To get there, you go through a painful process of trial and error — trying different options, failed payloads, dead ends. But with enough persistence, I believed I could make it happen.

At first, I tried sending basic requests to the same server (localhost), even experimenting with weird schemes like `file:///` and `gopher:///`. Looking back, that was too many steps too fast. So I stepped back.

I realized I first needed to check something much simpler: *“Can it reach external hosts at all?”*

I pointed a request to `<http://google.com>`. Not to exfiltrate anything – just to see if the call worked. If I could confirm any kind of callback, even blind, it would mean I had a foot in the door. That would be **SSRF** confirmed, but slim to none impact YET.

I was so focused, I didn’t even notice my coffee had gone cold.

## Breakthrough

Then I spotted something important — it supported custom headers. If this environment was running in the cloud, and if that request handler respected headers, I had a shot at the biggest impact: **cloud metadata access**. Which cloud though?

I cycled through different metadata endpoint formats — AWS, GCP, Azure — until finally, **one of them answered**. This payload returned data:

```
http://169.254.169.254/metadata/instance?api-version=2021-02-01
```

And it only worked with the header:

```
Metadata: true
```

Press enter or click to view image in full size

![]()

**Bingo. Azure confirmed.**

## Some Juicy Stuff. Finally.

Now that I had confirmed Azure as the cloud provider, it was time to push the SSRF further. Reading instance metadata was one thing. But could I extract credentials?

Azure exposes Managed Identity tokens through the same internal IP — you just need to hit the right endpoint and include the correct headers. So I built the next payload:

```
http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/
```

Headers:

```
Metadata: true
```

I ran the request and waited. No errors. Just a clean, well-formatted JSON response with an access token. A valid, signed **OAuth2 Bearer token** tied to the server’s own identity.

At this point, I wasn’t just poking around anymore. I had a live token that could talk to Azure’s Management API — with whatever permissions that identity had. Even if it was just read-only, that alone could expose resource names, storage accounts, internal architecture, and more.

But if the role had write access? The impact could escalate fast:

* Create new resources
* Modify cloud infrastructure
* Or even pivot into lateral movement via chained cloud APIs

This wasn’t just **proof of concept** — this was success.

## The Aftermath

I put everything together — the metadata access, the token extraction, and the security risks tied to Managed Identity abuse and submitted the report. A few days later, I got a response. At first, it looked like bad news:

![]()

But then came the twist — the original finding had been marked as resolved… **but never actually fixed**:

Press enter or click to view image in full size

![]()

They acknowledged that my report proved the issue still existed. Not only that — I had provided clearer reproduction steps and showed greater impact through token theft. So they moved it into **triaged**.

**$1,500.**

A rare gesture of goodwill — and one that honestly meant more than just the money.

Some programs don’t even reply to duplicates. This one admitted fault, owned it, and rewarded the effort.

I really love hunting on programs like this when they treat researchers very well!

## Final Thoughts

This wasn’t my first SSRF — and it definitely won’t be the last. What stood out to me most in this case wasn’t the payload, or even the token. It was the **process**.

* Start small.
* Ask the right questions.
* Follow the boring leads.
* Never give up.

At first glance, the bug looked like nothing. A sandboxed scripting language, a hidden function, and some confusing responses. But with enough persistence, asking the right questions, testing small steps, and digging layer by layer — it led to **a critical cloud compromise path**.

That’s the thing with SSRFs: They often start as “low/none impact.” But given time, context, and creativity — they escalate.

And finally:...