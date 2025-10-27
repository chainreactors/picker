---
title: How extensions trick CWS search
url: https://palant.info/2025/01/08/how-extensions-trick-cws-search/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-09
fetch_date: 2025-10-06T20:12:40.261609
---

# How extensions trick CWS search

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# How extensions trick CWS search

2025-01-08
 [Add-Ons](/categories/add-ons/)/[Security](/categories/security/)/[Google](/categories/google/)
 51 mins
 [4 comments](/2025/01/08/how-extensions-trick-cws-search/#comments)

A few months ago I searched for âNorton Password Managerâ in Chrome Web Store and got lots of seemingly unrelated results. Not just that, the actual Norton Password Manager was listed last. These search results are still essentially the same today, only that Norton Password Manager moved to the top of the list:

![Screenshot of Chrome Web Store search results listing six extensions. While Norton Password Manager is at the top, the remaining search results like âVytal - Spoof Timezone, Geolocation & Localeâ, âFree VPN - 1VPNâ or âCharm - Coupons, Promo Codes, & Discountsâ appear completely unrelated. All extensions are marked as featured.](/2025/01/08/how-extensions-trick-cws-search/search_results.png)

I was stumped how Google managed to mess up search results so badly and even [posted the following on Mastodon](https://infosec.exchange/users/WPalant/statuses/113396203134184793):

> Interesting. When I search for âNorton Password Managerâ on Chrome Web Store, it first lists five completely unrelated extensions, and only the last search result is the actual Norton Password Manager. Somebody told me that website is run by a company specializing in search, so this shouldnât be due to incompetence, right? What is it then?

Somebody suggested that the extensions somehow managed to pay Google for this placement which seemsâ¦ well, rather unlikely. For reasons, I came back to this a few weeks ago and decided to take a closer look at the extensions displayed there. These seemed shady, with at least three results being former open source extensions (as in: still claiming to be open source but the code repository linked didnât contain the current state).

And then I somehow happened to see what it looks like when I change Chrome Web Store language:

![Screenshot of Chrome Web Store search results listing the same six extensions. The change in language is visible because the âFeaturedâ badge is now called something else. All extension descriptions are still English however, but they are different. 1VPN calls itself âBrowsec vpn urban vpn touch tunnelbear vpn 1click vpn 1clickvpn - 1VPNâ and Vytal calls itself âVytal - Works With 1click VPN & Hotspot VPNâ.](/2025/01/08/how-extensions-trick-cws-search/search_results2.png)

Now I donât claim to know Swahili but what happened here clearly wasnât translating.

#### Contents

* [The trick](#the-trick)
* [Who is doing it?](#who-is-doing-it)
  + [Kodice LLC / Karbon Project LP / BroCode LTD](#kodice-llc-karbon-project-lp-brocode-ltd)
  + [PDF Toolbox cluster](#pdf-toolbox-cluster)
  + [ZingFront Software / ZingDeck / BigMData](#zingfront-software-zingdeck-bigmdata)
  + [ExtensionsBox, Lazytech, Yue Apps, Chrome Extension Hub, Infwiz, NioMaker](#extensionsbox-lazytech-yue-apps-chrome-extension-hub-infwiz-niomaker)
  + [Free Business Apps](#free-business-apps)
* [The approaches](#the-approaches)
  + [1. Different extension name](#1-different-extension-name)
  + [2. Different short description](#2-different-short-description)
  + [3. Using competitorsâ names](#3-using-competitors-names)
  + [4. Considerably more extensive extension description](#4-considerably-more-extensive-extension-description)
  + [5. Keywords at the end of extension description](#5-keywords-at-the-end-of-extension-description)
  + [6. Keywords within the extension description](#6-keywords-within-the-extension-description)
  + [7. Different extension description](#7-different-extension-description)
* [And what should Google do about it?](#and-what-should-google-do-about-it)
* [The extensions in question](#the-extensions-in-question)
  + [Kodice / Karbon Project / BroCode](#kodice-karbon-project-brocode)
  + [PDF Toolbox cluster](#pdf-toolbox-cluster-1)
  + [ZingFront / ZingDeck / BigMData](#zingfront-zingdeck-bigmdata)
  + [ExtensionsBox](#extensionsbox)
  + [Lazytech](#lazytech)
  + [Yue Apps](#yue-apps)
  + [Chrome Extension Hub](#chrome-extension-hub)
  + [Infwiz](#infwiz)
  + [NioMaker](#niomaker)
  + [FreeBusinessApps](#freebusinessapps)
  + [Everything else](#everything-else)

## The trick

Google Chrome is currently available in 55 languages. Browser extensions can choose to support any subset of these languages, even though most of them support exactly one. Not only the extensionâs user interface can be translated, its name and short description can be made available in multiple languages as well. Chrome Web Store considers such translations according to the userâs selected language. Chrome Web Store also has an extensive description field which isnât contained within the extension but can be translated.

Apparently, some extension authors figured out that the Chrome Web Store search index is shared across all languages. If you wanted to show up in the search when people look for your competitors for example, you could add their names to your extensionâs description â but that might come across as spammy. So what you do instead is sacrificing some of the âless popularâ languages and stuff the descriptions there full of relevant keywords. And then your extension starts showing up for these keywords even when they are entered in the English version of the Chrome Web Store. After all, who cares about Swahili other than maybe five million native speakers?

Iâve been maintaining a [Github repository with Chrome extension manifests](https://github.com/palant/chrome-extension-manifests-dataset) for a while, uploading new snapshots every now and then. Unfortunately, it only contained English names and descriptions. So now Iâve added a directory with localized descriptions for each extension. With that data, most of the issues became immediately obvious â even if you donât know Swahili.

![Screenshot of a JSON listing. The key name is sw indicating Swahili language. The corresponding description starts with âCharm is a lightweight, privacy friendly coupon finder.â Later on it contains a sequence of newlines, followed by a wall of text along the lines of: âGMass: Powerful mail merge for GMail Wikiwand - Wikipedia, and beyond Super dark mode Desktopifyâ](/2025/01/08/how-extensions-trick-cws-search/json.png)

**Update** (2025-01-09): Apparently, Google has already been made aware of this issue [a year ago at the latest](https://groups.google.com/a/chromium.org/g/chromium-extensions/c/JMtfgiagcgY/m/TNMERoXWAwAJ). Your guess is as good as mine as to why it hasnât been addressed yet.

## Who is doing it?

Sifting through the suspicious descriptions and weeding out false positives brought up 920 extensions with bogus âtranslationsâ so far, and I definitely didnât get all of them (see [the extension lists](#the-extensions-in-question)). But that doesnât actually mean hundreds of extension developers. Iâve quickly noticed patterns, somebody applying roughly the same strategy to a large cluster of extensions. For example, European developers tended to âsacrificeâ some Asian languages like Bengali whereas developers originating in Asia preferred European languages like Estonian. These strategies were distinctly different from each other and there wasnât a whole lot of them, so there seems to be a relative low number of parties involved. Some I could even put a name on.

### Kodice LLC / Karbon Project LP / BroCode LTD

One such cluster of extensions [has been featured on this blog in 2023 already](/2023/06/08/another-cluster-of-potentially-malicious-chrome-extensions/). Back then I listed 108 of their extensions which was only a small sample of their operations. Out of that original sample, 96 extension remain active in Chro...