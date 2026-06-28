---
title: EU-Backed DNS Resolver Collects Pirate Site Blocklist, Which It Doesn’t Use
url: https://torrentfreak.com/eu-backed-dns-resolver-collects-pirate-site-blocklist-which-it-doesnt-use/
source: TorrentFreak
date: 2026-06-27
fetch_date: 2026-06-28T06:14:23.186750
---

# EU-Backed DNS Resolver Collects Pirate Site Blocklist, Which It Doesn’t Use

[![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/logo.svg)](/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/search.svg)

* News ▼
  + [Piracy](https://torrentfreak.com/category/piracy/)
  + [Piracy Research](https://torrentfreak.com/category/research/)
  + [Law and Politics](https://torrentfreak.com/category/law-politics/)
  + [Lawsuits](https://torrentfreak.com/category/lawsuits/)
  + [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/)
  + [Technology](https://torrentfreak.com/category/technology/)
* [Contact](https://torrentfreak.com/contact/)
* [Subscribe](https://torrentfreak.com/subscriptions/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/x.svg)

# EU-Backed DNS Resolver Collects Pirate Site Blocklist, Which It Doesn’t Use

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") >

DNS4EU is a relatively young DNS provider that launched last year with European Commission funding. The company is pitched as a privacy-first alternative to Google and Cloudflare, but it also comes with site blocking in mind. DNS4EU has shown an interest in pirate site blocklists, including the one that's maintained by Dutch anti-piracy group BREIN. After looking into it, however, DNS4EU decided not to use them, because BREIN isn't a government authority.

![dns4eu](https://torrentfreak.com/images/dns4eu-600x387.png)Earlier this month, [BREIN published](https://stichtingbrein.nl/annual-report-2025/) its latest annual report, providing insights into its priorities and achievements.

Among other things, the Dutch anti-piracy group reports that it shut down 50 IPTV/VOD subscription vendors, 42 streaming sites, while also stopping 673 pirate site proxies and mirrors.

BREIN also keeps the Dutch pirate site blocklist up to date. By the end of 2025 it covered 303 unique domains, 13 platforms, and 8 IP addresses. These are part of the dynamic blocking efforts, backed by a voluntary agreement with ISPs, as well as court orders.

## BREIN Shares Blocklist Data With DNS4EU

By now, most Dutch site blocking efforts are standard practice, but BREIN also shared a new and intriguing detail in its full report, which involves the European DNS resolver [DNS4EU](https://joindns4.eu/).

As it turns out, BREIN is actively and automatically sharing the Dutch blocklist data with DNS4EU.

BREIN was under the impression that the blocklist data would be used to block pirate sites. Understandably, that is something the group wholeheartedly supports.

“BREIN sees several advantages, particularly the ability to block illegal sites more effectively. BREIN therefore shares the details of websites blocked in the Netherlands and sends DNS4EU up-to-date lists of blocked websites,” BREIN’s annual report reads.

Speaking with TorrentFreak, BREIN’s director Bastiaan van Ramshorst explains that they offer secure access to the same blocklist server that ISPs use. In addition, DNS4EU reportedly said that it would be interested in getting similar data from other countries as well.

## Funded by the EU, Blocking in Mind

BREIN’s report and comment don’t explain why the DNS provider might be interested in blocklists, but the DNS provider’s origins provide useful context.

DNS4EU is a public DNS resolver, co-funded by the European Commission and currently operated by a consortium led by Czech cybersecurity company [Whalebone](https://www.whalebone.io/). The service launched [last year](https://joindns4.eu/learn/dns4eu-public-service-launched) as a sovereign European alternative to non-EU resolvers such as Google Public DNS and Cloudflare.

When the European Commission published its call for proposals in 2022, the tender specified that the resolver should be able to filter illegal material on legal grounds. As [we reported at the time](https://torrentfreak.com/the-eu-wants-its-own-dns-resolver-that-can-block-unlawful-traffic-220119/), the documentation listed the following requirement.

“Filtering of URLs leading to illegal content based on legal requirements applicable in the EU or in national jurisdictions (e.g. based on court orders), in full compliance with EU rules.”

This type of blocking can also expand to copyrighted content. This is already taking place in response to court orders, [such as in France](https://joindns4.eu/legal-information-and-compliance), but the agreement between BREIN and DNS4EU suggests that voluntary blocking could be an option too.

Whalebone now runs DNS4EU without EU funding, but it appears that the interest in blocking remained.

## No Voluntary Pirate Site Blocks

The logical assumption that DNS4EU would use the blocklist data to block sites can’t be backed up by data. TorrentFreak’s tests show that blocked domains, including The Pirate Bay, are readily accessible, also from The Netherlands.

To find out more about DNS4EU’s plans with this case, we reached out to the operating company Whalebone, which declined to confirm any blocking and pointed to the DNS4EU resolver policy instead.

Under [that policy](https://legal-documents-dns4eu.s3.fr-par.scw.cloud/DNS4EU-Public-DNS-Resolver-policy-2025.pdf), DNS4EU commits “not to block DNS resolution except for when required by law, enforceable decision of the competent court or other government authority or elected by the User.”

From DNS4EU’s Policy
[![not to block](https://torrentfreak.com/images/notoblock.png)](https://torrentfreak.com/images/notoblock.png)

The Dutch blocklist is based on civil court orders against the ISPs, not against DNS4EU. This means that DNS4EU is not legally required to take action.

DNS4EU’s own numbers confirm that it is not taking any voluntary action, at least where copyright is concerned. Its first transparency report, covering June through December 2025, logs roughly 63 million voluntary “own-initiative” blocks. These are almost all linked to phishing and scam domains.

The number of blocked domains in the copyright infringement category is zero, as is the total for the broader intellectual property category.

## No Reason to Block

This chain of events raises an obvious question. Why would DNS4EU reach out to BREIN to request access to the blocklist, and ask for more, only to leave it untouched?

When we first pressed Whalebone, a spokesperson explained that, while the company leads the [DNS4EU consortium](https://joindns4.eu/about#consortium), other members are involved and there was no agreement yet on how to move forward.

“I need to check with them what was the agreement,” the Whalebone spokesperson informed us two weeks ago. “These discussions are currently ongoing.”

Shortly before publication, after consulting the consortium, Whalebone followed up with a fuller statement, which it says was also sent to BREIN. This time the answer was clear: the data will not be used.

“DNS4EU team contacted BREIN regarding this matter, however, we later discovered that BREIN is not the governmental regulatory body. Therefore, there is no reason to proceed with implementing their blocking list. The data has not been used in any way,” the statement reads.

This neatly explains why BREIN’s blocklist is not put to use by the DNS provider. However, it also raises additional questions. Does DNS4EU currently block sites based on blocklists from governmental regulators, and if so, are any of these blocklists currently in place?

* [Previous Post![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/arrow-right.svg)](https://torrentfreak.com/ace-uefa-and-mexico-chase-pirlotvs-950-million-visit-piracy-network/)

### Tagged In:

* [brein](https://torrentfreak.com/tag/brein/)
* [DNS](https://torrentfreak.com/tag/dns/)
* [dns4eu](https://torrentfreak.com/tag/dns4eu/)

### You Might Also Like:

[![](https://torrentfreak.com/...