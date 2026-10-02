---
title: HashcatRosetta: Reading the Rosetta Stone of Password Cracking
url: https://trustedsec.com/blog/hashcatrosetta-reading-the-rosetta-stone-of-password-cracking
source: TrustedSec
date: 2026-10-01
fetch_date: 2026-10-02T07:49:17.665375
---

# HashcatRosetta: Reading the Rosetta Stone of Password Cracking

[Skip to Main Content](#main)

[TrustedSec](https://trustedsec.com/)

* [Solutions](https://trustedsec.com/solutions)

  ## Solutions

  Our custom solutions are tailored to address the unique challenges of different roles in security.

  [Solutions](https://trustedsec.com/solutions)

  + [01

    For Leadership

    We understand the challenges facing modern executives and develop solutions unique to leaders.](https://trustedsec.com/solutions/for-leadership)
  + [02

    For Operations

    We stay one step ahead to proactively safeguard our clients and partners.](https://trustedsec.com/solutions/for-operations)
  + [03

    For Infrastructure

    From architecture to resiliency and maintainability, we keep your tech aligned to best practices.](https://trustedsec.com/solutions/for-infrastructure)
  + [04

    For Assurance

    Our compliance experts guide partners through regulatory requirements to ensure standards are met.](https://trustedsec.com/solutions/for-assurance)
* [Services](https://trustedsec.com/services)

  ## Services

  From building to testing to hardening, our services support security at every stage.

  [Services](https://trustedsec.com/services)

  + [01

    Design

    Design an exceptional, custom security program alongside our security experts.](https://trustedsec.com/services/design)
  + [02

    Evaluate

    Evaluate your security program with proven assessment methodologies.](https://trustedsec.com/services/evaluate)
  + [03

    Harden

    Harden your security program with the help of our security experts.](https://trustedsec.com/services/harden)
  + [04

    Respond

    Respond to threats to your security program with the help of our security experts.](https://trustedsec.com/services/respond)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

  ## About Us

  Driven by purpose, fueled by experts.

  [About Us](https://trustedsec.com/about-us)

  + [01

    Our Team

    Meet our security experts.](https://trustedsec.com/about-us/our-team)
  + [02

    Our Partners

    Become a TrustedSec partner to help your customers anticipate and prepare for potential attacks.](https://trustedsec.com/about-us/our-partners)
  + [03

    News

    Our team is trusted by local and national media to be the subject matter experts for security news.](https://trustedsec.com/about-us/news)
  + [04

    Events

    See our upcoming webinars, conferences, talks, trainings, and more!](https://trustedsec.com/about-us/events)

Search

Menu

Search Input

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Solutions](https://trustedsec.com/solutions)
* [Services](https://trustedsec.com/services)
* [Research](https://trustedsec.com/research)
* [Blog](https://trustedsec.com/blog)
* [Resources](https://trustedsec.com/resources)
* [About Us](https://trustedsec.com/about-us)

Search

* [Contact Us](https://trustedsec.com/contact)
* [Report a breach](https://trustedsec.com/report-a-breach)

* [Blog](https://trustedsec.com/blog)
* [HashcatRosetta: Reading the Rosetta Stone of Password Cracking](https://trustedsec.com/blog/hashcatrosetta-reading-the-rosetta-stone-of-password-cracking)

October 01, 2026

# HashcatRosetta: Reading the Rosetta Stone of Password Cracking

Written by
Justin Bollinger

Password Audits
Penetration Testing
Artificial Intelligence (AI)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-Covers/HashcatRosettaPart2_WebHero.jpg?w=320&h=320&q=90&auto=format&fit=crop&dm=1790608995&s=cebf6da86d898994cc2f402aaef221cd)

Table of contents

* [Two Different Problems Solved by One Tool](#Problems)
* [Explaining a Rule](#Explaining)
* [Finding Out Which Rules Actually Work](#Finding Out Which Rules Actually Work)
* [Static Analysis Without Running Anything](#Analysis)
* [Reading Mask Files Too](#Reading)
* [How I Built it Wrong First](#Wrong)
* [Installing](#Installing)
* [How I Actually Use This](#Use)

Share

* Share URL
* [Share via Email](/cdn-cgi/l/email-protection#1a25696f78707f796e2759727f79713f282a756f6e3f282a6e7273693f282a7b686e7379767f3f282a7c6875773f282a4e686f696e7f7e497f793f282b3c7b776a2178757e6327527b6972797b6e4875697f6e6e7b3f295b3f282a487f7b7e73747d3f282a6e727f3f282a4875697f6e6e7b3f282a496e75747f3f282a757c3f282a4a7b69696d75687e3f282a59687b797173747d3f295b3f282a726e6e6a693f295b3f285c3f285c6e686f696e7f7e697f79347975773f285c7876757d3f285c727b6972797b6e6875697f6e6e7b37687f7b7e73747d376e727f376875697f6e6e7b37696e75747f37757c376a7b69696d75687e3779687b797173747d "Share via Email")
* [Share on Facebook](https://www.facebook.com/sharer.php?u=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhashcatrosetta-reading-the-rosetta-stone-of-password-cracking "Share on Facebook")
* [Share on X](https://twitter.com/share?text=HashcatRosetta%3A%20Reading%20the%20Rosetta%20Stone%20of%20Password%20Cracking%3A%20https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhashcatrosetta-reading-the-rosetta-stone-of-password-cracking "Share on X")
* [Share on LinkedIn](https://www.linkedin.com/shareArticle?url=https%3A%2F%2Ftrustedsec.com%2Fblog%2Fhashcatrosetta-reading-the-rosetta-stone-of-password-cracking&mini=true "Share on LinkedIn")

*Part 2 of 3. [Part 1](https://trustedsec.com/blog/whats-new-in-hate-crack-since-2-0) is the reference for everything new in hate\_crack since 2.0. This post is the deep dive into HashcatRosetta: what it does, how it works internally, and how it got built. Part 3 (coming soon) is the plumbing: where configuration lives now and why it moved, how releases get cut, and one very bad commit.*

When I first started cracking seriously, my rule game consisted of downloading a rule file, pointing hashcat at it, and hoping. It worked well enough that I never had a reason to look inside. Then one day, I did. This is line 53 of `best64.rule`, which ships with hashcat and which I had run more times than I can count:

`^e ^h ^t`

I stared at that for a while. Three prepends and the letters `e`, `h`, `t`, in an order that means nothing, and I could not have told you what it did to a single password. That's `best64`, not some cursed monster of a file I downloaded off a forum, but the rules hashcat itself ships as the sensible default. (It has 77 of them, incidentally. Not 64. Yes, I know the name is historical, and that it started life as an actual best 64 and grew from there. I'm going to keep being a curmudgeon about the arithmetic not matching the label.)

![](https://trusted-sec.transforms.svdcdn.com/production/images/Blog-assets/hate-crack_Bollinger/Fig01_Bollinger_HashcatRosetta.png?w=320&q=90&auto=format&fit=max&dm=1790608759&s=2e8b3ceb408a4fe56a6d787c0d136b2e)

Every Rule File I Have Ever run, Roughly

hashcat rules are effectively write-only. The syntax is dense on purpose, because these things execute on a GPU billions of times a second, but the result is a language most of us copy and paste without reading. And that's a problem bigger than embarrassment, because the whole premise of rule-based attacks is that *some rules earn their keep and most don't*. If you can't read them, you can't tell which is which, and you certainly can't tune them for the target in front of you.

To this end, I wrote [HashcatRosetta](https://github.com/bandrel/HashcatRosetta) to translate.

## Two Different Problems Solved by One Tool

HashcatRosetta does two related things. Separating them up front matters, because they solve different problems.

**It explains rules.** Give it a rule and a baseword and it walks you through the transformation one operation at a time. This is the dictionary half.

**It analyzes what your rules actually did.** Point it at hashcat's `--debug-mode 4` output and it tells you which rules were applied, how often, to how many distinct basewords, and how many unique candidates they produced. This is the half that changes your methodology, ...