---
title: BIScience: Collecting browsing history under false pretenses
url: https://palant.info/2025/01/13/biscience-collecting-browsing-history-under-false-pretenses/
source: Over Security - Cybersecurity news aggregator
date: 2025-01-14
fetch_date: 2025-10-06T20:12:55.410606
---

# BIScience: Collecting browsing history under false pretenses

[Almost Secure](/)

* [Home](/)
* [Articles](/articles/)
* [Categories](/categories/)
* [About](/about/)
* ##

  Read More Â»

[ ]

# BIScience: Collecting browsing history under false pretenses

2025-01-13
 [Add-Ons](/categories/add-ons/)/[Privacy](/categories/privacy/)/[Google](/categories/google/)
 14 mins
 [0 comments](/2025/01/13/biscience-collecting-browsing-history-under-false-pretenses/#comments)

* This is a guest post by a researcher who wants to remain anonymous. You can contact the author via email.

Recently, John Tuckner of Secure Annex and Wladimir Palant published [great research](https://secureannex.com/blog/sclpfybn-moneitization-scheme/) about how BIScience and its various brands collect user data. This inspired us to publish part of our ongoing research to help the extension ecosystem be safer from bad actors.

This post details what BIScience does with the collected data and how their public disclosures are inconsistent with actual practices, based on evidence compiled over several years.

![Screenshot of a website citing a bunch of numbers: 10 Million+ opt-in panelists globally and growing, 60 Global Markets, 4.5 Petabyte behavioral data collected monthly, 13 Months average retention time of panelists, 250 Million online user events per day, 2 Million eCommerce product searches per day, 10 Million keyword searches recorded daily, 400 Million unique domains tracked daily](/2025/01/13/biscience-collecting-browsing-history-under-false-pretenses/biscience-website.png)

Screenshot of claims on the BIScience website

#### Contents

* [Who is BIScience?](#who-is-biscience)
  + [BIScience collects data from millions of users](#biscience-collects-data-from-millions-of-users)
* [BIScience buys data from partner third-party extensions](#biscience-buys-data-from-partner-third-party-extensions)
* [BIScience receives raw data, not anonymized data](#biscience-receives-raw-data-not-anonymized-data)
* [Misleading CWS policies compliance](#misleading-cws-policies-compliance)
  + [BIScience extensions exception claims](#biscience-extensions-exception-claims)
  + [Partner extensions exception claims, guided by BIScience](#partner-extensions-exception-claims-guided-by-biscience)
    - [BIScience SDK](#biscience-sdk)
    - [Unnecessary features](#unnecessary-features)
    - [Misleading privacy policy disclosures](#misleading-privacy-policy-disclosures)
    - [Misleading user consent](#misleading-user-consent)
* [Our hope for the future](#our-hope-for-the-future)
* [Related reading](#related-reading)
* [IOCs](#iocs)

## Who is BIScience?

BIScience is a long-established data broker that owns multiple extensions in the Chrome Web Store (CWS) that collect clickstream data under false pretenses. They also provide a software development kit (SDK) to partner third-party extension developers to collect and sell clickstream data from users, again under false pretenses. This SDK will send data to `sclpfybn.com` and other endpoints controlled by BIScience.

“Clickstream data” is an analytics industry term for “browsing history”. It consists of every URL users visit as they browse the web.

According to their website, BIScience “provides the deepest digital & behavioral data intelligence to market research companies, brands, publishers & investment firms”. They sell clickstream data through their [Clickstream OS](https://www.biscience.com/clickstreamos/) product and sell derived data under other product names.

BIScience owns AdClarity. They provide “advertising intelligence” for companies to monitor competitors. In other words, they have a large database of ads observed across the web. They use data collected from services operated by BIScience and third parties they partner with.

BIScience also owns Urban Cyber Security. They provide VPN, ad blocking, and safe browsing services under various names: Urban VPN, 1ClickVPN, Urban Browser Guard, Urban Safe Browsing, and Urban Ad Blocker. Urban collects user browsing history from these services, which is then sold by BIScience to third parties through Clickstream OS, AdClarity, and other products.

BIScience also owned GeoSurf, a residential proxy service that shut down in December 2023.

### BIScience collects data from millions of users

BIScience is a huge player in the browser extension ecosystem, based on their own claims and our observed activity. They also collect data from other sources, including Windows apps and Android apps that spy on other running apps.

The websites of BIScience and AdClarity make the following claims:

* They collect data from 25 million users, over 250 million user events per day, 400 million unique domains
* They process 4.5 petabytes of data every month
* They are the “largest human panel based ad intelligence platform”

These numbers are the most recent figures from all pages on their websites, not only the home pages. They have consistently risen over the years based on archived website data, so it’s safe to say any lower figures on their website are outdated.

## BIScience buys data from partner third-party extensions

BIScience proactively contacts extension developers to buy clickstream data. They claim to buy this data in anonymized form, and in a manner compliant with Chrome Web Store policies. Both claims are demonstrably false.

Several third-party extensions integrate with BIScience’s SDK. Some are listed in the Secure Annex [blog post](https://secureannex.com/blog/sclpfybn-moneitization-scheme/), and we have identified more in the [IOCs section](#iocs). There are additional extensions which use their own custom endpoint on their own domain, making it more difficult to identify their sale of user data to BIScience and potentially other data brokers. Secure Annex identifies October 2023 as the earliest known date of BIScience integrations. Our evidence points to 2019 or earlier.

Our internal data shows the Visual Effects for Google Meet extension and other extensions collecting data since at least mid-2022. BIScience has likely been collecting data from extensions since 2019 or earlier, based on public GitHub posts by BIScience representatives ([2021](https://github.com/120Studio/120home/issues/22), [2021](https://github.com/RaeAtBiscience/RaeAtBiscience/blob/main/ME.me), [2022](https://github.com/Rae1223/monetisation)) and the 2019 [DataSpii research](https://arstechnica.com/information-technology/2019/07/dataspii-inside-the-debacle-that-dished-private-data-from-apple-tesla-blue-origin-and-4m-people/) that found some references to AdClarity in extensions. BIScience was founded in 2009 when they launched GeoSurf. They later [launched AdClarity](https://techcrunch.com/2012/02/16/adclarity-launch/) in 2012.

## BIScience receives raw data, not anonymized data

Despite BIScience’s claims that they only acquire anonymized data, their own extensions send raw URLs, and third-party extensions also send raw URLs to BIScience. Therefore BIScience collects granular clickstream data, not anonymized data.

If they meant to say that they only use/resell anonymized data, that’s not comforting either. BIScience receives the raw data and may store, use, or resell it as they choose. They may be compelled by governments to provide the raw data, or other bad actors may compromise their systems and access the raw data. In general, collecting more data than needed increases risks for user privacy.

Even if they anonymize data as soon as they receive it, anonymous clickstream data can contain sensitive or identifying information. A notable example is the [Avast-Jumpshot case](/2019/10/28/avast-online-security-and-avast-secure-browser-are-spying-on-you/) discovered by Wladimir Palant, who also wrote a [deep dive](/2020/02/18/insights-from-avast/jumpshot-data-pitfalls-of-data-anonymization/) into why anonymizing browsing history is very hard.

As the [U.S. FTC investigation found](https://www.ftc.gov/legal-library/browse/cases-proceedings/2023033-avast), Jumpshot stored unique device IDs tha...