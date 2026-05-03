---
title: When Logout Isn’t Really Goodbye: A Subtle Data Exposure Bug.
url: https://infosecwriteups.com/when-logout-isnt-really-goodbye-a-subtle-data-exposure-bug-271b683ddb9a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-02
fetch_date: 2026-05-03T05:28:57.297324
---

# When Logout Isn’t Really Goodbye: A Subtle Data Exposure Bug.

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhen-logout-isnt-really-goodbye-a-subtle-data-exposure-bug-271b683ddb9a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhen-logout-isnt-really-goodbye-a-subtle-data-exposure-bug-271b683ddb9a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-271b683ddb9a---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-271b683ddb9a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[![kjulius](https://miro.medium.com/v2/resize:fill:64:64/1*pNjTItx95RQhfspL_MnSoA.jpeg)](https://kjulius.medium.com/?source=post_page---byline--271b683ddb9a---------------------------------------)

[kjulius](https://kjulius.medium.com/?source=post_page---byline--271b683ddb9a---------------------------------------)

4 min read

·

23 hours ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D271b683ddb9a&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fwhen-logout-isnt-really-goodbye-a-subtle-data-exposure-bug-271b683ddb9a&source=---header_actions--271b683ddb9a---------------------post_audio_button------------------)

Share

When Logout Isn’t Really Goodbye: A Subtle Data Exposure Bug.

Press enter or click to view image in full size

![]()

How a “low severity” simple P4 bug still managed to teach a high-value lesson (and yes… it paid 💰). Beginner friendly…

## ⚠️ Disclaimer.

This was conducted under **authorized testing conditions** for educational and security research purposes. No data was abused, and the issue has been responsibly disclosed and fixed.

## 🧩 The Discovery.

While testing authentication flows on a government-backed login system, I came across something that felt… off.

The application used a modern **SSO login flow via QR code**. Everything worked as expected:

* Login was smooth.
* Session handling seemed solid.
* Logout confirmed success.

But then came a simple action that changed everything:

👉 I clicked the **browser back button**.

Press enter or click to view image in full size

![]()

PoC

And just like that, my **previously authenticated page reappeared**, fully populated with **sensitive personal information** — even though I had already logged out.

Press enter or click to view image in full size

![]()

PoC

## What Was Happening?

At first glance, it looked like a **broken logout** or even a **session hijacking opportunity**. But deeper testing told a different story.

Here’s what I confirmed:

* ✅ Logout endpoint worked correctly.
* ✅ Session was invalidated server-side.
* ✅ Any refresh or API call returned **401 Unauthorized.**
* ❌ Yet sensitive data was still visible after pressing **Back.**

So what gives?

## The Technical Explanation.

This behavior is caused by the browser’s **Back/Forward Cache (bfcache)**.

Instead of making a new request, the browser:

* Restores the entire page from memory.
* Skips revalidation with the server.
* Displays the previous DOM instantly.

Even though the server has **terminated the session**, the browser is simply **replaying what it already rendered**.

And importantly:

```
Cache-Control: no-cache, must-revalidate
Pragma: no-cache
```

These headers do **not fully prevent bfcache**.

## Why This Matters.

You might think:

> *“If the session is dead, what’s the big deal?”*

Here’s the real-world risk.

## Scenario: Shared Device Exposure.

1. A user logs into their account on a **public or shared computer.**
2. They log out and walk away.
3. Another user presses the **Back button.**
4. Sensitive information is instantly revealed:

* Names.
* Emails.
* Account details.
* Possibly government-linked identifiers/IDs.

Even without interaction, **confidential data is exposed**.

## ⚖️ Severity: Why This Is “Only” P4.

From a bug bounty perspective, this is typically classified as:

> ***Sensitive Information Exposure via Client-Side Cache.***

Why not higher?

* ❌ No session reuse.
* ❌ No unauthorized API access.
* ❌ No privilege escalation.
* ❌ No account takeover.

✔️ Data is **not retrievable from the server.**
✔️ The issue is **purely client-side rendering.**

## Get kjulius’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

So it lands as:

* **Low severity (P4).**
* Sometimes **Informational.**

But don’t let that fool you — it’s still a **real privacy concern**.

## 🏗️ What Better Implementations Look Like.

Some applications go a step further.

Instead of allowing cached pages to render, they:

## 🔁 Force Reload on Back Navigation.

```
window.onpageshow = function (event) {
    if (event.persisted) {
        window.location.reload();
    }
};
```

## 🔒 Or Redirect Immediately.

* Detect invalid session.
* Show **“Session expired”.**
* Prevent sensitive UI from appearing at all.

That’s why you may notice:

> *Some sites* never *show old data after logout — even with the back button.*

## 🧠 Key Takeaway.

This bug highlights an important principle:

> ***Security isn’t just about blocking access — it’s also about controlling what remains visible.***

Even when:

* Authentication is correct.
* Sessions are invalidated.
* APIs are protected.

You can still have **residual data exposure**.

## 📝 Final Thoughts.

This wasn’t a flashy bug.
No bypasses. No exploits. No takeover.

Just a simple browser action — revealing a subtle gap between:

* **Server-side security.**
* **Client-side behavior.**

And that’s exactly why it matters.

Because sometimes, the most overlooked issues are the ones sitting **right in front of the user’s screen**.

## 📝 The Report (and the bounty part).

I documented everything properly:

* Steps to reproduce.
* Screenshots.
* Network behavior.
* Impact (without exaggeration — very important).

Submitted it.

Waited…

And then:

👉 **Accepted.**
👉 **Issue acknowledged.**
👉 **Got paid. 💰**
👉 **Fix implemented. ✅**

Now when you hit Back?

No more surprise reunion with your old session 😄

Press enter or click to view image in full size

![]()

Thanks for reading. If this made you smile (or double-check your logout 😅), feel free to leave some 👏, on “X” as <https://x.com/ethical_h4ck3r_> follow for more security research and write-ups.

[Cache Memory](https://medium.com/tag/cache-memory?source=post_page-----271b683ddb9a---------------------------------------)

[P4 Bugs](https://medium.com/tag/p4-bugs?source=post_page-----271b683ddb9a--------------------------------...