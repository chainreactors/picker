---
title: Bitlocker, the FBI, and Risk
url: https://shostack.org/blog/bitlocker-the-fbi-and-risk/
source: Shostack & Friends Blog
date: 2026-01-23
fetch_date: 2026-01-24T03:31:29.065925
---

# Bitlocker, the FBI, and Risk

[Skip to main content](#main-content)

[![Shostack and Associates logo, click for Homepage](/img/Shostack-logo-white.png)](/)

* [About](/about/)
  + [Shostack + Associates](/about/)
  + [Adam Shostack](/about/adam/)
* [Services](/training/)
  + [Training](/training/)
  + [Accelerator](/secure-design-accelerator/)
  + [Expert Witness](/expert-witness/)
  + [Consulting](/consulting/)
* [Resources](/resources/)
  + [Overview](/resources/)
  + [Threat Modeling](/resources/threat-modeling/)
  + [Books](/books/)
  + [Games](/tm-games/)
  + [Cyber Public Health](/resources/cyber-public-health/)
  + [Lessons Learned](/resources/lessons/)
  + [Videos](/resources/videos/)
  + [Whitepapers](/resources/whitepapers/)
* [Blog](/blog/)
* [Contact](/contact/)

1. [Shostack + Associates](/)
2. [Blog](/blog/)
3. Bitlocker, the FBI, and Risk

Shostack + Friends Blog

# Bitlocker, the FBI, and Risk

What can the Bitlocker story tell us about risk?
![A bitlocker UI](/images/blog/img/2026/bitlocker-1000w.png)

There’s a story out, [Microsoft gave FBI a set of
BitLocker encryption keys to unlock suspects’ laptops](https://techcrunch.com/2026/01/23/microsoft-gave-fbi-a-set-of-bitlocker-encryption-keys-to-unlock-suspects-laptops-reports/).

Security is classically described as ensuring confidentiality,
integrity, and availability. These are often portrayed as a
triangle, with the properties in tension, and this story
illustrates why. When you encrypt data, you strengthen
confidentiality, and if you lose your key, the data is no longer available.

While I was at Microsoft, I had a lot of conversations about this
tradeoff, fearing outcomes like these. I often heard the argument
that the risk of data loss as people forget their key, pass away
without sharing it, or otherwise lose access to their data was bigger
than the risk of warrants. To be frank, I never had a great
counter-argument. We had plenty of data on support calls for lost
keys, plenty of enterprise customer conversations about key loss and
helpdesks, and few lawful access cases, especially as Bitlocker
rolled out.

The argument that key backup should not have been automatic is
stronger, but runs into usability complexity. (Do regular people
understand what encryption is? What a key is? What UI options they clicked
a few minutes ago?) All of this is happening as part of a very rapid
transition in how Microsoft wants you to think about your computer,
access to it via Microsoft Accounts, to your data via OneDrive, and
other elements of changing security boundaries.

I want to talk about this relative to the word “risk,” which we use
pretty naturally here. The first thing to ask is risk to whom? Data
loss was Microsoft’s “fault,” and we listened to people who’d lost their digital
lives. Everyone had stories of meeting people who were justifiably
distraught after a failure of some sort. Many of the stories I heard
of people losing access to their PCs were really heart-wrenching,
making the risk of data loss both available and salient.

The second thing to note is that, in a functioning liberal
democracy, the police investigate criminals, and have to go through a
process to meet rules like “No warrants shall issue, but upon probable cause,
supported by Oath or affirmation, and particularly describing the
place to be searched, and the persons or things to be seized.” And in
a functioning democracy, we expect that there are checks and balances
around such uses of government power. It’s easy to discount the rights
of suspects or criminals, or to minimize your obligation to protect
them like other customers. This ties into ‘who bears the risk?’

The third thing to note is that was easier, for most Microsoft
employees, to use a mental model of the police as friendly Redmond
police than a secret police force or goons busting down doors.

All of this leads to a mental model where the risk to Microsoft
takes precedence over the risk to people trying to keep their data
secret on their PCs.

If you’re paying very close attention, you’ll have noticed that I
did not use a single number in this discussion of risk. Had I included
numbers, especially for the police risks, they would have been magnets
for debate.

What I hope you take away from this is first, this is not a flaw in
Bitlocker, but rather an unavoidable security-security tradeoff
between availability and confidentiality. The second thing is: this is
not about “Microsoft good” or “Microsoft bad” but that risk management
processes need to be explicit about where the risk falls, that our
perceptions often play a role, and that standards that obligate a
company to “make risk decisions” may not have the results that their
authors want if those standards don’t specify risk to whom.

To be clear, I've been gone from Microsoft for
a long time, and do not speak for them.

Originally published by Adam on 23 Jan 2026

Categories:
  [risk](/blog/category/risk)
  [security](/blog/category/security)
  [threat modeling](/blog/category/threat-modeling)

## Our Favorite Content

[General threat modeling posts](/blog/category/threat-modeling/)

[The Security Principles of Saltzer and Schroeder, illustrated with Star Wars](/blog/the-security-principles-of-saltzer-and-schroeder/)

[Other Star Wars blog posts](/blog/category/star-wars/)

[Modeling attackers and their motives](/blog/modeling-attackers-and-their-motives/)

[Doing science with near misses](/blog/doing-science-with-near-misses/)

[Posts about Adam’s “Threats” book](/blog/category/threats-book/)

[Posts about Adam’s “Threat Modeling” book](/blog/category/threat-modeling-book/)

[Posts about “The New School of Information Security” book](/blog/category/the-new-school/)

[About this blog](/blog/about/)

## Subscribe (RSS/Mail)

RSS/ATOM: The RSS [feed is here](https://shostack.org/feed.xml). We recommend RSS as the best way to follow this blog, and think generally RSS is the best way to take control of the information you take in. You can [read our thinking here](https://shostack.org/blog/take-control-of-what-you-read/).

Email: If you’d like a lower volume set of updates on what Adam is doing, [Adam’s New Thing](/contact/) gets only a few messages a year, guaranteed. We include a subset of posts in each.

## Recent posts

[![A bitlocker UI](/images/blog/img/2026/bitlocker-175w.png)](/blog/bitlocker-the-fbi-and-risk/)

### [Bitlocker, the FBI, and Risk](/blog/bitlocker-the-fbi-and-risk/)

23 Jan 2026

What can the Bitlocker story tell us about risk?

[![Graph showing number of reports of GPS spoofing every year since 1998, with a significant steep increase in the last 3 years.](/images/blog/img/2026/SA-26-01-Fig2-NASA_Aviation_Safety_Report_data-175w.jpeg)](/blog/security-advisory-26-01-gps-attacks/)

### [Security Advisory SA-26-01 GPS Attacks](/blog/security-advisory-26-01-gps-attacks/)

22 Jan 2026

GPS attacks trigger revisiting threat models

[![Archimedes 2026 Healthcare Security Week banner](/images/blog/img/2026/HCSW_header_2026-175w.webp)](/blog/threat-modeling-essentials-archimedes-2026-hcsw/)

### [Threat Modeling Essentials at Archimedes 2026 Healthcare Security Week](/blog/threat-modeling-essentials-archimedes-2026-hcsw/)

14 Jan 2026

Threat Modeling Essentials, led by Adam Shostack, is a standout offering at Archimedes 2026 Healthcare Security Week, Feb 18 in Las Vegas.

[![A person with wires and dials coming out of their skull. They're in a library but chained to a desk and unable to reach books.](/images/blog/img/2026/take-control-of-what-you-read-redux-175w.png)](/blog/take-control-of-what-you-read-redux/)

### [Take Control of What you Read, Redux](/blog/take-control-of-what-you-read-redux/)

11 Jan 2026

In 2026, it’s more important than ever to take control of what you read

## Popular Blog Topics

[Threat Model Thursday](/blog/category/threat-model-thursday/),
exploring specific published threat models

[Threat Modeling](/blog/category/threat-modeling/) (general topic)

[Application Security](/blog/category/...