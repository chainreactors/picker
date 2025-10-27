---
title: Microsoft SharePoint Zero-Day
url: https://www.schneier.com/blog/archives/2025/07/microsoft-sharepoint-zero-day.html
source: Schneier on Security
date: 2025-07-29
fetch_date: 2025-10-06T23:58:08.940735
---

# Microsoft SharePoint Zero-Day

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

## Microsoft SharePoint Zero-Day

Chinese hackers are exploiting a high-severity vulnerability in Microsoft SharePoint to [steal data](https://arstechnica.com/security/2025/07/sharepoint-vulnerability-with-9-8-severity-rating-is-under-exploit-across-the-globe/) worldwide:

> The vulnerability, tracked as CVE-2025-53770, carries a severity rating of 9.8 out of a possible 10. It gives unauthenticated remote access to SharePoint Servers exposed to the Internet. Starting Friday, researchers began warning of active exploitation of the vulnerability, which affects SharePoint Servers that infrastructure customers run in-house. Microsoft’s cloud-hosted SharePoint Online and Microsoft 365 are not affected.

[Here’s](https://msrc.microsoft.com/blog/2025/07/customer-guidance-for-sharepoint-vulnerability-cve-2025-53770/) Microsoft on patching instructions. Patching isn’t enough, as attackers have used the vulnerability to steal authentication credentials. It’s an absolute mess. CISA has [more information](https://www.cisa.gov/news-events/alerts/2025/07/20/update-microsoft-releases-guidance-exploitation-sharepoint-vulnerabilities). [Also](https://unit42.paloaltonetworks.com/microsoft-sharepoint-cve-2025-49704-cve-2025-49706-cve-2025-53770/) [these](https://www.akamai.com/blog/security-research/sharepoint-vulnerability-rce-active-exploitation-detections-mitigations) [four](https://www.wired.com/story/microsoft-sharepoint-hack-china-end-of-life-updates/) [links](https://thehackernews.com/2025/07/hackers-exploit-sharepoint-zero-day.html). Two [Slashdot](https://it.slashdot.org/story/25/07/21/1523207/microsoft-releases-emergency-patches-for-actively-exploited-sharepoint-zero-days) [threads](https://news.slashdot.org/story/25/07/23/1652240/us-nuclear-weapons-agency-among-400-organizations-breached-by-chinese-hackers).

This is an unfolding security mess, and quite the hacking coup.

Tags: [exploits](https://www.schneier.com/tag/exploits/), [hacking](https://www.schneier.com/tag/hacking/), [Microsoft](https://www.schneier.com/tag/microsoft/), [vulnerabilities](https://www.schneier.com/tag/vulnerabilities/), [zero-day](https://www.schneier.com/tag/zero-day/)

[Posted on July 28, 2025 at 7:09 AM](https://www.schneier.com/blog/archives/2025/07/microsoft-sharepoint-zero-day.html) •
[21 Comments](https://www.schneier.com/blog/archives/2025/07/microsoft-sharepoint-zero-day.html#comments)

### Comments

Clive Robinson •
[July 28, 2025 10:09 AM](https://www.schneier.com/blog/archives/2025/07/microsoft-sharepoint-zero-day.html/#comment-446744)

@ Bruce,

With regards,

> “It’s an absolute mess”

You don’t make it clear if you mean this particular Microsoft Product, or Microsoft’s software production in general…

Recent attacks have happened on a severity of 9 or greater due to a myriad of failures in the way Microsoft design, prototype, produce, and support software.

In one case Microsoft trying to fix one fault, showed crackers –we presume from reverse engineering the Microsoft issued patch– how to find and exploit similar flaws in around a day…

The fact these attacks are being found, exploits created and put into action in such a short period of time seriously suggests that Microsoft and similar need to review the way they go about things.

Further, even though Current AI LLM and ML systems are fairly bad with software, they are compared to humans incredibly fast.

It is the nature of attack progress and software development that the direction is forward. Thus we can only expect Current AI performance with analysing and developing software to “improve”.

Thus it may not be long before “patch to fielded attack” is measured in minutes not hours.

AlexT •
[July 28, 2025 10:40 AM](https://www.schneier.com/blog/archives/2025/07/microsoft-sharepoint-zero-day.html/#comment-446745)

Am I correct that this only applies to on-site SharePoint?!

Stephen •
[July 28, 2025 11:41 AM](https://www.schneier.com/blog/archives/2025/07/microsoft-sharepoint-zero-day.html/#comment-446746)

Everything I’ve seen indicates this is only “on premises” deployments. SharePoint Online is (at this point) unaffected.

This seems to be a new threat model. If the time it takes to reverse-engineer an exploit from the patched binaries beats the time to test and deploy the patch into production, you’re screwed to the severity of the patched vulnerabilities.

One can envision encryption / obfuscation of the executable code to slow down automated analysis, but that performance penalty would also be borne by legitimate users.

Maybe all it takes to subscribe to a zero-day vulnerability newsletter are the license fees and the development and execution resources consumed by the automated analysis. If that’s the case, this is not a problem unique to Microsoft – unless they are releasing comparatively more patches that effectively increases the attack surface. But at least on paper, these attacks should work against any systems that receive patches from remote repositories.

lurker •
[July 28, 2025 2:40 PM](https://www.schneier.com/blog/archives/2025/07/microsoft-sharepoint-zero-day.html/#comment-446749)

@Stephen

Yup, and it exposes part of the puzzle: they use “on premises” SharePont to avoid the problems of the internet, yet they still drag the dirty ole internet in …

Clive Robinson •
[July 28, 2025 3:21 PM](https://www.schneier.com/blog/archives/2025/07/microsoft-sharepoint-zero-day.html/#comment-446750)

@ Stephen, ALL,

With regards,

> “If the time it takes to reverse-engineer an exploit from the patched binaries beats the time to test and deploy the patch into production, you’re screwed to the severity of the patched vulnerabilities.”

It’s actually “worse than that”.

When an exploit is discovered, it is always,

“An instance in a class of attacks”

This is due to the notion of “code reuse” in it’s various forms and especially in common functions like “serialisation”.

That is the class of attackable vulnerabilities is almost always bigger than just a single instance, and the number of instances will almost certainly grow with time and ongoing development.

Thus if it’s the first instance discovered in a new class there are almost certainly a significant number of instances of other attackable vulnerabilities in the class not just,

1, in the current code,
2, but in future code to come.

But also classes tend not to exist in isolation they tend to be grouped with related classes. Thus are in effect sub classes of a larger more general class.

So finding just one “new instance” means you have to fix not just,

1, that vulnerability,
2, but others in it’s class,
3, and related classes.

Which is apparently not what Microsoft did in rushing a patch out of the door they only fixed “the vulnerability”.

The allegadly Chinese attackers then reverse engineered the patch and found other vulnerabilities in the class or a closely related class.

My point abo...