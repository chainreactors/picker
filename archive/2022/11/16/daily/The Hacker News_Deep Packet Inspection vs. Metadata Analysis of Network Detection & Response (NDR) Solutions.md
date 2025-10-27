---
title: Deep Packet Inspection vs. Metadata Analysis of Network Detection & Response (NDR) Solutions
url: https://thehackernews.com/2022/11/deep-packet-inspection-vs-metadata.html
source: The Hacker News
date: 2022-11-16
fetch_date: 2025-10-03T22:56:04.247953
---

# Deep Packet Inspection vs. Metadata Analysis of Network Detection & Response (NDR) Solutions

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

# [Deep Packet Inspection vs. Metadata Analysis of Network Detection & Response (NDR) Solutions](https://thehackernews.com/2022/11/deep-packet-inspection-vs-metadata.html)

**Nov 15, 2022**The Hacker News

[![Network Detection and Response NDR Solutions](data:image/png;base64... "Network Detection and Response NDR Solutions")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEha56gW5ADX3bU8HRLHaiUoy__Z8c4j6mRLvJCgJrKdl-inqCN7-lmik5QsqEG5tZpOhQyC57V7vQFqNJEXD9jHKhCW8E5Ij516fKt1RPYL3bnzxX8Lp1We7CSC1QdurlPYuc9dVZsf7bEgIbiN2zm767Mytbenu0G4FHCwasV0qvjMW8ledvjKLNEo/s790-rw-e365/NDR.jpg)

Today, most Network Detection and Response (NDR) solutions rely on traffic mirroring and Deep Packet Inspection (DPI). Traffic mirroring is typically deployed on a single-core switch to provide a copy of the network traffic to a sensor that uses DPI to thoroughly analyze the payload. While this approach provides detailed analysis, it requires large amounts of processing power and is blind when it comes to encrypted network traffic. Metadata Analysis has been specifically developed to overcome these limitations. By utilizing metadata for analysis, network communications can be observed at any collection point and be enriched by the information providing insights about encrypted communication.

Network Detection and Response (NDR) solutions have become crucial to reliably monitor and protect network operations. However, as network traffic becomes encrypted and data volumes continue to increase, most traditional NDR solutions are reaching their limits. This begs the question: What detection technologies should organizations utilize to ensure the maximum security of their systems?

This article will shed light on the concept of Deep Packet Inspection (DPI) and Metadata Analysis. We will compare both detection technologies and examine how modern Network Detection and Response (NDR) solutions can effectively protect IT/OT networks from advanced cyber threats.

## **What is Deep Packet Inspection (DPI), and how does it work?**

DPI is a way of network traffic monitoring used to inspect network packets flowing across a specific connection point or switch. In DPI, the whole traffic is typically mirrored by a core switch to a DPI sensor. The DPI sensor then examines both the header and data section of the packet. If the data section is not encrypted, DPI data are rich in information and allow for robust analysis of the monitored connection points. Traditional NDR solutions rely on DPI-based technologies, which are quite popular to this day. However, in the face of rapidly expanding attack surfaces and evolving IT environments, the limitations of DPI have become increasingly prevalent.

## **Why Is DPI not enough to detect Advanced Cyberattacks?**

Organizations are increasingly using encryption to protect their network traffic and online interactions. Although encryption brings enormous benefits to online privacy and cybersecurity, it also provides a suitable opportunity for cybercriminals to hide in the dark when launching devastating cyberattacks. As DPI was not designed for the analysis of encrypted traffic, it has become blind to the inspection of encrypted packet payloads. This is a significant shortfall for DPI since most modern cyberattacks, such as APT, ransomware, and lateral movement, heavily utilise encryption in their attack routine to receive attack instructions from remote Command and Control Servers (C&C) scattered across cyberspace. In addition to absent encryption capabilities, DPI requires large amounts of processing power and time in order to thoroughly inspect the data section of each packet. Consequently, DPI cannot analyze all network packets in data-heavy networks, making it an unfeasible solution for high-bandwidth networks.

## **The New Approach: Metadata Analysis**

Metadata analysis has been developed to overcome the limitations of DPI. By utilizing metadata for network analysis, security teams can monitor all network communications passing through any physical, virtualized or cloud networks without inspecting the entire data section of each packet. Consequently, Metadata analysis is unaffected by encryption and can deal with ever-increasing network traffic. In order to provide security teams with real-time intelligence of all network traffic, Metadata analysis captures vast arrays of attributes about network communications, applications, and actors (e.g., user logins). For instance, for every session passing through the network, the source/destination IP address, session length, protocol used (TCP, UDP), and the type of services used are recorded. Metadata can capture many other key attributes, which effectively help detect and prevent advanced cyberattacks:

* Host and server IP address, port number, geo-location information
* DNS and DHCP information mapping devices to IP addresses
* Web page accesses, along with the URL and header information
* Users to systems mapping using DC log data
* Encrypted web pages – encryption type, cypher and hash, client/server FQDN
* Different objects hashes – such as JavaScript and images

## **How can Security Teams benefit from metadata-based NDR?**

Implementing a Network Detection and Response (NDR) solution based on Metadata analysis provides security teams with reliable insights on what happens inside their network – no matter whether the traffic is encrypted or not. Metadata analysis supplemented by system and application logs allows security teams to detect vulnerabilities and improve internal visibility into blind spots, such as shadow IT devices, which are considered a common entry point exploited by cybercriminals. This holistic visibility is not possible with DPI-based NDR solutions. In addition, lightweight metadata allows for efficient log data storage of historical records, facilitating forensics investigations. Data-heavy DPI analysis makes long-term storage of historical data practically infeasible or very expensive. Finally, the metadata approach allows security teams t...