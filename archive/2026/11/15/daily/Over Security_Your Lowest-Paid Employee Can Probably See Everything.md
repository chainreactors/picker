---
title: Your Lowest-Paid Employee Can Probably See Everything
url: https://pentester.ca/blog/lowest-paid-employee
source: Over Security
date: 2026-11-15
fetch_date: 2026-11-16T08:48:45.196278
---

# Your Lowest-Paid Employee Can Probably See Everything

[Skip to main content](#main)

[](/assets/images/Orbs/PT_Orb_LoopDark.webm)
![](/assets/images/Logos/Pentester.ca_Full_Logo_Dark.svg)

[](/assets/images/Orbs/PT_DarkPink_Orb.webm)

* Based in Tokyo,
  [E: [email protected]](/cdn-cgi/l/email-protection#b6c1dedfc2d3ded7c2f6c6d3d8c2d3c5c2d3c498d5d7)
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

# Your Lowest-Paid Employee Can Probably See Everything

By Kaeden | Pentester.ca | April 2, 2026

Companies spend millions on firewalls, endpoint detection, and perimeter security. Then they give a part-time employee the keys to the kingdom.

This is one of the most common patterns I find in my security research, and one of the least talked about. It's not about hackers breaking in from the outside. It's about what's already accessible from the inside, to people who were never supposed to see it.

## The Pattern

I've found this at multiple Fortune 500 companies. The setup is always the same: a company has thousands of employees at different levels, from entry-level workers to regional managers to C-suite executives. They all log in to internal systems. And somewhere along the way, nobody checked what the lowest-level accounts can actually access.

At one company, a basic employee account could reach internal tools and third-party platforms that should have been restricted to corporate or management. Monitoring dashboards where application logs contained plaintext cloud infrastructure credentials. Live operational tracking across multiple countries. A security camera system for an entire region that only checked the user's first and last name in each request, no session token, no role verification. Internal research platforms with confidential business documents accessible to any authenticated user. And third-party services where the default credentials had never been changed.

That was just one company. I've found the same pattern at others.

Every one of these findings came from simply logging in and navigating to URLs that nobody thought to restrict. No exploits. No privilege escalation. Just access that was never supposed to be there. Internal tools, third-party integrations, vendor dashboards, all wide open to the lowest-level account in the organization.

## Why This Happens

Role-based access control is an afterthought. When companies build internal tools, they focus on making them work. Access control gets added later, if at all. The assumption is that only the "right" people will know the URL or have the context to use it. That assumption is wrong.

Internal tools don't get pentested. Security budgets go to customer-facing applications. The internal dashboard that 50,000 employees use every day? Nobody has ever tested what a curious entry-level worker can reach from it.

Third-party integrations inherit bad defaults. Companies plug in vendor tools, monitoring platforms, and management dashboards without auditing what access levels are exposed. The vendor sets permissive defaults because it's easier to support, and nobody on the company side ever tightens them.

Nobody thinks entry-level employees are a threat. This is the most dangerous assumption. It's not about whether your employees are malicious. It's about what happens when one of their accounts gets compromised. A phished credential for a part-time worker shouldn't give an attacker access to AWS keys, CCTV systems, and executive contact information. But at multiple Fortune 500 companies I've tested, it does.

## The Real Risk

This isn't a theoretical concern. According to Verizon's annual data breach report, 30% of breaches involve internal actors. BeyondTrust has reported that elevation of privilege has been the number one vulnerability category in Microsoft environments for five consecutive years. And the average cost of a breach involving compromised credentials is among the highest, because attackers with legitimate access are the hardest to detect.

When a phishing email lands in a part-time employee's inbox and they click the link, the attacker gets whatever that employee has access to. If that's just their own schedule and pay stubs, the damage is contained. If it's the CEO's contact information, live CCTV feeds, and cloud infrastructure credentials, you have a catastrophic breach from one compromised entry-level account.

## What You Should Do

* Audit what your lowest-level accounts can access. Log in as your most junior employee and see what you can reach. You will be surprised.
* Implement proper role-based access control on every internal tool. If a tool is meant for franchise owners, verify that the logged-in user is a franchise owner. Don't rely on people not knowing the URL.
* Pentest your internal tools, not just your customer-facing app. The attack surface behind the login page is often larger and less defended than anything on the public internet.
* Audit third-party vendor defaults. Every vendor integration, monitoring dashboard, and management portal should be reviewed for what access levels it exposes and to whom.
* Assume every account will be compromised. Design your access controls so that when an entry-level credential gets phished, the blast radius is as small as possible.

This is one of the areas I focus on in my security work, and one I think more companies need to take seriously. The biggest companies in the world are getting this wrong. I've seen it firsthand.

[Get a Free Consultation
![](/assets/images/Top_Right_Arrow_Black.svg)](https://cal.com/whitehat/30min?user=whitehat)
[![](/assets/images/Top_Right_Arrow_Black.svg)Back to all posts](/blog)

## Read About My Work

* [![](/assets/images/Top_Right_Arrow_Black.svg)Blog](/blog)

© 2026 Designed by [PixelPonderer](https://pixelponderer.com/)

## Got Security?

[[email protected]](/cdn-cgi/l/email-protection#2057484954454841546050454e5445535445520e4341)

[Let's Connect
![](/assets/images/Top_Right_Arrow_Black.svg)](https://cal.com/whitehat/30min?user=whitehat)

## Where to Find Me

* [![](/assets/images/Top_Right_Arrow_Black.svg) LinkedIn](https://www.linkedin.com/in/kaeden69420/)

Based in Tokyo, Japan

Disclaimer: Got Vulnerabilities?® is a parody. Got Milk?® is a registered trademark of the California Milk Processor Board.