---
title: Strox Phishing Service & How It Works
url: https://lukeleal.com/research/posts/strox-phishing-service-and-how-it-works/
source: Over Security - Cybersecurity news aggregator
date: 2022-11-11
fetch_date: 2025-10-03T22:24:15.687311
---

# Strox Phishing Service & How It Works

[└──╼ # Cybersecurity Research 🚀](/research/posts/)

menu

* [Backdoors](https://lukeleal.com/research/tags/backdoor/)
* [Phishing](https://lukeleal.com/research/tags/phishing/)
* [Skimmers](https://lukeleal.com/research/tags/skimmer/)

+ Show more ▾

- [Past Research](https://blog.sucuri.net/author/luke)
- [PGP Key](https://lukeleal.com/research/pages/pgp/)
- [RSS](https://lukeleal.com/research/posts/index.xml)

* [Backdoors](https://lukeleal.com/research/tags/backdoor/)
* [Phishing](https://lukeleal.com/research/tags/phishing/)
* [Skimmers](https://lukeleal.com/research/tags/skimmer/)
* [Past Research](https://blog.sucuri.net/author/luke)
* [PGP Key](https://lukeleal.com/research/pages/pgp/)
* [RSS](https://lukeleal.com/research/posts/index.xml)

# [Strox Phishing Service & How It Works](https://lukeleal.com/research/posts/strox-phishing-service-and-how-it-works/)

2022-11-07
::
Luke

#[strox](https://lukeleal.com/research/tags/strox/)
#[strox.su](https://lukeleal.com/research/tags/strox.su/)
#[phishing](https://lukeleal.com/research/tags/phishing/)
#[PHaaS](https://lukeleal.com/research/tags/phaas/)
#[phishing-as-a-service](https://lukeleal.com/research/tags/phishing-as-a-service/)
#[fraud](https://lukeleal.com/research/tags/fraud/)
#[PHP](https://lukeleal.com/research/tags/php/)
#[website malware](https://lukeleal.com/research/tags/website-malware/)
![Strox Phishing Service & How It Works](https://lukeleal.com/research/strox.png)

## Outline

* [**Strox = Phishing-as-a-Service (PHaaS) Provider**](#strox--phishing-as-a-service-phaas-provider)

  + [Strox Phishing Kit & Page Features](#strox-phishing-kit--page-features)
  + [Bulletproof Hosting](#bulletproof-hosting)
* [**Anti-Red/Never-Red/Anti-Bot Protection**](#anti-rednever-redanti-bot-protection)
  + [Installation Process](#installation-process)
* [**Active Marketplace = Fast Way To Sell Phished Logins**](#active-marketplace--fast-way-to-sell-phished-logins)
* [**Who is Strox?**](#who-is-strox)
* [Tutorial Videos](#tutorial-videos)
* [Sample](#sample)

# Traditional Phishing Deployment = Learning Curve[⌗](#traditional-phishing-deployment--learning-curve)

The problem with the traditional style of phishing deployment is that **someone needs to be experienced** in acquiring these required resources from different marketplaces/vendors, **and then know how to configure them so that their phishing page will properly load** from the hosting server and how to get victims to it.

> This initial ***learning curve*** acts as a type of ***barrier to entry***, which can help to dissuade new users from attempting phishing and just ultimately giving up.
>
> Unfortunately it also presents an opportunity for a phishing vendor to remove these **barriers of entry** and make it even easier to set up high quality phishing pages.

## **Strox = Phishing-as-a-Service (PHaaS) Provider**[⌗](#strox--phishing-as-a-service-phaas-provider)

![](/research/strox-guide-01.png)

`Strox` is a ***Phishing-as-a-Service provider*** as they unify all the necessary resources and offer a single account that can be used to deploy and manage multiple phishing pages that exist across different hosting environments.

It is similar to the idea of ***[vertical integration](https://en.wikipedia.org/wiki/Vertical_integration)*** within an industry.

The only part that `Strox` cannot control is domain registration, but they do recommend a ***certain*** domain registrar that is notorious for malicious domains.

#### Strox Platform[⌗](#strox-platform)

`Strox` created a **22** page PDF guide on how to use their service and released it on their website (October 23, 2022), but it’s behind a paywall on their website.

**[You can instead download the PDF here for free](https://lukeleal.com/strox-guide.pdf)**.

![](/research/strox-guide-02.png)

Activation costs $0...just add $25 to your account first. Hmm, no thanks.

### Strox Phishing Kit & Page Features[⌗](#strox-phishing-kit--page-features)

> **`Strox` Kit** refers to the panel management interface that users use to manage their phishing pages. It is centralized and hosted by `Strox`.

![Strox Kit = Phishing Panel](/research/strox-guide-03.png)
> ***`Strox` Pages*** are phishing kits that exist as a single PHP file, so they are **not** provided to the buyer in a compressed file (e.g *.zip* file).
>
> Instead the **buyer is given an API key that allows them to deploy the phishing page to only the hosting server IP that they configure in the phishing page settings on the `Strox` platform. Otherwise the phishing page won’t load**.

![](/research/strox-guide-04.png)
> Also, `Strox` does not send out phishing results via email as is common with other phishing kits, but rather uses the ***Telegram bot*** method and also directly to the `Strox` phishing platform.

#### Highly Customizable[⌗](#highly-customizable)

![](/research/strox_page_order.png)

Any of these pages can be removed or modified by the phisher at any time.

> The `Strox` phishing pages/kits are highly customizable by the phisher and they can remove pages or add them as needed.

![](/research/custom_options.png)
> The phisher even can add their own new custom inputs onto the pages.

### Bulletproof Hosting[⌗](#bulletproof-hosting)

![](/research/strox-cpanel.png)

Surprisingly, `Strox` does not rely on hacked or compromised cPanel installations that are readily available from other hackers.

Instead `Strox` retains hosting at a so-called ***bulletproof host*** which just means web companies that don’t take down criminal content even after receiving complaints.

One of these ***bulletproof hosts*** is well known and goes by a few different names:

* **PONYTECH**
* **FranTech Solutions**
* **BuyVM**

These are all operating under the same AS - **[AS53667](https://ipinfo.io/AS53667#block-summary)**.

```
aut-num:    AS53667
as-name:    FRANTECH
descr:      Frantech Solutions
admin-c:    Francisco Dias
tech-c:     Francisco Dias
mnt-by:     MAINT-AS53667
changed:    [email protected] 20170106  #00:18:12Z
source:     RADB
```

And **PONYTECH** is a [known malware distributor as discovered by HP’s Threat Research team](https://threatresearch.ext.hp.com/mapping-malware-distribution-network/).

Usually bulletproof hosts are located in foreign countries to evade US law enforcement, but this one operates many web servers within US based datacenters.

They should probably familarize themselves with [recent arrests with potentially 20 year sentences that have been given to bulletproof host operators](https://www.zdnet.com/article/group-pleads-guilty-to-running-bulletproof-hosting-service-for-criminal-gangs-malware-payloads/).

#### URLScan.io[⌗](#urlscanio)

Also, I recommend checking out the `urlscan.io` pages for the two ASNs mentioned:

**[AS53667](https://urlscan.io/asn/AS53667)**

**[AS30823](https://urlscan.io/asn/AS30823)**

Many of the entries are malicious and this host operator should be investigated by law enforcement IMO.

## **Anti-Red/Never-Red/Anti-Bot Protection**[⌗](#anti-rednever-redanti-bot-protection)

`Strox` also recently (*late October 2022*) began offering a service that is supposed to protect non-`Strox` phishing pages from being detected by security services.

![](/research/anti-red-04.png)
> The name ***Anti/Never-Red*** refers to the buyer never receiving the nasty red browser warning page on the phishing page URL (which is not true, eventually it will be flagged).

### Installation Process[⌗](#installation-process)

You can view the video released by `Strox` on the process for configuring the ***Anti/Never-Red*** service:

*Click full screen if it doesn’t show anything while playing :x*

It basically just provides a *protector* directory that is used to store the phishing page files while performing bot filtering to prevent access to those malicious files.

## **Active Marketplace = Fast Way To Sell Phished Logins**[⌗](#active-marketplace--fast-way-to-sell-phished-logins)

![](/research/strox-guide-08.png)
> An int...