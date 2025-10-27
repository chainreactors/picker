---
title: “DeceptionAds” — Fake Captcha Driving Infostealer Infections and a Glimpse to the Dark Side of…
url: https://medium.com/@guardiosecurity/deceptionads-fake-captcha-driving-infostealer-infections-and-a-glimpse-to-the-dark-side-of-0c516f4dc0b6
source: Over Security - Cybersecurity news aggregator
date: 2024-12-17
fetch_date: 2025-10-06T19:41:39.925622
---

# “DeceptionAds” — Fake Captcha Driving Infostealer Infections and a Glimpse to the Dark Side of…

[Sitemap](/sitemap/sitemap.xml)

[Open in app](https://rsci.app.link/?%24canonical_url=https%3A%2F%2Fmedium.com%2Fp%2F0c516f4dc0b6&%7Efeature=LoOpenInAppButton&%7Echannel=ShowPostUnderUser&%7Estage=mobileNavBar&source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40guardiosecurity%2Fdeceptionads-fake-captcha-driving-infostealer-infections-and-a-glimpse-to-the-dark-side-of-0c516f4dc0b6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

[Medium Logo](/?source=post_page---top_nav_layout_nav-----------------------------------------)

[Write](/m/signin?operation=register&redirect=https%3A%2F%2Fmedium.com%2Fnew-story&source=---top_nav_layout_nav-----------------------new_post_topnav------------------)

[Search](/search?source=post_page---top_nav_layout_nav-----------------------------------------)

Sign up

[Sign in](/m/signin?operation=login&redirect=https%3A%2F%2Fmedium.com%2F%40guardiosecurity%2Fdeceptionads-fake-captcha-driving-infostealer-infections-and-a-glimpse-to-the-dark-side-of-0c516f4dc0b6&source=post_page---top_nav_layout_nav-----------------------global_nav------------------)

![](https://miro.medium.com/v2/resize:fill:64:64/1*dmbNkD5D-u45r44go_cf0g.png)

# **“DeceptionAds” — Fake Captcha Driving Infostealer Infections and a Glimpse to the Dark Side of Internet Advertising**

[![Guardio](https://miro.medium.com/v2/resize:fill:64:64/1*s7SJaF9dODo7rWqa2rFQ6Q.png)](/%40guardiosecurity?source=post_page---byline--0c516f4dc0b6---------------------------------------)

[Guardio](/%40guardiosecurity?source=post_page---byline--0c516f4dc0b6---------------------------------------)

17 min read

·

Dec 16, 2024

--

4

Listen

Share

By [**Nati Tal**](https://www.linkedin.com/in/natital/)(Head of [Guardio Labs](http://www.guard.io/))

> Guardio Labs tracked and analyzed a large-scale fake captcha campaign distributing a disastrous Lumma info-stealer malware that circumvents general security measures like Safe Browsing. Entirely reliant on a single ad network for propagation, this campaign showcases the core mechanisms of **malvertising** — **delivering over 1 million daily “ad impressions” and causing thousands of daily victims to lose their accounts and money** through a network of **3,000+** content sites funneling traffic. Our research dissects this campaign and provides insights into the malvertising industry’s infrastructure, tactics, and key players.
>
> Through a detailed analysis of redirect chains, obfuscated scripts, and Traffic Distribution Systems (TDS) — in collaboration with our friends at [Infoblox](https://blogs.infoblox.com/) — we traced the campaign’s origins to **Monetag**, a part of ProepllerAds’ network previously tracked by Infoblox under the name “**Vane Viper**.” Further investigation reveals how threat actors leveraged services like **BeMob** ad-tracking to cloak their malicious intent, showcasing the fragmented accountability in the ad ecosystem. This lack of oversight leaves internet users vulnerable and enables malvertising campaigns to flourish at scale.

Press enter or click to view image in full size

![]()

## The Fake-Captcha Lumma Stealer Campaign

For several weeks, a large-scale deceptive campaign has leveraged a cunning technique: tricking users into installing dangerous stealer malware via a captcha verification page. This seemingly legitimate captcha page appears unexpectedly as you browse a content site, perfectly mimicking a real verification process. It asks you to confirm you’re human through a series of keyboard clicks, which ultimately trigger the Run dialog on your Windows system. Unknowingly, you paste and execute a cleverly crafted PowerShell command, instantly installing stealer malware that targets your social accounts, banking credentials, passwords, and personal files. Vicious, effective, and dangerously evasive!

Despite recent [news coverage](https://www.darkreading.com/cyberattacks-data-breaches/trick-captcha-lumma-stealer-malware), the question remains: How does a fake captcha suddenly appear, tricking unsuspecting users into executing a malicious PowerShell command under the guise of verifying their human identity? What keeps this campaign not only active but thriving?

Press enter or click to view image in full size

![]()

The fake captcha flow — forcing site visitors to unknowingly execute a PowerShell command

What are we overlooking? It’s not solely the clever disguise of captcha imitation that marks the success of this campaign. The real concern lies in how this perilous page makes its way onto our screens. The answer is **malvertising — malvertising on steroids**. This initial deceit is just the surface; the ad network underlying mechanics reveal a darker, more complex web of digital threats.

## Ad-Networks As Enablers

Since the early days of the internet, advertising has been a cornerstone, growing increasingly vital over the years. For instance, in 2023, almost 70% of Google’s revenue stems from advertisements, highlighting the lucrative nature of this industry.

However, the ad tech industry has also taken a darker turn, becoming a prominent channel for malicious activities. Examples abound, from fake e-commerce sites advertised on [Facebook](https://labs.guard.io/malverposting-with-over-500k-estimated-infections-facebook-ads-fuel-this-evolving-stealer-54b03d24b349) to deceptive “Download” buttons that deliver [unexpected software](https://labs.guard.io/zipb-the-all-you-can-infect-buffet-494aa8b805a0) and even rogue [sponsored results in Google](https://labs.guard.io/masquerads-googles-ad-words-massively-abused-by-threat-actors-targeting-organizations-gpus-42ae73ee8a1e).

The responsibility often falls on **Ad Networks**. These services form the link between advertisers seeking to sell products or services and website publishers looking to monetize available space. Ad networks handle the coding, analytics, and management necessary for both parties.

Press enter or click to view image in full size

![]()

The Ad-Network ecosystem — Publishers monetizing on ad zones and Advertisers seeking impressions

The process is straightforward: website owners register with an ad network, receive code snippets to integrate into their sites, creating “Advertisement Zones.” These zones, when activated, direct traffic to the network’s Traffic Distribution System (TDS), which houses numerous domains and redirectors. The system then selects the most optimized advertisement to display based on visitor analysis, campaign budgets, and settings — all in milliseconds. The advertisers focus on optimizing landing pages for conversion, while website owners collect their earnings.

## Evolving From Advertising to Malvertising Captchas

Ad networks have proven exceptionally successful; they are fine-tuned machines built from the ground up to distribute traffic on a massive scale, from advertisers to internet users across a vast ecosystem of websites. But what happens when advertisers are replaced with threat actors? Yea, you’re right—we get **Malvertising**.

Many active ad networks are raising alarms with the content they distribute today. Although they don’t have sole control or responsibility for this content, the overtly malicious intent and scale of the activities exploiting their networks are too significant to ignore or absolve them of all responsibility.

Press enter or click to view image in full size

![]()

A visitor activating an ad-placement process and the ad network selecting the target creative (good or bad)

The scenario above is a real-life example of how just three simple clicks on an ostensibly benign website can lead you down an unexpected path—perhaps when you only want to watch a movie. But will you actually get to see that movie? Unfortunately, that’s far from guaranteed…

## Fake-Captcha’s Malvertising: End-2-End Analysis

This Fake Captcha ca...