---
title: A Close Up Look at the Consumer Data Broker Radaris
url: https://krebsonsecurity.com/2024/03/a-close-up-look-at-the-consumer-data-broker-radaris/
source: Krebs on Security
date: 2024-03-09
fetch_date: 2025-10-04T12:13:15.788629
---

# A Close Up Look at the Consumer Data Broker Radaris

Advertisement

[![](/b-gartner/7.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

Advertisement

[![](/b-gartner/4.jpg)](https://www.gartner.com/en/conferences/na/identity-access-management-us?utm_source=krebs&utm_medium=banner&utm_campaign=EVT_NA_2025_IAM20_PP_MP6_KREBSONSECURITY)

[![Krebs on Security](https://krebsonsecurity.com/wp-content/uploads/2021/03/kos-27-03-2021.jpg)](https://krebsonsecurity.com/ "Krebs on Security")

[Skip to content](#content "Skip to content")

* [Home](https://krebsonsecurity.com/)
* [About the Author](https://krebsonsecurity.com/about/)
* [Advertising/Speaking](https://krebsonsecurity.com/cpm/)

# A Close Up Look at the Consumer Data Broker Radaris

March 8, 2024

[34 Comments](https://krebsonsecurity.com/2024/03/a-close-up-look-at-the-consumer-data-broker-radaris/#comments)

If you live in the United States, the data broker **Radaris** likely knows a great deal about you, and they are happy to sell what they know to anyone. But how much do we know about Radaris? Publicly available data indicates that in addition to running a dizzying array of people-search websites, the co-founders of Radaris operate multiple Russian-language dating services and affiliate programs. It also appears many of their businesses have ties to a California marketing firm that works with a Russian state-run media conglomerate currently sanctioned by the U.S. government.

Formed in 2009, Radaris is a vast people-search network for finding data on individuals, properties, phone numbers, businesses and addresses. Search for any American’s name in Google and the chances are excellent that a listing for them at Radaris.com will show up prominently in the results.

![](https://krebsonsecurity.com/wp-content/uploads/2024/03/radarisbtk.png)

Radaris reports typically bundle a substantial amount of data scraped from public and court documents, including any current or previous addresses and phone numbers, known email addresses and registered domain names. The reports also list address and phone records for the target’s known relatives and associates. Such information could be useful if you were trying to determine the maiden name of someone’s mother, or successfully answer a range of other [knowledge-based authentication questions](https://krebsonsecurity.com/tag/knowledge-based-authentication/).

Currently, consumer reports advertised for sale at Radaris.com are being fulfilled by a different people-search company called **TruthFinder**. But Radaris also operates a number of other people-search properties — like **Centeda.com** — that sell consumer reports directly and behave almost identically to TruthFinder: That is, reel the visitor in with promises of detailed background reports on people, and then charge a $34.99 monthly subscription fee just to view the results.

The **Better Business Bureau** (BBB) assigns Radaris a rating of “F” for consistently ignoring consumers seeking to have their information removed from Radaris’ various online properties. Of the 159 complaints detailed there in the last year, several were from people who had used third-party identity protection services to have their information removed from Radaris, only to receive a notice a few months later that their Radaris record had been restored.

What’s more, Radaris’ automated process for requesting the removal of your information requires signing up for an account, potentially providing more information about yourself that the company didn’t already have (see screenshot above).

Radaris has not responded to requests for comment.

Radaris, TruthFinder and others like them all force users to agree that their reports will not be used to evaluate someone’s eligibility for credit, or a new apartment or job. This language is so prominent in people-search reports because selling reports for those purposes would classify these firms as consumer reporting agencies (CRAs) and expose them to regulations under the [Fair Credit Reporting Act](https://www.ftc.gov/legal-library/browse/statutes/fair-credit-reporting-act) (FCRA).

These data brokers do not want to be treated as CRAs, and for this reason their people search reports typically do not include detailed credit histories, financial information, or full Social Security Numbers (Radaris reports include the first six digits of one’s SSN).

But in September 2023, the **U.S. Federal Trade Commission** [found](https://www.ftc.gov/news-events/news/press-releases/2023/09/ftc-says-truthfinder-instant-checkmate-deceived-users-about-background-report-accuracy-violated-fcra) that TruthFinder and another people-search service Instant Checkmate were trying to have it both ways. The FTC levied a $5.8 million penalty against the companies for allegedly acting as CRAs because they assembled and compiled information on consumers into background reports that were marketed and sold for employment and tenant screening purposes.

![](https://krebsonsecurity.com/wp-content/uploads/2024/03/ftc-tfad.png)

The FTC also found TruthFinder and Instant Checkmate deceived users about background report accuracy. The FTC alleges these companies made millions from their monthly subscriptions using push notifications and marketing emails that claimed that the subject of a background report had a criminal or arrest record, when the record was merely a traffic ticket.

“All the while, the companies touted the accuracy of their reports in online ads and other promotional materials, claiming that their reports contain “the MOST ACCURATE information available to the public,” the FTC noted. The FTC says, however, that all the information used in their background reports is obtained from third parties that expressly disclaim that the information is accurate, and that TruthFinder and Instant Checkmate take no steps to verify the accuracy of the information.

The FTC said both companies deceived customers by providing “Remove” and “Flag as Inaccurate” buttons that did not work as advertised. Rather, the “Remove” button removed the disputed information only from the report as displayed to that customer; however, the same item of information remained visible to other customers who searched for the same person.

The FTC also said that when a customer flagged an item in the background report as inaccurate, the companies never took any steps to investigate those claims, to modify the reports, or to flag to other customers that the information had been disputed.

## WHO IS RADARIS?

According to [Radaris’ profile](https://pitchbook.com/profiles/company/62546-05#funding) at the investor website **Pitchbook.com**, the company’s founder and “co-chief executive officer” is a Massachusetts resident named **Gary Norden,** also known as **Gary Nard.**

An analysis of email addresses known to have been used by Mr. Norden shows his real name is **Igor****Lybarsky** (also spelled Lubarsky). Igor’s brother **Dmitry**, who goes by “Dan,” appears to be the other co-CEO of Radaris. Dmitry Lybarsky’s Facebook/Meta account says he was born in March 1963.

![](https://krebsonsecurity.com/wp-content/uploads/2024/03/lybarskybros.png)

Indirectly or directly, the Lybarskys [own multiple properties in both Sherborn and Wellesley, Mass](https://medium.com/%40deckerthinktank/41-n-main-sherborn-saga-continues-dc23e4d1bebc). However, the Radaris website is operated by an offshore entity called **Bitseller Expert Ltd**, which is incorporated in Cyprus. Neither Lybarsky brother responded to requests for comment.

A review of the domain names registered by Gary Norden shows that beginning in the early 2000s, he and Dan built an e-commerce empire by marketing prepaid calling cards and VOIP services to Russian expatriates who are living in the United States and seeking an affordable way to stay in touch with loved ones back home.

[![](https://krebsonsecurity.com/wp-content/uploads/2024/03/l...