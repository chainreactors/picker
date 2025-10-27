---
title: 2 Months of TabGuard
url: https://hackademix.net/2022/10/17/2-months-of-tabguard/
source: hackademix.net
date: 2022-10-18
fetch_date: 2025-10-03T20:07:26.082188
---

# 2 Months of TabGuard

[Skip to content](#content)

[![hackademix.net](https://hackademix.net/wp-content/uploads/2022/11/logo.png)](https://hackademix.net/)

[hackademix.net](https://hackademix.net/)

ma1 on NoScript, the Universe & Everything

# 2 Months of TabGuard

NoScript’s **Cross-tab Identity Leak Protection** (or “TabGuard”) is an experimental countermeasure against the [Targeted Deanonymization via the Cache Side Channel](https://leakuidatorplusteam.github.io/) attack by Mojtaba Zaheri, Yossi Oren and Reza Curtmola, presented at [Usenix Security in August 2022](https://www.usenix.org/conference/usenixsecurity22/presentation/zaheri).

It is loosely inspired by the Leakuidator+ browser extension proposed by the authors as a defense, but it’s designed to better integrate with Firefox and the Tor Browser and provide protection against variants of the attack not covered yet. When triggered, TabGuard suspends authenticated requests across related tabs and gives the user the ability to either “Load anonymously” (preventing the attack but also logging out from the target site) or “Load normally”, which may be required by some legitimate cross-site workflows such as online payments, single sign-on and 3rd party authentication systems.

![NoScript's Potential Identity Leak dialog](/wp-content/uploads/2022/10/tabguard1.png)

This protection is enabled by default on any Private Browsing window (and therefore in the Tor Browser), but can be disabled or enabled globally from the *NoScript Options>Advanced* panel.

![](https://hackademix.net/wp-content/uploads/2022/10/tabguard2.png)

[Released on August the 11th 2022](https://twitter.com/ma1/status/1557751019945299969), 2 months later this protection has proven its effectiveness against a whole class of cross-site leaks that currently find no mitigation in mainstream browsers.

Nonetheless, we keep researching ways to make it less obtrusive and approach new approaches to protect users against this kind of attacks. Stay tuned!

Published October 17, 2022

Categorized as [NoScript](https://hackademix.net/category/noscript/)

![](https://secure.gravatar.com/avatar/290e868e00e8429bf1624a461b8ef81e?s=85&d=monsterid&r=g)

## Post navigation

[Previous post

NoScript, Red or Blue? Whatever Suits You!](https://hackademix.net/2022/10/17/noscript-red-or-blue-whatever-suits-you/)

* [2 Months of TabGuard](https://hackademix.net/2022/10/17/2-months-of-tabguard/)
* [NoScript, Red or Blue? Whatever Suits You!](https://hackademix.net/2022/10/17/noscript-red-or-blue-whatever-suits-you/)
* [Contextual Policies & LAN Protection (ABE Quantum) in NoScript 11.3!](https://hackademix.net/2022/02/17/contextual-policies-lan-protection-abe-quantum-in-noscript-113/)
* [Welcome SmartBlock: Script Surrogates for the masses!](https://hackademix.net/2021/03/23/welcome-smartblock-script-surrogates-for-the-masses/)
* [CCleaner Wiping Out Firefox Extensions Data: Expected Fix & Work-Around](https://hackademix.net/2020/08/05/ccleaner-wiping-out-firefox-extensions-data-expected-fix-work-around/)

* [Anonymity](https://hackademix.net/category/anonymity/)
* [Mozilla](https://hackademix.net/category/mozilla/)
* [NoScript](https://hackademix.net/category/noscript/)
* [Personal](https://hackademix.net/category/personal/)
* [Politics](https://hackademix.net/category/politics/)
* [Security](https://hackademix.net/category/security/)
* [Uncategorized](https://hackademix.net/category/uncategorized/)

[![NoScript Logo](https://hackademix.net/wp-content/uploads/2022/11/noscript-logo-full-1280-1024x1024.png "Click here to go to the NoScript website")](https://noscript.net/)

[![hackademix.net](https://hackademix.net/wp-content/uploads/2022/11/logo.png)](https://hackademix.net/)

Proudly powered by [WordPress](https://wordpress.org/).