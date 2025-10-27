---
title: Google Project Zero Changes Its Disclosure Policy
url: https://www.schneier.com/blog/archives/2025/08/google-project-zero-changes-its-disclosure-policy.html
source: Schneier on Security
date: 2025-08-09
fetch_date: 2025-10-07T00:49:42.586033
---

# Google Project Zero Changes Its Disclosure Policy

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

## Google Project Zero Changes Its Disclosure Policy

Google’s vulnerability finding team is again [pushing the envelope](https://www.infosecurity-magazine.com/news/google-report-new-vulnerabilities/) of responsible disclosure:

> Google’s Project Zero team will retain its existing 90+30 policy regarding vulnerability disclosures, in which it provides vendors with 90 days before full disclosure takes place, with a 30-day period allowed for patch adoption if the bug is fixed before the deadline.
>
> However, as of July 29, Project Zero will also release limited details about any discovery they make within one week of vendor disclosure. This information will encompass:
>
> * The vendor or open-source project that received the report* The affected product* The date the report was filed and when the 90-day disclosure deadline expires

I have mixed feelings about this. On the one hand, I like that it puts more pressure on vendors to patch quickly. On the other hand, if no indication is provided regarding how severe a vulnerability is, it could easily cause unnecessary panic.

The problem is that Google is not a neutral vulnerability hunting party. To the extent that it finds, publishes, and reduces confidence in competitors’ products, Google benefits as a company.

Tags: [disclosure](https://www.schneier.com/tag/disclosure/), [Google](https://www.schneier.com/tag/google/), [patching](https://www.schneier.com/tag/patching/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/)

[Posted on August 8, 2025 at 7:01 AM](https://www.schneier.com/blog/archives/2025/08/google-project-zero-changes-its-disclosure-policy.html) •
[8 Comments](https://www.schneier.com/blog/archives/2025/08/google-project-zero-changes-its-disclosure-policy.html#comments)

### Comments

ResearcherZero •
[August 8, 2025 8:48 AM](https://www.schneier.com/blog/archives/2025/08/google-project-zero-changes-its-disclosure-policy.html/#comment-447040)

@Bruce

Google has been known to wait a few months before disclosing their own incidents, after publishing incidents at other firms first. Perhaps they should lead by example by first reporting their own breaches and providing a heads-up to others about the vulnerabilities.

‘https://cloud.google.com/blog/topics/threat-intelligence/voice-phishing-data-extortion

ResearcherZero •
[August 8, 2025 9:21 AM](https://www.schneier.com/blog/archives/2025/08/google-project-zero-changes-its-disclosure-policy.html/#comment-447043)

Oh, and open source their products in a manner which is actually “open”. This would stop filling the world with e-waste, as EOL equipment could actually be patched. Something every company could do if they were kind enough to open their propriety firmware, allowing proper scrutiny and the patching of all those long outstanding vulnerabilities they never patched.

All that mined consumer data belongs to the consumer, not the company. Pretend you care.

[Derek Jones](https://shape-of-code.com) •
[August 8, 2025 10:32 AM](https://www.schneier.com/blog/archives/2025/08/google-project-zero-changes-its-disclosure-policy.html/#comment-447046)

The data clearly shows that the shortest survival rate of discovered vulnerabilities are those that follow the sequence “private-patched-public” (at least in the first few years of 2000): <https://shape-of-code.com/2016/10/05/does-public-disclosure-of-vulnerabilities-improve-vendor-response/>

Clive Robinson •
[August 8, 2025 10:34 AM](https://www.schneier.com/blog/archives/2025/08/google-project-zero-changes-its-disclosure-policy.html/#comment-447047)

@ Bruce, ALL,

With regards,

> “I have mixed feelings about this. On the one hand, I like that it puts more pressure on vendors to patch quickly. On the other hand, if no indication is provided regarding how severe a vulnerability is, it could easily cause unnecessary panic.”

I too have mixed feelings.

However there has been little or no choice in changing things.

As most here will know Microsoft got hit with zero days as little as 24hours after a patch was released.

We still do not know if,

1, The patch was rapidly reverse engineered.

The simple fact is Microsoft only had one of three “on premises” patches done, and their Cloud Service patched.

Whilst it is known that “Reverse Engineering Patches” is a known attacker activity… Doing it in not just a day for the vulnerability patched but also finding related vulnerabilities in the code base appears almost impossible…

But is it?

The answer if you think about it is “NO” as finding related vulnerabilities can be done by pattern matching with a little stochastic input.

Which as I’ve previously mentioned is almost ideal work for Current AI LLMs.

The hard part is going to be finding and optimising a new ML transformer.

And I fully expect this to be a “Hot Research” subject where AI on boarding is giving multi-million dollar offers.

And that’s the issue, Current AI systems are well suited to doing “Reverse Engineering” of patches to find the actual instance of the vulnerability. And due to so much “Code Reuse” “Technical debt” there will almost certainly be other instances in the same class of vulnerability, or close classes.

Thus 90days may not be a luxury we can live with any longer…

[Ian McKellar](https://ian.mckellar.org) •
[August 8, 2025 4:07 PM](https://www.schneier.com/blog/archives/2025/08/google-project-zero-changes-its-disclosure-policy.html/#comment-447055)

> The problem is that Google is not a neutral vulnerability hunting party. To the extent that it finds, publishes, and reduces confidence in competitors’ products, Google benefits as a company.

Half the vulnerabilities listed as being subject to this new policy are in Google products. Holding Google to the same standard as other vendors is critical to Project Zero’s credibility.

mw •
[August 11, 2025 1:41 AM](https://www.schneier.com/blog/archives/2025/08/google-project-zero-changes-its-disclosure-policy.html/#comment-447080)

Everyone is talking about vulnerabilities and patching. Noone is talking about secure software and quality assurance. Esp. Microsoft and others release bloatware. There is a number of bug in every 1,000 lines of code. The more code the more bugs and every vulnerability is in fact a bug and has to be fixed immediately. Reducing the code size and removing unneccessary parts will make software more secure and even reduces the number of 0-days.

Jaime •
[August 11, 2025 12:48 PM](https://www.schneier.com/blog/archives/2025/08/google-project-zero-changes-its-disclosure-policy.html/#comment-447105)

> Noone is talking about secure software and quality assurance.

Sure they are. For example, OWASP has managed to convince the developers of the world to create fewer injection bugs. However, we’re still the type of industry where the companies that ignore security, and manage to get lucky enough to not be publicly embarrassed by a breach,...