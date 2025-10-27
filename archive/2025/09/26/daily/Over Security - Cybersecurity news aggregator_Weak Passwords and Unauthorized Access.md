---
title: Weak Passwords and Unauthorized Access
url: https://www.adainese.it/blog/2021/03/18/weak-passwords-and-unauthorized-access/
source: Over Security - Cybersecurity news aggregator
date: 2025-09-26
fetch_date: 2025-10-02T20:44:11.305405
---

# Weak Passwords and Unauthorized Access

# [Andrea Dainese](/)

* [Home](/)
* [About](/#about)
* [Blog](/blog)
* [Categories](/categories)

# Weak Passwords and Unauthorized Access

#### Table of contents

* [We Have a Problem](#we-have-a-problem)
* [How Attackers Think About Passwords](#how-attackers-think-about-passwords)
* [The Risks of Weak Passwords](#the-risks-of-weak-passwords)
* [How *Not* to Choose a Password](#how-not-to-choose-a-password)
* [Attacks Against Passwords](#attacks-against-passwords)
* [Choosing and Managing Passwords](#choosing-and-managing-passwords)
* [Awareness and Training](#awareness-and-training)
* [Conclusions](#conclusions)

#### Latest posts

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/10/01/circular-dependencies-with-ndo/)

[Circular Dependencies with NDO](/blog/2025/10/01/circular-dependencies-with-ndo/)
October 01, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)

[Modifying an object in Strata Cloud Manager](/blog/2025/09/28/modifying-an-object-in-strata-cloud-manager/)
September 28, 2025

[![Post cover](/images/categories/learning-paths.webp)](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)

[From Single-Site to Multi-Site with NDO](/blog/2025/09/24/from-single-site-to-multi-site-with-ndo/)
September 24, 2025

[![Post cover](/images/vendors/paloalto.webp)](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)

[Retrieving firewall interfaces with Strata Cloud Manager](/blog/2025/09/21/retrieving-firewall-interfaces-with-strata-cloud-manager/)
September 21, 2025

[![Post cover](/images/vendors/eve-ng.webp)](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)

[EVE-NG Linux VM SSH troubleshooting](/blog/2025/09/20/eve-ng-linux-vm-ssh-troubleshooting/)
September 20, 2025

#### Categories

[![Category cover](/images/categories/automation.webp)](/categories/automation)

[Automation](/categories/automation)
 159 posts

[![Category cover](/images/categories/learning-paths.webp)](/categories/learning-paths)

[Learning paths](/categories/learning-paths)
 123 posts

[![Category cover](/images/categories/ciso.webp)](/categories/ciso)

[CISO](/categories/ciso)
 23 posts

[![Category cover](/images/categories/personal-security.webp)](/categories/personal-security)

[Personal Security](/categories/personal-security)
 22 posts

[![Category cover](/images/categories/security.webp)](/categories/security)

[Security](/categories/security)
 20 posts

[![Category cover](/images/categories/notes.webp)](/categories/notes)

[Notes](/categories/notes)
 19 posts

[![Category cover](/images/categories/infrastructure.webp)](/categories/infrastructure)

[Infrastructure](/categories/infrastructure)
 12 posts

[![Category cover](/images/categories/ot-ics.webp)](/categories/ot-ics)

[OT/ICS](/categories/ot-ics)
 5 posts

[![Category cover](/images/categories/books.webp)](/categories/books)

[Books](/categories/books)
 3 posts

[![Category cover](/images/categories/unetlab.webp)](/categories/unetlab)

[UNetLab](/categories/unetlab)
 3 posts

[![Category cover](/images/categories/writeup.webp)](/categories/writeup)

[Write-up](/categories/writeup)
 3 posts

[![Category cover](/images/categories/osint.webp)](/categories/osint)

[OSInt](/categories/osint)
 2 posts

[![Category cover](/images/categories/life.webp)](/categories/life)

[My life](/categories/life)
 1 posts

## Weak Passwords and Unauthorized Access

Andrea Dainese

March 18, 2021

[CISO](/categories/ciso/ "All posts under CISO"),
[Personal Security](/categories/personal-security/ "All posts under Personal Security")

[![Post cover](/blog/2021/03/18/weak-passwords-and-unauthorized-access/password.webp)](/blog/2021/03/18/weak-passwords-and-unauthorized-access/password.webp)

A few months ago, a new “collection” of data breaches began circulating: someone had taken the time to aggregate cleaned-up data from multiple past breaches into a single consolidated database.
The result was a well-organized archive containing more than a billion email addresses and corresponding passwords.

This was nothing new, but due to its compact size and structured format, the dataset became particularly interesting to analyze.

## We Have a Problem

While reviewing the file, it became clear that we face a significant issue: **many people still do not understand how to manage passwords or the importance of doing so.**

Analyzing only a small, yet statistically significant portion of the database revealed that **the chosen passwords were extremely weak.**

[![Most commonly used password in 2020](/blog/2021/03/18/weak-passwords-and-unauthorized-access/most-used-passwords.webp)](/blog/2021/03/18/weak-passwords-and-unauthorized-access/most-used-passwords.webp)

The problem is serious because **the same careless behavior individuals use in their private lives often extends into the workplace**. This means that not only are individuals exposing themselves to risks such as identity theft, but **they are also exposing their companies to corporate security breaches.**

It’s time to go back to the basics.

## How Attackers Think About Passwords

From the attacker’s perspective, the reasoning is straightforward:

1. Define an objective (often financial gain).
2. Assess possible targets that can help achieve that objective.
3. Select targets that optimize effort—those most vulnerable or with the most available information.
4. Execute the attack.

With access to public online tools, past data breaches, and marketplaces on the Darknet, attackers can easily identify potential victims. Using exposed passwords and personal information, they gain a significant advantage.

## The Risks of Weak Passwords

By obtaining one or more passwords for a target, an attacker can infer patterns in the target’s thinking. They can then attempt to access services using known or predictable credentials.

The risks are clear:

* For individuals: **account takeover and identity theft**.
* For organizations: **unauthorized access** to IT and telecommunication systems (as defined in 615-ter of the Italian penal code).

This may sound like a distant threat, but the hyper-digital nature of today’s world has led to an exponential increase in **account theft reports**. For organizations, this often manifests as **anomalous login activity.**

## How *Not* to Choose a Password

When creating passwords, many people believe they are being clever, but they often:

* Fail to realize how common their logic actually is.
* Underestimate the likelihood of being targeted.
* Overlook the consequences of a focused attack.
* Use trivial passwords (e.g., `margherita`).
* Use predictable keyboard sequences (e.g., `1q2w3e4r`).
* Apply “creative” formulas they believe to be unbreakable (e.g., `googleLaVita3Bella`).
* Reuse the same password across multiple sites.

We must face reality: **every account containing personal data has value.** The real question is *how much value*—and in the case of email or social media accounts, the answer is generally **a lot**.

From a corporate perspective, requiring users to set at least 12-character alphanumeric passwords with uppercase, lowercase, and special symbols often results in passwords like `PizzaMargherita2012!`.

## Attacks Against Passwords

Let’s return to the attacker’s perspective. Given the available information:

* If a target reuses the same password across services, a single data breach exposes **all their accounts**—including corporate ones.
* If a target uses an algorithmic pattern, once one or two passwords are leaked, an attacker can deduce the formula and generate future credentials.
* If a password is simple, brute force attacks (using ordered probability dictionaries) can crack it quickly.

In nearly all cases, attackers can compromise at least some accounts.

## Choosing and Managing Passwords

Given the threat landscape, each account must be protected by a password that is:

* **Unique**: otherwise, one breach compromis...