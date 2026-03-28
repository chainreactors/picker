---
title: BreachForums Data Leaks: Technical Analysis and Timeline Attribution (2022–2026)
url: https://www.d3lab.net/breachforums-data-leaks-technical-analysis-and-timeline-attribution-2022-2026/
source: D3Lab
date: 2026-03-27
fetch_date: 2026-03-28T04:20:13.331371
---

# BreachForums Data Leaks: Technical Analysis and Timeline Attribution (2022–2026)

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

# BreachForums Data Leaks: Technical Analysis and Timeline Attribution (2022–2026)

[Data Leak](https://www.d3lab.net/category/data-leak/)

[![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/03/BreachForums_DataLea_TimeLine.png?resize=1210%2C423&ssl=1)](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/03/BreachForums_DataLea_TimeLine.png?fit=1030%2C687&ssl=1 "BreachForums_DataLea_TimeLine")

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/03/BreachForums_DataLea_TimeLine.png?resize=1030%2C687&ssl=1)

## Introduction

Over the past few years, multiple data leaks attributed to BreachForums have been publicly released, often associated with different domains used by the platform over time (`.vc`, `.co`, `.hn`, `.bf`).

However, many sources tend to conflate these datasets, creating confusion between:

* the publication date of the leak
* the actual time period the data refers to
* the infrastructure (domain) active at the time of data collection

This article provides a technical and evidence-based reconstruction, aimed at Cyber Threat Intelligence and OSINT analysts, clearly distinguishing between leak publication and actual data timelines.

## Methodology

Each dataset was analyzed based on the following elements:

* publication date
* dataset format
* database structure (MyBB-based)
* maximum value of the `lastactive` field in the user table
* availability of file hashes (MD5 / SHA256), when possible

The `lastactive` field was used as a reference point to estimate the most recent activity recorded in the dataset, allowing a reliable temporal attribution.

For ethical and legal reasons, D3Lab does not retain full copies of leaked databases. Hashes are reported only when available at the time of analysis.

## Timeline of analyzed leaks

| Name | Publication Date | Lastactive | Domain | Users/Emails | Type |
| --- | --- | --- | --- | --- | --- |
| Breachforums.vc | 2023-06-19 | 2023-06-17 | breachforums.vc | ~ 4,204 | users |
| Breachforums.co | 2024-07-26 | 2022-11-29 | breachforums.co | ~ 310,187 | full database |
| Breachforums.hn | 2026-01-12 | 2025-08-12 | breachforums.hn | ~ 324,649 | users |
| Breachforums.bf | 2026-03-27 | 2026-02-10 | breachforums.bf | ~ 340,000 | users |

---

## Dataset Analysis

### Breachforums.vc

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/03/Screenshot-2023-06-19-alle-15.02.45.png?resize=1030%2C495&ssl=1)

This dataset was released on June 19, 2023 via the forum “cronos.li”, as a SQL file named `ht0k4qYO.sql`. The structure is consistent with the `mybb_users` table used by MyBB.

Available hashes:

* MD5: 416896dcc1d9a8975702d897535dd8c2
* SHA256: 6d6b506693dbc7a19d65771f9869361fd8b639e40012049411c43c418df73d45

The most recent `lastactive` value corresponds to June 17, 2023 (UTC), approximately two days before publication.

This indicates that the dataset represents a near real-time snapshot of the infrastructure active on `breachforums.vc`.

---

### Breachforums.co

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/03/Screenshot-2024-07-26-alle-09.34.59.png?resize=492%2C312&ssl=1)

In July 2024, a dataset was distributed via the Telegram channel “explain” (now offline) under the name `breached_full.7z` or `s7rDZZSp.rar`, containing 89 NDJSON files.

Unlike the other leaks, this dataset represents a full database dump and includes multiple tables, such as user accounts, threads, private messages, IP logs, and payment-related data.

The analysis of the `lastactive` field shows that the data is consistent up to November 29, 2022, matching the claim made in the original leak.

This confirms that the dataset represents a historical database (v1), corresponding to the period when the forum was operating under `breachforums.co`, later redistributed in 2024.

---

### Breachforums.hn

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/03/Screenshot-2026-01-12-alle-16.31.21.png?resize=1030%2C708&ssl=1)
![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/03/Screenshot-2026-01-12-alle-16.32.58.png?resize=1030%2C309&ssl=1)

The dataset associated with `breachforums.hn` was released on January 12, 2026 through a dedicated website (`shinyhunte[.]rs`) linked to [ShinyHunters](https://en.wikipedia.org/wiki/ShinyHunters).

The file `databoose.sql` contains a dump of the MyBB user table.

Available hashes:

* MD5: f280d678e83099db8c3539764d212ccf
* SHA256: 790f3595850e4d8c212a35a40eb69fe0431fda6abcfbbf4592126bf636df2088

The most recent `lastactive` value corresponds to August 12, 2025, which aligns with the period during which the forum was still accessible via `breachforums.hn`.

This timeline is further supported by OSINT sources, including the deepdarkCTI [commit](https://github.com/fastfire/deepdarkCTI/commit/7fe82c1a908416fc904193df6eecf4b7552c6ba5), documenting the shutdown of the domain in the same timeframe.

This dataset represents a snapshot of the platform shortly before its closure.

---

### Breachforums.bf

![](https://i0.wp.com/www.d3lab.net/wp-content/uploads/2026/03/Screenshot-2026-03-27-alle-09.35.39.png?resize=977%2C627&ssl=1)

The most recent dataset was released on March 27, 2026 via an ONION service, again attributed to [ShinyHunters](https://en.wikipedia.org/wiki/ShinyHunters).

The file `bf_03_2026.sql` contains a dump of the user table, with a randomized prefix (`hcclmafd2jnkwmfufmybb_users`), suggesting a non-standard configuration.

Available hashes:

* MD5: 36117bdf2096b3233d78d889c44bcc59
* SHA256: 5496517861f3d3b16759ff63d6c3a54250f0aa42ce7a0b989d2c4e223424fc62

The most recent `lastactive` value corresponds to February 10, 2026.

Additionally, internal references to subdomains such as `cdn.breachforums.bf` and `escrow.breachforums.bf` further confirm attribution to the infrastructure active at that time.

This dataset represents a recent snapshot of the `.bf` phase of the forum.

---

## Correlation with Have I Been Pwned

To further validate the datasets, a correlation was established with classifications provided by [Have I Been Pwned.](https://haveibeenpwned.com/)

| Domain | HIBP Name |
| --- | --- |
| breachforums.bf | [BreachForums Version 5](https://haveibeenpwned.com/Breach/BreachForumsV5) |
| breachforums.hn | [BreachForums (2025)](https://haveibeenpwned.com/Breach/BreachForums2025) |
| breachforums.co | BreachForums |
| breachforums.vc | [BreachForums Clone](https://haveibeenpwned.com/Breach/BreachForumsClone) |

This mapping highlights how HIBP naming follows a versioning or temporal logic, while this analysis is based on infrastructure and forensic data attribution.

---

## Conclusions and Considerations

This demonstrates that the domain associated with a leak does not necessarily indicate the timing of the compromise, but rather the context in which the data was originally collected.

Distinguishing between publication date and actual data timeline is critical to avoid misattribution.

The combined use of technical indicators such as the `lastactive` field, structural database analysis, and OSINT correlation enables a more accurate reconstruction of the BreachForums infrastructure lifecycle.

Th...