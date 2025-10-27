---
title: DAZN’s Piracy Shield ‘Smart TV’ Block Revoked After IPTV Portal Complaint
url: https://torrentfreak.com/dazns-piracy-shield-smart-tv-block-revoked-after-iptv-portal-complaint-241111/
source: TorrentFreak
date: 2024-11-12
fetch_date: 2025-10-06T19:27:52.282999
---

# DAZN’s Piracy Shield ‘Smart TV’ Block Revoked After IPTV Portal Complaint

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

# DAZN’s Piracy Shield ‘Smart TV’ Block Revoked After IPTV Portal Complaint

November 11, 2024 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [Site Blocking](https://torrentfreak.com/category/anti-piracy/site-blocking/ "Go to the Site Blocking category archives.") >

After DAZN received a warning for the blunder that saw Google Drive blocked in Italy, a company behind a smart TV video player app had a DAZN-initiated blocking decision revoked after a successful appeal. That may seem like a win, but the finer details reveal a legal framework that favors rightsholders so strongly, online services incurring liability for the actions of users seems inevitable.

![piracy-shield-planet-s](https://torrentfreak.com/images/piracy-shield-planet-s.png)
While judicial oversight may be initially unavoidable when site-blocking is first introduced to a country, systems with less friction are strongly preferred.

The law that supports Italy’s Piracy Shield system allows for blocking with no judicial oversight. An amendment passed quietly last year now allows rightsholders to block online resources without any input from telecoms regulator AGCOM. The system has almost no friction at the blocking stage. That comes at the cost of significant blunders, which could been prevented by proper checks and balances.

Details of a complaint alleging more unwarranted blocking reveal an unusual situation where the interpretation of new law and its blocking boundaries appear to be determined by rightsholders alone. There’s no case law to provide guidance and any complaints are handled at a significantly slower pace than initial blocking takes place.

## DAZN Files Complaint Against Smart TV Software

DAZN added *https://tizen.smartone-iptv.com* and *https://lg.smartone-iptv.com* to the Piracy Shield blocking platform on August 18, rendering both inaccessible in Italy. This action is based on assertions that the domains were violating its Serie A football broadcasting rights.

According to AGCOM, DAZN’s evidence was supported by a declaration that the reported domain names are “unequivocally intended for the violation of copyright or related rights of audiovisual works,” including sporting events broadcast live.

The regulator’s report clearly states that DAZN’s declaration was provided “under its own responsibility.” On face value that seems to indicate that no other entity is responsible when things go wrong.

## SmartOne Files Objection

After being placed on the system, Italian ISPs blocked both resources. Two days later, on August 20, SmartOne filed a formal complaint with AGCOM to protest the blocking. An excerpt of that correspondence, translated but otherwise ‘as-is’, reads as follows;

> *The domains (DNS) belong to a Smart TV application, it’s a player and entertainment application agreed and approved by so many TV manufacturers like Samsung, LG, Hisense, Toshiba, VIDAA OS and so many others.*
>
> We don’t sell any contents and IPTV data, our domain includes the IPTV word and might cause confusion for so many parties, but we can provide any info or proof to show that we don’t offer any piracy contents or illegal contents. We hereby request to remove our domains from the block system: tizen.smartone-iptv.com, lg.smartone-iptv.com, and any other domain related to smartone- iptv.com […]

The subdomains in the two [fully qualified domain names](https://en.wikipedia.org/wiki/Fully_qualified_domain_name) (FQDNs) supplied by DAZN suggest that each brand is allocated its own subdomain.

We can confirm that the subdomains androidtv, webos, foxxum, vestel and others also exist, indicating a typical setup for an app catering for different technical requirements on a per-manufacturer basis. Those FQDN subdomains are not blocked.

![smartone-tv](https://torrentfreak.com/images/smartone-tv.png)

In its report responding to the complaint, AGCOM refers again to DAZN’s evidence, which clearly states content being made available, in violation of DAZN’s rights.

## DAZN Insists SmartOne is a Pirate IPTV Service

“From the checks carried out on the domain names reported through the relevant documentation attached by the reporting party, it appeared that the live broadcast of the matches of the Italian Serie A football championship were made available in violation of articles 1, paragraph 1, 12, 13, 16 and 78-bis, 78-ter, of the aforementioned law no [633/41](https://wipolex-res.wipo.int/edocs/lexdocs/laws/en/it/it211en.html),” AGCOM explains.

On September 2, 2024, SmartOne sent counter-arguments to AGCOM for use in the complaint procedure.

“We do not provide any content or transfer any matches or videos that are owned by any other company such as ‘Dazn’ or ‘la Società’ claims, the content operated on the program is under the user’s responsibility,” the communication reads.

“The links https:// tizen.smartone-iptv.com and https:// lg.smartone-iptv.com are links that contain some program operating files and do not contain any link to broadcasts of the Italian League, and we are ready to provide any other clarifications or other information.”

Nevertheless, DAZN had made its position clear and in its counter-arguments, refused to concede even an inch.

“These FQDNs were found to be linked to IP addresses that we reported for suspicious activity. Forensic analysis […] confirmed that the detected IP addresses are unique and directly linked to the illicit IPTV broadcasts,” DAZN said in its response.

“It is important to underline that, although Smartone-IPTV may initially appear as a simple generic player, the evidence collected and uploaded to the Piracy Shield Platform clearly indicates that it plays not only a Player role, but also an active role in the distribution of abusive content.”

## Domains Play ‘Active Role’

Our checks on an unofficial Piracy Shield database revealed that both FQDNs were added to the blocklist on August 18, 2024, around 18:40. In both cases the main domain (smartone-iptv.com) operates via Cloudflare IP addresses, but the subdomains do not.

![smartone-1](https://torrentfreak.com/images/smartone-1.png)

Each subdomain has its own IP address at hosting provider Hetzner Online which link to other domains, each with a reference to LG/Tizen. As DAZN points out, the IP addresses used are indeed unique.

What “active role” they play in the distribution of ‘abusive’ content isn’t immediately clear but neither the IP addresses nor the domains were put on the Piracy Shield blocklist. Why that’s the case given the role they allegedly play only makes things even more unusual.

## AGCOM Considers Evidence and Renders its Decision

AGCOM’s summing up of DAZN’s evidence and what that means for the complaint is a bit of a rollercoaster; it begins with good news for SmartOne, then cites information that suggests suspicion of illicit activity, but without sufficient confidence to act accordingly.

> *The SmartOne IPTV application does not provide pre-configured streaming video content lists, but these must be uploaded by users. In particular, SmartOne IPTV impleme...