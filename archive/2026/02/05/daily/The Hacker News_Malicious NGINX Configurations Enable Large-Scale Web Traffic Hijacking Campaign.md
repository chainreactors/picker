---
title: Malicious NGINX Configurations Enable Large-Scale Web Traffic Hijacking Campaign
url: https://thehackernews.com/2026/02/hackers-exploit-react2shell-to-hijack.html
source: The Hacker News
date: 2026-02-05
fetch_date: 2026-02-06T04:10:23.548543
---

# Malicious NGINX Configurations Enable Large-Scale Web Traffic Hijacking Campaign

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

[![Security Service Edge](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEg5Ij_-TeqFMEsRFzgRRFzSRlVK6oHCncN_eJ2fkOdsA_1tN9HQbAlEEife2Z2JUt1lPv4st5n9KZP84jGEYY9Up6BQ7QE-N5rs6OhzL5thxGzVxnMx3JH9cGRLi9S5Kl-iV5PgjBeTdkBLnv_inF8UUAo88iqdmgJuPIc_6qiPyUMXwFyZWbZvkZkcRXSw/s728-e100/gartner-d.jpg)](https://thehackernews.uk/sse-awards-insight-d)

# [Malicious NGINX Configurations Enable Large-Scale Web Traffic Hijacking Campaign](https://thehackernews.com/2026/02/hackers-exploit-react2shell-to-hijack.html)

**Ravie Lakshmanan**Feb 05, 2026Web Security / Vulnerability

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi1rduNeKuuHUpRierQx1jig2SMH0dhcoENNLniZavZ25JgD68fkxRwp3s4H42sJrL7OXa4r0QublDt9VQ2mjh1uIBuQsvPi4iHtrY2JHw4res_AZQc3pf-AQ610FvG6o_TcXxDliH5JlNJbaVN0AXj3De60H669V9fTQIyqNRNHHMgSfwbjZe8xt3cPhIy/s1700-e365/nginx-hacked.jpg)

Cybersecurity researchers have disclosed details of an active web traffic hijacking campaign that has targeted NGINX installations and management panels like Baota (BT) in an attempt to route it through the attacker's infrastructure.

Datadog Security Labs [said](https://securitylabs.datadoghq.com/articles/web-traffic-hijacking-nginx-configuration-malicious/) it observed threat actors associated with the recent [React2Shell](https://thehackernews.com/2025/12/critical-react2shell-flaw-added-to-cisa.html) ([CVE-2025-55182](https://thehackernews.com/2025/12/react2shell-vulnerability-actively.html), CVSS score: 10.0) exploitation using malicious NGINX configurations to pull off the attack.

"The malicious configuration intercepts legitimate web traffic between users and websites and routes it through attacker-controlled backend servers," security researcher Ryan Simon said. "The campaign targets Asian TLDs (.in, .id, .pe, .bd, .th), Chinese hosting infrastructure (Baota Panel), and government and educational TLDs (.edu, .gov)."

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/sse-customer-awards-d)

The activity involves the use of shell scripts to inject malicious configurations into NGINX, an open-source reverse proxy and load balancer for web traffic management. These "location" configurations are designed to capture incoming requests on certain predefined URL paths and redirect them to domains under the attackers' control via the "[proxy\_pass](https://docs.nginx.com/nginx/admin-guide/web-server/reverse-proxy/)" directive.

[![](data:image/png;base64...)](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEi0tGUXkPOGnWYmYS4DLtCbL81qH7zF_OVje4EF7W3PJ61JUny87zGlu2Tx8ChUERj74-CaB63fvjOSq2cZUbz60DOFDulVdm-0buUPK7uznAQCVgwWdpxl61u8d9E93_DRzv5ZTZ1dK7_aybyccD7WAbAqfW7yXuljr9Anc3qTv7kfNhTcn8_L_EokD3_Q/s1700-e365/diagram.png)

The scripts are part of a multi-stage toolkit that facilitates persistence and the creation of malicious configuration files incorporating the malicious directives to redirect web traffic. The components of the toolkit are listed below -

* **zx.sh**, which acts as the orchestrator to execute subsequent stages through legitimate utilities like curl or wget. In the event that the two programs are blocked, it creates a raw TCP connection to send an HTTP request
* **bt.sh**, which targets the Baota (BT) Management Panel environment to overwrite NGINX configuration files
* **4zdh.sh**, which enumerates common Nginx configuration locations and takes steps to minimize errors when creating the new configuration
* **zdh.sh**, which adopts a narrower targeting approach by focusing mainly on Linux or containerized NGINX configurations and targeting top-level domains (TLDs) such as .in and .id
* **ok.sh**, which is responsible for generating a report detailing all active NGINX traffic hijacking rules

"The toolkit contains target discovery and several scripts designed for persistence and the creation of malicious configuration files containing directives intended to redirect web traffic.

The disclosure comes as GreyNoise said two IP addresses – 193.142.147[.]209 and 87.121.84[.]24 – account for 56% of all observed exploitation attempts two months after React2Shell was publicly disclosed. A total of 1,083 unique source IP addresses have been involved in React2Shell exploitation between January 26 and February 2, 2026.

[![Cybersecurity](data:image/png;base64...)](https://thehackernews.uk/ztw-hands-on-d)

"The dominant sources deploy distinct post-exploitation payloads: one retrieves cryptomining binaries from staging servers, while the other opens reverse shells directly to the scanner IP," the threat intelligence firm [said](https://www.greynoise.io/blog/react2shell-exploitation-consolidates). "This approach suggests interest in interactive access rather than automated resource extraction."

It also follows the discovery of a coordinated reconnaissance campaign targeting Citrix ADC Gateway and Netscaler Gateway infrastructure using tens of thousands of residential proxies and a single Microsoft Azure IP address ("52.139.3[.]76") to discover login panels.

"The campaign ran two distinct modes: a massive distributed login panel discovery operation using residential proxy rotation, and a concentrated AWS-hosted version disclosure sprint," GreyNoise [noted](https://www.labs.greynoise.io/grimoire/2026-02-02-citrix-recon-residential-proxies/index.html). "They had complementary objectives of both finding login panels, and enumerating versions, which suggests coordinated reconnaissance."

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

[Cryptomining](https://thehackernews.com/search/label/Crypt...