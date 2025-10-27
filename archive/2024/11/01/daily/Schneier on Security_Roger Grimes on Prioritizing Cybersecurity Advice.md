---
title: Roger Grimes on Prioritizing Cybersecurity Advice
url: https://www.schneier.com/blog/archives/2024/10/roger-grimes-on-prioritizing-cybersecurity-advice.html
source: Schneier on Security
date: 2024-11-01
fetch_date: 2025-10-06T19:19:45.977214
---

# Roger Grimes on Prioritizing Cybersecurity Advice

# [Schneier on Security](https://www.schneier.com/)

Menu

* [Blog](https://www.schneier.com)
* [Newsletter](https://www.schneier.com/crypto-gram/)
* [Books](https://www.schneier.com/books/)
* [Essays](https://www.schneier.com/essays/)
* [News](https://www.schneier.com/news/)
* [Talks](https://www.schneier.com/talks/)
* [Academic](https://www.schneier.com/academic/)
* [About Me](https://www.schneier.com/blog/about/)

### Search

*Powered by [DuckDuckGo](https://duckduckgo.com/)*

Blog

Essays

Whole site

### Subscribe

[![Atom](https://www.schneier.com/wp-content/uploads/2019/10/rss-32px.png)](https://www.schneier.com/feed/atom/)[![Facebook](https://www.schneier.com/wp-content/uploads/2019/10/facebook-32px.png)](https://www.facebook.com/bruce.schneier)[![Twitter](https://www.schneier.com/wp-content/uploads/2019/10/twitter-32px.png)](https://twitter.com/schneierblog)[![Email](https://www.schneier.com/wp-content/uploads/2019/10/email-32px.png)](https://www.schneier.com/crypto-gram)

[Home](https://www.schneier.com)[Blog](https://www.schneier.com/blog/archives/)

## Roger Grimes on Prioritizing Cybersecurity Advice

This is a [good point](https://www.linkedin.com/pulse/every-cybersecurity-list-should-risk-ranked-roger-grimes-ippze):

> Part of the problem is that we are constantly handed lists…list of required controls…list of things we are being asked to fix or improve…lists of new projects…lists of threats, and so on, that are not ranked for risks. For example, we are often given a cybersecurity guideline (e.g., PCI-DSS, HIPAA, SOX, NIST, etc.) with hundreds of recommendations. They are all great recommendations, which if followed, will reduce risk in your environment.
>
> What they do not tell you is which of the recommended things will have the most impact on best reducing risk in your environment. They do not tell you that one, two or three of these things…among the hundreds that have been given to you, will reduce more risk than all the others.
>
> […]
>
> The solution?
>
> Here is one big one: Do not use or rely on un-risk-ranked lists. Require any list of controls, threats, defenses, solutions to be risk-ranked according to how much actual risk they will reduce in the current environment if implemented.
>
> […]
>
> This specific CISA document has at least 21 main recommendations, many of which lead to two or more other more specific recommendations. Overall, it has several dozen recommendations, each of which individually will likely take weeks to months to fulfill in any environment if not already accomplished. Any person following this document is…rightly…going to be expected to evaluate and implement all those recommendations. And doing so will absolutely reduce risk.
>
> The catch is: There are two recommendations that WILL DO MORE THAN ALL THE REST ADDED TOGETHER TO REDUCE CYBERSECURITY RISK most efficiently: patching and using multifactor authentication (MFA). Patching is listed third. MFA is listed eighth. And there is nothing to indicate their ability to significantly reduce cybersecurity risk as compared to the other recommendations. Two of these things are not like the other, but how is anyone reading the document supposed to know that patching and using MFA really matter more than all the rest?

Tags: [cybersecurity](https://www.schneier.com/tag/cybersecurity/), [patching](https://www.schneier.com/tag/patching/), [two-factor authentication](https://www.schneier.com/tag/two-factor-authentication/)

[Posted on October 31, 2024 at 11:43 AM](https://www.schneier.com/blog/archives/2024/10/roger-grimes-on-prioritizing-cybersecurity-advice.html) •
[12 Comments](https://www.schneier.com/blog/archives/2024/10/roger-grimes-on-prioritizing-cybersecurity-advice.html#comments)

### Comments

Corwin Grey •
[October 31, 2024 12:18 PM](https://www.schneier.com/blog/archives/2024/10/roger-grimes-on-prioritizing-cybersecurity-advice.html/#comment-441429)

This is one reason I prefer the CIS 20 Critical Controls. They have done a great deal of work at prioritizing and ranking the controls by degree of migitation provided but left enough room for adjustments to order based on business process or requlatory requirements.

Peter •
[October 31, 2024 1:07 PM](https://www.schneier.com/blog/archives/2024/10/roger-grimes-on-prioritizing-cybersecurity-advice.html/#comment-441431)

Big yawn, the CISA doc is equally pie in the sky as the others, it just spun differently as a different audience. Also the speaker is definitely showing their DHS bias here, NIST 800-53 controls have long had “P” codes (1-3) which align to implementation priorities based on value and they supercede the CAT levels (i.e. sort by P code first, then fix based on CAT level within that P code grouping). The problem is like all government regulation, it can just get ignored by the agency heads and so it is, CISA didn’t fix that.

As for “OMG CISA has an effective fix doc”, big yawn. The Australian CISA equiv has been publishing that for two decades, <https://www.cyber.gov.au/resources-business-and-government/essential-cyber-security/essential-eight> …I believe you yourself Bruce noted that 15 or so years ago on this very blog.

[Roland Turner](https://rolandturner.com/) •
[October 31, 2024 9:40 PM](https://www.schneier.com/blog/archives/2024/10/roger-grimes-on-prioritizing-cybersecurity-advice.html/#comment-441443)

In the category of things infosec folks are terrible at (I’m not excluding myself)…

We all “know” that risk treatment must be on the basis of a risk evaluation and candidate-control cost/impact evaluation, prioritised to maximise bang for buck, but it’s hard to explain adequately in a soundbite, or even in a several-page guide. The result is pre-digested lists of baseline controls against **common** risks.

The difficult problem is that the overwhelming majority of organisations are too small to have the expertise available to perform a realistic evaluation. Historically organisations that small were not a significant target population, but today they are. There’s a really awkward gap between individual/consumer-grade systems (secured directly by tech giants) and medium-large organisation systems where the expertise to evaluate and prioritise is available. Grimes’ point is valid, but is perhaps not addressing the problem that many [current] non-evaluated controls lists are aimed at.

Paul Sagi •
[November 1, 2024 5:05 AM](https://www.schneier.com/blog/archives/2024/10/roger-grimes-on-prioritizing-cybersecurity-advice.html/#comment-441450)

Regarding

<https://www.schneier.com/blog/archives/2024/10/roger-grimes-on-prioritizing-cybersecurity-advice.html>

The reason for ‘blanket’ lists of advice is that the purveyors of such advice can’t know the particular setup of each entity.

MFA and patching do have their place, although there are caveats:

Very important security safeguards are:
A) Anti-malware secure DNS (DoH, DoT, DNSSEC and Rebind protection). Note that not all secure DNS is anti-malware, most secure DNS offers no or little protection from malware. The best anti-malware secure DNS blocks 96% of malware.
B) A good bidirectional firewall, one which allows creation of custom rules.
C) Network segmentation
D) Air-gaps
E) Last (and least) is antivirus software, if malware is caught in your system by AV software you have already lost the war. (What other malware is in your system that the AV software did not detect?)

Keyloggers and RATs are a constant threat, keep them out of your network.

Depending on who you are, adversaries can be script kiddies, opportunistic scammers or nation-state actors.

The point of the above advice is to keep out threats as much as possible and isolate and contain the threats that do get in.

Peter Galbavy •
[November 1, 2024 5:20 AM](https://www.schneier.com/blog/archives/2024/10/roger-grimes-on-prioritizing-cybersecurity-advice.html/#comment-441451)

On first glance I agree with the sentiment, but then thinking a bit more I am not so sure. The ...