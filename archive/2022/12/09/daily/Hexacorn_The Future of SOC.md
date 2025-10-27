---
title: The Future of SOC
url: https://www.hexacorn.com/blog/2022/12/08/the-future-of-soc/
source: Hexacorn
date: 2022-12-09
fetch_date: 2025-10-04T00:59:20.296482
---

# The Future of SOC

[Skip to primary content](#content)

# [Hexacorn](https://www.hexacorn.com/blog/)

## Hexacorn

Search

### Main menu

* [Home](https://www.hexacorn.com/)
* [Services](https://www.hexacorn.com/services.html)
* [Products & Freebies](https://www.hexacorn.com/products_and_freebies.html)
* [Case Studies](https://www.hexacorn.com/case_studies.html)
* [Contact Us](https://www.hexacorn.com/contact.html)

### Post navigation

[← Previous](https://www.hexacorn.com/blog/2022/12/03/using-make_sc_hash_db-py-to-create-api-hashing-dbs/)
[Next →](https://www.hexacorn.com/blog/2022/12/09/marrying-client-side-windows-based-cryptencrypt-and-server-sidelinux-based-cryptopensslrsa/)

# The Future of SOC

Posted on [2022-12-08](https://www.hexacorn.com/blog/2022/12/08/the-future-of-soc/ "11:32 pm")  by  [adam](https://www.hexacorn.com/blog/author/adam/ "View all posts by adam")

Over last few years we moved away from a SOC that used to be almost solely focused on Network and Windows events and artifacts (probably a strong fintech bias here) towards the one that is a Frankenstein’s monster we see today – very fractured, multi-dimensional, multi-platform, multi-architectural, multi-device and multi-everything-centric, plus certainly multi-regional (regulated markets, data across borders)/privacy-savvy, on- and off-prem, covering \*aaS and endpoints/servers/mobile/virtualization/containers/CI/CD pipelines, and did I mention multi-cloud, public and private environments, vendor vs. proprietary, with a bonus of over-eager employees who keep sending ‘dangerous’ stuff to SOC because they have been trained well to report <insert any suspicious events here>’ ? And finally, one where NO ONE knows anymore at least the basics of all the existing, rapidly emerging, and more and more confusing technologies, let alone the gamut of ideas and solutions that help to address (or, at least detect) many of these security problems.

I think we moved away from a fairly understood model known between … let’s say 2000-2018 /COMFORTABLE/ towards the one that is (as of today at least) 2018-+ full of unknown unknowns /VERY UNCOMFORTABLE/…

How do we deal with it today?

Usually a bridge, a Slack or Teams channel with 100-200 people on it.

I think divide and conquer is the only way to deal with it. Also, more and more work has to focus on building bridges with internal owners of technologies / architects than ever before. This includes for instance, a lot of DevSecOps work, shifting left, early involvement in app development improvement and their release cycles, security-oriented feature and LOG requests, heavy red-team footprint on breaking it all, and in opposition to the previous decade – lots of very hands-off work. Lots of commanding and coordination.

Borrowing the quote from [dre](https://twitter.com/AndreGironda) – *Blue Teaming is 90 percent social capital today*.

Times have definitely changed…

And in parallel:
– stronger than ever reliance on vendors
– real (as in ‘old school’) cyber skills are in a strong decline — what took years to acquire and master is now gamified by vendor offerings that dumbify a lot of problems and requirements; I am not against it, because we need help and while sometimes it comes in a form of a b/s and extrapolations, we must admit that many non-technical analysts today, even w/o reading a single RFC in their life can easily handle many incidents by just… talking and via vendor consoles – this would be impossible 10 years ago
– seriously, tools of today are fantastic: advanced sandboxes, threat intel portals, bug bounty portals, and the whole social media sharing makes it far easier to find and share information that used to be available only to a few in the past
– the environments get more complicated — we need to work towards universal playbooks that cover heavily regulated regional markets
– portability is the key (work in one place -> work everywhere w/o many changes) — affects multiple instances of systems of records, SOPs, detections, metrics (again, regional/regulated markets, plus ability to quickly recover in case of a breach)
– follow the Sun is now more complicated as it includes Follow the Regulated Market
– from log deprivation to log over-saturation — time for some log governance, at source? common models for field naming? not only naming conventions, but also … and I really mean it… one, common, universal, … TIMESTAMP FORMAT?
– optimization efforts should be a norm — most of detection engineering, threat hunting teams add to the workload, we need an opposite force that asks — hmm is it really necessary? the same goes for a ruthless approach towards an email fatigue — convert to tickets or kill at source, disable, decommission
– how many emails your workflow and automation is sending today? can you trim it down?

—

The above is what scares me. It’s currently hardly manageable, and it’s not sustainable. It’s a whack-a-mole on steroids. We were meant to stop the whack-a-mole. And it not only happens now, it has intensified a lot in recent years and imho this trend will continue. When we all started to really like the idea of having EDRs at our disposal… the \*aaS happened and there is no way back. Suddenly all our incident response playbooks, SOPs need to focus on a completely different type of threats. Lots of this work is actually more focused on a proper access management than infiltration by APT actors via well-known TTPs. A lot of work is also focused on shared responsibility — when you deal with alerts on-prem, on endpoints, it’s all nice and cozy, but when you are \*aaS, there is a moment where an external password spray hitting the client application ran on the server you host, one has to decide when the transfer of security responsibility occurs. Is it a threat to the hosting environment? The instance of the app? Both? It’s… complicated.

What is the SOC of the future?

I think there is no SOC in the future. There is a cross-organizational incident response committee (you don’t wanna know how much I hate this word!) that actively engages in tackling issues at hand, and ‘incident commands’ respective teams leading the issues to a closure. Security becomes part of the day to day operations. Representatives from many functions actually are talking to each other, often, and the ‘old security’ in isolation is no longer a topic of any conversations. What is though, is addressing the ‘are we affected’ question on VERY REGULAR BASIS? To help with that, advanced Asset inventories covering hardware, software, \*aaS, SBOMs, packages, all aiming at exposure assessment and potential containment & closing communication loops are a MUST. It’s no longer a strictly speaking, a technical problem. It’s a problem that has a stage, that stage is not only political, but also visionary. Whoever does the minimum effort to collect and maintain the best asset inventory, then predict, plan to contain, and finally close, will be the winner of the many brownie points to be distributed in this area in the future.

And that’s why the future belongs to TRIAGE function.

That Omelas child, the punchbag, the scapegoat. The first line of defense, and the most important. Yet so often neglected.

Clear SOPs for Triage will help to handle most of incoming ‘requests’. You want that Triage team to be supported as hell. Their procedures must be simple, to the point, and with clear paths of both closure and escalation. Such triage function will train the best IR practitioners of the future. Jacks of all trades, outspoken, cooperative, and assertive.

The game is changing and we need to adapt. It’s time you take your Triage team out for a good dinner.

This entry was posted in [Incident Response](https://www.hexacorn.com/blog/category/incident-response/), [SOC](https://www.hexacorn.com/blog/category/soc/), [Triage](https://www.hexacorn.com/blog/category/triage/) by [adam](https://www.hexacorn.com/blog/author/adam/). Bookmark the [permalink](https://www.hexacorn.com/blog/2022/12/0...