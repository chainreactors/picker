---
title: Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It
url: https://thehackernews.com/2026/11/microsoft-paint-rce-fix-now-available.html
source: The Hacker News
date: 2026-11-06
fetch_date: 2026-11-07T08:02:13.790241
---

# Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It

#1 Trusted Cybersecurity News Platform

Followed by 5.80+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[Get Updates](#email-outer)

* [Home](/)
* [Newsletter](#email-outer)
* [Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Threat Intelligence](/search/label/Threat%20Intelligence)
* [Vulnerabilities](/search/label/Vulnerability)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Awards](https://awards.thehackernews.com/)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Awards](https://awards.thehackernews.com/)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg98jBiF1GNyn9ReXVuuNzrDrJ8-mdCvE5IhR6dUbEnucAAvmCW-lbjZmzjJx0EhFV2R6xhfph0uQ-cz4IO46xmarphU8oOZmuqbdHxTeosFZTJ45LN6VEQOAdLCFB_iwlP3t9_i9qiQqQua1oJMGmp5wILrYvUWRBTMAVJphcDt7Qo0Yi5gK9pIHhW5pAb/s728-nu-rw-lo-l85-e365/wiz-d.png)](https://thehackernews.uk/appsec-ai-readiness-d)

# [Microsoft Paint RCE Fix Now Available, but Windows Update Won't Deliver It](https://thehackernews.com/2026/11/microsoft-paint-rce-fix-now-available.html)

**Swati Khandelwal**Nov 06, 2026Vulnerability / Windows Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFEFFUv1MUNRoFx03Jcw0k5NZCU0EOf5qEpbvAEQoTSTzoxHWPk1rc7XgQeG1USPP9vVB0ePI_lzQLqBU5bHdQ7-YrwEXFo8gJwayqwCvCtcDrw1JYMxKYxieV3bcQeCRAJAxt8CRfifzMzL22_ab0Z0OxwWrNckC36gPEOnubZnzagv6DkV7iY4AQJfA/s1700-nu-rw-lo-l85-e365/paint-rce.jpg)

A fix for **CVE-2026-83844**, a remote code execution flaw in Windows Paint, is now in the Microsoft Store. Paint gets this fix only through a Store update, not through Windows updates.

The fixed build, 11.2609.401.0, was the newest Paint build in all ten countries The Hacker News checked today.

The flaw is an out-of-bounds read that could let an attacker run code over a network. Microsoft rates it as Important, with a CVSS score of 8.1, and says that a successful attack requires a deep understanding of the target system. The flaw was not known to be exploited or publicly disclosed when the company published it on October 13.

Brian Vitko of RFF, a device-management software maker, checked which Paint builds the Store offered in six countries earlier this week. He found that the newest in each was 11.2605.81.0, a build without the fix.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-governance-platform-d)

His test virtual machine has since moved to the fixed build on its own, through Store auto-update. That is one machine, and how quickly other PCs will get the build is not yet clear.

### Which Build Counts as Fixed

Microsoft's [security advisory](https://msrc.microsoft.com/update-guide/vulnerability/CVE-2026-83844) names 11.2609.401.0 as the fixed build. The CVE record for the flaw, which the company also publishes, still lists Paint as affected only below 11.2605.91.0. Its [NVD entry](https://nvd.nist.gov/vuln/detail/CVE-2026-83844) shows the same range.

So a scanner that reads the CVE record would treat any build from 11.2605.91.0 up as fixed. A copy at 11.2609.401.0 or later passes under both numbers.

As recently as last week, the advisory gave 11.2605.91.0 as the fixed build, according to a [forum question](https://learn.microsoft.com/en-us/answers/questions/6055591/microsoft-paint-11-2605-91-0) on Microsoft Q&A. The advisory's revision history still shows only its October 13 entry, with no note about the change.

### How to Check Every Copy of Paint

Paint, like other Store apps, is installed separately for each user account on a PC. Windows can also keep a provisioned copy that it installs for each new user. A check of only the signed-in account can miss older copies.

Vitko's [test write-up](https://getrff.com/blog/windows-paint-cve-2026-83844-store-fix-missing/) gives two commands to run in a PowerShell window opened as administrator. The first lists every user's copy of Paint, and the second lists the provisioned copy.

`Get-AppxPackage -AllUsers -Name Microsoft.Paint | Select-Object Version, @{ n = 'Users'; e = { $_.PackageUserInformation.UserSecurityId.Username -join ', ' } }`

`Get-AppxProvisionedPackage -Online | Where-Object DisplayName -eq 'Microsoft.Paint' | Select-Object Version`

For any copy below 11.2609.401.0:

1. Update Paint through the Store, or let the Store auto-update install the fixed build. In Intune and other device-management tools, the Store app update scan does this across many PCs.
2. Run both commands again and check that every copy shows 11.2609.401.0 or later.

The advisory lists no workaround or mitigation. Before the fix reached the Store, Vitko suggested removing Paint where nobody needs it, for every user and from the provisioned copy. He did not test that step.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/network-defense-dd)

### Attack Conditions and Exploitation Status

An attacker could exploit the flaw by sending "a specially crafted packet to an affected service over the network," the advisory says, but it does not name the service. The attack would require no sign-in and no user assistance.

The flaw was not in the Known Exploited Vulnerabilities catalog run by the U.S. Cybersecurity and Infrastructure Security Agency when The Hacker News checked today. The catalog was last updated earlier this week.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Microsoft](https://thehackernews.com/search/label/Microsoft), [Patch Management](https://thehackernews.com/search/label/Patch%20Management), [remote code execution](https://thehackernews.com/search/label/remote%20code%20execution), [Vulnerability](https://thehackernews.com/search/label/Vulnerability), [Windows Security](https://thehackernews.com/search/label/Windows%20Security)

⚡ Top Stories This Week

[![The Hacker News](data:image/svg+xml;base64...)

Leaked LiteLLM Master Key Let Attackers Steal GitHub Tokens and Hijack Release Pipeline](https://thehackernews.com/2026/10/leaked-litellm-master-key-let-attackers.html)

[![The Hacker News](data:image/svg+xml;base64...)

Chinese Hackers Use AI-Powered ARTEX to Target Ov...