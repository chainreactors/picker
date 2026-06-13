---
title: China-Linked Hackers Backdoored Linux Login Software to Hide for Nearly a Decade
url: https://thehackernews.com/2026/06/china-linked-hackers-backdoored-linux.html
source: The Hacker News
date: 2026-06-12
fetch_date: 2026-06-13T06:12:07.505644
---

# China-Linked Hackers Backdoored Linux Login Software to Hide for Nearly a Decade

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

# [China-Linked Hackers Backdoored Linux Login Software to Hide for Nearly a Decade](https://thehackernews.com/2026/06/china-linked-hackers-backdoored-linux.html)

**Swati Khandelwal**Jun 12, 2026Linux / Network Security

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEhxJqmKAQv_I_7JkmQwoIVSx2BkRPUEb9TTNOd2RkNqTg3tcLyZszN8KiXfUUeIBSPSoxjzMAn2inE6TL791l5B_CbQaHqG708c2tgN-kSUmz_fTuewdcrWHS8u-xdWKIr6fEhx2W7_JDszsJ1oXO9v47JxU81490QKz0ZRL2OOFoljevoD8f6OMozfMZU/s1700-e365/linux-backdoor.jpg)

Instead of hiding on the laptops and servers defenders watch most closely, a China-nexus group spent close to a decade hidden inside the Linux login system itself.

Sygnia, which tracks the group as **Velvet Ant**, says it backdoored the PAM and OpenSSH components that decide who is allowed to sign in, planting its access where ordinary cleanup could not reach it. The network it targeted had no direct internet access, so the group first staged through internet-facing systems to get there.

The earliest traces go back to 2016. Instead of dropping new malware that a scanner might catch, the attacker changed the trusted login programs themselves. Nothing obvious appeared, and no exploit was needed, so the activity looked like normal administration.

On many machines, the attacker replaced the main PAM login module with backdoored copies. Some let them in with a secret password; others quietly recorded real usernames and passwords as people logged in.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ai-cant-stop-d)

Researchers found nine separate versions. The OpenSSH programs were altered the same way, logging credentials and every command typed, with a hidden switch to turn that logging off when needed.

Reaching the isolated network at all took extra work. The attacker used other disguised tools and an internet-facing web server as a bridge, passing commands through it to open remote sessions deep inside the segment that had no direct internet access.

Because the login system itself was compromised, normal containment did little. Password resets and killed sessions do not help when the thing that checks those credentials is working for the attacker.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgFm2U2Wdk-YYFY_MLDGS0OFTLVVZxtcM7aijUJyK6az8EoNkygFAga1-qrxL3vsC07RlYeAvedVxNpVW5osp-g_vm_3RVJtZ9hnL5FKSIyivVovwtUcF0-daOT6Gp5vmA4LwHDB7JjCPqJ4DjU_ogWty_J7rKgqnhMcGp4TP6L4csfRshMW12RlgmXpoM/s1700-e365/login.png)

This is not new for the group. Each time defenders find one foothold, Velvet Ant moves to gear they watch less and sets up there. In a [2024 case](https://www.sygnia.co/blog/china-nexus-threat-group-velvet-ant/), Sygnia found the same actor turning internet-exposed [F5 BIG-IP appliances](https://thehackernews.com/2024/06/china-linked-hackers-infiltrate-east.html) into internal command servers.

Later that year, it reported the group exploiting a Cisco NX-OS flaw, [CVE-2024-20399](https://nvd.nist.gov/vuln/detail/CVE-2024-20399), to [plant a backdoor on the switches](https://thehackernews.com/2024/07/chinese-hackers-exploiting-cisco.html). That bug needs admin access first, so it is a persistence tool, not a remote break-in. Cisco patched it in July 2024, and CISA flagged it as exploited the next day.

[Operation Highland](https://www.sygnia.co/blog/operation-highland-velvet-ant/) is the same idea, one level deeper. Load balancers, switches, and the login software itself are trusted by default and rarely checked, which is exactly why a patient attacker hides inside them.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/vpn-threat-report-m)

Operation Highland is not a one-CVE problem. The attacker changed trusted programs after getting in, so the fix is verification, not patching, and cleanup is delicate: a wrong replacement can lock admins out of a live system.

* **Watch the login files**. Monitor the PAM and OpenSSH programs and their key files for any change, and alert when they change.
* **Hunt by checking what changed**, not by waiting for an alert. Compare these programs against known-good copies, because nothing will flag them for you.
* **Remove the backdoor before resetting passwords**, or the new ones get stolen the same way. Test any replacement in a lab first.

The earlier F5 and Cisco cases have their own checks: patch CVE-2024-20399 on Cisco Nexus gear, and watch F5 boxes for unexpected outbound connections.

The wider lesson is plain: infrastructure that sits outside normal monitoring still needs integrity checks, and that now includes the login layer.

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

[Backdoor](https://thehackernews.com/search/label/Backdoor), [china](https://thehackernews.com/search/label/china), [Credential Theft](https://thehackernews.com/search/label/Credential%20Theft), [cybersecurity](https://thehackernews.com/search/label/cybersecurity), [linux](https://thehackernews.com/search/label/linux), [network security](https://thehackernews.com/search/label/network%20security), [OpenSSH](https://thehackernews.com/search/label/OpenSSH), [PAM](https://thehackernews.c...