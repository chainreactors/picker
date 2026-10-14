---
title: Releasing the Cobalt Strike Beacon Corpus
url: https://blog.fox-it.com/2026/10/13/releasing-the-cobalt-strike-beacon-corpus/
source: Fox-IT International blog
date: 2026-10-13
fetch_date: 2026-10-14T06:51:57.493132
---

# Releasing the Cobalt Strike Beacon Corpus

[Skip to content](#content)

[![Fox-IT International blog](https://blog.fox-it.com/wp-content/uploads/2019/02/fox-it-logo.png)](https://blog.fox-it.com/)

[Fox-IT International blog](https://blog.fox-it.com/)

News and opinions from Fox-IT

Menu

* [Home](https://blog.fox-it.com/)
* [Archive](https://blog.fox-it.com/archive/)
* [Back to Fox-IT](http://www.fox-it.com)

# Releasing the Cobalt Strike Beacon Corpus

[Fox-SRT](https://blog.fox-it.com/author/foxsrt/)

[Blog](https://blog.fox-it.com/category/blog/), [Cobalt Strike](https://blog.fox-it.com/category/cobalt-strike/), [Threat Intelligence](https://blog.fox-it.com/category/threat-intelligence/)

October 13, 2026
7 Minutes

**Authors:** Yun Zheng Hu

# Introduction

Today Fox-IT is publicly releasing its full Cobalt Strike Beacon Corpus, containing 56,843 raw beacons and their parsed configurations, from 190,182 sightings collected from 30,604 unique IP addresses running a Team Server (the Cobalt Strike command-and-control server that beacons connect back to) between 4 July 2018 and 29 September 2026, over eight years of beacon data. The corpus is available on Hugging Face: <https://huggingface.co/datasets/fox-srt/cobaltstrike-beacon-corpus>

Back in March 2022 we published [Mining Data from Cobalt Strike Beacons](https://web.archive.org/web/20220328134535/https%3A//research.nccgroup.com/2022/03/25/mining-data-from-cobalt-strike-beacons/). That post covered 128,340 beacon sightings collected from July 2018 to February 2022, and it introduced our Python project [dissect.cobaltstrike](https://github.com/fox-it/dissect.cobaltstrike) for parsing them.

Since then, public scanning for Team Servers has become routine, and Cobalt Strike has shipped versions 4.6 through 4.13. Researchers have regularly asked us for an updated dataset. And here it is, a large, consistent, long-running dataset for the infosec community to build on. The corpus includes the raw beacon payloads, not just our parsed output, so anyone can reproduce our results or improve on them.

We also see publishing this corpus as an act of preservation. C2 infrastructure is short-lived, as the median Team Server is reachable for just 14 days, and the beacons it serves vanish with it. Eight years of collection captures things that can no longer be observed today, like the waves of cracked 4.0 builds or the adoption of leaked versions. By publishing the raw beacons alongside the parsed data, we keep that record available for anyone to study, long after the servers themselves are gone.

# What’s in the corpus

The corpus is published on Hugging Face as two Parquet files:

| File | Size | Rows | Contents |
| --- | --- | --- | --- |
| beacons.parquet | 52 MB | 190,182 | Every sighting of a beacon, with collection metadata, network context and the parsed beacon configuration. |
| payloads.parquet | 9.7 GB | 56,843 | The raw beacon payloads, wrapped in [CaRT](https://github.com/CybercentreCanada/cart) as an extra safety layer so the samples are neutered until you deliberately unpack them. |

All beacons were downloaded directly from internet-facing Team Servers, mostly on TCP ports 80 and 443 (HTTP and HTTPS) and UDP port 53 (DNS), with a small number on other ports. We deliberately didn’t include samples from other sources such as VirusTotal, so the corpus reflects the Cobalt Strike landscape as it was visible on the internet.

# How we collected it

The collection method matches our 2022 post. We fingerprint likely Team Servers on the internet, then request a beacon payload from each one using a URI that passes Cobalt Strike’s checksum8 check. Every beacon that comes back is parsed with `dissect.cobaltstrike`, which decodes the configuration block. The result is stored as a sighting.

* **Discovery**: candidate hosts from our own internet-wide scanning. As in 2022, we’re keeping our fingerprints private so they stay effective; writing your own is left as an exercise for the reader.
* **Download**: x86 beacons over HTTP(S) and DNS.
* **DNS**: for DNS listeners we’re not publishing that fingerprint either, but it’s not rocket science. The beacon is [fetched](https://raw.githubusercontent.com/fox-it/dissect.cobaltstrike/refs/heads/main/scripts/pull_dns_beacon.py) as a series of TXT record lookups sent over UDP port 53 directly to the Team Server’s DNS listener.
* **Parse**: Use `dissect.cobaltstrike` to parse the beacon and export the configuration
* **Enrich**: TLS certificate data captured at collection time (where available) and GeoIP/ASN via [historical GeoIP databases](https://github.com/ooni/historical-geoip).

Note that there might be some small gaps in the collection due to automation issues that we did not catch in time.

# Getting started

Most research only needs the **beacons.parquet** dataset. The **payloads.parquet** dataset containing raw beacon payloads is only required if you want to re-parse the beacons or look into the ones that failed parsing.

I’m a big fan of DuckDB (and SQLite), and over time I’ve become fond of SQL for querying data as well. DuckDB is very fast, and AI assistants are very good at writing SQL queries. These days, that beats hand-writing pandas code and the matching matplotlib charts. That’s why I recommend exploring the data with DuckDB, for example in a Jupyter notebook.

An example of using DuckDB to query the dataset on Hugging Face directly:

```
SELECT watermark,
       count(*)                          AS sightings,
       count(DISTINCT collected_from_ip) AS servers,
       min(collected_on)                 AS first_seen,
       max(collected_on)                 AS last_seen
FROM 'hf://datasets/fox-srt/cobaltstrike-beacon-corpus/data/beacons.parquet'
GROUP BY watermark
ORDER BY sightings DESC
LIMIT 20;
```

[![](https://blog.fox-it.com/wp-content/uploads/2026/10/duckdb_watermark_results.png?w=800)](https://blog.fox-it.com/wp-content/uploads/2026/10/duckdb_watermark_results.png)

Take a look at our Jupyter notebook in the Hugging Face repository as a starting point. It contains every query and chart from the sections below, so you can rerun them or adapt them to your own research questions.

# A first look at the data

Here are a few quick results to show what the corpus can answer. They’re a starting point, not a full analysis. As with our 2022 post, we invite researchers to explore the data; see also “Research ideas” below.

## Old versions never die

[![](https://blog.fox-it.com/wp-content/uploads/2026/10/cobaltstrike_versions_by_month.png?w=800)](https://blog.fox-it.com/wp-content/uploads/2026/10/cobaltstrike_versions_by_month.png)

Each Cobalt Strike release takes over from the last, but old versions linger. Cobalt Strike 4.0 dominated most of 2020, 4.1–4.2 drove the early 2021 peak of about 3,000 beacons a month, 4.3–4.4 led from mid-2021 through 2022, and 4.5–4.8 took over in 2023. Since 2024, 4.9 and 4.5–4.8 have shared the lead, while 4.10+ remains a small share. Volume has since dropped to around 200 beacons a month, partly because fewer servers stage their beacon, which brings us to the next graph.

## No beacon for you

[![](https://blog.fox-it.com/wp-content/uploads/2026/10/cobaltstrike_staging_stats.png?w=800)](https://blog.fox-it.com/wp-content/uploads/2026/10/cobaltstrike_staging_stats.png)

Our collection relies on beacon staging, meaning a Team Server can serve its beacon as a downloadable payload to anyone who requests the right URI or DNS record. Operators can turn this off (the `[host_stage](https://hstechdocs.helpsystems.com/manuals/cobaltstrike/current/userguide/content/topics/listener-infrastructure_payload-staging.htm)` option in the Malleable C2 profile), and disabling it is common OPSEC advice. To measure how much this affects our beacon collection, we counted two numbers per month:

1. The unique Team Servers (ip:port) confirmed by our high-confidence HTTP fingerprint
2. The unique Team Servers (ip:port) that handed out a beacon over HTTP(S)

These are monthly totals, not ...