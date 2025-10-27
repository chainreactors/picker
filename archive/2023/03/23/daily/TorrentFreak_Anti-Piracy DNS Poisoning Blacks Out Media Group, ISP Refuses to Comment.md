---
title: Anti-Piracy DNS Poisoning Blacks Out Media Group, ISP Refuses to Comment
url: https://torrentfreak.com/anti-piracy-dns-poisoning-blacks-out-media-group-isp-refuses-to-comment-230322/
source: TorrentFreak
date: 2023-03-23
fetch_date: 2025-10-04T10:26:11.701298
---

# Anti-Piracy DNS Poisoning Blacks Out Media Group, ISP Refuses to Comment

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

# Anti-Piracy DNS Poisoning Blacks Out Media Group, ISP Refuses to Comment

March 22, 2023 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

For several days last week, visitors to the website of tech-focused media group Heise were diverted to Germany's piracy-blocking portal instead. Users of ISP 1&1 were diverted to a page reserved for pirate site visitors, informing them that Heise had been rendered inaccessible for copyright reasons. Calls for an explanation are met with silence.

[![website not available](https://torrentfreak.com/images/website-not-available.png)](https://torrentfreak.com/images/website-not-available.png)In a world where clear and independent reporting struggles to get heard in a sea of sensationalized clickbait, the German [Heise group](https://en.wikipedia.org/wiki/Heise_%28company%29) is generally recognized as a reliable and accurate news source.

For several days last week, an unknown number of visitors to [heise.de](https://www.heise.de/) were denied access to the company’s reporting. Instead, they found themselves redirected to Germany’s anti-piracy website blocking portal and statements that had no basis in fact.

## Silently Blocked For Several Days

A Heise analysis, published Tuesday, reveals that the publication first learned of issues affecting access to its website last Friday, March 17. More messages from readers were received on Monday, and all reported the same thing. When attempting to access heise.de, web browsers responded with a certificate error and an explanation.

A bright orange splash page informed Heise readers that due to copyright infringement, Heise had been rendered inaccessible. The message usually confronts internet users who attempt to access a specific set of sites previously identified as facilitators of mass online copyright infringement.

[![website not available](https://torrentfreak.com/images/website-not-available.png)](https://torrentfreak.com/images/website-not-available.png)

Heise had no idea why the message was being displayed but did find a common denominator. All of the readers reporting problems were using the same internet service provider – [1&1 AG](https://www.1und1.ag/), a €3.9 billion telecoms group servicing 15.6 million fixed line and mobile customers.

## DNS Tampering/Poisoning

Heise reports that its editors and system administrators were getting closer to the source of the problem on Friday but then a reader provided crucial information.

“He had set up his provider’s standard DNS server with the IP address 82.144.41.8 as the DNS server in his router,” Heise [reports](https://www.heise.de/news/DNS-Panne-heise-de-landet-bei-1-1-im-Copyright-Filter-7561803.html).

“This temporarily answered a question about www.heise.de with a CNAME entry that referred to the notice.cuii.info page. Other readers also confirmed that they were using the provider’s default DNS servers.”

Under normal conditions, web browsers accessing heise.de receive a response from the Domain Name System (DNS) to visit an IP address defined by the publication. In this case, Heise.de’s domain had a surprise CNAME (Canonical Name) entry that mapped heise.de to notice.cuii.info, the location of the orange splash screen carrying the copyright notification.

Since Heise itself is a 1&1 customer, staff tried to replicate the issues experienced by customers on a 1&1 DSL connection in the company’s editorial office. That ultimately failed and the redirect eventually disappeared on its own.

## Heise Requests Answers, Receives None

In an effort to get to the bottom of the mystery, Heise said it contacted 1&1’s press office. The publication was informed that the internet service provider’s technical department would investigate but as things stand, Heise has received no response.

“The case remains a mystery: Only a small proportion of the queries to 1&1 DNS servers seem to be affected, and it is also not a regional problem. The tips came from Berlin and Hesse, among others,” Heise reports.

Starting from the position that the Domain Name System shouldn’t be tampered with, the question is why that appears not to be the case here. The short answer is that, with assistance from 1&1, Germany has implemented a DNS tampering system that enables rightsholders to redirect 1&1’s customers to a blocking page when they attempt to access specific pirate site domains.

## CUII and Site-Blocking in Germany

Copyright Clearing House on the Internet (CUII) was [launched in 2021](https://torrentfreak.com/isps-and-rightsholders-unite-to-block-pirate-sites-in-germany-210311/). It operates from cuii.info and its blocking notification page is located at notice.cuii.info, the subdomain/domain that appeared in Heise.de’s DNS CNAME records.

“The Copyright Clearing House on the Internet (CUII) is an independent body. It was set up by Internet access providers and rights holders in order to use objective criteria to check whether the blocking of access to a structurally infringing website is lawful,” CUII explains.

Current members of CUII: *1&1 AG (telecoms), German Book Traders’ Association, Federal Music Industry Association (BVMI), German Football League (DFL), Freenet DLS (telecoms), German Games Industry Association, Motion Picture Association (MPA), Sky Deutschland, STM (publishers), Telefónica Germany, Telekom Germany, German Film Producers Association (VDF), and Vodafone Germany.*

[![heise-cuii](https://torrentfreak.com/images/heise-cuii.png)](https://torrentfreak.com/images/heise-cuii.png)

“At the request of the rights holder, a review committee will examine and, if the requirements are met, recommend a DNS blocking of this structurally copyright-violating website,” the [CUII website notes](https://cuii.info/faq/).

When a blocking decision is recommended, the matter is then referred to the German government’s Federal Network Agency (BNetzA) to confirm that a blockade will not violate net neutrality. Currently a [small number of pirate sites](https://cuii.info/empfehlungen/) are affected.

[![cuii blocking decisions](https://torrentfreak.com/images/cuii-blocking-decisions-.png)](https://torrentfreak.com/images/cuii-blocking-decisions-.png)

## Code of Conduct

CUII’s stated purpose to recommend blocking of websites whose main purpose is to infringe copyright. The body is limited to handling “clear cases” where platforms have no real interest in supplying legal content.

Under its code of conduct, CUII observes the requirements laid down by the Court of Justice of the European Union to prevent internet service providers from encroaching on internet users’ freedom to access information online.

“For this reason, the Federal Network Agency is also involved in the process as the competent authority so that it can review the recommended blocking based on the requirements of the Net Neutrality Ordinance,” CUII notes.

## Who Will Accept Responsibility?

Given all of the checks, processes and...