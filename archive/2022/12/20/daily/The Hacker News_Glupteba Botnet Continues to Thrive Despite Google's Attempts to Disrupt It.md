---
title: Glupteba Botnet Continues to Thrive Despite Google's Attempts to Disrupt It
url: https://thehackernews.com/2022/12/glupteba-botnet-continues-to-thrive.html
source: The Hacker News
date: 2022-12-20
fetch_date: 2025-10-04T02:01:20.779532
---

# Glupteba Botnet Continues to Thrive Despite Google's Attempts to Disrupt It

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

# [Glupteba Botnet Continues to Thrive Despite Google's Attempts to Disrupt It](https://thehackernews.com/2022/12/glupteba-botnet-continues-to-thrive.html)

**Dec 19, 2022**Ravie LakshmananBlockchain / Botnet

[![Glupteba Botnet](data:image/png;base64... "Glupteba Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEiNnQLSvhchGkVsJm3od8dE-N5eOaFUbDjEhwXrx8v9U9YQJuM0DAaftV2Nfr13DgSB6vs5o2SG67D1uKeoWzs2Y7kGzlzxDlxcunPMPax0Abl5OnlrvbHIcr1lDgC7zrXCoqUaQwdlRBYTDvdDi7HdQ7-6XrRgpG4mWhNSHAmQIQuMCsUFf_OvZRjR/s790-rw-e365/blockchain-botnet.png)

The operators of the Glupteba botnet resurfaced in June 2022 as part of a renewed and "upscaled" campaign, months after Google disrupted the malicious activity.

The ongoing attack is suggestive of the malware's resilience in the face of takedowns, cybersecurity company Nozomi Networks said in a write-up. "In addition, there was a tenfold increase in TOR hidden services being used as C2 servers since the 2021 campaign," it [noted](https://www.nozominetworks.com/blog/tracking-malicious-glupteba-activity-through-the-blockchain/).

The malware, which is distributed through fraudulent ads or software cracks, is also equipped to retrieve additional payloads that enable it to steal credentials, mine cryptocurrencies, and expand its reach by exploiting vulnerabilities in IoT devices from [MikroTik](https://thehackernews.com/2022/03/over-200000-microtik-routers-worldwide.html) and [Netgear](https://thehackernews.com/2021/11/critical-root-rce-bug-affects-multiple.html).

It's also an instance of an unusual malware that leverages blockchain as a mechanism for command-and-control (C2) [since at least 2019](https://www.trendmicro.com/en_us/research/19/i/glupteba-campaign-hits-network-routers-and-updates-cc-servers-with-data-from-bitcoin-transactions.html), rendering its infrastructure resistant to takedown efforts as in the case of a traditional server.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Specifically, the botnet is designed to search the public Bitcoin blockchain for transactions related to wallet addresses owned by the threat actor so as to fetch the encrypted C2 server address.

"This is made possible by the [OP\_RETURN](https://en.bitcoin.it/wiki/OP_RETURN) opcode that enables storage of up to 80 bytes of arbitrary data within the signature script," the industrial and IoT security firm explained, adding the mechanism also makes Glupteba hard to dismantle as "there is no way to erase nor censor a validated Bitcoin transaction."

The method also makes it convenient to replace a C2 server should it be taken down, as all that is needed for the operators is to publish a new transaction from the actor-controlled Bitcoin wallet address with the encoded updated server.

[![Glupteba Botnet](data:image/png;base64... "Glupteba Botnet")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEjgDFi686_kmVCrYrfcVxvKcKanbV1Io6duKPJQI7HxYvmvFIydRV6e1YWJlcNFoaKa91yyuZ9D2Wy3z3XJrMiIzoWQN4IzaC0fWSAcUWPdxZcPXgD6uN8U7k8WwJ1CT6XghdR9iIGC1m0ddTPzQBZivvOf-59_QL8p04BC9p6NSZ8JsrJc8zHdm9dY/s790-rw-e365/malware-code.png)

In December 2021, Google [managed](https://thehackernews.com/2021/12/google-disrupts-blockchain-based.html) to cause a significant dent to its operations, alongside filing a lawsuit against two Russian nationals who oversaw the botnet. Last month, a U.S. court [ruled in favor](https://thehackernews.com/2022/11/google-wins-lawsuit-against-russians.html) of the tech giant.

"While Glupteba operators have resumed activity on some non-Google platforms and IoT devices, shining a legal spotlight on the group makes it less appealing for other criminal operations to work with them," the internet behemoth [pointed out](https://blog.google/outreach-initiatives/public-policy/a-ruling-in-our-legal-case-against-the-glupteba-botnet/) in November.

Nozomi Networks, which examined over 1,500 Glupteba samples uploaded to VirusTotal, said it was able to extract 15 wallet addresses that were put to use by the threat actors dating all the way back to June 19, 2019.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

The ongoing campaign that commenced in June 2022 is also perhaps the biggest wave in the past few years, what with the number of rogue bitcoin addresses jumping to 17, up from four in 2021.

One of those addresses, which was [first active on June 1, 2022](https://www.blockchain.com/explorer/addresses/btc/1KfLXEveeDEi58wvuBBxuywUA1V66F5QXK), has transacted 11 times to date and is used in as many as 1,197 artifacts, making it the most widely used wallet address. The last transaction was recorded on November 8, 2022.

"Threat actors are increasingly leveraging blockchain technology to launch cyberattacks," the researchers said. "By taking advantage of the distributed and decentralized nature of blockchain, malicious actors can exploit its anonymity for a variety of attacks, ranging from malware propagation to ransomware distribution."

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

[botnet](https://thehackernews.com/search/label/botnet)[Glupteba](https://thehackernews.com/search/label/Glupteba)[Google](http...