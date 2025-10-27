---
title: Google Receives Piracy Shield Orders to Block Pirate Sites in Public DNS
url: https://torrentfreak.com/google-receives-piracy-shield-orders-to-block-pirate-sites-in-public-dns-250618/
source: TorrentFreak
date: 2025-06-19
fetch_date: 2025-10-06T22:57:22.235200
---

# Google Receives Piracy Shield Orders to Block Pirate Sites in Public DNS

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

# Google Receives Piracy Shield Orders to Block Pirate Sites in Public DNS

June 18, 2025 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

Italian telecoms regulator AGCOM has regularly criticized Google over its anti-piracy efforts, but the signs suggest that change is on the way. AGCOM says a system activated last month, relayed blocking orders received by the Piracy Shield anti-piracy system, directly to Google, which "promptly" blocked pirate site domains on its public DNS resolver. AGCOM says the system should be fully operational "as soon as possible" but warns that Google will still have to do more.

![piracy-shield-planet-s](https://torrentfreak.com/images/piracy-shield-planet-s.png)
In countries where site-blocking has been established for years, relatively small but always expanding measures happen mostly unannounced. It’s often too late to complain when the public are the last to know.

Enhanced blocking measures and tools, with an emphasis on speed and limited judicial oversight, already receive support under national law. Italy’s high profile Piracy Shield system is one such example; mandatory participation by local ISPs to rapidly block alleged pirate sites, no questions asked, has now expanded to [other service providers and intermediaries](https://torrentfreak.com/italy-approves-piracy-shield-vpn-dns-proposal-risk-of-prison-for-isps-intact-241001/) in less than two years.

Operators of third party DNS resolvers, such as Cloudflare, Google, and Quad9, are now seen as [anti-piracy enforcers](https://torrentfreak.com/google-cloudflare-summoned-to-explain-their-plans-to-defeat-pirate-iptv-240805/) with an obligation to comply. Internet users who find themselves blocked by their ISP, can use public DNS resolvers to circumvent blocking. Italy wants to close that loophole as quickly as possible and according to AGCOM, work with Google is already underway.

## Court Instructs Google to Join Piracy Shield

Piracy Shield welcomed a new, but presumably reluctant addition to the site-blocking framework as part of a limited trial last month.

Google’s involvement is linked to a decision handed down by the Court of Milan last December. When football league Serie A complained that Cloudflare was refusing to comply with site-blocking orders, the Court said that a failure to block moving forward would incur fines of €10,000 per day.

A similar [case against Google](https://torrentfreak.com/court-orders-google-to-poison-public-dns-to-prevent-iptv-piracy-250321/) reached the same conclusion in March. AGCOM said that Serie A’s case was so strong, Google’s participation in the proceeding wasn’t required.

Google’s participation in Piracy Shield most certainly was, however.

## Piracy Shield Relayed Blocking Orders to Google

The football clubs of Serie A played their last games of the season May 23-25. In line with established procedures, rightsholder monitoring during the days running up to those matches led to pirate site domain names and IP addresses being added to the non-public Piracy Shield database.

According to AGCOM commissioner Massimiliano Capitanio, once the final matches got underway, blocking instructions sent by rightsholders to Piracy Shield, were relayed by the latter to local ISPs, and also directly to Google.

“Through a process developed with the Mountain View company, the sites reported on the Piracy Shield platform during the last championship matches were promptly communicated to Google which, consequently, prevented access through its public DNS. A first but important sign of collaboration in this battle for legality,” Capitanio said.

![google dns](https://torrentfreak.com/images/google-dns-1.png)

When presented with a domain name, Google’s DNS ordinarily responds with the relevant IP address as determined by its records, thus facilitating access to the corresponding website. When a domain name is operated by pirates offering live football streams, for example, internet users who access the domain may reach a site where Serie A matches are made available for free.

Once Google blocks or otherwise tampers with the records that link a domain to an IP address, users of Google’s DNS won’t be directed to the pirate site in question. The extent of Google’s blocking in the trial last month is unknown but, in theory, it could’ve been significant.

## Piracy Shield Transparency Remains Poor

Behind-the-scenes operations at Piracy Shield are not for public consumption. Since the domain names and IP addresses blocked via the platform aren’t made available officially, reliance on data made available unofficially is the only option available.

![piracy shield tickets1](https://torrentfreak.com/images/piracy-shield-tickets1.png)

As illustrated in the image above, domains ([FQDN](https://en.wikipedia.org/wiki/Fully_qualified_domain_name#:~:text=A%20fully%20qualified%20domain%20name,domain%20and%20the%20root%20zone.)) and IPv4 IP addresses are quite heavily redacted; most likely a necessary limitation to ensure that the valuable [*piracyshield.iperv.it*](https://piracyshield.iperv.it/) resource stays online.

Fortunately, the redactions don’t hinder collection of data on the number of domains and IP addresses blocked, and the dates when those blocks were requested.

Data shows that blocking requests in the days leading up to May 23 and ending on May 25 when the championship games concluded, concerned 988 FQDN and 78 IPv4 IP addresses.

![](https://torrentfreak.com/images/serie-a-final-matches-likely-blocked-by-Google.png)

How many tickets were processed by Google, either in full, in part, or not, is unavailable to the public. Running totals of the number of domains and IP addresses requested for blocking overall is the extent of current transparency, with no sign of change anytime soon.

There are no obvious surprises in the tickets referenced above, but the presence of Amazon IP addresses had the potential to pique Google’s interest, if nothing else.

## Google Will Still Need to Do More

Describing the tests last month as “experimental”, Commissioner Capitanio expects to see Google’s full participation in the very near future.

“The goal is for this experimental activity to be fully operational as soon as possible and for other entities involved in the accessibility of pirate sites, such as VPNs, to adopt automated measures to block pirate sites within 30 minutes of AGCOM’s report, in full compliance with national law,” he explains.

“At the same time, other actions must be taken to combat the phenomenon, such as prohibiting access to pirate APPs and continuing to sanction users who illegally use these services.”

In a world filled with uncertainty, “other actions must be taken” is an anti-piracy standard that hasn’t changed in decades; most likely, it never will.

* [![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/arrow-left.svg)Next Post](https://torrentfreak.com/x-vs-...