---
title: Click to Pray, Click to Leak: The Pope's Official App Exposes 700,000+ User Emails
url: https://bobdahacker.com/blog/click-to-pray
source: Over Security
date: 2026-09-03
fetch_date: 2026-09-04T06:43:51.105370
---

# Click to Pray, Click to Leak: The Pope's Official App Exposes 700,000+ User Emails

[bobdahacker](/)

☰

* [home](/)
* [blog](/blog)

# Click to Pray, Click to Leak: The Pope's Official App Exposes 700,000+ User Emails

July 24, 2026

BobDaHacker

*I reported this on January 3rd, 2026. It is now July 24th. Six months later. The vulnerability is still live. Nobody has ever responded. I guess my email wasn't in their prayers.*

## What is Click To Pray?

Click To Pray is the official prayer app of the Pope's Worldwide Prayer Network. Pope Francis himself launched it during a Sunday Angelus address in St. Peter's Square back in 2019. He held up a tablet on the balcony and told the world to download it. Very cool. Very holy. Very leaky.

The app lets users pray alongside the Pope's monthly intentions, share prayer requests with the community, and follow a daily prayer rhythm. It's available on iOS, Android, and the web at clicktopray.org, in seven languages. As of July 2026, it has **719,517 registered accounts**.

It's a Pontifical Work. This is Vatican infrastructure. God's tech stack, if you will.

## The Vulnerability

When you create an account on Click To Pray, you're assigned a sequential numeric user ID. Simple enough.

The API endpoint `GET https://api.clicktopray.org/user/users/{id}` returns user data for any account when you supply a valid user ID. No authorization check. No ownership validation. Just increment the number and get someone else's data. The Lord provides.

Here's what the API hands back for user 69420 (nice):

![API response for user 69420](/static/images/blogs/clicktopray/api_response_69420.png)

Email address. First name. Last name. Country. Date of birth (or as their backend calls it, `borned_date`, because apparently bad grammar isn't a sacrament). Role. Whether the account has been deleted. All of it, for any user, no questions asked.

The role field is `"PRAYER"`. Your role on the Pope's prayer app is prayer. Thank you, backend team.

The response headers also have `X-Powered-By: Express` because the Vatican is running its prayer infrastructure on the framework you learn in week two of a Node.js bootcamp.

That's an IDOR. Insecure Direct Object Reference. One of the most basic access control flaws in web security. You ask for your own data, the server gives it to you. You ask for someone else's data, the server gives you that too. Thou shalt not authorize, apparently.

## The Scale

With sequential user IDs and no rate limiting, an attacker could enumerate every single account on the platform. All 719,517 of them. One GET request per user. `for i in range(1, 719518): scrape()`. That's it. That's the exploit.

That's 700,000+ email addresses belonging to people who signed up for an app to pray. A lot of these users are likely older, less tech-savvy, and deeply trusting of anything associated with the Vatican. A harvested list like this would be a phishing goldmine. Imagine getting an email that says "The Holy Father requests your urgent attention" with a Vatican-looking link. Grandma is clicking that. Every time.

## But Wait, There's More

While poking around, I noticed something fun. The signup endpoint `POST https://api.clicktopray.org/user/users/sign-up` returns the account's `validation_hash` directly in the response body.

![Signup response showing validation_hash](/static/images/blogs/clicktopray/signup_response.png)

That `validation_hash` is the exact same UUID used in the email verification link:

![Verification email with matching UUID](/static/images/blogs/clicktopray/verification_email.png)

So the API hands you the verification token before you even check your email. You can sign up with any email address and verify the account immediately without ever accessing the inbox. The verification email is just a suggestion at that point. Faith-based email verification, if you will.

Oh, and that verification email? My email client slapped a big warning on it:

> ⚠️ This email has failed its domain's authentication requirements. It may be spoofed or improperly forwarded.

The Pope's official prayer app is sending emails that look like phishing. Their SPF, DKIM, or DMARC is misconfigured, which means their legitimate emails are indistinguishable from someone impersonating them. So not only is the API leaking 700,000 email addresses that could be used for phishing, but the real emails from Click To Pray already look like phishing. An attacker wouldn't even need to try hard. They could send a pixel-perfect phishing email and it would have the same level of email authentication as the real thing: none. God works in mysterious ways.

## Disclosure

I found this in early January 2026 and on January 3rd I emailed nine people: the general info address, six individual staff members at clicktopray.org, and two contacts at popesprayer.va (the Pope's Worldwide Prayer Network). No response. From any of them.

Six months. Nothing. No fix. No acknowledgment. The vulnerability stayed wide open while hundreds of thousands of users kept signing up to pray, handing over their email addresses to a platform that couldn't be bothered to protect them.

Eventually I brought it to a journalist at Dark Reading. They reached out to the Pope's Worldwide Prayer Network's press email, since Click To Pray doesn't even have a dedicated press contact. Also nothing. At this point I'm starting to think they took a vow of silence.

You can read Dark Reading's coverage here: [Vatican's Official Prayer App Leaks 700K+ Global Users' PII](https://www.darkreading.com/vulnerabilities-threats/vatican-official-prayer-app-leaks-700k-pii)

| Date | What |
| --- | --- |
| Early January 2026 | Discovered the IDOR on clicktopray.org |
| January 3, 2026 | Emailed Click To Pray with full disclosure. No response. |
| July 2026 | Brought it to a journalist. |
| July 2026 | Journalist contacted the Pope's Worldwide Prayer Network press email. No response. |
| July 2026 | Still not fixed. Still no response. Amen. |

No bug bounty. No security.txt. No VDP. No acknowledgment. No evidence anyone on their end has ever read a single email about this. Ironic, given how many of their users' emails I could read.

## To Click To Pray

Your app is endorsed by the Pope. It's operated by a Pontifical Work. Hundreds of thousands of faithful users trusted you with their email addresses when they signed up to pray together.

Fix the IDOR. I reported it six months ago. This is not a complicated fix. Validate that the authenticated user is requesting their own data before returning it. That's it. One `if` statement. Even Moses only needed ten commandments. You need one.

Publish a security.txt. Set up a VDP. Give researchers a way to reach you that doesn't involve literally praying for a response.

Your users deserve better. And while you're at it, fix `borned_date`. That's not a word.

# Update (2026-07-24) they fixed it

Sometime after Dark Reading ran the story, the endpoint changed. Seven months of silence, and then, without a word to me, `GET /user/users/{id}` quietly stopped handing out the good stuff.

First name. Last name. That's it. No email address, no country, no `borned_date`. The PII that made this a 700,000-record phishing list is gone.

The authorization check is there now: request your own user ID and you still get your email back, request someone else's and you get a public profile. Names are supposed to be public on a platform where you pray alongside other people, so what's left is what was always meant to be visible. They wrote the if statement. One if statement, exactly as promised. Moses would be proud.

I also never got an email. Not an acknowledgment, not a thank you, not a "we've addressed this." I only know it's fixed because I saw a reddit comments from 5 hours ago saying it was fixed. I went back and checked the endpoint myself.

Still, they fixed it, and they fixed it right. That was the point. Amen.

---

So long and thanks for all the prayers :3

[home](/)
[blog](/blog)

© 2025 bobdahacker