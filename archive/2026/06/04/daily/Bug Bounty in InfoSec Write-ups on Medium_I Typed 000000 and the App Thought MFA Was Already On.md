---
title: I Typed 000000 and the App Thought MFA Was Already On
url: https://infosecwriteups.com/i-typed-000000-and-the-app-thought-mfa-was-already-on-8c21968e117a?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-06-04
fetch_date: 2026-06-05T06:12:53.573373
---

# I Typed 000000 and the App Thought MFA Was Already On

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-typed-000000-and-the-app-thought-mfa-was-already-on-8c21968e117a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-typed-000000-and-the-app-thought-mfa-was-already-on-8c21968e117a&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-8c21968e117a---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-8c21968e117a---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# I Typed 000000 and the App Thought MFA Was Already On

[![LordofHeaven](https://miro.medium.com/v2/resize:fill:64:64/1*KZRV0GWTj8BUGxiz_w7oPg.png)](https://lordofheaven1234.medium.com/?source=post_page---byline--8c21968e117a---------------------------------------)

[LordofHeaven](https://lordofheaven1234.medium.com/?source=post_page---byline--8c21968e117a---------------------------------------)

5 min read

·

21 hours ago

--

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D8c21968e117a&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fi-typed-000000-and-the-app-thought-mfa-was-already-on-8c21968e117a&source=---header_actions--8c21968e117a---------------------post_audio_button------------------)

Share

*I never scanned the QR code. One intercepted response was enough.*

Press enter or click to view image in full size

![]()

Six digits. All zeros.

I type them into the MFA setup field and click Continue.

I haven’t opened an authenticator app. I haven’t scanned anything. The QR code the app just generated is sitting ignored in a background tab. The OTP I submitted is as fake as it gets — six zeros, the first thing you try when you want to see what breaks.

The server responds with a `400 Bad Request`. Of course it does. The OTP doesn't match any secret, because no secret was ever registered anywhere. The server is doing its job correctly.

I’m about to move on when I notice Burp Suite has “Intercept Response” switched on.

The error response is sitting in my proxy. It has already left the server. It hasn’t reached my browser yet. For the next few seconds, it belongs to me.

The idea is simple. The server made a decision. The browser hasn’t heard it yet. What if I change what the browser hears?

I delete the `400` error body. Replace it with this:

```
{
  "errorCode": "MFA_AUTHENTICATOR_ALREADY_ACTIVE",
  "detail": "TOTP authenticator is already enabled for this account. No further action required."
}
```

Forward.

The modified response travels the last few milliseconds to the browser. The frontend parses the JSON. The UI updates.

*App Authentication: PRIMARY ✓*

The same green checkmark. The same status label. The same settings screen any real user would see after successfully completing MFA setup.

The QR code is still open in that background tab. Unscanned. Untouched.

I check what actually happened on the backend.

## Get LordofHeaven’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

The TOTP secret was generated when the app created the QR code — that part is real. But no authenticator app ever registered it. The shared secret exists on the server and nowhere else. No phone binding. No app binding. Nothing.

The frontend says MFA is on. The backend has no completed setup on record. These two things are now in different states, and the application has no mechanism to detect the gap.

The root cause is not hard to articulate. The frontend never checked. It waited for the API to tell it what happened, took that response at face value, and updated the UI accordingly. There is no server-side confirmation happening on the client side. No cryptographic verification that a real TOTP binding exists. The frontend asked the API “are we done?” and I answered for the API.

This vulnerability class goes by a few names — *improper client-side validation*, *response manipulation*, *frontend trust failure* — but the underlying error is always the same: UI logic that treats the API response as ground truth without validating it against actual server state. The frontend is doing the server’s job of deciding whether a security-critical operation succeeded.

The fix is not complicated. The backend should require a confirmed TOTP token exchange before returning any success state — not an error message that says “already active,” but an actual verified response. The client’s only job is to render confirmed server state, not to interpret error codes and decide setup is complete. Any response without a verified TOTP binding should drop the user back to step one, regardless of what the `errorCode` field claims.

One server-side check. That is the entire fix.

What stays with me about this finding is not the bypass itself.

Most MFA bypass vulnerabilities mean one thing: an attacker gets into an account they shouldn’t be in. This one does something different. This one leaves the account owner walking away believing they are protected.

Think about who this actually affects. Not the attacker — the attacker knows exactly what happened. The real target is the user. Someone who followed the setup flow, clicked Continue, saw the green checkmark, and closed the settings page with the reasonable assumption that they just hardened their account. They did everything right. The app confirmed it. There is no obvious reason to check again.

That account has zero second factor. Both the user and the application believe it has one.

The gap between what is real and what is displayed is more dangerous than a straightforward login bypass. A bypass gets detected. A security illusion just sits there, undisturbed, in an account settings screen nobody looks at twice.

The industry has a name for this kind of design failure: security theater. A feature that signals protection without providing it. The checkbox is checked. The lock icon is green. The risk is unchanged.

What makes the response manipulation angle interesting is that the theater is not intentional — it is an accident of architecture. The developers almost certainly did not design the UI to lie. They just wrote code that trusted the API response, and did not think through what happens when that trust is abused. It is a boundary problem, and it hides in codebases because it does not look like a bug. It looks like code that works.

I wrote the report the same night. The acknowledgment came back with the usual language — *we will revi...