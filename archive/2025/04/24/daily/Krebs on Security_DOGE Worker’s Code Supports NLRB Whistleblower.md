---
title: DOGE Worker’s Code Supports NLRB Whistleblower
url: https://krebsonsecurity.com/2025/04/doge-workers-code-supports-nlrb-whistleblower/
source: Krebs on Security
date: 2025-04-24
fetch_date: 2025-10-06T22:12:26.086761
---

# DOGE Worker’s Code Supports NLRB Whistleblower

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-sysdig/2.png)](https://content.foleon.com/sysdig/sysdig-cloud-defense-report-2025/?utm_source=krebs-on-security&utm_medium=display&utm_campaign=aware_amer_the-right-way_na_ung_display&utm_content=AD000462_1240x160)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# DOGE Worker’s Code Supports NLRB Whistleblower

April 23, 2025

[59 Comments](https://krebsonsecurity.com/2025/04/doge-workers-code-supports-nlrb-whistleblower/#comments)

A whistleblower at the **National Labor Relations Board** (NLRB) alleged last week that denizens of Elon Musk’s **Department of Government Efficiency** (DOGE) siphoned gigabytes of data from the agency’s sensitive case files in early March. The whistleblower said accounts created for DOGE at the NLRB downloaded three code repositories from **GitHub**. Further investigation into one of those code bundles shows it is remarkably similar to a program published in January 2025 by **Marko Elez**, a 25-year-old DOGE employee who has worked at a number of Musk’s companies.

[![](https://krebsonsecurity.com/wp-content/uploads/2025/04/db-powershellcmds.png)](https://krebsonsecurity.com/wp-content/uploads/2025/04/db-powershellcmds.png)

A screenshot shared by NLRB whistleblower Daniel Berulis shows three downloads from GitHub.

According to [a whistleblower complaint](https://krebsonsecurity.com/2025/04/whistleblower-doge-siphoned-nlrb-case-data/) filed last week by **Daniel J. Berulis**, a 38-year-old security architect at the NLRB, officials from DOGE met with NLRB leaders on March 3 and demanded the creation of several all-powerful “tenant admin” accounts that were to be exempted from network logging activity that would otherwise keep a detailed record of all actions taken by those accounts.

Berulis said the new DOGE accounts had unrestricted permission to read, copy, and alter information contained in NLRB databases. The new accounts also could restrict log visibility, delay retention, route logs elsewhere, or even remove them entirely — top-tier user privileges that neither Berulis nor his boss possessed.

Berulis said he discovered one of the DOGE accounts had downloaded three external code libraries from **GitHub** that neither NLRB nor its contractors ever used. A “readme” file in one of the code bundles explained it was created to rotate connections through a large pool of cloud Internet addresses that serve “*as a proxy to generate pseudo-infinite IPs for web scraping and brute forcing*.” Brute force attacks involve automated login attempts that try many credential combinations in rapid sequence.

A search on that description in Google brings up a code repository at GitHub for a user with the account name “**Ge0rg3**” who published a program roughly four years ago called “[requests-ip-rotator](https://github.com/Ge0rg3/requests-ip-rotator),” described as a library that will allow the user “to bypass IP-based rate-limits for sites and services.”

![](https://krebsonsecurity.com/wp-content/uploads/2025/04/ge0rge-gh.png)

“A Python library to utilize AWS API Gateway’s large IP pool as a proxy to generate pseudo-infinite IPs for web scraping and brute forcing,” the description reads.

Ge0rg3’s code is “open source,” in that anyone can copy it and reuse it non-commercially. As it happens, there is a newer version of this project that was derived or “forked” from Ge0rg3’s code — called “[async-ip-rotator](https://github.com/markoelez/async-ip-rotator/blob/master/README.md)” — and it was committed to GitHub in January 2025 by DOGE captain [Marko Elez](https://github.com/markoelez).

[![](https://krebsonsecurity.com/wp-content/uploads/2025/04/melez-gh.png)](https://krebsonsecurity.com/wp-content/uploads/2025/04/melez-gh.png)

The whistleblower stated that one of the GitHub files downloaded by the DOGE employees who transferred sensitive files from an NLRB case database was an archive whose README file read: “Python library to utilize AWS API Gateway’s large IP pool as a proxy to generate pseudo-infinite IPs for web scraping and brute forcing.” Elez’s code pictured here was forked in January 2025 from a code library that shares the same description.

A key DOGE staff member who gained access to the Treasury Department’s central payments system, Elez has worked for a number of Musk companies, including **X**, **SpaceX**, and **xAI**. Elez was among the first DOGE employees to face public scrutiny, after **The Wall Street Journal** [linked him to social media posts](https://www.wsj.com/tech/doge-staffer-resigns-over-racist-posts-d9f11a93) that advocated racism and eugenics.

Elez resigned after that brief scandal, but was rehired after President Donald Trump and Vice President JD Vance expressed support for him. **Politico** [reports](https://www.politico.com/news/2025/03/29/doge-marco-elez-software-engineer-us-payroll-00259303) Elez is now a **Labor Department** aide detailed to multiple agencies, including the **Department of Health and Human Services**.

“During Elez’s initial stint at Treasury, he violated the agency’s information security policies by sending a spreadsheet containing names and payments information to officials at the General Services Administration,” Politico wrote, citing court filings.

KrebsOnSecurity sought comment from both the NLRB and DOGE, and will update this story if either responds.

The NLRB has been effectively hobbled since **President Trump** fired three board members, leaving the agency without the quorum it needs to function. Both **Amazon** and Musk’s **SpaceX** have [been suing](https://apnews.com/article/amazon-nlrb-unconstitutional-spacex-elon-musk-ab42977117d883e97110a7bf8e8b257f) the NLRB over complaints the agency filed in disputes about workers’ rights and union organizing, arguing that the NLRB’s very existence is unconstitutional. On March 5, a U.S. appeals court [unanimously rejected](https://www.reuters.com/legal/government/musks-spacex-loses-early-legal-challenge-us-labor-boards-powers-2025-03-05/) Musk’s claim that the NLRB’s structure somehow violates the Constitution.

Berulis’s complaint alleges the DOGE accounts at NLRB downloaded more than 10 gigabytes of data from the agency’s case files, a database that includes reams of sensitive records including information about employees who want to form unions and proprietary business documents. Berulis said he went public after higher-ups at the agency told him not to report the matter to the US-CERT, as they’d previously agreed.

Berulis told KrebsOnSecurity he worried the unauthorized data transfer by DOGE could unfairly advantage defendants in a number of ongoing labor disputes before the agency.

“If any company got the case data that would be an unfair advantage,” Berulis said. “They could identify and fire employees and union organizers without saying why.”

![](https://krebsonsecurity.com/wp-content/uploads/2025/04/markoelez.png)

Marko Elez, in a photo from a social media profile.

Berulis said the other two GitHub archives that DOGE employees downloaded to NLRB systems included **Integuru**, a software framework designed to reverse engineer application programming interfaces (APIs) that websites use to fetch data; and a “headless” browser called **Browserless**, which is made for automating web-based tasks that require a pool of browsers, such as web scraping and automated testing.

On February 6, someone [posted a lengthy and detailed critique](https://web.archive.org/web/20250423135719/https%3A//github...