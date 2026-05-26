---
title: How I Found 2 Bugs on BBC’s Subdomains and Made It Into Their Hall of Fame
url: https://infosecwriteups.com/how-i-found-2-bugs-on-bbcs-subdomains-and-made-it-into-their-hall-of-fame-86fc4be89e68?source=rss----7b722bfd1b8d--bug_bounty
source: Bug Bounty in InfoSec Write-ups on Medium
date: 2026-05-25
fetch_date: 2026-05-26T06:09:37.665049
---

# How I Found 2 Bugs on BBC’s Subdomains and Made It Into Their Hall of Fame

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://play.google.com/store/apps/details?id=com.medium.reader&referrer=utm_source%3DmobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-2-bugs-on-bbcs-subdomains-and-made-it-into-their-hall-of-fame-86fc4be89e68&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

Get app

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-2-bugs-on-bbcs-subdomains-and-made-it-into-their-hall-of-fame-86fc4be89e68&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![Unknown user](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## InfoSec Write-ups](https://infosecwriteups.com/?source=post_page---publication_nav-7b722bfd1b8d-86fc4be89e68---------------------------------------)

·

[![InfoSec Write-ups](https://miro.medium.com/v2/resize:fill:76:76/1*SWJxYWGZzgmBP1D0Qg_3zQ.png)](https://infosecwriteups.com/?source=post_page---post_publication_sidebar-7b722bfd1b8d-86fc4be89e68---------------------------------------)

A collection of write-ups from the best hackers in the world on topics ranging from bug bounties and CTFs to vulnhub machines, hardware challenges and real life encounters. Subscribe to our weekly newsletter for the coolest infosec updates: <https://weekly.infosecwriteups.com/>

# How I Found 2 Bugs on BBC’s Subdomains and Made It Into Their Hall of Fame

[![LordofHeaven](https://miro.medium.com/v2/resize:fill:64:64/1*KZRV0GWTj8BUGxiz_w7oPg.png)](https://lordofheaven1234.medium.com/?source=post_page---byline--86fc4be89e68---------------------------------------)

[LordofHeaven](https://lordofheaven1234.medium.com/?source=post_page---byline--86fc4be89e68---------------------------------------)

6 min read

·

21 hours ago

--

1

[Listen](https://medium.com/m/signin?actionUrl=https%3A%2F%2Fmedium.com%2Fplans%3Fdimension%3Dpost_audio_button%26postId%3D86fc4be89e68&operation=register&redirect=https%3A%2F%2Finfosecwriteups.com%2Fhow-i-found-2-bugs-on-bbcs-subdomains-and-made-it-into-their-hall-of-fame-86fc4be89e68&source=---header_actions--86fc4be89e68---------------------post_audio_button------------------)

Share

Press enter or click to view image in full size

![]()

## A real case study in hyperlink injection and SSTI & two vulnerabilities hiding in plain sight

I almost didn’t report them.

I was so convinced both bugs were duplicates that I sat on the findings for a few hours before finally writing the PoC. That hesitation would have cost me a Hall of Fame entry and a BBC swag T-shirt.

The lesson hit harder than the bugs themselves.

## The Setup: Chasing a Name on a Wall

I’d been passively eyeing the BBC’s vulnerability disclosure program for a while. Not because of the money — it’s a VDP, there’s no monetary reward — but because of the Hall of Fame.

[## Security Disclosure Policy

### Working with the research community to improve our online security

www.bbc.com](https://www.bbc.com/backstage/security-disclosure-policy/?source=post_page-----86fc4be89e68---------------------------------------)

Getting your name on a company’s security acknowledgment page means something in this field. It’s credibility you can’t fake. So one afternoon I opened my terminal, pointed subfinder at a BBC domain, and started the recon that led to two findings I still think about.

Out of the list that came back, two subdomains looked interesting enough to investigate. I’ll refer to them as `xyz.bbc.com` and `abc.bbc.com` I won't disclose the exact URLs as a courtesy to the BBC security team.

What happened next is what I want to walk you through.

## Bug #1: Hyperlink Injection in a Contact Form

The first target had a Contact Us page. Standard stuff — organisation name, country, contact name, email, phone, enquiry type, message.

I started where I always start: the basics. I sprayed some XSS payloads across every input field. Nothing fired. The application handled them cleanly.

So I stepped back and thought about what else these fields could do.

**Hyperlink injection is boring. That’s exactly why it works.**

Most hunters skip it. It doesn’t look like a “real” vulnerability. It doesn’t pop an alert box or dump a database. But what it *does* do is allow an attacker to inject arbitrary URLs into emails that the application sends on behalf of a trusted brand — in this case, the BBC.

I replaced the input values across multiple fields with `http://evil.com` and submitted the form.

Press enter or click to view image in full size

![]()

A few seconds later, a confirmation email arrived.

Every injected URL had rendered as a **live, clickable hyperlink** in the email body — sent from an official BBC domain. The email confirmed: Organisation name, contact name, phone number, and message — all containing my URL, all hyperlinked.

![]()

Think about what that means in practice. A phishing campaign delivered from a trusted BBC sender address, carrying attacker-controlled links, to anyone who submits that form. No technical sophistication required to weaponize it.

I documented the full reproduction steps, attached the screenshots, and moved to the second subdomain.

[## 🕵️‍♂️💻 “I Didn’t Plan to Find a P1… But My Script Had Other Plans 🧠💣”

### 🎬 It all started with a YouTube video…

infosecwriteups.com](/%EF%B8%8F-%EF%B8%8F-i-didnt-plan-to-find-a-p1-but-my-script-had-other-plans-77691a46985b?source=post_page-----86fc4be89e68---------------------------------------)

## Bug #2: Server-Side Template Injection via Registration Email

The second subdomain had a registration flow. You sign up, provide a name and email, and receive a welcome email.

That welcome email was the attack surface.

**SSTI — Server-Side Template Injection — is one of those vulnerabilities that looks impossible until it isn’t.**

The idea is simple: if the application takes user-supplied input and renders it inside a template engine without sanitisation, math expressions like `{{7*7}}` get *evaluated*, not printed. Instead of seeing `{{7*7}}` in the output, you see `49`.

## Get LordofHeaven’s stories in your inbox

Join Medium for free to get updates from this writer.

Subscribe

Subscribe

[x]

Remember me for faster sign in

I created a new account. For the first name I entered `{{50*100}}`. For the last name I entered `{{7*7}}`.

![]()

Then I waited for the verification email.

![]()

The subject line read: **Welcome, 5000**

The template engine had evaluated `{{50*100}}` as `5000` and rendered it directly into the email. The application was passing unsanitised user input into a live template context.

That’s not just an injection bug — that’s a direct path to **Remote Code Execution** in many template engines, depending on the sandbox configuration and the engine in use. I kept the PoC clean and within the scope of confirming vulnerability, then wrote up the report.

## What Happened After the Reports

Both findings went to BBC’s Vulnerability Disclosure Programme.

Within a few days, I received confirmation from their security team. Both vulnerabilities were valid. Neither was a duplicate — the thing I’d been most worried about.

Shortly after, I got an email telling me I’d been added to the BBC VDP Hall of Fame.

Press enter or click to view image in full size

![]()

[## Acknowledgements

### The BBC wishes to t...