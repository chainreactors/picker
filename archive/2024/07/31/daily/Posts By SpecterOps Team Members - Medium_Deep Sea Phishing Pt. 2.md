---
title: Deep Sea Phishing Pt. 2
url: https://posts.specterops.io/deep-sea-phishing-pt-2-29c48f1e214e?source=rss----f05f8696e3cc---4
source: Posts By SpecterOps Team Members - Medium
date: 2024-07-31
fetch_date: 2025-10-06T17:46:50.048663
---

# Deep Sea Phishing Pt. 2

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F29c48f1e214e&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderCollection&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fdeep-sea-phishing-pt-2-29c48f1e214e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Fposts.specterops.io%2Fdeep-sea-phishing-pt-2-29c48f1e214e&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[## Posts By SpecterOps Team Members](https://posts.specterops.io/?source=post_page---publication_nav-f05f8696e3cc-29c48f1e214e---------------------------------------)

·

Follow publication

[![Posts By SpecterOps Team Members](https://miro.medium.com/v2/resize:fill:76:76/1*D-FDlfkqivRBQZoESrwtqw.png)](https://posts.specterops.io/?source=post_page---post_publication_sidebar-f05f8696e3cc-29c48f1e214e---------------------------------------)

Posts from SpecterOps team members on various topics relating information security

Follow publication

## PHISHING SCHOOL

# Deep Sea Phishing Pt. 2

## Making Your Malware Look Legit to Bypasses EDR

[![Forrest Kasler](https://miro.medium.com/v2/da:true/resize:fill:64:64/0*twL-x8eyh-Q1_GWn)](https://medium.com/%40fakasler?source=post_page---byline--29c48f1e214e---------------------------------------)

[Forrest Kasler](https://medium.com/%40fakasler?source=post_page---byline--29c48f1e214e---------------------------------------)

7 min read

·

Jul 30, 2024

--

Listen

Share

I wanted to write this blog about several good techniques for endpoint detection and response (EDR) evasion; however, as I was writing about how to evade EDRs, I was hit with an epiphany:

💡*“EDR evasion is all about looking like legitimate software” — ph3eds, 2024*

Boom! That’s it! That’s the complete game changer that only took me 10 years to finally crystalize! You’re welcome.

*“EDR evasion is all about looking like legitimate software”*? No duh! Why is that even worth writing a blog about?!

Please, let me explain.

## **What is Legitimate Software?**

When I say legitimate software, I mean software that a trustworthy source like Microsoft has authored and signed. So, to bypass EDR, we want all of our malicious actions to come from a binary that a trusted source authored and signed. When we put it that way, there are actually multiple ways to achieve this goal. This blog is about the many ways we can hide our code and our actions so that they look legit.

**Note:** You can’t just sign a Meterpreter payload and expect it to bypass EDRs. The point here is to blend in the best we can to extend the useful life of our custom payloads as long as possible.

## **❌ Not Legit — Untrusted, Unsigned**

We are starting at the bottom here: an untrusted, unsigned binary similar to what we might write as an initial access payload, based on [my previous blog](/deep-sea-phishing-pt-1-092a0637e2fd). We may have achieved “unknown bad” status, but that’s about the only thing we have going for us at this point. We do not have a trusted, signed binary, so we don’t look very legit. Let’s fix that!

## **🤷‍♂️Barely Legit — Steal a Cert and Sign It!**

This section is really just a plug for Tijme Gommers’s amazing blog about how they were able to use VirusTotal to find and crack code signing certificates embedded in software samples:

<https://tij.me/blog/finding-and-utilising-leaked-code-signing-certificates/>

This is a gray area and definitely not advised for the average red team. It’s a jerk move to burn someone else’s certificate, even if they do suck at software design. Not to mention that VirusTotal subscriptions are insanely pricey!

## 🤔 **Kinda Legit — Get a Cert and Sign It!**

You can actually get a code signing certificate and sign your own malware with it. To get a trustworthy one, you will need to go through an “extended validation” process. That means you need to be a real company and show some documents to prove it. Per Digicert’s [website](https://docs.digicert.com/en/certcentral/manage-certificates/organization-and-domain-management/organization-validation.html), this validation process…

*“also includes verifying that the organization is not listed in any fraud,* ***phishing****, or government restricted entities, or anti-terrorism databases”*

The certs tend to range somewhere between $500-$1,000 per year. Of course, if you go this route, make sure to use your certificate sparingly to avoid losing it.

I’ve actually worked with a team that did this and we managed to keep the certificate for a couple of years without issues. We only used it for very targeted, individualized social engineering, but it was helpful for minimizing the warnings displayed to the targets and bypassing some EDR products.

## 👌**Probably Legit — Microsoft Signed (a.k.a. LOLBins/LOLBAS)**

Also frequently referred to as “application whitelisting bypasses”, these are binaries that come standard on a range of Windows operating systems. Many of them can execute code or scripts:

<https://lolbas-project.github.io/#/execute>

Over the years, I’ve gotten some insane mileage out of these utilities and I find that many of them still work to bypass a surprising number of EDR products. VBscript is still alive and well as an initial access vector, so don’t forget about it!

## ✅ **Pretty Legit! — Sideloading**

Sideloading is another way we can execute our code from within a trusted signed binary. The trick here is to use DLL search order to trick a legitimate binary into loading and executing our malicious code. At the time of this writing, this seems to be the primary method of ceding access for the team here at SpecterOps. Nick Powers and Steven Flores published a [blog](/less-smartscreen-more-caffeine-ab-using-clickonce-for-trusted-code-execution-1446ea8051c5) on the subject, spoke at [Defcon](https://www.youtube.com/watch?v=cyHxoKvD8Ck), and released [tools](https://github.com/0xthirteen/AssemblyHunter) to help with the discovery and exploitation process. More specifically, they demonstrate how to sideload ClickOnce applications. Keep in mind that you can use a very similar process to sideload other binaries as well. The SpecterOps team has found many ways to sideload some very popular software. I would highly recommend digging around on your own system for sideloading opportunities.

## 💯**Totally Legit — Screen Sharing/Meeting Apps**

Did you know that, by default, you can share your screen on Microsoft Teams to users outside of your organization? I guess this kind of makes sense to help collaboration during meetings with other companies, but did you know you can then “Give Control” to an outsider: as in, hand over your mouse and keyboard inputs to a person outside your organization? And they can drive around your desktop willy-nilly. Sick!

Apparently, this is a totally legitimate feature of Teams and it’s allowed by default even for outsiders. I’ve used this feature to perform entire purple team exercises just over Teams as the method of ceded access. There are several other popular screen sharing and meeting apps that have similar features. Of course, put me behind a keyboard, and I’ve suddenly got way more options of how t...