---
title: The Fix That Wasn't: Why Outsourced Dev Teams Are Your Biggest Security Risk
url: https://pentester.ca/blog/outsourced-dev-teams
source: Over Security
date: 2026-11-15
fetch_date: 2026-11-16T08:48:45.024106
---

# The Fix That Wasn't: Why Outsourced Dev Teams Are Your Biggest Security Risk

[Skip to main content](#main)

[](/assets/images/Orbs/PT_Orb_LoopDark.webm)
![](/assets/images/Logos/Pentester.ca_Full_Logo_Dark.svg)

[](/assets/images/Orbs/PT_DarkPink_Orb.webm)

* Based in Tokyo,
  [E: [email protected]](/cdn-cgi/l/email-protection#9cebf4f5e8f9f4fde8dcecf9f2e8f9efe8f9eeb2fffd)
* Japan
  --:--:-- (GMT+9)

* [Home](/)
* [What You Get](/#what-you-get)
* [Why Hire Me?](/#why-hire-me)
* [Who Have I Helped?](/#who-helped)
* [The Feedback](/#feedback)
* [Blog](/blog)
* [Contact](#contact)

[![Pentester.ca - home](/assets/images/Logos/Pentester.ca_Full_Logo_Light.svg)](/)

[![](/assets/images/Title_Element_Black.svg)
BLOG](/blog)

# The Fix That Wasn't: Why Outsourced Dev Teams Are Your Biggest Security Risk

By Kaeden | Pentester.ca | March 31, 2026

There's a conversation I have over and over again. A company hires an agency to build their app. The app ships. It works. Everyone is happy. Then someone like me takes a look, and the whole thing falls apart. And you better hope it's someone like me, not someone who wants to exploit it.

This isn't about where developers are located. Talented engineers exist everywhere. This is about a business model where agencies are incentivized to ship features fast, security isn't in the contract, and nobody checks the work.

## The Agency That Left Every Database Open

A YouTuber with way over 10 million subscribers hired an agency to build a website with user accounts. The agency left the entire database wide open. User data, admin functionality, everything exposed. When I looked into the agency's other work, every single app in their portfolio had the same problem: open databases with no security rules, whether they were using Firebase or Supabase. Six apps, six open databases. One was leaking signed contracts and government-issued ID photos.

When the agency realized I was looking at their other projects, they banned my IP address and briefly took their own website offline to hide the evidence. The client cut ties immediately. The agency acted like they were still hired.

When I confronted the agency, they blamed their clients for not configuring the database security, even though the agency built the apps, chose the platforms, set up the databases, and never told their clients security rules were their responsibility. I had to step in and explain that securing the database is part of building the app.

From what I've seen, agencies will often bend the truth or not give their clients the full picture. They'll downplay vulnerabilities, claim things are fixed when they aren't, or shift blame to avoid losing the contract. At the end of the day, they're focused on keeping the client paying, not on being honest about the state of the product. The client doesn't have the technical expertise to question them, so they get away with it. And the worst part? The people running these agencies often aren't technical either. The CEOs and founders are sales people, not engineers. They don't understand the vulnerabilities any better than the clients do. They're selling development services they can't quality-check themselves.

Almost a year later, I checked the agency's newer projects. Still open. New apps, new clients, same problem. They learned nothing.

And these aren't just small startups. Firebase and Supabase are being used to manage hundreds of thousands of vending machines, retail kiosks, and enterprise systems. I've seen Fortune 500 companies with misconfigured databases, and even major gaming peripheral companies. The same default-open database problem, at every scale imaginable.

I've seen the exact same pattern with other agencies. One that builds apps for companies in aviation, fitness, and food had open databases on every client project. When I reported it, they told me to stop contacting their clients directly. I've also found critical vulnerabilities in several apps that appeared on Shark Tank, all built by external agencies. One company's VP of Technology confirmed the flaws came from "the original version of the app, which was built by an external agency." These were funded companies that had been on national television, and their agencies shipped apps where anyone could log into anyone else's account.

## Authentication Theater

The most common vulnerability I find in outsourced apps: the agency implements a Google, Apple, or Facebook sign-in screen that looks legitimate, but behind the scenes, the app just sends the user's email or a public user ID to the server, and the server blindly trusts it as proof of identity. No actual verification happens. If I know your email, I can log in as you.

I've found this in many major apps, including dating apps with millions of users, smart home device companies where it gave access to home cameras, and more. I reported them all, of course. They mostly ended up fixing it, after months and months of back and forth.

## The Fix That Wasn't

When I report vulnerabilities, companies pass my findings to their agency. The agency says it's fixed. I retest. It's not fixed. This cycle can repeat three, four, five times.

The agency's developers often don't understand the vulnerability, even when I explain it in my own words, step by step, being as specific as possible. And sometimes, even after spelling it out, they ignore what I told them and implement it their own way. Which doesn't work. And then we're back to retesting.

Instead of actually fixing the problem, I've seen agencies add layers of security theater: blocking certain phones from using the app, encrypting network traffic with keys hidden in the app code, adding checks that only exist in the user interface. None of it fixes the underlying vulnerability. All it does is make it slightly more annoying to demonstrate the problem. I've lost count of how many times I walked through all of an agency's "security" layers on a social app and could still log in as any user at the end of it.

## What You Should Do

* Include security requirements in your agency contract. If it doesn't mention security, they won't prioritize it.
* Get a security assessment before launch, not after. It's cheaper than a breach.
* Verify fixes independently. When your agency says they've fixed a security issue, don't take their word for it.
* Own your own infrastructure. If the agency controls your cloud accounts and deployment, you have a bigger problem than code quality.

## The Bottom Line

Every week, I find products where a single request exposes thousands of users' personal data. Products where anyone can log in as anyone. Products where the developers left the door wide open and nobody ever checked.

The companies behind these products aren't negligent. They just trusted that the team they hired would handle security. That trust, more often than not, is misplaced.

[Get a Free Consultation
![](/assets/images/Top_Right_Arrow_Black.svg)](https://cal.com/whitehat/30min?user=whitehat)
[![](/assets/images/Top_Right_Arrow_Black.svg)Back to all posts](/blog)

## Read About My Work

* [![](/assets/images/Top_Right_Arrow_Black.svg)Blog](/blog)

© 2026 Designed by [PixelPonderer](https://pixelponderer.com/)

## Got Security?

[[email protected]](/cdn-cgi/l/email-protection#1d6a75746978757c695d6d787369786e69786f337e7c)

[Let's Connect
![](/assets/images/Top_Right_Arrow_Black.svg)](https://cal.com/whitehat/30min?user=whitehat)

## Where to Find Me

* [![](/assets/images/Top_Right_Arrow_Black.svg) LinkedIn](https://www.linkedin.com/in/kaeden69420/)

Based in Tokyo, Japan

Disclaimer: Got Vulnerabilities?® is a parody. Got Milk?® is a registered trademark of the California Milk Processor Board.