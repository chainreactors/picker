---
title: AGCOM Runs Massive Piracy Blocking Operation But Has ‘Trouble’ Configuring Its Domain Name?
url: https://torrentfreak.com/agcom-runs-massive-piracy-blocking-operation-but-has-trouble-configuring-its-domain-name-240316/
source: TorrentFreak
date: 2024-03-17
fetch_date: 2025-10-04T12:10:11.918242
---

# AGCOM Runs Massive Piracy Blocking Operation But Has ‘Trouble’ Configuring Its Domain Name?

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

# AGCOM Runs Massive Piracy Blocking Operation But Has ‘Trouble’ Configuring Its Domain Name?

March 16, 2024 by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Opinion Articles](https://torrentfreak.com/category/opinion/ "Go to the Opinion Articles category archives.") >

Italian telco watchdog AGCOM has taken on the task of rolling out one of the largest piracy-blocking schemes the Internet has ever witnessed. The organization fiercely defends its IP-address blocking efforts and has full confidence in its technical expertise. Curiously, however, AGCOM's domain name is only partly functioning, as it explicitly requires a www subdomain.

![banana](https://torrentfreak.com/images/banada.jpg)

AGCOM issues the relevant site IP address blocking orders and, from the get-go, it countered critics by stating that the system was “working perfectly”.

High marks aside, Internet providers and network specialists painted a different picture. They noticed several [overblocking examples](https://torrentfreak.com/fake-news-propaganda-props-up-piracy-shield-errors-dismissed-as-lies-240225/) and not just small ones either. In response to one order, ISPs were required to block an IP address belonging to Internet infrastructure provider Cloudflare, which reportedly rendered [thousands of websites](https://torrentfreak.com/piracy-shield-cloudflare-disaster-blocks-countless-sites-fires-up-opposition-240226/) unreachable across Italy.

AGCOM prefers not to give credence to the widespread critique and remains laser-focused on defeating online piracy. This week, tensions rose to alarming levels when AGCOM chief Massimiliano Capitanio issued a new warning, suggesting that people watching pirate streams or downloading piracy apps, risk fines of up to 5,000 euros.

While Capitanio’s comments are certainly not intended as “[psychological terrorism](https://torrentfreak.com/pirate-iptv-user-fines-soon-but-not-psychological-terrorism-240313/),” some framed it as nuanceless scaremongering. At this point, however, it’s clear that very little is going to stop AGCOM from going full steam ahead with its anti-piracy efforts. And, as long as the group operates within the legal boundaries, they have every right to do so.

Taking the hard-line does come with risks, however. Small mistakes can turn into big ones and oversights risk being framed as incompetence; or worse; counter-ammunition. For example, the Piracy Shield’s overblocking errors may fuel site-blocking opposition in other countries, including in the United States where lawmakers are wary of overblocking.

## AGCOM Domain ‘Troubles’

In a similar vein, the public may start to notice other purported errors. That happened earlier this week when we were alerted to the fact that AGCOM’s domain name, agcom.it, is configured rather peculiarly. The domain only works through the [www](https://www.agcom.it/) version, but not [without it](https://agcom.it/).

While the www. subdomain is a largely outdated concept nowadays, most sites still support it by [properly](https://www.cloudflare.com/learning/dns/dns-records/dns-a-record/) configuring the domain’s [A records](https://dnschecker.org/all-dns-records-of-domain.php?query=www.torrentfreak.com&rtype=ALL&dns=opendns). For example, if you try to access <https://www.torrentfreak.com> in a browser we will redirect you to the non-www version you’re on now.

Pretty much all websites operate this way, including the domain names of anti-piracy outfits such as ACE, the RIAA, and BREIN. The sites can be accessed with and without www, with one redirecting visitors to the other. Setting this up this way takes less than a minute.

For some reason, however, AGCOM has decided [not to add any official records](https://dnschecker.org/all-dns-records-of-domain.php?query=agcom.it&rtype=ALL&dns=opendns) for its root domain. We can’t think of a practical reason why this is the case, so we assume that this is an oversight that makes the site harder to reach.

![agcom](https://torrentfreak.com/images/agcom-noa.jpg)

## Root Domain Unreachable

Luckily, most popular browsers correct these types of errors when you enter the domain name in the address bar, but following a direct link will lead nowhere. DNS resolvers simply don’t know to what IP-address the traffic should go.

![agcom not accesible](https://torrentfreak.com/images/agcom-not-reached.jpg)

This isn’t some type of standard we’re making up, it’s one of the basic principles of the web as [DNSimple explains](https://support.dnsimple.com/articles/common-dns-records/#common-dns-records-1).

“Each domain needs to have a record for the root domain. Otherwise your domain won’t resolve, and accessing the URL in the browser will return a resolution error.”

To make matters more confusing, AGCOM also has some other subdomains, including [geo.agcom.it](https://geo.agcom.it/) and conciliaweb.agcom.it. These both work fine, without an extra www subdomain.

Again, we have no idea why AGCOM hasn’t configured its root domain properly. For many other organizations, this would be a petty issue, but since AGCOM is a key player in one of the largest blocking operations on the Internet, dubious technical decisions may find themselves under the spotlight.

TorrentFreak asked AGCOM for a comment on our findings but the telco watchdog didn’t immediately respond. The MX records for agcom.it are properly configured, however, so our question should have arrived, assuming that our domain isn’t on any blocklist.

* [![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/arrow-left.svg)Next Post](https://torrentfreak.com/laligas-card-sharing-piracy-fight-harmed-by-misinformation-confusion-240317/)
* [Previous Post![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/arrow-right.svg)](https://torrentfreak.com/bittorrent-is-no-longer-the-king-of-upstream-internet-traffic-240315/)

### Tagged In:

* [italy](https://torrentfreak.com/tag/italy/)
* [Piracy Shield](https://torrentfreak.com/tag/piracy-shield/)

### You Might Also Like:

[![](https://torrentfreak.com/images/sky-piracyshield-xfac-500x210.png)

Anti-Piracy

### Italy Expands Piracy Shield to Live TV, Begins With ‘The X Factor’

* September 24, 2025, 13:53 by Andy Maxwell](https://torrentfreak.com/italy-expands-piracy-shield-to-live-tv-begins-with-the-x-factor-250924/)

[![](https://torrentfreak.com/images/reseller-f-500x210.png)

Anti-Piracy

### New Pirate IPTV Police Operation Raises Stakes For Resellers & Customers

* September 18, 2025, 11:34 by Andy Maxwell](https://torrentfreak.com/new-pirate-iptv-police-operation-raises-stakes-for-resellers-customers-250918/)

[![](https://torrentfreak.com/images/wiredmessfeat-500x210.jpg)

Anti-Piracy

### Internet Society: Italy’s “Piracy Shield” Failures Are a Warning Against “Blunt” Piracy Blocking

* September 13, 2025, 13:38 by Ernesto Van der Sar](https://torrentfreak.com/internet-society-italys-piracy-shield-failures-are-a-warning-against-blunt-piracy-blocking/)

![](https://torrentfreak.com/wp-content/themes/tf-theme-v2/build/assets/img/comment.svg)

[Submit a correction or tip.](/contact/)

##### Sponsors

[...