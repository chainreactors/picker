---
title: Anatomy of a Phish: How Tech-Support Scams Buy Their Way Onto Your Screen
url: https://pixmsecurity.com/blog/blog/anatomy-of-a-phish-malvertising-tech-support-scams/
source: Over Security
date: 2026-10-14
fetch_date: 2026-10-15T06:45:18.746666
---

# Anatomy of a Phish: How Tech-Support Scams Buy Their Way Onto Your Screen

[![Pixm Security Logo](https://pixmsecurity.com/wp-content/themes/Divi-Child/images/pixm-logo-header-white.png)](https://pixmsecurity.com)

* [About](https://pixmsecurity.com/about/)
* [About Us](https://pixmsecurity.com/about-us/)
* [Partners](https://pixmsecurity.com/partners/)
* Resources
  + [Blog](https://pixmsecurity.com/blog/)
  + [News](/news)
  + [Case Studies](https://pixmsecurity.com/case-studies/)
* [Login](https://app.pixm.net)
* [Book a Demo](https://pixmsecurity.com/request-demo/)
* [Free Install](https://chrome.google.com/webstore/detail/pixm-phishing-protection/flomofhkchlalfciiibgbfcpolhmglai?hl=en)
* [Free Install](https://apps.apple.com/app/pixm-phishing-protection/id1622871362)
* [Free Install](https://addons.mozilla.org/en-US/firefox/addon/pixm-web/)

Have a question for us?

Contact support at support@pixm.net

[Book a Demo](/request-free-trial/)

Open Menu

## Request Your Demo

"\*" indicates required fields

### Contact Information

First Name\*

Last Name\*

Company\*

Email\*

Work Phone

CAPTCHA

Request Demo

# Anatomy of a Phish: How Tech-Support Scams Buy Their Way Onto Your Screen

Anatomy of a Phish · Threat Research

# How Tech-Support Scams Buy Their Way Onto Your Screen

An analysis of how fake Microsoft Support pages are delivered through social, native and programmatic advertising, and why that delivery path evades email security and domain reputation.

**PIXM Threat Research**Published Oct 13, 20267 min read

### Summary

* Roughly six in ten tech-support scam pages in our detections arrived with ad-click tracking parameters attached, indicating paid delivery.
* The delivering channel shifted over 2026 (native, then social, then programmatic) while the landing-page kit stayed the same.
* Some campaigns encode the callback phone number in the landing page’s hostname.

[Indicators ↓](#ioc)

On August 5, 2026, someone clicked a sponsored link and landed on what looked like Microsoft’s support website. Fake error messages covered the screen, and a chat window told them to call +1 (877) 295-2069 to unlock their computer. The page was hosted on Microsoft’s own Azure cloud, and the phone number was even written into its web address: `w8win05m877n2069c004.z13.web.core.windows[.]net`.

The link was an ad from Taboola, the company behind the “Recommended for you” story links that appear under articles on many news sites. When someone clicks one of those links, Taboola adds a tracking code to the web address so the advertiser can count the click. That code was still attached to this scam page’s address. Nobody emailed this page to anyone. Someone paid to put it in front of them.

This post traces how pages like this one reach their victims, drawing on the tech-support scam pages PIXM detected between March 2025 and early October 2026. It covers the delivery side of the scam whose phone-call endgame we dissected in [Anatomy of a Phish: Engineered Panic](#r1), and it goes deeper than our June brief, [Ad-Funded Phishing](#r2), which first flagged Facebook and Google ad parameters on these pages.

 ![Fake Microsoft Support page with stacked error dialogs and support chat](https://pixmsecurity.com/wp-content/uploads/2026/10/01-taboola-ad-scam-hostname-number.jpeg)

**Figure 1.** Fake Microsoft Support page reached through a Taboola ad (Aug 5, 2026). The callback number in the chat window also appears in the hostname.

## How the delivery chain works

In the pages we analyzed, the chain has four stages:

1. **Ad placement.** The operator buys inventory on a social, native, or programmatic network. In practice, that means paying for ad slots: a sponsored post in a social feed, a "recommended for you" tile under a news article (native), or a banner auctioned in real time across thousands of websites through an ad exchange (programmatic).
2. **Click-through.** The ad resolves to a throwaway landing page on Azure Static Websites, Bunny CDN, or Heroku. The URL keeps the platform’s click identifier.
3. **Browser takeover.** The page renders a Microsoft Support clone with stacked error dialogs and a “Windows Firewall has locked your session” prompt.
4. **Callback.** All paths end in a phone number. No credential is collected on the page; the fraud happens on the call.[1](#r1)

**Table 1.** Components of a programmatic-exchange landing URL (captured Oct 1, 2026).

| Component | Observed value | Interpretation |
| --- | --- | --- |
| Host | message101js829wd4678.z13.web.core.windows[.]net | Random Azure Static Website, rotated per wave |
| `domain` | <publisher site> | Placement where the ad was served |
| `exchange` | 2272 | Ad-exchange supply identifier |
| `campaign` | czlbb101BC-8559-ssp2272-11994 | Operator’s campaign label |

 ![Scam page with Authentication Required lock box](https://pixmsecurity.com/wp-content/uploads/2026/10/02-facebook-ad-scam-unlock-pc.jpeg)

**Figure 2.** The same kit delivered through a Facebook ad (Oct 9, 2026). The lock box and chat window show different numbers.

## Why it evades common controls

**Email security has no visibility.** There is no message, attachment or sender to evaluate. **Domain reputation is ineffective**: landing pages use `web.core.windows[.]net`, `b-cdn[.]net` and `herokuapp[.]com`, with a new hostname per wave. **Ad review evaluates the creative, not the destination.** **MFA is not in play**, since no credential is entered.

## Observations from PIXM data

**Table 2.** Ad channel indicated by click parameters, among ad-tagged tech-support scam pages.

| Channel | Parameter evidence | Share of ad-tagged pages | Most active |
| --- | --- | --- | --- |
| Native ads | `tblci` | ~45% | Q1 2026 |
| Social (Facebook) | `fbclid`, `utm_source=fb` | ~38% | Q2 2026 |
| Search (Google Ads) | `gclid`, `gad_source` | ~11% | Q2 2026 |
| Programmatic exchange | `domain`, `exchange`, `campaign` | ~6% | Q3 2026 |

The kit itself changed little across channels. Operators appear to move spend between networks while reusing the same landing page.

## Recommendations

* Treat ad-delivered pages as an attack surface; browser- or DNS-level ad blocking on managed devices removes much of this path.
* Evaluate pages on trusted cloud hosts by rendered content, not hosting domain.
* Brief users that Microsoft does not display phone numbers in pop-ups and that closing the tab is safe.
* Use point-of-click page analysis. PIXM’s computer vision identifies counterfeit support screens regardless of delivery channel or hostname.

## Indicators

| Indicator | Type | Observed |
| --- | --- | --- |
| w8win05m877n2069c004.z13.web.core.windows[.]net | Landing host | 2026-08-05 |
| message101js829wd4678.z13.web.core.windows[.]net | Landing host | 2026-10-01 |
| kyc2zneedzkz3rapb4xytq8u.z21.web.core.windows[.]net | Landing host | 2026-10-09 |
| ppoimnbc-3f54910e3deb.herokuapp[.]com | Landing host | 2026-08-06 |

## References

1. [Anatomy of a Phish: Engineered Panic, One Phone Call From Disaster](https://pixmsecurity.com/blog/blog/anatomy-of-a-phish-engineered-panic-one-phone-call-from-disaster/), PIXM, June 2026.
2. [Ad-Funded Phishing: How Facebook and Google Deliver Attacks to Enterprise Browsers](https://pixmsecurity.com/blog/blog/ad-funded-phishing-heroku-azure-facebook-june-2026/), PIXM, June 2026.

Questions, or want to share indicators? Contact threatresearch@pixmsecurity.com. To see PIXM’s point-of-click protection, [request a demo](https://pixmsecurity.com/request-demo/).

#### On this page

[How the delivery chain works](#how) [Why it evades common controls](#why) [Observations from PIXM data](#data) [Recommendations](#do) [Indicators](#ioc) [References](#refs)

Search for:

#### Recent Posts

* [Anatomy of a Phish: How Tech-Support Scams Buy Their Way Onto Your Screen](https://pixmsecurity.com/blog/blog/anatomy-of-a-phish-malvertising-tech-support-scams/)
* [AI-Era Phishing Is Here, and it’s Not Targeting the Mailbox](https://pixmsecurity.com/blog/blog/ai-era-phishing-flanking-the-corporate-inbox/)
* [Prime ...