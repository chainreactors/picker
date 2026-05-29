---
title: B1ack’s Stash Releases 4.6 Million Payment Cards: Web Skimming Leak Analysis
url: https://www.d3lab.net/b1acks-stash-releases-4-6-million-payment-cards-web-skimming-leak-analysis/
source: D3Lab
date: 2026-05-28
fetch_date: 2026-05-29T06:06:20.669616
---

# B1ack’s Stash Releases 4.6 Million Payment Cards: Web Skimming Leak Analysis

[![D3Lab](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2019/04/D3Lab_Logo_Enfold-300x102.png?fit=300%2C102&ssl=1 "D3Lab_Logo_Enfold-300×102")](https://www.d3lab.net/ "D3Lab_Logo_Enfold-300×102")

* [Home](https://www.d3lab.net/)
* [Services](/#services)
* [Philosophy](/#philosophy)
* [Contact](/#contact)
* [Blog](https://www.d3lab.net/blog/)
* [Fare clic per aprire il campo di ricerca
  Fare clic per aprire il campo di ricerca

  Cerca](?s= "Fare clic per aprire il campo di ricerca")
* **Menu**
  Menu

* [Collegamento a X](https://twitter.com/D3LabIT "Collegamento a X")
* [Collegamento a LinkedIn](https://www.linkedin.com/company/d3labsrl/ "Collegamento a LinkedIn")
* [Collegamento a Rss questo sito](https://www.d3lab.net/feed/ "Collegamento a Rss  questo sito")
* [Collegamento a Mail](/#contact "Collegamento a Mail")

# B1ack’s Stash Releases 4.6 Million Payment Cards: Web Skimming Leak Analysis

[Data Leak](https://www.d3lab.net/category/data-leak/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/05/b1ack_forum-scaled.png?resize=1210%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/05/b1ack_forum-scaled.png?fit=1030%2C454&ssl=1 "b1ack_forum")

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/05/b1ack_forum.png?resize=1030%2C454&ssl=1)

On May 18, 2026, the criminal marketplace **B1ack’s Stash** published a new archive containing millions of compromised payment cards on a well-known underground forum. The release had an explicitly promotional purpose: driving traffic to the illegal market, reinforcing its reputation within the carding ecosystem, and, according to the threat actor’s own narrative, punishing sellers accused of reselling the same cards elsewhere.

In the announcement, the threat actor claimed to have “suspended” almost 8 million CVV2 cards and made them available for free in the marketplace’s freebies section. The download link, distributed through Exploit.in’s Send platform, was limited to **1,000 downloads or 30 days**.

## A Criminal Marketing Operation

The free publication of large volumes of payment card data is not unusual in carding-focused marketplaces. The model is straightforward: release part of the inventory for free to generate attention, attract new registrations, demonstrate the alleged quality of the data, and push criminals toward purchasing newer or more targeted batches.

We had [already observed](https://www.d3lab.net/b1acks-stash-releases-1-million-credit-cards-on-a-deep-web-forum/) a similar dynamic in February 2025, when B1ack’s Stash published a previous dataset presented as a mass free release. At the time, the analysis identified **1,018,014 unique cards**, including **192,174 issued by European financial institutions**. The May 2026 release therefore confirms a strategy already adopted by the marketplace: using public leaks as an advertising tool and as a positioning mechanism within the underground market.

## Dataset Composition

The analyzed file contains **4,668,889 records**. Each row follows a consistent 14-field structure separated by the pipe character (`|`):

```
PAN|expiration_month|expiration_year|CVV|name|address|city|state/province|postal_code|country|email|phone|IP|final_field
```

For ethical and security reasons, we do not publish any PAN, CVV, address, email, phone number, or personal data that could identify individuals.

The combined presence of PAN, expiration date, CVV2, personal details, billing address, email, phone number, and IP address is consistent with data collected through **web skimmers** or similar compromises of online payment flows. In e-skimming scenarios, malicious JavaScript code is injected into compromised checkout pages and intercepts the data entered by the user during the transaction.

The format observed in 2026 is partially different from the one analyzed in 2025: the previous release also included information such as date of birth and User-Agent, while the new dataset appears more standardized and focused on the resale of CVV2 cards.

## Data Quality and Uniqueness

The analysis identified an extremely low number of duplicates:

| Metric | Value |
| --- | --- |
| Total records | 4,668,889 |
| Unique PANs | 4,668,887 |
| Duplicate PAN values | 1 |
| Duplicate records beyond the first occurrence | 2 |

From a formal card validation perspective, considering numeric PAN, compatible length, Luhn algorithm, expiration date, and CVV length, **4,659,138 records** are formally valid, equal to **99.7911%** of the dataset.

This does not mean that all cards are actually usable or still active. Formal validation only measures the syntactic and mathematical consistency of the data. Establishing whether a card is actually associated with an issuing institution, still active, or already known from previous compromises requires external enrichment, such as BIN/IIN validation and correlation with previous leaks.

A more restrictive metric, considering both a formally valid card and a complete record, results in **1,619,092 records**, equal to **34.6783%** of the dataset.

The main anomalies or incomplete fields identified are:

| Check | Non-compliant records | Percentage |
| --- | --- | --- |
| Missing or invalid IP | 2,672,733 | 57.2456% |
| Missing or invalid email | 770,494 | 16.5027% |
| Missing phone number | 641,190 | 13.7332% |
| Missing postal code | 430,160 | 9.2133% |
| Missing state/province | 416,610 | 8.9231% |
| Missing address | 368,259 | 7.8875% |
| Missing city | 262,607 | 5.6246% |
| Missing name | 87,466 | 1.8734% |
| Invalid expiration date or expired card | 9,314 | 0.1995% |
| PAN failing Luhn validation | 339 | 0.0073% |
| Inconsistent CVV | 154 | 0.0033% |

## Payment Networks Involved

The payment network distribution, estimated from the PAN, shows a clear prevalence of Visa and Mastercard:

| Payment network | Records | Percentage |
| --- | --- | --- |
| Visa | 2,885,775 | 61.8086% |
| Mastercard | 1,498,617 | 32.0979% |
| American Express | 152,075 | 3.2572% |
| Discover | 124,533 | 2.6673% |
| Other/Undetermined | 7,889 | 0.1690% |

These figures are consistent with a dataset collected at global scale, with strong exposure of the payment networks most commonly used in online transactions.

## Countries Involved

The `country` field in the dataset indicates the country associated with each record, most likely the billing or residence country provided during checkout. It should not automatically be interpreted as the country of the card issuer.

The main countries present in the dataset are:

| Country | Records | Percentage |
| --- | --- | --- |
| United States | 3,242,564 | 69.4504% |
| Canada | 172,392 | 3.6924% |
| United Kingdom | 168,910 | 3.6178% |
| France | 131,260 | 2.8114% |
| Malaysia | 126,449 | 2.7083% |
| Australia | 50,466 | 1.0809% |
| Ireland | 50,166 | 1.0745% |
| Italy | 47,694 | 1.0215% |
| Spain | 45,208 | 0.9683% |
| Hong Kong | 39,902 | 0.8546% |
| Thailand | 36,609 | 0.7841% |
| Germany | 35,841 | 0.7677% |
| Switzerland | 35,607 | 0.7626% |
| Singapore | 35,419 | 0.7586% |
| India | 34,639 | 0.7419% |

The strong prevalence of the United States, accounting for approximately 69.45% of the dataset, combined with the presence of European countries and Asian financial hubs, suggests a collection that is not limited to a single local campaign but is compatible with multiple compromises of e-commerce websites or online payment flows.

## Italy Focus

The dataset contains **47,694 records** with the country set to `ITALY`, equal to **1.0215%** of the full archive.

This subset was further enriched through BIN/IIN validation and correlation with previously known leaks. Based on this analysis, **18,026 Italian cards are valid and newly observed**, meaning they are associated with a real issuing institution and had not previously been detected in other analyzed data leaks.

This equals **37.7951%** of the Italian subset and **0.3861%** of the full dataset.

## Why the Dataset Is Consist...