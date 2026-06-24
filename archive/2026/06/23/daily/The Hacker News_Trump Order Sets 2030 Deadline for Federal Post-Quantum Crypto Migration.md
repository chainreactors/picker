---
title: Trump Order Sets 2030 Deadline for Federal Post-Quantum Crypto Migration
url: https://thehackernews.com/2026/06/trump-order-sets-2030-deadline-for.html
source: The Hacker News
date: 2026-06-23
fetch_date: 2026-06-24T06:06:31.079771
---

# Trump Order Sets 2030 Deadline for Federal Post-Quantum Crypto Migration

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

[![cybersecurity](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjQl2axNwsfhbXOFynrg_uAZsvHi3OvNGSA8KJO-BKR8Xm3x7yjKV3EvfY4v5mwXx6LF0uWFb9h9d9iAV_Pi-YYhqimX9wx4OaLdDJEdR215Xrxq_PAtXkaLfQso4pTSjbj6fvh_ZTliLpzWZSZfcoZgyXtKwhN-SSDDlmbtUqGLshc0KqYQGWYHMN52Sl1/s728-e100/zz-d.jpg)](https://thehackernews.uk/ai-vuln-protection-d)

# [Trump Order Sets 2030 Deadline for Federal Post-Quantum Crypto Migration](https://thehackernews.com/2026/06/trump-order-sets-2030-deadline-for.html)

**Swati Khandelwal**Jun 23, 2026Cryptography / Quantum Computing

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhoC7KFWoDGkSi-UzAyKNUkw-Ogs4oy2tCOAYXiYAAkqEUC1WMotLAE1GUwoWApfXK3prWVctTP05aLGjru0hDBfJkZ1NzPiFeI1VObgSNCx4egTrYhKIUt4m1S14eQ6_GpdffFBL4Ak3Mgjw7UiiBethv1lmyd_OaPIfhk_b-zuMjxCHLZtih8Tk6MtRg/s1700-e365/unitedstates.jpg)

President Trump signed an [executive order on June 22](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/) setting hard deadlines for federal agencies to move high-value assets and high-impact systems to post-quantum cryptography.

Key establishment must move by December 31, 2030; digital signatures by December 31, 2031. EO 14409 leaves national security systems on a separate track.

The deadlines matter because of a threat that does not need a working quantum computer today. Adversaries can collect encrypted U.S. data now and decrypt it later, once a large-scale quantum machine exists, the risk is known as ["harvest now, decrypt later"](https://thehackernews.com/2025/02/google-cloud-kms-adds-quantum-safe.html).

The order describes that risk directly and pulls the government's PQC timeline forward by four to five years. The prior government-wide target, set by the 2022 National Security Memorandum 10, ran to 2035.

The two deadlines line up with the standards NIST [finalized in August 2024](https://www.nist.gov/news-events/news/2024/08/nist-releases-first-3-finalized-post-quantum-encryption-standards). Key establishment uses FIPS 203, the ML-KEM algorithm formerly called CRYSTALS-Kyber.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Digital signatures use FIPS 204 and 205, ML-DSA, and SLH-DSA. The standards have been ready for almost two years. The order is what turns them into a schedule with consequences.

## What agencies have to do, and when

The near-term clock starts fast. Within 30 days, each agency head names a PQC migration lead who reports to the agency CIO and owns the cryptographic inventory and migration plan.

Within 90 days, OMB issues guidance requiring agencies to review their inventories of high-value assets and high-impact systems, plan the migration, and submit that plan.

NIST runs a pilot migration on a subset of its own systems, to be finished by December 31, 2027.

The order reaches past federal networks. The Federal Acquisition Regulatory Council has 180 days to propose a rule giving "covered contractors" until December 31, 2030, to meet NIST's FIPS, including the PQC algorithms.

A second proposed rule, due in 270 days, would fold cryptographic flaws into contractor vulnerability disclosure programs, including tests for missing encryption and for non-FIPS algorithms. Sector Risk Management Agencies and CISA are told to help critical infrastructure operators build their own migration plans, though that part is assistance, not a mandate.

Then there is the inventory angle. Within 270 days, CISA and NIST are to publish the minimum elements for a cryptographic bill of materials, a machine-readable list of the cryptographic assets in a piece of hardware or software.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

That is the groundwork for crypto-agility: you cannot swap out weak algorithms on a deadline if you do not know where they are.

## The practical read

For federal teams and the vendors who sell to them, the work is the inventory, and it starts now. Find every place key exchange and signatures happen, flag what is not NIST PQC, and sequence the swap against the 2030 and 2031 dates.

Contractors should expect the FAR clause and a 2030 compliance line once the rule lands. The standards exist. The deadlines now exist. The gating task for almost everyone is knowing what cryptography is running, and where.

A companion order signed the same day, ["Ushering in the Next Frontier of Quantum Innovation,"](https://www.whitehouse.gov/presidential-actions/2026/06/ushering-in-the-next-frontier-of-quantum-innovation/) pushes the other side of the equation: building the quantum computers that make the migration urgent in the first place.

The teeth are still being written. OMB's 90-day guidance and the FAR rules will decide whether 2030 and 2031 become real procurement pressure or just another federal migration target that slips once the hard work starts.

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

[CISA](https://thehackernews.com/search/label/CISA), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [Executive Order](https://thehackernews.com/search/label/Executive%20Order), [NIST](https://thehackernews.com/search/label/NIST), [Post-Quantum Cryptography](https://thehackernews.com/search/label/Post-Quantum%20Cryptography), [Quantum Computing](https://thehackernews.com/search/label/Quantum%20Computing)

⚡ Top Stories This Week

[![Chrome V8 Zero-Day CVE-2026-11645 Exploited in the Wild - Patch Now](d...