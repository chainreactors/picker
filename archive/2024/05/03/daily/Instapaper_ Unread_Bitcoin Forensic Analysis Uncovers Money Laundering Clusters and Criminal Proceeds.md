---
title: Bitcoin Forensic Analysis Uncovers Money Laundering Clusters and Criminal Proceeds
url: https://thehackernews.com/2024/05/bitcoin-forensic-analysis-uncovers.html
source: Instapaper: Unread
date: 2024-05-03
fetch_date: 2025-10-06T17:17:15.048310
---

# Bitcoin Forensic Analysis Uncovers Money Laundering Clusters and Criminal Proceeds

#1 Trusted Cybersecurity News Platform

Followed by 5.20+ million[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.facebook.com/thehackernews)

[![The Hacker News Logo](data:image/png;base64...)](/)

**

**

[** Subscribe – Get Latest News](#email-outer)

* [** Home](/)
* [** Newsletter](#email-outer)
* [** Webinars](/p/upcoming-hacker-news-webinars.html)

* [Home](/)
* [Data Breaches](/search/label/data%20breach)
* [Cyber Attacks](/search/label/Cyber%20Attack)
* [Vulnerabilities](/search/label/Vulnerability)
* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Expert Insights](https://thehackernews.com/expert-insights/)
* [Contact](/p/submit-news.html)

**

**

**

Resources

* [Webinars](/p/upcoming-hacker-news-webinars.html)
* [Free eBooks](https://thehackernews.tradepub.com)

About Site

* [About THN](/p/about-us.html)
* [Jobs](/p/careers-technical-writer-designer-and.html)
* [Advertise with us](/p/advertising-with-hacker-news.html)

Contact/Tip Us

[**

Reach out to get featured—contact us to send your exclusive story idea, research, hacks, or ask us a question or leave a comment/feedback!](/p/submit-news.html)

Follow Us On Social Media

[**](https://www.facebook.com/thehackernews)
[**](https://twitter.com/thehackersnews)
[**](https://www.linkedin.com/company/thehackernews/)
[**](https://www.youtube.com/c/thehackernews?sub_confirmation=1)
[**](https://www.instagram.com/thehackernews/)

[** RSS Feeds](https://feeds.feedburner.com/TheHackersNews)
[** Email Alerts](#email-outer)

[![Salesforce Security Handbook](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjWa8tsMNqlevi1HGF1ALQRGIq7hROPFAbHd3R1RTEOe73T8_Q2xW_-91t2jSGjU5peiPb8QYblGp4igNW-u2Qmlxbp2BKzTVMSvyXDZJmC-BYpiiJHrcnG5drmSP97iZ9PVIf1DeEr7U-7vWpe4HXwfMjt8FGNgq5mOycOJluYr9wF7YOKrQY9MfArwgjt/s728-e100/ai-agent-security-d.png)](https://thehackernews.uk/ai-agent-security-d)

# [Bitcoin Forensic Analysis Uncovers Money Laundering Clusters and Criminal Proceeds](https://thehackernews.com/2024/05/bitcoin-forensic-analysis-uncovers.html)

**May 01, 2024**Ravie LakshmananFinancial Crime / Forensic Analysis

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgWxADP1ARMwS8u094E6BhMuF0vfvJd_rCbLY9gLSSFCbJ7_CpY3f8AajraT87gINijNm-hDFZj2QmsoGRJz26OfmnR40y3O-_bddmNLQIh45SmYcR6jlt4rzqaC9Y3WjWMUOgG1zIMHrChvpNx0fqY_PnhvBveqdj_78NRzwRolWl6WZhrNa8eOFuXwZkB/s790-rw-e365/blockchain.png)

A forensic analysis of a graph dataset containing transactions on the Bitcoin blockchain has revealed clusters associated with illicit activity and money laundering, including detecting criminal proceeds sent to a crypto exchange and previously unknown wallets belonging to a Russian darknet market.

The [findings](https://www.elliptic.co/blog/our-new-research-enhancing-blockchain-analytics-through-ai) come from Elliptic in collaboration with researchers from the MIT-IBM Watson AI Lab.

The 26 GB dataset, dubbed **[Elliptic2](https://www.kaggle.com/datasets/ellipticco/elliptic2-data-set)**, is a "large graph dataset containing 122K labeled subgraphs of Bitcoin clusters within a background graph consisting of 49M node clusters and 196M edge transactions," the co-authors [said](https://arxiv.org/abs/2404.19109) in a paper shared with The Hacker News.

Elliptic2 builds on the [Elliptic Data Set](https://www.kaggle.com/datasets/ellipticco/elliptic-data-set) (aka Elliptic1), a transaction graph that was made public in July 2019 with the goal of [combating financial crime](https://arxiv.org/abs/1908.02591) using graph convolutional neural networks ([GCNs](https://distill.pub/2021/gnn-intro/)).

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

The idea, in a nutshell, is to uncover unlawful activity and money laundering patterns by taking advantage of [blockchain's pseudonymity](https://www.certik.com/resources/blog/what-is-pseudonymity-and-anonymity) and combining it with knowledge about the presence of licit (e.g., exchange, wallet provider, miner, etc.) and illicit services (e.g., darknet market, malware, terrorist organizations, Ponzi scheme, etc.) on the network.

"Using machine learning at the subgraph level – i.e., the groups of transactions that make up instances of money laundering – can be effective at predicting whether crypto transactions constitute proceeds of crime," Tom Robinson, chief scientist and co-founder of Elliptic, told The Hacker News.

"This is different to conventional crypto anti-money laundering ([AML](https://en.wikipedia.org/wiki/Anti%E2%80%93money_laundering)) solutions, which rely on tracing funds from known illicit wallets, or pattern-matching with known money laundering practices."

The study, which experimented with three different subgraph classification methods on Elliptic2, such as [GNN-Seg](https://towardsdatascience.com/graph-convolutional-networks-introduction-to-gnns-24b3f60d6c95), [Sub2Vec](https://arxiv.org/abs/1702.06921), and [GLASS](https://openreview.net/forum?id=XLxhEjKNbXj), identified subgraphs that represented crypto exchange accounts potentially engaging in illegitimate activity.

On top of that, it has made it possible to trace back the source of funds associated with suspicious subgraphs to various entities, including a cryptocurrency mixer, a Panama-based Ponzi scheme, and an invite-only Russian dark web forum.

Robinson said just considering the "shape" – the local structures within a complex network – of the money laundering subgraphs proved to be an already effective way to flag criminal activity.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

Further examination of the subgraphs predicted using the trained GLASS model has also identified known cryptocurrency laundering patterns, such as the presence of peeling chains and nested services.

"A peeling chain is where a small amount of cryptocurrency is 'peeled' to a destination address, while the remainder is sent to another address under the user's control," Robinson explained. "This happens repeatedly to form a peeling chain. The pattern can have legitimate financial privacy purposes, but it can also be indicative of money laundering, especially where the 'peeled' cryptocurrency is repeatedly sent to an exchange service."

"This is a known crypto laundering technique and has an analogy in 'smurfing' within traditional finance – so the fact that our machine learning mode independently identified it is encouraging."

As for the next steps, the research is expected to focus on increasing the accuracy and precision of these techniques, as well as extending the work to further blockchains, Robinson added.

Found this article interesting? Follow us on [Google News](https://news.google.com/publications/CAAqLQgKIidDQklTRndnTWFoTUtFWFJvWldoaFkydGxjbTVsZDNNdVkyOXRLQUFQAQ), [Twitter](https://twitter.com/thehackersnews) and [LinkedIn](https://www.linkedin.com/company/thehackernews/) to read more exclusive content we post.

SHARE
[**](#link_share)
[**](#link_share)
[**](#link_share)
**

[**Tweet](#link_share)

[**Share](#link_share)

[**Share](#link_share)

**Share

**
[**Share on Facebook](#link_share)
[**Share on Twitter](#link_share)
[**Share on Linkedin](#link_share)
[**Share on Reddit](#link_share)
[**Share on Hacker News](#link_share)
[**Share on Email](#link_share)
[**Share on WhatsApp](#link_share)
[![Facebook Messenger](data:image/png;base64...)Share on Facebook Messenger](#link_share)
[**Share on Telegram](#link_share)

SHARE **

[Bitcoin](https://thehackernews.com/search/label/Bitcoin)[Blockchain](https://thehackernews.com/search/label/Blockchain)[Crypto Exchange](https://thehackernews.com/search/label/Crypto%20Exchange)[darknet](https://thehackernews.com/search/label/darknet)[Financial Crime](https://thehackernews.com/search/label/Financial%20Crime)[Forensic Analysis](https://thehacker...