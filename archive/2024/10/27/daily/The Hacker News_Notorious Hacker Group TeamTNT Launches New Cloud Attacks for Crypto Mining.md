---
title: Notorious Hacker Group TeamTNT Launches New Cloud Attacks for Crypto Mining
url: https://thehackernews.com/2024/10/notorious-hacker-group-teamtnt-launches.html
source: The Hacker News
date: 2024-10-27
fetch_date: 2025-10-06T18:52:41.338303
---

# Notorious Hacker Group TeamTNT Launches New Cloud Attacks for Crypto Mining

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

# [Notorious Hacker Group TeamTNT Launches New Cloud Attacks for Crypto Mining](https://thehackernews.com/2024/10/notorious-hacker-group-teamtnt-launches.html)

**Oct 26, 2024**Ravie LakshmananCloud Security / Cryptocurrency

[![Cloud Attacks for Crypto Mining](data:image/png;base64... "Cloud Attacks for Crypto Mining")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEitrezLabESR5-VGZ06cIjmOmAWM5mNKzHgZheuyRWaFj2b0h-Vf3_bOpTfzigRO8jnoB1pi7aSWvi-IBc6WO42g4VzjYeZ-gTaFKTLTSt83cold7gnkU-cTLp7_cl9dGS7zrAgSztSn2IDNt4HAX65E4ifTaC5cqMYUgz8E3N080keDN5iF1X_GmjZlg-K/s790-rw-e365/coker.png)

The infamous cryptojacking group known as [TeamTNT](https://thehackernews.com/2024/09/new-teamtnt-cryptojacking-campaign.html) appears to be readying for a new large-scale campaign targeting cloud-native environments for mining cryptocurrencies and renting out breached servers to third-parties.

"The group is currently targeting exposed Docker daemons to deploy Sliver malware, a cyber worm, and cryptominers, using compromised servers and Docker Hub as the infrastructure to spread their malware," Assaf Morag, director of threat intelligence at cloud security firm Aqua, [said](https://www.aquasec.com/blog/threat-alert-teamtnts-docker-gatling-gun-campaign/) in a report published Friday.

The attack activity is once again a testament to the threat actor's persistence and its ability to evolve its tactics and mounting multi-stage assaults with the goal of compromising Docker environments and enlisting them into a Docker Swarm.

[![DFIR Retainer Services](data:image/png;base64...)](https://thehackernews.uk/cloud-insight-d)

Besides using Docker Hub to host and distribute their malicious payloads, TeamTNT has been observed offering the victims' computational power to other parties for illicit cryptocurrency mining, thus diversifying its monetization strategy.

Rumblings of the attack campaign emerged earlier this month when Datadog [disclosed](https://thehackernews.com/2024/10/new-cryptojacking-attack-targets-docker.html) malicious attempts to corral infected Docker instances into a Docker Swarm, alluding it could be the work of TeamTNT, while also stopping short of making a formal attribution. But the full extent of the operation hasn't been clear, until now.

Morag told The Hacker News that Datadog "found the infrastructure in a very early stage" and that their discovery "forced the threat actor to change the campaign a bit."

[![Cloud Attacks for Crypto Mining](data:image/png;base64... "Cloud Attacks for Crypto Mining")](https://blogger.googleusercontent.com/img/b/R29vZ2xl/AVvXsEgZI7bb_YkDCrHxahMDIV_7Qe-8U4d0yetgxgXru9fgD2lbsSZqo2MSqa4nwUH0g_s2H3j5GbQhDd4a68d6sKPO-wCZJlHJgIcG5GWLwztwiQXo4xbqKsZBr4OkdzzybEPZTmPtuReZ6B3dEjaISivF58GRqVKSw4Ida6-Q3Gu1eO9RZgpUQdiHiJY0FM-L/s790-rw-e365/docker.png)

The attacks entail identifying unauthenticated and exposed Docker API endpoints using masscan and ZGrab and using them for cryptominer deployment and selling the compromised infrastructure to others on a mining rental platform called Mining Rig Rentals, effectively offloading the job of having to manage them themselves, a sign of the maturation of the illicit business model.

Specifically, this is carried out by means of an attack script that scans for Docker daemons on ports 2375, 2376, 4243, and 4244 across nearly 16.7 million IP addresses. It subsequently deploys a container running an Alpine Linux image with malicious commands.

The image, retrieved from a compromised Docker Hub account ("nmlm99") under their control, also executes an initial shell script named the Docker Gatling Gun ("TDGGinit.sh") to launch post-exploitation activities.

One notable change observed by Aqua is the shift away from the Tsunami backdoor to the open-source [Sliver](https://thehackernews.com/2023/01/threat-actors-turn-to-sliver-as-open.html) command-and-control (C2) framework for remotely commandeering the infected servers.

"Additionally, TeamTNT continues to use their established naming conventions, such as Chimaera, TDGG, and bioset (for C2 operations), which reinforces the idea that this is a classic TeamTNT campaign," Morag said.

[![CIS Build Kits](data:image/png;base64...)](https://thehackernews.uk/platform-shield-d)

"In this campaign TeamTNT is also using anondns (AnonDNS or Anonymous DNS is a concept or service designed to provide anonymity and privacy when resolving DNS queries), in order to point to their web server."

The findings come as Trend Micro shed light on a new campaign that involved a targeted brute-force attack against an unnamed customer to deliver the [Prometei](https://thehackernews.com/2023/03/new-version-of-prometei-botnet-infects.html) crypto mining botnet.

"Prometei spreads in the system by exploiting vulnerabilities in Remote Desktop Protocol (RDP) and Server Message Block (SMB)," the company [said](https://www.trendmicro.com/en_us/research/24/j/unmasking-prometei-a-deep-dive-into-our-mxdr-findings.html), highlighting the threat actor's efforts on setting up persistence, evading security tools, and gaining deeper access to an organization's network through credential dumping and lateral movement.

"The affected machines connect to a mining pool server which can be used to mine cryptocurrencies (Monero) on compromised machines without the victim's knowledge."

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
[**Share...