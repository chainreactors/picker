---
title: How insecure is Avast Secure Browser?
url: https://palant.info/2024/07/15/how-insecure-is-avast-secure-browser/
source: Over Security - Cybersecurity news aggregator
date: 2024-07-16
fetch_date: 2025-10-06T17:46:03.482203
---

# How insecure is Avast Secure Browser?

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# How insecure is Avast Secure Browser?

2024-07-15
 [Avast](/categories/avast/)/[Security](/categories/security/)/[Antivirus](/categories/antivirus/)
 18 mins
 [7 comments](/2024/07/15/how-insecure-is-avast-secure-browser/#comments)

A while ago I already looked into Avast Secure Browser. Back then it didnât end well for Avast: I [found critical vulnerabilities allowing arbitrary websites to infect userâs computer](/2020/01/13/pwning-avast-secure-browser-for-fun-and-profit/). Worse yet: much of it was due to neglect of secure coding practices, existing security mechanisms were disabled for no good reason. I didnât finish that investigation because I discovered that [the browser was essentially spyware](/2019/10/28/avast-online-security-and-avast-secure-browser-are-spying-on-you/), collecting your browsing history and selling it via Avastâs Jumpshot subsidiary.

But that was almost five years ago. After an initial phase of denial, Avast decided to [apologize and to wind down Jumpshot](https://blog.avast.com/a-message-from-avast). It was certainly a mere coincidence that Avast was subsequently sold to NortonLifeLock, called Gen Digital today. Yes, Avast is truly reformed and paying for their crimes [in Europe](https://www.edpb.europa.eu/news/news/2024/czech-sa-imposed-fine-139-million-eur-infringement-art-6-and-art-13-gdpr_en) and [the US](https://www.ftc.gov/system/files/ftc_gov/pdf/202_3033_-_avast_final_consent_package.pdf). According to the European decision, Avast is still arguing [despite better knowledge](/2020/02/18/insights-from-avast/jumpshot-data-pitfalls-of-data-anonymization/) that their data collection was fully anonymized and completely privacy-conformant butâ¦ well, old habits are hard to get rid of.

Either way, itâs time to take a look at Avast Secure Browser again. Becauseâ¦ all right, because of the name. That was a truly ingenious idea to name their browser like that, nerd sniping security professionals into giving them free security audits. By now they certainly would have addressed the issues raised in my original article and made everything much more secure, right?

![Malicious actors coming through Avast software](/2024/07/15/how-insecure-is-avast-secure-browser/avast.png)

*Note*: This article does not present any actual security vulnerabilities. Instead, this is a high-level overview of design decisions that put users at risk, artificially inflating the attack surface and putting lots of trust into the many, many companies involved with the Avast webspaces. TL;DR: I wouldnât run Avast Secure Browser on any real operating system, only inside a virtual machine containing no data whatsoever.

#### Contents

* [Summary of the findings](#summary-of-the-findings)
* [What is Avast Secure Browser?](#what-is-avast-secure-browser)
* [The pre-installed extensions](#the-pre-installed-extensions)
  + [Security mechanisms disabled](#security-mechanisms-disabled)
  + [The (lack of) ad blocking privacy](#the-lack-of-ad-blocking-privacy)
  + [The onboarding experience](#the-onboarding-experience)
* [Super-powered websites](#super-powered-websites)

## Summary of the findings

The issues raised in my original article about the pre-installed browser extensions are still partially present. Two extensions are relaxing the default protection provided by [Content-Security-Policy](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Security-Policy) even though it could have been easily avoided. One extension is requesting massive privileges, even though it doesnât actually need them. At least they switched from jQuery to React, but they still somehow managed to end up with HTML injection vulnerabilities.

In addition, two extensions will accept messages from any Avast website â or servers pretending to be Avast websites, since HTTPS-encrypted connections arenât being enforced. In the case of the Privacy Guard (sic!) extension, this messaging exposes usersâ entire browsing information to websites willing to listen. Yes, Avast used to collect and sell that information in the past, and this issue could in principle allow them to do it again, this time in a less detectable way.

The Messaging extension is responsible for the rather invasive âonboardingâ functionality of the browser, allowing an Avast web server to determine almost arbitrary rules to nag the user â or to redirect visited websites. Worse yet, access to internal browser APIs has been exposed to a number of Avast domains. Even if Avast (and all the other numerous companies involved in running these domains) are to be trusted, there is little reason to believe that such a huge attack surface can possibly be secure. So it has to be expected that other websites will also be able to abuse access to these APIs.

## What is Avast Secure Browser?

Avast Secure Browser is something you get automatically if you donât take care while installing your Avast antivirus product. Or AVG antivirus. Or Avira. Or Norton. Or CCleaner. All these brands belong to Gen Digital now, and all of them will push Avast Secure Browser under different names.

According to their web page, there are good reasons to promote this browser:

![Website screenshot showing Avast Secure Browser name and logo above the title âDownload a secure, private browser thatâs 100% free.â The text below says: âOur free private browser helps you surf the web, message, and shop more safely online. Plus, block ads and boost your online privacy.â](/2024/07/15/how-insecure-is-avast-secure-browser/website.png)

So one of the reasons is: this browser is 100% free. And it really is, as in: âyou are the product.â I took the liberty of making a screenshot of the browser and marking the advertising space:

![Screenshot of a browser showing a new tab, most of it marked with half-transparent red. The marked areas are: VPN button next to the location bar, bookmarks bar (six out of seven bookmarks), the space above the search bar (German-language ad for a tourism company) and the space below it (more sponsored bookmarks).](/2024/07/15/how-insecure-is-avast-secure-browser/browser_advertising.png)

Yes, maybe this isnât entirely fair. Iâm still indecisive as to whether the search bar should also be marked. The default search engine is Bing and the browser will nudge you towards keeping it selected. Not because Microsoftâs search engine is so secure and private of course but because they are paying for it.

But these are quality ads and actually useful! Like that ad for a shop selling food supplements, so that you can lead a healthy life. A quick search reveals that one of the three food supplements shown in the ad is likely useless with the suspicion of being harmful. Another brings up lots of articles by interested parties claiming great scientifically proven benefits but no actual scientific research on the topic. Finally the third one could probably help a lot â if there were any way of getting it into your body in sufficient concentration, which seems completely impossible with oral intake.

Now that we got âfreeâ covered, we can focus on the security and privacy aspects in the subsequent sections.

## The pre-installed extensions

There are various reasons for browser vendors to pre-package extensions with their browser. Mozilla Firefox uses extensions to distribute experimental features before they become an integral part of the browser. As I learned back in 2011, Google Chrome [uses such extensions to promote their web applications and give them an advantage over competition](/2011/11/15/google-chrome-and-pre-installed-web-apps/). And as Simon Willison discovered only a few days ago, the Google Hangouts extension built into Google Chrome [gives Google domains access to internal browser APIs](https://simonwillison.net/2024/Jul/9/hangout_servicesthunkjs...