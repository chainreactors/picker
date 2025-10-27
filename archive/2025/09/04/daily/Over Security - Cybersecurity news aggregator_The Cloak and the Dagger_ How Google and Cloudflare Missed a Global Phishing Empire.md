---
title: The Cloak and the Dagger: How Google and Cloudflare Missed a Global Phishing Empire
url: https://reporter.deepspecter.com/the-cloak-and-the-dagger-how-google-and-cloudflare-missed-a-global-phishing-empire-ed7176ebf82f
source: Over Security - Cybersecurity news aggregator
date: 2025-09-04
fetch_date: 2025-10-02T19:38:16.840607
---

# The Cloak and the Dagger: How Google and Cloudflare Missed a Global Phishing Empire

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2Fed7176ebf82f&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Freporter.deepspecter.com%2Fthe-cloak-and-the-dagger-how-google-and-cloudflare-missed-a-global-phishing-empire-ed7176ebf82f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](https://medium.com/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](https://medium.com/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](https://medium.com/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](https://medium.com/m/signin?operation=login&redirect=https%3A%2F%2Freporter.deepspecter.com%2Fthe-cloak-and-the-dagger-how-google-and-cloudflare-missed-a-global-phishing-empire-ed7176ebf82f&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

[Mastodon](https://me.dm/%40deepspecter)

# The Cloak and the Dagger: How Google and Cloudflare Missed a Global Phishing Empire

[![Deep Specter Research](https://miro.medium.com/v2/resize:fill:64:64/1*_L_0HFU03vcDwGmr2CLt3Q.png)](/?source=post_page---byline--ed7176ebf82f---------------------------------------)

[Deep Specter Research](/?source=post_page---byline--ed7176ebf82f---------------------------------------)

13 min read

·

Sep 2, 2025

--

Listen

Share

## Intro

First, we examine **Google and Cloudflare** as infrastructure providers with broad operational reach. Their services power a significant portion of the internet, and as such, they carry a wide scope of responsibility. When these platforms enable long-term abuse — such as cloaked phishing sites or illegal operations (e.g.[APT41 Group tactics](https://cyberscoop.com/google-calendar-apt-41-c2-winnti/) ) — their role shifts from passive intermediary to potential enabler, **especially when threat intelligence sources have already flagged the relevant infrastructure identifiers (e.g., domains, IPs, certificates) as malicious** and no action is taken, we aware about [Cloudflare Policy](https://www.cloudflare.com/terms/) and Google’s Shared responsibility, but since these organizations practically routing most of the internet, we believe **where inaction may be interpreted as willful blindness.**

Second, we address **a vendor like Lockheed Martin**, a company with substantial national security relevance and public trust. As a defense contractor and prominent publicly traded entity, Lockheed Martin has both the visibility and technical capability to detect cloned or spoofed versions of its digital assets — as we ourselves have identified. From this standpoint, we believe Lockheed Martin and other similar companies should implement stronger monitoring and proactive detection mechanisms to prevent abuse like phishing, brand hijacking, or impersonation. **In our view, this is not just a technical gap, but a responsibility tied to their status and trust profile.**

## Executive Summary

Deep Specter Research exposes a multi-year, industrial-scale phishing and brand impersonation scheme operating for over 3 years on Google Cloud (Nasdaq:GOOG) and Cloudflare (NYSE:NET) platforms. Despite repeated alerts, these tech giants failed to act, exposing public companies to millions in potential regulatory penalties. This failure constitutes industry-wide willful blindness. Key findings:

* 48,000 hosts, >80 clusters abusing high-trust expired domains
* Multiple impersonations of Fortune 500 companies incl. Lockheed Martin
* Malware and gambling content served from brand-trusted resources
* Cloaked sites receive traffic from Google, Meta, Android apps
* Cloudflare & Google failed to respond despite >265 public detections
* Potential GDPR, DMCA, and FTC exposure for involved companies

What happens when a forgotten domain resurfaces — not as a blank page, but as a **perfect clone of a Fortune 500 defense contractor**?

We uncovered a large-scale, cloud-hosted infrastructure that hijacks abandoned or expired domains, then pairs them with cloned websites of major global brands — including **Lockheed Martin** and many other US and non-US companies. These clones aren’t theoretical risks. They’ve been **live**, **undetected**, and **interacting with users and malware** for **years**.

But the real issue isn’t just technical. It’s **business-critical**:

> *Many of the cloned sites still load resources from the original brand’s cloud infrastructure — meaning the* ***original brand may actively be serving content to a malicious impersonator***

From a legal and regulatory standpoint, this creates **significant regulatory and legal liability**. Not only is the impersonation possible, but it continues *with the unintentional assistance of the original asset owner*. This suggests a **failure to monitor** and raises serious questions about **due diligence**, **data protection**, and **customer safety**.

At **Deep Specter Research**, we don’t just surface security anomalies.

We **translate technical findings into business vulnerabilities and regulatory exposure** — assigning real-world accountability to organizations who fail to take reasonable steps to protect their digital assets.

We work closely with **legal experts and privacy advocates** to ensure the public is informed, regulators are aware, and enterprises are held responsible.

## The Research

**Several years ago, I was a fan of fighter jets**. I collected their pictures and figures, constructed them from LEGO and, of course, read news about them. My favorite movie was “Top Gun”, and I watched them both (old and new one) at least 5 times.

One of the sources, constantly providing pictures and news was this Facebook page (100K subscribers):

Press enter or click to view image in full size

![]()

military fighter jets facebook community

They also had a website, while it seems like most people in 2022–2023 mostly viewed their Facebook page:

`militaryfighterjet[.]com`

Press enter or click to view image in full size

![]()

military fighter jets site

All was good, until 2024–09–14 18:00:32 (last September)..

What happened is their “DNS record expired” 2 months before approximately. This means, somebody “forgot to pay the bill”, causing them to lose ownership over the domain `militaryfighterjet[.]com` and their domain was “on sale” and bought by somebody else.

This happens sometimes. Not too often, but happens.

**What followed, however, was highly unusual.**

On 2024–09–16 14:49:50 this domain started to show this “168 Lottery Results” gambling page:

Press enter or click to view image in full size

![]()

when accessed directly using Desktop Browsers…

But when You search for this domain in Google:

Press enter or click to view image in full size

![]()

or when accessed from Mobile Devices or just by adding “/index-2.html” to the domain address:

Press enter or click to view image in full size

![]()

**This is clearly a clone of** [Lockheed Martin’s](https://www.lockheedmartin.com/) **site**!

This means, that someone who acquired `militaryfighterjet[.]com` now showing there clone of Lockheed Martin website (including login pages for employees and partners), and gambling website altogether!

This is something that called “Cloaking”.

It is SEO (Search Engine Optimization) black-hat technique where content presented to search engine crawlers (like GoogleBot) is different from the content presented to human users. The main goal is to manipulate search engine ranking or to hide illicit ...