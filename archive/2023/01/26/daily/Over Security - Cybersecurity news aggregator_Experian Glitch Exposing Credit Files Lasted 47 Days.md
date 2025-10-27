---
title: Experian Glitch Exposing Credit Files Lasted 47 Days
url: https://krebsonsecurity.com/2023/01/experian-glitch-exposing-credit-files-lasted-47-days/
source: Over Security - Cybersecurity news aggregator
date: 2023-01-26
fetch_date: 2025-10-04T04:53:40.331035
---

# Experian Glitch Exposing Credit Files Lasted 47 Days

Advertisement

[![](/b-gartner/3.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# Experian Glitch Exposing Credit Files Lasted 47 Days

January 25, 2023

[40 Comments](https://krebsonsecurity.com/2023/01/experian-glitch-exposing-credit-files-lasted-47-days/#comments)

On Dec. 23, 2022, KrebsOnSecurity [alerted](https://krebsonsecurity.com/2023/01/identity-thieves-bypassed-experian-security-to-view-credit-reports/) big-three consumer credit reporting bureau **Experian** that identity thieves had worked out how to bypass its security and access any consumer’s full credit report — armed with nothing more than a person’s name, address, date of birth, and Social Security number. Experian fixed the glitch, but remained silent about the incident for a month. This week, however, Experian acknowledged that the security failure persisted for nearly seven weeks, between Nov. 9, 2022 and Dec. 26, 2022.

![](https://krebsonsecurity.com/wp-content/uploads/2023/01/experianresponse.png)

The tip about the Experian weakness came from **Jenya Kushnir**, a security researcher living in Ukraine who said he discovered the method being used by identity thieves after spending time on **Telegram** chat channels dedicated to cybercrime.

Normally, Experian’s website will ask a series of multiple-choice questions about one’s financial history, as a way of validating the identity of the person requesting the credit report. But Kushnir said the crooks learned they could bypass those questions and trick Experian into giving them access to anyone’s credit report, just by editing the address displayed in the browser URL bar at a specific point in Experian’s identity verification process.

When I tested Kushnir’s instructions on my own identity at Experian, I found I was able to see my report even though Experian’s website told me it didn’t have enough information to validate my identity. A security researcher friend who tested it at Experian found she also could bypass Experian’s four or five multiple-choice security questions and go straight to her full credit report at Experian.

Experian [acknowledged receipt of my Dec. 23 report](https://krebsonsecurity.com/2023/01/identity-thieves-bypassed-experian-security-to-view-credit-reports/) four days later on Dec. 27, a day after Kushnir’s method stopped working on Experian’s website (the exploit worked as long as you came to Experian’s website via [annualcreditreport.com](https://www.annualcreditreport.com) — the site mandated to provide a free copy of your credit report from each of the major bureaus once a year).

Experian never did respond to official requests for comment on that story. But earlier this week, I received an otherwise unhelpful letter via snail mail from Experian (see image above), which stated that the weakness we reported persisted between Nov. 9, 2022 and Dec. 26, 2022.

“During this time period, we experienced an isolated technical issue where a security feature may not have functioned,” Experian explained.

It’s not entirely clear whether Experian sent me this paper notice because they legally had to, or if they felt I deserved a response in writing and thought maybe they’d kill two birds with one stone. But it’s pretty crazy that it took them a full month to notify me about the potential impact of a security failure that *I* notified *them* about.

It’s also a little nuts that Experian didn’t simply include a copy of my current credit report along with this letter, which is confusingly worded and reads like they suspect someone other than me may have been granted access to my credit report without any kind of screening or authorization.

After all, if I hadn’t authorized the request for my credit file that apparently prompted this letter (I had), that would mean the thieves already had my report. Shouldn’t I be granted the same visibility into my own credit file as them?

Instead, their woefully inadequate letter once again puts the onus on me to wait endlessly on hold for an Experian representative over the phone, or sign up for a free year’s worth of Experian monitoring my credit report.

As it stands, using Kushnir’s exploit was the only time I’ve ever been able to get Experian’s website to cough up a copy of my credit report. To make matters worse, a majority of the information in that credit report is not mine. So I’ve got that to look forward to.

If there is a silver lining here, I suppose that if I were Experian, I probably wouldn’t want to show Brian Krebs his credit file either. Because it’s clear this company has no idea who I really am. And in a weird, kind of sad way I guess, that makes me happy.

For thoughts on what you can do to minimize your victimization by and overall worth to the credit bureaus, see [this section of the most recent Experian story](https://krebsonsecurity.com/2023/01/identity-thieves-bypassed-experian-security-to-view-credit-reports/#:~:text=WHAT%20CAN%20YOU%20DO).

*This entry was posted on Wednesday 25th of January 2023 02:58 PM*

[A Little Sunshine](https://krebsonsecurity.com/category/sunshine/) [Data Breaches](https://krebsonsecurity.com/category/data-breaches/) [Web Fraud 2.0](https://krebsonsecurity.com/category/web-fraud-2-0/)

[Experian](https://krebsonsecurity.com/tag/experian/) [Experian breach](https://krebsonsecurity.com/tag/experian-breach/)

Post navigation

[← Administrator of RSOCKS Proxy Botnet Pleads Guilty](https://krebsonsecurity.com/2023/01/administrator-of-rsocks-proxy-botnet-pleads-guilty/)
[Finland’s Most-Wanted Hacker Nabbed in France →](https://krebsonsecurity.com/2023/02/finlands-most-wanted-hacker-nabbed-in-france/)

## 40 thoughts on “Experian Glitch Exposing Credit Files Lasted 47 Days”

1. Jay [January 25, 2023](https://krebsonsecurity.com/2023/01/experian-glitch-exposing-credit-files-lasted-47-days/#comment-575873)

   Such blatant incompetence. It’s painfully obvious that we consumers are absolutely unprotected and abused by for profit companies like Experian, who get the green light to operate as it pleases because there’s no government oversight and no judicial consequence strong enough to terminate their irresponsible enterprise.
2. Stratocaster [January 25, 2023](https://krebsonsecurity.com/2023/01/experian-glitch-exposing-credit-files-lasted-47-days/#comment-575875)

   So this is the company which was providing “remediation services” to victims of the Equifax breach? Time for federal regulatory intervention for all credit bureaus.
3. Tom Christopher [January 25, 2023](https://krebsonsecurity.com/2023/01/experian-glitch-exposing-credit-files-lasted-47-days/#comment-575876)

   Why or why would we entrust our extremely important information to these for profit companies. This needs to be a government function, in its own dept., probably Home Land Security.

   1. Larry Wannabetech [January 25, 2023](https://krebsonsecurity.com/2023/01/experian-glitch-exposing-credit-files-lasted-47-days/#comment-575886)

      Oh sure I trust the government. And we don’t entrust our extremely important information to these companies. They just take it! Remember we are the product, NOT the customer.
   2. [The Doctor](https://drwho.virtadpt.net/) [January 27, 2023](https://krebsonsecurity.com/2023/01/experian-glitch-exposing-credit-files-lasted-47-days/#comment-576019)

      If there were ...