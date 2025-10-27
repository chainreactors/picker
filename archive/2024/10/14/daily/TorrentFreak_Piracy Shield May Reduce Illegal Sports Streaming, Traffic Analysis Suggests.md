---
title: Piracy Shield May Reduce Illegal Sports Streaming, Traffic Analysis Suggests
url: https://torrentfreak.com/piracy-shield-may-reduce-illegal-sports-streaming-traffic-analysis-suggests-241013/
source: TorrentFreak
date: 2024-10-14
fetch_date: 2025-10-06T18:48:51.621152
---

# Piracy Shield May Reduce Illegal Sports Streaming, Traffic Analysis Suggests

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

# Piracy Shield May Reduce Illegal Sports Streaming, Traffic Analysis Suggests

October 13, 2024 by
[Andy Maxwell](https://torrentfreak.com/author/andy/)

[Home](https://torrentfreak.com "Go to TorrentFreak.") > [Piracy Research](https://torrentfreak.com/category/research/ "Go to the Piracy Research category archives.") >

Italy's Piracy Shield blocking system was launched early 2024 promising to end the flood of pirate IPTV providers saturating the local market. Site-blocking proponents' claims of huge success were met by reports of significant failures. In the absence of any useful, credible data being made available by those behind Piracy Shield, researchers in Italy are trying to answer the big question: Is Piracy Shield effective at reducing access to pirated live sports streams?

[![piracy-shield-3](https://torrentfreak.com/images/piracy-shield-3.png)](https://torrentfreak.com/images/piracy-shield-3.png)Piracy Shield’s first birthday is still several months away so the appearance of a study into its effectiveness came as a surprise but not an unwelcome one.

Commentary by Italian telecoms regulator AGCOM, mirrored by top-tier football league Serie A and streaming service DAZN, hasn’t been at all useful for those seeking answers to the two most important questions:

1) How effective is Piracy Shield at denying access to pirate live sports streams?
2) What is the effect (if any) on new subscriber uptake and customer churn?

Thus far, success has been expressed via the number of domains and IP addresses added to the system for blocking. With roughly 25,000 domains and IP addresses currently blocked, and huge numbers added week after week, the need for more blocking is just as easily framed as a measure of failure.

## How Effective is Piracy Shield?

A study to measure how effective Piracy Shield is at blocking was recently conducted at the University of Padua. Graduate student Maffei Davide and Prof. Alessandro Galeazzi, with support from Dr. Giacomo Quadrio and Dr. Enrico Bassetti of the [SPRITZ](https://spritz.math.unipd.it/) security group, opted for an analysis of [network traffic](https://www.datacenterplatform.com/data-centers/universita-degli-studi-di-padova/universita-degli-studi-di-padova-italy/vsix-dc/) via the university’s [VSIX[g] node](https://www.vs-ix.org/).

“The project was born from the need to collect information on the functioning of Piracy Shield, as well as on the evaluation of its effectiveness. Through the analysis of network flows, we want to be able to distinguish video flows from other types of traffic and identify the differences between ordinary and pirated traffic,” David Maffei explains.

Using traffic analysis, the researchers examined various characteristics such as communication protocols (TCP, UDP), network ports commonly associated with streaming services, stream duration and size, and packet flags signaling successful transmission and reception.

Through the analysis of these and other characteristics, the researchers aimed to isolate video streaming traffic from other network activity. The next task was to isolate likely legal streaming traffic, from traffic likely to be illegal.

## Identifying Legal Streaming Traffic

To identify streaming traffic likely to be legal, the researchers needed to establish which companies hold the broadcast rights for the sporting events being analyzed. After identifying Sky and DAZN, the next step was to discover their Content Delivery Network (CDN) partners; in this case, both Sky and DAZN mainly use Akamai.

The next stage required the researchers to determine the IP addresses generating network traffic coinciding with football match broadcasts. The paper provides additional detail but in broad terms, the researchers considered i) average traffic rate (between 1 and 20Mbps), ii) consistent traffic patterns (to exclude addresses with high traffic peaks unrelated to streaming), and iii) significant difference in traffic during match time, when compared with the two-hour slots before and after a game.

After identifying the Content Delivery Network (in this case Akamai) used for legal broadcasts and finding the corresponding Autonomous System Numbers (ASN), the researchers were able to reconstruct the legal streaming traffic to generate a legal traffic baseline, as illustrated in the image below.

*Legal traffic baseline (May 2024)*[![legal-traffic-baseline](https://torrentfreak.com/images/legal-traffic-baseline.png)](https://torrentfreak.com/images/legal-traffic-baseline.png)

This baseline allowed the researchers to compare legal traffic with suspected illegal traffic.

## Identifying Suspected Illegal Streaming Traffic

The researchers began by identifying the most-used network ports used during the match period; overwhelmingly ports 443 (https) and 80 (http) in the top 50.

The data generated by these high-traffic ports was analyzed to detect network flows with similar characteristics to those associated with video streaming, following the pattern of legal traffic established in the baseline. To facilitate identification, traffic graphs were generated for each port, with port 41122 producing a very similar profile to the legal baseline.

[![port-baseline-comparison](https://torrentfreak.com/images/port-baseline-comparison.png)](https://torrentfreak.com/images/port-baseline-comparison.png)

Among many checks carried out to ensure that traffic was actually illegal, the researchers compared this traffic with traffic generated by ASNs linked to websites previously blocked for copyright infringement. Again, the finer details are available in the full report.

## Piracy Shield: Effective or Not?

When referencing Piracy Shield, the researchers appear to take the whole system into consideration, from the detection and identification of pirate streams by affected rightsholders, to the eventual blocking of domains and IP addresses by ISPs.

Key metrics the researchers wanted to consider but were forced to leave out, include detection rates, false positive rates, response times, and efficient management of IP addresses and availability. The researchers cite limited data availability and a general lack of transparency throughout the system as obstacles to more comprehensive research.

To evaluate the effectiveness of Piracy Shield, the researchers compared legal traffic with suspected illegal traffic. The image below shows data reconstructed from traffic generated by ASNs associated with IP addresses blocked by Piracy Shield (orange) and separately identified legal traffic (blue).

[![piracy-shield-network traffic](https://torrentfreak.com/images/piracy-shield-network-trafficpng.png)](https://torrentfreak.com/images/piracy-shield-network-trafficpng.png)

“The graph highlights that illegal traffic presents significant volume peaks at football match times, indicated by the vertical dotted lines. These peaks coincide temporally with the start an end of sports events, suggesting a strong correlation between presumed pirate traffic and the unauthorized transmission of sports content,” the report notes.

The paper notes difficulties in identifying specific patterns related to illegal video streaming (orange), although a clear pattern typical...