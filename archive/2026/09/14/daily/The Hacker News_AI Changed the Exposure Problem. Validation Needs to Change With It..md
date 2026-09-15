---
title: AI Changed the Exposure Problem. Validation Needs to Change With It.
url: https://thehackernews.com/2026/09/ai-changed-exposure-problem-validation.html
source: The Hacker News
date: 2026-09-14
fetch_date: 2026-09-15T07:03:16.173702
---

# AI Changed the Exposure Problem. Validation Needs to Change With It.

#1 Trusted Cybersecurity News Platform

Followed by 5.70+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Get the Latest News](#email-outer)

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiHP9KRFkaxKFUKQNRU3CkfxCyJLEuIfmo6ov7iWHHRBE1ShJKfXdPvozMZMVuvOJipQ8Qbap3UBmtjKvZh-xBqLeUartPWmRuQj2W8nqdCk2_XlYLXpj15R4Du2oJ1nNVPqIuR-TwbMyPQe4gxxCcMYvUMbFO_Nin2OdhyzkJvX8Sn83aEbM1C5sgaaCqI/s728-nu-rw-lo-l85-e365/wiz-sep-d.png)](https://thehackernews.uk/claude-security-guide-d)

# [AI Changed the Exposure Problem. Validation Needs to Change With It.](https://thehackernews.com/2026/09/ai-changed-exposure-problem-validation.html)

**The Hacker News**Sep 14, 2026Vulnerability / Penetration Testing

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEid_ratIPK3F0IGyzyDTTPaV26Nnh4gQoFjS0ejR49J_tbGb92GgukT-Mnr9xv9mK7h0QSdeXujxiEtD0AqVKNmrKoG9BMEuut7CB1368iyt3Gr6Xu5mAdkDsUQC86K9GZ-Uw6qfPvYYr9BUvHzn014_rzQeMS5dCVXEwkRLs3eViylo5ChmZs6QQygxE4/s1700-nu-rw-lo-l85-e365/picus-main.jpg)

There's a lot of noise around AI and cybersecurity right now. What’s actually important is far simpler, if often lost in the hubbub. **Vulnerability discovery is getting faster and happening at a much greater scale, while defenders still have to work out which findings actually deserve their action.**

In the first half of 2026, a whopping 35,853 CVEs were published, [roughly 49%](https://zerodayclock.com/) more than in the year before. Yet only [495 were catalogued](https://www.vulncheck.com/blog/state-of-exploitation-1h-2026) as exploited in the wild during that same period, and 116 were already under attack on the day they became public. Meanwhile, Anthropic’s own [disclosure data](https://red.anthropic.com/2026/cvd/ledger/) shows Mythos-class models surfacing 26,153 vulnerability candidates in open-source software, with only [421 of those](https://red.anthropic.com/2026/cvd/) getting patched upstream.

That small exploited subset is a very important point. It tells defenders that **treating every vulnerability with a High or Critical CVSS rating as an emergency is not only impossible, it’s actually the wrong model**. The critical task security teams face is **deciding which exposures, on which assets, require immediate action**, especially as both the number of findings grows and the gap between disclosure and exploitation narrows.

## **The CVSS Alone Can’t Tell You What Matters in Your Environment**

The same CVE can affect hundreds of assets, but the **impact is rarely the same across them**. Some instances are unreachable. Some sit behind controls that interrupt the techniques required for exploitation. Others are exposed on business-critical systems where prevention fails, and detection never fires.

**The CVSS gives you a common severity baseline. It can’t give you the context that determines impact to your organization.**

This is why defenders need evidence from their own environment to find out whether the exposure is actually exploitable, which assets it affects, and whether those assets are reachable and important to the business. As vulnerability volume grows, this distinction becomes more and more important.

## **Automated Pentesting Alone Can’t Validate Every Exposure**

Once you move beyond severity scores, automated pentesting gives you some of the strongest evidence you can gather. It can run real exploits, prove that an exposure is exploitable in your environment, chain vulnerabilities, credentials, and misconfigurations into attack paths, and show how far an attacker could actually progress across your network.

Yet coverage remains limited in practice. **[Omdia research](https://go.synack.com/ai-pentesting-report-omdia)** **found that while 95% of organizations rank pentesting as a top or high priority, only 32% of their average attack surface is tested each year.** Agentic and automated approaches can expand that coverage, but they don’t remove every **constraint of live exploitation**.

**For CVE-based exploitation, a working exploit still has to exist, and the target has to be safe to test.** Newly disclosed CVEs may have no working exploit yet, while it simply may not be possible to test a live exploit on business-critical, restricted, and air-gapped assets. Those exposures still need an exploitability verdict, even when there’s nothing an automated pentest can safely run.

This is the gap automated pentesting can’t close on its own. It’s **a required part of validation**, but **it can’t validate every exposure**.

## **All for One. One for All Exposures.**

This is where the pieces come together.

* **[Exploitability validation](https://www.picussecurity.com/platform/exposure-validation)** determines whether an exposure is, in fact, exploitable in your environment, including CVEs with no working exploit and assets that live exploitation can’t safely reach.
* **[Security control validation](https://www.picussecurity.com/platform/breach-and-attack-simulation)** tests whether your prevention and detection controls actually block, detect, or miss the attack.
* **[Agentic pentesting](https://www.picussecurity.com/platform/autonomous-penetration-testing)** safely runs real exploits and chains exposures to show how far an attacker can progress through your specific environment.

These methods answer different questions under different exposure conditions. **Mythos readiness requires all three capabilities, brought together in one platform with the same goal: validating exposures across your unique environment.** This doesn’t mean you have to always use all three against every exposure. The goal is to **apply each method where it fits best** and let the **evidence contribute to the same decision process**.

These three key pieces become even more powerful when they operate as one program. A **finding can trigger the validation step it actually needs**, **new evidence can change remediation priority**, and **fixes can be re-validated** instead of disappearing into a closed ticket. That keeps exploitability, control effectiveness, and attack-path evidence connected instead of leaving them to wallow in separate workflows.

This is also where [Gartner®’s May research](https://www.gartner.com/en/documents/7851581) note points: toward validated attack paths, decision-driven response, and exposure reduction all integrated into operational workflows.

This also happens to be the working model behind our **[Validation Summit ’26](https:/...