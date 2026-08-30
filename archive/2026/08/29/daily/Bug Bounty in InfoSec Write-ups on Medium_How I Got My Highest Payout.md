---
title: How I Got My Highest Payout
url: https://infosecwriteups.com/how-i-got-my-highest-payout-466213a1cb47?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-08-29
fetch_date: 2026-08-30T07:42:03.169627
---

# How I Got My Highest Payout

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-got-my-highest-payout-466213a1cb47&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-got-my-highest-payout-466213a1cb47&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-466213a1cb47---------------------------------------)

·

1. [Nobody wants to fill out the form](/?source=post_page-----466213a1cb47---------------------------------------#9053 "Nobody wants to fill out the form")
2. [The request that looked wrong](/?source=post_page-----466213a1cb47---------------------------------------#7682 "The request that looked wrong")
3. [The wrong turn](/?source=post_page-----466213a1cb47---------------------------------------#b87c "The wrong turn")
4. [The swap](/?source=post_page-----466213a1cb47---------------------------------------#1b02 "The swap")
5. [Where most people stop](/?source=post_page-----466213a1cb47---------------------------------------#e1a8 "Where most people stop")
6. [Why it broke](/?source=post_page-----466213a1cb47---------------------------------------#15b5 "Why it broke")
7. [Takeaway](/?source=post_page-----466213a1cb47---------------------------------------#4ab9 "Takeaway")

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-466213a1cb47---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

[Bug Bounty](https://medium.com/tag/bug-bounty?source=post_page---header_tags--466213a1cb47---------------------------------------)

[Cybersecurity](https://medium.com/tag/cybersecurity?source=post_page---header_tags--466213a1cb47---------------------------------------)

[Pentesting](https://medium.com/tag/pentesting?source=post_page---header_tags--466213a1cb47---------------------------------------)

[Security](https://medium.com/tag/security?source=post_page---header_tags--466213a1cb47---------------------------------------)

[Hackerone](https://medium.com/tag/hackerone?source=post_page---header_tags--466213a1cb47---------------------------------------)

# How I Got My Highest Payout

[![Adhamkhairy](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*xv5j3MG7_VrAoW34)](https://0xsponge.medium.com/?source=post_page---byline--466213a1cb47---------------------------------------)

[Adhamkhairy](https://0xsponge.medium.com/?source=post_page---byline--466213a1cb47---------------------------------------)

5 min read

·

Jul 31, 2026

--

3

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D466213a1cb47&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-got-my-highest-payout-466213a1cb47&source=---header_actions--466213a1cb47---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

The Token Was Fine. That Was the Whole Problem.

The target was an application portal. You register, you fill out a genuinely **ENORMOUS** form, and at the end it generates a PDF of everything you submitted: income figures, tax numbers, personal identifiers, household details. Not just yours. Your whole family’s.

Filling that form out properly took me close to an **HOUR**.

And that hour is why the bug was still there.

## Nobody wants to fill out the form

Most hunters land on a target like this, see a multi-stage form with validation on every field, and go looking for something with a shorter path to a request. I get it. It’s boring. You didn’t get into this to type in fake tax figures for an hour.

But that friction is the whole reason the bug survived. Every previous hunter bounced off the setup, so nobody ever reached the endpoints that only appear *after* you have a real, completed application sitting in the database.

The harder a target is to set up, the fewer people have looked at what’s behind the setup.

So I filled out the form. **Twice** I’d need a second account eventually anyway.

## The request that looked wrong

Every data call on the platform looked like this:

```
POST /App/SomeController/SomeMethod HTTP/1.1
Host: portal.example.com
Authorization: Bearer <JWT>
Content-Type: application/json

{"UserId":"<blob>",
 "ApplicationId":"<blob>",
 "PageName":"...",
 "Token":"<the same JWT again>"}
```

The Bearer token already says who I am. So why is my `UserId` *also* in the body? And why is the token in there a second time?

Either those IDs are decoration, or they’re the thing actually doing the lookup. Only one of those is interesting.

## The wrong turn

I saw a JWT and went after the JWT, because that’s the reflex.

Flipped a byte in the signature → `401`. Set `alg` to `none` → `401`.

Their authentication was flawless. Signature properly verified, no algorithm confusion, nothing. I kept poking anyway for a while because I’d already decided that was the bug.

Then it clicked, and the failure was the clue.

A verified token answers **who is asking**. It says nothing about **what they’re allowed to have**. And I still had that unexplained `UserId` in the body.

## The swap

Account **A** is me. Account **V** is the victim also me, different email, with a real completed application on it. That’s what the second hour of form-filling bought.

Kept **A’s own untouched Bearer token**. Swapped the body IDs for V’s.

```
POST /App/AppCertification/GetAppCertification HTTP/1.1
Authorization: Bearer <A's own token>

{"UserId":"<V's>","ApplicationId":"<V's>", ...}
```

```
HTTP/1.1 200 OK

{"ReturnMessage":"Success","Username":"<V's>", ...}
```

My session. V’s data.

## Get Adhamkhairy’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

Then the PDF export endpoint, same trick:

```
HTTP/1.1 200 OK
Content-Type: application/pdf
Content-Length: 105590
Content-Disposition: attachment; filename=Profile-<V's reference>.pdf
```

103 KB. Filename stamped with **the victim’s** reference number. That’s not a leaked field; that’s the entire application. Every number that household typed in, exported as a file, by me, from a free account I made in a minute.

## Where most people stop

Here’s the part I want you to actually read.

I had mass PII. Full dossier, whole family, one request. And there’s an obvious objection sitting right on top of it:

**You need two non-sequential IDs to pull this off.** They aren’t integers you can increment — they’re long opaque ciphertext blobs. Unguessable. So the argument writes itself: *sure it’s a bug, but you’d need the victim’s IDs, and you can’t get those.* Low severity. Targeted at best.

That’...