---
title: Cloudflare Reports Surge in Streaming Piracy Takedowns, Removes 20k+ Storage Accounts
url: https://torrentfreak.com/cloudflare-reports-surge-in-streaming-piracy-takedowns-removes-20k-storage-accounts/
source: TorrentFreak
date: 2025-12-28
fetch_date: 2025-12-29T03:34:39.518157
---

# Cloudflare Reports Surge in Streaming Piracy Takedowns, Removes 20k+ Storage Accounts

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

# Cloudflare Reports Surge in Streaming Piracy Takedowns, Removes 20k+ Storage Accounts

today by
[Ernesto Van der Sar](https://torrentfreak.com/author/ernesto/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Anti-Piracy](https://torrentfreak.com/category/anti-piracy/ "Go to the Anti-Piracy category archives.") > [DMCA](https://torrentfreak.com/category/anti-piracy/dmca/ "Go to the DMCA category archives.") >

Cloudflare’s latest transparency report reveals a massive 3,800% surge in copyright-related takedown actions, fueled by a shift to more automated enforcement. By granting rightsholders direct API access, the company says that it was able to target live sports streaming piracy more effectively. This resulted in the termination of over 20,000 R2 storage accounts in just six months.

![cloudflare logo](https://torrentfreak.com/images/cloudflare-logo-dark.jpg)
As one of the leading Internet infrastructure companies, [Cloudflare](https://cloudflare.com/) finds itself at the center of various copyright disputes.

The American company says it powers nearly 20% of the web. This includes several Fortune 500 companies, but also many pirate sites and services.

For years, rightsholders have urged Cloudflare to do something about these pirate sites. However, the company typically doesn’t take action against customers that use its CDN services. Instead, it simply forwarded takedown notices to their respective hosting services.

If customers do use hosting-related Cloudflare services, they will have their content removed. These types of customers have increased significantly over time, and this year, Cloudflare reports a significant spike in takedown activity.

## 3,800% Increase in Takedowns

Cloudflare’s latest [Transparency Report](https://torrentfreak.com/images/BDES-7971_1H_2025_Cloudflare-s_Transparency_Report_Abuse_V3.pdf), published last week, shows that the company received 124,872 hosting-related copyright complaints in the first half of 2025. Of these reports, 54,357 resulted in Cloudflare taking action, presumably by disabling or removing the content in question.

These figures represent a dramatic year-over-year increase, as Cloudflare reported ‘only’ 1,394 copyright-related takedown actions in the six months prior. That’s an impressive 3,800% increase.

If we zoom out further, we see that the hosting-related reports and takedowns have grown steadily over the years.

**Evolution of Cloudflare’s copyright actions**

| Period | Reports Received | Reports Actioned |
| --- | --- | --- |
| 2023 H1 | 376 | 252 |
| 2023 H2 | 1,111 | 1,078 |
| 2024 H1 | 10,892 | 1,046 |
| 2024 H2 | 11,508 | 1,394 |
| 2025 H1 | 124,872 | 54,357 |

Source: Cloudflare Transparency Report Data / TorrentFreak

The most recent spike is not merely the result of increased hosting activity, however. Cloudflare notes that it started to actively engage with rightsholders in the first half of the year to tackle unlicensed sports streaming.

## Rightsholders Get API Access

Justin Paine, Cloudflare’s Vice President of Trust & Safety, [notes](https://blog.cloudflare.com/h1-2025-transparency-report/) that this increase is partly the result of a shift toward more automated processes. Specifically, the company offered rightsholders access to a dedicated API, designed to streamline the submission of copyright complaints.

Through the API, rightsholders were able to automate takedown requests. This resulted in a higher takedown volume and a lower median reaction time, which is key when dealing with time-sensitive content such as live sports streams.

“This engagement resulted in a significant increase in both reports of streaming and corresponding DMCA takedown actions on hosted content, which jumped from 1,394 to 54,357,” Cloudflare’s transparency report reads.

This collaboration and the newly gained insights further boosted the enforcement efforts and resulted in actions against thousands of Cloudflare [R2 storage accounts](https://developers.cloudflare.com/r2/). In the first half of 2025, Cloudflare terminated 21,218 accounts, of which 19,817 were processed automatically.

## Increased Blocking & DNS at Risk

Site blocking also remained a hot topic. In response to various court orders or regulatory authorities, Cloudflare has also [geo-blocked access](https://torrentfreak.com/cloudflare-blocked-400-sports-piracy-domains-in-france-last-year-250303/) to several domains that use its CDN pass-through services. It is clear that the blocking pressure is mounting, with most requests coming from France.

**CDN blocking orders**

![blocked](https://torrentfreak.com/images/blovked-cloudflare.png)

Cloudflare typically does not meddle with its DNS resolver. Instead, it geo-blocks requests for these domains. The transparency report doesn’t mention any data regarding DNS blocking orders and notes that DNS-based blocking will be avoided at all costs.

“Cloudflare has pursued legal remedies before complying with requests to block access to domains or content through the 1.1.1.1 Public DNS Resolver or identified alternate mechanisms to comply with relevant court orders.”

“To date, Cloudflare has not blocked content through the 1.1.1.1 Public DNS Resolver,” the transparency report adds.

## Clunky Blocks & UK Cooperation

In addition to being subject to direct orders, Cloudflare services are also blocked by third parties. For example, ISPs in Spain and Italy were required to block Cloudflare infrastructure to comply with IP-address blocking actions targeted at illegal sports streams.

Commenting on these efforts, Justin Paine specifically calls out the Spanish football league LaLiga for its “clunky” blocking approach and [its “unapologetic” stance](https://torrentfreak.com/laliga-threatens-cloudflare-customer-for-using-an-ip-address-linked-to-piracy-250826/).

“The disproportionate effect of IP address blocking is well known. LaLiga has nonetheless been unapologetic about causing the blocking of countless unrelated websites, suggesting that their commercial interests should trump the rights of Spanish Internet users to access the broader Internet during match times,” Paine notes.

While Cloudflare remains vehemently against aggressive blocking demands, it is slowly but steadily increasing its cooperation with rightsholders. In addition to the earlier mentioned streaming takedown efforts, Cloudflare also started to voluntarily block pirate sites in the UK.

As [previously unveiled here](https://torrentfreak.com/cloudflare-starts-blocking-pirate-sites-for-uk-users-thats-a-pretty-big-deal-250715/), Cloudflare started blocking domain names based on older site-blocking orders where it wasn’t a party. This is similar to the approach Google takes in various countries.

According to Paine, this blocking action in the UK is part of a voluntary agreement with rightsholders, affecting Cloudflare’s pass-through CDN and security services.

“When we take action on domains pursuant to these orders, we post an interstitial page that returns a 451 status code that directs the visitor to the specific order, which includes a process for affected parties to contest the blocking action.”

![Cloudflare 451 2025-07-15](https://torrentfreak.com/images/Cloudflare-...