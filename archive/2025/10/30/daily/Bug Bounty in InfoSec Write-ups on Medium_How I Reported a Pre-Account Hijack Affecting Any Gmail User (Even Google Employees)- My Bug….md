---
title: How I Reported a Pre-Account Hijack Affecting Any Gmail User (Even Google Employees)- My Bug…
url: https://infosecwriteups.com/how-i-reported-a-pre-account-hijack-affecting-any-gmail-user-even-google-employees-my-bug-258180c8dd70?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2025-10-30
fetch_date: 2025-10-31T03:12:52.160531
---

# How I Reported a Pre-Account Hijack Affecting Any Gmail User (Even Google Employees)- My Bug…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F258180c8dd70&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-reported-a-pre-account-hijack-affecting-any-gmail-user-even-google-employees-my-bug-258180c8dd70&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-reported-a-pre-account-hijack-affecting-any-gmail-user-even-google-employees-my-bug-258180c8dd70&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-258180c8dd70---------------------------------------)

·

Follow publication

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-258180c8dd70---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

Follow publication

# How I Reported a Pre-Account Hijack Affecting Any Gmail User (Even Google Employees)- My Bug Report Journey with Google

[![Harsh kothari](https://miro.medium.com/v2/resize:fill:64:64/1*2pJvWjazjVBZujnOU9c9Tw.jpeg)](https://cyberhrsh.medium.com/?source=post_page---byline--258180c8dd70---------------------------------------)

[Harsh kothari](https://cyberhrsh.medium.com/?source=post_page---byline--258180c8dd70---------------------------------------)

4 min read

·

18 hours ago

--

Listen

Share

## Intro - a normal night that turned interesting

Bug hunting looks cool on Twitter: big payouts, P1 RCEs, flex posts. Reality is usually half-cold coffee, many tabs, and small logic bugs that break real user trust.

I found one of those quiet but dangerous bugs on a Google subdomain. Short version: **you could create a full account for any Gmail address, get a token, and change profile or cart - all without email verification and without rate-limiting.** Bad, right? Very bad.

This is my story - how I found it, how I reported it, the follow-ups, the frustration, and what I learned.

## Whoami?

Ek aur din, ek aur vulnerability. Same banda, naye emotions 😭. Intro ke liye purane writeups padho yaar.
(Translation - Another day, another vulnerability. Same guy, new emotions 😭. Read old write-ups for the intro, friend.)

## The “wait, that worked?” moment

I was just poking around the Website. I found the website is using graphql , I already had learned how graphql works and stuff so without wasting time I runned Graphql Introspection query and I found many things. Interestingly i found an registeration mutation. I tried and results , Success.

No OTP. No verification. Just a token in response. I could update name, add address, and even pre-fill the shopping cart via GraphQL mutations.

Two feelings hit me: **(1)** “Yes - proof!” and **(2)** “Oh no - this is dangerous.”

The main reason it is more dangerous because they only have SSO for Sign-up / Sign-in , if the real user later logged in with Google OAuth, they would land inside the account I had already created. Zero-click takeover. Silent and nasty.

(Fun Fact- They can’t even revoke the account as they don’t have any reset password option or any other way they can revoke the JWT token.)

I tested carefully and kept all sensitive stuff private. I made a small, repeatable PoC: createCustomer → generateCustomerToken → updateCustomer/addProductsToCart → victim logs in via OAuth → victim ends up in attacker account.

## PoC and impact (short & clear)

I prepared:

* a private PoC video (redacted here),
* reproduction steps (sanitized),
* a clear impact list.

Why it matters:

* **Zero-click account takeover** — no phishing, no user interaction needed.
* **Persistent access** — attacker has a valid JWT; victim cannot revoke.
* **Business logic abuse** — attacker can prefill carts, spam, change profile, maybe place orders if payment saved.
* **Internal risk** — I tested behavior for an internal-style email during private testing (kept private here).

This was a logic bug, not a shiny exploit - but the damage could be real.

## Reporting to Google VRP — timeline (real, no filter)

I submitted the report and started the usual back-and-forth.

* **Jun 13, 2025 —** Report submitted (triaged).
* **Jun 18, 2025 —** Sent detailed attack scenario and PoC video to Google on request.
* **Jun 28, 2025 —** Clarified that the victim cannot remove attacker or revoke token.
* **Jul 7, 2025 —** Shared additional impact (internal-style email test — private).
* **Jul 10, 2025 —** Status: accepted (filed to product team).
* **Jul 24 & Jul 31, 2025 —** VRP panel’s reward decision: $0.
* **Oct 15, 2025 —** Final: closed — reason: application is operated by a third-party vendor (out of scope for VRP).

Important: I also tried contacting the vendor directly about the bug, but I didn’t get a reply from them. Still, the vulnerability was **eventually resolved** now they have forget password option GraphQL is also secured (good - users protected), even though vendor communication was radio-silent from my side.

Press enter or click to view image in full size

![]()

Proof (I am not the fake medium writer ifykyk😂 )

## The emotional part - excitement and a bit of let-down

That PoC moment - big dopamine spike. Getting triaged and accepted - validation. The follow-ups - expected. The closure because of “vendor-operated” scope - frustrating.

I pushed with WHOIS and ownership info, argued that a Google subdomain with user-facing security issues needs fixing regardless of vendor operation. The panel reviewed and still closed the report citing vendor operation. It felt like: I did the right technical job, but the procedural ladder stopped the reward path.

Still - the main win: the bug was fixed. That’s what matters for users.

## What I learned (practical, short)

If you hunt logic bugs or build auth systems, keep these in mind:

* **Check signup & SSO edges first.** Signup, invite, change-email, SSO-linking - these often hide logic mistakes.
* **Don’t issue long-lived tokens before verification.** Tokens before verification = trouble.
* **Give users session visibility & revocation.** If someone links via SSO, users should be able to see and remove sessions.
* **Rate-limit / CAPTCHA unauthenticated endpoints.** GraphQL is powerful — throttle public mutations.
* **Collect ownership evidence early.** WHOIS, registrar info, footer screenshots — they help if scope is questioned.
* **Be ready for non-technical fights.** Scope and ownership debates happen. Patience + evidence win.

## Message for other researchers — short & real

Be curious more than flashy. Tools help, but thinking wins. Click around like a normal user. Try weird flows. Ask “what if” and follow it.

When you report:

* Make PoC repeatable and clean.
* Explain impact in simple words engineers understand...