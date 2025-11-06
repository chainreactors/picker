---
title: [StalkPhish.io] Advanced Phishing Detection with one API
url: https://stalkphish.com/2025/11/05/stalkphish-io-advanced-phishing-detection-with-one-api/
source: Over Security - Cybersecurity news aggregator
date: 2025-11-05
fetch_date: 2025-11-06T03:16:01.522875
---

# [StalkPhish.io] Advanced Phishing Detection with one API

[![StalkPhish – phishing, scam and brand impersonation detection](https://stalkphish.com/wp-content/uploads/2021/03/stalkphish-incl-200x60-txt-white.png)](https://stalkphish.com/)

[StalkPhish – phishing, scam and brand impersonation detection](https://stalkphish.com/)

StalkPhish – We provide B2B tools, data and knowledge for a better phishing and brand impersonation detection.

* [Home](https://stalkphish.com/)
* [Products](https://stalkphish.com/portfolio/products/)
* [Projects](https://stalkphish.com/products/)
  + [PhishingKit-Yara-Rules](https://stalkphish.com/products/phishingkit-yara-rules/)
  + [PhishingKitHunter](https://stalkphish.com/products/phishingkithunter/)
  + [StalkPhish OSS](https://stalkphish.com/products/stalkphish/)
* [Blog](https://stalkphish.com/blog-feed/)
* [Contact](https://stalkphish.com/contact/)
* [About](https://stalkphish.com/about-2/)
* [Press & Media](https://stalkphish.com/press-media/)

* [Twitter](https://twitter.com/Stalkphish_io)
* [LinkedIn](https://www.linkedin.com/company/stalkphish)
* [GitHub](https://github.com/t4d/StalkPhish)
* [Youtube](https://www.youtube.com/channel/UC5hb1CaRdmbSWpN0wTz6SFw)

Show search form
Menu- Select Page -HomeProductsProjects - PhishingKit-Yara-Rules - PhishingKitHunter - StalkPhish OSSBlogContactAboutPress & Media

Search for:

 Hide search form

![](https://stalkphish.com/wp-content/uploads/2025/11/stalkphish-api1.4-homedoc.png?w=1084)

# [StalkPhish.io] Advanced Phishing Detection with one API

![StalkPhish's avatar](https://2.gravatar.com/avatar/2ecf84df3d23b66e9e3dc59759be2600c71c9cd576b072248f211024b06278a3?s=35&d=identicon&r=G) By [StalkPhish](https://stalkphish.com/author/stalkphish/)

in [Non classé](https://stalkphish.com/category/non-classe/)

on [11/05/202511/05/2025](https://stalkphish.com/2025/11/05/stalkphish-io-advanced-phishing-detection-with-one-api/)

[No comments](https://stalkphish.com/2025/11/05/stalkphish-io-advanced-phishing-detection-with-one-api/#respond)

# Introducing the Enhanced StalkPhish.io API: Advanced Phishing Detection at Your Fingertips

At StalkPhish, we’ve been committed to staying ahead of phishing threats and providing our users with the most comprehensive tools for detecting and investigating brand impersonation, fraud campaigns, and phishing attacks. Today, we’re excited to share details about our enhanced API that brings powerful search capabilities and real-time threat intelligence directly to your security workflows.

## Why We Built This API

Fighting phishing is not an easy task. You need to detect campaigns before you can start dismantling them. It’s a race against time—the faster you detect a campaign, the faster you can take it down. Our daily operations involve detecting, enriching, and sorting tens of thousands of phishing URLs, and we’ve designed our API to put this wealth of intelligence at your disposal programmatically.

What sets StalkPhish apart is our original approach: we don’t just detect phishing URLs—we gather intelligence on the threat actors behind campaigns and the developers of phishing kits. By extracting and analyzing data embedded within phishing kits themselves, we help you understand not just the “what” but the “who” behind phishing operations. This threat actor-centric intelligence is crucial for tracking campaigns over time, identifying infrastructure reuse, and anticipating future attacks.

## A Tiered Approach to Threat Intelligence

Understanding that different organizations have different needs and budgets, we’ve structured our API access across three subscription tiers:

### Free Tier

Perfect for researchers and small-scale investigations, the Free tier provides:

* 10 API calls per day
* Access to the last 4 hours of phishing data
* Up to 30 results per query
* Basic URL and IP address search capabilities

### Standard Tier

For security teams needing regular access to threat intelligence:

* 1000 API calls per day
* 30-day historical data access
* Up to 100 results per query
* Additional search capabilities including page title searches and extracted email addresses
* Google Safe Browsing status and phishing scores
* SSL certificate information

### Pro Tier

Our most comprehensive offering for enterprise security operations:

* 10,000 API calls per day
* 180-day historical data access
* Up to 200 results per query
* Full feature access including brand search, favicon hash matching, and phishing kit analysis
* Telegram bot/channel extraction data
* Phishing kit family classification
* ZIP file hash searches for tracking kit reuse

## Powerful Search Capabilities

One of the most powerful features of our enhanced API is the advanced search system with boolean operator support. Security analysts can now construct complex queries to pinpoint specific threats:

```
# Search for PayPal phishing with login pages
curl -H "Authorization: Token YOUR_TOKEN" \
"https://api.stalkphish.io/api/v1/search/url/paypal%20AND%20login"

# Find Microsoft or Apple impersonation attempts
curl -H "Authorization: Token YOUR_TOKEN" \
"https://api.stalkphish.io/api/v1/search/url/microsoft%20OR%20apple"

# Exclude legitimate sites from results
curl -H "Authorization: Token YOUR_TOKEN" \
"https://api.stalkphish.io/api/v1/search/url/banking%20NOT%20legitimate"
```

The API supports combining up to 5 boolean operators with a maximum of 10 search terms, allowing for precise threat hunting and campaign tracking.

## Temporal Filters for Time-Based Analysis

Phishing campaigns often follow patterns and trends. Our API includes flexible temporal filtering to help you track campaigns over time:

```
# Search for recent PayPal phishing (last 7 days)
response = requests.get(
    'https://api.stalkphish.io/api/v1/search/url/paypal',
    headers={'Authorization': 'Token YOUR_TOKEN'},
    params={'last_days': 7}
)

# Custom date range search
response = requests.get(
    'https://api.stalkphish.io/api/v1/search/url/microsoft',
    headers={'Authorization': 'Token YOUR_TOKEN'},
    params={
        'from_date': '2024-07-01',
        'to_date': '2024-07-31'
    }
)
```

## Beyond URLs: Multi-Vector Threat Hunting

As we’ve shared in previous blog posts, StalkPhish.io’s probes retrieve relevant information directly from phishing kits themselves. The API exposes this rich data through multiple search vectors:

**IP Address Search**: Track infrastructure reuse across campaigns by searching for specific IPv4 addresses hosting phishing sites.

**Brand Search (Pro)**: Monitor phishing attempts targeting specific brands or companies you’re protecting.

**Favicon Hash Search (Pro)**: Identify related phishing sites using MMH3 favicon hashes—particularly useful for tracking campaigns that reuse infrastructure or kits.

**Email Extraction Search (Pro)**: Find phishing pages containing specific email addresses, useful for tracking scammer operations.

**ZIP File Hash Search (Pro)**: As we’ve documented in our [PhishingKit-Yara-Rules project](https://stalkphish.com/products/phishingkit-yara-rules/), tracking phishing kit reuse is crucial. Search by MD5, SHA1, or SHA256 hashes to identify known kits across different domains.

## Phishing Kit Intelligence

Since years, [StalkPhish.io](https://stalkphish.io) has included a system for classifying phishing kits. This enhancement allows us to effectively categorize phishing kits collected through our infrastructure. The API now exposes this classification data in the Pro tier response:

```
{
  "zipfilename": "phishing_kit.zip",
  "zipfilehash": "abc123def456",
  "phishingkit_family": "PK_Paypal_RD304",
  "page_hash": "sha256hash",
  "extracted_telegram": [{
    "botID": "1548908025:fc51cd8e6218a1a38da47ed00230f057681",
    "channelID": "987654321"
  }],
  "targeted_brand": "PayPal"
}
```

This data is invaluable for understanding campaign infrastructure and tracking threat actor operations over time. As we’ve blogged about previously, many phishing kits use Telegram for data exfiltration, and our API surfac...